"""
Implement pd.DataFrame typing and data model handling.
"""
import json
import operator
import time
from functools import cached_property
from typing import Optional, Sequence
import llvmlite.binding as ll
import numba
import numpy as np
import pandas as pd
import pyarrow as pa
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.imputils import impl_ret_borrowed, lower_constant
from numba.core.typing.templates import AbstractTemplate, bound_function, infer_global, signature
from numba.cpython.listobj import ListInstance
from numba.extending import infer_getattr, intrinsic, lower_builtin, lower_cast, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_model
from numba.parfors.array_analysis import ArrayAnalysis
import bodo
from bodo.hiframes.datetime_date_ext import datetime_date_array_type
from bodo.hiframes.pd_categorical_ext import CategoricalArrayType
from bodo.hiframes.pd_index_ext import HeterogeneousIndexType, NumericIndexType, RangeIndexType, is_pd_index_type
from bodo.hiframes.pd_multi_index_ext import MultiIndexType
from bodo.hiframes.pd_series_ext import HeterogeneousSeriesType, SeriesType
from bodo.hiframes.series_indexing import SeriesIlocType
from bodo.hiframes.table import Table, TableType, decode_if_dict_table, get_table_data, set_table_data_codegen
from bodo.hiframes.time_ext import TimeArrayType
from bodo.io import json_cpp
from bodo.libs.array import arr_info_list_to_table, array_to_info, delete_info_decref_array, delete_table, delete_table_decref_arrays, info_from_table, info_to_array, py_table_to_cpp_table, shuffle_table
from bodo.libs.array_item_arr_ext import ArrayItemArrayType
from bodo.libs.binary_arr_ext import binary_array_type
from bodo.libs.bool_arr_ext import boolean_array
from bodo.libs.decimal_arr_ext import DecimalArrayType
from bodo.libs.int_arr_ext import IntegerArrayType
from bodo.libs.str_arr_ext import str_arr_from_sequence
from bodo.libs.str_ext import string_type, unicode_to_utf8
from bodo.libs.struct_arr_ext import StructArrayType
from bodo.utils import tracing
from bodo.utils.cg_helpers import is_ll_eq
from bodo.utils.conversion import fix_arr_dtype, index_to_array
from bodo.utils.templates import OverloadedKeyAttributeTemplate
from bodo.utils.transform import get_const_func_output_type
from bodo.utils.typing import BodoError, BodoWarning, ColNamesMetaType, check_unsupported_args, create_unsupported_overload, decode_if_dict_array, dtype_to_array_type, get_index_data_arr_types, get_literal_value, get_overload_const, get_overload_const_bool, get_overload_const_int, get_overload_const_list, get_overload_const_str, get_udf_error_msg, get_udf_out_arr_type, is_heterogeneous_tuple_type, is_iterable_type, is_literal_type, is_overload_bool, is_overload_constant_bool, is_overload_constant_int, is_overload_constant_str, is_overload_false, is_overload_int, is_overload_none, is_overload_true, is_str_arr_type, is_tuple_like_type, raise_bodo_error, to_nullable_type, to_str_arr_if_dict_array
from bodo.utils.utils import is_null_pointer
_json_write = types.ExternalFunction('json_write', types.void(types.voidptr,
    types.voidptr, types.int64, types.int64, types.bool_, types.bool_,
    types.voidptr, types.voidptr))
ll.add_symbol('json_write', json_cpp.json_write)


class DataFrameType(types.ArrayCompatible):
    ndim = 2

    def __init__(self, data: Optional[Sequence['types.Array']]=None, index=
        None, columns: Optional[Sequence[str]]=None, dist=None,
        is_table_format=False):
        from bodo.transforms.distributed_analysis import Distribution
        self.data = data
        if index is None:
            index = RangeIndexType(types.none)
        self.index = index
        self.columns = columns
        dist = Distribution.OneD_Var if dist is None else dist
        self.dist = dist
        self.is_table_format = is_table_format
        if columns is None:
            assert is_table_format, 'Determining columns at runtime is only supported for DataFrame with table format'
            self.table_type = TableType(tuple(data[:-1]), True)
        else:
            self.table_type = TableType(data) if is_table_format else None
        super(DataFrameType, self).__init__(name=
            f'dataframe({data}, {index}, {columns}, {dist}, {is_table_format}, {self.has_runtime_cols})'
            )

    def __str__(self):
        if not self.has_runtime_cols and len(self.columns) > 20:
            nck__fgplr = f'{len(self.data)} columns of types {set(self.data)}'
            gehxr__tklm = (
                f"('{self.columns[0]}', '{self.columns[1]}', ..., '{self.columns[-1]}')"
                )
            vxzsj__jmtq = str(hash(super().__str__()))
            return (
                f'dataframe({nck__fgplr}, {self.index}, {gehxr__tklm}, {self.dist}, {self.is_table_format}, {self.has_runtime_cols}, key_hash={vxzsj__jmtq})'
                )
        return super().__str__()

    def copy(self, data=None, index=None, columns=None, dist=None,
        is_table_format=None):
        if data is None:
            data = self.data
        if columns is None:
            columns = self.columns
        if index is None:
            index = self.index
        if dist is None:
            dist = self.dist
        if is_table_format is None:
            is_table_format = self.is_table_format
        return DataFrameType(data, index, columns, dist, is_table_format)

    @property
    def has_runtime_cols(self):
        return self.columns is None

    @cached_property
    def column_index(self):
        return {ojaae__obyr: i for i, ojaae__obyr in enumerate(self.columns)}

    @property
    def runtime_colname_typ(self):
        return self.data[-1] if self.has_runtime_cols else None

    @property
    def runtime_data_types(self):
        return self.data[:-1] if self.has_runtime_cols else self.data

    @property
    def as_array(self):
        return types.Array(types.undefined, 2, 'C')

    @property
    def key(self):
        return (self.data, self.index, self.columns, self.dist, self.
            is_table_format)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)

    def unify(self, typingctx, other):
        from bodo.transforms.distributed_analysis import Distribution
        if (isinstance(other, DataFrameType) and len(other.data) == len(
            self.data) and other.columns == self.columns and other.
            has_runtime_cols == self.has_runtime_cols):
            zoh__azm = (self.index if self.index == other.index else self.
                index.unify(typingctx, other.index))
            data = tuple(qpf__mjz.unify(typingctx, oljme__jtcl) if qpf__mjz !=
                oljme__jtcl else qpf__mjz for qpf__mjz, oljme__jtcl in zip(
                self.data, other.data))
            dist = Distribution(min(self.dist.value, other.dist.value))
            if zoh__azm is not None and None not in data:
                return DataFrameType(data, zoh__azm, self.columns, dist,
                    self.is_table_format)
        if isinstance(other, DataFrameType) and len(self.data
            ) == 0 and not self.has_runtime_cols:
            return other

    def can_convert_to(self, typingctx, other):
        from numba.core.typeconv import Conversion
        if (isinstance(other, DataFrameType) and self.data == other.data and
            self.index == other.index and self.columns == other.columns and
            self.dist != other.dist and self.has_runtime_cols == other.
            has_runtime_cols):
            return Conversion.safe

    def is_precise(self):
        return all(qpf__mjz.is_precise() for qpf__mjz in self.data
            ) and self.index.is_precise()

    def replace_col_type(self, col_name, new_type):
        if col_name not in self.columns:
            raise ValueError(
                f"DataFrameType.replace_col_type replaced column must be found in the DataFrameType. '{col_name}' not found in DataFrameType with columns {self.columns}"
                )
        ofgb__yst = self.columns.index(col_name)
        jplms__symdn = tuple(list(self.data[:ofgb__yst]) + [new_type] +
            list(self.data[ofgb__yst + 1:]))
        return DataFrameType(jplms__symdn, self.index, self.columns, self.
            dist, self.is_table_format)


def check_runtime_cols_unsupported(df, func_name):
    if isinstance(df, DataFrameType) and df.has_runtime_cols:
        raise BodoError(
            f'{func_name} on DataFrames with columns determined at runtime is not yet supported. Please return the DataFrame to regular Python to update typing information.'
            )


class DataFramePayloadType(types.Type):

    def __init__(self, df_type):
        self.df_type = df_type
        super(DataFramePayloadType, self).__init__(name=
            f'DataFramePayloadType({df_type})')

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


@register_model(DataFramePayloadType)
class DataFramePayloadModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        data_typ = types.Tuple(fe_type.df_type.data)
        if fe_type.df_type.is_table_format:
            data_typ = types.Tuple([fe_type.df_type.table_type])
        yijzz__ypj = [('data', data_typ), ('index', fe_type.df_type.index),
            ('parent', types.pyobject)]
        if fe_type.df_type.has_runtime_cols:
            yijzz__ypj.append(('columns', fe_type.df_type.runtime_colname_typ))
        super(DataFramePayloadModel, self).__init__(dmm, fe_type, yijzz__ypj)


@register_model(DataFrameType)
class DataFrameModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        payload_type = DataFramePayloadType(fe_type)
        yijzz__ypj = [('meminfo', types.MemInfoPointer(payload_type)), (
            'parent', types.pyobject)]
        super(DataFrameModel, self).__init__(dmm, fe_type, yijzz__ypj)


make_attribute_wrapper(DataFrameType, 'meminfo', '_meminfo')


@infer_getattr
class DataFrameAttribute(OverloadedKeyAttributeTemplate):
    key = DataFrameType

    def resolve_shape(self, df):
        return types.Tuple([types.int64, types.int64])

    @bound_function('df.head')
    def resolve_head(self, df, args, kws):
        func_name = 'DataFrame.head'
        check_runtime_cols_unsupported(df, f'{func_name}()')
        jkysm__ntwqv = 'n',
        xgm__klqg = {'n': 5}
        zvto__sck, euzxq__zjvad = bodo.utils.typing.fold_typing_args(func_name,
            args, kws, jkysm__ntwqv, xgm__klqg)
        afzsi__ckcai = euzxq__zjvad[0]
        if not is_overload_int(afzsi__ckcai):
            raise BodoError(f"{func_name}(): 'n' must be an Integer")
        ytk__bvqt = df.copy()
        return ytk__bvqt(*euzxq__zjvad).replace(pysig=zvto__sck)

    @bound_function('df.corr')
    def resolve_corr(self, df, args, kws):
        func_name = 'DataFrame.corr'
        check_runtime_cols_unsupported(df, f'{func_name}()')
        teevc__dbxr = (df,) + args
        jkysm__ntwqv = 'df', 'method', 'min_periods'
        xgm__klqg = {'method': 'pearson', 'min_periods': 1}
        pdc__nzfg = 'method',
        zvto__sck, euzxq__zjvad = bodo.utils.typing.fold_typing_args(func_name,
            teevc__dbxr, kws, jkysm__ntwqv, xgm__klqg, pdc__nzfg)
        quh__qdgs = euzxq__zjvad[2]
        if not is_overload_int(quh__qdgs):
            raise BodoError(f"{func_name}(): 'min_periods' must be an Integer")
        jyv__diwt = []
        jymx__gzadm = []
        for ojaae__obyr, ebx__yqdmk in zip(df.columns, df.data):
            if bodo.utils.typing._is_pandas_numeric_dtype(ebx__yqdmk.dtype):
                jyv__diwt.append(ojaae__obyr)
                jymx__gzadm.append(types.Array(types.float64, 1, 'A'))
        if len(jyv__diwt) == 0:
            raise_bodo_error('DataFrame.corr(): requires non-empty dataframe')
        jymx__gzadm = tuple(jymx__gzadm)
        jyv__diwt = tuple(jyv__diwt)
        index_typ = bodo.utils.typing.type_col_to_index(jyv__diwt)
        ytk__bvqt = DataFrameType(jymx__gzadm, index_typ, jyv__diwt)
        return ytk__bvqt(*euzxq__zjvad).replace(pysig=zvto__sck)

    @bound_function('df.pipe', no_unliteral=True)
    def resolve_pipe(self, df, args, kws):
        check_runtime_cols_unsupported(df, 'DataFrame.pipe()')
        return bodo.hiframes.pd_groupby_ext.resolve_obj_pipe(self, df, args,
            kws, 'DataFrame')

    @bound_function('df.apply', no_unliteral=True)
    def resolve_apply(self, df, args, kws):
        check_runtime_cols_unsupported(df, 'DataFrame.apply()')
        kws = dict(kws)
        elvp__usq = args[0] if len(args) > 0 else kws.pop('func', None)
        axis = args[1] if len(args) > 1 else kws.pop('axis', types.literal(0))
        iarph__fzf = args[2] if len(args) > 2 else kws.pop('raw', types.
            literal(False))
        ahn__jdik = args[3] if len(args) > 3 else kws.pop('result_type',
            types.none)
        nieq__ekqw = args[4] if len(args) > 4 else kws.pop('args', types.
            Tuple([]))
        kohq__aknrl = dict(raw=iarph__fzf, result_type=ahn__jdik)
        kas__ugyhf = dict(raw=False, result_type=None)
        check_unsupported_args('Dataframe.apply', kohq__aknrl, kas__ugyhf,
            package_name='pandas', module_name='DataFrame')
        bgsz__inci = True
        if types.unliteral(elvp__usq) == types.unicode_type:
            if not is_overload_constant_str(elvp__usq):
                raise BodoError(
                    f'DataFrame.apply(): string argument (for builtins) must be a compile time constant'
                    )
            bgsz__inci = False
        if not is_overload_constant_int(axis):
            raise BodoError(
                'Dataframe.apply(): axis argument must be a compile time constant.'
                )
        croxi__zgwxe = get_overload_const_int(axis)
        if bgsz__inci and croxi__zgwxe != 1:
            raise BodoError(
                'Dataframe.apply(): only axis=1 supported for user-defined functions'
                )
        elif croxi__zgwxe not in (0, 1):
            raise BodoError('Dataframe.apply(): axis must be either 0 or 1')
        imu__lec = []
        for arr_typ in df.data:
            zsf__cba = SeriesType(arr_typ.dtype, arr_typ, df.index, string_type
                )
            ghxbg__irz = self.context.resolve_function_type(operator.
                getitem, (SeriesIlocType(zsf__cba), types.int64), {}
                ).return_type
            imu__lec.append(ghxbg__irz)
        agda__ohou = types.none
        xyr__ota = HeterogeneousIndexType(types.BaseTuple.from_types(tuple(
            types.literal(ojaae__obyr) for ojaae__obyr in df.columns)), None)
        ovk__pjisy = types.BaseTuple.from_types(imu__lec)
        mhm__alz = types.Tuple([types.bool_] * len(ovk__pjisy))
        gepz__ckm = bodo.NullableTupleType(ovk__pjisy, mhm__alz)
        visfm__zhv = df.index.dtype
        bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df.index,
            'DataFrame.apply()')
        if visfm__zhv == types.NPDatetime('ns'):
            visfm__zhv = bodo.pd_timestamp_tz_naive_type
        if visfm__zhv == types.NPTimedelta('ns'):
            visfm__zhv = bodo.pd_timedelta_type
        if is_heterogeneous_tuple_type(ovk__pjisy):
            ppc__quo = HeterogeneousSeriesType(gepz__ckm, xyr__ota, visfm__zhv)
        else:
            ppc__quo = SeriesType(ovk__pjisy.dtype, gepz__ckm, xyr__ota,
                visfm__zhv)
        devj__alx = ppc__quo,
        if nieq__ekqw is not None:
            devj__alx += tuple(nieq__ekqw.types)
        try:
            if not bgsz__inci:
                fkpue__goozy = bodo.utils.transform.get_udf_str_return_type(df,
                    get_overload_const_str(elvp__usq), self.context,
                    'DataFrame.apply', axis if croxi__zgwxe == 1 else None)
            else:
                fkpue__goozy = get_const_func_output_type(elvp__usq,
                    devj__alx, kws, self.context, numba.core.registry.
                    cpu_target.target_context)
        except Exception as qva__qscug:
            raise_bodo_error(get_udf_error_msg('DataFrame.apply()', qva__qscug)
                )
        if bgsz__inci:
            if not (is_overload_constant_int(axis) and 
                get_overload_const_int(axis) == 1):
                raise BodoError(
                    'Dataframe.apply(): only user-defined functions with axis=1 supported'
                    )
            if isinstance(fkpue__goozy, (SeriesType, HeterogeneousSeriesType)
                ) and fkpue__goozy.const_info is None:
                raise BodoError(
                    'Invalid Series output in UDF (Series with constant length and constant Index value expected)'
                    )
            if isinstance(fkpue__goozy, HeterogeneousSeriesType):
                zvl__tupjy, apgmu__vpch = fkpue__goozy.const_info
                if isinstance(fkpue__goozy.data, bodo.libs.
                    nullable_tuple_ext.NullableTupleType):
                    wyt__auqqh = fkpue__goozy.data.tuple_typ.types
                elif isinstance(fkpue__goozy.data, types.Tuple):
                    wyt__auqqh = fkpue__goozy.data.types
                else:
                    raise_bodo_error(
                        'df.apply(): Unexpected Series return type for Heterogeneous data'
                        )
                wqxwu__mmrwy = tuple(to_nullable_type(dtype_to_array_type(
                    vsqe__ksi)) for vsqe__ksi in wyt__auqqh)
                ddrrb__slxl = DataFrameType(wqxwu__mmrwy, df.index, apgmu__vpch
                    )
            elif isinstance(fkpue__goozy, SeriesType):
                emoh__wwh, apgmu__vpch = fkpue__goozy.const_info
                wqxwu__mmrwy = tuple(to_nullable_type(dtype_to_array_type(
                    fkpue__goozy.dtype)) for zvl__tupjy in range(emoh__wwh))
                ddrrb__slxl = DataFrameType(wqxwu__mmrwy, df.index, apgmu__vpch
                    )
            else:
                mdb__xjfr = get_udf_out_arr_type(fkpue__goozy)
                ddrrb__slxl = SeriesType(mdb__xjfr.dtype, mdb__xjfr, df.
                    index, None)
        else:
            ddrrb__slxl = fkpue__goozy
        azyxv__nubvg = ', '.join("{} = ''".format(qpf__mjz) for qpf__mjz in
            kws.keys())
        llvq__jarb = f"""def apply_stub(func, axis=0, raw=False, result_type=None, args=(), {azyxv__nubvg}):
"""
        llvq__jarb += '    pass\n'
        nrsh__tdq = {}
        exec(llvq__jarb, {}, nrsh__tdq)
        uwybi__mfn = nrsh__tdq['apply_stub']
        zvto__sck = numba.core.utils.pysignature(uwybi__mfn)
        oso__cvupv = (elvp__usq, axis, iarph__fzf, ahn__jdik, nieq__ekqw
            ) + tuple(kws.values())
        return signature(ddrrb__slxl, *oso__cvupv).replace(pysig=zvto__sck)

    @bound_function('df.plot', no_unliteral=True)
    def resolve_plot(self, df, args, kws):
        func_name = 'DataFrame.plot'
        check_runtime_cols_unsupported(df, f'{func_name}()')
        jkysm__ntwqv = ('x', 'y', 'kind', 'figsize', 'ax', 'subplots',
            'sharex', 'sharey', 'layout', 'use_index', 'title', 'grid',
            'legend', 'style', 'logx', 'logy', 'loglog', 'xticks', 'yticks',
            'xlim', 'ylim', 'rot', 'fontsize', 'colormap', 'table', 'yerr',
            'xerr', 'secondary_y', 'sort_columns', 'xlabel', 'ylabel',
            'position', 'stacked', 'mark_right', 'include_bool', 'backend')
        xgm__klqg = {'x': None, 'y': None, 'kind': 'line', 'figsize': None,
            'ax': None, 'subplots': False, 'sharex': None, 'sharey': False,
            'layout': None, 'use_index': True, 'title': None, 'grid': None,
            'legend': True, 'style': None, 'logx': False, 'logy': False,
            'loglog': False, 'xticks': None, 'yticks': None, 'xlim': None,
            'ylim': None, 'rot': None, 'fontsize': None, 'colormap': None,
            'table': False, 'yerr': None, 'xerr': None, 'secondary_y': 
            False, 'sort_columns': False, 'xlabel': None, 'ylabel': None,
            'position': 0.5, 'stacked': False, 'mark_right': True,
            'include_bool': False, 'backend': None}
        pdc__nzfg = ('subplots', 'sharex', 'sharey', 'layout', 'use_index',
            'grid', 'style', 'logx', 'logy', 'loglog', 'xlim', 'ylim',
            'rot', 'colormap', 'table', 'yerr', 'xerr', 'sort_columns',
            'secondary_y', 'colorbar', 'position', 'stacked', 'mark_right',
            'include_bool', 'backend')
        zvto__sck, euzxq__zjvad = bodo.utils.typing.fold_typing_args(func_name,
            args, kws, jkysm__ntwqv, xgm__klqg, pdc__nzfg)
        bpde__lhfj = euzxq__zjvad[2]
        if not is_overload_constant_str(bpde__lhfj):
            raise BodoError(
                f"{func_name}: kind must be a constant string and one of ('line', 'scatter')."
                )
        pgi__imye = euzxq__zjvad[0]
        if not is_overload_none(pgi__imye) and not (is_overload_int(
            pgi__imye) or is_overload_constant_str(pgi__imye)):
            raise BodoError(
                f'{func_name}: x must be a constant column name, constant integer, or None.'
                )
        if is_overload_constant_str(pgi__imye):
            hsy__qhya = get_overload_const_str(pgi__imye)
            if hsy__qhya not in df.columns:
                raise BodoError(f'{func_name}: {hsy__qhya} column not found.')
        elif is_overload_int(pgi__imye):
            tynrt__sbvyh = get_overload_const_int(pgi__imye)
            if tynrt__sbvyh > len(df.columns):
                raise BodoError(
                    f'{func_name}: x: {tynrt__sbvyh} is out of bounds for axis 0 with size {len(df.columns)}'
                    )
            pgi__imye = df.columns[pgi__imye]
        briil__kxwy = euzxq__zjvad[1]
        if not is_overload_none(briil__kxwy) and not (is_overload_int(
            briil__kxwy) or is_overload_constant_str(briil__kxwy)):
            raise BodoError(
                'df.plot(): y must be a constant column name, constant integer, or None.'
                )
        if is_overload_constant_str(briil__kxwy):
            bzyzf__vkgf = get_overload_const_str(briil__kxwy)
            if bzyzf__vkgf not in df.columns:
                raise BodoError(f'{func_name}: {bzyzf__vkgf} column not found.'
                    )
        elif is_overload_int(briil__kxwy):
            fox__jjknj = get_overload_const_int(briil__kxwy)
            if fox__jjknj > len(df.columns):
                raise BodoError(
                    f'{func_name}: y: {fox__jjknj} is out of bounds for axis 0 with size {len(df.columns)}'
                    )
            briil__kxwy = df.columns[briil__kxwy]
        gml__qip = euzxq__zjvad[3]
        if not is_overload_none(gml__qip) and not is_tuple_like_type(gml__qip):
            raise BodoError(
                f'{func_name}: figsize must be a constant numeric tuple (width, height) or None.'
                )
        pfeb__zuqud = euzxq__zjvad[10]
        if not is_overload_none(pfeb__zuqud) and not is_overload_constant_str(
            pfeb__zuqud):
            raise BodoError(
                f'{func_name}: title must be a constant string or None.')
        sfq__duyab = euzxq__zjvad[12]
        if not is_overload_bool(sfq__duyab):
            raise BodoError(f'{func_name}: legend must be a boolean type.')
        rgg__kbqb = euzxq__zjvad[17]
        if not is_overload_none(rgg__kbqb) and not is_tuple_like_type(rgg__kbqb
            ):
            raise BodoError(
                f'{func_name}: xticks must be a constant tuple or None.')
        eto__xkxz = euzxq__zjvad[18]
        if not is_overload_none(eto__xkxz) and not is_tuple_like_type(eto__xkxz
            ):
            raise BodoError(
                f'{func_name}: yticks must be a constant tuple or None.')
        izojh__ofrit = euzxq__zjvad[22]
        if not is_overload_none(izojh__ofrit) and not is_overload_int(
            izojh__ofrit):
            raise BodoError(
                f'{func_name}: fontsize must be an integer or None.')
        guxr__xokp = euzxq__zjvad[29]
        if not is_overload_none(guxr__xokp) and not is_overload_constant_str(
            guxr__xokp):
            raise BodoError(
                f'{func_name}: xlabel must be a constant string or None.')
        ilbcw__vrzmx = euzxq__zjvad[30]
        if not is_overload_none(ilbcw__vrzmx) and not is_overload_constant_str(
            ilbcw__vrzmx):
            raise BodoError(
                f'{func_name}: ylabel must be a constant string or None.')
        sze__fqqn = types.List(types.mpl_line_2d_type)
        bpde__lhfj = get_overload_const_str(bpde__lhfj)
        if bpde__lhfj == 'scatter':
            if is_overload_none(pgi__imye) and is_overload_none(briil__kxwy):
                raise BodoError(
                    f'{func_name}: {bpde__lhfj} requires an x and y column.')
            elif is_overload_none(pgi__imye):
                raise BodoError(
                    f'{func_name}: {bpde__lhfj} x column is missing.')
            elif is_overload_none(briil__kxwy):
                raise BodoError(
                    f'{func_name}: {bpde__lhfj} y column is missing.')
            sze__fqqn = types.mpl_path_collection_type
        elif bpde__lhfj != 'line':
            raise BodoError(f'{func_name}: {bpde__lhfj} plot is not supported.'
                )
        return signature(sze__fqqn, *euzxq__zjvad).replace(pysig=zvto__sck)

    def generic_resolve(self, df, attr):
        if self._is_existing_attr(attr):
            return
        check_runtime_cols_unsupported(df,
            'Acessing DataFrame columns by attribute')
        if attr in df.columns:
            hdj__ebwc = df.columns.index(attr)
            arr_typ = df.data[hdj__ebwc]
            return SeriesType(arr_typ.dtype, arr_typ, df.index, types.
                StringLiteral(attr))
        if len(df.columns) > 0 and isinstance(df.columns[0], tuple):
            wglzj__fzj = []
            jplms__symdn = []
            dklb__gth = False
            for i, wooye__izfcb in enumerate(df.columns):
                if wooye__izfcb[0] != attr:
                    continue
                dklb__gth = True
                wglzj__fzj.append(wooye__izfcb[1] if len(wooye__izfcb) == 2
                     else wooye__izfcb[1:])
                jplms__symdn.append(df.data[i])
            if dklb__gth:
                return DataFrameType(tuple(jplms__symdn), df.index, tuple(
                    wglzj__fzj))


DataFrameAttribute._no_unliteral = True


@overload(operator.getitem, no_unliteral=True)
def namedtuple_getitem_overload(tup, idx):
    if isinstance(tup, types.BaseNamedTuple) and is_overload_constant_str(idx):
        crzgk__vhtzh = get_overload_const_str(idx)
        val_ind = tup.instance_class._fields.index(crzgk__vhtzh)
        return lambda tup, idx: tup[val_ind]


def decref_df_data(context, builder, payload, df_type):
    if df_type.is_table_format:
        context.nrt.decref(builder, df_type.table_type, builder.
            extract_value(payload.data, 0))
        context.nrt.decref(builder, df_type.index, payload.index)
        if df_type.has_runtime_cols:
            context.nrt.decref(builder, df_type.data[-1], payload.columns)
        return
    for i in range(len(df_type.data)):
        hqu__gznvj = builder.extract_value(payload.data, i)
        context.nrt.decref(builder, df_type.data[i], hqu__gznvj)
    context.nrt.decref(builder, df_type.index, payload.index)


def define_df_dtor(context, builder, df_type, payload_type):
    uuvv__vmw = builder.module
    wccp__xdz = lir.FunctionType(lir.VoidType(), [cgutils.voidptr_t])
    ufpqm__jbz = cgutils.get_or_insert_function(uuvv__vmw, wccp__xdz, name=
        '.dtor.df.{}'.format(df_type))
    if not ufpqm__jbz.is_declaration:
        return ufpqm__jbz
    ufpqm__jbz.linkage = 'linkonce_odr'
    builder = lir.IRBuilder(ufpqm__jbz.append_basic_block())
    hbfwr__qaf = ufpqm__jbz.args[0]
    nor__ebpvx = context.get_value_type(payload_type).as_pointer()
    gslp__kpov = builder.bitcast(hbfwr__qaf, nor__ebpvx)
    payload = context.make_helper(builder, payload_type, ref=gslp__kpov)
    decref_df_data(context, builder, payload, df_type)
    has_parent = cgutils.is_not_null(builder, payload.parent)
    with builder.if_then(has_parent):
        evef__xguld = context.get_python_api(builder)
        knqq__blghl = evef__xguld.gil_ensure()
        evef__xguld.decref(payload.parent)
        evef__xguld.gil_release(knqq__blghl)
    builder.ret_void()
    return ufpqm__jbz


def construct_dataframe(context, builder, df_type, data_tup, index_val,
    parent=None, colnames=None):
    payload_type = DataFramePayloadType(df_type)
    qjoct__biehx = cgutils.create_struct_proxy(payload_type)(context, builder)
    qjoct__biehx.data = data_tup
    qjoct__biehx.index = index_val
    if colnames is not None:
        assert df_type.has_runtime_cols, 'construct_dataframe can only provide colnames if columns are determined at runtime'
        qjoct__biehx.columns = colnames
    nsnd__jueer = context.get_value_type(payload_type)
    utuhs__cvtt = context.get_abi_sizeof(nsnd__jueer)
    mlwgb__wpmko = define_df_dtor(context, builder, df_type, payload_type)
    nmx__snjdg = context.nrt.meminfo_alloc_dtor(builder, context.
        get_constant(types.uintp, utuhs__cvtt), mlwgb__wpmko)
    wcje__fjxy = context.nrt.meminfo_data(builder, nmx__snjdg)
    rjaym__oahe = builder.bitcast(wcje__fjxy, nsnd__jueer.as_pointer())
    zxonr__nvk = cgutils.create_struct_proxy(df_type)(context, builder)
    zxonr__nvk.meminfo = nmx__snjdg
    if parent is None:
        zxonr__nvk.parent = cgutils.get_null_value(zxonr__nvk.parent.type)
    else:
        zxonr__nvk.parent = parent
        qjoct__biehx.parent = parent
        has_parent = cgutils.is_not_null(builder, parent)
        with builder.if_then(has_parent):
            evef__xguld = context.get_python_api(builder)
            knqq__blghl = evef__xguld.gil_ensure()
            evef__xguld.incref(parent)
            evef__xguld.gil_release(knqq__blghl)
    builder.store(qjoct__biehx._getvalue(), rjaym__oahe)
    return zxonr__nvk._getvalue()


@intrinsic
def init_runtime_cols_dataframe(typingctx, data_typ, index_typ,
    colnames_index_typ=None):
    assert isinstance(data_typ, types.BaseTuple) and isinstance(data_typ.
        dtype, TableType
        ) and data_typ.dtype.has_runtime_cols, 'init_runtime_cols_dataframe must be called with a table that determines columns at runtime.'
    assert bodo.hiframes.pd_index_ext.is_pd_index_type(colnames_index_typ
        ) or isinstance(colnames_index_typ, bodo.hiframes.
        pd_multi_index_ext.MultiIndexType), 'Column names must be an index'
    if isinstance(data_typ.dtype.arr_types, types.UniTuple):
        jwve__kuj = [data_typ.dtype.arr_types.dtype] * len(data_typ.dtype.
            arr_types)
    else:
        jwve__kuj = [vsqe__ksi for vsqe__ksi in data_typ.dtype.arr_types]
    loc__lampv = DataFrameType(tuple(jwve__kuj + [colnames_index_typ]),
        index_typ, None, is_table_format=True)

    def codegen(context, builder, signature, args):
        df_type = signature.return_type
        data_tup, index, col_names = args
        parent = None
        bviiw__qqtx = construct_dataframe(context, builder, df_type,
            data_tup, index, parent, col_names)
        context.nrt.incref(builder, data_typ, data_tup)
        context.nrt.incref(builder, index_typ, index)
        context.nrt.incref(builder, colnames_index_typ, col_names)
        return bviiw__qqtx
    sig = signature(loc__lampv, data_typ, index_typ, colnames_index_typ)
    return sig, codegen


@intrinsic
def init_dataframe(typingctx, data_tup_typ, index_typ, col_names_typ):
    assert is_pd_index_type(index_typ) or isinstance(index_typ, MultiIndexType
        ), 'init_dataframe(): invalid index type'
    emoh__wwh = len(data_tup_typ.types)
    if emoh__wwh == 0:
        column_names = ()
    sav__pzjw = col_names_typ.instance_type if isinstance(col_names_typ,
        types.TypeRef) else col_names_typ
    assert isinstance(sav__pzjw, ColNamesMetaType) and isinstance(sav__pzjw
        .meta, tuple
        ), 'Third argument to init_dataframe must be of type ColNamesMetaType, and must contain a tuple of column names'
    column_names = sav__pzjw.meta
    if emoh__wwh == 1 and isinstance(data_tup_typ.types[0], TableType):
        emoh__wwh = len(data_tup_typ.types[0].arr_types)
    assert len(column_names
        ) == emoh__wwh, 'init_dataframe(): number of column names does not match number of columns'
    is_table_format = False
    fiu__ufrh = data_tup_typ.types
    if emoh__wwh != 0 and isinstance(data_tup_typ.types[0], TableType):
        fiu__ufrh = data_tup_typ.types[0].arr_types
        is_table_format = True
    loc__lampv = DataFrameType(fiu__ufrh, index_typ, column_names,
        is_table_format=is_table_format)

    def codegen(context, builder, signature, args):
        df_type = signature.return_type
        data_tup = args[0]
        index_val = args[1]
        parent = None
        if is_table_format:
            tpupg__ehs = cgutils.create_struct_proxy(loc__lampv.table_type)(
                context, builder, builder.extract_value(data_tup, 0))
            parent = tpupg__ehs.parent
        bviiw__qqtx = construct_dataframe(context, builder, df_type,
            data_tup, index_val, parent, None)
        context.nrt.incref(builder, data_tup_typ, data_tup)
        context.nrt.incref(builder, index_typ, index_val)
        return bviiw__qqtx
    sig = signature(loc__lampv, data_tup_typ, index_typ, col_names_typ)
    return sig, codegen


@intrinsic
def has_parent(typingctx, df=None):
    check_runtime_cols_unsupported(df, 'has_parent')

    def codegen(context, builder, sig, args):
        zxonr__nvk = cgutils.create_struct_proxy(sig.args[0])(context,
            builder, value=args[0])
        return cgutils.is_not_null(builder, zxonr__nvk.parent)
    return signature(types.bool_, df), codegen


@intrinsic
def _column_needs_unboxing(typingctx, df_typ, i_typ=None):
    check_runtime_cols_unsupported(df_typ, '_column_needs_unboxing')
    assert isinstance(df_typ, DataFrameType) and is_overload_constant_int(i_typ
        )

    def codegen(context, builder, sig, args):
        qjoct__biehx = get_dataframe_payload(context, builder, df_typ, args[0])
        ubs__rdp = get_overload_const_int(i_typ)
        arr_typ = df_typ.data[ubs__rdp]
        if df_typ.is_table_format:
            tpupg__ehs = cgutils.create_struct_proxy(df_typ.table_type)(context
                , builder, builder.extract_value(qjoct__biehx.data, 0))
            tebsi__zjs = df_typ.table_type.type_to_blk[arr_typ]
            jxd__nowvg = getattr(tpupg__ehs, f'block_{tebsi__zjs}')
            cln__sji = ListInstance(context, builder, types.List(arr_typ),
                jxd__nowvg)
            thv__gwwmb = context.get_constant(types.int64, df_typ.
                table_type.block_offsets[ubs__rdp])
            hqu__gznvj = cln__sji.getitem(thv__gwwmb)
        else:
            hqu__gznvj = builder.extract_value(qjoct__biehx.data, ubs__rdp)
        gpdj__kxzh = cgutils.alloca_once_value(builder, hqu__gznvj)
        wrjir__budfy = cgutils.alloca_once_value(builder, context.
            get_constant_null(arr_typ))
        return is_ll_eq(builder, gpdj__kxzh, wrjir__budfy)
    return signature(types.bool_, df_typ, i_typ), codegen


def get_dataframe_payload(context, builder, df_type, value):
    nmx__snjdg = cgutils.create_struct_proxy(df_type)(context, builder, value
        ).meminfo
    payload_type = DataFramePayloadType(df_type)
    payload = context.nrt.meminfo_data(builder, nmx__snjdg)
    nor__ebpvx = context.get_value_type(payload_type).as_pointer()
    payload = builder.bitcast(payload, nor__ebpvx)
    return context.make_helper(builder, payload_type, ref=payload)


@intrinsic
def _get_dataframe_data(typingctx, df_typ=None):
    check_runtime_cols_unsupported(df_typ, '_get_dataframe_data')
    loc__lampv = types.Tuple(df_typ.data)
    if df_typ.is_table_format:
        loc__lampv = types.Tuple([TableType(df_typ.data)])
    sig = signature(loc__lampv, df_typ)

    def codegen(context, builder, signature, args):
        qjoct__biehx = get_dataframe_payload(context, builder, signature.
            args[0], args[0])
        return impl_ret_borrowed(context, builder, signature.return_type,
            qjoct__biehx.data)
    return sig, codegen


@intrinsic
def get_dataframe_index(typingctx, df_typ=None):

    def codegen(context, builder, signature, args):
        qjoct__biehx = get_dataframe_payload(context, builder, signature.
            args[0], args[0])
        return impl_ret_borrowed(context, builder, df_typ.index,
            qjoct__biehx.index)
    loc__lampv = df_typ.index
    sig = signature(loc__lampv, df_typ)
    return sig, codegen


def get_dataframe_data(df, i):
    return df[i]


@infer_global(get_dataframe_data)
class GetDataFrameDataInfer(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        assert len(args) == 2
        if not is_overload_constant_int(args[1]):
            raise_bodo_error(
                'Selecting a DataFrame column requires a constant column label'
                )
        df = args[0]
        check_runtime_cols_unsupported(df, 'get_dataframe_data')
        i = get_overload_const_int(args[1])
        ytk__bvqt = df.data[i]
        return ytk__bvqt(*args)


GetDataFrameDataInfer.prefer_literal = True


def get_dataframe_data_impl(df, i):
    if df.is_table_format:

        def _impl(df, i):
            if has_parent(df) and _column_needs_unboxing(df, i):
                bodo.hiframes.boxing.unbox_dataframe_column(df, i)
            return get_table_data(_get_dataframe_data(df)[0], i)
        return _impl

    def _impl(df, i):
        if has_parent(df) and _column_needs_unboxing(df, i):
            bodo.hiframes.boxing.unbox_dataframe_column(df, i)
        return _get_dataframe_data(df)[i]
    return _impl


@intrinsic
def get_dataframe_table(typingctx, df_typ=None):
    assert df_typ.is_table_format, 'get_dataframe_table() expects table format'

    def codegen(context, builder, signature, args):
        qjoct__biehx = get_dataframe_payload(context, builder, signature.
            args[0], args[0])
        return impl_ret_borrowed(context, builder, df_typ.table_type,
            builder.extract_value(qjoct__biehx.data, 0))
    return df_typ.table_type(df_typ), codegen


def get_dataframe_all_data(df):
    return df.data


def get_dataframe_all_data_impl(df):
    if df.is_table_format:

        def _impl(df):
            return get_dataframe_table(df)
        return _impl
    data = ', '.join(
        f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})' for i in
        range(len(df.columns)))
    ktvt__ubml = ',' if len(df.columns) > 1 else ''
    return eval(f'lambda df: ({data}{ktvt__ubml})', {'bodo': bodo})


@infer_global(get_dataframe_all_data)
class GetDataFrameAllDataInfer(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        assert len(args) == 1
        df_type = args[0]
        check_runtime_cols_unsupported(df_type, 'get_dataframe_data')
        ytk__bvqt = (df_type.table_type if df_type.is_table_format else
            types.BaseTuple.from_types(df_type.data))
        return ytk__bvqt(*args)


@lower_builtin(get_dataframe_all_data, DataFrameType)
def lower_get_dataframe_all_data(context, builder, sig, args):
    impl = get_dataframe_all_data_impl(*sig.args)
    return context.compile_internal(builder, impl, sig, args)


@intrinsic
def get_dataframe_column_names(typingctx, df_typ=None):
    assert df_typ.has_runtime_cols, 'get_dataframe_column_names() expects columns to be determined at runtime'

    def codegen(context, builder, signature, args):
        qjoct__biehx = get_dataframe_payload(context, builder, signature.
            args[0], args[0])
        return impl_ret_borrowed(context, builder, df_typ.
            runtime_colname_typ, qjoct__biehx.columns)
    return df_typ.runtime_colname_typ(df_typ), codegen


@lower_builtin(get_dataframe_data, DataFrameType, types.IntegerLiteral)
def lower_get_dataframe_data(context, builder, sig, args):
    impl = get_dataframe_data_impl(*sig.args)
    return context.compile_internal(builder, impl, sig, args)


def alias_ext_dummy_func(lhs_name, args, alias_map, arg_aliases):
    assert len(args) >= 1
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)


numba.core.ir_utils.alias_func_extensions['get_dataframe_data',
    'bodo.hiframes.pd_dataframe_ext'] = alias_ext_dummy_func
numba.core.ir_utils.alias_func_extensions['get_dataframe_index',
    'bodo.hiframes.pd_dataframe_ext'] = alias_ext_dummy_func
numba.core.ir_utils.alias_func_extensions['get_dataframe_table',
    'bodo.hiframes.pd_dataframe_ext'] = alias_ext_dummy_func
numba.core.ir_utils.alias_func_extensions['get_dataframe_all_data',
    'bodo.hiframes.pd_dataframe_ext'] = alias_ext_dummy_func


def alias_ext_init_dataframe(lhs_name, args, alias_map, arg_aliases):
    assert len(args) == 3
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)
    numba.core.ir_utils._add_alias(lhs_name, args[1].name, alias_map,
        arg_aliases)


numba.core.ir_utils.alias_func_extensions['init_dataframe',
    'bodo.hiframes.pd_dataframe_ext'] = alias_ext_init_dataframe


def init_dataframe_equiv(self, scope, equiv_set, loc, args, kws):
    from bodo.hiframes.pd_index_ext import HeterogeneousIndexType
    assert len(args) == 3 and not kws
    data_tup = args[0]
    index = args[1]
    ovk__pjisy = self.typemap[data_tup.name]
    if any(is_tuple_like_type(vsqe__ksi) for vsqe__ksi in ovk__pjisy.types):
        return None
    if equiv_set.has_shape(data_tup):
        zdhsj__ysvu = equiv_set.get_shape(data_tup)
        if len(zdhsj__ysvu) > 1:
            equiv_set.insert_equiv(*zdhsj__ysvu)
        if len(zdhsj__ysvu) > 0:
            xyr__ota = self.typemap[index.name]
            if not isinstance(xyr__ota, HeterogeneousIndexType
                ) and equiv_set.has_shape(index):
                equiv_set.insert_equiv(zdhsj__ysvu[0], index)
            return ArrayAnalysis.AnalyzeResult(shape=(zdhsj__ysvu[0], len(
                zdhsj__ysvu)), pre=[])
    return None


(ArrayAnalysis._analyze_op_call_bodo_hiframes_pd_dataframe_ext_init_dataframe
    ) = init_dataframe_equiv


def get_dataframe_data_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 2 and not kws
    ksw__ajb = args[0]
    data_types = self.typemap[ksw__ajb.name].data
    if any(is_tuple_like_type(vsqe__ksi) for vsqe__ksi in data_types):
        return None
    if equiv_set.has_shape(ksw__ajb):
        return ArrayAnalysis.AnalyzeResult(shape=equiv_set.get_shape(
            ksw__ajb)[0], pre=[])
    return None


(ArrayAnalysis.
    _analyze_op_call_bodo_hiframes_pd_dataframe_ext_get_dataframe_data
    ) = get_dataframe_data_equiv


def get_dataframe_index_equiv(self, scope, equiv_set, loc, args, kws):
    from bodo.hiframes.pd_index_ext import HeterogeneousIndexType
    assert len(args) == 1 and not kws
    ksw__ajb = args[0]
    xyr__ota = self.typemap[ksw__ajb.name].index
    if isinstance(xyr__ota, HeterogeneousIndexType):
        return None
    if equiv_set.has_shape(ksw__ajb):
        return ArrayAnalysis.AnalyzeResult(shape=equiv_set.get_shape(
            ksw__ajb)[0], pre=[])
    return None


(ArrayAnalysis.
    _analyze_op_call_bodo_hiframes_pd_dataframe_ext_get_dataframe_index
    ) = get_dataframe_index_equiv


def get_dataframe_table_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 1 and not kws
    ksw__ajb = args[0]
    if equiv_set.has_shape(ksw__ajb):
        return ArrayAnalysis.AnalyzeResult(shape=equiv_set.get_shape(
            ksw__ajb), pre=[])


(ArrayAnalysis.
    _analyze_op_call_bodo_hiframes_pd_dataframe_ext_get_dataframe_table
    ) = get_dataframe_table_equiv


def get_dataframe_column_names_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 1 and not kws
    ksw__ajb = args[0]
    if equiv_set.has_shape(ksw__ajb):
        return ArrayAnalysis.AnalyzeResult(shape=equiv_set.get_shape(
            ksw__ajb)[1], pre=[])
    return None


(ArrayAnalysis.
    _analyze_op_call_bodo_hiframes_pd_dataframe_ext_get_dataframe_column_names
    ) = get_dataframe_column_names_equiv


@intrinsic
def set_dataframe_data(typingctx, df_typ, c_ind_typ, arr_typ=None):
    check_runtime_cols_unsupported(df_typ, 'set_dataframe_data')
    assert is_overload_constant_int(c_ind_typ)
    ubs__rdp = get_overload_const_int(c_ind_typ)
    if df_typ.data[ubs__rdp] != arr_typ:
        raise BodoError(
            'Changing dataframe column data type inplace is not supported in conditionals/loops or for dataframe arguments'
            )

    def codegen(context, builder, signature, args):
        ttmc__ixat, zvl__tupjy, szese__wyh = args
        qjoct__biehx = get_dataframe_payload(context, builder, df_typ,
            ttmc__ixat)
        if df_typ.is_table_format:
            tpupg__ehs = cgutils.create_struct_proxy(df_typ.table_type)(context
                , builder, builder.extract_value(qjoct__biehx.data, 0))
            tebsi__zjs = df_typ.table_type.type_to_blk[arr_typ]
            jxd__nowvg = getattr(tpupg__ehs, f'block_{tebsi__zjs}')
            cln__sji = ListInstance(context, builder, types.List(arr_typ),
                jxd__nowvg)
            thv__gwwmb = context.get_constant(types.int64, df_typ.
                table_type.block_offsets[ubs__rdp])
            cln__sji.setitem(thv__gwwmb, szese__wyh, True)
        else:
            hqu__gznvj = builder.extract_value(qjoct__biehx.data, ubs__rdp)
            context.nrt.decref(builder, df_typ.data[ubs__rdp], hqu__gznvj)
            qjoct__biehx.data = builder.insert_value(qjoct__biehx.data,
                szese__wyh, ubs__rdp)
            context.nrt.incref(builder, arr_typ, szese__wyh)
        zxonr__nvk = cgutils.create_struct_proxy(df_typ)(context, builder,
            value=ttmc__ixat)
        payload_type = DataFramePayloadType(df_typ)
        gslp__kpov = context.nrt.meminfo_data(builder, zxonr__nvk.meminfo)
        nor__ebpvx = context.get_value_type(payload_type).as_pointer()
        gslp__kpov = builder.bitcast(gslp__kpov, nor__ebpvx)
        builder.store(qjoct__biehx._getvalue(), gslp__kpov)
        return impl_ret_borrowed(context, builder, df_typ, ttmc__ixat)
    sig = signature(df_typ, df_typ, c_ind_typ, arr_typ)
    return sig, codegen


@intrinsic
def set_df_index(typingctx, df_t, index_t=None):
    check_runtime_cols_unsupported(df_t, 'set_df_index')

    def codegen(context, builder, signature, args):
        rvcke__upd = args[0]
        index_val = args[1]
        df_typ = signature.args[0]
        ezej__xrd = cgutils.create_struct_proxy(df_typ)(context, builder,
            value=rvcke__upd)
        dosw__led = get_dataframe_payload(context, builder, df_typ, rvcke__upd)
        zxonr__nvk = construct_dataframe(context, builder, signature.
            return_type, dosw__led.data, index_val, ezej__xrd.parent, None)
        context.nrt.incref(builder, index_t, index_val)
        context.nrt.incref(builder, types.Tuple(df_t.data), dosw__led.data)
        return zxonr__nvk
    loc__lampv = DataFrameType(df_t.data, index_t, df_t.columns, df_t.dist,
        df_t.is_table_format)
    sig = signature(loc__lampv, df_t, index_t)
    return sig, codegen


@intrinsic
def set_df_column_with_reflect(typingctx, df_type, cname_type, arr_type=None):
    check_runtime_cols_unsupported(df_type, 'set_df_column_with_reflect')
    assert is_literal_type(cname_type), 'constant column name expected'
    col_name = get_literal_value(cname_type)
    emoh__wwh = len(df_type.columns)
    ghet__zgkwd = emoh__wwh
    zwvo__knza = df_type.data
    column_names = df_type.columns
    index_typ = df_type.index
    qljd__heqjd = col_name not in df_type.columns
    ubs__rdp = emoh__wwh
    if qljd__heqjd:
        zwvo__knza += arr_type,
        column_names += col_name,
        ghet__zgkwd += 1
    else:
        ubs__rdp = df_type.columns.index(col_name)
        zwvo__knza = tuple(arr_type if i == ubs__rdp else zwvo__knza[i] for
            i in range(emoh__wwh))

    def codegen(context, builder, signature, args):
        ttmc__ixat, zvl__tupjy, szese__wyh = args
        in_dataframe_payload = get_dataframe_payload(context, builder,
            df_type, ttmc__ixat)
        hsro__deud = cgutils.create_struct_proxy(df_type)(context, builder,
            value=ttmc__ixat)
        if df_type.is_table_format:
            skzk__jbw = df_type.table_type
            dwlv__kgl = builder.extract_value(in_dataframe_payload.data, 0)
            yzz__oszj = TableType(zwvo__knza)
            ktrj__kiy = set_table_data_codegen(context, builder, skzk__jbw,
                dwlv__kgl, yzz__oszj, arr_type, szese__wyh, ubs__rdp,
                qljd__heqjd)
            data_tup = context.make_tuple(builder, types.Tuple([yzz__oszj]),
                [ktrj__kiy])
        else:
            fiu__ufrh = [(builder.extract_value(in_dataframe_payload.data,
                i) if i != ubs__rdp else szese__wyh) for i in range(emoh__wwh)]
            if qljd__heqjd:
                fiu__ufrh.append(szese__wyh)
            for ksw__ajb, rblat__bnz in zip(fiu__ufrh, zwvo__knza):
                context.nrt.incref(builder, rblat__bnz, ksw__ajb)
            data_tup = context.make_tuple(builder, types.Tuple(zwvo__knza),
                fiu__ufrh)
        index_val = in_dataframe_payload.index
        context.nrt.incref(builder, index_typ, index_val)
        csfy__lumgj = construct_dataframe(context, builder, signature.
            return_type, data_tup, index_val, hsro__deud.parent, None)
        if not qljd__heqjd and arr_type == df_type.data[ubs__rdp]:
            decref_df_data(context, builder, in_dataframe_payload, df_type)
            payload_type = DataFramePayloadType(df_type)
            gslp__kpov = context.nrt.meminfo_data(builder, hsro__deud.meminfo)
            nor__ebpvx = context.get_value_type(payload_type).as_pointer()
            gslp__kpov = builder.bitcast(gslp__kpov, nor__ebpvx)
            rmo__drw = get_dataframe_payload(context, builder, df_type,
                csfy__lumgj)
            builder.store(rmo__drw._getvalue(), gslp__kpov)
            context.nrt.incref(builder, index_typ, index_val)
            if df_type.is_table_format:
                context.nrt.incref(builder, yzz__oszj, builder.
                    extract_value(data_tup, 0))
            else:
                for ksw__ajb, rblat__bnz in zip(fiu__ufrh, zwvo__knza):
                    context.nrt.incref(builder, rblat__bnz, ksw__ajb)
        has_parent = cgutils.is_not_null(builder, hsro__deud.parent)
        with builder.if_then(has_parent):
            evef__xguld = context.get_python_api(builder)
            knqq__blghl = evef__xguld.gil_ensure()
            cwqr__dol = context.get_env_manager(builder)
            context.nrt.incref(builder, arr_type, szese__wyh)
            ojaae__obyr = numba.core.pythonapi._BoxContext(context, builder,
                evef__xguld, cwqr__dol)
            ukf__wxq = ojaae__obyr.pyapi.from_native_value(arr_type,
                szese__wyh, ojaae__obyr.env_manager)
            if isinstance(col_name, str):
                ltheu__uew = context.insert_const_string(builder.module,
                    col_name)
                heoc__websc = evef__xguld.string_from_string(ltheu__uew)
            else:
                assert isinstance(col_name, int)
                heoc__websc = evef__xguld.long_from_longlong(context.
                    get_constant(types.intp, col_name))
            evef__xguld.object_setitem(hsro__deud.parent, heoc__websc, ukf__wxq
                )
            evef__xguld.decref(ukf__wxq)
            evef__xguld.decref(heoc__websc)
            evef__xguld.gil_release(knqq__blghl)
        return csfy__lumgj
    loc__lampv = DataFrameType(zwvo__knza, index_typ, column_names, df_type
        .dist, df_type.is_table_format)
    sig = signature(loc__lampv, df_type, cname_type, arr_type)
    return sig, codegen


@lower_constant(DataFrameType)
def lower_constant_dataframe(context, builder, df_type, pyval):
    check_runtime_cols_unsupported(df_type, 'lowering a constant DataFrame')
    emoh__wwh = len(pyval.columns)
    fiu__ufrh = []
    for i in range(emoh__wwh):
        lxk__fpp = pyval.iloc[:, i]
        if isinstance(df_type.data[i], bodo.DatetimeArrayType):
            ukf__wxq = lxk__fpp.array
        else:
            ukf__wxq = lxk__fpp.values
        fiu__ufrh.append(ukf__wxq)
    fiu__ufrh = tuple(fiu__ufrh)
    if df_type.is_table_format:
        tpupg__ehs = context.get_constant_generic(builder, df_type.
            table_type, Table(fiu__ufrh))
        data_tup = lir.Constant.literal_struct([tpupg__ehs])
    else:
        data_tup = lir.Constant.literal_struct([context.
            get_constant_generic(builder, df_type.data[i], wooye__izfcb) for
            i, wooye__izfcb in enumerate(fiu__ufrh)])
    index_val = context.get_constant_generic(builder, df_type.index, pyval.
        index)
    ynxo__zzech = context.get_constant_null(types.pyobject)
    payload = lir.Constant.literal_struct([data_tup, index_val, ynxo__zzech])
    payload = cgutils.global_constant(builder, '.const.payload', payload
        ).bitcast(cgutils.voidptr_t)
    pskl__mspy = context.get_constant(types.int64, -1)
    mvr__omul = context.get_constant_null(types.voidptr)
    nmx__snjdg = lir.Constant.literal_struct([pskl__mspy, mvr__omul,
        mvr__omul, payload, pskl__mspy])
    nmx__snjdg = cgutils.global_constant(builder, '.const.meminfo', nmx__snjdg
        ).bitcast(cgutils.voidptr_t)
    return lir.Constant.literal_struct([nmx__snjdg, ynxo__zzech])


@lower_cast(DataFrameType, DataFrameType)
def cast_df_to_df(context, builder, fromty, toty, val):
    if (fromty.data == toty.data and fromty.index == toty.index and fromty.
        columns == toty.columns and fromty.is_table_format == toty.
        is_table_format and fromty.dist != toty.dist and fromty.
        has_runtime_cols == toty.has_runtime_cols):
        return val
    if not fromty.has_runtime_cols and not toty.has_runtime_cols and len(fromty
        .data) == 0 and len(toty.columns):
        return _cast_empty_df(context, builder, toty)
    if len(fromty.data) != len(toty.data) or fromty.data != toty.data and any(
        context.typing_context.unify_pairs(fromty.data[i], toty.data[i]) is
        None for i in range(len(fromty.data))
        ) or fromty.has_runtime_cols != toty.has_runtime_cols:
        raise BodoError(f'Invalid dataframe cast from {fromty} to {toty}')
    in_dataframe_payload = get_dataframe_payload(context, builder, fromty, val)
    if isinstance(fromty.index, RangeIndexType) and isinstance(toty.index,
        NumericIndexType):
        zoh__azm = context.cast(builder, in_dataframe_payload.index, fromty
            .index, toty.index)
    else:
        zoh__azm = in_dataframe_payload.index
        context.nrt.incref(builder, fromty.index, zoh__azm)
    if (fromty.is_table_format == toty.is_table_format and fromty.data ==
        toty.data):
        jplms__symdn = in_dataframe_payload.data
        if fromty.is_table_format:
            context.nrt.incref(builder, types.Tuple([fromty.table_type]),
                jplms__symdn)
        else:
            context.nrt.incref(builder, types.BaseTuple.from_types(fromty.
                data), jplms__symdn)
    elif not fromty.is_table_format and toty.is_table_format:
        jplms__symdn = _cast_df_data_to_table_format(context, builder,
            fromty, toty, val, in_dataframe_payload)
    elif fromty.is_table_format and not toty.is_table_format:
        jplms__symdn = _cast_df_data_to_tuple_format(context, builder,
            fromty, toty, val, in_dataframe_payload)
    elif fromty.is_table_format and toty.is_table_format:
        jplms__symdn = _cast_df_data_keep_table_format(context, builder,
            fromty, toty, val, in_dataframe_payload)
    else:
        jplms__symdn = _cast_df_data_keep_tuple_format(context, builder,
            fromty, toty, val, in_dataframe_payload)
    return construct_dataframe(context, builder, toty, jplms__symdn,
        zoh__azm, in_dataframe_payload.parent, None)


def _cast_empty_df(context, builder, toty):
    vpzvc__wprg = {}
    if isinstance(toty.index, RangeIndexType):
        index = 'bodo.hiframes.pd_index_ext.init_range_index(0, 0, 1, None)'
    else:
        vlhm__zgjeq = get_index_data_arr_types(toty.index)[0]
        dnq__ijpxc = bodo.utils.transform.get_type_alloc_counts(vlhm__zgjeq
            ) - 1
        vad__lyqre = ', '.join('0' for zvl__tupjy in range(dnq__ijpxc))
        index = (
            'bodo.utils.conversion.index_from_array(bodo.utils.utils.alloc_type(0, index_arr_type, ({}{})))'
            .format(vad__lyqre, ', ' if dnq__ijpxc == 1 else ''))
        vpzvc__wprg['index_arr_type'] = vlhm__zgjeq
    dkikk__jus = []
    for i, arr_typ in enumerate(toty.data):
        dnq__ijpxc = bodo.utils.transform.get_type_alloc_counts(arr_typ) - 1
        vad__lyqre = ', '.join('0' for zvl__tupjy in range(dnq__ijpxc))
        zfotl__uzko = ('bodo.utils.utils.alloc_type(0, arr_type{}, ({}{}))'
            .format(i, vad__lyqre, ', ' if dnq__ijpxc == 1 else ''))
        dkikk__jus.append(zfotl__uzko)
        vpzvc__wprg[f'arr_type{i}'] = arr_typ
    dkikk__jus = ', '.join(dkikk__jus)
    llvq__jarb = 'def impl():\n'
    pezd__yeqiu = bodo.hiframes.dataframe_impl._gen_init_df(llvq__jarb,
        toty.columns, dkikk__jus, index, vpzvc__wprg)
    df = context.compile_internal(builder, pezd__yeqiu, toty(), [])
    return df


def _cast_df_data_to_table_format(context, builder, fromty, toty, df,
    in_dataframe_payload):
    check_runtime_cols_unsupported(toty,
        'casting traditional DataFrame to table format')
    kqz__qxxd = toty.table_type
    tpupg__ehs = cgutils.create_struct_proxy(kqz__qxxd)(context, builder)
    tpupg__ehs.parent = in_dataframe_payload.parent
    for vsqe__ksi, tebsi__zjs in kqz__qxxd.type_to_blk.items():
        vhf__sgwwx = context.get_constant(types.int64, len(kqz__qxxd.
            block_to_arr_ind[tebsi__zjs]))
        zvl__tupjy, wsydj__zdaw = ListInstance.allocate_ex(context, builder,
            types.List(vsqe__ksi), vhf__sgwwx)
        wsydj__zdaw.size = vhf__sgwwx
        setattr(tpupg__ehs, f'block_{tebsi__zjs}', wsydj__zdaw.value)
    for i, vsqe__ksi in enumerate(fromty.data):
        vba__gyw = toty.data[i]
        if vsqe__ksi != vba__gyw:
            rcdq__alric = fromty, types.literal(i)
            impl = lambda df, i: bodo.hiframes.boxing.unbox_col_if_needed(df, i
                )
            sig = types.none(*rcdq__alric)
            args = df, context.get_constant(types.int64, i)
            context.compile_internal(builder, impl, sig, args)
        hqu__gznvj = builder.extract_value(in_dataframe_payload.data, i)
        if vsqe__ksi != vba__gyw:
            lfsn__jdmg = context.cast(builder, hqu__gznvj, vsqe__ksi, vba__gyw)
            ayxkn__asni = False
        else:
            lfsn__jdmg = hqu__gznvj
            ayxkn__asni = True
        tebsi__zjs = kqz__qxxd.type_to_blk[vsqe__ksi]
        jxd__nowvg = getattr(tpupg__ehs, f'block_{tebsi__zjs}')
        cln__sji = ListInstance(context, builder, types.List(vsqe__ksi),
            jxd__nowvg)
        thv__gwwmb = context.get_constant(types.int64, kqz__qxxd.
            block_offsets[i])
        cln__sji.setitem(thv__gwwmb, lfsn__jdmg, ayxkn__asni)
    data_tup = context.make_tuple(builder, types.Tuple([kqz__qxxd]), [
        tpupg__ehs._getvalue()])
    return data_tup


def _cast_df_data_keep_tuple_format(context, builder, fromty, toty, df,
    in_dataframe_payload):
    check_runtime_cols_unsupported(toty,
        'casting traditional DataFrame columns')
    fiu__ufrh = []
    for i in range(len(fromty.data)):
        if fromty.data[i] != toty.data[i]:
            rcdq__alric = fromty, types.literal(i)
            impl = lambda df, i: bodo.hiframes.boxing.unbox_col_if_needed(df, i
                )
            sig = types.none(*rcdq__alric)
            args = df, context.get_constant(types.int64, i)
            context.compile_internal(builder, impl, sig, args)
            hqu__gznvj = builder.extract_value(in_dataframe_payload.data, i)
            lfsn__jdmg = context.cast(builder, hqu__gznvj, fromty.data[i],
                toty.data[i])
            ayxkn__asni = False
        else:
            lfsn__jdmg = builder.extract_value(in_dataframe_payload.data, i)
            ayxkn__asni = True
        if ayxkn__asni:
            context.nrt.incref(builder, toty.data[i], lfsn__jdmg)
        fiu__ufrh.append(lfsn__jdmg)
    data_tup = context.make_tuple(builder, types.Tuple(toty.data), fiu__ufrh)
    return data_tup


def _cast_df_data_keep_table_format(context, builder, fromty, toty, df,
    in_dataframe_payload):
    check_runtime_cols_unsupported(toty,
        'casting table format DataFrame columns')
    skzk__jbw = fromty.table_type
    dwlv__kgl = cgutils.create_struct_proxy(skzk__jbw)(context, builder,
        builder.extract_value(in_dataframe_payload.data, 0))
    yzz__oszj = toty.table_type
    ktrj__kiy = cgutils.create_struct_proxy(yzz__oszj)(context, builder)
    ktrj__kiy.parent = in_dataframe_payload.parent
    for vsqe__ksi, tebsi__zjs in yzz__oszj.type_to_blk.items():
        vhf__sgwwx = context.get_constant(types.int64, len(yzz__oszj.
            block_to_arr_ind[tebsi__zjs]))
        zvl__tupjy, wsydj__zdaw = ListInstance.allocate_ex(context, builder,
            types.List(vsqe__ksi), vhf__sgwwx)
        wsydj__zdaw.size = vhf__sgwwx
        setattr(ktrj__kiy, f'block_{tebsi__zjs}', wsydj__zdaw.value)
    for i in range(len(fromty.data)):
        gvxkb__izdso = fromty.data[i]
        vba__gyw = toty.data[i]
        if gvxkb__izdso != vba__gyw:
            rcdq__alric = fromty, types.literal(i)
            impl = lambda df, i: bodo.hiframes.boxing.unbox_col_if_needed(df, i
                )
            sig = types.none(*rcdq__alric)
            args = df, context.get_constant(types.int64, i)
            context.compile_internal(builder, impl, sig, args)
        rdy__kljs = skzk__jbw.type_to_blk[gvxkb__izdso]
        zxy__ojty = getattr(dwlv__kgl, f'block_{rdy__kljs}')
        eqib__foovs = ListInstance(context, builder, types.List(
            gvxkb__izdso), zxy__ojty)
        nyxot__wqnc = context.get_constant(types.int64, skzk__jbw.
            block_offsets[i])
        hqu__gznvj = eqib__foovs.getitem(nyxot__wqnc)
        if gvxkb__izdso != vba__gyw:
            lfsn__jdmg = context.cast(builder, hqu__gznvj, gvxkb__izdso,
                vba__gyw)
            ayxkn__asni = False
        else:
            lfsn__jdmg = hqu__gznvj
            ayxkn__asni = True
        kny__posvz = yzz__oszj.type_to_blk[vsqe__ksi]
        wsydj__zdaw = getattr(ktrj__kiy, f'block_{kny__posvz}')
        xxg__hel = ListInstance(context, builder, types.List(vba__gyw),
            wsydj__zdaw)
        pjwu__ecjn = context.get_constant(types.int64, yzz__oszj.
            block_offsets[i])
        xxg__hel.setitem(pjwu__ecjn, lfsn__jdmg, ayxkn__asni)
    data_tup = context.make_tuple(builder, types.Tuple([yzz__oszj]), [
        ktrj__kiy._getvalue()])
    return data_tup


def _cast_df_data_to_tuple_format(context, builder, fromty, toty, df,
    in_dataframe_payload):
    check_runtime_cols_unsupported(fromty,
        'casting table format to traditional DataFrame')
    kqz__qxxd = fromty.table_type
    tpupg__ehs = cgutils.create_struct_proxy(kqz__qxxd)(context, builder,
        builder.extract_value(in_dataframe_payload.data, 0))
    fiu__ufrh = []
    for i, vsqe__ksi in enumerate(toty.data):
        gvxkb__izdso = fromty.data[i]
        if vsqe__ksi != gvxkb__izdso:
            rcdq__alric = fromty, types.literal(i)
            impl = lambda df, i: bodo.hiframes.boxing.unbox_col_if_needed(df, i
                )
            sig = types.none(*rcdq__alric)
            args = df, context.get_constant(types.int64, i)
            context.compile_internal(builder, impl, sig, args)
        tebsi__zjs = kqz__qxxd.type_to_blk[gvxkb__izdso]
        jxd__nowvg = getattr(tpupg__ehs, f'block_{tebsi__zjs}')
        cln__sji = ListInstance(context, builder, types.List(gvxkb__izdso),
            jxd__nowvg)
        thv__gwwmb = context.get_constant(types.int64, kqz__qxxd.
            block_offsets[i])
        hqu__gznvj = cln__sji.getitem(thv__gwwmb)
        if vsqe__ksi != gvxkb__izdso:
            lfsn__jdmg = context.cast(builder, hqu__gznvj, gvxkb__izdso,
                vsqe__ksi)
        else:
            lfsn__jdmg = hqu__gznvj
            context.nrt.incref(builder, vsqe__ksi, lfsn__jdmg)
        fiu__ufrh.append(lfsn__jdmg)
    data_tup = context.make_tuple(builder, types.Tuple(toty.data), fiu__ufrh)
    return data_tup


@overload(pd.DataFrame, inline='always', no_unliteral=True)
def pd_dataframe_overload(data=None, index=None, columns=None, dtype=None,
    copy=False):
    if not is_overload_constant_bool(copy):
        raise BodoError(
            "pd.DataFrame(): 'copy' argument should be a constant boolean")
    copy = get_overload_const(copy)
    vzj__xsg, dkikk__jus, index_arg = _get_df_args(data, index, columns,
        dtype, copy)
    uxq__sikx = ColNamesMetaType(tuple(vzj__xsg))
    llvq__jarb = (
        'def _init_df(data=None, index=None, columns=None, dtype=None, copy=False):\n'
        )
    llvq__jarb += (
        """  return bodo.hiframes.pd_dataframe_ext.init_dataframe({}, {}, __col_name_meta_value_pd_overload)
"""
        .format(dkikk__jus, index_arg))
    nrsh__tdq = {}
    exec(llvq__jarb, {'bodo': bodo, 'np': np,
        '__col_name_meta_value_pd_overload': uxq__sikx}, nrsh__tdq)
    gah__llyzi = nrsh__tdq['_init_df']
    return gah__llyzi


@intrinsic
def _tuple_to_table_format_decoded(typingctx, df_typ):
    assert not df_typ.is_table_format, '_tuple_to_table_format requires a tuple format input'

    def codegen(context, builder, signature, args):
        return context.cast(builder, args[0], signature.args[0], signature.
            return_type)
    loc__lampv = DataFrameType(to_str_arr_if_dict_array(df_typ.data),
        df_typ.index, df_typ.columns, dist=df_typ.dist, is_table_format=True)
    sig = signature(loc__lampv, df_typ)
    return sig, codegen


@intrinsic
def _table_to_tuple_format_decoded(typingctx, df_typ):
    assert df_typ.is_table_format, '_tuple_to_table_format requires a table format input'

    def codegen(context, builder, signature, args):
        return context.cast(builder, args[0], signature.args[0], signature.
            return_type)
    loc__lampv = DataFrameType(to_str_arr_if_dict_array(df_typ.data),
        df_typ.index, df_typ.columns, dist=df_typ.dist, is_table_format=False)
    sig = signature(loc__lampv, df_typ)
    return sig, codegen


def _get_df_args(data, index, columns, dtype, copy):
    vck__yjn = ''
    if not is_overload_none(dtype):
        vck__yjn = '.astype(dtype)'
    index_is_none = is_overload_none(index)
    index_arg = 'bodo.utils.conversion.convert_to_index(index)'
    if isinstance(data, types.BaseTuple):
        if not data.types[0] == types.StringLiteral('__bodo_tup'):
            raise BodoError('pd.DataFrame tuple input data not supported yet')
        assert len(data.types) % 2 == 1, 'invalid const dict tuple structure'
        emoh__wwh = (len(data.types) - 1) // 2
        zmcgd__doqm = [vsqe__ksi.literal_value for vsqe__ksi in data.types[
            1:emoh__wwh + 1]]
        data_val_types = dict(zip(zmcgd__doqm, data.types[emoh__wwh + 1:]))
        fiu__ufrh = ['data[{}]'.format(i) for i in range(emoh__wwh + 1, 2 *
            emoh__wwh + 1)]
        data_dict = dict(zip(zmcgd__doqm, fiu__ufrh))
        if is_overload_none(index):
            for i, vsqe__ksi in enumerate(data.types[emoh__wwh + 1:]):
                if isinstance(vsqe__ksi, SeriesType):
                    index_arg = (
                        'bodo.hiframes.pd_series_ext.get_series_index(data[{}])'
                        .format(emoh__wwh + 1 + i))
                    index_is_none = False
                    break
    elif is_overload_none(data):
        data_dict = {}
        data_val_types = {}
    else:
        if not (isinstance(data, types.Array) and data.ndim == 2):
            raise BodoError(
                'pd.DataFrame() only supports constant dictionary and array input'
                )
        if is_overload_none(columns):
            raise BodoError(
                "pd.DataFrame() 'columns' argument is required when an array is passed as data"
                )
        hqhzd__husfb = '.copy()' if copy else ''
        gpdu__siw = get_overload_const_list(columns)
        emoh__wwh = len(gpdu__siw)
        data_val_types = {ojaae__obyr: data.copy(ndim=1) for ojaae__obyr in
            gpdu__siw}
        fiu__ufrh = ['data[:,{}]{}'.format(i, hqhzd__husfb) for i in range(
            emoh__wwh)]
        data_dict = dict(zip(gpdu__siw, fiu__ufrh))
    if is_overload_none(columns):
        col_names = data_dict.keys()
    else:
        col_names = get_overload_const_list(columns)
    df_len = _get_df_len_from_info(data_dict, data_val_types, col_names,
        index_is_none, index_arg)
    _fill_null_arrays(data_dict, col_names, df_len, dtype)
    if index_is_none:
        if is_overload_none(data):
            index_arg = (
                'bodo.hiframes.pd_index_ext.init_binary_str_index(bodo.libs.str_arr_ext.pre_alloc_string_array(0, 0))'
                )
        else:
            index_arg = (
                'bodo.hiframes.pd_index_ext.init_range_index(0, {}, 1, None)'
                .format(df_len))
    dkikk__jus = '({},)'.format(', '.join(
        'bodo.utils.conversion.coerce_to_array({}, True, scalar_to_arr_len={}){}'
        .format(data_dict[ojaae__obyr], df_len, vck__yjn) for ojaae__obyr in
        col_names))
    if len(col_names) == 0:
        dkikk__jus = '()'
    return col_names, dkikk__jus, index_arg


def _get_df_len_from_info(data_dict, data_val_types, col_names,
    index_is_none, index_arg):
    df_len = '0'
    for ojaae__obyr in col_names:
        if ojaae__obyr in data_dict and is_iterable_type(data_val_types[
            ojaae__obyr]):
            df_len = 'len({})'.format(data_dict[ojaae__obyr])
            break
    if df_len == '0':
        if not index_is_none:
            df_len = f'len({index_arg})'
        elif data_dict:
            raise BodoError(
                'Internal Error: Unable to determine length of DataFrame Index. If this is unexpected, please try passing an index value.'
                )
    return df_len


def _fill_null_arrays(data_dict, col_names, df_len, dtype):
    if all(ojaae__obyr in data_dict for ojaae__obyr in col_names):
        return
    if is_overload_none(dtype):
        dtype = 'bodo.string_array_type'
    else:
        dtype = 'bodo.utils.conversion.array_type_from_dtype(dtype)'
    bxft__olja = 'bodo.libs.array_kernels.gen_na_array({}, {})'.format(df_len,
        dtype)
    for ojaae__obyr in col_names:
        if ojaae__obyr not in data_dict:
            data_dict[ojaae__obyr] = bxft__olja


@infer_global(len)
class LenTemplate(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        assert len(args) == 1
        if isinstance(args[0], (DataFrameType, bodo.TableType)):
            return types.int64(*args)


@lower_builtin(len, DataFrameType)
def table_len_lower(context, builder, sig, args):
    impl = df_len_overload(*sig.args)
    return context.compile_internal(builder, impl, sig, args)


def df_len_overload(df):
    if not isinstance(df, DataFrameType):
        return
    if df.has_runtime_cols:

        def impl(df):
            if is_null_pointer(df._meminfo):
                return 0
            vsqe__ksi = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)
            return len(vsqe__ksi)
        return impl
    if len(df.columns) == 0:

        def impl(df):
            if is_null_pointer(df._meminfo):
                return 0
            return len(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df))
        return impl

    def impl(df):
        if is_null_pointer(df._meminfo):
            return 0
        return len(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, 0))
    return impl


@infer_global(operator.getitem)
class GetItemTuple(AbstractTemplate):
    key = operator.getitem

    def generic(self, args, kws):
        tup, idx = args
        if not isinstance(tup, types.BaseTuple) or not isinstance(idx,
            types.IntegerLiteral):
            return
        xwu__rneq = idx.literal_value
        if isinstance(xwu__rneq, int):
            ytk__bvqt = tup.types[xwu__rneq]
        elif isinstance(xwu__rneq, slice):
            ytk__bvqt = types.BaseTuple.from_types(tup.types[xwu__rneq])
        return signature(ytk__bvqt, *args)


GetItemTuple.prefer_literal = True


@lower_builtin(operator.getitem, types.BaseTuple, types.IntegerLiteral)
@lower_builtin(operator.getitem, types.BaseTuple, types.SliceLiteral)
def getitem_tuple_lower(context, builder, sig, args):
    tlhu__tkr, idx = sig.args
    idx = idx.literal_value
    tup, zvl__tupjy = args
    if isinstance(idx, int):
        if idx < 0:
            idx += len(tlhu__tkr)
        if not 0 <= idx < len(tlhu__tkr):
            raise IndexError('cannot index at %d in %s' % (idx, tlhu__tkr))
        rmcg__mxi = builder.extract_value(tup, idx)
    elif isinstance(idx, slice):
        mja__otyi = cgutils.unpack_tuple(builder, tup)[idx]
        rmcg__mxi = context.make_tuple(builder, sig.return_type, mja__otyi)
    else:
        raise NotImplementedError('unexpected index %r for %s' % (idx, sig.
            args[0]))
    return impl_ret_borrowed(context, builder, sig.return_type, rmcg__mxi)


def join_dummy(left_df, right_df, left_on, right_on, how, suffix_x,
    suffix_y, is_join, indicator, _bodo_na_equal, gen_cond):
    return left_df


@infer_global(join_dummy)
class JoinTyper(AbstractTemplate):

    def generic(self, args, kws):
        from bodo.hiframes.pd_dataframe_ext import DataFrameType
        from bodo.utils.typing import is_overload_str
        assert not kws
        (left_df, right_df, left_on, right_on, zqxm__jjg, suffix_x,
            suffix_y, is_join, indicator, zvl__tupjy, zvl__tupjy) = args
        how = get_overload_const_str(zqxm__jjg)
        if how == 'cross':
            data = left_df.data + right_df.data
            columns = left_df.columns + right_df.columns
            xwyc__xgo = DataFrameType(data, RangeIndexType(types.none),
                columns, is_table_format=True)
            return signature(xwyc__xgo, *args)
        left_on = get_overload_const_list(left_on)
        right_on = get_overload_const_list(right_on)
        jmvgg__aelpn = {ojaae__obyr: i for i, ojaae__obyr in enumerate(left_on)
            }
        myqi__untib = {ojaae__obyr: i for i, ojaae__obyr in enumerate(right_on)
            }
        rhwo__rbzz = set(left_on) & set(right_on)
        fep__gtdog = set(left_df.columns) & set(right_df.columns)
        uuf__dfja = fep__gtdog - rhwo__rbzz
        dbex__hjood = '$_bodo_index_' in left_on
        ivscm__qsav = '$_bodo_index_' in right_on
        ofwdc__yzi = how in {'left', 'outer'}
        fyqr__pzeef = how in {'right', 'outer'}
        columns = []
        data = []
        if dbex__hjood or ivscm__qsav:
            if dbex__hjood:
                uiy__uioe = bodo.utils.typing.get_index_data_arr_types(left_df
                    .index)[0]
            else:
                uiy__uioe = left_df.data[left_df.column_index[left_on[0]]]
            if ivscm__qsav:
                jck__vdaq = bodo.utils.typing.get_index_data_arr_types(right_df
                    .index)[0]
            else:
                jck__vdaq = right_df.data[right_df.column_index[right_on[0]]]
        if dbex__hjood and not ivscm__qsav and not is_join.literal_value:
            yhr__nvud = right_on[0]
            if yhr__nvud in left_df.column_index:
                columns.append(yhr__nvud)
                if (jck__vdaq == bodo.dict_str_arr_type and uiy__uioe ==
                    bodo.string_array_type):
                    cmg__mucyd = bodo.string_array_type
                else:
                    cmg__mucyd = jck__vdaq
                data.append(cmg__mucyd)
        if ivscm__qsav and not dbex__hjood and not is_join.literal_value:
            hhtqc__jlj = left_on[0]
            if hhtqc__jlj in right_df.column_index:
                columns.append(hhtqc__jlj)
                if (uiy__uioe == bodo.dict_str_arr_type and jck__vdaq ==
                    bodo.string_array_type):
                    cmg__mucyd = bodo.string_array_type
                else:
                    cmg__mucyd = uiy__uioe
                data.append(cmg__mucyd)
        for gvxkb__izdso, lxk__fpp in zip(left_df.data, left_df.columns):
            columns.append(str(lxk__fpp) + suffix_x.literal_value if 
                lxk__fpp in uuf__dfja else lxk__fpp)
            if lxk__fpp in rhwo__rbzz:
                if gvxkb__izdso == bodo.dict_str_arr_type:
                    gvxkb__izdso = right_df.data[right_df.column_index[
                        lxk__fpp]]
                data.append(gvxkb__izdso)
            else:
                if (gvxkb__izdso == bodo.dict_str_arr_type and lxk__fpp in
                    jmvgg__aelpn):
                    if ivscm__qsav:
                        gvxkb__izdso = jck__vdaq
                    else:
                        sksjc__bajv = jmvgg__aelpn[lxk__fpp]
                        bebv__yzkr = right_on[sksjc__bajv]
                        gvxkb__izdso = right_df.data[right_df.column_index[
                            bebv__yzkr]]
                if fyqr__pzeef:
                    gvxkb__izdso = to_nullable_type(gvxkb__izdso)
                data.append(gvxkb__izdso)
        for gvxkb__izdso, lxk__fpp in zip(right_df.data, right_df.columns):
            if lxk__fpp not in rhwo__rbzz:
                columns.append(str(lxk__fpp) + suffix_y.literal_value if 
                    lxk__fpp in uuf__dfja else lxk__fpp)
                if (gvxkb__izdso == bodo.dict_str_arr_type and lxk__fpp in
                    myqi__untib):
                    if dbex__hjood:
                        gvxkb__izdso = uiy__uioe
                    else:
                        sksjc__bajv = myqi__untib[lxk__fpp]
                        bcft__kvf = left_on[sksjc__bajv]
                        gvxkb__izdso = left_df.data[left_df.column_index[
                            bcft__kvf]]
                if ofwdc__yzi:
                    gvxkb__izdso = to_nullable_type(gvxkb__izdso)
                data.append(gvxkb__izdso)
        cqerg__jpyx = get_overload_const_bool(indicator)
        if cqerg__jpyx:
            columns.append('_merge')
            data.append(bodo.CategoricalArrayType(bodo.PDCategoricalDtype((
                'left_only', 'right_only', 'both'), bodo.string_type, False)))
        index_typ = RangeIndexType(types.none)
        yhxtp__utzx = False
        if dbex__hjood and ivscm__qsav and not is_overload_str(how, 'asof'):
            index_typ = left_df.index
            yhxtp__utzx = True
        elif dbex__hjood and not ivscm__qsav:
            index_typ = right_df.index
            yhxtp__utzx = True
        elif ivscm__qsav and not dbex__hjood:
            index_typ = left_df.index
            yhxtp__utzx = True
        if yhxtp__utzx and isinstance(index_typ, bodo.hiframes.pd_index_ext
            .RangeIndexType):
            index_typ = bodo.hiframes.pd_index_ext.NumericIndexType(types.int64
                )
        xwyc__xgo = DataFrameType(tuple(data), index_typ, tuple(columns),
            is_table_format=True)
        return signature(xwyc__xgo, *args)


JoinTyper._no_unliteral = True


@lower_builtin(join_dummy, types.VarArg(types.Any))
def lower_join_dummy(context, builder, sig, args):
    zxonr__nvk = cgutils.create_struct_proxy(sig.return_type)(context, builder)
    return zxonr__nvk._getvalue()


@overload(pd.concat, inline='always', no_unliteral=True)
def concat_overload(objs, axis=0, join='outer', join_axes=None,
    ignore_index=False, keys=None, levels=None, names=None,
    verify_integrity=False, sort=None, copy=True):
    if not is_overload_constant_int(axis):
        raise BodoError("pd.concat(): 'axis' should be a constant integer")
    if not is_overload_constant_bool(ignore_index):
        raise BodoError(
            "pd.concat(): 'ignore_index' should be a constant boolean")
    axis = get_overload_const_int(axis)
    ignore_index = is_overload_true(ignore_index)
    kohq__aknrl = dict(join=join, join_axes=join_axes, keys=keys, levels=
        levels, names=names, verify_integrity=verify_integrity, sort=sort,
        copy=copy)
    xgm__klqg = dict(join='outer', join_axes=None, keys=None, levels=None,
        names=None, verify_integrity=False, sort=None, copy=True)
    check_unsupported_args('pandas.concat', kohq__aknrl, xgm__klqg,
        package_name='pandas', module_name='General')
    llvq__jarb = """def impl(objs, axis=0, join='outer', join_axes=None, ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=None, copy=True):
"""
    if axis == 1:
        if not isinstance(objs, types.BaseTuple):
            raise_bodo_error(
                'Only tuple argument for pd.concat(axis=1) expected')
        index = (
            'bodo.hiframes.pd_index_ext.init_range_index(0, len(objs[0]), 1, None)'
            )
        wdgry__opc = 0
        dkikk__jus = []
        names = []
        for i, unl__vzig in enumerate(objs.types):
            assert isinstance(unl__vzig, (SeriesType, DataFrameType))
            check_runtime_cols_unsupported(unl__vzig, 'pandas.concat()')
            if isinstance(unl__vzig, SeriesType):
                names.append(str(wdgry__opc))
                wdgry__opc += 1
                dkikk__jus.append(
                    'bodo.hiframes.pd_series_ext.get_series_data(objs[{}])'
                    .format(i))
            else:
                names.extend(unl__vzig.columns)
                for amvs__flk in range(len(unl__vzig.data)):
                    dkikk__jus.append(
                        'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(objs[{}], {})'
                        .format(i, amvs__flk))
        return bodo.hiframes.dataframe_impl._gen_init_df(llvq__jarb, names,
            ', '.join(dkikk__jus), index)
    if axis != 0:
        raise_bodo_error('pd.concat(): axis must be 0 or 1')
    if isinstance(objs, types.BaseTuple) and isinstance(objs.types[0],
        DataFrameType):
        assert all(isinstance(vsqe__ksi, DataFrameType) for vsqe__ksi in
            objs.types)
        tvh__lshej = []
        for df in objs.types:
            check_runtime_cols_unsupported(df, 'pandas.concat()')
            tvh__lshej.extend(df.columns)
        tvh__lshej = list(dict.fromkeys(tvh__lshej).keys())
        jwve__kuj = {}
        for wdgry__opc, ojaae__obyr in enumerate(tvh__lshej):
            for i, df in enumerate(objs.types):
                if ojaae__obyr in df.column_index:
                    jwve__kuj[f'arr_typ{wdgry__opc}'] = df.data[df.
                        column_index[ojaae__obyr]]
                    break
        assert len(jwve__kuj) == len(tvh__lshej)
        kbc__zzcp = []
        for wdgry__opc, ojaae__obyr in enumerate(tvh__lshej):
            args = []
            for i, df in enumerate(objs.types):
                if ojaae__obyr in df.column_index:
                    ubs__rdp = df.column_index[ojaae__obyr]
                    args.append(
                        'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(objs[{}], {})'
                        .format(i, ubs__rdp))
                else:
                    args.append(
                        'bodo.libs.array_kernels.gen_na_array(len(objs[{}]), arr_typ{})'
                        .format(i, wdgry__opc))
            llvq__jarb += ('  A{} = bodo.libs.array_kernels.concat(({},))\n'
                .format(wdgry__opc, ', '.join(args)))
        if ignore_index:
            index = (
                'bodo.hiframes.pd_index_ext.init_range_index(0, len(A0), 1, None)'
                )
        else:
            index = (
                """bodo.utils.conversion.index_from_array(bodo.libs.array_kernels.concat(({},)))
"""
                .format(', '.join(
                'bodo.utils.conversion.index_to_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(objs[{}]))'
                .format(i) for i in range(len(objs.types)) if len(objs[i].
                columns) > 0)))
        return bodo.hiframes.dataframe_impl._gen_init_df(llvq__jarb,
            tvh__lshej, ', '.join('A{}'.format(i) for i in range(len(
            tvh__lshej))), index, jwve__kuj)
    if isinstance(objs, types.BaseTuple) and isinstance(objs.types[0],
        SeriesType):
        assert all(isinstance(vsqe__ksi, SeriesType) for vsqe__ksi in objs.
            types)
        llvq__jarb += ('  out_arr = bodo.libs.array_kernels.concat(({},))\n'
            .format(', '.join(
            'bodo.hiframes.pd_series_ext.get_series_data(objs[{}])'.format(
            i) for i in range(len(objs.types)))))
        if ignore_index:
            llvq__jarb += """  index = bodo.hiframes.pd_index_ext.init_range_index(0, len(out_arr), 1, None)
"""
        else:
            llvq__jarb += (
                """  index = bodo.utils.conversion.index_from_array(bodo.libs.array_kernels.concat(({},)))
"""
                .format(', '.join(
                'bodo.utils.conversion.index_to_array(bodo.hiframes.pd_series_ext.get_series_index(objs[{}]))'
                .format(i) for i in range(len(objs.types)))))
        llvq__jarb += (
            '  return bodo.hiframes.pd_series_ext.init_series(out_arr, index)\n'
            )
        nrsh__tdq = {}
        exec(llvq__jarb, {'bodo': bodo, 'np': np, 'numba': numba}, nrsh__tdq)
        return nrsh__tdq['impl']
    if isinstance(objs, types.List) and isinstance(objs.dtype, DataFrameType):
        check_runtime_cols_unsupported(objs.dtype, 'pandas.concat()')
        bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(objs.
            dtype, 'pandas.concat()')
        df_type = objs.dtype
        for wdgry__opc, ojaae__obyr in enumerate(df_type.columns):
            llvq__jarb += '  arrs{} = []\n'.format(wdgry__opc)
            llvq__jarb += '  for i in range(len(objs)):\n'
            llvq__jarb += '    df = objs[i]\n'
            llvq__jarb += (
                """    arrs{0}.append(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {0}))
"""
                .format(wdgry__opc))
            llvq__jarb += (
                '  out_arr{0} = bodo.libs.array_kernels.concat(arrs{0})\n'.
                format(wdgry__opc))
        if ignore_index:
            index = (
                'bodo.hiframes.pd_index_ext.init_range_index(0, len(out_arr0), 1, None)'
                )
        else:
            llvq__jarb += '  arrs_index = []\n'
            llvq__jarb += '  for i in range(len(objs)):\n'
            llvq__jarb += '    df = objs[i]\n'
            llvq__jarb += """    arrs_index.append(bodo.utils.conversion.index_to_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)))
"""
            if objs.dtype.index.name_typ == types.none:
                name = None
            else:
                name = objs.dtype.index.name_typ.literal_value
            index = f"""bodo.utils.conversion.index_from_array(bodo.libs.array_kernels.concat(arrs_index), {name!r})
"""
        return bodo.hiframes.dataframe_impl._gen_init_df(llvq__jarb,
            df_type.columns, ', '.join('out_arr{}'.format(i) for i in range
            (len(df_type.columns))), index)
    if isinstance(objs, types.List) and isinstance(objs.dtype, SeriesType):
        llvq__jarb += '  arrs = []\n'
        llvq__jarb += '  for i in range(len(objs)):\n'
        llvq__jarb += (
            '    arrs.append(bodo.hiframes.pd_series_ext.get_series_data(objs[i]))\n'
            )
        llvq__jarb += '  out_arr = bodo.libs.array_kernels.concat(arrs)\n'
        if ignore_index:
            llvq__jarb += """  index = bodo.hiframes.pd_index_ext.init_range_index(0, len(out_arr), 1, None)
"""
        else:
            llvq__jarb += '  arrs_index = []\n'
            llvq__jarb += '  for i in range(len(objs)):\n'
            llvq__jarb += '    S = objs[i]\n'
            llvq__jarb += """    arrs_index.append(bodo.utils.conversion.index_to_array(bodo.hiframes.pd_series_ext.get_series_index(S)))
"""
            llvq__jarb += """  index = bodo.utils.conversion.index_from_array(bodo.libs.array_kernels.concat(arrs_index))
"""
        llvq__jarb += (
            '  return bodo.hiframes.pd_series_ext.init_series(out_arr, index)\n'
            )
        nrsh__tdq = {}
        exec(llvq__jarb, {'bodo': bodo, 'np': np, 'numba': numba}, nrsh__tdq)
        return nrsh__tdq['impl']
    raise BodoError('pd.concat(): input type {} not supported yet'.format(objs)
        )


def sort_values_dummy(df, by, ascending, inplace, na_position,
    _bodo_chunk_bounds):
    pass


@infer_global(sort_values_dummy)
class SortDummyTyper(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        df = args[0]
        index = df.index
        if isinstance(index, bodo.hiframes.pd_index_ext.RangeIndexType):
            index = bodo.hiframes.pd_index_ext.NumericIndexType(types.int64)
        loc__lampv = df.copy(index=index)
        return signature(loc__lampv, *args)


SortDummyTyper._no_unliteral = True


@lower_builtin(sort_values_dummy, types.VarArg(types.Any))
def lower_sort_values_dummy(context, builder, sig, args):
    if sig.return_type == types.none:
        return
    dve__lsl = cgutils.create_struct_proxy(sig.return_type)(context, builder)
    return dve__lsl._getvalue()


@overload_method(DataFrameType, 'itertuples', inline='always', no_unliteral
    =True)
def itertuples_overload(df, index=True, name='Pandas'):
    check_runtime_cols_unsupported(df, 'DataFrame.itertuples()')
    kohq__aknrl = dict(index=index, name=name)
    xgm__klqg = dict(index=True, name='Pandas')
    check_unsupported_args('DataFrame.itertuples', kohq__aknrl, xgm__klqg,
        package_name='pandas', module_name='DataFrame')

    def _impl(df, index=True, name='Pandas'):
        return bodo.hiframes.pd_dataframe_ext.itertuples_dummy(df)
    return _impl


def itertuples_dummy(df):
    return df


@infer_global(itertuples_dummy)
class ItertuplesDummyTyper(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        df, = args
        assert 'Index' not in df.columns
        columns = ('Index',) + df.columns
        jwve__kuj = (types.Array(types.int64, 1, 'C'),) + df.data
        poi__bbelu = bodo.hiframes.dataframe_impl.DataFrameTupleIterator(
            columns, jwve__kuj)
        return signature(poi__bbelu, *args)


@lower_builtin(itertuples_dummy, types.VarArg(types.Any))
def lower_itertuples_dummy(context, builder, sig, args):
    dve__lsl = cgutils.create_struct_proxy(sig.return_type)(context, builder)
    return dve__lsl._getvalue()


def query_dummy(df, expr):
    return df.eval(expr)


@infer_global(query_dummy)
class QueryDummyTyper(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        return signature(SeriesType(types.bool_, index=RangeIndexType(types
            .none)), *args)


@lower_builtin(query_dummy, types.VarArg(types.Any))
def lower_query_dummy(context, builder, sig, args):
    dve__lsl = cgutils.create_struct_proxy(sig.return_type)(context, builder)
    return dve__lsl._getvalue()


def val_isin_dummy(S, vals):
    return S in vals


def val_notin_dummy(S, vals):
    return S not in vals


@infer_global(val_isin_dummy)
@infer_global(val_notin_dummy)
class ValIsinTyper(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        return signature(SeriesType(types.bool_, index=args[0].index), *args)


@lower_builtin(val_isin_dummy, types.VarArg(types.Any))
@lower_builtin(val_notin_dummy, types.VarArg(types.Any))
def lower_val_isin_dummy(context, builder, sig, args):
    dve__lsl = cgutils.create_struct_proxy(sig.return_type)(context, builder)
    return dve__lsl._getvalue()


@numba.generated_jit(nopython=True)
def pivot_impl(index_tup, columns_tup, values_tup, pivot_values,
    index_names, columns_name, value_names, check_duplicates=True,
    is_already_shuffled=False, _constant_pivot_values=None, parallel=False):
    if not is_overload_constant_bool(check_duplicates):
        raise BodoError(
            'pivot_impl(): check_duplicates must be a constant boolean')
    glblf__yxmr = get_overload_const_bool(check_duplicates)
    xtmtq__walmx = not get_overload_const_bool(is_already_shuffled)
    lpsj__pejyf = not is_overload_none(_constant_pivot_values)
    index_names = index_names.instance_type if isinstance(index_names,
        types.TypeRef) else index_names
    columns_name = columns_name.instance_type if isinstance(columns_name,
        types.TypeRef) else columns_name
    value_names = value_names.instance_type if isinstance(value_names,
        types.TypeRef) else value_names
    _constant_pivot_values = (_constant_pivot_values.instance_type if
        isinstance(_constant_pivot_values, types.TypeRef) else
        _constant_pivot_values)
    apecn__biy = len(value_names) > 1
    bdqis__kmnie = None
    zaddl__kzs = None
    yunk__hjf = None
    dwk__yha = None
    fwtd__imsk = isinstance(values_tup, types.UniTuple)
    if fwtd__imsk:
        jwu__nljh = [to_str_arr_if_dict_array(to_nullable_type(values_tup.
            dtype))]
    else:
        jwu__nljh = [to_str_arr_if_dict_array(to_nullable_type(rblat__bnz)) for
            rblat__bnz in values_tup]
    llvq__jarb = 'def impl(\n'
    llvq__jarb += """    index_tup, columns_tup, values_tup, pivot_values, index_names, columns_name, value_names, check_duplicates=True, is_already_shuffled=False, _constant_pivot_values=None, parallel=False
"""
    llvq__jarb += '):\n'
    llvq__jarb += (
        "    ev = tracing.Event('pivot_impl', is_parallel=parallel)\n")
    if xtmtq__walmx:
        llvq__jarb += '    if parallel:\n'
        llvq__jarb += (
            "        ev_shuffle = tracing.Event('shuffle_pivot_index')\n")
        tord__nflgy = ', '.join([f'array_to_info(index_tup[{i}])' for i in
            range(len(index_tup))] + [f'array_to_info(columns_tup[{i}])' for
            i in range(len(columns_tup))] + [
            f'array_to_info(values_tup[{i}])' for i in range(len(values_tup))])
        llvq__jarb += f'        info_list = [{tord__nflgy}]\n'
        llvq__jarb += '        cpp_table = arr_info_list_to_table(info_list)\n'
        llvq__jarb += f"""        out_cpp_table = shuffle_table(cpp_table, {len(index_tup)}, parallel, 0)
"""
        gwgx__pnlf = ', '.join([
            f'info_to_array(info_from_table(out_cpp_table, {i}), index_tup[{i}])'
             for i in range(len(index_tup))])
        pifv__zoioz = ', '.join([
            f'info_to_array(info_from_table(out_cpp_table, {i + len(index_tup)}), columns_tup[{i}])'
             for i in range(len(columns_tup))])
        ary__lmz = ', '.join([
            f'info_to_array(info_from_table(out_cpp_table, {i + len(index_tup) + len(columns_tup)}), values_tup[{i}])'
             for i in range(len(values_tup))])
        llvq__jarb += f'        index_tup = ({gwgx__pnlf},)\n'
        llvq__jarb += f'        columns_tup = ({pifv__zoioz},)\n'
        llvq__jarb += f'        values_tup = ({ary__lmz},)\n'
        llvq__jarb += '        delete_table(cpp_table)\n'
        llvq__jarb += '        delete_table(out_cpp_table)\n'
        llvq__jarb += '        ev_shuffle.finalize()\n'
    llvq__jarb += '    columns_arr = columns_tup[0]\n'
    if fwtd__imsk:
        llvq__jarb += '    values_arrs = [arr for arr in values_tup]\n'
    llvq__jarb += (
        "    ev_unique = tracing.Event('pivot_unique_index_map', is_parallel=parallel)\n"
        )
    llvq__jarb += """    unique_index_arr_tup, row_vector = bodo.libs.array_ops.array_unique_vector_map(
"""
    llvq__jarb += '        index_tup\n'
    llvq__jarb += '    )\n'
    llvq__jarb += '    n_rows = len(unique_index_arr_tup[0])\n'
    llvq__jarb += '    num_values_arrays = len(values_tup)\n'
    llvq__jarb += '    n_unique_pivots = len(pivot_values)\n'
    if fwtd__imsk:
        llvq__jarb += '    n_cols = num_values_arrays * n_unique_pivots\n'
    else:
        llvq__jarb += '    n_cols = n_unique_pivots\n'
    llvq__jarb += '    col_map = {}\n'
    llvq__jarb += '    for i in range(n_unique_pivots):\n'
    llvq__jarb += '        if bodo.libs.array_kernels.isna(pivot_values, i):\n'
    llvq__jarb += '            raise ValueError(\n'
    llvq__jarb += """                "DataFrame.pivot(): NA values in 'columns' array not supported\"
"""
    llvq__jarb += '            )\n'
    llvq__jarb += '        col_map[pivot_values[i]] = i\n'
    llvq__jarb += '    ev_unique.finalize()\n'
    llvq__jarb += (
        "    ev_alloc = tracing.Event('pivot_alloc', is_parallel=parallel)\n")
    vmqd__cqqe = False
    for i, qbf__hpxv in enumerate(jwu__nljh):
        if is_str_arr_type(qbf__hpxv):
            vmqd__cqqe = True
            llvq__jarb += f"""    len_arrs_{i} = [np.zeros(n_rows, np.int64) for _ in range(n_cols)]
"""
            llvq__jarb += f'    total_lens_{i} = np.zeros(n_cols, np.int64)\n'
    if vmqd__cqqe:
        if glblf__yxmr:
            llvq__jarb += '    nbytes = (n_rows + 7) >> 3\n'
            llvq__jarb += """    seen_bitmaps = [np.zeros(nbytes, np.int8) for _ in range(n_unique_pivots)]
"""
        llvq__jarb += '    for i in range(len(columns_arr)):\n'
        llvq__jarb += '        col_name = columns_arr[i]\n'
        llvq__jarb += '        pivot_idx = col_map[col_name]\n'
        llvq__jarb += '        row_idx = row_vector[i]\n'
        if glblf__yxmr:
            llvq__jarb += '        seen_bitmap = seen_bitmaps[pivot_idx]\n'
            llvq__jarb += """        if bodo.libs.int_arr_ext.get_bit_bitmap_arr(seen_bitmap, row_idx):
"""
            llvq__jarb += """            raise ValueError("DataFrame.pivot(): 'index' contains duplicate entries for the same output column")
"""
            llvq__jarb += '        else:\n'
            llvq__jarb += """            bodo.libs.int_arr_ext.set_bit_to_arr(seen_bitmap, row_idx, 1)
"""
        if fwtd__imsk:
            llvq__jarb += '        for j in range(num_values_arrays):\n'
            llvq__jarb += (
                '            col_idx = (j * len(pivot_values)) + pivot_idx\n')
            llvq__jarb += '            len_arr = len_arrs_0[col_idx]\n'
            llvq__jarb += '            values_arr = values_arrs[j]\n'
            llvq__jarb += (
                '            if not bodo.libs.array_kernels.isna(values_arr, i):\n'
                )
            llvq__jarb += """                str_val_len = bodo.libs.str_arr_ext.get_str_arr_item_length(values_arr, i)
"""
            llvq__jarb += '                len_arr[row_idx] = str_val_len\n'
            llvq__jarb += (
                '                total_lens_0[col_idx] += str_val_len\n')
        else:
            for i, qbf__hpxv in enumerate(jwu__nljh):
                if is_str_arr_type(qbf__hpxv):
                    llvq__jarb += f"""        if not bodo.libs.array_kernels.isna(values_tup[{i}], i):
"""
                    llvq__jarb += f"""            str_val_len_{i} = bodo.libs.str_arr_ext.get_str_arr_item_length(values_tup[{i}], i)
"""
                    llvq__jarb += f"""            len_arrs_{i}[pivot_idx][row_idx] = str_val_len_{i}
"""
                    llvq__jarb += (
                        f'            total_lens_{i}[pivot_idx] += str_val_len_{i}\n'
                        )
    llvq__jarb += f"    ev_alloc.add_attribute('num_rows', n_rows)\n"
    for i, qbf__hpxv in enumerate(jwu__nljh):
        if is_str_arr_type(qbf__hpxv):
            llvq__jarb += f'    data_arrs_{i} = [\n'
            llvq__jarb += (
                '        bodo.libs.str_arr_ext.gen_na_str_array_lens(\n')
            llvq__jarb += (
                f'            n_rows, total_lens_{i}[i], len_arrs_{i}[i]\n')
            llvq__jarb += '        )\n'
            llvq__jarb += '        for i in range(n_cols)\n'
            llvq__jarb += '    ]\n'
            llvq__jarb += f'    if tracing.is_tracing():\n'
            llvq__jarb += '         for i in range(n_cols):\n'
            llvq__jarb += f"""            ev_alloc.add_attribute('total_str_chars_out_column_{i}_' + str(i), total_lens_{i}[i])
"""
        else:
            llvq__jarb += f'    data_arrs_{i} = [\n'
            llvq__jarb += f"""        bodo.libs.array_kernels.gen_na_array(n_rows, data_arr_typ_{i})
"""
            llvq__jarb += '        for _ in range(n_cols)\n'
            llvq__jarb += '    ]\n'
    if not vmqd__cqqe and glblf__yxmr:
        llvq__jarb += '    nbytes = (n_rows + 7) >> 3\n'
        llvq__jarb += """    seen_bitmaps = [np.zeros(nbytes, np.int8) for _ in range(n_unique_pivots)]
"""
    llvq__jarb += '    ev_alloc.finalize()\n'
    llvq__jarb += (
        "    ev_fill = tracing.Event('pivot_fill_data', is_parallel=parallel)\n"
        )
    llvq__jarb += '    for i in range(len(columns_arr)):\n'
    llvq__jarb += '        col_name = columns_arr[i]\n'
    llvq__jarb += '        pivot_idx = col_map[col_name]\n'
    llvq__jarb += '        row_idx = row_vector[i]\n'
    if not vmqd__cqqe and glblf__yxmr:
        llvq__jarb += '        seen_bitmap = seen_bitmaps[pivot_idx]\n'
        llvq__jarb += """        if bodo.libs.int_arr_ext.get_bit_bitmap_arr(seen_bitmap, row_idx):
"""
        llvq__jarb += """            raise ValueError("DataFrame.pivot(): 'index' contains duplicate entries for the same output column")
"""
        llvq__jarb += '        else:\n'
        llvq__jarb += (
            '            bodo.libs.int_arr_ext.set_bit_to_arr(seen_bitmap, row_idx, 1)\n'
            )
    if fwtd__imsk:
        llvq__jarb += '        for j in range(num_values_arrays):\n'
        llvq__jarb += (
            '            col_idx = (j * len(pivot_values)) + pivot_idx\n')
        llvq__jarb += '            col_arr = data_arrs_0[col_idx]\n'
        llvq__jarb += '            values_arr = values_arrs[j]\n'
        llvq__jarb += """            bodo.libs.array_kernels.copy_array_element(col_arr, row_idx, values_arr, i)
"""
    else:
        for i, qbf__hpxv in enumerate(jwu__nljh):
            llvq__jarb += f'        col_arr_{i} = data_arrs_{i}[pivot_idx]\n'
            llvq__jarb += f"""        bodo.libs.array_kernels.copy_array_element(col_arr_{i}, row_idx, values_tup[{i}], i)
"""
    if len(index_names) == 1:
        llvq__jarb += """    index = bodo.utils.conversion.index_from_array(unique_index_arr_tup[0], index_names_lit)
"""
        bdqis__kmnie = index_names.meta[0]
    else:
        llvq__jarb += """    index = bodo.hiframes.pd_multi_index_ext.init_multi_index(unique_index_arr_tup, index_names_lit, None)
"""
        bdqis__kmnie = tuple(index_names.meta)
    llvq__jarb += f'    if tracing.is_tracing():\n'
    llvq__jarb += f'        index_nbytes = index.nbytes\n'
    llvq__jarb += f"        ev.add_attribute('index_nbytes', index_nbytes)\n"
    if not lpsj__pejyf:
        yunk__hjf = columns_name.meta[0]
        if apecn__biy:
            llvq__jarb += (
                f'    num_rows = {len(value_names)} * len(pivot_values)\n')
            zaddl__kzs = value_names.meta
            if all(isinstance(ojaae__obyr, str) for ojaae__obyr in zaddl__kzs):
                zaddl__kzs = pd.array(zaddl__kzs, 'string')
            elif all(isinstance(ojaae__obyr, int) for ojaae__obyr in zaddl__kzs
                ):
                zaddl__kzs = np.array(zaddl__kzs, 'int64')
            else:
                raise BodoError(
                    f"pivot(): column names selected for 'values' must all share a common int or string type. Please convert your names to a common type using DataFrame.rename()"
                    )
            if isinstance(zaddl__kzs.dtype, pd.StringDtype):
                llvq__jarb += '    total_chars = 0\n'
                llvq__jarb += f'    for i in range({len(value_names)}):\n'
                llvq__jarb += """        value_name_str_len = bodo.libs.str_arr_ext.get_str_arr_item_length(value_names_lit, i)
"""
                llvq__jarb += '        total_chars += value_name_str_len\n'
                llvq__jarb += """    new_value_names = bodo.libs.str_arr_ext.pre_alloc_string_array(num_rows, total_chars * len(pivot_values))
"""
            else:
                llvq__jarb += """    new_value_names = bodo.utils.utils.alloc_type(num_rows, value_names_lit, (-1,))
"""
            if is_str_arr_type(pivot_values):
                llvq__jarb += '    total_chars = 0\n'
                llvq__jarb += '    for i in range(len(pivot_values)):\n'
                llvq__jarb += """        pivot_val_str_len = bodo.libs.str_arr_ext.get_str_arr_item_length(pivot_values, i)
"""
                llvq__jarb += '        total_chars += pivot_val_str_len\n'
                llvq__jarb += f"""    new_pivot_values = bodo.libs.str_arr_ext.pre_alloc_string_array(num_rows, total_chars * {len(value_names)})
"""
            else:
                llvq__jarb += """    new_pivot_values = bodo.utils.utils.alloc_type(num_rows, pivot_values, (-1,))
"""
            llvq__jarb += f'    for i in range({len(value_names)}):\n'
            llvq__jarb += '        for j in range(len(pivot_values)):\n'
            llvq__jarb += """            new_value_names[(i * len(pivot_values)) + j] = value_names_lit[i]
"""
            llvq__jarb += """            new_pivot_values[(i * len(pivot_values)) + j] = pivot_values[j]
"""
            llvq__jarb += """    column_index = bodo.hiframes.pd_multi_index_ext.init_multi_index((new_value_names, new_pivot_values), (None, columns_name_lit), None)
"""
        else:
            llvq__jarb += """    column_index =  bodo.utils.conversion.index_from_array(pivot_values, columns_name_lit)
"""
    llvq__jarb += '    ev_fill.finalize()\n'
    kqz__qxxd = None
    if lpsj__pejyf:
        if apecn__biy:
            onj__ardi = []
            for wwhb__rujs in _constant_pivot_values.meta:
                for amh__djs in value_names.meta:
                    onj__ardi.append((wwhb__rujs, amh__djs))
            column_names = tuple(onj__ardi)
        else:
            column_names = tuple(_constant_pivot_values.meta)
        dwk__yha = ColNamesMetaType(column_names)
        netwk__ozz = []
        for rblat__bnz in jwu__nljh:
            netwk__ozz.extend([rblat__bnz] * len(_constant_pivot_values))
        ubw__ibui = tuple(netwk__ozz)
        kqz__qxxd = TableType(ubw__ibui)
        llvq__jarb += (
            f'    table = bodo.hiframes.table.init_table(table_type, False)\n')
        llvq__jarb += (
            f'    table = bodo.hiframes.table.set_table_len(table, n_rows)\n')
        for i, rblat__bnz in enumerate(jwu__nljh):
            llvq__jarb += f"""    table = bodo.hiframes.table.set_table_block(table, data_arrs_{i}, {kqz__qxxd.type_to_blk[rblat__bnz]})
"""
        llvq__jarb += (
            '    result = bodo.hiframes.pd_dataframe_ext.init_dataframe(\n')
        llvq__jarb += '        (table,), index, columns_typ\n'
        llvq__jarb += '    )\n'
    else:
        wcipl__dgb = ', '.join(f'data_arrs_{i}' for i in range(len(jwu__nljh)))
        llvq__jarb += f"""    table = bodo.hiframes.table.init_runtime_table_from_lists(({wcipl__dgb},), n_rows)
"""
        llvq__jarb += (
            '    result = bodo.hiframes.pd_dataframe_ext.init_runtime_cols_dataframe(\n'
            )
        llvq__jarb += '        (table,), index, column_index\n'
        llvq__jarb += '    )\n'
    llvq__jarb += '    ev.finalize()\n'
    llvq__jarb += '    return result\n'
    nrsh__tdq = {}
    hxxd__wrbdf = {f'data_arr_typ_{i}': qbf__hpxv for i, qbf__hpxv in
        enumerate(jwu__nljh)}
    jyyzi__xyde = {'bodo': bodo, 'np': np, 'array_to_info': array_to_info,
        'arr_info_list_to_table': arr_info_list_to_table, 'shuffle_table':
        shuffle_table, 'info_to_array': info_to_array, 'delete_table':
        delete_table, 'info_from_table': info_from_table, 'table_type':
        kqz__qxxd, 'columns_typ': dwk__yha, 'index_names_lit': bdqis__kmnie,
        'value_names_lit': zaddl__kzs, 'columns_name_lit': yunk__hjf, **
        hxxd__wrbdf, 'tracing': tracing}
    exec(llvq__jarb, jyyzi__xyde, nrsh__tdq)
    impl = nrsh__tdq['impl']
    return impl


def gen_pandas_parquet_metadata(column_names, data_types, index,
    write_non_range_index_to_metadata, write_rangeindex_to_metadata,
    partition_cols=None, is_runtime_columns=False):
    niobw__qgmfh = {}
    niobw__qgmfh['columns'] = []
    if partition_cols is None:
        partition_cols = []
    for col_name, dbx__kmoqj in zip(column_names, data_types):
        if col_name in partition_cols:
            continue
        qrcfw__iygy = None
        if isinstance(dbx__kmoqj, bodo.DatetimeArrayType):
            wtrw__sbcbg = 'datetimetz'
            luygq__lxw = 'datetime64[ns]'
            if isinstance(dbx__kmoqj.tz, int):
                niij__xkg = (bodo.libs.pd_datetime_arr_ext.
                    nanoseconds_to_offset(dbx__kmoqj.tz))
            else:
                niij__xkg = pd.DatetimeTZDtype(tz=dbx__kmoqj.tz).tz
            qrcfw__iygy = {'timezone': pa.lib.tzinfo_to_string(niij__xkg)}
        elif isinstance(dbx__kmoqj, types.Array
            ) or dbx__kmoqj == boolean_array:
            wtrw__sbcbg = luygq__lxw = dbx__kmoqj.dtype.name
            if luygq__lxw.startswith('datetime'):
                wtrw__sbcbg = 'datetime'
        elif is_str_arr_type(dbx__kmoqj):
            wtrw__sbcbg = 'unicode'
            luygq__lxw = 'object'
        elif dbx__kmoqj == binary_array_type:
            wtrw__sbcbg = 'bytes'
            luygq__lxw = 'object'
        elif isinstance(dbx__kmoqj, DecimalArrayType):
            wtrw__sbcbg = luygq__lxw = 'object'
        elif isinstance(dbx__kmoqj, IntegerArrayType):
            vjaud__vbyfi = dbx__kmoqj.dtype.name
            if vjaud__vbyfi.startswith('int'):
                luygq__lxw = 'Int' + vjaud__vbyfi[3:]
            elif vjaud__vbyfi.startswith('uint'):
                luygq__lxw = 'UInt' + vjaud__vbyfi[4:]
            else:
                if is_runtime_columns:
                    col_name = 'Runtime determined column of type'
                raise BodoError(
                    'to_parquet(): unknown dtype in nullable Integer column {} {}'
                    .format(col_name, dbx__kmoqj))
            wtrw__sbcbg = dbx__kmoqj.dtype.name
        elif isinstance(dbx__kmoqj, bodo.FloatingArrayType):
            vjaud__vbyfi = dbx__kmoqj.dtype.name
            wtrw__sbcbg = vjaud__vbyfi
            luygq__lxw = vjaud__vbyfi.capitalize()
        elif dbx__kmoqj == datetime_date_array_type:
            wtrw__sbcbg = 'datetime'
            luygq__lxw = 'object'
        elif isinstance(dbx__kmoqj, TimeArrayType):
            wtrw__sbcbg = 'datetime'
            luygq__lxw = 'object'
        elif isinstance(dbx__kmoqj, (StructArrayType, ArrayItemArrayType)):
            wtrw__sbcbg = 'object'
            luygq__lxw = 'object'
        else:
            if is_runtime_columns:
                col_name = 'Runtime determined column of type'
            raise BodoError(
                'to_parquet(): unsupported column type for metadata generation : {} {}'
                .format(col_name, dbx__kmoqj))
        ftmj__jfjd = {'name': col_name, 'field_name': col_name,
            'pandas_type': wtrw__sbcbg, 'numpy_type': luygq__lxw,
            'metadata': qrcfw__iygy}
        niobw__qgmfh['columns'].append(ftmj__jfjd)
    if write_non_range_index_to_metadata:
        if isinstance(index, MultiIndexType):
            raise BodoError('to_parquet: MultiIndex not supported yet')
        if 'none' in index.name:
            ajm__bybi = '__index_level_0__'
            kxq__gzum = None
        else:
            ajm__bybi = '%s'
            kxq__gzum = '%s'
        niobw__qgmfh['index_columns'] = [ajm__bybi]
        niobw__qgmfh['columns'].append({'name': kxq__gzum, 'field_name':
            ajm__bybi, 'pandas_type': index.pandas_type_name, 'numpy_type':
            index.numpy_type_name, 'metadata': None})
    elif write_rangeindex_to_metadata:
        niobw__qgmfh['index_columns'] = [{'kind': 'range', 'name': '%s',
            'start': '%d', 'stop': '%d', 'step': '%d'}]
    else:
        niobw__qgmfh['index_columns'] = []
    niobw__qgmfh['pandas_version'] = pd.__version__
    return niobw__qgmfh


@overload_method(DataFrameType, 'to_parquet', no_unliteral=True)
def to_parquet_overload(df, path, engine='auto', compression='snappy',
    index=None, partition_cols=None, storage_options=None, row_group_size=-
    1, _bodo_file_prefix='part-', _bodo_timestamp_tz=None, _is_parallel=False):
    check_unsupported_args('DataFrame.to_parquet', {'storage_options':
        storage_options}, {'storage_options': None}, package_name='pandas',
        module_name='IO')
    if df.has_runtime_cols and not is_overload_none(partition_cols):
        raise BodoError(
            f"DataFrame.to_parquet(): Providing 'partition_cols' on DataFrames with columns determined at runtime is not yet supported. Please return the DataFrame to regular Python to update typing information."
            )
    if not is_overload_none(engine) and get_overload_const_str(engine) not in (
        'auto', 'pyarrow'):
        raise BodoError('DataFrame.to_parquet(): only pyarrow engine supported'
            )
    if not is_overload_none(compression) and get_overload_const_str(compression
        ) not in {'snappy', 'gzip', 'brotli'}:
        raise BodoError('to_parquet(): Unsupported compression: ' + str(
            get_overload_const_str(compression)))
    if not is_overload_none(partition_cols):
        partition_cols = get_overload_const_list(partition_cols)
        beun__ngf = []
        for qnle__tna in partition_cols:
            try:
                idx = df.columns.index(qnle__tna)
            except ValueError as dldvg__vaw:
                raise BodoError(
                    f'Partition column {qnle__tna} is not in dataframe')
            beun__ngf.append(idx)
    else:
        partition_cols = None
    if not is_overload_none(index) and not is_overload_constant_bool(index):
        raise BodoError('to_parquet(): index must be a constant bool or None')
    if not is_overload_int(row_group_size):
        raise BodoError('to_parquet(): row_group_size must be integer')
    if not is_overload_none(_bodo_timestamp_tz) and (not
        is_overload_constant_str(_bodo_timestamp_tz) or not
        get_overload_const_str(_bodo_timestamp_tz)):
        raise BodoError(
            'to_parquet(): _bodo_timestamp_tz must be None or a constant string'
            )
    from bodo.io.parquet_pio import parquet_write_table_cpp, parquet_write_table_partitioned_cpp
    czl__yob = isinstance(df.index, bodo.hiframes.pd_index_ext.RangeIndexType)
    qadd__iwgn = df.index is not None and (is_overload_true(_is_parallel) or
        not is_overload_true(_is_parallel) and not czl__yob)
    write_non_range_index_to_metadata = is_overload_true(index
        ) or is_overload_none(index) and (not czl__yob or is_overload_true(
        _is_parallel))
    write_rangeindex_to_metadata = is_overload_none(index
        ) and czl__yob and not is_overload_true(_is_parallel)
    if df.has_runtime_cols:
        if isinstance(df.runtime_colname_typ, MultiIndexType):
            raise BodoError(
                'DataFrame.to_parquet(): Not supported with MultiIndex runtime column names. Please return the DataFrame to regular Python to update typing information.'
                )
        if not isinstance(df.runtime_colname_typ, bodo.hiframes.
            pd_index_ext.StringIndexType):
            raise BodoError(
                'DataFrame.to_parquet(): parquet must have string column names. Please return the DataFrame with runtime column names to regular Python to modify column names.'
                )
        mavoe__lkh = df.runtime_data_types
        pccu__elv = len(mavoe__lkh)
        qrcfw__iygy = gen_pandas_parquet_metadata([''] * pccu__elv,
            mavoe__lkh, df.index, write_non_range_index_to_metadata,
            write_rangeindex_to_metadata, partition_cols=partition_cols,
            is_runtime_columns=True)
        nnh__wkt = qrcfw__iygy['columns'][:pccu__elv]
        qrcfw__iygy['columns'] = qrcfw__iygy['columns'][pccu__elv:]
        nnh__wkt = [json.dumps(pgi__imye).replace('""', '{0}') for
            pgi__imye in nnh__wkt]
        pdxv__dzz = json.dumps(qrcfw__iygy)
        ljvi__hsc = '"columns": ['
        fxu__osp = pdxv__dzz.find(ljvi__hsc)
        if fxu__osp == -1:
            raise BodoError(
                'DataFrame.to_parquet(): Unexpected metadata string for runtime columns.  Please return the DataFrame to regular Python to update typing information.'
                )
        tcel__wid = fxu__osp + len(ljvi__hsc)
        ldhso__cddqz = pdxv__dzz[:tcel__wid]
        pdxv__dzz = pdxv__dzz[tcel__wid:]
        rnqwb__gwq = len(qrcfw__iygy['columns'])
    else:
        pdxv__dzz = json.dumps(gen_pandas_parquet_metadata(df.columns, df.
            data, df.index, write_non_range_index_to_metadata,
            write_rangeindex_to_metadata, partition_cols=partition_cols,
            is_runtime_columns=False))
    if not is_overload_true(_is_parallel) and czl__yob:
        pdxv__dzz = pdxv__dzz.replace('"%d"', '%d')
        if df.index.name == 'RangeIndexType(none)':
            pdxv__dzz = pdxv__dzz.replace('"%s"', '%s')
    if not df.is_table_format:
        dkikk__jus = ', '.join(
            'array_to_info(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {}))'
            .format(i) for i in range(len(df.columns)))
    llvq__jarb = """def df_to_parquet(df, path, engine='auto', compression='snappy', index=None, partition_cols=None, storage_options=None, row_group_size=-1, _bodo_file_prefix='part-', _bodo_timestamp_tz=None, _is_parallel=False):
"""
    if df.is_table_format:
        llvq__jarb += '    py_table = get_dataframe_table(df)\n'
        llvq__jarb += (
            '    table = py_table_to_cpp_table(py_table, py_table_typ)\n')
    else:
        llvq__jarb += '    info_list = [{}]\n'.format(dkikk__jus)
        llvq__jarb += '    table = arr_info_list_to_table(info_list)\n'
    if df.has_runtime_cols:
        llvq__jarb += '    columns_index = get_dataframe_column_names(df)\n'
        llvq__jarb += '    names_arr = index_to_array(columns_index)\n'
        llvq__jarb += '    col_names = array_to_info(names_arr)\n'
    else:
        llvq__jarb += '    col_names = array_to_info(col_names_arr)\n'
    if is_overload_true(index) or is_overload_none(index) and qadd__iwgn:
        llvq__jarb += """    index_col = array_to_info(index_to_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)))
"""
        pwq__oey = True
    else:
        llvq__jarb += '    index_col = array_to_info(np.empty(0))\n'
        pwq__oey = False
    if df.has_runtime_cols:
        llvq__jarb += '    columns_lst = []\n'
        llvq__jarb += '    num_cols = 0\n'
        for i in range(len(df.runtime_data_types)):
            llvq__jarb += f'    for _ in range(len(py_table.block_{i})):\n'
            llvq__jarb += f"""        columns_lst.append({nnh__wkt[i]!r}.replace('{{0}}', '"' + names_arr[num_cols] + '"'))
"""
            llvq__jarb += '        num_cols += 1\n'
        if rnqwb__gwq:
            llvq__jarb += "    columns_lst.append('')\n"
        llvq__jarb += '    columns_str = ", ".join(columns_lst)\n'
        llvq__jarb += ('    metadata = """' + ldhso__cddqz +
            '""" + columns_str + """' + pdxv__dzz + '"""\n')
    else:
        llvq__jarb += '    metadata = """' + pdxv__dzz + '"""\n'
    llvq__jarb += '    if compression is None:\n'
    llvq__jarb += "        compression = 'none'\n"
    llvq__jarb += '    if _bodo_timestamp_tz is None:\n'
    llvq__jarb += "        _bodo_timestamp_tz = ''\n"
    llvq__jarb += '    if df.index.name is not None:\n'
    llvq__jarb += '        name_ptr = df.index.name\n'
    llvq__jarb += '    else:\n'
    llvq__jarb += "        name_ptr = 'null'\n"
    llvq__jarb += f"""    bucket_region = bodo.io.fs_io.get_s3_bucket_region_njit(path, parallel=_is_parallel)
"""
    egu__xhkm = None
    if partition_cols:
        egu__xhkm = pd.array([col_name for col_name in df.columns if 
            col_name not in partition_cols])
        cmbt__tqy = ', '.join(
            f'array_to_info(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}).dtype.categories.values)'
             for i in range(len(df.columns)) if isinstance(df.data[i],
            CategoricalArrayType) and i in beun__ngf)
        if cmbt__tqy:
            llvq__jarb += '    cat_info_list = [{}]\n'.format(cmbt__tqy)
            llvq__jarb += (
                '    cat_table = arr_info_list_to_table(cat_info_list)\n')
        else:
            llvq__jarb += '    cat_table = table\n'
        llvq__jarb += (
            '    col_names_no_partitions = array_to_info(col_names_no_parts_arr)\n'
            )
        llvq__jarb += (
            f'    part_cols_idxs = np.array({beun__ngf}, dtype=np.int32)\n')
        llvq__jarb += (
            '    parquet_write_table_partitioned_cpp(unicode_to_utf8(path),\n')
        llvq__jarb += """                            table, col_names, col_names_no_partitions, cat_table,
"""
        llvq__jarb += (
            '                            part_cols_idxs.ctypes, len(part_cols_idxs),\n'
            )
        llvq__jarb += (
            '                            unicode_to_utf8(compression),\n')
        llvq__jarb += '                            _is_parallel,\n'
        llvq__jarb += (
            '                            unicode_to_utf8(bucket_region),\n')
        llvq__jarb += '                            row_group_size,\n'
        llvq__jarb += (
            '                            unicode_to_utf8(_bodo_file_prefix),\n'
            )
        llvq__jarb += (
            '                            unicode_to_utf8(_bodo_timestamp_tz))\n'
            )
        llvq__jarb += '    delete_table_decref_arrays(table)\n'
        llvq__jarb += '    delete_info_decref_array(index_col)\n'
        llvq__jarb += '    delete_info_decref_array(col_names_no_partitions)\n'
        llvq__jarb += '    delete_info_decref_array(col_names)\n'
        if cmbt__tqy:
            llvq__jarb += '    delete_table_decref_arrays(cat_table)\n'
    elif write_rangeindex_to_metadata:
        llvq__jarb += '    parquet_write_table_cpp(unicode_to_utf8(path),\n'
        llvq__jarb += (
            '                            table, col_names, index_col,\n')
        llvq__jarb += '                            ' + str(pwq__oey) + ',\n'
        llvq__jarb += (
            '                            unicode_to_utf8(metadata),\n')
        llvq__jarb += (
            '                            unicode_to_utf8(compression),\n')
        llvq__jarb += (
            '                            _is_parallel, 1, df.index.start,\n')
        llvq__jarb += (
            '                            df.index.stop, df.index.step,\n')
        llvq__jarb += (
            '                            unicode_to_utf8(name_ptr),\n')
        llvq__jarb += (
            '                            unicode_to_utf8(bucket_region),\n')
        llvq__jarb += '                            row_group_size,\n'
        llvq__jarb += (
            '                            unicode_to_utf8(_bodo_file_prefix),\n'
            )
        llvq__jarb += '                              False,\n'
        llvq__jarb += (
            '                            unicode_to_utf8(_bodo_timestamp_tz),\n'
            )
        llvq__jarb += '                              False)\n'
        llvq__jarb += '    delete_table_decref_arrays(table)\n'
        llvq__jarb += '    delete_info_decref_array(index_col)\n'
        llvq__jarb += '    delete_info_decref_array(col_names)\n'
    else:
        llvq__jarb += '    parquet_write_table_cpp(unicode_to_utf8(path),\n'
        llvq__jarb += (
            '                            table, col_names, index_col,\n')
        llvq__jarb += '                            ' + str(pwq__oey) + ',\n'
        llvq__jarb += (
            '                            unicode_to_utf8(metadata),\n')
        llvq__jarb += (
            '                            unicode_to_utf8(compression),\n')
        llvq__jarb += '                            _is_parallel, 0, 0, 0, 0,\n'
        llvq__jarb += (
            '                            unicode_to_utf8(name_ptr),\n')
        llvq__jarb += (
            '                            unicode_to_utf8(bucket_region),\n')
        llvq__jarb += '                            row_group_size,\n'
        llvq__jarb += (
            '                            unicode_to_utf8(_bodo_file_prefix),\n'
            )
        llvq__jarb += '                              False,\n'
        llvq__jarb += (
            '                            unicode_to_utf8(_bodo_timestamp_tz),\n'
            )
        llvq__jarb += '                              False)\n'
        llvq__jarb += '    delete_table_decref_arrays(table)\n'
        llvq__jarb += '    delete_info_decref_array(index_col)\n'
        llvq__jarb += '    delete_info_decref_array(col_names)\n'
    nrsh__tdq = {}
    if df.has_runtime_cols:
        hlad__rle = None
    else:
        for lxk__fpp in df.columns:
            if not isinstance(lxk__fpp, str):
                raise BodoError(
                    'DataFrame.to_parquet(): parquet must have string column names'
                    )
        hlad__rle = pd.array(df.columns)
    exec(llvq__jarb, {'np': np, 'bodo': bodo, 'unicode_to_utf8':
        unicode_to_utf8, 'array_to_info': array_to_info,
        'arr_info_list_to_table': arr_info_list_to_table,
        'str_arr_from_sequence': str_arr_from_sequence,
        'parquet_write_table_cpp': parquet_write_table_cpp,
        'parquet_write_table_partitioned_cpp':
        parquet_write_table_partitioned_cpp, 'index_to_array':
        index_to_array, 'delete_info_decref_array':
        delete_info_decref_array, 'delete_table_decref_arrays':
        delete_table_decref_arrays, 'col_names_arr': hlad__rle,
        'py_table_to_cpp_table': py_table_to_cpp_table, 'py_table_typ': df.
        table_type, 'get_dataframe_table': get_dataframe_table,
        'col_names_no_parts_arr': egu__xhkm, 'get_dataframe_column_names':
        get_dataframe_column_names, 'fix_arr_dtype': fix_arr_dtype,
        'decode_if_dict_array': decode_if_dict_array,
        'decode_if_dict_table': decode_if_dict_table}, nrsh__tdq)
    qexk__flw = nrsh__tdq['df_to_parquet']
    return qexk__flw


def to_sql_exception_guard(df, name, con, schema=None, if_exists='fail',
    index=True, index_label=None, chunksize=None, dtype=None, method=None,
    _is_table_create=False, _is_parallel=False):
    otar__uktcr = tracing.Event('to_sql_exception_guard', is_parallel=
        _is_parallel)
    aka__oyjd = 'all_ok'
    jsof__zbpj, enu__nsmma = bodo.ir.sql_ext.parse_dbtype(con)
    if _is_parallel and bodo.get_rank() == 0:
        lzq__xximc = 100
        if chunksize is None:
            jozg__lvmf = lzq__xximc
        else:
            jozg__lvmf = min(chunksize, lzq__xximc)
        if _is_table_create:
            df = df.iloc[:jozg__lvmf, :]
        else:
            df = df.iloc[jozg__lvmf:, :]
            if len(df) == 0:
                return aka__oyjd
    ugrr__qvc = df.columns
    try:
        if jsof__zbpj == 'oracle':
            import os
            import sqlalchemy as sa
            from sqlalchemy.dialects.oracle import VARCHAR2
            yghud__bgjl = os.environ.get('BODO_DISABLE_ORACLE_VARCHAR2', None)
            tud__dodnf = bodo.typeof(df)
            mrb__acmmt = {}
            for ojaae__obyr, rhpt__wum in zip(tud__dodnf.columns,
                tud__dodnf.data):
                if df[ojaae__obyr].dtype == 'object':
                    if rhpt__wum == datetime_date_array_type:
                        mrb__acmmt[ojaae__obyr] = sa.types.Date
                    elif rhpt__wum in (bodo.string_array_type, bodo.
                        dict_str_arr_type) and (not yghud__bgjl or 
                        yghud__bgjl == '0'):
                        mrb__acmmt[ojaae__obyr] = VARCHAR2(4000)
            dtype = mrb__acmmt
        try:
            lvisa__lhte = tracing.Event('df_to_sql', is_parallel=_is_parallel)
            df.to_sql(name, con, schema, if_exists, index, index_label,
                chunksize, dtype, method)
            lvisa__lhte.finalize()
        except Exception as qva__qscug:
            aka__oyjd = qva__qscug.args[0]
            if jsof__zbpj == 'oracle' and 'ORA-12899' in aka__oyjd:
                aka__oyjd += """
                String is larger than VARCHAR2 maximum length.
                Please set environment variable `BODO_DISABLE_ORACLE_VARCHAR2` to
                disable Bodo's optimziation use of VARCHA2.
                NOTE: Oracle `to_sql` with CLOB datatypes is known to be really slow.
                """
        return aka__oyjd
    finally:
        df.columns = ugrr__qvc
        otar__uktcr.finalize()


@numba.njit
def to_sql_exception_guard_encaps(df, name, con, schema=None, if_exists=
    'fail', index=True, index_label=None, chunksize=None, dtype=None,
    method=None, _is_table_create=False, _is_parallel=False):
    otar__uktcr = tracing.Event('to_sql_exception_guard_encaps',
        is_parallel=_is_parallel)
    with numba.objmode(out='unicode_type'):
        omzry__nrhs = tracing.Event('to_sql_exception_guard_encaps:objmode',
            is_parallel=_is_parallel)
        out = to_sql_exception_guard(df, name, con, schema, if_exists,
            index, index_label, chunksize, dtype, method, _is_table_create,
            _is_parallel)
        omzry__nrhs.finalize()
    otar__uktcr.finalize()
    return out


@overload_method(DataFrameType, 'to_sql')
def to_sql_overload(df, name, con, schema=None, if_exists='fail', index=
    True, index_label=None, chunksize=None, dtype=None, method=None,
    _bodo_allow_downcasting=False, _is_parallel=False):
    import warnings
    check_runtime_cols_unsupported(df, 'DataFrame.to_sql()')
    df: DataFrameType = df
    assert df.columns is not None and df.data is not None
    if is_overload_none(schema):
        if bodo.get_rank() == 0:
            warnings.warn(BodoWarning(
                f'DataFrame.to_sql(): schema argument is recommended to avoid permission issues when writing the table.'
                ))
    if not (is_overload_none(chunksize) or isinstance(chunksize, types.Integer)
        ):
        raise BodoError(
            "DataFrame.to_sql(): 'chunksize' argument must be an integer if provided."
            )
    from bodo.io.helpers import exception_propagating_thread_type
    from bodo.io.parquet_pio import parquet_write_table_cpp
    from bodo.io.snowflake import snowflake_connector_cursor_python_type
    for lxk__fpp in df.columns:
        if not isinstance(lxk__fpp, str):
            raise BodoError(
                'DataFrame.to_sql(): input dataframe must have string column names. Please return the DataFrame with runtime column names to regular Python to modify column names.'
                )
    hlad__rle = pd.array(df.columns)
    llvq__jarb = """def df_to_sql(
    df, name, con,
    schema=None, if_exists='fail', index=True,
    index_label=None, chunksize=None, dtype=None,
    method=None, _bodo_allow_downcasting=False,
    _is_parallel=False,
):
"""
    llvq__jarb += """    if con.startswith('iceberg'):
        con_str = bodo.io.iceberg.format_iceberg_conn_njit(con)
        if schema is None:
            raise ValueError('DataFrame.to_sql(): schema must be provided when writing to an Iceberg table.')
        if chunksize is not None:
            raise ValueError('DataFrame.to_sql(): chunksize not supported for Iceberg tables.')
        if index and bodo.get_rank() == 0:
            warnings.warn('index is not supported for Iceberg tables.')      
        if index_label is not None and bodo.get_rank() == 0:
            warnings.warn('index_label is not supported for Iceberg tables.')
"""
    if df.is_table_format:
        llvq__jarb += f'        py_table = get_dataframe_table(df)\n'
        llvq__jarb += (
            f'        table = py_table_to_cpp_table(py_table, py_table_typ)\n')
    else:
        dkikk__jus = ', '.join(
            f'array_to_info(get_dataframe_data(df, {i}))' for i in range(
            len(df.columns)))
        llvq__jarb += f'        info_list = [{dkikk__jus}]\n'
        llvq__jarb += f'        table = arr_info_list_to_table(info_list)\n'
    llvq__jarb += """        col_names = array_to_info(col_names_arr)
        bodo.io.iceberg.iceberg_write(
            name, con_str, schema, table, col_names,
            if_exists, _is_parallel, pyarrow_table_schema,
            _bodo_allow_downcasting,
        )
        delete_table_decref_arrays(table)
        delete_info_decref_array(col_names)
"""
    llvq__jarb += "    elif con.startswith('snowflake'):\n"
    llvq__jarb += """        if index and bodo.get_rank() == 0:
            warnings.warn('index is not supported for Snowflake tables.')      
        if index_label is not None and bodo.get_rank() == 0:
            warnings.warn('index_label is not supported for Snowflake tables.')
        if _bodo_allow_downcasting and bodo.get_rank() == 0:
            warnings.warn('_bodo_allow_downcasting is not supported for Snowflake tables.')
        ev = tracing.Event('snowflake_write_impl', sync=False)
"""
    llvq__jarb += "        location = ''\n"
    if not is_overload_none(schema):
        llvq__jarb += '        location += \'"\' + schema + \'".\'\n'
    llvq__jarb += '        location += name\n'
    llvq__jarb += '        my_rank = bodo.get_rank()\n'
    llvq__jarb += """        with bodo.objmode(
            cursor='snowflake_connector_cursor_type',
            tmp_folder='temporary_directory_type',
            stage_name='unicode_type',
            parquet_path='unicode_type',
            upload_using_snowflake_put='boolean',
            old_creds='DictType(unicode_type, unicode_type)',
            azure_stage_direct_upload='boolean',
            old_core_site='unicode_type',
            old_sas_token='unicode_type',
        ):
            (
                cursor, tmp_folder, stage_name, parquet_path, upload_using_snowflake_put, old_creds, azure_stage_direct_upload, old_core_site, old_sas_token,
            ) = bodo.io.snowflake.connect_and_get_upload_info(con)
"""
    llvq__jarb += '        bodo.barrier()\n'
    llvq__jarb += '        if azure_stage_direct_upload:\n'
    llvq__jarb += (
        '            bodo.libs.distributed_api.disconnect_hdfs_njit()\n')
    llvq__jarb += '        if chunksize is None:\n'
    llvq__jarb += """            ev_estimate_chunksize = tracing.Event('estimate_chunksize')          
"""
    if df.is_table_format and len(df.columns) > 0:
        llvq__jarb += f"""            nbytes_arr = np.empty({len(df.columns)}, np.int64)
            table = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)
            bodo.utils.table_utils.generate_table_nbytes(table, nbytes_arr, 0)
            memory_usage = np.sum(nbytes_arr)
"""
    else:
        data = ', '.join(
            f'bodo.libs.array_ops.array_op_nbytes(get_dataframe_data(df, {i}))'
             for i in range(len(df.columns)))
        ktvt__ubml = ',' if len(df.columns) == 1 else ''
        llvq__jarb += (
            f'            memory_usage = np.array(({data}{ktvt__ubml}), np.int64).sum()\n'
            )
    llvq__jarb += """            nsplits = int(max(1, memory_usage / bodo.io.snowflake.SF_WRITE_PARQUET_CHUNK_SIZE))
            chunksize = max(1, (len(df) + nsplits - 1) // nsplits)
            ev_estimate_chunksize.finalize()
"""
    if df.has_runtime_cols:
        llvq__jarb += (
            '        columns_index = get_dataframe_column_names(df)\n')
        llvq__jarb += '        names_arr = index_to_array(columns_index)\n'
        llvq__jarb += '        col_names = array_to_info(names_arr)\n'
    else:
        llvq__jarb += '        col_names = array_to_info(col_names_arr)\n'
    llvq__jarb += '        index_col = array_to_info(np.empty(0))\n'
    llvq__jarb += """        bucket_region = bodo.io.fs_io.get_s3_bucket_region_njit(parquet_path, parallel=_is_parallel)
"""
    llvq__jarb += """        ev_upload_df = tracing.Event('upload_df', is_parallel=False)           
"""
    llvq__jarb += '        upload_threads_in_progress = []\n'
    llvq__jarb += """        for chunk_idx, i in enumerate(range(0, len(df), chunksize)):           
"""
    llvq__jarb += """            chunk_name = f'file{chunk_idx}_rank{my_rank}_{bodo.io.helpers.uuid4_helper()}.parquet'
"""
    llvq__jarb += '            chunk_path = parquet_path + chunk_name\n'
    llvq__jarb += (
        '            chunk_path = chunk_path.replace("\\\\", "\\\\\\\\")\n')
    llvq__jarb += (
        '            chunk_path = chunk_path.replace("\'", "\\\\\'")\n')
    llvq__jarb += """            ev_to_df_table = tracing.Event(f'to_df_table_{chunk_idx}', is_parallel=False)
"""
    llvq__jarb += '            chunk = df.iloc[i : i + chunksize]\n'
    if df.is_table_format:
        llvq__jarb += (
            '            py_table_chunk = get_dataframe_table(chunk)\n')
        llvq__jarb += """            table_chunk = py_table_to_cpp_table(py_table_chunk, py_table_typ)
"""
    else:
        bdr__esxr = ', '.join(
            f'array_to_info(get_dataframe_data(chunk, {i}))' for i in range
            (len(df.columns)))
        llvq__jarb += (
            f'            table_chunk = arr_info_list_to_table([{bdr__esxr}])     \n'
            )
    llvq__jarb += '            ev_to_df_table.finalize()\n'
    llvq__jarb += """            ev_pq_write_cpp = tracing.Event(f'pq_write_cpp_{chunk_idx}', is_parallel=False)
            ev_pq_write_cpp.add_attribute('chunk_start', i)
            ev_pq_write_cpp.add_attribute('chunk_end', i + len(chunk))
            ev_pq_write_cpp.add_attribute('chunk_size', len(chunk))
            ev_pq_write_cpp.add_attribute('chunk_path', chunk_path)
            parquet_write_table_cpp(
                unicode_to_utf8(chunk_path),
                table_chunk, col_names, index_col,
                False,
                unicode_to_utf8('null'),
                unicode_to_utf8(bodo.io.snowflake.SF_WRITE_PARQUET_COMPRESSION),
                False,
                0,
                0, 0, 0,
                unicode_to_utf8('null'),
                unicode_to_utf8(bucket_region),
                chunksize,
                unicode_to_utf8('null'),
                True,
                unicode_to_utf8('UTC'),
                True,
            )
            ev_pq_write_cpp.finalize()
            delete_table_decref_arrays(table_chunk)
            if upload_using_snowflake_put:
                with bodo.objmode(upload_thread='types.optional(exception_propagating_thread_type)'):
                    upload_thread = bodo.io.snowflake.do_upload_and_cleanup(
                        cursor, chunk_idx, chunk_path, stage_name,
                    )
                if bodo.io.snowflake.SF_WRITE_OVERLAP_UPLOAD:
                    upload_threads_in_progress.append(upload_thread)
        delete_info_decref_array(index_col)
        delete_info_decref_array(col_names)
        if bodo.io.snowflake.SF_WRITE_OVERLAP_UPLOAD:
            with bodo.objmode():
                bodo.io.helpers.join_all_threads(upload_threads_in_progress)
        ev_upload_df.finalize()
"""
    llvq__jarb += '        bodo.barrier()\n'
    fcft__mrhl = bodo.io.snowflake.gen_snowflake_schema(df.columns, df.data)
    llvq__jarb += f"""        with bodo.objmode():
            bodo.io.snowflake.create_table_copy_into(
                cursor, stage_name, location, {fcft__mrhl},
                if_exists, old_creds, tmp_folder,
                azure_stage_direct_upload, old_core_site,
                old_sas_token,
            )
"""
    llvq__jarb += '        if azure_stage_direct_upload:\n'
    llvq__jarb += (
        '            bodo.libs.distributed_api.disconnect_hdfs_njit()\n')
    llvq__jarb += '        ev.finalize()\n'
    llvq__jarb += '    else:\n'
    llvq__jarb += (
        '        if _bodo_allow_downcasting and bodo.get_rank() == 0:\n')
    llvq__jarb += """            warnings.warn('_bodo_allow_downcasting is not supported for SQL tables.')
"""
    llvq__jarb += '        rank = bodo.libs.distributed_api.get_rank()\n'
    llvq__jarb += "        err_msg = 'unset'\n"
    llvq__jarb += '        if rank != 0:\n'
    llvq__jarb += """            err_msg = bodo.libs.distributed_api.bcast_scalar(err_msg)          
"""
    llvq__jarb += '        elif rank == 0:\n'
    llvq__jarb += '            err_msg = to_sql_exception_guard_encaps(\n'
    llvq__jarb += """                          df, name, con, schema, if_exists, index, index_label,
"""
    llvq__jarb += '                          chunksize, dtype, method,\n'
    llvq__jarb += '                          True, _is_parallel,\n'
    llvq__jarb += '                      )\n'
    llvq__jarb += """            err_msg = bodo.libs.distributed_api.bcast_scalar(err_msg)          
"""
    llvq__jarb += "        if_exists = 'append'\n"
    llvq__jarb += "        if _is_parallel and err_msg == 'all_ok':\n"
    llvq__jarb += '            err_msg = to_sql_exception_guard_encaps(\n'
    llvq__jarb += """                          df, name, con, schema, if_exists, index, index_label,
"""
    llvq__jarb += '                          chunksize, dtype, method,\n'
    llvq__jarb += '                          False, _is_parallel,\n'
    llvq__jarb += '                      )\n'
    llvq__jarb += "        if err_msg != 'all_ok':\n"
    llvq__jarb += "            print('err_msg=', err_msg)\n"
    llvq__jarb += (
        "            raise ValueError('error in to_sql() operation')\n")
    nrsh__tdq = {}
    jyyzi__xyde = globals().copy()
    jyyzi__xyde.update({'arr_info_list_to_table': arr_info_list_to_table,
        'array_to_info': array_to_info, 'bodo': bodo, 'col_names_arr':
        hlad__rle, 'delete_info_decref_array': delete_info_decref_array,
        'delete_table_decref_arrays': delete_table_decref_arrays,
        'get_dataframe_column_names': get_dataframe_column_names,
        'get_dataframe_data': get_dataframe_data, 'get_dataframe_table':
        get_dataframe_table, 'index_to_array': index_to_array, 'np': np,
        'parquet_write_table_cpp': parquet_write_table_cpp,
        'py_table_to_cpp_table': py_table_to_cpp_table, 'py_table_typ': df.
        table_type, 'pyarrow_table_schema': bodo.io.helpers.
        numba_to_pyarrow_schema(df, is_iceberg=True), 'time': time,
        'to_sql_exception_guard_encaps': to_sql_exception_guard_encaps,
        'tracing': tracing, 'unicode_to_utf8': unicode_to_utf8, 'warnings':
        warnings})
    exec(llvq__jarb, jyyzi__xyde, nrsh__tdq)
    _impl = nrsh__tdq['df_to_sql']
    return _impl


@overload_method(DataFrameType, 'to_csv', no_unliteral=True)
def to_csv_overload(df, path_or_buf=None, sep=',', na_rep='', float_format=
    None, columns=None, header=True, index=True, index_label=None, mode='w',
    encoding=None, compression=None, quoting=None, quotechar='"',
    line_terminator=None, chunksize=None, date_format=None, doublequote=
    True, escapechar=None, decimal='.', errors='strict', storage_options=
    None, _bodo_file_prefix='part-'):
    check_runtime_cols_unsupported(df, 'DataFrame.to_csv()')
    check_unsupported_args('DataFrame.to_csv', {'encoding': encoding,
        'mode': mode, 'errors': errors, 'storage_options': storage_options},
        {'encoding': None, 'mode': 'w', 'errors': 'strict',
        'storage_options': None}, package_name='pandas', module_name='IO')
    if not (is_overload_none(path_or_buf) or is_overload_constant_str(
        path_or_buf) or path_or_buf == string_type):
        raise BodoError(
            "DataFrame.to_csv(): 'path_or_buf' argument should be None or string"
            )
    if not is_overload_none(compression):
        raise BodoError(
            "DataFrame.to_csv(): 'compression' argument supports only None, which is the default in JIT code."
            )
    if is_overload_constant_str(path_or_buf):
        kvfi__hqanu = get_overload_const_str(path_or_buf)
        if kvfi__hqanu.endswith(('.gz', '.bz2', '.zip', '.xz')):
            import warnings
            from bodo.utils.typing import BodoWarning
            warnings.warn(BodoWarning(
                "DataFrame.to_csv(): 'compression' argument defaults to None in JIT code, which is the only supported value."
                ))
    if not (is_overload_none(columns) or isinstance(columns, (types.List,
        types.Tuple))):
        raise BodoError(
            "DataFrame.to_csv(): 'columns' argument must be list a or tuple type."
            )
    if is_overload_none(path_or_buf):

        def _impl(df, path_or_buf=None, sep=',', na_rep='', float_format=
            None, columns=None, header=True, index=True, index_label=None,
            mode='w', encoding=None, compression=None, quoting=None,
            quotechar='"', line_terminator=None, chunksize=None,
            date_format=None, doublequote=True, escapechar=None, decimal=
            '.', errors='strict', storage_options=None, _bodo_file_prefix=
            'part-'):
            with numba.objmode(D='unicode_type'):
                D = df.to_csv(path_or_buf, sep, na_rep, float_format,
                    columns, header, index, index_label, mode, encoding,
                    compression, quoting, quotechar, line_terminator,
                    chunksize, date_format, doublequote, escapechar,
                    decimal, errors, storage_options)
            return D
        return _impl

    def _impl(df, path_or_buf=None, sep=',', na_rep='', float_format=None,
        columns=None, header=True, index=True, index_label=None, mode='w',
        encoding=None, compression=None, quoting=None, quotechar='"',
        line_terminator=None, chunksize=None, date_format=None, doublequote
        =True, escapechar=None, decimal='.', errors='strict',
        storage_options=None, _bodo_file_prefix='part-'):
        with numba.objmode(D='unicode_type'):
            D = df.to_csv(None, sep, na_rep, float_format, columns, header,
                index, index_label, mode, encoding, compression, quoting,
                quotechar, line_terminator, chunksize, date_format,
                doublequote, escapechar, decimal, errors, storage_options)
        bodo.io.fs_io.csv_write(path_or_buf, D, _bodo_file_prefix)
    return _impl


@overload_method(DataFrameType, 'to_json', no_unliteral=True)
def to_json_overload(df, path_or_buf=None, orient='records', date_format=
    None, double_precision=10, force_ascii=True, date_unit='ms',
    default_handler=None, lines=True, compression='infer', index=True,
    indent=None, storage_options=None, _bodo_file_prefix='part-'):
    check_runtime_cols_unsupported(df, 'DataFrame.to_json()')
    check_unsupported_args('DataFrame.to_json', {'storage_options':
        storage_options}, {'storage_options': None}, package_name='pandas',
        module_name='IO')
    if path_or_buf is None or path_or_buf == types.none:

        def _impl(df, path_or_buf=None, orient='records', date_format=None,
            double_precision=10, force_ascii=True, date_unit='ms',
            default_handler=None, lines=True, compression='infer', index=
            True, indent=None, storage_options=None, _bodo_file_prefix='part-'
            ):
            with numba.objmode(D='unicode_type'):
                D = df.to_json(path_or_buf, orient, date_format,
                    double_precision, force_ascii, date_unit,
                    default_handler, lines, compression, index, indent,
                    storage_options)
            return D
        return _impl

    def _impl(df, path_or_buf=None, orient='records', date_format=None,
        double_precision=10, force_ascii=True, date_unit='ms',
        default_handler=None, lines=True, compression='infer', index=True,
        indent=None, storage_options=None, _bodo_file_prefix='part-'):
        with numba.objmode(D='unicode_type'):
            D = df.to_json(None, orient, date_format, double_precision,
                force_ascii, date_unit, default_handler, lines, compression,
                index, indent, storage_options)
        vmwn__izyg = bodo.io.fs_io.get_s3_bucket_region_njit(path_or_buf,
            parallel=False)
        if lines and orient == 'records':
            bodo.hiframes.pd_dataframe_ext._json_write(unicode_to_utf8(
                path_or_buf), unicode_to_utf8(D), 0, len(D), False, True,
                unicode_to_utf8(vmwn__izyg), unicode_to_utf8(_bodo_file_prefix)
                )
            bodo.utils.utils.check_and_propagate_cpp_exception()
        else:
            bodo.hiframes.pd_dataframe_ext._json_write(unicode_to_utf8(
                path_or_buf), unicode_to_utf8(D), 0, len(D), False, False,
                unicode_to_utf8(vmwn__izyg), unicode_to_utf8(_bodo_file_prefix)
                )
            bodo.utils.utils.check_and_propagate_cpp_exception()
    return _impl


@overload(pd.get_dummies, inline='always', no_unliteral=True)
def get_dummies(data, prefix=None, prefix_sep='_', dummy_na=False, columns=
    None, sparse=False, drop_first=False, dtype=None):
    rdei__afue = {'prefix': prefix, 'prefix_sep': prefix_sep, 'dummy_na':
        dummy_na, 'columns': columns, 'sparse': sparse, 'drop_first':
        drop_first, 'dtype': dtype}
    dmxz__jbedi = {'prefix': None, 'prefix_sep': '_', 'dummy_na': False,
        'columns': None, 'sparse': False, 'drop_first': False, 'dtype': None}
    check_unsupported_args('pandas.get_dummies', rdei__afue, dmxz__jbedi,
        package_name='pandas', module_name='General')
    if not categorical_can_construct_dataframe(data):
        raise BodoError(
            'pandas.get_dummies() only support categorical data types with explicitly known categories'
            )
    llvq__jarb = """def impl(data, prefix=None, prefix_sep='_', dummy_na=False, columns=None, sparse=False, drop_first=False, dtype=None,):
"""
    if isinstance(data, SeriesType):
        tcudo__nvm = data.data.dtype.categories
        llvq__jarb += (
            '  data_values = bodo.hiframes.pd_series_ext.get_series_data(data)\n'
            )
    else:
        tcudo__nvm = data.dtype.categories
        llvq__jarb += '  data_values = data\n'
    emoh__wwh = len(tcudo__nvm)
    llvq__jarb += """  codes = bodo.hiframes.pd_categorical_ext.get_categorical_arr_codes(data_values)
"""
    llvq__jarb += '  numba.parfors.parfor.init_prange()\n'
    llvq__jarb += '  n = len(data_values)\n'
    for i in range(emoh__wwh):
        llvq__jarb += '  data_arr_{} = np.empty(n, np.uint8)\n'.format(i)
    llvq__jarb += '  for i in numba.parfors.parfor.internal_prange(n):\n'
    llvq__jarb += '      if bodo.libs.array_kernels.isna(data_values, i):\n'
    for amvs__flk in range(emoh__wwh):
        llvq__jarb += '          data_arr_{}[i] = 0\n'.format(amvs__flk)
    llvq__jarb += '      else:\n'
    for mjbpx__qni in range(emoh__wwh):
        llvq__jarb += '          data_arr_{0}[i] = codes[i] == {0}\n'.format(
            mjbpx__qni)
    dkikk__jus = ', '.join(f'data_arr_{i}' for i in range(emoh__wwh))
    index = 'bodo.hiframes.pd_index_ext.init_range_index(0, n, 1, None)'
    if isinstance(tcudo__nvm[0], np.datetime64):
        tcudo__nvm = tuple(pd.Timestamp(ojaae__obyr) for ojaae__obyr in
            tcudo__nvm)
    elif isinstance(tcudo__nvm[0], np.timedelta64):
        tcudo__nvm = tuple(pd.Timedelta(ojaae__obyr) for ojaae__obyr in
            tcudo__nvm)
    return bodo.hiframes.dataframe_impl._gen_init_df(llvq__jarb, tcudo__nvm,
        dkikk__jus, index)


def categorical_can_construct_dataframe(val):
    if isinstance(val, CategoricalArrayType):
        return val.dtype.categories is not None
    elif isinstance(val, SeriesType) and isinstance(val.data,
        CategoricalArrayType):
        return val.data.dtype.categories is not None
    return False


def handle_inplace_df_type_change(inplace, _bodo_transformed, func_name):
    if is_overload_false(_bodo_transformed
        ) and bodo.transforms.typing_pass.in_partial_typing and (
        is_overload_true(inplace) or not is_overload_constant_bool(inplace)):
        bodo.transforms.typing_pass.typing_transform_required = True
        raise Exception('DataFrame.{}(): transform necessary for inplace'.
            format(func_name))


pd_unsupported = (pd.read_pickle, pd.read_table, pd.read_fwf, pd.
    read_clipboard, pd.ExcelFile, pd.read_html, pd.read_xml, pd.read_hdf,
    pd.read_feather, pd.read_orc, pd.read_sas, pd.read_spss, pd.
    read_sql_query, pd.read_gbq, pd.read_stata, pd.ExcelWriter, pd.
    json_normalize, pd.merge_ordered, pd.factorize, pd.wide_to_long, pd.
    bdate_range, pd.period_range, pd.infer_freq, pd.interval_range, pd.eval,
    pd.test, pd.Grouper)
pd_util_unsupported = pd.util.hash_array, pd.util.hash_pandas_object
dataframe_unsupported = ['set_flags', 'convert_dtypes', 'bool', '__iter__',
    'items', 'iteritems', 'keys', 'iterrows', 'lookup', 'pop', 'xs', 'get',
    'add', 'sub', 'mul', 'div', 'truediv', 'floordiv', 'mod', 'pow', 'dot',
    'radd', 'rsub', 'rmul', 'rdiv', 'rtruediv', 'rfloordiv', 'rmod', 'rpow',
    'lt', 'gt', 'le', 'ge', 'ne', 'eq', 'combine', 'combine_first',
    'subtract', 'divide', 'multiply', 'applymap', 'agg', 'aggregate',
    'transform', 'expanding', 'ewm', 'all', 'any', 'clip', 'corrwith',
    'cummax', 'cummin', 'eval', 'kurt', 'kurtosis', 'mad', 'mode', 'round',
    'sem', 'skew', 'value_counts', 'add_prefix', 'add_suffix', 'align',
    'at_time', 'between_time', 'equals', 'reindex', 'reindex_like',
    'rename_axis', 'set_axis', 'truncate', 'backfill', 'bfill', 'ffill',
    'interpolate', 'pad', 'droplevel', 'reorder_levels', 'nlargest',
    'nsmallest', 'swaplevel', 'stack', 'unstack', 'swapaxes', 'squeeze',
    'to_xarray', 'T', 'transpose', 'compare', 'update', 'asfreq', 'asof',
    'slice_shift', 'tshift', 'first_valid_index', 'last_valid_index',
    'resample', 'to_period', 'to_timestamp', 'tz_convert', 'tz_localize',
    'boxplot', 'hist', 'from_dict', 'from_records', 'to_pickle', 'to_hdf',
    'to_dict', 'to_excel', 'to_html', 'to_feather', 'to_latex', 'to_stata',
    'to_gbq', 'to_records', 'to_clipboard', 'to_markdown', 'to_xml']
dataframe_unsupported_attrs = ['at', 'attrs', 'axes', 'flags', 'style',
    'sparse']


def _install_pd_unsupported(mod_name, pd_unsupported):
    for hajk__owsbs in pd_unsupported:
        fpt__tps = mod_name + '.' + hajk__owsbs.__name__
        overload(hajk__owsbs, no_unliteral=True)(create_unsupported_overload
            (fpt__tps))


def _install_dataframe_unsupported():
    for sjl__cxr in dataframe_unsupported_attrs:
        clbzc__yth = 'DataFrame.' + sjl__cxr
        overload_attribute(DataFrameType, sjl__cxr)(create_unsupported_overload
            (clbzc__yth))
    for fpt__tps in dataframe_unsupported:
        clbzc__yth = 'DataFrame.' + fpt__tps + '()'
        overload_method(DataFrameType, fpt__tps)(create_unsupported_overload
            (clbzc__yth))


_install_pd_unsupported('pandas', pd_unsupported)
_install_pd_unsupported('pandas.util', pd_util_unsupported)
_install_dataframe_unsupported()
