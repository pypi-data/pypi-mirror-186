"""
Implementation of DataFrame attributes and methods using overload.
"""
import operator
import re
import warnings
from collections import namedtuple
from typing import Tuple
import numba
import numpy as np
import pandas as pd
from numba.core import cgutils, ir, types
from numba.core.imputils import RefType, impl_ret_borrowed, impl_ret_new_ref, iternext_impl, lower_builtin
from numba.core.ir_utils import mk_unique_var, next_label
from numba.core.typing import signature
from numba.core.typing.templates import AbstractTemplate, infer_global
from numba.extending import lower_getattr, models, overload, overload_attribute, overload_method, register_model, type_callable
import bodo
from bodo.hiframes.datetime_date_ext import datetime_date_array_type
from bodo.hiframes.datetime_timedelta_ext import _no_input, datetime_timedelta_array_type
from bodo.hiframes.pd_categorical_ext import CategoricalArrayType
from bodo.hiframes.pd_dataframe_ext import DataFrameType, check_runtime_cols_unsupported, handle_inplace_df_type_change
from bodo.hiframes.pd_index_ext import DatetimeIndexType, RangeIndexType, StringIndexType, is_pd_index_type
from bodo.hiframes.pd_multi_index_ext import MultiIndexType
from bodo.hiframes.pd_series_ext import SeriesType, if_series_to_array_type
from bodo.hiframes.pd_timestamp_ext import pd_timestamp_tz_naive_type
from bodo.hiframes.rolling import is_supported_shift_array_type
from bodo.hiframes.split_impl import string_array_split_view_type
from bodo.hiframes.time_ext import TimeArrayType
from bodo.libs.array_item_arr_ext import ArrayItemArrayType
from bodo.libs.binary_arr_ext import binary_array_type
from bodo.libs.bool_arr_ext import BooleanArrayType, boolean_array
from bodo.libs.decimal_arr_ext import DecimalArrayType
from bodo.libs.dict_arr_ext import dict_str_arr_type
from bodo.libs.float_arr_ext import FloatingArrayType
from bodo.libs.int_arr_ext import IntegerArrayType
from bodo.libs.interval_arr_ext import IntervalArrayType
from bodo.libs.map_arr_ext import MapArrayType
from bodo.libs.str_arr_ext import string_array_type
from bodo.libs.str_ext import string_type
from bodo.libs.struct_arr_ext import StructArrayType
from bodo.utils import tracing
from bodo.utils.transform import bodo_types_with_params, gen_const_tup, no_side_effect_call_tuples
from bodo.utils.typing import BodoError, BodoWarning, ColNamesMetaType, check_unsupported_args, dtype_to_array_type, ensure_constant_arg, ensure_constant_values, get_castable_arr_dtype, get_index_data_arr_types, get_index_names, get_literal_value, get_nullable_and_non_nullable_types, get_overload_const_bool, get_overload_const_int, get_overload_const_list, get_overload_const_str, get_overload_const_tuple, get_overload_constant_dict, get_overload_constant_series, is_common_scalar_dtype, is_literal_type, is_overload_bool, is_overload_bool_list, is_overload_constant_bool, is_overload_constant_dict, is_overload_constant_int, is_overload_constant_list, is_overload_constant_series, is_overload_constant_str, is_overload_constant_tuple, is_overload_false, is_overload_int, is_overload_none, is_overload_true, is_overload_zero, is_scalar_type, parse_dtype, raise_bodo_error, unliteral_val
from bodo.utils.utils import is_array_typ


@overload_attribute(DataFrameType, 'index', inline='always')
def overload_dataframe_index(df):
    return lambda df: bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)


def generate_col_to_index_func_text(col_names: Tuple):
    if all(isinstance(a, str) for a in col_names) or all(isinstance(a,
        bytes) for a in col_names):
        vcw__bju = f'bodo.utils.conversion.coerce_to_array({col_names})'
        return (
            f'bodo.hiframes.pd_index_ext.init_binary_str_index({vcw__bju})\n')
    elif all(isinstance(a, (int, float)) for a in col_names):
        arr = f'bodo.utils.conversion.coerce_to_array({col_names})'
        return f'bodo.hiframes.pd_index_ext.init_numeric_index({arr})\n'
    else:
        return f'bodo.hiframes.pd_index_ext.init_heter_index({col_names})\n'


@overload_attribute(DataFrameType, 'columns', inline='always')
def overload_dataframe_columns(df):
    xood__fcig = 'def impl(df):\n'
    if df.has_runtime_cols:
        xood__fcig += (
            '  return bodo.hiframes.pd_dataframe_ext.get_dataframe_column_names(df)\n'
            )
    else:
        rlgfr__rjnej = (bodo.hiframes.dataframe_impl.
            generate_col_to_index_func_text(df.columns))
        xood__fcig += f'  return {rlgfr__rjnej}'
    hrbgo__eykz = {}
    exec(xood__fcig, {'bodo': bodo}, hrbgo__eykz)
    impl = hrbgo__eykz['impl']
    return impl


@overload_attribute(DataFrameType, 'values')
def overload_dataframe_values(df):
    check_runtime_cols_unsupported(df, 'DataFrame.values')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.values')
    if not is_df_values_numpy_supported_dftyp(df):
        raise_bodo_error(
            'DataFrame.values: only supported for dataframes containing numeric values'
            )
    iryek__rfuyn = len(df.columns)
    bnp__kvz = set(i for i in range(iryek__rfuyn) if isinstance(df.data[i],
        IntegerArrayType))
    data_args = ', '.join(
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {}){}'.
        format(i, '.astype(float)' if i in bnp__kvz else '') for i in range
        (iryek__rfuyn))
    xood__fcig = 'def f(df):\n'.format()
    xood__fcig += '    return np.stack(({},), 1)\n'.format(data_args)
    hrbgo__eykz = {}
    exec(xood__fcig, {'bodo': bodo, 'np': np}, hrbgo__eykz)
    sbtpq__bgkdx = hrbgo__eykz['f']
    return sbtpq__bgkdx


@overload_method(DataFrameType, 'to_numpy', inline='always', no_unliteral=True)
def overload_dataframe_to_numpy(df, dtype=None, copy=False, na_value=_no_input
    ):
    check_runtime_cols_unsupported(df, 'DataFrame.to_numpy()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.to_numpy()')
    if not is_df_values_numpy_supported_dftyp(df):
        raise_bodo_error(
            'DataFrame.to_numpy(): only supported for dataframes containing numeric values'
            )
    hsn__bxq = {'dtype': dtype, 'na_value': na_value}
    mawl__wldaq = {'dtype': None, 'na_value': _no_input}
    check_unsupported_args('DataFrame.to_numpy', hsn__bxq, mawl__wldaq,
        package_name='pandas', module_name='DataFrame')

    def impl(df, dtype=None, copy=False, na_value=_no_input):
        return df.values
    return impl


@overload_attribute(DataFrameType, 'ndim', inline='always')
def overload_dataframe_ndim(df):
    return lambda df: 2


@overload_attribute(DataFrameType, 'size')
def overload_dataframe_size(df):
    if df.has_runtime_cols:

        def impl(df):
            t = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)
            gcda__yenmt = bodo.hiframes.table.compute_num_runtime_columns(t)
            return gcda__yenmt * len(t)
        return impl
    ncols = len(df.columns)
    return lambda df: ncols * len(df)


@lower_getattr(DataFrameType, 'shape')
def lower_dataframe_shape(context, builder, typ, val):
    impl = overload_dataframe_shape(typ)
    return context.compile_internal(builder, impl, types.Tuple([types.int64,
        types.int64])(typ), (val,))


def overload_dataframe_shape(df):
    if df.has_runtime_cols:

        def impl(df):
            t = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)
            gcda__yenmt = bodo.hiframes.table.compute_num_runtime_columns(t)
            return len(t), gcda__yenmt
        return impl
    ncols = len(df.columns)
    return lambda df: (len(df), ncols)


@overload_attribute(DataFrameType, 'dtypes')
def overload_dataframe_dtypes(df):
    check_runtime_cols_unsupported(df, 'DataFrame.dtypes')
    xood__fcig = 'def impl(df):\n'
    data = ', '.join(
        f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}).dtype\n'
         for i in range(len(df.columns)))
    csm__pusld = ',' if len(df.columns) == 1 else ''
    index = f'bodo.hiframes.pd_index_ext.init_heter_index({df.columns})'
    xood__fcig += f"""  return bodo.hiframes.pd_series_ext.init_series(({data}{csm__pusld}), {index}, None)
"""
    hrbgo__eykz = {}
    exec(xood__fcig, {'bodo': bodo}, hrbgo__eykz)
    impl = hrbgo__eykz['impl']
    return impl


@overload_attribute(DataFrameType, 'empty')
def overload_dataframe_empty(df):
    check_runtime_cols_unsupported(df, 'DataFrame.empty')
    if len(df.columns) == 0:
        return lambda df: True
    return lambda df: len(df) == 0


@overload_method(DataFrameType, 'assign', no_unliteral=True)
def overload_dataframe_assign(df, **kwargs):
    check_runtime_cols_unsupported(df, 'DataFrame.assign()')
    raise_bodo_error('Invalid df.assign() call')


@overload_method(DataFrameType, 'insert', no_unliteral=True)
def overload_dataframe_insert(df, loc, column, value, allow_duplicates=False):
    check_runtime_cols_unsupported(df, 'DataFrame.insert()')
    raise_bodo_error('Invalid df.insert() call')


def _get_dtype_str(dtype):
    if isinstance(dtype, types.Function):
        if dtype.key[0] == str:
            return "'str'"
        elif dtype.key[0] == float:
            return 'float'
        elif dtype.key[0] == int:
            return 'int'
        elif dtype.key[0] == bool:
            return 'bool'
        else:
            raise BodoError(f'invalid dtype: {dtype}')
    if type(dtype) in bodo.libs.int_arr_ext.pd_int_dtype_classes:
        return dtype.name
    if isinstance(dtype, types.DTypeSpec):
        dtype = dtype.dtype
    if isinstance(dtype, types.functions.NumberClass):
        return f"'{dtype.key}'"
    if isinstance(dtype, types.PyObject) or dtype in (object, 'object'):
        return "'object'"
    if dtype in (bodo.libs.str_arr_ext.string_dtype, pd.StringDtype()):
        return 'str'
    return f"'{dtype}'"


@overload_method(DataFrameType, 'astype', inline='always', no_unliteral=True)
def overload_dataframe_astype(df, dtype, copy=True, errors='raise',
    _bodo_nan_to_str=True, _bodo_object_typeref=None):
    check_runtime_cols_unsupported(df, 'DataFrame.astype()')
    hsn__bxq = {'errors': errors}
    mawl__wldaq = {'errors': 'raise'}
    check_unsupported_args('df.astype', hsn__bxq, mawl__wldaq, package_name
        ='pandas', module_name='DataFrame')
    if dtype == types.unicode_type:
        raise_bodo_error(
            "DataFrame.astype(): 'dtype' when passed as string must be a constant value"
            )
    if not is_overload_bool(copy):
        raise BodoError("DataFrame.astype(): 'copy' must be a boolean value")
    extra_globals = None
    header = """def impl(df, dtype, copy=True, errors='raise', _bodo_nan_to_str=True, _bodo_object_typeref=None):
"""
    if df.is_table_format:
        extra_globals = {}
        header += (
            '  table = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)\n'
            )
        faovb__zku = []
    if _bodo_object_typeref is not None:
        assert isinstance(_bodo_object_typeref, types.TypeRef
            ), 'Bodo schema used in DataFrame.astype should be a TypeRef'
        hsk__mdrbn = _bodo_object_typeref.instance_type
        assert isinstance(hsk__mdrbn, DataFrameType
            ), 'Bodo schema used in DataFrame.astype is only supported for DataFrame schemas'
        if df.is_table_format:
            for i, name in enumerate(df.columns):
                if name in hsk__mdrbn.column_index:
                    idx = hsk__mdrbn.column_index[name]
                    arr_typ = hsk__mdrbn.data[idx]
                else:
                    arr_typ = df.data[i]
                faovb__zku.append(arr_typ)
        else:
            extra_globals = {}
            rzgk__eaotr = {}
            for i, name in enumerate(hsk__mdrbn.columns):
                arr_typ = hsk__mdrbn.data[i]
                extra_globals[f'_bodo_schema{i}'] = get_castable_arr_dtype(
                    arr_typ)
                rzgk__eaotr[name] = f'_bodo_schema{i}'
            data_args = ', '.join(
                f'bodo.utils.conversion.fix_arr_dtype(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}), {rzgk__eaotr[ahner__puklw]}, copy, nan_to_str=_bodo_nan_to_str, from_series=True)'
                 if ahner__puklw in rzgk__eaotr else
                f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})'
                 for i, ahner__puklw in enumerate(df.columns))
    elif is_overload_constant_dict(dtype) or is_overload_constant_series(dtype
        ):
        vhiqa__spoh = get_overload_constant_dict(dtype
            ) if is_overload_constant_dict(dtype) else dict(
            get_overload_constant_series(dtype))
        if df.is_table_format:
            vhiqa__spoh = {name: dtype_to_array_type(parse_dtype(dtype)) for
                name, dtype in vhiqa__spoh.items()}
            for i, name in enumerate(df.columns):
                if name in vhiqa__spoh:
                    arr_typ = vhiqa__spoh[name]
                else:
                    arr_typ = df.data[i]
                faovb__zku.append(arr_typ)
        else:
            data_args = ', '.join(
                f'bodo.utils.conversion.fix_arr_dtype(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}), {_get_dtype_str(vhiqa__spoh[ahner__puklw])}, copy, nan_to_str=_bodo_nan_to_str, from_series=True)'
                 if ahner__puklw in vhiqa__spoh else
                f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})'
                 for i, ahner__puklw in enumerate(df.columns))
    elif df.is_table_format:
        arr_typ = dtype_to_array_type(parse_dtype(dtype))
        faovb__zku = [arr_typ] * len(df.columns)
    else:
        data_args = ', '.join(
            f'bodo.utils.conversion.fix_arr_dtype(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}), dtype, copy, nan_to_str=_bodo_nan_to_str, from_series=True)'
             for i in range(len(df.columns)))
    if df.is_table_format:
        outa__gdv = bodo.TableType(tuple(faovb__zku))
        extra_globals['out_table_typ'] = outa__gdv
        data_args = (
            'bodo.utils.table_utils.table_astype(table, out_table_typ, copy, _bodo_nan_to_str)'
            )
    return _gen_init_df(header, df.columns, data_args, extra_globals=
        extra_globals)


@overload_method(DataFrameType, 'copy', inline='always', no_unliteral=True)
def overload_dataframe_copy(df, deep=True):
    check_runtime_cols_unsupported(df, 'DataFrame.copy()')
    header = 'def impl(df, deep=True):\n'
    extra_globals = None
    if df.is_table_format:
        header += (
            '  table = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)\n'
            )
        icoxw__ryc = types.none
        extra_globals = {'output_arr_typ': icoxw__ryc}
        if is_overload_false(deep):
            data_args = (
                'bodo.utils.table_utils.generate_mappable_table_func(' +
                'table, ' + 'None, ' + 'output_arr_typ, ' + 'True)')
        elif is_overload_true(deep):
            data_args = (
                'bodo.utils.table_utils.generate_mappable_table_func(' +
                'table, ' + "'copy', " + 'output_arr_typ, ' + 'True)')
        else:
            data_args = (
                'bodo.utils.table_utils.generate_mappable_table_func(' +
                'table, ' + "'copy', " + 'output_arr_typ, ' +
                'True) if deep else bodo.utils.table_utils.generate_mappable_table_func('
                 + 'table, ' + 'None, ' + 'output_arr_typ, ' + 'True)')
    else:
        aad__kfpch = []
        for i in range(len(df.columns)):
            arr = f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})'
            if is_overload_true(deep):
                aad__kfpch.append(arr + '.copy()')
            elif is_overload_false(deep):
                aad__kfpch.append(arr)
            else:
                aad__kfpch.append(f'{arr}.copy() if deep else {arr}')
        data_args = ', '.join(aad__kfpch)
    return _gen_init_df(header, df.columns, data_args, extra_globals=
        extra_globals)


@overload_method(DataFrameType, 'rename', inline='always', no_unliteral=True)
def overload_dataframe_rename(df, mapper=None, index=None, columns=None,
    axis=None, copy=True, inplace=False, level=None, errors='ignore',
    _bodo_transformed=False):
    check_runtime_cols_unsupported(df, 'DataFrame.rename()')
    handle_inplace_df_type_change(inplace, _bodo_transformed, 'rename')
    hsn__bxq = {'index': index, 'level': level, 'errors': errors}
    mawl__wldaq = {'index': None, 'level': None, 'errors': 'ignore'}
    check_unsupported_args('DataFrame.rename', hsn__bxq, mawl__wldaq,
        package_name='pandas', module_name='DataFrame')
    if not is_overload_constant_bool(inplace):
        raise BodoError(
            "DataFrame.rename(): 'inplace' keyword only supports boolean constant assignment"
            )
    if not is_overload_none(mapper):
        if not is_overload_none(columns):
            raise BodoError(
                "DataFrame.rename(): Cannot specify both 'mapper' and 'columns'"
                )
        if not (is_overload_constant_int(axis) and get_overload_const_int(
            axis) == 1):
            raise BodoError(
                "DataFrame.rename(): 'mapper' only supported with axis=1")
        if not is_overload_constant_dict(mapper):
            raise_bodo_error(
                "'mapper' argument to DataFrame.rename() should be a constant dictionary"
                )
        ozr__xool = get_overload_constant_dict(mapper)
    elif not is_overload_none(columns):
        if not is_overload_none(axis):
            raise BodoError(
                "DataFrame.rename(): Cannot specify both 'axis' and 'columns'")
        if not is_overload_constant_dict(columns):
            raise_bodo_error(
                "'columns' argument to DataFrame.rename() should be a constant dictionary"
                )
        ozr__xool = get_overload_constant_dict(columns)
    else:
        raise_bodo_error(
            "DataFrame.rename(): must pass columns either via 'mapper' and 'axis'=1 or 'columns'"
            )
    voidi__jeofb = tuple([ozr__xool.get(df.columns[i], df.columns[i]) for i in
        range(len(df.columns))])
    header = """def impl(df, mapper=None, index=None, columns=None, axis=None, copy=True, inplace=False, level=None, errors='ignore', _bodo_transformed=False):
"""
    extra_globals = None
    cneh__tfgg = None
    if df.is_table_format:
        header += (
            '  table = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)\n'
            )
        cneh__tfgg = df.copy(columns=voidi__jeofb)
        icoxw__ryc = types.none
        extra_globals = {'output_arr_typ': icoxw__ryc}
        if is_overload_false(copy):
            data_args = (
                'bodo.utils.table_utils.generate_mappable_table_func(' +
                'table, ' + 'None, ' + 'output_arr_typ, ' + 'True)')
        elif is_overload_true(copy):
            data_args = (
                'bodo.utils.table_utils.generate_mappable_table_func(' +
                'table, ' + "'copy', " + 'output_arr_typ, ' + 'True)')
        else:
            data_args = (
                'bodo.utils.table_utils.generate_mappable_table_func(' +
                'table, ' + "'copy', " + 'output_arr_typ, ' +
                'True) if copy else bodo.utils.table_utils.generate_mappable_table_func('
                 + 'table, ' + 'None, ' + 'output_arr_typ, ' + 'True)')
    else:
        aad__kfpch = []
        for i in range(len(df.columns)):
            arr = f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})'
            if is_overload_true(copy):
                aad__kfpch.append(arr + '.copy()')
            elif is_overload_false(copy):
                aad__kfpch.append(arr)
            else:
                aad__kfpch.append(f'{arr}.copy() if copy else {arr}')
        data_args = ', '.join(aad__kfpch)
    return _gen_init_df(header, voidi__jeofb, data_args, extra_globals=
        extra_globals)


@overload_method(DataFrameType, 'filter', no_unliteral=True)
def overload_dataframe_filter(df, items=None, like=None, regex=None, axis=None
    ):
    check_runtime_cols_unsupported(df, 'DataFrame.filter()')
    mnzy__qud = not is_overload_none(items)
    fzz__vrq = not is_overload_none(like)
    whsb__mob = not is_overload_none(regex)
    ytduj__rlf = mnzy__qud ^ fzz__vrq ^ whsb__mob
    tddni__czkan = not (mnzy__qud or fzz__vrq or whsb__mob)
    if tddni__czkan:
        raise BodoError(
            'DataFrame.filter(): one of keyword arguments `items`, `like`, and `regex` must be supplied'
            )
    if not ytduj__rlf:
        raise BodoError(
            'DataFrame.filter(): keyword arguments `items`, `like`, and `regex` are mutually exclusive'
            )
    if is_overload_none(axis):
        axis = 'columns'
    if is_overload_constant_str(axis):
        axis = get_overload_const_str(axis)
        if axis not in {'index', 'columns'}:
            raise_bodo_error(
                'DataFrame.filter(): keyword arguments `axis` must be either "index" or "columns" if string'
                )
        zxxj__uouum = 0 if axis == 'index' else 1
    elif is_overload_constant_int(axis):
        axis = get_overload_const_int(axis)
        if axis not in {0, 1}:
            raise_bodo_error(
                'DataFrame.filter(): keyword arguments `axis` must be either 0 or 1 if integer'
                )
        zxxj__uouum = axis
    else:
        raise_bodo_error(
            'DataFrame.filter(): keyword arguments `axis` must be constant string or integer'
            )
    assert zxxj__uouum in {0, 1}
    xood__fcig = (
        'def impl(df, items=None, like=None, regex=None, axis=None):\n')
    if zxxj__uouum == 0:
        raise BodoError(
            'DataFrame.filter(): filtering based on index is not supported.')
    if zxxj__uouum == 1:
        rpvhr__imzu = []
        tcwf__xgozn = []
        kadc__dkf = []
        if mnzy__qud:
            if is_overload_constant_list(items):
                aphm__jjj = get_overload_const_list(items)
            else:
                raise BodoError(
                    "Dataframe.filter(): argument 'items' must be a list of constant strings."
                    )
        if fzz__vrq:
            if is_overload_constant_str(like):
                qfl__eaw = get_overload_const_str(like)
            else:
                raise BodoError(
                    "Dataframe.filter(): argument 'like' must be a constant string."
                    )
        if whsb__mob:
            if is_overload_constant_str(regex):
                cuns__clrep = get_overload_const_str(regex)
                mar__yazul = re.compile(cuns__clrep)
            else:
                raise BodoError(
                    "Dataframe.filter(): argument 'regex' must be a constant string."
                    )
        for i, ahner__puklw in enumerate(df.columns):
            if not is_overload_none(items
                ) and ahner__puklw in aphm__jjj or not is_overload_none(like
                ) and qfl__eaw in str(ahner__puklw) or not is_overload_none(
                regex) and mar__yazul.search(str(ahner__puklw)):
                tcwf__xgozn.append(ahner__puklw)
                kadc__dkf.append(i)
        for i in kadc__dkf:
            var_name = f'data_{i}'
            rpvhr__imzu.append(var_name)
            xood__fcig += f"""  {var_name} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})
"""
        data_args = ', '.join(rpvhr__imzu)
        return _gen_init_df(xood__fcig, tcwf__xgozn, data_args)


@overload_method(DataFrameType, 'isna', inline='always', no_unliteral=True)
@overload_method(DataFrameType, 'isnull', inline='always', no_unliteral=True)
def overload_dataframe_isna(df):
    check_runtime_cols_unsupported(df, 'DataFrame.isna()')
    header = 'def impl(df):\n'
    extra_globals = None
    cneh__tfgg = None
    if df.is_table_format:
        icoxw__ryc = types.Array(types.bool_, 1, 'C')
        cneh__tfgg = DataFrameType(tuple([icoxw__ryc] * len(df.data)), df.
            index, df.columns, df.dist, is_table_format=True)
        extra_globals = {'output_arr_typ': icoxw__ryc}
        data_args = ('bodo.utils.table_utils.generate_mappable_table_func(' +
            'bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df), ' +
            "'bodo.libs.array_ops.array_op_isna', " + 'output_arr_typ, ' +
            'False)')
    else:
        data_args = ', '.join(
            f'bodo.libs.array_ops.array_op_isna(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}))'
             for i in range(len(df.columns)))
    return _gen_init_df(header, df.columns, data_args, extra_globals=
        extra_globals)


@overload_method(DataFrameType, 'select_dtypes', inline='always',
    no_unliteral=True)
def overload_dataframe_select_dtypes(df, include=None, exclude=None):
    check_runtime_cols_unsupported(df, 'DataFrame.select_dtypes')
    atc__cvdy = is_overload_none(include)
    ghh__ntm = is_overload_none(exclude)
    zglu__eroy = 'DataFrame.select_dtypes'
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.select_dtypes()')
    if atc__cvdy and ghh__ntm:
        raise_bodo_error(
            'DataFrame.select_dtypes() At least one of include or exclude must not be none'
            )

    def is_legal_input(elem):
        return is_overload_constant_str(elem) or isinstance(elem, types.
            DTypeSpec) or isinstance(elem, types.Function)
    if not atc__cvdy:
        if is_overload_constant_list(include):
            include = get_overload_const_list(include)
            akhog__knxql = [dtype_to_array_type(parse_dtype(elem,
                zglu__eroy)) for elem in include]
        elif is_legal_input(include):
            akhog__knxql = [dtype_to_array_type(parse_dtype(include,
                zglu__eroy))]
        else:
            raise_bodo_error(
                'DataFrame.select_dtypes() only supports constant strings or types as arguments'
                )
        akhog__knxql = get_nullable_and_non_nullable_types(akhog__knxql)
        dbp__wkcj = tuple(ahner__puklw for i, ahner__puklw in enumerate(df.
            columns) if df.data[i] in akhog__knxql)
    else:
        dbp__wkcj = df.columns
    if not ghh__ntm:
        if is_overload_constant_list(exclude):
            exclude = get_overload_const_list(exclude)
            zqniy__ammzh = [dtype_to_array_type(parse_dtype(elem,
                zglu__eroy)) for elem in exclude]
        elif is_legal_input(exclude):
            zqniy__ammzh = [dtype_to_array_type(parse_dtype(exclude,
                zglu__eroy))]
        else:
            raise_bodo_error(
                'DataFrame.select_dtypes() only supports constant strings or types as arguments'
                )
        zqniy__ammzh = get_nullable_and_non_nullable_types(zqniy__ammzh)
        dbp__wkcj = tuple(ahner__puklw for ahner__puklw in dbp__wkcj if df.
            data[df.column_index[ahner__puklw]] not in zqniy__ammzh)
    data_args = ', '.join(
        f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {df.column_index[ahner__puklw]})'
         for ahner__puklw in dbp__wkcj)
    header = 'def impl(df, include=None, exclude=None):\n'
    return _gen_init_df(header, dbp__wkcj, data_args)


@overload_method(DataFrameType, 'notna', inline='always', no_unliteral=True)
@overload_method(DataFrameType, 'notnull', inline='always', no_unliteral=True)
def overload_dataframe_notna(df):
    check_runtime_cols_unsupported(df, 'DataFrame.notna()')
    header = 'def impl(df):\n'
    extra_globals = None
    cneh__tfgg = None
    if df.is_table_format:
        icoxw__ryc = types.Array(types.bool_, 1, 'C')
        cneh__tfgg = DataFrameType(tuple([icoxw__ryc] * len(df.data)), df.
            index, df.columns, df.dist, is_table_format=True)
        extra_globals = {'output_arr_typ': icoxw__ryc}
        data_args = ('bodo.utils.table_utils.generate_mappable_table_func(' +
            'bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df), ' +
            "'~bodo.libs.array_ops.array_op_isna', " + 'output_arr_typ, ' +
            'False)')
    else:
        data_args = ', '.join(
            f'bodo.libs.array_ops.array_op_isna(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})) == False'
             for i in range(len(df.columns)))
    return _gen_init_df(header, df.columns, data_args, extra_globals=
        extra_globals)


def overload_dataframe_head(df, n=5):
    if df.is_table_format:
        data_args = (
            'bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)[:n]')
    else:
        data_args = ', '.join(
            f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})[:n]'
             for i in range(len(df.columns)))
    header = 'def impl(df, n=5):\n'
    index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)[:n]'
    return _gen_init_df(header, df.columns, data_args, index)


@lower_builtin('df.head', DataFrameType, types.Integer)
@lower_builtin('df.head', DataFrameType, types.Omitted)
def dataframe_head_lower(context, builder, sig, args):
    impl = overload_dataframe_head(*sig.args)
    return context.compile_internal(builder, impl, sig, args)


@overload_method(DataFrameType, 'tail', inline='always', no_unliteral=True)
def overload_dataframe_tail(df, n=5):
    check_runtime_cols_unsupported(df, 'DataFrame.tail()')
    if not is_overload_int(n):
        raise BodoError("Dataframe.tail(): 'n' must be an Integer")
    if df.is_table_format:
        data_args = (
            'bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)[m:]')
    else:
        data_args = ', '.join(
            f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})[m:]'
             for i in range(len(df.columns)))
    header = 'def impl(df, n=5):\n'
    header += '  m = bodo.hiframes.series_impl.tail_slice(len(df), n)\n'
    index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)[m:]'
    return _gen_init_df(header, df.columns, data_args, index)


@overload_method(DataFrameType, 'first', inline='always', no_unliteral=True)
def overload_dataframe_first(df, offset):
    check_runtime_cols_unsupported(df, 'DataFrame.first()')
    lfblb__hzh = (types.unicode_type, bodo.month_begin_type, bodo.
        month_end_type, bodo.week_type, bodo.date_offset_type)
    if not isinstance(df.index, DatetimeIndexType):
        raise BodoError(
            'DataFrame.first(): only supports a DatetimeIndex index')
    if types.unliteral(offset) not in lfblb__hzh:
        raise BodoError(
            "DataFrame.first(): 'offset' must be an string or DateOffset")
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.first()')
    index = (
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)[:valid_entries]'
        )
    data_args = ', '.join(
        f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})[:valid_entries]'
         for i in range(len(df.columns)))
    header = 'def impl(df, offset):\n'
    header += (
        '  df_index = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)\n'
        )
    header += '  if len(df_index):\n'
    header += '    start_date = df_index[0]\n'
    header += """    valid_entries = bodo.libs.array_kernels.get_valid_entries_from_date_offset(df_index, offset, start_date, False)
"""
    header += '  else:\n'
    header += '    valid_entries = 0\n'
    return _gen_init_df(header, df.columns, data_args, index)


@overload_method(DataFrameType, 'last', inline='always', no_unliteral=True)
def overload_dataframe_last(df, offset):
    check_runtime_cols_unsupported(df, 'DataFrame.last()')
    lfblb__hzh = (types.unicode_type, bodo.month_begin_type, bodo.
        month_end_type, bodo.week_type, bodo.date_offset_type)
    if not isinstance(df.index, DatetimeIndexType):
        raise BodoError('DataFrame.last(): only supports a DatetimeIndex index'
            )
    if types.unliteral(offset) not in lfblb__hzh:
        raise BodoError(
            "DataFrame.last(): 'offset' must be an string or DateOffset")
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.last()')
    index = (
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)[len(df)-valid_entries:]'
        )
    data_args = ', '.join(
        f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})[len(df)-valid_entries:]'
         for i in range(len(df.columns)))
    header = 'def impl(df, offset):\n'
    header += (
        '  df_index = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)\n'
        )
    header += '  if len(df_index):\n'
    header += '    final_date = df_index[-1]\n'
    header += """    valid_entries = bodo.libs.array_kernels.get_valid_entries_from_date_offset(df_index, offset, final_date, True)
"""
    header += '  else:\n'
    header += '    valid_entries = 0\n'
    return _gen_init_df(header, df.columns, data_args, index)


@overload_method(DataFrameType, 'to_string', no_unliteral=True)
def to_string_overload(df, buf=None, columns=None, col_space=None, header=
    True, index=True, na_rep='NaN', formatters=None, float_format=None,
    sparsify=None, index_names=True, justify=None, max_rows=None, min_rows=
    None, max_cols=None, show_dimensions=False, decimal='.', line_width=
    None, max_colwidth=None, encoding=None):
    check_runtime_cols_unsupported(df, 'DataFrame.to_string()')

    def impl(df, buf=None, columns=None, col_space=None, header=True, index
        =True, na_rep='NaN', formatters=None, float_format=None, sparsify=
        None, index_names=True, justify=None, max_rows=None, min_rows=None,
        max_cols=None, show_dimensions=False, decimal='.', line_width=None,
        max_colwidth=None, encoding=None):
        with numba.objmode(res='string'):
            res = df.to_string(buf=buf, columns=columns, col_space=
                col_space, header=header, index=index, na_rep=na_rep,
                formatters=formatters, float_format=float_format, sparsify=
                sparsify, index_names=index_names, justify=justify,
                max_rows=max_rows, min_rows=min_rows, max_cols=max_cols,
                show_dimensions=show_dimensions, decimal=decimal,
                line_width=line_width, max_colwidth=max_colwidth, encoding=
                encoding)
        return res
    return impl


@overload_method(DataFrameType, 'isin', inline='always', no_unliteral=True)
def overload_dataframe_isin(df, values):
    check_runtime_cols_unsupported(df, 'DataFrame.isin()')
    from bodo.utils.typing import is_iterable_type
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.isin()')
    xood__fcig = 'def impl(df, values):\n'
    rpyqc__oexn = {}
    llmn__nhykt = False
    if isinstance(values, DataFrameType):
        llmn__nhykt = True
        for i, ahner__puklw in enumerate(df.columns):
            if ahner__puklw in values.column_index:
                djxgf__hiwk = 'val{}'.format(i)
                xood__fcig += f"""  {djxgf__hiwk} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(values, {values.column_index[ahner__puklw]})
"""
                rpyqc__oexn[ahner__puklw] = djxgf__hiwk
    elif is_iterable_type(values) and not isinstance(values, SeriesType):
        rpyqc__oexn = {ahner__puklw: 'values' for ahner__puklw in df.columns}
    else:
        raise_bodo_error(f'pd.isin(): not supported for type {values}')
    data = []
    for i in range(len(df.columns)):
        djxgf__hiwk = 'data{}'.format(i)
        xood__fcig += (
            '  {} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {})\n'
            .format(djxgf__hiwk, i))
        data.append(djxgf__hiwk)
    lgbn__hlewj = ['out{}'.format(i) for i in range(len(df.columns))]
    dwmop__vad = """
  numba.parfors.parfor.init_prange()
  n = len({0})
  m = len({1})
  {2} = np.empty(n, np.bool_)
  for i in numba.parfors.parfor.internal_prange(n):
    {2}[i] = {0}[i] == {1}[i] if i < m else False
"""
    avsea__thgm = """
  numba.parfors.parfor.init_prange()
  n = len({0})
  {2} = np.empty(n, np.bool_)
  for i in numba.parfors.parfor.internal_prange(n):
    {2}[i] = {0}[i] in {1}
"""
    pkzcd__opafa = '  {} = np.zeros(len(df), np.bool_)\n'
    for i, (cname, wxlc__bbnw) in enumerate(zip(df.columns, data)):
        if cname in rpyqc__oexn:
            icd__wplfd = rpyqc__oexn[cname]
            if llmn__nhykt:
                xood__fcig += dwmop__vad.format(wxlc__bbnw, icd__wplfd,
                    lgbn__hlewj[i])
            else:
                xood__fcig += avsea__thgm.format(wxlc__bbnw, icd__wplfd,
                    lgbn__hlewj[i])
        else:
            xood__fcig += pkzcd__opafa.format(lgbn__hlewj[i])
    return _gen_init_df(xood__fcig, df.columns, ','.join(lgbn__hlewj))


@overload_method(DataFrameType, 'abs', inline='always', no_unliteral=True)
def overload_dataframe_abs(df):
    check_runtime_cols_unsupported(df, 'DataFrame.abs()')
    for arr_typ in df.data:
        if not (isinstance(arr_typ.dtype, types.Number) or arr_typ.dtype ==
            bodo.timedelta64ns):
            raise_bodo_error(
                f'DataFrame.abs(): Only supported for numeric and Timedelta. Encountered array with dtype {arr_typ.dtype}'
                )
    iryek__rfuyn = len(df.columns)
    data_args = ', '.join(
        'np.abs(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {}))'
        .format(i) for i in range(iryek__rfuyn))
    header = 'def impl(df):\n'
    return _gen_init_df(header, df.columns, data_args)


def overload_dataframe_corr(df, method='pearson', min_periods=1):
    moa__vmhnb = [ahner__puklw for ahner__puklw, tmy__jocol in zip(df.
        columns, df.data) if bodo.utils.typing._is_pandas_numeric_dtype(
        tmy__jocol.dtype)]
    assert len(moa__vmhnb) != 0
    snrdo__ocnvh = ''
    if not any(tmy__jocol == types.float64 for tmy__jocol in df.data):
        snrdo__ocnvh = '.astype(np.float64)'
    mwy__ctfb = ', '.join(
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {}){}'.
        format(df.column_index[ahner__puklw], '.astype(np.float64)' if 
        isinstance(df.data[df.column_index[ahner__puklw]], IntegerArrayType
        ) or df.data[df.column_index[ahner__puklw]] == boolean_array else
        '') for ahner__puklw in moa__vmhnb)
    xjbv__eln = 'np.stack(({},), 1){}'.format(mwy__ctfb, snrdo__ocnvh)
    data_args = ', '.join('res[:,{}]'.format(i) for i in range(len(moa__vmhnb))
        )
    index = f'{generate_col_to_index_func_text(moa__vmhnb)}\n'
    header = "def impl(df, method='pearson', min_periods=1):\n"
    header += '  mat = {}\n'.format(xjbv__eln)
    header += '  res = bodo.libs.array_kernels.nancorr(mat, 0, min_periods)\n'
    return _gen_init_df(header, moa__vmhnb, data_args, index)


@lower_builtin('df.corr', DataFrameType, types.VarArg(types.Any))
def dataframe_corr_lower(context, builder, sig, args):
    impl = overload_dataframe_corr(*sig.args)
    return context.compile_internal(builder, impl, sig, args)


@overload_method(DataFrameType, 'cov', inline='always', no_unliteral=True)
def overload_dataframe_cov(df, min_periods=None, ddof=1):
    check_runtime_cols_unsupported(df, 'DataFrame.cov()')
    dvves__ibrvv = dict(ddof=ddof)
    nwky__ohw = dict(ddof=1)
    check_unsupported_args('DataFrame.cov', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    uzab__wwuaw = '1' if is_overload_none(min_periods) else 'min_periods'
    moa__vmhnb = [ahner__puklw for ahner__puklw, tmy__jocol in zip(df.
        columns, df.data) if bodo.utils.typing._is_pandas_numeric_dtype(
        tmy__jocol.dtype)]
    if len(moa__vmhnb) == 0:
        raise_bodo_error('DataFrame.cov(): requires non-empty dataframe')
    snrdo__ocnvh = ''
    if not any(tmy__jocol == types.float64 for tmy__jocol in df.data):
        snrdo__ocnvh = '.astype(np.float64)'
    mwy__ctfb = ', '.join(
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {}){}'.
        format(df.column_index[ahner__puklw], '.astype(np.float64)' if 
        isinstance(df.data[df.column_index[ahner__puklw]], IntegerArrayType
        ) or df.data[df.column_index[ahner__puklw]] == boolean_array else
        '') for ahner__puklw in moa__vmhnb)
    xjbv__eln = 'np.stack(({},), 1){}'.format(mwy__ctfb, snrdo__ocnvh)
    data_args = ', '.join('res[:,{}]'.format(i) for i in range(len(moa__vmhnb))
        )
    index = f'pd.Index({moa__vmhnb})\n'
    header = 'def impl(df, min_periods=None, ddof=1):\n'
    header += '  mat = {}\n'.format(xjbv__eln)
    header += '  res = bodo.libs.array_kernels.nancorr(mat, 1, {})\n'.format(
        uzab__wwuaw)
    return _gen_init_df(header, moa__vmhnb, data_args, index)


@overload_method(DataFrameType, 'count', inline='always', no_unliteral=True)
def overload_dataframe_count(df, axis=0, level=None, numeric_only=False):
    check_runtime_cols_unsupported(df, 'DataFrame.count()')
    dvves__ibrvv = dict(axis=axis, level=level, numeric_only=numeric_only)
    nwky__ohw = dict(axis=0, level=None, numeric_only=False)
    check_unsupported_args('DataFrame.count', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    data_args = ', '.join(
        f'bodo.libs.array_ops.array_op_count(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}))'
         for i in range(len(df.columns)))
    xood__fcig = 'def impl(df, axis=0, level=None, numeric_only=False):\n'
    xood__fcig += '  data = np.array([{}])\n'.format(data_args)
    rlgfr__rjnej = (bodo.hiframes.dataframe_impl.
        generate_col_to_index_func_text(df.columns))
    xood__fcig += (
        f'  return bodo.hiframes.pd_series_ext.init_series(data, {rlgfr__rjnej})\n'
        )
    hrbgo__eykz = {}
    exec(xood__fcig, {'bodo': bodo, 'np': np}, hrbgo__eykz)
    impl = hrbgo__eykz['impl']
    return impl


@overload_method(DataFrameType, 'nunique', inline='always', no_unliteral=True)
def overload_dataframe_nunique(df, axis=0, dropna=True):
    check_runtime_cols_unsupported(df, 'DataFrame.unique()')
    dvves__ibrvv = dict(axis=axis)
    nwky__ohw = dict(axis=0)
    if not is_overload_bool(dropna):
        raise BodoError('DataFrame.nunique: dropna must be a boolean value')
    check_unsupported_args('DataFrame.nunique', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    data_args = ', '.join(
        f'bodo.libs.array_kernels.nunique(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}), dropna)'
         for i in range(len(df.columns)))
    xood__fcig = 'def impl(df, axis=0, dropna=True):\n'
    xood__fcig += '  data = np.asarray(({},))\n'.format(data_args)
    rlgfr__rjnej = (bodo.hiframes.dataframe_impl.
        generate_col_to_index_func_text(df.columns))
    xood__fcig += (
        f'  return bodo.hiframes.pd_series_ext.init_series(data, {rlgfr__rjnej})\n'
        )
    hrbgo__eykz = {}
    exec(xood__fcig, {'bodo': bodo, 'np': np}, hrbgo__eykz)
    impl = hrbgo__eykz['impl']
    return impl


@overload_method(DataFrameType, 'prod', inline='always', no_unliteral=True)
@overload_method(DataFrameType, 'product', inline='always', no_unliteral=True)
def overload_dataframe_prod(df, axis=None, skipna=None, level=None,
    numeric_only=None, min_count=0):
    check_runtime_cols_unsupported(df, 'DataFrame.prod()')
    dvves__ibrvv = dict(skipna=skipna, level=level, numeric_only=
        numeric_only, min_count=min_count)
    nwky__ohw = dict(skipna=None, level=None, numeric_only=None, min_count=0)
    check_unsupported_args('DataFrame.prod', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.product()')
    return _gen_reduce_impl(df, 'prod', axis=axis)


@overload_method(DataFrameType, 'sum', inline='always', no_unliteral=True)
def overload_dataframe_sum(df, axis=None, skipna=None, level=None,
    numeric_only=None, min_count=0):
    check_runtime_cols_unsupported(df, 'DataFrame.sum()')
    dvves__ibrvv = dict(skipna=skipna, level=level, numeric_only=
        numeric_only, min_count=min_count)
    nwky__ohw = dict(skipna=None, level=None, numeric_only=None, min_count=0)
    check_unsupported_args('DataFrame.sum', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.sum()')
    return _gen_reduce_impl(df, 'sum', axis=axis)


@overload_method(DataFrameType, 'max', inline='always', no_unliteral=True)
def overload_dataframe_max(df, axis=None, skipna=None, level=None,
    numeric_only=None):
    check_runtime_cols_unsupported(df, 'DataFrame.max()')
    dvves__ibrvv = dict(skipna=skipna, level=level, numeric_only=numeric_only)
    nwky__ohw = dict(skipna=None, level=None, numeric_only=None)
    check_unsupported_args('DataFrame.max', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.max()')
    return _gen_reduce_impl(df, 'max', axis=axis)


@overload_method(DataFrameType, 'min', inline='always', no_unliteral=True)
def overload_dataframe_min(df, axis=None, skipna=None, level=None,
    numeric_only=None):
    check_runtime_cols_unsupported(df, 'DataFrame.min()')
    dvves__ibrvv = dict(skipna=skipna, level=level, numeric_only=numeric_only)
    nwky__ohw = dict(skipna=None, level=None, numeric_only=None)
    check_unsupported_args('DataFrame.min', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.min()')
    return _gen_reduce_impl(df, 'min', axis=axis)


@overload_method(DataFrameType, 'mean', inline='always', no_unliteral=True)
def overload_dataframe_mean(df, axis=None, skipna=None, level=None,
    numeric_only=None):
    check_runtime_cols_unsupported(df, 'DataFrame.mean()')
    dvves__ibrvv = dict(skipna=skipna, level=level, numeric_only=numeric_only)
    nwky__ohw = dict(skipna=None, level=None, numeric_only=None)
    check_unsupported_args('DataFrame.mean', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.mean()')
    return _gen_reduce_impl(df, 'mean', axis=axis)


@overload_method(DataFrameType, 'var', inline='always', no_unliteral=True)
def overload_dataframe_var(df, axis=None, skipna=None, level=None, ddof=1,
    numeric_only=None):
    check_runtime_cols_unsupported(df, 'DataFrame.var()')
    dvves__ibrvv = dict(skipna=skipna, level=level, ddof=ddof, numeric_only
        =numeric_only)
    nwky__ohw = dict(skipna=None, level=None, ddof=1, numeric_only=None)
    check_unsupported_args('DataFrame.var', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.var()')
    return _gen_reduce_impl(df, 'var', axis=axis)


@overload_method(DataFrameType, 'std', inline='always', no_unliteral=True)
def overload_dataframe_std(df, axis=None, skipna=None, level=None, ddof=1,
    numeric_only=None):
    check_runtime_cols_unsupported(df, 'DataFrame.std()')
    dvves__ibrvv = dict(skipna=skipna, level=level, ddof=ddof, numeric_only
        =numeric_only)
    nwky__ohw = dict(skipna=None, level=None, ddof=1, numeric_only=None)
    check_unsupported_args('DataFrame.std', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.std()')
    return _gen_reduce_impl(df, 'std', axis=axis)


@overload_method(DataFrameType, 'median', inline='always', no_unliteral=True)
def overload_dataframe_median(df, axis=None, skipna=None, level=None,
    numeric_only=None):
    check_runtime_cols_unsupported(df, 'DataFrame.median()')
    dvves__ibrvv = dict(skipna=skipna, level=level, numeric_only=numeric_only)
    nwky__ohw = dict(skipna=None, level=None, numeric_only=None)
    check_unsupported_args('DataFrame.median', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.median()')
    return _gen_reduce_impl(df, 'median', axis=axis)


@overload_method(DataFrameType, 'quantile', inline='always', no_unliteral=True)
def overload_dataframe_quantile(df, q=0.5, axis=0, numeric_only=True,
    interpolation='linear'):
    check_runtime_cols_unsupported(df, 'DataFrame.quantile()')
    dvves__ibrvv = dict(numeric_only=numeric_only, interpolation=interpolation)
    nwky__ohw = dict(numeric_only=True, interpolation='linear')
    check_unsupported_args('DataFrame.quantile', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.quantile()')
    return _gen_reduce_impl(df, 'quantile', 'q', axis=axis)


@overload_method(DataFrameType, 'idxmax', inline='always', no_unliteral=True)
def overload_dataframe_idxmax(df, axis=0, skipna=True):
    check_runtime_cols_unsupported(df, 'DataFrame.idxmax()')
    dvves__ibrvv = dict(axis=axis, skipna=skipna)
    nwky__ohw = dict(axis=0, skipna=True)
    check_unsupported_args('DataFrame.idxmax', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.idxmax()')
    for ejla__ipsft in df.data:
        if not (bodo.utils.utils.is_np_array_typ(ejla__ipsft) and (
            ejla__ipsft.dtype in [bodo.datetime64ns, bodo.timedelta64ns] or
            isinstance(ejla__ipsft.dtype, (types.Number, types.Boolean))) or
            isinstance(ejla__ipsft, (bodo.IntegerArrayType, bodo.
            FloatingArrayType, bodo.CategoricalArrayType)) or ejla__ipsft in
            [bodo.boolean_array, bodo.datetime_date_array_type]):
            raise BodoError(
                f'DataFrame.idxmax() only supported for numeric column types. Column type: {ejla__ipsft} not supported.'
                )
        if isinstance(ejla__ipsft, bodo.CategoricalArrayType
            ) and not ejla__ipsft.dtype.ordered:
            raise BodoError(
                'DataFrame.idxmax(): categorical columns must be ordered')
    return _gen_reduce_impl(df, 'idxmax', axis=axis)


@overload_method(DataFrameType, 'idxmin', inline='always', no_unliteral=True)
def overload_dataframe_idxmin(df, axis=0, skipna=True):
    check_runtime_cols_unsupported(df, 'DataFrame.idxmin()')
    dvves__ibrvv = dict(axis=axis, skipna=skipna)
    nwky__ohw = dict(axis=0, skipna=True)
    check_unsupported_args('DataFrame.idxmin', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.idxmin()')
    for ejla__ipsft in df.data:
        if not (bodo.utils.utils.is_np_array_typ(ejla__ipsft) and (
            ejla__ipsft.dtype in [bodo.datetime64ns, bodo.timedelta64ns] or
            isinstance(ejla__ipsft.dtype, (types.Number, types.Boolean))) or
            isinstance(ejla__ipsft, (bodo.IntegerArrayType, bodo.
            FloatingArrayType, bodo.CategoricalArrayType)) or ejla__ipsft in
            [bodo.boolean_array, bodo.datetime_date_array_type]):
            raise BodoError(
                f'DataFrame.idxmin() only supported for numeric column types. Column type: {ejla__ipsft} not supported.'
                )
        if isinstance(ejla__ipsft, bodo.CategoricalArrayType
            ) and not ejla__ipsft.dtype.ordered:
            raise BodoError(
                'DataFrame.idxmin(): categorical columns must be ordered')
    return _gen_reduce_impl(df, 'idxmin', axis=axis)


@overload_method(DataFrameType, 'infer_objects', inline='always')
def overload_dataframe_infer_objects(df):
    check_runtime_cols_unsupported(df, 'DataFrame.infer_objects()')
    return lambda df: df.copy()


def _gen_reduce_impl(df, func_name, args=None, axis=None):
    args = '' if is_overload_none(args) else args
    if is_overload_none(axis):
        axis = 0
    elif is_overload_constant_int(axis):
        axis = get_overload_const_int(axis)
    else:
        raise_bodo_error(
            f'DataFrame.{func_name}: axis must be a constant Integer')
    assert axis in (0, 1), f'invalid axis argument for DataFrame.{func_name}'
    if func_name in ('idxmax', 'idxmin'):
        out_colnames = df.columns
    else:
        moa__vmhnb = tuple(ahner__puklw for ahner__puklw, tmy__jocol in zip
            (df.columns, df.data) if bodo.utils.typing.
            _is_pandas_numeric_dtype(tmy__jocol.dtype))
        out_colnames = moa__vmhnb
    assert len(out_colnames) != 0
    try:
        if func_name in ('idxmax', 'idxmin') and axis == 0:
            comm_dtype = None
        else:
            ker__tfgnl = [numba.np.numpy_support.as_dtype(df.data[df.
                column_index[ahner__puklw]].dtype) for ahner__puklw in
                out_colnames]
            comm_dtype = numba.np.numpy_support.from_dtype(np.
                find_common_type(ker__tfgnl, []))
    except NotImplementedError as xstvf__tlntg:
        raise BodoError(
            f'Dataframe.{func_name}() with column types: {df.data} could not be merged to a common type.'
            )
    bolv__fuyub = ''
    if func_name in ('sum', 'prod'):
        bolv__fuyub = ', min_count=0'
    ddof = ''
    if func_name in ('var', 'std'):
        ddof = 'ddof=1, '
    xood__fcig = (
        'def impl(df, axis=None, skipna=None, level=None,{} numeric_only=None{}):\n'
        .format(ddof, bolv__fuyub))
    if func_name == 'quantile':
        xood__fcig = (
            "def impl(df, q=0.5, axis=0, numeric_only=True, interpolation='linear'):\n"
            )
    if func_name in ('idxmax', 'idxmin'):
        xood__fcig = 'def impl(df, axis=0, skipna=True):\n'
    if axis == 0:
        xood__fcig += _gen_reduce_impl_axis0(df, func_name, out_colnames,
            comm_dtype, args)
    else:
        xood__fcig += _gen_reduce_impl_axis1(func_name, out_colnames,
            comm_dtype, df)
    hrbgo__eykz = {}
    exec(xood__fcig, {'bodo': bodo, 'np': np, 'pd': pd, 'numba': numba},
        hrbgo__eykz)
    impl = hrbgo__eykz['impl']
    return impl


def _gen_reduce_impl_axis0(df, func_name, out_colnames, comm_dtype, args):
    map__xlyuk = ''
    if func_name in ('min', 'max'):
        map__xlyuk = ', dtype=np.{}'.format(comm_dtype)
    if comm_dtype == types.float32 and func_name in ('sum', 'prod', 'mean',
        'var', 'std', 'median'):
        map__xlyuk = ', dtype=np.float32'
    uqtti__gsku = f'bodo.libs.array_ops.array_op_{func_name}'
    bbz__vbwwk = ''
    if func_name in ['sum', 'prod']:
        bbz__vbwwk = 'True, min_count'
    elif func_name in ['idxmax', 'idxmin']:
        bbz__vbwwk = 'index'
    elif func_name == 'quantile':
        bbz__vbwwk = 'q'
    elif func_name in ['std', 'var']:
        bbz__vbwwk = 'True, ddof'
    elif func_name == 'median':
        bbz__vbwwk = 'True'
    data_args = ', '.join(
        f'{uqtti__gsku}(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {df.column_index[ahner__puklw]}), {bbz__vbwwk})'
         for ahner__puklw in out_colnames)
    xood__fcig = ''
    if func_name in ('idxmax', 'idxmin'):
        xood__fcig += (
            '  index = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)\n'
            )
        xood__fcig += (
            '  data = bodo.utils.conversion.coerce_to_array(({},))\n'.
            format(data_args))
    else:
        xood__fcig += '  data = np.asarray(({},){})\n'.format(data_args,
            map__xlyuk)
    xood__fcig += f"""  return bodo.hiframes.pd_series_ext.init_series(data, pd.Index({out_colnames}))
"""
    return xood__fcig


def _gen_reduce_impl_axis1(func_name, out_colnames, comm_dtype, df_type):
    yakrw__yrbk = [df_type.column_index[ahner__puklw] for ahner__puklw in
        out_colnames]
    index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)'
    data_args = '\n    '.join(
        'arr_{0} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {0})'
        .format(i) for i in yakrw__yrbk)
    uep__hcvzq = '\n        '.join(f'row[{i}] = arr_{yakrw__yrbk[i]}[i]' for
        i in range(len(out_colnames)))
    assert len(data_args) > 0, f'empty dataframe in DataFrame.{func_name}()'
    idgsh__iekkp = f'len(arr_{yakrw__yrbk[0]})'
    svf__mdspf = {'max': 'np.nanmax', 'min': 'np.nanmin', 'sum':
        'np.nansum', 'prod': 'np.nanprod', 'mean': 'np.nanmean', 'median':
        'np.nanmedian', 'var': 'bodo.utils.utils.nanvar_ddof1', 'std':
        'bodo.utils.utils.nanstd_ddof1'}
    if func_name in svf__mdspf:
        hle__ofz = svf__mdspf[func_name]
        ncpq__vzle = 'float64' if func_name in ['mean', 'median', 'std', 'var'
            ] else comm_dtype
        xood__fcig = f"""
    {data_args}
    numba.parfors.parfor.init_prange()
    n = {idgsh__iekkp}
    row = np.empty({len(out_colnames)}, np.{comm_dtype})
    A = np.empty(n, np.{ncpq__vzle})
    for i in numba.parfors.parfor.internal_prange(n):
        {uep__hcvzq}
        A[i] = {hle__ofz}(row)
    return bodo.hiframes.pd_series_ext.init_series(A, {index})
"""
        return xood__fcig
    else:
        raise BodoError(f'DataFrame.{func_name}(): Not supported for axis=1')


@overload_method(DataFrameType, 'pct_change', inline='always', no_unliteral
    =True)
def overload_dataframe_pct_change(df, periods=1, fill_method='pad', limit=
    None, freq=None):
    check_runtime_cols_unsupported(df, 'DataFrame.pct_change()')
    dvves__ibrvv = dict(fill_method=fill_method, limit=limit, freq=freq)
    nwky__ohw = dict(fill_method='pad', limit=None, freq=None)
    check_unsupported_args('DataFrame.pct_change', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.pct_change()')
    data_args = ', '.join(
        f'bodo.hiframes.rolling.pct_change(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}), periods, False)'
         for i in range(len(df.columns)))
    header = (
        "def impl(df, periods=1, fill_method='pad', limit=None, freq=None):\n")
    return _gen_init_df(header, df.columns, data_args)


@overload_method(DataFrameType, 'cumprod', inline='always', no_unliteral=True)
def overload_dataframe_cumprod(df, axis=None, skipna=True):
    check_runtime_cols_unsupported(df, 'DataFrame.cumprod()')
    dvves__ibrvv = dict(axis=axis, skipna=skipna)
    nwky__ohw = dict(axis=None, skipna=True)
    check_unsupported_args('DataFrame.cumprod', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.cumprod()')
    data_args = ', '.join(
        f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}).cumprod()'
         for i in range(len(df.columns)))
    header = 'def impl(df, axis=None, skipna=True):\n'
    return _gen_init_df(header, df.columns, data_args)


@overload_method(DataFrameType, 'cumsum', inline='always', no_unliteral=True)
def overload_dataframe_cumsum(df, axis=None, skipna=True):
    check_runtime_cols_unsupported(df, 'DataFrame.cumsum()')
    dvves__ibrvv = dict(skipna=skipna)
    nwky__ohw = dict(skipna=True)
    check_unsupported_args('DataFrame.cumsum', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.cumsum()')
    data_args = ', '.join(
        f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}).cumsum()'
         for i in range(len(df.columns)))
    header = 'def impl(df, axis=None, skipna=True):\n'
    return _gen_init_df(header, df.columns, data_args)


def _is_describe_type(data):
    return isinstance(data, (IntegerArrayType, FloatingArrayType)
        ) or isinstance(data, types.Array) and isinstance(data.dtype, types
        .Number) or data.dtype == bodo.datetime64ns


@overload_method(DataFrameType, 'describe', inline='always', no_unliteral=True)
def overload_dataframe_describe(df, percentiles=None, include=None, exclude
    =None, datetime_is_numeric=True):
    check_runtime_cols_unsupported(df, 'DataFrame.describe()')
    dvves__ibrvv = dict(percentiles=percentiles, include=include, exclude=
        exclude, datetime_is_numeric=datetime_is_numeric)
    nwky__ohw = dict(percentiles=None, include=None, exclude=None,
        datetime_is_numeric=True)
    check_unsupported_args('DataFrame.describe', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.describe()')
    moa__vmhnb = [ahner__puklw for ahner__puklw, tmy__jocol in zip(df.
        columns, df.data) if _is_describe_type(tmy__jocol)]
    if len(moa__vmhnb) == 0:
        raise BodoError('df.describe() only supports numeric columns')
    vqzkv__kkx = sum(df.data[df.column_index[ahner__puklw]].dtype == bodo.
        datetime64ns for ahner__puklw in moa__vmhnb)

    def _get_describe(col_ind):
        mjyxi__obnu = df.data[col_ind].dtype == bodo.datetime64ns
        if vqzkv__kkx and vqzkv__kkx != len(moa__vmhnb):
            if mjyxi__obnu:
                return f'des_{col_ind} + (np.nan,)'
            return (
                f'des_{col_ind}[:2] + des_{col_ind}[3:] + (des_{col_ind}[2],)')
        return f'des_{col_ind}'
    header = """def impl(df, percentiles=None, include=None, exclude=None, datetime_is_numeric=True):
"""
    for ahner__puklw in moa__vmhnb:
        col_ind = df.column_index[ahner__puklw]
        header += f"""  des_{col_ind} = bodo.libs.array_ops.array_op_describe(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {col_ind}))
"""
    data_args = ', '.join(_get_describe(df.column_index[ahner__puklw]) for
        ahner__puklw in moa__vmhnb)
    ehmhj__hzh = "['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']"
    if vqzkv__kkx == len(moa__vmhnb):
        ehmhj__hzh = "['count', 'mean', 'min', '25%', '50%', '75%', 'max']"
    elif vqzkv__kkx:
        ehmhj__hzh = (
            "['count', 'mean', 'min', '25%', '50%', '75%', 'max', 'std']")
    index = f'bodo.utils.conversion.convert_to_index({ehmhj__hzh})'
    return _gen_init_df(header, moa__vmhnb, data_args, index)


@overload_method(DataFrameType, 'take', inline='always', no_unliteral=True)
def overload_dataframe_take(df, indices, axis=0, convert=None, is_copy=True):
    check_runtime_cols_unsupported(df, 'DataFrame.take()')
    dvves__ibrvv = dict(axis=axis, convert=convert, is_copy=is_copy)
    nwky__ohw = dict(axis=0, convert=None, is_copy=True)
    check_unsupported_args('DataFrame.take', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    data_args = ', '.join(
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {})[indices_t]'
        .format(i) for i in range(len(df.columns)))
    header = 'def impl(df, indices, axis=0, convert=None, is_copy=True):\n'
    header += (
        '  indices_t = bodo.utils.conversion.coerce_to_ndarray(indices)\n')
    index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)[indices_t]'
    return _gen_init_df(header, df.columns, data_args, index)


@overload_method(DataFrameType, 'shift', inline='always', no_unliteral=True)
def overload_dataframe_shift(df, periods=1, freq=None, axis=0, fill_value=None
    ):
    check_runtime_cols_unsupported(df, 'DataFrame.shift()')
    dvves__ibrvv = dict(freq=freq, axis=axis)
    nwky__ohw = dict(freq=None, axis=0)
    check_unsupported_args('DataFrame.shift', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.shift()')
    for jmj__qcf in df.data:
        if not is_supported_shift_array_type(jmj__qcf):
            raise BodoError(
                f'Dataframe.shift() column input type {jmj__qcf.dtype} not supported yet.'
                )
    if not is_overload_int(periods):
        raise BodoError(
            "DataFrame.shift(): 'periods' input must be an integer.")
    data_args = ', '.join(
        f'bodo.hiframes.rolling.shift(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}), periods, False, fill_value)'
         for i in range(len(df.columns)))
    header = 'def impl(df, periods=1, freq=None, axis=0, fill_value=None):\n'
    return _gen_init_df(header, df.columns, data_args)


@overload_method(DataFrameType, 'diff', inline='always', no_unliteral=True)
def overload_dataframe_diff(df, periods=1, axis=0):
    check_runtime_cols_unsupported(df, 'DataFrame.diff()')
    dvves__ibrvv = dict(axis=axis)
    nwky__ohw = dict(axis=0)
    check_unsupported_args('DataFrame.diff', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.diff()')
    for jmj__qcf in df.data:
        if not (isinstance(jmj__qcf, types.Array) and (isinstance(jmj__qcf.
            dtype, types.Number) or jmj__qcf.dtype == bodo.datetime64ns)):
            raise BodoError(
                f'DataFrame.diff() column input type {jmj__qcf.dtype} not supported.'
                )
    if not is_overload_int(periods):
        raise BodoError("DataFrame.diff(): 'periods' input must be an integer."
            )
    header = 'def impl(df, periods=1, axis= 0):\n'
    for i in range(len(df.columns)):
        header += (
            f'  data_{i} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})\n'
            )
    data_args = ', '.join(
        f'bodo.hiframes.series_impl.dt64_arr_sub(data_{i}, bodo.hiframes.rolling.shift(data_{i}, periods, False))'
         if df.data[i] == types.Array(bodo.datetime64ns, 1, 'C') else
        f'data_{i} - bodo.hiframes.rolling.shift(data_{i}, periods, False)' for
        i in range(len(df.columns)))
    return _gen_init_df(header, df.columns, data_args)


@overload_method(DataFrameType, 'explode', inline='always', no_unliteral=True)
def overload_dataframe_explode(df, column, ignore_index=False):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.explode()')
    phvff__yyof = (
        "DataFrame.explode(): 'column' must a constant label or list of labels"
        )
    if not is_literal_type(column):
        raise_bodo_error(phvff__yyof)
    if is_overload_constant_list(column) or is_overload_constant_tuple(column):
        jcpgn__uwxl = get_overload_const_list(column)
    else:
        jcpgn__uwxl = [get_literal_value(column)]
    wuz__pug = [df.column_index[ahner__puklw] for ahner__puklw in jcpgn__uwxl]
    for i in wuz__pug:
        if not isinstance(df.data[i], ArrayItemArrayType) and df.data[i
            ].dtype != string_array_split_view_type:
            raise BodoError(
                f'DataFrame.explode(): columns must have array-like entries')
    n = len(df.columns)
    header = 'def impl(df, column, ignore_index=False):\n'
    header += (
        '  index = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)\n')
    header += '  index_arr = bodo.utils.conversion.index_to_array(index)\n'
    for i in range(n):
        header += (
            f'  data{i} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})\n'
            )
    header += (
        f'  counts = bodo.libs.array_kernels.get_arr_lens(data{wuz__pug[0]})\n'
        )
    for i in range(n):
        if i in wuz__pug:
            header += (
                f'  out_data{i} = bodo.libs.array_kernels.explode_no_index(data{i}, counts)\n'
                )
        else:
            header += (
                f'  out_data{i} = bodo.libs.array_kernels.repeat_kernel(data{i}, counts)\n'
                )
    header += (
        '  new_index = bodo.libs.array_kernels.repeat_kernel(index_arr, counts)\n'
        )
    data_args = ', '.join(f'out_data{i}' for i in range(n))
    index = 'bodo.utils.conversion.convert_to_index(new_index)'
    return _gen_init_df(header, df.columns, data_args, index)


@overload_method(DataFrameType, 'set_index', inline='always', no_unliteral=True
    )
def overload_dataframe_set_index(df, keys, drop=True, append=False, inplace
    =False, verify_integrity=False):
    check_runtime_cols_unsupported(df, 'DataFrame.set_index()')
    hsn__bxq = {'inplace': inplace, 'append': append, 'verify_integrity':
        verify_integrity}
    mawl__wldaq = {'inplace': False, 'append': False, 'verify_integrity': False
        }
    check_unsupported_args('DataFrame.set_index', hsn__bxq, mawl__wldaq,
        package_name='pandas', module_name='DataFrame')
    if not is_overload_constant_str(keys):
        raise_bodo_error(
            "DataFrame.set_index(): 'keys' must be a constant string")
    col_name = get_overload_const_str(keys)
    col_ind = df.columns.index(col_name)
    header = """def impl(df, keys, drop=True, append=False, inplace=False, verify_integrity=False):
"""
    data_args = ', '.join(
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {})'.format(
        i) for i in range(len(df.columns)) if i != col_ind)
    columns = tuple(ahner__puklw for ahner__puklw in df.columns if 
        ahner__puklw != col_name)
    index = (
        'bodo.utils.conversion.index_from_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {}), {})'
        .format(col_ind, f"'{col_name}'" if isinstance(col_name, str) else
        col_name))
    return _gen_init_df(header, columns, data_args, index)


@overload_method(DataFrameType, 'query', no_unliteral=True)
def overload_dataframe_query(df, expr, inplace=False):
    check_runtime_cols_unsupported(df, 'DataFrame.query()')
    hsn__bxq = {'inplace': inplace}
    mawl__wldaq = {'inplace': False}
    check_unsupported_args('query', hsn__bxq, mawl__wldaq, package_name=
        'pandas', module_name='DataFrame')
    if not isinstance(expr, (types.StringLiteral, types.UnicodeType)):
        raise BodoError('query(): expr argument should be a string')

    def impl(df, expr, inplace=False):
        lyp__syzei = bodo.hiframes.pd_dataframe_ext.query_dummy(df, expr)
        return df[lyp__syzei]
    return impl


@overload_method(DataFrameType, 'duplicated', inline='always', no_unliteral
    =True)
def overload_dataframe_duplicated(df, subset=None, keep='first'):
    check_runtime_cols_unsupported(df, 'DataFrame.duplicated()')
    hsn__bxq = {'subset': subset, 'keep': keep}
    mawl__wldaq = {'subset': None, 'keep': 'first'}
    check_unsupported_args('DataFrame.duplicated', hsn__bxq, mawl__wldaq,
        package_name='pandas', module_name='DataFrame')
    iryek__rfuyn = len(df.columns)
    xood__fcig = "def impl(df, subset=None, keep='first'):\n"
    for i in range(iryek__rfuyn):
        xood__fcig += (
            '  data_{0} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {0})\n'
            .format(i))
    pvmnn__cfe = ', '.join(f'data_{i}' for i in range(iryek__rfuyn))
    pvmnn__cfe += ',' if iryek__rfuyn == 1 else ''
    xood__fcig += (
        f'  duplicated = bodo.libs.array_kernels.duplicated(({pvmnn__cfe}))\n')
    xood__fcig += (
        '  index = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)\n')
    xood__fcig += (
        '  return bodo.hiframes.pd_series_ext.init_series(duplicated, index)\n'
        )
    hrbgo__eykz = {}
    exec(xood__fcig, {'bodo': bodo}, hrbgo__eykz)
    impl = hrbgo__eykz['impl']
    return impl


@overload_method(DataFrameType, 'drop_duplicates', inline='always',
    no_unliteral=True)
def overload_dataframe_drop_duplicates(df, subset=None, keep='first',
    inplace=False, ignore_index=False):
    check_runtime_cols_unsupported(df, 'DataFrame.drop_duplicates()')
    hsn__bxq = {'keep': keep, 'inplace': inplace, 'ignore_index': ignore_index}
    mawl__wldaq = {'keep': 'first', 'inplace': False, 'ignore_index': False}
    lks__iikg = []
    if is_overload_constant_list(subset):
        lks__iikg = get_overload_const_list(subset)
    elif is_overload_constant_str(subset):
        lks__iikg = [get_overload_const_str(subset)]
    elif is_overload_constant_int(subset):
        lks__iikg = [get_overload_const_int(subset)]
    elif not is_overload_none(subset):
        raise_bodo_error(
            'DataFrame.drop_duplicates(): subset must be a constant column name, constant list of column names or None'
            )
    rspp__nctaq = []
    for col_name in lks__iikg:
        if col_name not in df.column_index:
            raise BodoError(
                'DataFrame.drop_duplicates(): All subset columns must be found in the DataFrame.'
                 +
                f'Column {col_name} not found in DataFrame columns {df.columns}'
                )
        rspp__nctaq.append(df.column_index[col_name])
    check_unsupported_args('DataFrame.drop_duplicates', hsn__bxq,
        mawl__wldaq, package_name='pandas', module_name='DataFrame')
    orl__fxy = []
    if rspp__nctaq:
        for ugff__hna in rspp__nctaq:
            if isinstance(df.data[ugff__hna], bodo.MapArrayType):
                orl__fxy.append(df.columns[ugff__hna])
    else:
        for i, col_name in enumerate(df.columns):
            if isinstance(df.data[i], bodo.MapArrayType):
                orl__fxy.append(col_name)
    if orl__fxy:
        raise BodoError(f'DataFrame.drop_duplicates(): Columns {orl__fxy} ' +
            f'have dictionary types which cannot be used to drop duplicates. '
             +
            "Please consider using the 'subset' argument to skip these columns."
            )
    iryek__rfuyn = len(df.columns)
    qnq__pyn = ['data_{}'.format(i) for i in rspp__nctaq]
    ekpcx__jnxq = ['data_{}'.format(i) for i in range(iryek__rfuyn) if i not in
        rspp__nctaq]
    if qnq__pyn:
        hmlh__bnvt = len(qnq__pyn)
    else:
        hmlh__bnvt = iryek__rfuyn
    jelwc__pcd = ', '.join(qnq__pyn + ekpcx__jnxq)
    data_args = ', '.join('data_{}'.format(i) for i in range(iryek__rfuyn))
    xood__fcig = (
        "def impl(df, subset=None, keep='first', inplace=False, ignore_index=False):\n"
        )
    for i in range(iryek__rfuyn):
        xood__fcig += (
            '  data_{0} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {0})\n'
            .format(i))
    index = (
        'bodo.utils.conversion.index_to_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df))'
        )
    xood__fcig += (
        """  ({0},), index_arr = bodo.libs.array_kernels.drop_duplicates(({0},), {1}, {2})
"""
        .format(jelwc__pcd, index, hmlh__bnvt))
    xood__fcig += (
        '  index = bodo.utils.conversion.index_from_array(index_arr)\n')
    return _gen_init_df(xood__fcig, df.columns, data_args, 'index')


def create_dataframe_mask_where_overload(func_name):

    def overload_dataframe_mask_where(df, cond, other=np.nan, inplace=False,
        axis=None, level=None, errors='raise', try_cast=False):
        bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
            f'DataFrame.{func_name}()')
        _validate_arguments_mask_where(f'DataFrame.{func_name}', df, cond,
            other, inplace, axis, level, errors, try_cast)
        header = """def impl(df, cond, other=np.nan, inplace=False, axis=None, level=None, errors='raise', try_cast=False):
"""
        if func_name == 'mask':
            header += '  cond = ~cond\n'
        gen_all_false = [False]
        if cond.ndim == 1:
            cond_str = lambda i, _: 'cond'
        elif cond.ndim == 2:
            if isinstance(cond, DataFrameType):

                def cond_str(i, gen_all_false):
                    if df.columns[i] in cond.column_index:
                        return (
                            f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(cond, {cond.column_index[df.columns[i]]})'
                            )
                    else:
                        gen_all_false[0] = True
                        return 'all_false'
            elif isinstance(cond, types.Array):
                cond_str = lambda i, _: f'cond[:,{i}]'
        if not hasattr(other, 'ndim') or other.ndim == 1:
            axysj__mraj = lambda i: 'other'
        elif other.ndim == 2:
            if isinstance(other, DataFrameType):
                axysj__mraj = (lambda i: 
                    f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(other, {other.column_index[df.columns[i]]})'
                     if df.columns[i] in other.column_index else 'None')
            elif isinstance(other, types.Array):
                axysj__mraj = lambda i: f'other[:,{i}]'
        iryek__rfuyn = len(df.columns)
        data_args = ', '.join(
            f'bodo.hiframes.series_impl.where_impl({cond_str(i, gen_all_false)}, bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}), {axysj__mraj(i)})'
             for i in range(iryek__rfuyn))
        if gen_all_false[0]:
            header += '  all_false = np.zeros(len(df), dtype=bool)\n'
        return _gen_init_df(header, df.columns, data_args)
    return overload_dataframe_mask_where


def _install_dataframe_mask_where_overload():
    for func_name in ('mask', 'where'):
        vbn__oqkmt = create_dataframe_mask_where_overload(func_name)
        overload_method(DataFrameType, func_name, no_unliteral=True)(vbn__oqkmt
            )


_install_dataframe_mask_where_overload()


def _validate_arguments_mask_where(func_name, df, cond, other, inplace,
    axis, level, errors, try_cast):
    dvves__ibrvv = dict(inplace=inplace, level=level, errors=errors,
        try_cast=try_cast)
    nwky__ohw = dict(inplace=False, level=None, errors='raise', try_cast=False)
    check_unsupported_args(f'{func_name}', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error(f'{func_name}(): axis argument not supported')
    if not (isinstance(cond, (SeriesType, types.Array, BooleanArrayType)) and
        (cond.ndim == 1 or cond.ndim == 2) and cond.dtype == types.bool_
        ) and not (isinstance(cond, DataFrameType) and cond.ndim == 2 and
        all(cond.data[i].dtype == types.bool_ for i in range(len(df.columns)))
        ):
        raise BodoError(
            f"{func_name}(): 'cond' argument must be a DataFrame, Series, 1- or 2-dimensional array of booleans"
            )
    iryek__rfuyn = len(df.columns)
    if hasattr(other, 'ndim') and (other.ndim != 1 or other.ndim != 2):
        if other.ndim == 2:
            if not isinstance(other, (DataFrameType, types.Array)):
                raise BodoError(
                    f"{func_name}(): 'other', if 2-dimensional, must be a DataFrame or array."
                    )
        elif other.ndim != 1:
            raise BodoError(
                f"{func_name}(): 'other' must be either 1 or 2-dimensional")
    if isinstance(other, DataFrameType):
        for i in range(iryek__rfuyn):
            if df.columns[i] in other.column_index:
                bodo.hiframes.series_impl._validate_self_other_mask_where(
                    func_name, 'Series', df.data[i], other.data[other.
                    column_index[df.columns[i]]])
            else:
                bodo.hiframes.series_impl._validate_self_other_mask_where(
                    func_name, 'Series', df.data[i], None, is_default=True)
    elif isinstance(other, SeriesType):
        for i in range(iryek__rfuyn):
            bodo.hiframes.series_impl._validate_self_other_mask_where(func_name
                , 'Series', df.data[i], other.data)
    else:
        for i in range(iryek__rfuyn):
            bodo.hiframes.series_impl._validate_self_other_mask_where(func_name
                , 'Series', df.data[i], other, max_ndim=2)


def _gen_init_df(header, columns, data_args, index=None, extra_globals=None):
    if index is None:
        index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)'
    if extra_globals is None:
        extra_globals = {}
    svd__hhwud = ColNamesMetaType(tuple(columns))
    data_args = '({}{})'.format(data_args, ',' if data_args else '')
    xood__fcig = f"""{header}  return bodo.hiframes.pd_dataframe_ext.init_dataframe({data_args}, {index}, __col_name_meta_value_gen_init_df)
"""
    hrbgo__eykz = {}
    hhmzo__opk = {'bodo': bodo, 'np': np, 'pd': pd, 'numba': numba,
        '__col_name_meta_value_gen_init_df': svd__hhwud}
    hhmzo__opk.update(extra_globals)
    exec(xood__fcig, hhmzo__opk, hrbgo__eykz)
    impl = hrbgo__eykz['impl']
    return impl


def _get_binop_columns(lhs, rhs, is_inplace=False):
    if lhs.columns != rhs.columns:
        xgfjg__vgex = pd.Index(lhs.columns)
        bbpc__jpkpu = pd.Index(rhs.columns)
        bypyx__esrss, cjpj__ches, mbmru__qrv = xgfjg__vgex.join(bbpc__jpkpu,
            how='left' if is_inplace else 'outer', level=None,
            return_indexers=True)
        return tuple(bypyx__esrss), cjpj__ches, mbmru__qrv
    return lhs.columns, range(len(lhs.columns)), range(len(lhs.columns))


def create_binary_op_overload(op):

    def overload_dataframe_binary_op(lhs, rhs):
        mfuye__kxl = numba.core.utils.OPERATORS_TO_BUILTINS[op]
        lkv__mnh = operator.eq, operator.ne
        check_runtime_cols_unsupported(lhs, mfuye__kxl)
        check_runtime_cols_unsupported(rhs, mfuye__kxl)
        if isinstance(lhs, DataFrameType):
            if isinstance(rhs, DataFrameType):
                bypyx__esrss, cjpj__ches, mbmru__qrv = _get_binop_columns(lhs,
                    rhs)
                data_args = ', '.join(
                    f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(lhs, {alw__qch}) {mfuye__kxl}bodo.hiframes.pd_dataframe_ext.get_dataframe_data(rhs, {dfdqj__fpbwk})'
                     if alw__qch != -1 and dfdqj__fpbwk != -1 else
                    f'bodo.libs.array_kernels.gen_na_array(len(lhs), float64_arr_type)'
                     for alw__qch, dfdqj__fpbwk in zip(cjpj__ches, mbmru__qrv))
                header = 'def impl(lhs, rhs):\n'
                index = (
                    'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(lhs)')
                return _gen_init_df(header, bypyx__esrss, data_args, index,
                    extra_globals={'float64_arr_type': types.Array(types.
                    float64, 1, 'C')})
            elif isinstance(rhs, SeriesType):
                raise_bodo_error(
                    'Comparison operation between Dataframe and Series is not supported yet.'
                    )
            sqn__tfro = []
            cxok__grfkl = []
            if op in lkv__mnh:
                for i, hjr__csg in enumerate(lhs.data):
                    if is_common_scalar_dtype([hjr__csg.dtype, rhs]):
                        sqn__tfro.append(
                            f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(lhs, {i}) {mfuye__kxl} rhs'
                            )
                    else:
                        atd__vga = f'arr{i}'
                        cxok__grfkl.append(atd__vga)
                        sqn__tfro.append(atd__vga)
                data_args = ', '.join(sqn__tfro)
            else:
                data_args = ', '.join(
                    f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(lhs, {i}) {mfuye__kxl} rhs'
                     for i in range(len(lhs.columns)))
            header = 'def impl(lhs, rhs):\n'
            if len(cxok__grfkl) > 0:
                header += '  numba.parfors.parfor.init_prange()\n'
                header += '  n = len(lhs)\n'
                header += ''.join(
                    f'  {atd__vga} = np.empty(n, dtype=np.bool_)\n' for
                    atd__vga in cxok__grfkl)
                header += (
                    '  for i in numba.parfors.parfor.internal_prange(n):\n')
                header += ''.join('    {0}[i] = {1}\n'.format(atd__vga, op ==
                    operator.ne) for atd__vga in cxok__grfkl)
            index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(lhs)'
            return _gen_init_df(header, lhs.columns, data_args, index)
        if isinstance(rhs, DataFrameType):
            if isinstance(lhs, SeriesType):
                raise_bodo_error(
                    'Comparison operation between Dataframe and Series is not supported yet.'
                    )
            sqn__tfro = []
            cxok__grfkl = []
            if op in lkv__mnh:
                for i, hjr__csg in enumerate(rhs.data):
                    if is_common_scalar_dtype([lhs, hjr__csg.dtype]):
                        sqn__tfro.append(
                            f'lhs {mfuye__kxl} bodo.hiframes.pd_dataframe_ext.get_dataframe_data(rhs, {i})'
                            )
                    else:
                        atd__vga = f'arr{i}'
                        cxok__grfkl.append(atd__vga)
                        sqn__tfro.append(atd__vga)
                data_args = ', '.join(sqn__tfro)
            else:
                data_args = ', '.join(
                    'lhs {1} bodo.hiframes.pd_dataframe_ext.get_dataframe_data(rhs, {0})'
                    .format(i, mfuye__kxl) for i in range(len(rhs.columns)))
            header = 'def impl(lhs, rhs):\n'
            if len(cxok__grfkl) > 0:
                header += '  numba.parfors.parfor.init_prange()\n'
                header += '  n = len(rhs)\n'
                header += ''.join('  {0} = np.empty(n, dtype=np.bool_)\n'.
                    format(atd__vga) for atd__vga in cxok__grfkl)
                header += (
                    '  for i in numba.parfors.parfor.internal_prange(n):\n')
                header += ''.join('    {0}[i] = {1}\n'.format(atd__vga, op ==
                    operator.ne) for atd__vga in cxok__grfkl)
            index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(rhs)'
            return _gen_init_df(header, rhs.columns, data_args, index)
    return overload_dataframe_binary_op


skips = [operator.lt, operator.le, operator.eq, operator.ne, operator.gt,
    operator.ge, operator.add, operator.sub, operator.mul, operator.truediv,
    operator.floordiv, operator.pow, operator.mod]


def _install_binary_ops():
    for op in bodo.hiframes.pd_series_ext.series_binary_ops:
        if op in skips:
            continue
        vbn__oqkmt = create_binary_op_overload(op)
        overload(op)(vbn__oqkmt)


_install_binary_ops()


def create_inplace_binary_op_overload(op):

    def overload_dataframe_inplace_binary_op(left, right):
        mfuye__kxl = numba.core.utils.OPERATORS_TO_BUILTINS[op]
        check_runtime_cols_unsupported(left, mfuye__kxl)
        check_runtime_cols_unsupported(right, mfuye__kxl)
        if isinstance(left, DataFrameType):
            if isinstance(right, DataFrameType):
                bypyx__esrss, _, mbmru__qrv = _get_binop_columns(left,
                    right, True)
                xood__fcig = 'def impl(left, right):\n'
                for i, dfdqj__fpbwk in enumerate(mbmru__qrv):
                    if dfdqj__fpbwk == -1:
                        xood__fcig += f"""  df_arr{i} = bodo.libs.array_kernels.gen_na_array(len(left), float64_arr_type)
"""
                        continue
                    xood__fcig += f"""  df_arr{i} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(left, {i})
"""
                    xood__fcig += f"""  df_arr{i} {mfuye__kxl} bodo.hiframes.pd_dataframe_ext.get_dataframe_data(right, {dfdqj__fpbwk})
"""
                data_args = ', '.join(f'df_arr{i}' for i in range(len(
                    bypyx__esrss)))
                index = (
                    'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(left)')
                return _gen_init_df(xood__fcig, bypyx__esrss, data_args,
                    index, extra_globals={'float64_arr_type': types.Array(
                    types.float64, 1, 'C')})
            xood__fcig = 'def impl(left, right):\n'
            for i in range(len(left.columns)):
                xood__fcig += (
                    """  df_arr{0} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(left, {0})
"""
                    .format(i))
                xood__fcig += '  df_arr{0} {1} right\n'.format(i, mfuye__kxl)
            data_args = ', '.join('df_arr{}'.format(i) for i in range(len(
                left.columns)))
            index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(left)'
            return _gen_init_df(xood__fcig, left.columns, data_args, index)
    return overload_dataframe_inplace_binary_op


def _install_inplace_binary_ops():
    for op in bodo.hiframes.pd_series_ext.series_inplace_binary_ops:
        vbn__oqkmt = create_inplace_binary_op_overload(op)
        overload(op, no_unliteral=True)(vbn__oqkmt)


_install_inplace_binary_ops()


def create_unary_op_overload(op):

    def overload_dataframe_unary_op(df):
        if isinstance(df, DataFrameType):
            mfuye__kxl = numba.core.utils.OPERATORS_TO_BUILTINS[op]
            check_runtime_cols_unsupported(df, mfuye__kxl)
            data_args = ', '.join(
                '{1} bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {0})'
                .format(i, mfuye__kxl) for i in range(len(df.columns)))
            header = 'def impl(df):\n'
            return _gen_init_df(header, df.columns, data_args)
    return overload_dataframe_unary_op


def _install_unary_ops():
    for op in bodo.hiframes.pd_series_ext.series_unary_ops:
        vbn__oqkmt = create_unary_op_overload(op)
        overload(op, no_unliteral=True)(vbn__oqkmt)


_install_unary_ops()


def overload_isna(obj):
    check_runtime_cols_unsupported(obj, 'pd.isna()')
    if isinstance(obj, (DataFrameType, SeriesType)
        ) or bodo.hiframes.pd_index_ext.is_pd_index_type(obj):
        return lambda obj: obj.isna()
    if is_array_typ(obj):

        def impl(obj):
            numba.parfors.parfor.init_prange()
            n = len(obj)
            lmbw__xjm = np.empty(n, np.bool_)
            for i in numba.parfors.parfor.internal_prange(n):
                lmbw__xjm[i] = bodo.libs.array_kernels.isna(obj, i)
            return lmbw__xjm
        return impl


overload(pd.isna, inline='always')(overload_isna)
overload(pd.isnull, inline='always')(overload_isna)


@overload(pd.isna)
@overload(pd.isnull)
def overload_isna_scalar(obj):
    if isinstance(obj, (DataFrameType, SeriesType)
        ) or bodo.hiframes.pd_index_ext.is_pd_index_type(obj) or is_array_typ(
        obj):
        return
    if isinstance(obj, (types.List, types.UniTuple)):

        def impl(obj):
            n = len(obj)
            lmbw__xjm = np.empty(n, np.bool_)
            for i in range(n):
                lmbw__xjm[i] = pd.isna(obj[i])
            return lmbw__xjm
        return impl
    obj = types.unliteral(obj)
    if obj == bodo.string_type:
        return lambda obj: unliteral_val(False)
    if isinstance(obj, types.Integer):
        return lambda obj: unliteral_val(False)
    if isinstance(obj, types.Float):
        return lambda obj: np.isnan(obj)
    if isinstance(obj, (types.NPDatetime, types.NPTimedelta)):
        return lambda obj: np.isnat(obj)
    if obj == types.none:
        return lambda obj: unliteral_val(True)
    if isinstance(obj, bodo.hiframes.pd_timestamp_ext.PandasTimestampType):
        return lambda obj: np.isnat(bodo.hiframes.pd_timestamp_ext.
            integer_to_dt64(obj.value))
    if obj == bodo.hiframes.datetime_timedelta_ext.pd_timedelta_type:
        return lambda obj: np.isnat(bodo.hiframes.pd_timestamp_ext.
            integer_to_timedelta64(obj.value))
    if isinstance(obj, types.Optional):
        return lambda obj: obj is None
    return lambda obj: unliteral_val(False)


@overload(operator.setitem, no_unliteral=True)
def overload_setitem_arr_none(A, idx, val):
    if is_array_typ(A, False) and isinstance(idx, types.Integer
        ) and val == types.none:
        return lambda A, idx, val: bodo.libs.array_kernels.setna(A, idx)


def overload_notna(obj):
    check_runtime_cols_unsupported(obj, 'pd.notna()')
    if isinstance(obj, (DataFrameType, SeriesType)):
        return lambda obj: obj.notna()
    if isinstance(obj, (types.List, types.UniTuple)) or is_array_typ(obj,
        include_index_series=True):
        return lambda obj: ~pd.isna(obj)
    return lambda obj: not pd.isna(obj)


overload(pd.notna, inline='always', no_unliteral=True)(overload_notna)
overload(pd.notnull, inline='always', no_unliteral=True)(overload_notna)


def _get_pd_dtype_str(t):
    if t.dtype == types.NPDatetime('ns'):
        return "'datetime64[ns]'"
    return bodo.ir.csv_ext._get_pd_dtype_str(t)


@overload_method(DataFrameType, 'replace', inline='always', no_unliteral=True)
def overload_dataframe_replace(df, to_replace=None, value=None, inplace=
    False, limit=None, regex=False, method='pad'):
    check_runtime_cols_unsupported(df, 'DataFrame.replace()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.replace()')
    if is_overload_none(to_replace):
        raise BodoError('replace(): to_replace value of None is not supported')
    hsn__bxq = {'inplace': inplace, 'limit': limit, 'regex': regex,
        'method': method}
    mawl__wldaq = {'inplace': False, 'limit': None, 'regex': False,
        'method': 'pad'}
    check_unsupported_args('replace', hsn__bxq, mawl__wldaq, package_name=
        'pandas', module_name='DataFrame')
    data_args = ', '.join(
        f'df.iloc[:, {i}].replace(to_replace, value).values' for i in range
        (len(df.columns)))
    header = """def impl(df, to_replace=None, value=None, inplace=False, limit=None, regex=False, method='pad'):
"""
    return _gen_init_df(header, df.columns, data_args)


def _is_col_access(expr_node):
    dorir__sqyvy = str(expr_node)
    return dorir__sqyvy.startswith('(left.') or dorir__sqyvy.startswith(
        '(right.')


def _insert_NA_cond(expr_node, left_columns, left_data, right_columns,
    right_data):
    fzd__cjsgb = {'left': 0, 'right': 0, 'NOT_NA': 0}
    env = pd.core.computation.scope.ensure_scope(2, {}, {}, (fzd__cjsgb,))
    yqems__jxxjm = pd.core.computation.parsing.clean_column_name

    def append_null_checks(expr_node, null_set):
        if not null_set:
            return expr_node
        uxv__bhdtl = ' & '.join([('NOT_NA.`' + x + '`') for x in null_set])
        jmuzg__qxrk = {('NOT_NA', yqems__jxxjm(hjr__csg)): hjr__csg for
            hjr__csg in null_set}
        hwarl__dlbch, _, _ = _parse_query_expr(uxv__bhdtl, env, [], [],
            None, join_cleaned_cols=jmuzg__qxrk)
        ukv__fezj = (pd.core.computation.ops.BinOp.
            _disallow_scalar_only_bool_ops)
        pd.core.computation.ops.BinOp._disallow_scalar_only_bool_ops = (lambda
            self: None)
        try:
            fdlzl__znwl = pd.core.computation.ops.BinOp('&', hwarl__dlbch,
                expr_node)
        finally:
            (pd.core.computation.ops.BinOp._disallow_scalar_only_bool_ops
                ) = ukv__fezj
        return fdlzl__znwl

    def _insert_NA_cond_body(expr_node, null_set):
        if isinstance(expr_node, pd.core.computation.ops.BinOp):
            if expr_node.op == '|':
                myui__fens = set()
                otkn__qvydo = set()
                hgb__npw = _insert_NA_cond_body(expr_node.lhs, myui__fens)
                cdw__slnl = _insert_NA_cond_body(expr_node.rhs, otkn__qvydo)
                wimk__mzxa = myui__fens.intersection(otkn__qvydo)
                myui__fens.difference_update(wimk__mzxa)
                otkn__qvydo.difference_update(wimk__mzxa)
                null_set.update(wimk__mzxa)
                expr_node.lhs = append_null_checks(hgb__npw, myui__fens)
                expr_node.rhs = append_null_checks(cdw__slnl, otkn__qvydo)
                expr_node.operands = expr_node.lhs, expr_node.rhs
            else:
                expr_node.lhs = _insert_NA_cond_body(expr_node.lhs, null_set)
                expr_node.rhs = _insert_NA_cond_body(expr_node.rhs, null_set)
        elif _is_col_access(expr_node):
            tin__lem = expr_node.name
            oyt__mbfr, col_name = tin__lem.split('.')
            if oyt__mbfr == 'left':
                rff__prbu = left_columns
                data = left_data
            else:
                rff__prbu = right_columns
                data = right_data
            howrv__pxo = data[rff__prbu.index(col_name)]
            if bodo.utils.typing.is_nullable(howrv__pxo):
                null_set.add(expr_node.name)
        return expr_node
    null_set = set()
    dxw__skp = _insert_NA_cond_body(expr_node, null_set)
    return append_null_checks(expr_node, null_set)


def _extract_equal_conds(expr_node):
    if not hasattr(expr_node, 'op'):
        return [], [], expr_node
    if expr_node.op == '==' and _is_col_access(expr_node.lhs
        ) and _is_col_access(expr_node.rhs):
        eklvn__lvq = str(expr_node.lhs)
        tozuf__mzpvp = str(expr_node.rhs)
        if eklvn__lvq.startswith('(left.') and tozuf__mzpvp.startswith('(left.'
            ) or eklvn__lvq.startswith('(right.') and tozuf__mzpvp.startswith(
            '(right.'):
            return [], [], expr_node
        left_on = [eklvn__lvq.split('.')[1][:-1]]
        right_on = [tozuf__mzpvp.split('.')[1][:-1]]
        if eklvn__lvq.startswith('(right.'):
            return right_on, left_on, None
        return left_on, right_on, None
    if expr_node.op == '&':
        azn__rrbpy, egznr__fvy, eny__jnitv = _extract_equal_conds(expr_node.lhs
            )
        bgw__jgtc, ovd__bzlo, gjfk__zppl = _extract_equal_conds(expr_node.rhs)
        left_on = azn__rrbpy + bgw__jgtc
        right_on = egznr__fvy + ovd__bzlo
        if eny__jnitv is None:
            return left_on, right_on, gjfk__zppl
        if gjfk__zppl is None:
            return left_on, right_on, eny__jnitv
        expr_node.lhs = eny__jnitv
        expr_node.rhs = gjfk__zppl
        expr_node.operands = expr_node.lhs, expr_node.rhs
        return left_on, right_on, expr_node
    return [], [], expr_node


def _parse_merge_cond(on_str, left_columns, left_data, right_columns,
    right_data):
    fzd__cjsgb = {'left': 0, 'right': 0}
    env = pd.core.computation.scope.ensure_scope(2, {}, {}, (fzd__cjsgb,))
    ozr__xool = dict()
    yqems__jxxjm = pd.core.computation.parsing.clean_column_name
    for name, aqkm__tlft in (('left', left_columns), ('right', right_columns)):
        for hjr__csg in aqkm__tlft:
            voqo__hwlr = yqems__jxxjm(hjr__csg)
            zsji__dqrwj = name, voqo__hwlr
            if zsji__dqrwj in ozr__xool:
                raise_bodo_error(
                    f"pd.merge(): {name} table contains two columns that are escaped to the same Python identifier '{hjr__csg}' and '{ozr__xool[voqo__hwlr]}' Please rename one of these columns. To avoid this issue, please use names that are valid Python identifiers."
                    )
            ozr__xool[zsji__dqrwj] = hjr__csg
    ehuv__nim, _, _ = _parse_query_expr(on_str, env, [], [], None,
        join_cleaned_cols=ozr__xool)
    left_on, right_on, ofig__feot = _extract_equal_conds(ehuv__nim.terms)
    return left_on, right_on, _insert_NA_cond(ofig__feot, left_columns,
        left_data, right_columns, right_data)


@overload_method(DataFrameType, 'merge', inline='always', no_unliteral=True)
@overload(pd.merge, inline='always', no_unliteral=True)
def overload_dataframe_merge(left, right, how='inner', on=None, left_on=
    None, right_on=None, left_index=False, right_index=False, sort=False,
    suffixes=('_x', '_y'), copy=True, indicator=False, validate=None,
    _bodo_na_equal=True):
    check_runtime_cols_unsupported(left, 'DataFrame.merge()')
    check_runtime_cols_unsupported(right, 'DataFrame.merge()')
    dvves__ibrvv = dict(sort=sort, copy=copy, validate=validate)
    nwky__ohw = dict(sort=False, copy=True, validate=None)
    check_unsupported_args('DataFrame.merge', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    validate_merge_spec(left, right, how, on, left_on, right_on, left_index,
        right_index, sort, suffixes, copy, indicator, validate)
    how = get_overload_const_str(how)
    utfns__reta = tuple(sorted(set(left.columns) & set(right.columns), key=
        lambda k: str(k)))
    cdwjr__ohp = ''
    if not is_overload_none(on):
        left_on = right_on = on
        if is_overload_constant_str(on):
            on_str = get_overload_const_str(on)
            if on_str not in utfns__reta and ('left.' in on_str or 'right.' in
                on_str):
                left_on, right_on, ipfdt__lvnr = _parse_merge_cond(on_str,
                    left.columns, left.data, right.columns, right.data)
                if ipfdt__lvnr is None:
                    cdwjr__ohp = ''
                else:
                    cdwjr__ohp = str(ipfdt__lvnr)
    if is_overload_none(on) and is_overload_none(left_on) and is_overload_none(
        right_on) and is_overload_false(left_index) and is_overload_false(
        right_index):
        left_keys = utfns__reta
        right_keys = utfns__reta
    else:
        if is_overload_true(left_index):
            left_keys = ['$_bodo_index_']
        else:
            left_keys = get_overload_const_list(left_on)
            validate_keys(left_keys, left)
        if is_overload_true(right_index):
            right_keys = ['$_bodo_index_']
        else:
            right_keys = get_overload_const_list(right_on)
            validate_keys(right_keys, right)
    if not is_overload_bool(indicator):
        raise_bodo_error(
            'DataFrame.merge(): indicator must be a constant boolean')
    indicator_val = get_overload_const_bool(indicator)
    if not is_overload_bool(_bodo_na_equal):
        raise_bodo_error(
            'DataFrame.merge(): bodo extension _bodo_na_equal must be a constant boolean'
            )
    sjdr__ayzju = get_overload_const_bool(_bodo_na_equal)
    validate_keys_length(left_index, right_index, left_keys, right_keys)
    validate_keys_dtypes(left, right, left_index, right_index, left_keys,
        right_keys)
    if is_overload_constant_tuple(suffixes):
        ciesw__pwtp = get_overload_const_tuple(suffixes)
    if is_overload_constant_list(suffixes):
        ciesw__pwtp = list(get_overload_const_list(suffixes))
    suffix_x = ciesw__pwtp[0]
    suffix_y = ciesw__pwtp[1]
    validate_unicity_output_column_names(suffix_x, suffix_y, left_keys,
        right_keys, left.columns, right.columns, indicator_val)
    left_keys = gen_const_tup(left_keys)
    right_keys = gen_const_tup(right_keys)
    xood__fcig = "def _impl(left, right, how='inner', on=None, left_on=None,\n"
    xood__fcig += (
        '    right_on=None, left_index=False, right_index=False, sort=False,\n'
        )
    xood__fcig += """    suffixes=('_x', '_y'), copy=True, indicator=False, validate=None, _bodo_na_equal=True):
"""
    xood__fcig += (
        """  return bodo.hiframes.pd_dataframe_ext.join_dummy(left, right, {}, {}, '{}', '{}', '{}', False, {}, {}, '{}')
"""
        .format(left_keys, right_keys, how, suffix_x, suffix_y,
        indicator_val, sjdr__ayzju, cdwjr__ohp))
    hrbgo__eykz = {}
    exec(xood__fcig, {'bodo': bodo}, hrbgo__eykz)
    _impl = hrbgo__eykz['_impl']
    return _impl


def common_validate_merge_merge_asof_spec(name_func, left, right, on,
    left_on, right_on, left_index, right_index, suffixes):
    if not isinstance(left, DataFrameType) or not isinstance(right,
        DataFrameType):
        raise BodoError(name_func + '() requires dataframe inputs')
    valid_dataframe_column_types = (ArrayItemArrayType, MapArrayType,
        StructArrayType, CategoricalArrayType, types.Array,
        IntegerArrayType, FloatingArrayType, DecimalArrayType,
        IntervalArrayType, bodo.DatetimeArrayType, TimeArrayType)
    qdkvt__cay = {string_array_type, dict_str_arr_type, binary_array_type,
        datetime_date_array_type, datetime_timedelta_array_type, boolean_array}
    odbx__fpmb = {get_overload_const_str(emwr__ekaq) for emwr__ekaq in (
        left_on, right_on, on) if is_overload_constant_str(emwr__ekaq)}
    for df in (left, right):
        for i, hjr__csg in enumerate(df.data):
            if not isinstance(hjr__csg, valid_dataframe_column_types
                ) and hjr__csg not in qdkvt__cay:
                raise BodoError(
                    f'{name_func}(): use of column with {type(hjr__csg)} in merge unsupported'
                    )
            if df.columns[i] in odbx__fpmb and isinstance(hjr__csg,
                MapArrayType):
                raise BodoError(
                    f'{name_func}(): merge on MapArrayType unsupported')
    ensure_constant_arg(name_func, 'left_index', left_index, bool)
    ensure_constant_arg(name_func, 'right_index', right_index, bool)
    if not is_overload_constant_tuple(suffixes
        ) and not is_overload_constant_list(suffixes):
        raise_bodo_error(name_func +
            "(): suffixes parameters should be ['_left', '_right']")
    if is_overload_constant_tuple(suffixes):
        ciesw__pwtp = get_overload_const_tuple(suffixes)
    if is_overload_constant_list(suffixes):
        ciesw__pwtp = list(get_overload_const_list(suffixes))
    if len(ciesw__pwtp) != 2:
        raise BodoError(name_func +
            '(): The number of suffixes should be exactly 2')
    utfns__reta = tuple(set(left.columns) & set(right.columns))
    if not is_overload_none(on):
        hghwt__gre = False
        if is_overload_constant_str(on):
            on_str = get_overload_const_str(on)
            hghwt__gre = on_str not in utfns__reta and ('left.' in on_str or
                'right.' in on_str)
        if len(utfns__reta) == 0 and not hghwt__gre:
            raise_bodo_error(name_func +
                '(): No common columns to perform merge on. Merge options: left_on={lon}, right_on={ron}, left_index={lidx}, right_index={ridx}'
                .format(lon=is_overload_true(left_on), ron=is_overload_true
                (right_on), lidx=is_overload_true(left_index), ridx=
                is_overload_true(right_index)))
        if not is_overload_none(left_on) or not is_overload_none(right_on):
            raise BodoError(name_func +
                '(): Can only pass argument "on" OR "left_on" and "right_on", not a combination of both.'
                )
    if (is_overload_true(left_index) or not is_overload_none(left_on)
        ) and is_overload_none(right_on) and not is_overload_true(right_index):
        raise BodoError(name_func +
            '(): Must pass right_on or right_index=True')
    if (is_overload_true(right_index) or not is_overload_none(right_on)
        ) and is_overload_none(left_on) and not is_overload_true(left_index):
        raise BodoError(name_func + '(): Must pass left_on or left_index=True')


def validate_merge_spec(left, right, how, on, left_on, right_on, left_index,
    right_index, sort, suffixes, copy, indicator, validate):
    common_validate_merge_merge_asof_spec('merge', left, right, on, left_on,
        right_on, left_index, right_index, suffixes)
    ensure_constant_values('merge', 'how', how, ('left', 'right', 'outer',
        'inner', 'cross'))


def validate_merge_asof_spec(left, right, on, left_on, right_on, left_index,
    right_index, by, left_by, right_by, suffixes, tolerance,
    allow_exact_matches, direction):
    common_validate_merge_merge_asof_spec('merge_asof', left, right, on,
        left_on, right_on, left_index, right_index, suffixes)
    if not is_overload_true(allow_exact_matches):
        raise BodoError(
            'merge_asof(): allow_exact_matches parameter only supports default value True'
            )
    if not is_overload_none(tolerance):
        raise BodoError(
            'merge_asof(): tolerance parameter only supports default value None'
            )
    if not is_overload_none(by):
        raise BodoError(
            'merge_asof(): by parameter only supports default value None')
    if not is_overload_none(left_by):
        raise BodoError(
            'merge_asof(): left_by parameter only supports default value None')
    if not is_overload_none(right_by):
        raise BodoError(
            'merge_asof(): right_by parameter only supports default value None'
            )
    if not is_overload_constant_str(direction):
        raise BodoError(
            'merge_asof(): direction parameter should be of type str')
    else:
        direction = get_overload_const_str(direction)
        if direction != 'backward':
            raise BodoError(
                "merge_asof(): direction parameter only supports default value 'backward'"
                )


def validate_merge_asof_keys_length(left_on, right_on, left_index,
    right_index, left_keys, right_keys):
    if not is_overload_true(left_index) and not is_overload_true(right_index):
        if len(right_keys) != len(left_keys):
            raise BodoError('merge(): len(right_on) must equal len(left_on)')
    if not is_overload_none(left_on) and is_overload_true(right_index):
        raise BodoError(
            'merge(): right_index = True and specifying left_on is not suppported yet.'
            )
    if not is_overload_none(right_on) and is_overload_true(left_index):
        raise BodoError(
            'merge(): left_index = True and specifying right_on is not suppported yet.'
            )


def validate_keys_length(left_index, right_index, left_keys, right_keys):
    if not is_overload_true(left_index) and not is_overload_true(right_index):
        if len(right_keys) != len(left_keys):
            raise BodoError('merge(): len(right_on) must equal len(left_on)')
    if is_overload_true(right_index):
        if len(left_keys) != 1:
            raise BodoError(
                'merge(): len(left_on) must equal the number of levels in the index of "right", which is 1'
                )
    if is_overload_true(left_index):
        if len(right_keys) != 1:
            raise BodoError(
                'merge(): len(right_on) must equal the number of levels in the index of "left", which is 1'
                )


def validate_keys_dtypes(left, right, left_index, right_index, left_keys,
    right_keys):
    mivr__xnx = numba.core.registry.cpu_target.typing_context
    if is_overload_true(left_index) or is_overload_true(right_index):
        if is_overload_true(left_index) and is_overload_true(right_index):
            twsm__xiadi = left.index
            qpt__gymt = isinstance(twsm__xiadi, StringIndexType)
            qmbk__ikct = right.index
            wdi__gpcck = isinstance(qmbk__ikct, StringIndexType)
        elif is_overload_true(left_index):
            twsm__xiadi = left.index
            qpt__gymt = isinstance(twsm__xiadi, StringIndexType)
            qmbk__ikct = right.data[right.columns.index(right_keys[0])]
            wdi__gpcck = qmbk__ikct.dtype == string_type
        elif is_overload_true(right_index):
            twsm__xiadi = left.data[left.columns.index(left_keys[0])]
            qpt__gymt = twsm__xiadi.dtype == string_type
            qmbk__ikct = right.index
            wdi__gpcck = isinstance(qmbk__ikct, StringIndexType)
        if qpt__gymt and wdi__gpcck:
            return
        twsm__xiadi = twsm__xiadi.dtype
        qmbk__ikct = qmbk__ikct.dtype
        try:
            vbk__psywm = mivr__xnx.resolve_function_type(operator.eq, (
                twsm__xiadi, qmbk__ikct), {})
        except:
            raise_bodo_error(
                'merge: You are trying to merge on {lk_dtype} and {rk_dtype} columns. If you wish to proceed you should use pd.concat'
                .format(lk_dtype=twsm__xiadi, rk_dtype=qmbk__ikct))
    else:
        for tvvgg__gjnj, xzzt__vyzhf in zip(left_keys, right_keys):
            twsm__xiadi = left.data[left.columns.index(tvvgg__gjnj)].dtype
            lmzs__defpt = left.data[left.columns.index(tvvgg__gjnj)]
            qmbk__ikct = right.data[right.columns.index(xzzt__vyzhf)].dtype
            ahvql__fhl = right.data[right.columns.index(xzzt__vyzhf)]
            if lmzs__defpt == ahvql__fhl:
                continue
            vhgdx__nkgg = (
                'merge: You are trying to merge on column {lk} of {lk_dtype} and column {rk} of {rk_dtype}. If you wish to proceed you should use pd.concat'
                .format(lk=tvvgg__gjnj, lk_dtype=twsm__xiadi, rk=
                xzzt__vyzhf, rk_dtype=qmbk__ikct))
            rxnrt__rlkey = twsm__xiadi == string_type
            yylf__gpavx = qmbk__ikct == string_type
            if rxnrt__rlkey ^ yylf__gpavx:
                raise_bodo_error(vhgdx__nkgg)
            try:
                vbk__psywm = mivr__xnx.resolve_function_type(operator.eq, (
                    twsm__xiadi, qmbk__ikct), {})
            except:
                raise_bodo_error(vhgdx__nkgg)


def validate_keys(keys, df):
    gzloz__dhhyb = set(keys).difference(set(df.columns))
    if len(gzloz__dhhyb) > 0:
        if is_overload_constant_str(df.index.name_typ
            ) and get_overload_const_str(df.index.name_typ) in gzloz__dhhyb:
            raise_bodo_error(
                f'merge(): use of index {df.index.name_typ} as key for on/left_on/right_on is unsupported'
                )
        raise_bodo_error(
            f"""merge(): invalid key {gzloz__dhhyb} for on/left_on/right_on
merge supports only valid column names {df.columns}"""
            )


@overload_method(DataFrameType, 'join', inline='always', no_unliteral=True)
def overload_dataframe_join(left, other, on=None, how='left', lsuffix='',
    rsuffix='', sort=False):
    check_runtime_cols_unsupported(left, 'DataFrame.join()')
    check_runtime_cols_unsupported(other, 'DataFrame.join()')
    dvves__ibrvv = dict(lsuffix=lsuffix, rsuffix=rsuffix)
    nwky__ohw = dict(lsuffix='', rsuffix='')
    check_unsupported_args('DataFrame.join', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    validate_join_spec(left, other, on, how, lsuffix, rsuffix, sort)
    how = get_overload_const_str(how)
    if not is_overload_none(on):
        left_keys = get_overload_const_list(on)
    else:
        left_keys = ['$_bodo_index_']
    right_keys = ['$_bodo_index_']
    left_keys = gen_const_tup(left_keys)
    right_keys = gen_const_tup(right_keys)
    xood__fcig = "def _impl(left, other, on=None, how='left',\n"
    xood__fcig += "    lsuffix='', rsuffix='', sort=False):\n"
    xood__fcig += (
        """  return bodo.hiframes.pd_dataframe_ext.join_dummy(left, other, {}, {}, '{}', '{}', '{}', True, False, True, '')
"""
        .format(left_keys, right_keys, how, lsuffix, rsuffix))
    hrbgo__eykz = {}
    exec(xood__fcig, {'bodo': bodo}, hrbgo__eykz)
    _impl = hrbgo__eykz['_impl']
    return _impl


def validate_join_spec(left, other, on, how, lsuffix, rsuffix, sort):
    if not isinstance(other, DataFrameType):
        raise BodoError('join() requires dataframe inputs')
    ensure_constant_values('merge', 'how', how, ('left', 'right', 'outer',
        'inner'))
    if not is_overload_none(on) and len(get_overload_const_list(on)) != 1:
        raise BodoError('join(): len(on) must equals to 1 when specified.')
    if not is_overload_none(on):
        egk__cmwdk = get_overload_const_list(on)
        validate_keys(egk__cmwdk, left)
    if not is_overload_false(sort):
        raise BodoError(
            'join(): sort parameter only supports default value False')
    utfns__reta = tuple(set(left.columns) & set(other.columns))
    if len(utfns__reta) > 0:
        raise_bodo_error(
            'join(): not supporting joining on overlapping columns:{cols} Use DataFrame.merge() instead.'
            .format(cols=utfns__reta))


def validate_unicity_output_column_names(suffix_x, suffix_y, left_keys,
    right_keys, left_columns, right_columns, indicator_val):
    lbvc__dkgjk = set(left_keys) & set(right_keys)
    izija__acx = set(left_columns) & set(right_columns)
    uzjg__zxbik = izija__acx - lbvc__dkgjk
    imjg__hknyf = set(left_columns) - izija__acx
    csoxo__mfir = set(right_columns) - izija__acx
    rqhz__yzlnx = {}

    def insertOutColumn(col_name):
        if col_name in rqhz__yzlnx:
            raise_bodo_error(
                'join(): two columns happen to have the same name : {}'.
                format(col_name))
        rqhz__yzlnx[col_name] = 0
    for jrrzo__oxpqf in lbvc__dkgjk:
        insertOutColumn(jrrzo__oxpqf)
    for jrrzo__oxpqf in uzjg__zxbik:
        yngst__ksh = str(jrrzo__oxpqf) + suffix_x
        xurxy__dqo = str(jrrzo__oxpqf) + suffix_y
        insertOutColumn(yngst__ksh)
        insertOutColumn(xurxy__dqo)
    for jrrzo__oxpqf in imjg__hknyf:
        insertOutColumn(jrrzo__oxpqf)
    for jrrzo__oxpqf in csoxo__mfir:
        insertOutColumn(jrrzo__oxpqf)
    if indicator_val:
        insertOutColumn('_merge')


@overload(pd.merge_asof, inline='always', no_unliteral=True)
def overload_dataframe_merge_asof(left, right, on=None, left_on=None,
    right_on=None, left_index=False, right_index=False, by=None, left_by=
    None, right_by=None, suffixes=('_x', '_y'), tolerance=None,
    allow_exact_matches=True, direction='backward'):
    raise BodoError('pandas.merge_asof() not support yet')
    validate_merge_asof_spec(left, right, on, left_on, right_on, left_index,
        right_index, by, left_by, right_by, suffixes, tolerance,
        allow_exact_matches, direction)
    if not isinstance(left, DataFrameType) or not isinstance(right,
        DataFrameType):
        raise BodoError('merge_asof() requires dataframe inputs')
    utfns__reta = tuple(sorted(set(left.columns) & set(right.columns), key=
        lambda k: str(k)))
    if not is_overload_none(on):
        left_on = right_on = on
    if is_overload_none(on) and is_overload_none(left_on) and is_overload_none(
        right_on) and is_overload_false(left_index) and is_overload_false(
        right_index):
        left_keys = utfns__reta
        right_keys = utfns__reta
    else:
        if is_overload_true(left_index):
            left_keys = ['$_bodo_index_']
        else:
            left_keys = get_overload_const_list(left_on)
            validate_keys(left_keys, left)
        if is_overload_true(right_index):
            right_keys = ['$_bodo_index_']
        else:
            right_keys = get_overload_const_list(right_on)
            validate_keys(right_keys, right)
    validate_merge_asof_keys_length(left_on, right_on, left_index,
        right_index, left_keys, right_keys)
    validate_keys_dtypes(left, right, left_index, right_index, left_keys,
        right_keys)
    left_keys = gen_const_tup(left_keys)
    right_keys = gen_const_tup(right_keys)
    if isinstance(suffixes, tuple):
        ciesw__pwtp = suffixes
    if is_overload_constant_list(suffixes):
        ciesw__pwtp = list(get_overload_const_list(suffixes))
    if isinstance(suffixes, types.Omitted):
        ciesw__pwtp = suffixes.value
    suffix_x = ciesw__pwtp[0]
    suffix_y = ciesw__pwtp[1]
    xood__fcig = (
        'def _impl(left, right, on=None, left_on=None, right_on=None,\n')
    xood__fcig += (
        '    left_index=False, right_index=False, by=None, left_by=None,\n')
    xood__fcig += "    right_by=None, suffixes=('_x', '_y'), tolerance=None,\n"
    xood__fcig += "    allow_exact_matches=True, direction='backward'):\n"
    xood__fcig += '  suffix_x = suffixes[0]\n'
    xood__fcig += '  suffix_y = suffixes[1]\n'
    xood__fcig += (
        """  return bodo.hiframes.pd_dataframe_ext.join_dummy(left, right, {}, {}, 'asof', '{}', '{}', False, False, True, '')
"""
        .format(left_keys, right_keys, suffix_x, suffix_y))
    hrbgo__eykz = {}
    exec(xood__fcig, {'bodo': bodo}, hrbgo__eykz)
    _impl = hrbgo__eykz['_impl']
    return _impl


@overload_method(DataFrameType, 'groupby', inline='always', no_unliteral=True)
def overload_dataframe_groupby(df, by=None, axis=0, level=None, as_index=
    True, sort=False, group_keys=True, squeeze=False, observed=True, dropna
    =True, _bodo_num_shuffle_keys=-1):
    check_runtime_cols_unsupported(df, 'DataFrame.groupby()')
    validate_groupby_spec(df, by, axis, level, as_index, sort, group_keys,
        squeeze, observed, dropna, _bodo_num_shuffle_keys)

    def _impl(df, by=None, axis=0, level=None, as_index=True, sort=False,
        group_keys=True, squeeze=False, observed=True, dropna=True,
        _bodo_num_shuffle_keys=-1):
        return bodo.hiframes.pd_groupby_ext.init_groupby(df, by, as_index,
            dropna, _bodo_num_shuffle_keys)
    return _impl


def validate_groupby_spec(df, by, axis, level, as_index, sort, group_keys,
    squeeze, observed, dropna, _num_shuffle_keys):
    if is_overload_none(by):
        raise BodoError("groupby(): 'by' must be supplied.")
    if not is_overload_zero(axis):
        raise BodoError(
            "groupby(): 'axis' parameter only supports integer value 0.")
    if not is_overload_none(level):
        raise BodoError(
            "groupby(): 'level' is not supported since MultiIndex is not supported."
            )
    if not is_literal_type(by) and not is_overload_constant_list(by):
        raise_bodo_error(
            f"groupby(): 'by' parameter only supports a constant column label or column labels, not {by}."
            )
    if len(set(get_overload_const_list(by)).difference(set(df.columns))) > 0:
        raise_bodo_error(
            "groupby(): invalid key {} for 'by' (not available in columns {})."
            .format(get_overload_const_list(by), df.columns))
    if not is_overload_constant_bool(as_index):
        raise_bodo_error(
            "groupby(): 'as_index' parameter must be a constant bool, not {}."
            .format(as_index))
    if not is_overload_constant_bool(dropna):
        raise_bodo_error(
            "groupby(): 'dropna' parameter must be a constant bool, not {}."
            .format(dropna))
    if not is_overload_constant_int(_num_shuffle_keys):
        raise_bodo_error(
            f"groupby(): '_num_shuffle_keys' parameter must be a constant integer, not {_num_shuffle_keys}."
            )
    dvves__ibrvv = dict(sort=sort, group_keys=group_keys, squeeze=squeeze,
        observed=observed)
    ous__zajx = dict(sort=False, group_keys=True, squeeze=False, observed=True)
    check_unsupported_args('Dataframe.groupby', dvves__ibrvv, ous__zajx,
        package_name='pandas', module_name='GroupBy')


def pivot_error_checking(df, index, columns, values, func_name):
    zldj__usu = func_name == 'DataFrame.pivot_table'
    if zldj__usu:
        if is_overload_none(index) or not is_literal_type(index):
            raise_bodo_error(
                f"DataFrame.pivot_table(): 'index' argument is required and must be constant column labels"
                )
    elif not is_overload_none(index) and not is_literal_type(index):
        raise_bodo_error(
            f"{func_name}(): if 'index' argument is provided it must be constant column labels"
            )
    if is_overload_none(columns) or not is_literal_type(columns):
        raise_bodo_error(
            f"{func_name}(): 'columns' argument is required and must be a constant column label"
            )
    if not is_overload_none(values) and not is_literal_type(values):
        raise_bodo_error(
            f"{func_name}(): if 'values' argument is provided it must be constant column labels"
            )
    kewd__asihh = get_literal_value(columns)
    if isinstance(kewd__asihh, (list, tuple)):
        if len(kewd__asihh) > 1:
            raise BodoError(
                f"{func_name}(): 'columns' argument must be a constant column label not a {kewd__asihh}"
                )
        kewd__asihh = kewd__asihh[0]
    if kewd__asihh not in df.columns:
        raise BodoError(
            f"{func_name}(): 'columns' column {kewd__asihh} not found in DataFrame {df}."
            )
    cvp__qjvb = df.column_index[kewd__asihh]
    if is_overload_none(index):
        qbiqq__gmhdj = []
        uejf__upy = []
    else:
        uejf__upy = get_literal_value(index)
        if not isinstance(uejf__upy, (list, tuple)):
            uejf__upy = [uejf__upy]
        qbiqq__gmhdj = []
        for index in uejf__upy:
            if index not in df.column_index:
                raise BodoError(
                    f"{func_name}(): 'index' column {index} not found in DataFrame {df}."
                    )
            qbiqq__gmhdj.append(df.column_index[index])
    if not (all(isinstance(ahner__puklw, int) for ahner__puklw in uejf__upy
        ) or all(isinstance(ahner__puklw, str) for ahner__puklw in uejf__upy)):
        raise BodoError(
            f"{func_name}(): column names selected for 'index' must all share a common int or string type. Please convert your names to a common type using DataFrame.rename()"
            )
    if is_overload_none(values):
        hwu__kklow = []
        jan__bkbr = []
        kfda__vopkp = qbiqq__gmhdj + [cvp__qjvb]
        for i, ahner__puklw in enumerate(df.columns):
            if i not in kfda__vopkp:
                hwu__kklow.append(i)
                jan__bkbr.append(ahner__puklw)
    else:
        jan__bkbr = get_literal_value(values)
        if not isinstance(jan__bkbr, (list, tuple)):
            jan__bkbr = [jan__bkbr]
        hwu__kklow = []
        for val in jan__bkbr:
            if val not in df.column_index:
                raise BodoError(
                    f"{func_name}(): 'values' column {val} not found in DataFrame {df}."
                    )
            hwu__kklow.append(df.column_index[val])
    rmbgh__ohkad = set(hwu__kklow) | set(qbiqq__gmhdj) | {cvp__qjvb}
    if len(rmbgh__ohkad) != len(hwu__kklow) + len(qbiqq__gmhdj) + 1:
        raise BodoError(
            f"{func_name}(): 'index', 'columns', and 'values' must all refer to different columns"
            )

    def check_valid_index_typ(index_column):
        if isinstance(index_column, (bodo.ArrayItemArrayType, bodo.
            MapArrayType, bodo.StructArrayType, bodo.TupleArrayType, bodo.
            IntervalArrayType)):
            raise BodoError(
                f"{func_name}(): 'index' DataFrame column must have scalar rows"
                )
        if isinstance(index_column, bodo.CategoricalArrayType):
            raise BodoError(
                f"{func_name}(): 'index' DataFrame column does not support categorical data"
                )
    if len(qbiqq__gmhdj) == 0:
        index = df.index
        if isinstance(index, MultiIndexType):
            raise BodoError(
                f"{func_name}(): 'index' cannot be None with a DataFrame with a multi-index"
                )
        if not isinstance(index, RangeIndexType):
            check_valid_index_typ(index.data)
        if not is_literal_type(df.index.name_typ):
            raise BodoError(
                f"{func_name}(): If 'index' is None, the name of the DataFrame's Index must be constant at compile-time"
                )
    else:
        for luwpq__pshp in qbiqq__gmhdj:
            index_column = df.data[luwpq__pshp]
            check_valid_index_typ(index_column)
    era__ehqka = df.data[cvp__qjvb]
    if isinstance(era__ehqka, (bodo.ArrayItemArrayType, bodo.MapArrayType,
        bodo.StructArrayType, bodo.TupleArrayType, bodo.IntervalArrayType)):
        raise BodoError(
            f"{func_name}(): 'columns' DataFrame column must have scalar rows")
    if isinstance(era__ehqka, bodo.CategoricalArrayType):
        raise BodoError(
            f"{func_name}(): 'columns' DataFrame column does not support categorical data"
            )
    for hyqtd__zca in hwu__kklow:
        zuwqa__yljpk = df.data[hyqtd__zca]
        if isinstance(zuwqa__yljpk, (bodo.ArrayItemArrayType, bodo.
            MapArrayType, bodo.StructArrayType, bodo.TupleArrayType)
            ) or zuwqa__yljpk == bodo.binary_array_type:
            raise BodoError(
                f"{func_name}(): 'values' DataFrame column must have scalar rows"
                )
    return (uejf__upy, kewd__asihh, jan__bkbr, qbiqq__gmhdj, cvp__qjvb,
        hwu__kklow)


@overload(pd.pivot, inline='always', no_unliteral=True)
@overload_method(DataFrameType, 'pivot', inline='always', no_unliteral=True)
def overload_dataframe_pivot(data, index=None, columns=None, values=None):
    check_runtime_cols_unsupported(data, 'DataFrame.pivot()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(data,
        'DataFrame.pivot()')
    if not isinstance(data, DataFrameType):
        raise BodoError("pandas.pivot(): 'data' argument must be a DataFrame")
    (uejf__upy, kewd__asihh, jan__bkbr, luwpq__pshp, cvp__qjvb, awk__hfhd) = (
        pivot_error_checking(data, index, columns, values, 'DataFrame.pivot'))
    if len(uejf__upy) == 0:
        if is_overload_none(data.index.name_typ):
            zvlly__soqd = None,
        else:
            zvlly__soqd = get_literal_value(data.index.name_typ),
    else:
        zvlly__soqd = tuple(uejf__upy)
    uejf__upy = ColNamesMetaType(zvlly__soqd)
    jan__bkbr = ColNamesMetaType(tuple(jan__bkbr))
    kewd__asihh = ColNamesMetaType((kewd__asihh,))
    xood__fcig = 'def impl(data, index=None, columns=None, values=None):\n'
    xood__fcig += "    ev = tracing.Event('df.pivot')\n"
    xood__fcig += f'    pivot_values = data.iloc[:, {cvp__qjvb}].unique()\n'
    xood__fcig += '    result = bodo.hiframes.pd_dataframe_ext.pivot_impl(\n'
    if len(luwpq__pshp) == 0:
        xood__fcig += f"""        (bodo.utils.conversion.index_to_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(data)),),
"""
    else:
        xood__fcig += '        (\n'
        for zeym__mgzpr in luwpq__pshp:
            xood__fcig += f"""            bodo.hiframes.pd_dataframe_ext.get_dataframe_data(data, {zeym__mgzpr}),
"""
        xood__fcig += '        ),\n'
    xood__fcig += f"""        (bodo.hiframes.pd_dataframe_ext.get_dataframe_data(data, {cvp__qjvb}),),
"""
    xood__fcig += '        (\n'
    for hyqtd__zca in awk__hfhd:
        xood__fcig += f"""            bodo.hiframes.pd_dataframe_ext.get_dataframe_data(data, {hyqtd__zca}),
"""
    xood__fcig += '        ),\n'
    xood__fcig += '        pivot_values,\n'
    xood__fcig += '        index_lit,\n'
    xood__fcig += '        columns_lit,\n'
    xood__fcig += '        values_lit,\n'
    xood__fcig += '    )\n'
    xood__fcig += '    ev.finalize()\n'
    xood__fcig += '    return result\n'
    hrbgo__eykz = {}
    exec(xood__fcig, {'bodo': bodo, 'index_lit': uejf__upy, 'columns_lit':
        kewd__asihh, 'values_lit': jan__bkbr, 'tracing': tracing}, hrbgo__eykz)
    impl = hrbgo__eykz['impl']
    return impl


@overload(pd.pivot_table, inline='always', no_unliteral=True)
@overload_method(DataFrameType, 'pivot_table', inline='always',
    no_unliteral=True)
def overload_dataframe_pivot_table(data, values=None, index=None, columns=
    None, aggfunc='mean', fill_value=None, margins=False, dropna=True,
    margins_name='All', observed=False, sort=True, _pivot_values=None):
    check_runtime_cols_unsupported(data, 'DataFrame.pivot_table()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(data,
        'DataFrame.pivot_table()')
    dvves__ibrvv = dict(fill_value=fill_value, margins=margins, dropna=
        dropna, margins_name=margins_name, observed=observed, sort=sort)
    nwky__ohw = dict(fill_value=None, margins=False, dropna=True,
        margins_name='All', observed=False, sort=True)
    check_unsupported_args('DataFrame.pivot_table', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    if not isinstance(data, DataFrameType):
        raise BodoError(
            "pandas.pivot_table(): 'data' argument must be a DataFrame")
    (uejf__upy, kewd__asihh, jan__bkbr, luwpq__pshp, cvp__qjvb, awk__hfhd) = (
        pivot_error_checking(data, index, columns, values,
        'DataFrame.pivot_table'))
    nvky__kivos = uejf__upy
    uejf__upy = ColNamesMetaType(tuple(uejf__upy))
    jan__bkbr = ColNamesMetaType(tuple(jan__bkbr))
    qiqzu__yli = kewd__asihh
    kewd__asihh = ColNamesMetaType((kewd__asihh,))
    xood__fcig = 'def impl(\n'
    xood__fcig += '    data,\n'
    xood__fcig += '    values=None,\n'
    xood__fcig += '    index=None,\n'
    xood__fcig += '    columns=None,\n'
    xood__fcig += '    aggfunc="mean",\n'
    xood__fcig += '    fill_value=None,\n'
    xood__fcig += '    margins=False,\n'
    xood__fcig += '    dropna=True,\n'
    xood__fcig += '    margins_name="All",\n'
    xood__fcig += '    observed=False,\n'
    xood__fcig += '    sort=True,\n'
    xood__fcig += '    _pivot_values=None,\n'
    xood__fcig += '):\n'
    xood__fcig += "    ev = tracing.Event('df.pivot_table')\n"
    len__fwk = luwpq__pshp + [cvp__qjvb] + awk__hfhd
    xood__fcig += f'    data = data.iloc[:, {len__fwk}]\n'
    udg__acqb = nvky__kivos + [qiqzu__yli]
    if not is_overload_none(_pivot_values):
        fvkd__snw = tuple(sorted(_pivot_values.meta))
        _pivot_values = ColNamesMetaType(fvkd__snw)
        xood__fcig += '    pivot_values = _pivot_values_arr\n'
        xood__fcig += (
            f'    data = data[data.iloc[:, {len(luwpq__pshp)}].isin(pivot_values)]\n'
            )
        if all(isinstance(ahner__puklw, str) for ahner__puklw in fvkd__snw):
            mmbc__vky = pd.array(fvkd__snw, 'string')
        elif all(isinstance(ahner__puklw, int) for ahner__puklw in fvkd__snw):
            mmbc__vky = np.array(fvkd__snw, 'int64')
        else:
            raise BodoError(
                f'pivot(): pivot values selcected via pivot JIT argument must all share a common int or string type.'
                )
    else:
        mmbc__vky = None
    ntid__swn = is_overload_constant_str(aggfunc) and get_overload_const_str(
        aggfunc) == 'nunique'
    attbq__blim = len(udg__acqb) if ntid__swn else len(nvky__kivos)
    xood__fcig += f"""    data = data.groupby({udg__acqb!r}, as_index=False, _bodo_num_shuffle_keys={attbq__blim}).agg(aggfunc)
"""
    if is_overload_none(_pivot_values):
        xood__fcig += (
            f'    pivot_values = data.iloc[:, {len(luwpq__pshp)}].unique()\n')
    xood__fcig += '    result = bodo.hiframes.pd_dataframe_ext.pivot_impl(\n'
    xood__fcig += '        (\n'
    for i in range(0, len(luwpq__pshp)):
        xood__fcig += (
            f'            bodo.hiframes.pd_dataframe_ext.get_dataframe_data(data, {i}),\n'
            )
    xood__fcig += '        ),\n'
    xood__fcig += f"""        (bodo.hiframes.pd_dataframe_ext.get_dataframe_data(data, {len(luwpq__pshp)}),),
"""
    xood__fcig += '        (\n'
    for i in range(len(luwpq__pshp) + 1, len(awk__hfhd) + len(luwpq__pshp) + 1
        ):
        xood__fcig += (
            f'            bodo.hiframes.pd_dataframe_ext.get_dataframe_data(data, {i}),\n'
            )
    xood__fcig += '        ),\n'
    xood__fcig += '        pivot_values,\n'
    xood__fcig += '        index_lit,\n'
    xood__fcig += '        columns_lit,\n'
    xood__fcig += '        values_lit,\n'
    xood__fcig += '        check_duplicates=False,\n'
    xood__fcig += f'        is_already_shuffled={not ntid__swn},\n'
    xood__fcig += '        _constant_pivot_values=_constant_pivot_values,\n'
    xood__fcig += '    )\n'
    xood__fcig += '    ev.finalize()\n'
    xood__fcig += '    return result\n'
    hrbgo__eykz = {}
    exec(xood__fcig, {'bodo': bodo, 'numba': numba, 'index_lit': uejf__upy,
        'columns_lit': kewd__asihh, 'values_lit': jan__bkbr,
        '_pivot_values_arr': mmbc__vky, '_constant_pivot_values':
        _pivot_values, 'tracing': tracing}, hrbgo__eykz)
    impl = hrbgo__eykz['impl']
    return impl


@overload(pd.melt, inline='always', no_unliteral=True)
@overload_method(DataFrameType, 'melt', inline='always', no_unliteral=True)
def overload_dataframe_melt(frame, id_vars=None, value_vars=None, var_name=
    None, value_name='value', col_level=None, ignore_index=True):
    dvves__ibrvv = dict(col_level=col_level, ignore_index=ignore_index)
    nwky__ohw = dict(col_level=None, ignore_index=True)
    check_unsupported_args('DataFrame.melt', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    if not isinstance(frame, DataFrameType):
        raise BodoError("pandas.melt(): 'frame' argument must be a DataFrame.")
    if not is_overload_none(id_vars) and not is_literal_type(id_vars):
        raise_bodo_error(
            "DataFrame.melt(): 'id_vars', if specified, must be a literal.")
    if not is_overload_none(value_vars) and not is_literal_type(value_vars):
        raise_bodo_error(
            "DataFrame.melt(): 'value_vars', if specified, must be a literal.")
    if not is_overload_none(var_name) and not (is_literal_type(var_name) and
        (is_scalar_type(var_name) or isinstance(value_name, types.Omitted))):
        raise_bodo_error(
            "DataFrame.melt(): 'var_name', if specified, must be a literal.")
    if value_name != 'value' and not (is_literal_type(value_name) and (
        is_scalar_type(value_name) or isinstance(value_name, types.Omitted))):
        raise_bodo_error(
            "DataFrame.melt(): 'value_name', if specified, must be a literal.")
    var_name = get_literal_value(var_name) if not is_overload_none(var_name
        ) else 'variable'
    value_name = get_literal_value(value_name
        ) if value_name != 'value' else 'value'
    rkt__eik = get_literal_value(id_vars) if not is_overload_none(id_vars
        ) else []
    if not isinstance(rkt__eik, (list, tuple)):
        rkt__eik = [rkt__eik]
    for ahner__puklw in rkt__eik:
        if ahner__puklw not in frame.columns:
            raise BodoError(
                f"DataFrame.melt(): 'id_vars' column {ahner__puklw} not found in {frame}."
                )
    gmpvs__styo = [frame.column_index[i] for i in rkt__eik]
    if is_overload_none(value_vars):
        eqkfv__rkhoe = []
        crm__jes = []
        for i, ahner__puklw in enumerate(frame.columns):
            if i not in gmpvs__styo:
                eqkfv__rkhoe.append(i)
                crm__jes.append(ahner__puklw)
    else:
        crm__jes = get_literal_value(value_vars)
        if not isinstance(crm__jes, (list, tuple)):
            crm__jes = [crm__jes]
        crm__jes = [v for v in crm__jes if v not in rkt__eik]
        if not crm__jes:
            raise BodoError(
                "DataFrame.melt(): currently empty 'value_vars' is unsupported."
                )
        eqkfv__rkhoe = []
        for val in crm__jes:
            if val not in frame.column_index:
                raise BodoError(
                    f"DataFrame.melt(): 'value_vars' column {val} not found in DataFrame {frame}."
                    )
            eqkfv__rkhoe.append(frame.column_index[val])
    for ahner__puklw in crm__jes:
        if ahner__puklw not in frame.columns:
            raise BodoError(
                f"DataFrame.melt(): 'value_vars' column {ahner__puklw} not found in {frame}."
                )
    if not (all(isinstance(ahner__puklw, int) for ahner__puklw in crm__jes) or
        all(isinstance(ahner__puklw, str) for ahner__puklw in crm__jes)):
        raise BodoError(
            f"DataFrame.melt(): column names selected for 'value_vars' must all share a common int or string type. Please convert your names to a common type using DataFrame.rename()"
            )
    xsy__yhnr = frame.data[eqkfv__rkhoe[0]]
    dxjs__jvit = [frame.data[i].dtype for i in eqkfv__rkhoe]
    eqkfv__rkhoe = np.array(eqkfv__rkhoe, dtype=np.int64)
    gmpvs__styo = np.array(gmpvs__styo, dtype=np.int64)
    _, aszmt__kauj = bodo.utils.typing.get_common_scalar_dtype(dxjs__jvit)
    if not aszmt__kauj:
        raise BodoError(
            "DataFrame.melt(): columns selected in 'value_vars' must have a unifiable type."
            )
    extra_globals = {'np': np, 'value_lit': crm__jes, 'val_type': xsy__yhnr}
    header = 'def impl(\n'
    header += '  frame,\n'
    header += '  id_vars=None,\n'
    header += '  value_vars=None,\n'
    header += '  var_name=None,\n'
    header += "  value_name='value',\n"
    header += '  col_level=None,\n'
    header += '  ignore_index=True,\n'
    header += '):\n'
    header += (
        '  dummy_id = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(frame, 0)\n'
        )
    if frame.is_table_format and all(v == xsy__yhnr.dtype for v in dxjs__jvit):
        extra_globals['value_idxs'] = bodo.utils.typing.MetaType(tuple(
            eqkfv__rkhoe))
        header += (
            '  table = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(frame)\n'
            )
        header += (
            '  val_col = bodo.utils.table_utils.table_concat(table, value_idxs, val_type)\n'
            )
    elif len(crm__jes) == 1:
        header += f"""  val_col = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(frame, {eqkfv__rkhoe[0]})
"""
    else:
        lya__ddly = ', '.join(
            f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(frame, {i})'
             for i in eqkfv__rkhoe)
        header += (
            f'  val_col = bodo.libs.array_kernels.concat(({lya__ddly},))\n')
    header += """  var_col = bodo.libs.array_kernels.repeat_like(bodo.utils.conversion.coerce_to_array(value_lit), dummy_id)
"""
    for i in gmpvs__styo:
        header += (
            f'  id{i} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(frame, {i})\n'
            )
        header += (
            f'  out_id{i} = bodo.libs.array_kernels.concat([id{i}] * {len(crm__jes)})\n'
            )
    zgw__hcgax = ', '.join(f'out_id{i}' for i in gmpvs__styo) + (', ' if 
        len(gmpvs__styo) > 0 else '')
    data_args = zgw__hcgax + 'var_col, val_col'
    columns = tuple(rkt__eik + [var_name, value_name])
    index = (
        f'bodo.hiframes.pd_index_ext.init_range_index(0, len(frame) * {len(crm__jes)}, 1, None)'
        )
    return _gen_init_df(header, columns, data_args, index, extra_globals)


@overload(pd.crosstab, inline='always', no_unliteral=True)
def crosstab_overload(index, columns, values=None, rownames=None, colnames=
    None, aggfunc=None, margins=False, margins_name='All', dropna=True,
    normalize=False, _pivot_values=None):
    raise BodoError(f'pandas.crosstab() not supported yet')
    dvves__ibrvv = dict(values=values, rownames=rownames, colnames=colnames,
        aggfunc=aggfunc, margins=margins, margins_name=margins_name, dropna
        =dropna, normalize=normalize)
    nwky__ohw = dict(values=None, rownames=None, colnames=None, aggfunc=
        None, margins=False, margins_name='All', dropna=True, normalize=False)
    check_unsupported_args('pandas.crosstab', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(index,
        'pandas.crosstab()')
    if not isinstance(index, SeriesType):
        raise BodoError(
            f"pandas.crosstab(): 'index' argument only supported for Series types, found {index}"
            )
    if not isinstance(columns, SeriesType):
        raise BodoError(
            f"pandas.crosstab(): 'columns' argument only supported for Series types, found {columns}"
            )

    def _impl(index, columns, values=None, rownames=None, colnames=None,
        aggfunc=None, margins=False, margins_name='All', dropna=True,
        normalize=False, _pivot_values=None):
        return bodo.hiframes.pd_groupby_ext.crosstab_dummy(index, columns,
            _pivot_values)
    return _impl


@overload_method(DataFrameType, 'sort_values', inline='always',
    no_unliteral=True)
def overload_dataframe_sort_values(df, by, axis=0, ascending=True, inplace=
    False, kind='quicksort', na_position='last', ignore_index=False, key=
    None, _bodo_chunk_bounds=None, _bodo_transformed=False):
    check_runtime_cols_unsupported(df, 'DataFrame.sort_values()')
    dvves__ibrvv = dict(ignore_index=ignore_index, key=key)
    nwky__ohw = dict(ignore_index=False, key=None)
    check_unsupported_args('DataFrame.sort_values', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    handle_inplace_df_type_change(inplace, _bodo_transformed, 'sort_values')
    validate_sort_values_spec(df, by, axis, ascending, inplace, kind,
        na_position, _bodo_chunk_bounds)

    def _impl(df, by, axis=0, ascending=True, inplace=False, kind=
        'quicksort', na_position='last', ignore_index=False, key=None,
        _bodo_chunk_bounds=None, _bodo_transformed=False):
        return bodo.hiframes.pd_dataframe_ext.sort_values_dummy(df, by,
            ascending, inplace, na_position, _bodo_chunk_bounds)
    return _impl


def validate_sort_values_spec(df, by, axis, ascending, inplace, kind,
    na_position, _bodo_chunk_bounds):
    if is_overload_none(by) or not is_literal_type(by
        ) and not is_overload_constant_list(by):
        raise_bodo_error(
            "sort_values(): 'by' parameter only supports a constant column label or column labels. by={}"
            .format(by))
    osdm__fwguy = set(df.columns)
    if is_overload_constant_str(df.index.name_typ):
        osdm__fwguy.add(get_overload_const_str(df.index.name_typ))
    if is_overload_constant_tuple(by):
        aps__mdgc = [get_overload_const_tuple(by)]
    else:
        aps__mdgc = get_overload_const_list(by)
    aps__mdgc = set((k, '') if (k, '') in osdm__fwguy else k for k in aps__mdgc
        )
    if len(aps__mdgc.difference(osdm__fwguy)) > 0:
        yggk__blo = list(set(get_overload_const_list(by)).difference(
            osdm__fwguy))
        raise_bodo_error(f'sort_values(): invalid keys {yggk__blo} for by.')
    if not is_overload_none(_bodo_chunk_bounds) and len(aps__mdgc) != 1:
        raise_bodo_error(
            f'sort_values(): _bodo_chunk_bounds only supported when there is a single key.'
            )
    if not is_overload_zero(axis):
        raise_bodo_error(
            "sort_values(): 'axis' parameter only supports integer value 0.")
    if not is_overload_bool(ascending) and not is_overload_bool_list(ascending
        ):
        raise_bodo_error(
            "sort_values(): 'ascending' parameter must be of type bool or list of bool, not {}."
            .format(ascending))
    if not is_overload_bool(inplace):
        raise_bodo_error(
            "sort_values(): 'inplace' parameter must be of type bool, not {}."
            .format(inplace))
    if kind != 'quicksort' and not isinstance(kind, types.Omitted):
        warnings.warn(BodoWarning(
            'sort_values(): specifying sorting algorithm is not supported in Bodo. Bodo uses stable sort.'
            ))
    if is_overload_constant_str(na_position):
        na_position = get_overload_const_str(na_position)
        if na_position not in ('first', 'last'):
            raise BodoError(
                "sort_values(): na_position should either be 'first' or 'last'"
                )
    elif is_overload_constant_list(na_position):
        ghus__tkcto = get_overload_const_list(na_position)
        for na_position in ghus__tkcto:
            if na_position not in ('first', 'last'):
                raise BodoError(
                    "sort_values(): Every value in na_position should either be 'first' or 'last'"
                    )
    else:
        raise_bodo_error(
            f'sort_values(): na_position parameter must be a literal constant of type str or a constant list of str with 1 entry per key column, not {na_position}'
            )
    na_position = get_overload_const_str(na_position)
    if na_position not in ['first', 'last']:
        raise BodoError(
            "sort_values(): na_position should either be 'first' or 'last'")


@overload_method(DataFrameType, 'sort_index', inline='always', no_unliteral
    =True)
def overload_dataframe_sort_index(df, axis=0, level=None, ascending=True,
    inplace=False, kind='quicksort', na_position='last', sort_remaining=
    True, ignore_index=False, key=None):
    check_runtime_cols_unsupported(df, 'DataFrame.sort_index()')
    dvves__ibrvv = dict(axis=axis, level=level, kind=kind, sort_remaining=
        sort_remaining, ignore_index=ignore_index, key=key)
    nwky__ohw = dict(axis=0, level=None, kind='quicksort', sort_remaining=
        True, ignore_index=False, key=None)
    check_unsupported_args('DataFrame.sort_index', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    if not is_overload_bool(ascending):
        raise BodoError(
            "DataFrame.sort_index(): 'ascending' parameter must be of type bool"
            )
    if not is_overload_bool(inplace):
        raise BodoError(
            "DataFrame.sort_index(): 'inplace' parameter must be of type bool")
    if not is_overload_constant_str(na_position) or get_overload_const_str(
        na_position) not in ('first', 'last'):
        raise_bodo_error(
            "DataFrame.sort_index(): 'na_position' should either be 'first' or 'last'"
            )

    def _impl(df, axis=0, level=None, ascending=True, inplace=False, kind=
        'quicksort', na_position='last', sort_remaining=True, ignore_index=
        False, key=None):
        return bodo.hiframes.pd_dataframe_ext.sort_values_dummy(df,
            '$_bodo_index_', ascending, inplace, na_position, None)
    return _impl


@overload_method(DataFrameType, 'rank', inline='always', no_unliteral=True)
def overload_dataframe_rank(df, axis=0, method='average', numeric_only=None,
    na_option='keep', ascending=True, pct=False):
    xood__fcig = """def impl(df, axis=0, method='average', numeric_only=None, na_option='keep', ascending=True, pct=False):
"""
    iryek__rfuyn = len(df.columns)
    data_args = ', '.join(
        'bodo.libs.array_kernels.rank(data_{}, method=method, na_option=na_option, ascending=ascending, pct=pct)'
        .format(i) for i in range(iryek__rfuyn))
    for i in range(iryek__rfuyn):
        xood__fcig += (
            '  data_{0} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {0})\n'
            .format(i))
    index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)'
    return _gen_init_df(xood__fcig, df.columns, data_args, index)


@overload_method(DataFrameType, 'fillna', inline='always', no_unliteral=True)
def overload_dataframe_fillna(df, value=None, method=None, axis=None,
    inplace=False, limit=None, downcast=None):
    check_runtime_cols_unsupported(df, 'DataFrame.fillna()')
    dvves__ibrvv = dict(limit=limit, downcast=downcast)
    nwky__ohw = dict(limit=None, downcast=None)
    check_unsupported_args('DataFrame.fillna', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.fillna()')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise BodoError("DataFrame.fillna(): 'axis' argument not supported.")
    aow__agjo = not is_overload_none(value)
    jxklt__ebzsb = not is_overload_none(method)
    if aow__agjo and jxklt__ebzsb:
        raise BodoError(
            "DataFrame.fillna(): Cannot specify both 'value' and 'method'.")
    if not aow__agjo and not jxklt__ebzsb:
        raise BodoError(
            "DataFrame.fillna(): Must specify one of 'value' and 'method'.")
    if aow__agjo:
        vwi__ntm = 'value=value'
    else:
        vwi__ntm = 'method=method'
    data_args = [(
        f"df['{ahner__puklw}'].fillna({vwi__ntm}, inplace=inplace)" if
        isinstance(ahner__puklw, str) else
        f'df[{ahner__puklw}].fillna({vwi__ntm}, inplace=inplace)') for
        ahner__puklw in df.columns]
    xood__fcig = """def impl(df, value=None, method=None, axis=None, inplace=False, limit=None, downcast=None):
"""
    if is_overload_true(inplace):
        xood__fcig += '  ' + '  \n'.join(data_args) + '\n'
        hrbgo__eykz = {}
        exec(xood__fcig, {}, hrbgo__eykz)
        impl = hrbgo__eykz['impl']
        return impl
    else:
        return _gen_init_df(xood__fcig, df.columns, ', '.join(tmy__jocol +
            '.values' for tmy__jocol in data_args))


@overload_method(DataFrameType, 'reset_index', inline='always',
    no_unliteral=True)
def overload_dataframe_reset_index(df, level=None, drop=False, inplace=
    False, col_level=0, col_fill='', _bodo_transformed=False):
    check_runtime_cols_unsupported(df, 'DataFrame.reset_index()')
    dvves__ibrvv = dict(col_level=col_level, col_fill=col_fill)
    nwky__ohw = dict(col_level=0, col_fill='')
    check_unsupported_args('DataFrame.reset_index', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    handle_inplace_df_type_change(inplace, _bodo_transformed, 'reset_index')
    if not _is_all_levels(df, level):
        raise_bodo_error(
            'DataFrame.reset_index(): only dropping all index levels supported'
            )
    if not is_overload_constant_bool(drop):
        raise BodoError(
            "DataFrame.reset_index(): 'drop' parameter should be a constant boolean value"
            )
    if not is_overload_constant_bool(inplace):
        raise BodoError(
            "DataFrame.reset_index(): 'inplace' parameter should be a constant boolean value"
            )
    xood__fcig = """def impl(df, level=None, drop=False, inplace=False, col_level=0, col_fill='', _bodo_transformed=False,):
"""
    xood__fcig += (
        '  index = bodo.hiframes.pd_index_ext.init_range_index(0, len(df), 1, None)\n'
        )
    drop = is_overload_true(drop)
    inplace = is_overload_true(inplace)
    columns = df.columns
    data_args = [
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {}){}\n'.
        format(i, '' if inplace else '.copy()') for i in range(len(df.columns))
        ]
    if not drop:
        adzrp__rjqjx = 'index' if 'index' not in columns else 'level_0'
        index_names = get_index_names(df.index, 'DataFrame.reset_index()',
            adzrp__rjqjx)
        columns = index_names + columns
        if isinstance(df.index, MultiIndexType):
            xood__fcig += """  m_index = bodo.hiframes.pd_index_ext.get_index_data(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df))
"""
            khd__ykx = ['m_index[{}]'.format(i) for i in range(df.index.
                nlevels)]
            data_args = khd__ykx + data_args
        else:
            jvt__vdaki = (
                'bodo.utils.conversion.index_to_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df))'
                )
            data_args = [jvt__vdaki] + data_args
    return _gen_init_df(xood__fcig, columns, ', '.join(data_args), 'index')


def _is_all_levels(df, level):
    fkihz__tau = len(get_index_data_arr_types(df.index))
    return is_overload_none(level) or is_overload_constant_int(level
        ) and get_overload_const_int(level
        ) == 0 and fkihz__tau == 1 or is_overload_constant_list(level
        ) and list(get_overload_const_list(level)) == list(range(fkihz__tau))


@overload_method(DataFrameType, 'dropna', inline='always', no_unliteral=True)
def overload_dataframe_dropna(df, axis=0, how='any', thresh=None, subset=
    None, inplace=False):
    check_runtime_cols_unsupported(df, 'DataFrame.dropna()')
    if not is_overload_constant_bool(inplace) or is_overload_true(inplace):
        raise BodoError('DataFrame.dropna(): inplace=True is not supported')
    if not is_overload_zero(axis):
        raise_bodo_error(f'df.dropna(): only axis=0 supported')
    ensure_constant_values('dropna', 'how', how, ('any', 'all'))
    if is_overload_none(subset):
        tgzn__jlzs = list(range(len(df.columns)))
    elif not is_overload_constant_list(subset):
        raise_bodo_error(
            f'df.dropna(): subset argument should a constant list, not {subset}'
            )
    else:
        nlpng__alf = get_overload_const_list(subset)
        tgzn__jlzs = []
        for plmux__cnp in nlpng__alf:
            if plmux__cnp not in df.column_index:
                raise_bodo_error(
                    f"df.dropna(): column '{plmux__cnp}' not in data frame columns {df}"
                    )
            tgzn__jlzs.append(df.column_index[plmux__cnp])
    iryek__rfuyn = len(df.columns)
    data_args = ', '.join('data_{}'.format(i) for i in range(iryek__rfuyn))
    xood__fcig = (
        "def impl(df, axis=0, how='any', thresh=None, subset=None, inplace=False):\n"
        )
    for i in range(iryek__rfuyn):
        xood__fcig += (
            '  data_{0} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {0})\n'
            .format(i))
    index = (
        'bodo.utils.conversion.index_to_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df))'
        )
    xood__fcig += (
        """  ({0}, index_arr) = bodo.libs.array_kernels.dropna(({0}, {1}), how, thresh, ({2},))
"""
        .format(data_args, index, ', '.join(str(a) for a in tgzn__jlzs)))
    xood__fcig += (
        '  index = bodo.utils.conversion.index_from_array(index_arr)\n')
    return _gen_init_df(xood__fcig, df.columns, data_args, 'index')


@overload_method(DataFrameType, 'drop', inline='always', no_unliteral=True)
def overload_dataframe_drop(df, labels=None, axis=0, index=None, columns=
    None, level=None, inplace=False, errors='raise', _bodo_transformed=False):
    check_runtime_cols_unsupported(df, 'DataFrame.drop()')
    dvves__ibrvv = dict(index=index, level=level, errors=errors)
    nwky__ohw = dict(index=None, level=None, errors='raise')
    check_unsupported_args('DataFrame.drop', dvves__ibrvv, nwky__ohw,
        package_name='pandas', module_name='DataFrame')
    handle_inplace_df_type_change(inplace, _bodo_transformed, 'drop')
    if not is_overload_constant_bool(inplace):
        raise_bodo_error(
            "DataFrame.drop(): 'inplace' parameter should be a constant bool")
    if not is_overload_none(labels):
        if not is_overload_none(columns):
            raise BodoError(
                "Dataframe.drop(): Cannot specify both 'labels' and 'columns'")
        if not is_overload_constant_int(axis) or get_overload_const_int(axis
            ) != 1:
            raise_bodo_error('DataFrame.drop(): only axis=1 supported')
        if is_overload_constant_str(labels):
            iur__aekqw = get_overload_const_str(labels),
        elif is_overload_constant_list(labels):
            iur__aekqw = get_overload_const_list(labels)
        else:
            raise_bodo_error(
                'constant list of columns expected for labels in DataFrame.drop()'
                )
    else:
        if is_overload_none(columns):
            raise BodoError(
                "DataFrame.drop(): Need to specify at least one of 'labels' or 'columns'"
                )
        if is_overload_constant_str(columns):
            iur__aekqw = get_overload_const_str(columns),
        elif is_overload_constant_list(columns):
            iur__aekqw = get_overload_const_list(columns)
        else:
            raise_bodo_error(
                'constant list of columns expected for labels in DataFrame.drop()'
                )
    for ahner__puklw in iur__aekqw:
        if ahner__puklw not in df.columns:
            raise_bodo_error(
                'DataFrame.drop(): column {} not in DataFrame columns {}'.
                format(ahner__puklw, df.columns))
    if len(set(iur__aekqw)) == len(df.columns):
        raise BodoError('DataFrame.drop(): Dropping all columns not supported.'
            )
    inplace = is_overload_true(inplace)
    voidi__jeofb = tuple(ahner__puklw for ahner__puklw in df.columns if 
        ahner__puklw not in iur__aekqw)
    data_args = ', '.join(
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {}){}'.
        format(df.column_index[ahner__puklw], '.copy()' if not inplace else
        '') for ahner__puklw in voidi__jeofb)
    xood__fcig = (
        'def impl(df, labels=None, axis=0, index=None, columns=None,\n')
    xood__fcig += (
        "     level=None, inplace=False, errors='raise', _bodo_transformed=False):\n"
        )
    index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)'
    return _gen_init_df(xood__fcig, voidi__jeofb, data_args, index)


@overload_method(DataFrameType, 'append', inline='always', no_unliteral=True)
def overload_dataframe_append(df, other, ignore_index=False,
    verify_integrity=False, sort=None):
    check_runtime_cols_unsupported(df, 'DataFrame.append()')
    check_runtime_cols_unsupported(other, 'DataFrame.append()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.append()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(other,
        'DataFrame.append()')
    if isinstance(other, DataFrameType):
        return (lambda df, other, ignore_index=False, verify_integrity=
            False, sort=None: pd.concat((df, other), ignore_index=
            ignore_index, verify_integrity=verify_integrity))
    if isinstance(other, types.BaseTuple):
        return (lambda df, other, ignore_index=False, verify_integrity=
            False, sort=None: pd.concat((df,) + other, ignore_index=
            ignore_index, verify_integrity=verify_integrity))
    if isinstance(other, types.List) and isinstance(other.dtype, DataFrameType
        ):
        return (lambda df, other, ignore_index=False, verify_integrity=
            False, sort=None: pd.concat([df] + other, ignore_index=
            ignore_index, verify_integrity=verify_integrity))
    raise BodoError(
        'invalid df.append() input. Only dataframe and list/tuple of dataframes supported'
        )


@overload_method(DataFrameType, 'sample', inline='always', no_unliteral=True)
def overload_dataframe_sample(df, n=None, frac=None, replace=False, weights
    =None, random_state=None, axis=None, ignore_index=False):
    check_runtime_cols_unsupported(df, 'DataFrame.sample()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.sample()')
    dvves__ibrvv = dict(random_state=random_state, weights=weights, axis=
        axis, ignore_index=ignore_index)
    jlwy__xof = dict(random_state=None, weights=None, axis=None,
        ignore_index=False)
    check_unsupported_args('DataFrame.sample', dvves__ibrvv, jlwy__xof,
        package_name='pandas', module_name='DataFrame')
    if not is_overload_none(n) and not is_overload_none(frac):
        raise BodoError(
            'DataFrame.sample(): only one of n and frac option can be selected'
            )
    iryek__rfuyn = len(df.columns)
    data_args = ', '.join('data_{}'.format(i) for i in range(iryek__rfuyn))
    iij__nuz = ', '.join('rhs_data_{}'.format(i) for i in range(iryek__rfuyn))
    xood__fcig = """def impl(df, n=None, frac=None, replace=False, weights=None, random_state=None, axis=None, ignore_index=False):
"""
    xood__fcig += '  if (frac == 1 or n == len(df)) and not replace:\n'
    xood__fcig += (
        '    return bodo.allgatherv(bodo.random_shuffle(df), False)\n')
    for i in range(iryek__rfuyn):
        xood__fcig += (
            """  rhs_data_{0} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {0})
"""
            .format(i))
    xood__fcig += '  if frac is None:\n'
    xood__fcig += '    frac_d = -1.0\n'
    xood__fcig += '  else:\n'
    xood__fcig += '    frac_d = frac\n'
    xood__fcig += '  if n is None:\n'
    xood__fcig += '    n_i = 0\n'
    xood__fcig += '  else:\n'
    xood__fcig += '    n_i = n\n'
    index = (
        'bodo.utils.conversion.index_to_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df))'
        )
    xood__fcig += f"""  ({data_args},), index_arr = bodo.libs.array_kernels.sample_table_operation(({iij__nuz},), {index}, n_i, frac_d, replace)
"""
    xood__fcig += (
        '  index = bodo.utils.conversion.index_from_array(index_arr)\n')
    return bodo.hiframes.dataframe_impl._gen_init_df(xood__fcig, df.columns,
        data_args, 'index')


@numba.njit
def _sizeof_fmt(num, size_qualifier=''):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return f'{num:3.1f}{size_qualifier} {x}'
        num /= 1024.0
    return f'{num:3.1f}{size_qualifier} PB'


@overload_method(DataFrameType, 'info', no_unliteral=True)
def overload_dataframe_info(df, verbose=None, buf=None, max_cols=None,
    memory_usage=None, show_counts=None, null_counts=None):
    check_runtime_cols_unsupported(df, 'DataFrame.info()')
    hsn__bxq = {'verbose': verbose, 'buf': buf, 'max_cols': max_cols,
        'memory_usage': memory_usage, 'show_counts': show_counts,
        'null_counts': null_counts}
    mawl__wldaq = {'verbose': None, 'buf': None, 'max_cols': None,
        'memory_usage': None, 'show_counts': None, 'null_counts': None}
    check_unsupported_args('DataFrame.info', hsn__bxq, mawl__wldaq,
        package_name='pandas', module_name='DataFrame')
    avjd__yrug = f"<class '{str(type(df)).split('.')[-1]}"
    if len(df.columns) == 0:

        def _info_impl(df, verbose=None, buf=None, max_cols=None,
            memory_usage=None, show_counts=None, null_counts=None):
            kyykp__vrbim = avjd__yrug + '\n'
            kyykp__vrbim += 'Index: 0 entries\n'
            kyykp__vrbim += 'Empty DataFrame'
            print(kyykp__vrbim)
        return _info_impl
    else:
        xood__fcig = """def _info_impl(df, verbose=None, buf=None, max_cols=None, memory_usage=None, show_counts=None, null_counts=None): #pragma: no cover
"""
        xood__fcig += '    ncols = df.shape[1]\n'
        xood__fcig += f'    lines = "{avjd__yrug}\\n"\n'
        xood__fcig += f'    lines += "{df.index}: "\n'
        xood__fcig += (
            '    index = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)\n'
            )
        if isinstance(df.index, bodo.hiframes.pd_index_ext.RangeIndexType):
            xood__fcig += """    lines += f"{len(index)} entries, {index.start} to {index.stop-1}\\n\"
"""
        elif isinstance(df.index, bodo.hiframes.pd_index_ext.StringIndexType):
            xood__fcig += """    lines += f"{len(index)} entries, {index[0]} to {index[len(index)-1]}\\n\"
"""
        else:
            xood__fcig += (
                '    lines += f"{len(index)} entries, {index[0]} to {index[-1]}\\n"\n'
                )
        xood__fcig += (
            '    lines += f"Data columns (total {ncols} columns):\\n"\n')
        xood__fcig += (
            f'    space = {max(len(str(k)) for k in df.columns) + 1}\n')
        xood__fcig += '    column_width = max(space, 7)\n'
        xood__fcig += '    column= "Column"\n'
        xood__fcig += '    underl= "------"\n'
        xood__fcig += (
            '    lines += f"#   {column:<{column_width}} Non-Null Count  Dtype\\n"\n'
            )
        xood__fcig += (
            '    lines += f"--- {underl:<{column_width}} --------------  -----\\n"\n'
            )
        xood__fcig += '    mem_size = 0\n'
        xood__fcig += (
            '    col_name = bodo.libs.str_arr_ext.pre_alloc_string_array(ncols, -1)\n'
            )
        xood__fcig += """    non_null_count = bodo.libs.str_arr_ext.pre_alloc_string_array(ncols, -1)
"""
        xood__fcig += (
            '    col_dtype = bodo.libs.str_arr_ext.pre_alloc_string_array(ncols, -1)\n'
            )
        gdyuu__akea = dict()
        for i in range(len(df.columns)):
            xood__fcig += f"""    non_null_count[{i}] = str(bodo.libs.array_ops.array_op_count(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})))
"""
            bungw__jqrr = f'{df.data[i].dtype}'
            if isinstance(df.data[i], bodo.CategoricalArrayType):
                bungw__jqrr = 'category'
            elif isinstance(df.data[i], bodo.IntegerArrayType):
                bxl__isxgn = bodo.libs.int_arr_ext.IntDtype(df.data[i].dtype
                    ).name
                bungw__jqrr = f'{bxl__isxgn[:-7]}'
            xood__fcig += f'    col_dtype[{i}] = "{bungw__jqrr}"\n'
            if bungw__jqrr in gdyuu__akea:
                gdyuu__akea[bungw__jqrr] += 1
            else:
                gdyuu__akea[bungw__jqrr] = 1
            xood__fcig += f'    col_name[{i}] = "{df.columns[i]}"\n'
            xood__fcig += f"""    mem_size += bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}).nbytes
"""
        xood__fcig += """    column_info = [f'{i:^3} {name:<{column_width}} {count} non-null      {dtype}' for i, (name, count, dtype) in enumerate(zip(col_name, non_null_count, col_dtype))]
"""
        xood__fcig += '    for i in column_info:\n'
        xood__fcig += "        lines += f'{i}\\n'\n"
        clqpy__tzbqq = ', '.join(f'{k}({gdyuu__akea[k]})' for k in sorted(
            gdyuu__akea))
        xood__fcig += f"    lines += 'dtypes: {clqpy__tzbqq}\\n'\n"
        xood__fcig += '    mem_size += df.index.nbytes\n'
        xood__fcig += '    total_size = _sizeof_fmt(mem_size)\n'
        xood__fcig += "    lines += f'memory usage: {total_size}'\n"
        xood__fcig += '    print(lines)\n'
        hrbgo__eykz = {}
        exec(xood__fcig, {'_sizeof_fmt': _sizeof_fmt, 'pd': pd, 'bodo':
            bodo, 'np': np}, hrbgo__eykz)
        _info_impl = hrbgo__eykz['_info_impl']
        return _info_impl


@overload_method(DataFrameType, 'memory_usage', inline='always',
    no_unliteral=True)
def overload_dataframe_memory_usage(df, index=True, deep=False):
    check_runtime_cols_unsupported(df, 'DataFrame.memory_usage()')
    xood__fcig = 'def impl(df, index=True, deep=False):\n'
    qphtx__rlq = (
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df).nbytes')
    piuq__wnj = is_overload_true(index)
    columns = df.columns
    if piuq__wnj:
        columns = ('Index',) + columns
    if len(columns) == 0:
        ubbnp__ionb = ()
    elif all(isinstance(ahner__puklw, int) for ahner__puklw in columns):
        ubbnp__ionb = np.array(columns, 'int64')
    elif all(isinstance(ahner__puklw, str) for ahner__puklw in columns):
        ubbnp__ionb = pd.array(columns, 'string')
    else:
        ubbnp__ionb = columns
    if df.is_table_format and len(df.columns) > 0:
        cje__ifhh = int(piuq__wnj)
        gcda__yenmt = len(columns)
        xood__fcig += f'  nbytes_arr = np.empty({gcda__yenmt}, np.int64)\n'
        xood__fcig += (
            '  table = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)\n'
            )
        xood__fcig += f"""  bodo.utils.table_utils.generate_table_nbytes(table, nbytes_arr, {cje__ifhh})
"""
        if piuq__wnj:
            xood__fcig += f'  nbytes_arr[0] = {qphtx__rlq}\n'
        xood__fcig += f"""  return bodo.hiframes.pd_series_ext.init_series(nbytes_arr, pd.Index(column_vals), None)
"""
    else:
        data = ', '.join(
            f'bodo.libs.array_ops.array_op_nbytes(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}))'
             for i in range(len(df.columns)))
        if piuq__wnj:
            data = f'{qphtx__rlq},{data}'
        else:
            csm__pusld = ',' if len(columns) == 1 else ''
            data = f'{data}{csm__pusld}'
        xood__fcig += f"""  return bodo.hiframes.pd_series_ext.init_series(({data}), pd.Index(column_vals), None)
"""
    hrbgo__eykz = {}
    exec(xood__fcig, {'bodo': bodo, 'np': np, 'pd': pd, 'column_vals':
        ubbnp__ionb}, hrbgo__eykz)
    impl = hrbgo__eykz['impl']
    return impl


@overload(pd.read_excel, no_unliteral=True)
def overload_read_excel(io, sheet_name=0, header=0, names=None, index_col=
    None, usecols=None, squeeze=False, dtype=None, engine=None, converters=
    None, true_values=None, false_values=None, skiprows=None, nrows=None,
    na_values=None, keep_default_na=True, na_filter=True, verbose=False,
    parse_dates=False, date_parser=None, thousands=None, comment=None,
    skipfooter=0, convert_float=True, mangle_dupe_cols=True, _bodo_df_type=None
    ):
    df_type = _bodo_df_type.instance_type
    uaa__lysq = 'read_excel_df{}'.format(next_label())
    setattr(types, uaa__lysq, df_type)
    zcdu__vaxzq = False
    if is_overload_constant_list(parse_dates):
        zcdu__vaxzq = get_overload_const_list(parse_dates)
    pgc__hnmac = ', '.join(["'{}':{}".format(cname, _get_pd_dtype_str(t)) for
        cname, t in zip(df_type.columns, df_type.data)])
    xood__fcig = f"""
def impl(
    io,
    sheet_name=0,
    header=0,
    names=None,
    index_col=None,
    usecols=None,
    squeeze=False,
    dtype=None,
    engine=None,
    converters=None,
    true_values=None,
    false_values=None,
    skiprows=None,
    nrows=None,
    na_values=None,
    keep_default_na=True,
    na_filter=True,
    verbose=False,
    parse_dates=False,
    date_parser=None,
    thousands=None,
    comment=None,
    skipfooter=0,
    convert_float=True,
    mangle_dupe_cols=True,
    _bodo_df_type=None,
):
    with numba.objmode(df="{uaa__lysq}"):
        df = pd.read_excel(
            io=io,
            sheet_name=sheet_name,
            header=header,
            names={list(df_type.columns)},
            index_col=index_col,
            usecols=usecols,
            squeeze=squeeze,
            dtype={{{pgc__hnmac}}},
            engine=engine,
            converters=converters,
            true_values=true_values,
            false_values=false_values,
            skiprows=skiprows,
            nrows=nrows,
            na_values=na_values,
            keep_default_na=keep_default_na,
            na_filter=na_filter,
            verbose=verbose,
            parse_dates={zcdu__vaxzq},
            date_parser=date_parser,
            thousands=thousands,
            comment=comment,
            skipfooter=skipfooter,
            convert_float=convert_float,
            mangle_dupe_cols=mangle_dupe_cols,
        )
    return df
"""
    hrbgo__eykz = {}
    exec(xood__fcig, globals(), hrbgo__eykz)
    impl = hrbgo__eykz['impl']
    return impl


def overload_dataframe_plot(df, x=None, y=None, kind='line', figsize=None,
    xlabel=None, ylabel=None, title=None, legend=True, fontsize=None,
    xticks=None, yticks=None, ax=None):
    try:
        import matplotlib.pyplot as plt
    except ImportError as xstvf__tlntg:
        raise BodoError('df.plot needs matplotllib which is not installed.')
    xood__fcig = (
        "def impl(df, x=None, y=None, kind='line', figsize=None, xlabel=None, \n"
        )
    xood__fcig += '    ylabel=None, title=None, legend=True, fontsize=None, \n'
    xood__fcig += '    xticks=None, yticks=None, ax=None):\n'
    if is_overload_none(ax):
        xood__fcig += '   fig, ax = plt.subplots()\n'
    else:
        xood__fcig += '   fig = ax.get_figure()\n'
    if not is_overload_none(figsize):
        xood__fcig += '   fig.set_figwidth(figsize[0])\n'
        xood__fcig += '   fig.set_figheight(figsize[1])\n'
    if is_overload_none(xlabel):
        xood__fcig += '   xlabel = x\n'
    xood__fcig += '   ax.set_xlabel(xlabel)\n'
    if is_overload_none(ylabel):
        xood__fcig += '   ylabel = y\n'
    else:
        xood__fcig += '   ax.set_ylabel(ylabel)\n'
    if not is_overload_none(title):
        xood__fcig += '   ax.set_title(title)\n'
    if not is_overload_none(fontsize):
        xood__fcig += '   ax.tick_params(labelsize=fontsize)\n'
    kind = get_overload_const_str(kind)
    if kind == 'line':
        if is_overload_none(x) and is_overload_none(y):
            for i in range(len(df.columns)):
                if isinstance(df.data[i], (types.Array, IntegerArrayType)
                    ) and isinstance(df.data[i].dtype, (types.Integer,
                    types.Float)):
                    xood__fcig += (
                        f'   ax.plot(df.iloc[:, {i}], label=df.columns[{i}])\n'
                        )
        elif is_overload_none(x):
            xood__fcig += '   ax.plot(df[y], label=y)\n'
        elif is_overload_none(y):
            vmpgs__wwhhu = get_overload_const_str(x)
            pmp__uddon = df.columns.index(vmpgs__wwhhu)
            for i in range(len(df.columns)):
                if isinstance(df.data[i], (types.Array, IntegerArrayType)
                    ) and isinstance(df.data[i].dtype, (types.Integer,
                    types.Float)):
                    if pmp__uddon != i:
                        xood__fcig += (
                            f'   ax.plot(df[x], df.iloc[:, {i}], label=df.columns[{i}])\n'
                            )
        else:
            xood__fcig += '   ax.plot(df[x], df[y], label=y)\n'
    elif kind == 'scatter':
        legend = False
        xood__fcig += '   ax.scatter(df[x], df[y], s=20)\n'
        xood__fcig += '   ax.set_ylabel(ylabel)\n'
    if not is_overload_none(xticks):
        xood__fcig += '   ax.set_xticks(xticks)\n'
    if not is_overload_none(yticks):
        xood__fcig += '   ax.set_yticks(yticks)\n'
    if is_overload_true(legend):
        xood__fcig += '   ax.legend()\n'
    xood__fcig += '   return ax\n'
    hrbgo__eykz = {}
    exec(xood__fcig, {'bodo': bodo, 'plt': plt}, hrbgo__eykz)
    impl = hrbgo__eykz['impl']
    return impl


@lower_builtin('df.plot', DataFrameType, types.VarArg(types.Any))
def dataframe_plot_low(context, builder, sig, args):
    impl = overload_dataframe_plot(*sig.args)
    return context.compile_internal(builder, impl, sig, args)


def is_df_values_numpy_supported_dftyp(df_typ):
    for ajuak__ewej in df_typ.data:
        if not (isinstance(ajuak__ewej, (IntegerArrayType,
            FloatingArrayType)) or isinstance(ajuak__ewej.dtype, types.
            Number) or ajuak__ewej.dtype in (bodo.datetime64ns, bodo.
            timedelta64ns)):
            return False
    return True


def typeref_to_type(v):
    if isinstance(v, types.BaseTuple):
        return types.BaseTuple.from_types(tuple(typeref_to_type(a) for a in v))
    return v.instance_type if isinstance(v, (types.TypeRef, types.NumberClass)
        ) else v


def _install_typer_for_type(type_name, typ):

    @type_callable(typ)
    def type_call_type(context):

        def typer(*args, **kws):
            args = tuple(typeref_to_type(v) for v in args)
            kws = {name: typeref_to_type(v) for name, v in kws.items()}
            return types.TypeRef(typ(*args, **kws))
        return typer
    no_side_effect_call_tuples.add((type_name, bodo))
    no_side_effect_call_tuples.add((typ,))


def _install_type_call_typers():
    for type_name in bodo_types_with_params:
        typ = getattr(bodo, type_name)
        _install_typer_for_type(type_name, typ)


_install_type_call_typers()


def set_df_col(df, cname, arr, inplace):
    df[cname] = arr


@infer_global(set_df_col)
class SetDfColInfer(AbstractTemplate):

    def generic(self, args, kws):
        from bodo.hiframes.pd_dataframe_ext import DataFrameType
        assert not kws
        assert len(args) == 4
        assert isinstance(args[1], types.Literal)
        qbqyb__pgbt = args[0]
        lpjds__vgfms = args[1].literal_value
        val = args[2]
        assert val != types.unknown
        fej__zvypv = qbqyb__pgbt
        check_runtime_cols_unsupported(qbqyb__pgbt, 'set_df_col()')
        if isinstance(qbqyb__pgbt, DataFrameType):
            index = qbqyb__pgbt.index
            if len(qbqyb__pgbt.columns) == 0:
                index = bodo.hiframes.pd_index_ext.RangeIndexType(types.none)
            if isinstance(val, SeriesType):
                if len(qbqyb__pgbt.columns) == 0:
                    index = val.index
                val = val.data
            if is_pd_index_type(val):
                val = bodo.utils.typing.get_index_data_arr_types(val)[0]
            if isinstance(val, types.List):
                val = dtype_to_array_type(val.dtype)
            if is_overload_constant_str(val) or val == types.unicode_type:
                val = bodo.dict_str_arr_type
            elif not is_array_typ(val):
                val = dtype_to_array_type(val)
            if lpjds__vgfms in qbqyb__pgbt.columns:
                voidi__jeofb = qbqyb__pgbt.columns
                gcz__yuz = qbqyb__pgbt.columns.index(lpjds__vgfms)
                djcbm__mxhsv = list(qbqyb__pgbt.data)
                djcbm__mxhsv[gcz__yuz] = val
                djcbm__mxhsv = tuple(djcbm__mxhsv)
            else:
                voidi__jeofb = qbqyb__pgbt.columns + (lpjds__vgfms,)
                djcbm__mxhsv = qbqyb__pgbt.data + (val,)
            fej__zvypv = DataFrameType(djcbm__mxhsv, index, voidi__jeofb,
                qbqyb__pgbt.dist, qbqyb__pgbt.is_table_format)
        return fej__zvypv(*args)


SetDfColInfer.prefer_literal = True


def __bodosql_replace_columns_dummy(df, col_names_to_replace,
    cols_to_replace_with):
    for i in range(len(col_names_to_replace)):
        df[col_names_to_replace[i]] = cols_to_replace_with[i]


@infer_global(__bodosql_replace_columns_dummy)
class BodoSQLReplaceColsInfer(AbstractTemplate):

    def generic(self, args, kws):
        from bodo.hiframes.pd_dataframe_ext import DataFrameType
        assert not kws
        assert len(args) == 3
        assert is_overload_constant_tuple(args[1])
        assert isinstance(args[2], types.BaseTuple)
        fsd__dbfkp = args[0]
        assert isinstance(fsd__dbfkp, DataFrameType) and len(fsd__dbfkp.columns
            ) > 0, 'Error while typechecking __bodosql_replace_columns_dummy: we should only generate a call __bodosql_replace_columns_dummy if the input dataframe'
        col_names_to_replace = get_overload_const_tuple(args[1])
        zdbrv__nlc = args[2]
        assert len(col_names_to_replace) == len(zdbrv__nlc
            ), 'Error while typechecking __bodosql_replace_columns_dummy: the tuple of column indicies to replace should be equal to the number of columns to replace them with'
        assert len(col_names_to_replace) <= len(fsd__dbfkp.columns
            ), 'Error while typechecking __bodosql_replace_columns_dummy: The number of indicies provided should be less than or equal to the number of columns in the input dataframe'
        for col_name in col_names_to_replace:
            assert col_name in fsd__dbfkp.columns, 'Error while typechecking __bodosql_replace_columns_dummy: All columns specified to be replaced should already be present in input dataframe'
        check_runtime_cols_unsupported(fsd__dbfkp,
            '__bodosql_replace_columns_dummy()')
        index = fsd__dbfkp.index
        voidi__jeofb = fsd__dbfkp.columns
        djcbm__mxhsv = list(fsd__dbfkp.data)
        for i in range(len(col_names_to_replace)):
            col_name = col_names_to_replace[i]
            gbjeq__dzb = zdbrv__nlc[i]
            assert isinstance(gbjeq__dzb, SeriesType
                ), 'Error while typechecking __bodosql_replace_columns_dummy: the values to replace the columns with are expected to be series'
            if isinstance(gbjeq__dzb, SeriesType):
                gbjeq__dzb = gbjeq__dzb.data
            ugff__hna = fsd__dbfkp.column_index[col_name]
            djcbm__mxhsv[ugff__hna] = gbjeq__dzb
        djcbm__mxhsv = tuple(djcbm__mxhsv)
        fej__zvypv = DataFrameType(djcbm__mxhsv, index, voidi__jeofb,
            fsd__dbfkp.dist, fsd__dbfkp.is_table_format)
        return fej__zvypv(*args)


BodoSQLReplaceColsInfer.prefer_literal = True


def _parse_query_expr(expr, env, columns, cleaned_columns, index_name=None,
    join_cleaned_cols=()):
    iykzm__rmhq = {}

    def _rewrite_membership_op(self, node, left, right):
        fvn__asu = node.op
        op = self.visit(fvn__asu)
        return op, fvn__asu, left, right

    def _maybe_evaluate_binop(self, op, op_class, lhs, rhs, eval_in_python=
        ('in', 'not in'), maybe_eval_in_python=('==', '!=', '<', '>', '<=',
        '>=')):
        res = op(lhs, rhs)
        return res
    qvzn__mfacd = []


    class NewFuncNode(pd.core.computation.ops.FuncNode):

        def __init__(self, name):
            if (name not in pd.core.computation.ops.MATHOPS or pd.core.
                computation.check._NUMEXPR_INSTALLED and pd.core.
                computation.check_NUMEXPR_VERSION < pd.core.computation.ops
                .LooseVersion('2.6.9') and name in ('floor', 'ceil')):
                if name not in qvzn__mfacd:
                    raise BodoError('"{0}" is not a supported function'.
                        format(name))
            self.name = name
            if name in qvzn__mfacd:
                self.func = name
            else:
                self.func = getattr(np, name)

        def __call__(self, *args):
            return pd.core.computation.ops.MathCall(self, args)

        def __repr__(self):
            return pd.io.formats.printing.pprint_thing('(' + self.name + ')')

    def visit_Attribute(self, node, **kwargs):
        gdlxx__mgt = node.attr
        value = node.value
        ake__minqb = pd.core.computation.ops.LOCAL_TAG
        if gdlxx__mgt in ('str', 'dt'):
            try:
                rnuad__inx = str(self.visit(value))
            except pd.core.computation.ops.UndefinedVariableError as vfdq__rhu:
                col_name = vfdq__rhu.args[0].split("'")[1]
                raise BodoError(
                    'df.query(): column {} is not found in dataframe columns {}'
                    .format(col_name, columns))
        else:
            rnuad__inx = str(self.visit(value))
        zsji__dqrwj = rnuad__inx, gdlxx__mgt
        if zsji__dqrwj in join_cleaned_cols:
            gdlxx__mgt = join_cleaned_cols[zsji__dqrwj]
        name = rnuad__inx + '.' + gdlxx__mgt
        if name.startswith(ake__minqb):
            name = name[len(ake__minqb):]
        if gdlxx__mgt in ('str', 'dt'):
            oqcmt__rnuz = columns[cleaned_columns.index(rnuad__inx)]
            iykzm__rmhq[oqcmt__rnuz] = rnuad__inx
            self.env.scope[name] = 0
            return self.term_type(ake__minqb + name, self.env)
        qvzn__mfacd.append(name)
        return NewFuncNode(name)

    def __str__(self):
        if isinstance(self.value, list):
            return '{}'.format(self.value)
        if isinstance(self.value, str):
            return "'{}'".format(self.value)
        return pd.io.formats.printing.pprint_thing(self.name)

    def math__str__(self):
        if self.op in qvzn__mfacd:
            return pd.io.formats.printing.pprint_thing('{0}({1})'.format(
                self.op, ','.join(map(str, self.operands))))
        snzj__xipx = map(lambda a:
            'bodo.hiframes.pd_series_ext.get_series_data({})'.format(str(a)
            ), self.operands)
        op = 'np.{}'.format(self.op)
        lpjds__vgfms = (
            'bodo.hiframes.pd_index_ext.init_range_index(0, len({}), 1, None)'
            .format(str(self.operands[0])))
        return pd.io.formats.printing.pprint_thing(
            'bodo.hiframes.pd_series_ext.init_series({0}({1}), {2})'.format
            (op, ','.join(snzj__xipx), lpjds__vgfms))

    def op__str__(self):
        vwcrs__aofj = ('({0})'.format(pd.io.formats.printing.pprint_thing(
            zgp__vfm)) for zgp__vfm in self.operands)
        if self.op == 'in':
            return pd.io.formats.printing.pprint_thing(
                'bodo.hiframes.pd_dataframe_ext.val_isin_dummy({})'.format(
                ', '.join(vwcrs__aofj)))
        if self.op == 'not in':
            return pd.io.formats.printing.pprint_thing(
                'bodo.hiframes.pd_dataframe_ext.val_notin_dummy({})'.format
                (', '.join(vwcrs__aofj)))
        return pd.io.formats.printing.pprint_thing(' {0} '.format(self.op).
            join(vwcrs__aofj))
    enjf__bkwo = (pd.core.computation.expr.BaseExprVisitor.
        _rewrite_membership_op)
    rlq__nxvl = pd.core.computation.expr.BaseExprVisitor._maybe_evaluate_binop
    wwnf__vmgt = pd.core.computation.expr.BaseExprVisitor.visit_Attribute
    jkd__usp = (pd.core.computation.expr.BaseExprVisitor.
        _maybe_downcast_constants)
    karuu__nbp = pd.core.computation.ops.Term.__str__
    ikbyt__kswv = pd.core.computation.ops.MathCall.__str__
    pyqc__bttt = pd.core.computation.ops.Op.__str__
    ukv__fezj = pd.core.computation.ops.BinOp._disallow_scalar_only_bool_ops
    try:
        pd.core.computation.expr.BaseExprVisitor._rewrite_membership_op = (
            _rewrite_membership_op)
        pd.core.computation.expr.BaseExprVisitor._maybe_evaluate_binop = (
            _maybe_evaluate_binop)
        pd.core.computation.expr.BaseExprVisitor.visit_Attribute = (
            visit_Attribute)
        (pd.core.computation.expr.BaseExprVisitor._maybe_downcast_constants
            ) = lambda self, left, right: (left, right)
        pd.core.computation.ops.Term.__str__ = __str__
        pd.core.computation.ops.MathCall.__str__ = math__str__
        pd.core.computation.ops.Op.__str__ = op__str__
        pd.core.computation.ops.BinOp._disallow_scalar_only_bool_ops = (lambda
            self: None)
        ehuv__nim = pd.core.computation.expr.Expr(expr, env=env)
        uid__zlnd = str(ehuv__nim)
    except pd.core.computation.ops.UndefinedVariableError as vfdq__rhu:
        if not is_overload_none(index_name) and get_overload_const_str(
            index_name) == vfdq__rhu.args[0].split("'")[1]:
            raise BodoError(
                "df.query(): Refering to named index ('{}') by name is not supported"
                .format(get_overload_const_str(index_name)))
        else:
            raise BodoError(f'df.query(): undefined variable, {vfdq__rhu}')
    finally:
        pd.core.computation.expr.BaseExprVisitor._rewrite_membership_op = (
            enjf__bkwo)
        pd.core.computation.expr.BaseExprVisitor._maybe_evaluate_binop = (
            rlq__nxvl)
        pd.core.computation.expr.BaseExprVisitor.visit_Attribute = wwnf__vmgt
        (pd.core.computation.expr.BaseExprVisitor._maybe_downcast_constants
            ) = jkd__usp
        pd.core.computation.ops.Term.__str__ = karuu__nbp
        pd.core.computation.ops.MathCall.__str__ = ikbyt__kswv
        pd.core.computation.ops.Op.__str__ = pyqc__bttt
        pd.core.computation.ops.BinOp._disallow_scalar_only_bool_ops = (
            ukv__fezj)
    xah__gzcyp = pd.core.computation.parsing.clean_column_name
    iykzm__rmhq.update({ahner__puklw: xah__gzcyp(ahner__puklw) for
        ahner__puklw in columns if xah__gzcyp(ahner__puklw) in ehuv__nim.names}
        )
    return ehuv__nim, uid__zlnd, iykzm__rmhq


class DataFrameTupleIterator(types.SimpleIteratorType):

    def __init__(self, col_names, arr_typs):
        self.array_types = arr_typs
        self.col_names = col_names
        gjk__hosu = ['{}={}'.format(col_names[i], arr_typs[i]) for i in
            range(len(col_names))]
        name = 'itertuples({})'.format(','.join(gjk__hosu))
        zmq__nrr = namedtuple('Pandas', col_names)
        pkr__ewswp = types.NamedTuple([_get_series_dtype(a) for a in
            arr_typs], zmq__nrr)
        super(DataFrameTupleIterator, self).__init__(name, pkr__ewswp)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


def _get_series_dtype(arr_typ):
    if arr_typ == types.Array(types.NPDatetime('ns'), 1, 'C'):
        return pd_timestamp_tz_naive_type
    return arr_typ.dtype


def get_itertuples():
    pass


@infer_global(get_itertuples)
class TypeIterTuples(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        assert len(args) % 2 == 0, 'name and column pairs expected'
        col_names = [a.literal_value for a in args[:len(args) // 2]]
        ghie__ioqq = [if_series_to_array_type(a) for a in args[len(args) // 2:]
            ]
        assert 'Index' not in col_names[0]
        col_names = ['Index'] + col_names
        ghie__ioqq = [types.Array(types.int64, 1, 'C')] + ghie__ioqq
        hcelc__fce = DataFrameTupleIterator(col_names, ghie__ioqq)
        return hcelc__fce(*args)


TypeIterTuples.prefer_literal = True


@register_model(DataFrameTupleIterator)
class DataFrameTupleIteratorModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        pidh__ymb = [('index', types.EphemeralPointer(types.uintp))] + [(
            'array{}'.format(i), arr) for i, arr in enumerate(fe_type.
            array_types[1:])]
        super(DataFrameTupleIteratorModel, self).__init__(dmm, fe_type,
            pidh__ymb)

    def from_return(self, builder, value):
        return value


@lower_builtin(get_itertuples, types.VarArg(types.Any))
def get_itertuples_impl(context, builder, sig, args):
    dvbe__sxz = args[len(args) // 2:]
    hvtmt__ukaqy = sig.args[len(sig.args) // 2:]
    xci__tkpg = context.make_helper(builder, sig.return_type)
    jjbe__txdcw = context.get_constant(types.intp, 0)
    hnvcj__hdrf = cgutils.alloca_once_value(builder, jjbe__txdcw)
    xci__tkpg.index = hnvcj__hdrf
    for i, arr in enumerate(dvbe__sxz):
        setattr(xci__tkpg, 'array{}'.format(i), arr)
    for arr, arr_typ in zip(dvbe__sxz, hvtmt__ukaqy):
        context.nrt.incref(builder, arr_typ, arr)
    res = xci__tkpg._getvalue()
    return impl_ret_new_ref(context, builder, sig.return_type, res)


@lower_builtin('getiter', DataFrameTupleIterator)
def getiter_itertuples(context, builder, sig, args):
    return impl_ret_borrowed(context, builder, sig.return_type, args[0])


@lower_builtin('iternext', DataFrameTupleIterator)
@iternext_impl(RefType.UNTRACKED)
def iternext_itertuples(context, builder, sig, args, result):
    wltis__tex, = sig.args
    vujm__ctdh, = args
    xci__tkpg = context.make_helper(builder, wltis__tex, value=vujm__ctdh)
    gmsvs__ecr = signature(types.intp, wltis__tex.array_types[1])
    xxq__bcfjr = context.compile_internal(builder, lambda a: len(a),
        gmsvs__ecr, [xci__tkpg.array0])
    index = builder.load(xci__tkpg.index)
    mwgjd__dsrsn = builder.icmp_signed('<', index, xxq__bcfjr)
    result.set_valid(mwgjd__dsrsn)
    with builder.if_then(mwgjd__dsrsn):
        values = [index]
        for i, arr_typ in enumerate(wltis__tex.array_types[1:]):
            klti__nrm = getattr(xci__tkpg, 'array{}'.format(i))
            if arr_typ == types.Array(types.NPDatetime('ns'), 1, 'C'):
                czpt__eqrlm = signature(pd_timestamp_tz_naive_type, arr_typ,
                    types.intp)
                val = context.compile_internal(builder, lambda a, i: bodo.
                    hiframes.pd_timestamp_ext.
                    convert_datetime64_to_timestamp(np.int64(a[i])),
                    czpt__eqrlm, [klti__nrm, index])
            else:
                czpt__eqrlm = signature(arr_typ.dtype, arr_typ, types.intp)
                val = context.compile_internal(builder, lambda a, i: a[i],
                    czpt__eqrlm, [klti__nrm, index])
            values.append(val)
        value = context.make_tuple(builder, wltis__tex.yield_type, values)
        result.yield_(value)
        srbu__edhcp = cgutils.increment_index(builder, index)
        builder.store(srbu__edhcp, xci__tkpg.index)


def _analyze_op_pair_first(self, scope, equiv_set, expr, lhs):
    typ = self.typemap[expr.value.name].first_type
    if not isinstance(typ, types.NamedTuple):
        return None
    lhs = ir.Var(scope, mk_unique_var('tuple_var'), expr.loc)
    self.typemap[lhs.name] = typ
    rhs = ir.Expr.pair_first(expr.value, expr.loc)
    nvlov__hacyd = ir.Assign(rhs, lhs, expr.loc)
    qwbjx__klfm = lhs
    kne__ksgo = []
    rpudd__gea = []
    kfuwf__kecmy = typ.count
    for i in range(kfuwf__kecmy):
        auy__eeyio = ir.Var(qwbjx__klfm.scope, mk_unique_var('{}_size{}'.
            format(qwbjx__klfm.name, i)), qwbjx__klfm.loc)
        ldb__dihsz = ir.Expr.static_getitem(lhs, i, None, qwbjx__klfm.loc)
        self.calltypes[ldb__dihsz] = None
        kne__ksgo.append(ir.Assign(ldb__dihsz, auy__eeyio, qwbjx__klfm.loc))
        self._define(equiv_set, auy__eeyio, types.intp, ldb__dihsz)
        rpudd__gea.append(auy__eeyio)
    xfdlp__rgrut = tuple(rpudd__gea)
    return numba.parfors.array_analysis.ArrayAnalysis.AnalyzeResult(shape=
        xfdlp__rgrut, pre=[nvlov__hacyd] + kne__ksgo)


numba.parfors.array_analysis.ArrayAnalysis._analyze_op_pair_first = (
    _analyze_op_pair_first)
