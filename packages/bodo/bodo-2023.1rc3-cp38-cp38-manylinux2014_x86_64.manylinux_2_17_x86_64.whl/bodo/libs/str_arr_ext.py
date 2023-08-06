"""Array implementation for string objects, which are usually immutable.
The characters are stored in a contiguous data array, and an offsets array marks the
the individual strings. For example:
value:             ['a', 'bc', '', 'abc', None, 'bb']
data:              [a, b, c, a, b, c, b, b]
offsets:           [0, 1, 3, 3, 6, 6, 8]
"""
import glob
import operator
import numba
import numba.core.typing.typeof
import numpy as np
import pandas as pd
import pyarrow as pa
from numba.core import cgutils, types
from numba.core.imputils import impl_ret_borrowed, lower_constant
from numba.core.unsafe.bytes import memcpy_region
from numba.extending import NativeValue, box, intrinsic, lower_builtin, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_jitable, register_model, type_callable, typeof_impl, unbox
import bodo
from bodo.libs.array_item_arr_ext import ArrayItemArrayPayloadType, ArrayItemArrayType, _get_array_item_arr_payload, np_offset_type, offset_type
from bodo.libs.binary_arr_ext import BinaryArrayType, binary_array_type, pre_alloc_binary_array
from bodo.libs.str_ext import memcmp, string_type, unicode_to_utf8_and_len
from bodo.utils.typing import BodoArrayIterator, BodoError, is_list_like_index_type, is_overload_constant_int, is_overload_none, is_overload_true, is_str_arr_type, parse_dtype, raise_bodo_error
use_pd_string_array = False
use_pd_pyarrow_string_array = True
char_type = types.uint8
char_arr_type = types.Array(char_type, 1, 'C')
offset_arr_type = types.Array(offset_type, 1, 'C')
null_bitmap_arr_type = types.Array(types.uint8, 1, 'C')
data_ctypes_type = types.ArrayCTypes(char_arr_type)
offset_ctypes_type = types.ArrayCTypes(offset_arr_type)


class StringArrayType(types.IterableType, types.ArrayCompatible):

    def __init__(self):
        super(StringArrayType, self).__init__(name='StringArrayType()')

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    @property
    def dtype(self):
        return string_type

    @property
    def iterator_type(self):
        return BodoArrayIterator(self)

    def copy(self):
        return StringArrayType()


string_array_type = StringArrayType()


@typeof_impl.register(pd.arrays.StringArray)
def typeof_string_array(val, c):
    return string_array_type


@typeof_impl.register(pd.arrays.ArrowStringArray)
def typeof_pyarrow_string_array(val, c):
    if pa.types.is_dictionary(val._data.combine_chunks().type):
        return bodo.dict_str_arr_type
    return string_array_type


@register_model(BinaryArrayType)
@register_model(StringArrayType)
class StringArrayModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        olx__pdokq = ArrayItemArrayType(char_arr_type)
        vhsu__fjcs = [('data', olx__pdokq)]
        models.StructModel.__init__(self, dmm, fe_type, vhsu__fjcs)


make_attribute_wrapper(StringArrayType, 'data', '_data')
make_attribute_wrapper(BinaryArrayType, 'data', '_data')
lower_builtin('getiter', string_array_type)(numba.np.arrayobj.getiter_array)


@intrinsic
def init_str_arr(typingctx, data_typ=None):
    assert isinstance(data_typ, ArrayItemArrayType
        ) and data_typ.dtype == types.Array(char_type, 1, 'C')

    def codegen(context, builder, sig, args):
        khgaa__bmux, = args
        ivqv__tlvt = context.make_helper(builder, string_array_type)
        ivqv__tlvt.data = khgaa__bmux
        context.nrt.incref(builder, data_typ, khgaa__bmux)
        return ivqv__tlvt._getvalue()
    return string_array_type(data_typ), codegen


class StringDtype(types.Number):

    def __init__(self):
        super(StringDtype, self).__init__('StringDtype')


string_dtype = StringDtype()
register_model(StringDtype)(models.OpaqueModel)


@box(StringDtype)
def box_string_dtype(typ, val, c):
    apxl__qdz = c.context.insert_const_string(c.builder.module, 'pandas')
    dgf__fjkyx = c.pyapi.import_module_noblock(apxl__qdz)
    qtirw__nbwi = c.pyapi.call_method(dgf__fjkyx, 'StringDtype', ())
    c.pyapi.decref(dgf__fjkyx)
    return qtirw__nbwi


@unbox(StringDtype)
def unbox_string_dtype(typ, val, c):
    return NativeValue(c.context.get_dummy_value())


typeof_impl.register(pd.StringDtype)(lambda a, b: string_dtype)
type_callable(pd.StringDtype)(lambda c: lambda : string_dtype)
lower_builtin(pd.StringDtype)(lambda c, b, s, a: c.get_dummy_value())


def create_binary_op_overload(op):

    def overload_string_array_binary_op(lhs, rhs):
        eqr__lzfen = bodo.libs.dict_arr_ext.get_binary_op_overload(op, lhs, rhs
            )
        if eqr__lzfen is not None:
            return eqr__lzfen
        if is_str_arr_type(lhs) and is_str_arr_type(rhs):

            def impl_both(lhs, rhs):
                numba.parfors.parfor.init_prange()
                qnhvy__zkfvs = len(lhs)
                out_arr = bodo.libs.bool_arr_ext.alloc_bool_array(qnhvy__zkfvs)
                for i in numba.parfors.parfor.internal_prange(qnhvy__zkfvs):
                    if bodo.libs.array_kernels.isna(lhs, i
                        ) or bodo.libs.array_kernels.isna(rhs, i):
                        bodo.libs.array_kernels.setna(out_arr, i)
                        continue
                    val = op(lhs[i], rhs[i])
                    out_arr[i] = val
                return out_arr
            return impl_both
        if is_str_arr_type(lhs) and types.unliteral(rhs) == string_type:

            def impl_left(lhs, rhs):
                numba.parfors.parfor.init_prange()
                qnhvy__zkfvs = len(lhs)
                out_arr = bodo.libs.bool_arr_ext.alloc_bool_array(qnhvy__zkfvs)
                for i in numba.parfors.parfor.internal_prange(qnhvy__zkfvs):
                    if bodo.libs.array_kernels.isna(lhs, i):
                        bodo.libs.array_kernels.setna(out_arr, i)
                        continue
                    val = op(lhs[i], rhs)
                    out_arr[i] = val
                return out_arr
            return impl_left
        if types.unliteral(lhs) == string_type and is_str_arr_type(rhs):

            def impl_right(lhs, rhs):
                numba.parfors.parfor.init_prange()
                qnhvy__zkfvs = len(rhs)
                out_arr = bodo.libs.bool_arr_ext.alloc_bool_array(qnhvy__zkfvs)
                for i in numba.parfors.parfor.internal_prange(qnhvy__zkfvs):
                    if bodo.libs.array_kernels.isna(rhs, i):
                        bodo.libs.array_kernels.setna(out_arr, i)
                        continue
                    val = op(lhs, rhs[i])
                    out_arr[i] = val
                return out_arr
            return impl_right
        raise_bodo_error(
            f'{op} operator not supported for data types {lhs} and {rhs}.')
    return overload_string_array_binary_op


def overload_add_operator_string_array(lhs, rhs):
    nlc__tvie = is_str_arr_type(lhs) or isinstance(lhs, types.Array
        ) and lhs.dtype == string_type
    ieek__wmgyn = is_str_arr_type(rhs) or isinstance(rhs, types.Array
        ) and rhs.dtype == string_type
    if is_str_arr_type(lhs) and ieek__wmgyn or nlc__tvie and is_str_arr_type(
        rhs):

        def impl_both(lhs, rhs):
            numba.parfors.parfor.init_prange()
            l = len(lhs)
            out_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(l, -1)
            for j in numba.parfors.parfor.internal_prange(l):
                if bodo.libs.array_kernels.isna(lhs, j
                    ) or bodo.libs.array_kernels.isna(rhs, j):
                    out_arr[j] = ''
                    bodo.libs.array_kernels.setna(out_arr, j)
                else:
                    out_arr[j] = lhs[j] + rhs[j]
            return out_arr
        return impl_both
    if is_str_arr_type(lhs) and types.unliteral(rhs) == string_type:

        def impl_left(lhs, rhs):
            numba.parfors.parfor.init_prange()
            l = len(lhs)
            out_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(l, -1)
            for j in numba.parfors.parfor.internal_prange(l):
                if bodo.libs.array_kernels.isna(lhs, j):
                    out_arr[j] = ''
                    bodo.libs.array_kernels.setna(out_arr, j)
                else:
                    out_arr[j] = lhs[j] + rhs
            return out_arr
        return impl_left
    if types.unliteral(lhs) == string_type and is_str_arr_type(rhs):

        def impl_right(lhs, rhs):
            numba.parfors.parfor.init_prange()
            l = len(rhs)
            out_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(l, -1)
            for j in numba.parfors.parfor.internal_prange(l):
                if bodo.libs.array_kernels.isna(rhs, j):
                    out_arr[j] = ''
                    bodo.libs.array_kernels.setna(out_arr, j)
                else:
                    out_arr[j] = lhs + rhs[j]
            return out_arr
        return impl_right


def overload_mul_operator_str_arr(lhs, rhs):
    if is_str_arr_type(lhs) and isinstance(rhs, types.Integer):

        def impl(lhs, rhs):
            numba.parfors.parfor.init_prange()
            l = len(lhs)
            out_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(l, -1)
            for j in numba.parfors.parfor.internal_prange(l):
                if bodo.libs.array_kernels.isna(lhs, j):
                    out_arr[j] = ''
                    bodo.libs.array_kernels.setna(out_arr, j)
                else:
                    out_arr[j] = lhs[j] * rhs
            return out_arr
        return impl
    if isinstance(lhs, types.Integer) and is_str_arr_type(rhs):

        def impl(lhs, rhs):
            return rhs * lhs
        return impl


def _get_str_binary_arr_payload(context, builder, arr_value, arr_typ):
    assert arr_typ == string_array_type or arr_typ == binary_array_type
    serc__rocvd = context.make_helper(builder, arr_typ, arr_value)
    olx__pdokq = ArrayItemArrayType(char_arr_type)
    alg__tbz = _get_array_item_arr_payload(context, builder, olx__pdokq,
        serc__rocvd.data)
    return alg__tbz


@intrinsic
def num_strings(typingctx, str_arr_typ=None):
    assert str_arr_typ == string_array_type

    def codegen(context, builder, sig, args):
        in_str_arr, = args
        alg__tbz = _get_str_binary_arr_payload(context, builder, in_str_arr,
            string_array_type)
        return alg__tbz.n_arrays
    return types.int64(string_array_type), codegen


def _get_num_total_chars(builder, offsets, num_strings):
    return builder.zext(builder.load(builder.gep(offsets, [num_strings])),
        lir.IntType(64))


@numba.njit
def check_offsets(str_arr):
    offsets = bodo.libs.array_item_arr_ext.get_offsets(str_arr._data)
    n_chars = bodo.libs.str_arr_ext.num_total_chars(str_arr)
    for i in range(bodo.libs.array_item_arr_ext.get_n_arrays(str_arr._data)):
        if offsets[i] > n_chars or offsets[i + 1] - offsets[i] < 0:
            print('wrong offset found', i, offsets[i])
            break


@intrinsic
def num_total_chars(typingctx, in_arr_typ=None):
    assert in_arr_typ in [binary_array_type, string_array_type]

    def codegen(context, builder, sig, args):
        in_str_arr, = args
        alg__tbz = _get_str_binary_arr_payload(context, builder, in_str_arr,
            sig.args[0])
        uywh__bsgox = context.make_helper(builder, offset_arr_type,
            alg__tbz.offsets).data
        return _get_num_total_chars(builder, uywh__bsgox, alg__tbz.n_arrays)
    return types.uint64(in_arr_typ), codegen


@intrinsic
def get_offset_ptr(typingctx, in_arr_typ=None):
    assert in_arr_typ in [binary_array_type, string_array_type]

    def codegen(context, builder, sig, args):
        in_str_arr, = args
        alg__tbz = _get_str_binary_arr_payload(context, builder, in_str_arr,
            sig.args[0])
        zkw__xdu = context.make_helper(builder, offset_arr_type, alg__tbz.
            offsets)
        mlgwj__qfoc = context.make_helper(builder, offset_ctypes_type)
        mlgwj__qfoc.data = builder.bitcast(zkw__xdu.data, lir.IntType(
            offset_type.bitwidth).as_pointer())
        mlgwj__qfoc.meminfo = zkw__xdu.meminfo
        qtirw__nbwi = mlgwj__qfoc._getvalue()
        return impl_ret_borrowed(context, builder, offset_ctypes_type,
            qtirw__nbwi)
    return offset_ctypes_type(in_arr_typ), codegen


@intrinsic
def get_data_ptr(typingctx, in_arr_typ=None):
    assert in_arr_typ in [binary_array_type, string_array_type]

    def codegen(context, builder, sig, args):
        in_str_arr, = args
        alg__tbz = _get_str_binary_arr_payload(context, builder, in_str_arr,
            sig.args[0])
        khgaa__bmux = context.make_helper(builder, char_arr_type, alg__tbz.data
            )
        mlgwj__qfoc = context.make_helper(builder, data_ctypes_type)
        mlgwj__qfoc.data = khgaa__bmux.data
        mlgwj__qfoc.meminfo = khgaa__bmux.meminfo
        qtirw__nbwi = mlgwj__qfoc._getvalue()
        return impl_ret_borrowed(context, builder, data_ctypes_type,
            qtirw__nbwi)
    return data_ctypes_type(in_arr_typ), codegen


@intrinsic
def get_data_ptr_ind(typingctx, in_arr_typ, int_t=None):
    assert in_arr_typ in [binary_array_type, string_array_type]

    def codegen(context, builder, sig, args):
        iyin__afsez, ind = args
        alg__tbz = _get_str_binary_arr_payload(context, builder,
            iyin__afsez, sig.args[0])
        khgaa__bmux = context.make_helper(builder, char_arr_type, alg__tbz.data
            )
        mlgwj__qfoc = context.make_helper(builder, data_ctypes_type)
        mlgwj__qfoc.data = builder.gep(khgaa__bmux.data, [ind])
        mlgwj__qfoc.meminfo = khgaa__bmux.meminfo
        qtirw__nbwi = mlgwj__qfoc._getvalue()
        return impl_ret_borrowed(context, builder, data_ctypes_type,
            qtirw__nbwi)
    return data_ctypes_type(in_arr_typ, types.intp), codegen


@intrinsic
def copy_single_char(typingctx, dst_ptr_t, dst_ind_t, src_ptr_t, src_ind_t=None
    ):

    def codegen(context, builder, sig, args):
        kaoz__lstk, ulsxq__pzx, knc__nrrnq, mzb__oeby = args
        ehif__ejlu = builder.bitcast(builder.gep(kaoz__lstk, [ulsxq__pzx]),
            lir.IntType(8).as_pointer())
        aeh__umh = builder.bitcast(builder.gep(knc__nrrnq, [mzb__oeby]),
            lir.IntType(8).as_pointer())
        lqdd__vlcs = builder.load(aeh__umh)
        builder.store(lqdd__vlcs, ehif__ejlu)
        return context.get_dummy_value()
    return types.void(types.voidptr, types.intp, types.voidptr, types.intp
        ), codegen


@intrinsic
def get_null_bitmap_ptr(typingctx, in_arr_typ=None):
    assert in_arr_typ in [binary_array_type, string_array_type]

    def codegen(context, builder, sig, args):
        in_str_arr, = args
        alg__tbz = _get_str_binary_arr_payload(context, builder, in_str_arr,
            sig.args[0])
        aliad__enzg = context.make_helper(builder, null_bitmap_arr_type,
            alg__tbz.null_bitmap)
        mlgwj__qfoc = context.make_helper(builder, data_ctypes_type)
        mlgwj__qfoc.data = aliad__enzg.data
        mlgwj__qfoc.meminfo = aliad__enzg.meminfo
        qtirw__nbwi = mlgwj__qfoc._getvalue()
        return impl_ret_borrowed(context, builder, data_ctypes_type,
            qtirw__nbwi)
    return data_ctypes_type(in_arr_typ), codegen


@intrinsic
def getitem_str_offset(typingctx, in_arr_typ, ind_t=None):
    assert in_arr_typ in [binary_array_type, string_array_type]

    def codegen(context, builder, sig, args):
        in_str_arr, ind = args
        alg__tbz = _get_str_binary_arr_payload(context, builder, in_str_arr,
            sig.args[0])
        uywh__bsgox = context.make_helper(builder, offset_arr_type,
            alg__tbz.offsets).data
        return builder.load(builder.gep(uywh__bsgox, [ind]))
    return offset_type(in_arr_typ, ind_t), codegen


@intrinsic
def setitem_str_offset(typingctx, str_arr_typ, ind_t, val_t=None):
    assert str_arr_typ == string_array_type

    def codegen(context, builder, sig, args):
        in_str_arr, ind, val = args
        alg__tbz = _get_str_binary_arr_payload(context, builder, in_str_arr,
            string_array_type)
        offsets = context.make_helper(builder, offset_arr_type, alg__tbz.
            offsets).data
        builder.store(val, builder.gep(offsets, [ind]))
        return context.get_dummy_value()
    return types.void(string_array_type, ind_t, offset_type), codegen


@intrinsic
def getitem_str_bitmap(typingctx, in_bitmap_typ, ind_t=None):

    def codegen(context, builder, sig, args):
        ovpnu__yxqhu, ind = args
        if in_bitmap_typ == data_ctypes_type:
            mlgwj__qfoc = context.make_helper(builder, data_ctypes_type,
                ovpnu__yxqhu)
            ovpnu__yxqhu = mlgwj__qfoc.data
        return builder.load(builder.gep(ovpnu__yxqhu, [ind]))
    return char_type(in_bitmap_typ, ind_t), codegen


@intrinsic
def setitem_str_bitmap(typingctx, in_bitmap_typ, ind_t, val_t=None):

    def codegen(context, builder, sig, args):
        ovpnu__yxqhu, ind, val = args
        if in_bitmap_typ == data_ctypes_type:
            mlgwj__qfoc = context.make_helper(builder, data_ctypes_type,
                ovpnu__yxqhu)
            ovpnu__yxqhu = mlgwj__qfoc.data
        builder.store(val, builder.gep(ovpnu__yxqhu, [ind]))
        return context.get_dummy_value()
    return types.void(in_bitmap_typ, ind_t, char_type), codegen


@intrinsic
def copy_str_arr_slice(typingctx, out_str_arr_typ, in_str_arr_typ, ind_t=None):
    assert out_str_arr_typ == string_array_type and in_str_arr_typ == string_array_type

    def codegen(context, builder, sig, args):
        out_str_arr, in_str_arr, ind = args
        xmfz__svw = _get_str_binary_arr_payload(context, builder,
            in_str_arr, string_array_type)
        uxb__nolp = _get_str_binary_arr_payload(context, builder,
            out_str_arr, string_array_type)
        dlic__egz = context.make_helper(builder, offset_arr_type, xmfz__svw
            .offsets).data
        scnxq__sjw = context.make_helper(builder, offset_arr_type,
            uxb__nolp.offsets).data
        mlw__nldey = context.make_helper(builder, char_arr_type, xmfz__svw.data
            ).data
        mwovb__hxue = context.make_helper(builder, char_arr_type, uxb__nolp
            .data).data
        pwc__kuuq = context.make_helper(builder, null_bitmap_arr_type,
            xmfz__svw.null_bitmap).data
        oakyp__uoo = context.make_helper(builder, null_bitmap_arr_type,
            uxb__nolp.null_bitmap).data
        ubola__ser = builder.add(ind, context.get_constant(types.intp, 1))
        cgutils.memcpy(builder, scnxq__sjw, dlic__egz, ubola__ser)
        cgutils.memcpy(builder, mwovb__hxue, mlw__nldey, builder.load(
            builder.gep(dlic__egz, [ind])))
        wcu__pnf = builder.add(ind, lir.Constant(lir.IntType(64), 7))
        aqc__wfoaq = builder.lshr(wcu__pnf, lir.Constant(lir.IntType(64), 3))
        cgutils.memcpy(builder, oakyp__uoo, pwc__kuuq, aqc__wfoaq)
        return context.get_dummy_value()
    return types.void(string_array_type, string_array_type, ind_t), codegen


@intrinsic
def copy_data(typingctx, str_arr_typ, out_str_arr_typ=None):
    assert str_arr_typ == string_array_type and out_str_arr_typ == string_array_type

    def codegen(context, builder, sig, args):
        out_str_arr, in_str_arr = args
        xmfz__svw = _get_str_binary_arr_payload(context, builder,
            in_str_arr, string_array_type)
        uxb__nolp = _get_str_binary_arr_payload(context, builder,
            out_str_arr, string_array_type)
        dlic__egz = context.make_helper(builder, offset_arr_type, xmfz__svw
            .offsets).data
        mlw__nldey = context.make_helper(builder, char_arr_type, xmfz__svw.data
            ).data
        mwovb__hxue = context.make_helper(builder, char_arr_type, uxb__nolp
            .data).data
        num_total_chars = _get_num_total_chars(builder, dlic__egz,
            xmfz__svw.n_arrays)
        cgutils.memcpy(builder, mwovb__hxue, mlw__nldey, num_total_chars)
        return context.get_dummy_value()
    return types.void(string_array_type, string_array_type), codegen


@intrinsic
def copy_non_null_offsets(typingctx, str_arr_typ, out_str_arr_typ=None):
    assert str_arr_typ == string_array_type and out_str_arr_typ == string_array_type

    def codegen(context, builder, sig, args):
        out_str_arr, in_str_arr = args
        xmfz__svw = _get_str_binary_arr_payload(context, builder,
            in_str_arr, string_array_type)
        uxb__nolp = _get_str_binary_arr_payload(context, builder,
            out_str_arr, string_array_type)
        dlic__egz = context.make_helper(builder, offset_arr_type, xmfz__svw
            .offsets).data
        scnxq__sjw = context.make_helper(builder, offset_arr_type,
            uxb__nolp.offsets).data
        pwc__kuuq = context.make_helper(builder, null_bitmap_arr_type,
            xmfz__svw.null_bitmap).data
        qnhvy__zkfvs = xmfz__svw.n_arrays
        qibtu__fkrer = context.get_constant(offset_type, 0)
        blm__wwtlw = cgutils.alloca_once_value(builder, qibtu__fkrer)
        with cgutils.for_range(builder, qnhvy__zkfvs) as qel__huqgv:
            doqz__utcf = lower_is_na(context, builder, pwc__kuuq,
                qel__huqgv.index)
            with cgutils.if_likely(builder, builder.not_(doqz__utcf)):
                zwu__ivr = builder.load(builder.gep(dlic__egz, [qel__huqgv.
                    index]))
                uti__wzbse = builder.load(blm__wwtlw)
                builder.store(zwu__ivr, builder.gep(scnxq__sjw, [uti__wzbse]))
                builder.store(builder.add(uti__wzbse, lir.Constant(context.
                    get_value_type(offset_type), 1)), blm__wwtlw)
        uti__wzbse = builder.load(blm__wwtlw)
        zwu__ivr = builder.load(builder.gep(dlic__egz, [qnhvy__zkfvs]))
        builder.store(zwu__ivr, builder.gep(scnxq__sjw, [uti__wzbse]))
        return context.get_dummy_value()
    return types.void(string_array_type, string_array_type), codegen


@intrinsic
def str_copy(typingctx, buff_arr_typ, ind_typ, str_typ, len_typ=None):

    def codegen(context, builder, sig, args):
        saohl__lcqla, ind, str, xkelg__ucyy = args
        saohl__lcqla = context.make_array(sig.args[0])(context, builder,
            saohl__lcqla)
        asx__vavez = builder.gep(saohl__lcqla.data, [ind])
        cgutils.raw_memcpy(builder, asx__vavez, str, xkelg__ucyy, 1)
        return context.get_dummy_value()
    return types.void(null_bitmap_arr_type, types.intp, types.voidptr,
        types.intp), codegen


@intrinsic
def str_copy_ptr(typingctx, ptr_typ, ind_typ, str_typ, len_typ=None):

    def codegen(context, builder, sig, args):
        asx__vavez, ind, ucu__njtny, xkelg__ucyy = args
        asx__vavez = builder.gep(asx__vavez, [ind])
        cgutils.raw_memcpy(builder, asx__vavez, ucu__njtny, xkelg__ucyy, 1)
        return context.get_dummy_value()
    return types.void(types.voidptr, types.intp, types.voidptr, types.intp
        ), codegen


@numba.generated_jit(nopython=True)
def get_str_arr_item_length(A, i):
    if A == bodo.dict_str_arr_type:

        def impl(A, i):
            idx = A._indices[i]
            wgkvl__jwm = A._data
            return np.int64(getitem_str_offset(wgkvl__jwm, idx + 1) -
                getitem_str_offset(wgkvl__jwm, idx))
        return impl
    else:
        return lambda A, i: np.int64(getitem_str_offset(A, i + 1) -
            getitem_str_offset(A, i))


@numba.njit(no_cpython_wrapper=True)
def get_str_arr_str_length(A, i):
    gsvpy__indt = np.int64(getitem_str_offset(A, i))
    sir__djfjf = np.int64(getitem_str_offset(A, i + 1))
    l = sir__djfjf - gsvpy__indt
    emd__ptav = get_data_ptr_ind(A, gsvpy__indt)
    for j in range(l):
        if bodo.hiframes.split_impl.getitem_c_arr(emd__ptav, j) >= 128:
            return len(A[i])
    return l


@numba.njit(no_cpython_wrapper=True)
def get_str_arr_item_ptr(A, i):
    return get_data_ptr_ind(A, getitem_str_offset(A, i))


@numba.generated_jit(no_cpython_wrapper=True, nopython=True)
def get_str_arr_item_copy(B, j, A, i):
    if B != string_array_type:
        raise BodoError(
            'get_str_arr_item_copy(): Output array must be a string array')
    if not is_str_arr_type(A):
        raise BodoError(
            'get_str_arr_item_copy(): Input array must be a string array or dictionary encoded array'
            )
    if A == bodo.dict_str_arr_type:
        vepsb__tnooo = 'in_str_arr = A._data'
        jib__gvkkr = 'input_index = A._indices[i]'
    else:
        vepsb__tnooo = 'in_str_arr = A'
        jib__gvkkr = 'input_index = i'
    aoyzz__mlz = f"""def impl(B, j, A, i):
        if j == 0:
            setitem_str_offset(B, 0, 0)

        {vepsb__tnooo}
        {jib__gvkkr}

        # set NA
        if bodo.libs.array_kernels.isna(A, i):
            str_arr_set_na(B, j)
            return
        else:
            str_arr_set_not_na(B, j)

        # get input array offsets
        in_start_offset = getitem_str_offset(in_str_arr, input_index)
        in_end_offset = getitem_str_offset(in_str_arr, input_index + 1)
        val_len = in_end_offset - in_start_offset

        # set output offset
        out_start_offset = getitem_str_offset(B, j)
        out_end_offset = out_start_offset + val_len
        setitem_str_offset(B, j + 1, out_end_offset)

        # copy data
        if val_len != 0:
            # ensure required space in output array
            data_arr = B._data
            bodo.libs.array_item_arr_ext.ensure_data_capacity(
                data_arr, np.int64(out_start_offset), np.int64(out_end_offset)
            )
            out_data_ptr = get_data_ptr(B).data
            in_data_ptr = get_data_ptr(in_str_arr).data
            memcpy_region(
                out_data_ptr,
                out_start_offset,
                in_data_ptr,
                in_start_offset,
                val_len,
                1,
            )"""
    nfuew__folk = {}
    exec(aoyzz__mlz, {'setitem_str_offset': setitem_str_offset,
        'memcpy_region': memcpy_region, 'getitem_str_offset':
        getitem_str_offset, 'str_arr_set_na': str_arr_set_na,
        'str_arr_set_not_na': str_arr_set_not_na, 'get_data_ptr':
        get_data_ptr, 'bodo': bodo, 'np': np}, nfuew__folk)
    impl = nfuew__folk['impl']
    return impl


@numba.njit(no_cpython_wrapper=True)
def get_str_null_bools(str_arr):
    qnhvy__zkfvs = len(str_arr)
    fkp__brz = np.empty(qnhvy__zkfvs, np.bool_)
    for i in range(qnhvy__zkfvs):
        fkp__brz[i] = bodo.libs.array_kernels.isna(str_arr, i)
    return fkp__brz


def to_list_if_immutable_arr(arr, str_null_bools=None):
    return arr


@overload(to_list_if_immutable_arr, no_unliteral=True)
def to_list_if_immutable_arr_overload(data, str_null_bools=None):
    if is_str_arr_type(data) or data == binary_array_type:

        def to_list_impl(data, str_null_bools=None):
            qnhvy__zkfvs = len(data)
            l = []
            for i in range(qnhvy__zkfvs):
                l.append(data[i])
            return l
        return to_list_impl
    if isinstance(data, types.BaseTuple):
        iuvw__zan = data.count
        phyn__xupn = ['to_list_if_immutable_arr(data[{}])'.format(i) for i in
            range(iuvw__zan)]
        if is_overload_true(str_null_bools):
            phyn__xupn += ['get_str_null_bools(data[{}])'.format(i) for i in
                range(iuvw__zan) if is_str_arr_type(data.types[i]) or data.
                types[i] == binary_array_type]
        aoyzz__mlz = 'def f(data, str_null_bools=None):\n'
        aoyzz__mlz += '  return ({}{})\n'.format(', '.join(phyn__xupn), ',' if
            iuvw__zan == 1 else '')
        nfuew__folk = {}
        exec(aoyzz__mlz, {'to_list_if_immutable_arr':
            to_list_if_immutable_arr, 'get_str_null_bools':
            get_str_null_bools, 'bodo': bodo}, nfuew__folk)
        zrinh__fihi = nfuew__folk['f']
        return zrinh__fihi
    return lambda data, str_null_bools=None: data


def cp_str_list_to_array(str_arr, str_list, str_null_bools=None):
    return


@overload(cp_str_list_to_array, no_unliteral=True)
def cp_str_list_to_array_overload(str_arr, list_data, str_null_bools=None):
    if str_arr == string_array_type:
        if is_overload_none(str_null_bools):

            def cp_str_list_impl(str_arr, list_data, str_null_bools=None):
                qnhvy__zkfvs = len(list_data)
                for i in range(qnhvy__zkfvs):
                    ucu__njtny = list_data[i]
                    str_arr[i] = ucu__njtny
            return cp_str_list_impl
        else:

            def cp_str_list_impl_null(str_arr, list_data, str_null_bools=None):
                qnhvy__zkfvs = len(list_data)
                for i in range(qnhvy__zkfvs):
                    ucu__njtny = list_data[i]
                    str_arr[i] = ucu__njtny
                    if str_null_bools[i]:
                        str_arr_set_na(str_arr, i)
                    else:
                        str_arr_set_not_na(str_arr, i)
            return cp_str_list_impl_null
    if isinstance(str_arr, types.BaseTuple):
        iuvw__zan = str_arr.count
        spw__osox = 0
        aoyzz__mlz = 'def f(str_arr, list_data, str_null_bools=None):\n'
        for i in range(iuvw__zan):
            if is_overload_true(str_null_bools) and str_arr.types[i
                ] == string_array_type:
                aoyzz__mlz += (
                    '  cp_str_list_to_array(str_arr[{}], list_data[{}], list_data[{}])\n'
                    .format(i, i, iuvw__zan + spw__osox))
                spw__osox += 1
            else:
                aoyzz__mlz += (
                    '  cp_str_list_to_array(str_arr[{}], list_data[{}])\n'.
                    format(i, i))
        aoyzz__mlz += '  return\n'
        nfuew__folk = {}
        exec(aoyzz__mlz, {'cp_str_list_to_array': cp_str_list_to_array},
            nfuew__folk)
        edcw__bzm = nfuew__folk['f']
        return edcw__bzm
    return lambda str_arr, list_data, str_null_bools=None: None


def str_list_to_array(str_list):
    return str_list


@overload(str_list_to_array, no_unliteral=True)
def str_list_to_array_overload(str_list):
    if isinstance(str_list, types.List) and str_list.dtype == bodo.string_type:

        def str_list_impl(str_list):
            qnhvy__zkfvs = len(str_list)
            str_arr = pre_alloc_string_array(qnhvy__zkfvs, -1)
            for i in range(qnhvy__zkfvs):
                ucu__njtny = str_list[i]
                str_arr[i] = ucu__njtny
            return str_arr
        return str_list_impl
    return lambda str_list: str_list


def get_num_total_chars(A):
    pass


@overload(get_num_total_chars)
def overload_get_num_total_chars(A):
    if isinstance(A, types.List) and A.dtype == string_type:

        def str_list_impl(A):
            qnhvy__zkfvs = len(A)
            xbek__keaw = 0
            for i in range(qnhvy__zkfvs):
                ucu__njtny = A[i]
                xbek__keaw += get_utf8_size(ucu__njtny)
            return xbek__keaw
        return str_list_impl
    assert A == string_array_type
    return lambda A: num_total_chars(A)


@overload_method(StringArrayType, 'copy', no_unliteral=True)
def str_arr_copy_overload(arr):

    def copy_impl(arr):
        qnhvy__zkfvs = len(arr)
        n_chars = num_total_chars(arr)
        owzhp__lvocm = pre_alloc_string_array(qnhvy__zkfvs, np.int64(n_chars))
        copy_str_arr_slice(owzhp__lvocm, arr, qnhvy__zkfvs)
        return owzhp__lvocm
    return copy_impl


@overload(len, no_unliteral=True)
def str_arr_len_overload(str_arr):
    if str_arr == string_array_type:

        def str_arr_len(str_arr):
            return str_arr.size
        return str_arr_len


@overload_attribute(StringArrayType, 'size')
def str_arr_size_overload(str_arr):
    return lambda str_arr: len(str_arr._data)


@overload_attribute(StringArrayType, 'shape')
def str_arr_shape_overload(str_arr):
    return lambda str_arr: (str_arr.size,)


@overload_attribute(StringArrayType, 'nbytes')
def str_arr_nbytes_overload(str_arr):
    return lambda str_arr: str_arr._data.nbytes


@overload_method(types.Array, 'tolist', no_unliteral=True)
@overload_method(StringArrayType, 'tolist', no_unliteral=True)
def overload_to_list(arr):
    return lambda arr: list(arr)


import llvmlite.binding as ll
from llvmlite import ir as lir
from bodo.libs import array_ext, hstr_ext
ll.add_symbol('get_str_len', hstr_ext.get_str_len)
ll.add_symbol('setitem_string_array', hstr_ext.setitem_string_array)
ll.add_symbol('is_na', hstr_ext.is_na)
ll.add_symbol('string_array_from_sequence', array_ext.
    string_array_from_sequence)
ll.add_symbol('pd_array_from_string_array', hstr_ext.pd_array_from_string_array
    )
ll.add_symbol('np_array_from_string_array', hstr_ext.np_array_from_string_array
    )
ll.add_symbol('pd_pyarrow_array_from_string_array', hstr_ext.
    pd_pyarrow_array_from_string_array)
ll.add_symbol('convert_len_arr_to_offset32', hstr_ext.
    convert_len_arr_to_offset32)
ll.add_symbol('convert_len_arr_to_offset', hstr_ext.convert_len_arr_to_offset)
ll.add_symbol('set_string_array_range', hstr_ext.set_string_array_range)
ll.add_symbol('str_arr_to_int64', hstr_ext.str_arr_to_int64)
ll.add_symbol('str_arr_to_float64', hstr_ext.str_arr_to_float64)
ll.add_symbol('get_utf8_size', hstr_ext.get_utf8_size)
ll.add_symbol('print_str_arr', hstr_ext.print_str_arr)
ll.add_symbol('inplace_int64_to_str', hstr_ext.inplace_int64_to_str)
ll.add_symbol('str_to_dict_str_array', hstr_ext.str_to_dict_str_array)
inplace_int64_to_str = types.ExternalFunction('inplace_int64_to_str', types
    .void(types.voidptr, types.int64, types.int64))
convert_len_arr_to_offset32 = types.ExternalFunction(
    'convert_len_arr_to_offset32', types.void(types.voidptr, types.intp))
convert_len_arr_to_offset = types.ExternalFunction('convert_len_arr_to_offset',
    types.void(types.voidptr, types.voidptr, types.intp))
setitem_string_array = types.ExternalFunction('setitem_string_array', types
    .void(types.CPointer(offset_type), types.CPointer(char_type), types.
    uint64, types.voidptr, types.intp, offset_type, offset_type, types.intp))
_get_utf8_size = types.ExternalFunction('get_utf8_size', types.intp(types.
    voidptr, types.intp, offset_type))
_print_str_arr = types.ExternalFunction('print_str_arr', types.void(types.
    uint64, types.uint64, types.CPointer(offset_type), types.CPointer(
    char_type)))


@numba.generated_jit(nopython=True)
def empty_str_arr(in_seq):
    aoyzz__mlz = 'def f(in_seq):\n'
    aoyzz__mlz += '    n_strs = len(in_seq)\n'
    aoyzz__mlz += '    A = pre_alloc_string_array(n_strs, -1)\n'
    aoyzz__mlz += '    return A\n'
    nfuew__folk = {}
    exec(aoyzz__mlz, {'pre_alloc_string_array': pre_alloc_string_array},
        nfuew__folk)
    pbbr__qgs = nfuew__folk['f']
    return pbbr__qgs


@numba.generated_jit(nopython=True)
def str_arr_from_sequence(in_seq):
    in_seq = types.unliteral(in_seq)
    if in_seq.dtype == bodo.bytes_type:
        muu__wjyk = 'pre_alloc_binary_array'
    else:
        muu__wjyk = 'pre_alloc_string_array'
    aoyzz__mlz = 'def f(in_seq):\n'
    aoyzz__mlz += '    n_strs = len(in_seq)\n'
    aoyzz__mlz += f'    A = {muu__wjyk}(n_strs, -1)\n'
    aoyzz__mlz += '    for i in range(n_strs):\n'
    aoyzz__mlz += '        A[i] = in_seq[i]\n'
    aoyzz__mlz += '    return A\n'
    nfuew__folk = {}
    exec(aoyzz__mlz, {'pre_alloc_string_array': pre_alloc_string_array,
        'pre_alloc_binary_array': pre_alloc_binary_array}, nfuew__folk)
    pbbr__qgs = nfuew__folk['f']
    return pbbr__qgs


@intrinsic
def set_all_offsets_to_0(typingctx, arr_typ=None):
    assert arr_typ in (string_array_type, binary_array_type
        ), 'set_all_offsets_to_0 requires a string or binary array'

    def codegen(context, builder, sig, args):
        in_str_arr, = args
        alg__tbz = _get_str_binary_arr_payload(context, builder, in_str_arr,
            sig.args[0])
        ddoo__unoms = builder.add(alg__tbz.n_arrays, lir.Constant(lir.
            IntType(64), 1))
        sux__dwmj = builder.lshr(lir.Constant(lir.IntType(64), offset_type.
            bitwidth), lir.Constant(lir.IntType(64), 3))
        aqc__wfoaq = builder.mul(ddoo__unoms, sux__dwmj)
        djij__hsss = context.make_array(offset_arr_type)(context, builder,
            alg__tbz.offsets).data
        cgutils.memset(builder, djij__hsss, aqc__wfoaq, 0)
        return context.get_dummy_value()
    return types.none(arr_typ), codegen


@intrinsic
def set_bitmap_all_NA(typingctx, arr_typ=None):
    assert arr_typ in (string_array_type, binary_array_type
        ), 'set_bitmap_all_NA requires a string or binary array'

    def codegen(context, builder, sig, args):
        in_str_arr, = args
        alg__tbz = _get_str_binary_arr_payload(context, builder, in_str_arr,
            sig.args[0])
        jrk__ftj = alg__tbz.n_arrays
        aqc__wfoaq = builder.lshr(builder.add(jrk__ftj, lir.Constant(lir.
            IntType(64), 7)), lir.Constant(lir.IntType(64), 3))
        qcxx__ccwcp = context.make_array(null_bitmap_arr_type)(context,
            builder, alg__tbz.null_bitmap).data
        cgutils.memset(builder, qcxx__ccwcp, aqc__wfoaq, 0)
        return context.get_dummy_value()
    return types.none(arr_typ), codegen


@numba.njit
def pre_alloc_string_array(n_strs, n_chars):
    if n_chars is None:
        n_chars = -1
    str_arr = init_str_arr(bodo.libs.array_item_arr_ext.
        pre_alloc_array_item_array(np.int64(n_strs), (np.int64(n_chars),),
        char_arr_type))
    if n_chars == 0:
        set_all_offsets_to_0(str_arr)
    return str_arr


@register_jitable
def gen_na_str_array_lens(n_strs, total_len, len_arr):
    str_arr = pre_alloc_string_array(n_strs, total_len)
    set_bitmap_all_NA(str_arr)
    offsets = bodo.libs.array_item_arr_ext.get_offsets(str_arr._data)
    trblq__qypwx = 0
    if total_len == 0:
        for i in range(len(offsets)):
            offsets[i] = 0
    else:
        izkm__uggu = len(len_arr)
        for i in range(izkm__uggu):
            offsets[i] = trblq__qypwx
            trblq__qypwx += len_arr[i]
        offsets[izkm__uggu] = trblq__qypwx
    return str_arr


kBitmask = np.array([1, 2, 4, 8, 16, 32, 64, 128], dtype=np.uint8)


@numba.njit
def set_bit_to(bits, i, bit_is_set):
    mqule__pvrn = i // 8
    tjk__kbhg = getitem_str_bitmap(bits, mqule__pvrn)
    tjk__kbhg ^= np.uint8(-np.uint8(bit_is_set) ^ tjk__kbhg) & kBitmask[i % 8]
    setitem_str_bitmap(bits, mqule__pvrn, tjk__kbhg)


@numba.njit
def get_bit_bitmap(bits, i):
    return getitem_str_bitmap(bits, i >> 3) >> (i & 7) & 1


@numba.njit
def copy_nulls_range(out_str_arr, in_str_arr, out_start):
    deria__iaou = get_null_bitmap_ptr(out_str_arr)
    znf__jrlu = get_null_bitmap_ptr(in_str_arr)
    for j in range(len(in_str_arr)):
        fevj__tnw = get_bit_bitmap(znf__jrlu, j)
        set_bit_to(deria__iaou, out_start + j, fevj__tnw)


@intrinsic
def set_string_array_range(typingctx, out_typ, in_typ, curr_str_typ,
    curr_chars_typ=None):
    assert out_typ == string_array_type and in_typ == string_array_type or out_typ == binary_array_type and in_typ == binary_array_type, 'set_string_array_range requires string or binary arrays'
    assert isinstance(curr_str_typ, types.Integer) and isinstance(
        curr_chars_typ, types.Integer
        ), 'set_string_array_range requires integer indices'

    def codegen(context, builder, sig, args):
        out_arr, iyin__afsez, znssp__lox, xcxb__mxggr = args
        xmfz__svw = _get_str_binary_arr_payload(context, builder,
            iyin__afsez, string_array_type)
        uxb__nolp = _get_str_binary_arr_payload(context, builder, out_arr,
            string_array_type)
        dlic__egz = context.make_helper(builder, offset_arr_type, xmfz__svw
            .offsets).data
        scnxq__sjw = context.make_helper(builder, offset_arr_type,
            uxb__nolp.offsets).data
        mlw__nldey = context.make_helper(builder, char_arr_type, xmfz__svw.data
            ).data
        mwovb__hxue = context.make_helper(builder, char_arr_type, uxb__nolp
            .data).data
        num_total_chars = _get_num_total_chars(builder, dlic__egz,
            xmfz__svw.n_arrays)
        uliu__fdrzz = lir.FunctionType(lir.VoidType(), [lir.IntType(
            offset_type.bitwidth).as_pointer(), lir.IntType(8).as_pointer(),
            lir.IntType(offset_type.bitwidth).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(64), lir.IntType(64), lir.IntType(64),
            lir.IntType(64)])
        nblz__mjrw = cgutils.get_or_insert_function(builder.module,
            uliu__fdrzz, name='set_string_array_range')
        builder.call(nblz__mjrw, [scnxq__sjw, mwovb__hxue, dlic__egz,
            mlw__nldey, znssp__lox, xcxb__mxggr, xmfz__svw.n_arrays,
            num_total_chars])
        sbkea__hpf = context.typing_context.resolve_value_type(copy_nulls_range
            )
        gkfe__wyosz = sbkea__hpf.get_call_type(context.typing_context, (
            string_array_type, string_array_type, types.int64), {})
        jez__ipw = context.get_function(sbkea__hpf, gkfe__wyosz)
        jez__ipw(builder, (out_arr, iyin__afsez, znssp__lox))
        return context.get_dummy_value()
    sig = types.void(out_typ, in_typ, types.intp, types.intp)
    return sig, codegen


@box(BinaryArrayType)
@box(StringArrayType)
def box_str_arr(typ, val, c):
    assert typ in [binary_array_type, string_array_type]
    yuao__haehv = c.context.make_helper(c.builder, typ, val)
    olx__pdokq = ArrayItemArrayType(char_arr_type)
    alg__tbz = _get_array_item_arr_payload(c.context, c.builder, olx__pdokq,
        yuao__haehv.data)
    wpeqp__jxd = c.context.get_constant(types.int32, int(typ ==
        binary_array_type))
    kgv__jsgk = 'np_array_from_string_array'
    if use_pd_string_array and typ != binary_array_type:
        kgv__jsgk = 'pd_array_from_string_array'
    if use_pd_pyarrow_string_array and typ != binary_array_type:
        from bodo.libs.array import array_info_type, array_to_info_codegen
        frk__mfhv = array_to_info_codegen(c.context, c.builder,
            array_info_type(typ), (val,), incref=False)
        uliu__fdrzz = lir.FunctionType(c.pyapi.pyobj, [lir.IntType(8).
            as_pointer()])
        kgv__jsgk = 'pd_pyarrow_array_from_string_array'
        vhr__vbkgj = cgutils.get_or_insert_function(c.builder.module,
            uliu__fdrzz, name=kgv__jsgk)
        arr = c.builder.call(vhr__vbkgj, [frk__mfhv])
        c.context.nrt.decref(c.builder, typ, val)
        return arr
    uliu__fdrzz = lir.FunctionType(c.context.get_argument_type(types.
        pyobject), [lir.IntType(64), lir.IntType(offset_type.bitwidth).
        as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(8).
        as_pointer(), lir.IntType(32)])
    vhr__vbkgj = cgutils.get_or_insert_function(c.builder.module,
        uliu__fdrzz, name=kgv__jsgk)
    uywh__bsgox = c.context.make_array(offset_arr_type)(c.context, c.
        builder, alg__tbz.offsets).data
    emd__ptav = c.context.make_array(char_arr_type)(c.context, c.builder,
        alg__tbz.data).data
    qcxx__ccwcp = c.context.make_array(null_bitmap_arr_type)(c.context, c.
        builder, alg__tbz.null_bitmap).data
    arr = c.builder.call(vhr__vbkgj, [alg__tbz.n_arrays, uywh__bsgox,
        emd__ptav, qcxx__ccwcp, wpeqp__jxd])
    c.context.nrt.decref(c.builder, typ, val)
    return arr


@intrinsic
def str_arr_is_na(typingctx, str_arr_typ, ind_typ=None):
    assert str_arr_typ in (string_array_type, binary_array_type
        ), 'str_arr_is_na: string/binary array expected'

    def codegen(context, builder, sig, args):
        in_str_arr, ind = args
        alg__tbz = _get_str_binary_arr_payload(context, builder, in_str_arr,
            str_arr_typ)
        qcxx__ccwcp = context.make_array(null_bitmap_arr_type)(context,
            builder, alg__tbz.null_bitmap).data
        vvwfa__itzbi = builder.lshr(ind, lir.Constant(lir.IntType(64), 3))
        euqn__azmjw = builder.urem(ind, lir.Constant(lir.IntType(64), 8))
        tjk__kbhg = builder.load(builder.gep(qcxx__ccwcp, [vvwfa__itzbi],
            inbounds=True))
        ena__zvtg = lir.ArrayType(lir.IntType(8), 8)
        ktkye__dhdbm = cgutils.alloca_once_value(builder, lir.Constant(
            ena__zvtg, (1, 2, 4, 8, 16, 32, 64, 128)))
        ecaj__vyp = builder.load(builder.gep(ktkye__dhdbm, [lir.Constant(
            lir.IntType(64), 0), euqn__azmjw], inbounds=True))
        return builder.icmp_unsigned('==', builder.and_(tjk__kbhg,
            ecaj__vyp), lir.Constant(lir.IntType(8), 0))
    return types.bool_(str_arr_typ, types.intp), codegen


@intrinsic
def str_arr_set_na(typingctx, str_arr_typ, ind_typ=None):
    assert str_arr_typ in [string_array_type, binary_array_type
        ], 'str_arr_set_na: string/binary array expected'

    def codegen(context, builder, sig, args):
        in_str_arr, ind = args
        alg__tbz = _get_str_binary_arr_payload(context, builder, in_str_arr,
            str_arr_typ)
        vvwfa__itzbi = builder.lshr(ind, lir.Constant(lir.IntType(64), 3))
        euqn__azmjw = builder.urem(ind, lir.Constant(lir.IntType(64), 8))
        qcxx__ccwcp = context.make_array(null_bitmap_arr_type)(context,
            builder, alg__tbz.null_bitmap).data
        offsets = context.make_helper(builder, offset_arr_type, alg__tbz.
            offsets).data
        kbbn__zlp = builder.gep(qcxx__ccwcp, [vvwfa__itzbi], inbounds=True)
        tjk__kbhg = builder.load(kbbn__zlp)
        ena__zvtg = lir.ArrayType(lir.IntType(8), 8)
        ktkye__dhdbm = cgutils.alloca_once_value(builder, lir.Constant(
            ena__zvtg, (1, 2, 4, 8, 16, 32, 64, 128)))
        ecaj__vyp = builder.load(builder.gep(ktkye__dhdbm, [lir.Constant(
            lir.IntType(64), 0), euqn__azmjw], inbounds=True))
        ecaj__vyp = builder.xor(ecaj__vyp, lir.Constant(lir.IntType(8), -1))
        builder.store(builder.and_(tjk__kbhg, ecaj__vyp), kbbn__zlp)
        oqm__lktos = builder.add(ind, lir.Constant(lir.IntType(64), 1))
        erk__viuh = builder.icmp_unsigned('!=', oqm__lktos, alg__tbz.n_arrays)
        with builder.if_then(erk__viuh):
            builder.store(builder.load(builder.gep(offsets, [ind])),
                builder.gep(offsets, [oqm__lktos]))
        return context.get_dummy_value()
    return types.void(str_arr_typ, types.intp), codegen


@intrinsic
def str_arr_set_not_na(typingctx, str_arr_typ, ind_typ=None):
    assert str_arr_typ in [binary_array_type, string_array_type
        ], 'str_arr_set_not_na: string/binary array expected'

    def codegen(context, builder, sig, args):
        in_str_arr, ind = args
        alg__tbz = _get_str_binary_arr_payload(context, builder, in_str_arr,
            str_arr_typ)
        vvwfa__itzbi = builder.lshr(ind, lir.Constant(lir.IntType(64), 3))
        euqn__azmjw = builder.urem(ind, lir.Constant(lir.IntType(64), 8))
        qcxx__ccwcp = context.make_array(null_bitmap_arr_type)(context,
            builder, alg__tbz.null_bitmap).data
        kbbn__zlp = builder.gep(qcxx__ccwcp, [vvwfa__itzbi], inbounds=True)
        tjk__kbhg = builder.load(kbbn__zlp)
        ena__zvtg = lir.ArrayType(lir.IntType(8), 8)
        ktkye__dhdbm = cgutils.alloca_once_value(builder, lir.Constant(
            ena__zvtg, (1, 2, 4, 8, 16, 32, 64, 128)))
        ecaj__vyp = builder.load(builder.gep(ktkye__dhdbm, [lir.Constant(
            lir.IntType(64), 0), euqn__azmjw], inbounds=True))
        builder.store(builder.or_(tjk__kbhg, ecaj__vyp), kbbn__zlp)
        return context.get_dummy_value()
    return types.void(str_arr_typ, types.intp), codegen


@intrinsic
def set_null_bits_to_value(typingctx, arr_typ, value_typ=None):
    assert (arr_typ == string_array_type or arr_typ == binary_array_type
        ) and is_overload_constant_int(value_typ)

    def codegen(context, builder, sig, args):
        in_str_arr, value = args
        alg__tbz = _get_str_binary_arr_payload(context, builder, in_str_arr,
            string_array_type)
        aqc__wfoaq = builder.udiv(builder.add(alg__tbz.n_arrays, lir.
            Constant(lir.IntType(64), 7)), lir.Constant(lir.IntType(64), 8))
        qcxx__ccwcp = context.make_array(null_bitmap_arr_type)(context,
            builder, alg__tbz.null_bitmap).data
        cgutils.memset(builder, qcxx__ccwcp, aqc__wfoaq, value)
        return context.get_dummy_value()
    return types.none(arr_typ, types.int8), codegen


def _get_str_binary_arr_data_payload_ptr(context, builder, str_arr):
    yjs__dbm = context.make_helper(builder, string_array_type, str_arr)
    olx__pdokq = ArrayItemArrayType(char_arr_type)
    muj__uufsp = context.make_helper(builder, olx__pdokq, yjs__dbm.data)
    uan__qfe = ArrayItemArrayPayloadType(olx__pdokq)
    zln__aon = context.nrt.meminfo_data(builder, muj__uufsp.meminfo)
    jbryt__vzzy = builder.bitcast(zln__aon, context.get_value_type(uan__qfe
        ).as_pointer())
    return jbryt__vzzy


@intrinsic
def move_str_binary_arr_payload(typingctx, to_arr_typ, from_arr_typ=None):
    assert to_arr_typ == string_array_type and from_arr_typ == string_array_type or to_arr_typ == binary_array_type and from_arr_typ == binary_array_type

    def codegen(context, builder, sig, args):
        bpml__ocsdr, dse__fhxna = args
        qfhe__xnxhx = _get_str_binary_arr_data_payload_ptr(context, builder,
            dse__fhxna)
        qgy__zbw = _get_str_binary_arr_data_payload_ptr(context, builder,
            bpml__ocsdr)
        eumd__dcpu = _get_str_binary_arr_payload(context, builder,
            dse__fhxna, sig.args[1])
        ilsq__flj = _get_str_binary_arr_payload(context, builder,
            bpml__ocsdr, sig.args[0])
        context.nrt.incref(builder, char_arr_type, eumd__dcpu.data)
        context.nrt.incref(builder, offset_arr_type, eumd__dcpu.offsets)
        context.nrt.incref(builder, null_bitmap_arr_type, eumd__dcpu.
            null_bitmap)
        context.nrt.decref(builder, char_arr_type, ilsq__flj.data)
        context.nrt.decref(builder, offset_arr_type, ilsq__flj.offsets)
        context.nrt.decref(builder, null_bitmap_arr_type, ilsq__flj.null_bitmap
            )
        builder.store(builder.load(qfhe__xnxhx), qgy__zbw)
        return context.get_dummy_value()
    return types.none(to_arr_typ, from_arr_typ), codegen


dummy_use = numba.njit(lambda a: None)


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def get_utf8_size(s):
    if isinstance(s, types.StringLiteral):
        l = len(s.literal_value.encode())
        return lambda s: l

    def impl(s):
        if s is None:
            return 0
        s = bodo.utils.indexing.unoptional(s)
        if s._is_ascii == 1:
            return len(s)
        qnhvy__zkfvs = _get_utf8_size(s._data, s._length, s._kind)
        dummy_use(s)
        return qnhvy__zkfvs
    return impl


@intrinsic
def setitem_str_arr_ptr(typingctx, str_arr_t, ind_t, ptr_t, len_t=None):

    def codegen(context, builder, sig, args):
        arr, ind, asx__vavez, usyzt__atyf = args
        alg__tbz = _get_str_binary_arr_payload(context, builder, arr, sig.
            args[0])
        offsets = context.make_helper(builder, offset_arr_type, alg__tbz.
            offsets).data
        data = context.make_helper(builder, char_arr_type, alg__tbz.data).data
        uliu__fdrzz = lir.FunctionType(lir.VoidType(), [lir.IntType(
            offset_type.bitwidth).as_pointer(), lir.IntType(8).as_pointer(),
            lir.IntType(64), lir.IntType(8).as_pointer(), lir.IntType(64),
            lir.IntType(32), lir.IntType(32), lir.IntType(64)])
        qmlfq__lrp = cgutils.get_or_insert_function(builder.module,
            uliu__fdrzz, name='setitem_string_array')
        uewy__jauh = context.get_constant(types.int32, -1)
        kwp__fghj = context.get_constant(types.int32, 1)
        num_total_chars = _get_num_total_chars(builder, offsets, alg__tbz.
            n_arrays)
        builder.call(qmlfq__lrp, [offsets, data, num_total_chars, builder.
            extract_value(asx__vavez, 0), usyzt__atyf, uewy__jauh,
            kwp__fghj, ind])
        return context.get_dummy_value()
    return types.void(str_arr_t, ind_t, ptr_t, len_t), codegen


def lower_is_na(context, builder, bull_bitmap, ind):
    uliu__fdrzz = lir.FunctionType(lir.IntType(1), [lir.IntType(8).
        as_pointer(), lir.IntType(64)])
    lsg__yqez = cgutils.get_or_insert_function(builder.module, uliu__fdrzz,
        name='is_na')
    return builder.call(lsg__yqez, [bull_bitmap, ind])


@intrinsic
def _memcpy(typingctx, dest_t, src_t, count_t, item_size_t=None):

    def codegen(context, builder, sig, args):
        ehif__ejlu, aeh__umh, iuvw__zan, puifu__gqh = args
        cgutils.raw_memcpy(builder, ehif__ejlu, aeh__umh, iuvw__zan, puifu__gqh
            )
        return context.get_dummy_value()
    return types.void(types.voidptr, types.voidptr, types.intp, types.intp
        ), codegen


@numba.njit
def print_str_arr(arr):
    _print_str_arr(num_strings(arr), num_total_chars(arr), get_offset_ptr(
        arr), get_data_ptr(arr))


def inplace_eq(A, i, val):
    return A[i] == val


@overload(inplace_eq)
def inplace_eq_overload(A, ind, val):

    def impl(A, ind, val):
        txdxw__iegi, kepgr__vurce = unicode_to_utf8_and_len(val)
        eqete__akl = getitem_str_offset(A, ind)
        jcs__dnuxj = getitem_str_offset(A, ind + 1)
        yqvfu__kdwe = jcs__dnuxj - eqete__akl
        if yqvfu__kdwe != kepgr__vurce:
            return False
        asx__vavez = get_data_ptr_ind(A, eqete__akl)
        return memcmp(asx__vavez, txdxw__iegi, kepgr__vurce) == 0
    return impl


def str_arr_setitem_int_to_str(A, ind, value):
    A[ind] = str(value)


@overload(str_arr_setitem_int_to_str)
def overload_str_arr_setitem_int_to_str(A, ind, val):

    def impl(A, ind, val):
        eqete__akl = getitem_str_offset(A, ind)
        yqvfu__kdwe = bodo.libs.str_ext.int_to_str_len(val)
        qjvc__osk = eqete__akl + yqvfu__kdwe
        bodo.libs.array_item_arr_ext.ensure_data_capacity(A._data,
            eqete__akl, qjvc__osk)
        asx__vavez = get_data_ptr_ind(A, eqete__akl)
        inplace_int64_to_str(asx__vavez, yqvfu__kdwe, val)
        setitem_str_offset(A, ind + 1, eqete__akl + yqvfu__kdwe)
        str_arr_set_not_na(A, ind)
    return impl


@intrinsic
def inplace_set_NA_str(typingctx, ptr_typ=None):

    def codegen(context, builder, sig, args):
        asx__vavez, = args
        ziky__kuqb = context.insert_const_string(builder.module, '<NA>')
        fylc__axf = lir.Constant(lir.IntType(64), len('<NA>'))
        cgutils.raw_memcpy(builder, asx__vavez, ziky__kuqb, fylc__axf, 1)
    return types.none(types.voidptr), codegen


def str_arr_setitem_NA_str(A, ind):
    A[ind] = '<NA>'


@overload(str_arr_setitem_NA_str)
def overload_str_arr_setitem_NA_str(A, ind):
    jri__bda = len('<NA>')

    def impl(A, ind):
        eqete__akl = getitem_str_offset(A, ind)
        qjvc__osk = eqete__akl + jri__bda
        bodo.libs.array_item_arr_ext.ensure_data_capacity(A._data,
            eqete__akl, qjvc__osk)
        asx__vavez = get_data_ptr_ind(A, eqete__akl)
        inplace_set_NA_str(asx__vavez)
        setitem_str_offset(A, ind + 1, eqete__akl + jri__bda)
        str_arr_set_not_na(A, ind)
    return impl


@overload(operator.getitem, no_unliteral=True)
def str_arr_getitem_int(A, ind):
    if A != string_array_type:
        return
    if isinstance(ind, types.Integer):

        def str_arr_getitem_impl(A, ind):
            if ind < 0:
                ind += A.size
            eqete__akl = getitem_str_offset(A, ind)
            jcs__dnuxj = getitem_str_offset(A, ind + 1)
            usyzt__atyf = jcs__dnuxj - eqete__akl
            asx__vavez = get_data_ptr_ind(A, eqete__akl)
            kimf__qcc = decode_utf8(asx__vavez, usyzt__atyf)
            return kimf__qcc
        return str_arr_getitem_impl
    if ind != bodo.boolean_array and is_list_like_index_type(ind
        ) and ind.dtype == types.bool_:

        def bool_impl(A, ind):
            ind = bodo.utils.conversion.coerce_to_array(ind)
            qnhvy__zkfvs = len(A)
            n_strs = 0
            n_chars = 0
            for i in range(qnhvy__zkfvs):
                if not bodo.libs.array_kernels.isna(ind, i) and ind[i]:
                    n_strs += 1
                    n_chars += get_str_arr_item_length(A, i)
            out_arr = pre_alloc_string_array(n_strs, n_chars)
            hopjr__tcbv = get_data_ptr(out_arr).data
            nzbbd__vqdni = get_data_ptr(A).data
            spw__osox = 0
            uti__wzbse = 0
            setitem_str_offset(out_arr, 0, 0)
            for i in range(qnhvy__zkfvs):
                if not bodo.libs.array_kernels.isna(ind, i) and ind[i]:
                    oua__tzuvq = get_str_arr_item_length(A, i)
                    if oua__tzuvq == 0:
                        pass
                    elif oua__tzuvq == 1:
                        copy_single_char(hopjr__tcbv, uti__wzbse,
                            nzbbd__vqdni, getitem_str_offset(A, i))
                    else:
                        memcpy_region(hopjr__tcbv, uti__wzbse, nzbbd__vqdni,
                            getitem_str_offset(A, i), oua__tzuvq, 1)
                    uti__wzbse += oua__tzuvq
                    setitem_str_offset(out_arr, spw__osox + 1, uti__wzbse)
                    if str_arr_is_na(A, i):
                        str_arr_set_na(out_arr, spw__osox)
                    else:
                        str_arr_set_not_na(out_arr, spw__osox)
                    spw__osox += 1
            return out_arr
        return bool_impl
    if is_list_like_index_type(ind) and isinstance(ind.dtype, types.Integer):

        def str_arr_arr_impl(A, ind):
            ind = bodo.utils.conversion.coerce_to_array(ind)
            qnhvy__zkfvs = len(ind)
            n_chars = 0
            for i in range(qnhvy__zkfvs):
                n_chars += get_str_arr_item_length(A, ind[i])
            out_arr = pre_alloc_string_array(qnhvy__zkfvs, n_chars)
            hopjr__tcbv = get_data_ptr(out_arr).data
            nzbbd__vqdni = get_data_ptr(A).data
            uti__wzbse = 0
            setitem_str_offset(out_arr, 0, 0)
            for i in range(qnhvy__zkfvs):
                if bodo.libs.array_kernels.isna(ind, i):
                    raise ValueError(
                        'Cannot index with an integer indexer containing NA values'
                        )
                hwobf__aug = ind[i]
                oua__tzuvq = get_str_arr_item_length(A, hwobf__aug)
                if oua__tzuvq == 0:
                    pass
                elif oua__tzuvq == 1:
                    copy_single_char(hopjr__tcbv, uti__wzbse, nzbbd__vqdni,
                        getitem_str_offset(A, hwobf__aug))
                else:
                    memcpy_region(hopjr__tcbv, uti__wzbse, nzbbd__vqdni,
                        getitem_str_offset(A, hwobf__aug), oua__tzuvq, 1)
                uti__wzbse += oua__tzuvq
                setitem_str_offset(out_arr, i + 1, uti__wzbse)
                if str_arr_is_na(A, hwobf__aug):
                    str_arr_set_na(out_arr, i)
                else:
                    str_arr_set_not_na(out_arr, i)
            return out_arr
        return str_arr_arr_impl
    if isinstance(ind, types.SliceType):

        def str_arr_slice_impl(A, ind):
            qnhvy__zkfvs = len(A)
            mngva__axln = numba.cpython.unicode._normalize_slice(ind,
                qnhvy__zkfvs)
            fccm__eodxh = numba.cpython.unicode._slice_span(mngva__axln)
            if mngva__axln.step == 1:
                eqete__akl = getitem_str_offset(A, mngva__axln.start)
                jcs__dnuxj = getitem_str_offset(A, mngva__axln.stop)
                n_chars = jcs__dnuxj - eqete__akl
                owzhp__lvocm = pre_alloc_string_array(fccm__eodxh, np.int64
                    (n_chars))
                for i in range(fccm__eodxh):
                    owzhp__lvocm[i] = A[mngva__axln.start + i]
                    if str_arr_is_na(A, mngva__axln.start + i):
                        str_arr_set_na(owzhp__lvocm, i)
                return owzhp__lvocm
            else:
                owzhp__lvocm = pre_alloc_string_array(fccm__eodxh, -1)
                for i in range(fccm__eodxh):
                    owzhp__lvocm[i] = A[mngva__axln.start + i * mngva__axln
                        .step]
                    if str_arr_is_na(A, mngva__axln.start + i * mngva__axln
                        .step):
                        str_arr_set_na(owzhp__lvocm, i)
                return owzhp__lvocm
        return str_arr_slice_impl
    if ind != bodo.boolean_array:
        raise BodoError(
            f'getitem for StringArray with indexing type {ind} not supported.')


dummy_use = numba.njit(lambda a: None)


@overload(operator.setitem)
def str_arr_setitem(A, idx, val):
    if A != string_array_type:
        return
    if val == types.none or isinstance(val, types.optional):
        return
    uiq__zvd = (
        f'StringArray setitem with index {idx} and value {val} not supported yet.'
        )
    if isinstance(idx, types.Integer):
        if val != string_type:
            raise BodoError(uiq__zvd)
        erjw__aws = 4

        def impl_scalar(A, idx, val):
            cnkz__wprso = (val._length if val._is_ascii else erjw__aws *
                val._length)
            khgaa__bmux = A._data
            eqete__akl = np.int64(getitem_str_offset(A, idx))
            qjvc__osk = eqete__akl + cnkz__wprso
            bodo.libs.array_item_arr_ext.ensure_data_capacity(khgaa__bmux,
                eqete__akl, qjvc__osk)
            setitem_string_array(get_offset_ptr(A), get_data_ptr(A),
                qjvc__osk, val._data, val._length, val._kind, val._is_ascii,
                idx)
            str_arr_set_not_na(A, idx)
            dummy_use(A)
            dummy_use(val)
        return impl_scalar
    if isinstance(idx, types.SliceType):
        if val == string_array_type:

            def impl_slice(A, idx, val):
                mngva__axln = numba.cpython.unicode._normalize_slice(idx,
                    len(A))
                gsvpy__indt = mngva__axln.start
                khgaa__bmux = A._data
                eqete__akl = np.int64(getitem_str_offset(A, gsvpy__indt))
                qjvc__osk = eqete__akl + np.int64(num_total_chars(val))
                bodo.libs.array_item_arr_ext.ensure_data_capacity(khgaa__bmux,
                    eqete__akl, qjvc__osk)
                set_string_array_range(A, val, gsvpy__indt, eqete__akl)
                awt__zzww = 0
                for i in range(mngva__axln.start, mngva__axln.stop,
                    mngva__axln.step):
                    if str_arr_is_na(val, awt__zzww):
                        str_arr_set_na(A, i)
                    else:
                        str_arr_set_not_na(A, i)
                    awt__zzww += 1
            return impl_slice
        elif isinstance(val, types.List) and val.dtype == string_type:

            def impl_slice_list(A, idx, val):
                hxll__wmven = str_list_to_array(val)
                A[idx] = hxll__wmven
            return impl_slice_list
        elif val == string_type:

            def impl_slice(A, idx, val):
                mngva__axln = numba.cpython.unicode._normalize_slice(idx,
                    len(A))
                for i in range(mngva__axln.start, mngva__axln.stop,
                    mngva__axln.step):
                    A[i] = val
            return impl_slice
        else:
            raise BodoError(uiq__zvd)
    if is_list_like_index_type(idx) and idx.dtype == types.bool_:
        if val == string_type:

            def impl_bool_scalar(A, idx, val):
                qnhvy__zkfvs = len(A)
                idx = bodo.utils.conversion.coerce_to_array(idx)
                out_arr = pre_alloc_string_array(qnhvy__zkfvs, -1)
                for i in numba.parfors.parfor.internal_prange(qnhvy__zkfvs):
                    if not bodo.libs.array_kernels.isna(idx, i) and idx[i]:
                        out_arr[i] = val
                    elif bodo.libs.array_kernels.isna(A, i):
                        out_arr[i] = ''
                        str_arr_set_na(out_arr, i)
                    else:
                        get_str_arr_item_copy(out_arr, i, A, i)
                move_str_binary_arr_payload(A, out_arr)
            return impl_bool_scalar
        elif val == string_array_type or isinstance(val, types.Array
            ) and isinstance(val.dtype, types.UnicodeCharSeq):

            def impl_bool_arr(A, idx, val):
                qnhvy__zkfvs = len(A)
                idx = bodo.utils.conversion.coerce_to_array(idx,
                    use_nullable_array=True)
                out_arr = pre_alloc_string_array(qnhvy__zkfvs, -1)
                qkzyl__gvqxs = 0
                for i in numba.parfors.parfor.internal_prange(qnhvy__zkfvs):
                    if not bodo.libs.array_kernels.isna(idx, i) and idx[i]:
                        if bodo.libs.array_kernels.isna(val, qkzyl__gvqxs):
                            out_arr[i] = ''
                            str_arr_set_na(out_arr, qkzyl__gvqxs)
                        else:
                            out_arr[i] = str(val[qkzyl__gvqxs])
                        qkzyl__gvqxs += 1
                    elif bodo.libs.array_kernels.isna(A, i):
                        out_arr[i] = ''
                        str_arr_set_na(out_arr, i)
                    else:
                        get_str_arr_item_copy(out_arr, i, A, i)
                move_str_binary_arr_payload(A, out_arr)
            return impl_bool_arr
        else:
            raise BodoError(uiq__zvd)
    raise BodoError(uiq__zvd)


@overload_attribute(StringArrayType, 'dtype')
def overload_str_arr_dtype(A):
    return lambda A: pd.StringDtype()


@overload_attribute(StringArrayType, 'ndim')
def overload_str_arr_ndim(A):
    return lambda A: 1


@overload_method(StringArrayType, 'astype', no_unliteral=True)
def overload_str_arr_astype(A, dtype, copy=True):
    if dtype == types.unicode_type:
        raise_bodo_error(
            "StringArray.astype(): 'dtype' when passed as string must be a constant value"
            )
    if isinstance(dtype, types.Function) and dtype.key[0] == str:
        return lambda A, dtype, copy=True: A
    pxqz__bvy = parse_dtype(dtype, 'StringArray.astype')
    if A == pxqz__bvy:
        return lambda A, dtype, copy=True: A
    if not isinstance(pxqz__bvy, (types.Float, types.Integer)
        ) and pxqz__bvy not in (types.bool_, bodo.libs.bool_arr_ext.
        boolean_dtype, bodo.dict_str_arr_type):
        raise BodoError('invalid dtype in StringArray.astype()')
    if isinstance(pxqz__bvy, types.Float):

        def impl_float(A, dtype, copy=True):
            numba.parfors.parfor.init_prange()
            qnhvy__zkfvs = len(A)
            B = np.empty(qnhvy__zkfvs, pxqz__bvy)
            for i in numba.parfors.parfor.internal_prange(qnhvy__zkfvs):
                if bodo.libs.array_kernels.isna(A, i):
                    B[i] = np.nan
                else:
                    B[i] = float(A[i])
            return B
        return impl_float
    elif pxqz__bvy == types.bool_:

        def impl_bool(A, dtype, copy=True):
            numba.parfors.parfor.init_prange()
            qnhvy__zkfvs = len(A)
            B = np.empty(qnhvy__zkfvs, pxqz__bvy)
            for i in numba.parfors.parfor.internal_prange(qnhvy__zkfvs):
                if bodo.libs.array_kernels.isna(A, i):
                    B[i] = False
                else:
                    B[i] = bool(A[i])
            return B
        return impl_bool
    elif pxqz__bvy == bodo.libs.bool_arr_ext.boolean_dtype:

        def impl_bool(A, dtype, copy=True):
            numba.parfors.parfor.init_prange()
            qnhvy__zkfvs = len(A)
            B = np.empty(qnhvy__zkfvs, pxqz__bvy)
            for i in numba.parfors.parfor.internal_prange(qnhvy__zkfvs):
                if bodo.libs.array_kernels.isna(A, i):
                    bodo.libs.array_kernels.setna(B, i)
                else:
                    B[i] = bool(A[i])
            return B
        return impl_bool
    elif pxqz__bvy == bodo.dict_str_arr_type:

        def impl_dict_str(A, dtype, copy=True):
            return str_arr_to_dict_str_arr(A)
        return impl_dict_str
    else:

        def impl_int(A, dtype, copy=True):
            numba.parfors.parfor.init_prange()
            qnhvy__zkfvs = len(A)
            B = np.empty(qnhvy__zkfvs, pxqz__bvy)
            for i in numba.parfors.parfor.internal_prange(qnhvy__zkfvs):
                B[i] = int(A[i])
            return B
        return impl_int


@numba.jit
def str_arr_to_dict_str_arr(A):
    return str_arr_to_dict_str_arr_cpp(A)


@intrinsic
def str_arr_to_dict_str_arr_cpp(typingctx, str_arr_t):

    def codegen(context, builder, sig, args):
        str_arr, = args
        hwr__gwmxj = bodo.libs.array.array_to_info_codegen(context, builder,
            bodo.libs.array.array_info_type(sig.args[0]), (str_arr,), False)
        uliu__fdrzz = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer()])
        ibbzm__pqkpc = cgutils.get_or_insert_function(builder.module,
            uliu__fdrzz, name='str_to_dict_str_array')
        mpgqj__zedjb = builder.call(ibbzm__pqkpc, [hwr__gwmxj])
        bodo.utils.utils.inlined_check_and_propagate_cpp_exception(context,
            builder)
        wgkvl__jwm = bodo.libs.array.info_to_array_codegen(context, builder,
            sig.return_type(bodo.libs.array.array_info_type, sig.
            return_type), (mpgqj__zedjb, context.get_constant_null(sig.
            return_type)))
        return wgkvl__jwm
    assert str_arr_t == bodo.string_array_type, 'str_arr_to_dict_str_arr: Input Array is not a Bodo String Array'
    sig = bodo.dict_str_arr_type(bodo.string_array_type)
    return sig, codegen


@intrinsic
def decode_utf8(typingctx, ptr_t, len_t=None):

    def codegen(context, builder, sig, args):
        asx__vavez, usyzt__atyf = args
        cgwr__lgetg = context.get_python_api(builder)
        sgls__cni = cgwr__lgetg.string_from_string_and_size(asx__vavez,
            usyzt__atyf)
        hobr__yonpl = cgwr__lgetg.to_native_value(string_type, sgls__cni).value
        mtu__dygup = cgutils.create_struct_proxy(string_type)(context,
            builder, hobr__yonpl)
        mtu__dygup.hash = mtu__dygup.hash.type(-1)
        cgwr__lgetg.decref(sgls__cni)
        return mtu__dygup._getvalue()
    return string_type(types.voidptr, types.intp), codegen


def get_arr_data_ptr(arr, ind):
    return arr


@overload(get_arr_data_ptr, no_unliteral=True)
def overload_get_arr_data_ptr(arr, ind):
    assert isinstance(types.unliteral(ind), types.Integer)
    if isinstance(arr, bodo.libs.int_arr_ext.IntegerArrayType):

        def impl_int(arr, ind):
            return bodo.hiframes.split_impl.get_c_arr_ptr(arr._data.ctypes, ind
                )
        return impl_int
    assert isinstance(arr, types.Array)

    def impl_np(arr, ind):
        return bodo.hiframes.split_impl.get_c_arr_ptr(arr.ctypes, ind)
    return impl_np


def set_to_numeric_out_na_err(out_arr, out_ind, err_code):
    pass


@overload(set_to_numeric_out_na_err)
def set_to_numeric_out_na_err_overload(out_arr, out_ind, err_code):
    if isinstance(out_arr, bodo.libs.int_arr_ext.IntegerArrayType):

        def impl_int(out_arr, out_ind, err_code):
            bodo.libs.int_arr_ext.set_bit_to_arr(out_arr._null_bitmap,
                out_ind, 0 if err_code == -1 else 1)
        return impl_int
    assert isinstance(out_arr, types.Array)
    if isinstance(out_arr.dtype, types.Float):

        def impl_np(out_arr, out_ind, err_code):
            if err_code == -1:
                out_arr[out_ind] = np.nan
        return impl_np
    return lambda out_arr, out_ind, err_code: None


@numba.njit(no_cpython_wrapper=True)
def str_arr_item_to_numeric(out_arr, out_ind, str_arr, ind):
    err_code = _str_arr_item_to_numeric(get_arr_data_ptr(out_arr, out_ind),
        str_arr, ind, out_arr.dtype)
    set_to_numeric_out_na_err(out_arr, out_ind, err_code)


@intrinsic
def _str_arr_item_to_numeric(typingctx, out_ptr_t, str_arr_t, ind_t,
    out_dtype_t=None):
    assert str_arr_t == string_array_type, '_str_arr_item_to_numeric: str arr expected'
    assert ind_t == types.int64, '_str_arr_item_to_numeric: integer index expected'

    def codegen(context, builder, sig, args):
        xiusa__ojs, arr, ind, tzkv__plkv = args
        alg__tbz = _get_str_binary_arr_payload(context, builder, arr,
            string_array_type)
        offsets = context.make_helper(builder, offset_arr_type, alg__tbz.
            offsets).data
        data = context.make_helper(builder, char_arr_type, alg__tbz.data).data
        uliu__fdrzz = lir.FunctionType(lir.IntType(32), [xiusa__ojs.type,
            lir.IntType(offset_type.bitwidth).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(64)])
        ytlpw__jjqer = 'str_arr_to_int64'
        if sig.args[3].dtype == types.float64:
            ytlpw__jjqer = 'str_arr_to_float64'
        else:
            assert sig.args[3].dtype == types.int64
        osw__dnt = cgutils.get_or_insert_function(builder.module,
            uliu__fdrzz, ytlpw__jjqer)
        return builder.call(osw__dnt, [xiusa__ojs, offsets, data, ind])
    return types.int32(out_ptr_t, string_array_type, types.int64, out_dtype_t
        ), codegen


@unbox(BinaryArrayType)
@unbox(StringArrayType)
def unbox_str_series(typ, val, c):
    wpeqp__jxd = c.context.get_constant(types.int32, int(typ ==
        binary_array_type))
    uliu__fdrzz = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
        IntType(8).as_pointer(), lir.IntType(32)])
    kfprn__mvkh = cgutils.get_or_insert_function(c.builder.module,
        uliu__fdrzz, name='string_array_from_sequence')
    tfec__xdwvr = c.builder.call(kfprn__mvkh, [val, wpeqp__jxd])
    olx__pdokq = ArrayItemArrayType(char_arr_type)
    muj__uufsp = c.context.make_helper(c.builder, olx__pdokq)
    muj__uufsp.meminfo = tfec__xdwvr
    yjs__dbm = c.context.make_helper(c.builder, typ)
    khgaa__bmux = muj__uufsp._getvalue()
    yjs__dbm.data = khgaa__bmux
    zdpx__okjee = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(yjs__dbm._getvalue(), is_error=zdpx__okjee)


@lower_constant(BinaryArrayType)
@lower_constant(StringArrayType)
def lower_constant_str_arr(context, builder, typ, pyval):
    qnhvy__zkfvs = len(pyval)
    uti__wzbse = 0
    feesi__zqb = np.empty(qnhvy__zkfvs + 1, np_offset_type)
    nbdq__gnzs = []
    uoahp__plnmi = np.empty(qnhvy__zkfvs + 7 >> 3, np.uint8)
    for i, s in enumerate(pyval):
        feesi__zqb[i] = uti__wzbse
        hxhmu__uhv = pd.isna(s)
        bodo.libs.int_arr_ext.set_bit_to_arr(uoahp__plnmi, i, int(not
            hxhmu__uhv))
        if hxhmu__uhv:
            continue
        uic__dhho = list(s.encode()) if isinstance(s, str) else list(s)
        nbdq__gnzs.extend(uic__dhho)
        uti__wzbse += len(uic__dhho)
    feesi__zqb[qnhvy__zkfvs] = uti__wzbse
    ojl__epn = np.array(nbdq__gnzs, np.uint8)
    jub__cbx = context.get_constant(types.int64, qnhvy__zkfvs)
    ncp__tcj = context.get_constant_generic(builder, char_arr_type, ojl__epn)
    gop__aakum = context.get_constant_generic(builder, offset_arr_type,
        feesi__zqb)
    zdi__hgtjm = context.get_constant_generic(builder, null_bitmap_arr_type,
        uoahp__plnmi)
    alg__tbz = lir.Constant.literal_struct([jub__cbx, ncp__tcj, gop__aakum,
        zdi__hgtjm])
    alg__tbz = cgutils.global_constant(builder, '.const.payload', alg__tbz
        ).bitcast(cgutils.voidptr_t)
    gvop__yhp = context.get_constant(types.int64, -1)
    xbued__ytqnw = context.get_constant_null(types.voidptr)
    hsyi__aoh = lir.Constant.literal_struct([gvop__yhp, xbued__ytqnw,
        xbued__ytqnw, alg__tbz, gvop__yhp])
    hsyi__aoh = cgutils.global_constant(builder, '.const.meminfo', hsyi__aoh
        ).bitcast(cgutils.voidptr_t)
    khgaa__bmux = lir.Constant.literal_struct([hsyi__aoh])
    yjs__dbm = lir.Constant.literal_struct([khgaa__bmux])
    return yjs__dbm


def pre_alloc_str_arr_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 2 and not kws
    return ArrayAnalysis.AnalyzeResult(shape=args[0], pre=[])


from numba.parfors.array_analysis import ArrayAnalysis
(ArrayAnalysis._analyze_op_call_bodo_libs_str_arr_ext_pre_alloc_string_array
    ) = pre_alloc_str_arr_equiv


@overload(glob.glob, no_unliteral=True)
def overload_glob_glob(pathname, recursive=False):

    def _glob_glob_impl(pathname, recursive=False):
        with numba.objmode(l='list_str_type'):
            l = glob.glob(pathname, recursive=recursive)
        return l
    return _glob_glob_impl
