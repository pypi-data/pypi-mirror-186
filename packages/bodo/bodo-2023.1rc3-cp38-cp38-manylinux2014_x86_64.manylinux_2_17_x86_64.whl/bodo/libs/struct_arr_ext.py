"""Array implementation for structs of values.
Corresponds to Spark's StructType: https://spark.apache.org/docs/latest/sql-reference.html
Corresponds to Arrow's Struct arrays: https://arrow.apache.org/docs/format/Columnar.html

The values are stored in contiguous data arrays; one array per field. For example:
A:             ["AA", "B", "C"]
B:             [1, 2, 4]
"""
import operator
import llvmlite.binding as ll
import numpy as np
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.imputils import impl_ret_borrowed
from numba.extending import NativeValue, box, intrinsic, models, overload, overload_attribute, overload_method, register_model, unbox
from numba.parfors.array_analysis import ArrayAnalysis
from numba.typed.typedobjectutils import _cast
import bodo
from bodo.hiframes.datetime_date_ext import datetime_date_type
from bodo.hiframes.time_ext import TimeType
from bodo.libs import array_ext
from bodo.utils.cg_helpers import gen_allocate_array, get_array_elem_counts, get_bitmap_bit, is_na_value, pyarray_setitem, seq_getitem, set_bitmap_bit, to_arr_obj_if_list_obj
from bodo.utils.typing import BodoError, dtype_to_array_type, get_overload_const_int, get_overload_const_str, is_list_like_index_type, is_overload_constant_int, is_overload_constant_str, is_overload_none
ll.add_symbol('struct_array_from_sequence', array_ext.
    struct_array_from_sequence)
ll.add_symbol('np_array_from_struct_array', array_ext.
    np_array_from_struct_array)


class StructArrayType(types.ArrayCompatible):

    def __init__(self, data, names=None):
        assert isinstance(data, tuple) and len(data) > 0 and all(bodo.utils
            .utils.is_array_typ(vpcj__poci, False) for vpcj__poci in data)
        if names is not None:
            assert isinstance(names, tuple) and all(isinstance(vpcj__poci,
                str) for vpcj__poci in names) and len(names) == len(data)
        else:
            names = tuple('f{}'.format(i) for i in range(len(data)))
        self.data = data
        self.names = names
        super(StructArrayType, self).__init__(name=
            'StructArrayType({}, {})'.format(data, names))

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    @property
    def dtype(self):
        return StructType(tuple(mmet__xul.dtype for mmet__xul in self.data),
            self.names)

    @classmethod
    def from_dict(cls, d):
        assert isinstance(d, dict)
        names = tuple(str(vpcj__poci) for vpcj__poci in d.keys())
        data = tuple(dtype_to_array_type(mmet__xul) for mmet__xul in d.values()
            )
        return StructArrayType(data, names)

    def copy(self):
        return StructArrayType(self.data, self.names)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


class StructArrayPayloadType(types.Type):

    def __init__(self, data):
        assert isinstance(data, tuple) and all(bodo.utils.utils.
            is_array_typ(vpcj__poci, False) for vpcj__poci in data)
        self.data = data
        super(StructArrayPayloadType, self).__init__(name=
            'StructArrayPayloadType({})'.format(data))

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


@register_model(StructArrayPayloadType)
class StructArrayPayloadModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        cvmc__celx = [('data', types.BaseTuple.from_types(fe_type.data)), (
            'null_bitmap', types.Array(types.uint8, 1, 'C'))]
        models.StructModel.__init__(self, dmm, fe_type, cvmc__celx)


@register_model(StructArrayType)
class StructArrayModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        payload_type = StructArrayPayloadType(fe_type.data)
        cvmc__celx = [('meminfo', types.MemInfoPointer(payload_type))]
        models.StructModel.__init__(self, dmm, fe_type, cvmc__celx)


def define_struct_arr_dtor(context, builder, struct_arr_type, payload_type):
    nodu__gdew = builder.module
    wej__mdnpu = lir.FunctionType(lir.VoidType(), [cgutils.voidptr_t])
    xhmmd__copjf = cgutils.get_or_insert_function(nodu__gdew, wej__mdnpu,
        name='.dtor.struct_arr.{}.{}.'.format(struct_arr_type.data,
        struct_arr_type.names))
    if not xhmmd__copjf.is_declaration:
        return xhmmd__copjf
    xhmmd__copjf.linkage = 'linkonce_odr'
    builder = lir.IRBuilder(xhmmd__copjf.append_basic_block())
    efzso__zax = xhmmd__copjf.args[0]
    bqby__jzjd = context.get_value_type(payload_type).as_pointer()
    ebh__fgrqf = builder.bitcast(efzso__zax, bqby__jzjd)
    ntla__gpwij = context.make_helper(builder, payload_type, ref=ebh__fgrqf)
    context.nrt.decref(builder, types.BaseTuple.from_types(struct_arr_type.
        data), ntla__gpwij.data)
    context.nrt.decref(builder, types.Array(types.uint8, 1, 'C'),
        ntla__gpwij.null_bitmap)
    builder.ret_void()
    return xhmmd__copjf


def construct_struct_array(context, builder, struct_arr_type, n_structs,
    n_elems, c=None):
    payload_type = StructArrayPayloadType(struct_arr_type.data)
    fkmd__uxd = context.get_value_type(payload_type)
    cxj__xckx = context.get_abi_sizeof(fkmd__uxd)
    vfh__wubh = define_struct_arr_dtor(context, builder, struct_arr_type,
        payload_type)
    nucyy__sqre = context.nrt.meminfo_alloc_dtor(builder, context.
        get_constant(types.uintp, cxj__xckx), vfh__wubh)
    gbtmw__jwxk = context.nrt.meminfo_data(builder, nucyy__sqre)
    kgtv__ncb = builder.bitcast(gbtmw__jwxk, fkmd__uxd.as_pointer())
    ntla__gpwij = cgutils.create_struct_proxy(payload_type)(context, builder)
    arrs = []
    lnbo__xuay = 0
    for arr_typ in struct_arr_type.data:
        usq__bro = bodo.utils.transform.get_type_alloc_counts(arr_typ.dtype)
        hezjv__ujmfb = cgutils.pack_array(builder, [n_structs] + [builder.
            extract_value(n_elems, i) for i in range(lnbo__xuay, lnbo__xuay +
            usq__bro)])
        arr = gen_allocate_array(context, builder, arr_typ, hezjv__ujmfb, c)
        arrs.append(arr)
        lnbo__xuay += usq__bro
    ntla__gpwij.data = cgutils.pack_array(builder, arrs
        ) if types.is_homogeneous(*struct_arr_type.data
        ) else cgutils.pack_struct(builder, arrs)
    dndio__tpdke = builder.udiv(builder.add(n_structs, lir.Constant(lir.
        IntType(64), 7)), lir.Constant(lir.IntType(64), 8))
    aqwab__lum = bodo.utils.utils._empty_nd_impl(context, builder, types.
        Array(types.uint8, 1, 'C'), [dndio__tpdke])
    null_bitmap_ptr = aqwab__lum.data
    ntla__gpwij.null_bitmap = aqwab__lum._getvalue()
    builder.store(ntla__gpwij._getvalue(), kgtv__ncb)
    return nucyy__sqre, ntla__gpwij.data, null_bitmap_ptr


def _get_C_API_ptrs(c, data_tup, data_typ, names):
    hmhmn__sdxy = []
    assert len(data_typ) > 0
    for i, arr_typ in enumerate(data_typ):
        rqoi__mdgk = c.builder.extract_value(data_tup, i)
        arr = c.context.make_array(arr_typ)(c.context, c.builder, value=
            rqoi__mdgk)
        hmhmn__sdxy.append(arr.data)
    owbo__vzi = cgutils.pack_array(c.builder, hmhmn__sdxy
        ) if types.is_homogeneous(*data_typ) else cgutils.pack_struct(c.
        builder, hmhmn__sdxy)
    bpwgk__bsyjq = cgutils.alloca_once_value(c.builder, owbo__vzi)
    lhn__txdn = [c.context.get_constant(types.int32, bodo.utils.utils.
        numba_to_c_type(vpcj__poci.dtype)) for vpcj__poci in data_typ]
    nqj__zyos = cgutils.alloca_once_value(c.builder, cgutils.pack_array(c.
        builder, lhn__txdn))
    hqelh__uou = cgutils.pack_array(c.builder, [c.context.
        insert_const_string(c.builder.module, vpcj__poci) for vpcj__poci in
        names])
    jghk__qfxm = cgutils.alloca_once_value(c.builder, hqelh__uou)
    return bpwgk__bsyjq, nqj__zyos, jghk__qfxm


@unbox(StructArrayType)
def unbox_struct_array(typ, val, c, is_tuple_array=False):
    from bodo.libs.tuple_arr_ext import TupleArrayType
    n_structs = bodo.utils.utils.object_length(c, val)
    rvhr__irr = all(isinstance(mmet__xul, types.Array) and (mmet__xul.dtype in
        (types.int64, types.float64, types.bool_, datetime_date_type) or
        isinstance(mmet__xul.dtype, TimeType)) for mmet__xul in typ.data)
    if rvhr__irr:
        n_elems = cgutils.pack_array(c.builder, [], lir.IntType(64))
    else:
        ewa__tytta = get_array_elem_counts(c, c.builder, c.context, val, 
            TupleArrayType(typ.data) if is_tuple_array else typ)
        n_elems = cgutils.pack_array(c.builder, [c.builder.extract_value(
            ewa__tytta, i) for i in range(1, ewa__tytta.type.count)], lir.
            IntType(64))
    nucyy__sqre, data_tup, null_bitmap_ptr = construct_struct_array(c.
        context, c.builder, typ, n_structs, n_elems, c)
    if rvhr__irr:
        bpwgk__bsyjq, nqj__zyos, jghk__qfxm = _get_C_API_ptrs(c, data_tup,
            typ.data, typ.names)
        wej__mdnpu = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
            as_pointer(), lir.IntType(32), lir.IntType(8).as_pointer(), lir
            .IntType(8).as_pointer(), lir.IntType(8).as_pointer(), lir.
            IntType(8).as_pointer(), lir.IntType(1)])
        xhmmd__copjf = cgutils.get_or_insert_function(c.builder.module,
            wej__mdnpu, name='struct_array_from_sequence')
        c.builder.call(xhmmd__copjf, [val, c.context.get_constant(types.
            int32, len(typ.data)), c.builder.bitcast(bpwgk__bsyjq, lir.
            IntType(8).as_pointer()), null_bitmap_ptr, c.builder.bitcast(
            nqj__zyos, lir.IntType(8).as_pointer()), c.builder.bitcast(
            jghk__qfxm, lir.IntType(8).as_pointer()), c.context.
            get_constant(types.bool_, is_tuple_array)])
    else:
        _unbox_struct_array_generic(typ, val, c, n_structs, data_tup,
            null_bitmap_ptr, is_tuple_array)
    paz__lti = c.context.make_helper(c.builder, typ)
    paz__lti.meminfo = nucyy__sqre
    tyuvc__xvl = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(paz__lti._getvalue(), is_error=tyuvc__xvl)


def _unbox_struct_array_generic(typ, val, c, n_structs, data_tup,
    null_bitmap_ptr, is_tuple_array=False):
    context = c.context
    builder = c.builder
    zupj__tpigm = context.insert_const_string(builder.module, 'pandas')
    jhdwy__tutjs = c.pyapi.import_module_noblock(zupj__tpigm)
    fur__kpr = c.pyapi.object_getattr_string(jhdwy__tutjs, 'NA')
    with cgutils.for_range(builder, n_structs) as vzu__pwf:
        afi__fhtq = vzu__pwf.index
        cku__edoa = seq_getitem(builder, context, val, afi__fhtq)
        set_bitmap_bit(builder, null_bitmap_ptr, afi__fhtq, 0)
        for dqsgb__bisg in range(len(typ.data)):
            arr_typ = typ.data[dqsgb__bisg]
            data_arr = builder.extract_value(data_tup, dqsgb__bisg)

            def set_na(data_arr, i):
                bodo.libs.array_kernels.setna(data_arr, i)
            sig = types.none(arr_typ, types.int64)
            tvo__pwsfb, ptt__zgov = c.pyapi.call_jit_code(set_na, sig, [
                data_arr, afi__fhtq])
        qkgra__dcax = is_na_value(builder, context, cku__edoa, fur__kpr)
        blw__ytkog = builder.icmp_unsigned('!=', qkgra__dcax, lir.Constant(
            qkgra__dcax.type, 1))
        with builder.if_then(blw__ytkog):
            set_bitmap_bit(builder, null_bitmap_ptr, afi__fhtq, 1)
            for dqsgb__bisg in range(len(typ.data)):
                arr_typ = typ.data[dqsgb__bisg]
                if is_tuple_array:
                    iimou__qyen = c.pyapi.tuple_getitem(cku__edoa, dqsgb__bisg)
                else:
                    iimou__qyen = c.pyapi.dict_getitem_string(cku__edoa,
                        typ.names[dqsgb__bisg])
                qkgra__dcax = is_na_value(builder, context, iimou__qyen,
                    fur__kpr)
                blw__ytkog = builder.icmp_unsigned('!=', qkgra__dcax, lir.
                    Constant(qkgra__dcax.type, 1))
                with builder.if_then(blw__ytkog):
                    iimou__qyen = to_arr_obj_if_list_obj(c, context,
                        builder, iimou__qyen, arr_typ.dtype)
                    field_val = c.pyapi.to_native_value(arr_typ.dtype,
                        iimou__qyen).value
                    data_arr = builder.extract_value(data_tup, dqsgb__bisg)

                    def set_data(data_arr, i, field_val):
                        data_arr[i] = field_val
                    sig = types.none(arr_typ, types.int64, arr_typ.dtype)
                    tvo__pwsfb, ptt__zgov = c.pyapi.call_jit_code(set_data,
                        sig, [data_arr, afi__fhtq, field_val])
                    c.context.nrt.decref(builder, arr_typ.dtype, field_val)
        c.pyapi.decref(cku__edoa)
    c.pyapi.decref(jhdwy__tutjs)
    c.pyapi.decref(fur__kpr)


def _get_struct_arr_payload(context, builder, arr_typ, arr):
    paz__lti = context.make_helper(builder, arr_typ, arr)
    payload_type = StructArrayPayloadType(arr_typ.data)
    gbtmw__jwxk = context.nrt.meminfo_data(builder, paz__lti.meminfo)
    kgtv__ncb = builder.bitcast(gbtmw__jwxk, context.get_value_type(
        payload_type).as_pointer())
    ntla__gpwij = cgutils.create_struct_proxy(payload_type)(context,
        builder, builder.load(kgtv__ncb))
    return ntla__gpwij


@box(StructArrayType)
def box_struct_arr(typ, val, c, is_tuple_array=False):
    ntla__gpwij = _get_struct_arr_payload(c.context, c.builder, typ, val)
    tvo__pwsfb, length = c.pyapi.call_jit_code(lambda A: len(A), types.
        int64(typ), [val])
    null_bitmap_ptr = c.context.make_helper(c.builder, types.Array(types.
        uint8, 1, 'C'), ntla__gpwij.null_bitmap).data
    rvhr__irr = all(isinstance(mmet__xul, types.Array) and (mmet__xul.dtype in
        (types.int64, types.float64, types.bool_, datetime_date_type) or
        isinstance(mmet__xul.dtype, TimeType)) for mmet__xul in typ.data)
    if rvhr__irr:
        bpwgk__bsyjq, nqj__zyos, jghk__qfxm = _get_C_API_ptrs(c,
            ntla__gpwij.data, typ.data, typ.names)
        wej__mdnpu = lir.FunctionType(c.context.get_argument_type(types.
            pyobject), [lir.IntType(64), lir.IntType(32), lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(1)])
        bxuby__tionf = cgutils.get_or_insert_function(c.builder.module,
            wej__mdnpu, name='np_array_from_struct_array')
        arr = c.builder.call(bxuby__tionf, [length, c.context.get_constant(
            types.int32, len(typ.data)), c.builder.bitcast(bpwgk__bsyjq,
            lir.IntType(8).as_pointer()), null_bitmap_ptr, c.builder.
            bitcast(nqj__zyos, lir.IntType(8).as_pointer()), c.builder.
            bitcast(jghk__qfxm, lir.IntType(8).as_pointer()), c.context.
            get_constant(types.bool_, is_tuple_array)])
    else:
        arr = _box_struct_array_generic(typ, c, length, ntla__gpwij.data,
            null_bitmap_ptr, is_tuple_array)
    c.context.nrt.decref(c.builder, typ, val)
    return arr


def _box_struct_array_generic(typ, c, length, data_arrs_tup,
    null_bitmap_ptr, is_tuple_array=False):
    context = c.context
    builder = c.builder
    zupj__tpigm = context.insert_const_string(builder.module, 'numpy')
    sxx__zqkzf = c.pyapi.import_module_noblock(zupj__tpigm)
    lgq__ris = c.pyapi.object_getattr_string(sxx__zqkzf, 'object_')
    rqra__opfo = c.pyapi.long_from_longlong(length)
    wex__ignww = c.pyapi.call_method(sxx__zqkzf, 'ndarray', (rqra__opfo,
        lgq__ris))
    sbh__mnvem = c.pyapi.object_getattr_string(sxx__zqkzf, 'nan')
    with cgutils.for_range(builder, length) as vzu__pwf:
        afi__fhtq = vzu__pwf.index
        pyarray_setitem(builder, context, wex__ignww, afi__fhtq, sbh__mnvem)
        tkp__kceb = get_bitmap_bit(builder, null_bitmap_ptr, afi__fhtq)
        qhov__iwzce = builder.icmp_unsigned('!=', tkp__kceb, lir.Constant(
            lir.IntType(8), 0))
        with builder.if_then(qhov__iwzce):
            if is_tuple_array:
                cku__edoa = c.pyapi.tuple_new(len(typ.data))
            else:
                cku__edoa = c.pyapi.dict_new(len(typ.data))
            for i, arr_typ in enumerate(typ.data):
                if is_tuple_array:
                    c.pyapi.incref(sbh__mnvem)
                    c.pyapi.tuple_setitem(cku__edoa, i, sbh__mnvem)
                else:
                    c.pyapi.dict_setitem_string(cku__edoa, typ.names[i],
                        sbh__mnvem)
                data_arr = c.builder.extract_value(data_arrs_tup, i)
                tvo__pwsfb, hwk__eomde = c.pyapi.call_jit_code(lambda
                    data_arr, ind: not bodo.libs.array_kernels.isna(
                    data_arr, ind), types.bool_(arr_typ, types.int64), [
                    data_arr, afi__fhtq])
                with builder.if_then(hwk__eomde):
                    tvo__pwsfb, field_val = c.pyapi.call_jit_code(lambda
                        data_arr, ind: data_arr[ind], arr_typ.dtype(arr_typ,
                        types.int64), [data_arr, afi__fhtq])
                    zrup__bjc = c.pyapi.from_native_value(arr_typ.dtype,
                        field_val, c.env_manager)
                    if is_tuple_array:
                        c.pyapi.tuple_setitem(cku__edoa, i, zrup__bjc)
                    else:
                        c.pyapi.dict_setitem_string(cku__edoa, typ.names[i],
                            zrup__bjc)
                        c.pyapi.decref(zrup__bjc)
            pyarray_setitem(builder, context, wex__ignww, afi__fhtq, cku__edoa)
            c.pyapi.decref(cku__edoa)
    c.pyapi.decref(sxx__zqkzf)
    c.pyapi.decref(lgq__ris)
    c.pyapi.decref(rqra__opfo)
    c.pyapi.decref(sbh__mnvem)
    return wex__ignww


def _fix_nested_counts(nested_counts, struct_arr_type, nested_counts_type,
    builder):
    cawb__nnqw = bodo.utils.transform.get_type_alloc_counts(struct_arr_type
        ) - 1
    if cawb__nnqw == 0:
        return nested_counts
    if not isinstance(nested_counts_type, types.UniTuple):
        nested_counts = cgutils.pack_array(builder, [lir.Constant(lir.
            IntType(64), -1) for wycx__ebmqb in range(cawb__nnqw)])
    elif nested_counts_type.count < cawb__nnqw:
        nested_counts = cgutils.pack_array(builder, [builder.extract_value(
            nested_counts, i) for i in range(nested_counts_type.count)] + [
            lir.Constant(lir.IntType(64), -1) for wycx__ebmqb in range(
            cawb__nnqw - nested_counts_type.count)])
    return nested_counts


@intrinsic
def pre_alloc_struct_array(typingctx, num_structs_typ, nested_counts_typ,
    dtypes_typ, names_typ=None):
    assert isinstance(num_structs_typ, types.Integer) and isinstance(dtypes_typ
        , types.BaseTuple)
    if is_overload_none(names_typ):
        names = tuple(f'f{i}' for i in range(len(dtypes_typ)))
    else:
        names = tuple(get_overload_const_str(mmet__xul) for mmet__xul in
            names_typ.types)
    kkswd__vleak = tuple(mmet__xul.instance_type for mmet__xul in
        dtypes_typ.types)
    struct_arr_type = StructArrayType(kkswd__vleak, names)

    def codegen(context, builder, sig, args):
        mofe__itm, nested_counts, wycx__ebmqb, wycx__ebmqb = args
        nested_counts_type = sig.args[1]
        nested_counts = _fix_nested_counts(nested_counts, struct_arr_type,
            nested_counts_type, builder)
        nucyy__sqre, wycx__ebmqb, wycx__ebmqb = construct_struct_array(context,
            builder, struct_arr_type, mofe__itm, nested_counts)
        paz__lti = context.make_helper(builder, struct_arr_type)
        paz__lti.meminfo = nucyy__sqre
        return paz__lti._getvalue()
    return struct_arr_type(num_structs_typ, nested_counts_typ, dtypes_typ,
        names_typ), codegen


def pre_alloc_struct_array_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 4 and not kws
    return ArrayAnalysis.AnalyzeResult(shape=args[0], pre=[])


(ArrayAnalysis._analyze_op_call_bodo_libs_struct_arr_ext_pre_alloc_struct_array
    ) = pre_alloc_struct_array_equiv


class StructType(types.Type):

    def __init__(self, data, names):
        assert isinstance(data, tuple) and len(data) > 0
        assert isinstance(names, tuple) and all(isinstance(vpcj__poci, str) for
            vpcj__poci in names) and len(names) == len(data)
        self.data = data
        self.names = names
        super(StructType, self).__init__(name='StructType({}, {})'.format(
            data, names))

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


class StructPayloadType(types.Type):

    def __init__(self, data):
        assert isinstance(data, tuple)
        self.data = data
        super(StructPayloadType, self).__init__(name=
            'StructPayloadType({})'.format(data))

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


@register_model(StructPayloadType)
class StructPayloadModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        cvmc__celx = [('data', types.BaseTuple.from_types(fe_type.data)), (
            'null_bitmap', types.UniTuple(types.int8, len(fe_type.data)))]
        models.StructModel.__init__(self, dmm, fe_type, cvmc__celx)


@register_model(StructType)
class StructModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        payload_type = StructPayloadType(fe_type.data)
        cvmc__celx = [('meminfo', types.MemInfoPointer(payload_type))]
        models.StructModel.__init__(self, dmm, fe_type, cvmc__celx)


def define_struct_dtor(context, builder, struct_type, payload_type):
    nodu__gdew = builder.module
    wej__mdnpu = lir.FunctionType(lir.VoidType(), [cgutils.voidptr_t])
    xhmmd__copjf = cgutils.get_or_insert_function(nodu__gdew, wej__mdnpu,
        name='.dtor.struct.{}.{}.'.format(struct_type.data, struct_type.names))
    if not xhmmd__copjf.is_declaration:
        return xhmmd__copjf
    xhmmd__copjf.linkage = 'linkonce_odr'
    builder = lir.IRBuilder(xhmmd__copjf.append_basic_block())
    efzso__zax = xhmmd__copjf.args[0]
    bqby__jzjd = context.get_value_type(payload_type).as_pointer()
    ebh__fgrqf = builder.bitcast(efzso__zax, bqby__jzjd)
    ntla__gpwij = context.make_helper(builder, payload_type, ref=ebh__fgrqf)
    for i in range(len(struct_type.data)):
        wypfz__tkn = builder.extract_value(ntla__gpwij.null_bitmap, i)
        qhov__iwzce = builder.icmp_unsigned('==', wypfz__tkn, lir.Constant(
            wypfz__tkn.type, 1))
        with builder.if_then(qhov__iwzce):
            val = builder.extract_value(ntla__gpwij.data, i)
            context.nrt.decref(builder, struct_type.data[i], val)
    builder.ret_void()
    return xhmmd__copjf


def _get_struct_payload(context, builder, typ, struct):
    struct = context.make_helper(builder, typ, struct)
    payload_type = StructPayloadType(typ.data)
    gbtmw__jwxk = context.nrt.meminfo_data(builder, struct.meminfo)
    kgtv__ncb = builder.bitcast(gbtmw__jwxk, context.get_value_type(
        payload_type).as_pointer())
    ntla__gpwij = cgutils.create_struct_proxy(payload_type)(context,
        builder, builder.load(kgtv__ncb))
    return ntla__gpwij, kgtv__ncb


@unbox(StructType)
def unbox_struct(typ, val, c):
    context = c.context
    builder = c.builder
    zupj__tpigm = context.insert_const_string(builder.module, 'pandas')
    jhdwy__tutjs = c.pyapi.import_module_noblock(zupj__tpigm)
    fur__kpr = c.pyapi.object_getattr_string(jhdwy__tutjs, 'NA')
    csq__yhh = []
    nulls = []
    for i, mmet__xul in enumerate(typ.data):
        zrup__bjc = c.pyapi.dict_getitem_string(val, typ.names[i])
        xiut__nae = cgutils.alloca_once_value(c.builder, context.
            get_constant(types.uint8, 0))
        yzvbl__kelc = cgutils.alloca_once_value(c.builder, cgutils.
            get_null_value(context.get_value_type(mmet__xul)))
        qkgra__dcax = is_na_value(builder, context, zrup__bjc, fur__kpr)
        qhov__iwzce = builder.icmp_unsigned('!=', qkgra__dcax, lir.Constant
            (qkgra__dcax.type, 1))
        with builder.if_then(qhov__iwzce):
            builder.store(context.get_constant(types.uint8, 1), xiut__nae)
            field_val = c.pyapi.to_native_value(mmet__xul, zrup__bjc).value
            builder.store(field_val, yzvbl__kelc)
        csq__yhh.append(builder.load(yzvbl__kelc))
        nulls.append(builder.load(xiut__nae))
    c.pyapi.decref(jhdwy__tutjs)
    c.pyapi.decref(fur__kpr)
    nucyy__sqre = construct_struct(context, builder, typ, csq__yhh, nulls)
    struct = context.make_helper(builder, typ)
    struct.meminfo = nucyy__sqre
    tyuvc__xvl = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(struct._getvalue(), is_error=tyuvc__xvl)


@box(StructType)
def box_struct(typ, val, c):
    vlj__pcp = c.pyapi.dict_new(len(typ.data))
    ntla__gpwij, wycx__ebmqb = _get_struct_payload(c.context, c.builder,
        typ, val)
    assert len(typ.data) > 0
    for i, val_typ in enumerate(typ.data):
        c.pyapi.dict_setitem_string(vlj__pcp, typ.names[i], c.pyapi.
            borrow_none())
        wypfz__tkn = c.builder.extract_value(ntla__gpwij.null_bitmap, i)
        qhov__iwzce = c.builder.icmp_unsigned('==', wypfz__tkn, lir.
            Constant(wypfz__tkn.type, 1))
        with c.builder.if_then(qhov__iwzce):
            kqqp__kkeeo = c.builder.extract_value(ntla__gpwij.data, i)
            c.context.nrt.incref(c.builder, val_typ, kqqp__kkeeo)
            iimou__qyen = c.pyapi.from_native_value(val_typ, kqqp__kkeeo, c
                .env_manager)
            c.pyapi.dict_setitem_string(vlj__pcp, typ.names[i], iimou__qyen)
            c.pyapi.decref(iimou__qyen)
    c.context.nrt.decref(c.builder, typ, val)
    return vlj__pcp


@intrinsic
def init_struct(typingctx, data_typ, names_typ=None):
    names = tuple(get_overload_const_str(mmet__xul) for mmet__xul in
        names_typ.types)
    struct_type = StructType(data_typ.types, names)

    def codegen(context, builder, sig, args):
        data, fodew__iom = args
        payload_type = StructPayloadType(struct_type.data)
        fkmd__uxd = context.get_value_type(payload_type)
        cxj__xckx = context.get_abi_sizeof(fkmd__uxd)
        vfh__wubh = define_struct_dtor(context, builder, struct_type,
            payload_type)
        nucyy__sqre = context.nrt.meminfo_alloc_dtor(builder, context.
            get_constant(types.uintp, cxj__xckx), vfh__wubh)
        gbtmw__jwxk = context.nrt.meminfo_data(builder, nucyy__sqre)
        kgtv__ncb = builder.bitcast(gbtmw__jwxk, fkmd__uxd.as_pointer())
        ntla__gpwij = cgutils.create_struct_proxy(payload_type)(context,
            builder)
        ntla__gpwij.data = data
        ntla__gpwij.null_bitmap = cgutils.pack_array(builder, [context.
            get_constant(types.uint8, 1) for wycx__ebmqb in range(len(
            data_typ.types))])
        builder.store(ntla__gpwij._getvalue(), kgtv__ncb)
        context.nrt.incref(builder, data_typ, data)
        struct = context.make_helper(builder, struct_type)
        struct.meminfo = nucyy__sqre
        return struct._getvalue()
    return struct_type(data_typ, names_typ), codegen


@intrinsic
def get_struct_data(typingctx, struct_typ=None):
    assert isinstance(struct_typ, StructType)

    def codegen(context, builder, sig, args):
        struct, = args
        ntla__gpwij, wycx__ebmqb = _get_struct_payload(context, builder,
            struct_typ, struct)
        return impl_ret_borrowed(context, builder, sig.return_type,
            ntla__gpwij.data)
    return types.BaseTuple.from_types(struct_typ.data)(struct_typ), codegen


@intrinsic
def get_struct_null_bitmap(typingctx, struct_typ=None):
    assert isinstance(struct_typ, StructType)

    def codegen(context, builder, sig, args):
        struct, = args
        ntla__gpwij, wycx__ebmqb = _get_struct_payload(context, builder,
            struct_typ, struct)
        return impl_ret_borrowed(context, builder, sig.return_type,
            ntla__gpwij.null_bitmap)
    jkp__hyrud = types.UniTuple(types.int8, len(struct_typ.data))
    return jkp__hyrud(struct_typ), codegen


@intrinsic
def set_struct_data(typingctx, struct_typ, field_ind_typ, val_typ=None):
    assert isinstance(struct_typ, StructType) and is_overload_constant_int(
        field_ind_typ)
    field_ind = get_overload_const_int(field_ind_typ)

    def codegen(context, builder, sig, args):
        struct, wycx__ebmqb, val = args
        ntla__gpwij, kgtv__ncb = _get_struct_payload(context, builder,
            struct_typ, struct)
        zjd__jqqm = ntla__gpwij.data
        poe__ytm = builder.insert_value(zjd__jqqm, val, field_ind)
        rev__hfq = types.BaseTuple.from_types(struct_typ.data)
        context.nrt.decref(builder, rev__hfq, zjd__jqqm)
        context.nrt.incref(builder, rev__hfq, poe__ytm)
        ntla__gpwij.data = poe__ytm
        builder.store(ntla__gpwij._getvalue(), kgtv__ncb)
        return context.get_dummy_value()
    return types.none(struct_typ, field_ind_typ, val_typ), codegen


def _get_struct_field_ind(struct, ind, op):
    if not is_overload_constant_str(ind):
        raise BodoError(
            'structs (from struct array) only support constant strings for {}, not {}'
            .format(op, ind))
    swje__jfsm = get_overload_const_str(ind)
    if swje__jfsm not in struct.names:
        raise BodoError('Field {} does not exist in struct {}'.format(
            swje__jfsm, struct))
    return struct.names.index(swje__jfsm)


def is_field_value_null(s, field_name):
    pass


@overload(is_field_value_null, no_unliteral=True)
def overload_is_field_value_null(s, field_name):
    field_ind = _get_struct_field_ind(s, field_name, 'element access (getitem)'
        )
    return lambda s, field_name: get_struct_null_bitmap(s)[field_ind] == 0


@overload(operator.getitem, no_unliteral=True)
def struct_getitem(struct, ind):
    if not isinstance(struct, StructType):
        return
    field_ind = _get_struct_field_ind(struct, ind, 'element access (getitem)')
    return lambda struct, ind: get_struct_data(struct)[field_ind]


@overload(operator.setitem, no_unliteral=True)
def struct_setitem(struct, ind, val):
    if not isinstance(struct, StructType):
        return
    field_ind = _get_struct_field_ind(struct, ind, 'item assignment (setitem)')
    field_typ = struct.data[field_ind]
    return lambda struct, ind, val: set_struct_data(struct, field_ind,
        _cast(val, field_typ))


@overload(len, no_unliteral=True)
def overload_struct_arr_len(struct):
    if isinstance(struct, StructType):
        num_fields = len(struct.data)
        return lambda struct: num_fields


def construct_struct(context, builder, struct_type, values, nulls):
    payload_type = StructPayloadType(struct_type.data)
    fkmd__uxd = context.get_value_type(payload_type)
    cxj__xckx = context.get_abi_sizeof(fkmd__uxd)
    vfh__wubh = define_struct_dtor(context, builder, struct_type, payload_type)
    nucyy__sqre = context.nrt.meminfo_alloc_dtor(builder, context.
        get_constant(types.uintp, cxj__xckx), vfh__wubh)
    gbtmw__jwxk = context.nrt.meminfo_data(builder, nucyy__sqre)
    kgtv__ncb = builder.bitcast(gbtmw__jwxk, fkmd__uxd.as_pointer())
    ntla__gpwij = cgutils.create_struct_proxy(payload_type)(context, builder)
    ntla__gpwij.data = cgutils.pack_array(builder, values
        ) if types.is_homogeneous(*struct_type.data) else cgutils.pack_struct(
        builder, values)
    ntla__gpwij.null_bitmap = cgutils.pack_array(builder, nulls)
    builder.store(ntla__gpwij._getvalue(), kgtv__ncb)
    return nucyy__sqre


@intrinsic
def struct_array_get_struct(typingctx, struct_arr_typ, ind_typ=None):
    assert isinstance(struct_arr_typ, StructArrayType) and isinstance(ind_typ,
        types.Integer)
    bjnvy__opt = tuple(d.dtype for d in struct_arr_typ.data)
    qidlb__hla = StructType(bjnvy__opt, struct_arr_typ.names)

    def codegen(context, builder, sig, args):
        neek__yuel, ind = args
        ntla__gpwij = _get_struct_arr_payload(context, builder,
            struct_arr_typ, neek__yuel)
        csq__yhh = []
        odqop__glxxf = []
        for i, arr_typ in enumerate(struct_arr_typ.data):
            rqoi__mdgk = builder.extract_value(ntla__gpwij.data, i)
            cia__hyo = context.compile_internal(builder, lambda arr, ind: 
                np.uint8(0) if bodo.libs.array_kernels.isna(arr, ind) else
                np.uint8(1), types.uint8(arr_typ, types.int64), [rqoi__mdgk,
                ind])
            odqop__glxxf.append(cia__hyo)
            fltsn__aksbp = cgutils.alloca_once_value(builder, context.
                get_constant_null(arr_typ.dtype))
            qhov__iwzce = builder.icmp_unsigned('==', cia__hyo, lir.
                Constant(cia__hyo.type, 1))
            with builder.if_then(qhov__iwzce):
                kzqe__gcxp = context.compile_internal(builder, lambda arr,
                    ind: arr[ind], arr_typ.dtype(arr_typ, types.int64), [
                    rqoi__mdgk, ind])
                builder.store(kzqe__gcxp, fltsn__aksbp)
            csq__yhh.append(builder.load(fltsn__aksbp))
        if isinstance(qidlb__hla, types.DictType):
            wkwc__oykq = [context.insert_const_string(builder.module,
                jcan__qhad) for jcan__qhad in struct_arr_typ.names]
            ouhpt__rdyd = cgutils.pack_array(builder, csq__yhh)
            pto__nlkm = cgutils.pack_array(builder, wkwc__oykq)

            def impl(names, vals):
                d = {}
                for i, jcan__qhad in enumerate(names):
                    d[jcan__qhad] = vals[i]
                return d
            hxn__fbjlc = context.compile_internal(builder, impl, qidlb__hla
                (types.Tuple(tuple(types.StringLiteral(jcan__qhad) for
                jcan__qhad in struct_arr_typ.names)), types.Tuple(
                bjnvy__opt)), [pto__nlkm, ouhpt__rdyd])
            context.nrt.decref(builder, types.BaseTuple.from_types(
                bjnvy__opt), ouhpt__rdyd)
            return hxn__fbjlc
        nucyy__sqre = construct_struct(context, builder, qidlb__hla,
            csq__yhh, odqop__glxxf)
        struct = context.make_helper(builder, qidlb__hla)
        struct.meminfo = nucyy__sqre
        return struct._getvalue()
    return qidlb__hla(struct_arr_typ, ind_typ), codegen


@intrinsic
def get_data(typingctx, arr_typ=None):
    assert isinstance(arr_typ, StructArrayType)

    def codegen(context, builder, sig, args):
        arr, = args
        ntla__gpwij = _get_struct_arr_payload(context, builder, arr_typ, arr)
        return impl_ret_borrowed(context, builder, sig.return_type,
            ntla__gpwij.data)
    return types.BaseTuple.from_types(arr_typ.data)(arr_typ), codegen


@intrinsic
def get_null_bitmap(typingctx, arr_typ=None):
    assert isinstance(arr_typ, StructArrayType)

    def codegen(context, builder, sig, args):
        arr, = args
        ntla__gpwij = _get_struct_arr_payload(context, builder, arr_typ, arr)
        return impl_ret_borrowed(context, builder, sig.return_type,
            ntla__gpwij.null_bitmap)
    return types.Array(types.uint8, 1, 'C')(arr_typ), codegen


@intrinsic
def init_struct_arr(typingctx, data_typ, null_bitmap_typ, names_typ=None):
    names = tuple(get_overload_const_str(mmet__xul) for mmet__xul in
        names_typ.types)
    struct_arr_type = StructArrayType(data_typ.types, names)

    def codegen(context, builder, sig, args):
        data, aqwab__lum, fodew__iom = args
        payload_type = StructArrayPayloadType(struct_arr_type.data)
        fkmd__uxd = context.get_value_type(payload_type)
        cxj__xckx = context.get_abi_sizeof(fkmd__uxd)
        vfh__wubh = define_struct_arr_dtor(context, builder,
            struct_arr_type, payload_type)
        nucyy__sqre = context.nrt.meminfo_alloc_dtor(builder, context.
            get_constant(types.uintp, cxj__xckx), vfh__wubh)
        gbtmw__jwxk = context.nrt.meminfo_data(builder, nucyy__sqre)
        kgtv__ncb = builder.bitcast(gbtmw__jwxk, fkmd__uxd.as_pointer())
        ntla__gpwij = cgutils.create_struct_proxy(payload_type)(context,
            builder)
        ntla__gpwij.data = data
        ntla__gpwij.null_bitmap = aqwab__lum
        builder.store(ntla__gpwij._getvalue(), kgtv__ncb)
        context.nrt.incref(builder, data_typ, data)
        context.nrt.incref(builder, null_bitmap_typ, aqwab__lum)
        paz__lti = context.make_helper(builder, struct_arr_type)
        paz__lti.meminfo = nucyy__sqre
        return paz__lti._getvalue()
    return struct_arr_type(data_typ, null_bitmap_typ, names_typ), codegen


@overload(operator.getitem, no_unliteral=True)
def struct_arr_getitem(arr, ind):
    if not isinstance(arr, StructArrayType):
        return
    if isinstance(ind, types.Integer):

        def struct_arr_getitem_impl(arr, ind):
            if ind < 0:
                ind += len(arr)
            return struct_array_get_struct(arr, ind)
        return struct_arr_getitem_impl
    if ind != bodo.boolean_array:
        pit__clwzg = len(arr.data)
        msmkk__pyhg = 'def impl(arr, ind):\n'
        msmkk__pyhg += '  data = get_data(arr)\n'
        msmkk__pyhg += '  null_bitmap = get_null_bitmap(arr)\n'
        if is_list_like_index_type(ind) and ind.dtype == types.bool_:
            msmkk__pyhg += """  out_null_bitmap = get_new_null_mask_bool_index(null_bitmap, ind, len(data[0]))
"""
        elif is_list_like_index_type(ind) and isinstance(ind.dtype, types.
            Integer):
            msmkk__pyhg += """  out_null_bitmap = get_new_null_mask_int_index(null_bitmap, ind, len(data[0]))
"""
        elif isinstance(ind, types.SliceType):
            msmkk__pyhg += """  out_null_bitmap = get_new_null_mask_slice_index(null_bitmap, ind, len(data[0]))
"""
        else:
            raise BodoError('invalid index {} in struct array indexing'.
                format(ind))
        msmkk__pyhg += (
            '  return init_struct_arr(({},), out_null_bitmap, ({},))\n'.
            format(', '.join('ensure_contig_if_np(data[{}][ind])'.format(i) for
            i in range(pit__clwzg)), ', '.join("'{}'".format(jcan__qhad) for
            jcan__qhad in arr.names)))
        uliha__lnr = {}
        exec(msmkk__pyhg, {'init_struct_arr': init_struct_arr, 'get_data':
            get_data, 'get_null_bitmap': get_null_bitmap,
            'ensure_contig_if_np': bodo.utils.conversion.
            ensure_contig_if_np, 'get_new_null_mask_bool_index': bodo.utils
            .indexing.get_new_null_mask_bool_index,
            'get_new_null_mask_int_index': bodo.utils.indexing.
            get_new_null_mask_int_index, 'get_new_null_mask_slice_index':
            bodo.utils.indexing.get_new_null_mask_slice_index}, uliha__lnr)
        impl = uliha__lnr['impl']
        return impl


@overload(operator.setitem, no_unliteral=True)
def struct_arr_setitem(arr, ind, val):
    if not isinstance(arr, StructArrayType):
        return
    if val == types.none or isinstance(val, types.optional):
        return
    if isinstance(ind, types.Integer):
        pit__clwzg = len(arr.data)
        msmkk__pyhg = 'def impl(arr, ind, val):\n'
        msmkk__pyhg += '  data = get_data(arr)\n'
        msmkk__pyhg += '  null_bitmap = get_null_bitmap(arr)\n'
        msmkk__pyhg += '  set_bit_to_arr(null_bitmap, ind, 1)\n'
        for i in range(pit__clwzg):
            if isinstance(val, StructType):
                msmkk__pyhg += "  if is_field_value_null(val, '{}'):\n".format(
                    arr.names[i])
                msmkk__pyhg += (
                    '    bodo.libs.array_kernels.setna(data[{}], ind)\n'.
                    format(i))
                msmkk__pyhg += '  else:\n'
                msmkk__pyhg += "    data[{}][ind] = val['{}']\n".format(i,
                    arr.names[i])
            else:
                msmkk__pyhg += "  data[{}][ind] = val['{}']\n".format(i,
                    arr.names[i])
        uliha__lnr = {}
        exec(msmkk__pyhg, {'bodo': bodo, 'get_data': get_data,
            'get_null_bitmap': get_null_bitmap, 'set_bit_to_arr': bodo.libs
            .int_arr_ext.set_bit_to_arr, 'is_field_value_null':
            is_field_value_null}, uliha__lnr)
        impl = uliha__lnr['impl']
        return impl
    if isinstance(ind, types.SliceType):
        pit__clwzg = len(arr.data)
        msmkk__pyhg = 'def impl(arr, ind, val):\n'
        msmkk__pyhg += '  data = get_data(arr)\n'
        msmkk__pyhg += '  null_bitmap = get_null_bitmap(arr)\n'
        msmkk__pyhg += '  val_data = get_data(val)\n'
        msmkk__pyhg += '  val_null_bitmap = get_null_bitmap(val)\n'
        msmkk__pyhg += """  setitem_slice_index_null_bits(null_bitmap, val_null_bitmap, ind, len(arr))
"""
        for i in range(pit__clwzg):
            msmkk__pyhg += '  data[{0}][ind] = val_data[{0}]\n'.format(i)
        uliha__lnr = {}
        exec(msmkk__pyhg, {'bodo': bodo, 'get_data': get_data,
            'get_null_bitmap': get_null_bitmap, 'set_bit_to_arr': bodo.libs
            .int_arr_ext.set_bit_to_arr, 'setitem_slice_index_null_bits':
            bodo.utils.indexing.setitem_slice_index_null_bits}, uliha__lnr)
        impl = uliha__lnr['impl']
        return impl
    raise BodoError(
        'only setitem with scalar/slice index is currently supported for struct arrays'
        )


@overload(len, no_unliteral=True)
def overload_struct_arr_len(A):
    if isinstance(A, StructArrayType):
        return lambda A: len(get_data(A)[0])


@overload_attribute(StructArrayType, 'shape')
def overload_struct_arr_shape(A):
    return lambda A: (len(get_data(A)[0]),)


@overload_attribute(StructArrayType, 'dtype')
def overload_struct_arr_dtype(A):
    return lambda A: np.object_


@overload_attribute(StructArrayType, 'ndim')
def overload_struct_arr_ndim(A):
    return lambda A: 1


@overload_attribute(StructArrayType, 'nbytes')
def overload_struct_arr_nbytes(A):
    msmkk__pyhg = 'def impl(A):\n'
    msmkk__pyhg += '  total_nbytes = 0\n'
    msmkk__pyhg += '  data = get_data(A)\n'
    for i in range(len(A.data)):
        msmkk__pyhg += f'  total_nbytes += data[{i}].nbytes\n'
    msmkk__pyhg += '  total_nbytes += get_null_bitmap(A).nbytes\n'
    msmkk__pyhg += '  return total_nbytes\n'
    uliha__lnr = {}
    exec(msmkk__pyhg, {'get_data': get_data, 'get_null_bitmap':
        get_null_bitmap}, uliha__lnr)
    impl = uliha__lnr['impl']
    return impl


@overload_method(StructArrayType, 'copy', no_unliteral=True)
def overload_struct_arr_copy(A):
    names = A.names

    def copy_impl(A):
        data = get_data(A)
        aqwab__lum = get_null_bitmap(A)
        nfot__tas = bodo.libs.struct_arr_ext.copy_arr_tup(data)
        edge__nbn = aqwab__lum.copy()
        return init_struct_arr(nfot__tas, edge__nbn, names)
    return copy_impl


def copy_arr_tup(arrs):
    return tuple(vpcj__poci.copy() for vpcj__poci in arrs)


@overload(copy_arr_tup, no_unliteral=True)
def copy_arr_tup_overload(arrs):
    xdt__fmm = arrs.count
    msmkk__pyhg = 'def f(arrs):\n'
    msmkk__pyhg += '  return ({},)\n'.format(','.join('arrs[{}].copy()'.
        format(i) for i in range(xdt__fmm)))
    uliha__lnr = {}
    exec(msmkk__pyhg, {}, uliha__lnr)
    impl = uliha__lnr['f']
    return impl
