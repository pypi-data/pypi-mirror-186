"""Support for Pandas Groupby operations
"""
import operator
from enum import Enum
import numba
import numpy as np
from numba.core import cgutils, types
from numba.core.imputils import impl_ret_borrowed
from numba.core.registry import CPUDispatcher
from numba.core.typing.templates import AbstractTemplate, bound_function, infer_global, signature
from numba.extending import infer, infer_getattr, intrinsic, lower_builtin, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_model
import bodo
from bodo.hiframes.pd_dataframe_ext import DataFrameType
from bodo.hiframes.pd_index_ext import NumericIndexType, RangeIndexType
from bodo.hiframes.pd_multi_index_ext import MultiIndexType
from bodo.hiframes.pd_series_ext import HeterogeneousSeriesType, SeriesType
from bodo.libs.array import arr_info_list_to_table, array_to_info, delete_table, delete_table_decref_arrays, get_groupby_labels, get_null_shuffle_info, get_shuffle_info, info_from_table, info_to_array, reverse_shuffle_table, shuffle_table
from bodo.libs.array_item_arr_ext import ArrayItemArrayType
from bodo.libs.decimal_arr_ext import Decimal128Type
from bodo.libs.float_arr_ext import FloatDtype, FloatingArrayType
from bodo.libs.int_arr_ext import IntDtype, IntegerArrayType
from bodo.libs.str_arr_ext import string_array_type
from bodo.libs.str_ext import string_type
from bodo.libs.tuple_arr_ext import TupleArrayType
from bodo.utils.templates import OverloadedKeyAttributeTemplate
from bodo.utils.transform import get_call_expr_arg, get_const_func_output_type
from bodo.utils.typing import BodoError, ColNamesMetaType, check_unsupported_args, create_unsupported_overload, dtype_to_array_type, get_index_data_arr_types, get_index_name_types, get_literal_value, get_overload_const_bool, get_overload_const_func, get_overload_const_int, get_overload_const_list, get_overload_const_str, get_overload_constant_dict, get_udf_error_msg, get_udf_out_arr_type, is_dtype_nullable, is_literal_type, is_overload_constant_bool, is_overload_constant_dict, is_overload_constant_int, is_overload_constant_list, is_overload_constant_str, is_overload_false, is_overload_none, is_overload_true, list_cumulative, raise_bodo_error, to_nullable_type, to_numeric_index_if_range_index, to_str_arr_if_dict_array
from bodo.utils.utils import dt_err, is_expr


class DataFrameGroupByType(types.Type):

    def __init__(self, df_type, keys, selection, as_index, dropna=True,
        explicit_select=False, series_select=False, _num_shuffle_keys=-1):
        self.df_type = df_type
        self.keys = keys
        self.selection = selection
        self.as_index = as_index
        self.dropna = dropna
        self.explicit_select = explicit_select
        self.series_select = series_select
        self._num_shuffle_keys = _num_shuffle_keys
        super(DataFrameGroupByType, self).__init__(name=
            f'DataFrameGroupBy({df_type}, {keys}, {selection}, {as_index}, {dropna}, {explicit_select}, {series_select}, {_num_shuffle_keys})'
            )

    def copy(self):
        return DataFrameGroupByType(self.df_type, self.keys, self.selection,
            self.as_index, self.dropna, self.explicit_select, self.
            series_select, self._num_shuffle_keys)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


@register_model(DataFrameGroupByType)
class GroupbyModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        zgh__gwxj = [('obj', fe_type.df_type)]
        super(GroupbyModel, self).__init__(dmm, fe_type, zgh__gwxj)


make_attribute_wrapper(DataFrameGroupByType, 'obj', 'obj')


def validate_udf(func_name, func):
    if not isinstance(func, (types.functions.MakeFunctionLiteral, bodo.
        utils.typing.FunctionLiteral, types.Dispatcher, CPUDispatcher)):
        raise_bodo_error(
            f"Groupby.{func_name}: 'func' must be user defined function")


@intrinsic
def init_groupby(typingctx, obj_type, by_type, as_index_type, dropna_type,
    _num_shuffle_keys):

    def codegen(context, builder, signature, args):
        ioj__njxdu = args[0]
        fnelg__fmu = signature.return_type
        jzko__tdg = cgutils.create_struct_proxy(fnelg__fmu)(context, builder)
        jzko__tdg.obj = ioj__njxdu
        context.nrt.incref(builder, signature.args[0], ioj__njxdu)
        return jzko__tdg._getvalue()
    if is_overload_constant_list(by_type):
        keys = tuple(get_overload_const_list(by_type))
    elif is_literal_type(by_type):
        keys = get_literal_value(by_type),
    else:
        assert False, 'Reached unreachable code in init_groupby; there is an validate_groupby_spec'
    selection = list(obj_type.columns)
    for dqwnq__tubmg in keys:
        selection.remove(dqwnq__tubmg)
    if is_overload_constant_bool(as_index_type):
        as_index = is_overload_true(as_index_type)
    else:
        as_index = True
    if is_overload_constant_bool(dropna_type):
        dropna = is_overload_true(dropna_type)
    else:
        dropna = True
    if is_overload_constant_int(_num_shuffle_keys):
        hqn__qmnfp = get_overload_const_int(_num_shuffle_keys)
    else:
        hqn__qmnfp = -1
    fnelg__fmu = DataFrameGroupByType(obj_type, keys, tuple(selection),
        as_index, dropna, False, _num_shuffle_keys=hqn__qmnfp)
    return fnelg__fmu(obj_type, by_type, as_index_type, dropna_type,
        _num_shuffle_keys), codegen


@lower_builtin('groupby.count', types.VarArg(types.Any))
@lower_builtin('groupby.size', types.VarArg(types.Any))
@lower_builtin('groupby.apply', types.VarArg(types.Any))
@lower_builtin('groupby.agg', types.VarArg(types.Any))
def lower_groupby_count_dummy(context, builder, sig, args):
    return context.get_constant_null(sig.return_type)


@infer
class StaticGetItemDataFrameGroupBy(AbstractTemplate):
    key = 'static_getitem'

    def generic(self, args, kws):
        grpby, mil__jccux = args
        if isinstance(grpby, DataFrameGroupByType):
            series_select = False
            if isinstance(mil__jccux, (tuple, list)):
                if len(set(mil__jccux).difference(set(grpby.df_type.columns))
                    ) > 0:
                    raise_bodo_error(
                        'groupby: selected column {} not found in dataframe'
                        .format(set(mil__jccux).difference(set(grpby.
                        df_type.columns))))
                selection = mil__jccux
            else:
                if mil__jccux not in grpby.df_type.columns:
                    raise_bodo_error(
                        'groupby: selected column {} not found in dataframe'
                        .format(mil__jccux))
                selection = mil__jccux,
                series_select = True
            bgn__xitbi = DataFrameGroupByType(grpby.df_type, grpby.keys,
                selection, grpby.as_index, grpby.dropna, True,
                series_select, _num_shuffle_keys=grpby._num_shuffle_keys)
            return signature(bgn__xitbi, *args)


@infer_global(operator.getitem)
class GetItemDataFrameGroupBy(AbstractTemplate):

    def generic(self, args, kws):
        grpby, mil__jccux = args
        if isinstance(grpby, DataFrameGroupByType) and is_literal_type(
            mil__jccux):
            bgn__xitbi = StaticGetItemDataFrameGroupBy.generic(self, (grpby,
                get_literal_value(mil__jccux)), {}).return_type
            return signature(bgn__xitbi, *args)


GetItemDataFrameGroupBy.prefer_literal = True


@lower_builtin('static_getitem', DataFrameGroupByType, types.Any)
@lower_builtin(operator.getitem, DataFrameGroupByType, types.Any)
def static_getitem_df_groupby(context, builder, sig, args):
    return impl_ret_borrowed(context, builder, sig.return_type, args[0])


def get_groupby_output_dtype(arr_type, func_name, index_type=None):
    mytil__guye = arr_type == ArrayItemArrayType(string_array_type)
    eekof__vgof = arr_type.dtype
    if isinstance(eekof__vgof, bodo.hiframes.datetime_timedelta_ext.
        DatetimeTimeDeltaType):
        raise BodoError(
            f"""column type of {eekof__vgof} is not supported in groupby built-in function {func_name}.
{dt_err}"""
            )
    if func_name == 'median' and not isinstance(eekof__vgof, (
        Decimal128Type, types.Float, types.Integer)):
        return (None,
            'For median, only column of integer, float or Decimal type are allowed'
            )
    elif func_name in ('first', 'last', 'sum', 'prod', 'min', 'max',
        'count', 'nunique', 'head') and isinstance(arr_type, (
        TupleArrayType, ArrayItemArrayType)):
        return (None,
            f'column type of list/tuple of {eekof__vgof} is not supported in groupby built-in function {func_name}'
            )
    elif func_name in {'median', 'mean', 'var', 'std'} and isinstance(
        eekof__vgof, (Decimal128Type, types.Integer, types.Float)):
        return dtype_to_array_type(types.float64), 'ok'
    elif func_name == 'boolor_agg':
        if isinstance(eekof__vgof, (Decimal128Type, types.Integer, types.
            Float, types.Boolean)):
            return bodo.boolean_array, 'ok'
        return (None,
            f'For boolor_agg, only columns of type integer, float, Decimal, or boolean type are allowed'
            )
    if not isinstance(eekof__vgof, (types.Integer, types.Float, types.Boolean)
        ):
        if mytil__guye or eekof__vgof == types.unicode_type:
            if func_name not in {'count', 'nunique', 'min', 'max', 'sum',
                'first', 'last', 'head'}:
                return (None,
                    f'column type of strings or list of strings is not supported in groupby built-in function {func_name}'
                    )
        else:
            if isinstance(eekof__vgof, bodo.PDCategoricalDtype):
                if func_name in ('min', 'max') and not eekof__vgof.ordered:
                    return (None,
                        f'categorical column must be ordered in groupby built-in function {func_name}'
                        )
            if func_name not in {'count', 'nunique', 'min', 'max', 'first',
                'last', 'head'}:
                return (None,
                    f'column type of {eekof__vgof} is not supported in groupby built-in function {func_name}'
                    )
    if isinstance(eekof__vgof, types.Boolean) and func_name in {'cumsum',
        'mean', 'sum', 'std', 'var'}:
        if func_name in {'sum'}:
            return to_nullable_type(dtype_to_array_type(types.int64)), 'ok'
        return (None,
            f'groupby built-in functions {func_name} does not support boolean column'
            )
    elif func_name in {'idxmin', 'idxmax'}:
        return dtype_to_array_type(get_index_data_arr_types(index_type)[0].
            dtype), 'ok'
    elif func_name in {'count', 'nunique'}:
        return dtype_to_array_type(types.int64), 'ok'
    else:
        return arr_type, 'ok'


def get_pivot_output_dtype(arr_type, func_name, index_type=None):
    eekof__vgof = arr_type.dtype
    if func_name in {'count'}:
        return IntDtype(types.int64)
    if func_name in {'sum', 'prod', 'min', 'max'}:
        if func_name in {'sum', 'prod'} and not isinstance(eekof__vgof, (
            types.Integer, types.Float)):
            raise BodoError(
                'pivot_table(): sum and prod operations require integer or float input'
                )
        if isinstance(eekof__vgof, types.Integer):
            return IntDtype(eekof__vgof)
        return eekof__vgof
    if func_name in {'mean', 'var', 'std'}:
        return types.float64
    raise BodoError('invalid pivot operation')


def check_args_kwargs(func_name, len_args, args, kws):
    if len(kws) > 0:
        qswco__gzc = list(kws.keys())[0]
        raise BodoError(
            f"Groupby.{func_name}() got an unexpected keyword argument '{qswco__gzc}'."
            )
    elif len(args) > len_args:
        raise BodoError(
            f'Groupby.{func_name}() takes {len_args + 1} positional argument but {len(args)} were given.'
            )


class ColumnType(Enum):
    KeyColumn = 0
    NumericalColumn = 1
    NonNumericalColumn = 2


def get_keys_not_as_index(grp, out_columns, out_data, out_column_type,
    multi_level_names=False):
    for dqwnq__tubmg in grp.keys:
        if multi_level_names:
            wfmgb__qodli = dqwnq__tubmg, ''
        else:
            wfmgb__qodli = dqwnq__tubmg
        vxx__unp = grp.df_type.column_index[dqwnq__tubmg]
        data = grp.df_type.data[vxx__unp]
        out_columns.append(wfmgb__qodli)
        out_data.append(data)
        out_column_type.append(ColumnType.KeyColumn.value)


def get_agg_typ(grp, args, func_name, typing_context, target_context, func=
    None, kws=None, raise_on_any_error=False):
    index = RangeIndexType(types.none)
    out_data = []
    out_columns = []
    out_column_type = []
    if func_name in ('head', 'ngroup'):
        grp.as_index = True
    if not grp.as_index:
        get_keys_not_as_index(grp, out_columns, out_data, out_column_type)
    elif func_name in ('head', 'ngroup'):
        if grp.df_type.index == index:
            index = NumericIndexType(types.int64, types.none)
        else:
            index = grp.df_type.index
    elif len(grp.keys) > 1:
        hmdid__mjxpo = tuple(grp.df_type.column_index[grp.keys[zbu__shl]] for
            zbu__shl in range(len(grp.keys)))
        fqfkr__mhyqm = tuple(grp.df_type.data[vxx__unp] for vxx__unp in
            hmdid__mjxpo)
        index = MultiIndexType(fqfkr__mhyqm, tuple(types.StringLiteral(
            dqwnq__tubmg) for dqwnq__tubmg in grp.keys))
    else:
        vxx__unp = grp.df_type.column_index[grp.keys[0]]
        rlxq__axouu = grp.df_type.data[vxx__unp]
        index = bodo.hiframes.pd_index_ext.array_type_to_index(rlxq__axouu,
            types.StringLiteral(grp.keys[0]))
    rzyw__zya = {}
    vtdu__trsu = []
    if func_name in ('size', 'count'):
        kws = dict(kws) if kws else {}
        check_args_kwargs(func_name, 0, args, kws)
    if func_name == 'size':
        out_data.append(types.Array(types.int64, 1, 'C'))
        out_columns.append('size')
        rzyw__zya[None, 'size'] = 'size'
    elif func_name == 'ngroup':
        out_data.append(types.Array(types.int64, 1, 'C'))
        out_columns.append('ngroup')
        rzyw__zya[None, 'ngroup'] = 'ngroup'
        kws = dict(kws) if kws else {}
        ascending = args[0] if len(args) > 0 else kws.pop('ascending', True)
        ivxgr__hbn = dict(ascending=ascending)
        xoy__sidby = dict(ascending=True)
        check_unsupported_args(f'Groupby.{func_name}', ivxgr__hbn,
            xoy__sidby, package_name='pandas', module_name='GroupBy')
        check_args_kwargs(func_name, 1, args, kws)
    else:
        columns = (grp.selection if func_name != 'head' or grp.
            explicit_select else grp.df_type.columns)
        for ehvz__kgr in columns:
            vxx__unp = grp.df_type.column_index[ehvz__kgr]
            data = grp.df_type.data[vxx__unp]
            if func_name in ('sum', 'cumsum'):
                data = to_str_arr_if_dict_array(data)
            pef__fen = ColumnType.NonNumericalColumn.value
            if isinstance(data, (types.Array, IntegerArrayType,
                FloatingArrayType)) and isinstance(data.dtype, (types.
                Integer, types.Float)):
                pef__fen = ColumnType.NumericalColumn.value
            if func_name == 'agg':
                try:
                    nqe__qrhw = SeriesType(data.dtype, data, None, string_type)
                    ikdf__yvt = get_const_func_output_type(func, (nqe__qrhw
                        ,), {}, typing_context, target_context)
                    if ikdf__yvt != ArrayItemArrayType(string_array_type):
                        ikdf__yvt = dtype_to_array_type(ikdf__yvt)
                    err_msg = 'ok'
                except:
                    raise_bodo_error(
                        'Groupy.agg()/Groupy.aggregate(): column {col} of type {type} is unsupported/not a valid input type for user defined function'
                        .format(col=ehvz__kgr, type=data.dtype))
            else:
                if func_name in ('first', 'last', 'min', 'max'):
                    kws = dict(kws) if kws else {}
                    wjo__zjoh = args[0] if len(args) > 0 else kws.pop(
                        'numeric_only', False)
                    jyjle__zyj = args[1] if len(args) > 1 else kws.pop(
                        'min_count', -1)
                    ivxgr__hbn = dict(numeric_only=wjo__zjoh, min_count=
                        jyjle__zyj)
                    xoy__sidby = dict(numeric_only=False, min_count=-1)
                    check_unsupported_args(f'Groupby.{func_name}',
                        ivxgr__hbn, xoy__sidby, package_name='pandas',
                        module_name='GroupBy')
                elif func_name in ('sum', 'prod'):
                    kws = dict(kws) if kws else {}
                    wjo__zjoh = args[0] if len(args) > 0 else kws.pop(
                        'numeric_only', True)
                    jyjle__zyj = args[1] if len(args) > 1 else kws.pop(
                        'min_count', 0)
                    ivxgr__hbn = dict(numeric_only=wjo__zjoh, min_count=
                        jyjle__zyj)
                    xoy__sidby = dict(numeric_only=True, min_count=0)
                    check_unsupported_args(f'Groupby.{func_name}',
                        ivxgr__hbn, xoy__sidby, package_name='pandas',
                        module_name='GroupBy')
                elif func_name in ('mean', 'median'):
                    kws = dict(kws) if kws else {}
                    wjo__zjoh = args[0] if len(args) > 0 else kws.pop(
                        'numeric_only', True)
                    ivxgr__hbn = dict(numeric_only=wjo__zjoh)
                    xoy__sidby = dict(numeric_only=True)
                    check_unsupported_args(f'Groupby.{func_name}',
                        ivxgr__hbn, xoy__sidby, package_name='pandas',
                        module_name='GroupBy')
                elif func_name in ('idxmin', 'idxmax'):
                    kws = dict(kws) if kws else {}
                    diz__feec = args[0] if len(args) > 0 else kws.pop('axis', 0
                        )
                    quvy__yja = args[1] if len(args) > 1 else kws.pop('skipna',
                        True)
                    ivxgr__hbn = dict(axis=diz__feec, skipna=quvy__yja)
                    xoy__sidby = dict(axis=0, skipna=True)
                    check_unsupported_args(f'Groupby.{func_name}',
                        ivxgr__hbn, xoy__sidby, package_name='pandas',
                        module_name='GroupBy')
                elif func_name in ('var', 'std'):
                    kws = dict(kws) if kws else {}
                    klwa__wievn = args[0] if len(args) > 0 else kws.pop('ddof',
                        1)
                    ivxgr__hbn = dict(ddof=klwa__wievn)
                    xoy__sidby = dict(ddof=1)
                    check_unsupported_args(f'Groupby.{func_name}',
                        ivxgr__hbn, xoy__sidby, package_name='pandas',
                        module_name='GroupBy')
                elif func_name == 'nunique':
                    kws = dict(kws) if kws else {}
                    dropna = args[0] if len(args) > 0 else kws.pop('dropna', 1)
                    check_args_kwargs(func_name, 1, args, kws)
                elif func_name == 'head':
                    if len(args) == 0:
                        kws.pop('n', None)
                ikdf__yvt, err_msg = get_groupby_output_dtype(data,
                    func_name, grp.df_type.index)
            if err_msg == 'ok':
                ikdf__yvt = to_str_arr_if_dict_array(ikdf__yvt
                    ) if func_name in ('sum', 'cumsum') else ikdf__yvt
                out_data.append(ikdf__yvt)
                out_columns.append(ehvz__kgr)
                if func_name == 'agg':
                    qxnd__hbd = bodo.ir.aggregate._get_udf_name(bodo.ir.
                        aggregate._get_const_agg_func(func, None))
                    rzyw__zya[ehvz__kgr, qxnd__hbd] = ehvz__kgr
                else:
                    rzyw__zya[ehvz__kgr, func_name] = ehvz__kgr
                out_column_type.append(pef__fen)
            elif raise_on_any_error:
                raise BodoError(
                    f'Groupby with function {func_name} not supported. Error message: {err_msg}'
                    )
            else:
                vtdu__trsu.append(err_msg)
    if func_name == 'sum':
        ziy__mlw = any([(ckanr__zjf == ColumnType.NumericalColumn.value) for
            ckanr__zjf in out_column_type])
        if ziy__mlw:
            out_data = [ckanr__zjf for ckanr__zjf, cdrt__dwett in zip(
                out_data, out_column_type) if cdrt__dwett != ColumnType.
                NonNumericalColumn.value]
            out_columns = [ckanr__zjf for ckanr__zjf, cdrt__dwett in zip(
                out_columns, out_column_type) if cdrt__dwett != ColumnType.
                NonNumericalColumn.value]
            rzyw__zya = {}
            for ehvz__kgr in out_columns:
                if grp.as_index is False and ehvz__kgr in grp.keys:
                    continue
                rzyw__zya[ehvz__kgr, func_name] = ehvz__kgr
    dby__xek = len(vtdu__trsu)
    if len(out_data) == 0:
        if dby__xek == 0:
            raise BodoError('No columns in output.')
        else:
            raise BodoError(
                'No columns in output. {} column{} dropped for following reasons: {}'
                .format(dby__xek, ' was' if dby__xek == 1 else 's were',
                ','.join(vtdu__trsu)))
    lews__swg = DataFrameType(tuple(out_data), index, tuple(out_columns),
        is_table_format=True)
    if (len(grp.selection) == 1 and grp.series_select and grp.as_index or 
        func_name == 'size' and grp.as_index or func_name == 'ngroup'):
        if isinstance(out_data[0], IntegerArrayType):
            ezv__xruhm = IntDtype(out_data[0].dtype)
        elif isinstance(out_data[0], FloatingArrayType):
            ezv__xruhm = FloatDtype(out_data[0].dtype)
        else:
            ezv__xruhm = out_data[0].dtype
        tinb__qrn = types.none if func_name in ('size', 'ngroup'
            ) else types.StringLiteral(grp.selection[0])
        lews__swg = SeriesType(ezv__xruhm, data=out_data[0], index=index,
            name_typ=tinb__qrn)
    return signature(lews__swg, *args), rzyw__zya


def get_agg_funcname_and_outtyp(grp, col, f_val, typing_context,
    target_context, raise_on_any_error):
    twddp__jpkkc = True
    if isinstance(f_val, str):
        twddp__jpkkc = False
        uvks__enump = f_val
    elif is_overload_constant_str(f_val):
        twddp__jpkkc = False
        uvks__enump = get_overload_const_str(f_val)
    elif bodo.utils.typing.is_builtin_function(f_val):
        twddp__jpkkc = False
        uvks__enump = bodo.utils.typing.get_builtin_function_name(f_val)
    if not twddp__jpkkc:
        if uvks__enump not in bodo.ir.aggregate.supported_agg_funcs[:-1]:
            raise BodoError(f'unsupported aggregate function {uvks__enump}')
        bgn__xitbi = DataFrameGroupByType(grp.df_type, grp.keys, (col,),
            grp.as_index, grp.dropna, True, True, _num_shuffle_keys=grp.
            _num_shuffle_keys)
        out_tp = get_agg_typ(bgn__xitbi, (), uvks__enump, typing_context,
            target_context, raise_on_any_error=raise_on_any_error)[0
            ].return_type
    else:
        if is_expr(f_val, 'make_function'):
            nhl__ieizx = types.functions.MakeFunctionLiteral(f_val)
        else:
            nhl__ieizx = f_val
        validate_udf('agg', nhl__ieizx)
        func = get_overload_const_func(nhl__ieizx, None)
        pzo__gxe = func.code if hasattr(func, 'code') else func.__code__
        uvks__enump = pzo__gxe.co_name
        bgn__xitbi = DataFrameGroupByType(grp.df_type, grp.keys, (col,),
            grp.as_index, grp.dropna, True, True, _num_shuffle_keys=grp.
            _num_shuffle_keys)
        out_tp = get_agg_typ(bgn__xitbi, (), 'agg', typing_context,
            target_context, nhl__ieizx, raise_on_any_error=raise_on_any_error)[
            0].return_type
    return uvks__enump, out_tp


def resolve_agg(grp, args, kws, typing_context, target_context):
    func = get_call_expr_arg('agg', args, dict(kws), 0, 'func', default=
        types.none)
    qexon__ukxj = kws and all(isinstance(kqw__axez, types.Tuple) and len(
        kqw__axez) == 2 for kqw__axez in kws.values())
    raise_on_any_error = qexon__ukxj
    if is_overload_none(func) and not qexon__ukxj:
        raise_bodo_error("Groupby.agg()/aggregate(): Must provide 'func'")
    if len(args) > 1 or kws and not qexon__ukxj:
        raise_bodo_error(
            'Groupby.agg()/aggregate(): passing extra arguments to functions not supported yet.'
            )
    bqzxm__mozxx = False

    def _append_out_type(grp, out_data, out_tp):
        if grp.as_index is False:
            out_data.append(out_tp.data[len(grp.keys)])
        else:
            out_data.append(out_tp.data)
    if qexon__ukxj or is_overload_constant_dict(func):
        if qexon__ukxj:
            sywfj__duap = [get_literal_value(eotoh__ucq) for eotoh__ucq,
                hygib__uhdvz in kws.values()]
            zmi__peenz = [get_literal_value(fcrt__wxcf) for hygib__uhdvz,
                fcrt__wxcf in kws.values()]
        else:
            sxex__zhnw = get_overload_constant_dict(func)
            sywfj__duap = tuple(sxex__zhnw.keys())
            zmi__peenz = tuple(sxex__zhnw.values())
        for bwj__ehv in ('head', 'ngroup'):
            if bwj__ehv in zmi__peenz:
                raise BodoError(
                    f'Groupby.agg()/aggregate(): {bwj__ehv} cannot be mixed with other groupby operations.'
                    )
        if any(ehvz__kgr not in grp.selection and ehvz__kgr not in grp.keys for
            ehvz__kgr in sywfj__duap):
            raise_bodo_error(
                f'Selected column names {sywfj__duap} not all available in dataframe column names {grp.selection}'
                )
        multi_level_names = any(isinstance(f_val, (tuple, list)) for f_val in
            zmi__peenz)
        if qexon__ukxj and multi_level_names:
            raise_bodo_error(
                'Groupby.agg()/aggregate(): cannot pass multiple functions in a single pd.NamedAgg()'
                )
        rzyw__zya = {}
        out_columns = []
        out_data = []
        out_column_type = []
        zznbm__fwck = []
        if not grp.as_index:
            get_keys_not_as_index(grp, out_columns, out_data,
                out_column_type, multi_level_names=multi_level_names)
        for wuw__cxii, f_val in zip(sywfj__duap, zmi__peenz):
            if isinstance(f_val, (tuple, list)):
                gnzi__srp = 0
                for nhl__ieizx in f_val:
                    uvks__enump, out_tp = get_agg_funcname_and_outtyp(grp,
                        wuw__cxii, nhl__ieizx, typing_context,
                        target_context, raise_on_any_error)
                    bqzxm__mozxx = uvks__enump in list_cumulative
                    if uvks__enump == '<lambda>' and len(f_val) > 1:
                        uvks__enump = '<lambda_' + str(gnzi__srp) + '>'
                        gnzi__srp += 1
                    out_columns.append((wuw__cxii, uvks__enump))
                    rzyw__zya[wuw__cxii, uvks__enump] = wuw__cxii, uvks__enump
                    _append_out_type(grp, out_data, out_tp)
            else:
                uvks__enump, out_tp = get_agg_funcname_and_outtyp(grp,
                    wuw__cxii, f_val, typing_context, target_context,
                    raise_on_any_error)
                bqzxm__mozxx = uvks__enump in list_cumulative
                if multi_level_names:
                    out_columns.append((wuw__cxii, uvks__enump))
                    rzyw__zya[wuw__cxii, uvks__enump] = wuw__cxii, uvks__enump
                elif not qexon__ukxj:
                    out_columns.append(wuw__cxii)
                    rzyw__zya[wuw__cxii, uvks__enump] = wuw__cxii
                elif qexon__ukxj:
                    zznbm__fwck.append(uvks__enump)
                _append_out_type(grp, out_data, out_tp)
        if qexon__ukxj:
            for zbu__shl, wkhj__cuefc in enumerate(kws.keys()):
                out_columns.append(wkhj__cuefc)
                rzyw__zya[sywfj__duap[zbu__shl], zznbm__fwck[zbu__shl]
                    ] = wkhj__cuefc
        if bqzxm__mozxx:
            index = grp.df_type.index
        else:
            index = out_tp.index
        lews__swg = DataFrameType(tuple(out_data), index, tuple(out_columns
            ), is_table_format=True)
        return signature(lews__swg, *args), rzyw__zya
    if isinstance(func, types.BaseTuple) and not isinstance(func, types.
        LiteralStrKeyDict) or is_overload_constant_list(func):
        if not (len(grp.selection) == 1 and grp.explicit_select):
            raise_bodo_error(
                'Groupby.agg()/aggregate(): must select exactly one column when more than one function is supplied'
                )
        if is_overload_constant_list(func):
            cnadz__yhnm = get_overload_const_list(func)
        else:
            cnadz__yhnm = func.types
        if len(cnadz__yhnm) == 0:
            raise_bodo_error(
                'Groupby.agg()/aggregate(): List of functions must contain at least 1 function'
                )
        out_data = []
        out_columns = []
        out_column_type = []
        gnzi__srp = 0
        if not grp.as_index:
            get_keys_not_as_index(grp, out_columns, out_data, out_column_type)
        rzyw__zya = {}
        iyu__uvosv = grp.selection[0]
        for f_val in cnadz__yhnm:
            uvks__enump, out_tp = get_agg_funcname_and_outtyp(grp,
                iyu__uvosv, f_val, typing_context, target_context,
                raise_on_any_error)
            bqzxm__mozxx = uvks__enump in list_cumulative
            if uvks__enump == '<lambda>' and len(cnadz__yhnm) > 1:
                uvks__enump = '<lambda_' + str(gnzi__srp) + '>'
                gnzi__srp += 1
            out_columns.append(uvks__enump)
            rzyw__zya[iyu__uvosv, uvks__enump] = uvks__enump
            _append_out_type(grp, out_data, out_tp)
        if bqzxm__mozxx:
            index = grp.df_type.index
        else:
            index = out_tp.index
        lews__swg = DataFrameType(tuple(out_data), index, tuple(out_columns
            ), is_table_format=True)
        return signature(lews__swg, *args), rzyw__zya
    uvks__enump = ''
    if types.unliteral(func) == types.unicode_type:
        uvks__enump = get_overload_const_str(func)
    if bodo.utils.typing.is_builtin_function(func):
        uvks__enump = bodo.utils.typing.get_builtin_function_name(func)
    if uvks__enump:
        args = args[1:]
        kws.pop('func', None)
        return get_agg_typ(grp, args, uvks__enump, typing_context, kws)
    validate_udf('agg', func)
    return get_agg_typ(grp, args, 'agg', typing_context, target_context, func)


def resolve_transformative(grp, args, kws, msg, name_operation):
    index = to_numeric_index_if_range_index(grp.df_type.index)
    if isinstance(index, MultiIndexType):
        raise_bodo_error(
            f'Groupby.{name_operation}: MultiIndex input not supported for groupby operations that use input Index'
            )
    out_columns = []
    out_data = []
    if name_operation in list_cumulative:
        kws = dict(kws) if kws else {}
        diz__feec = args[0] if len(args) > 0 else kws.pop('axis', 0)
        wjo__zjoh = args[1] if len(args) > 1 else kws.pop('numeric_only', False
            )
        quvy__yja = args[2] if len(args) > 2 else kws.pop('skipna', 1)
        ivxgr__hbn = dict(axis=diz__feec, numeric_only=wjo__zjoh)
        xoy__sidby = dict(axis=0, numeric_only=False)
        check_unsupported_args(f'Groupby.{name_operation}', ivxgr__hbn,
            xoy__sidby, package_name='pandas', module_name='GroupBy')
        check_args_kwargs(name_operation, 3, args, kws)
    elif name_operation == 'shift':
        nvlb__ayvd = args[0] if len(args) > 0 else kws.pop('periods', 1)
        yywz__ldhx = args[1] if len(args) > 1 else kws.pop('freq', None)
        diz__feec = args[2] if len(args) > 2 else kws.pop('axis', 0)
        vsuns__iazm = args[3] if len(args) > 3 else kws.pop('fill_value', None)
        ivxgr__hbn = dict(freq=yywz__ldhx, axis=diz__feec, fill_value=
            vsuns__iazm)
        xoy__sidby = dict(freq=None, axis=0, fill_value=None)
        check_unsupported_args(f'Groupby.{name_operation}', ivxgr__hbn,
            xoy__sidby, package_name='pandas', module_name='GroupBy')
        check_args_kwargs(name_operation, 4, args, kws)
    elif name_operation == 'transform':
        kws = dict(kws)
        fdv__wojef = args[0] if len(args) > 0 else kws.pop('func', None)
        odd__orzoo = kws.pop('engine', None)
        caqev__rnt = kws.pop('engine_kwargs', None)
        ivxgr__hbn = dict(engine=odd__orzoo, engine_kwargs=caqev__rnt)
        xoy__sidby = dict(engine=None, engine_kwargs=None)
        check_unsupported_args(f'Groupby.transform', ivxgr__hbn, xoy__sidby,
            package_name='pandas', module_name='GroupBy')
    rzyw__zya = {}
    for ehvz__kgr in grp.selection:
        out_columns.append(ehvz__kgr)
        rzyw__zya[ehvz__kgr, name_operation] = ehvz__kgr
        vxx__unp = grp.df_type.column_index[ehvz__kgr]
        data = grp.df_type.data[vxx__unp]
        xjqnu__btcfd = (name_operation if name_operation != 'transform' else
            get_literal_value(fdv__wojef))
        if xjqnu__btcfd in ('sum', 'cumsum'):
            data = to_str_arr_if_dict_array(data)
        if name_operation == 'cumprod':
            if not isinstance(data.dtype, (types.Integer, types.Float)):
                raise BodoError(msg)
        if name_operation == 'cumsum':
            if data.dtype != types.unicode_type and data != ArrayItemArrayType(
                string_array_type) and not isinstance(data.dtype, (types.
                Integer, types.Float)):
                raise BodoError(msg)
        if name_operation in ('cummin', 'cummax'):
            if not isinstance(data.dtype, types.Integer
                ) and not is_dtype_nullable(data.dtype):
                raise BodoError(msg)
        if name_operation == 'shift':
            if isinstance(data, (TupleArrayType, ArrayItemArrayType)):
                raise BodoError(msg)
            if isinstance(data.dtype, bodo.hiframes.datetime_timedelta_ext.
                DatetimeTimeDeltaType):
                raise BodoError(
                    f"""column type of {data.dtype} is not supported in groupby built-in function shift.
{dt_err}"""
                    )
        if name_operation == 'transform':
            ikdf__yvt, err_msg = get_groupby_output_dtype(data,
                get_literal_value(fdv__wojef), grp.df_type.index)
            if err_msg == 'ok':
                data = ikdf__yvt
            else:
                raise BodoError(
                    f'column type of {data.dtype} is not supported by {args[0]} yet.\n'
                    )
        out_data.append(data)
    if len(out_data) == 0:
        raise BodoError('No columns in output.')
    lews__swg = DataFrameType(tuple(out_data), index, tuple(out_columns),
        is_table_format=True)
    if len(grp.selection) == 1 and grp.series_select and grp.as_index:
        lews__swg = SeriesType(out_data[0].dtype, data=out_data[0], index=
            index, name_typ=types.StringLiteral(grp.selection[0]))
    return signature(lews__swg, *args), rzyw__zya


def resolve_gb(grp, args, kws, func_name, typing_context, target_context,
    err_msg=''):
    if func_name in set(list_cumulative) | {'shift', 'transform'}:
        return resolve_transformative(grp, args, kws, err_msg, func_name)
    elif func_name in {'agg', 'aggregate'}:
        return resolve_agg(grp, args, kws, typing_context, target_context)
    else:
        return get_agg_typ(grp, args, func_name, typing_context,
            target_context, kws=kws)


@infer_getattr
class DataframeGroupByAttribute(OverloadedKeyAttributeTemplate):
    key = DataFrameGroupByType
    _attr_set = None

    @bound_function('groupby.agg', no_unliteral=True)
    def resolve_agg(self, grp, args, kws):
        return resolve_gb(grp, args, kws, 'agg', self.context, numba.core.
            registry.cpu_target.target_context)[0]

    @bound_function('groupby.aggregate', no_unliteral=True)
    def resolve_aggregate(self, grp, args, kws):
        return resolve_gb(grp, args, kws, 'agg', self.context, numba.core.
            registry.cpu_target.target_context)[0]

    @bound_function('groupby.sum', no_unliteral=True)
    def resolve_sum(self, grp, args, kws):
        return resolve_gb(grp, args, kws, 'sum', self.context, numba.core.
            registry.cpu_target.target_context)[0]

    @bound_function('groupby.count', no_unliteral=True)
    def resolve_count(self, grp, args, kws):
        return resolve_gb(grp, args, kws, 'count', self.context, numba.core
            .registry.cpu_target.target_context)[0]

    @bound_function('groupby.nunique', no_unliteral=True)
    def resolve_nunique(self, grp, args, kws):
        return resolve_gb(grp, args, kws, 'nunique', self.context, numba.
            core.registry.cpu_target.target_context)[0]

    @bound_function('groupby.median', no_unliteral=True)
    def resolve_median(self, grp, args, kws):
        return resolve_gb(grp, args, kws, 'median', self.context, numba.
            core.registry.cpu_target.target_context)[0]

    @bound_function('groupby.mean', no_unliteral=True)
    def resolve_mean(self, grp, args, kws):
        return resolve_gb(grp, args, kws, 'mean', self.context, numba.core.
            registry.cpu_target.target_context)[0]

    @bound_function('groupby.min', no_unliteral=True)
    def resolve_min(self, grp, args, kws):
        return resolve_gb(grp, args, kws, 'min', self.context, numba.core.
            registry.cpu_target.target_context)[0]

    @bound_function('groupby.max', no_unliteral=True)
    def resolve_max(self, grp, args, kws):
        return resolve_gb(grp, args, kws, 'max', self.context, numba.core.
            registry.cpu_target.target_context)[0]

    @bound_function('groupby.prod', no_unliteral=True)
    def resolve_prod(self, grp, args, kws):
        return resolve_gb(grp, args, kws, 'prod', self.context, numba.core.
            registry.cpu_target.target_context)[0]

    @bound_function('groupby.var', no_unliteral=True)
    def resolve_var(self, grp, args, kws):
        return resolve_gb(grp, args, kws, 'var', self.context, numba.core.
            registry.cpu_target.target_context)[0]

    @bound_function('groupby.std', no_unliteral=True)
    def resolve_std(self, grp, args, kws):
        return resolve_gb(grp, args, kws, 'std', self.context, numba.core.
            registry.cpu_target.target_context)[0]

    @bound_function('groupby.first', no_unliteral=True)
    def resolve_first(self, grp, args, kws):
        return resolve_gb(grp, args, kws, 'first', self.context, numba.core
            .registry.cpu_target.target_context)[0]

    @bound_function('groupby.last', no_unliteral=True)
    def resolve_last(self, grp, args, kws):
        return resolve_gb(grp, args, kws, 'last', self.context, numba.core.
            registry.cpu_target.target_context)[0]

    @bound_function('groupby.idxmin', no_unliteral=True)
    def resolve_idxmin(self, grp, args, kws):
        return resolve_gb(grp, args, kws, 'idxmin', self.context, numba.
            core.registry.cpu_target.target_context)[0]

    @bound_function('groupby.idxmax', no_unliteral=True)
    def resolve_idxmax(self, grp, args, kws):
        return resolve_gb(grp, args, kws, 'idxmax', self.context, numba.
            core.registry.cpu_target.target_context)[0]

    @bound_function('groupby.size', no_unliteral=True)
    def resolve_size(self, grp, args, kws):
        return resolve_gb(grp, args, kws, 'size', self.context, numba.core.
            registry.cpu_target.target_context)[0]

    @bound_function('groupby.cumsum', no_unliteral=True)
    def resolve_cumsum(self, grp, args, kws):
        msg = (
            'Groupby.cumsum() only supports columns of types integer, float, string or liststring'
            )
        return resolve_gb(grp, args, kws, 'cumsum', self.context, numba.
            core.registry.cpu_target.target_context, err_msg=msg)[0]

    @bound_function('groupby.cumprod', no_unliteral=True)
    def resolve_cumprod(self, grp, args, kws):
        msg = (
            'Groupby.cumprod() only supports columns of types integer and float'
            )
        return resolve_gb(grp, args, kws, 'cumprod', self.context, numba.
            core.registry.cpu_target.target_context, err_msg=msg)[0]

    @bound_function('groupby.cummin', no_unliteral=True)
    def resolve_cummin(self, grp, args, kws):
        msg = (
            'Groupby.cummin() only supports columns of types integer, float, string, liststring, date, datetime or timedelta'
            )
        return resolve_gb(grp, args, kws, 'cummin', self.context, numba.
            core.registry.cpu_target.target_context, err_msg=msg)[0]

    @bound_function('groupby.cummax', no_unliteral=True)
    def resolve_cummax(self, grp, args, kws):
        msg = (
            'Groupby.cummax() only supports columns of types integer, float, string, liststring, date, datetime or timedelta'
            )
        return resolve_gb(grp, args, kws, 'cummax', self.context, numba.
            core.registry.cpu_target.target_context, err_msg=msg)[0]

    @bound_function('groupby.shift', no_unliteral=True)
    def resolve_shift(self, grp, args, kws):
        msg = (
            'Column type of list/tuple is not supported in groupby built-in function shift'
            )
        return resolve_gb(grp, args, kws, 'shift', self.context, numba.core
            .registry.cpu_target.target_context, err_msg=msg)[0]

    @bound_function('groupby.pipe', no_unliteral=True)
    def resolve_pipe(self, grp, args, kws):
        return resolve_obj_pipe(self, grp, args, kws, 'GroupBy')

    @bound_function('groupby.transform', no_unliteral=True)
    def resolve_transform(self, grp, args, kws):
        msg = (
            'Groupby.transform() only supports sum, count, min, max, mean, and std operations'
            )
        return resolve_gb(grp, args, kws, 'transform', self.context, numba.
            core.registry.cpu_target.target_context, err_msg=msg)[0]

    @bound_function('groupby.head', no_unliteral=True)
    def resolve_head(self, grp, args, kws):
        msg = 'Unsupported Gropupby head operation.\n'
        return resolve_gb(grp, args, kws, 'head', self.context, numba.core.
            registry.cpu_target.target_context, err_msg=msg)[0]

    @bound_function('groupby.ngroup', no_unliteral=True)
    def resolve_ngroup(self, grp, args, kws):
        msg = 'Unsupported Gropupby head operation.\n'
        return resolve_gb(grp, args, kws, 'ngroup', self.context, numba.
            core.registry.cpu_target.target_context, err_msg=msg)[0]

    @bound_function('groupby.apply', no_unliteral=True)
    def resolve_apply(self, grp, args, kws):
        kws = dict(kws)
        func = args[0] if len(args) > 0 else kws.pop('func', None)
        f_args = tuple(args[1:]) if len(args) > 0 else ()
        utefm__sxevp = _get_groupby_apply_udf_out_type(func, grp, f_args,
            kws, self.context, numba.core.registry.cpu_target.target_context)
        pokp__mbdbp = isinstance(utefm__sxevp, (SeriesType,
            HeterogeneousSeriesType)
            ) and utefm__sxevp.const_info is not None or not isinstance(
            utefm__sxevp, (SeriesType, DataFrameType))
        if pokp__mbdbp:
            out_data = []
            out_columns = []
            out_column_type = []
            if not grp.as_index:
                get_keys_not_as_index(grp, out_columns, out_data,
                    out_column_type)
                nihxg__rpc = NumericIndexType(types.int64, types.none)
            elif len(grp.keys) > 1:
                hmdid__mjxpo = tuple(grp.df_type.column_index[grp.keys[
                    zbu__shl]] for zbu__shl in range(len(grp.keys)))
                fqfkr__mhyqm = tuple(grp.df_type.data[vxx__unp] for
                    vxx__unp in hmdid__mjxpo)
                nihxg__rpc = MultiIndexType(fqfkr__mhyqm, tuple(types.
                    literal(dqwnq__tubmg) for dqwnq__tubmg in grp.keys))
            else:
                vxx__unp = grp.df_type.column_index[grp.keys[0]]
                rlxq__axouu = grp.df_type.data[vxx__unp]
                nihxg__rpc = bodo.hiframes.pd_index_ext.array_type_to_index(
                    rlxq__axouu, types.literal(grp.keys[0]))
            out_data = tuple(out_data)
            out_columns = tuple(out_columns)
        else:
            yeutz__mbt = tuple(grp.df_type.data[grp.df_type.column_index[
                ehvz__kgr]] for ehvz__kgr in grp.keys)
            goxzd__wti = tuple(types.literal(kqw__axez) for kqw__axez in
                grp.keys) + get_index_name_types(utefm__sxevp.index)
            if not grp.as_index:
                yeutz__mbt = types.Array(types.int64, 1, 'C'),
                goxzd__wti = (types.none,) + get_index_name_types(utefm__sxevp
                    .index)
            nihxg__rpc = MultiIndexType(yeutz__mbt +
                get_index_data_arr_types(utefm__sxevp.index), goxzd__wti)
        if pokp__mbdbp:
            if isinstance(utefm__sxevp, HeterogeneousSeriesType):
                hygib__uhdvz, prdna__gda = utefm__sxevp.const_info
                if isinstance(utefm__sxevp.data, bodo.libs.
                    nullable_tuple_ext.NullableTupleType):
                    nztuy__qkbnj = utefm__sxevp.data.tuple_typ.types
                elif isinstance(utefm__sxevp.data, types.Tuple):
                    nztuy__qkbnj = utefm__sxevp.data.types
                snqe__hhpmg = tuple(to_nullable_type(dtype_to_array_type(
                    orgys__zgj)) for orgys__zgj in nztuy__qkbnj)
                exd__xdx = DataFrameType(out_data + snqe__hhpmg, nihxg__rpc,
                    out_columns + prdna__gda)
            elif isinstance(utefm__sxevp, SeriesType):
                socg__ajd, prdna__gda = utefm__sxevp.const_info
                snqe__hhpmg = tuple(to_nullable_type(dtype_to_array_type(
                    utefm__sxevp.dtype)) for hygib__uhdvz in range(socg__ajd))
                exd__xdx = DataFrameType(out_data + snqe__hhpmg, nihxg__rpc,
                    out_columns + prdna__gda)
            else:
                zcye__mvad = get_udf_out_arr_type(utefm__sxevp)
                if not grp.as_index:
                    exd__xdx = DataFrameType(out_data + (zcye__mvad,),
                        nihxg__rpc, out_columns + ('',))
                else:
                    exd__xdx = SeriesType(zcye__mvad.dtype, zcye__mvad,
                        nihxg__rpc, None)
        elif isinstance(utefm__sxevp, SeriesType):
            exd__xdx = SeriesType(utefm__sxevp.dtype, utefm__sxevp.data,
                nihxg__rpc, utefm__sxevp.name_typ)
        else:
            exd__xdx = DataFrameType(utefm__sxevp.data, nihxg__rpc,
                utefm__sxevp.columns)
        iaz__vop = gen_apply_pysig(len(f_args), kws.keys())
        ucst__kidc = (func, *f_args) + tuple(kws.values())
        return signature(exd__xdx, *ucst__kidc).replace(pysig=iaz__vop)

    def generic_resolve(self, grpby, attr):
        if self._is_existing_attr(attr):
            return
        if attr not in grpby.df_type.columns:
            raise_bodo_error(
                f'groupby: invalid attribute {attr} (column not found in dataframe or unsupported function)'
                )
        return DataFrameGroupByType(grpby.df_type, grpby.keys, (attr,),
            grpby.as_index, grpby.dropna, True, True, _num_shuffle_keys=
            grpby._num_shuffle_keys)


def _get_groupby_apply_udf_out_type(func, grp, f_args, kws, typing_context,
    target_context):
    mraqj__pfocq = grp.df_type
    if grp.explicit_select:
        if len(grp.selection) == 1:
            wuw__cxii = grp.selection[0]
            zcye__mvad = mraqj__pfocq.data[mraqj__pfocq.column_index[wuw__cxii]
                ]
            lnumx__uncs = SeriesType(zcye__mvad.dtype, zcye__mvad,
                mraqj__pfocq.index, types.literal(wuw__cxii))
        else:
            lnklq__fqn = tuple(mraqj__pfocq.data[mraqj__pfocq.column_index[
                ehvz__kgr]] for ehvz__kgr in grp.selection)
            lnumx__uncs = DataFrameType(lnklq__fqn, mraqj__pfocq.index,
                tuple(grp.selection))
    else:
        lnumx__uncs = mraqj__pfocq
    rospf__vdb = lnumx__uncs,
    rospf__vdb += tuple(f_args)
    try:
        utefm__sxevp = get_const_func_output_type(func, rospf__vdb, kws,
            typing_context, target_context)
    except Exception as gnpdo__srg:
        raise_bodo_error(get_udf_error_msg('GroupBy.apply()', gnpdo__srg),
            getattr(gnpdo__srg, 'loc', None))
    return utefm__sxevp


def resolve_obj_pipe(self, grp, args, kws, obj_name):
    kws = dict(kws)
    func = args[0] if len(args) > 0 else kws.pop('func', None)
    f_args = tuple(args[1:]) if len(args) > 0 else ()
    rospf__vdb = (grp,) + f_args
    try:
        utefm__sxevp = get_const_func_output_type(func, rospf__vdb, kws,
            self.context, numba.core.registry.cpu_target.target_context, False)
    except Exception as gnpdo__srg:
        raise_bodo_error(get_udf_error_msg(f'{obj_name}.pipe()', gnpdo__srg
            ), getattr(gnpdo__srg, 'loc', None))
    iaz__vop = gen_apply_pysig(len(f_args), kws.keys())
    ucst__kidc = (func, *f_args) + tuple(kws.values())
    return signature(utefm__sxevp, *ucst__kidc).replace(pysig=iaz__vop)


def gen_apply_pysig(n_args, kws):
    oog__scjwj = ', '.join(f'arg{zbu__shl}' for zbu__shl in range(n_args))
    oog__scjwj = oog__scjwj + ', ' if oog__scjwj else ''
    upih__qfi = ', '.join(f"{pykfu__xtxr} = ''" for pykfu__xtxr in kws)
    wdy__txnoh = f'def apply_stub(func, {oog__scjwj}{upih__qfi}):\n'
    wdy__txnoh += '    pass\n'
    dccys__fqisu = {}
    exec(wdy__txnoh, {}, dccys__fqisu)
    mprl__xrqx = dccys__fqisu['apply_stub']
    return numba.core.utils.pysignature(mprl__xrqx)


def crosstab_dummy(index, columns, _pivot_values):
    return 0


@infer_global(crosstab_dummy)
class CrossTabTyper(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        index, columns, _pivot_values = args
        xsdsi__mld = types.Array(types.int64, 1, 'C')
        olgz__iayk = _pivot_values.meta
        vwptf__wveoj = len(olgz__iayk)
        ozel__aiw = bodo.hiframes.pd_index_ext.array_type_to_index(index.
            data, types.StringLiteral('index'))
        csw__uqa = DataFrameType((xsdsi__mld,) * vwptf__wveoj, ozel__aiw,
            tuple(olgz__iayk))
        return signature(csw__uqa, *args)


CrossTabTyper._no_unliteral = True


@lower_builtin(crosstab_dummy, types.VarArg(types.Any))
def lower_crosstab_dummy(context, builder, sig, args):
    return context.get_constant_null(sig.return_type)


def get_group_indices(keys, dropna, _is_parallel):
    return np.arange(len(keys))


@overload(get_group_indices)
def get_group_indices_overload(keys, dropna, _is_parallel):
    wdy__txnoh = 'def impl(keys, dropna, _is_parallel):\n'
    wdy__txnoh += (
        "    ev = bodo.utils.tracing.Event('get_group_indices', _is_parallel)\n"
        )
    wdy__txnoh += '    info_list = [{}]\n'.format(', '.join(
        f'array_to_info(keys[{zbu__shl}])' for zbu__shl in range(len(keys.
        types))))
    wdy__txnoh += '    table = arr_info_list_to_table(info_list)\n'
    wdy__txnoh += '    group_labels = np.empty(len(keys[0]), np.int64)\n'
    wdy__txnoh += '    sort_idx = np.empty(len(keys[0]), np.int64)\n'
    wdy__txnoh += """    ngroups = get_groupby_labels(table, group_labels.ctypes, sort_idx.ctypes, dropna, _is_parallel)
"""
    wdy__txnoh += '    delete_table_decref_arrays(table)\n'
    wdy__txnoh += '    ev.finalize()\n'
    wdy__txnoh += '    return sort_idx, group_labels, ngroups\n'
    dccys__fqisu = {}
    exec(wdy__txnoh, {'bodo': bodo, 'np': np, 'get_groupby_labels':
        get_groupby_labels, 'array_to_info': array_to_info,
        'arr_info_list_to_table': arr_info_list_to_table,
        'delete_table_decref_arrays': delete_table_decref_arrays}, dccys__fqisu
        )
    cbw__zud = dccys__fqisu['impl']
    return cbw__zud


@numba.njit(no_cpython_wrapper=True)
def generate_slices(labels, ngroups):
    hkn__wvvot = len(labels)
    igh__unqh = np.zeros(ngroups, dtype=np.int64)
    jyk__wutrf = np.zeros(ngroups, dtype=np.int64)
    trxr__djl = 0
    dzs__rzi = 0
    for zbu__shl in range(hkn__wvvot):
        gwot__nva = labels[zbu__shl]
        if gwot__nva < 0:
            trxr__djl += 1
        else:
            dzs__rzi += 1
            if zbu__shl == hkn__wvvot - 1 or gwot__nva != labels[zbu__shl + 1]:
                igh__unqh[gwot__nva] = trxr__djl
                jyk__wutrf[gwot__nva] = trxr__djl + dzs__rzi
                trxr__djl += dzs__rzi
                dzs__rzi = 0
    return igh__unqh, jyk__wutrf


def shuffle_dataframe(df, keys, _is_parallel):
    return df, keys, _is_parallel


@overload(shuffle_dataframe, prefer_literal=True)
def overload_shuffle_dataframe(df, keys, _is_parallel):
    cbw__zud, hygib__uhdvz = gen_shuffle_dataframe(df, keys, _is_parallel)
    return cbw__zud


def gen_shuffle_dataframe(df, keys, _is_parallel):
    socg__ajd = len(df.columns)
    lxxea__hjbn = len(keys.types)
    assert is_overload_constant_bool(_is_parallel
        ), 'shuffle_dataframe: _is_parallel is not a constant'
    wdy__txnoh = 'def impl(df, keys, _is_parallel):\n'
    if is_overload_false(_is_parallel):
        wdy__txnoh += '  return df, keys, get_null_shuffle_info()\n'
        dccys__fqisu = {}
        exec(wdy__txnoh, {'get_null_shuffle_info': get_null_shuffle_info},
            dccys__fqisu)
        cbw__zud = dccys__fqisu['impl']
        return cbw__zud
    for zbu__shl in range(socg__ajd):
        wdy__txnoh += f"""  in_arr{zbu__shl} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {zbu__shl})
"""
    wdy__txnoh += f"""  in_index_arr = bodo.utils.conversion.index_to_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df))
"""
    wdy__txnoh += '  info_list = [{}, {}, {}]\n'.format(', '.join(
        f'array_to_info(keys[{zbu__shl}])' for zbu__shl in range(
        lxxea__hjbn)), ', '.join(f'array_to_info(in_arr{zbu__shl})' for
        zbu__shl in range(socg__ajd)), 'array_to_info(in_index_arr)')
    wdy__txnoh += '  table = arr_info_list_to_table(info_list)\n'
    wdy__txnoh += (
        f'  out_table = shuffle_table(table, {lxxea__hjbn}, _is_parallel, 1)\n'
        )
    for zbu__shl in range(lxxea__hjbn):
        wdy__txnoh += f"""  out_key{zbu__shl} = info_to_array(info_from_table(out_table, {zbu__shl}), keys{zbu__shl}_typ)
"""
    for zbu__shl in range(socg__ajd):
        wdy__txnoh += f"""  out_arr{zbu__shl} = info_to_array(info_from_table(out_table, {zbu__shl + lxxea__hjbn}), in_arr{zbu__shl}_typ)
"""
    wdy__txnoh += f"""  out_arr_index = info_to_array(info_from_table(out_table, {lxxea__hjbn + socg__ajd}), ind_arr_typ)
"""
    wdy__txnoh += '  shuffle_info = get_shuffle_info(out_table)\n'
    wdy__txnoh += '  delete_table(out_table)\n'
    wdy__txnoh += '  delete_table(table)\n'
    out_data = ', '.join(f'out_arr{zbu__shl}' for zbu__shl in range(socg__ajd))
    wdy__txnoh += (
        '  out_index = bodo.utils.conversion.index_from_array(out_arr_index)\n'
        )
    wdy__txnoh += f"""  out_df = bodo.hiframes.pd_dataframe_ext.init_dataframe(({out_data},), out_index, __col_name_meta_value_df_shuffle)
"""
    wdy__txnoh += '  return out_df, ({},), shuffle_info\n'.format(', '.join
        (f'out_key{zbu__shl}' for zbu__shl in range(lxxea__hjbn)))
    mkab__eoij = {'bodo': bodo, 'array_to_info': array_to_info,
        'arr_info_list_to_table': arr_info_list_to_table, 'shuffle_table':
        shuffle_table, 'info_from_table': info_from_table, 'info_to_array':
        info_to_array, 'delete_table': delete_table, 'get_shuffle_info':
        get_shuffle_info, '__col_name_meta_value_df_shuffle':
        ColNamesMetaType(df.columns), 'ind_arr_typ': types.Array(types.
        int64, 1, 'C') if isinstance(df.index, RangeIndexType) else df.
        index.data}
    mkab__eoij.update({f'keys{zbu__shl}_typ': keys.types[zbu__shl] for
        zbu__shl in range(lxxea__hjbn)})
    mkab__eoij.update({f'in_arr{zbu__shl}_typ': df.data[zbu__shl] for
        zbu__shl in range(socg__ajd)})
    dccys__fqisu = {}
    exec(wdy__txnoh, mkab__eoij, dccys__fqisu)
    cbw__zud = dccys__fqisu['impl']
    return cbw__zud, mkab__eoij


def reverse_shuffle(data, shuffle_info):
    return data


@overload(reverse_shuffle)
def overload_reverse_shuffle(data, shuffle_info):
    if isinstance(data, bodo.hiframes.pd_multi_index_ext.MultiIndexType):
        jjn__hyf = len(data.array_types)
        wdy__txnoh = 'def impl(data, shuffle_info):\n'
        wdy__txnoh += '  info_list = [{}]\n'.format(', '.join(
            f'array_to_info(data._data[{zbu__shl}])' for zbu__shl in range(
            jjn__hyf)))
        wdy__txnoh += '  table = arr_info_list_to_table(info_list)\n'
        wdy__txnoh += (
            '  out_table = reverse_shuffle_table(table, shuffle_info)\n')
        for zbu__shl in range(jjn__hyf):
            wdy__txnoh += f"""  out_arr{zbu__shl} = info_to_array(info_from_table(out_table, {zbu__shl}), data._data[{zbu__shl}])
"""
        wdy__txnoh += '  delete_table(out_table)\n'
        wdy__txnoh += '  delete_table(table)\n'
        wdy__txnoh += (
            '  return init_multi_index(({},), data._names, data._name)\n'.
            format(', '.join(f'out_arr{zbu__shl}' for zbu__shl in range(
            jjn__hyf))))
        dccys__fqisu = {}
        exec(wdy__txnoh, {'bodo': bodo, 'array_to_info': array_to_info,
            'arr_info_list_to_table': arr_info_list_to_table,
            'reverse_shuffle_table': reverse_shuffle_table,
            'info_from_table': info_from_table, 'info_to_array':
            info_to_array, 'delete_table': delete_table, 'init_multi_index':
            bodo.hiframes.pd_multi_index_ext.init_multi_index}, dccys__fqisu)
        cbw__zud = dccys__fqisu['impl']
        return cbw__zud
    if bodo.hiframes.pd_index_ext.is_index_type(data):

        def impl_index(data, shuffle_info):
            xjvao__rdybj = bodo.utils.conversion.index_to_array(data)
            cfib__utnb = reverse_shuffle(xjvao__rdybj, shuffle_info)
            return bodo.utils.conversion.index_from_array(cfib__utnb)
        return impl_index

    def impl_arr(data, shuffle_info):
        amo__jyy = [array_to_info(data)]
        bmu__ufgaw = arr_info_list_to_table(amo__jyy)
        yhy__zkn = reverse_shuffle_table(bmu__ufgaw, shuffle_info)
        cfib__utnb = info_to_array(info_from_table(yhy__zkn, 0), data)
        delete_table(yhy__zkn)
        delete_table(bmu__ufgaw)
        return cfib__utnb
    return impl_arr


@overload_method(DataFrameGroupByType, 'value_counts', inline='always',
    no_unliteral=True)
def groupby_value_counts(grp, normalize=False, sort=True, ascending=False,
    bins=None, dropna=True):
    ivxgr__hbn = dict(normalize=normalize, sort=sort, bins=bins, dropna=dropna)
    xoy__sidby = dict(normalize=False, sort=True, bins=None, dropna=True)
    check_unsupported_args('Groupby.value_counts', ivxgr__hbn, xoy__sidby,
        package_name='pandas', module_name='GroupBy')
    if len(grp.selection) > 1 or not grp.as_index:
        raise BodoError(
            "'DataFrameGroupBy' object has no attribute 'value_counts'")
    if not is_overload_constant_bool(ascending):
        raise BodoError(
            'Groupby.value_counts() ascending must be a constant boolean')
    srx__xss = get_overload_const_bool(ascending)
    dmmvd__uoou = grp.selection[0]
    wdy__txnoh = f"""def impl(grp, normalize=False, sort=True, ascending=False, bins=None, dropna=True):
"""
    ounqp__jxut = (
        f"lambda S: S.value_counts(ascending={srx__xss}, _index_name='{dmmvd__uoou}')"
        )
    wdy__txnoh += f'    return grp.apply({ounqp__jxut})\n'
    dccys__fqisu = {}
    exec(wdy__txnoh, {'bodo': bodo}, dccys__fqisu)
    cbw__zud = dccys__fqisu['impl']
    return cbw__zud


groupby_unsupported_attr = {'groups', 'indices'}
groupby_unsupported = {'__iter__', 'get_group', 'all', 'any', 'bfill',
    'backfill', 'cumcount', 'cummax', 'cummin', 'cumprod', 'ffill', 'nth',
    'ohlc', 'pad', 'rank', 'pct_change', 'sem', 'tail', 'corr', 'cov',
    'describe', 'diff', 'fillna', 'filter', 'hist', 'mad', 'plot',
    'quantile', 'resample', 'sample', 'skew', 'take', 'tshift'}
series_only_unsupported_attrs = {'is_monotonic_increasing',
    'is_monotonic_decreasing'}
series_only_unsupported = {'nlargest', 'nsmallest', 'unique'}
dataframe_only_unsupported = {'corrwith', 'boxplot'}


def _install_groupby_unsupported():
    for lpwr__mqd in groupby_unsupported_attr:
        overload_attribute(DataFrameGroupByType, lpwr__mqd, no_unliteral=True)(
            create_unsupported_overload(f'DataFrameGroupBy.{lpwr__mqd}'))
    for lpwr__mqd in groupby_unsupported:
        overload_method(DataFrameGroupByType, lpwr__mqd, no_unliteral=True)(
            create_unsupported_overload(f'DataFrameGroupBy.{lpwr__mqd}'))
    for lpwr__mqd in series_only_unsupported_attrs:
        overload_attribute(DataFrameGroupByType, lpwr__mqd, no_unliteral=True)(
            create_unsupported_overload(f'SeriesGroupBy.{lpwr__mqd}'))
    for lpwr__mqd in series_only_unsupported:
        overload_method(DataFrameGroupByType, lpwr__mqd, no_unliteral=True)(
            create_unsupported_overload(f'SeriesGroupBy.{lpwr__mqd}'))
    for lpwr__mqd in dataframe_only_unsupported:
        overload_method(DataFrameGroupByType, lpwr__mqd, no_unliteral=True)(
            create_unsupported_overload(f'DataFrameGroupBy.{lpwr__mqd}'))


_install_groupby_unsupported()
