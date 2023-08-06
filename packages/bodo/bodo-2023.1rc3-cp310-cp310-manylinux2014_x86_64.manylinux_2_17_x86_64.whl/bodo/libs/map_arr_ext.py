"""Array implementation for map values.
Corresponds to Spark's MapType: https://spark.apache.org/docs/latest/sql-reference.html
Corresponds to Arrow's Map arrays: https://github.com/apache/arrow/blob/master/format/Schema.fbs

The implementation uses an array(struct) array underneath similar to Spark and Arrow.
For example: [{1: 2.1, 3: 1.1}, {5: -1.0}]
[[{"key": 1, "value" 2.1}, {"key": 3, "value": 1.1}], [{"key": 5, "value": -1.0}]]
"""
import operator
import llvmlite.binding as ll
import numba
import numpy as np
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.extending import NativeValue, box, intrinsic, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_model, unbox
from numba.parfors.array_analysis import ArrayAnalysis
import bodo
from bodo.hiframes.datetime_date_ext import datetime_date_type
from bodo.libs.array_item_arr_ext import ArrayItemArrayType, _get_array_item_arr_payload, offset_type
from bodo.libs.struct_arr_ext import StructArrayType, _get_struct_arr_payload
from bodo.utils.cg_helpers import dict_keys, dict_merge_from_seq2, dict_values, gen_allocate_array, get_array_elem_counts, get_bitmap_bit, is_na_value, pyarray_setitem, seq_getitem, set_bitmap_bit
from bodo.utils.typing import BodoError
from bodo.libs import array_ext, hdist
ll.add_symbol('count_total_elems_list_array', array_ext.
    count_total_elems_list_array)
ll.add_symbol('map_array_from_sequence', array_ext.map_array_from_sequence)
ll.add_symbol('np_array_from_map_array', array_ext.np_array_from_map_array)


class MapArrayType(types.ArrayCompatible):

    def __init__(self, key_arr_type, value_arr_type):
        self.key_arr_type = key_arr_type
        self.value_arr_type = value_arr_type
        super(MapArrayType, self).__init__(name='MapArrayType({}, {})'.
            format(key_arr_type, value_arr_type))

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    @property
    def dtype(self):
        return types.DictType(self.key_arr_type.dtype, self.value_arr_type.
            dtype)

    def copy(self):
        return MapArrayType(self.key_arr_type, self.value_arr_type)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


def _get_map_arr_data_type(map_type):
    nhirs__owyk = StructArrayType((map_type.key_arr_type, map_type.
        value_arr_type), ('key', 'value'))
    return ArrayItemArrayType(nhirs__owyk)


@register_model(MapArrayType)
class MapArrayModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        gpqwk__wnf = _get_map_arr_data_type(fe_type)
        aovqg__bucjk = [('data', gpqwk__wnf)]
        models.StructModel.__init__(self, dmm, fe_type, aovqg__bucjk)


make_attribute_wrapper(MapArrayType, 'data', '_data')


@unbox(MapArrayType)
def unbox_map_array(typ, val, c):
    n_maps = bodo.utils.utils.object_length(c, val)
    ikwvt__lpak = all(isinstance(wkon__qeejq, types.Array) and wkon__qeejq.
        dtype in (types.int64, types.float64, types.bool_,
        datetime_date_type) for wkon__qeejq in (typ.key_arr_type, typ.
        value_arr_type))
    if ikwvt__lpak:
        whbjj__zgtaj = lir.FunctionType(lir.IntType(64), [lir.IntType(8).
            as_pointer()])
        xefa__adlmf = cgutils.get_or_insert_function(c.builder.module,
            whbjj__zgtaj, name='count_total_elems_list_array')
        lzgms__nhoig = cgutils.pack_array(c.builder, [n_maps, c.builder.
            call(xefa__adlmf, [val])])
    else:
        lzgms__nhoig = get_array_elem_counts(c, c.builder, c.context, val, typ)
    gpqwk__wnf = _get_map_arr_data_type(typ)
    data_arr = gen_allocate_array(c.context, c.builder, gpqwk__wnf,
        lzgms__nhoig, c)
    etgm__qgoc = _get_array_item_arr_payload(c.context, c.builder,
        gpqwk__wnf, data_arr)
    null_bitmap_ptr = c.context.make_array(types.Array(types.uint8, 1, 'C'))(c
        .context, c.builder, etgm__qgoc.null_bitmap).data
    offsets_ptr = c.context.make_array(types.Array(offset_type, 1, 'C'))(c.
        context, c.builder, etgm__qgoc.offsets).data
    avxwz__ytrnh = _get_struct_arr_payload(c.context, c.builder, gpqwk__wnf
        .dtype, etgm__qgoc.data)
    key_arr = c.builder.extract_value(avxwz__ytrnh.data, 0)
    value_arr = c.builder.extract_value(avxwz__ytrnh.data, 1)
    sig = types.none(types.Array(types.uint8, 1, 'C'))
    yddn__yru, kvb__llo = c.pyapi.call_jit_code(lambda A: A.fill(255), sig,
        [avxwz__ytrnh.null_bitmap])
    if ikwvt__lpak:
        quoe__dko = c.context.make_array(gpqwk__wnf.dtype.data[0])(c.
            context, c.builder, key_arr).data
        rycds__ltosv = c.context.make_array(gpqwk__wnf.dtype.data[1])(c.
            context, c.builder, value_arr).data
        whbjj__zgtaj = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(offset_type.bitwidth).as_pointer(),
            lir.IntType(8).as_pointer(), lir.IntType(32), lir.IntType(32)])
        vitj__dpoim = cgutils.get_or_insert_function(c.builder.module,
            whbjj__zgtaj, name='map_array_from_sequence')
        fsa__cgv = bodo.utils.utils.numba_to_c_type(typ.key_arr_type.dtype)
        wmjtn__cfp = bodo.utils.utils.numba_to_c_type(typ.value_arr_type.dtype)
        c.builder.call(vitj__dpoim, [val, c.builder.bitcast(quoe__dko, lir.
            IntType(8).as_pointer()), c.builder.bitcast(rycds__ltosv, lir.
            IntType(8).as_pointer()), offsets_ptr, null_bitmap_ptr, lir.
            Constant(lir.IntType(32), fsa__cgv), lir.Constant(lir.IntType(
            32), wmjtn__cfp)])
    else:
        _unbox_map_array_generic(typ, val, c, n_maps, key_arr, value_arr,
            offsets_ptr, null_bitmap_ptr)
    kjw__dwrcd = c.context.make_helper(c.builder, typ)
    kjw__dwrcd.data = data_arr
    rul__tzr = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(kjw__dwrcd._getvalue(), is_error=rul__tzr)


def _unbox_map_array_generic(typ, val, c, n_maps, key_arr, value_arr,
    offsets_ptr, null_bitmap_ptr):
    from bodo.libs.array_item_arr_ext import _unbox_array_item_array_copy_data
    context = c.context
    builder = c.builder
    hysq__egpdi = context.insert_const_string(builder.module, 'pandas')
    tfv__bnycz = c.pyapi.import_module_noblock(hysq__egpdi)
    tnlp__jyu = c.pyapi.object_getattr_string(tfv__bnycz, 'NA')
    xdaef__jwpjs = c.context.get_constant(offset_type, 0)
    builder.store(xdaef__jwpjs, offsets_ptr)
    qokkc__ezfaz = cgutils.alloca_once_value(builder, context.get_constant(
        types.int64, 0))
    with cgutils.for_range(builder, n_maps) as cpol__urtr:
        tbgw__jbnea = cpol__urtr.index
        item_ind = builder.load(qokkc__ezfaz)
        builder.store(builder.trunc(item_ind, lir.IntType(offset_type.
            bitwidth)), builder.gep(offsets_ptr, [tbgw__jbnea]))
        ujkg__xbz = seq_getitem(builder, context, val, tbgw__jbnea)
        set_bitmap_bit(builder, null_bitmap_ptr, tbgw__jbnea, 0)
        dtbi__upkq = is_na_value(builder, context, ujkg__xbz, tnlp__jyu)
        zmcwy__jiwbw = builder.icmp_unsigned('!=', dtbi__upkq, lir.Constant
            (dtbi__upkq.type, 1))
        with builder.if_then(zmcwy__jiwbw):
            set_bitmap_bit(builder, null_bitmap_ptr, tbgw__jbnea, 1)
            wics__jbb = dict_keys(builder, context, ujkg__xbz)
            osvw__ncet = dict_values(builder, context, ujkg__xbz)
            n_items = bodo.utils.utils.object_length(c, wics__jbb)
            _unbox_array_item_array_copy_data(typ.key_arr_type, wics__jbb,
                c, key_arr, item_ind, n_items)
            _unbox_array_item_array_copy_data(typ.value_arr_type,
                osvw__ncet, c, value_arr, item_ind, n_items)
            builder.store(builder.add(item_ind, n_items), qokkc__ezfaz)
            c.pyapi.decref(wics__jbb)
            c.pyapi.decref(osvw__ncet)
        c.pyapi.decref(ujkg__xbz)
    builder.store(builder.trunc(builder.load(qokkc__ezfaz), lir.IntType(
        offset_type.bitwidth)), builder.gep(offsets_ptr, [n_maps]))
    c.pyapi.decref(tfv__bnycz)
    c.pyapi.decref(tnlp__jyu)


@box(MapArrayType)
def box_map_arr(typ, val, c):
    kjw__dwrcd = c.context.make_helper(c.builder, typ, val)
    data_arr = kjw__dwrcd.data
    gpqwk__wnf = _get_map_arr_data_type(typ)
    etgm__qgoc = _get_array_item_arr_payload(c.context, c.builder,
        gpqwk__wnf, data_arr)
    null_bitmap_ptr = c.context.make_array(types.Array(types.uint8, 1, 'C'))(c
        .context, c.builder, etgm__qgoc.null_bitmap).data
    offsets_ptr = c.context.make_array(types.Array(offset_type, 1, 'C'))(c.
        context, c.builder, etgm__qgoc.offsets).data
    avxwz__ytrnh = _get_struct_arr_payload(c.context, c.builder, gpqwk__wnf
        .dtype, etgm__qgoc.data)
    key_arr = c.builder.extract_value(avxwz__ytrnh.data, 0)
    value_arr = c.builder.extract_value(avxwz__ytrnh.data, 1)
    if all(isinstance(wkon__qeejq, types.Array) and wkon__qeejq.dtype in (
        types.int64, types.float64, types.bool_, datetime_date_type) for
        wkon__qeejq in (typ.key_arr_type, typ.value_arr_type)):
        quoe__dko = c.context.make_array(gpqwk__wnf.dtype.data[0])(c.
            context, c.builder, key_arr).data
        rycds__ltosv = c.context.make_array(gpqwk__wnf.dtype.data[1])(c.
            context, c.builder, value_arr).data
        whbjj__zgtaj = lir.FunctionType(c.context.get_argument_type(types.
            pyobject), [lir.IntType(64), lir.IntType(8).as_pointer(), lir.
            IntType(8).as_pointer(), lir.IntType(offset_type.bitwidth).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(32), lir
            .IntType(32)])
        egv__cax = cgutils.get_or_insert_function(c.builder.module,
            whbjj__zgtaj, name='np_array_from_map_array')
        fsa__cgv = bodo.utils.utils.numba_to_c_type(typ.key_arr_type.dtype)
        wmjtn__cfp = bodo.utils.utils.numba_to_c_type(typ.value_arr_type.dtype)
        arr = c.builder.call(egv__cax, [etgm__qgoc.n_arrays, c.builder.
            bitcast(quoe__dko, lir.IntType(8).as_pointer()), c.builder.
            bitcast(rycds__ltosv, lir.IntType(8).as_pointer()), offsets_ptr,
            null_bitmap_ptr, lir.Constant(lir.IntType(32), fsa__cgv), lir.
            Constant(lir.IntType(32), wmjtn__cfp)])
    else:
        arr = _box_map_array_generic(typ, c, etgm__qgoc.n_arrays, key_arr,
            value_arr, offsets_ptr, null_bitmap_ptr)
    c.context.nrt.decref(c.builder, typ, val)
    return arr


def _box_map_array_generic(typ, c, n_maps, key_arr, value_arr, offsets_ptr,
    null_bitmap_ptr):
    context = c.context
    builder = c.builder
    hysq__egpdi = context.insert_const_string(builder.module, 'numpy')
    vzhq__wloxu = c.pyapi.import_module_noblock(hysq__egpdi)
    spoy__lpyzk = c.pyapi.object_getattr_string(vzhq__wloxu, 'object_')
    ynqk__qnz = c.pyapi.long_from_longlong(n_maps)
    jli__bkhxu = c.pyapi.call_method(vzhq__wloxu, 'ndarray', (ynqk__qnz,
        spoy__lpyzk))
    ttxl__pkdv = c.pyapi.object_getattr_string(vzhq__wloxu, 'nan')
    jgs__exo = c.pyapi.unserialize(c.pyapi.serialize_object(zip))
    qokkc__ezfaz = cgutils.alloca_once_value(builder, lir.Constant(lir.
        IntType(64), 0))
    with cgutils.for_range(builder, n_maps) as cpol__urtr:
        slrjb__wcfb = cpol__urtr.index
        pyarray_setitem(builder, context, jli__bkhxu, slrjb__wcfb, ttxl__pkdv)
        ekow__pvc = get_bitmap_bit(builder, null_bitmap_ptr, slrjb__wcfb)
        dqsm__zysk = builder.icmp_unsigned('!=', ekow__pvc, lir.Constant(
            lir.IntType(8), 0))
        with builder.if_then(dqsm__zysk):
            n_items = builder.sext(builder.sub(builder.load(builder.gep(
                offsets_ptr, [builder.add(slrjb__wcfb, lir.Constant(
                slrjb__wcfb.type, 1))])), builder.load(builder.gep(
                offsets_ptr, [slrjb__wcfb]))), lir.IntType(64))
            item_ind = builder.load(qokkc__ezfaz)
            ujkg__xbz = c.pyapi.dict_new()
            fckox__zvcta = lambda data_arr, item_ind, n_items: data_arr[
                item_ind:item_ind + n_items]
            yddn__yru, tivwx__bfz = c.pyapi.call_jit_code(fckox__zvcta, typ
                .key_arr_type(typ.key_arr_type, types.int64, types.int64),
                [key_arr, item_ind, n_items])
            yddn__yru, wiag__idj = c.pyapi.call_jit_code(fckox__zvcta, typ.
                value_arr_type(typ.value_arr_type, types.int64, types.int64
                ), [value_arr, item_ind, n_items])
            gpr__acb = c.pyapi.from_native_value(typ.key_arr_type,
                tivwx__bfz, c.env_manager)
            wzjt__vax = c.pyapi.from_native_value(typ.value_arr_type,
                wiag__idj, c.env_manager)
            alpy__wxyu = c.pyapi.call_function_objargs(jgs__exo, (gpr__acb,
                wzjt__vax))
            dict_merge_from_seq2(builder, context, ujkg__xbz, alpy__wxyu)
            builder.store(builder.add(item_ind, n_items), qokkc__ezfaz)
            pyarray_setitem(builder, context, jli__bkhxu, slrjb__wcfb,
                ujkg__xbz)
            c.pyapi.decref(alpy__wxyu)
            c.pyapi.decref(gpr__acb)
            c.pyapi.decref(wzjt__vax)
            c.pyapi.decref(ujkg__xbz)
    c.pyapi.decref(jgs__exo)
    c.pyapi.decref(vzhq__wloxu)
    c.pyapi.decref(spoy__lpyzk)
    c.pyapi.decref(ynqk__qnz)
    c.pyapi.decref(ttxl__pkdv)
    return jli__bkhxu


def init_map_arr_codegen(context, builder, sig, args):
    data_arr, = args
    kjw__dwrcd = context.make_helper(builder, sig.return_type)
    kjw__dwrcd.data = data_arr
    context.nrt.incref(builder, sig.args[0], data_arr)
    return kjw__dwrcd._getvalue()


@intrinsic
def init_map_arr(typingctx, data_typ=None):
    assert isinstance(data_typ, ArrayItemArrayType) and isinstance(data_typ
        .dtype, StructArrayType)
    ytj__dkla = MapArrayType(data_typ.dtype.data[0], data_typ.dtype.data[1])
    return ytj__dkla(data_typ), init_map_arr_codegen


def alias_ext_init_map_arr(lhs_name, args, alias_map, arg_aliases):
    assert len(args) == 1
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)


numba.core.ir_utils.alias_func_extensions['init_map_arr',
    'bodo.libs.map_arr_ext'] = alias_ext_init_map_arr


@numba.njit
def pre_alloc_map_array(num_maps, nested_counts, struct_typ):
    xiaq__lkn = bodo.libs.array_item_arr_ext.pre_alloc_array_item_array(
        num_maps, nested_counts, struct_typ)
    return init_map_arr(xiaq__lkn)


def pre_alloc_map_array_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 3 and not kws
    return ArrayAnalysis.AnalyzeResult(shape=args[0], pre=[])


(ArrayAnalysis._analyze_op_call_bodo_libs_map_arr_ext_pre_alloc_map_array
    ) = pre_alloc_map_array_equiv


@overload(len, no_unliteral=True)
def overload_map_arr_len(A):
    if isinstance(A, MapArrayType):
        return lambda A: len(A._data)


@overload_attribute(MapArrayType, 'shape')
def overload_map_arr_shape(A):
    return lambda A: (len(A._data),)


@overload_attribute(MapArrayType, 'dtype')
def overload_map_arr_dtype(A):
    return lambda A: np.object_


@overload_attribute(MapArrayType, 'ndim')
def overload_map_arr_ndim(A):
    return lambda A: 1


@overload_attribute(MapArrayType, 'nbytes')
def overload_map_arr_nbytes(A):
    return lambda A: A._data.nbytes


@overload_method(MapArrayType, 'copy')
def overload_map_arr_copy(A):
    return lambda A: init_map_arr(A._data.copy())


@overload(operator.setitem, no_unliteral=True)
def map_arr_setitem(arr, ind, val):
    if not isinstance(arr, MapArrayType):
        return
    hnkrx__yiimb = arr.key_arr_type, arr.value_arr_type
    if isinstance(ind, types.Integer):

        def map_arr_setitem_impl(arr, ind, val):
            duwot__jmmr = val.keys()
            wnwqv__jvjvi = bodo.libs.struct_arr_ext.pre_alloc_struct_array(len
                (val), (-1,), hnkrx__yiimb, ('key', 'value'))
            for vsyl__djo, vpo__ycc in enumerate(duwot__jmmr):
                wnwqv__jvjvi[vsyl__djo] = bodo.libs.struct_arr_ext.init_struct(
                    (vpo__ycc, val[vpo__ycc]), ('key', 'value'))
            arr._data[ind] = wnwqv__jvjvi
        return map_arr_setitem_impl
    raise BodoError(
        'operator.setitem with MapArrays is only supported with an integer index.'
        )


@overload(operator.getitem, no_unliteral=True)
def map_arr_getitem(arr, ind):
    if not isinstance(arr, MapArrayType):
        return
    if isinstance(ind, types.Integer):

        def map_arr_getitem_impl(arr, ind):
            if ind < 0:
                ind += len(arr)
            mebt__hvzhk = dict()
            qss__jvg = bodo.libs.array_item_arr_ext.get_offsets(arr._data)
            wnwqv__jvjvi = bodo.libs.array_item_arr_ext.get_data(arr._data)
            kgbpy__cghei, ckeb__awtd = bodo.libs.struct_arr_ext.get_data(
                wnwqv__jvjvi)
            rnbq__miyt = qss__jvg[ind]
            wsuq__rvrlr = qss__jvg[ind + 1]
            for vsyl__djo in range(rnbq__miyt, wsuq__rvrlr):
                mebt__hvzhk[kgbpy__cghei[vsyl__djo]] = ckeb__awtd[vsyl__djo]
            return mebt__hvzhk
        return map_arr_getitem_impl
    raise BodoError(
        'operator.getitem with MapArrays is only supported with an integer index.'
        )
