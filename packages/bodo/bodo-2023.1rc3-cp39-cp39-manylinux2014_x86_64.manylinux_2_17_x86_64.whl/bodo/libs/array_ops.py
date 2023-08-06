"""
Implements array operations for usage by DataFrames and Series
such as count and max.
"""
import numba
import numpy as np
import pandas as pd
from numba import generated_jit
from numba.core import types
from numba.extending import overload
import bodo
from bodo.hiframes.datetime_date_ext import datetime_date_array_type
from bodo.hiframes.pd_categorical_ext import CategoricalArrayType
from bodo.utils import tracing
from bodo.utils.typing import element_type, is_hashable_type, is_iterable_type, is_overload_true, is_overload_zero, is_str_arr_type


def array_op_any(arr, skipna=True):
    pass


@overload(array_op_any)
def overload_array_op_any(A, skipna=True):
    if isinstance(A, types.Array) and isinstance(A.dtype, types.Integer
        ) or isinstance(A, bodo.libs.int_arr_ext.IntegerArrayType):
        ejea__cqmkk = 0
    elif isinstance(A, bodo.libs.bool_arr_ext.BooleanArrayType) or isinstance(A
        , types.Array) and A.dtype == types.bool_:
        ejea__cqmkk = False
    elif A == bodo.string_array_type:
        ejea__cqmkk = ''
    elif A == bodo.binary_array_type:
        ejea__cqmkk = b''
    else:
        raise bodo.utils.typing.BodoError(
            f'Cannot perform any with this array type: {A}')

    def impl(A, skipna=True):
        numba.parfors.parfor.init_prange()
        pac__oriwv = 0
        for ijqj__hlcub in numba.parfors.parfor.internal_prange(len(A)):
            if not bodo.libs.array_kernels.isna(A, ijqj__hlcub):
                if A[ijqj__hlcub] != ejea__cqmkk:
                    pac__oriwv += 1
        return pac__oriwv != 0
    return impl


def array_op_all(arr, skipna=True):
    pass


@overload(array_op_all)
def overload_array_op_all(A, skipna=True):
    if isinstance(A, types.Array) and isinstance(A.dtype, types.Integer
        ) or isinstance(A, bodo.libs.int_arr_ext.IntegerArrayType):
        ejea__cqmkk = 0
    elif isinstance(A, bodo.libs.bool_arr_ext.BooleanArrayType) or isinstance(A
        , types.Array) and A.dtype == types.bool_:
        ejea__cqmkk = False
    elif A == bodo.string_array_type:
        ejea__cqmkk = ''
    elif A == bodo.binary_array_type:
        ejea__cqmkk = b''
    else:
        raise bodo.utils.typing.BodoError(
            f'Cannot perform all with this array type: {A}')

    def impl(A, skipna=True):
        numba.parfors.parfor.init_prange()
        pac__oriwv = 0
        for ijqj__hlcub in numba.parfors.parfor.internal_prange(len(A)):
            if not bodo.libs.array_kernels.isna(A, ijqj__hlcub):
                if A[ijqj__hlcub] == ejea__cqmkk:
                    pac__oriwv += 1
        return pac__oriwv == 0
    return impl


@numba.njit
def array_op_median(arr, skipna=True, parallel=False):
    yonj__iwk = np.empty(1, types.float64)
    bodo.libs.array_kernels.median_series_computation(yonj__iwk.ctypes, arr,
        parallel, skipna)
    return yonj__iwk[0]


def array_op_isna(arr):
    pass


@overload(array_op_isna)
def overload_array_op_isna(arr):

    def impl(arr):
        numba.parfors.parfor.init_prange()
        vmj__pkv = len(arr)
        ethaa__gbt = np.empty(vmj__pkv, np.bool_)
        for ijqj__hlcub in numba.parfors.parfor.internal_prange(vmj__pkv):
            ethaa__gbt[ijqj__hlcub] = bodo.libs.array_kernels.isna(arr,
                ijqj__hlcub)
        return ethaa__gbt
    return impl


def array_op_count(arr):
    pass


@overload(array_op_count)
def overload_array_op_count(arr):

    def impl(arr):
        numba.parfors.parfor.init_prange()
        pac__oriwv = 0
        for ijqj__hlcub in numba.parfors.parfor.internal_prange(len(arr)):
            xhh__hhku = 0
            if not bodo.libs.array_kernels.isna(arr, ijqj__hlcub):
                xhh__hhku = 1
            pac__oriwv += xhh__hhku
        yonj__iwk = pac__oriwv
        return yonj__iwk
    return impl


def array_op_describe(arr):
    pass


def array_op_describe_impl(arr):
    ipmf__xjcx = array_op_count(arr)
    ituhi__eiw = array_op_min(arr)
    oqp__usw = array_op_max(arr)
    dylga__xrybx = array_op_mean(arr)
    yybcb__cke = array_op_std(arr)
    bpud__kyom = array_op_quantile(arr, 0.25)
    ajqi__cuny = array_op_quantile(arr, 0.5)
    dim__xebe = array_op_quantile(arr, 0.75)
    return (ipmf__xjcx, dylga__xrybx, yybcb__cke, ituhi__eiw, bpud__kyom,
        ajqi__cuny, dim__xebe, oqp__usw)


def array_op_describe_dt_impl(arr):
    ipmf__xjcx = array_op_count(arr)
    ituhi__eiw = array_op_min(arr)
    oqp__usw = array_op_max(arr)
    dylga__xrybx = array_op_mean(arr)
    bpud__kyom = array_op_quantile(arr, 0.25)
    ajqi__cuny = array_op_quantile(arr, 0.5)
    dim__xebe = array_op_quantile(arr, 0.75)
    return (ipmf__xjcx, dylga__xrybx, ituhi__eiw, bpud__kyom, ajqi__cuny,
        dim__xebe, oqp__usw)


@overload(array_op_describe)
def overload_array_op_describe(arr):
    if arr.dtype == bodo.datetime64ns:
        return array_op_describe_dt_impl
    return array_op_describe_impl


@generated_jit(nopython=True)
def array_op_nbytes(arr):
    return array_op_nbytes_impl


def array_op_nbytes_impl(arr):
    return arr.nbytes


def array_op_min(arr):
    pass


@overload(array_op_min)
def overload_array_op_min(arr):
    if arr.dtype == bodo.timedelta64ns:

        def impl_td64(arr):
            numba.parfors.parfor.init_prange()
            brzi__dxdv = numba.cpython.builtins.get_type_max_value(np.int64)
            pac__oriwv = 0
            for ijqj__hlcub in numba.parfors.parfor.internal_prange(len(arr)):
                cpn__poowi = brzi__dxdv
                xhh__hhku = 0
                if not bodo.libs.array_kernels.isna(arr, ijqj__hlcub):
                    cpn__poowi = (bodo.hiframes.pd_timestamp_ext.
                        timedelta64_to_integer(arr[ijqj__hlcub]))
                    xhh__hhku = 1
                brzi__dxdv = min(brzi__dxdv, cpn__poowi)
                pac__oriwv += xhh__hhku
            return bodo.hiframes.pd_index_ext._tdi_val_finalize(brzi__dxdv,
                pac__oriwv)
        return impl_td64
    if arr.dtype == bodo.datetime64ns:

        def impl_dt64(arr):
            numba.parfors.parfor.init_prange()
            brzi__dxdv = numba.cpython.builtins.get_type_max_value(np.int64)
            pac__oriwv = 0
            for ijqj__hlcub in numba.parfors.parfor.internal_prange(len(arr)):
                cpn__poowi = brzi__dxdv
                xhh__hhku = 0
                if not bodo.libs.array_kernels.isna(arr, ijqj__hlcub):
                    cpn__poowi = (bodo.hiframes.pd_timestamp_ext.
                        dt64_to_integer(arr[ijqj__hlcub]))
                    xhh__hhku = 1
                brzi__dxdv = min(brzi__dxdv, cpn__poowi)
                pac__oriwv += xhh__hhku
            return bodo.hiframes.pd_index_ext._dti_val_finalize(brzi__dxdv,
                pac__oriwv)
        return impl_dt64
    if isinstance(arr, CategoricalArrayType):

        def impl_cat(arr):
            vblt__rwl = (bodo.hiframes.pd_categorical_ext.
                get_categorical_arr_codes(arr))
            numba.parfors.parfor.init_prange()
            brzi__dxdv = numba.cpython.builtins.get_type_max_value(np.int64)
            pac__oriwv = 0
            for ijqj__hlcub in numba.parfors.parfor.internal_prange(len(
                vblt__rwl)):
                gkjl__ktqoh = vblt__rwl[ijqj__hlcub]
                if gkjl__ktqoh == -1:
                    continue
                brzi__dxdv = min(brzi__dxdv, gkjl__ktqoh)
                pac__oriwv += 1
            yonj__iwk = bodo.hiframes.series_kernels._box_cat_val(brzi__dxdv,
                arr.dtype, pac__oriwv)
            return yonj__iwk
        return impl_cat
    if arr == datetime_date_array_type:

        def impl_date(arr):
            numba.parfors.parfor.init_prange()
            brzi__dxdv = bodo.hiframes.series_kernels._get_date_max_value()
            pac__oriwv = 0
            for ijqj__hlcub in numba.parfors.parfor.internal_prange(len(arr)):
                cpn__poowi = brzi__dxdv
                xhh__hhku = 0
                if not bodo.libs.array_kernels.isna(arr, ijqj__hlcub):
                    cpn__poowi = arr[ijqj__hlcub]
                    xhh__hhku = 1
                brzi__dxdv = min(brzi__dxdv, cpn__poowi)
                pac__oriwv += xhh__hhku
            yonj__iwk = bodo.hiframes.series_kernels._sum_handle_nan(brzi__dxdv
                , pac__oriwv)
            return yonj__iwk
        return impl_date

    def impl(arr):
        numba.parfors.parfor.init_prange()
        brzi__dxdv = bodo.hiframes.series_kernels._get_type_max_value(arr.dtype
            )
        pac__oriwv = 0
        for ijqj__hlcub in numba.parfors.parfor.internal_prange(len(arr)):
            cpn__poowi = brzi__dxdv
            xhh__hhku = 0
            if not bodo.libs.array_kernels.isna(arr, ijqj__hlcub):
                cpn__poowi = arr[ijqj__hlcub]
                xhh__hhku = 1
            brzi__dxdv = min(brzi__dxdv, cpn__poowi)
            pac__oriwv += xhh__hhku
        yonj__iwk = bodo.hiframes.series_kernels._sum_handle_nan(brzi__dxdv,
            pac__oriwv)
        return yonj__iwk
    return impl


def array_op_max(arr):
    pass


@overload(array_op_max)
def overload_array_op_max(arr):
    if arr.dtype == bodo.timedelta64ns:

        def impl_td64(arr):
            numba.parfors.parfor.init_prange()
            brzi__dxdv = numba.cpython.builtins.get_type_min_value(np.int64)
            pac__oriwv = 0
            for ijqj__hlcub in numba.parfors.parfor.internal_prange(len(arr)):
                cpn__poowi = brzi__dxdv
                xhh__hhku = 0
                if not bodo.libs.array_kernels.isna(arr, ijqj__hlcub):
                    cpn__poowi = (bodo.hiframes.pd_timestamp_ext.
                        timedelta64_to_integer(arr[ijqj__hlcub]))
                    xhh__hhku = 1
                brzi__dxdv = max(brzi__dxdv, cpn__poowi)
                pac__oriwv += xhh__hhku
            return bodo.hiframes.pd_index_ext._tdi_val_finalize(brzi__dxdv,
                pac__oriwv)
        return impl_td64
    if arr.dtype == bodo.datetime64ns:

        def impl_dt64(arr):
            numba.parfors.parfor.init_prange()
            brzi__dxdv = numba.cpython.builtins.get_type_min_value(np.int64)
            pac__oriwv = 0
            for ijqj__hlcub in numba.parfors.parfor.internal_prange(len(arr)):
                cpn__poowi = brzi__dxdv
                xhh__hhku = 0
                if not bodo.libs.array_kernels.isna(arr, ijqj__hlcub):
                    cpn__poowi = (bodo.hiframes.pd_timestamp_ext.
                        dt64_to_integer(arr[ijqj__hlcub]))
                    xhh__hhku = 1
                brzi__dxdv = max(brzi__dxdv, cpn__poowi)
                pac__oriwv += xhh__hhku
            return bodo.hiframes.pd_index_ext._dti_val_finalize(brzi__dxdv,
                pac__oriwv)
        return impl_dt64
    if isinstance(arr, CategoricalArrayType):

        def impl_cat(arr):
            vblt__rwl = (bodo.hiframes.pd_categorical_ext.
                get_categorical_arr_codes(arr))
            numba.parfors.parfor.init_prange()
            brzi__dxdv = -1
            for ijqj__hlcub in numba.parfors.parfor.internal_prange(len(
                vblt__rwl)):
                brzi__dxdv = max(brzi__dxdv, vblt__rwl[ijqj__hlcub])
            yonj__iwk = bodo.hiframes.series_kernels._box_cat_val(brzi__dxdv,
                arr.dtype, 1)
            return yonj__iwk
        return impl_cat
    if arr == datetime_date_array_type:

        def impl_date(arr):
            numba.parfors.parfor.init_prange()
            brzi__dxdv = bodo.hiframes.series_kernels._get_date_min_value()
            pac__oriwv = 0
            for ijqj__hlcub in numba.parfors.parfor.internal_prange(len(arr)):
                cpn__poowi = brzi__dxdv
                xhh__hhku = 0
                if not bodo.libs.array_kernels.isna(arr, ijqj__hlcub):
                    cpn__poowi = arr[ijqj__hlcub]
                    xhh__hhku = 1
                brzi__dxdv = max(brzi__dxdv, cpn__poowi)
                pac__oriwv += xhh__hhku
            yonj__iwk = bodo.hiframes.series_kernels._sum_handle_nan(brzi__dxdv
                , pac__oriwv)
            return yonj__iwk
        return impl_date

    def impl(arr):
        numba.parfors.parfor.init_prange()
        brzi__dxdv = bodo.hiframes.series_kernels._get_type_min_value(arr.dtype
            )
        pac__oriwv = 0
        for ijqj__hlcub in numba.parfors.parfor.internal_prange(len(arr)):
            cpn__poowi = brzi__dxdv
            xhh__hhku = 0
            if not bodo.libs.array_kernels.isna(arr, ijqj__hlcub):
                cpn__poowi = arr[ijqj__hlcub]
                xhh__hhku = 1
            brzi__dxdv = max(brzi__dxdv, cpn__poowi)
            pac__oriwv += xhh__hhku
        yonj__iwk = bodo.hiframes.series_kernels._sum_handle_nan(brzi__dxdv,
            pac__oriwv)
        return yonj__iwk
    return impl


def array_op_mean(arr):
    pass


@overload(array_op_mean)
def overload_array_op_mean(arr):
    if arr.dtype == bodo.datetime64ns:

        def impl(arr):
            return pd.Timestamp(types.int64(bodo.libs.array_ops.
                array_op_mean(arr.view(np.int64))))
        return impl
    ivf__lzf = types.float64
    cmec__lzq = types.float64
    if isinstance(arr, types.Array) and arr.dtype == types.float32:
        ivf__lzf = types.float32
        cmec__lzq = types.float32
    yuibf__gmv = ivf__lzf(0)
    ictd__nld = cmec__lzq(0)
    cmgj__temc = cmec__lzq(1)

    def impl(arr):
        numba.parfors.parfor.init_prange()
        brzi__dxdv = yuibf__gmv
        pac__oriwv = ictd__nld
        for ijqj__hlcub in numba.parfors.parfor.internal_prange(len(arr)):
            cpn__poowi = yuibf__gmv
            xhh__hhku = ictd__nld
            if not bodo.libs.array_kernels.isna(arr, ijqj__hlcub):
                cpn__poowi = arr[ijqj__hlcub]
                xhh__hhku = cmgj__temc
            brzi__dxdv += cpn__poowi
            pac__oriwv += xhh__hhku
        yonj__iwk = bodo.hiframes.series_kernels._mean_handle_nan(brzi__dxdv,
            pac__oriwv)
        return yonj__iwk
    return impl


def array_op_var(arr, skipna, ddof):
    pass


@overload(array_op_var)
def overload_array_op_var(arr, skipna, ddof):

    def impl(arr, skipna, ddof):
        numba.parfors.parfor.init_prange()
        hsf__ydx = 0.0
        fwiuv__vsap = 0.0
        pac__oriwv = 0
        for ijqj__hlcub in numba.parfors.parfor.internal_prange(len(arr)):
            cpn__poowi = 0.0
            xhh__hhku = 0
            if not bodo.libs.array_kernels.isna(arr, ijqj__hlcub
                ) or not skipna:
                cpn__poowi = arr[ijqj__hlcub]
                xhh__hhku = 1
            hsf__ydx += cpn__poowi
            fwiuv__vsap += cpn__poowi * cpn__poowi
            pac__oriwv += xhh__hhku
        yonj__iwk = bodo.hiframes.series_kernels._compute_var_nan_count_ddof(
            hsf__ydx, fwiuv__vsap, pac__oriwv, ddof)
        return yonj__iwk
    return impl


def array_op_std(arr, skipna=True, ddof=1):
    pass


@overload(array_op_std)
def overload_array_op_std(arr, skipna=True, ddof=1):
    if arr.dtype == bodo.datetime64ns:

        def impl_dt64(arr, skipna=True, ddof=1):
            return pd.Timedelta(types.int64(array_op_var(arr.view(np.int64),
                skipna, ddof) ** 0.5))
        return impl_dt64
    return lambda arr, skipna=True, ddof=1: array_op_var(arr, skipna, ddof
        ) ** 0.5


def array_op_quantile(arr, q):
    pass


@overload(array_op_quantile)
def overload_array_op_quantile(arr, q):
    if is_iterable_type(q):
        if arr.dtype == bodo.datetime64ns:

            def _impl_list_dt(arr, q):
                ethaa__gbt = np.empty(len(q), np.int64)
                for ijqj__hlcub in range(len(q)):
                    nenlt__zcyao = np.float64(q[ijqj__hlcub])
                    ethaa__gbt[ijqj__hlcub] = bodo.libs.array_kernels.quantile(
                        arr.view(np.int64), nenlt__zcyao)
                return ethaa__gbt.view(np.dtype('datetime64[ns]'))
            return _impl_list_dt

        def impl_list(arr, q):
            ethaa__gbt = np.empty(len(q), np.float64)
            for ijqj__hlcub in range(len(q)):
                nenlt__zcyao = np.float64(q[ijqj__hlcub])
                ethaa__gbt[ijqj__hlcub] = bodo.libs.array_kernels.quantile(arr,
                    nenlt__zcyao)
            return ethaa__gbt
        return impl_list
    if arr.dtype == bodo.datetime64ns:

        def _impl_dt(arr, q):
            return pd.Timestamp(bodo.libs.array_kernels.quantile(arr.view(
                np.int64), np.float64(q)))
        return _impl_dt

    def impl(arr, q):
        return bodo.libs.array_kernels.quantile(arr, np.float64(q))
    return impl


def array_op_sum(arr, skipna, min_count):
    pass


@overload(array_op_sum, no_unliteral=True)
def overload_array_op_sum(arr, skipna, min_count):
    if isinstance(arr.dtype, types.Integer):
        puy__rmg = types.intp
    elif arr.dtype == types.bool_:
        puy__rmg = np.int64
    else:
        puy__rmg = arr.dtype
    rkvee__qzg = puy__rmg(0)
    if isinstance(arr.dtype, types.Float) and (not is_overload_true(skipna) or
        not is_overload_zero(min_count)):

        def impl(arr, skipna, min_count):
            numba.parfors.parfor.init_prange()
            brzi__dxdv = rkvee__qzg
            vmj__pkv = len(arr)
            pac__oriwv = 0
            for ijqj__hlcub in numba.parfors.parfor.internal_prange(vmj__pkv):
                cpn__poowi = rkvee__qzg
                xhh__hhku = 0
                if not bodo.libs.array_kernels.isna(arr, ijqj__hlcub
                    ) or not skipna:
                    cpn__poowi = arr[ijqj__hlcub]
                    xhh__hhku = 1
                brzi__dxdv += cpn__poowi
                pac__oriwv += xhh__hhku
            yonj__iwk = bodo.hiframes.series_kernels._var_handle_mincount(
                brzi__dxdv, pac__oriwv, min_count)
            return yonj__iwk
    else:

        def impl(arr, skipna, min_count):
            numba.parfors.parfor.init_prange()
            brzi__dxdv = rkvee__qzg
            vmj__pkv = len(arr)
            for ijqj__hlcub in numba.parfors.parfor.internal_prange(vmj__pkv):
                cpn__poowi = rkvee__qzg
                if not bodo.libs.array_kernels.isna(arr, ijqj__hlcub):
                    cpn__poowi = arr[ijqj__hlcub]
                brzi__dxdv += cpn__poowi
            return brzi__dxdv
    return impl


def array_op_prod(arr, skipna, min_count):
    pass


@overload(array_op_prod)
def overload_array_op_prod(arr, skipna, min_count):
    kjr__ojfzs = arr.dtype(1)
    if arr.dtype == types.bool_:
        kjr__ojfzs = 1
    if isinstance(arr.dtype, types.Float):

        def impl(arr, skipna, min_count):
            numba.parfors.parfor.init_prange()
            brzi__dxdv = kjr__ojfzs
            pac__oriwv = 0
            for ijqj__hlcub in numba.parfors.parfor.internal_prange(len(arr)):
                cpn__poowi = kjr__ojfzs
                xhh__hhku = 0
                if not bodo.libs.array_kernels.isna(arr, ijqj__hlcub
                    ) or not skipna:
                    cpn__poowi = arr[ijqj__hlcub]
                    xhh__hhku = 1
                pac__oriwv += xhh__hhku
                brzi__dxdv *= cpn__poowi
            yonj__iwk = bodo.hiframes.series_kernels._var_handle_mincount(
                brzi__dxdv, pac__oriwv, min_count)
            return yonj__iwk
    else:

        def impl(arr, skipna, min_count):
            numba.parfors.parfor.init_prange()
            brzi__dxdv = kjr__ojfzs
            for ijqj__hlcub in numba.parfors.parfor.internal_prange(len(arr)):
                cpn__poowi = kjr__ojfzs
                if not bodo.libs.array_kernels.isna(arr, ijqj__hlcub):
                    cpn__poowi = arr[ijqj__hlcub]
                brzi__dxdv *= cpn__poowi
            return brzi__dxdv
    return impl


def array_op_idxmax(arr, index):
    pass


@overload(array_op_idxmax, inline='always')
def overload_array_op_idxmax(arr, index):

    def impl(arr, index):
        ijqj__hlcub = bodo.libs.array_kernels._nan_argmax(arr)
        return index[ijqj__hlcub]
    return impl


def array_op_idxmin(arr, index):
    pass


@overload(array_op_idxmin, inline='always')
def overload_array_op_idxmin(arr, index):

    def impl(arr, index):
        ijqj__hlcub = bodo.libs.array_kernels._nan_argmin(arr)
        return index[ijqj__hlcub]
    return impl


def _convert_isin_values(values, use_hash_impl):
    pass


@overload(_convert_isin_values, no_unliteral=True)
def overload_convert_isin_values(values, use_hash_impl):
    if is_overload_true(use_hash_impl):

        def impl(values, use_hash_impl):
            ybnsm__owg = {}
            for iezgs__rsj in values:
                ybnsm__owg[bodo.utils.conversion.box_if_dt64(iezgs__rsj)] = 0
            return ybnsm__owg
        return impl
    else:

        def impl(values, use_hash_impl):
            return values
        return impl


def array_op_isin(arr, values):
    pass


@overload(array_op_isin, inline='always')
def overload_array_op_isin(arr, values):
    use_hash_impl = element_type(values) == element_type(arr
        ) and is_hashable_type(element_type(values))

    def impl(arr, values):
        values = bodo.libs.array_ops._convert_isin_values(values, use_hash_impl
            )
        numba.parfors.parfor.init_prange()
        vmj__pkv = len(arr)
        ethaa__gbt = np.empty(vmj__pkv, np.bool_)
        for ijqj__hlcub in numba.parfors.parfor.internal_prange(vmj__pkv):
            ethaa__gbt[ijqj__hlcub] = bodo.utils.conversion.box_if_dt64(arr
                [ijqj__hlcub]) in values
        return ethaa__gbt
    return impl


@generated_jit(nopython=True)
def array_unique_vector_map(in_arr_tup):
    wjs__mzsk = len(in_arr_tup) != 1
    lvly__ytvuk = list(in_arr_tup.types)
    lnf__mnjff = 'def impl(in_arr_tup):\n'
    lnf__mnjff += (
        "  ev = tracing.Event('array_unique_vector_map', is_parallel=False)\n")
    lnf__mnjff += '  n = len(in_arr_tup[0])\n'
    if wjs__mzsk:
        ehdi__xidsc = ', '.join([f'in_arr_tup[{ijqj__hlcub}][unused]' for
            ijqj__hlcub in range(len(in_arr_tup))])
        brmyv__kaiys = ', '.join(['False' for tyz__dguup in range(len(
            in_arr_tup))])
        lnf__mnjff += f"""  arr_map = {{bodo.libs.nullable_tuple_ext.build_nullable_tuple(({ehdi__xidsc},), ({brmyv__kaiys},)): 0 for unused in range(0)}}
"""
        lnf__mnjff += '  map_vector = np.empty(n, np.int64)\n'
        for ijqj__hlcub, pzc__tii in enumerate(lvly__ytvuk):
            lnf__mnjff += f'  in_lst_{ijqj__hlcub} = []\n'
            if is_str_arr_type(pzc__tii):
                lnf__mnjff += f'  total_len_{ijqj__hlcub} = 0\n'
            lnf__mnjff += f'  null_in_lst_{ijqj__hlcub} = []\n'
        lnf__mnjff += '  for i in range(n):\n'
        sdug__zqzpr = ', '.join([f'in_arr_tup[{ijqj__hlcub}][i]' for
            ijqj__hlcub in range(len(lvly__ytvuk))])
        uuxy__imgwb = ', '.join([
            f'bodo.libs.array_kernels.isna(in_arr_tup[{ijqj__hlcub}], i)' for
            ijqj__hlcub in range(len(lvly__ytvuk))])
        lnf__mnjff += f"""    data_val = bodo.libs.nullable_tuple_ext.build_nullable_tuple(({sdug__zqzpr},), ({uuxy__imgwb},))
"""
        lnf__mnjff += '    if data_val not in arr_map:\n'
        lnf__mnjff += '      set_val = len(arr_map)\n'
        lnf__mnjff += '      values_tup = data_val._data\n'
        lnf__mnjff += '      nulls_tup = data_val._null_values\n'
        for ijqj__hlcub, pzc__tii in enumerate(lvly__ytvuk):
            lnf__mnjff += (
                f'      in_lst_{ijqj__hlcub}.append(values_tup[{ijqj__hlcub}])\n'
                )
            lnf__mnjff += (
                f'      null_in_lst_{ijqj__hlcub}.append(nulls_tup[{ijqj__hlcub}])\n'
                )
            if is_str_arr_type(pzc__tii):
                lnf__mnjff += f"""      total_len_{ijqj__hlcub}  += nulls_tup[{ijqj__hlcub}] * bodo.libs.str_arr_ext.get_str_arr_item_length(in_arr_tup[{ijqj__hlcub}], i)
"""
        lnf__mnjff += '      arr_map[data_val] = len(arr_map)\n'
        lnf__mnjff += '    else:\n'
        lnf__mnjff += '      set_val = arr_map[data_val]\n'
        lnf__mnjff += '    map_vector[i] = set_val\n'
        lnf__mnjff += '  n_rows = len(arr_map)\n'
        for ijqj__hlcub, pzc__tii in enumerate(lvly__ytvuk):
            if is_str_arr_type(pzc__tii):
                lnf__mnjff += f"""  out_arr_{ijqj__hlcub} = bodo.libs.str_arr_ext.pre_alloc_string_array(n_rows, total_len_{ijqj__hlcub})
"""
            else:
                lnf__mnjff += f"""  out_arr_{ijqj__hlcub} = bodo.utils.utils.alloc_type(n_rows, in_arr_tup[{ijqj__hlcub}], (-1,))
"""
        lnf__mnjff += '  for j in range(len(arr_map)):\n'
        for ijqj__hlcub in range(len(lvly__ytvuk)):
            lnf__mnjff += f'    if null_in_lst_{ijqj__hlcub}[j]:\n'
            lnf__mnjff += (
                f'      bodo.libs.array_kernels.setna(out_arr_{ijqj__hlcub}, j)\n'
                )
            lnf__mnjff += '    else:\n'
            lnf__mnjff += (
                f'      out_arr_{ijqj__hlcub}[j] = in_lst_{ijqj__hlcub}[j]\n')
        rqm__mwov = ', '.join([f'out_arr_{ijqj__hlcub}' for ijqj__hlcub in
            range(len(lvly__ytvuk))])
        lnf__mnjff += "  ev.add_attribute('n_map_entries', n_rows)\n"
        lnf__mnjff += '  ev.finalize()\n'
        lnf__mnjff += f'  return ({rqm__mwov},), map_vector\n'
    else:
        lnf__mnjff += '  in_arr = in_arr_tup[0]\n'
        lnf__mnjff += (
            f'  arr_map = {{in_arr[unused]: 0 for unused in range(0)}}\n')
        lnf__mnjff += '  map_vector = np.empty(n, np.int64)\n'
        lnf__mnjff += '  is_na = 0\n'
        lnf__mnjff += '  in_lst = []\n'
        lnf__mnjff += '  na_idxs = []\n'
        if is_str_arr_type(lvly__ytvuk[0]):
            lnf__mnjff += '  total_len = 0\n'
        lnf__mnjff += '  for i in range(n):\n'
        lnf__mnjff += '    if bodo.libs.array_kernels.isna(in_arr, i):\n'
        lnf__mnjff += '      is_na = 1\n'
        lnf__mnjff += '      # Always put NA in the last location.\n'
        lnf__mnjff += '      # We use -1 as a placeholder\n'
        lnf__mnjff += '      set_val = -1\n'
        lnf__mnjff += '      na_idxs.append(i)\n'
        lnf__mnjff += '    else:\n'
        lnf__mnjff += '      data_val = in_arr[i]\n'
        lnf__mnjff += '      if data_val not in arr_map:\n'
        lnf__mnjff += '        set_val = len(arr_map)\n'
        lnf__mnjff += '        in_lst.append(data_val)\n'
        if is_str_arr_type(lvly__ytvuk[0]):
            lnf__mnjff += """        total_len += bodo.libs.str_arr_ext.get_str_arr_item_length(in_arr, i)
"""
        lnf__mnjff += '        arr_map[data_val] = len(arr_map)\n'
        lnf__mnjff += '      else:\n'
        lnf__mnjff += '        set_val = arr_map[data_val]\n'
        lnf__mnjff += '    map_vector[i] = set_val\n'
        lnf__mnjff += '  map_vector[na_idxs] = len(arr_map)\n'
        lnf__mnjff += '  n_rows = len(arr_map) + is_na\n'
        if is_str_arr_type(lvly__ytvuk[0]):
            lnf__mnjff += """  out_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(n_rows, total_len)
"""
        else:
            lnf__mnjff += (
                '  out_arr = bodo.utils.utils.alloc_type(n_rows, in_arr, (-1,))\n'
                )
        lnf__mnjff += '  for j in range(len(arr_map)):\n'
        lnf__mnjff += '    out_arr[j] = in_lst[j]\n'
        lnf__mnjff += '  if is_na:\n'
        lnf__mnjff += (
            '    bodo.libs.array_kernels.setna(out_arr, n_rows - 1)\n')
        lnf__mnjff += "  ev.add_attribute('n_map_entries', n_rows)\n"
        lnf__mnjff += '  ev.finalize()\n'
        lnf__mnjff += f'  return (out_arr,), map_vector\n'
    rql__ipsdi = {}
    exec(lnf__mnjff, {'bodo': bodo, 'np': np, 'tracing': tracing}, rql__ipsdi)
    impl = rql__ipsdi['impl']
    return impl
