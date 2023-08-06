"""
Implementation of Series attributes and methods using overload.
"""
import operator
import numba
import numpy as np
import pandas as pd
from numba.core import types
from numba.core.typing.templates import AbstractTemplate, infer_global
from numba.extending import lower_builtin, overload, overload_attribute, overload_method, register_jitable
import bodo
from bodo.hiframes.datetime_datetime_ext import datetime_datetime_type
from bodo.hiframes.datetime_timedelta_ext import PDTimeDeltaType, datetime_timedelta_type
from bodo.hiframes.pd_categorical_ext import CategoricalArrayType, PDCategoricalDtype
from bodo.hiframes.pd_offsets_ext import is_offsets_type
from bodo.hiframes.pd_series_ext import HeterogeneousSeriesType, SeriesType, if_series_to_array_type, is_series_type
from bodo.hiframes.pd_timestamp_ext import PandasTimestampType, convert_val_to_timestamp, pd_timestamp_tz_naive_type
from bodo.hiframes.rolling import is_supported_shift_array_type
from bodo.libs.array_item_arr_ext import ArrayItemArrayType
from bodo.libs.binary_arr_ext import BinaryArrayType, binary_array_type, bytes_type
from bodo.libs.bool_arr_ext import BooleanArrayType, boolean_array
from bodo.libs.decimal_arr_ext import Decimal128Type, DecimalArrayType
from bodo.libs.float_arr_ext import FloatingArrayType
from bodo.libs.int_arr_ext import IntegerArrayType
from bodo.libs.pd_datetime_arr_ext import unwrap_tz_array
from bodo.libs.str_arr_ext import StringArrayType
from bodo.libs.str_ext import string_type
from bodo.utils.transform import is_var_size_item_array_type
from bodo.utils.typing import BodoError, ColNamesMetaType, can_replace, check_unsupported_args, dtype_to_array_type, element_type, get_common_scalar_dtype, get_index_names, get_literal_value, get_overload_const_bytes, get_overload_const_int, get_overload_const_str, is_common_scalar_dtype, is_iterable_type, is_literal_type, is_nullable_type, is_overload_bool, is_overload_constant_bool, is_overload_constant_bytes, is_overload_constant_int, is_overload_constant_nan, is_overload_constant_str, is_overload_false, is_overload_int, is_overload_none, is_overload_true, is_overload_zero, is_scalar_type, is_str_arr_type, raise_bodo_error, to_nullable_type, to_str_arr_if_dict_array


@overload_attribute(HeterogeneousSeriesType, 'index', inline='always')
@overload_attribute(SeriesType, 'index', inline='always')
def overload_series_index(s):
    return lambda s: bodo.hiframes.pd_series_ext.get_series_index(s)


@overload_attribute(HeterogeneousSeriesType, 'values', inline='always')
@overload_attribute(SeriesType, 'values', inline='always')
def overload_series_values(s):
    if isinstance(s.data, bodo.DatetimeArrayType):

        def impl(s):
            rdn__kvefx = bodo.hiframes.pd_series_ext.get_series_data(s)
            dysu__bduc = bodo.libs.pd_datetime_arr_ext.unwrap_tz_array(
                rdn__kvefx)
            return dysu__bduc
        return impl
    return lambda s: bodo.hiframes.pd_series_ext.get_series_data(s)


@overload_attribute(SeriesType, 'dtype', inline='always')
def overload_series_dtype(s):
    if s.dtype == bodo.string_type:
        raise BodoError('Series.dtype not supported for string Series yet')
    return lambda s: bodo.hiframes.pd_series_ext.get_series_data(s).dtype


@overload_attribute(HeterogeneousSeriesType, 'shape')
@overload_attribute(SeriesType, 'shape')
def overload_series_shape(s):
    return lambda s: (len(bodo.hiframes.pd_series_ext.get_series_data(s)),)


@overload_attribute(HeterogeneousSeriesType, 'ndim', inline='always')
@overload_attribute(SeriesType, 'ndim', inline='always')
def overload_series_ndim(s):
    return lambda s: 1


@overload_attribute(HeterogeneousSeriesType, 'size')
@overload_attribute(SeriesType, 'size')
def overload_series_size(s):
    return lambda s: len(bodo.hiframes.pd_series_ext.get_series_data(s))


@overload_attribute(HeterogeneousSeriesType, 'T', inline='always')
@overload_attribute(SeriesType, 'T', inline='always')
def overload_series_T(s):
    return lambda s: s


@overload_attribute(SeriesType, 'hasnans', inline='always')
def overload_series_hasnans(s):
    return lambda s: s.isna().sum() != 0


@overload_attribute(HeterogeneousSeriesType, 'empty')
@overload_attribute(SeriesType, 'empty')
def overload_series_empty(s):
    return lambda s: len(bodo.hiframes.pd_series_ext.get_series_data(s)) == 0


@overload_attribute(SeriesType, 'dtypes', inline='always')
def overload_series_dtypes(s):
    return lambda s: s.dtype


@overload_attribute(HeterogeneousSeriesType, 'name', inline='always')
@overload_attribute(SeriesType, 'name', inline='always')
def overload_series_name(s):
    return lambda s: bodo.hiframes.pd_series_ext.get_series_name(s)


@overload(len, no_unliteral=True)
def overload_series_len(S):
    if isinstance(S, (SeriesType, HeterogeneousSeriesType)):
        return lambda S: len(bodo.hiframes.pd_series_ext.get_series_data(S))


@overload_method(SeriesType, 'copy', inline='always', no_unliteral=True)
def overload_series_copy(S, deep=True):
    if is_overload_true(deep):

        def impl1(S, deep=True):
            arr = bodo.hiframes.pd_series_ext.get_series_data(S)
            index = bodo.hiframes.pd_series_ext.get_series_index(S)
            name = bodo.hiframes.pd_series_ext.get_series_name(S)
            return bodo.hiframes.pd_series_ext.init_series(arr.copy(),
                index, name)
        return impl1
    if is_overload_false(deep):

        def impl2(S, deep=True):
            arr = bodo.hiframes.pd_series_ext.get_series_data(S)
            index = bodo.hiframes.pd_series_ext.get_series_index(S)
            name = bodo.hiframes.pd_series_ext.get_series_name(S)
            return bodo.hiframes.pd_series_ext.init_series(arr, index, name)
        return impl2

    def impl(S, deep=True):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        if deep:
            arr = arr.copy()
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        return bodo.hiframes.pd_series_ext.init_series(arr, index, name)
    return impl


@overload_method(SeriesType, 'to_list', no_unliteral=True)
@overload_method(SeriesType, 'tolist', no_unliteral=True)
def overload_series_to_list(S):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.tolist()')
    if isinstance(S.dtype, types.Float):

        def impl_float(S):
            uqy__qsuj = list()
            for ynjr__fnfp in range(len(S)):
                uqy__qsuj.append(S.iat[ynjr__fnfp])
            return uqy__qsuj
        return impl_float

    def impl(S):
        uqy__qsuj = list()
        for ynjr__fnfp in range(len(S)):
            if bodo.libs.array_kernels.isna(S.values, ynjr__fnfp):
                raise ValueError(
                    'Series.to_list(): Not supported for NA values with non-float dtypes'
                    )
            uqy__qsuj.append(S.iat[ynjr__fnfp])
        return uqy__qsuj
    return impl


@overload_method(SeriesType, 'to_numpy', inline='always', no_unliteral=True)
def overload_series_to_numpy(S, dtype=None, copy=False, na_value=None):
    yppn__bgd = dict(dtype=dtype, copy=copy, na_value=na_value)
    ihi__bqwp = dict(dtype=None, copy=False, na_value=None)
    check_unsupported_args('Series.to_numpy', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')

    def impl(S, dtype=None, copy=False, na_value=None):
        return S.values
    return impl


@overload_method(SeriesType, 'reset_index', inline='always', no_unliteral=True)
def overload_series_reset_index(S, level=None, drop=False, name=None,
    inplace=False):
    yppn__bgd = dict(name=name, inplace=inplace)
    ihi__bqwp = dict(name=None, inplace=False)
    check_unsupported_args('Series.reset_index', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not bodo.hiframes.dataframe_impl._is_all_levels(S, level):
        raise_bodo_error(
            'Series.reset_index(): only dropping all index levels supported')
    if not is_overload_constant_bool(drop):
        raise_bodo_error(
            "Series.reset_index(): 'drop' parameter should be a constant boolean value"
            )
    if is_overload_true(drop):

        def impl_drop(S, level=None, drop=False, name=None, inplace=False):
            arr = bodo.hiframes.pd_series_ext.get_series_data(S)
            index = bodo.hiframes.pd_index_ext.init_range_index(0, len(arr),
                1, None)
            name = bodo.hiframes.pd_series_ext.get_series_name(S)
            return bodo.hiframes.pd_series_ext.init_series(arr, index, name)
        return impl_drop

    def get_name_literal(name_typ, is_index=False, series_name=None):
        if is_overload_none(name_typ):
            if is_index:
                return 'index' if series_name != 'index' else 'level_0'
            return 0
        if is_literal_type(name_typ):
            return get_literal_value(name_typ)
        else:
            raise BodoError(
                'Series.reset_index() not supported for non-literal series names'
                )
    series_name = get_name_literal(S.name_typ)
    if isinstance(S.index, bodo.hiframes.pd_multi_index_ext.MultiIndexType):
        qsfw__whw = ', '.join(['index_arrs[{}]'.format(ynjr__fnfp) for
            ynjr__fnfp in range(S.index.nlevels)])
    else:
        qsfw__whw = '    bodo.utils.conversion.index_to_array(index)\n'
    scmi__rdgp = 'index' if 'index' != series_name else 'level_0'
    nud__vsop = get_index_names(S.index, 'Series.reset_index()', scmi__rdgp)
    columns = [name for name in nud__vsop]
    columns.append(series_name)
    deqe__ahp = (
        'def _impl(S, level=None, drop=False, name=None, inplace=False):\n')
    deqe__ahp += '    arr = bodo.hiframes.pd_series_ext.get_series_data(S)\n'
    deqe__ahp += (
        '    index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
    if isinstance(S.index, bodo.hiframes.pd_multi_index_ext.MultiIndexType):
        deqe__ahp += (
            '    index_arrs = bodo.hiframes.pd_index_ext.get_index_data(index)\n'
            )
    deqe__ahp += (
        '    df_index = bodo.hiframes.pd_index_ext.init_range_index(0, len(S), 1, None)\n'
        )
    deqe__ahp += f"""    return bodo.hiframes.pd_dataframe_ext.init_dataframe(({qsfw__whw}, arr), df_index, __col_name_meta_value_series_reset_index)
"""
    nii__tveq = {}
    exec(deqe__ahp, {'bodo': bodo,
        '__col_name_meta_value_series_reset_index': ColNamesMetaType(tuple(
        columns))}, nii__tveq)
    lzfr__vaom = nii__tveq['_impl']
    return lzfr__vaom


@overload_method(SeriesType, 'isna', inline='always', no_unliteral=True)
@overload_method(SeriesType, 'isnull', inline='always', no_unliteral=True)
def overload_series_isna(S):

    def impl(S):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        wzmu__etpuf = bodo.libs.array_ops.array_op_isna(arr)
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf, index, name
            )
    return impl


@overload_method(SeriesType, 'round', inline='always', no_unliteral=True)
def overload_series_round(S, decimals=0):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.round()')

    def impl(S, decimals=0):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        numba.parfors.parfor.init_prange()
        n = len(arr)
        wzmu__etpuf = bodo.utils.utils.alloc_type(n, arr, (-1,))
        for ynjr__fnfp in numba.parfors.parfor.internal_prange(n):
            if pd.isna(arr[ynjr__fnfp]):
                bodo.libs.array_kernels.setna(wzmu__etpuf, ynjr__fnfp)
            else:
                wzmu__etpuf[ynjr__fnfp] = np.round(arr[ynjr__fnfp], decimals)
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf, index, name
            )
    return impl


@overload_method(SeriesType, 'sum', inline='always', no_unliteral=True)
def overload_series_sum(S, axis=None, skipna=True, level=None, numeric_only
    =None, min_count=0):
    yppn__bgd = dict(level=level, numeric_only=numeric_only)
    ihi__bqwp = dict(level=None, numeric_only=None)
    check_unsupported_args('Series.sum', yppn__bgd, ihi__bqwp, package_name
        ='pandas', module_name='Series')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error('Series.sum(): axis argument not supported')
    if not is_overload_bool(skipna):
        raise BodoError('Series.sum(): skipna argument must be a boolean')
    if not is_overload_int(min_count):
        raise BodoError('Series.sum(): min_count argument must be an integer')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S, 'Series.sum()'
        )

    def impl(S, axis=None, skipna=True, level=None, numeric_only=None,
        min_count=0):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        return bodo.libs.array_ops.array_op_sum(arr, skipna, min_count)
    return impl


@overload_method(SeriesType, 'prod', inline='always', no_unliteral=True)
@overload_method(SeriesType, 'product', inline='always', no_unliteral=True)
def overload_series_prod(S, axis=None, skipna=True, level=None,
    numeric_only=None, min_count=0):
    yppn__bgd = dict(level=level, numeric_only=numeric_only)
    ihi__bqwp = dict(level=None, numeric_only=None)
    check_unsupported_args('Series.product', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error('Series.product(): axis argument not supported')
    if not is_overload_bool(skipna):
        raise BodoError('Series.product(): skipna argument must be a boolean')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.product()')

    def impl(S, axis=None, skipna=True, level=None, numeric_only=None,
        min_count=0):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        return bodo.libs.array_ops.array_op_prod(arr, skipna, min_count)
    return impl


@overload_method(SeriesType, 'any', inline='always', no_unliteral=True)
def overload_series_any(S, axis=0, bool_only=None, skipna=True, level=None):
    yppn__bgd = dict(axis=axis, bool_only=bool_only, skipna=skipna, level=level
        )
    ihi__bqwp = dict(axis=0, bool_only=None, skipna=True, level=None)
    check_unsupported_args('Series.any', yppn__bgd, ihi__bqwp, package_name
        ='pandas', module_name='Series')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S, 'Series.any()'
        )

    def impl(S, axis=0, bool_only=None, skipna=True, level=None):
        A = bodo.hiframes.pd_series_ext.get_series_data(S)
        return bodo.libs.array_ops.array_op_any(A)
    return impl


@overload_method(SeriesType, 'equals', inline='always', no_unliteral=True)
def overload_series_equals(S, other):
    if not isinstance(other, SeriesType):
        raise BodoError("Series.equals() 'other' must be a Series")
    if isinstance(S.data, bodo.ArrayItemArrayType):
        raise BodoError(
            'Series.equals() not supported for Series where each element is an array or list'
            )
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.equals()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(other,
        'Series.equals()')
    if S.data != other.data:
        return lambda S, other: False

    def impl(S, other):
        xvjzb__hhi = bodo.hiframes.pd_series_ext.get_series_data(S)
        hug__lia = bodo.hiframes.pd_series_ext.get_series_data(other)
        numba.parfors.parfor.init_prange()
        qtx__jin = 0
        for ynjr__fnfp in numba.parfors.parfor.internal_prange(len(xvjzb__hhi)
            ):
            xakhd__wjd = 0
            dwl__oum = bodo.libs.array_kernels.isna(xvjzb__hhi, ynjr__fnfp)
            nffw__qlyrh = bodo.libs.array_kernels.isna(hug__lia, ynjr__fnfp)
            if dwl__oum and not nffw__qlyrh or not dwl__oum and nffw__qlyrh:
                xakhd__wjd = 1
            elif not dwl__oum:
                if xvjzb__hhi[ynjr__fnfp] != hug__lia[ynjr__fnfp]:
                    xakhd__wjd = 1
            qtx__jin += xakhd__wjd
        return qtx__jin == 0
    return impl


@overload_method(SeriesType, 'all', inline='always', no_unliteral=True)
def overload_series_all(S, axis=0, bool_only=None, skipna=True, level=None):
    yppn__bgd = dict(axis=axis, bool_only=bool_only, skipna=skipna, level=level
        )
    ihi__bqwp = dict(axis=0, bool_only=None, skipna=True, level=None)
    check_unsupported_args('Series.all', yppn__bgd, ihi__bqwp, package_name
        ='pandas', module_name='Series')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S, 'Series.all()'
        )

    def impl(S, axis=0, bool_only=None, skipna=True, level=None):
        A = bodo.hiframes.pd_series_ext.get_series_data(S)
        return bodo.libs.array_ops.array_op_all(A)
    return impl


@overload_method(SeriesType, 'mad', inline='always', no_unliteral=True)
def overload_series_mad(S, axis=None, skipna=True, level=None):
    yppn__bgd = dict(level=level)
    ihi__bqwp = dict(level=None)
    check_unsupported_args('Series.mad', yppn__bgd, ihi__bqwp, package_name
        ='pandas', module_name='Series')
    if not is_overload_bool(skipna):
        raise BodoError("Series.mad(): 'skipna' argument must be a boolean")
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error('Series.mad(): axis argument not supported')
    fejcn__ivwg = types.float64
    fyb__uvvr = types.float64
    if S.dtype == types.float32:
        fejcn__ivwg = types.float32
        fyb__uvvr = types.float32
    htnrf__smmw = fejcn__ivwg(0)
    tzw__tqsdq = fyb__uvvr(0)
    bhl__bepjt = fyb__uvvr(1)
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S, 'Series.mad()'
        )

    def impl(S, axis=None, skipna=True, level=None):
        A = bodo.hiframes.pd_series_ext.get_series_data(S)
        numba.parfors.parfor.init_prange()
        kjug__gniab = htnrf__smmw
        qtx__jin = tzw__tqsdq
        for ynjr__fnfp in numba.parfors.parfor.internal_prange(len(A)):
            xakhd__wjd = htnrf__smmw
            cgq__gkc = tzw__tqsdq
            if not bodo.libs.array_kernels.isna(A, ynjr__fnfp) or not skipna:
                xakhd__wjd = A[ynjr__fnfp]
                cgq__gkc = bhl__bepjt
            kjug__gniab += xakhd__wjd
            qtx__jin += cgq__gkc
        fchoc__rioc = bodo.hiframes.series_kernels._mean_handle_nan(kjug__gniab
            , qtx__jin)
        gafe__cwh = htnrf__smmw
        for ynjr__fnfp in numba.parfors.parfor.internal_prange(len(A)):
            xakhd__wjd = htnrf__smmw
            if not bodo.libs.array_kernels.isna(A, ynjr__fnfp) or not skipna:
                xakhd__wjd = abs(A[ynjr__fnfp] - fchoc__rioc)
            gafe__cwh += xakhd__wjd
        xhm__dpor = bodo.hiframes.series_kernels._mean_handle_nan(gafe__cwh,
            qtx__jin)
        return xhm__dpor
    return impl


@overload_method(SeriesType, 'mean', inline='always', no_unliteral=True)
def overload_series_mean(S, axis=None, skipna=None, level=None,
    numeric_only=None):
    if not isinstance(S.dtype, types.Number) and S.dtype not in [bodo.
        datetime64ns, types.bool_]:
        raise BodoError(f"Series.mean(): Series with type '{S}' not supported")
    yppn__bgd = dict(skipna=skipna, level=level, numeric_only=numeric_only)
    ihi__bqwp = dict(skipna=None, level=None, numeric_only=None)
    check_unsupported_args('Series.mean', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error('Series.mean(): axis argument not supported')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.mean()')

    def impl(S, axis=None, skipna=None, level=None, numeric_only=None):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        return bodo.libs.array_ops.array_op_mean(arr)
    return impl


@overload_method(SeriesType, 'sem', inline='always', no_unliteral=True)
def overload_series_sem(S, axis=None, skipna=True, level=None, ddof=1,
    numeric_only=None):
    yppn__bgd = dict(level=level, numeric_only=numeric_only)
    ihi__bqwp = dict(level=None, numeric_only=None)
    check_unsupported_args('Series.sem', yppn__bgd, ihi__bqwp, package_name
        ='pandas', module_name='Series')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error('Series.sem(): axis argument not supported')
    if not is_overload_bool(skipna):
        raise BodoError('Series.sem(): skipna argument must be a boolean')
    if not is_overload_int(ddof):
        raise BodoError('Series.sem(): ddof argument must be an integer')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S, 'Series.sem()'
        )

    def impl(S, axis=None, skipna=True, level=None, ddof=1, numeric_only=None):
        A = bodo.hiframes.pd_series_ext.get_series_data(S)
        numba.parfors.parfor.init_prange()
        niact__qky = 0
        spvg__djsn = 0
        qtx__jin = 0
        for ynjr__fnfp in numba.parfors.parfor.internal_prange(len(A)):
            xakhd__wjd = 0
            cgq__gkc = 0
            if not bodo.libs.array_kernels.isna(A, ynjr__fnfp) or not skipna:
                xakhd__wjd = A[ynjr__fnfp]
                cgq__gkc = 1
            niact__qky += xakhd__wjd
            spvg__djsn += xakhd__wjd * xakhd__wjd
            qtx__jin += cgq__gkc
        lzxbl__uvwtt = (bodo.hiframes.series_kernels.
            _compute_var_nan_count_ddof(niact__qky, spvg__djsn, qtx__jin, ddof)
            )
        yjoae__uln = bodo.hiframes.series_kernels._sem_handle_nan(lzxbl__uvwtt,
            qtx__jin)
        return yjoae__uln
    return impl


@overload_method(SeriesType, 'kurt', inline='always', no_unliteral=True)
@overload_method(SeriesType, 'kurtosis', inline='always', no_unliteral=True)
def overload_series_kurt(S, axis=None, skipna=True, level=None,
    numeric_only=None):
    yppn__bgd = dict(level=level, numeric_only=numeric_only)
    ihi__bqwp = dict(level=None, numeric_only=None)
    check_unsupported_args('Series.kurtosis', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error('Series.kurtosis(): axis argument not supported')
    if not is_overload_bool(skipna):
        raise BodoError(
            "Series.kurtosis(): 'skipna' argument must be a boolean")
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.kurtosis()')

    def impl(S, axis=None, skipna=True, level=None, numeric_only=None):
        A = bodo.hiframes.pd_series_ext.get_series_data(S)
        numba.parfors.parfor.init_prange()
        niact__qky = 0.0
        spvg__djsn = 0.0
        ldfbh__wks = 0.0
        xec__rabs = 0.0
        qtx__jin = 0
        for ynjr__fnfp in numba.parfors.parfor.internal_prange(len(A)):
            xakhd__wjd = 0.0
            cgq__gkc = 0
            if not bodo.libs.array_kernels.isna(A, ynjr__fnfp) or not skipna:
                xakhd__wjd = np.float64(A[ynjr__fnfp])
                cgq__gkc = 1
            niact__qky += xakhd__wjd
            spvg__djsn += xakhd__wjd ** 2
            ldfbh__wks += xakhd__wjd ** 3
            xec__rabs += xakhd__wjd ** 4
            qtx__jin += cgq__gkc
        lzxbl__uvwtt = bodo.hiframes.series_kernels.compute_kurt(niact__qky,
            spvg__djsn, ldfbh__wks, xec__rabs, qtx__jin)
        return lzxbl__uvwtt
    return impl


@overload_method(SeriesType, 'skew', inline='always', no_unliteral=True)
def overload_series_skew(S, axis=None, skipna=True, level=None,
    numeric_only=None):
    yppn__bgd = dict(level=level, numeric_only=numeric_only)
    ihi__bqwp = dict(level=None, numeric_only=None)
    check_unsupported_args('Series.skew', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error('Series.skew(): axis argument not supported')
    if not is_overload_bool(skipna):
        raise BodoError('Series.skew(): skipna argument must be a boolean')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.skew()')

    def impl(S, axis=None, skipna=True, level=None, numeric_only=None):
        A = bodo.hiframes.pd_series_ext.get_series_data(S)
        numba.parfors.parfor.init_prange()
        niact__qky = 0.0
        spvg__djsn = 0.0
        ldfbh__wks = 0.0
        qtx__jin = 0
        for ynjr__fnfp in numba.parfors.parfor.internal_prange(len(A)):
            xakhd__wjd = 0.0
            cgq__gkc = 0
            if not bodo.libs.array_kernels.isna(A, ynjr__fnfp) or not skipna:
                xakhd__wjd = np.float64(A[ynjr__fnfp])
                cgq__gkc = 1
            niact__qky += xakhd__wjd
            spvg__djsn += xakhd__wjd ** 2
            ldfbh__wks += xakhd__wjd ** 3
            qtx__jin += cgq__gkc
        lzxbl__uvwtt = bodo.hiframes.series_kernels.compute_skew(niact__qky,
            spvg__djsn, ldfbh__wks, qtx__jin)
        return lzxbl__uvwtt
    return impl


@overload_method(SeriesType, 'var', inline='always', no_unliteral=True)
def overload_series_var(S, axis=None, skipna=True, level=None, ddof=1,
    numeric_only=None):
    yppn__bgd = dict(level=level, numeric_only=numeric_only)
    ihi__bqwp = dict(level=None, numeric_only=None)
    check_unsupported_args('Series.var', yppn__bgd, ihi__bqwp, package_name
        ='pandas', module_name='Series')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error('Series.var(): axis argument not supported')
    if not is_overload_bool(skipna):
        raise BodoError('Series.var(): skipna argument must be a boolean')
    if not is_overload_int(ddof):
        raise BodoError('Series.var(): ddof argument must be an integer')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S, 'Series.var()'
        )

    def impl(S, axis=None, skipna=True, level=None, ddof=1, numeric_only=None):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        return bodo.libs.array_ops.array_op_var(arr, skipna, ddof)
    return impl


@overload_method(SeriesType, 'std', inline='always', no_unliteral=True)
def overload_series_std(S, axis=None, skipna=True, level=None, ddof=1,
    numeric_only=None):
    yppn__bgd = dict(level=level, numeric_only=numeric_only)
    ihi__bqwp = dict(level=None, numeric_only=None)
    check_unsupported_args('Series.std', yppn__bgd, ihi__bqwp, package_name
        ='pandas', module_name='Series')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error('Series.std(): axis argument not supported')
    if not is_overload_bool(skipna):
        raise BodoError('Series.std(): skipna argument must be a boolean')
    if not is_overload_int(ddof):
        raise BodoError('Series.std(): ddof argument must be an integer')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S, 'Series.std()'
        )

    def impl(S, axis=None, skipna=True, level=None, ddof=1, numeric_only=None):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        return bodo.libs.array_ops.array_op_std(arr, skipna, ddof)
    return impl


@overload_method(SeriesType, 'dot', inline='always', no_unliteral=True)
def overload_series_dot(S, other):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S, 'Series.dot()'
        )
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(other,
        'Series.dot()')

    def impl(S, other):
        xvjzb__hhi = bodo.hiframes.pd_series_ext.get_series_data(S)
        hug__lia = bodo.hiframes.pd_series_ext.get_series_data(other)
        numba.parfors.parfor.init_prange()
        ronkx__jcm = 0
        for ynjr__fnfp in numba.parfors.parfor.internal_prange(len(xvjzb__hhi)
            ):
            yux__ucgd = xvjzb__hhi[ynjr__fnfp]
            hrgim__qjkwj = hug__lia[ynjr__fnfp]
            ronkx__jcm += yux__ucgd * hrgim__qjkwj
        return ronkx__jcm
    return impl


@overload_method(SeriesType, 'cumsum', inline='always', no_unliteral=True)
def overload_series_cumsum(S, axis=None, skipna=True):
    yppn__bgd = dict(skipna=skipna)
    ihi__bqwp = dict(skipna=True)
    check_unsupported_args('Series.cumsum', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error('Series.cumsum(): axis argument not supported')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.cumsum()')

    def impl(S, axis=None, skipna=True):
        A = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        return bodo.hiframes.pd_series_ext.init_series(bodo.libs.
            array_kernels.accum_func(A, 'cumsum'), index, name)
    return impl


@overload_method(SeriesType, 'cumprod', inline='always', no_unliteral=True)
def overload_series_cumprod(S, axis=None, skipna=True):
    yppn__bgd = dict(skipna=skipna)
    ihi__bqwp = dict(skipna=True)
    check_unsupported_args('Series.cumprod', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error('Series.cumprod(): axis argument not supported')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.cumprod()')

    def impl(S, axis=None, skipna=True):
        A = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        return bodo.hiframes.pd_series_ext.init_series(bodo.libs.
            array_kernels.accum_func(A, 'cumprod'), index, name)
    return impl


@overload_method(SeriesType, 'cummin', inline='always', no_unliteral=True)
def overload_series_cummin(S, axis=None, skipna=True):
    yppn__bgd = dict(skipna=skipna)
    ihi__bqwp = dict(skipna=True)
    check_unsupported_args('Series.cummin', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error('Series.cummin(): axis argument not supported')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.cummin()')

    def impl(S, axis=None, skipna=True):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        return bodo.hiframes.pd_series_ext.init_series(bodo.libs.
            array_kernels.accum_func(arr, 'cummin'), index, name)
    return impl


@overload_method(SeriesType, 'cummax', inline='always', no_unliteral=True)
def overload_series_cummax(S, axis=None, skipna=True):
    yppn__bgd = dict(skipna=skipna)
    ihi__bqwp = dict(skipna=True)
    check_unsupported_args('Series.cummax', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error('Series.cummax(): axis argument not supported')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.cummax()')

    def impl(S, axis=None, skipna=True):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        return bodo.hiframes.pd_series_ext.init_series(bodo.libs.
            array_kernels.accum_func(arr, 'cummax'), index, name)
    return impl


@overload_method(SeriesType, 'rename', inline='always', no_unliteral=True)
def overload_series_rename(S, index=None, axis=None, copy=True, inplace=
    False, level=None, errors='ignore'):
    if not (index == bodo.string_type or isinstance(index, types.StringLiteral)
        ):
        raise BodoError("Series.rename() 'index' can only be a string")
    yppn__bgd = dict(copy=copy, inplace=inplace, level=level, errors=errors)
    ihi__bqwp = dict(copy=True, inplace=False, level=None, errors='ignore')
    check_unsupported_args('Series.rename', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')

    def impl(S, index=None, axis=None, copy=True, inplace=False, level=None,
        errors='ignore'):
        A = bodo.hiframes.pd_series_ext.get_series_data(S)
        nzh__aqul = bodo.hiframes.pd_series_ext.get_series_index(S)
        return bodo.hiframes.pd_series_ext.init_series(A, nzh__aqul, index)
    return impl


@overload_method(SeriesType, 'rename_axis', inline='always', no_unliteral=True)
def overload_series_rename_axis(S, mapper=None, index=None, columns=None,
    axis=None, copy=True, inplace=False):
    yppn__bgd = dict(index=index, columns=columns, axis=axis, copy=copy,
        inplace=inplace)
    ihi__bqwp = dict(index=None, columns=None, axis=None, copy=True,
        inplace=False)
    check_unsupported_args('Series.rename_axis', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if is_overload_none(mapper) or not is_scalar_type(mapper):
        raise BodoError(
            "Series.rename_axis(): 'mapper' is required and must be a scalar type."
            )

    def impl(S, mapper=None, index=None, columns=None, axis=None, copy=True,
        inplace=False):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        index = index.rename(mapper)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        return bodo.hiframes.pd_series_ext.init_series(arr, index, name)
    return impl


@overload_method(SeriesType, 'abs', inline='always', no_unliteral=True)
def overload_series_abs(S):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S, 'Series.abs()'
        )
    vrmns__mvrx = S.data

    def impl(S):
        A = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        numba.parfors.parfor.init_prange()
        n = len(A)
        wzmu__etpuf = bodo.utils.utils.alloc_type(n, vrmns__mvrx, (-1,))
        for ynjr__fnfp in numba.parfors.parfor.internal_prange(n):
            if bodo.libs.array_kernels.isna(A, ynjr__fnfp):
                bodo.libs.array_kernels.setna(wzmu__etpuf, ynjr__fnfp)
                continue
            wzmu__etpuf[ynjr__fnfp] = np.abs(A[ynjr__fnfp])
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf, index, name
            )
    return impl


@overload_method(SeriesType, 'count', no_unliteral=True)
def overload_series_count(S, level=None):
    yppn__bgd = dict(level=level)
    ihi__bqwp = dict(level=None)
    check_unsupported_args('Series.count', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')

    def impl(S, level=None):
        A = bodo.hiframes.pd_series_ext.get_series_data(S)
        return bodo.libs.array_ops.array_op_count(A)
    return impl


@overload_method(SeriesType, 'corr', inline='always', no_unliteral=True)
def overload_series_corr(S, other, method='pearson', min_periods=None):
    yppn__bgd = dict(method=method, min_periods=min_periods)
    ihi__bqwp = dict(method='pearson', min_periods=None)
    check_unsupported_args('Series.corr', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.corr()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(other,
        'Series.corr()')

    def impl(S, other, method='pearson', min_periods=None):
        n = S.count()
        xoa__jnsj = S.sum()
        gnoqz__qwynd = other.sum()
        a = n * (S * other).sum() - xoa__jnsj * gnoqz__qwynd
        sxdcq__xazx = n * (S ** 2).sum() - xoa__jnsj ** 2
        zoxn__bkj = n * (other ** 2).sum() - gnoqz__qwynd ** 2
        return a / np.sqrt(sxdcq__xazx * zoxn__bkj)
    return impl


@overload_method(SeriesType, 'cov', inline='always', no_unliteral=True)
def overload_series_cov(S, other, min_periods=None, ddof=1):
    yppn__bgd = dict(min_periods=min_periods)
    ihi__bqwp = dict(min_periods=None)
    check_unsupported_args('Series.cov', yppn__bgd, ihi__bqwp, package_name
        ='pandas', module_name='Series')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S, 'Series.cov()'
        )
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(other,
        'Series.cov()')

    def impl(S, other, min_periods=None, ddof=1):
        xoa__jnsj = S.mean()
        gnoqz__qwynd = other.mean()
        dpr__lyx = ((S - xoa__jnsj) * (other - gnoqz__qwynd)).sum()
        N = np.float64(S.count() - ddof)
        nonzero_len = S.count() * other.count()
        return _series_cov_helper(dpr__lyx, N, nonzero_len)
    return impl


def _series_cov_helper(sum_val, N, nonzero_len):
    return


@overload(_series_cov_helper, no_unliteral=True)
def _overload_series_cov_helper(sum_val, N, nonzero_len):

    def impl(sum_val, N, nonzero_len):
        if not nonzero_len:
            return np.nan
        if N <= 0.0:
            xsp__rpp = np.sign(sum_val)
            return np.inf * xsp__rpp
        return sum_val / N
    return impl


@overload_method(SeriesType, 'min', inline='always', no_unliteral=True)
def overload_series_min(S, axis=None, skipna=None, level=None, numeric_only
    =None):
    yppn__bgd = dict(skipna=skipna, level=level, numeric_only=numeric_only)
    ihi__bqwp = dict(skipna=None, level=None, numeric_only=None)
    check_unsupported_args('Series.min', yppn__bgd, ihi__bqwp, package_name
        ='pandas', module_name='Series')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error('Series.min(): axis argument not supported')
    if isinstance(S.dtype, PDCategoricalDtype):
        if not S.dtype.ordered:
            raise BodoError(
                'Series.min(): only ordered categoricals are possible')
    if isinstance(S.dtype, bodo.libs.pd_datetime_arr_ext.PandasDatetimeTZDtype
        ):
        hox__vtiq = S.dtype.tz

        def impl(S, axis=None, skipna=None, level=None, numeric_only=None):
            arr = unwrap_tz_array(bodo.hiframes.pd_series_ext.
                get_series_data(S))
            min_val = bodo.libs.array_ops.array_op_min(arr)
            return convert_val_to_timestamp(min_val.value, tz=hox__vtiq)
        return impl

    def impl(S, axis=None, skipna=None, level=None, numeric_only=None):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        return bodo.libs.array_ops.array_op_min(arr)
    return impl


@overload(max, no_unliteral=True)
def overload_series_builtins_max(S):
    if isinstance(S, SeriesType):

        def impl(S):
            return S.max()
        return impl


@overload(min, no_unliteral=True)
def overload_series_builtins_min(S):
    if isinstance(S, SeriesType):

        def impl(S):
            return S.min()
        return impl


@overload(sum, no_unliteral=True)
def overload_series_builtins_sum(S):
    if isinstance(S, SeriesType):

        def impl(S):
            return S.sum()
        return impl


@overload(np.prod, inline='always', no_unliteral=True)
def overload_series_np_prod(S):
    if isinstance(S, SeriesType):

        def impl(S):
            return S.prod()
        return impl


@overload_method(SeriesType, 'max', inline='always', no_unliteral=True)
def overload_series_max(S, axis=None, skipna=None, level=None, numeric_only
    =None):
    yppn__bgd = dict(skipna=skipna, level=level, numeric_only=numeric_only)
    ihi__bqwp = dict(skipna=None, level=None, numeric_only=None)
    check_unsupported_args('Series.max', yppn__bgd, ihi__bqwp, package_name
        ='pandas', module_name='Series')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error('Series.max(): axis argument not supported')
    if isinstance(S.dtype, PDCategoricalDtype):
        if not S.dtype.ordered:
            raise BodoError(
                'Series.max(): only ordered categoricals are possible')
    if isinstance(S.dtype, bodo.libs.pd_datetime_arr_ext.PandasDatetimeTZDtype
        ):
        hox__vtiq = S.dtype.tz

        def impl(S, axis=None, skipna=None, level=None, numeric_only=None):
            arr = unwrap_tz_array(bodo.hiframes.pd_series_ext.
                get_series_data(S))
            max_val = bodo.libs.array_ops.array_op_max(arr)
            return convert_val_to_timestamp(max_val.value, tz=hox__vtiq)
        return impl

    def impl(S, axis=None, skipna=None, level=None, numeric_only=None):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        return bodo.libs.array_ops.array_op_max(arr)
    return impl


@overload_method(SeriesType, 'idxmin', inline='always', no_unliteral=True)
def overload_series_idxmin(S, axis=0, skipna=True):
    yppn__bgd = dict(axis=axis, skipna=skipna)
    ihi__bqwp = dict(axis=0, skipna=True)
    check_unsupported_args('Series.idxmin', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.idxmin()')
    if not (S.dtype == types.none or bodo.utils.utils.is_np_array_typ(S.
        data) and (S.dtype in [bodo.datetime64ns, bodo.timedelta64ns] or
        isinstance(S.dtype, (types.Number, types.Boolean))) or isinstance(S
        .data, (bodo.IntegerArrayType, bodo.FloatingArrayType, bodo.
        CategoricalArrayType)) or S.data in [bodo.boolean_array, bodo.
        datetime_date_array_type]):
        raise BodoError(
            f'Series.idxmin() only supported for numeric array types. Array type: {S.data} not supported.'
            )
    if isinstance(S.data, bodo.CategoricalArrayType) and not S.dtype.ordered:
        raise BodoError(
            'Series.idxmin(): only ordered categoricals are possible')

    def impl(S, axis=0, skipna=True):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        return bodo.libs.array_ops.array_op_idxmin(arr, index)
    return impl


@overload_method(SeriesType, 'idxmax', inline='always', no_unliteral=True)
def overload_series_idxmax(S, axis=0, skipna=True):
    yppn__bgd = dict(axis=axis, skipna=skipna)
    ihi__bqwp = dict(axis=0, skipna=True)
    check_unsupported_args('Series.idxmax', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.idxmax()')
    if not (S.dtype == types.none or bodo.utils.utils.is_np_array_typ(S.
        data) and (S.dtype in [bodo.datetime64ns, bodo.timedelta64ns] or
        isinstance(S.dtype, (types.Number, types.Boolean))) or isinstance(S
        .data, (bodo.IntegerArrayType, bodo.FloatingArrayType, bodo.
        CategoricalArrayType)) or S.data in [bodo.boolean_array, bodo.
        datetime_date_array_type]):
        raise BodoError(
            f'Series.idxmax() only supported for numeric array types. Array type: {S.data} not supported.'
            )
    if isinstance(S.data, bodo.CategoricalArrayType) and not S.dtype.ordered:
        raise BodoError(
            'Series.idxmax(): only ordered categoricals are possible')

    def impl(S, axis=0, skipna=True):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        return bodo.libs.array_ops.array_op_idxmax(arr, index)
    return impl


@overload_method(SeriesType, 'infer_objects', inline='always')
def overload_series_infer_objects(S):
    return lambda S: S.copy()


@overload_attribute(SeriesType, 'is_monotonic', inline='always')
@overload_attribute(SeriesType, 'is_monotonic_increasing', inline='always')
def overload_series_is_monotonic_increasing(S):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.is_monotonic_increasing')
    return lambda S: bodo.libs.array_kernels.series_monotonicity(bodo.
        hiframes.pd_series_ext.get_series_data(S), 1)


@overload_attribute(SeriesType, 'is_monotonic_decreasing', inline='always')
def overload_series_is_monotonic_decreasing(S):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.is_monotonic_decreasing')
    return lambda S: bodo.libs.array_kernels.series_monotonicity(bodo.
        hiframes.pd_series_ext.get_series_data(S), 2)


@overload_attribute(SeriesType, 'nbytes', inline='always')
def overload_series_nbytes(S):
    return lambda S: bodo.hiframes.pd_series_ext.get_series_data(S).nbytes


@overload_method(SeriesType, 'autocorr', inline='always', no_unliteral=True)
def overload_series_autocorr(S, lag=1):
    return lambda S, lag=1: bodo.libs.array_kernels.autocorr(bodo.hiframes.
        pd_series_ext.get_series_data(S), lag)


@overload_method(SeriesType, 'median', inline='always', no_unliteral=True)
def overload_series_median(S, axis=None, skipna=True, level=None,
    numeric_only=None):
    yppn__bgd = dict(level=level, numeric_only=numeric_only)
    ihi__bqwp = dict(level=None, numeric_only=None)
    check_unsupported_args('Series.median', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error('Series.median(): axis argument not supported')
    if not is_overload_bool(skipna):
        raise BodoError('Series.median(): skipna argument must be a boolean')
    return (lambda S, axis=None, skipna=True, level=None, numeric_only=None:
        bodo.libs.array_ops.array_op_median(bodo.hiframes.pd_series_ext.
        get_series_data(S), skipna))


def overload_series_head(S, n=5):

    def impl(S, n=5):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        gfg__dpzx = arr[:n]
        lkr__xoner = index[:n]
        return bodo.hiframes.pd_series_ext.init_series(gfg__dpzx,
            lkr__xoner, name)
    return impl


@lower_builtin('series.head', SeriesType, types.Integer)
@lower_builtin('series.head', SeriesType, types.Omitted)
def series_head_lower(context, builder, sig, args):
    impl = overload_series_head(*sig.args)
    return context.compile_internal(builder, impl, sig, args)


@numba.extending.register_jitable
def tail_slice(k, n):
    if n == 0:
        return k
    return -n


@overload_method(SeriesType, 'tail', inline='always', no_unliteral=True)
def overload_series_tail(S, n=5):
    if not is_overload_int(n):
        raise BodoError("Series.tail(): 'n' must be an Integer")

    def impl(S, n=5):
        almdo__nieh = tail_slice(len(S), n)
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        gfg__dpzx = arr[almdo__nieh:]
        lkr__xoner = index[almdo__nieh:]
        return bodo.hiframes.pd_series_ext.init_series(gfg__dpzx,
            lkr__xoner, name)
    return impl


@overload_method(SeriesType, 'first', inline='always', no_unliteral=True)
def overload_series_first(S, offset):
    awz__wimr = (types.unicode_type, bodo.month_begin_type, bodo.
        month_end_type, bodo.week_type, bodo.date_offset_type)
    if types.unliteral(offset) not in awz__wimr:
        raise BodoError(
            "Series.first(): 'offset' must be a string or a DateOffset")
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.first()')

    def impl(S, offset):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        if len(index):
            obecl__cuno = index[0]
            rtxnb__rdl = (bodo.libs.array_kernels.
                get_valid_entries_from_date_offset(index, offset,
                obecl__cuno, False))
        else:
            rtxnb__rdl = 0
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        gfg__dpzx = arr[:rtxnb__rdl]
        lkr__xoner = index[:rtxnb__rdl]
        return bodo.hiframes.pd_series_ext.init_series(gfg__dpzx,
            lkr__xoner, name)
    return impl


@overload_method(SeriesType, 'last', inline='always', no_unliteral=True)
def overload_series_last(S, offset):
    awz__wimr = (types.unicode_type, bodo.month_begin_type, bodo.
        month_end_type, bodo.week_type, bodo.date_offset_type)
    if types.unliteral(offset) not in awz__wimr:
        raise BodoError(
            "Series.last(): 'offset' must be a string or a DateOffset")
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.last()')

    def impl(S, offset):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        if len(index):
            nmb__ugo = index[-1]
            rtxnb__rdl = (bodo.libs.array_kernels.
                get_valid_entries_from_date_offset(index, offset, nmb__ugo,
                True))
        else:
            rtxnb__rdl = 0
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        gfg__dpzx = arr[len(arr) - rtxnb__rdl:]
        lkr__xoner = index[len(arr) - rtxnb__rdl:]
        return bodo.hiframes.pd_series_ext.init_series(gfg__dpzx,
            lkr__xoner, name)
    return impl


@overload_method(SeriesType, 'first_valid_index', inline='always',
    no_unliteral=True)
def overload_series_first_valid_index(S):

    def impl(S):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        cieta__wodph = bodo.utils.conversion.index_to_array(index)
        adtp__lwg, czgum__owkg = (bodo.libs.array_kernels.
            first_last_valid_index(arr, cieta__wodph))
        return czgum__owkg if adtp__lwg else None
    return impl


@overload_method(SeriesType, 'last_valid_index', inline='always',
    no_unliteral=True)
def overload_series_last_valid_index(S):

    def impl(S):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        cieta__wodph = bodo.utils.conversion.index_to_array(index)
        adtp__lwg, czgum__owkg = (bodo.libs.array_kernels.
            first_last_valid_index(arr, cieta__wodph, False))
        return czgum__owkg if adtp__lwg else None
    return impl


@overload_method(SeriesType, 'nlargest', inline='always', no_unliteral=True)
def overload_series_nlargest(S, n=5, keep='first'):
    yppn__bgd = dict(keep=keep)
    ihi__bqwp = dict(keep='first')
    check_unsupported_args('Series.nlargest', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not is_overload_int(n):
        raise BodoError('Series.nlargest(): n argument must be an integer')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.nlargest()')

    def impl(S, n=5, keep='first'):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        cieta__wodph = bodo.utils.conversion.coerce_to_ndarray(index)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        wzmu__etpuf, gtxd__ksoi = bodo.libs.array_kernels.nlargest(arr,
            cieta__wodph, n, True, bodo.hiframes.series_kernels.gt_f)
        qdyl__gas = bodo.utils.conversion.convert_to_index(gtxd__ksoi)
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
            qdyl__gas, name)
    return impl


@overload_method(SeriesType, 'nsmallest', inline='always', no_unliteral=True)
def overload_series_nsmallest(S, n=5, keep='first'):
    yppn__bgd = dict(keep=keep)
    ihi__bqwp = dict(keep='first')
    check_unsupported_args('Series.nsmallest', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not is_overload_int(n):
        raise BodoError('Series.nsmallest(): n argument must be an integer')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.nsmallest()')

    def impl(S, n=5, keep='first'):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        cieta__wodph = bodo.utils.conversion.coerce_to_ndarray(index)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        wzmu__etpuf, gtxd__ksoi = bodo.libs.array_kernels.nlargest(arr,
            cieta__wodph, n, False, bodo.hiframes.series_kernels.lt_f)
        qdyl__gas = bodo.utils.conversion.convert_to_index(gtxd__ksoi)
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
            qdyl__gas, name)
    return impl


@overload_method(SeriesType, 'notnull', inline='always', no_unliteral=True)
@overload_method(SeriesType, 'notna', inline='always', no_unliteral=True)
def overload_series_notna(S):
    return lambda S: S.isna() == False


@overload_method(SeriesType, 'astype', inline='always', no_unliteral=True)
@overload_method(HeterogeneousSeriesType, 'astype', inline='always',
    no_unliteral=True)
def overload_series_astype(S, dtype, copy=True, errors='raise',
    _bodo_nan_to_str=True):
    yppn__bgd = dict(errors=errors)
    ihi__bqwp = dict(errors='raise')
    check_unsupported_args('Series.astype', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if dtype == types.unicode_type:
        raise_bodo_error(
            "Series.astype(): 'dtype' when passed as string must be a constant value"
            )
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.astype()')

    def impl(S, dtype, copy=True, errors='raise', _bodo_nan_to_str=True):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        wzmu__etpuf = bodo.utils.conversion.fix_arr_dtype(arr, dtype, copy,
            nan_to_str=_bodo_nan_to_str, from_series=True)
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf, index, name
            )
    return impl


@overload_method(SeriesType, 'take', inline='always', no_unliteral=True)
def overload_series_take(S, indices, axis=0, is_copy=True):
    yppn__bgd = dict(axis=axis, is_copy=is_copy)
    ihi__bqwp = dict(axis=0, is_copy=True)
    check_unsupported_args('Series.take', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not (is_iterable_type(indices) and isinstance(indices.dtype, types.
        Integer)):
        raise BodoError(
            f"Series.take() 'indices' must be an array-like and contain integers. Found type {indices}."
            )

    def impl(S, indices, axis=0, is_copy=True):
        vuuil__qjn = bodo.utils.conversion.coerce_to_ndarray(indices)
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        return bodo.hiframes.pd_series_ext.init_series(arr[vuuil__qjn],
            index[vuuil__qjn], name)
    return impl


@overload_method(SeriesType, 'argsort', inline='always', no_unliteral=True)
def overload_series_argsort(S, axis=0, kind='quicksort', order=None):
    yppn__bgd = dict(axis=axis, kind=kind, order=order)
    ihi__bqwp = dict(axis=0, kind='quicksort', order=None)
    check_unsupported_args('Series.argsort', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')

    def impl(S, axis=0, kind='quicksort', order=None):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        n = len(arr)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        egxx__vydoc = S.notna().values
        if not egxx__vydoc.all():
            wzmu__etpuf = np.full(n, -1, np.int64)
            wzmu__etpuf[egxx__vydoc] = argsort(arr[egxx__vydoc])
        else:
            wzmu__etpuf = argsort(arr)
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf, index, name
            )
    return impl


@overload_method(SeriesType, 'rank', inline='always', no_unliteral=True)
def overload_series_rank(S, axis=0, method='average', numeric_only=None,
    na_option='keep', ascending=True, pct=False):
    yppn__bgd = dict(axis=axis, numeric_only=numeric_only)
    ihi__bqwp = dict(axis=0, numeric_only=None)
    check_unsupported_args('Series.rank', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not is_overload_constant_str(method):
        raise BodoError(
            "Series.rank(): 'method' argument must be a constant string")
    if not is_overload_constant_str(na_option):
        raise BodoError(
            "Series.rank(): 'na_option' argument must be a constant string")

    def impl(S, axis=0, method='average', numeric_only=None, na_option=
        'keep', ascending=True, pct=False):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        wzmu__etpuf = bodo.libs.array_kernels.rank(arr, method=method,
            na_option=na_option, ascending=ascending, pct=pct)
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf, index, name
            )
    return impl


@overload_method(SeriesType, 'sort_index', inline='always', no_unliteral=True)
def overload_series_sort_index(S, axis=0, level=None, ascending=True,
    inplace=False, kind='quicksort', na_position='last', sort_remaining=
    True, ignore_index=False, key=None):
    yppn__bgd = dict(axis=axis, level=level, inplace=inplace, kind=kind,
        sort_remaining=sort_remaining, ignore_index=ignore_index, key=key)
    ihi__bqwp = dict(axis=0, level=None, inplace=False, kind='quicksort',
        sort_remaining=True, ignore_index=False, key=None)
    check_unsupported_args('Series.sort_index', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not is_overload_bool(ascending):
        raise BodoError(
            "Series.sort_index(): 'ascending' parameter must be of type bool")
    if not is_overload_constant_str(na_position) or get_overload_const_str(
        na_position) not in ('first', 'last'):
        raise_bodo_error(
            "Series.sort_index(): 'na_position' should either be 'first' or 'last'"
            )
    cnahc__dxymg = ColNamesMetaType(('$_bodo_col3_',))

    def impl(S, axis=0, level=None, ascending=True, inplace=False, kind=
        'quicksort', na_position='last', sort_remaining=True, ignore_index=
        False, key=None):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        pkeu__mmvcj = bodo.hiframes.pd_dataframe_ext.init_dataframe((arr,),
            index, cnahc__dxymg)
        wukxv__tfchw = pkeu__mmvcj.sort_index(ascending=ascending, inplace=
            inplace, na_position=na_position)
        wzmu__etpuf = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(
            wukxv__tfchw, 0)
        qdyl__gas = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(
            wukxv__tfchw)
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
            qdyl__gas, name)
    return impl


@overload_method(SeriesType, 'sort_values', inline='always', no_unliteral=True)
def overload_series_sort_values(S, axis=0, ascending=True, inplace=False,
    kind='quicksort', na_position='last', ignore_index=False, key=None):
    yppn__bgd = dict(axis=axis, inplace=inplace, kind=kind, ignore_index=
        ignore_index, key=key)
    ihi__bqwp = dict(axis=0, inplace=False, kind='quicksort', ignore_index=
        False, key=None)
    check_unsupported_args('Series.sort_values', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not is_overload_bool(ascending):
        raise BodoError(
            "Series.sort_values(): 'ascending' parameter must be of type bool")
    if not is_overload_constant_str(na_position) or get_overload_const_str(
        na_position) not in ('first', 'last'):
        raise_bodo_error(
            "Series.sort_values(): 'na_position' should either be 'first' or 'last'"
            )
    gvzfb__sulwh = ColNamesMetaType(('$_bodo_col_',))

    def impl(S, axis=0, ascending=True, inplace=False, kind='quicksort',
        na_position='last', ignore_index=False, key=None):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        pkeu__mmvcj = bodo.hiframes.pd_dataframe_ext.init_dataframe((arr,),
            index, gvzfb__sulwh)
        wukxv__tfchw = pkeu__mmvcj.sort_values(['$_bodo_col_'], ascending=
            ascending, inplace=inplace, na_position=na_position)
        wzmu__etpuf = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(
            wukxv__tfchw, 0)
        qdyl__gas = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(
            wukxv__tfchw)
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
            qdyl__gas, name)
    return impl


def get_bin_inds(bins, arr):
    return arr


@overload(get_bin_inds, inline='always', no_unliteral=True)
def overload_get_bin_inds(bins, arr, is_nullable=True, include_lowest=True):
    assert is_overload_constant_bool(is_nullable)
    jind__lnxov = is_overload_true(is_nullable)
    deqe__ahp = 'def impl(bins, arr, is_nullable=True, include_lowest=True):\n'
    deqe__ahp += '  numba.parfors.parfor.init_prange()\n'
    deqe__ahp += '  n = len(arr)\n'
    if jind__lnxov:
        deqe__ahp += (
            '  out_arr = bodo.libs.int_arr_ext.alloc_int_array(n, np.int64)\n')
    else:
        deqe__ahp += '  out_arr = np.empty(n, np.int64)\n'
    deqe__ahp += '  for i in numba.parfors.parfor.internal_prange(n):\n'
    deqe__ahp += '    if bodo.libs.array_kernels.isna(arr, i):\n'
    if jind__lnxov:
        deqe__ahp += '      bodo.libs.array_kernels.setna(out_arr, i)\n'
    else:
        deqe__ahp += '      out_arr[i] = -1\n'
    deqe__ahp += '      continue\n'
    deqe__ahp += '    val = arr[i]\n'
    deqe__ahp += '    if include_lowest and val == bins[0]:\n'
    deqe__ahp += '      ind = 1\n'
    deqe__ahp += '    else:\n'
    deqe__ahp += '      ind = np.searchsorted(bins, val)\n'
    deqe__ahp += '    if ind == 0 or ind == len(bins):\n'
    if jind__lnxov:
        deqe__ahp += '      bodo.libs.array_kernels.setna(out_arr, i)\n'
    else:
        deqe__ahp += '      out_arr[i] = -1\n'
    deqe__ahp += '    else:\n'
    deqe__ahp += '      out_arr[i] = ind - 1\n'
    deqe__ahp += '  return out_arr\n'
    nii__tveq = {}
    exec(deqe__ahp, {'bodo': bodo, 'np': np, 'numba': numba}, nii__tveq)
    impl = nii__tveq['impl']
    return impl


@register_jitable
def _round_frac(x, precision: int):
    if not np.isfinite(x) or x == 0:
        return x
    else:
        algy__wdmlz, brp__znuqx = np.divmod(x, 1)
        if algy__wdmlz == 0:
            ioq__ouqvk = -int(np.floor(np.log10(abs(brp__znuqx)))
                ) - 1 + precision
        else:
            ioq__ouqvk = precision
        return np.around(x, ioq__ouqvk)


@register_jitable
def _infer_precision(base_precision: int, bins) ->int:
    for precision in range(base_precision, 20):
        vij__kyv = np.array([_round_frac(b, precision) for b in bins])
        if len(np.unique(vij__kyv)) == len(bins):
            return precision
    return base_precision


def get_bin_labels(bins):
    pass


@overload(get_bin_labels, no_unliteral=True)
def overload_get_bin_labels(bins, right=True, include_lowest=True):
    dtype = np.float64 if isinstance(bins.dtype, types.Integer) else bins.dtype
    if dtype == bodo.datetime64ns:
        ylf__xod = bodo.timedelta64ns(1)

        def impl_dt64(bins, right=True, include_lowest=True):
            sahn__igo = bins.copy()
            if right and include_lowest:
                sahn__igo[0] = sahn__igo[0] - ylf__xod
            jstyq__cpm = bodo.libs.interval_arr_ext.init_interval_array(
                sahn__igo[:-1], sahn__igo[1:])
            return bodo.hiframes.pd_index_ext.init_interval_index(jstyq__cpm,
                None)
        return impl_dt64

    def impl(bins, right=True, include_lowest=True):
        base_precision = 3
        precision = _infer_precision(base_precision, bins)
        sahn__igo = np.array([_round_frac(b, precision) for b in bins],
            dtype=dtype)
        if right and include_lowest:
            sahn__igo[0] = sahn__igo[0] - 10.0 ** -precision
        jstyq__cpm = bodo.libs.interval_arr_ext.init_interval_array(sahn__igo
            [:-1], sahn__igo[1:])
        return bodo.hiframes.pd_index_ext.init_interval_index(jstyq__cpm, None)
    return impl


def get_output_bin_counts(count_series, nbins):
    pass


@overload(get_output_bin_counts, no_unliteral=True)
def overload_get_output_bin_counts(count_series, nbins):

    def impl(count_series, nbins):
        ksxm__wyl = bodo.hiframes.pd_series_ext.get_series_data(count_series)
        xbyr__ehffp = bodo.utils.conversion.index_to_array(bodo.hiframes.
            pd_series_ext.get_series_index(count_series))
        wzmu__etpuf = np.zeros(nbins, np.int64)
        for ynjr__fnfp in range(len(ksxm__wyl)):
            wzmu__etpuf[xbyr__ehffp[ynjr__fnfp]] = ksxm__wyl[ynjr__fnfp]
        return wzmu__etpuf
    return impl


def compute_bins(nbins, min_val, max_val):
    pass


@overload(compute_bins, no_unliteral=True)
def overload_compute_bins(nbins, min_val, max_val, right=True):

    def impl(nbins, min_val, max_val, right=True):
        if nbins < 1:
            raise ValueError('`bins` should be a positive integer.')
        min_val = min_val + 0.0
        max_val = max_val + 0.0
        if np.isinf(min_val) or np.isinf(max_val):
            raise ValueError(
                'cannot specify integer `bins` when input data contains infinity'
                )
        elif min_val == max_val:
            min_val -= 0.001 * abs(min_val) if min_val != 0 else 0.001
            max_val += 0.001 * abs(max_val) if max_val != 0 else 0.001
            bins = np.linspace(min_val, max_val, nbins + 1, endpoint=True)
        else:
            bins = np.linspace(min_val, max_val, nbins + 1, endpoint=True)
            vbovk__dsoaj = (max_val - min_val) * 0.001
            if right:
                bins[0] -= vbovk__dsoaj
            else:
                bins[-1] += vbovk__dsoaj
        return bins
    return impl


@overload_method(SeriesType, 'value_counts', inline='always', no_unliteral=True
    )
def overload_series_value_counts(S, normalize=False, sort=True, ascending=
    False, bins=None, dropna=True, _index_name=None):
    yppn__bgd = dict(dropna=dropna)
    ihi__bqwp = dict(dropna=True)
    check_unsupported_args('Series.value_counts', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not is_overload_constant_bool(normalize):
        raise_bodo_error(
            'Series.value_counts(): normalize argument must be a constant boolean'
            )
    if not is_overload_constant_bool(sort):
        raise_bodo_error(
            'Series.value_counts(): sort argument must be a constant boolean')
    if not is_overload_bool(ascending):
        raise_bodo_error(
            'Series.value_counts(): ascending argument must be a constant boolean'
            )
    cxkac__ricdr = not is_overload_none(bins)
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.value_counts()')
    deqe__ahp = 'def impl(\n'
    deqe__ahp += '    S,\n'
    deqe__ahp += '    normalize=False,\n'
    deqe__ahp += '    sort=True,\n'
    deqe__ahp += '    ascending=False,\n'
    deqe__ahp += '    bins=None,\n'
    deqe__ahp += '    dropna=True,\n'
    deqe__ahp += (
        '    _index_name=None,  # bodo argument. See groupby.value_counts\n')
    deqe__ahp += '):\n'
    deqe__ahp += '    arr = bodo.hiframes.pd_series_ext.get_series_data(S)\n'
    deqe__ahp += (
        '    index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
    deqe__ahp += '    name = bodo.hiframes.pd_series_ext.get_series_name(S)\n'
    if cxkac__ricdr:
        deqe__ahp += '    right = True\n'
        deqe__ahp += _gen_bins_handling(bins, S.dtype)
        deqe__ahp += '    arr = get_bin_inds(bins, arr)\n'
    deqe__ahp += '    in_df = bodo.hiframes.pd_dataframe_ext.init_dataframe(\n'
    deqe__ahp += (
        '        (arr,), index, __col_name_meta_value_series_value_counts\n')
    deqe__ahp += '    )\n'
    deqe__ahp += "    count_series = in_df.groupby('$_bodo_col2_').size()\n"
    if cxkac__ricdr:
        deqe__ahp += """    count_series = bodo.gatherv(count_series, allgather=True, warn_if_rep=False)
"""
        deqe__ahp += (
            '    count_arr = get_output_bin_counts(count_series, len(bins) - 1)\n'
            )
        deqe__ahp += '    index = get_bin_labels(bins)\n'
    else:
        deqe__ahp += (
            '    count_arr = bodo.hiframes.pd_series_ext.get_series_data(count_series)\n'
            )
        deqe__ahp += '    ind_arr = bodo.utils.conversion.coerce_to_array(\n'
        deqe__ahp += (
            '        bodo.hiframes.pd_series_ext.get_series_index(count_series)\n'
            )
        deqe__ahp += '    )\n'
        deqe__ahp += """    index = bodo.utils.conversion.index_from_array(ind_arr, name=_index_name)
"""
    deqe__ahp += (
        '    res = bodo.hiframes.pd_series_ext.init_series(count_arr, index, name)\n'
        )
    if is_overload_true(sort):
        deqe__ahp += '    res = res.sort_values(ascending=ascending)\n'
    if is_overload_true(normalize):
        uun__lbbm = 'len(S)' if cxkac__ricdr else 'count_arr.sum()'
        deqe__ahp += f'    res = res / float({uun__lbbm})\n'
    deqe__ahp += '    return res\n'
    nii__tveq = {}
    exec(deqe__ahp, {'bodo': bodo, 'pd': pd, 'np': np, 'get_bin_inds':
        get_bin_inds, 'get_bin_labels': get_bin_labels,
        'get_output_bin_counts': get_output_bin_counts, 'compute_bins':
        compute_bins, '__col_name_meta_value_series_value_counts':
        ColNamesMetaType(('$_bodo_col2_',))}, nii__tveq)
    impl = nii__tveq['impl']
    return impl


def _gen_bins_handling(bins, dtype):
    deqe__ahp = ''
    if isinstance(bins, types.Integer):
        deqe__ahp += '    min_val = bodo.libs.array_ops.array_op_min(arr)\n'
        deqe__ahp += '    max_val = bodo.libs.array_ops.array_op_max(arr)\n'
        if dtype == bodo.datetime64ns:
            deqe__ahp += '    min_val = min_val.value\n'
            deqe__ahp += '    max_val = max_val.value\n'
        deqe__ahp += '    bins = compute_bins(bins, min_val, max_val, right)\n'
        if dtype == bodo.datetime64ns:
            deqe__ahp += (
                "    bins = bins.astype(np.int64).view(np.dtype('datetime64[ns]'))\n"
                )
    else:
        deqe__ahp += (
            '    bins = bodo.utils.conversion.coerce_to_ndarray(bins)\n')
    return deqe__ahp


@overload(pd.cut, inline='always', no_unliteral=True)
def overload_cut(x, bins, right=True, labels=None, retbins=False, precision
    =3, include_lowest=False, duplicates='raise', ordered=True):
    yppn__bgd = dict(right=right, labels=labels, retbins=retbins, precision
        =precision, duplicates=duplicates, ordered=ordered)
    ihi__bqwp = dict(right=True, labels=None, retbins=False, precision=3,
        duplicates='raise', ordered=True)
    check_unsupported_args('pandas.cut', yppn__bgd, ihi__bqwp, package_name
        ='pandas', module_name='General')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(x, 'pandas.cut()'
        )
    deqe__ahp = 'def impl(\n'
    deqe__ahp += '    x,\n'
    deqe__ahp += '    bins,\n'
    deqe__ahp += '    right=True,\n'
    deqe__ahp += '    labels=None,\n'
    deqe__ahp += '    retbins=False,\n'
    deqe__ahp += '    precision=3,\n'
    deqe__ahp += '    include_lowest=False,\n'
    deqe__ahp += "    duplicates='raise',\n"
    deqe__ahp += '    ordered=True\n'
    deqe__ahp += '):\n'
    if isinstance(x, SeriesType):
        deqe__ahp += (
            '    arr = bodo.hiframes.pd_series_ext.get_series_data(x)\n')
        deqe__ahp += (
            '    index = bodo.hiframes.pd_series_ext.get_series_index(x)\n')
        deqe__ahp += (
            '    name = bodo.hiframes.pd_series_ext.get_series_name(x)\n')
    else:
        deqe__ahp += '    arr = bodo.utils.conversion.coerce_to_array(x)\n'
    deqe__ahp += _gen_bins_handling(bins, x.dtype)
    deqe__ahp += '    arr = get_bin_inds(bins, arr, False, include_lowest)\n'
    deqe__ahp += (
        '    label_index = get_bin_labels(bins, right, include_lowest)\n')
    deqe__ahp += """    cat_dtype = bodo.hiframes.pd_categorical_ext.init_cat_dtype(label_index, ordered, None, None)
"""
    deqe__ahp += """    out_arr = bodo.hiframes.pd_categorical_ext.init_categorical_array(arr, cat_dtype)
"""
    if isinstance(x, SeriesType):
        deqe__ahp += (
            '    res = bodo.hiframes.pd_series_ext.init_series(out_arr, index, name)\n'
            )
        deqe__ahp += '    return res\n'
    else:
        deqe__ahp += '    return out_arr\n'
    nii__tveq = {}
    exec(deqe__ahp, {'bodo': bodo, 'pd': pd, 'np': np, 'get_bin_inds':
        get_bin_inds, 'get_bin_labels': get_bin_labels,
        'get_output_bin_counts': get_output_bin_counts, 'compute_bins':
        compute_bins}, nii__tveq)
    impl = nii__tveq['impl']
    return impl


def _get_q_list(q):
    return q


@overload(_get_q_list, no_unliteral=True)
def get_q_list_overload(q):
    if is_overload_int(q):
        return lambda q: np.linspace(0, 1, q + 1)
    return lambda q: q


@overload(pd.unique, inline='always', no_unliteral=True)
def overload_unique(values):
    if not is_series_type(values) and not (bodo.utils.utils.is_array_typ(
        values, False) and values.ndim == 1):
        raise BodoError(
            "pd.unique(): 'values' must be either a Series or a 1-d array")
    if is_series_type(values):

        def impl(values):
            arr = bodo.hiframes.pd_series_ext.get_series_data(values)
            return bodo.allgatherv(bodo.libs.array_kernels.unique(arr), False)
        return impl
    else:
        return lambda values: bodo.allgatherv(bodo.libs.array_kernels.
            unique(values), False)


@overload(pd.qcut, inline='always', no_unliteral=True)
def overload_qcut(x, q, labels=None, retbins=False, precision=3, duplicates
    ='raise'):
    yppn__bgd = dict(labels=labels, retbins=retbins, precision=precision,
        duplicates=duplicates)
    ihi__bqwp = dict(labels=None, retbins=False, precision=3, duplicates=
        'raise')
    check_unsupported_args('pandas.qcut', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='General')
    if not (is_overload_int(q) or is_iterable_type(q)):
        raise BodoError(
            "pd.qcut(): 'q' should be an integer or a list of quantiles")
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(x,
        'pandas.qcut()')

    def impl(x, q, labels=None, retbins=False, precision=3, duplicates='raise'
        ):
        woxg__pyme = _get_q_list(q)
        arr = bodo.utils.conversion.coerce_to_array(x)
        bins = bodo.libs.array_ops.array_op_quantile(arr, woxg__pyme)
        return pd.cut(x, bins, include_lowest=True)
    return impl


@overload_method(SeriesType, 'groupby', inline='always', no_unliteral=True)
def overload_series_groupby(S, by=None, axis=0, level=None, as_index=True,
    sort=True, group_keys=True, squeeze=False, observed=True, dropna=True):
    yppn__bgd = dict(axis=axis, sort=sort, group_keys=group_keys, squeeze=
        squeeze, observed=observed, dropna=dropna)
    ihi__bqwp = dict(axis=0, sort=True, group_keys=True, squeeze=False,
        observed=True, dropna=True)
    check_unsupported_args('Series.groupby', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='GroupBy')
    if not is_overload_true(as_index):
        raise BodoError('as_index=False only valid with DataFrame')
    if is_overload_none(by) and is_overload_none(level):
        raise BodoError("You have to supply one of 'by' and 'level'")
    if not is_overload_none(by) and not is_overload_none(level):
        raise BodoError(
            "Series.groupby(): 'level' argument should be None if 'by' is not None"
            )
    if not is_overload_none(level):
        if not (is_overload_constant_int(level) and get_overload_const_int(
            level) == 0) or isinstance(S.index, bodo.hiframes.
            pd_multi_index_ext.MultiIndexType):
            raise BodoError(
                "Series.groupby(): MultiIndex case or 'level' other than 0 not supported yet"
                )
        cdg__wgxpq = ColNamesMetaType((' ', ''))

        def impl_index(S, by=None, axis=0, level=None, as_index=True, sort=
            True, group_keys=True, squeeze=False, observed=True, dropna=True):
            arr = bodo.hiframes.pd_series_ext.get_series_data(S)
            index = bodo.hiframes.pd_series_ext.get_series_index(S)
            rztib__jpeg = bodo.utils.conversion.coerce_to_array(index)
            pkeu__mmvcj = bodo.hiframes.pd_dataframe_ext.init_dataframe((
                rztib__jpeg, arr), index, cdg__wgxpq)
            return pkeu__mmvcj.groupby(' ')['']
        return impl_index
    cuu__mslvj = by
    if isinstance(by, SeriesType):
        cuu__mslvj = by.data
    if isinstance(cuu__mslvj, DecimalArrayType):
        raise BodoError(
            'Series.groupby(): by argument with decimal type is not supported yet.'
            )
    if isinstance(by, bodo.hiframes.pd_categorical_ext.CategoricalArrayType):
        raise BodoError(
            'Series.groupby(): by argument with categorical type is not supported yet.'
            )
    dkp__nprmq = ColNamesMetaType((' ', ''))

    def impl(S, by=None, axis=0, level=None, as_index=True, sort=True,
        group_keys=True, squeeze=False, observed=True, dropna=True):
        rztib__jpeg = bodo.utils.conversion.coerce_to_array(by)
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        pkeu__mmvcj = bodo.hiframes.pd_dataframe_ext.init_dataframe((
            rztib__jpeg, arr), index, dkp__nprmq)
        return pkeu__mmvcj.groupby(' ')['']
    return impl


@overload_method(SeriesType, 'append', inline='always', no_unliteral=True)
def overload_series_append(S, to_append, ignore_index=False,
    verify_integrity=False):
    yppn__bgd = dict(verify_integrity=verify_integrity)
    ihi__bqwp = dict(verify_integrity=False)
    check_unsupported_args('Series.append', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.append()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(to_append,
        'Series.append()')
    if isinstance(to_append, SeriesType):
        return (lambda S, to_append, ignore_index=False, verify_integrity=
            False: pd.concat((S, to_append), ignore_index=ignore_index,
            verify_integrity=verify_integrity))
    if isinstance(to_append, types.BaseTuple):
        return (lambda S, to_append, ignore_index=False, verify_integrity=
            False: pd.concat((S,) + to_append, ignore_index=ignore_index,
            verify_integrity=verify_integrity))
    return (lambda S, to_append, ignore_index=False, verify_integrity=False:
        pd.concat([S] + to_append, ignore_index=ignore_index,
        verify_integrity=verify_integrity))


@overload_method(SeriesType, 'isin', inline='always', no_unliteral=True)
def overload_series_isin(S, values):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.isin()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(values,
        'Series.isin()')
    if bodo.utils.utils.is_array_typ(values):

        def impl_arr(S, values):
            ekj__ciq = bodo.utils.conversion.coerce_to_array(values)
            A = bodo.hiframes.pd_series_ext.get_series_data(S)
            index = bodo.hiframes.pd_series_ext.get_series_index(S)
            name = bodo.hiframes.pd_series_ext.get_series_name(S)
            n = len(A)
            wzmu__etpuf = np.empty(n, np.bool_)
            bodo.libs.array.array_isin(wzmu__etpuf, A, ekj__ciq, False)
            return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                index, name)
        return impl_arr
    if not isinstance(values, (types.Set, types.List)):
        raise BodoError(
            "Series.isin(): 'values' parameter should be a set or a list")

    def impl(S, values):
        A = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        wzmu__etpuf = bodo.libs.array_ops.array_op_isin(A, values)
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf, index, name
            )
    return impl


@overload_method(SeriesType, 'quantile', inline='always', no_unliteral=True)
def overload_series_quantile(S, q=0.5, interpolation='linear'):
    yppn__bgd = dict(interpolation=interpolation)
    ihi__bqwp = dict(interpolation='linear')
    check_unsupported_args('Series.quantile', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.quantile()')
    if is_iterable_type(q) and isinstance(q.dtype, types.Number):

        def impl_list(S, q=0.5, interpolation='linear'):
            arr = bodo.hiframes.pd_series_ext.get_series_data(S)
            wzmu__etpuf = bodo.libs.array_ops.array_op_quantile(arr, q)
            name = bodo.hiframes.pd_series_ext.get_series_name(S)
            index = bodo.hiframes.pd_index_ext.init_numeric_index(bodo.
                utils.conversion.coerce_to_array(q), None)
            return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                index, name)
        return impl_list
    elif isinstance(q, (float, types.Number)) or is_overload_constant_int(q):

        def impl(S, q=0.5, interpolation='linear'):
            arr = bodo.hiframes.pd_series_ext.get_series_data(S)
            return bodo.libs.array_ops.array_op_quantile(arr, q)
        return impl
    else:
        raise BodoError(
            f'Series.quantile() q type must be float or iterable of floats only.'
            )


@overload_method(SeriesType, 'nunique', inline='always', no_unliteral=True)
def overload_series_nunique(S, dropna=True):
    if not is_overload_bool(dropna):
        raise BodoError('Series.nunique: dropna must be a boolean value')

    def impl(S, dropna=True):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        return bodo.libs.array_kernels.nunique(arr, dropna)
    return impl


@overload_method(SeriesType, 'unique', inline='always', no_unliteral=True)
def overload_series_unique(S):

    def impl(S):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        zhbu__iuuq = bodo.libs.array_kernels.unique(arr)
        return bodo.allgatherv(zhbu__iuuq, False)
    return impl


@overload_method(SeriesType, 'describe', inline='always', no_unliteral=True)
def overload_series_describe(S, percentiles=None, include=None, exclude=
    None, datetime_is_numeric=True):
    yppn__bgd = dict(percentiles=percentiles, include=include, exclude=
        exclude, datetime_is_numeric=datetime_is_numeric)
    ihi__bqwp = dict(percentiles=None, include=None, exclude=None,
        datetime_is_numeric=True)
    check_unsupported_args('Series.describe', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.describe()')
    if not (isinstance(S.data, types.Array) and (isinstance(S.data.dtype,
        types.Number) or S.data.dtype == bodo.datetime64ns)
        ) and not isinstance(S.data, (IntegerArrayType, FloatingArrayType)):
        raise BodoError(f'describe() column input type {S.data} not supported.'
            )
    if S.data.dtype == bodo.datetime64ns:

        def impl_dt(S, percentiles=None, include=None, exclude=None,
            datetime_is_numeric=True):
            arr = bodo.hiframes.pd_series_ext.get_series_data(S)
            name = bodo.hiframes.pd_series_ext.get_series_name(S)
            return bodo.hiframes.pd_series_ext.init_series(bodo.libs.
                array_ops.array_op_describe(arr), bodo.utils.conversion.
                convert_to_index(['count', 'mean', 'min', '25%', '50%',
                '75%', 'max']), name)
        return impl_dt

    def impl(S, percentiles=None, include=None, exclude=None,
        datetime_is_numeric=True):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        return bodo.hiframes.pd_series_ext.init_series(bodo.libs.array_ops.
            array_op_describe(arr), bodo.utils.conversion.convert_to_index(
            ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']), name)
    return impl


@overload_method(SeriesType, 'memory_usage', inline='always', no_unliteral=True
    )
def overload_series_memory_usage(S, index=True, deep=False):
    if is_overload_true(index):

        def impl(S, index=True, deep=False):
            arr = bodo.hiframes.pd_series_ext.get_series_data(S)
            index = bodo.hiframes.pd_series_ext.get_series_index(S)
            return arr.nbytes + index.nbytes
        return impl
    else:

        def impl(S, index=True, deep=False):
            arr = bodo.hiframes.pd_series_ext.get_series_data(S)
            return arr.nbytes
        return impl


def binary_str_fillna_inplace_series_impl(is_binary=False):
    if is_binary:
        dpd__cjdxz = 'bodo.libs.binary_arr_ext.pre_alloc_binary_array'
    else:
        dpd__cjdxz = 'bodo.libs.str_arr_ext.pre_alloc_string_array'
    deqe__ahp = '\n'.join(('def impl(', '    S,', '    value=None,',
        '    method=None,', '    axis=None,', '    inplace=False,',
        '    limit=None,', '    downcast=None,', '):',
        '    in_arr = bodo.hiframes.pd_series_ext.get_series_data(S)',
        '    fill_arr = bodo.hiframes.pd_series_ext.get_series_data(value)',
        '    n = len(in_arr)', '    nf = len(fill_arr)',
        "    assert n == nf, 'fillna() requires same length arrays'",
        f'    out_arr = {dpd__cjdxz}(n, -1)',
        '    for j in numba.parfors.parfor.internal_prange(n):',
        '        s = in_arr[j]',
        '        if bodo.libs.array_kernels.isna(in_arr, j) and not bodo.libs.array_kernels.isna('
        , '            fill_arr, j', '        ):',
        '            s = fill_arr[j]', '        out_arr[j] = s',
        '    bodo.libs.str_arr_ext.move_str_binary_arr_payload(in_arr, out_arr)'
        ))
    ymp__tady = dict()
    exec(deqe__ahp, {'bodo': bodo, 'numba': numba}, ymp__tady)
    satbs__xiixv = ymp__tady['impl']
    return satbs__xiixv


def binary_str_fillna_inplace_impl(is_binary=False):
    if is_binary:
        dpd__cjdxz = 'bodo.libs.binary_arr_ext.pre_alloc_binary_array'
    else:
        dpd__cjdxz = 'bodo.libs.str_arr_ext.pre_alloc_string_array'
    deqe__ahp = 'def impl(S,\n'
    deqe__ahp += '     value=None,\n'
    deqe__ahp += '    method=None,\n'
    deqe__ahp += '    axis=None,\n'
    deqe__ahp += '    inplace=False,\n'
    deqe__ahp += '    limit=None,\n'
    deqe__ahp += '   downcast=None,\n'
    deqe__ahp += '):\n'
    deqe__ahp += (
        '    in_arr = bodo.hiframes.pd_series_ext.get_series_data(S)\n')
    deqe__ahp += '    n = len(in_arr)\n'
    deqe__ahp += f'    out_arr = {dpd__cjdxz}(n, -1)\n'
    deqe__ahp += '    for j in numba.parfors.parfor.internal_prange(n):\n'
    deqe__ahp += '        s = in_arr[j]\n'
    deqe__ahp += '        if bodo.libs.array_kernels.isna(in_arr, j):\n'
    deqe__ahp += '            s = value\n'
    deqe__ahp += '        out_arr[j] = s\n'
    deqe__ahp += (
        '    bodo.libs.str_arr_ext.move_str_binary_arr_payload(in_arr, out_arr)\n'
        )
    ymp__tady = dict()
    exec(deqe__ahp, {'bodo': bodo, 'numba': numba}, ymp__tady)
    satbs__xiixv = ymp__tady['impl']
    return satbs__xiixv


def fillna_inplace_series_impl(S, value=None, method=None, axis=None,
    inplace=False, limit=None, downcast=None):
    iwuhx__bmy = bodo.hiframes.pd_series_ext.get_series_data(S)
    sgu__fov = bodo.hiframes.pd_series_ext.get_series_data(value)
    for ynjr__fnfp in numba.parfors.parfor.internal_prange(len(iwuhx__bmy)):
        s = iwuhx__bmy[ynjr__fnfp]
        if bodo.libs.array_kernels.isna(iwuhx__bmy, ynjr__fnfp
            ) and not bodo.libs.array_kernels.isna(sgu__fov, ynjr__fnfp):
            s = sgu__fov[ynjr__fnfp]
        iwuhx__bmy[ynjr__fnfp] = s


def fillna_inplace_impl(S, value=None, method=None, axis=None, inplace=
    False, limit=None, downcast=None):
    iwuhx__bmy = bodo.hiframes.pd_series_ext.get_series_data(S)
    for ynjr__fnfp in numba.parfors.parfor.internal_prange(len(iwuhx__bmy)):
        s = iwuhx__bmy[ynjr__fnfp]
        if bodo.libs.array_kernels.isna(iwuhx__bmy, ynjr__fnfp):
            s = value
        iwuhx__bmy[ynjr__fnfp] = s


def str_fillna_alloc_series_impl(S, value=None, method=None, axis=None,
    inplace=False, limit=None, downcast=None):
    iwuhx__bmy = bodo.hiframes.pd_series_ext.get_series_data(S)
    index = bodo.hiframes.pd_series_ext.get_series_index(S)
    name = bodo.hiframes.pd_series_ext.get_series_name(S)
    sgu__fov = bodo.hiframes.pd_series_ext.get_series_data(value)
    n = len(iwuhx__bmy)
    wzmu__etpuf = bodo.libs.str_arr_ext.pre_alloc_string_array(n, -1)
    for vtry__cvoha in numba.parfors.parfor.internal_prange(n):
        s = iwuhx__bmy[vtry__cvoha]
        if bodo.libs.array_kernels.isna(iwuhx__bmy, vtry__cvoha
            ) and not bodo.libs.array_kernels.isna(sgu__fov, vtry__cvoha):
            s = sgu__fov[vtry__cvoha]
        wzmu__etpuf[vtry__cvoha] = s
        if bodo.libs.array_kernels.isna(iwuhx__bmy, vtry__cvoha
            ) and bodo.libs.array_kernels.isna(sgu__fov, vtry__cvoha):
            bodo.libs.array_kernels.setna(wzmu__etpuf, vtry__cvoha)
    return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf, index, name)


def fillna_series_impl(S, value=None, method=None, axis=None, inplace=False,
    limit=None, downcast=None):
    iwuhx__bmy = bodo.hiframes.pd_series_ext.get_series_data(S)
    index = bodo.hiframes.pd_series_ext.get_series_index(S)
    name = bodo.hiframes.pd_series_ext.get_series_name(S)
    sgu__fov = bodo.hiframes.pd_series_ext.get_series_data(value)
    n = len(iwuhx__bmy)
    wzmu__etpuf = bodo.utils.utils.alloc_type(n, iwuhx__bmy.dtype, (-1,))
    for ynjr__fnfp in numba.parfors.parfor.internal_prange(n):
        s = iwuhx__bmy[ynjr__fnfp]
        if bodo.libs.array_kernels.isna(iwuhx__bmy, ynjr__fnfp
            ) and not bodo.libs.array_kernels.isna(sgu__fov, ynjr__fnfp):
            s = sgu__fov[ynjr__fnfp]
        wzmu__etpuf[ynjr__fnfp] = s
    return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf, index, name)


@overload_method(SeriesType, 'fillna', no_unliteral=True)
def overload_series_fillna(S, value=None, method=None, axis=None, inplace=
    False, limit=None, downcast=None):
    yppn__bgd = dict(limit=limit, downcast=downcast)
    ihi__bqwp = dict(limit=None, downcast=None)
    check_unsupported_args('Series.fillna', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    fccvp__dwrvu = not is_overload_none(value)
    tsb__vcx = not is_overload_none(method)
    if fccvp__dwrvu and tsb__vcx:
        raise BodoError(
            "Series.fillna(): Cannot specify both 'value' and 'method'.")
    if not fccvp__dwrvu and not tsb__vcx:
        raise BodoError(
            "Series.fillna(): Must specify one of 'value' and 'method'.")
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error('Series.fillna(): axis argument not supported')
    elif is_iterable_type(value) and not isinstance(value, SeriesType):
        raise BodoError('Series.fillna(): "value" parameter cannot be a list')
    elif is_var_size_item_array_type(S.data
        ) and not S.dtype == bodo.string_type:
        raise BodoError(
            f'Series.fillna() with inplace=True not supported for {S.dtype} values yet.'
            )
    if not is_overload_constant_bool(inplace):
        raise_bodo_error(
            "Series.fillna(): 'inplace' argument must be a constant boolean")
    if tsb__vcx:
        if is_overload_true(inplace):
            raise BodoError(
                "Series.fillna() with inplace=True not supported with 'method' argument yet."
                )
        uhqd__uess = (
            "Series.fillna(): 'method' argument if provided must be a constant string and one of ('backfill', 'bfill', 'pad' 'ffill')."
            )
        if not is_overload_constant_str(method):
            raise_bodo_error(uhqd__uess)
        elif get_overload_const_str(method) not in ('backfill', 'bfill',
            'pad', 'ffill'):
            raise BodoError(uhqd__uess)
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.fillna()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(value,
        'Series.fillna()')
    pkjtp__azkjr = element_type(S.data)
    ovrg__sol = None
    if fccvp__dwrvu:
        ovrg__sol = element_type(types.unliteral(value))
    if ovrg__sol and not can_replace(pkjtp__azkjr, ovrg__sol):
        raise BodoError(
            f'Series.fillna(): Cannot use value type {ovrg__sol} with series type {pkjtp__azkjr}'
            )
    if is_overload_true(inplace):
        if S.dtype == bodo.string_type:
            if S.data == bodo.dict_str_arr_type:
                raise_bodo_error(
                    "Series.fillna(): 'inplace' not supported for dictionary-encoded string arrays yet."
                    )
            if is_overload_constant_str(value) and get_overload_const_str(value
                ) == '':
                return (lambda S, value=None, method=None, axis=None,
                    inplace=False, limit=None, downcast=None: bodo.libs.
                    str_arr_ext.set_null_bits_to_value(bodo.hiframes.
                    pd_series_ext.get_series_data(S), -1))
            if isinstance(value, SeriesType):
                return binary_str_fillna_inplace_series_impl(is_binary=False)
            return binary_str_fillna_inplace_impl(is_binary=False)
        if S.dtype == bodo.bytes_type:
            if is_overload_constant_bytes(value) and get_overload_const_bytes(
                value) == b'':
                return (lambda S, value=None, method=None, axis=None,
                    inplace=False, limit=None, downcast=None: bodo.libs.
                    str_arr_ext.set_null_bits_to_value(bodo.hiframes.
                    pd_series_ext.get_series_data(S), -1))
            if isinstance(value, SeriesType):
                return binary_str_fillna_inplace_series_impl(is_binary=True)
            return binary_str_fillna_inplace_impl(is_binary=True)
        else:
            if isinstance(value, SeriesType):
                return fillna_inplace_series_impl
            return fillna_inplace_impl
    else:
        uxrgd__wxl = to_str_arr_if_dict_array(S.data)
        if isinstance(value, SeriesType):

            def fillna_series_impl(S, value=None, method=None, axis=None,
                inplace=False, limit=None, downcast=None):
                iwuhx__bmy = bodo.hiframes.pd_series_ext.get_series_data(S)
                index = bodo.hiframes.pd_series_ext.get_series_index(S)
                name = bodo.hiframes.pd_series_ext.get_series_name(S)
                sgu__fov = bodo.hiframes.pd_series_ext.get_series_data(value)
                n = len(iwuhx__bmy)
                wzmu__etpuf = bodo.utils.utils.alloc_type(n, uxrgd__wxl, (-1,))
                for ynjr__fnfp in numba.parfors.parfor.internal_prange(n):
                    if bodo.libs.array_kernels.isna(iwuhx__bmy, ynjr__fnfp
                        ) and bodo.libs.array_kernels.isna(sgu__fov, ynjr__fnfp
                        ):
                        bodo.libs.array_kernels.setna(wzmu__etpuf, ynjr__fnfp)
                        continue
                    if bodo.libs.array_kernels.isna(iwuhx__bmy, ynjr__fnfp):
                        wzmu__etpuf[ynjr__fnfp
                            ] = bodo.utils.conversion.unbox_if_tz_naive_timestamp(
                            sgu__fov[ynjr__fnfp])
                        continue
                    wzmu__etpuf[ynjr__fnfp
                        ] = bodo.utils.conversion.unbox_if_tz_naive_timestamp(
                        iwuhx__bmy[ynjr__fnfp])
                return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                    index, name)
            return fillna_series_impl
        if tsb__vcx:
            elq__nlnb = (types.unicode_type, types.bool_, bodo.datetime64ns,
                bodo.timedelta64ns)
            if not isinstance(pkjtp__azkjr, (types.Integer, types.Float)
                ) and pkjtp__azkjr not in elq__nlnb:
                raise BodoError(
                    f"Series.fillna(): series of type {pkjtp__azkjr} are not supported with 'method' argument."
                    )

            def fillna_method_impl(S, value=None, method=None, axis=None,
                inplace=False, limit=None, downcast=None):
                iwuhx__bmy = bodo.hiframes.pd_series_ext.get_series_data(S)
                index = bodo.hiframes.pd_series_ext.get_series_index(S)
                name = bodo.hiframes.pd_series_ext.get_series_name(S)
                wzmu__etpuf = bodo.libs.array_kernels.ffill_bfill_arr(
                    iwuhx__bmy, method)
                return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                    index, name)
            return fillna_method_impl

        def fillna_impl(S, value=None, method=None, axis=None, inplace=
            False, limit=None, downcast=None):
            value = bodo.utils.conversion.unbox_if_tz_naive_timestamp(value)
            iwuhx__bmy = bodo.hiframes.pd_series_ext.get_series_data(S)
            index = bodo.hiframes.pd_series_ext.get_series_index(S)
            name = bodo.hiframes.pd_series_ext.get_series_name(S)
            n = len(iwuhx__bmy)
            wzmu__etpuf = bodo.utils.utils.alloc_type(n, uxrgd__wxl, (-1,))
            for ynjr__fnfp in numba.parfors.parfor.internal_prange(n):
                s = bodo.utils.conversion.unbox_if_tz_naive_timestamp(
                    iwuhx__bmy[ynjr__fnfp])
                if bodo.libs.array_kernels.isna(iwuhx__bmy, ynjr__fnfp):
                    s = value
                wzmu__etpuf[ynjr__fnfp] = s
            return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                index, name)
        return fillna_impl


def create_fillna_specific_method_overload(overload_name):

    def overload_series_fillna_specific_method(S, axis=None, inplace=False,
        limit=None, downcast=None):
        qrv__tmvh = {'ffill': 'ffill', 'bfill': 'bfill', 'pad': 'ffill',
            'backfill': 'bfill'}[overload_name]
        yppn__bgd = dict(limit=limit, downcast=downcast)
        ihi__bqwp = dict(limit=None, downcast=None)
        check_unsupported_args(f'Series.{overload_name}', yppn__bgd,
            ihi__bqwp, package_name='pandas', module_name='Series')
        if not (is_overload_none(axis) or is_overload_zero(axis)):
            raise BodoError(
                f'Series.{overload_name}(): axis argument not supported')
        pkjtp__azkjr = element_type(S.data)
        elq__nlnb = (types.unicode_type, types.bool_, bodo.datetime64ns,
            bodo.timedelta64ns)
        if not isinstance(pkjtp__azkjr, (types.Integer, types.Float)
            ) and pkjtp__azkjr not in elq__nlnb:
            raise BodoError(
                f'Series.{overload_name}(): series of type {pkjtp__azkjr} are not supported.'
                )

        def impl(S, axis=None, inplace=False, limit=None, downcast=None):
            iwuhx__bmy = bodo.hiframes.pd_series_ext.get_series_data(S)
            index = bodo.hiframes.pd_series_ext.get_series_index(S)
            name = bodo.hiframes.pd_series_ext.get_series_name(S)
            wzmu__etpuf = bodo.libs.array_kernels.ffill_bfill_arr(iwuhx__bmy,
                qrv__tmvh)
            return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                index, name)
        return impl
    return overload_series_fillna_specific_method


fillna_specific_methods = 'ffill', 'bfill', 'pad', 'backfill'


def _install_fillna_specific_methods():
    for overload_name in fillna_specific_methods:
        koqn__wykgs = create_fillna_specific_method_overload(overload_name)
        overload_method(SeriesType, overload_name, no_unliteral=True)(
            koqn__wykgs)


_install_fillna_specific_methods()


def check_unsupported_types(S, to_replace, value):
    if any(bodo.utils.utils.is_array_typ(x, True) for x in [S.dtype,
        to_replace, value]):
        zlzex__irlh = (
            'Series.replace(): only support with Scalar, List, or Dictionary')
        raise BodoError(zlzex__irlh)
    elif isinstance(to_replace, types.DictType) and not is_overload_none(value
        ):
        zlzex__irlh = (
            "Series.replace(): 'value' must be None when 'to_replace' is a dictionary"
            )
        raise BodoError(zlzex__irlh)
    elif any(isinstance(x, (PandasTimestampType, PDTimeDeltaType)) for x in
        [to_replace, value]):
        zlzex__irlh = (
            f'Series.replace(): Not supported for types {to_replace} and {value}'
            )
        raise BodoError(zlzex__irlh)


def series_replace_error_checking(S, to_replace, value, inplace, limit,
    regex, method):
    yppn__bgd = dict(inplace=inplace, limit=limit, regex=regex, method=method)
    ptj__slr = dict(inplace=False, limit=None, regex=False, method='pad')
    check_unsupported_args('Series.replace', yppn__bgd, ptj__slr,
        package_name='pandas', module_name='Series')
    check_unsupported_types(S, to_replace, value)


@overload_method(SeriesType, 'replace', inline='always', no_unliteral=True)
def overload_series_replace(S, to_replace=None, value=None, inplace=False,
    limit=None, regex=False, method='pad'):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.replace()')
    series_replace_error_checking(S, to_replace, value, inplace, limit,
        regex, method)
    pkjtp__azkjr = element_type(S.data)
    if isinstance(to_replace, types.DictType):
        ewo__giql = element_type(to_replace.key_type)
        ovrg__sol = element_type(to_replace.value_type)
    else:
        ewo__giql = element_type(to_replace)
        ovrg__sol = element_type(value)
    wpbya__icnq = None
    if pkjtp__azkjr != types.unliteral(ewo__giql):
        if bodo.utils.typing.equality_always_false(pkjtp__azkjr, types.
            unliteral(ewo__giql)
            ) or not bodo.utils.typing.types_equality_exists(pkjtp__azkjr,
            ewo__giql):

            def impl(S, to_replace=None, value=None, inplace=False, limit=
                None, regex=False, method='pad'):
                return S.copy()
            return impl
        if isinstance(pkjtp__azkjr, (types.Float, types.Integer)
            ) or pkjtp__azkjr == np.bool_:
            wpbya__icnq = pkjtp__azkjr
    if not can_replace(pkjtp__azkjr, types.unliteral(ovrg__sol)):

        def impl(S, to_replace=None, value=None, inplace=False, limit=None,
            regex=False, method='pad'):
            return S.copy()
        return impl
    qrf__gyszv = to_str_arr_if_dict_array(S.data)
    if isinstance(qrf__gyszv, CategoricalArrayType):

        def cat_impl(S, to_replace=None, value=None, inplace=False, limit=
            None, regex=False, method='pad'):
            iwuhx__bmy = bodo.hiframes.pd_series_ext.get_series_data(S)
            index = bodo.hiframes.pd_series_ext.get_series_index(S)
            name = bodo.hiframes.pd_series_ext.get_series_name(S)
            return bodo.hiframes.pd_series_ext.init_series(iwuhx__bmy.
                replace(to_replace, value), index, name)
        return cat_impl

    def impl(S, to_replace=None, value=None, inplace=False, limit=None,
        regex=False, method='pad'):
        iwuhx__bmy = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        n = len(iwuhx__bmy)
        wzmu__etpuf = bodo.utils.utils.alloc_type(n, qrf__gyszv, (-1,))
        mpgu__nqpko = build_replace_dict(to_replace, value, wpbya__icnq)
        for ynjr__fnfp in numba.parfors.parfor.internal_prange(n):
            if bodo.libs.array_kernels.isna(iwuhx__bmy, ynjr__fnfp):
                bodo.libs.array_kernels.setna(wzmu__etpuf, ynjr__fnfp)
                continue
            s = iwuhx__bmy[ynjr__fnfp]
            if s in mpgu__nqpko:
                s = mpgu__nqpko[s]
            wzmu__etpuf[ynjr__fnfp] = s
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf, index, name
            )
    return impl


def build_replace_dict(to_replace, value, key_dtype_conv):
    pass


@overload(build_replace_dict)
def _build_replace_dict(to_replace, value, key_dtype_conv):
    emwhr__gjafe = isinstance(to_replace, (types.Number, Decimal128Type)
        ) or to_replace in [bodo.string_type, types.boolean, bodo.bytes_type]
    vvvqa__pmnvm = is_iterable_type(to_replace)
    kwvkt__qrw = isinstance(value, (types.Number, Decimal128Type)
        ) or value in [bodo.string_type, bodo.bytes_type, types.boolean]
    tupaa__orra = is_iterable_type(value)
    if emwhr__gjafe and kwvkt__qrw:
        if not is_overload_none(key_dtype_conv):

            def impl_cast(to_replace, value, key_dtype_conv):
                mpgu__nqpko = {}
                mpgu__nqpko[key_dtype_conv(to_replace)] = value
                return mpgu__nqpko
            return impl_cast

        def impl(to_replace, value, key_dtype_conv):
            mpgu__nqpko = {}
            mpgu__nqpko[to_replace] = value
            return mpgu__nqpko
        return impl
    if vvvqa__pmnvm and kwvkt__qrw:
        if not is_overload_none(key_dtype_conv):

            def impl_cast(to_replace, value, key_dtype_conv):
                mpgu__nqpko = {}
                for okr__ijxqz in to_replace:
                    mpgu__nqpko[key_dtype_conv(okr__ijxqz)] = value
                return mpgu__nqpko
            return impl_cast

        def impl(to_replace, value, key_dtype_conv):
            mpgu__nqpko = {}
            for okr__ijxqz in to_replace:
                mpgu__nqpko[okr__ijxqz] = value
            return mpgu__nqpko
        return impl
    if vvvqa__pmnvm and tupaa__orra:
        if not is_overload_none(key_dtype_conv):

            def impl_cast(to_replace, value, key_dtype_conv):
                mpgu__nqpko = {}
                assert len(to_replace) == len(value
                    ), 'To_replace and value lengths must be the same'
                for ynjr__fnfp in range(len(to_replace)):
                    mpgu__nqpko[key_dtype_conv(to_replace[ynjr__fnfp])
                        ] = value[ynjr__fnfp]
                return mpgu__nqpko
            return impl_cast

        def impl(to_replace, value, key_dtype_conv):
            mpgu__nqpko = {}
            assert len(to_replace) == len(value
                ), 'To_replace and value lengths must be the same'
            for ynjr__fnfp in range(len(to_replace)):
                mpgu__nqpko[to_replace[ynjr__fnfp]] = value[ynjr__fnfp]
            return mpgu__nqpko
        return impl
    if isinstance(to_replace, numba.types.DictType) and is_overload_none(value
        ):
        return lambda to_replace, value, key_dtype_conv: to_replace
    raise BodoError(
        'Series.replace(): Not supported for types to_replace={} and value={}'
        .format(to_replace, value))


@overload_method(SeriesType, 'diff', inline='always', no_unliteral=True)
def overload_series_diff(S, periods=1):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.diff()')
    if not (isinstance(S.data, types.Array) and (isinstance(S.data.dtype,
        types.Number) or S.data.dtype == bodo.datetime64ns)):
        raise BodoError(
            f'Series.diff() column input type {S.data} not supported.')
    if not is_overload_int(periods):
        raise BodoError("Series.diff(): 'periods' input must be an integer.")
    if S.data == types.Array(bodo.datetime64ns, 1, 'C'):

        def impl_datetime(S, periods=1):
            arr = bodo.hiframes.pd_series_ext.get_series_data(S)
            index = bodo.hiframes.pd_series_ext.get_series_index(S)
            name = bodo.hiframes.pd_series_ext.get_series_name(S)
            wzmu__etpuf = bodo.hiframes.series_impl.dt64_arr_sub(arr, bodo.
                hiframes.rolling.shift(arr, periods, False))
            return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                index, name)
        return impl_datetime

    def impl(S, periods=1):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        wzmu__etpuf = arr - bodo.hiframes.rolling.shift(arr, periods, False)
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf, index, name
            )
    return impl


@overload_method(SeriesType, 'explode', inline='always', no_unliteral=True)
def overload_series_explode(S, ignore_index=False):
    from bodo.hiframes.split_impl import string_array_split_view_type
    yppn__bgd = dict(ignore_index=ignore_index)
    uobs__ultl = dict(ignore_index=False)
    check_unsupported_args('Series.explode', yppn__bgd, uobs__ultl,
        package_name='pandas', module_name='Series')
    if not (isinstance(S.data, ArrayItemArrayType) or S.data ==
        string_array_split_view_type):
        return lambda S, ignore_index=False: S.copy()

    def impl(S, ignore_index=False):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        cieta__wodph = bodo.utils.conversion.index_to_array(index)
        wzmu__etpuf, oaj__syo = bodo.libs.array_kernels.explode(arr,
            cieta__wodph)
        qdyl__gas = bodo.utils.conversion.index_from_array(oaj__syo)
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
            qdyl__gas, name)
    return impl


@overload(np.digitize, inline='always', no_unliteral=True)
def overload_series_np_digitize(x, bins, right=False):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(x,
        'numpy.digitize()')
    if isinstance(x, SeriesType):

        def impl(x, bins, right=False):
            arr = bodo.hiframes.pd_series_ext.get_series_data(x)
            return np.digitize(arr, bins, right)
        return impl


@overload(np.argmax, inline='always', no_unliteral=True)
def argmax_overload(a, axis=None, out=None):
    if isinstance(a, types.Array) and is_overload_constant_int(axis
        ) and get_overload_const_int(axis) == 1:

        def impl(a, axis=None, out=None):
            qdhkh__uvoas = np.empty(len(a), a.dtype)
            numba.parfors.parfor.init_prange()
            n = len(a)
            for ynjr__fnfp in numba.parfors.parfor.internal_prange(n):
                qdhkh__uvoas[ynjr__fnfp] = np.argmax(a[ynjr__fnfp])
            return qdhkh__uvoas
        return impl


@overload(np.argmin, inline='always', no_unliteral=True)
def argmin_overload(a, axis=None, out=None):
    if isinstance(a, types.Array) and is_overload_constant_int(axis
        ) and get_overload_const_int(axis) == 1:

        def impl(a, axis=None, out=None):
            fgdo__lscj = np.empty(len(a), a.dtype)
            numba.parfors.parfor.init_prange()
            n = len(a)
            for ynjr__fnfp in numba.parfors.parfor.internal_prange(n):
                fgdo__lscj[ynjr__fnfp] = np.argmin(a[ynjr__fnfp])
            return fgdo__lscj
        return impl


def overload_series_np_dot(a, b, out=None):
    if (isinstance(a, SeriesType) or isinstance(b, SeriesType)
        ) and not is_overload_none(out):
        raise BodoError("np.dot(): 'out' parameter not supported yet")
    if isinstance(a, SeriesType) and isinstance(b, SeriesType):

        def impl(a, b, out=None):
            arr = bodo.utils.conversion.ndarray_if_nullable_arr(bodo.
                hiframes.pd_series_ext.get_series_data(a))
            bqvq__vhr = bodo.utils.conversion.ndarray_if_nullable_arr(bodo.
                hiframes.pd_series_ext.get_series_data(b))
            return np.dot(arr, bqvq__vhr)
        return impl
    if isinstance(a, SeriesType):

        def impl(a, b, out=None):
            arr = bodo.utils.conversion.ndarray_if_nullable_arr(bodo.
                hiframes.pd_series_ext.get_series_data(a))
            b = bodo.utils.conversion.ndarray_if_nullable_arr(b)
            return np.dot(arr, b)
        return impl
    if isinstance(b, SeriesType):

        def impl(a, b, out=None):
            a = bodo.utils.conversion.ndarray_if_nullable_arr(a)
            arr = bodo.utils.conversion.ndarray_if_nullable_arr(bodo.
                hiframes.pd_series_ext.get_series_data(b))
            return np.dot(a, arr)
        return impl


overload(np.dot, inline='always', no_unliteral=True)(overload_series_np_dot)
overload(operator.matmul, inline='always', no_unliteral=True)(
    overload_series_np_dot)


@overload_method(SeriesType, 'dropna', inline='always', no_unliteral=True)
def overload_series_dropna(S, axis=0, inplace=False, how=None):
    yppn__bgd = dict(axis=axis, inplace=inplace, how=how)
    duea__rfu = dict(axis=0, inplace=False, how=None)
    check_unsupported_args('Series.dropna', yppn__bgd, duea__rfu,
        package_name='pandas', module_name='Series')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.dropna()')
    if S.dtype == bodo.string_type:

        def dropna_str_impl(S, axis=0, inplace=False, how=None):
            iwuhx__bmy = bodo.hiframes.pd_series_ext.get_series_data(S)
            name = bodo.hiframes.pd_series_ext.get_series_name(S)
            egxx__vydoc = S.notna().values
            cieta__wodph = bodo.utils.conversion.extract_index_array(S)
            qdyl__gas = bodo.utils.conversion.convert_to_index(cieta__wodph
                [egxx__vydoc])
            wzmu__etpuf = (bodo.hiframes.series_kernels.
                _series_dropna_str_alloc_impl_inner(iwuhx__bmy))
            return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                qdyl__gas, name)
        return dropna_str_impl
    else:

        def dropna_impl(S, axis=0, inplace=False, how=None):
            iwuhx__bmy = bodo.hiframes.pd_series_ext.get_series_data(S)
            name = bodo.hiframes.pd_series_ext.get_series_name(S)
            cieta__wodph = bodo.utils.conversion.extract_index_array(S)
            egxx__vydoc = S.notna().values
            qdyl__gas = bodo.utils.conversion.convert_to_index(cieta__wodph
                [egxx__vydoc])
            wzmu__etpuf = iwuhx__bmy[egxx__vydoc]
            return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                qdyl__gas, name)
        return dropna_impl


@overload_method(SeriesType, 'shift', inline='always', no_unliteral=True)
def overload_series_shift(S, periods=1, freq=None, axis=0, fill_value=None):
    yppn__bgd = dict(freq=freq, axis=axis)
    ihi__bqwp = dict(freq=None, axis=0)
    check_unsupported_args('Series.shift', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not is_supported_shift_array_type(S.data):
        raise BodoError(
            f"Series.shift(): Series input type '{S.data.dtype}' not supported yet."
            )
    if not is_overload_int(periods):
        raise BodoError("Series.shift(): 'periods' input must be an integer.")

    def impl(S, periods=1, freq=None, axis=0, fill_value=None):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        wzmu__etpuf = bodo.hiframes.rolling.shift(arr, periods, False,
            fill_value)
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf, index, name
            )
    return impl


@overload_method(SeriesType, 'pct_change', inline='always', no_unliteral=True)
def overload_series_pct_change(S, periods=1, fill_method='pad', limit=None,
    freq=None):
    yppn__bgd = dict(fill_method=fill_method, limit=limit, freq=freq)
    ihi__bqwp = dict(fill_method='pad', limit=None, freq=None)
    check_unsupported_args('Series.pct_change', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    if not is_overload_int(periods):
        raise BodoError(
            'Series.pct_change(): periods argument must be an Integer')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.pct_change()')

    def impl(S, periods=1, fill_method='pad', limit=None, freq=None):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        wzmu__etpuf = bodo.hiframes.rolling.pct_change(arr, periods, False)
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf, index, name
            )
    return impl


def create_series_mask_where_overload(func_name):

    def overload_series_mask_where(S, cond, other=np.nan, inplace=False,
        axis=None, level=None, errors='raise', try_cast=False):
        bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
            f'Series.{func_name}()')
        bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(other,
            f'Series.{func_name}()')
        _validate_arguments_mask_where(f'Series.{func_name}', 'Series', S,
            cond, other, inplace, axis, level, errors, try_cast)
        if is_overload_constant_nan(other):
            eke__frvrl = 'None'
        else:
            eke__frvrl = 'other'
        deqe__ahp = """def impl(S, cond, other=np.nan, inplace=False, axis=None, level=None, errors='raise',try_cast=False):
"""
        if func_name == 'mask':
            deqe__ahp += '  cond = ~cond\n'
        deqe__ahp += '  arr = bodo.hiframes.pd_series_ext.get_series_data(S)\n'
        deqe__ahp += (
            '  index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
        deqe__ahp += (
            '  name = bodo.hiframes.pd_series_ext.get_series_name(S)\n')
        deqe__ahp += (
            f'  out_arr = bodo.hiframes.series_impl.where_impl(cond, arr, {eke__frvrl})\n'
            )
        deqe__ahp += (
            '  return bodo.hiframes.pd_series_ext.init_series(out_arr, index, name)\n'
            )
        nii__tveq = {}
        exec(deqe__ahp, {'bodo': bodo, 'np': np}, nii__tveq)
        impl = nii__tveq['impl']
        return impl
    return overload_series_mask_where


def _install_series_mask_where_overload():
    for func_name in ('mask', 'where'):
        koqn__wykgs = create_series_mask_where_overload(func_name)
        overload_method(SeriesType, func_name, no_unliteral=True)(koqn__wykgs)


_install_series_mask_where_overload()


def _validate_arguments_mask_where(func_name, module_name, S, cond, other,
    inplace, axis, level, errors, try_cast):
    yppn__bgd = dict(inplace=inplace, level=level, errors=errors, try_cast=
        try_cast)
    ihi__bqwp = dict(inplace=False, level=None, errors='raise', try_cast=False)
    check_unsupported_args(f'{func_name}', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name=module_name)
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error(f'{func_name}(): axis argument not supported')
    if isinstance(S, bodo.hiframes.pd_index_ext.RangeIndexType):
        arr = types.Array(types.int64, 1, 'C')
    else:
        arr = S.data
    if isinstance(other, SeriesType):
        _validate_self_other_mask_where(func_name, module_name, arr, other.data
            )
    else:
        _validate_self_other_mask_where(func_name, module_name, arr, other)
    if not (isinstance(cond, (SeriesType, types.Array, BooleanArrayType)) and
        cond.ndim == 1 and cond.dtype == types.bool_):
        raise BodoError(
            f"{func_name}() 'cond' argument must be a Series or 1-dim array of booleans"
            )


def _validate_self_other_mask_where(func_name, module_name, arr, other,
    max_ndim=1, is_default=False):
    if not (isinstance(arr, types.Array) or isinstance(arr,
        BooleanArrayType) or isinstance(arr, IntegerArrayType) or
        isinstance(arr, FloatingArrayType) or bodo.utils.utils.is_array_typ
        (arr, False) and arr.dtype in [bodo.string_type, bodo.bytes_type] or
        isinstance(arr, bodo.CategoricalArrayType) and arr.dtype.elem_type
         not in [bodo.datetime64ns, bodo.timedelta64ns, bodo.
        pd_timestamp_tz_naive_type, bodo.pd_timedelta_type]):
        raise BodoError(
            f'{func_name}() {module_name} data with type {arr} not yet supported'
            )
    awb__lhn = is_overload_constant_nan(other)
    if not (is_default or awb__lhn or is_scalar_type(other) or isinstance(
        other, types.Array) and other.ndim >= 1 and other.ndim <= max_ndim or
        isinstance(other, SeriesType) and (isinstance(arr, types.Array) or 
        arr.dtype in [bodo.string_type, bodo.bytes_type]) or 
        is_str_arr_type(other) and (arr.dtype == bodo.string_type or 
        isinstance(arr, bodo.CategoricalArrayType) and arr.dtype.elem_type ==
        bodo.string_type) or isinstance(other, BinaryArrayType) and (arr.
        dtype == bodo.bytes_type or isinstance(arr, bodo.
        CategoricalArrayType) and arr.dtype.elem_type == bodo.bytes_type) or
        (not (isinstance(other, (StringArrayType, BinaryArrayType)) or 
        other == bodo.dict_str_arr_type) and (isinstance(arr.dtype, types.
        Integer) and (bodo.utils.utils.is_array_typ(other) and isinstance(
        other.dtype, types.Integer) or is_series_type(other) and isinstance
        (other.dtype, types.Integer))) or (bodo.utils.utils.is_array_typ(
        other) and arr.dtype == other.dtype or is_series_type(other) and 
        arr.dtype == other.dtype)) and (isinstance(arr, BooleanArrayType) or
        isinstance(arr, (IntegerArrayType, FloatingArrayType)))):
        raise BodoError(
            f"{func_name}() 'other' must be a scalar, non-categorical series, 1-dim numpy array or StringArray with a matching type for {module_name}."
            )
    if not is_default:
        if isinstance(arr.dtype, bodo.PDCategoricalDtype):
            atx__kyutu = arr.dtype.elem_type
        else:
            atx__kyutu = arr.dtype
        if is_iterable_type(other):
            wiz__optl = other.dtype
        elif awb__lhn:
            wiz__optl = types.float64
        else:
            wiz__optl = types.unliteral(other)
        if not awb__lhn and not is_common_scalar_dtype([atx__kyutu, wiz__optl]
            ):
            raise BodoError(
                f"{func_name}() {module_name.lower()} and 'other' must share a common type."
                )


def create_explicit_binary_op_overload(op):

    def overload_series_explicit_binary_op(S, other, level=None, fill_value
        =None, axis=0):
        yppn__bgd = dict(level=level, axis=axis)
        ihi__bqwp = dict(level=None, axis=0)
        check_unsupported_args('series.{}'.format(op.__name__), yppn__bgd,
            ihi__bqwp, package_name='pandas', module_name='Series')
        avnos__vdiv = other == string_type or is_overload_constant_str(other)
        bahf__lnijc = is_iterable_type(other) and other.dtype == string_type
        kgjz__xatcb = S.dtype == string_type and (op == operator.add and (
            avnos__vdiv or bahf__lnijc) or op == operator.mul and
            isinstance(other, types.Integer))
        nwj__xuljc = S.dtype == bodo.timedelta64ns
        qbceo__dqicv = S.dtype == bodo.datetime64ns
        kss__eon = is_iterable_type(other) and (other.dtype ==
            datetime_timedelta_type or other.dtype == bodo.timedelta64ns)
        ixv__cgwe = is_iterable_type(other) and (other.dtype ==
            datetime_datetime_type or other.dtype ==
            pd_timestamp_tz_naive_type or other.dtype == bodo.datetime64ns)
        ibac__waw = nwj__xuljc and (kss__eon or ixv__cgwe
            ) or qbceo__dqicv and kss__eon
        ibac__waw = ibac__waw and op == operator.add
        if not (isinstance(S.dtype, types.Number) or kgjz__xatcb or ibac__waw):
            raise BodoError(f'Unsupported types for Series.{op.__name__}')
        amyfi__kbhv = numba.core.registry.cpu_target.typing_context
        if is_scalar_type(other):
            args = S.data, other
            qrf__gyszv = amyfi__kbhv.resolve_function_type(op, args, {}
                ).return_type
            if isinstance(S.data, (IntegerArrayType, FloatingArrayType)
                ) and qrf__gyszv == types.Array(types.bool_, 1, 'C'):
                qrf__gyszv = boolean_array

            def impl_scalar(S, other, level=None, fill_value=None, axis=0):
                arr = bodo.hiframes.pd_series_ext.get_series_data(S)
                index = bodo.hiframes.pd_series_ext.get_series_index(S)
                name = bodo.hiframes.pd_series_ext.get_series_name(S)
                numba.parfors.parfor.init_prange()
                other = bodo.utils.conversion.unbox_if_tz_naive_timestamp(other
                    )
                n = len(arr)
                wzmu__etpuf = bodo.utils.utils.alloc_type(n, qrf__gyszv, (-1,))
                for ynjr__fnfp in numba.parfors.parfor.internal_prange(n):
                    kyx__zbz = bodo.libs.array_kernels.isna(arr, ynjr__fnfp)
                    if kyx__zbz:
                        if fill_value is None:
                            bodo.libs.array_kernels.setna(wzmu__etpuf,
                                ynjr__fnfp)
                        else:
                            wzmu__etpuf[ynjr__fnfp] = op(fill_value, other)
                    else:
                        wzmu__etpuf[ynjr__fnfp] = op(arr[ynjr__fnfp], other)
                return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                    index, name)
            return impl_scalar
        args = S.data, types.Array(other.dtype, 1, 'C')
        qrf__gyszv = amyfi__kbhv.resolve_function_type(op, args, {}
            ).return_type
        if isinstance(S.data, (IntegerArrayType, FloatingArrayType)
            ) and qrf__gyszv == types.Array(types.bool_, 1, 'C'):
            qrf__gyszv = boolean_array

        def impl(S, other, level=None, fill_value=None, axis=0):
            arr = bodo.hiframes.pd_series_ext.get_series_data(S)
            index = bodo.hiframes.pd_series_ext.get_series_index(S)
            name = bodo.hiframes.pd_series_ext.get_series_name(S)
            lpq__xrr = bodo.utils.conversion.coerce_to_array(other)
            numba.parfors.parfor.init_prange()
            n = len(arr)
            wzmu__etpuf = bodo.utils.utils.alloc_type(n, qrf__gyszv, (-1,))
            for ynjr__fnfp in numba.parfors.parfor.internal_prange(n):
                kyx__zbz = bodo.libs.array_kernels.isna(arr, ynjr__fnfp)
                jtjfd__uac = bodo.libs.array_kernels.isna(lpq__xrr, ynjr__fnfp)
                if kyx__zbz and jtjfd__uac:
                    bodo.libs.array_kernels.setna(wzmu__etpuf, ynjr__fnfp)
                elif kyx__zbz:
                    if fill_value is None:
                        bodo.libs.array_kernels.setna(wzmu__etpuf, ynjr__fnfp)
                    else:
                        wzmu__etpuf[ynjr__fnfp] = op(fill_value, lpq__xrr[
                            ynjr__fnfp])
                elif jtjfd__uac:
                    if fill_value is None:
                        bodo.libs.array_kernels.setna(wzmu__etpuf, ynjr__fnfp)
                    else:
                        wzmu__etpuf[ynjr__fnfp] = op(arr[ynjr__fnfp],
                            fill_value)
                else:
                    wzmu__etpuf[ynjr__fnfp] = op(arr[ynjr__fnfp], lpq__xrr[
                        ynjr__fnfp])
            return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                index, name)
        return impl
    return overload_series_explicit_binary_op


def create_explicit_binary_reverse_op_overload(op):

    def overload_series_explicit_binary_reverse_op(S, other, level=None,
        fill_value=None, axis=0):
        if not is_overload_none(level):
            raise BodoError('level argument not supported')
        if not is_overload_zero(axis):
            raise BodoError('axis argument not supported')
        if not isinstance(S.dtype, types.Number):
            raise BodoError('only numeric values supported')
        amyfi__kbhv = numba.core.registry.cpu_target.typing_context
        if isinstance(other, types.Number):
            args = other, S.data
            qrf__gyszv = amyfi__kbhv.resolve_function_type(op, args, {}
                ).return_type
            if isinstance(S.data, (IntegerArrayType, FloatingArrayType)
                ) and qrf__gyszv == types.Array(types.bool_, 1, 'C'):
                qrf__gyszv = boolean_array

            def impl_scalar(S, other, level=None, fill_value=None, axis=0):
                arr = bodo.hiframes.pd_series_ext.get_series_data(S)
                index = bodo.hiframes.pd_series_ext.get_series_index(S)
                name = bodo.hiframes.pd_series_ext.get_series_name(S)
                numba.parfors.parfor.init_prange()
                n = len(arr)
                wzmu__etpuf = bodo.utils.utils.alloc_type(n, qrf__gyszv, None)
                for ynjr__fnfp in numba.parfors.parfor.internal_prange(n):
                    kyx__zbz = bodo.libs.array_kernels.isna(arr, ynjr__fnfp)
                    if kyx__zbz:
                        if fill_value is None:
                            bodo.libs.array_kernels.setna(wzmu__etpuf,
                                ynjr__fnfp)
                        else:
                            wzmu__etpuf[ynjr__fnfp] = op(other, fill_value)
                    else:
                        wzmu__etpuf[ynjr__fnfp] = op(other, arr[ynjr__fnfp])
                return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                    index, name)
            return impl_scalar
        args = types.Array(other.dtype, 1, 'C'), S.data
        qrf__gyszv = amyfi__kbhv.resolve_function_type(op, args, {}
            ).return_type
        if isinstance(S.data, (IntegerArrayType, FloatingArrayType)
            ) and qrf__gyszv == types.Array(types.bool_, 1, 'C'):
            qrf__gyszv = boolean_array

        def impl(S, other, level=None, fill_value=None, axis=0):
            arr = bodo.hiframes.pd_series_ext.get_series_data(S)
            index = bodo.hiframes.pd_series_ext.get_series_index(S)
            name = bodo.hiframes.pd_series_ext.get_series_name(S)
            lpq__xrr = bodo.hiframes.pd_series_ext.get_series_data(other)
            numba.parfors.parfor.init_prange()
            n = len(arr)
            wzmu__etpuf = bodo.utils.utils.alloc_type(n, qrf__gyszv, None)
            for ynjr__fnfp in numba.parfors.parfor.internal_prange(n):
                kyx__zbz = bodo.libs.array_kernels.isna(arr, ynjr__fnfp)
                jtjfd__uac = bodo.libs.array_kernels.isna(lpq__xrr, ynjr__fnfp)
                wzmu__etpuf[ynjr__fnfp] = op(lpq__xrr[ynjr__fnfp], arr[
                    ynjr__fnfp])
                if kyx__zbz and jtjfd__uac:
                    bodo.libs.array_kernels.setna(wzmu__etpuf, ynjr__fnfp)
                elif kyx__zbz:
                    if fill_value is None:
                        bodo.libs.array_kernels.setna(wzmu__etpuf, ynjr__fnfp)
                    else:
                        wzmu__etpuf[ynjr__fnfp] = op(lpq__xrr[ynjr__fnfp],
                            fill_value)
                elif jtjfd__uac:
                    if fill_value is None:
                        bodo.libs.array_kernels.setna(wzmu__etpuf, ynjr__fnfp)
                    else:
                        wzmu__etpuf[ynjr__fnfp] = op(fill_value, arr[
                            ynjr__fnfp])
                else:
                    wzmu__etpuf[ynjr__fnfp] = op(lpq__xrr[ynjr__fnfp], arr[
                        ynjr__fnfp])
            return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                index, name)
        return impl
    return overload_series_explicit_binary_reverse_op


explicit_binop_funcs_two_ways = {operator.add: {'add'}, operator.sub: {
    'sub'}, operator.mul: {'mul'}, operator.truediv: {'div', 'truediv'},
    operator.floordiv: {'floordiv'}, operator.mod: {'mod'}, operator.pow: {
    'pow'}}
explicit_binop_funcs_single = {operator.lt: 'lt', operator.gt: 'gt',
    operator.le: 'le', operator.ge: 'ge', operator.ne: 'ne', operator.eq: 'eq'}
explicit_binop_funcs = set()
split_logical_binops_funcs = [operator.or_, operator.and_]


def _install_explicit_binary_ops():
    for op, bhyy__alhsh in explicit_binop_funcs_two_ways.items():
        for name in bhyy__alhsh:
            koqn__wykgs = create_explicit_binary_op_overload(op)
            gwa__rxla = create_explicit_binary_reverse_op_overload(op)
            fjzrh__bnmju = 'r' + name
            overload_method(SeriesType, name, no_unliteral=True)(koqn__wykgs)
            overload_method(SeriesType, fjzrh__bnmju, no_unliteral=True)(
                gwa__rxla)
            explicit_binop_funcs.add(name)
    for op, name in explicit_binop_funcs_single.items():
        koqn__wykgs = create_explicit_binary_op_overload(op)
        overload_method(SeriesType, name, no_unliteral=True)(koqn__wykgs)
        explicit_binop_funcs.add(name)


_install_explicit_binary_ops()


def create_binary_op_overload(op):

    def overload_series_binary_op(lhs, rhs):
        if (isinstance(lhs, SeriesType) and isinstance(rhs, SeriesType) and
            lhs.dtype == bodo.datetime64ns and rhs.dtype == bodo.
            datetime64ns and op == operator.sub):

            def impl_dt64(lhs, rhs):
                arr = bodo.hiframes.pd_series_ext.get_series_data(lhs)
                index = bodo.hiframes.pd_series_ext.get_series_index(lhs)
                name = bodo.hiframes.pd_series_ext.get_series_name(lhs)
                ajr__mtoul = (bodo.utils.conversion.
                    get_array_if_series_or_index(rhs))
                wzmu__etpuf = dt64_arr_sub(arr, ajr__mtoul)
                return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                    index, name)
            return impl_dt64
        if op in [operator.add, operator.sub] and isinstance(lhs, SeriesType
            ) and lhs.dtype == bodo.datetime64ns and is_offsets_type(rhs):

            def impl_offsets(lhs, rhs):
                arr = bodo.hiframes.pd_series_ext.get_series_data(lhs)
                index = bodo.hiframes.pd_series_ext.get_series_index(lhs)
                name = bodo.hiframes.pd_series_ext.get_series_name(lhs)
                numba.parfors.parfor.init_prange()
                n = len(lhs)
                wzmu__etpuf = np.empty(n, np.dtype('datetime64[ns]'))
                for ynjr__fnfp in numba.parfors.parfor.internal_prange(n):
                    if bodo.libs.array_kernels.isna(arr, ynjr__fnfp):
                        bodo.libs.array_kernels.setna(wzmu__etpuf, ynjr__fnfp)
                        continue
                    ugn__vlovy = (bodo.hiframes.pd_timestamp_ext.
                        convert_datetime64_to_timestamp(arr[ynjr__fnfp]))
                    yar__gli = op(ugn__vlovy, rhs)
                    wzmu__etpuf[ynjr__fnfp
                        ] = bodo.hiframes.pd_timestamp_ext.integer_to_dt64(
                        yar__gli.value)
                return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                    index, name)
            return impl_offsets
        if op == operator.add and is_offsets_type(lhs) and isinstance(rhs,
            SeriesType) and rhs.dtype == bodo.datetime64ns:

            def impl(lhs, rhs):
                return op(rhs, lhs)
            return impl
        if isinstance(lhs, SeriesType):
            if lhs.dtype in [bodo.datetime64ns, bodo.timedelta64ns]:

                def impl(lhs, rhs):
                    arr = bodo.hiframes.pd_series_ext.get_series_data(lhs)
                    index = bodo.hiframes.pd_series_ext.get_series_index(lhs)
                    name = bodo.hiframes.pd_series_ext.get_series_name(lhs)
                    ajr__mtoul = (bodo.utils.conversion.
                        get_array_if_series_or_index(rhs))
                    wzmu__etpuf = op(arr, bodo.utils.conversion.
                        unbox_if_tz_naive_timestamp(ajr__mtoul))
                    return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                        index, name)
                return impl

            def impl(lhs, rhs):
                arr = bodo.hiframes.pd_series_ext.get_series_data(lhs)
                index = bodo.hiframes.pd_series_ext.get_series_index(lhs)
                name = bodo.hiframes.pd_series_ext.get_series_name(lhs)
                ajr__mtoul = (bodo.utils.conversion.
                    get_array_if_series_or_index(rhs))
                wzmu__etpuf = op(arr, ajr__mtoul)
                return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                    index, name)
            return impl
        if isinstance(rhs, SeriesType):
            if rhs.dtype in [bodo.datetime64ns, bodo.timedelta64ns]:

                def impl(lhs, rhs):
                    arr = bodo.hiframes.pd_series_ext.get_series_data(rhs)
                    index = bodo.hiframes.pd_series_ext.get_series_index(rhs)
                    name = bodo.hiframes.pd_series_ext.get_series_name(rhs)
                    lqdz__pvldl = (bodo.utils.conversion.
                        get_array_if_series_or_index(lhs))
                    wzmu__etpuf = op(bodo.utils.conversion.
                        unbox_if_tz_naive_timestamp(lqdz__pvldl), arr)
                    return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                        index, name)
                return impl

            def impl(lhs, rhs):
                arr = bodo.hiframes.pd_series_ext.get_series_data(rhs)
                index = bodo.hiframes.pd_series_ext.get_series_index(rhs)
                name = bodo.hiframes.pd_series_ext.get_series_name(rhs)
                lqdz__pvldl = (bodo.utils.conversion.
                    get_array_if_series_or_index(lhs))
                wzmu__etpuf = op(lqdz__pvldl, arr)
                return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                    index, name)
            return impl
    return overload_series_binary_op


skips = list(explicit_binop_funcs_two_ways.keys()) + list(
    explicit_binop_funcs_single.keys()) + split_logical_binops_funcs


def _install_binary_ops():
    for op in bodo.hiframes.pd_series_ext.series_binary_ops:
        if op in skips:
            continue
        koqn__wykgs = create_binary_op_overload(op)
        overload(op)(koqn__wykgs)


_install_binary_ops()


def dt64_arr_sub(arg1, arg2):
    return arg1 - arg2


@overload(dt64_arr_sub, no_unliteral=True)
def overload_dt64_arr_sub(arg1, arg2):
    assert arg1 == types.Array(bodo.datetime64ns, 1, 'C'
        ) and arg2 == types.Array(bodo.datetime64ns, 1, 'C')
    agyx__nsen = np.dtype('timedelta64[ns]')

    def impl(arg1, arg2):
        numba.parfors.parfor.init_prange()
        n = len(arg1)
        S = np.empty(n, agyx__nsen)
        for ynjr__fnfp in numba.parfors.parfor.internal_prange(n):
            if bodo.libs.array_kernels.isna(arg1, ynjr__fnfp
                ) or bodo.libs.array_kernels.isna(arg2, ynjr__fnfp):
                bodo.libs.array_kernels.setna(S, ynjr__fnfp)
                continue
            S[ynjr__fnfp
                ] = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                bodo.hiframes.pd_timestamp_ext.dt64_to_integer(arg1[
                ynjr__fnfp]) - bodo.hiframes.pd_timestamp_ext.
                dt64_to_integer(arg2[ynjr__fnfp]))
        return S
    return impl


def create_inplace_binary_op_overload(op):

    def overload_series_inplace_binary_op(S, other):
        if isinstance(S, SeriesType) or isinstance(other, SeriesType):

            def impl(S, other):
                arr = bodo.utils.conversion.get_array_if_series_or_index(S)
                lpq__xrr = bodo.utils.conversion.get_array_if_series_or_index(
                    other)
                op(arr, lpq__xrr)
                return S
            return impl
    return overload_series_inplace_binary_op


def _install_inplace_binary_ops():
    for op in bodo.hiframes.pd_series_ext.series_inplace_binary_ops:
        koqn__wykgs = create_inplace_binary_op_overload(op)
        overload(op, no_unliteral=True)(koqn__wykgs)


_install_inplace_binary_ops()


def create_unary_op_overload(op):

    def overload_series_unary_op(S):
        if isinstance(S, SeriesType):

            def impl(S):
                arr = bodo.hiframes.pd_series_ext.get_series_data(S)
                index = bodo.hiframes.pd_series_ext.get_series_index(S)
                name = bodo.hiframes.pd_series_ext.get_series_name(S)
                wzmu__etpuf = op(arr)
                return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                    index, name)
            return impl
    return overload_series_unary_op


def _install_unary_ops():
    for op in bodo.hiframes.pd_series_ext.series_unary_ops:
        koqn__wykgs = create_unary_op_overload(op)
        overload(op, no_unliteral=True)(koqn__wykgs)


_install_unary_ops()


def create_ufunc_overload(ufunc):
    if ufunc.nin == 1:

        def overload_series_ufunc_nin_1(S):
            if isinstance(S, SeriesType):

                def impl(S):
                    arr = bodo.hiframes.pd_series_ext.get_series_data(S)
                    index = bodo.hiframes.pd_series_ext.get_series_index(S)
                    name = bodo.hiframes.pd_series_ext.get_series_name(S)
                    wzmu__etpuf = ufunc(arr)
                    return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                        index, name)
                return impl
        return overload_series_ufunc_nin_1
    elif ufunc.nin == 2:

        def overload_series_ufunc_nin_2(S1, S2):
            if isinstance(S1, SeriesType):

                def impl(S1, S2):
                    arr = bodo.hiframes.pd_series_ext.get_series_data(S1)
                    index = bodo.hiframes.pd_series_ext.get_series_index(S1)
                    name = bodo.hiframes.pd_series_ext.get_series_name(S1)
                    lpq__xrr = (bodo.utils.conversion.
                        get_array_if_series_or_index(S2))
                    wzmu__etpuf = ufunc(arr, lpq__xrr)
                    return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                        index, name)
                return impl
            elif isinstance(S2, SeriesType):

                def impl(S1, S2):
                    arr = bodo.utils.conversion.get_array_if_series_or_index(S1
                        )
                    lpq__xrr = bodo.hiframes.pd_series_ext.get_series_data(S2)
                    index = bodo.hiframes.pd_series_ext.get_series_index(S2)
                    name = bodo.hiframes.pd_series_ext.get_series_name(S2)
                    wzmu__etpuf = ufunc(arr, lpq__xrr)
                    return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                        index, name)
                return impl
        return overload_series_ufunc_nin_2
    else:
        raise RuntimeError(
            "Don't know how to register ufuncs from ufunc_db with arity > 2")


def _install_np_ufuncs():
    import numba.np.ufunc_db
    for ufunc in numba.np.ufunc_db.get_ufuncs():
        koqn__wykgs = create_ufunc_overload(ufunc)
        overload(ufunc, no_unliteral=True)(koqn__wykgs)


_install_np_ufuncs()


def argsort(A):
    return np.argsort(A)


@overload(argsort, no_unliteral=True)
def overload_argsort(A):

    def impl(A):
        n = len(A)
        ali__ayiz = bodo.libs.str_arr_ext.to_list_if_immutable_arr((A.copy(),))
        rdn__kvefx = np.arange(n),
        bodo.libs.timsort.sort(ali__ayiz, 0, n, rdn__kvefx)
        return rdn__kvefx[0]
    return impl


@overload(pd.to_numeric, inline='always', no_unliteral=True)
def overload_to_numeric(arg_a, errors='raise', downcast=None):
    if not is_overload_none(downcast) and not (is_overload_constant_str(
        downcast) and get_overload_const_str(downcast) in ('integer',
        'signed', 'unsigned', 'float')):
        raise BodoError(
            'pd.to_numeric(): invalid downcasting method provided {}'.
            format(downcast))
    out_dtype = types.float64
    if not is_overload_none(downcast):
        wtpvw__iaqg = get_overload_const_str(downcast)
        if wtpvw__iaqg in ('integer', 'signed'):
            out_dtype = types.int64
        elif wtpvw__iaqg == 'unsigned':
            out_dtype = types.uint64
        else:
            assert wtpvw__iaqg == 'float'
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(arg_a,
        'pandas.to_numeric()')
    if isinstance(arg_a, (types.Array, IntegerArrayType)):
        return lambda arg_a, errors='raise', downcast=None: arg_a.astype(
            out_dtype)
    if isinstance(arg_a, SeriesType):

        def impl_series(arg_a, errors='raise', downcast=None):
            iwuhx__bmy = bodo.hiframes.pd_series_ext.get_series_data(arg_a)
            index = bodo.hiframes.pd_series_ext.get_series_index(arg_a)
            name = bodo.hiframes.pd_series_ext.get_series_name(arg_a)
            wzmu__etpuf = pd.to_numeric(iwuhx__bmy, errors, downcast)
            return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                index, name)
        return impl_series
    if not is_str_arr_type(arg_a):
        raise BodoError(f'pd.to_numeric(): invalid argument type {arg_a}')
    if arg_a == bodo.dict_str_arr_type:
        return (lambda arg_a, errors='raise', downcast=None: bodo.libs.
            dict_arr_ext.dict_arr_to_numeric(arg_a, errors, downcast))
    vra__yvziy = types.Array(types.float64, 1, 'C'
        ) if out_dtype == types.float64 else IntegerArrayType(types.int64)

    def to_numeric_impl(arg_a, errors='raise', downcast=None):
        numba.parfors.parfor.init_prange()
        n = len(arg_a)
        vtd__ndtly = bodo.utils.utils.alloc_type(n, vra__yvziy, (-1,))
        for ynjr__fnfp in numba.parfors.parfor.internal_prange(n):
            if bodo.libs.array_kernels.isna(arg_a, ynjr__fnfp):
                bodo.libs.array_kernels.setna(vtd__ndtly, ynjr__fnfp)
            else:
                bodo.libs.str_arr_ext.str_arr_item_to_numeric(vtd__ndtly,
                    ynjr__fnfp, arg_a, ynjr__fnfp)
        return vtd__ndtly
    return to_numeric_impl


def series_filter_bool(arr, bool_arr):
    return arr[bool_arr]


@infer_global(series_filter_bool)
class SeriesFilterBoolInfer(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        assert len(args) == 2
        llna__qzh = if_series_to_array_type(args[0])
        if isinstance(llna__qzh, types.Array) and isinstance(llna__qzh.
            dtype, types.Integer):
            llna__qzh = types.Array(types.float64, 1, 'C')
        return llna__qzh(*args)


def where_impl_one_arg(c):
    return np.where(c)


@overload(where_impl_one_arg, no_unliteral=True)
def overload_where_unsupported_one_arg(condition):
    if isinstance(condition, SeriesType) or bodo.utils.utils.is_array_typ(
        condition, False):
        return lambda condition: np.where(condition)


def overload_np_where_one_arg(condition):
    if isinstance(condition, SeriesType):

        def impl_series(condition):
            condition = bodo.hiframes.pd_series_ext.get_series_data(condition)
            return bodo.libs.array_kernels.nonzero(condition)
        return impl_series
    elif bodo.utils.utils.is_array_typ(condition, False):

        def impl(condition):
            return bodo.libs.array_kernels.nonzero(condition)
        return impl


overload(np.where, inline='always', no_unliteral=True)(
    overload_np_where_one_arg)
overload(where_impl_one_arg, inline='always', no_unliteral=True)(
    overload_np_where_one_arg)


def where_impl(c, x, y):
    return np.where(c, x, y)


@overload(where_impl, no_unliteral=True)
def overload_where_unsupported(condition, x, y):
    if not isinstance(condition, (SeriesType, types.Array, BooleanArrayType)
        ) or condition.ndim != 1:
        return lambda condition, x, y: np.where(condition, x, y)


@overload(where_impl, no_unliteral=True)
@overload(np.where, no_unliteral=True)
def overload_np_where(condition, x, y):
    if not isinstance(condition, (SeriesType, types.Array, BooleanArrayType)
        ) or condition.ndim != 1:
        return
    assert condition.dtype == types.bool_, 'invalid condition dtype'
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(x,
        'numpy.where()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(y,
        'numpy.where()')
    lripx__ptmka = bodo.utils.utils.is_array_typ(x, True)
    ilq__sfhd = bodo.utils.utils.is_array_typ(y, True)
    deqe__ahp = 'def _impl(condition, x, y):\n'
    if isinstance(condition, SeriesType):
        deqe__ahp += (
            '  condition = bodo.hiframes.pd_series_ext.get_series_data(condition)\n'
            )
    if lripx__ptmka and not bodo.utils.utils.is_array_typ(x, False):
        deqe__ahp += '  x = bodo.utils.conversion.coerce_to_array(x)\n'
    if ilq__sfhd and not bodo.utils.utils.is_array_typ(y, False):
        deqe__ahp += '  y = bodo.utils.conversion.coerce_to_array(y)\n'
    deqe__ahp += '  n = len(condition)\n'
    nyg__zsr = x.dtype if lripx__ptmka else types.unliteral(x)
    tsdop__tlqk = y.dtype if ilq__sfhd else types.unliteral(y)
    if not isinstance(x, CategoricalArrayType):
        nyg__zsr = element_type(x)
    if not isinstance(y, CategoricalArrayType):
        tsdop__tlqk = element_type(y)

    def get_data(x):
        if isinstance(x, SeriesType):
            return x.data
        elif isinstance(x, types.Array):
            return x
        return types.unliteral(x)
    kpf__yvvmf = get_data(x)
    vtg__aehe = get_data(y)
    is_nullable = any(bodo.utils.typing.is_nullable(rdn__kvefx) for
        rdn__kvefx in [kpf__yvvmf, vtg__aehe])
    if vtg__aehe == types.none:
        if isinstance(nyg__zsr, types.Number):
            out_dtype = types.Array(types.float64, 1, 'C')
        else:
            out_dtype = to_nullable_type(x)
    elif kpf__yvvmf == vtg__aehe and not is_nullable:
        out_dtype = dtype_to_array_type(nyg__zsr)
    elif nyg__zsr == string_type or tsdop__tlqk == string_type:
        out_dtype = bodo.string_array_type
    elif kpf__yvvmf == bytes_type or (lripx__ptmka and nyg__zsr == bytes_type
        ) and (vtg__aehe == bytes_type or ilq__sfhd and tsdop__tlqk ==
        bytes_type):
        out_dtype = binary_array_type
    elif isinstance(nyg__zsr, bodo.PDCategoricalDtype):
        out_dtype = None
    elif nyg__zsr in [bodo.timedelta64ns, bodo.datetime64ns]:
        out_dtype = types.Array(nyg__zsr, 1, 'C')
    elif tsdop__tlqk in [bodo.timedelta64ns, bodo.datetime64ns]:
        out_dtype = types.Array(tsdop__tlqk, 1, 'C')
    else:
        out_dtype = numba.from_dtype(np.promote_types(numba.np.
            numpy_support.as_dtype(nyg__zsr), numba.np.numpy_support.
            as_dtype(tsdop__tlqk)))
        out_dtype = types.Array(out_dtype, 1, 'C')
        if is_nullable:
            out_dtype = bodo.utils.typing.to_nullable_type(out_dtype)
    if isinstance(nyg__zsr, bodo.PDCategoricalDtype):
        ptp__kzbf = 'x'
    else:
        ptp__kzbf = 'out_dtype'
    deqe__ahp += (
        f'  out_arr = bodo.utils.utils.alloc_type(n, {ptp__kzbf}, (-1,))\n')
    if isinstance(nyg__zsr, bodo.PDCategoricalDtype):
        deqe__ahp += """  out_codes = bodo.hiframes.pd_categorical_ext.get_categorical_arr_codes(out_arr)
"""
        deqe__ahp += (
            '  x_codes = bodo.hiframes.pd_categorical_ext.get_categorical_arr_codes(x)\n'
            )
    deqe__ahp += '  for j in numba.parfors.parfor.internal_prange(n):\n'
    deqe__ahp += (
        '    if not bodo.libs.array_kernels.isna(condition, j) and condition[j]:\n'
        )
    if lripx__ptmka:
        deqe__ahp += '      if bodo.libs.array_kernels.isna(x, j):\n'
        deqe__ahp += '        setna(out_arr, j)\n'
        deqe__ahp += '        continue\n'
    if isinstance(nyg__zsr, bodo.PDCategoricalDtype):
        deqe__ahp += '      out_codes[j] = x_codes[j]\n'
    else:
        deqe__ahp += (
            '      out_arr[j] = bodo.utils.conversion.unbox_if_tz_naive_timestamp({})\n'
            .format('x[j]' if lripx__ptmka else 'x'))
    deqe__ahp += '    else:\n'
    if ilq__sfhd:
        deqe__ahp += '      if bodo.libs.array_kernels.isna(y, j):\n'
        deqe__ahp += '        setna(out_arr, j)\n'
        deqe__ahp += '        continue\n'
    if vtg__aehe == types.none:
        if isinstance(nyg__zsr, bodo.PDCategoricalDtype):
            deqe__ahp += '      out_codes[j] = -1\n'
        else:
            deqe__ahp += '      setna(out_arr, j)\n'
    else:
        deqe__ahp += (
            '      out_arr[j] = bodo.utils.conversion.unbox_if_tz_naive_timestamp({})\n'
            .format('y[j]' if ilq__sfhd else 'y'))
    deqe__ahp += '  return out_arr\n'
    nii__tveq = {}
    exec(deqe__ahp, {'bodo': bodo, 'numba': numba, 'setna': bodo.libs.
        array_kernels.setna, 'np': np, 'out_dtype': out_dtype}, nii__tveq)
    lzfr__vaom = nii__tveq['_impl']
    return lzfr__vaom


def _verify_np_select_arg_typs(condlist, choicelist, default):
    if isinstance(condlist, (types.List, types.UniTuple)):
        if not (bodo.utils.utils.is_np_array_typ(condlist.dtype) and 
            condlist.dtype.dtype == types.bool_):
            raise BodoError(
                "np.select(): 'condlist' argument must be list or tuple of boolean ndarrays. If passing a Series, please convert with pd.Series.to_numpy()."
                )
    else:
        raise BodoError(
            "np.select(): 'condlist' argument must be list or tuple of boolean ndarrays. If passing a Series, please convert with pd.Series.to_numpy()."
            )
    if not isinstance(choicelist, (types.List, types.UniTuple, types.BaseTuple)
        ):
        raise BodoError(
            "np.select(): 'choicelist' argument must be list or tuple type")
    if isinstance(choicelist, (types.List, types.UniTuple)):
        ndw__avzgb = choicelist.dtype
        if not bodo.utils.utils.is_array_typ(ndw__avzgb, True):
            raise BodoError(
                "np.select(): 'choicelist' argument must be list or tuple of series/arrays types"
                )
        if is_series_type(ndw__avzgb):
            atdgf__kfntr = ndw__avzgb.data.dtype
        else:
            atdgf__kfntr = ndw__avzgb.dtype
        if isinstance(atdgf__kfntr, bodo.PDCategoricalDtype):
            raise BodoError(
                'np.select(): data with choicelist of type Categorical not yet supported'
                )
        zuw__nuok = ndw__avzgb
    else:
        paka__tepw = []
        for ndw__avzgb in choicelist:
            if not bodo.utils.utils.is_array_typ(ndw__avzgb, True):
                raise BodoError(
                    "np.select(): 'choicelist' argument must be list or tuple of series/arrays types"
                    )
            if is_series_type(ndw__avzgb):
                atdgf__kfntr = ndw__avzgb.data.dtype
            else:
                atdgf__kfntr = ndw__avzgb.dtype
            if isinstance(atdgf__kfntr, bodo.PDCategoricalDtype):
                raise BodoError(
                    'np.select(): data with choicelist of type Categorical not yet supported'
                    )
            paka__tepw.append(atdgf__kfntr)
        if not is_common_scalar_dtype(paka__tepw):
            raise BodoError(
                f"np.select(): 'choicelist' items must be arrays with a commmon data type. Found a tuple with the following data types {choicelist}."
                )
        zuw__nuok = choicelist[0]
    if is_series_type(zuw__nuok):
        zuw__nuok = zuw__nuok.data
    if is_overload_constant_int(default) and get_overload_const_int(default
        ) == 0:
        pass
    else:
        if not is_scalar_type(default):
            raise BodoError(
                "np.select(): 'default' argument must be scalar type")
        if not (is_common_scalar_dtype([default, zuw__nuok.dtype]) or 
            default == types.none or is_overload_constant_nan(default)):
            raise BodoError(
                f"np.select(): 'default' is not type compatible with the array types in choicelist. Choicelist type: {choicelist}, Default type: {default}"
                )
    if not (isinstance(zuw__nuok, types.Array) or isinstance(zuw__nuok,
        BooleanArrayType) or isinstance(zuw__nuok, IntegerArrayType) or
        isinstance(zuw__nuok, FloatingArrayType) or bodo.utils.utils.
        is_array_typ(zuw__nuok, False) and zuw__nuok.dtype in [bodo.
        string_type, bodo.bytes_type]):
        raise BodoError(
            f'np.select(): data with choicelist of type {zuw__nuok} not yet supported'
            )


@overload(np.select)
def overload_np_select(condlist, choicelist, default=0):
    _verify_np_select_arg_typs(condlist, choicelist, default)
    ekj__fuvw = isinstance(choicelist, (types.List, types.UniTuple)
        ) and isinstance(condlist, (types.List, types.UniTuple))
    if isinstance(choicelist, (types.List, types.UniTuple)):
        dvuva__agy = choicelist.dtype
    else:
        nwg__hgqb = False
        paka__tepw = []
        for ndw__avzgb in choicelist:
            bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(
                ndw__avzgb, 'numpy.select()')
            if is_nullable_type(ndw__avzgb):
                nwg__hgqb = True
            if is_series_type(ndw__avzgb):
                atdgf__kfntr = ndw__avzgb.data.dtype
            else:
                atdgf__kfntr = ndw__avzgb.dtype
            if isinstance(atdgf__kfntr, bodo.PDCategoricalDtype):
                raise BodoError(
                    'np.select(): data with choicelist of type Categorical not yet supported'
                    )
            paka__tepw.append(atdgf__kfntr)
        uiiy__apvb, klxyi__kbr = get_common_scalar_dtype(paka__tepw)
        if not klxyi__kbr:
            raise BodoError('Internal error in overload_np_select')
        krxfa__qmj = dtype_to_array_type(uiiy__apvb)
        if nwg__hgqb:
            krxfa__qmj = to_nullable_type(krxfa__qmj)
        dvuva__agy = krxfa__qmj
    if isinstance(dvuva__agy, SeriesType):
        dvuva__agy = dvuva__agy.data
    if is_overload_constant_int(default) and get_overload_const_int(default
        ) == 0:
        qiz__sfo = True
    else:
        qiz__sfo = False
    gsjn__lhafe = False
    qqfx__vounk = False
    if qiz__sfo:
        if isinstance(dvuva__agy.dtype, types.Number):
            pass
        elif dvuva__agy.dtype == types.bool_:
            qqfx__vounk = True
        else:
            gsjn__lhafe = True
            dvuva__agy = to_nullable_type(dvuva__agy)
    elif default == types.none or is_overload_constant_nan(default):
        gsjn__lhafe = True
        dvuva__agy = to_nullable_type(dvuva__agy)
    deqe__ahp = 'def np_select_impl(condlist, choicelist, default=0):\n'
    deqe__ahp += '  if len(condlist) != len(choicelist):\n'
    deqe__ahp += """    raise ValueError('list of cases must be same length as list of conditions')
"""
    deqe__ahp += '  output_len = len(choicelist[0])\n'
    deqe__ahp += (
        '  out = bodo.utils.utils.alloc_type(output_len, alloc_typ, (-1,))\n')
    deqe__ahp += '  for i in range(output_len):\n'
    if gsjn__lhafe:
        deqe__ahp += '    bodo.libs.array_kernels.setna(out, i)\n'
    elif qqfx__vounk:
        deqe__ahp += '    out[i] = False\n'
    else:
        deqe__ahp += '    out[i] = default\n'
    if ekj__fuvw:
        deqe__ahp += '  for i in range(len(condlist) - 1, -1, -1):\n'
        deqe__ahp += '    cond = condlist[i]\n'
        deqe__ahp += '    choice = choicelist[i]\n'
        deqe__ahp += '    out = np.where(cond, choice, out)\n'
    else:
        for ynjr__fnfp in range(len(choicelist) - 1, -1, -1):
            deqe__ahp += f'  cond = condlist[{ynjr__fnfp}]\n'
            deqe__ahp += f'  choice = choicelist[{ynjr__fnfp}]\n'
            deqe__ahp += f'  out = np.where(cond, choice, out)\n'
    deqe__ahp += '  return out'
    nii__tveq = dict()
    exec(deqe__ahp, {'bodo': bodo, 'numba': numba, 'setna': bodo.libs.
        array_kernels.setna, 'np': np, 'alloc_typ': dvuva__agy}, nii__tveq)
    impl = nii__tveq['np_select_impl']
    return impl


@overload_method(SeriesType, 'duplicated', inline='always', no_unliteral=True)
def overload_series_duplicated(S, keep='first'):

    def impl(S, keep='first'):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        wzmu__etpuf = bodo.libs.array_kernels.duplicated((arr,))
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf, index, name
            )
    return impl


@overload_method(SeriesType, 'drop_duplicates', inline='always',
    no_unliteral=True)
def overload_series_drop_duplicates(S, subset=None, keep='first', inplace=False
    ):
    yppn__bgd = dict(subset=subset, keep=keep, inplace=inplace)
    ihi__bqwp = dict(subset=None, keep='first', inplace=False)
    check_unsupported_args('Series.drop_duplicates', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')

    def impl(S, subset=None, keep='first', inplace=False):
        krg__pds = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.utils.conversion.index_to_array(bodo.hiframes.
            pd_series_ext.get_series_index(S))
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        (krg__pds,), cieta__wodph = bodo.libs.array_kernels.drop_duplicates((
            krg__pds,), index, 1)
        index = bodo.utils.conversion.index_from_array(cieta__wodph)
        return bodo.hiframes.pd_series_ext.init_series(krg__pds, index, name)
    return impl


@overload_method(SeriesType, 'between', inline='always', no_unliteral=True)
def overload_series_between(S, left, right, inclusive='both'):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.between()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(left,
        'Series.between()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(right,
        'Series.between()')
    fcyn__rrsqv = element_type(S.data)
    if not is_common_scalar_dtype([fcyn__rrsqv, left]):
        raise_bodo_error(
            "Series.between(): 'left' must be compariable with the Series data"
            )
    if not is_common_scalar_dtype([fcyn__rrsqv, right]):
        raise_bodo_error(
            "Series.between(): 'right' must be compariable with the Series data"
            )
    if not is_overload_constant_str(inclusive) or get_overload_const_str(
        inclusive) not in ('both', 'neither'):
        raise_bodo_error(
            "Series.between(): 'inclusive' must be a constant string and one of ('both', 'neither')"
            )

    def impl(S, left, right, inclusive='both'):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        numba.parfors.parfor.init_prange()
        n = len(arr)
        wzmu__etpuf = bodo.libs.bool_arr_ext.alloc_bool_array(n)
        for ynjr__fnfp in numba.parfors.parfor.internal_prange(n):
            if bodo.libs.array_kernels.isna(arr, ynjr__fnfp):
                bodo.libs.array_kernels.setna(wzmu__etpuf, ynjr__fnfp)
                continue
            xakhd__wjd = bodo.utils.conversion.box_if_dt64(arr[ynjr__fnfp])
            if inclusive == 'both':
                wzmu__etpuf[ynjr__fnfp
                    ] = xakhd__wjd <= right and xakhd__wjd >= left
            else:
                wzmu__etpuf[ynjr__fnfp
                    ] = xakhd__wjd < right and xakhd__wjd > left
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf, index, name
            )
    return impl


@overload_method(SeriesType, 'repeat', inline='always', no_unliteral=True)
def overload_series_repeat(S, repeats, axis=None):
    yppn__bgd = dict(axis=axis)
    ihi__bqwp = dict(axis=None)
    check_unsupported_args('Series.repeat', yppn__bgd, ihi__bqwp,
        package_name='pandas', module_name='Series')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S,
        'Series.repeat()')
    if not (isinstance(repeats, types.Integer) or is_iterable_type(repeats) and
        isinstance(repeats.dtype, types.Integer)):
        raise BodoError(
            "Series.repeat(): 'repeats' should be an integer or array of integers"
            )
    if isinstance(repeats, types.Integer):

        def impl_int(S, repeats, axis=None):
            arr = bodo.hiframes.pd_series_ext.get_series_data(S)
            index = bodo.hiframes.pd_series_ext.get_series_index(S)
            name = bodo.hiframes.pd_series_ext.get_series_name(S)
            cieta__wodph = bodo.utils.conversion.index_to_array(index)
            wzmu__etpuf = bodo.libs.array_kernels.repeat_kernel(arr, repeats)
            oaj__syo = bodo.libs.array_kernels.repeat_kernel(cieta__wodph,
                repeats)
            qdyl__gas = bodo.utils.conversion.index_from_array(oaj__syo)
            return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
                qdyl__gas, name)
        return impl_int

    def impl_arr(S, repeats, axis=None):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        name = bodo.hiframes.pd_series_ext.get_series_name(S)
        cieta__wodph = bodo.utils.conversion.index_to_array(index)
        repeats = bodo.utils.conversion.coerce_to_array(repeats)
        wzmu__etpuf = bodo.libs.array_kernels.repeat_kernel(arr, repeats)
        oaj__syo = bodo.libs.array_kernels.repeat_kernel(cieta__wodph, repeats)
        qdyl__gas = bodo.utils.conversion.index_from_array(oaj__syo)
        return bodo.hiframes.pd_series_ext.init_series(wzmu__etpuf,
            qdyl__gas, name)
    return impl_arr


@overload_method(SeriesType, 'to_dict', no_unliteral=True)
def overload_to_dict(S, into=None):

    def impl(S, into=None):
        rdn__kvefx = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.utils.conversion.index_to_array(bodo.hiframes.
            pd_series_ext.get_series_index(S))
        n = len(rdn__kvefx)
        ofz__yttom = {}
        for ynjr__fnfp in range(n):
            xakhd__wjd = bodo.utils.conversion.box_if_dt64(rdn__kvefx[
                ynjr__fnfp])
            ofz__yttom[index[ynjr__fnfp]] = xakhd__wjd
        return ofz__yttom
    return impl


@overload_method(SeriesType, 'to_frame', inline='always', no_unliteral=True)
def overload_series_to_frame(S, name=None):
    uhqd__uess = (
        "Series.to_frame(): output column name should be known at compile time. Set 'name' to a constant value."
        )
    if is_overload_none(name):
        if is_literal_type(S.name_typ):
            vari__ook = get_literal_value(S.name_typ)
        else:
            raise_bodo_error(uhqd__uess)
    elif is_literal_type(name):
        vari__ook = get_literal_value(name)
    else:
        raise_bodo_error(uhqd__uess)
    vari__ook = 0 if vari__ook is None else vari__ook
    oeaoi__yftlg = ColNamesMetaType((vari__ook,))

    def impl(S, name=None):
        arr = bodo.hiframes.pd_series_ext.get_series_data(S)
        index = bodo.hiframes.pd_series_ext.get_series_index(S)
        return bodo.hiframes.pd_dataframe_ext.init_dataframe((arr,), index,
            oeaoi__yftlg)
    return impl


@overload_method(SeriesType, 'keys', inline='always', no_unliteral=True)
def overload_series_keys(S):

    def impl(S):
        return bodo.hiframes.pd_series_ext.get_series_index(S)
    return impl
