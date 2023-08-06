"""Array implementation for variable-size array items.
Corresponds to Spark's ArrayType: https://spark.apache.org/docs/latest/sql-reference.html
Corresponds to Arrow's Variable-size List: https://arrow.apache.org/docs/format/Columnar.html

The values are stored in a contingous data array, while an offsets array marks the
individual arrays. For example:
value:             [[1, 2], [3], None, [5, 4, 6], []]
data:              [1, 2, 3, 5, 4, 6]
offsets:           [0, 2, 3, 3, 6, 6]
"""
import operator
import llvmlite.binding as ll
import numba
import numpy as np
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.imputils import impl_ret_borrowed
from numba.extending import NativeValue, box, intrinsic, models, overload, overload_attribute, overload_method, register_model, unbox
from numba.parfors.array_analysis import ArrayAnalysis
import bodo
from bodo.hiframes.datetime_date_ext import datetime_date_type
from bodo.libs import array_ext
from bodo.utils.cg_helpers import gen_allocate_array, get_array_elem_counts, get_bitmap_bit, is_na_value, pyarray_setitem, seq_getitem, set_bitmap_bit, to_arr_obj_if_list_obj
from bodo.utils.indexing import add_nested_counts, init_nested_counts
from bodo.utils.typing import BodoError, is_iterable_type, is_list_like_index_type
ll.add_symbol('count_total_elems_list_array', array_ext.
    count_total_elems_list_array)
ll.add_symbol('array_item_array_from_sequence', array_ext.
    array_item_array_from_sequence)
ll.add_symbol('np_array_from_array_item_array', array_ext.
    np_array_from_array_item_array)
offset_type = types.uint64
np_offset_type = numba.np.numpy_support.as_dtype(offset_type)


class ArrayItemArrayType(types.ArrayCompatible):

    def __init__(self, dtype):
        assert bodo.utils.utils.is_array_typ(dtype, False)
        self.dtype = dtype
        super(ArrayItemArrayType, self).__init__(name=
            'ArrayItemArrayType({})'.format(dtype))

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    def copy(self):
        return ArrayItemArrayType(self.dtype)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


class ArrayItemArrayPayloadType(types.Type):

    def __init__(self, array_type):
        self.array_type = array_type
        super(ArrayItemArrayPayloadType, self).__init__(name=
            'ArrayItemArrayPayloadType({})'.format(array_type))

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


@register_model(ArrayItemArrayPayloadType)
class ArrayItemArrayPayloadModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        eeng__fnton = [('n_arrays', types.int64), ('data', fe_type.
            array_type.dtype), ('offsets', types.Array(offset_type, 1, 'C')
            ), ('null_bitmap', types.Array(types.uint8, 1, 'C'))]
        models.StructModel.__init__(self, dmm, fe_type, eeng__fnton)


@register_model(ArrayItemArrayType)
class ArrayItemArrayModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        payload_type = ArrayItemArrayPayloadType(fe_type)
        eeng__fnton = [('meminfo', types.MemInfoPointer(payload_type))]
        models.StructModel.__init__(self, dmm, fe_type, eeng__fnton)


def define_array_item_dtor(context, builder, array_item_type, payload_type):
    mmn__ypfqr = builder.module
    txzj__khwaa = lir.FunctionType(lir.VoidType(), [cgutils.voidptr_t])
    hiq__ngqlb = cgutils.get_or_insert_function(mmn__ypfqr, txzj__khwaa,
        name='.dtor.array_item.{}'.format(array_item_type.dtype))
    if not hiq__ngqlb.is_declaration:
        return hiq__ngqlb
    hiq__ngqlb.linkage = 'linkonce_odr'
    builder = lir.IRBuilder(hiq__ngqlb.append_basic_block())
    scpok__xwvk = hiq__ngqlb.args[0]
    mnf__cuhqk = context.get_value_type(payload_type).as_pointer()
    jbtl__chh = builder.bitcast(scpok__xwvk, mnf__cuhqk)
    hsbr__avb = context.make_helper(builder, payload_type, ref=jbtl__chh)
    context.nrt.decref(builder, array_item_type.dtype, hsbr__avb.data)
    context.nrt.decref(builder, types.Array(offset_type, 1, 'C'), hsbr__avb
        .offsets)
    context.nrt.decref(builder, types.Array(types.uint8, 1, 'C'), hsbr__avb
        .null_bitmap)
    builder.ret_void()
    return hiq__ngqlb


def construct_array_item_array(context, builder, array_item_type, n_arrays,
    n_elems, c=None):
    payload_type = ArrayItemArrayPayloadType(array_item_type)
    qsa__tkm = context.get_value_type(payload_type)
    ddib__whsa = context.get_abi_sizeof(qsa__tkm)
    atch__eucxn = define_array_item_dtor(context, builder, array_item_type,
        payload_type)
    dykgo__lrh = context.nrt.meminfo_alloc_dtor(builder, context.
        get_constant(types.uintp, ddib__whsa), atch__eucxn)
    igdia__ykkx = context.nrt.meminfo_data(builder, dykgo__lrh)
    pyg__vmn = builder.bitcast(igdia__ykkx, qsa__tkm.as_pointer())
    hsbr__avb = cgutils.create_struct_proxy(payload_type)(context, builder)
    hsbr__avb.n_arrays = n_arrays
    gma__xfb = n_elems.type.count
    djsu__pjmy = builder.extract_value(n_elems, 0)
    utnhj__qhqca = cgutils.alloca_once_value(builder, djsu__pjmy)
    ydyc__mpamo = builder.icmp_signed('==', djsu__pjmy, lir.Constant(
        djsu__pjmy.type, -1))
    with builder.if_then(ydyc__mpamo):
        builder.store(n_arrays, utnhj__qhqca)
    n_elems = cgutils.pack_array(builder, [builder.load(utnhj__qhqca)] + [
        builder.extract_value(n_elems, nbit__inwo) for nbit__inwo in range(
        1, gma__xfb)])
    hsbr__avb.data = gen_allocate_array(context, builder, array_item_type.
        dtype, n_elems, c)
    yxzih__ipf = builder.add(n_arrays, lir.Constant(lir.IntType(64), 1))
    igxie__dixy = bodo.utils.utils._empty_nd_impl(context, builder, types.
        Array(offset_type, 1, 'C'), [yxzih__ipf])
    offsets_ptr = igxie__dixy.data
    builder.store(context.get_constant(offset_type, 0), offsets_ptr)
    builder.store(builder.trunc(builder.extract_value(n_elems, 0), lir.
        IntType(offset_type.bitwidth)), builder.gep(offsets_ptr, [n_arrays]))
    hsbr__avb.offsets = igxie__dixy._getvalue()
    pur__ffaz = builder.udiv(builder.add(n_arrays, lir.Constant(lir.IntType
        (64), 7)), lir.Constant(lir.IntType(64), 8))
    lkj__bzln = bodo.utils.utils._empty_nd_impl(context, builder, types.
        Array(types.uint8, 1, 'C'), [pur__ffaz])
    null_bitmap_ptr = lkj__bzln.data
    hsbr__avb.null_bitmap = lkj__bzln._getvalue()
    builder.store(hsbr__avb._getvalue(), pyg__vmn)
    return dykgo__lrh, hsbr__avb.data, offsets_ptr, null_bitmap_ptr


def _unbox_array_item_array_copy_data(arr_typ, arr_obj, c, data_arr,
    item_ind, n_items):
    context = c.context
    builder = c.builder
    arr_obj = to_arr_obj_if_list_obj(c, context, builder, arr_obj, arr_typ)
    arr_val = c.pyapi.to_native_value(arr_typ, arr_obj).value
    sig = types.none(arr_typ, types.int64, types.int64, arr_typ)

    def copy_data(data_arr, item_ind, n_items, arr_val):
        data_arr[item_ind:item_ind + n_items] = arr_val
    cjn__dkrc, glut__ieeq = c.pyapi.call_jit_code(copy_data, sig, [data_arr,
        item_ind, n_items, arr_val])
    c.context.nrt.decref(builder, arr_typ, arr_val)


def _unbox_array_item_array_generic(typ, val, c, n_arrays, data_arr,
    offsets_ptr, null_bitmap_ptr):
    context = c.context
    builder = c.builder
    stbdh__whkm = context.insert_const_string(builder.module, 'pandas')
    vpsx__dfz = c.pyapi.import_module_noblock(stbdh__whkm)
    oxlk__bhkv = c.pyapi.object_getattr_string(vpsx__dfz, 'NA')
    jznty__mwq = c.context.get_constant(offset_type, 0)
    builder.store(jznty__mwq, offsets_ptr)
    incgu__fwqar = cgutils.alloca_once_value(builder, context.get_constant(
        types.int64, 0))
    with cgutils.for_range(builder, n_arrays) as eztq__xdogn:
        gun__cmh = eztq__xdogn.index
        item_ind = builder.load(incgu__fwqar)
        builder.store(builder.trunc(item_ind, lir.IntType(offset_type.
            bitwidth)), builder.gep(offsets_ptr, [gun__cmh]))
        arr_obj = seq_getitem(builder, context, val, gun__cmh)
        set_bitmap_bit(builder, null_bitmap_ptr, gun__cmh, 0)
        mez__deau = is_na_value(builder, context, arr_obj, oxlk__bhkv)
        uzzw__xrc = builder.icmp_unsigned('!=', mez__deau, lir.Constant(
            mez__deau.type, 1))
        with builder.if_then(uzzw__xrc):
            set_bitmap_bit(builder, null_bitmap_ptr, gun__cmh, 1)
            n_items = bodo.utils.utils.object_length(c, arr_obj)
            _unbox_array_item_array_copy_data(typ.dtype, arr_obj, c,
                data_arr, item_ind, n_items)
            builder.store(builder.add(item_ind, n_items), incgu__fwqar)
        c.pyapi.decref(arr_obj)
    builder.store(builder.trunc(builder.load(incgu__fwqar), lir.IntType(
        offset_type.bitwidth)), builder.gep(offsets_ptr, [n_arrays]))
    c.pyapi.decref(vpsx__dfz)
    c.pyapi.decref(oxlk__bhkv)


@unbox(ArrayItemArrayType)
def unbox_array_item_array(typ, val, c):
    zdjw__gci = isinstance(typ.dtype, types.Array) and typ.dtype.dtype in (
        types.int64, types.float64, types.bool_, datetime_date_type)
    n_arrays = bodo.utils.utils.object_length(c, val)
    if zdjw__gci:
        txzj__khwaa = lir.FunctionType(lir.IntType(64), [lir.IntType(8).
            as_pointer()])
        zlwq__ymco = cgutils.get_or_insert_function(c.builder.module,
            txzj__khwaa, name='count_total_elems_list_array')
        n_elems = cgutils.pack_array(c.builder, [c.builder.call(zlwq__ymco,
            [val])])
    else:
        wfgi__fuod = get_array_elem_counts(c, c.builder, c.context, val, typ)
        n_elems = cgutils.pack_array(c.builder, [c.builder.extract_value(
            wfgi__fuod, nbit__inwo) for nbit__inwo in range(1, wfgi__fuod.
            type.count)])
    dykgo__lrh, data_arr, offsets_ptr, null_bitmap_ptr = (
        construct_array_item_array(c.context, c.builder, typ, n_arrays,
        n_elems, c))
    if zdjw__gci:
        tvux__kooqk = bodo.utils.utils.numba_to_c_type(typ.dtype.dtype)
        ouade__scuj = c.context.make_array(typ.dtype)(c.context, c.builder,
            data_arr).data
        txzj__khwaa = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(
            offset_type.bitwidth).as_pointer(), lir.IntType(8).as_pointer(),
            lir.IntType(32)])
        hiq__ngqlb = cgutils.get_or_insert_function(c.builder.module,
            txzj__khwaa, name='array_item_array_from_sequence')
        c.builder.call(hiq__ngqlb, [val, c.builder.bitcast(ouade__scuj, lir
            .IntType(8).as_pointer()), offsets_ptr, null_bitmap_ptr, lir.
            Constant(lir.IntType(32), tvux__kooqk)])
    else:
        _unbox_array_item_array_generic(typ, val, c, n_arrays, data_arr,
            offsets_ptr, null_bitmap_ptr)
    ntpxp__boue = c.context.make_helper(c.builder, typ)
    ntpxp__boue.meminfo = dykgo__lrh
    bylql__bnsp = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(ntpxp__boue._getvalue(), is_error=bylql__bnsp)


def _get_array_item_arr_payload(context, builder, arr_typ, arr):
    ntpxp__boue = context.make_helper(builder, arr_typ, arr)
    payload_type = ArrayItemArrayPayloadType(arr_typ)
    igdia__ykkx = context.nrt.meminfo_data(builder, ntpxp__boue.meminfo)
    pyg__vmn = builder.bitcast(igdia__ykkx, context.get_value_type(
        payload_type).as_pointer())
    hsbr__avb = cgutils.create_struct_proxy(payload_type)(context, builder,
        builder.load(pyg__vmn))
    return hsbr__avb


def _box_array_item_array_generic(typ, c, n_arrays, data_arr, offsets_ptr,
    null_bitmap_ptr):
    context = c.context
    builder = c.builder
    stbdh__whkm = context.insert_const_string(builder.module, 'numpy')
    zhuf__cnaa = c.pyapi.import_module_noblock(stbdh__whkm)
    adabl__gwq = c.pyapi.object_getattr_string(zhuf__cnaa, 'object_')
    fxn__plk = c.pyapi.long_from_longlong(n_arrays)
    ojy__yrim = c.pyapi.call_method(zhuf__cnaa, 'ndarray', (fxn__plk,
        adabl__gwq))
    zsh__efud = c.pyapi.object_getattr_string(zhuf__cnaa, 'nan')
    incgu__fwqar = cgutils.alloca_once_value(builder, lir.Constant(lir.
        IntType(64), 0))
    with cgutils.for_range(builder, n_arrays) as eztq__xdogn:
        gun__cmh = eztq__xdogn.index
        pyarray_setitem(builder, context, ojy__yrim, gun__cmh, zsh__efud)
        rfki__wszu = get_bitmap_bit(builder, null_bitmap_ptr, gun__cmh)
        blq__wdoal = builder.icmp_unsigned('!=', rfki__wszu, lir.Constant(
            lir.IntType(8), 0))
        with builder.if_then(blq__wdoal):
            n_items = builder.sext(builder.sub(builder.load(builder.gep(
                offsets_ptr, [builder.add(gun__cmh, lir.Constant(gun__cmh.
                type, 1))])), builder.load(builder.gep(offsets_ptr, [
                gun__cmh]))), lir.IntType(64))
            item_ind = builder.load(incgu__fwqar)
            cjn__dkrc, jyr__slv = c.pyapi.call_jit_code(lambda data_arr,
                item_ind, n_items: data_arr[item_ind:item_ind + n_items],
                typ.dtype(typ.dtype, types.int64, types.int64), [data_arr,
                item_ind, n_items])
            builder.store(builder.add(item_ind, n_items), incgu__fwqar)
            arr_obj = c.pyapi.from_native_value(typ.dtype, jyr__slv, c.
                env_manager)
            pyarray_setitem(builder, context, ojy__yrim, gun__cmh, arr_obj)
            c.pyapi.decref(arr_obj)
    c.pyapi.decref(zhuf__cnaa)
    c.pyapi.decref(adabl__gwq)
    c.pyapi.decref(fxn__plk)
    c.pyapi.decref(zsh__efud)
    return ojy__yrim


@box(ArrayItemArrayType)
def box_array_item_arr(typ, val, c):
    hsbr__avb = _get_array_item_arr_payload(c.context, c.builder, typ, val)
    data_arr = hsbr__avb.data
    offsets_ptr = c.context.make_helper(c.builder, types.Array(offset_type,
        1, 'C'), hsbr__avb.offsets).data
    null_bitmap_ptr = c.context.make_helper(c.builder, types.Array(types.
        uint8, 1, 'C'), hsbr__avb.null_bitmap).data
    if isinstance(typ.dtype, types.Array) and typ.dtype.dtype in (types.
        int64, types.float64, types.bool_, datetime_date_type):
        tvux__kooqk = bodo.utils.utils.numba_to_c_type(typ.dtype.dtype)
        ouade__scuj = c.context.make_helper(c.builder, typ.dtype, data_arr
            ).data
        txzj__khwaa = lir.FunctionType(c.context.get_argument_type(types.
            pyobject), [lir.IntType(64), lir.IntType(8).as_pointer(), lir.
            IntType(offset_type.bitwidth).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(32)])
        kcceo__rqs = cgutils.get_or_insert_function(c.builder.module,
            txzj__khwaa, name='np_array_from_array_item_array')
        arr = c.builder.call(kcceo__rqs, [hsbr__avb.n_arrays, c.builder.
            bitcast(ouade__scuj, lir.IntType(8).as_pointer()), offsets_ptr,
            null_bitmap_ptr, lir.Constant(lir.IntType(32), tvux__kooqk)])
    else:
        arr = _box_array_item_array_generic(typ, c, hsbr__avb.n_arrays,
            data_arr, offsets_ptr, null_bitmap_ptr)
    c.context.nrt.decref(c.builder, typ, val)
    return arr


def lower_pre_alloc_array_item_array(context, builder, sig, args):
    array_item_type = sig.return_type
    gyt__ugdf, lkwl__hspiw, hpyri__ilu = args
    frj__frne = bodo.utils.transform.get_type_alloc_counts(array_item_type.
        dtype)
    qalwa__ojuy = sig.args[1]
    if not isinstance(qalwa__ojuy, types.UniTuple):
        lkwl__hspiw = cgutils.pack_array(builder, [lir.Constant(lir.IntType
            (64), -1) for hpyri__ilu in range(frj__frne)])
    elif qalwa__ojuy.count < frj__frne:
        lkwl__hspiw = cgutils.pack_array(builder, [builder.extract_value(
            lkwl__hspiw, nbit__inwo) for nbit__inwo in range(qalwa__ojuy.
            count)] + [lir.Constant(lir.IntType(64), -1) for hpyri__ilu in
            range(frj__frne - qalwa__ojuy.count)])
    dykgo__lrh, hpyri__ilu, hpyri__ilu, hpyri__ilu = (
        construct_array_item_array(context, builder, array_item_type,
        gyt__ugdf, lkwl__hspiw))
    ntpxp__boue = context.make_helper(builder, array_item_type)
    ntpxp__boue.meminfo = dykgo__lrh
    return ntpxp__boue._getvalue()


@intrinsic
def pre_alloc_array_item_array(typingctx, num_arrs_typ, num_values_typ,
    dtype_typ=None):
    assert isinstance(num_arrs_typ, types.Integer)
    array_item_type = ArrayItemArrayType(dtype_typ.instance_type)
    num_values_typ = types.unliteral(num_values_typ)
    return array_item_type(types.int64, num_values_typ, dtype_typ
        ), lower_pre_alloc_array_item_array


def pre_alloc_array_item_array_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 3 and not kws
    return ArrayAnalysis.AnalyzeResult(shape=args[0], pre=[])


(ArrayAnalysis.
    _analyze_op_call_bodo_libs_array_item_arr_ext_pre_alloc_array_item_array
    ) = pre_alloc_array_item_array_equiv


def init_array_item_array_codegen(context, builder, signature, args):
    n_arrays, fepz__bxe, igxie__dixy, lkj__bzln = args
    array_item_type = signature.return_type
    payload_type = ArrayItemArrayPayloadType(array_item_type)
    qsa__tkm = context.get_value_type(payload_type)
    ddib__whsa = context.get_abi_sizeof(qsa__tkm)
    atch__eucxn = define_array_item_dtor(context, builder, array_item_type,
        payload_type)
    dykgo__lrh = context.nrt.meminfo_alloc_dtor(builder, context.
        get_constant(types.uintp, ddib__whsa), atch__eucxn)
    igdia__ykkx = context.nrt.meminfo_data(builder, dykgo__lrh)
    pyg__vmn = builder.bitcast(igdia__ykkx, qsa__tkm.as_pointer())
    hsbr__avb = cgutils.create_struct_proxy(payload_type)(context, builder)
    hsbr__avb.n_arrays = n_arrays
    hsbr__avb.data = fepz__bxe
    hsbr__avb.offsets = igxie__dixy
    hsbr__avb.null_bitmap = lkj__bzln
    builder.store(hsbr__avb._getvalue(), pyg__vmn)
    context.nrt.incref(builder, signature.args[1], fepz__bxe)
    context.nrt.incref(builder, signature.args[2], igxie__dixy)
    context.nrt.incref(builder, signature.args[3], lkj__bzln)
    ntpxp__boue = context.make_helper(builder, array_item_type)
    ntpxp__boue.meminfo = dykgo__lrh
    return ntpxp__boue._getvalue()


@intrinsic
def init_array_item_array(typingctx, n_arrays_typ, data_type, offsets_typ,
    null_bitmap_typ=None):
    assert null_bitmap_typ == types.Array(types.uint8, 1, 'C')
    gsedb__bcv = ArrayItemArrayType(data_type)
    sig = gsedb__bcv(types.int64, data_type, offsets_typ, null_bitmap_typ)
    return sig, init_array_item_array_codegen


@intrinsic
def get_offsets(typingctx, arr_typ=None):
    assert isinstance(arr_typ, ArrayItemArrayType)

    def codegen(context, builder, sig, args):
        arr, = args
        hsbr__avb = _get_array_item_arr_payload(context, builder, arr_typ, arr)
        return impl_ret_borrowed(context, builder, sig.return_type,
            hsbr__avb.offsets)
    return types.Array(offset_type, 1, 'C')(arr_typ), codegen


@intrinsic
def get_offsets_ind(typingctx, arr_typ, ind_t=None):
    assert isinstance(arr_typ, ArrayItemArrayType)

    def codegen(context, builder, sig, args):
        arr, ind = args
        hsbr__avb = _get_array_item_arr_payload(context, builder, arr_typ, arr)
        ouade__scuj = context.make_array(types.Array(offset_type, 1, 'C'))(
            context, builder, hsbr__avb.offsets).data
        igxie__dixy = builder.bitcast(ouade__scuj, lir.IntType(offset_type.
            bitwidth).as_pointer())
        return builder.load(builder.gep(igxie__dixy, [ind]))
    return offset_type(arr_typ, types.int64), codegen


@intrinsic
def get_data(typingctx, arr_typ=None):
    assert isinstance(arr_typ, ArrayItemArrayType)

    def codegen(context, builder, sig, args):
        arr, = args
        hsbr__avb = _get_array_item_arr_payload(context, builder, arr_typ, arr)
        return impl_ret_borrowed(context, builder, sig.return_type,
            hsbr__avb.data)
    return arr_typ.dtype(arr_typ), codegen


@intrinsic
def get_null_bitmap(typingctx, arr_typ=None):
    assert isinstance(arr_typ, ArrayItemArrayType)

    def codegen(context, builder, sig, args):
        arr, = args
        hsbr__avb = _get_array_item_arr_payload(context, builder, arr_typ, arr)
        return impl_ret_borrowed(context, builder, sig.return_type,
            hsbr__avb.null_bitmap)
    return types.Array(types.uint8, 1, 'C')(arr_typ), codegen


def alias_ext_single_array(lhs_name, args, alias_map, arg_aliases):
    assert len(args) == 1
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)


numba.core.ir_utils.alias_func_extensions['get_offsets',
    'bodo.libs.array_item_arr_ext'] = alias_ext_single_array
numba.core.ir_utils.alias_func_extensions['get_data',
    'bodo.libs.array_item_arr_ext'] = alias_ext_single_array
numba.core.ir_utils.alias_func_extensions['get_null_bitmap',
    'bodo.libs.array_item_arr_ext'] = alias_ext_single_array


@intrinsic
def get_n_arrays(typingctx, arr_typ=None):
    assert isinstance(arr_typ, ArrayItemArrayType)

    def codegen(context, builder, sig, args):
        arr, = args
        hsbr__avb = _get_array_item_arr_payload(context, builder, arr_typ, arr)
        return hsbr__avb.n_arrays
    return types.int64(arr_typ), codegen


@intrinsic
def replace_data_arr(typingctx, arr_typ, data_typ=None):
    assert isinstance(arr_typ, ArrayItemArrayType
        ) and data_typ == arr_typ.dtype

    def codegen(context, builder, sig, args):
        arr, ohkmt__qil = args
        ntpxp__boue = context.make_helper(builder, arr_typ, arr)
        payload_type = ArrayItemArrayPayloadType(arr_typ)
        igdia__ykkx = context.nrt.meminfo_data(builder, ntpxp__boue.meminfo)
        pyg__vmn = builder.bitcast(igdia__ykkx, context.get_value_type(
            payload_type).as_pointer())
        hsbr__avb = cgutils.create_struct_proxy(payload_type)(context,
            builder, builder.load(pyg__vmn))
        context.nrt.decref(builder, data_typ, hsbr__avb.data)
        hsbr__avb.data = ohkmt__qil
        context.nrt.incref(builder, data_typ, ohkmt__qil)
        builder.store(hsbr__avb._getvalue(), pyg__vmn)
    return types.none(arr_typ, data_typ), codegen


@numba.njit(no_cpython_wrapper=True)
def ensure_data_capacity(arr, old_size, new_size):
    fepz__bxe = get_data(arr)
    jcxa__zatut = len(fepz__bxe)
    if jcxa__zatut < new_size:
        sewe__llv = max(2 * jcxa__zatut, new_size)
        ohkmt__qil = bodo.libs.array_kernels.resize_and_copy(fepz__bxe,
            old_size, sewe__llv)
        replace_data_arr(arr, ohkmt__qil)


@numba.njit(no_cpython_wrapper=True)
def trim_excess_data(arr):
    fepz__bxe = get_data(arr)
    igxie__dixy = get_offsets(arr)
    mtzsx__ykpmr = len(fepz__bxe)
    nur__xfxzc = igxie__dixy[-1]
    if mtzsx__ykpmr != nur__xfxzc:
        ohkmt__qil = bodo.libs.array_kernels.resize_and_copy(fepz__bxe,
            nur__xfxzc, nur__xfxzc)
        replace_data_arr(arr, ohkmt__qil)


@overload(len, no_unliteral=True)
def overload_array_item_arr_len(A):
    if isinstance(A, ArrayItemArrayType):
        return lambda A: get_n_arrays(A)


@overload_attribute(ArrayItemArrayType, 'shape')
def overload_array_item_arr_shape(A):
    return lambda A: (get_n_arrays(A),)


@overload_attribute(ArrayItemArrayType, 'dtype')
def overload_array_item_arr_dtype(A):
    return lambda A: np.object_


@overload_attribute(ArrayItemArrayType, 'ndim')
def overload_array_item_arr_ndim(A):
    return lambda A: 1


@overload_attribute(ArrayItemArrayType, 'nbytes')
def overload_array_item_arr_nbytes(A):
    return lambda A: get_data(A).nbytes + get_offsets(A
        ).nbytes + get_null_bitmap(A).nbytes


@overload(operator.getitem, no_unliteral=True)
def array_item_arr_getitem_array(arr, ind):
    if not isinstance(arr, ArrayItemArrayType):
        return
    if isinstance(ind, types.Integer):

        def array_item_arr_getitem_impl(arr, ind):
            if ind < 0:
                ind += len(arr)
            igxie__dixy = get_offsets(arr)
            fepz__bxe = get_data(arr)
            bqx__eggti = igxie__dixy[ind]
            yxe__cpt = igxie__dixy[ind + 1]
            return fepz__bxe[bqx__eggti:yxe__cpt]
        return array_item_arr_getitem_impl
    if ind != bodo.boolean_array and is_list_like_index_type(ind
        ) and ind.dtype == types.bool_:
        qwl__dvv = arr.dtype

        def impl_bool(arr, ind):
            gzpa__hoz = len(arr)
            if gzpa__hoz != len(ind):
                raise IndexError(
                    'boolean index did not match indexed array along dimension 0'
                    )
            lkj__bzln = get_null_bitmap(arr)
            n_arrays = 0
            yxoai__jmlz = init_nested_counts(qwl__dvv)
            for nbit__inwo in range(gzpa__hoz):
                if ind[nbit__inwo]:
                    n_arrays += 1
                    opl__nsgv = arr[nbit__inwo]
                    yxoai__jmlz = add_nested_counts(yxoai__jmlz, opl__nsgv)
            ojy__yrim = pre_alloc_array_item_array(n_arrays, yxoai__jmlz,
                qwl__dvv)
            dsn__btzva = get_null_bitmap(ojy__yrim)
            cnko__aouz = 0
            for boytr__swxn in range(gzpa__hoz):
                if ind[boytr__swxn]:
                    ojy__yrim[cnko__aouz] = arr[boytr__swxn]
                    kco__fcj = bodo.libs.int_arr_ext.get_bit_bitmap_arr(
                        lkj__bzln, boytr__swxn)
                    bodo.libs.int_arr_ext.set_bit_to_arr(dsn__btzva,
                        cnko__aouz, kco__fcj)
                    cnko__aouz += 1
            return ojy__yrim
        return impl_bool
    if is_list_like_index_type(ind) and isinstance(ind.dtype, types.Integer):
        qwl__dvv = arr.dtype

        def impl_int(arr, ind):
            lkj__bzln = get_null_bitmap(arr)
            gzpa__hoz = len(ind)
            n_arrays = gzpa__hoz
            yxoai__jmlz = init_nested_counts(qwl__dvv)
            for igt__eamr in range(gzpa__hoz):
                nbit__inwo = ind[igt__eamr]
                opl__nsgv = arr[nbit__inwo]
                yxoai__jmlz = add_nested_counts(yxoai__jmlz, opl__nsgv)
            ojy__yrim = pre_alloc_array_item_array(n_arrays, yxoai__jmlz,
                qwl__dvv)
            dsn__btzva = get_null_bitmap(ojy__yrim)
            for qha__rmbej in range(gzpa__hoz):
                boytr__swxn = ind[qha__rmbej]
                ojy__yrim[qha__rmbej] = arr[boytr__swxn]
                kco__fcj = bodo.libs.int_arr_ext.get_bit_bitmap_arr(lkj__bzln,
                    boytr__swxn)
                bodo.libs.int_arr_ext.set_bit_to_arr(dsn__btzva, qha__rmbej,
                    kco__fcj)
            return ojy__yrim
        return impl_int
    if isinstance(ind, types.SliceType):

        def impl_slice(arr, ind):
            gzpa__hoz = len(arr)
            rhsd__kpbgu = numba.cpython.unicode._normalize_slice(ind, gzpa__hoz
                )
            hsuhx__cuy = np.arange(rhsd__kpbgu.start, rhsd__kpbgu.stop,
                rhsd__kpbgu.step)
            return arr[hsuhx__cuy]
        return impl_slice


@overload(operator.setitem)
def array_item_arr_setitem(A, idx, val):
    if not isinstance(A, ArrayItemArrayType):
        return
    if isinstance(idx, types.Integer):

        def impl_scalar(A, idx, val):
            igxie__dixy = get_offsets(A)
            lkj__bzln = get_null_bitmap(A)
            if idx == 0:
                igxie__dixy[0] = 0
            n_items = len(val)
            caz__frdn = igxie__dixy[idx] + n_items
            ensure_data_capacity(A, igxie__dixy[idx], caz__frdn)
            fepz__bxe = get_data(A)
            igxie__dixy[idx + 1] = igxie__dixy[idx] + n_items
            fepz__bxe[igxie__dixy[idx]:igxie__dixy[idx + 1]] = val
            bodo.libs.int_arr_ext.set_bit_to_arr(lkj__bzln, idx, 1)
        return impl_scalar
    if isinstance(idx, types.SliceType) and A.dtype == val:

        def impl_slice_elem(A, idx, val):
            rhsd__kpbgu = numba.cpython.unicode._normalize_slice(idx, len(A))
            for nbit__inwo in range(rhsd__kpbgu.start, rhsd__kpbgu.stop,
                rhsd__kpbgu.step):
                A[nbit__inwo] = val
        return impl_slice_elem
    if isinstance(idx, types.SliceType) and is_iterable_type(val):

        def impl_slice(A, idx, val):
            val = bodo.utils.conversion.coerce_to_array(val,
                use_nullable_array=True)
            igxie__dixy = get_offsets(A)
            lkj__bzln = get_null_bitmap(A)
            xaxh__ged = get_offsets(val)
            vjjn__pxr = get_data(val)
            fahe__lqd = get_null_bitmap(val)
            gzpa__hoz = len(A)
            rhsd__kpbgu = numba.cpython.unicode._normalize_slice(idx, gzpa__hoz
                )
            ybom__jxe, aiez__eknrv = rhsd__kpbgu.start, rhsd__kpbgu.stop
            assert rhsd__kpbgu.step == 1
            if ybom__jxe == 0:
                igxie__dixy[ybom__jxe] = 0
            gzd__wssl = igxie__dixy[ybom__jxe]
            caz__frdn = gzd__wssl + len(vjjn__pxr)
            ensure_data_capacity(A, gzd__wssl, caz__frdn)
            fepz__bxe = get_data(A)
            fepz__bxe[gzd__wssl:gzd__wssl + len(vjjn__pxr)] = vjjn__pxr
            igxie__dixy[ybom__jxe:aiez__eknrv + 1] = xaxh__ged + gzd__wssl
            ova__gqb = 0
            for nbit__inwo in range(ybom__jxe, aiez__eknrv):
                kco__fcj = bodo.libs.int_arr_ext.get_bit_bitmap_arr(fahe__lqd,
                    ova__gqb)
                bodo.libs.int_arr_ext.set_bit_to_arr(lkj__bzln, nbit__inwo,
                    kco__fcj)
                ova__gqb += 1
        return impl_slice
    raise BodoError(
        'only setitem with scalar index is currently supported for list arrays'
        )


@overload_method(ArrayItemArrayType, 'copy', no_unliteral=True)
def overload_array_item_arr_copy(A):

    def copy_impl(A):
        return init_array_item_array(len(A), get_data(A).copy(),
            get_offsets(A).copy(), get_null_bitmap(A).copy())
    return copy_impl
