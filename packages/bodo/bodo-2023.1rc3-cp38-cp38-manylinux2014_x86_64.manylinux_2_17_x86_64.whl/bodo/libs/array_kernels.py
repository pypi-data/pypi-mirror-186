"""
Implements array kernels such as median and quantile.
"""
import hashlib
import inspect
import math
import operator
import re
import warnings
from math import sqrt
import llvmlite.binding as ll
import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from numba.core import cgutils, types, typing
from numba.core.imputils import lower_builtin
from numba.core.ir_utils import find_const, guard
from numba.core.typing import signature
from numba.core.typing.templates import AbstractTemplate, infer_global
from numba.extending import overload, overload_attribute, register_jitable
from numba.np.arrayobj import make_array
from numba.np.numpy_support import as_dtype
from numba.parfors.array_analysis import ArrayAnalysis
import bodo
from bodo.hiframes.datetime_date_ext import datetime_date_array_type
from bodo.hiframes.datetime_timedelta_ext import datetime_timedelta_array_type
from bodo.hiframes.pd_categorical_ext import CategoricalArrayType, init_categorical_array
from bodo.hiframes.split_impl import string_array_split_view_type
from bodo.hiframes.time_ext import TimeArrayType
from bodo.libs import quantile_alg
from bodo.libs.array import arr_info_list_to_table, array_to_info, delete_info_decref_array, delete_table, delete_table_decref_arrays, drop_duplicates_local_dictionary, drop_duplicates_table, info_from_table, info_to_array, sample_table
from bodo.libs.array_item_arr_ext import ArrayItemArrayType, offset_type
from bodo.libs.bool_arr_ext import BooleanArrayType, boolean_array
from bodo.libs.decimal_arr_ext import DecimalArrayType
from bodo.libs.dict_arr_ext import DictionaryArrayType, init_dict_arr
from bodo.libs.distributed_api import Reduce_Type
from bodo.libs.float_arr_ext import FloatingArrayType
from bodo.libs.int_arr_ext import IntegerArrayType, alloc_int_array
from bodo.libs.pd_datetime_arr_ext import DatetimeArrayType
from bodo.libs.str_arr_ext import pre_alloc_string_array, str_arr_set_na, string_array_type
from bodo.libs.struct_arr_ext import StructArrayType
from bodo.libs.tuple_arr_ext import TupleArrayType
from bodo.utils.indexing import add_nested_counts, init_nested_counts
from bodo.utils.typing import BodoError, check_unsupported_args, decode_if_dict_array, element_type, find_common_np_dtype, get_overload_const_bool, get_overload_const_list, get_overload_const_str, is_bin_arr_type, is_overload_constant_bool, is_overload_constant_str, is_overload_none, is_overload_true, is_str_arr_type, raise_bodo_error, to_str_arr_if_dict_array
from bodo.utils.utils import build_set_seen_na, check_and_propagate_cpp_exception, numba_to_c_type, unliteral_all
ll.add_symbol('quantile_sequential', quantile_alg.quantile_sequential)
ll.add_symbol('quantile_parallel', quantile_alg.quantile_parallel)
MPI_ROOT = 0
sum_op = np.int32(bodo.libs.distributed_api.Reduce_Type.Sum.value)
max_op = np.int32(bodo.libs.distributed_api.Reduce_Type.Max.value)
min_op = np.int32(bodo.libs.distributed_api.Reduce_Type.Min.value)


def isna(arr, i):
    return False


@overload(isna)
def overload_isna(arr, i):
    i = types.unliteral(i)
    if arr == string_array_type:
        return lambda arr, i: bodo.libs.str_arr_ext.str_arr_is_na(arr, i)
    if isinstance(arr, (IntegerArrayType, FloatingArrayType,
        DecimalArrayType, TimeArrayType)) or arr in (boolean_array,
        datetime_date_array_type, datetime_timedelta_array_type,
        string_array_split_view_type):
        return lambda arr, i: not bodo.libs.int_arr_ext.get_bit_bitmap_arr(arr
            ._null_bitmap, i)
    if isinstance(arr, ArrayItemArrayType):
        return lambda arr, i: not bodo.libs.int_arr_ext.get_bit_bitmap_arr(bodo
            .libs.array_item_arr_ext.get_null_bitmap(arr), i)
    if isinstance(arr, bodo.libs.map_arr_ext.MapArrayType):
        return lambda arr, i: not bodo.libs.int_arr_ext.get_bit_bitmap_arr(bodo
            .libs.array_item_arr_ext.get_null_bitmap(arr._data), i)
    if isinstance(arr, StructArrayType):
        return lambda arr, i: not bodo.libs.int_arr_ext.get_bit_bitmap_arr(bodo
            .libs.struct_arr_ext.get_null_bitmap(arr), i)
    if isinstance(arr, TupleArrayType):
        return lambda arr, i: bodo.libs.array_kernels.isna(arr._data, i)
    if isinstance(arr, bodo.hiframes.pd_categorical_ext.CategoricalArrayType):
        return lambda arr, i: arr.codes[i] == -1
    if arr == bodo.binary_array_type:
        return lambda arr, i: not bodo.libs.int_arr_ext.get_bit_bitmap_arr(bodo
            .libs.array_item_arr_ext.get_null_bitmap(arr._data), i)
    if isinstance(arr, types.List):
        if arr.dtype == types.none:
            return lambda arr, i: True
        elif isinstance(arr.dtype, types.optional):
            return lambda arr, i: arr[i] is None
        else:
            return lambda arr, i: False
    if isinstance(arr, bodo.NullableTupleType):
        return lambda arr, i: arr._null_values[i]
    if isinstance(arr, DictionaryArrayType):
        return lambda arr, i: not bodo.libs.int_arr_ext.get_bit_bitmap_arr(arr
            ._indices._null_bitmap, i) or bodo.libs.array_kernels.isna(arr.
            _data, arr._indices[i])
    if isinstance(arr, DatetimeArrayType):
        return lambda arr, i: np.isnat(arr._data[i])
    assert isinstance(arr, types.Array), f'Invalid array type in isna(): {arr}'
    dtype = arr.dtype
    if isinstance(dtype, types.Float):
        return lambda arr, i: np.isnan(arr[i])
    if isinstance(dtype, (types.NPDatetime, types.NPTimedelta)):
        return lambda arr, i: np.isnat(arr[i])
    return lambda arr, i: False


def setna(arr, ind, int_nan_const=0):
    arr[ind] = np.nan


@overload(setna, no_unliteral=True)
def setna_overload(arr, ind, int_nan_const=0):
    if isinstance(arr, types.Array) and isinstance(arr.dtype, types.Float):
        return setna
    if isinstance(arr.dtype, (types.NPDatetime, types.NPTimedelta)):
        paizq__tsid = arr.dtype('NaT')

        def _setnan_impl(arr, ind, int_nan_const=0):
            arr[ind] = paizq__tsid
        return _setnan_impl
    if isinstance(arr, DatetimeArrayType):
        paizq__tsid = bodo.datetime64ns('NaT')

        def _setnan_impl(arr, ind, int_nan_const=0):
            arr._data[ind] = paizq__tsid
        return _setnan_impl
    if arr == string_array_type:

        def impl(arr, ind, int_nan_const=0):
            arr[ind] = ''
            str_arr_set_na(arr, ind)
        return impl
    if isinstance(arr, DictionaryArrayType):
        return lambda arr, ind, int_nan_const=0: bodo.libs.array_kernels.setna(
            arr._indices, ind)
    if arr == boolean_array:

        def impl(arr, ind, int_nan_const=0):
            arr[ind] = False
            bodo.libs.int_arr_ext.set_bit_to_arr(arr._null_bitmap, ind, 0)
        return impl
    if isinstance(arr, (IntegerArrayType, FloatingArrayType, DecimalArrayType)
        ):
        return (lambda arr, ind, int_nan_const=0: bodo.libs.int_arr_ext.
            set_bit_to_arr(arr._null_bitmap, ind, 0))
    if arr == bodo.binary_array_type:

        def impl_binary_arr(arr, ind, int_nan_const=0):
            zzj__trbp = bodo.libs.array_item_arr_ext.get_offsets(arr._data)
            zzj__trbp[ind + 1] = zzj__trbp[ind]
            bodo.libs.int_arr_ext.set_bit_to_arr(bodo.libs.
                array_item_arr_ext.get_null_bitmap(arr._data), ind, 0)
        return impl_binary_arr
    if isinstance(arr, bodo.libs.array_item_arr_ext.ArrayItemArrayType):

        def impl_arr_item(arr, ind, int_nan_const=0):
            zzj__trbp = bodo.libs.array_item_arr_ext.get_offsets(arr)
            zzj__trbp[ind + 1] = zzj__trbp[ind]
            bodo.libs.int_arr_ext.set_bit_to_arr(bodo.libs.
                array_item_arr_ext.get_null_bitmap(arr), ind, 0)
        return impl_arr_item
    if isinstance(arr, bodo.libs.map_arr_ext.MapArrayType):

        def impl_arr_item(arr, ind, int_nan_const=0):
            zzj__trbp = bodo.libs.array_item_arr_ext.get_offsets(arr._data)
            zzj__trbp[ind + 1] = zzj__trbp[ind]
            bodo.libs.int_arr_ext.set_bit_to_arr(bodo.libs.
                array_item_arr_ext.get_null_bitmap(arr._data), ind, 0)
        return impl_arr_item
    if isinstance(arr, bodo.libs.struct_arr_ext.StructArrayType):

        def impl(arr, ind, int_nan_const=0):
            bodo.libs.int_arr_ext.set_bit_to_arr(bodo.libs.struct_arr_ext.
                get_null_bitmap(arr), ind, 0)
            data = bodo.libs.struct_arr_ext.get_data(arr)
            setna_tup(data, ind)
        return impl
    if isinstance(arr, TupleArrayType):

        def impl(arr, ind, int_nan_const=0):
            bodo.libs.array_kernels.setna(arr._data, ind)
        return impl
    if arr.dtype == types.bool_:

        def b_set(arr, ind, int_nan_const=0):
            arr[ind] = False
        return b_set
    if isinstance(arr, bodo.hiframes.pd_categorical_ext.CategoricalArrayType):

        def setna_cat(arr, ind, int_nan_const=0):
            arr.codes[ind] = -1
        return setna_cat
    if isinstance(arr.dtype, types.Integer):

        def setna_int(arr, ind, int_nan_const=0):
            arr[ind] = int_nan_const
        return setna_int
    if arr == datetime_date_array_type:

        def setna_datetime_date(arr, ind, int_nan_const=0):
            arr._data[ind] = (1970 << 32) + (1 << 16) + 1
            bodo.libs.int_arr_ext.set_bit_to_arr(arr._null_bitmap, ind, 0)
        return setna_datetime_date
    if isinstance(arr, bodo.TimeArrayType):

        def setna_time(arr, ind, int_nan_const=0):
            bodo.libs.int_arr_ext.set_bit_to_arr(arr._null_bitmap, ind, 0)
        return setna_time
    if arr == datetime_timedelta_array_type:

        def setna_datetime_timedelta(arr, ind, int_nan_const=0):
            bodo.libs.array_kernels.setna(arr._days_data, ind)
            bodo.libs.array_kernels.setna(arr._seconds_data, ind)
            bodo.libs.array_kernels.setna(arr._microseconds_data, ind)
            bodo.libs.int_arr_ext.set_bit_to_arr(arr._null_bitmap, ind, 0)
        return setna_datetime_timedelta
    return lambda arr, ind, int_nan_const=0: None


def copy_array_element(out_arr, out_ind, in_arr, in_ind):
    pass


@overload(copy_array_element)
def overload_copy_array_element(out_arr, out_ind, in_arr, in_ind):
    if out_arr == bodo.string_array_type and is_str_arr_type(in_arr):

        def impl_str(out_arr, out_ind, in_arr, in_ind):
            if bodo.libs.array_kernels.isna(in_arr, in_ind):
                bodo.libs.array_kernels.setna(out_arr, out_ind)
            else:
                bodo.libs.str_arr_ext.get_str_arr_item_copy(out_arr,
                    out_ind, in_arr, in_ind)
        return impl_str
    if isinstance(out_arr, DatetimeArrayType) and isinstance(in_arr,
        DatetimeArrayType) and out_arr.tz == in_arr.tz:

        def impl_dt(out_arr, out_ind, in_arr, in_ind):
            if bodo.libs.array_kernels.isna(in_arr, in_ind):
                bodo.libs.array_kernels.setna(out_arr, out_ind)
            else:
                out_arr._data[out_ind] = in_arr._data[in_ind]
        return impl_dt

    def impl(out_arr, out_ind, in_arr, in_ind):
        if bodo.libs.array_kernels.isna(in_arr, in_ind):
            bodo.libs.array_kernels.setna(out_arr, out_ind)
        else:
            out_arr[out_ind] = in_arr[in_ind]
    return impl


def setna_tup(arr_tup, ind, int_nan_const=0):
    pass


@overload(setna_tup, no_unliteral=True)
def overload_setna_tup(arr_tup, ind, int_nan_const=0):
    bkue__pnt = arr_tup.count
    xybk__dhl = 'def f(arr_tup, ind, int_nan_const=0):\n'
    for i in range(bkue__pnt):
        xybk__dhl += '  setna(arr_tup[{}], ind, int_nan_const)\n'.format(i)
    xybk__dhl += '  return\n'
    agnk__yixr = {}
    exec(xybk__dhl, {'setna': setna}, agnk__yixr)
    impl = agnk__yixr['f']
    return impl


def setna_slice(arr, s):
    arr[s] = np.nan


@overload(setna_slice, no_unliteral=True)
def overload_setna_slice(arr, s):

    def impl(arr, s):
        lllqa__rlul = numba.cpython.unicode._normalize_slice(s, len(arr))
        for i in range(lllqa__rlul.start, lllqa__rlul.stop, lllqa__rlul.step):
            setna(arr, i)
    return impl


@numba.generated_jit
def first_last_valid_index(arr, index_arr, is_first=True, parallel=False):
    is_first = get_overload_const_bool(is_first)
    if is_first:
        czm__fux = 'n'
        xqke__qze = 'n_pes'
        brds__zjogg = 'min_op'
    else:
        czm__fux = 'n-1, -1, -1'
        xqke__qze = '-1'
        brds__zjogg = 'max_op'
    xybk__dhl = f"""def impl(arr, index_arr, is_first=True, parallel=False):
    n = len(arr)
    index_value = index_arr[0]
    has_valid = False
    loc_valid_rank = -1
    if parallel:
        rank = bodo.libs.distributed_api.get_rank()
        n_pes = bodo.libs.distributed_api.get_size()
        loc_valid_rank = {xqke__qze}
    for i in range({czm__fux}):
        if not isna(arr, i):
            if parallel:
                loc_valid_rank = rank
            index_value = index_arr[i]
            has_valid = True
            break
    if parallel:
        possible_valid_rank = np.int32(bodo.libs.distributed_api.dist_reduce(loc_valid_rank, {brds__zjogg}))
        if possible_valid_rank != {xqke__qze}:
            has_valid = True
            index_value = bodo.libs.distributed_api.bcast_scalar(index_value, possible_valid_rank)
    return has_valid, box_if_dt64(index_value)

    """
    agnk__yixr = {}
    exec(xybk__dhl, {'np': np, 'bodo': bodo, 'isna': isna, 'max_op': max_op,
        'min_op': min_op, 'box_if_dt64': bodo.utils.conversion.box_if_dt64},
        agnk__yixr)
    impl = agnk__yixr['impl']
    return impl


ll.add_symbol('median_series_computation', quantile_alg.
    median_series_computation)
_median_series_computation = types.ExternalFunction('median_series_computation'
    , types.void(types.voidptr, bodo.libs.array.array_info_type, types.
    bool_, types.bool_))


@numba.njit
def median_series_computation(res, arr, is_parallel, skipna):
    gdh__amwvk = array_to_info(arr)
    _median_series_computation(res, gdh__amwvk, is_parallel, skipna)
    check_and_propagate_cpp_exception()
    delete_info_decref_array(gdh__amwvk)


ll.add_symbol('autocorr_series_computation', quantile_alg.
    autocorr_series_computation)
_autocorr_series_computation = types.ExternalFunction(
    'autocorr_series_computation', types.void(types.voidptr, bodo.libs.
    array.array_info_type, types.int64, types.bool_))


@numba.njit
def autocorr_series_computation(res, arr, lag, is_parallel):
    gdh__amwvk = array_to_info(arr)
    _autocorr_series_computation(res, gdh__amwvk, lag, is_parallel)
    check_and_propagate_cpp_exception()
    delete_info_decref_array(gdh__amwvk)


@numba.njit
def autocorr(arr, lag=1, parallel=False):
    res = np.empty(1, types.float64)
    autocorr_series_computation(res.ctypes, arr, lag, parallel)
    return res[0]


ll.add_symbol('compute_series_monotonicity', quantile_alg.
    compute_series_monotonicity)
_compute_series_monotonicity = types.ExternalFunction(
    'compute_series_monotonicity', types.void(types.voidptr, bodo.libs.
    array.array_info_type, types.int64, types.bool_))


@numba.njit
def series_monotonicity_call(res, arr, inc_dec, is_parallel):
    gdh__amwvk = array_to_info(arr)
    _compute_series_monotonicity(res, gdh__amwvk, inc_dec, is_parallel)
    check_and_propagate_cpp_exception()
    delete_info_decref_array(gdh__amwvk)


@numba.njit
def series_monotonicity(arr, inc_dec, parallel=False):
    res = np.empty(1, types.float64)
    series_monotonicity_call(res.ctypes, arr, inc_dec, parallel)
    xssos__jaz = res[0] > 0.5
    return xssos__jaz


@numba.generated_jit(nopython=True)
def get_valid_entries_from_date_offset(index_arr, offset, initial_date,
    is_last, is_parallel=False):
    if get_overload_const_bool(is_last):
        xvh__yev = '-'
        czg__sxoa = 'index_arr[0] > threshhold_date'
        czm__fux = '1, n+1'
        sfrb__vnfb = 'index_arr[-i] <= threshhold_date'
        rvkht__gehg = 'i - 1'
    else:
        xvh__yev = '+'
        czg__sxoa = 'index_arr[-1] < threshhold_date'
        czm__fux = 'n'
        sfrb__vnfb = 'index_arr[i] >= threshhold_date'
        rvkht__gehg = 'i'
    xybk__dhl = (
        'def impl(index_arr, offset, initial_date, is_last, is_parallel=False):\n'
        )
    if types.unliteral(offset) == types.unicode_type:
        xybk__dhl += (
            '  with numba.objmode(threshhold_date=bodo.pd_timestamp_tz_naive_type):\n'
            )
        xybk__dhl += (
            '    date_offset = pd.tseries.frequencies.to_offset(offset)\n')
        if not get_overload_const_bool(is_last):
            xybk__dhl += """    if not isinstance(date_offset, pd._libs.tslibs.Tick) and date_offset.is_on_offset(index_arr[0]):
"""
            xybk__dhl += (
                '      threshhold_date = initial_date - date_offset.base + date_offset\n'
                )
            xybk__dhl += '    else:\n'
            xybk__dhl += '      threshhold_date = initial_date + date_offset\n'
        else:
            xybk__dhl += (
                f'    threshhold_date = initial_date {xvh__yev} date_offset\n')
    else:
        xybk__dhl += f'  threshhold_date = initial_date {xvh__yev} offset\n'
    xybk__dhl += '  local_valid = 0\n'
    xybk__dhl += f'  n = len(index_arr)\n'
    xybk__dhl += f'  if n:\n'
    xybk__dhl += f'    if {czg__sxoa}:\n'
    xybk__dhl += '      loc_valid = n\n'
    xybk__dhl += '    else:\n'
    xybk__dhl += f'      for i in range({czm__fux}):\n'
    xybk__dhl += f'        if {sfrb__vnfb}:\n'
    xybk__dhl += f'          loc_valid = {rvkht__gehg}\n'
    xybk__dhl += '          break\n'
    xybk__dhl += '  if is_parallel:\n'
    xybk__dhl += (
        '    total_valid = bodo.libs.distributed_api.dist_reduce(loc_valid, sum_op)\n'
        )
    xybk__dhl += '    return total_valid\n'
    xybk__dhl += '  else:\n'
    xybk__dhl += '    return loc_valid\n'
    agnk__yixr = {}
    exec(xybk__dhl, {'bodo': bodo, 'pd': pd, 'numba': numba, 'sum_op':
        sum_op}, agnk__yixr)
    return agnk__yixr['impl']


def quantile(A, q):
    pass


def quantile_parallel(A, q):
    pass


@infer_global(quantile)
@infer_global(quantile_parallel)
class QuantileType(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        assert len(args) in [2, 3]
        return signature(types.float64, *unliteral_all(args))


@lower_builtin(quantile, types.Array, types.float64)
@lower_builtin(quantile, IntegerArrayType, types.float64)
@lower_builtin(quantile, FloatingArrayType, types.float64)
@lower_builtin(quantile, BooleanArrayType, types.float64)
def lower_dist_quantile_seq(context, builder, sig, args):
    rpju__xbicx = numba_to_c_type(sig.args[0].dtype)
    ilru__pfvj = cgutils.alloca_once_value(builder, lir.Constant(lir.
        IntType(32), rpju__xbicx))
    fij__sils = args[0]
    kyjb__nmu = sig.args[0]
    if isinstance(kyjb__nmu, (IntegerArrayType, FloatingArrayType,
        BooleanArrayType)):
        fij__sils = cgutils.create_struct_proxy(kyjb__nmu)(context, builder,
            fij__sils).data
        kyjb__nmu = types.Array(kyjb__nmu.dtype, 1, 'C')
    assert kyjb__nmu.ndim == 1
    arr = make_array(kyjb__nmu)(context, builder, fij__sils)
    euez__yqsnp = builder.extract_value(arr.shape, 0)
    qhu__sfw = [builder.bitcast(arr.data, lir.IntType(8).as_pointer()),
        euez__yqsnp, args[1], builder.load(ilru__pfvj)]
    nhcm__bcyyb = [lir.IntType(8).as_pointer(), lir.IntType(64), lir.
        DoubleType(), lir.IntType(32)]
    rgj__fbwue = lir.FunctionType(lir.DoubleType(), nhcm__bcyyb)
    okq__izvn = cgutils.get_or_insert_function(builder.module, rgj__fbwue,
        name='quantile_sequential')
    htv__yxyai = builder.call(okq__izvn, qhu__sfw)
    bodo.utils.utils.inlined_check_and_propagate_cpp_exception(context, builder
        )
    return htv__yxyai


@lower_builtin(quantile_parallel, types.Array, types.float64, types.intp)
@lower_builtin(quantile_parallel, IntegerArrayType, types.float64, types.intp)
@lower_builtin(quantile_parallel, FloatingArrayType, types.float64, types.intp)
@lower_builtin(quantile_parallel, BooleanArrayType, types.float64, types.intp)
def lower_dist_quantile_parallel(context, builder, sig, args):
    rpju__xbicx = numba_to_c_type(sig.args[0].dtype)
    ilru__pfvj = cgutils.alloca_once_value(builder, lir.Constant(lir.
        IntType(32), rpju__xbicx))
    fij__sils = args[0]
    kyjb__nmu = sig.args[0]
    if isinstance(kyjb__nmu, (IntegerArrayType, FloatingArrayType,
        BooleanArrayType)):
        fij__sils = cgutils.create_struct_proxy(kyjb__nmu)(context, builder,
            fij__sils).data
        kyjb__nmu = types.Array(kyjb__nmu.dtype, 1, 'C')
    assert kyjb__nmu.ndim == 1
    arr = make_array(kyjb__nmu)(context, builder, fij__sils)
    euez__yqsnp = builder.extract_value(arr.shape, 0)
    if len(args) == 3:
        homw__rkd = args[2]
    else:
        homw__rkd = euez__yqsnp
    qhu__sfw = [builder.bitcast(arr.data, lir.IntType(8).as_pointer()),
        euez__yqsnp, homw__rkd, args[1], builder.load(ilru__pfvj)]
    nhcm__bcyyb = [lir.IntType(8).as_pointer(), lir.IntType(64), lir.
        IntType(64), lir.DoubleType(), lir.IntType(32)]
    rgj__fbwue = lir.FunctionType(lir.DoubleType(), nhcm__bcyyb)
    okq__izvn = cgutils.get_or_insert_function(builder.module, rgj__fbwue,
        name='quantile_parallel')
    htv__yxyai = builder.call(okq__izvn, qhu__sfw)
    bodo.utils.utils.inlined_check_and_propagate_cpp_exception(context, builder
        )
    return htv__yxyai


@numba.generated_jit(nopython=True)
def _rank_detect_ties(arr):

    def impl(arr):
        n = len(arr)
        kcr__erq = bodo.utils.utils.alloc_type(n, np.bool_, (-1,))
        kcr__erq[0] = True
        bdx__ozox = pd.isna(arr)
        for i in range(1, len(arr)):
            if bdx__ozox[i] and bdx__ozox[i - 1]:
                kcr__erq[i] = False
            elif bdx__ozox[i] or bdx__ozox[i - 1]:
                kcr__erq[i] = True
            else:
                kcr__erq[i] = arr[i] != arr[i - 1]
        return kcr__erq
    return impl


def rank(arr, method='average', na_option='keep', ascending=True, pct=False):
    pass


@overload(rank, no_unliteral=True, inline='always')
def overload_rank(arr, method='average', na_option='keep', ascending=True,
    pct=False):
    if not is_overload_constant_str(method):
        raise_bodo_error(
            "Series.rank(): 'method' argument must be a constant string")
    method = get_overload_const_str(method)
    if not is_overload_constant_str(na_option):
        raise_bodo_error(
            "Series.rank(): 'na_option' argument must be a constant string")
    na_option = get_overload_const_str(na_option)
    if not is_overload_constant_bool(ascending):
        raise_bodo_error(
            "Series.rank(): 'ascending' argument must be a constant boolean")
    ascending = get_overload_const_bool(ascending)
    if not is_overload_constant_bool(pct):
        raise_bodo_error(
            "Series.rank(): 'pct' argument must be a constant boolean")
    pct = get_overload_const_bool(pct)
    if method == 'first' and not ascending:
        raise BodoError(
            "Series.rank(): method='first' with ascending=False is currently unsupported."
            )
    xybk__dhl = (
        "def impl(arr, method='average', na_option='keep', ascending=True, pct=False):\n"
        )
    xybk__dhl += '  na_idxs = pd.isna(arr)\n'
    xybk__dhl += '  sorter = bodo.hiframes.series_impl.argsort(arr)\n'
    xybk__dhl += '  nas = sum(na_idxs)\n'
    if not ascending:
        xybk__dhl += '  if nas and nas < (sorter.size - 1):\n'
        xybk__dhl += '    sorter[:-nas] = sorter[-(nas + 1)::-1]\n'
        xybk__dhl += '  else:\n'
        xybk__dhl += '    sorter = sorter[::-1]\n'
    if na_option == 'top':
        xybk__dhl += (
            '  sorter = np.concatenate((sorter[-nas:], sorter[:-nas]))\n')
    xybk__dhl += '  inv = np.empty(sorter.size, dtype=np.intp)\n'
    xybk__dhl += '  inv[sorter] = np.arange(sorter.size)\n'
    if method == 'first':
        xybk__dhl += '  ret = bodo.utils.conversion.fix_arr_dtype(\n'
        xybk__dhl += '    inv,\n'
        xybk__dhl += '    new_dtype=np.float64,\n'
        xybk__dhl += '    copy=True,\n'
        xybk__dhl += '    nan_to_str=False,\n'
        xybk__dhl += '    from_series=True,\n'
        xybk__dhl += '    ) + 1\n'
    else:
        xybk__dhl += '  arr = arr[sorter]\n'
        xybk__dhl += '  obs = bodo.libs.array_kernels._rank_detect_ties(arr)\n'
        xybk__dhl += '  dense = obs.cumsum()[inv]\n'
        if method == 'dense':
            xybk__dhl += '  ret = bodo.utils.conversion.fix_arr_dtype(\n'
            xybk__dhl += '    dense,\n'
            xybk__dhl += '    new_dtype=np.float64,\n'
            xybk__dhl += '    copy=True,\n'
            xybk__dhl += '    nan_to_str=False,\n'
            xybk__dhl += '    from_series=True,\n'
            xybk__dhl += '  )\n'
        else:
            xybk__dhl += (
                '  count = np.concatenate((np.nonzero(obs)[0], np.array([len(obs)])))\n'
                )
            xybk__dhl += """  count_float = bodo.utils.conversion.fix_arr_dtype(count, new_dtype=np.float64, copy=True, nan_to_str=False, from_series=True)
"""
            if method == 'max':
                xybk__dhl += '  ret = count_float[dense]\n'
            elif method == 'min':
                xybk__dhl += '  ret = count_float[dense - 1] + 1\n'
            else:
                xybk__dhl += (
                    '  ret = 0.5 * (count_float[dense] + count_float[dense - 1] + 1)\n'
                    )
    if pct:
        if method == 'dense':
            if na_option == 'keep':
                xybk__dhl += '  ret[na_idxs] = -1\n'
            xybk__dhl += '  div_val = np.max(ret)\n'
        elif na_option == 'keep':
            xybk__dhl += '  div_val = arr.size - nas\n'
        else:
            xybk__dhl += '  div_val = arr.size\n'
        xybk__dhl += '  for i in range(len(ret)):\n'
        xybk__dhl += '    ret[i] = ret[i] / div_val\n'
    if na_option == 'keep':
        xybk__dhl += '  ret[na_idxs] = np.nan\n'
    xybk__dhl += '  return ret\n'
    agnk__yixr = {}
    exec(xybk__dhl, {'np': np, 'pd': pd, 'bodo': bodo}, agnk__yixr)
    return agnk__yixr['impl']


@numba.njit
def min_heapify(arr, ind_arr, n, start, cmp_f):
    acwt__fet = start
    cagzd__rkwf = 2 * start + 1
    qips__xnut = 2 * start + 2
    if cagzd__rkwf < n and not cmp_f(arr[cagzd__rkwf], arr[acwt__fet]):
        acwt__fet = cagzd__rkwf
    if qips__xnut < n and not cmp_f(arr[qips__xnut], arr[acwt__fet]):
        acwt__fet = qips__xnut
    if acwt__fet != start:
        arr[start], arr[acwt__fet] = arr[acwt__fet], arr[start]
        ind_arr[start], ind_arr[acwt__fet] = ind_arr[acwt__fet], ind_arr[start]
        min_heapify(arr, ind_arr, n, acwt__fet, cmp_f)


def select_k_nonan(A, index_arr, m, k):
    return A[:k]


@overload(select_k_nonan, no_unliteral=True)
def select_k_nonan_overload(A, index_arr, m, k):
    dtype = A.dtype
    if isinstance(dtype, types.Integer):
        return lambda A, index_arr, m, k: (A[:k].copy(), index_arr[:k].copy
            (), k)

    def select_k_nonan_float(A, index_arr, m, k):
        suay__szlz = np.empty(k, A.dtype)
        gyynx__rjk = np.empty(k, index_arr.dtype)
        i = 0
        ind = 0
        while i < m and ind < k:
            if not bodo.libs.array_kernels.isna(A, i):
                suay__szlz[ind] = A[i]
                gyynx__rjk[ind] = index_arr[i]
                ind += 1
            i += 1
        if ind < k:
            suay__szlz = suay__szlz[:ind]
            gyynx__rjk = gyynx__rjk[:ind]
        return suay__szlz, gyynx__rjk, i
    return select_k_nonan_float


@numba.njit
def nlargest(A, index_arr, k, is_largest, cmp_f):
    A = bodo.utils.conversion.coerce_to_ndarray(A)
    m = len(A)
    if k == 0:
        return A[:0], index_arr[:0]
    if k >= m:
        hbca__svays = np.sort(A)
        pwkwq__skpdr = index_arr[np.argsort(A)]
        blr__qlh = pd.Series(hbca__svays).notna().values
        hbca__svays = hbca__svays[blr__qlh]
        pwkwq__skpdr = pwkwq__skpdr[blr__qlh]
        if is_largest:
            hbca__svays = hbca__svays[::-1]
            pwkwq__skpdr = pwkwq__skpdr[::-1]
        return np.ascontiguousarray(hbca__svays), np.ascontiguousarray(
            pwkwq__skpdr)
    suay__szlz, gyynx__rjk, start = select_k_nonan(A, index_arr, m, k)
    gyynx__rjk = gyynx__rjk[suay__szlz.argsort()]
    suay__szlz.sort()
    if not is_largest:
        suay__szlz = np.ascontiguousarray(suay__szlz[::-1])
        gyynx__rjk = np.ascontiguousarray(gyynx__rjk[::-1])
    for i in range(start, m):
        if cmp_f(A[i], suay__szlz[0]):
            suay__szlz[0] = A[i]
            gyynx__rjk[0] = index_arr[i]
            min_heapify(suay__szlz, gyynx__rjk, k, 0, cmp_f)
    gyynx__rjk = gyynx__rjk[suay__szlz.argsort()]
    suay__szlz.sort()
    if is_largest:
        suay__szlz = suay__szlz[::-1]
        gyynx__rjk = gyynx__rjk[::-1]
    return np.ascontiguousarray(suay__szlz), np.ascontiguousarray(gyynx__rjk)


@numba.njit
def nlargest_parallel(A, I, k, is_largest, cmp_f):
    zswr__ngimq = bodo.libs.distributed_api.get_rank()
    A = bodo.utils.conversion.coerce_to_ndarray(A)
    rnn__efltv, ucu__jvqdj = nlargest(A, I, k, is_largest, cmp_f)
    axk__vhdn = bodo.libs.distributed_api.gatherv(rnn__efltv)
    eyiz__uabgo = bodo.libs.distributed_api.gatherv(ucu__jvqdj)
    if zswr__ngimq == MPI_ROOT:
        res, qwgg__zqq = nlargest(axk__vhdn, eyiz__uabgo, k, is_largest, cmp_f)
    else:
        res = np.empty(k, A.dtype)
        qwgg__zqq = np.empty(k, I.dtype)
    bodo.libs.distributed_api.bcast(res)
    bodo.libs.distributed_api.bcast(qwgg__zqq)
    return res, qwgg__zqq


@numba.njit(no_cpython_wrapper=True, cache=True)
def nancorr(mat, cov=0, minpv=1, parallel=False):
    twnz__jmop, tusze__glzdp = mat.shape
    ltfcb__ulie = np.empty((tusze__glzdp, tusze__glzdp), dtype=np.float64)
    for okcv__nddx in range(tusze__glzdp):
        for vqft__taf in range(okcv__nddx + 1):
            aagi__ugpvv = 0
            gbkeh__ftmn = wyv__eynx = nmylp__mwfx = max__vqspm = 0.0
            for i in range(twnz__jmop):
                if np.isfinite(mat[i, okcv__nddx]) and np.isfinite(mat[i,
                    vqft__taf]):
                    bwms__sdtg = mat[i, okcv__nddx]
                    cggz__mqau = mat[i, vqft__taf]
                    aagi__ugpvv += 1
                    nmylp__mwfx += bwms__sdtg
                    max__vqspm += cggz__mqau
            if parallel:
                aagi__ugpvv = bodo.libs.distributed_api.dist_reduce(aagi__ugpvv
                    , sum_op)
                nmylp__mwfx = bodo.libs.distributed_api.dist_reduce(nmylp__mwfx
                    , sum_op)
                max__vqspm = bodo.libs.distributed_api.dist_reduce(max__vqspm,
                    sum_op)
            if aagi__ugpvv < minpv:
                ltfcb__ulie[okcv__nddx, vqft__taf] = ltfcb__ulie[vqft__taf,
                    okcv__nddx] = np.nan
            else:
                rwbk__bdcjd = nmylp__mwfx / aagi__ugpvv
                frtyd__uizvf = max__vqspm / aagi__ugpvv
                nmylp__mwfx = 0.0
                for i in range(twnz__jmop):
                    if np.isfinite(mat[i, okcv__nddx]) and np.isfinite(mat[
                        i, vqft__taf]):
                        bwms__sdtg = mat[i, okcv__nddx] - rwbk__bdcjd
                        cggz__mqau = mat[i, vqft__taf] - frtyd__uizvf
                        nmylp__mwfx += bwms__sdtg * cggz__mqau
                        gbkeh__ftmn += bwms__sdtg * bwms__sdtg
                        wyv__eynx += cggz__mqau * cggz__mqau
                if parallel:
                    nmylp__mwfx = bodo.libs.distributed_api.dist_reduce(
                        nmylp__mwfx, sum_op)
                    gbkeh__ftmn = bodo.libs.distributed_api.dist_reduce(
                        gbkeh__ftmn, sum_op)
                    wyv__eynx = bodo.libs.distributed_api.dist_reduce(wyv__eynx
                        , sum_op)
                yybj__fumh = aagi__ugpvv - 1.0 if cov else sqrt(gbkeh__ftmn *
                    wyv__eynx)
                if yybj__fumh != 0.0:
                    ltfcb__ulie[okcv__nddx, vqft__taf] = ltfcb__ulie[
                        vqft__taf, okcv__nddx] = nmylp__mwfx / yybj__fumh
                else:
                    ltfcb__ulie[okcv__nddx, vqft__taf] = ltfcb__ulie[
                        vqft__taf, okcv__nddx] = np.nan
    return ltfcb__ulie


@numba.generated_jit(nopython=True)
def duplicated(data, parallel=False):
    n = len(data)
    if n == 0:
        return lambda data, parallel=False: np.empty(0, dtype=np.bool_)
    june__nmujj = n != 1
    xybk__dhl = 'def impl(data, parallel=False):\n'
    xybk__dhl += '  if parallel:\n'
    bxu__gzyo = ', '.join(f'array_to_info(data[{i}])' for i in range(n))
    xybk__dhl += f'    cpp_table = arr_info_list_to_table([{bxu__gzyo}])\n'
    xybk__dhl += (
        f'    out_cpp_table = bodo.libs.array.shuffle_table(cpp_table, {n}, parallel, 1)\n'
        )
    qdz__gdhoc = ', '.join(
        f'info_to_array(info_from_table(out_cpp_table, {i}), data[{i}])' for
        i in range(n))
    xybk__dhl += f'    data = ({qdz__gdhoc},)\n'
    xybk__dhl += (
        '    shuffle_info = bodo.libs.array.get_shuffle_info(out_cpp_table)\n')
    xybk__dhl += '    bodo.libs.array.delete_table(out_cpp_table)\n'
    xybk__dhl += '    bodo.libs.array.delete_table(cpp_table)\n'
    xybk__dhl += '  n = len(data[0])\n'
    xybk__dhl += '  out = np.empty(n, np.bool_)\n'
    xybk__dhl += '  uniqs = dict()\n'
    if june__nmujj:
        xybk__dhl += '  for i in range(n):\n'
        wwcar__aze = ', '.join(f'data[{i}][i]' for i in range(n))
        ghvo__bfyva = ',  '.join(
            f'bodo.libs.array_kernels.isna(data[{i}], i)' for i in range(n))
        xybk__dhl += f"""    val = bodo.libs.nullable_tuple_ext.build_nullable_tuple(({wwcar__aze},), ({ghvo__bfyva},))
"""
        xybk__dhl += '    if val in uniqs:\n'
        xybk__dhl += '      out[i] = True\n'
        xybk__dhl += '    else:\n'
        xybk__dhl += '      out[i] = False\n'
        xybk__dhl += '      uniqs[val] = 0\n'
    else:
        xybk__dhl += '  data = data[0]\n'
        xybk__dhl += '  hasna = False\n'
        xybk__dhl += '  for i in range(n):\n'
        xybk__dhl += '    if bodo.libs.array_kernels.isna(data, i):\n'
        xybk__dhl += '      out[i] = hasna\n'
        xybk__dhl += '      hasna = True\n'
        xybk__dhl += '    else:\n'
        xybk__dhl += '      val = data[i]\n'
        xybk__dhl += '      if val in uniqs:\n'
        xybk__dhl += '        out[i] = True\n'
        xybk__dhl += '      else:\n'
        xybk__dhl += '        out[i] = False\n'
        xybk__dhl += '        uniqs[val] = 0\n'
    xybk__dhl += '  if parallel:\n'
    xybk__dhl += (
        '    out = bodo.hiframes.pd_groupby_ext.reverse_shuffle(out, shuffle_info)\n'
        )
    xybk__dhl += '  return out\n'
    agnk__yixr = {}
    exec(xybk__dhl, {'bodo': bodo, 'np': np, 'array_to_info': array_to_info,
        'arr_info_list_to_table': arr_info_list_to_table, 'info_to_array':
        info_to_array, 'info_from_table': info_from_table}, agnk__yixr)
    impl = agnk__yixr['impl']
    return impl


def sample_table_operation(data, ind_arr, n, frac, replace, parallel=False):
    pass


@overload(sample_table_operation, no_unliteral=True)
def overload_sample_table_operation(data, ind_arr, n, frac, replace,
    parallel=False):
    bkue__pnt = len(data)
    xybk__dhl = 'def impl(data, ind_arr, n, frac, replace, parallel=False):\n'
    xybk__dhl += '  info_list_total = [{}, array_to_info(ind_arr)]\n'.format(
        ', '.join('array_to_info(data[{}])'.format(x) for x in range(
        bkue__pnt)))
    xybk__dhl += '  table_total = arr_info_list_to_table(info_list_total)\n'
    xybk__dhl += (
        '  out_table = sample_table(table_total, n, frac, replace, parallel)\n'
        .format(bkue__pnt))
    for ptyys__ipyxv in range(bkue__pnt):
        xybk__dhl += (
            '  out_arr_{} = info_to_array(info_from_table(out_table, {}), data[{}])\n'
            .format(ptyys__ipyxv, ptyys__ipyxv, ptyys__ipyxv))
    xybk__dhl += (
        '  out_arr_index = info_to_array(info_from_table(out_table, {}), ind_arr)\n'
        .format(bkue__pnt))
    xybk__dhl += '  delete_table(out_table)\n'
    xybk__dhl += '  delete_table(table_total)\n'
    xybk__dhl += '  return ({},), out_arr_index\n'.format(', '.join(
        'out_arr_{}'.format(i) for i in range(bkue__pnt)))
    agnk__yixr = {}
    exec(xybk__dhl, {'np': np, 'bodo': bodo, 'array_to_info': array_to_info,
        'sample_table': sample_table, 'arr_info_list_to_table':
        arr_info_list_to_table, 'info_from_table': info_from_table,
        'info_to_array': info_to_array, 'delete_table': delete_table,
        'delete_table_decref_arrays': delete_table_decref_arrays}, agnk__yixr)
    impl = agnk__yixr['impl']
    return impl


def drop_duplicates(data, ind_arr, ncols, parallel=False):
    pass


@overload(drop_duplicates, no_unliteral=True)
def overload_drop_duplicates(data, ind_arr, ncols, parallel=False):
    bkue__pnt = len(data)
    xybk__dhl = 'def impl(data, ind_arr, ncols, parallel=False):\n'
    xybk__dhl += '  info_list_total = [{}, array_to_info(ind_arr)]\n'.format(
        ', '.join('array_to_info(data[{}])'.format(x) for x in range(
        bkue__pnt)))
    xybk__dhl += '  table_total = arr_info_list_to_table(info_list_total)\n'
    xybk__dhl += '  keep_i = 0\n'
    xybk__dhl += """  out_table = drop_duplicates_table(table_total, parallel, ncols, keep_i, False, True)
"""
    for ptyys__ipyxv in range(bkue__pnt):
        xybk__dhl += (
            '  out_arr_{} = info_to_array(info_from_table(out_table, {}), data[{}])\n'
            .format(ptyys__ipyxv, ptyys__ipyxv, ptyys__ipyxv))
    xybk__dhl += (
        '  out_arr_index = info_to_array(info_from_table(out_table, {}), ind_arr)\n'
        .format(bkue__pnt))
    xybk__dhl += '  delete_table(out_table)\n'
    xybk__dhl += '  delete_table(table_total)\n'
    xybk__dhl += '  return ({},), out_arr_index\n'.format(', '.join(
        'out_arr_{}'.format(i) for i in range(bkue__pnt)))
    agnk__yixr = {}
    exec(xybk__dhl, {'np': np, 'bodo': bodo, 'array_to_info': array_to_info,
        'drop_duplicates_table': drop_duplicates_table,
        'arr_info_list_to_table': arr_info_list_to_table, 'info_from_table':
        info_from_table, 'info_to_array': info_to_array, 'delete_table':
        delete_table, 'delete_table_decref_arrays':
        delete_table_decref_arrays}, agnk__yixr)
    impl = agnk__yixr['impl']
    return impl


def drop_duplicates_array(data_arr, parallel=False):
    pass


@overload(drop_duplicates_array, no_unliteral=True)
def overload_drop_duplicates_array(data_arr, parallel=False):

    def impl(data_arr, parallel=False):
        vban__div = [array_to_info(data_arr)]
        omeqc__njp = arr_info_list_to_table(vban__div)
        gubsh__kqi = 0
        dlst__iizzs = drop_duplicates_table(omeqc__njp, parallel, 1,
            gubsh__kqi, False, True)
        out_arr = info_to_array(info_from_table(dlst__iizzs, 0), data_arr)
        delete_table(dlst__iizzs)
        delete_table(omeqc__njp)
        return out_arr
    return impl


def dropna(data, how, thresh, subset, parallel=False):
    pass


@overload(dropna, no_unliteral=True)
def overload_dropna(data, how, thresh, subset):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(data,
        'bodo.dropna()')
    bnfv__stycb = len(data.types)
    qpzd__bypvb = [('out' + str(i)) for i in range(bnfv__stycb)]
    znfm__jfp = get_overload_const_list(subset)
    how = get_overload_const_str(how)
    dgtv__yiv = ['isna(data[{}], i)'.format(i) for i in znfm__jfp]
    htkj__gyc = 'not ({})'.format(' or '.join(dgtv__yiv))
    if not is_overload_none(thresh):
        htkj__gyc = '(({}) <= ({}) - thresh)'.format(' + '.join(dgtv__yiv),
            bnfv__stycb - 1)
    elif how == 'all':
        htkj__gyc = 'not ({})'.format(' and '.join(dgtv__yiv))
    xybk__dhl = 'def _dropna_imp(data, how, thresh, subset):\n'
    xybk__dhl += '  old_len = len(data[0])\n'
    xybk__dhl += '  new_len = 0\n'
    xybk__dhl += '  for i in range(old_len):\n'
    xybk__dhl += '    if {}:\n'.format(htkj__gyc)
    xybk__dhl += '      new_len += 1\n'
    for i, out in enumerate(qpzd__bypvb):
        if isinstance(data[i], bodo.CategoricalArrayType):
            xybk__dhl += (
                '  {0} = bodo.utils.utils.alloc_type(new_len, data[{1}], (-1,))\n'
                .format(out, i))
        else:
            xybk__dhl += (
                '  {0} = bodo.utils.utils.alloc_type(new_len, t{1}, (-1,))\n'
                .format(out, i))
    xybk__dhl += '  curr_ind = 0\n'
    xybk__dhl += '  for i in range(old_len):\n'
    xybk__dhl += '    if {}:\n'.format(htkj__gyc)
    for i in range(bnfv__stycb):
        xybk__dhl += '      if isna(data[{}], i):\n'.format(i)
        xybk__dhl += '        setna({}, curr_ind)\n'.format(qpzd__bypvb[i])
        xybk__dhl += '      else:\n'
        xybk__dhl += '        {}[curr_ind] = data[{}][i]\n'.format(qpzd__bypvb
            [i], i)
    xybk__dhl += '      curr_ind += 1\n'
    xybk__dhl += '  return {}\n'.format(', '.join(qpzd__bypvb))
    agnk__yixr = {}
    pyl__ekec = {'t{}'.format(i): pps__codr for i, pps__codr in enumerate(
        data.types)}
    pyl__ekec.update({'isna': isna, 'setna': setna, 'init_nested_counts':
        bodo.utils.indexing.init_nested_counts, 'add_nested_counts': bodo.
        utils.indexing.add_nested_counts, 'bodo': bodo})
    exec(xybk__dhl, pyl__ekec, agnk__yixr)
    axl__cde = agnk__yixr['_dropna_imp']
    return axl__cde


def get(arr, ind):
    pass


@overload(get, no_unliteral=True)
def overload_get(arr, ind):
    if isinstance(arr, ArrayItemArrayType):
        kyjb__nmu = arr.dtype
        wwhw__eytp = kyjb__nmu.dtype

        def get_arr_item(arr, ind):
            n = len(arr)
            mkpct__mosfx = init_nested_counts(wwhw__eytp)
            for k in range(n):
                if bodo.libs.array_kernels.isna(arr, k):
                    continue
                val = arr[k]
                if not len(val) > ind >= -len(val
                    ) or bodo.libs.array_kernels.isna(val, ind):
                    continue
                mkpct__mosfx = add_nested_counts(mkpct__mosfx, val[ind])
            out_arr = bodo.utils.utils.alloc_type(n, kyjb__nmu, mkpct__mosfx)
            for bhn__kzcqf in range(n):
                if bodo.libs.array_kernels.isna(arr, bhn__kzcqf):
                    setna(out_arr, bhn__kzcqf)
                    continue
                val = arr[bhn__kzcqf]
                if not len(val) > ind >= -len(val
                    ) or bodo.libs.array_kernels.isna(val, ind):
                    setna(out_arr, bhn__kzcqf)
                    continue
                out_arr[bhn__kzcqf] = val[ind]
            return out_arr
        return get_arr_item


def _is_same_categorical_array_type(arr_types):
    from bodo.hiframes.pd_categorical_ext import _to_readonly
    if not isinstance(arr_types, types.BaseTuple) or len(arr_types) == 0:
        return False
    oeu__ekp = _to_readonly(arr_types.types[0])
    return all(isinstance(pps__codr, CategoricalArrayType) and _to_readonly
        (pps__codr) == oeu__ekp for pps__codr in arr_types.types)


def concat(arr_list):
    pass


@overload(concat, no_unliteral=True)
def concat_overload(arr_list):
    if isinstance(arr_list, bodo.NullableTupleType):
        return lambda arr_list: bodo.libs.array_kernels.concat(arr_list._data)
    if isinstance(arr_list, (types.UniTuple, types.List)) and isinstance(
        arr_list.dtype, ArrayItemArrayType):
        vrntc__hxj = arr_list.dtype.dtype

        def array_item_concat_impl(arr_list):
            ojxk__nhto = 0
            wnol__btthb = []
            for A in arr_list:
                ordk__jsd = len(A)
                bodo.libs.array_item_arr_ext.trim_excess_data(A)
                wnol__btthb.append(bodo.libs.array_item_arr_ext.get_data(A))
                ojxk__nhto += ordk__jsd
            saeok__ckk = np.empty(ojxk__nhto + 1, offset_type)
            viiuy__ltsg = bodo.libs.array_kernels.concat(wnol__btthb)
            qfvd__zrrqn = np.empty(ojxk__nhto + 7 >> 3, np.uint8)
            vnsjh__itmvn = 0
            yeaao__jdst = 0
            for A in arr_list:
                ceii__blodx = bodo.libs.array_item_arr_ext.get_offsets(A)
                obt__ula = bodo.libs.array_item_arr_ext.get_null_bitmap(A)
                ordk__jsd = len(A)
                hvoqa__ewwf = ceii__blodx[ordk__jsd]
                for i in range(ordk__jsd):
                    saeok__ckk[i + vnsjh__itmvn] = ceii__blodx[i] + yeaao__jdst
                    los__iuy = bodo.libs.int_arr_ext.get_bit_bitmap_arr(
                        obt__ula, i)
                    bodo.libs.int_arr_ext.set_bit_to_arr(qfvd__zrrqn, i +
                        vnsjh__itmvn, los__iuy)
                vnsjh__itmvn += ordk__jsd
                yeaao__jdst += hvoqa__ewwf
            saeok__ckk[vnsjh__itmvn] = yeaao__jdst
            out_arr = bodo.libs.array_item_arr_ext.init_array_item_array(
                ojxk__nhto, viiuy__ltsg, saeok__ckk, qfvd__zrrqn)
            return out_arr
        return array_item_concat_impl
    if isinstance(arr_list, (types.UniTuple, types.List)) and isinstance(
        arr_list.dtype, bodo.StructArrayType):
        jqwb__nxxgj = arr_list.dtype.names
        xybk__dhl = 'def struct_array_concat_impl(arr_list):\n'
        xybk__dhl += f'    n_all = 0\n'
        for i in range(len(jqwb__nxxgj)):
            xybk__dhl += f'    concat_list{i} = []\n'
        xybk__dhl += '    for A in arr_list:\n'
        xybk__dhl += (
            '        data_tuple = bodo.libs.struct_arr_ext.get_data(A)\n')
        for i in range(len(jqwb__nxxgj)):
            xybk__dhl += f'        concat_list{i}.append(data_tuple[{i}])\n'
        xybk__dhl += '        n_all += len(A)\n'
        xybk__dhl += '    n_bytes = (n_all + 7) >> 3\n'
        xybk__dhl += '    new_mask = np.empty(n_bytes, np.uint8)\n'
        xybk__dhl += '    curr_bit = 0\n'
        xybk__dhl += '    for A in arr_list:\n'
        xybk__dhl += (
            '        old_mask = bodo.libs.struct_arr_ext.get_null_bitmap(A)\n')
        xybk__dhl += '        for j in range(len(A)):\n'
        xybk__dhl += (
            '            bit = bodo.libs.int_arr_ext.get_bit_bitmap_arr(old_mask, j)\n'
            )
        xybk__dhl += (
            '            bodo.libs.int_arr_ext.set_bit_to_arr(new_mask, curr_bit, bit)\n'
            )
        xybk__dhl += '            curr_bit += 1\n'
        xybk__dhl += '    return bodo.libs.struct_arr_ext.init_struct_arr(\n'
        nidhr__wsne = ', '.join([
            f'bodo.libs.array_kernels.concat(concat_list{i})' for i in
            range(len(jqwb__nxxgj))])
        xybk__dhl += f'        ({nidhr__wsne},),\n'
        xybk__dhl += '        new_mask,\n'
        xybk__dhl += f'        {jqwb__nxxgj},\n'
        xybk__dhl += '    )\n'
        agnk__yixr = {}
        exec(xybk__dhl, {'bodo': bodo, 'np': np}, agnk__yixr)
        return agnk__yixr['struct_array_concat_impl']
    if isinstance(arr_list, (types.UniTuple, types.List)) and isinstance(
        arr_list.dtype, bodo.DatetimeArrayType):
        yrq__bsrd = arr_list.dtype.tz

        def tz_aware_concat_impl(arr_list):
            gykh__ohfq = 0
            for A in arr_list:
                gykh__ohfq += len(A)
            kcihd__xwka = (bodo.libs.pd_datetime_arr_ext.
                alloc_pd_datetime_array(gykh__ohfq, yrq__bsrd))
            ozau__rql = 0
            for A in arr_list:
                for i in range(len(A)):
                    kcihd__xwka[i + ozau__rql] = A[i]
                ozau__rql += len(A)
            return kcihd__xwka
        return tz_aware_concat_impl
    if isinstance(arr_list, (types.UniTuple, types.List)
        ) and arr_list.dtype == datetime_date_array_type:

        def datetime_date_array_concat_impl(arr_list):
            gykh__ohfq = 0
            for A in arr_list:
                gykh__ohfq += len(A)
            kcihd__xwka = (bodo.hiframes.datetime_date_ext.
                alloc_datetime_date_array(gykh__ohfq))
            ozau__rql = 0
            for A in arr_list:
                for i in range(len(A)):
                    kcihd__xwka._data[i + ozau__rql] = A._data[i]
                    los__iuy = bodo.libs.int_arr_ext.get_bit_bitmap_arr(A.
                        _null_bitmap, i)
                    bodo.libs.int_arr_ext.set_bit_to_arr(kcihd__xwka.
                        _null_bitmap, i + ozau__rql, los__iuy)
                ozau__rql += len(A)
            return kcihd__xwka
        return datetime_date_array_concat_impl
    if isinstance(arr_list, (types.UniTuple, types.List)
        ) and arr_list.dtype == datetime_timedelta_array_type:

        def datetime_timedelta_array_concat_impl(arr_list):
            gykh__ohfq = 0
            for A in arr_list:
                gykh__ohfq += len(A)
            kcihd__xwka = (bodo.hiframes.datetime_timedelta_ext.
                alloc_datetime_timedelta_array(gykh__ohfq))
            ozau__rql = 0
            for A in arr_list:
                for i in range(len(A)):
                    kcihd__xwka._days_data[i + ozau__rql] = A._days_data[i]
                    kcihd__xwka._seconds_data[i + ozau__rql] = A._seconds_data[
                        i]
                    kcihd__xwka._microseconds_data[i + ozau__rql
                        ] = A._microseconds_data[i]
                    los__iuy = bodo.libs.int_arr_ext.get_bit_bitmap_arr(A.
                        _null_bitmap, i)
                    bodo.libs.int_arr_ext.set_bit_to_arr(kcihd__xwka.
                        _null_bitmap, i + ozau__rql, los__iuy)
                ozau__rql += len(A)
            return kcihd__xwka
        return datetime_timedelta_array_concat_impl
    if isinstance(arr_list, (types.UniTuple, types.List)) and isinstance(
        arr_list.dtype, DecimalArrayType):
        ovkg__mbzfo = arr_list.dtype.precision
        sor__rahx = arr_list.dtype.scale

        def decimal_array_concat_impl(arr_list):
            gykh__ohfq = 0
            for A in arr_list:
                gykh__ohfq += len(A)
            kcihd__xwka = bodo.libs.decimal_arr_ext.alloc_decimal_array(
                gykh__ohfq, ovkg__mbzfo, sor__rahx)
            ozau__rql = 0
            for A in arr_list:
                for i in range(len(A)):
                    kcihd__xwka._data[i + ozau__rql] = A._data[i]
                    los__iuy = bodo.libs.int_arr_ext.get_bit_bitmap_arr(A.
                        _null_bitmap, i)
                    bodo.libs.int_arr_ext.set_bit_to_arr(kcihd__xwka.
                        _null_bitmap, i + ozau__rql, los__iuy)
                ozau__rql += len(A)
            return kcihd__xwka
        return decimal_array_concat_impl
    if isinstance(arr_list, (types.UniTuple, types.List)) and (is_str_arr_type
        (arr_list.dtype) or arr_list.dtype == bodo.binary_array_type
        ) or isinstance(arr_list, types.BaseTuple) and all(is_str_arr_type(
        pps__codr) for pps__codr in arr_list.types):
        if isinstance(arr_list, types.BaseTuple):
            vwm__dfien = arr_list.types[0]
            for i in range(len(arr_list)):
                if arr_list.types[i] != bodo.dict_str_arr_type:
                    vwm__dfien = arr_list.types[i]
                    break
        else:
            vwm__dfien = arr_list.dtype
        if vwm__dfien == bodo.dict_str_arr_type:

            def impl_dict_arr(arr_list):
                ueqs__xdm = 0
                iqu__ufzth = 0
                wfdy__ays = 0
                for A in arr_list:
                    data_arr = A._data
                    pbrgb__fcty = A._indices
                    wfdy__ays += len(pbrgb__fcty)
                    ueqs__xdm += len(data_arr)
                    iqu__ufzth += bodo.libs.str_arr_ext.num_total_chars(
                        data_arr)
                ddb__bnt = pre_alloc_string_array(ueqs__xdm, iqu__ufzth)
                fdgww__bmj = bodo.libs.int_arr_ext.alloc_int_array(wfdy__ays,
                    np.int32)
                bodo.libs.str_arr_ext.set_null_bits_to_value(ddb__bnt, -1)
                kycyk__kyuz = 0
                sofsr__jjc = 0
                nww__bik = 0
                for A in arr_list:
                    data_arr = A._data
                    pbrgb__fcty = A._indices
                    wfdy__ays = len(pbrgb__fcty)
                    bodo.libs.str_arr_ext.set_string_array_range(ddb__bnt,
                        data_arr, kycyk__kyuz, sofsr__jjc)
                    for i in range(wfdy__ays):
                        if bodo.libs.array_kernels.isna(pbrgb__fcty, i
                            ) or bodo.libs.array_kernels.isna(data_arr,
                            pbrgb__fcty[i]):
                            bodo.libs.array_kernels.setna(fdgww__bmj, 
                                nww__bik + i)
                        else:
                            fdgww__bmj[nww__bik + i
                                ] = kycyk__kyuz + pbrgb__fcty[i]
                    kycyk__kyuz += len(data_arr)
                    sofsr__jjc += bodo.libs.str_arr_ext.num_total_chars(
                        data_arr)
                    nww__bik += wfdy__ays
                out_arr = init_dict_arr(ddb__bnt, fdgww__bmj, False, False)
                fov__qvf = drop_duplicates_local_dictionary(out_arr, False)
                return fov__qvf
            return impl_dict_arr

        def impl_str(arr_list):
            arr_list = decode_if_dict_array(arr_list)
            ueqs__xdm = 0
            iqu__ufzth = 0
            for A in arr_list:
                arr = A
                ueqs__xdm += len(arr)
                iqu__ufzth += bodo.libs.str_arr_ext.num_total_chars(arr)
            out_arr = bodo.utils.utils.alloc_type(ueqs__xdm, vwm__dfien, (
                iqu__ufzth,))
            bodo.libs.str_arr_ext.set_null_bits_to_value(out_arr, -1)
            kycyk__kyuz = 0
            sofsr__jjc = 0
            for A in arr_list:
                arr = A
                bodo.libs.str_arr_ext.set_string_array_range(out_arr, arr,
                    kycyk__kyuz, sofsr__jjc)
                kycyk__kyuz += len(arr)
                sofsr__jjc += bodo.libs.str_arr_ext.num_total_chars(arr)
            return out_arr
        return impl_str
    if isinstance(arr_list, (types.UniTuple, types.List)) and isinstance(
        arr_list.dtype, IntegerArrayType) or isinstance(arr_list, types.
        BaseTuple) and all(isinstance(pps__codr.dtype, types.Integer) for
        pps__codr in arr_list.types) and any(isinstance(pps__codr,
        IntegerArrayType) for pps__codr in arr_list.types):

        def impl_int_arr_list(arr_list):
            lre__qnis = convert_to_nullable_tup(arr_list)
            yqyz__pnmt = []
            ljxmr__xnmrs = 0
            for A in lre__qnis:
                yqyz__pnmt.append(A._data)
                ljxmr__xnmrs += len(A)
            viiuy__ltsg = bodo.libs.array_kernels.concat(yqyz__pnmt)
            newej__iuoqf = ljxmr__xnmrs + 7 >> 3
            gqtgc__hukwc = np.empty(newej__iuoqf, np.uint8)
            vvgfh__jlzfm = 0
            for A in lre__qnis:
                krax__qjla = A._null_bitmap
                for bhn__kzcqf in range(len(A)):
                    los__iuy = bodo.libs.int_arr_ext.get_bit_bitmap_arr(
                        krax__qjla, bhn__kzcqf)
                    bodo.libs.int_arr_ext.set_bit_to_arr(gqtgc__hukwc,
                        vvgfh__jlzfm, los__iuy)
                    vvgfh__jlzfm += 1
            return bodo.libs.int_arr_ext.init_integer_array(viiuy__ltsg,
                gqtgc__hukwc)
        return impl_int_arr_list
    if isinstance(arr_list, (types.UniTuple, types.List)
        ) and arr_list.dtype == boolean_array or isinstance(arr_list, types
        .BaseTuple) and all(pps__codr.dtype == types.bool_ for pps__codr in
        arr_list.types) and any(pps__codr == boolean_array for pps__codr in
        arr_list.types):

        def impl_bool_arr_list(arr_list):
            lre__qnis = convert_to_nullable_tup(arr_list)
            yqyz__pnmt = []
            ljxmr__xnmrs = 0
            for A in lre__qnis:
                yqyz__pnmt.append(A._data)
                ljxmr__xnmrs += len(A)
            viiuy__ltsg = bodo.libs.array_kernels.concat(yqyz__pnmt)
            newej__iuoqf = ljxmr__xnmrs + 7 >> 3
            gqtgc__hukwc = np.empty(newej__iuoqf, np.uint8)
            vvgfh__jlzfm = 0
            for A in lre__qnis:
                krax__qjla = A._null_bitmap
                for bhn__kzcqf in range(len(A)):
                    los__iuy = bodo.libs.int_arr_ext.get_bit_bitmap_arr(
                        krax__qjla, bhn__kzcqf)
                    bodo.libs.int_arr_ext.set_bit_to_arr(gqtgc__hukwc,
                        vvgfh__jlzfm, los__iuy)
                    vvgfh__jlzfm += 1
            return bodo.libs.bool_arr_ext.init_bool_array(viiuy__ltsg,
                gqtgc__hukwc)
        return impl_bool_arr_list
    if isinstance(arr_list, (types.UniTuple, types.List)) and isinstance(
        arr_list.dtype, FloatingArrayType) or isinstance(arr_list, types.
        BaseTuple) and all(isinstance(pps__codr.dtype, types.Float) for
        pps__codr in arr_list.types) and any(isinstance(pps__codr,
        FloatingArrayType) for pps__codr in arr_list.types):

        def impl_float_arr_list(arr_list):
            lre__qnis = convert_to_nullable_tup(arr_list)
            yqyz__pnmt = []
            ljxmr__xnmrs = 0
            for A in lre__qnis:
                yqyz__pnmt.append(A._data)
                ljxmr__xnmrs += len(A)
            viiuy__ltsg = bodo.libs.array_kernels.concat(yqyz__pnmt)
            newej__iuoqf = ljxmr__xnmrs + 7 >> 3
            gqtgc__hukwc = np.empty(newej__iuoqf, np.uint8)
            vvgfh__jlzfm = 0
            for A in lre__qnis:
                krax__qjla = A._null_bitmap
                for bhn__kzcqf in range(len(A)):
                    los__iuy = bodo.libs.int_arr_ext.get_bit_bitmap_arr(
                        krax__qjla, bhn__kzcqf)
                    bodo.libs.int_arr_ext.set_bit_to_arr(gqtgc__hukwc,
                        vvgfh__jlzfm, los__iuy)
                    vvgfh__jlzfm += 1
            return bodo.libs.float_arr_ext.init_float_array(viiuy__ltsg,
                gqtgc__hukwc)
        return impl_float_arr_list
    if isinstance(arr_list, (types.UniTuple, types.List)) and isinstance(
        arr_list.dtype, CategoricalArrayType):

        def cat_array_concat_impl(arr_list):
            obrg__iaaar = []
            for A in arr_list:
                obrg__iaaar.append(A.codes)
            return init_categorical_array(bodo.libs.array_kernels.concat(
                obrg__iaaar), arr_list[0].dtype)
        return cat_array_concat_impl
    if _is_same_categorical_array_type(arr_list):
        zwu__jeapf = ', '.join(f'arr_list[{i}].codes' for i in range(len(
            arr_list)))
        xybk__dhl = 'def impl(arr_list):\n'
        xybk__dhl += f"""    return init_categorical_array(bodo.libs.array_kernels.concat(({zwu__jeapf}, )), arr_list[0].dtype)
"""
        oxj__lpdn = {}
        exec(xybk__dhl, {'bodo': bodo, 'init_categorical_array':
            init_categorical_array}, oxj__lpdn)
        return oxj__lpdn['impl']
    if isinstance(arr_list, types.List) and isinstance(arr_list.dtype,
        types.Array) and arr_list.dtype.ndim == 1:
        dtype = arr_list.dtype.dtype

        def impl_np_arr_list(arr_list):
            ljxmr__xnmrs = 0
            for A in arr_list:
                ljxmr__xnmrs += len(A)
            out_arr = np.empty(ljxmr__xnmrs, dtype)
            dkw__lopk = 0
            for A in arr_list:
                n = len(A)
                out_arr[dkw__lopk:dkw__lopk + n] = A
                dkw__lopk += n
            return out_arr
        return impl_np_arr_list
    if isinstance(arr_list, types.BaseTuple) and any(isinstance(pps__codr,
        (types.Array, IntegerArrayType)) and isinstance(pps__codr.dtype,
        types.Integer) for pps__codr in arr_list.types) and any(isinstance(
        pps__codr, types.Array) and isinstance(pps__codr.dtype, types.Float
        ) for pps__codr in arr_list.types):
        return lambda arr_list: np.concatenate(astype_float_tup(arr_list))
    if isinstance(arr_list, (types.UniTuple, types.List)) and isinstance(
        arr_list.dtype, bodo.MapArrayType):

        def impl_map_arr_list(arr_list):
            xwrm__tikk = []
            for A in arr_list:
                xwrm__tikk.append(A._data)
            mlyhf__nfhoq = bodo.libs.array_kernels.concat(xwrm__tikk)
            ltfcb__ulie = bodo.libs.map_arr_ext.init_map_arr(mlyhf__nfhoq)
            return ltfcb__ulie
        return impl_map_arr_list
    if isinstance(arr_list, types.Tuple):
        ndjb__nva = all([(isinstance(zkla__cgea, bodo.DatetimeArrayType) or
            isinstance(zkla__cgea, types.Array) and zkla__cgea.dtype ==
            bodo.datetime64ns) for zkla__cgea in arr_list.types])
        if ndjb__nva:
            raise BodoError(
                f'Cannot concatenate the rows of Timestamp data with different timezones. Found types: {arr_list}. Please use pd.Series.tz_convert(None) to remove Timezone information.'
                )
    for zkla__cgea in arr_list:
        if not isinstance(zkla__cgea, types.Array):
            raise_bodo_error(f'concat of array types {arr_list} not supported')
    return lambda arr_list: np.concatenate(arr_list)


def astype_float_tup(arr_tup):
    return tuple(pps__codr.astype(np.float64) for pps__codr in arr_tup)


@overload(astype_float_tup, no_unliteral=True)
def overload_astype_float_tup(arr_tup):
    assert isinstance(arr_tup, types.BaseTuple)
    bkue__pnt = len(arr_tup.types)
    xybk__dhl = 'def f(arr_tup):\n'
    xybk__dhl += '  return ({}{})\n'.format(','.join(
        'arr_tup[{}].astype(np.float64)'.format(i) for i in range(bkue__pnt
        )), ',' if bkue__pnt == 1 else '')
    agnk__yixr = {}
    exec(xybk__dhl, {'np': np}, agnk__yixr)
    fsu__svt = agnk__yixr['f']
    return fsu__svt


def convert_to_nullable_tup(arr_tup):
    pass


@overload(convert_to_nullable_tup, no_unliteral=True)
def overload_convert_to_nullable_tup(arr_tup):
    if isinstance(arr_tup, (types.UniTuple, types.List)) and isinstance(arr_tup
        .dtype, (IntegerArrayType, FloatingArrayType, BooleanArrayType)):
        return lambda arr_tup: arr_tup
    assert isinstance(arr_tup, types.BaseTuple
        ), 'convert_to_nullable_tup: tuple expected'
    bkue__pnt = len(arr_tup.types)
    lxx__dvor = find_common_np_dtype(arr_tup.types)
    wwhw__eytp = None
    heon__hqxg = ''
    if isinstance(lxx__dvor, types.Integer):
        wwhw__eytp = bodo.libs.int_arr_ext.IntDtype(lxx__dvor)
        heon__hqxg = '.astype(out_dtype, False)'
    if isinstance(lxx__dvor, types.Float
        ) and bodo.libs.float_arr_ext._use_nullable_float:
        wwhw__eytp = bodo.libs.float_arr_ext.FloatDtype(lxx__dvor)
        heon__hqxg = '.astype(out_dtype, False)'
    xybk__dhl = 'def f(arr_tup):\n'
    xybk__dhl += '  return ({}{})\n'.format(','.join(
        f'bodo.utils.conversion.coerce_to_array(arr_tup[{i}], use_nullable_array=True){heon__hqxg}'
         for i in range(bkue__pnt)), ',' if bkue__pnt == 1 else '')
    agnk__yixr = {}
    exec(xybk__dhl, {'bodo': bodo, 'out_dtype': wwhw__eytp}, agnk__yixr)
    gzcv__wkm = agnk__yixr['f']
    return gzcv__wkm


def nunique(A, dropna):
    pass


def nunique_parallel(A, dropna):
    pass


@overload(nunique, no_unliteral=True)
def nunique_overload(A, dropna):

    def nunique_seq(A, dropna):
        s, pdx__mioqn = build_set_seen_na(A)
        return len(s) + int(not dropna and pdx__mioqn)
    return nunique_seq


@overload(nunique_parallel, no_unliteral=True)
def nunique_overload_parallel(A, dropna):
    sum_op = bodo.libs.distributed_api.Reduce_Type.Sum.value

    def nunique_par(A, dropna):
        anclr__bkt = bodo.libs.array_kernels.unique(A, dropna, parallel=True)
        afsq__audot = len(anclr__bkt)
        return bodo.libs.distributed_api.dist_reduce(afsq__audot, np.int32(
            sum_op))
    return nunique_par


def unique(A, dropna=False, parallel=False):
    pass


def accum_func(A, func_name, parallel=False):
    pass


@overload(accum_func, no_unliteral=True)
def accum_func_overload(A, func_name, parallel=False):
    assert is_overload_constant_str(func_name
        ), 'accum_func: func_name should be const'
    ivn__xzoi = get_overload_const_str(func_name)
    assert ivn__xzoi in ('cumsum', 'cumprod', 'cummin', 'cummax'
        ), 'accum_func: invalid func_name'
    if ivn__xzoi == 'cumsum':
        zljyi__lkcuy = A.dtype(0)
        subtv__cudaj = np.int32(Reduce_Type.Sum.value)
        pwls__brw = np.add
    if ivn__xzoi == 'cumprod':
        zljyi__lkcuy = A.dtype(1)
        subtv__cudaj = np.int32(Reduce_Type.Prod.value)
        pwls__brw = np.multiply
    if ivn__xzoi == 'cummin':
        if isinstance(A.dtype, types.Float):
            zljyi__lkcuy = np.finfo(A.dtype(1).dtype).max
        else:
            zljyi__lkcuy = np.iinfo(A.dtype(1).dtype).max
        subtv__cudaj = np.int32(Reduce_Type.Min.value)
        pwls__brw = min
    if ivn__xzoi == 'cummax':
        if isinstance(A.dtype, types.Float):
            zljyi__lkcuy = np.finfo(A.dtype(1).dtype).min
        else:
            zljyi__lkcuy = np.iinfo(A.dtype(1).dtype).min
        subtv__cudaj = np.int32(Reduce_Type.Max.value)
        pwls__brw = max
    evu__hvbt = A

    def impl(A, func_name, parallel=False):
        n = len(A)
        mjs__qlni = zljyi__lkcuy
        if parallel:
            for i in range(n):
                if not bodo.libs.array_kernels.isna(A, i):
                    mjs__qlni = pwls__brw(mjs__qlni, A[i])
            mjs__qlni = bodo.libs.distributed_api.dist_exscan(mjs__qlni,
                subtv__cudaj)
            if bodo.get_rank() == 0:
                mjs__qlni = zljyi__lkcuy
        out_arr = bodo.utils.utils.alloc_type(n, evu__hvbt, (-1,))
        for i in range(n):
            if bodo.libs.array_kernels.isna(A, i):
                bodo.libs.array_kernels.setna(out_arr, i)
                continue
            mjs__qlni = pwls__brw(mjs__qlni, A[i])
            out_arr[i] = mjs__qlni
        return out_arr
    return impl


@overload(unique, no_unliteral=True)
def unique_overload(A, dropna=False, parallel=False):

    def unique_impl(A, dropna=False, parallel=False):
        ujo__bzqqi = arr_info_list_to_table([array_to_info(A)])
        jdfi__iszs = 1
        gubsh__kqi = 0
        dlst__iizzs = drop_duplicates_table(ujo__bzqqi, parallel,
            jdfi__iszs, gubsh__kqi, dropna, True)
        out_arr = info_to_array(info_from_table(dlst__iizzs, 0), A)
        delete_table(ujo__bzqqi)
        delete_table(dlst__iizzs)
        return out_arr
    return unique_impl


def explode(arr, index_arr):
    return pd.Series(arr, index_arr).explode()


@overload(explode, no_unliteral=True)
def overload_explode(arr, index_arr):
    assert isinstance(arr, ArrayItemArrayType
        ) or arr == string_array_split_view_type
    vrntc__hxj = bodo.utils.typing.to_nullable_type(arr.dtype)
    lot__grawp = index_arr
    ssgip__zauh = lot__grawp.dtype

    def impl(arr, index_arr):
        n = len(arr)
        mkpct__mosfx = init_nested_counts(vrntc__hxj)
        bwly__lcl = init_nested_counts(ssgip__zauh)
        for i in range(n):
            xjtq__hff = index_arr[i]
            if isna(arr, i):
                mkpct__mosfx = (mkpct__mosfx[0] + 1,) + mkpct__mosfx[1:]
                bwly__lcl = add_nested_counts(bwly__lcl, xjtq__hff)
                continue
            opc__snf = arr[i]
            if len(opc__snf) == 0:
                mkpct__mosfx = (mkpct__mosfx[0] + 1,) + mkpct__mosfx[1:]
                bwly__lcl = add_nested_counts(bwly__lcl, xjtq__hff)
                continue
            mkpct__mosfx = add_nested_counts(mkpct__mosfx, opc__snf)
            for mhnc__crrgi in range(len(opc__snf)):
                bwly__lcl = add_nested_counts(bwly__lcl, xjtq__hff)
        out_arr = bodo.utils.utils.alloc_type(mkpct__mosfx[0], vrntc__hxj,
            mkpct__mosfx[1:])
        xdted__wjia = bodo.utils.utils.alloc_type(mkpct__mosfx[0],
            lot__grawp, bwly__lcl)
        yeaao__jdst = 0
        for i in range(n):
            if isna(arr, i):
                setna(out_arr, yeaao__jdst)
                xdted__wjia[yeaao__jdst] = index_arr[i]
                yeaao__jdst += 1
                continue
            opc__snf = arr[i]
            hvoqa__ewwf = len(opc__snf)
            if hvoqa__ewwf == 0:
                setna(out_arr, yeaao__jdst)
                xdted__wjia[yeaao__jdst] = index_arr[i]
                yeaao__jdst += 1
                continue
            out_arr[yeaao__jdst:yeaao__jdst + hvoqa__ewwf] = opc__snf
            xdted__wjia[yeaao__jdst:yeaao__jdst + hvoqa__ewwf] = index_arr[i]
            yeaao__jdst += hvoqa__ewwf
        return out_arr, xdted__wjia
    return impl


def explode_no_index(arr):
    pass


@overload(explode_no_index, no_unliteral=True)
def overload_explode_no_index(arr, counts):
    assert isinstance(arr, ArrayItemArrayType
        ) or arr == string_array_split_view_type
    vrntc__hxj = bodo.utils.typing.to_nullable_type(arr.dtype)

    def impl(arr, counts):
        n = len(arr)
        mkpct__mosfx = init_nested_counts(vrntc__hxj)
        for i in range(n):
            if isna(arr, i):
                mkpct__mosfx = (mkpct__mosfx[0] + 1,) + mkpct__mosfx[1:]
                qygs__klys = 1
            else:
                opc__snf = arr[i]
                zgyq__wemr = len(opc__snf)
                if zgyq__wemr == 0:
                    mkpct__mosfx = (mkpct__mosfx[0] + 1,) + mkpct__mosfx[1:]
                    qygs__klys = 1
                    continue
                else:
                    mkpct__mosfx = add_nested_counts(mkpct__mosfx, opc__snf)
                    qygs__klys = zgyq__wemr
            if counts[i] != qygs__klys:
                raise ValueError(
                    'DataFrame.explode(): columns must have matching element counts'
                    )
        out_arr = bodo.utils.utils.alloc_type(mkpct__mosfx[0], vrntc__hxj,
            mkpct__mosfx[1:])
        yeaao__jdst = 0
        for i in range(n):
            if isna(arr, i):
                setna(out_arr, yeaao__jdst)
                yeaao__jdst += 1
                continue
            opc__snf = arr[i]
            hvoqa__ewwf = len(opc__snf)
            if hvoqa__ewwf == 0:
                setna(out_arr, yeaao__jdst)
                yeaao__jdst += 1
                continue
            out_arr[yeaao__jdst:yeaao__jdst + hvoqa__ewwf] = opc__snf
            yeaao__jdst += hvoqa__ewwf
        return out_arr
    return impl


def get_arr_lens(arr, na_empty_as_one=True):
    pass


@overload(get_arr_lens, inline='always', no_unliteral=True)
def overload_get_arr_lens(arr, na_empty_as_one=True):
    na_empty_as_one = get_overload_const_bool(na_empty_as_one)
    assert isinstance(arr, ArrayItemArrayType
        ) or arr == string_array_split_view_type or is_str_arr_type(arr
        ) and not na_empty_as_one or is_bin_arr_type(arr
        ) and not na_empty_as_one, f'get_arr_lens: invalid input array type {arr}'
    if na_empty_as_one:
        xfw__hms = 'np.empty(n, np.int64)'
        iiq__vsib = 'out_arr[i] = 1'
        zvk__xmrha = 'max(len(arr[i]), 1)'
    else:
        xfw__hms = 'bodo.libs.int_arr_ext.alloc_int_array(n, np.int64)'
        iiq__vsib = 'bodo.libs.array_kernels.setna(out_arr, i)'
        zvk__xmrha = 'len(arr[i])'
    xybk__dhl = f"""def impl(arr, na_empty_as_one=True):
    numba.parfors.parfor.init_prange()
    n = len(arr)
    out_arr = {xfw__hms}
    for i in numba.parfors.parfor.internal_prange(n):
        if bodo.libs.array_kernels.isna(arr, i):
            {iiq__vsib}
        else:
            out_arr[i] = {zvk__xmrha}
    return out_arr
    """
    agnk__yixr = {}
    exec(xybk__dhl, {'bodo': bodo, 'numba': numba, 'np': np}, agnk__yixr)
    impl = agnk__yixr['impl']
    return impl


def explode_str_split(arr, pat, n, index_arr):
    pass


@overload(explode_str_split, no_unliteral=True)
def overload_explode_str_split(arr, pat, n, index_arr):
    assert is_str_arr_type(arr
        ), f'explode_str_split: string array expected, not {arr}'
    lot__grawp = index_arr
    ssgip__zauh = lot__grawp.dtype

    def impl(arr, pat, n, index_arr):
        zrnc__xmcox = pat is not None and len(pat) > 1
        if zrnc__xmcox:
            qqiw__wbcwk = re.compile(pat)
            if n == -1:
                n = 0
        elif n == 0:
            n = -1
        sqs__iwmi = len(arr)
        ueqs__xdm = 0
        iqu__ufzth = 0
        bwly__lcl = init_nested_counts(ssgip__zauh)
        for i in range(sqs__iwmi):
            xjtq__hff = index_arr[i]
            if bodo.libs.array_kernels.isna(arr, i):
                ueqs__xdm += 1
                bwly__lcl = add_nested_counts(bwly__lcl, xjtq__hff)
                continue
            if zrnc__xmcox:
                rleno__uqv = qqiw__wbcwk.split(arr[i], maxsplit=n)
            else:
                rleno__uqv = arr[i].split(pat, n)
            ueqs__xdm += len(rleno__uqv)
            for s in rleno__uqv:
                bwly__lcl = add_nested_counts(bwly__lcl, xjtq__hff)
                iqu__ufzth += bodo.libs.str_arr_ext.get_utf8_size(s)
        out_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(ueqs__xdm,
            iqu__ufzth)
        xdted__wjia = bodo.utils.utils.alloc_type(ueqs__xdm, lot__grawp,
            bwly__lcl)
        rntb__ptyh = 0
        for bhn__kzcqf in range(sqs__iwmi):
            if isna(arr, bhn__kzcqf):
                out_arr[rntb__ptyh] = ''
                bodo.libs.array_kernels.setna(out_arr, rntb__ptyh)
                xdted__wjia[rntb__ptyh] = index_arr[bhn__kzcqf]
                rntb__ptyh += 1
                continue
            if zrnc__xmcox:
                rleno__uqv = qqiw__wbcwk.split(arr[bhn__kzcqf], maxsplit=n)
            else:
                rleno__uqv = arr[bhn__kzcqf].split(pat, n)
            fwvic__kjfze = len(rleno__uqv)
            out_arr[rntb__ptyh:rntb__ptyh + fwvic__kjfze] = rleno__uqv
            xdted__wjia[rntb__ptyh:rntb__ptyh + fwvic__kjfze] = index_arr[
                bhn__kzcqf]
            rntb__ptyh += fwvic__kjfze
        return out_arr, xdted__wjia
    return impl


def gen_na_array(n, arr):
    pass


@overload(gen_na_array, no_unliteral=True)
def overload_gen_na_array(n, arr, use_dict_arr=False):
    if isinstance(arr, types.TypeRef):
        arr = arr.instance_type
    dtype = arr.dtype
    if not isinstance(arr, (FloatingArrayType, IntegerArrayType)
        ) and isinstance(dtype, (types.Integer, types.Float)):
        dtype = dtype if isinstance(dtype, types.Float) else types.float64

        def impl_float(n, arr, use_dict_arr=False):
            numba.parfors.parfor.init_prange()
            out_arr = np.empty(n, dtype)
            for i in numba.parfors.parfor.internal_prange(n):
                out_arr[i] = np.nan
            return out_arr
        return impl_float
    if arr == bodo.dict_str_arr_type and is_overload_true(use_dict_arr):

        def impl_dict(n, arr, use_dict_arr=False):
            rqy__nzpu = bodo.libs.str_arr_ext.pre_alloc_string_array(0, 0)
            qfu__upzkd = bodo.libs.int_arr_ext.alloc_int_array(n, np.int32)
            numba.parfors.parfor.init_prange()
            for i in numba.parfors.parfor.internal_prange(n):
                setna(qfu__upzkd, i)
            return bodo.libs.dict_arr_ext.init_dict_arr(rqy__nzpu,
                qfu__upzkd, True, True)
        return impl_dict
    lzwoi__qzco = to_str_arr_if_dict_array(arr)

    def impl(n, arr, use_dict_arr=False):
        numba.parfors.parfor.init_prange()
        out_arr = bodo.utils.utils.alloc_type(n, lzwoi__qzco, (0,))
        for i in numba.parfors.parfor.internal_prange(n):
            setna(out_arr, i)
        return out_arr
    return impl


def gen_na_array_equiv(self, scope, equiv_set, loc, args, kws):
    assert not kws
    return ArrayAnalysis.AnalyzeResult(shape=args[0], pre=[])


ArrayAnalysis._analyze_op_call_bodo_libs_array_kernels_gen_na_array = (
    gen_na_array_equiv)


def resize_and_copy(A, new_len):
    pass


@overload(resize_and_copy, no_unliteral=True)
def overload_resize_and_copy(A, old_size, new_len):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(A,
        'bodo.resize_and_copy()')
    jpubc__dstm = A
    if A == types.Array(types.uint8, 1, 'C'):

        def impl_char(A, old_size, new_len):
            out_arr = bodo.utils.utils.alloc_type(new_len, jpubc__dstm)
            bodo.libs.str_arr_ext.str_copy_ptr(out_arr.ctypes, 0, A.ctypes,
                old_size)
            return out_arr
        return impl_char

    def impl(A, old_size, new_len):
        out_arr = bodo.utils.utils.alloc_type(new_len, jpubc__dstm, (-1,))
        out_arr[:old_size] = A[:old_size]
        return out_arr
    return impl


@register_jitable
def calc_nitems(start, stop, step):
    thw__ooagw = math.ceil((stop - start) / step)
    return int(max(thw__ooagw, 0))


def calc_nitems_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 3 and not kws
    if guard(find_const, self.func_ir, args[0]) == 0 and guard(find_const,
        self.func_ir, args[2]) == 1:
        return ArrayAnalysis.AnalyzeResult(shape=args[1], pre=[])


ArrayAnalysis._analyze_op_call_bodo_libs_array_kernels_calc_nitems = (
    calc_nitems_equiv)


def arange_parallel_impl(return_type, *args):
    dtype = as_dtype(return_type.dtype)

    def arange_1(stop):
        return np.arange(0, stop, 1, dtype)

    def arange_2(start, stop):
        return np.arange(start, stop, 1, dtype)

    def arange_3(start, stop, step):
        return np.arange(start, stop, step, dtype)
    if any(isinstance(kmtw__pbfbt, types.Complex) for kmtw__pbfbt in args):

        def arange_4(start, stop, step, dtype):
            numba.parfors.parfor.init_prange()
            pbl__oqsm = (stop - start) / step
            thw__ooagw = math.ceil(pbl__oqsm.real)
            bdhl__rcnqp = math.ceil(pbl__oqsm.imag)
            yxh__qrmzz = int(max(min(bdhl__rcnqp, thw__ooagw), 0))
            arr = np.empty(yxh__qrmzz, dtype)
            for i in numba.parfors.parfor.internal_prange(yxh__qrmzz):
                arr[i] = start + i * step
            return arr
    else:

        def arange_4(start, stop, step, dtype):
            numba.parfors.parfor.init_prange()
            yxh__qrmzz = bodo.libs.array_kernels.calc_nitems(start, stop, step)
            arr = np.empty(yxh__qrmzz, dtype)
            for i in numba.parfors.parfor.internal_prange(yxh__qrmzz):
                arr[i] = start + i * step
            return arr
    if len(args) == 1:
        return arange_1
    elif len(args) == 2:
        return arange_2
    elif len(args) == 3:
        return arange_3
    elif len(args) == 4:
        return arange_4
    else:
        raise BodoError('parallel arange with types {}'.format(args))


if bodo.numba_compat._check_numba_change:
    lines = inspect.getsource(numba.parfors.parfor.arange_parallel_impl)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'c72b0390b4f3e52dcc5426bd42c6b55ff96bae5a425381900985d36e7527a4bd':
        warnings.warn('numba.parfors.parfor.arange_parallel_impl has changed')
numba.parfors.parfor.swap_functions_map['arange', 'numpy'
    ] = arange_parallel_impl


def sort(arr, ascending, inplace):
    pass


@overload(sort, no_unliteral=True)
def overload_sort(arr, ascending, inplace):

    def impl(arr, ascending, inplace):
        n = len(arr)
        data = np.arange(n),
        wzm__ruiow = arr,
        if not inplace:
            wzm__ruiow = arr.copy(),
        cwjfn__onktm = bodo.libs.str_arr_ext.to_list_if_immutable_arr(
            wzm__ruiow)
        ybfp__cluh = bodo.libs.str_arr_ext.to_list_if_immutable_arr(data, True)
        bodo.libs.timsort.sort(cwjfn__onktm, 0, n, ybfp__cluh)
        if not ascending:
            bodo.libs.timsort.reverseRange(cwjfn__onktm, 0, n, ybfp__cluh)
        bodo.libs.str_arr_ext.cp_str_list_to_array(wzm__ruiow, cwjfn__onktm)
        return wzm__ruiow[0]
    return impl


def overload_array_max(A):
    if isinstance(A, (IntegerArrayType, FloatingArrayType)
        ) or A == boolean_array:

        def impl(A):
            return pd.Series(A).max()
        return impl


overload(np.max, inline='always', no_unliteral=True)(overload_array_max)
overload(max, inline='always', no_unliteral=True)(overload_array_max)


def overload_array_min(A):
    if isinstance(A, (IntegerArrayType, FloatingArrayType)
        ) or A == boolean_array:

        def impl(A):
            return pd.Series(A).min()
        return impl


overload(np.min, inline='always', no_unliteral=True)(overload_array_min)
overload(min, inline='always', no_unliteral=True)(overload_array_min)


def overload_array_sum(A):
    if isinstance(A, (IntegerArrayType, FloatingArrayType)
        ) or A == boolean_array:

        def impl(A):
            return pd.Series(A).sum()
    return impl


overload(np.sum, inline='always', no_unliteral=True)(overload_array_sum)
overload(sum, inline='always', no_unliteral=True)(overload_array_sum)


@overload(np.prod, inline='always', no_unliteral=True)
def overload_array_prod(A):
    if isinstance(A, (IntegerArrayType, FloatingArrayType)
        ) or A == boolean_array:

        def impl(A):
            return pd.Series(A).prod()
    return impl


def nonzero(arr):
    pass


@overload(nonzero, no_unliteral=True)
def nonzero_overload(A, parallel=False):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(A,
        'bodo.nonzero()')
    if not bodo.utils.utils.is_array_typ(A, False):
        return

    def impl(A, parallel=False):
        n = len(A)
        if parallel:
            offset = bodo.libs.distributed_api.dist_exscan(n, Reduce_Type.
                Sum.value)
        else:
            offset = 0
        ltfcb__ulie = []
        for i in range(n):
            if A[i]:
                ltfcb__ulie.append(i + offset)
        return np.array(ltfcb__ulie, np.int64),
    return impl


def ffill_bfill_arr(arr):
    pass


@overload(ffill_bfill_arr, no_unliteral=True)
def ffill_bfill_overload(A, method, parallel=False):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(A,
        'bodo.ffill_bfill_arr()')
    jpubc__dstm = element_type(A)
    if jpubc__dstm == types.unicode_type:
        null_value = '""'
    elif jpubc__dstm == types.bool_:
        null_value = 'False'
    elif jpubc__dstm == bodo.datetime64ns:
        null_value = (
            'bodo.utils.conversion.unbox_if_tz_naive_timestamp(pd.to_datetime(0))'
            )
    elif jpubc__dstm == bodo.timedelta64ns:
        null_value = (
            'bodo.utils.conversion.unbox_if_tz_naive_timestamp(pd.to_timedelta(0))'
            )
    else:
        null_value = '0'
    rntb__ptyh = 'i'
    hvl__vha = False
    hrt__ptyep = get_overload_const_str(method)
    if hrt__ptyep in ('ffill', 'pad'):
        ewu__blc = 'n'
        send_right = True
    elif hrt__ptyep in ('backfill', 'bfill'):
        ewu__blc = 'n-1, -1, -1'
        send_right = False
        if jpubc__dstm == types.unicode_type:
            rntb__ptyh = '(n - 1) - i'
            hvl__vha = True
    xybk__dhl = 'def impl(A, method, parallel=False):\n'
    xybk__dhl += '  A = decode_if_dict_array(A)\n'
    xybk__dhl += '  has_last_value = False\n'
    xybk__dhl += f'  last_value = {null_value}\n'
    xybk__dhl += '  if parallel:\n'
    xybk__dhl += '    rank = bodo.libs.distributed_api.get_rank()\n'
    xybk__dhl += '    n_pes = bodo.libs.distributed_api.get_size()\n'
    xybk__dhl += f"""    has_last_value, last_value = null_border_icomm(A, rank, n_pes, {null_value}, {send_right})
"""
    xybk__dhl += '  n = len(A)\n'
    xybk__dhl += '  out_arr = bodo.utils.utils.alloc_type(n, A, (-1,))\n'
    xybk__dhl += f'  for i in range({ewu__blc}):\n'
    xybk__dhl += (
        '    if (bodo.libs.array_kernels.isna(A, i) and not has_last_value):\n'
        )
    xybk__dhl += (
        f'      bodo.libs.array_kernels.setna(out_arr, {rntb__ptyh})\n')
    xybk__dhl += '      continue\n'
    xybk__dhl += '    s = A[i]\n'
    xybk__dhl += '    if bodo.libs.array_kernels.isna(A, i):\n'
    xybk__dhl += '      s = last_value\n'
    xybk__dhl += f'    out_arr[{rntb__ptyh}] = s\n'
    xybk__dhl += '    last_value = s\n'
    xybk__dhl += '    has_last_value = True\n'
    if hvl__vha:
        xybk__dhl += '  return out_arr[::-1]\n'
    else:
        xybk__dhl += '  return out_arr\n'
    hualq__delj = {}
    exec(xybk__dhl, {'bodo': bodo, 'numba': numba, 'pd': pd,
        'null_border_icomm': null_border_icomm, 'decode_if_dict_array':
        decode_if_dict_array}, hualq__delj)
    impl = hualq__delj['impl']
    return impl


@register_jitable(cache=True)
def null_border_icomm(in_arr, rank, n_pes, null_value, send_right=True):
    if send_right:
        ejco__czm = 0
        deop__aeaeo = n_pes - 1
        qlrp__wsux = np.int32(rank + 1)
        agh__uzwum = np.int32(rank - 1)
        cgr__ttddc = len(in_arr) - 1
        wcio__yybhi = -1
        iqbg__dvuq = -1
    else:
        ejco__czm = n_pes - 1
        deop__aeaeo = 0
        qlrp__wsux = np.int32(rank - 1)
        agh__uzwum = np.int32(rank + 1)
        cgr__ttddc = 0
        wcio__yybhi = len(in_arr)
        iqbg__dvuq = 1
    tcpsq__khj = np.int32(bodo.hiframes.rolling.comm_border_tag)
    qvdib__dqdam = np.empty(1, dtype=np.bool_)
    rge__odbdm = bodo.utils.utils.alloc_type(1, in_arr, (-1,))
    lhu__rdql = np.empty(1, dtype=np.bool_)
    znk__webt = bodo.utils.utils.alloc_type(1, in_arr, (-1,))
    vlc__napj = False
    rwa__iypjr = null_value
    for i in range(cgr__ttddc, wcio__yybhi, iqbg__dvuq):
        if not isna(in_arr, i):
            vlc__napj = True
            rwa__iypjr = in_arr[i]
            break
    if rank != ejco__czm:
        nnkeh__miw = bodo.libs.distributed_api.irecv(qvdib__dqdam, 1,
            agh__uzwum, tcpsq__khj, True)
        bodo.libs.distributed_api.wait(nnkeh__miw, True)
        jsdq__ugk = bodo.libs.distributed_api.irecv(rge__odbdm, 1,
            agh__uzwum, tcpsq__khj, True)
        bodo.libs.distributed_api.wait(jsdq__ugk, True)
        smt__swm = qvdib__dqdam[0]
        asc__ukej = rge__odbdm[0]
    else:
        smt__swm = False
        asc__ukej = null_value
    if vlc__napj:
        lhu__rdql[0] = vlc__napj
        znk__webt[0] = rwa__iypjr
    else:
        lhu__rdql[0] = smt__swm
        znk__webt[0] = asc__ukej
    if rank != deop__aeaeo:
        gyp__aya = bodo.libs.distributed_api.isend(lhu__rdql, 1, qlrp__wsux,
            tcpsq__khj, True)
        rohvv__ntok = bodo.libs.distributed_api.isend(znk__webt, 1,
            qlrp__wsux, tcpsq__khj, True)
    return smt__swm, asc__ukej


@overload(np.sort, inline='always', no_unliteral=True)
def np_sort(A, axis=-1, kind=None, order=None):
    if not bodo.utils.utils.is_array_typ(A, False) or isinstance(A, types.Array
        ):
        return
    gxt__smp = {'axis': axis, 'kind': kind, 'order': order}
    ngnek__tshqi = {'axis': -1, 'kind': None, 'order': None}
    check_unsupported_args('np.sort', gxt__smp, ngnek__tshqi, 'numpy')

    def impl(A, axis=-1, kind=None, order=None):
        return pd.Series(A).sort_values().values
    return impl


def repeat_kernel(A, repeats):
    pass


@overload(repeat_kernel, no_unliteral=True)
def repeat_kernel_overload(A, repeats):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(A,
        'Series.repeat()')
    jpubc__dstm = to_str_arr_if_dict_array(A)
    if isinstance(repeats, types.Integer):
        if A == bodo.dict_str_arr_type:

            def impl_dict_int(A, repeats):
                data_arr = A._data.copy()
                pbrgb__fcty = A._indices
                sqs__iwmi = len(pbrgb__fcty)
                fdgww__bmj = alloc_int_array(sqs__iwmi * repeats, np.int32)
                for i in range(sqs__iwmi):
                    rntb__ptyh = i * repeats
                    if bodo.libs.array_kernels.isna(pbrgb__fcty, i):
                        for bhn__kzcqf in range(repeats):
                            bodo.libs.array_kernels.setna(fdgww__bmj, 
                                rntb__ptyh + bhn__kzcqf)
                    else:
                        fdgww__bmj[rntb__ptyh:rntb__ptyh + repeats
                            ] = pbrgb__fcty[i]
                return init_dict_arr(data_arr, fdgww__bmj, A.
                    _has_global_dictionary, A._has_deduped_local_dictionary)
            return impl_dict_int

        def impl_int(A, repeats):
            sqs__iwmi = len(A)
            out_arr = bodo.utils.utils.alloc_type(sqs__iwmi * repeats,
                jpubc__dstm, (-1,))
            for i in range(sqs__iwmi):
                rntb__ptyh = i * repeats
                if bodo.libs.array_kernels.isna(A, i):
                    for bhn__kzcqf in range(repeats):
                        bodo.libs.array_kernels.setna(out_arr, rntb__ptyh +
                            bhn__kzcqf)
                else:
                    out_arr[rntb__ptyh:rntb__ptyh + repeats] = A[i]
            return out_arr
        return impl_int
    if A == bodo.dict_str_arr_type:

        def impl_dict_arr(A, repeats):
            data_arr = A._data.copy()
            pbrgb__fcty = A._indices
            sqs__iwmi = len(pbrgb__fcty)
            fdgww__bmj = alloc_int_array(repeats.sum(), np.int32)
            rntb__ptyh = 0
            for i in range(sqs__iwmi):
                lcx__kahn = repeats[i]
                if lcx__kahn < 0:
                    raise ValueError('repeats may not contain negative values.'
                        )
                if bodo.libs.array_kernels.isna(pbrgb__fcty, i):
                    for bhn__kzcqf in range(lcx__kahn):
                        bodo.libs.array_kernels.setna(fdgww__bmj, 
                            rntb__ptyh + bhn__kzcqf)
                else:
                    fdgww__bmj[rntb__ptyh:rntb__ptyh + lcx__kahn
                        ] = pbrgb__fcty[i]
                rntb__ptyh += lcx__kahn
            return init_dict_arr(data_arr, fdgww__bmj, A.
                _has_global_dictionary, A._has_deduped_local_dictionary)
        return impl_dict_arr

    def impl_arr(A, repeats):
        sqs__iwmi = len(A)
        out_arr = bodo.utils.utils.alloc_type(repeats.sum(), jpubc__dstm, (-1,)
            )
        rntb__ptyh = 0
        for i in range(sqs__iwmi):
            lcx__kahn = repeats[i]
            if lcx__kahn < 0:
                raise ValueError('repeats may not contain negative values.')
            if bodo.libs.array_kernels.isna(A, i):
                for bhn__kzcqf in range(lcx__kahn):
                    bodo.libs.array_kernels.setna(out_arr, rntb__ptyh +
                        bhn__kzcqf)
            else:
                out_arr[rntb__ptyh:rntb__ptyh + lcx__kahn] = A[i]
            rntb__ptyh += lcx__kahn
        return out_arr
    return impl_arr


@overload(np.repeat, inline='always', no_unliteral=True)
def np_repeat(A, repeats):
    if not bodo.utils.utils.is_array_typ(A, False) or isinstance(A, types.Array
        ):
        return
    if not isinstance(repeats, types.Integer):
        raise BodoError(
            'Only integer type supported for repeats in np.repeat()')

    def impl(A, repeats):
        return bodo.libs.array_kernels.repeat_kernel(A, repeats)
    return impl


@numba.generated_jit
def repeat_like(A, dist_like_arr):
    if not bodo.utils.utils.is_array_typ(A, False
        ) or not bodo.utils.utils.is_array_typ(dist_like_arr, False):
        raise BodoError('Both A and dist_like_arr must be array-like.')

    def impl(A, dist_like_arr):
        return bodo.libs.array_kernels.repeat_kernel(A, len(dist_like_arr))
    return impl


@overload(np.unique, inline='always', no_unliteral=True)
def np_unique(A):
    if not bodo.utils.utils.is_array_typ(A, False) or isinstance(A, types.Array
        ):
        return

    def impl(A):
        dxsi__mkbs = bodo.libs.array_kernels.unique(A)
        return bodo.allgatherv(dxsi__mkbs, False)
    return impl


@overload(np.union1d, inline='always', no_unliteral=True)
def overload_union1d(A1, A2):
    if not bodo.utils.utils.is_array_typ(A1, False
        ) or not bodo.utils.utils.is_array_typ(A2, False):
        return
    if A1 != A2:
        raise BodoError('Both arrays must be the same type in np.union1d()')

    def impl(A1, A2):
        sgh__kgb = bodo.libs.array_kernels.concat([A1, A2])
        nken__szps = bodo.libs.array_kernels.unique(sgh__kgb)
        return pd.Series(nken__szps).sort_values().values
    return impl


@overload(np.intersect1d, inline='always', no_unliteral=True)
def overload_intersect1d(A1, A2, assume_unique=False, return_indices=False):
    if not bodo.utils.utils.is_array_typ(A1, False
        ) or not bodo.utils.utils.is_array_typ(A2, False):
        return
    gxt__smp = {'assume_unique': assume_unique, 'return_indices':
        return_indices}
    ngnek__tshqi = {'assume_unique': False, 'return_indices': False}
    check_unsupported_args('np.intersect1d', gxt__smp, ngnek__tshqi, 'numpy')
    if A1 != A2:
        raise BodoError('Both arrays must be the same type in np.intersect1d()'
            )
    if A1.ndim != 1 or A2.ndim != 1:
        raise BodoError('Only 1D arrays supported in np.intersect1d()')

    def impl(A1, A2, assume_unique=False, return_indices=False):
        czmj__ksik = bodo.libs.array_kernels.unique(A1)
        qojn__ecib = bodo.libs.array_kernels.unique(A2)
        sgh__kgb = bodo.libs.array_kernels.concat([czmj__ksik, qojn__ecib])
        tkcc__ygcm = pd.Series(sgh__kgb).sort_values().values
        return slice_array_intersect1d(tkcc__ygcm)
    return impl


@register_jitable
def slice_array_intersect1d(arr):
    blr__qlh = arr[1:] == arr[:-1]
    return arr[:-1][blr__qlh]


@register_jitable(cache=True)
def intersection_mask_comm(arr, rank, n_pes):
    tcpsq__khj = np.int32(bodo.hiframes.rolling.comm_border_tag)
    nmhxb__llxd = bodo.utils.utils.alloc_type(1, arr, (-1,))
    if rank != 0:
        huky__pfj = bodo.libs.distributed_api.isend(arr[:1], 1, np.int32(
            rank - 1), tcpsq__khj, True)
        bodo.libs.distributed_api.wait(huky__pfj, True)
    if rank == n_pes - 1:
        return None
    else:
        ault__kdgy = bodo.libs.distributed_api.irecv(nmhxb__llxd, 1, np.
            int32(rank + 1), tcpsq__khj, True)
        bodo.libs.distributed_api.wait(ault__kdgy, True)
        return nmhxb__llxd[0]


@register_jitable(cache=True)
def intersection_mask(arr, parallel=False):
    n = len(arr)
    blr__qlh = np.full(n, False)
    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            blr__qlh[i] = True
    if parallel:
        rank = bodo.libs.distributed_api.get_rank()
        n_pes = bodo.libs.distributed_api.get_size()
        xxt__hayt = intersection_mask_comm(arr, rank, n_pes)
        if rank != n_pes - 1 and arr[n - 1] == xxt__hayt:
            blr__qlh[n - 1] = True
    return blr__qlh


@overload(np.setdiff1d, inline='always', no_unliteral=True)
def overload_setdiff1d(A1, A2, assume_unique=False):
    if not bodo.utils.utils.is_array_typ(A1, False
        ) or not bodo.utils.utils.is_array_typ(A2, False):
        return
    gxt__smp = {'assume_unique': assume_unique}
    ngnek__tshqi = {'assume_unique': False}
    check_unsupported_args('np.setdiff1d', gxt__smp, ngnek__tshqi, 'numpy')
    if A1 != A2:
        raise BodoError('Both arrays must be the same type in np.setdiff1d()')
    if A1.ndim != 1 or A2.ndim != 1:
        raise BodoError('Only 1D arrays supported in np.setdiff1d()')

    def impl(A1, A2, assume_unique=False):
        czmj__ksik = bodo.libs.array_kernels.unique(A1)
        qojn__ecib = bodo.libs.array_kernels.unique(A2)
        blr__qlh = calculate_mask_setdiff1d(czmj__ksik, qojn__ecib)
        return pd.Series(czmj__ksik[blr__qlh]).sort_values().values
    return impl


@register_jitable
def calculate_mask_setdiff1d(A1, A2):
    blr__qlh = np.ones(len(A1), np.bool_)
    for i in range(len(A2)):
        blr__qlh &= A1 != A2[i]
    return blr__qlh


@overload(np.linspace, inline='always', no_unliteral=True)
def np_linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=
    None, axis=0):
    gxt__smp = {'retstep': retstep, 'axis': axis}
    ngnek__tshqi = {'retstep': False, 'axis': 0}
    check_unsupported_args('np.linspace', gxt__smp, ngnek__tshqi, 'numpy')
    pjcdn__wxi = False
    if is_overload_none(dtype):
        jpubc__dstm = np.promote_types(np.promote_types(numba.np.
            numpy_support.as_dtype(start), numba.np.numpy_support.as_dtype(
            stop)), numba.np.numpy_support.as_dtype(types.float64)).type
    else:
        if isinstance(dtype.dtype, types.Integer):
            pjcdn__wxi = True
        jpubc__dstm = numba.np.numpy_support.as_dtype(dtype).type
    if pjcdn__wxi:

        def impl_int(start, stop, num=50, endpoint=True, retstep=False,
            dtype=None, axis=0):
            nczsv__dtcof = np_linspace_get_stepsize(start, stop, num, endpoint)
            numba.parfors.parfor.init_prange()
            out_arr = np.empty(num, jpubc__dstm)
            for i in numba.parfors.parfor.internal_prange(num):
                out_arr[i] = jpubc__dstm(np.floor(start + i * nczsv__dtcof))
            return out_arr
        return impl_int
    else:

        def impl(start, stop, num=50, endpoint=True, retstep=False, dtype=
            None, axis=0):
            nczsv__dtcof = np_linspace_get_stepsize(start, stop, num, endpoint)
            numba.parfors.parfor.init_prange()
            out_arr = np.empty(num, jpubc__dstm)
            for i in numba.parfors.parfor.internal_prange(num):
                out_arr[i] = jpubc__dstm(start + i * nczsv__dtcof)
            return out_arr
        return impl


def np_linspace_get_stepsize(start, stop, num, endpoint):
    return 0


@overload(np_linspace_get_stepsize, no_unliteral=True)
def overload_np_linspace_get_stepsize(start, stop, num, endpoint):

    def impl(start, stop, num, endpoint):
        if num < 0:
            raise ValueError('np.linspace() Num must be >= 0')
        if endpoint:
            num -= 1
        if num > 1:
            return (stop - start) / num
        return 0
    return impl


@overload(operator.contains, no_unliteral=True)
def arr_contains(A, val):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(A,
        'np.contains()')
    if not (bodo.utils.utils.is_array_typ(A, False) and A.dtype == types.
        unliteral(val)):
        return

    def impl(A, val):
        numba.parfors.parfor.init_prange()
        bkue__pnt = 0
        n = len(A)
        for i in numba.parfors.parfor.internal_prange(n):
            if not bodo.libs.array_kernels.isna(A, i):
                bkue__pnt += A[i] == val
        return bkue__pnt > 0
    return impl


@overload(np.any, inline='always', no_unliteral=True)
def np_any(A, axis=None, out=None, keepdims=None):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(A, 'np.any()')
    if not (bodo.utils.utils.is_array_typ(A, False) and A.ndim == 1):
        return
    gxt__smp = {'axis': axis, 'out': out, 'keepdims': keepdims}
    ngnek__tshqi = {'axis': None, 'out': None, 'keepdims': None}
    check_unsupported_args('np.any', gxt__smp, ngnek__tshqi, 'numpy')

    def impl(A, axis=None, out=None, keepdims=None):
        numba.parfors.parfor.init_prange()
        bkue__pnt = 0
        n = len(A)
        for i in numba.parfors.parfor.internal_prange(n):
            if not bodo.libs.array_kernels.isna(A, i):
                bkue__pnt += int(bool(A[i]))
        return bkue__pnt > 0
    return impl


@overload(np.all, inline='always', no_unliteral=True)
def np_all(A, axis=None, out=None, keepdims=None):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(A, 'np.all()')
    if not (bodo.utils.utils.is_array_typ(A, False) and A.ndim == 1):
        return
    gxt__smp = {'axis': axis, 'out': out, 'keepdims': keepdims}
    ngnek__tshqi = {'axis': None, 'out': None, 'keepdims': None}
    check_unsupported_args('np.any', gxt__smp, ngnek__tshqi, 'numpy')

    def impl(A, axis=None, out=None, keepdims=None):
        numba.parfors.parfor.init_prange()
        bkue__pnt = 0
        n = len(A)
        for i in numba.parfors.parfor.internal_prange(n):
            if not bodo.libs.array_kernels.isna(A, i):
                bkue__pnt += int(bool(A[i]))
        return bkue__pnt == n
    return impl


@overload(np.cbrt, inline='always', no_unliteral=True)
def np_cbrt(A, out=None, where=True, casting='same_kind', order='K', dtype=
    None, subok=True):
    if not (isinstance(A, types.Number) or bodo.utils.utils.is_array_typ(A,
        False) and A.ndim == 1 and isinstance(A.dtype, types.Number)):
        return
    gxt__smp = {'out': out, 'where': where, 'casting': casting, 'order':
        order, 'dtype': dtype, 'subok': subok}
    ngnek__tshqi = {'out': None, 'where': True, 'casting': 'same_kind',
        'order': 'K', 'dtype': None, 'subok': True}
    check_unsupported_args('np.cbrt', gxt__smp, ngnek__tshqi, 'numpy')
    if bodo.utils.utils.is_array_typ(A, False):
        zodc__ixrfq = np.promote_types(numba.np.numpy_support.as_dtype(A.
            dtype), numba.np.numpy_support.as_dtype(types.float32)).type

        def impl_arr(A, out=None, where=True, casting='same_kind', order=
            'K', dtype=None, subok=True):
            numba.parfors.parfor.init_prange()
            n = len(A)
            out_arr = np.empty(n, zodc__ixrfq)
            for i in numba.parfors.parfor.internal_prange(n):
                if bodo.libs.array_kernels.isna(A, i):
                    bodo.libs.array_kernels.setna(out_arr, i)
                    continue
                out_arr[i] = np_cbrt_scalar(A[i], zodc__ixrfq)
            return out_arr
        return impl_arr
    zodc__ixrfq = np.promote_types(numba.np.numpy_support.as_dtype(A),
        numba.np.numpy_support.as_dtype(types.float32)).type

    def impl_scalar(A, out=None, where=True, casting='same_kind', order='K',
        dtype=None, subok=True):
        return np_cbrt_scalar(A, zodc__ixrfq)
    return impl_scalar


@register_jitable
def np_cbrt_scalar(x, float_dtype):
    if np.isnan(x):
        return np.nan
    pzeez__amidj = x < 0
    if pzeez__amidj:
        x = -x
    res = np.power(float_dtype(x), 1.0 / 3.0)
    if pzeez__amidj:
        return -res
    return res


@overload(np.hstack, no_unliteral=True)
def np_hstack(tup):
    nivq__wext = isinstance(tup, (types.BaseTuple, types.List))
    tpheb__dzk = isinstance(tup, (bodo.SeriesType, bodo.hiframes.
        pd_series_ext.HeterogeneousSeriesType)) and isinstance(tup.data, (
        types.BaseTuple, types.List, bodo.NullableTupleType))
    if isinstance(tup, types.BaseTuple):
        for zkla__cgea in tup.types:
            bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(
                zkla__cgea, 'numpy.hstack()')
            nivq__wext = nivq__wext and bodo.utils.utils.is_array_typ(
                zkla__cgea, False)
    elif isinstance(tup, types.List):
        bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(tup.dtype,
            'numpy.hstack()')
        nivq__wext = bodo.utils.utils.is_array_typ(tup.dtype, False)
    elif tpheb__dzk:
        bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(tup,
            'numpy.hstack()')
        qod__pcu = tup.data.tuple_typ if isinstance(tup.data, bodo.
            NullableTupleType) else tup.data
        for zkla__cgea in qod__pcu.types:
            tpheb__dzk = tpheb__dzk and bodo.utils.utils.is_array_typ(
                zkla__cgea, False)
    if not (nivq__wext or tpheb__dzk):
        return
    if tpheb__dzk:

        def impl_series(tup):
            arr_tup = bodo.hiframes.pd_series_ext.get_series_data(tup)
            return bodo.libs.array_kernels.concat(arr_tup)
        return impl_series

    def impl(tup):
        return bodo.libs.array_kernels.concat(tup)
    return impl


@overload(np.random.multivariate_normal, inline='always', no_unliteral=True)
def np_random_multivariate_normal(mean, cov, size=None, check_valid='warn',
    tol=1e-08):
    gxt__smp = {'check_valid': check_valid, 'tol': tol}
    ngnek__tshqi = {'check_valid': 'warn', 'tol': 1e-08}
    check_unsupported_args('np.random.multivariate_normal', gxt__smp,
        ngnek__tshqi, 'numpy')
    if not isinstance(size, types.Integer):
        raise BodoError(
            'np.random.multivariate_normal() size argument is required and must be an integer'
            )
    if not (bodo.utils.utils.is_array_typ(mean, False) and mean.ndim == 1):
        raise BodoError(
            'np.random.multivariate_normal() mean must be a 1 dimensional numpy array'
            )
    if not (bodo.utils.utils.is_array_typ(cov, False) and cov.ndim == 2):
        raise BodoError(
            'np.random.multivariate_normal() cov must be a 2 dimensional square, numpy array'
            )

    def impl(mean, cov, size=None, check_valid='warn', tol=1e-08):
        _validate_multivar_norm(cov)
        twnz__jmop = mean.shape[0]
        akymd__yyps = size, twnz__jmop
        lgek__mhrsm = np.random.standard_normal(akymd__yyps)
        cov = cov.astype(np.float64)
        ubf__scpup, s, qqjrz__lbh = np.linalg.svd(cov)
        res = np.dot(lgek__mhrsm, np.sqrt(s).reshape(twnz__jmop, 1) *
            qqjrz__lbh)
        ktgky__eiq = res + mean
        return ktgky__eiq
    return impl


def _validate_multivar_norm(cov):
    return


@overload(_validate_multivar_norm, no_unliteral=True)
def _overload_validate_multivar_norm(cov):

    def impl(cov):
        if cov.shape[0] != cov.shape[1]:
            raise ValueError(
                'np.random.multivariate_normal() cov must be a 2 dimensional square, numpy array'
                )
    return impl


def _nan_argmin(arr):
    return


@overload(_nan_argmin, no_unliteral=True)
def _overload_nan_argmin(arr):
    if isinstance(arr, (IntegerArrayType, FloatingArrayType)) or arr in [
        boolean_array, datetime_date_array_type
        ] or arr.dtype == bodo.timedelta64ns:

        def impl_bodo_arr(arr):
            numba.parfors.parfor.init_prange()
            xqke__qze = bodo.hiframes.series_kernels._get_type_max_value(arr)
            fws__ryprm = typing.builtins.IndexValue(-1, xqke__qze)
            for i in numba.parfors.parfor.internal_prange(len(arr)):
                if bodo.libs.array_kernels.isna(arr, i):
                    continue
                bpog__ekp = typing.builtins.IndexValue(i, arr[i])
                fws__ryprm = min(fws__ryprm, bpog__ekp)
            return fws__ryprm.index
        return impl_bodo_arr
    if isinstance(arr, CategoricalArrayType):
        assert arr.dtype.ordered, 'Categorical Array must be ordered to select an argmin'
        toqb__bivu = bodo.hiframes.pd_categorical_ext.get_categories_int_type(
            arr.dtype)

        def impl_cat_arr(arr):
            iuyhn__epuyp = (bodo.hiframes.pd_categorical_ext.
                get_categorical_arr_codes(arr))
            numba.parfors.parfor.init_prange()
            xqke__qze = toqb__bivu(len(arr.dtype.categories) + 1)
            fws__ryprm = typing.builtins.IndexValue(-1, xqke__qze)
            for i in numba.parfors.parfor.internal_prange(len(arr)):
                if bodo.libs.array_kernels.isna(arr, i):
                    continue
                bpog__ekp = typing.builtins.IndexValue(i, iuyhn__epuyp[i])
                fws__ryprm = min(fws__ryprm, bpog__ekp)
            return fws__ryprm.index
        return impl_cat_arr
    return lambda arr: arr.argmin()


def _nan_argmax(arr):
    return


@overload(_nan_argmax, no_unliteral=True)
def _overload_nan_argmax(arr):
    if isinstance(arr, (IntegerArrayType, FloatingArrayType)) or arr in [
        boolean_array, datetime_date_array_type
        ] or arr.dtype == bodo.timedelta64ns:

        def impl_bodo_arr(arr):
            n = len(arr)
            numba.parfors.parfor.init_prange()
            xqke__qze = bodo.hiframes.series_kernels._get_type_min_value(arr)
            fws__ryprm = typing.builtins.IndexValue(-1, xqke__qze)
            for i in numba.parfors.parfor.internal_prange(n):
                if bodo.libs.array_kernels.isna(arr, i):
                    continue
                bpog__ekp = typing.builtins.IndexValue(i, arr[i])
                fws__ryprm = max(fws__ryprm, bpog__ekp)
            return fws__ryprm.index
        return impl_bodo_arr
    if isinstance(arr, CategoricalArrayType):
        assert arr.dtype.ordered, 'Categorical Array must be ordered to select an argmin'
        toqb__bivu = bodo.hiframes.pd_categorical_ext.get_categories_int_type(
            arr.dtype)

        def impl_cat_arr(arr):
            n = len(arr)
            iuyhn__epuyp = (bodo.hiframes.pd_categorical_ext.
                get_categorical_arr_codes(arr))
            numba.parfors.parfor.init_prange()
            xqke__qze = toqb__bivu(-1)
            fws__ryprm = typing.builtins.IndexValue(-1, xqke__qze)
            for i in numba.parfors.parfor.internal_prange(n):
                if bodo.libs.array_kernels.isna(arr, i):
                    continue
                bpog__ekp = typing.builtins.IndexValue(i, iuyhn__epuyp[i])
                fws__ryprm = max(fws__ryprm, bpog__ekp)
            return fws__ryprm.index
        return impl_cat_arr
    return lambda arr: arr.argmax()


@overload_attribute(types.Array, 'nbytes', inline='always')
def overload_dataframe_index(A):
    return lambda A: A.size * bodo.io.np_io.get_dtype_size(A.dtype)
