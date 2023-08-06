"""
Indexing support for pd.DataFrame type.
"""
import operator
import numpy as np
import pandas as pd
from numba.core import cgutils, types
from numba.core.typing.templates import AbstractTemplate, infer_global
from numba.extending import intrinsic, lower_builtin, lower_cast, make_attribute_wrapper, models, overload, overload_attribute, register_model
import bodo
from bodo.hiframes.pd_dataframe_ext import DataFrameType, check_runtime_cols_unsupported
from bodo.utils.transform import gen_const_tup
from bodo.utils.typing import BodoError, get_overload_const_int, get_overload_const_list, get_overload_const_str, is_immutable_array, is_list_like_index_type, is_overload_constant_int, is_overload_constant_list, is_overload_constant_str, raise_bodo_error


@infer_global(operator.getitem)
class DataFrameGetItemTemplate(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        assert len(args) == 2
        check_runtime_cols_unsupported(args[0], 'DataFrame getitem (df[])')
        if isinstance(args[0], DataFrameType):
            return self.typecheck_df_getitem(args)
        elif isinstance(args[0], DataFrameLocType):
            return self.typecheck_loc_getitem(args)
        else:
            return

    def typecheck_loc_getitem(self, args):
        I = args[0]
        idx = args[1]
        df = I.df_type
        if isinstance(df.columns[0], tuple):
            raise_bodo_error(
                'DataFrame.loc[] getitem (location-based indexing) with multi-indexed columns not supported yet'
                )
        if is_list_like_index_type(idx) and idx.dtype == types.bool_:
            kcmrc__wzou = idx
            ejz__yrp = df.data
            eqjef__oxh = df.columns
            sdhc__kdsja = self.replace_range_with_numeric_idx_if_needed(df,
                kcmrc__wzou)
            yyjp__otty = DataFrameType(ejz__yrp, sdhc__kdsja, eqjef__oxh,
                is_table_format=df.is_table_format)
            return yyjp__otty(*args)
        if isinstance(idx, types.BaseTuple) and len(idx) == 2:
            uwi__ykum = idx.types[0]
            okxp__mfm = idx.types[1]
            if isinstance(uwi__ykum, types.Integer):
                if not isinstance(df.index, bodo.hiframes.pd_index_ext.
                    RangeIndexType):
                    raise_bodo_error(
                        'Dataframe.loc[int, col_ind] getitem only supported for dataframes with RangeIndexes'
                        )
                if is_overload_constant_str(okxp__mfm):
                    fshp__ektko = get_overload_const_str(okxp__mfm)
                    if fshp__ektko not in df.columns:
                        raise_bodo_error(
                            'dataframe {} does not include column {}'.
                            format(df, fshp__ektko))
                    ymva__oin = df.columns.index(fshp__ektko)
                    return df.data[ymva__oin].dtype(*args)
                if isinstance(okxp__mfm, types.UnicodeType):
                    raise_bodo_error(
                        f'DataFrame.loc[] getitem (location-based indexing) requires constant column names. For more information, see https://docs.bodo.ai/latest/bodo_parallelism/typing_considerations/#require_constants.'
                        )
                else:
                    raise_bodo_error(
                        f'DataFrame.loc[] getitem (location-based indexing) using {idx} not supported yet.'
                        )
            if is_list_like_index_type(uwi__ykum
                ) and uwi__ykum.dtype == types.bool_ or isinstance(uwi__ykum,
                types.SliceType):
                sdhc__kdsja = self.replace_range_with_numeric_idx_if_needed(df,
                    uwi__ykum)
                if is_overload_constant_str(okxp__mfm):
                    dya__tsj = get_overload_const_str(okxp__mfm)
                    if dya__tsj not in df.columns:
                        raise_bodo_error(
                            f'dataframe {df} does not include column {dya__tsj}'
                            )
                    ymva__oin = df.columns.index(dya__tsj)
                    fkjp__lub = df.data[ymva__oin]
                    cndw__efyjf = fkjp__lub.dtype
                    kfij__jtonf = types.literal(df.columns[ymva__oin])
                    yyjp__otty = bodo.SeriesType(cndw__efyjf, fkjp__lub,
                        sdhc__kdsja, kfij__jtonf)
                    return yyjp__otty(*args)
                if isinstance(okxp__mfm, types.UnicodeType):
                    raise_bodo_error(
                        f'DataFrame.loc[] getitem (location-based indexing) requires constant column names. For more information, see https://docs.bodo.ai/latest/bodo_parallelism/typing_considerations/#require_constants.'
                        )
                elif is_overload_constant_list(okxp__mfm):
                    kai__tihdp = get_overload_const_list(okxp__mfm)
                    kcef__lxdu = types.unliteral(okxp__mfm)
                    if kcef__lxdu.dtype == types.bool_:
                        if len(df.columns) != len(kai__tihdp):
                            raise_bodo_error(
                                f'dataframe {df} has {len(df.columns)} columns, but boolean array used with DataFrame.loc[] {kai__tihdp} has {len(kai__tihdp)} values'
                                )
                        aczw__cyf = []
                        jmuqz__exu = []
                        for gkzx__pfilv in range(len(kai__tihdp)):
                            if kai__tihdp[gkzx__pfilv]:
                                aczw__cyf.append(df.columns[gkzx__pfilv])
                                jmuqz__exu.append(df.data[gkzx__pfilv])
                        hhe__pjawr = tuple()
                        yxitr__cmu = df.is_table_format and len(aczw__cyf
                            ) > 0 and len(aczw__cyf
                            ) >= bodo.hiframes.boxing.TABLE_FORMAT_THRESHOLD
                        yyjp__otty = DataFrameType(tuple(jmuqz__exu),
                            sdhc__kdsja, tuple(aczw__cyf), is_table_format=
                            yxitr__cmu)
                        return yyjp__otty(*args)
                    elif kcef__lxdu.dtype == bodo.string_type:
                        hhe__pjawr, jmuqz__exu = (
                            get_df_getitem_kept_cols_and_data(df, kai__tihdp))
                        yxitr__cmu = df.is_table_format and len(kai__tihdp
                            ) > 0 and len(kai__tihdp
                            ) >= bodo.hiframes.boxing.TABLE_FORMAT_THRESHOLD
                        yyjp__otty = DataFrameType(jmuqz__exu, sdhc__kdsja,
                            hhe__pjawr, is_table_format=yxitr__cmu)
                        return yyjp__otty(*args)
        raise_bodo_error(
            f'DataFrame.loc[] getitem (location-based indexing) using {idx} not supported yet. If you are trying to select a subset of the columns by passing a list of column names, that list must be a compile time constant. See https://docs.bodo.ai/latest/bodo_parallelism/typing_considerations/#require_constants.'
            )

    def typecheck_df_getitem(self, args):
        df = args[0]
        ind = args[1]
        if is_overload_constant_str(ind) or is_overload_constant_int(ind):
            ind_val = get_overload_const_str(ind) if is_overload_constant_str(
                ind) else get_overload_const_int(ind)
            if isinstance(df.columns[0], tuple):
                aczw__cyf = []
                jmuqz__exu = []
                for gkzx__pfilv, ysx__bkt in enumerate(df.columns):
                    if ysx__bkt[0] != ind_val:
                        continue
                    aczw__cyf.append(ysx__bkt[1] if len(ysx__bkt) == 2 else
                        ysx__bkt[1:])
                    jmuqz__exu.append(df.data[gkzx__pfilv])
                fkjp__lub = tuple(jmuqz__exu)
                fmpx__obctu = df.index
                csxog__upzqz = tuple(aczw__cyf)
                yyjp__otty = DataFrameType(fkjp__lub, fmpx__obctu, csxog__upzqz
                    )
                return yyjp__otty(*args)
            else:
                if ind_val not in df.columns:
                    raise_bodo_error('dataframe {} does not include column {}'
                        .format(df, ind_val))
                ymva__oin = df.columns.index(ind_val)
                fkjp__lub = df.data[ymva__oin]
                cndw__efyjf = fkjp__lub.dtype
                fmpx__obctu = df.index
                kfij__jtonf = types.literal(df.columns[ymva__oin])
                yyjp__otty = bodo.SeriesType(cndw__efyjf, fkjp__lub,
                    fmpx__obctu, kfij__jtonf)
                return yyjp__otty(*args)
        if isinstance(ind, types.Integer) or isinstance(ind, types.UnicodeType
            ):
            raise_bodo_error(
                'df[] getitem selecting a subset of columns requires providing constant column names. For more information, see https://docs.bodo.ai/latest/bodo_parallelism/typing_considerations/#require_constants.'
                )
        if is_list_like_index_type(ind
            ) and ind.dtype == types.bool_ or isinstance(ind, types.SliceType):
            fkjp__lub = df.data
            fmpx__obctu = self.replace_range_with_numeric_idx_if_needed(df, ind
                )
            csxog__upzqz = df.columns
            yyjp__otty = DataFrameType(fkjp__lub, fmpx__obctu, csxog__upzqz,
                is_table_format=df.is_table_format)
            return yyjp__otty(*args)
        elif is_overload_constant_list(ind):
            fgi__wfnul = get_overload_const_list(ind)
            csxog__upzqz, fkjp__lub = get_df_getitem_kept_cols_and_data(df,
                fgi__wfnul)
            fmpx__obctu = df.index
            yxitr__cmu = df.is_table_format and len(fgi__wfnul) > 0 and len(
                fgi__wfnul) >= bodo.hiframes.boxing.TABLE_FORMAT_THRESHOLD
            yyjp__otty = DataFrameType(fkjp__lub, fmpx__obctu, csxog__upzqz,
                is_table_format=yxitr__cmu)
            return yyjp__otty(*args)
        raise_bodo_error(
            f'df[] getitem using {ind} not supported. If you are trying to select a subset of the columns, you must provide the column names you are selecting as a constant. See https://docs.bodo.ai/latest/bodo_parallelism/typing_considerations/#require_constants.'
            )

    def replace_range_with_numeric_idx_if_needed(self, df, ind):
        sdhc__kdsja = bodo.hiframes.pd_index_ext.NumericIndexType(types.
            int64, df.index.name_typ) if not isinstance(ind, types.SliceType
            ) and isinstance(df.index, bodo.hiframes.pd_index_ext.
            RangeIndexType) else df.index
        return sdhc__kdsja


DataFrameGetItemTemplate._no_unliteral = True


def get_df_getitem_kept_cols_and_data(df, cols_to_keep_list):
    for fnbn__zex in cols_to_keep_list:
        if fnbn__zex not in df.column_index:
            raise_bodo_error('Column {} not found in dataframe columns {}'.
                format(fnbn__zex, df.columns))
    csxog__upzqz = tuple(cols_to_keep_list)
    fkjp__lub = tuple(df.data[df.column_index[heyu__kxkx]] for heyu__kxkx in
        csxog__upzqz)
    return csxog__upzqz, fkjp__lub


@lower_builtin(operator.getitem, DataFrameType, types.Any)
def getitem_df_lower(context, builder, sig, args):
    impl = df_getitem_overload(*sig.args)
    return context.compile_internal(builder, impl, sig, args)


def df_getitem_overload(df, ind):
    if not isinstance(df, DataFrameType):
        return
    if is_overload_constant_str(ind) or is_overload_constant_int(ind):
        ind_val = get_overload_const_str(ind) if is_overload_constant_str(ind
            ) else get_overload_const_int(ind)
        if isinstance(df.columns[0], tuple):
            aczw__cyf = []
            jmuqz__exu = []
            for gkzx__pfilv, ysx__bkt in enumerate(df.columns):
                if ysx__bkt[0] != ind_val:
                    continue
                aczw__cyf.append(ysx__bkt[1] if len(ysx__bkt) == 2 else
                    ysx__bkt[1:])
                jmuqz__exu.append(
                    'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {})'
                    .format(gkzx__pfilv))
            dvnck__ptis = 'def impl(df, ind):\n'
            qymnn__adwa = (
                'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)')
            return bodo.hiframes.dataframe_impl._gen_init_df(dvnck__ptis,
                aczw__cyf, ', '.join(jmuqz__exu), qymnn__adwa)
        if ind_val not in df.columns:
            raise_bodo_error('dataframe {} does not include column {}'.
                format(df, ind_val))
        col_no = df.columns.index(ind_val)
        return lambda df, ind: bodo.hiframes.pd_series_ext.init_series(bodo
            .hiframes.pd_dataframe_ext.get_dataframe_data(df, col_no), bodo
            .hiframes.pd_dataframe_ext.get_dataframe_index(df), ind_val)
    if is_overload_constant_list(ind):
        fgi__wfnul = get_overload_const_list(ind)
        for fnbn__zex in fgi__wfnul:
            if fnbn__zex not in df.column_index:
                raise_bodo_error('Column {} not found in dataframe columns {}'
                    .format(fnbn__zex, df.columns))
        mre__gnw = None
        if df.is_table_format and len(fgi__wfnul) > 0 and len(fgi__wfnul
            ) >= bodo.hiframes.boxing.TABLE_FORMAT_THRESHOLD:
            jnb__pzwt = [df.column_index[fnbn__zex] for fnbn__zex in fgi__wfnul
                ]
            mre__gnw = {'col_nums_meta': bodo.utils.typing.MetaType(tuple(
                jnb__pzwt))}
            jmuqz__exu = (
                f'bodo.hiframes.table.table_subset(bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df), col_nums_meta, True)'
                )
        else:
            jmuqz__exu = ', '.join(
                f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {df.column_index[fnbn__zex]}).copy()'
                 for fnbn__zex in fgi__wfnul)
        dvnck__ptis = 'def impl(df, ind):\n'
        qymnn__adwa = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)'
        return bodo.hiframes.dataframe_impl._gen_init_df(dvnck__ptis,
            fgi__wfnul, jmuqz__exu, qymnn__adwa, extra_globals=mre__gnw)
    if is_list_like_index_type(ind) and ind.dtype == types.bool_ or isinstance(
        ind, types.SliceType):
        dvnck__ptis = 'def impl(df, ind):\n'
        if not isinstance(ind, types.SliceType):
            dvnck__ptis += (
                '  ind = bodo.utils.conversion.coerce_to_array(ind)\n')
        qymnn__adwa = (
            'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)[ind]')
        if df.is_table_format:
            jmuqz__exu = (
                f'bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)[ind]')
        else:
            jmuqz__exu = ', '.join(
                f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {df.column_index[fnbn__zex]})[ind]'
                 for fnbn__zex in df.columns)
        return bodo.hiframes.dataframe_impl._gen_init_df(dvnck__ptis, df.
            columns, jmuqz__exu, qymnn__adwa)
    raise_bodo_error('df[] getitem using {} not supported'.format(ind))


@overload(operator.setitem, no_unliteral=True)
def df_setitem_overload(df, idx, val):
    check_runtime_cols_unsupported(df, 'DataFrame setitem (df[])')
    if not isinstance(df, DataFrameType):
        return
    raise_bodo_error('DataFrame setitem: transform necessary')


class DataFrameILocType(types.Type):

    def __init__(self, df_type):
        self.df_type = df_type
        heyu__kxkx = 'DataFrameILocType({})'.format(df_type)
        super(DataFrameILocType, self).__init__(heyu__kxkx)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)
    ndim = 2


@register_model(DataFrameILocType)
class DataFrameILocModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        iexa__cyrhg = [('obj', fe_type.df_type)]
        super(DataFrameILocModel, self).__init__(dmm, fe_type, iexa__cyrhg)


make_attribute_wrapper(DataFrameILocType, 'obj', '_obj')


@intrinsic
def init_dataframe_iloc(typingctx, obj=None):

    def codegen(context, builder, signature, args):
        keu__cqnfq, = args
        elu__jhti = signature.return_type
        vkbnb__nlq = cgutils.create_struct_proxy(elu__jhti)(context, builder)
        vkbnb__nlq.obj = keu__cqnfq
        context.nrt.incref(builder, signature.args[0], keu__cqnfq)
        return vkbnb__nlq._getvalue()
    return DataFrameILocType(obj)(obj), codegen


@overload_attribute(DataFrameType, 'iloc')
def overload_dataframe_iloc(df):
    check_runtime_cols_unsupported(df, 'DataFrame.iloc')
    return lambda df: bodo.hiframes.dataframe_indexing.init_dataframe_iloc(df)


@overload(operator.getitem, no_unliteral=True)
def overload_iloc_getitem(I, idx):
    if not isinstance(I, DataFrameILocType):
        return
    df = I.df_type
    if isinstance(idx, types.Integer):
        return _gen_iloc_getitem_row_impl(df, df.columns, 'idx')
    if isinstance(idx, types.BaseTuple) and len(idx) == 2 and not isinstance(
        idx[1], types.SliceType):
        if not (is_overload_constant_list(idx.types[1]) or
            is_overload_constant_int(idx.types[1])):
            raise_bodo_error(
                'idx2 in df.iloc[idx1, idx2] should be a constant integer or constant list of integers. For more information, see https://docs.bodo.ai/latest/bodo_parallelism/typing_considerations/#require_constants.'
                )
        cfxue__xqybq = len(df.data)
        if is_overload_constant_int(idx.types[1]):
            is_out_series = True
            adsd__xdmuw = get_overload_const_int(idx.types[1])
            if adsd__xdmuw < 0 or adsd__xdmuw >= cfxue__xqybq:
                raise BodoError(
                    'df.iloc: column integer must refer to a valid column number'
                    )
            jjb__avsz = [adsd__xdmuw]
        else:
            is_out_series = False
            jjb__avsz = get_overload_const_list(idx.types[1])
            if any(not isinstance(ind, int) or ind < 0 or ind >=
                cfxue__xqybq for ind in jjb__avsz):
                raise BodoError(
                    'df.iloc: column list must be integers referring to a valid column number'
                    )
        col_names = tuple(pd.Series(df.columns, dtype=object)[jjb__avsz])
        if isinstance(idx.types[0], types.Integer):
            if isinstance(idx.types[1], types.Integer):
                adsd__xdmuw = jjb__avsz[0]

                def impl(I, idx):
                    df = I._obj
                    return bodo.utils.conversion.box_if_dt64(bodo.hiframes.
                        pd_dataframe_ext.get_dataframe_data(df, adsd__xdmuw
                        )[idx[0]])
                return impl
            return _gen_iloc_getitem_row_impl(df, col_names, 'idx[0]')
        if is_list_like_index_type(idx.types[0]) and isinstance(idx.types[0
            ].dtype, (types.Integer, types.Boolean)) or isinstance(idx.
            types[0], types.SliceType):
            return _gen_iloc_getitem_bool_slice_impl(df, col_names, idx.
                types[0], 'idx[0]', is_out_series)
    if is_list_like_index_type(idx) and isinstance(idx.dtype, (types.
        Integer, types.Boolean)) or isinstance(idx, types.SliceType):
        return _gen_iloc_getitem_bool_slice_impl(df, df.columns, idx, 'idx',
            False)
    if isinstance(idx, types.BaseTuple) and len(idx) == 2 and isinstance(idx
        [0], types.SliceType) and isinstance(idx[1], types.SliceType):
        raise_bodo_error(
            'slice2 in df.iloc[slice1,slice2] should be constant. For more information, see https://docs.bodo.ai/latest/bodo_parallelism/typing_considerations/#require_constants.'
            )
    raise_bodo_error(f'df.iloc[] getitem using {idx} not supported')


def _gen_iloc_getitem_bool_slice_impl(df, col_names, idx_typ, idx,
    is_out_series):
    dvnck__ptis = 'def impl(I, idx):\n'
    dvnck__ptis += '  df = I._obj\n'
    if isinstance(idx_typ, types.SliceType):
        dvnck__ptis += f'  idx_t = {idx}\n'
    else:
        dvnck__ptis += (
            f'  idx_t = bodo.utils.conversion.coerce_to_array({idx})\n')
    qymnn__adwa = (
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)[idx_t]')
    mre__gnw = None
    if df.is_table_format and not is_out_series:
        jnb__pzwt = [df.column_index[fnbn__zex] for fnbn__zex in col_names]
        mre__gnw = {'col_nums_meta': bodo.utils.typing.MetaType(tuple(
            jnb__pzwt))}
        jmuqz__exu = (
            f'bodo.hiframes.table.table_subset(bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df), col_nums_meta, False)[idx_t]'
            )
    else:
        jmuqz__exu = ', '.join(
            f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {df.column_index[fnbn__zex]})[idx_t]'
             for fnbn__zex in col_names)
    if is_out_series:
        mbk__jpku = f"'{col_names[0]}'" if isinstance(col_names[0], str
            ) else f'{col_names[0]}'
        dvnck__ptis += f"""  return bodo.hiframes.pd_series_ext.init_series({jmuqz__exu}, {qymnn__adwa}, {mbk__jpku})
"""
        wti__vdlq = {}
        exec(dvnck__ptis, {'bodo': bodo}, wti__vdlq)
        return wti__vdlq['impl']
    return bodo.hiframes.dataframe_impl._gen_init_df(dvnck__ptis, col_names,
        jmuqz__exu, qymnn__adwa, extra_globals=mre__gnw)


def _gen_iloc_getitem_row_impl(df, col_names, idx):
    dvnck__ptis = 'def impl(I, idx):\n'
    dvnck__ptis += '  df = I._obj\n'
    qpqdl__fviej = ', '.join(
        f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {df.column_index[fnbn__zex]})[{idx}]'
         for fnbn__zex in col_names)
    dvnck__ptis += f"""  row_idx = bodo.hiframes.pd_index_ext.init_heter_index({gen_const_tup(col_names)}, None)
"""
    dvnck__ptis += f"""  return bodo.hiframes.pd_series_ext.init_series(({qpqdl__fviej},), row_idx, None)
"""
    wti__vdlq = {}
    exec(dvnck__ptis, {'bodo': bodo}, wti__vdlq)
    impl = wti__vdlq['impl']
    return impl


@overload(operator.setitem, no_unliteral=True)
def df_iloc_setitem_overload(df, idx, val):
    if not isinstance(df, DataFrameILocType):
        return
    raise_bodo_error(
        f'DataFrame.iloc setitem unsupported for dataframe {df.df_type}, index {idx}, value {val}'
        )


class DataFrameLocType(types.Type):

    def __init__(self, df_type):
        self.df_type = df_type
        heyu__kxkx = 'DataFrameLocType({})'.format(df_type)
        super(DataFrameLocType, self).__init__(heyu__kxkx)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)
    ndim = 2


@register_model(DataFrameLocType)
class DataFrameLocModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        iexa__cyrhg = [('obj', fe_type.df_type)]
        super(DataFrameLocModel, self).__init__(dmm, fe_type, iexa__cyrhg)


make_attribute_wrapper(DataFrameLocType, 'obj', '_obj')


@intrinsic
def init_dataframe_loc(typingctx, obj=None):

    def codegen(context, builder, signature, args):
        keu__cqnfq, = args
        ach__gun = signature.return_type
        uvnn__xwv = cgutils.create_struct_proxy(ach__gun)(context, builder)
        uvnn__xwv.obj = keu__cqnfq
        context.nrt.incref(builder, signature.args[0], keu__cqnfq)
        return uvnn__xwv._getvalue()
    return DataFrameLocType(obj)(obj), codegen


@overload_attribute(DataFrameType, 'loc')
def overload_dataframe_loc(df):
    check_runtime_cols_unsupported(df, 'DataFrame.loc')
    return lambda df: bodo.hiframes.dataframe_indexing.init_dataframe_loc(df)


@lower_builtin(operator.getitem, DataFrameLocType, types.Any)
def loc_getitem_lower(context, builder, sig, args):
    impl = overload_loc_getitem(*sig.args)
    return context.compile_internal(builder, impl, sig, args)


def overload_loc_getitem(I, idx):
    if not isinstance(I, DataFrameLocType):
        return
    df = I.df_type
    if is_list_like_index_type(idx) and idx.dtype == types.bool_:
        dvnck__ptis = 'def impl(I, idx):\n'
        dvnck__ptis += '  df = I._obj\n'
        dvnck__ptis += '  idx_t = bodo.utils.conversion.coerce_to_array(idx)\n'
        qymnn__adwa = (
            'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)[idx_t]')
        if df.is_table_format:
            jmuqz__exu = (
                f'bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)[idx_t]'
                )
        else:
            jmuqz__exu = ', '.join(
                f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {df.column_index[fnbn__zex]})[idx_t]'
                 for fnbn__zex in df.columns)
        return bodo.hiframes.dataframe_impl._gen_init_df(dvnck__ptis, df.
            columns, jmuqz__exu, qymnn__adwa)
    if isinstance(idx, types.BaseTuple) and len(idx) == 2:
        quk__ofg = idx.types[1]
        if is_overload_constant_str(quk__ofg):
            daefc__sdotz = get_overload_const_str(quk__ofg)
            adsd__xdmuw = df.columns.index(daefc__sdotz)

            def impl_col_name(I, idx):
                df = I._obj
                qymnn__adwa = (bodo.hiframes.pd_dataframe_ext.
                    get_dataframe_index(df))
                tas__rbhrx = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(
                    df, adsd__xdmuw)
                return bodo.hiframes.pd_series_ext.init_series(tas__rbhrx,
                    qymnn__adwa, daefc__sdotz).loc[idx[0]]
            return impl_col_name
        if is_overload_constant_list(quk__ofg):
            col_idx_list = get_overload_const_list(quk__ofg)
            if len(col_idx_list) > 0 and not isinstance(col_idx_list[0], (
                bool, np.bool_)) and not all(fnbn__zex in df.column_index for
                fnbn__zex in col_idx_list):
                raise_bodo_error(
                    f'DataFrame.loc[]: invalid column list {col_idx_list}; not all in dataframe columns {df.columns}'
                    )
            return gen_df_loc_col_select_impl(df, col_idx_list)
    raise_bodo_error(
        f'DataFrame.loc[] getitem (location-based indexing) using {idx} not supported yet.'
        )


def gen_df_loc_col_select_impl(df, col_idx_list):
    col_names = []
    jjb__avsz = []
    if len(col_idx_list) > 0 and isinstance(col_idx_list[0], (bool, np.bool_)):
        for gkzx__pfilv, hmsx__bondb in enumerate(col_idx_list):
            if hmsx__bondb:
                jjb__avsz.append(gkzx__pfilv)
                col_names.append(df.columns[gkzx__pfilv])
    else:
        col_names = col_idx_list
        jjb__avsz = [df.column_index[fnbn__zex] for fnbn__zex in col_idx_list]
    mre__gnw = None
    if df.is_table_format and len(col_idx_list) > 0 and len(col_idx_list
        ) >= bodo.hiframes.boxing.TABLE_FORMAT_THRESHOLD:
        mre__gnw = {'col_nums_meta': bodo.utils.typing.MetaType(tuple(
            jjb__avsz))}
        jmuqz__exu = (
            f'bodo.hiframes.table.table_subset(bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df), col_nums_meta, False)[idx[0]]'
            )
    else:
        jmuqz__exu = ', '.join(
            f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {ind})[idx[0]]'
             for ind in jjb__avsz)
    qymnn__adwa = (
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)[idx[0]]')
    dvnck__ptis = 'def impl(I, idx):\n'
    dvnck__ptis += '  df = I._obj\n'
    return bodo.hiframes.dataframe_impl._gen_init_df(dvnck__ptis, col_names,
        jmuqz__exu, qymnn__adwa, extra_globals=mre__gnw)


@overload(operator.setitem, no_unliteral=True)
def df_loc_setitem_overload(df, idx, val):
    if not isinstance(df, DataFrameLocType):
        return
    raise_bodo_error(
        f'DataFrame.loc setitem unsupported for dataframe {df.df_type}, index {idx}, value {val}'
        )


class DataFrameIatType(types.Type):

    def __init__(self, df_type):
        self.df_type = df_type
        heyu__kxkx = 'DataFrameIatType({})'.format(df_type)
        super(DataFrameIatType, self).__init__(heyu__kxkx)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)
    ndim = 2


@register_model(DataFrameIatType)
class DataFrameIatModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        iexa__cyrhg = [('obj', fe_type.df_type)]
        super(DataFrameIatModel, self).__init__(dmm, fe_type, iexa__cyrhg)


make_attribute_wrapper(DataFrameIatType, 'obj', '_obj')


@intrinsic
def init_dataframe_iat(typingctx, obj=None):

    def codegen(context, builder, signature, args):
        keu__cqnfq, = args
        pdi__bqqqp = signature.return_type
        xbl__jrgpz = cgutils.create_struct_proxy(pdi__bqqqp)(context, builder)
        xbl__jrgpz.obj = keu__cqnfq
        context.nrt.incref(builder, signature.args[0], keu__cqnfq)
        return xbl__jrgpz._getvalue()
    return DataFrameIatType(obj)(obj), codegen


@overload_attribute(DataFrameType, 'iat')
def overload_dataframe_iat(df):
    check_runtime_cols_unsupported(df, 'DataFrame.iat')
    return lambda df: bodo.hiframes.dataframe_indexing.init_dataframe_iat(df)


@overload(operator.getitem, no_unliteral=True)
def overload_iat_getitem(I, idx):
    if not isinstance(I, DataFrameIatType):
        return
    if isinstance(idx, types.BaseTuple) and len(idx) == 2:
        if not isinstance(idx.types[0], types.Integer):
            raise BodoError(
                'DataFrame.iat: iAt based indexing can only have integer indexers'
                )
        if not is_overload_constant_int(idx.types[1]):
            raise_bodo_error(
                'DataFrame.iat getitem: column index must be a constant integer. For more informaton, see https://docs.bodo.ai/latest/bodo_parallelism/typing_considerations/#require_constants.'
                )
        adsd__xdmuw = get_overload_const_int(idx.types[1])

        def impl_col_ind(I, idx):
            df = I._obj
            tas__rbhrx = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df,
                adsd__xdmuw)
            return bodo.utils.conversion.box_if_dt64(tas__rbhrx[idx[0]])
        return impl_col_ind
    raise BodoError('df.iat[] getitem using {} not supported'.format(idx))


@overload(operator.setitem, no_unliteral=True)
def overload_iat_setitem(I, idx, val):
    if not isinstance(I, DataFrameIatType):
        return
    if isinstance(idx, types.BaseTuple) and len(idx) == 2:
        if not isinstance(idx.types[0], types.Integer):
            raise BodoError(
                'DataFrame.iat: iAt based indexing can only have integer indexers'
                )
        if not is_overload_constant_int(idx.types[1]):
            raise_bodo_error(
                'DataFrame.iat setitem: column index must be a constant integer. For more informaton, see https://docs.bodo.ai/latest/bodo_parallelism/typing_considerations/#require_constants.'
                )
        adsd__xdmuw = get_overload_const_int(idx.types[1])
        if is_immutable_array(I.df_type.data[adsd__xdmuw]):
            raise BodoError(
                f'DataFrame setitem not supported for column with immutable array type {I.df_type.data}'
                )

        def impl_col_ind(I, idx, val):
            df = I._obj
            tas__rbhrx = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df,
                adsd__xdmuw)
            tas__rbhrx[idx[0]
                ] = bodo.utils.conversion.unbox_if_tz_naive_timestamp(val)
        return impl_col_ind
    raise BodoError('df.iat[] setitem using {} not supported'.format(idx))


@lower_cast(DataFrameIatType, DataFrameIatType)
@lower_cast(DataFrameILocType, DataFrameILocType)
@lower_cast(DataFrameLocType, DataFrameLocType)
def cast_series_iat(context, builder, fromty, toty, val):
    xbl__jrgpz = cgutils.create_struct_proxy(fromty)(context, builder, val)
    hhmg__qztgf = context.cast(builder, xbl__jrgpz.obj, fromty.df_type,
        toty.df_type)
    cvp__iel = cgutils.create_struct_proxy(toty)(context, builder)
    cvp__iel.obj = hhmg__qztgf
    return cvp__iel._getvalue()
