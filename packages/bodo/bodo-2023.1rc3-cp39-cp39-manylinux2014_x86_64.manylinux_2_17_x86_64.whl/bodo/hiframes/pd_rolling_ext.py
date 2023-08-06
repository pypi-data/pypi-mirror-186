"""typing for rolling window functions
"""
from numba.core import cgutils, types
from numba.core.imputils import impl_ret_borrowed
from numba.core.typing.templates import AbstractTemplate, AttributeTemplate, signature
from numba.extending import infer, infer_getattr, intrinsic, lower_builtin, make_attribute_wrapper, models, overload, overload_method, register_model
import bodo
from bodo.hiframes.datetime_timedelta_ext import datetime_timedelta_type, pd_timedelta_type
from bodo.hiframes.pd_dataframe_ext import DataFrameType, check_runtime_cols_unsupported
from bodo.hiframes.pd_groupby_ext import DataFrameGroupByType
from bodo.hiframes.pd_series_ext import SeriesType
from bodo.hiframes.rolling import supported_rolling_funcs, unsupported_rolling_methods
from bodo.utils.typing import BodoError, check_unsupported_args, create_unsupported_overload, get_literal_value, is_const_func_type, is_literal_type, is_overload_bool, is_overload_constant_str, is_overload_int, is_overload_none, raise_bodo_error


class RollingType(types.Type):

    def __init__(self, obj_type, window_type, on, selection,
        explicit_select=False, series_select=False):
        if isinstance(obj_type, bodo.SeriesType):
            rvkxc__wir = 'Series'
        else:
            rvkxc__wir = 'DataFrame'
        bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(obj_type,
            f'{rvkxc__wir}.rolling()')
        self.obj_type = obj_type
        self.window_type = window_type
        self.on = on
        self.selection = selection
        self.explicit_select = explicit_select
        self.series_select = series_select
        super(RollingType, self).__init__(name=
            f'RollingType({obj_type}, {window_type}, {on}, {selection}, {explicit_select}, {series_select})'
            )

    def copy(self):
        return RollingType(self.obj_type, self.window_type, self.on, self.
            selection, self.explicit_select, self.series_select)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


@register_model(RollingType)
class RollingModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        ksb__bbpx = [('obj', fe_type.obj_type), ('window', fe_type.
            window_type), ('min_periods', types.int64), ('center', types.bool_)
            ]
        super(RollingModel, self).__init__(dmm, fe_type, ksb__bbpx)


make_attribute_wrapper(RollingType, 'obj', 'obj')
make_attribute_wrapper(RollingType, 'window', 'window')
make_attribute_wrapper(RollingType, 'center', 'center')
make_attribute_wrapper(RollingType, 'min_periods', 'min_periods')


@overload_method(DataFrameType, 'rolling', inline='always', no_unliteral=True)
def df_rolling_overload(df, window, min_periods=None, center=False,
    win_type=None, on=None, axis=0, closed=None):
    check_runtime_cols_unsupported(df, 'DataFrame.rolling()')
    kodv__fxkw = dict(win_type=win_type, axis=axis, closed=closed)
    pbaru__yjdzr = dict(win_type=None, axis=0, closed=None)
    check_unsupported_args('DataFrame.rolling', kodv__fxkw, pbaru__yjdzr,
        package_name='pandas', module_name='Window')
    _validate_rolling_args(df, window, min_periods, center, on)

    def impl(df, window, min_periods=None, center=False, win_type=None, on=
        None, axis=0, closed=None):
        min_periods = _handle_default_min_periods(min_periods, window)
        return bodo.hiframes.pd_rolling_ext.init_rolling(df, window,
            min_periods, center, on)
    return impl


@overload_method(SeriesType, 'rolling', inline='always', no_unliteral=True)
def overload_series_rolling(S, window, min_periods=None, center=False,
    win_type=None, on=None, axis=0, closed=None):
    kodv__fxkw = dict(win_type=win_type, axis=axis, closed=closed)
    pbaru__yjdzr = dict(win_type=None, axis=0, closed=None)
    check_unsupported_args('Series.rolling', kodv__fxkw, pbaru__yjdzr,
        package_name='pandas', module_name='Window')
    _validate_rolling_args(S, window, min_periods, center, on)

    def impl(S, window, min_periods=None, center=False, win_type=None, on=
        None, axis=0, closed=None):
        min_periods = _handle_default_min_periods(min_periods, window)
        return bodo.hiframes.pd_rolling_ext.init_rolling(S, window,
            min_periods, center, on)
    return impl


@intrinsic
def init_rolling(typingctx, obj_type, window_type, min_periods_type,
    center_type, on_type=None):

    def codegen(context, builder, signature, args):
        mcy__zjiz, dths__rsysi, puf__qua, qqxlh__abq, pro__lwsx = args
        wlo__atkmc = signature.return_type
        neis__exg = cgutils.create_struct_proxy(wlo__atkmc)(context, builder)
        neis__exg.obj = mcy__zjiz
        neis__exg.window = dths__rsysi
        neis__exg.min_periods = puf__qua
        neis__exg.center = qqxlh__abq
        context.nrt.incref(builder, signature.args[0], mcy__zjiz)
        context.nrt.incref(builder, signature.args[1], dths__rsysi)
        context.nrt.incref(builder, signature.args[2], puf__qua)
        context.nrt.incref(builder, signature.args[3], qqxlh__abq)
        return neis__exg._getvalue()
    on = get_literal_value(on_type)
    if isinstance(obj_type, SeriesType):
        selection = None
    elif isinstance(obj_type, DataFrameType):
        selection = obj_type.columns
    else:
        assert isinstance(obj_type, DataFrameGroupByType
            ), f'invalid obj type for rolling: {obj_type}'
        selection = obj_type.selection
    wlo__atkmc = RollingType(obj_type, window_type, on, selection, False)
    return wlo__atkmc(obj_type, window_type, min_periods_type, center_type,
        on_type), codegen


def _handle_default_min_periods(min_periods, window):
    return min_periods


@overload(_handle_default_min_periods)
def overload_handle_default_min_periods(min_periods, window):
    if is_overload_none(min_periods):
        if isinstance(window, types.Integer):
            return lambda min_periods, window: window
        else:
            return lambda min_periods, window: 1
    else:
        return lambda min_periods, window: min_periods


def _gen_df_rolling_out_data(rolling):
    pnwx__shi = not isinstance(rolling.window_type, types.Integer)
    xiinl__kbq = 'variable' if pnwx__shi else 'fixed'
    tjaq__xdrhw = 'None'
    if pnwx__shi:
        tjaq__xdrhw = ('bodo.utils.conversion.index_to_array(index)' if 
            rolling.on is None else
            f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {rolling.obj_type.columns.index(rolling.on)})'
            )
    usgja__mfyw = []
    zphu__lkc = 'on_arr, ' if pnwx__shi else ''
    if isinstance(rolling.obj_type, SeriesType):
        return (
            f'bodo.hiframes.rolling.rolling_{xiinl__kbq}(bodo.hiframes.pd_series_ext.get_series_data(df), {zphu__lkc}index_arr, window, minp, center, func, raw)'
            , tjaq__xdrhw, rolling.selection)
    assert isinstance(rolling.obj_type, DataFrameType
        ), 'expected df in rolling obj'
    nfk__dbs = rolling.obj_type.data
    out_cols = []
    for lbbxb__caqnb in rolling.selection:
        vxpd__fpe = rolling.obj_type.columns.index(lbbxb__caqnb)
        if lbbxb__caqnb == rolling.on:
            if len(rolling.selection) == 2 and rolling.series_select:
                continue
            zvrnt__iuztv = (
                f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {vxpd__fpe})'
                )
            out_cols.append(lbbxb__caqnb)
        else:
            if not isinstance(nfk__dbs[vxpd__fpe].dtype, (types.Boolean,
                types.Number)):
                continue
            zvrnt__iuztv = (
                f'bodo.hiframes.rolling.rolling_{xiinl__kbq}(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {vxpd__fpe}), {zphu__lkc}index_arr, window, minp, center, func, raw)'
                )
            out_cols.append(lbbxb__caqnb)
        usgja__mfyw.append(zvrnt__iuztv)
    return ', '.join(usgja__mfyw), tjaq__xdrhw, tuple(out_cols)


@overload_method(RollingType, 'apply', inline='always', no_unliteral=True)
def overload_rolling_apply(rolling, func, raw=False, engine=None,
    engine_kwargs=None, args=None, kwargs=None):
    kodv__fxkw = dict(engine=engine, engine_kwargs=engine_kwargs, args=args,
        kwargs=kwargs)
    pbaru__yjdzr = dict(engine=None, engine_kwargs=None, args=None, kwargs=None
        )
    check_unsupported_args('Rolling.apply', kodv__fxkw, pbaru__yjdzr,
        package_name='pandas', module_name='Window')
    if not is_const_func_type(func):
        raise BodoError(
            f"Rolling.apply(): 'func' parameter must be a function, not {func} (builtin functions not supported yet)."
            )
    if not is_overload_bool(raw):
        raise BodoError(
            f"Rolling.apply(): 'raw' parameter must be bool, not {raw}.")
    return _gen_rolling_impl(rolling, 'apply')


@overload_method(DataFrameGroupByType, 'rolling', inline='always',
    no_unliteral=True)
def groupby_rolling_overload(grp, window, min_periods=None, center=False,
    win_type=None, on=None, axis=0, closed=None, method='single'):
    kodv__fxkw = dict(win_type=win_type, axis=axis, closed=closed, method=
        method)
    pbaru__yjdzr = dict(win_type=None, axis=0, closed=None, method='single')
    check_unsupported_args('GroupBy.rolling', kodv__fxkw, pbaru__yjdzr,
        package_name='pandas', module_name='Window')
    _validate_rolling_args(grp, window, min_periods, center, on)

    def _impl(grp, window, min_periods=None, center=False, win_type=None,
        on=None, axis=0, closed=None, method='single'):
        min_periods = _handle_default_min_periods(min_periods, window)
        return bodo.hiframes.pd_rolling_ext.init_rolling(grp, window,
            min_periods, center, on)
    return _impl


def _gen_rolling_impl(rolling, fname, other=None):
    if isinstance(rolling.obj_type, DataFrameGroupByType):
        ssuqf__fol = f'def impl(rolling, {_get_rolling_func_args(fname)}):\n'
        jmdl__qura = f"'{rolling.on}'" if isinstance(rolling.on, str
            ) else f'{rolling.on}'
        selection = ''
        if rolling.explicit_select:
            selection = '[{}]'.format(', '.join(f"'{yxbcs__tgefp}'" if
                isinstance(yxbcs__tgefp, str) else f'{yxbcs__tgefp}' for
                yxbcs__tgefp in rolling.selection if yxbcs__tgefp !=
                rolling.on))
        ekk__qdpfu = buvc__ufug = ''
        if fname == 'apply':
            ekk__qdpfu = 'func, raw, args, kwargs'
            buvc__ufug = 'func, raw, None, None, args, kwargs'
        if fname == 'corr':
            ekk__qdpfu = buvc__ufug = 'other, pairwise'
        if fname == 'cov':
            ekk__qdpfu = buvc__ufug = 'other, pairwise, ddof'
        lbvl__kbxmz = (
            f'lambda df, window, minp, center, {ekk__qdpfu}: bodo.hiframes.pd_rolling_ext.init_rolling(df, window, minp, center, {jmdl__qura}){selection}.{fname}({buvc__ufug})'
            )
        ssuqf__fol += f"""  return rolling.obj.apply({lbvl__kbxmz}, rolling.window, rolling.min_periods, rolling.center, {ekk__qdpfu})
"""
        cnuxe__bwy = {}
        exec(ssuqf__fol, {'bodo': bodo}, cnuxe__bwy)
        impl = cnuxe__bwy['impl']
        return impl
    xwiz__qxnq = isinstance(rolling.obj_type, SeriesType)
    if fname in ('corr', 'cov'):
        out_cols = None if xwiz__qxnq else _get_corr_cov_out_cols(rolling,
            other, fname)
        df_cols = None if xwiz__qxnq else rolling.obj_type.columns
        other_cols = None if xwiz__qxnq else other.columns
        usgja__mfyw, tjaq__xdrhw = _gen_corr_cov_out_data(out_cols, df_cols,
            other_cols, rolling.window_type, fname)
    else:
        usgja__mfyw, tjaq__xdrhw, out_cols = _gen_df_rolling_out_data(rolling)
    pyn__pwy = xwiz__qxnq or len(rolling.selection) == (1 if rolling.on is
        None else 2) and rolling.series_select
    odr__vyg = f'def impl(rolling, {_get_rolling_func_args(fname)}):\n'
    odr__vyg += '  df = rolling.obj\n'
    odr__vyg += '  index = {}\n'.format(
        'bodo.hiframes.pd_series_ext.get_series_index(df)' if xwiz__qxnq else
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)')
    rvkxc__wir = 'None'
    if xwiz__qxnq:
        rvkxc__wir = 'bodo.hiframes.pd_series_ext.get_series_name(df)'
    elif pyn__pwy:
        lbbxb__caqnb = (set(out_cols) - set([rolling.on])).pop()
        rvkxc__wir = f"'{lbbxb__caqnb}'" if isinstance(lbbxb__caqnb, str
            ) else str(lbbxb__caqnb)
    odr__vyg += f'  name = {rvkxc__wir}\n'
    odr__vyg += '  window = rolling.window\n'
    odr__vyg += '  center = rolling.center\n'
    odr__vyg += '  minp = rolling.min_periods\n'
    odr__vyg += f'  on_arr = {tjaq__xdrhw}\n'
    if fname == 'apply':
        odr__vyg += (
            f'  index_arr = bodo.utils.conversion.index_to_array(index)\n')
    else:
        odr__vyg += f"  func = '{fname}'\n"
        odr__vyg += f'  index_arr = None\n'
        odr__vyg += f'  raw = False\n'
    if pyn__pwy:
        odr__vyg += (
            f'  return bodo.hiframes.pd_series_ext.init_series({usgja__mfyw}, index, name)'
            )
        cnuxe__bwy = {}
        rzo__efk = {'bodo': bodo}
        exec(odr__vyg, rzo__efk, cnuxe__bwy)
        impl = cnuxe__bwy['impl']
        return impl
    return bodo.hiframes.dataframe_impl._gen_init_df(odr__vyg, out_cols,
        usgja__mfyw)


def _get_rolling_func_args(fname):
    if fname == 'apply':
        return (
            'func, raw=False, engine=None, engine_kwargs=None, args=None, kwargs=None\n'
            )
    elif fname == 'corr':
        return 'other=None, pairwise=None, ddof=1\n'
    elif fname == 'cov':
        return 'other=None, pairwise=None, ddof=1\n'
    return ''


def create_rolling_overload(fname):

    def overload_rolling_func(rolling):
        return _gen_rolling_impl(rolling, fname)
    return overload_rolling_func


def _install_rolling_methods():
    for fname in supported_rolling_funcs:
        if fname in ('apply', 'corr', 'cov'):
            continue
        sph__xchie = create_rolling_overload(fname)
        overload_method(RollingType, fname, inline='always', no_unliteral=True
            )(sph__xchie)


def _install_rolling_unsupported_methods():
    for fname in unsupported_rolling_methods:
        overload_method(RollingType, fname, no_unliteral=True)(
            create_unsupported_overload(
            f'pandas.core.window.rolling.Rolling.{fname}()'))


_install_rolling_methods()
_install_rolling_unsupported_methods()


def _get_corr_cov_out_cols(rolling, other, func_name):
    if not isinstance(other, DataFrameType):
        raise_bodo_error(
            f"DataFrame.rolling.{func_name}(): requires providing a DataFrame for 'other'"
            )
    awru__uff = rolling.selection
    if rolling.on is not None:
        raise BodoError(
            f'variable window rolling {func_name} not supported yet.')
    out_cols = tuple(sorted(set(awru__uff) | set(other.columns), key=lambda
        k: str(k)))
    return out_cols


def _gen_corr_cov_out_data(out_cols, df_cols, other_cols, window_type,
    func_name):
    pnwx__shi = not isinstance(window_type, types.Integer)
    tjaq__xdrhw = 'None'
    if pnwx__shi:
        tjaq__xdrhw = 'bodo.utils.conversion.index_to_array(index)'
    zphu__lkc = 'on_arr, ' if pnwx__shi else ''
    usgja__mfyw = []
    if out_cols is None:
        return (
            f'bodo.hiframes.rolling.rolling_{func_name}(bodo.hiframes.pd_series_ext.get_series_data(df), bodo.hiframes.pd_series_ext.get_series_data(other), {zphu__lkc}window, minp, center)'
            , tjaq__xdrhw)
    for lbbxb__caqnb in out_cols:
        if lbbxb__caqnb in df_cols and lbbxb__caqnb in other_cols:
            jxl__azbjg = df_cols.index(lbbxb__caqnb)
            gbh__jdmv = other_cols.index(lbbxb__caqnb)
            zvrnt__iuztv = (
                f'bodo.hiframes.rolling.rolling_{func_name}(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {jxl__azbjg}), bodo.hiframes.pd_dataframe_ext.get_dataframe_data(other, {gbh__jdmv}), {zphu__lkc}window, minp, center)'
                )
        else:
            zvrnt__iuztv = 'np.full(len(df), np.nan)'
        usgja__mfyw.append(zvrnt__iuztv)
    return ', '.join(usgja__mfyw), tjaq__xdrhw


@overload_method(RollingType, 'corr', inline='always', no_unliteral=True)
def overload_rolling_corr(rolling, other=None, pairwise=None, ddof=1):
    dxg__bkekk = {'pairwise': pairwise, 'ddof': ddof}
    rmoa__xdvrq = {'pairwise': None, 'ddof': 1}
    check_unsupported_args('pandas.core.window.rolling.Rolling.corr',
        dxg__bkekk, rmoa__xdvrq, package_name='pandas', module_name='Window')
    return _gen_rolling_impl(rolling, 'corr', other)


@overload_method(RollingType, 'cov', inline='always', no_unliteral=True)
def overload_rolling_cov(rolling, other=None, pairwise=None, ddof=1):
    dxg__bkekk = {'ddof': ddof, 'pairwise': pairwise}
    rmoa__xdvrq = {'ddof': 1, 'pairwise': None}
    check_unsupported_args('pandas.core.window.rolling.Rolling.cov',
        dxg__bkekk, rmoa__xdvrq, package_name='pandas', module_name='Window')
    return _gen_rolling_impl(rolling, 'cov', other)


@infer
class GetItemDataFrameRolling2(AbstractTemplate):
    key = 'static_getitem'

    def generic(self, args, kws):
        rolling, ybiwz__unk = args
        if isinstance(rolling, RollingType):
            awru__uff = rolling.obj_type.selection if isinstance(rolling.
                obj_type, DataFrameGroupByType) else rolling.obj_type.columns
            series_select = False
            if isinstance(ybiwz__unk, (tuple, list)):
                if len(set(ybiwz__unk).difference(set(awru__uff))) > 0:
                    raise_bodo_error(
                        'rolling: selected column {} not found in dataframe'
                        .format(set(ybiwz__unk).difference(set(awru__uff))))
                selection = list(ybiwz__unk)
            else:
                if ybiwz__unk not in awru__uff:
                    raise_bodo_error(
                        'rolling: selected column {} not found in dataframe'
                        .format(ybiwz__unk))
                selection = [ybiwz__unk]
                series_select = True
            if rolling.on is not None:
                selection.append(rolling.on)
            fzenb__csy = RollingType(rolling.obj_type, rolling.window_type,
                rolling.on, tuple(selection), True, series_select)
            return signature(fzenb__csy, *args)


@lower_builtin('static_getitem', RollingType, types.Any)
def static_getitem_df_groupby(context, builder, sig, args):
    return impl_ret_borrowed(context, builder, sig.return_type, args[0])


@infer_getattr
class RollingAttribute(AttributeTemplate):
    key = RollingType

    def generic_resolve(self, rolling, attr):
        awru__uff = ()
        if isinstance(rolling.obj_type, DataFrameGroupByType):
            awru__uff = rolling.obj_type.selection
        if isinstance(rolling.obj_type, DataFrameType):
            awru__uff = rolling.obj_type.columns
        if attr in awru__uff:
            return RollingType(rolling.obj_type, rolling.window_type,
                rolling.on, (attr,) if rolling.on is None else (attr,
                rolling.on), True, True)


def _validate_rolling_args(obj, window, min_periods, center, on):
    assert isinstance(obj, (SeriesType, DataFrameType, DataFrameGroupByType)
        ), 'invalid rolling obj'
    func_name = 'Series' if isinstance(obj, SeriesType
        ) else 'DataFrame' if isinstance(obj, DataFrameType
        ) else 'DataFrameGroupBy'
    if not (is_overload_int(window) or is_overload_constant_str(window) or 
        window == bodo.string_type or window in (pd_timedelta_type,
        datetime_timedelta_type)):
        raise BodoError(
            f"{func_name}.rolling(): 'window' should be int or time offset (str, pd.Timedelta, datetime.timedelta), not {window}"
            )
    if not is_overload_bool(center):
        raise BodoError(
            f'{func_name}.rolling(): center must be a boolean, not {center}')
    if not (is_overload_none(min_periods) or isinstance(min_periods, types.
        Integer)):
        raise BodoError(
            f'{func_name}.rolling(): min_periods must be an integer, not {min_periods}'
            )
    if isinstance(obj, SeriesType) and not is_overload_none(on):
        raise BodoError(
            f"{func_name}.rolling(): 'on' not supported for Series yet (can use a DataFrame instead)."
            )
    dmcf__xgnp = obj.columns if isinstance(obj, DataFrameType
        ) else obj.df_type.columns if isinstance(obj, DataFrameGroupByType
        ) else []
    nfk__dbs = [obj.data] if isinstance(obj, SeriesType
        ) else obj.data if isinstance(obj, DataFrameType) else obj.df_type.data
    if not is_overload_none(on) and (not is_literal_type(on) or 
        get_literal_value(on) not in dmcf__xgnp):
        raise BodoError(
            f"{func_name}.rolling(): 'on' should be a constant column name.")
    if not is_overload_none(on):
        rppf__wgbtm = nfk__dbs[dmcf__xgnp.index(get_literal_value(on))]
        if not isinstance(rppf__wgbtm, types.Array
            ) or rppf__wgbtm.dtype != bodo.datetime64ns:
            raise BodoError(
                f"{func_name}.rolling(): 'on' column should have datetime64 data."
                )
    if not any(isinstance(oerkl__wpp.dtype, (types.Boolean, types.Number)) for
        oerkl__wpp in nfk__dbs):
        raise BodoError(f'{func_name}.rolling(): No numeric types to aggregate'
            )
