"""Dictionary encoded array data type, similar to DictionaryArray of Arrow.
The purpose is to improve memory consumption and performance over string_array_type for
string arrays that have a lot of repetitive values (typical in practice).
Can be extended to be used with types other than strings as well.
See:
https://bodo.atlassian.net/browse/BE-2295
https://bodo.atlassian.net/wiki/spaces/B/pages/993722369/Dictionary-encoded+String+Array+Support+in+Parquet+read+compute+...
https://arrow.apache.org/docs/cpp/api/array.html#dictionary-encoded
"""
import operator
import re
import llvmlite.binding as ll
import numba
import numpy as np
import pandas as pd
import pyarrow as pa
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.imputils import impl_ret_new_ref, lower_builtin, lower_constant
from numba.extending import NativeValue, box, intrinsic, lower_cast, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_jitable, register_model, typeof_impl, unbox
import bodo
from bodo.libs import hstr_ext
from bodo.libs.bool_arr_ext import init_bool_array
from bodo.libs.int_arr_ext import IntegerArrayType
from bodo.libs.str_arr_ext import StringArrayType, get_str_arr_item_length, overload_str_arr_astype, pre_alloc_string_array, string_array_type
from bodo.utils.typing import BodoArrayIterator, is_overload_none, raise_bodo_error
from bodo.utils.utils import synchronize_error_njit
ll.add_symbol('box_dict_str_array', hstr_ext.box_dict_str_array)
dict_indices_arr_type = IntegerArrayType(types.int32)


class DictionaryArrayType(types.IterableType, types.ArrayCompatible):

    def __init__(self, arr_data_type):
        self.data = arr_data_type
        super(DictionaryArrayType, self).__init__(name=
            f'DictionaryArrayType({arr_data_type})')

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    @property
    def iterator_type(self):
        return BodoArrayIterator(self)

    @property
    def dtype(self):
        return self.data.dtype

    def copy(self):
        return DictionaryArrayType(self.data)

    @property
    def indices_type(self):
        return dict_indices_arr_type

    @property
    def indices_dtype(self):
        return dict_indices_arr_type.dtype

    def unify(self, typingctx, other):
        if other == string_array_type:
            return string_array_type


dict_str_arr_type = DictionaryArrayType(string_array_type)


@register_model(DictionaryArrayType)
class DictionaryArrayModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        zjud__kpcqa = [('data', fe_type.data), ('indices',
            dict_indices_arr_type), ('has_global_dictionary', types.bool_),
            ('has_deduped_local_dictionary', types.bool_)]
        models.StructModel.__init__(self, dmm, fe_type, zjud__kpcqa)


make_attribute_wrapper(DictionaryArrayType, 'data', '_data')
make_attribute_wrapper(DictionaryArrayType, 'indices', '_indices')
make_attribute_wrapper(DictionaryArrayType, 'has_global_dictionary',
    '_has_global_dictionary')
make_attribute_wrapper(DictionaryArrayType, 'has_deduped_local_dictionary',
    '_has_deduped_local_dictionary')
lower_builtin('getiter', dict_str_arr_type)(numba.np.arrayobj.getiter_array)


@intrinsic
def init_dict_arr(typingctx, data_t, indices_t, glob_dict_t, unique_dict_t):
    assert indices_t == dict_indices_arr_type, 'invalid indices type for dict array'

    def codegen(context, builder, signature, args):
        wwub__enn, bkts__pwh, vgwm__zksu, uzr__wafjs = args
        skc__pxfgh = cgutils.create_struct_proxy(signature.return_type)(context
            , builder)
        skc__pxfgh.data = wwub__enn
        skc__pxfgh.indices = bkts__pwh
        skc__pxfgh.has_global_dictionary = vgwm__zksu
        skc__pxfgh.has_deduped_local_dictionary = uzr__wafjs
        context.nrt.incref(builder, signature.args[0], wwub__enn)
        context.nrt.incref(builder, signature.args[1], bkts__pwh)
        return skc__pxfgh._getvalue()
    itvh__idku = DictionaryArrayType(data_t)
    snpmj__click = itvh__idku(data_t, indices_t, types.bool_, types.bool_)
    return snpmj__click, codegen


@typeof_impl.register(pa.DictionaryArray)
def typeof_dict_value(val, c):
    if val.type.value_type == pa.string():
        return dict_str_arr_type


def to_pa_dict_arr(A):
    if isinstance(A, pa.DictionaryArray):
        return A
    if isinstance(A, pd.arrays.ArrowStringArray) and pa.types.is_dictionary(A
        ._data.type) and (pa.types.is_string(A._data.type.value_type) or pa
        .types.is_large_string(A._data.type.value_type)) and pa.types.is_int32(
        A._data.type.index_type):
        return A._data.combine_chunks()
    return pd.array(A, 'string[pyarrow]')._data.combine_chunks(
        ).dictionary_encode()


@unbox(DictionaryArrayType)
def unbox_dict_arr(typ, val, c):
    tos__ugv = c.pyapi.unserialize(c.pyapi.serialize_object(to_pa_dict_arr))
    val = c.pyapi.call_function_objargs(tos__ugv, [val])
    c.pyapi.decref(tos__ugv)
    skc__pxfgh = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    ppz__ztxu = c.pyapi.object_getattr_string(val, 'dictionary')
    xsro__yzos = c.pyapi.bool_from_bool(c.context.get_constant(types.bool_,
        False))
    yyd__qfws = c.pyapi.call_method(ppz__ztxu, 'to_numpy', (xsro__yzos,))
    skc__pxfgh.data = c.unbox(typ.data, yyd__qfws).value
    dic__bun = c.pyapi.object_getattr_string(val, 'indices')
    gdrbt__dztzz = c.context.insert_const_string(c.builder.module, 'pandas')
    ggpi__qnxh = c.pyapi.import_module_noblock(gdrbt__dztzz)
    rphg__smmin = c.pyapi.string_from_constant_string('Int32')
    lycan__lufx = c.pyapi.call_method(ggpi__qnxh, 'array', (dic__bun,
        rphg__smmin))
    skc__pxfgh.indices = c.unbox(dict_indices_arr_type, lycan__lufx).value
    skc__pxfgh.has_global_dictionary = c.context.get_constant(types.bool_, 
        False)
    skc__pxfgh.has_deduped_local_dictionary = c.context.get_constant(types.
        bool_, False)
    c.pyapi.decref(ppz__ztxu)
    c.pyapi.decref(xsro__yzos)
    c.pyapi.decref(yyd__qfws)
    c.pyapi.decref(dic__bun)
    c.pyapi.decref(ggpi__qnxh)
    c.pyapi.decref(rphg__smmin)
    c.pyapi.decref(lycan__lufx)
    c.pyapi.decref(val)
    rhdf__ivsmh = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(skc__pxfgh._getvalue(), is_error=rhdf__ivsmh)


@box(DictionaryArrayType)
def box_dict_arr(typ, val, c):
    skc__pxfgh = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    if typ == dict_str_arr_type:
        if bodo.libs.str_arr_ext.use_pd_pyarrow_string_array:
            from bodo.libs.array import array_info_type, array_to_info_codegen
            lfo__herh = array_to_info_codegen(c.context, c.builder,
                array_info_type(typ), (val,), incref=False)
            pvfvr__uvez = lir.FunctionType(c.pyapi.pyobj, [lir.IntType(8).
                as_pointer()])
            hjiys__bjb = 'pd_pyarrow_array_from_string_array'
            oyn__kxft = cgutils.get_or_insert_function(c.builder.module,
                pvfvr__uvez, name=hjiys__bjb)
            arr = c.builder.call(oyn__kxft, [lfo__herh])
            c.context.nrt.decref(c.builder, typ, val)
            return arr
        c.context.nrt.incref(c.builder, typ.data, skc__pxfgh.data)
        lab__kieus = c.box(typ.data, skc__pxfgh.data)
        wlme__pcql = cgutils.create_struct_proxy(dict_indices_arr_type)(c.
            context, c.builder, skc__pxfgh.indices)
        pvfvr__uvez = lir.FunctionType(c.pyapi.pyobj, [lir.IntType(64), c.
            pyapi.pyobj, lir.IntType(32).as_pointer(), lir.IntType(8).
            as_pointer()])
        oyn__kxft = cgutils.get_or_insert_function(c.builder.module,
            pvfvr__uvez, name='box_dict_str_array')
        hwxgh__zau = cgutils.create_struct_proxy(types.Array(types.int32, 1,
            'C'))(c.context, c.builder, wlme__pcql.data)
        pqlcs__kos = c.builder.extract_value(hwxgh__zau.shape, 0)
        vtust__afad = hwxgh__zau.data
        ojfa__dfnh = cgutils.create_struct_proxy(types.Array(types.int8, 1,
            'C'))(c.context, c.builder, wlme__pcql.null_bitmap).data
        yyd__qfws = c.builder.call(oyn__kxft, [pqlcs__kos, lab__kieus,
            vtust__afad, ojfa__dfnh])
        c.pyapi.decref(lab__kieus)
    else:
        gdrbt__dztzz = c.context.insert_const_string(c.builder.module,
            'pyarrow')
        zdc__qiq = c.pyapi.import_module_noblock(gdrbt__dztzz)
        say__sca = c.pyapi.object_getattr_string(zdc__qiq, 'DictionaryArray')
        c.context.nrt.incref(c.builder, typ.data, skc__pxfgh.data)
        lab__kieus = c.box(typ.data, skc__pxfgh.data)
        c.context.nrt.incref(c.builder, dict_indices_arr_type, skc__pxfgh.
            indices)
        dic__bun = c.box(dict_indices_arr_type, skc__pxfgh.indices)
        ipedb__afid = c.pyapi.call_method(say__sca, 'from_arrays', (
            dic__bun, lab__kieus))
        xsro__yzos = c.pyapi.bool_from_bool(c.context.get_constant(types.
            bool_, False))
        yyd__qfws = c.pyapi.call_method(ipedb__afid, 'to_numpy', (xsro__yzos,))
        c.pyapi.decref(zdc__qiq)
        c.pyapi.decref(lab__kieus)
        c.pyapi.decref(dic__bun)
        c.pyapi.decref(say__sca)
        c.pyapi.decref(ipedb__afid)
        c.pyapi.decref(xsro__yzos)
    c.context.nrt.decref(c.builder, typ, val)
    return yyd__qfws


@overload(len, no_unliteral=True)
def overload_dict_arr_len(A):
    if isinstance(A, DictionaryArrayType):
        return lambda A: len(A._indices)


@overload_attribute(DictionaryArrayType, 'shape')
def overload_dict_arr_shape(A):
    return lambda A: (len(A._indices),)


@overload_attribute(DictionaryArrayType, 'ndim')
def overload_dict_arr_ndim(A):
    return lambda A: 1


@overload_attribute(DictionaryArrayType, 'size')
def overload_dict_arr_size(A):
    return lambda A: len(A._indices)


@overload_method(DictionaryArrayType, 'tolist', no_unliteral=True)
def overload_dict_arr_tolist(A):
    return lambda A: list(A)


overload_method(DictionaryArrayType, 'astype', no_unliteral=True)(
    overload_str_arr_astype)


@overload_method(DictionaryArrayType, 'copy', no_unliteral=True)
def overload_dict_arr_copy(A):

    def copy_impl(A):
        return init_dict_arr(A._data.copy(), A._indices.copy(), A.
            _has_global_dictionary, A._has_deduped_local_dictionary)
    return copy_impl


@overload_attribute(DictionaryArrayType, 'dtype')
def overload_dict_arr_dtype(A):
    return lambda A: A._data.dtype


@overload_attribute(DictionaryArrayType, 'nbytes')
def dict_arr_nbytes_overload(A):
    return lambda A: A._data.nbytes + A._indices.nbytes


@lower_constant(DictionaryArrayType)
def lower_constant_dict_arr(context, builder, typ, pyval):
    if bodo.hiframes.boxing._use_dict_str_type and isinstance(pyval, np.ndarray
        ):
        pyval = pa.array(pyval).dictionary_encode()
    cken__jjj = pyval.dictionary.to_numpy(False)
    yvy__ahxne = pd.array(pyval.indices, 'Int32')
    cken__jjj = context.get_constant_generic(builder, typ.data, cken__jjj)
    yvy__ahxne = context.get_constant_generic(builder,
        dict_indices_arr_type, yvy__ahxne)
    gudfw__bfhzz = context.get_constant(types.bool_, False)
    tok__oxfzl = context.get_constant(types.bool_, False)
    gmd__yrawi = lir.Constant.literal_struct([cken__jjj, yvy__ahxne,
        gudfw__bfhzz, tok__oxfzl])
    return gmd__yrawi


@overload(operator.getitem, no_unliteral=True)
def dict_arr_getitem(A, ind):
    if not isinstance(A, DictionaryArrayType):
        return
    if isinstance(ind, types.Integer):

        def dict_arr_getitem_impl(A, ind):
            if bodo.libs.array_kernels.isna(A._indices, ind):
                return ''
            uka__yhizf = A._indices[ind]
            return A._data[uka__yhizf]
        return dict_arr_getitem_impl
    return lambda A, ind: init_dict_arr(A._data, A._indices[ind], A.
        _has_global_dictionary, A._has_deduped_local_dictionary)


@overload_method(DictionaryArrayType, '_decode', no_unliteral=True)
def overload_dict_arr_decode(A):

    def impl(A):
        wwub__enn = A._data
        bkts__pwh = A._indices
        pqlcs__kos = len(bkts__pwh)
        aaul__kccp = [get_str_arr_item_length(wwub__enn, i) for i in range(
            len(wwub__enn))]
        qjdzr__gag = 0
        for i in range(pqlcs__kos):
            if not bodo.libs.array_kernels.isna(bkts__pwh, i):
                qjdzr__gag += aaul__kccp[bkts__pwh[i]]
        qbd__pleq = pre_alloc_string_array(pqlcs__kos, qjdzr__gag)
        for i in range(pqlcs__kos):
            if bodo.libs.array_kernels.isna(bkts__pwh, i):
                bodo.libs.array_kernels.setna(qbd__pleq, i)
                continue
            ind = bkts__pwh[i]
            if bodo.libs.array_kernels.isna(wwub__enn, ind):
                bodo.libs.array_kernels.setna(qbd__pleq, i)
                continue
            qbd__pleq[i] = wwub__enn[ind]
        return qbd__pleq
    return impl


@overload(operator.setitem)
def dict_arr_setitem(A, idx, val):
    if not isinstance(A, DictionaryArrayType):
        return
    raise_bodo_error(
        "DictionaryArrayType is read-only and doesn't support setitem yet")


@numba.njit(no_cpython_wrapper=True)
def find_dict_ind_unique(arr, val):
    uka__yhizf = -1
    wwub__enn = arr._data
    for i in range(len(wwub__enn)):
        if bodo.libs.array_kernels.isna(wwub__enn, i):
            continue
        if wwub__enn[i] == val:
            uka__yhizf = i
            break
    return uka__yhizf


@numba.njit(no_cpython_wrapper=True)
def find_dict_ind_non_unique(arr, val):
    kaudm__fefd = set()
    wwub__enn = arr._data
    for i in range(len(wwub__enn)):
        if bodo.libs.array_kernels.isna(wwub__enn, i):
            continue
        if wwub__enn[i] == val:
            kaudm__fefd.add(i)
    return kaudm__fefd


@numba.njit(no_cpython_wrapper=True)
def dict_arr_eq(arr, val):
    pqlcs__kos = len(arr)
    if arr._has_deduped_local_dictionary:
        uka__yhizf = find_dict_ind_unique(arr, val)
        if uka__yhizf == -1:
            return init_bool_array(np.full(pqlcs__kos, False, np.bool_),
                arr._indices._null_bitmap.copy())
        return arr._indices == uka__yhizf
    else:
        rwkb__gfumw = find_dict_ind_non_unique(arr, val)
        if len(rwkb__gfumw) == 0:
            return init_bool_array(np.full(pqlcs__kos, False, np.bool_),
                arr._indices._null_bitmap.copy())
        eps__yocdf = np.empty(pqlcs__kos, dtype=np.bool_)
        for i in range(len(arr._indices)):
            eps__yocdf[i] = arr._indices[i] in rwkb__gfumw
        return init_bool_array(eps__yocdf, arr._indices._null_bitmap.copy())


@numba.njit(no_cpython_wrapper=True)
def dict_arr_ne(arr, val):
    pqlcs__kos = len(arr)
    if arr._has_deduped_local_dictionary:
        uka__yhizf = find_dict_ind_unique(arr, val)
        if uka__yhizf == -1:
            return init_bool_array(np.full(pqlcs__kos, True, np.bool_), arr
                ._indices._null_bitmap.copy())
        return arr._indices != uka__yhizf
    else:
        rwkb__gfumw = find_dict_ind_non_unique(arr, val)
        if len(rwkb__gfumw) == 0:
            return init_bool_array(np.full(pqlcs__kos, True, np.bool_), arr
                ._indices._null_bitmap.copy())
        eps__yocdf = np.empty(pqlcs__kos, dtype=np.bool_)
        for i in range(len(arr._indices)):
            eps__yocdf[i] = arr._indices[i] not in rwkb__gfumw
        return init_bool_array(eps__yocdf, arr._indices._null_bitmap.copy())


def get_binary_op_overload(op, lhs, rhs):
    if op == operator.eq:
        if lhs == dict_str_arr_type and types.unliteral(rhs
            ) == bodo.string_type:
            return lambda lhs, rhs: bodo.libs.dict_arr_ext.dict_arr_eq(lhs, rhs
                )
        if rhs == dict_str_arr_type and types.unliteral(lhs
            ) == bodo.string_type:
            return lambda lhs, rhs: bodo.libs.dict_arr_ext.dict_arr_eq(rhs, lhs
                )
    if op == operator.ne:
        if lhs == dict_str_arr_type and types.unliteral(rhs
            ) == bodo.string_type:
            return lambda lhs, rhs: bodo.libs.dict_arr_ext.dict_arr_ne(lhs, rhs
                )
        if rhs == dict_str_arr_type and types.unliteral(lhs
            ) == bodo.string_type:
            return lambda lhs, rhs: bodo.libs.dict_arr_ext.dict_arr_ne(rhs, lhs
                )


def convert_dict_arr_to_int(arr, dtype):
    return arr


@overload(convert_dict_arr_to_int)
def convert_dict_arr_to_int_overload(arr, dtype):

    def impl(arr, dtype):
        vvb__pjf = arr._data
        nlghl__turyk = bodo.libs.int_arr_ext.alloc_int_array(len(vvb__pjf),
            dtype)
        for vwv__aejnd in range(len(vvb__pjf)):
            if bodo.libs.array_kernels.isna(vvb__pjf, vwv__aejnd):
                bodo.libs.array_kernels.setna(nlghl__turyk, vwv__aejnd)
                continue
            nlghl__turyk[vwv__aejnd] = np.int64(vvb__pjf[vwv__aejnd])
        pqlcs__kos = len(arr)
        bkts__pwh = arr._indices
        qbd__pleq = bodo.libs.int_arr_ext.alloc_int_array(pqlcs__kos, dtype)
        for i in range(pqlcs__kos):
            if bodo.libs.array_kernels.isna(bkts__pwh, i):
                bodo.libs.array_kernels.setna(qbd__pleq, i)
                continue
            qbd__pleq[i] = nlghl__turyk[bkts__pwh[i]]
        return qbd__pleq
    return impl


def cat_dict_str(arrs, sep):
    pass


@overload(cat_dict_str)
def cat_dict_str_overload(arrs, sep):
    dvp__pxpo = len(arrs)
    hsgm__sqoc = 'def impl(arrs, sep):\n'
    hsgm__sqoc += '  ind_map = {}\n'
    hsgm__sqoc += '  out_strs = []\n'
    hsgm__sqoc += '  n = len(arrs[0])\n'
    for i in range(dvp__pxpo):
        hsgm__sqoc += f'  indices{i} = arrs[{i}]._indices\n'
    for i in range(dvp__pxpo):
        hsgm__sqoc += f'  data{i} = arrs[{i}]._data\n'
    hsgm__sqoc += (
        '  out_indices = bodo.libs.int_arr_ext.alloc_int_array(n, np.int32)\n')
    hsgm__sqoc += '  for i in range(n):\n'
    tylto__xzbpn = ' or '.join([
        f'bodo.libs.array_kernels.isna(arrs[{i}], i)' for i in range(
        dvp__pxpo)])
    hsgm__sqoc += f'    if {tylto__xzbpn}:\n'
    hsgm__sqoc += '      bodo.libs.array_kernels.setna(out_indices, i)\n'
    hsgm__sqoc += '      continue\n'
    for i in range(dvp__pxpo):
        hsgm__sqoc += f'    ind{i} = indices{i}[i]\n'
    cafj__qkd = '(' + ', '.join(f'ind{i}' for i in range(dvp__pxpo)) + ')'
    hsgm__sqoc += f'    if {cafj__qkd} not in ind_map:\n'
    hsgm__sqoc += '      out_ind = len(out_strs)\n'
    hsgm__sqoc += f'      ind_map[{cafj__qkd}] = out_ind\n'
    mijzs__lacjt = "''" if is_overload_none(sep) else 'sep'
    riir__pnl = ', '.join([f'data{i}[ind{i}]' for i in range(dvp__pxpo)])
    hsgm__sqoc += f'      v = {mijzs__lacjt}.join([{riir__pnl}])\n'
    hsgm__sqoc += '      out_strs.append(v)\n'
    hsgm__sqoc += '    else:\n'
    hsgm__sqoc += f'      out_ind = ind_map[{cafj__qkd}]\n'
    hsgm__sqoc += '    out_indices[i] = out_ind\n'
    hsgm__sqoc += (
        '  out_str_arr = bodo.libs.str_arr_ext.str_arr_from_sequence(out_strs)\n'
        )
    hsgm__sqoc += """  return bodo.libs.dict_arr_ext.init_dict_arr(out_str_arr, out_indices, False, False)
"""
    qmwqj__oajy = {}
    exec(hsgm__sqoc, {'bodo': bodo, 'numba': numba, 'np': np}, qmwqj__oajy)
    impl = qmwqj__oajy['impl']
    return impl


@lower_cast(DictionaryArrayType, StringArrayType)
def cast_dict_str_arr_to_str_arr(context, builder, fromty, toty, val):
    if fromty != dict_str_arr_type:
        return
    thppx__cywho = bodo.utils.typing.decode_if_dict_array_overload(fromty)
    snpmj__click = toty(fromty)
    lqm__dmsk = context.compile_internal(builder, thppx__cywho,
        snpmj__click, (val,))
    return impl_ret_new_ref(context, builder, toty, lqm__dmsk)


@register_jitable
def dict_arr_to_numeric(arr, errors, downcast):
    skc__pxfgh = arr._data
    dict_arr_out = pd.to_numeric(skc__pxfgh, errors, downcast)
    yvy__ahxne = arr._indices
    lny__jwt = len(yvy__ahxne)
    qbd__pleq = bodo.utils.utils.alloc_type(lny__jwt, dict_arr_out, (-1,))
    for i in range(lny__jwt):
        if bodo.libs.array_kernels.isna(arr, i):
            bodo.libs.array_kernels.setna(qbd__pleq, i)
            continue
        uka__yhizf = yvy__ahxne[i]
        if bodo.libs.array_kernels.isna(dict_arr_out, uka__yhizf):
            bodo.libs.array_kernels.setna(qbd__pleq, i)
            continue
        qbd__pleq[i] = dict_arr_out[uka__yhizf]
    return qbd__pleq


@register_jitable
def str_replace(arr, pat, repl, flags, regex):
    cken__jjj = arr._data
    fllve__xehbb = len(cken__jjj)
    ribwz__qaoj = pre_alloc_string_array(fllve__xehbb, -1)
    if regex:
        npacy__wizwu = re.compile(pat, flags)
        for i in range(fllve__xehbb):
            if bodo.libs.array_kernels.isna(cken__jjj, i):
                bodo.libs.array_kernels.setna(ribwz__qaoj, i)
                continue
            ribwz__qaoj[i] = npacy__wizwu.sub(repl=repl, string=cken__jjj[i])
    else:
        for i in range(fllve__xehbb):
            if bodo.libs.array_kernels.isna(cken__jjj, i):
                bodo.libs.array_kernels.setna(ribwz__qaoj, i)
                continue
            ribwz__qaoj[i] = cken__jjj[i].replace(pat, repl)
    return init_dict_arr(ribwz__qaoj, arr._indices.copy(), arr.
        _has_global_dictionary, False)


@register_jitable
def str_startswith(arr, pat, na):
    skc__pxfgh = arr._data
    dyhr__tymg = len(skc__pxfgh)
    dict_arr_out = bodo.libs.bool_arr_ext.alloc_bool_array(dyhr__tymg)
    for i in range(dyhr__tymg):
        dict_arr_out[i] = skc__pxfgh[i].startswith(pat)
    yvy__ahxne = arr._indices
    lny__jwt = len(yvy__ahxne)
    qbd__pleq = bodo.libs.bool_arr_ext.alloc_bool_array(lny__jwt)
    for i in range(lny__jwt):
        if bodo.libs.array_kernels.isna(arr, i):
            bodo.libs.array_kernels.setna(qbd__pleq, i)
        else:
            qbd__pleq[i] = dict_arr_out[yvy__ahxne[i]]
    return qbd__pleq


@register_jitable
def str_endswith(arr, pat, na):
    skc__pxfgh = arr._data
    dyhr__tymg = len(skc__pxfgh)
    dict_arr_out = bodo.libs.bool_arr_ext.alloc_bool_array(dyhr__tymg)
    for i in range(dyhr__tymg):
        dict_arr_out[i] = skc__pxfgh[i].endswith(pat)
    yvy__ahxne = arr._indices
    lny__jwt = len(yvy__ahxne)
    qbd__pleq = bodo.libs.bool_arr_ext.alloc_bool_array(lny__jwt)
    for i in range(lny__jwt):
        if bodo.libs.array_kernels.isna(arr, i):
            bodo.libs.array_kernels.setna(qbd__pleq, i)
        else:
            qbd__pleq[i] = dict_arr_out[yvy__ahxne[i]]
    return qbd__pleq


@numba.njit
def str_series_contains_regex(arr, pat, case, flags, na, regex):
    skc__pxfgh = arr._data
    nksfm__atgi = pd.Series(skc__pxfgh)
    with numba.objmode(dict_arr_out=bodo.boolean_array):
        dict_arr_out = pd.array(nksfm__atgi.array, 'string')._str_contains(pat,
            case, flags, na, regex)
    yvy__ahxne = arr._indices
    lny__jwt = len(yvy__ahxne)
    qbd__pleq = bodo.libs.bool_arr_ext.alloc_bool_array(lny__jwt)
    for i in range(lny__jwt):
        if bodo.libs.array_kernels.isna(arr, i):
            bodo.libs.array_kernels.setna(qbd__pleq, i)
        else:
            qbd__pleq[i] = dict_arr_out[yvy__ahxne[i]]
    return qbd__pleq


@register_jitable
def str_contains_non_regex(arr, pat, case):
    skc__pxfgh = arr._data
    dyhr__tymg = len(skc__pxfgh)
    dict_arr_out = bodo.libs.bool_arr_ext.alloc_bool_array(dyhr__tymg)
    if not case:
        lle__msgrb = pat.upper()
    for i in range(dyhr__tymg):
        if case:
            dict_arr_out[i] = pat in skc__pxfgh[i]
        else:
            dict_arr_out[i] = lle__msgrb in skc__pxfgh[i].upper()
    yvy__ahxne = arr._indices
    lny__jwt = len(yvy__ahxne)
    qbd__pleq = bodo.libs.bool_arr_ext.alloc_bool_array(lny__jwt)
    for i in range(lny__jwt):
        if bodo.libs.array_kernels.isna(arr, i):
            bodo.libs.array_kernels.setna(qbd__pleq, i)
        else:
            qbd__pleq[i] = dict_arr_out[yvy__ahxne[i]]
    return qbd__pleq


@numba.njit
def str_match(arr, pat, case, flags, na):
    skc__pxfgh = arr._data
    yvy__ahxne = arr._indices
    lny__jwt = len(yvy__ahxne)
    qbd__pleq = bodo.libs.bool_arr_ext.alloc_bool_array(lny__jwt)
    nksfm__atgi = pd.Series(skc__pxfgh)
    with numba.objmode(dict_arr_out=bodo.boolean_array):
        dict_arr_out = nksfm__atgi.array._str_match(pat, case, flags, na)
    for i in range(lny__jwt):
        if bodo.libs.array_kernels.isna(arr, i):
            bodo.libs.array_kernels.setna(qbd__pleq, i)
        else:
            qbd__pleq[i] = dict_arr_out[yvy__ahxne[i]]
    return qbd__pleq


def create_simple_str2str_methods(func_name, func_args, can_create_non_unique):
    hsgm__sqoc = f"""def str_{func_name}({', '.join(func_args)}):
    data_arr = arr._data
    n_data = len(data_arr)
    out_str_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(n_data, -1)
    for i in range(n_data):
        if bodo.libs.array_kernels.isna(data_arr, i):
            bodo.libs.array_kernels.setna(out_str_arr, i)
            continue
        out_str_arr[i] = data_arr[i].{func_name}({', '.join(func_args[1:])})
"""
    if can_create_non_unique:
        hsgm__sqoc += """    return init_dict_arr(out_str_arr, arr._indices.copy(), arr._has_global_dictionary, False)
"""
    else:
        hsgm__sqoc += """    return init_dict_arr(out_str_arr, arr._indices.copy(), arr._has_global_dictionary, arr._has_deduped_local_dictionary)
"""
    qmwqj__oajy = {}
    exec(hsgm__sqoc, {'bodo': bodo, 'numba': numba, 'init_dict_arr':
        init_dict_arr}, qmwqj__oajy)
    return qmwqj__oajy[f'str_{func_name}']


def _register_simple_str2str_methods():
    alll__kncy = {**dict.fromkeys(['capitalize', 'lower', 'swapcase',
        'title', 'upper'], ('arr',)), **dict.fromkeys(['lstrip', 'rstrip',
        'strip'], ('arr', 'to_strip')), **dict.fromkeys(['center', 'ljust',
        'rjust'], ('arr', 'width', 'fillchar')), **dict.fromkeys(['zfill'],
        ('arr', 'width'))}
    dimj__surg = {**dict.fromkeys(['capitalize', 'lower', 'title', 'upper',
        'lstrip', 'rstrip', 'strip', 'center', 'zfill', 'ljust', 'rjust'], 
        True), **dict.fromkeys(['swapcase'], False)}
    for func_name in alll__kncy.keys():
        aob__xpib = create_simple_str2str_methods(func_name, alll__kncy[
            func_name], dimj__surg[func_name])
        aob__xpib = register_jitable(aob__xpib)
        globals()[f'str_{func_name}'] = aob__xpib


_register_simple_str2str_methods()


@register_jitable
def str_index(arr, sub, start, end):
    cken__jjj = arr._data
    yvy__ahxne = arr._indices
    fllve__xehbb = len(cken__jjj)
    lny__jwt = len(yvy__ahxne)
    ykr__ibeoa = bodo.libs.int_arr_ext.alloc_int_array(fllve__xehbb, np.int64)
    qbd__pleq = bodo.libs.int_arr_ext.alloc_int_array(lny__jwt, np.int64)
    nbxjs__efl = False
    for i in range(fllve__xehbb):
        if bodo.libs.array_kernels.isna(cken__jjj, i):
            bodo.libs.array_kernels.setna(ykr__ibeoa, i)
        else:
            ykr__ibeoa[i] = cken__jjj[i].find(sub, start, end)
    for i in range(lny__jwt):
        if bodo.libs.array_kernels.isna(arr, i
            ) or bodo.libs.array_kernels.isna(ykr__ibeoa, yvy__ahxne[i]):
            bodo.libs.array_kernels.setna(qbd__pleq, i)
        else:
            qbd__pleq[i] = ykr__ibeoa[yvy__ahxne[i]]
            if qbd__pleq[i] == -1:
                nbxjs__efl = True
    bjyyw__usxvi = 'substring not found' if nbxjs__efl else ''
    synchronize_error_njit('ValueError', bjyyw__usxvi)
    return qbd__pleq


@register_jitable
def str_rindex(arr, sub, start, end):
    cken__jjj = arr._data
    yvy__ahxne = arr._indices
    fllve__xehbb = len(cken__jjj)
    lny__jwt = len(yvy__ahxne)
    ykr__ibeoa = bodo.libs.int_arr_ext.alloc_int_array(fllve__xehbb, np.int64)
    qbd__pleq = bodo.libs.int_arr_ext.alloc_int_array(lny__jwt, np.int64)
    nbxjs__efl = False
    for i in range(fllve__xehbb):
        if bodo.libs.array_kernels.isna(cken__jjj, i):
            bodo.libs.array_kernels.setna(ykr__ibeoa, i)
        else:
            ykr__ibeoa[i] = cken__jjj[i].rindex(sub, start, end)
    for i in range(lny__jwt):
        if bodo.libs.array_kernels.isna(arr, i
            ) or bodo.libs.array_kernels.isna(ykr__ibeoa, yvy__ahxne[i]):
            bodo.libs.array_kernels.setna(qbd__pleq, i)
        else:
            qbd__pleq[i] = ykr__ibeoa[yvy__ahxne[i]]
            if qbd__pleq[i] == -1:
                nbxjs__efl = True
    bjyyw__usxvi = 'substring not found' if nbxjs__efl else ''
    synchronize_error_njit('ValueError', bjyyw__usxvi)
    return qbd__pleq


def create_find_methods(func_name):
    hsgm__sqoc = f"""def str_{func_name}(arr, sub, start, end):
  data_arr = arr._data
  indices_arr = arr._indices
  n_data = len(data_arr)
  n_indices = len(indices_arr)
  tmp_dict_arr = bodo.libs.int_arr_ext.alloc_int_array(n_data, np.int64)
  out_int_arr = bodo.libs.int_arr_ext.alloc_int_array(n_indices, np.int64)
  for i in range(n_data):
    if bodo.libs.array_kernels.isna(data_arr, i):
      bodo.libs.array_kernels.setna(tmp_dict_arr, i)
      continue
    tmp_dict_arr[i] = data_arr[i].{func_name}(sub, start, end)
  for i in range(n_indices):
    if bodo.libs.array_kernels.isna(indices_arr, i) or bodo.libs.array_kernels.isna(
      tmp_dict_arr, indices_arr[i]
    ):
      bodo.libs.array_kernels.setna(out_int_arr, i)
    else:
      out_int_arr[i] = tmp_dict_arr[indices_arr[i]]
  return out_int_arr"""
    qmwqj__oajy = {}
    exec(hsgm__sqoc, {'bodo': bodo, 'numba': numba, 'init_dict_arr':
        init_dict_arr, 'np': np}, qmwqj__oajy)
    return qmwqj__oajy[f'str_{func_name}']


def _register_find_methods():
    nwgc__kvy = ['find', 'rfind']
    for func_name in nwgc__kvy:
        aob__xpib = create_find_methods(func_name)
        aob__xpib = register_jitable(aob__xpib)
        globals()[f'str_{func_name}'] = aob__xpib


_register_find_methods()


@register_jitable
def str_count(arr, pat, flags):
    cken__jjj = arr._data
    yvy__ahxne = arr._indices
    fllve__xehbb = len(cken__jjj)
    lny__jwt = len(yvy__ahxne)
    ykr__ibeoa = bodo.libs.int_arr_ext.alloc_int_array(fllve__xehbb, np.int64)
    dgun__dpagn = bodo.libs.int_arr_ext.alloc_int_array(lny__jwt, np.int64)
    regex = re.compile(pat, flags)
    for i in range(fllve__xehbb):
        if bodo.libs.array_kernels.isna(cken__jjj, i):
            bodo.libs.array_kernels.setna(ykr__ibeoa, i)
            continue
        ykr__ibeoa[i] = bodo.libs.str_ext.str_findall_count(regex, cken__jjj[i]
            )
    for i in range(lny__jwt):
        if bodo.libs.array_kernels.isna(yvy__ahxne, i
            ) or bodo.libs.array_kernels.isna(ykr__ibeoa, yvy__ahxne[i]):
            bodo.libs.array_kernels.setna(dgun__dpagn, i)
        else:
            dgun__dpagn[i] = ykr__ibeoa[yvy__ahxne[i]]
    return dgun__dpagn


@register_jitable
def str_len(arr):
    cken__jjj = arr._data
    yvy__ahxne = arr._indices
    lny__jwt = len(yvy__ahxne)
    ykr__ibeoa = bodo.libs.array_kernels.get_arr_lens(cken__jjj, False)
    dgun__dpagn = bodo.libs.int_arr_ext.alloc_int_array(lny__jwt, np.int64)
    for i in range(lny__jwt):
        if bodo.libs.array_kernels.isna(yvy__ahxne, i
            ) or bodo.libs.array_kernels.isna(ykr__ibeoa, yvy__ahxne[i]):
            bodo.libs.array_kernels.setna(dgun__dpagn, i)
        else:
            dgun__dpagn[i] = ykr__ibeoa[yvy__ahxne[i]]
    return dgun__dpagn


@register_jitable
def str_slice(arr, start, stop, step):
    cken__jjj = arr._data
    fllve__xehbb = len(cken__jjj)
    ribwz__qaoj = bodo.libs.str_arr_ext.pre_alloc_string_array(fllve__xehbb, -1
        )
    for i in range(fllve__xehbb):
        if bodo.libs.array_kernels.isna(cken__jjj, i):
            bodo.libs.array_kernels.setna(ribwz__qaoj, i)
            continue
        ribwz__qaoj[i] = cken__jjj[i][start:stop:step]
    return init_dict_arr(ribwz__qaoj, arr._indices.copy(), arr.
        _has_global_dictionary, False)


@register_jitable
def str_get(arr, i):
    cken__jjj = arr._data
    yvy__ahxne = arr._indices
    fllve__xehbb = len(cken__jjj)
    lny__jwt = len(yvy__ahxne)
    ribwz__qaoj = pre_alloc_string_array(fllve__xehbb, -1)
    qbd__pleq = pre_alloc_string_array(lny__jwt, -1)
    for vwv__aejnd in range(fllve__xehbb):
        if bodo.libs.array_kernels.isna(cken__jjj, vwv__aejnd) or not -len(
            cken__jjj[vwv__aejnd]) <= i < len(cken__jjj[vwv__aejnd]):
            bodo.libs.array_kernels.setna(ribwz__qaoj, vwv__aejnd)
            continue
        ribwz__qaoj[vwv__aejnd] = cken__jjj[vwv__aejnd][i]
    for vwv__aejnd in range(lny__jwt):
        if bodo.libs.array_kernels.isna(yvy__ahxne, vwv__aejnd
            ) or bodo.libs.array_kernels.isna(ribwz__qaoj, yvy__ahxne[
            vwv__aejnd]):
            bodo.libs.array_kernels.setna(qbd__pleq, vwv__aejnd)
            continue
        qbd__pleq[vwv__aejnd] = ribwz__qaoj[yvy__ahxne[vwv__aejnd]]
    return qbd__pleq


@register_jitable
def str_repeat_int(arr, repeats):
    cken__jjj = arr._data
    fllve__xehbb = len(cken__jjj)
    ribwz__qaoj = pre_alloc_string_array(fllve__xehbb, -1)
    for i in range(fllve__xehbb):
        if bodo.libs.array_kernels.isna(cken__jjj, i):
            bodo.libs.array_kernels.setna(ribwz__qaoj, i)
            continue
        ribwz__qaoj[i] = cken__jjj[i] * repeats
    return init_dict_arr(ribwz__qaoj, arr._indices.copy(), arr.
        _has_global_dictionary, arr._has_deduped_local_dictionary and 
        repeats != 0)


def create_str2bool_methods(func_name):
    hsgm__sqoc = f"""def str_{func_name}(arr):
    data_arr = arr._data
    indices_arr = arr._indices
    n_data = len(data_arr)
    n_indices = len(indices_arr)
    out_dict_arr = bodo.libs.bool_arr_ext.alloc_bool_array(n_data)
    out_bool_arr = bodo.libs.bool_arr_ext.alloc_bool_array(n_indices)
    for i in range(n_data):
        if bodo.libs.array_kernels.isna(data_arr, i):
            bodo.libs.array_kernels.setna(out_dict_arr, i)
            continue
        out_dict_arr[i] = np.bool_(data_arr[i].{func_name}())
    for i in range(n_indices):
        if bodo.libs.array_kernels.isna(indices_arr, i) or bodo.libs.array_kernels.isna(
            data_arr, indices_arr[i]        ):
            bodo.libs.array_kernels.setna(out_bool_arr, i)
        else:
            out_bool_arr[i] = out_dict_arr[indices_arr[i]]
    return out_bool_arr"""
    qmwqj__oajy = {}
    exec(hsgm__sqoc, {'bodo': bodo, 'numba': numba, 'np': np,
        'init_dict_arr': init_dict_arr}, qmwqj__oajy)
    return qmwqj__oajy[f'str_{func_name}']


def _register_str2bool_methods():
    for func_name in bodo.hiframes.pd_series_ext.str2bool_methods:
        aob__xpib = create_str2bool_methods(func_name)
        aob__xpib = register_jitable(aob__xpib)
        globals()[f'str_{func_name}'] = aob__xpib


_register_str2bool_methods()


@register_jitable
def str_extract(arr, pat, flags, n_cols):
    cken__jjj = arr._data
    yvy__ahxne = arr._indices
    fllve__xehbb = len(cken__jjj)
    lny__jwt = len(yvy__ahxne)
    regex = re.compile(pat, flags=flags)
    cmx__mxgm = []
    for mxb__hmm in range(n_cols):
        cmx__mxgm.append(pre_alloc_string_array(fllve__xehbb, -1))
    hlyjc__fbvbu = bodo.libs.bool_arr_ext.alloc_bool_array(fllve__xehbb)
    umkgj__ugiy = yvy__ahxne.copy()
    for i in range(fllve__xehbb):
        if bodo.libs.array_kernels.isna(cken__jjj, i):
            hlyjc__fbvbu[i] = True
            for vwv__aejnd in range(n_cols):
                bodo.libs.array_kernels.setna(cmx__mxgm[vwv__aejnd], i)
            continue
        ewp__oaduj = regex.search(cken__jjj[i])
        if ewp__oaduj:
            hlyjc__fbvbu[i] = False
            doetn__skr = ewp__oaduj.groups()
            for vwv__aejnd in range(n_cols):
                cmx__mxgm[vwv__aejnd][i] = doetn__skr[vwv__aejnd]
        else:
            hlyjc__fbvbu[i] = True
            for vwv__aejnd in range(n_cols):
                bodo.libs.array_kernels.setna(cmx__mxgm[vwv__aejnd], i)
    for i in range(lny__jwt):
        if hlyjc__fbvbu[umkgj__ugiy[i]]:
            bodo.libs.array_kernels.setna(umkgj__ugiy, i)
    hexh__abd = [init_dict_arr(cmx__mxgm[i], umkgj__ugiy.copy(), arr.
        _has_global_dictionary, False) for i in range(n_cols)]
    return hexh__abd


def create_extractall_methods(is_multi_group):
    txpr__psj = '_multi' if is_multi_group else ''
    hsgm__sqoc = f"""def str_extractall{txpr__psj}(arr, regex, n_cols, index_arr):
    data_arr = arr._data
    indices_arr = arr._indices
    n_data = len(data_arr)
    n_indices = len(indices_arr)
    indices_count = [0 for _ in range(n_data)]
    for i in range(n_indices):
        if not bodo.libs.array_kernels.isna(indices_arr, i):
            indices_count[indices_arr[i]] += 1
    dict_group_count = []
    out_dict_len = out_ind_len = 0
    for i in range(n_data):
        if bodo.libs.array_kernels.isna(data_arr, i):
            continue
        m = regex.findall(data_arr[i])
        dict_group_count.append((out_dict_len, len(m)))
        out_dict_len += len(m)
        out_ind_len += indices_count[i] * len(m)
    out_dict_arr_list = []
    for _ in range(n_cols):
        out_dict_arr_list.append(pre_alloc_string_array(out_dict_len, -1))
    out_indices_arr = bodo.libs.int_arr_ext.alloc_int_array(out_ind_len, np.int32)
    out_ind_arr = bodo.utils.utils.alloc_type(out_ind_len, index_arr, (-1,))
    out_match_arr = np.empty(out_ind_len, np.int64)
    curr_ind = 0
    for i in range(n_data):
        if bodo.libs.array_kernels.isna(data_arr, i):
            continue
        m = regex.findall(data_arr[i])
        for s in m:
            for j in range(n_cols):
                out_dict_arr_list[j][curr_ind] = s{'[j]' if is_multi_group else ''}
            curr_ind += 1
    curr_ind = 0
    for i in range(n_indices):
        if bodo.libs.array_kernels.isna(indices_arr, i):
            continue
        n_rows = dict_group_count[indices_arr[i]][1]
        for k in range(n_rows):
            out_indices_arr[curr_ind] = dict_group_count[indices_arr[i]][0] + k
            out_ind_arr[curr_ind] = index_arr[i]
            out_match_arr[curr_ind] = k
            curr_ind += 1
    out_arr_list = [
        init_dict_arr(
            out_dict_arr_list[i], out_indices_arr.copy(), arr._has_global_dictionary, False
        )
        for i in range(n_cols)
    ]
    return (out_ind_arr, out_match_arr, out_arr_list) 
"""
    qmwqj__oajy = {}
    exec(hsgm__sqoc, {'bodo': bodo, 'numba': numba, 'np': np,
        'init_dict_arr': init_dict_arr, 'pre_alloc_string_array':
        pre_alloc_string_array}, qmwqj__oajy)
    return qmwqj__oajy[f'str_extractall{txpr__psj}']


def _register_extractall_methods():
    for is_multi_group in [True, False]:
        txpr__psj = '_multi' if is_multi_group else ''
        aob__xpib = create_extractall_methods(is_multi_group)
        aob__xpib = register_jitable(aob__xpib)
        globals()[f'str_extractall{txpr__psj}'] = aob__xpib


_register_extractall_methods()
