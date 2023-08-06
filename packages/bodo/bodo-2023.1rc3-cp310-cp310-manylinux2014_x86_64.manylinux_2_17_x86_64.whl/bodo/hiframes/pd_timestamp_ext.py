"""Timestamp extension for Pandas Timestamp with timezone support."""
import calendar
import datetime
import operator
from typing import Union
import llvmlite.binding as ll
import numba
import numpy as np
import pandas as pd
import pytz
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.imputils import lower_constant
from numba.core.typing.templates import ConcreteTemplate, infer_global, signature
from numba.extending import NativeValue, box, intrinsic, lower_builtin, lower_cast, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_jitable, register_model, typeof_impl, unbox
import bodo.libs.str_ext
import bodo.utils.utils
from bodo.hiframes.datetime_date_ext import DatetimeDateType, _ord2ymd, _ymd2ord, get_isocalendar
from bodo.hiframes.datetime_timedelta_ext import PDTimeDeltaType, _no_input, datetime_timedelta_type, pd_timedelta_type
from bodo.hiframes.pd_categorical_ext import CategoricalArrayType
from bodo.libs import hdatetime_ext
from bodo.libs.pd_datetime_arr_ext import get_pytz_type_info
from bodo.libs.str_arr_ext import string_array_type
from bodo.utils.typing import BodoError, check_unsupported_args, get_literal_value, get_overload_const_bool, get_overload_const_int, get_overload_const_str, is_iterable_type, is_literal_type, is_overload_constant_int, is_overload_constant_str, is_overload_none, raise_bodo_error
ll.add_symbol('extract_year_days', hdatetime_ext.extract_year_days)
ll.add_symbol('get_month_day', hdatetime_ext.get_month_day)
ll.add_symbol('npy_datetimestruct_to_datetime', hdatetime_ext.
    npy_datetimestruct_to_datetime)
npy_datetimestruct_to_datetime = types.ExternalFunction(
    'npy_datetimestruct_to_datetime', types.int64(types.int64, types.int32,
    types.int32, types.int32, types.int32, types.int32, types.int32))
date_fields = ['year', 'month', 'day', 'hour', 'minute', 'second',
    'microsecond', 'nanosecond', 'quarter', 'dayofyear', 'day_of_year',
    'dayofweek', 'day_of_week', 'daysinmonth', 'days_in_month',
    'is_leap_year', 'is_month_start', 'is_month_end', 'is_quarter_start',
    'is_quarter_end', 'is_year_start', 'is_year_end', 'week', 'weekofyear',
    'weekday']
date_methods = ['normalize', 'day_name', 'month_name']
timedelta_fields = ['days', 'seconds', 'microseconds', 'nanoseconds']
timedelta_methods = ['total_seconds', 'to_pytimedelta']
iNaT = pd._libs.tslibs.iNaT


class PandasTimestampType(types.Type):

    def __init__(self, tz_val=None):
        self.tz = tz_val
        if tz_val is None:
            imfyi__dpm = 'PandasTimestampType()'
        else:
            imfyi__dpm = f'PandasTimestampType({tz_val})'
        super(PandasTimestampType, self).__init__(name=imfyi__dpm)


pd_timestamp_tz_naive_type = PandasTimestampType()


def check_tz_aware_unsupported(val, func_name):
    if isinstance(val, bodo.hiframes.series_dt_impl.
        SeriesDatetimePropertiesType):
        val = val.stype
    if isinstance(val, PandasTimestampType) and val.tz is not None:
        raise BodoError(
            f'{func_name} on Timezone-aware timestamp not yet supported. Please convert to timezone naive with ts.tz_convert(None)'
            )
    elif isinstance(val, bodo.DatetimeArrayType):
        raise BodoError(
            f'{func_name} on Timezone-aware array not yet supported. Please convert to timezone naive with arr.tz_convert(None)'
            )
    elif isinstance(val, bodo.DatetimeIndexType) and isinstance(val.data,
        bodo.DatetimeArrayType):
        raise BodoError(
            f'{func_name} on Timezone-aware index not yet supported. Please convert to timezone naive with index.tz_convert(None)'
            )
    elif isinstance(val, bodo.SeriesType) and isinstance(val.data, bodo.
        DatetimeArrayType):
        raise BodoError(
            f'{func_name} on Timezone-aware series not yet supported. Please convert to timezone naive with series.dt.tz_convert(None)'
            )
    elif isinstance(val, bodo.DataFrameType):
        for uqb__qhrtz in val.data:
            if isinstance(uqb__qhrtz, bodo.DatetimeArrayType):
                raise BodoError(
                    f'{func_name} on Timezone-aware columns not yet supported. Please convert each column to timezone naive with series.dt.tz_convert(None)'
                    )


@typeof_impl.register(pd.Timestamp)
def typeof_pd_timestamp(val, c):
    return PandasTimestampType(get_pytz_type_info(val.tz) if val.tz else None)


ts_field_typ = types.int64


@register_model(PandasTimestampType)
class PandasTimestampModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        iqw__jbsa = [('year', ts_field_typ), ('month', ts_field_typ), (
            'day', ts_field_typ), ('hour', ts_field_typ), ('minute',
            ts_field_typ), ('second', ts_field_typ), ('microsecond',
            ts_field_typ), ('nanosecond', ts_field_typ), ('value',
            ts_field_typ)]
        models.StructModel.__init__(self, dmm, fe_type, iqw__jbsa)


make_attribute_wrapper(PandasTimestampType, 'year', 'year')
make_attribute_wrapper(PandasTimestampType, 'month', 'month')
make_attribute_wrapper(PandasTimestampType, 'day', 'day')
make_attribute_wrapper(PandasTimestampType, 'hour', 'hour')
make_attribute_wrapper(PandasTimestampType, 'minute', 'minute')
make_attribute_wrapper(PandasTimestampType, 'second', 'second')
make_attribute_wrapper(PandasTimestampType, 'microsecond', 'microsecond')
make_attribute_wrapper(PandasTimestampType, 'nanosecond', 'nanosecond')
make_attribute_wrapper(PandasTimestampType, 'value', 'value')


@unbox(PandasTimestampType)
def unbox_pandas_timestamp(typ, val, c):
    zqke__rxmf = c.pyapi.object_getattr_string(val, 'year')
    xeou__lsg = c.pyapi.object_getattr_string(val, 'month')
    wylk__mxyxq = c.pyapi.object_getattr_string(val, 'day')
    msr__lcnlg = c.pyapi.object_getattr_string(val, 'hour')
    exwfy__ixy = c.pyapi.object_getattr_string(val, 'minute')
    gefl__rhlx = c.pyapi.object_getattr_string(val, 'second')
    quymk__lecg = c.pyapi.object_getattr_string(val, 'microsecond')
    bzhse__hrr = c.pyapi.object_getattr_string(val, 'nanosecond')
    ofvg__dgx = c.pyapi.object_getattr_string(val, 'value')
    afars__hlv = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    afars__hlv.year = c.pyapi.long_as_longlong(zqke__rxmf)
    afars__hlv.month = c.pyapi.long_as_longlong(xeou__lsg)
    afars__hlv.day = c.pyapi.long_as_longlong(wylk__mxyxq)
    afars__hlv.hour = c.pyapi.long_as_longlong(msr__lcnlg)
    afars__hlv.minute = c.pyapi.long_as_longlong(exwfy__ixy)
    afars__hlv.second = c.pyapi.long_as_longlong(gefl__rhlx)
    afars__hlv.microsecond = c.pyapi.long_as_longlong(quymk__lecg)
    afars__hlv.nanosecond = c.pyapi.long_as_longlong(bzhse__hrr)
    afars__hlv.value = c.pyapi.long_as_longlong(ofvg__dgx)
    c.pyapi.decref(zqke__rxmf)
    c.pyapi.decref(xeou__lsg)
    c.pyapi.decref(wylk__mxyxq)
    c.pyapi.decref(msr__lcnlg)
    c.pyapi.decref(exwfy__ixy)
    c.pyapi.decref(gefl__rhlx)
    c.pyapi.decref(quymk__lecg)
    c.pyapi.decref(bzhse__hrr)
    c.pyapi.decref(ofvg__dgx)
    ixn__lavty = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(afars__hlv._getvalue(), is_error=ixn__lavty)


@box(PandasTimestampType)
def box_pandas_timestamp(typ, val, c):
    mdbu__mdw = cgutils.create_struct_proxy(typ)(c.context, c.builder,
        value=val)
    zqke__rxmf = c.pyapi.long_from_longlong(mdbu__mdw.year)
    xeou__lsg = c.pyapi.long_from_longlong(mdbu__mdw.month)
    wylk__mxyxq = c.pyapi.long_from_longlong(mdbu__mdw.day)
    msr__lcnlg = c.pyapi.long_from_longlong(mdbu__mdw.hour)
    exwfy__ixy = c.pyapi.long_from_longlong(mdbu__mdw.minute)
    gefl__rhlx = c.pyapi.long_from_longlong(mdbu__mdw.second)
    ale__ttgy = c.pyapi.long_from_longlong(mdbu__mdw.microsecond)
    rqei__wau = c.pyapi.long_from_longlong(mdbu__mdw.nanosecond)
    vgs__uyiim = c.pyapi.unserialize(c.pyapi.serialize_object(pd.Timestamp))
    if typ.tz is None:
        res = c.pyapi.call_function_objargs(vgs__uyiim, (zqke__rxmf,
            xeou__lsg, wylk__mxyxq, msr__lcnlg, exwfy__ixy, gefl__rhlx,
            ale__ttgy, rqei__wau))
    else:
        if isinstance(typ.tz, int):
            nvfcn__aqw = c.pyapi.long_from_longlong(lir.Constant(lir.
                IntType(64), typ.tz))
        else:
            jes__uhx = c.context.insert_const_string(c.builder.module, str(
                typ.tz))
            nvfcn__aqw = c.pyapi.string_from_string(jes__uhx)
        args = c.pyapi.tuple_pack(())
        kwargs = c.pyapi.dict_pack([('year', zqke__rxmf), ('month',
            xeou__lsg), ('day', wylk__mxyxq), ('hour', msr__lcnlg), (
            'minute', exwfy__ixy), ('second', gefl__rhlx), ('microsecond',
            ale__ttgy), ('nanosecond', rqei__wau), ('tz', nvfcn__aqw)])
        res = c.pyapi.call(vgs__uyiim, args, kwargs)
        c.pyapi.decref(args)
        c.pyapi.decref(kwargs)
        c.pyapi.decref(nvfcn__aqw)
    c.pyapi.decref(zqke__rxmf)
    c.pyapi.decref(xeou__lsg)
    c.pyapi.decref(wylk__mxyxq)
    c.pyapi.decref(msr__lcnlg)
    c.pyapi.decref(exwfy__ixy)
    c.pyapi.decref(gefl__rhlx)
    c.pyapi.decref(ale__ttgy)
    c.pyapi.decref(rqei__wau)
    return res


@intrinsic
def init_timestamp(typingctx, year, month, day, hour, minute, second,
    microsecond, nanosecond, value, tz):

    def codegen(context, builder, sig, args):
        (year, month, day, hour, minute, second, jwozq__vcic, lfg__urfl,
            value, ynuvr__syafm) = args
        ts = cgutils.create_struct_proxy(sig.return_type)(context, builder)
        ts.year = year
        ts.month = month
        ts.day = day
        ts.hour = hour
        ts.minute = minute
        ts.second = second
        ts.microsecond = jwozq__vcic
        ts.nanosecond = lfg__urfl
        ts.value = value
        return ts._getvalue()
    if is_overload_none(tz):
        typ = pd_timestamp_tz_naive_type
    elif is_overload_constant_str(tz):
        typ = PandasTimestampType(get_overload_const_str(tz))
    elif is_overload_constant_int(tz):
        typ = PandasTimestampType(get_overload_const_int(tz))
    else:
        raise_bodo_error('tz must be a constant string, int, or None')
    return typ(types.int64, types.int64, types.int64, types.int64, types.
        int64, types.int64, types.int64, types.int64, types.int64, tz), codegen


@numba.generated_jit
def zero_if_none(value):
    if value == types.none:
        return lambda value: 0
    return lambda value: value


@lower_constant(PandasTimestampType)
def constant_timestamp(context, builder, ty, pyval):
    year = context.get_constant(types.int64, pyval.year)
    month = context.get_constant(types.int64, pyval.month)
    day = context.get_constant(types.int64, pyval.day)
    hour = context.get_constant(types.int64, pyval.hour)
    minute = context.get_constant(types.int64, pyval.minute)
    second = context.get_constant(types.int64, pyval.second)
    microsecond = context.get_constant(types.int64, pyval.microsecond)
    nanosecond = context.get_constant(types.int64, pyval.nanosecond)
    value = context.get_constant(types.int64, pyval.value)
    return lir.Constant.literal_struct((year, month, day, hour, minute,
        second, microsecond, nanosecond, value))


def tz_has_transition_times(tz: Union[str, int, None]):
    if isinstance(tz, str):
        otzyh__cvj = pytz.timezone(tz)
        return isinstance(otzyh__cvj, pytz.tzinfo.DstTzInfo)
    return False


@overload(pd.Timestamp, no_unliteral=True)
def overload_pd_timestamp(ts_input=_no_input, freq=None, tz=None, unit=None,
    year=None, month=None, day=None, hour=None, minute=None, second=None,
    microsecond=None, nanosecond=None, tzinfo=None):
    if not is_overload_none(tz) and is_overload_constant_str(tz
        ) and get_overload_const_str(tz) not in pytz.all_timezones_set:
        raise BodoError(
            "pandas.Timestamp(): 'tz', if provided, must be constant string found in pytz.all_timezones"
            )
    if ts_input == _no_input or getattr(ts_input, 'value', None) == _no_input:

        def impl_kw(ts_input=_no_input, freq=None, tz=None, unit=None, year
            =None, month=None, day=None, hour=None, minute=None, second=
            None, microsecond=None, nanosecond=None, tzinfo=None):
            return compute_val_for_timestamp(year, month, day, zero_if_none
                (hour), zero_if_none(minute), zero_if_none(second),
                zero_if_none(microsecond), zero_if_none(nanosecond), tz)
        return impl_kw
    if isinstance(types.unliteral(freq), types.Integer):

        def impl_pos(ts_input=_no_input, freq=None, tz=None, unit=None,
            year=None, month=None, day=None, hour=None, minute=None, second
            =None, microsecond=None, nanosecond=None, tzinfo=None):
            return compute_val_for_timestamp(ts_input, freq, tz,
                zero_if_none(unit), zero_if_none(year), zero_if_none(month),
                zero_if_none(day), zero_if_none(hour), None)
        return impl_pos
    if isinstance(ts_input, types.Number):
        if is_overload_none(unit):
            unit = 'ns'
        if not is_overload_constant_str(unit):
            raise BodoError(
                'pandas.Timedelta(): unit argument must be a constant str')
        unit = pd._libs.tslibs.timedeltas.parse_timedelta_unit(
            get_overload_const_str(unit))
        fgam__bry, precision = pd._libs.tslibs.conversion.precision_from_unit(
            unit)
        if isinstance(ts_input, types.Integer):

            def impl_int(ts_input=_no_input, freq=None, tz=None, unit=None,
                year=None, month=None, day=None, hour=None, minute=None,
                second=None, microsecond=None, nanosecond=None, tzinfo=None):
                value = ts_input * fgam__bry
                return convert_val_to_timestamp(value, tz)
            return impl_int

        def impl_float(ts_input=_no_input, freq=None, tz=None, unit=None,
            year=None, month=None, day=None, hour=None, minute=None, second
            =None, microsecond=None, nanosecond=None, tzinfo=None):
            nqzox__hmh = np.int64(ts_input)
            nwijm__zhmfa = ts_input - nqzox__hmh
            if precision:
                nwijm__zhmfa = np.round(nwijm__zhmfa, precision)
            value = nqzox__hmh * fgam__bry + np.int64(nwijm__zhmfa * fgam__bry)
            return convert_val_to_timestamp(value, tz)
        return impl_float
    if ts_input == bodo.string_type or is_overload_constant_str(ts_input):
        types.pd_timestamp_tz_naive_type = pd_timestamp_tz_naive_type
        if is_overload_none(tz):
            tz_val = None
        elif is_overload_constant_str(tz):
            tz_val = get_overload_const_str(tz)
        else:
            raise_bodo_error(
                'pandas.Timestamp(): tz argument must be a constant string or None'
                )
        typ = PandasTimestampType(tz_val)

        def impl_str(ts_input=_no_input, freq=None, tz=None, unit=None,
            year=None, month=None, day=None, hour=None, minute=None, second
            =None, microsecond=None, nanosecond=None, tzinfo=None):
            with numba.objmode(res=typ):
                res = pd.Timestamp(ts_input, tz=tz)
            return res
        return impl_str
    if isinstance(ts_input, PandasTimestampType):
        return (lambda ts_input=_no_input, freq=None, tz=None, unit=None,
            year=None, month=None, day=None, hour=None, minute=None, second
            =None, microsecond=None, nanosecond=None, tzinfo=None: ts_input)
    if ts_input == bodo.hiframes.datetime_datetime_ext.datetime_datetime_type:

        def impl_datetime(ts_input=_no_input, freq=None, tz=None, unit=None,
            year=None, month=None, day=None, hour=None, minute=None, second
            =None, microsecond=None, nanosecond=None, tzinfo=None):
            year = ts_input.year
            month = ts_input.month
            day = ts_input.day
            hour = ts_input.hour
            minute = ts_input.minute
            second = ts_input.second
            microsecond = ts_input.microsecond
            return compute_val_for_timestamp(year, month, day, zero_if_none
                (hour), zero_if_none(minute), zero_if_none(second),
                zero_if_none(microsecond), zero_if_none(nanosecond), tz)
        return impl_datetime
    if ts_input == bodo.hiframes.datetime_date_ext.datetime_date_type:

        def impl_date(ts_input=_no_input, freq=None, tz=None, unit=None,
            year=None, month=None, day=None, hour=None, minute=None, second
            =None, microsecond=None, nanosecond=None, tzinfo=None):
            year = ts_input.year
            month = ts_input.month
            day = ts_input.day
            return compute_val_for_timestamp(year, month, day, zero_if_none
                (hour), zero_if_none(minute), zero_if_none(second),
                zero_if_none(microsecond), zero_if_none(nanosecond), tz)
        return impl_date
    if isinstance(ts_input, numba.core.types.scalars.NPDatetime):
        fgam__bry, precision = pd._libs.tslibs.conversion.precision_from_unit(
            ts_input.unit)

        def impl_date(ts_input=_no_input, freq=None, tz=None, unit=None,
            year=None, month=None, day=None, hour=None, minute=None, second
            =None, microsecond=None, nanosecond=None, tzinfo=None):
            value = np.int64(ts_input) * fgam__bry
            return convert_val_to_timestamp(value, tz)
        return impl_date


@overload_attribute(PandasTimestampType, 'dayofyear')
@overload_attribute(PandasTimestampType, 'day_of_year')
def overload_pd_dayofyear(ptt):

    def pd_dayofyear(ptt):
        return get_day_of_year(ptt.year, ptt.month, ptt.day)
    return pd_dayofyear


@overload_method(PandasTimestampType, 'weekday')
@overload_attribute(PandasTimestampType, 'dayofweek')
@overload_attribute(PandasTimestampType, 'day_of_week')
def overload_pd_dayofweek(ptt):

    def pd_dayofweek(ptt):
        return get_day_of_week(ptt.year, ptt.month, ptt.day)
    return pd_dayofweek


@overload_attribute(PandasTimestampType, 'week')
@overload_attribute(PandasTimestampType, 'weekofyear')
def overload_week_number(ptt):

    def pd_week_number(ptt):
        ynuvr__syafm, quyc__crpno, ynuvr__syafm = get_isocalendar(ptt.year,
            ptt.month, ptt.day)
        return quyc__crpno
    return pd_week_number


@overload_method(PandasTimestampType, '__hash__', no_unliteral=True)
def dt64_hash(val):
    return lambda val: hash(val.value)


@overload_attribute(PandasTimestampType, 'days_in_month')
@overload_attribute(PandasTimestampType, 'daysinmonth')
def overload_pd_daysinmonth(ptt):

    def pd_daysinmonth(ptt):
        return get_days_in_month(ptt.year, ptt.month)
    return pd_daysinmonth


@overload_attribute(PandasTimestampType, 'is_leap_year')
def overload_pd_is_leap_year(ptt):

    def pd_is_leap_year(ptt):
        return is_leap_year(ptt.year)
    return pd_is_leap_year


@overload_attribute(PandasTimestampType, 'is_month_start')
def overload_pd_is_month_start(ptt):

    def pd_is_month_start(ptt):
        return ptt.day == 1
    return pd_is_month_start


@overload_attribute(PandasTimestampType, 'is_month_end')
def overload_pd_is_month_end(ptt):

    def pd_is_month_end(ptt):
        return ptt.day == get_days_in_month(ptt.year, ptt.month)
    return pd_is_month_end


@overload_attribute(PandasTimestampType, 'is_quarter_start')
def overload_pd_is_quarter_start(ptt):

    def pd_is_quarter_start(ptt):
        return ptt.day == 1 and ptt.month % 3 == 1
    return pd_is_quarter_start


@overload_attribute(PandasTimestampType, 'is_quarter_end')
def overload_pd_is_quarter_end(ptt):

    def pd_is_quarter_end(ptt):
        return ptt.month % 3 == 0 and ptt.day == get_days_in_month(ptt.year,
            ptt.month)
    return pd_is_quarter_end


@overload_attribute(PandasTimestampType, 'is_year_start')
def overload_pd_is_year_start(ptt):

    def pd_is_year_start(ptt):
        return ptt.day == 1 and ptt.month == 1
    return pd_is_year_start


@overload_attribute(PandasTimestampType, 'is_year_end')
def overload_pd_is_year_end(ptt):

    def pd_is_year_end(ptt):
        return ptt.day == 31 and ptt.month == 12
    return pd_is_year_end


@overload_attribute(PandasTimestampType, 'quarter')
def overload_quarter(ptt):

    def quarter(ptt):
        return (ptt.month - 1) // 3 + 1
    return quarter


@overload_method(PandasTimestampType, 'date', no_unliteral=True)
def overload_pd_timestamp_date(ptt):

    def pd_timestamp_date_impl(ptt):
        return datetime.date(ptt.year, ptt.month, ptt.day)
    return pd_timestamp_date_impl


@overload_method(PandasTimestampType, 'isocalendar', no_unliteral=True)
def overload_pd_timestamp_isocalendar(ptt):

    def impl(ptt):
        year, quyc__crpno, bxz__tep = get_isocalendar(ptt.year, ptt.month,
            ptt.day)
        return year, quyc__crpno, bxz__tep
    return impl


@overload_method(PandasTimestampType, 'isoformat', no_unliteral=True)
def overload_pd_timestamp_isoformat(ts, sep=None):
    if is_overload_none(sep):

        def timestamp_isoformat_impl(ts, sep=None):
            zyfqx__ndt = str_2d(ts.hour) + ':' + str_2d(ts.minute
                ) + ':' + str_2d(ts.second)
            if ts.microsecond != 0:
                zyfqx__ndt += '.' + str_2d(ts.microsecond)
                if ts.nanosecond != 0:
                    zyfqx__ndt += str_2d(ts.nanosecond)
            res = str(ts.year) + '-' + str_2d(ts.month) + '-' + str_2d(ts.day
                ) + 'T' + zyfqx__ndt
            return res
        return timestamp_isoformat_impl
    else:

        def timestamp_isoformat_impl(ts, sep=None):
            zyfqx__ndt = str_2d(ts.hour) + ':' + str_2d(ts.minute
                ) + ':' + str_2d(ts.second)
            if ts.microsecond != 0:
                zyfqx__ndt += '.' + str_2d(ts.microsecond)
                if ts.nanosecond != 0:
                    zyfqx__ndt += str_2d(ts.nanosecond)
            res = str(ts.year) + '-' + str_2d(ts.month) + '-' + str_2d(ts.day
                ) + sep + zyfqx__ndt
            return res
    return timestamp_isoformat_impl


@overload_method(PandasTimestampType, 'normalize', no_unliteral=True)
def overload_pd_timestamp_normalize(ptt):
    tz_literal = ptt.tz

    def impl(ptt):
        return pd.Timestamp(year=ptt.year, month=ptt.month, day=ptt.day, tz
            =tz_literal)
    return impl


@overload_method(PandasTimestampType, 'day_name', no_unliteral=True)
def overload_pd_timestamp_day_name(ptt, locale=None):
    xmtpp__vihuk = dict(locale=locale)
    qxt__ibwxs = dict(locale=None)
    check_unsupported_args('Timestamp.day_name', xmtpp__vihuk, qxt__ibwxs,
        package_name='pandas', module_name='Timestamp')

    def impl(ptt, locale=None):
        umw__qme = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday')
        ynuvr__syafm, ynuvr__syafm, vrs__jze = ptt.isocalendar()
        return umw__qme[vrs__jze - 1]
    return impl


@overload_method(PandasTimestampType, 'month_name', no_unliteral=True)
def overload_pd_timestamp_month_name(ptt, locale=None):
    xmtpp__vihuk = dict(locale=locale)
    qxt__ibwxs = dict(locale=None)
    check_unsupported_args('Timestamp.month_name', xmtpp__vihuk, qxt__ibwxs,
        package_name='pandas', module_name='Timestamp')

    def impl(ptt, locale=None):
        xmpzq__tzfy = ('January', 'February', 'March', 'April', 'May',
            'June', 'July', 'August', 'September', 'October', 'November',
            'December')
        return xmpzq__tzfy[ptt.month - 1]
    return impl


@overload_method(PandasTimestampType, 'tz_convert', no_unliteral=True)
def overload_pd_timestamp_tz_convert(ptt, tz):
    if ptt.tz is None:
        raise BodoError(
            'Cannot convert tz-naive Timestamp, use tz_localize to localize')
    if is_overload_none(tz):
        return lambda ptt, tz: convert_val_to_timestamp(ptt.value)
    elif is_overload_constant_str(tz):
        return lambda ptt, tz: convert_val_to_timestamp(ptt.value, tz=tz)


@overload_method(PandasTimestampType, 'tz_localize', no_unliteral=True)
def overload_pd_timestamp_tz_localize(ptt, tz, ambiguous='raise',
    nonexistent='raise'):
    if ptt.tz is not None and not is_overload_none(tz):
        raise BodoError(
            'Cannot localize tz-aware Timestamp, use tz_convert for conversions'
            )
    xmtpp__vihuk = dict(ambiguous=ambiguous, nonexistent=nonexistent)
    plctu__cayi = dict(ambiguous='raise', nonexistent='raise')
    check_unsupported_args('Timestamp.tz_localize', xmtpp__vihuk,
        plctu__cayi, package_name='pandas', module_name='Timestamp')
    if is_overload_none(tz) and ptt.tz is None:
        return lambda ptt, tz, ambiguous='raise', nonexistent='raise': ptt
    if is_overload_none(tz):
        nqwr__xda = ptt.tz
        nwr__oqga = False
    else:
        if not is_literal_type(tz):
            raise_bodo_error(
                'Timestamp.tz_localize(): tz value must be a literal string, integer, or None'
                )
        nqwr__xda = get_literal_value(tz)
        nwr__oqga = True
    vxayc__dton = None
    yuo__nrnf = None
    qls__jaf = False
    if tz_has_transition_times(nqwr__xda):
        qls__jaf = nwr__oqga
        nvfcn__aqw = pytz.timezone(nqwr__xda)
        yuo__nrnf = np.array(nvfcn__aqw._utc_transition_times, dtype='M8[ns]'
            ).view('i8')
        vxayc__dton = np.array(nvfcn__aqw._transition_info)[:, 0]
        vxayc__dton = (pd.Series(vxayc__dton).dt.total_seconds() * 1000000000
            ).astype(np.int64).values
        ycj__zcsh = "deltas[np.searchsorted(trans, value, side='right') - 1]"
    elif isinstance(nqwr__xda, str):
        nvfcn__aqw = pytz.timezone(nqwr__xda)
        ycj__zcsh = str(np.int64(nvfcn__aqw._utcoffset.total_seconds() * 
            1000000000))
    elif isinstance(nqwr__xda, int):
        ycj__zcsh = str(nqwr__xda)
    else:
        raise_bodo_error(
            'Timestamp.tz_localize(): tz value must be a literal string, integer, or None'
            )
    if nwr__oqga:
        wms__jyhl = '-'
    else:
        wms__jyhl = '+'
    boovd__lhrsx = (
        "def impl(ptt, tz, ambiguous='raise', nonexistent='raise'):\n")
    boovd__lhrsx += f'    value =  ptt.value\n'
    boovd__lhrsx += f'    delta =  {ycj__zcsh}\n'
    boovd__lhrsx += f'    new_value = value {wms__jyhl} delta\n'
    if qls__jaf:
        boovd__lhrsx += """    end_delta = deltas[np.searchsorted(trans, new_value, side='right') - 1]
"""
        boovd__lhrsx += '    offset = delta - end_delta\n'
        boovd__lhrsx += '    new_value = new_value + offset\n'
    boovd__lhrsx += f'    return convert_val_to_timestamp(new_value, tz=tz)\n'
    uffei__vaaw = {}
    exec(boovd__lhrsx, {'np': np, 'convert_val_to_timestamp':
        convert_val_to_timestamp, 'trans': yuo__nrnf, 'deltas': vxayc__dton
        }, uffei__vaaw)
    impl = uffei__vaaw['impl']
    return impl


@numba.njit
def str_2d(a):
    res = str(a)
    if len(res) == 1:
        return '0' + res
    return res


@overload(str, no_unliteral=True)
def ts_str_overload(a):
    if a == pd_timestamp_tz_naive_type:
        return lambda a: a.isoformat(' ')


@intrinsic
def extract_year_days(typingctx, dt64_t=None):
    assert dt64_t in (types.int64, types.NPDatetime('ns'))

    def codegen(context, builder, sig, args):
        lhib__iaqh = cgutils.alloca_once(builder, lir.IntType(64))
        builder.store(args[0], lhib__iaqh)
        year = cgutils.alloca_once(builder, lir.IntType(64))
        ybf__mwvji = cgutils.alloca_once(builder, lir.IntType(64))
        ujhrc__rid = lir.FunctionType(lir.VoidType(), [lir.IntType(64).
            as_pointer(), lir.IntType(64).as_pointer(), lir.IntType(64).
            as_pointer()])
        zjjm__bkn = cgutils.get_or_insert_function(builder.module,
            ujhrc__rid, name='extract_year_days')
        builder.call(zjjm__bkn, [lhib__iaqh, year, ybf__mwvji])
        return cgutils.pack_array(builder, [builder.load(lhib__iaqh),
            builder.load(year), builder.load(ybf__mwvji)])
    return types.Tuple([types.int64, types.int64, types.int64])(dt64_t
        ), codegen


@intrinsic
def get_month_day(typingctx, year_t, days_t=None):
    assert year_t == types.int64
    assert days_t == types.int64

    def codegen(context, builder, sig, args):
        month = cgutils.alloca_once(builder, lir.IntType(64))
        day = cgutils.alloca_once(builder, lir.IntType(64))
        ujhrc__rid = lir.FunctionType(lir.VoidType(), [lir.IntType(64), lir
            .IntType(64), lir.IntType(64).as_pointer(), lir.IntType(64).
            as_pointer()])
        zjjm__bkn = cgutils.get_or_insert_function(builder.module,
            ujhrc__rid, name='get_month_day')
        builder.call(zjjm__bkn, [args[0], args[1], month, day])
        return cgutils.pack_array(builder, [builder.load(month), builder.
            load(day)])
    return types.Tuple([types.int64, types.int64])(types.int64, types.int64
        ), codegen


@register_jitable
def get_day_of_year(year, month, day):
    cqoqe__pgfix = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 
        365, 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
    udve__eael = is_leap_year(year)
    wbwr__pppy = cqoqe__pgfix[udve__eael * 13 + month - 1]
    jdhkw__emgc = wbwr__pppy + day
    return jdhkw__emgc


@register_jitable
def get_day_of_week(y, m, d):
    khgp__vrfvu = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    y -= m < 3
    day = (y + y // 4 - y // 100 + y // 400 + khgp__vrfvu[m - 1] + d) % 7
    return (day + 6) % 7


@register_jitable
def get_days_in_month(year, month):
    is_leap_year = year & 3 == 0 and (year % 100 != 0 or year % 400 == 0)
    xubrn__juw = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 29, 
        31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return xubrn__juw[12 * is_leap_year + month - 1]


@register_jitable
def is_leap_year(year):
    return year & 3 == 0 and (year % 100 != 0 or year % 400 == 0)


@numba.generated_jit(nopython=True)
def compute_val_for_timestamp(year, month, day, hour, minute, second,
    microsecond, nanosecond, tz):
    ycj__zcsh = '0'
    nqwr__xda = get_literal_value(tz)
    vxayc__dton = None
    yuo__nrnf = None
    qls__jaf = False
    if tz_has_transition_times(nqwr__xda):
        qls__jaf = True
        nvfcn__aqw = pytz.timezone(nqwr__xda)
        yuo__nrnf = np.array(nvfcn__aqw._utc_transition_times, dtype='M8[ns]'
            ).view('i8')
        vxayc__dton = np.array(nvfcn__aqw._transition_info)[:, 0]
        vxayc__dton = (pd.Series(vxayc__dton).dt.total_seconds() * 1000000000
            ).astype(np.int64).values
        ycj__zcsh = (
            "deltas[np.searchsorted(trans, original_value, side='right') - 1]")
    elif isinstance(nqwr__xda, str):
        nvfcn__aqw = pytz.timezone(nqwr__xda)
        ycj__zcsh = str(np.int64(nvfcn__aqw._utcoffset.total_seconds() * 
            1000000000))
    elif isinstance(nqwr__xda, int):
        ycj__zcsh = str(nqwr__xda)
    elif nqwr__xda is not None:
        raise_bodo_error(
            'compute_val_for_timestamp(): tz value must be a constant string, integer or None'
            )
    boovd__lhrsx = """def impl(year, month, day, hour, minute, second, microsecond, nanosecond, tz):
"""
    boovd__lhrsx += f"""  original_value = npy_datetimestruct_to_datetime(year, month, day, hour, minute, second, microsecond) + nanosecond
"""
    boovd__lhrsx += f'  value = original_value - {ycj__zcsh}\n'
    if qls__jaf:
        boovd__lhrsx += """  start_trans = np.searchsorted(trans, original_value, side='right') - 1
"""
        boovd__lhrsx += (
            "  end_trans = np.searchsorted(trans, value, side='right') - 1\n")
        boovd__lhrsx += '  offset = deltas[start_trans] - deltas[end_trans]\n'
        boovd__lhrsx += '  value = value + offset\n'
    boovd__lhrsx += '  return init_timestamp(\n'
    boovd__lhrsx += '    year=year,\n'
    boovd__lhrsx += '    month=month,\n'
    boovd__lhrsx += '    day=day,\n'
    boovd__lhrsx += '    hour=hour,\n'
    boovd__lhrsx += '    minute=minute,'
    boovd__lhrsx += '    second=second,\n'
    boovd__lhrsx += '    microsecond=microsecond,\n'
    boovd__lhrsx += '    nanosecond=nanosecond,\n'
    boovd__lhrsx += f'    value=value,\n'
    boovd__lhrsx += '    tz=tz,\n'
    boovd__lhrsx += '  )\n'
    uffei__vaaw = {}
    exec(boovd__lhrsx, {'np': np, 'pd': pd, 'init_timestamp':
        init_timestamp, 'npy_datetimestruct_to_datetime':
        npy_datetimestruct_to_datetime, 'trans': yuo__nrnf, 'deltas':
        vxayc__dton}, uffei__vaaw)
    impl = uffei__vaaw['impl']
    return impl


@numba.generated_jit(nopython=True)
def convert_val_to_timestamp(ts_input, tz=None, is_convert=True):
    yuo__nrnf = vxayc__dton = np.array([])
    ycj__zcsh = '0'
    if is_overload_constant_str(tz):
        jes__uhx = get_overload_const_str(tz)
        nvfcn__aqw = pytz.timezone(jes__uhx)
        if isinstance(nvfcn__aqw, pytz.tzinfo.DstTzInfo):
            yuo__nrnf = np.array(nvfcn__aqw._utc_transition_times, dtype=
                'M8[ns]').view('i8')
            vxayc__dton = np.array(nvfcn__aqw._transition_info)[:, 0]
            vxayc__dton = (pd.Series(vxayc__dton).dt.total_seconds() * 
                1000000000).astype(np.int64).values
            ycj__zcsh = (
                "deltas[np.searchsorted(trans, ts_input, side='right') - 1]")
        else:
            vxayc__dton = np.int64(nvfcn__aqw._utcoffset.total_seconds() * 
                1000000000)
            ycj__zcsh = 'deltas'
    elif is_overload_constant_int(tz):
        wgjpy__ylur = get_overload_const_int(tz)
        ycj__zcsh = str(wgjpy__ylur)
    elif not is_overload_none(tz):
        raise_bodo_error(
            'convert_val_to_timestamp(): tz value must be a constant string or None'
            )
    is_convert = get_overload_const_bool(is_convert)
    if is_convert:
        sjk__ujhmp = 'tz_ts_input'
        nxu__bmesy = 'ts_input'
    else:
        sjk__ujhmp = 'ts_input'
        nxu__bmesy = 'tz_ts_input'
    boovd__lhrsx = 'def impl(ts_input, tz=None, is_convert=True):\n'
    boovd__lhrsx += f'  tz_ts_input = ts_input + {ycj__zcsh}\n'
    boovd__lhrsx += (
        f'  dt, year, days = extract_year_days(integer_to_dt64({sjk__ujhmp}))\n'
        )
    boovd__lhrsx += '  month, day = get_month_day(year, days)\n'
    boovd__lhrsx += '  return init_timestamp(\n'
    boovd__lhrsx += '    year=year,\n'
    boovd__lhrsx += '    month=month,\n'
    boovd__lhrsx += '    day=day,\n'
    boovd__lhrsx += '    hour=dt // (60 * 60 * 1_000_000_000),\n'
    boovd__lhrsx += '    minute=(dt // (60 * 1_000_000_000)) % 60,\n'
    boovd__lhrsx += '    second=(dt // 1_000_000_000) % 60,\n'
    boovd__lhrsx += '    microsecond=(dt // 1000) % 1_000_000,\n'
    boovd__lhrsx += '    nanosecond=dt % 1000,\n'
    boovd__lhrsx += f'    value={nxu__bmesy},\n'
    boovd__lhrsx += '    tz=tz,\n'
    boovd__lhrsx += '  )\n'
    uffei__vaaw = {}
    exec(boovd__lhrsx, {'np': np, 'pd': pd, 'trans': yuo__nrnf, 'deltas':
        vxayc__dton, 'integer_to_dt64': integer_to_dt64,
        'extract_year_days': extract_year_days, 'get_month_day':
        get_month_day, 'init_timestamp': init_timestamp, 'zero_if_none':
        zero_if_none}, uffei__vaaw)
    impl = uffei__vaaw['impl']
    return impl


@numba.njit(no_cpython_wrapper=True)
def convert_datetime64_to_timestamp(dt64):
    lhib__iaqh, year, ybf__mwvji = extract_year_days(dt64)
    month, day = get_month_day(year, ybf__mwvji)
    return init_timestamp(year=year, month=month, day=day, hour=lhib__iaqh //
        (60 * 60 * 1000000000), minute=lhib__iaqh // (60 * 1000000000) % 60,
        second=lhib__iaqh // 1000000000 % 60, microsecond=lhib__iaqh // 
        1000 % 1000000, nanosecond=lhib__iaqh % 1000, value=dt64, tz=None)


@numba.njit(no_cpython_wrapper=True)
def convert_numpy_timedelta64_to_datetime_timedelta(dt64):
    fhimh__rfbc = (bodo.hiframes.datetime_timedelta_ext.
        cast_numpy_timedelta_to_int(dt64))
    qaek__boqaz = fhimh__rfbc // (86400 * 1000000000)
    ugeqo__fseqb = fhimh__rfbc - qaek__boqaz * 86400 * 1000000000
    wmge__dbvuv = ugeqo__fseqb // 1000000000
    yfjyg__rqgtm = ugeqo__fseqb - wmge__dbvuv * 1000000000
    ketgc__ldh = yfjyg__rqgtm // 1000
    return datetime.timedelta(qaek__boqaz, wmge__dbvuv, ketgc__ldh)


@numba.njit(no_cpython_wrapper=True)
def convert_numpy_timedelta64_to_pd_timedelta(dt64):
    fhimh__rfbc = (bodo.hiframes.datetime_timedelta_ext.
        cast_numpy_timedelta_to_int(dt64))
    return pd.Timedelta(fhimh__rfbc)


@intrinsic
def integer_to_timedelta64(typingctx, val=None):

    def codegen(context, builder, sig, args):
        return args[0]
    return types.NPTimedelta('ns')(val), codegen


@intrinsic
def integer_to_dt64(typingctx, val=None):

    def codegen(context, builder, sig, args):
        return args[0]
    return types.NPDatetime('ns')(val), codegen


@intrinsic
def dt64_to_integer(typingctx, val=None):

    def codegen(context, builder, sig, args):
        return args[0]
    return types.int64(val), codegen


@lower_cast(types.NPDatetime('ns'), types.int64)
def cast_dt64_to_integer(context, builder, fromty, toty, val):
    return val


@overload_method(types.NPDatetime, '__hash__', no_unliteral=True)
def dt64_hash(val):
    return lambda val: hash(dt64_to_integer(val))


@overload_method(types.NPTimedelta, '__hash__', no_unliteral=True)
def td64_hash(val):
    return lambda val: hash(dt64_to_integer(val))


@intrinsic
def timedelta64_to_integer(typingctx, val=None):

    def codegen(context, builder, sig, args):
        return args[0]
    return types.int64(val), codegen


@lower_cast(bodo.timedelta64ns, types.int64)
def cast_td64_to_integer(context, builder, fromty, toty, val):
    return val


@numba.njit
def parse_datetime_str(val):
    with numba.objmode(res='int64'):
        res = pd.Timestamp(val).value
    return integer_to_dt64(res)


@numba.njit
def datetime_timedelta_to_timedelta64(val):
    with numba.objmode(res='NPTimedelta("ns")'):
        res = pd.to_timedelta(val)
        res = res.to_timedelta64()
    return res


@numba.njit
def series_str_dt64_astype(data):
    with numba.objmode(res="NPDatetime('ns')[::1]"):
        res = pd.Series(data.to_numpy()).astype('datetime64[ns]').values
    return res


@numba.njit
def series_str_td64_astype(data):
    with numba.objmode(res="NPTimedelta('ns')[::1]"):
        res = data.astype('timedelta64[ns]')
    return res


@numba.njit
def datetime_datetime_to_dt64(val):
    with numba.objmode(res='NPDatetime("ns")'):
        res = np.datetime64(val).astype('datetime64[ns]')
    return res


@register_jitable
def datetime_date_arr_to_dt64_arr(arr):
    with numba.objmode(res='NPDatetime("ns")[::1]'):
        res = np.array(arr, dtype='datetime64[ns]')
    return res


types.pd_timestamp_tz_naive_type = pd_timestamp_tz_naive_type


@register_jitable
def to_datetime_scalar(a, errors='raise', dayfirst=False, yearfirst=False,
    utc=None, format=None, exact=True, unit=None, infer_datetime_format=
    False, origin='unix', cache=True):
    with numba.objmode(t='pd_timestamp_tz_naive_type'):
        t = pd.to_datetime(a, errors=errors, dayfirst=dayfirst, yearfirst=
            yearfirst, utc=utc, format=format, exact=exact, unit=unit,
            infer_datetime_format=infer_datetime_format, origin=origin,
            cache=cache)
    return t


@numba.njit
def pandas_string_array_to_datetime(arr, errors, dayfirst, yearfirst, utc,
    format, exact, unit, infer_datetime_format, origin, cache):
    with numba.objmode(result='datetime_index'):
        result = pd.to_datetime(arr, errors=errors, dayfirst=dayfirst,
            yearfirst=yearfirst, utc=utc, format=format, exact=exact, unit=
            unit, infer_datetime_format=infer_datetime_format, origin=
            origin, cache=cache)
    return result


@numba.njit
def pandas_dict_string_array_to_datetime(arr, errors, dayfirst, yearfirst,
    utc, format, exact, unit, infer_datetime_format, origin, cache):
    jocbc__bcrx = len(arr)
    love__izr = np.empty(jocbc__bcrx, 'datetime64[ns]')
    pjal__tfor = arr._indices
    wxm__fprba = pandas_string_array_to_datetime(arr._data, errors,
        dayfirst, yearfirst, utc, format, exact, unit,
        infer_datetime_format, origin, cache).values
    for jib__rmefy in range(jocbc__bcrx):
        if bodo.libs.array_kernels.isna(pjal__tfor, jib__rmefy):
            bodo.libs.array_kernels.setna(love__izr, jib__rmefy)
            continue
        love__izr[jib__rmefy] = wxm__fprba[pjal__tfor[jib__rmefy]]
    return love__izr


@overload(pd.to_datetime, inline='always', no_unliteral=True)
def overload_to_datetime(arg_a, errors='raise', dayfirst=False, yearfirst=
    False, utc=None, format=None, exact=True, unit=None,
    infer_datetime_format=False, origin='unix', cache=True):
    vnr__ufd = {'errors': errors}
    bvjgx__pgg = {'errors': 'raise'}
    check_unsupported_args('pd.to_datetime', vnr__ufd, bvjgx__pgg,
        package_name='pandas')
    if arg_a == bodo.string_type or is_overload_constant_str(arg_a
        ) or is_overload_constant_int(arg_a) or isinstance(arg_a, types.Integer
        ):

        def pd_to_datetime_impl(arg_a, errors='raise', dayfirst=False,
            yearfirst=False, utc=None, format=None, exact=True, unit=None,
            infer_datetime_format=False, origin='unix', cache=True):
            return to_datetime_scalar(arg_a, errors=errors, dayfirst=
                dayfirst, yearfirst=yearfirst, utc=utc, format=format,
                exact=exact, unit=unit, infer_datetime_format=
                infer_datetime_format, origin=origin, cache=cache)
        return pd_to_datetime_impl
    if isinstance(arg_a, bodo.hiframes.pd_series_ext.SeriesType):

        def impl_series(arg_a, errors='raise', dayfirst=False, yearfirst=
            False, utc=None, format=None, exact=True, unit=None,
            infer_datetime_format=False, origin='unix', cache=True):
            arr = bodo.hiframes.pd_series_ext.get_series_data(arg_a)
            xngl__glr = bodo.hiframes.pd_series_ext.get_series_index(arg_a)
            imfyi__dpm = bodo.hiframes.pd_series_ext.get_series_name(arg_a)
            mueg__bdrhh = bodo.utils.conversion.coerce_to_ndarray(pd.
                to_datetime(arr, errors=errors, dayfirst=dayfirst,
                yearfirst=yearfirst, utc=utc, format=format, exact=exact,
                unit=unit, infer_datetime_format=infer_datetime_format,
                origin=origin, cache=cache))
            return bodo.hiframes.pd_series_ext.init_series(mueg__bdrhh,
                xngl__glr, imfyi__dpm)
        return impl_series
    if arg_a == bodo.hiframes.datetime_date_ext.datetime_date_array_type:
        wweh__gnwcq = np.dtype('datetime64[ns]')
        iNaT = pd._libs.tslibs.iNaT

        def impl_date_arr(arg_a, errors='raise', dayfirst=False, yearfirst=
            False, utc=None, format=None, exact=True, unit=None,
            infer_datetime_format=False, origin='unix', cache=True):
            jocbc__bcrx = len(arg_a)
            love__izr = np.empty(jocbc__bcrx, wweh__gnwcq)
            for jib__rmefy in numba.parfors.parfor.internal_prange(jocbc__bcrx
                ):
                val = iNaT
                if not bodo.libs.array_kernels.isna(arg_a, jib__rmefy):
                    data = arg_a[jib__rmefy]
                    val = (bodo.hiframes.pd_timestamp_ext.
                        npy_datetimestruct_to_datetime(data.year, data.
                        month, data.day, 0, 0, 0, 0))
                love__izr[jib__rmefy
                    ] = bodo.hiframes.pd_timestamp_ext.integer_to_dt64(val)
            return bodo.hiframes.pd_index_ext.init_datetime_index(love__izr,
                None)
        return impl_date_arr
    if arg_a == types.Array(types.NPDatetime('ns'), 1, 'C'):
        return (lambda arg_a, errors='raise', dayfirst=False, yearfirst=
            False, utc=None, format=None, exact=True, unit=None,
            infer_datetime_format=False, origin='unix', cache=True: bodo.
            hiframes.pd_index_ext.init_datetime_index(arg_a, None))
    if arg_a == string_array_type:

        def impl_string_array(arg_a, errors='raise', dayfirst=False,
            yearfirst=False, utc=None, format=None, exact=True, unit=None,
            infer_datetime_format=False, origin='unix', cache=True):
            return pandas_string_array_to_datetime(arg_a, errors, dayfirst,
                yearfirst, utc, format, exact, unit, infer_datetime_format,
                origin, cache)
        return impl_string_array
    if isinstance(arg_a, types.Array) and isinstance(arg_a.dtype, types.Integer
        ):
        wweh__gnwcq = np.dtype('datetime64[ns]')

        def impl_date_arr(arg_a, errors='raise', dayfirst=False, yearfirst=
            False, utc=None, format=None, exact=True, unit=None,
            infer_datetime_format=False, origin='unix', cache=True):
            jocbc__bcrx = len(arg_a)
            love__izr = np.empty(jocbc__bcrx, wweh__gnwcq)
            for jib__rmefy in numba.parfors.parfor.internal_prange(jocbc__bcrx
                ):
                data = arg_a[jib__rmefy]
                val = to_datetime_scalar(data, errors=errors, dayfirst=
                    dayfirst, yearfirst=yearfirst, utc=utc, format=format,
                    exact=exact, unit=unit, infer_datetime_format=
                    infer_datetime_format, origin=origin, cache=cache)
                love__izr[jib__rmefy
                    ] = bodo.hiframes.pd_timestamp_ext.datetime_datetime_to_dt64(
                    val)
            return bodo.hiframes.pd_index_ext.init_datetime_index(love__izr,
                None)
        return impl_date_arr
    if isinstance(arg_a, CategoricalArrayType
        ) and arg_a.dtype.elem_type == bodo.string_type:
        wweh__gnwcq = np.dtype('datetime64[ns]')

        def impl_cat_arr(arg_a, errors='raise', dayfirst=False, yearfirst=
            False, utc=None, format=None, exact=True, unit=None,
            infer_datetime_format=False, origin='unix', cache=True):
            jocbc__bcrx = len(arg_a)
            love__izr = np.empty(jocbc__bcrx, wweh__gnwcq)
            wdpv__yqomd = (bodo.hiframes.pd_categorical_ext.
                get_categorical_arr_codes(arg_a))
            wxm__fprba = pandas_string_array_to_datetime(arg_a.dtype.
                categories.values, errors, dayfirst, yearfirst, utc, format,
                exact, unit, infer_datetime_format, origin, cache).values
            for jib__rmefy in numba.parfors.parfor.internal_prange(jocbc__bcrx
                ):
                c = wdpv__yqomd[jib__rmefy]
                if c == -1:
                    bodo.libs.array_kernels.setna(love__izr, jib__rmefy)
                    continue
                love__izr[jib__rmefy] = wxm__fprba[c]
            return bodo.hiframes.pd_index_ext.init_datetime_index(love__izr,
                None)
        return impl_cat_arr
    if arg_a == bodo.dict_str_arr_type:

        def impl_dict_str_arr(arg_a, errors='raise', dayfirst=False,
            yearfirst=False, utc=None, format=None, exact=True, unit=None,
            infer_datetime_format=False, origin='unix', cache=True):
            love__izr = pandas_dict_string_array_to_datetime(arg_a, errors,
                dayfirst, yearfirst, utc, format, exact, unit,
                infer_datetime_format, origin, cache)
            return bodo.hiframes.pd_index_ext.init_datetime_index(love__izr,
                None)
        return impl_dict_str_arr
    if isinstance(arg_a, PandasTimestampType):

        def impl_timestamp(arg_a, errors='raise', dayfirst=False, yearfirst
            =False, utc=None, format=None, exact=True, unit=None,
            infer_datetime_format=False, origin='unix', cache=True):
            return arg_a
        return impl_timestamp
    if arg_a == bodo.datetime64ns:

        def impl_np_datetime(arg_a, errors='raise', dayfirst=False,
            yearfirst=False, utc=None, format=None, exact=True, unit=None,
            infer_datetime_format=False, origin='unix', cache=True):
            return pd.Timestamp(arg_a)
        return impl_np_datetime
    if is_overload_none(arg_a):

        def impl_np_datetime(arg_a, errors='raise', dayfirst=False,
            yearfirst=False, utc=None, format=None, exact=True, unit=None,
            infer_datetime_format=False, origin='unix', cache=True):
            return None
        return impl_np_datetime
    raise_bodo_error(f'pd.to_datetime(): cannot convert date type {arg_a}')


@overload(pd.to_timedelta, inline='always', no_unliteral=True)
def overload_to_timedelta(arg_a, unit='ns', errors='raise'):
    if not is_overload_constant_str(unit):
        raise BodoError(
            'pandas.to_timedelta(): unit should be a constant string')
    unit = pd._libs.tslibs.timedeltas.parse_timedelta_unit(
        get_overload_const_str(unit))
    if isinstance(arg_a, bodo.hiframes.pd_series_ext.SeriesType):

        def impl_series(arg_a, unit='ns', errors='raise'):
            arr = bodo.hiframes.pd_series_ext.get_series_data(arg_a)
            xngl__glr = bodo.hiframes.pd_series_ext.get_series_index(arg_a)
            imfyi__dpm = bodo.hiframes.pd_series_ext.get_series_name(arg_a)
            mueg__bdrhh = bodo.utils.conversion.coerce_to_ndarray(pd.
                to_timedelta(arr, unit, errors))
            return bodo.hiframes.pd_series_ext.init_series(mueg__bdrhh,
                xngl__glr, imfyi__dpm)
        return impl_series
    if is_overload_constant_str(arg_a) or arg_a in (pd_timedelta_type,
        datetime_timedelta_type, bodo.string_type):

        def impl_string(arg_a, unit='ns', errors='raise'):
            return pd.Timedelta(arg_a)
        return impl_string
    if isinstance(arg_a, types.Float):
        m, hlldf__iky = pd._libs.tslibs.conversion.precision_from_unit(unit)

        def impl_float_scalar(arg_a, unit='ns', errors='raise'):
            val = float_to_timedelta_val(arg_a, hlldf__iky, m)
            return pd.Timedelta(val)
        return impl_float_scalar
    if isinstance(arg_a, types.Integer):
        m, ynuvr__syafm = pd._libs.tslibs.conversion.precision_from_unit(unit)

        def impl_integer_scalar(arg_a, unit='ns', errors='raise'):
            return pd.Timedelta(arg_a * m)
        return impl_integer_scalar
    if is_iterable_type(arg_a) and not isinstance(arg_a, types.BaseTuple):
        m, hlldf__iky = pd._libs.tslibs.conversion.precision_from_unit(unit)
        cfg__wjl = np.dtype('timedelta64[ns]')
        if isinstance(arg_a.dtype, types.Float):

            def impl_float(arg_a, unit='ns', errors='raise'):
                jocbc__bcrx = len(arg_a)
                love__izr = np.empty(jocbc__bcrx, cfg__wjl)
                for jib__rmefy in numba.parfors.parfor.internal_prange(
                    jocbc__bcrx):
                    val = iNaT
                    if not bodo.libs.array_kernels.isna(arg_a, jib__rmefy):
                        val = float_to_timedelta_val(arg_a[jib__rmefy],
                            hlldf__iky, m)
                    love__izr[jib__rmefy
                        ] = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                        val)
                return bodo.hiframes.pd_index_ext.init_timedelta_index(
                    love__izr, None)
            return impl_float
        if isinstance(arg_a.dtype, types.Integer):

            def impl_int(arg_a, unit='ns', errors='raise'):
                jocbc__bcrx = len(arg_a)
                love__izr = np.empty(jocbc__bcrx, cfg__wjl)
                for jib__rmefy in numba.parfors.parfor.internal_prange(
                    jocbc__bcrx):
                    val = iNaT
                    if not bodo.libs.array_kernels.isna(arg_a, jib__rmefy):
                        val = arg_a[jib__rmefy] * m
                    love__izr[jib__rmefy
                        ] = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                        val)
                return bodo.hiframes.pd_index_ext.init_timedelta_index(
                    love__izr, None)
            return impl_int
        if arg_a.dtype == bodo.timedelta64ns:

            def impl_td64(arg_a, unit='ns', errors='raise'):
                arr = bodo.utils.conversion.coerce_to_ndarray(arg_a)
                return bodo.hiframes.pd_index_ext.init_timedelta_index(arr,
                    None)
            return impl_td64
        if arg_a.dtype == bodo.string_type or isinstance(arg_a.dtype, types
            .UnicodeCharSeq):

            def impl_str(arg_a, unit='ns', errors='raise'):
                return pandas_string_array_to_timedelta(arg_a, unit, errors)
            return impl_str
        if arg_a.dtype == datetime_timedelta_type:

            def impl_datetime_timedelta(arg_a, unit='ns', errors='raise'):
                jocbc__bcrx = len(arg_a)
                love__izr = np.empty(jocbc__bcrx, cfg__wjl)
                for jib__rmefy in numba.parfors.parfor.internal_prange(
                    jocbc__bcrx):
                    val = iNaT
                    if not bodo.libs.array_kernels.isna(arg_a, jib__rmefy):
                        zqxx__hwvq = arg_a[jib__rmefy]
                        val = (zqxx__hwvq.microseconds + 1000 * 1000 * (
                            zqxx__hwvq.seconds + 24 * 60 * 60 * zqxx__hwvq.
                            days)) * 1000
                    love__izr[jib__rmefy
                        ] = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                        val)
                return bodo.hiframes.pd_index_ext.init_timedelta_index(
                    love__izr, None)
            return impl_datetime_timedelta
    if is_overload_none(arg_a):
        return lambda arg_a, unit='ns', errors='raise': None
    raise_bodo_error(
        f'pd.to_timedelta(): cannot convert date type {arg_a.dtype}')


@register_jitable
def float_to_timedelta_val(data, precision, multiplier):
    nqzox__hmh = np.int64(data)
    nwijm__zhmfa = data - nqzox__hmh
    if precision:
        nwijm__zhmfa = np.round(nwijm__zhmfa, precision)
    return nqzox__hmh * multiplier + np.int64(nwijm__zhmfa * multiplier)


@numba.njit
def pandas_string_array_to_timedelta(arg_a, unit='ns', errors='raise'):
    with numba.objmode(result='timedelta_index'):
        result = pd.to_timedelta(arg_a, errors=errors)
    return result


def create_timestamp_cmp_op_overload(op):

    def overload_date_timestamp_cmp(lhs, rhs):
        if isinstance(lhs, PandasTimestampType
            ) and rhs == bodo.hiframes.datetime_date_ext.datetime_date_type:
            tz_literal = lhs.tz
            return lambda lhs, rhs: op(lhs, pd.Timestamp(rhs, tz=tz_literal))
        if (lhs == bodo.hiframes.datetime_date_ext.datetime_date_type and
            isinstance(rhs, PandasTimestampType)):
            tz_literal = rhs.tz
            return lambda lhs, rhs: op(pd.Timestamp(lhs, tz=tz_literal), rhs)
        if isinstance(lhs, PandasTimestampType) and isinstance(rhs,
            PandasTimestampType):
            if lhs.tz != rhs.tz:
                raise BodoError(
                    f'{numba.core.utils.OPERATORS_TO_BUILTINS[op]} with two Timestamps requires both Timestamps share the same timezone. '
                     +
                    f'Argument 0 has timezone {lhs.tz} and argument 1 has timezone {rhs.tz}. '
                     +
                    'To compare these values please convert to timezone naive with ts.tz_convert(None).'
                    )
            return lambda lhs, rhs: op(lhs.value, rhs.value)
        if lhs == pd_timestamp_tz_naive_type and rhs == bodo.datetime64ns:
            return lambda lhs, rhs: op(bodo.hiframes.pd_timestamp_ext.
                integer_to_dt64(lhs.value), rhs)
        if lhs == bodo.datetime64ns and rhs == pd_timestamp_tz_naive_type:
            return lambda lhs, rhs: op(lhs, bodo.hiframes.pd_timestamp_ext.
                integer_to_dt64(rhs.value))
    return overload_date_timestamp_cmp


@overload_method(PandasTimestampType, 'toordinal', no_unliteral=True)
def toordinal(date):

    def impl(date):
        return _ymd2ord(date.year, date.month, date.day)
    return impl


def overload_freq_methods(method):

    def freq_overload(td, freq, ambiguous='raise', nonexistent='raise'):
        xmtpp__vihuk = dict(ambiguous=ambiguous, nonexistent=nonexistent)
        tizp__ruab = dict(ambiguous='raise', nonexistent='raise')
        check_unsupported_args(f'Timestamp.{method}', xmtpp__vihuk,
            tizp__ruab, package_name='pandas', module_name='Timestamp')
        zxokn__pfh = ["freq == 'D'", "freq == 'H'",
            "freq == 'min' or freq == 'T'", "freq == 'S'",
            "freq == 'ms' or freq == 'L'", "freq == 'U' or freq == 'us'",
            "freq == 'N'"]
        ukh__jodo = [24 * 60 * 60 * 1000000 * 1000, 60 * 60 * 1000000 * 
            1000, 60 * 1000000 * 1000, 1000000 * 1000, 1000 * 1000, 1000, 1]
        vxayc__dton = None
        yuo__nrnf = None
        tz_literal = None
        boovd__lhrsx = (
            "def impl(td, freq, ambiguous='raise', nonexistent='raise'):\n")
        for jib__rmefy, zxfgk__jydn in enumerate(zxokn__pfh):
            uoxa__vaoj = 'if' if jib__rmefy == 0 else 'elif'
            boovd__lhrsx += '    {} {}:\n'.format(uoxa__vaoj, zxfgk__jydn)
            boovd__lhrsx += '        unit_value = {}\n'.format(ukh__jodo[
                jib__rmefy])
        boovd__lhrsx += '    else:\n'
        boovd__lhrsx += (
            "        raise ValueError('Incorrect Frequency specification')\n")
        if td == pd_timedelta_type:
            boovd__lhrsx += (
                """    return pd.Timedelta(unit_value * np.int64(np.{}(td.value / unit_value)))
"""
                .format(method))
        else:
            assert isinstance(td, PandasTimestampType
                ), 'Value must be a timestamp'
            boovd__lhrsx += f'    value = td.value\n'
            tz_literal = td.tz
            if tz_literal is not None:
                ycj__zcsh = '0'
                zmf__hrlao = False
                if tz_has_transition_times(tz_literal):
                    zmf__hrlao = True
                    nvfcn__aqw = pytz.timezone(tz_literal)
                    yuo__nrnf = np.array(nvfcn__aqw._utc_transition_times,
                        dtype='M8[ns]').view('i8')
                    vxayc__dton = np.array(nvfcn__aqw._transition_info)[:, 0]
                    vxayc__dton = (pd.Series(vxayc__dton).dt.total_seconds(
                        ) * 1000000000).astype(np.int64).values
                    ycj__zcsh = (
                        "deltas[np.searchsorted(trans, value, side='right') - 1]"
                        )
                elif isinstance(tz_literal, str):
                    nvfcn__aqw = pytz.timezone(tz_literal)
                    ycj__zcsh = str(np.int64(nvfcn__aqw._utcoffset.
                        total_seconds() * 1000000000))
                elif isinstance(tz_literal, int):
                    ycj__zcsh = str(tz_literal)
                boovd__lhrsx += f'    delta = {ycj__zcsh}\n'
                boovd__lhrsx += f'    value = value + delta\n'
            if method == 'ceil':
                boovd__lhrsx += (
                    '    value = value + np.remainder(-value, unit_value)\n')
            if method == 'floor':
                boovd__lhrsx += (
                    '    value = value - np.remainder(value, unit_value)\n')
            if method == 'round':
                boovd__lhrsx += '    if unit_value == 1:\n'
                boovd__lhrsx += '        value = value\n'
                boovd__lhrsx += '    else:\n'
                boovd__lhrsx += (
                    '        quotient, remainder = np.divmod(value, unit_value)\n'
                    )
                boovd__lhrsx += """        mask = np.logical_or(remainder > (unit_value // 2), np.logical_and(remainder == (unit_value // 2), quotient % 2))
"""
                boovd__lhrsx += '        if mask:\n'
                boovd__lhrsx += '            quotient = quotient + 1\n'
                boovd__lhrsx += '        value = quotient * unit_value\n'
            if tz_literal is not None:
                if zmf__hrlao:
                    boovd__lhrsx += f'    original_value = value\n'
                    boovd__lhrsx += """    start_trans = deltas[np.searchsorted(trans, original_value, side='right') - 1]
"""
                    boovd__lhrsx += '    value = value - start_trans\n'
                    boovd__lhrsx += """    end_trans = deltas[np.searchsorted(trans, value, side='right') - 1]
"""
                    boovd__lhrsx += '    offset = start_trans - end_trans\n'
                    boovd__lhrsx += '    value = value + offset\n'
                else:
                    boovd__lhrsx += f'    value = value - delta\n'
            boovd__lhrsx += '    return pd.Timestamp(value, tz=tz_literal)\n'
        uffei__vaaw = {}
        exec(boovd__lhrsx, {'np': np, 'pd': pd, 'deltas': vxayc__dton,
            'trans': yuo__nrnf, 'tz_literal': tz_literal}, uffei__vaaw)
        impl = uffei__vaaw['impl']
        return impl
    return freq_overload


def _install_freq_methods():
    fty__upd = ['ceil', 'floor', 'round']
    for method in fty__upd:
        vauyj__vze = overload_freq_methods(method)
        overload_method(PDTimeDeltaType, method, no_unliteral=True)(vauyj__vze)
        overload_method(PandasTimestampType, method, no_unliteral=True)(
            vauyj__vze)


_install_freq_methods()


@register_jitable
def compute_pd_timestamp(totmicrosec, nanosecond):
    microsecond = totmicrosec % 1000000
    zrjz__drix = totmicrosec // 1000000
    second = zrjz__drix % 60
    jsno__ggiu = zrjz__drix // 60
    minute = jsno__ggiu % 60
    tta__wegy = jsno__ggiu // 60
    hour = tta__wegy % 24
    tms__wmh = tta__wegy // 24
    year, month, day = _ord2ymd(tms__wmh)
    value = npy_datetimestruct_to_datetime(year, month, day, hour, minute,
        second, microsecond)
    value += zero_if_none(nanosecond)
    return init_timestamp(year, month, day, hour, minute, second,
        microsecond, nanosecond, value, None)


def overload_sub_operator_timestamp(lhs, rhs):
    if isinstance(lhs, PandasTimestampType) and rhs == datetime_timedelta_type:
        tz_literal = lhs.tz

        def impl(lhs, rhs):
            kdvr__gfelq = bodo.hiframes.datetime_timedelta_ext._to_nanoseconds(
                rhs)
            return pd.Timestamp(lhs.value - kdvr__gfelq, tz=tz_literal)
        return impl
    if lhs == pd_timestamp_tz_naive_type and rhs == pd_timestamp_tz_naive_type:

        def impl_timestamp(lhs, rhs):
            return convert_numpy_timedelta64_to_pd_timedelta(lhs.value -
                rhs.value)
        return impl_timestamp
    if isinstance(lhs, PandasTimestampType) and rhs == pd_timedelta_type:

        def impl(lhs, rhs):
            return lhs + -rhs
        return impl


def overload_add_operator_timestamp(lhs, rhs):
    if isinstance(lhs, PandasTimestampType) and rhs == datetime_timedelta_type:
        tz_literal = lhs.tz

        def impl(lhs, rhs):
            kdvr__gfelq = bodo.hiframes.datetime_timedelta_ext._to_nanoseconds(
                rhs)
            return pd.Timestamp(lhs.value + kdvr__gfelq, tz=tz_literal)
        return impl
    if isinstance(lhs, PandasTimestampType) and rhs == pd_timedelta_type:
        tz_literal = lhs.tz

        def impl(lhs, rhs):
            return pd.Timestamp(lhs.value + rhs.value, tz=tz_literal)
        return impl
    if lhs == pd_timedelta_type and isinstance(rhs, PandasTimestampType
        ) or lhs == datetime_timedelta_type and isinstance(rhs,
        PandasTimestampType):

        def impl(lhs, rhs):
            return rhs + lhs
        return impl


@overload(min, no_unliteral=True)
def timestamp_min(lhs, rhs):
    check_tz_aware_unsupported(lhs, f'Timestamp.min()')
    check_tz_aware_unsupported(rhs, f'Timestamp.min()')
    if lhs == pd_timestamp_tz_naive_type and rhs == pd_timestamp_tz_naive_type:

        def impl(lhs, rhs):
            return lhs if lhs < rhs else rhs
        return impl


@overload(max, no_unliteral=True)
def timestamp_max(lhs, rhs):
    check_tz_aware_unsupported(lhs, f'Timestamp.max()')
    check_tz_aware_unsupported(rhs, f'Timestamp.max()')
    if lhs == pd_timestamp_tz_naive_type and rhs == pd_timestamp_tz_naive_type:

        def impl(lhs, rhs):
            return lhs if lhs > rhs else rhs
        return impl


@overload_method(DatetimeDateType, 'strftime')
@overload_method(PandasTimestampType, 'strftime')
def strftime(ts, format):
    if isinstance(ts, DatetimeDateType):
        rcao__ggt = 'datetime.date'
    else:
        rcao__ggt = 'pandas.Timestamp'
    if types.unliteral(format) != types.unicode_type:
        raise BodoError(
            f"{rcao__ggt}.strftime(): 'strftime' argument must be a string")

    def impl(ts, format):
        with numba.objmode(res='unicode_type'):
            res = ts.strftime(format)
        return res
    return impl


@overload_method(PandasTimestampType, 'to_datetime64')
def to_datetime64(ts):

    def impl(ts):
        return integer_to_dt64(ts.value)
    return impl


def now_impl(tz=None):
    pass


@overload(now_impl, no_unilteral=True)
def now_impl_overload(tz=None):
    if is_overload_none(tz):
        caln__tqwwg = PandasTimestampType(None)
    elif is_overload_constant_str(tz):
        caln__tqwwg = PandasTimestampType(get_overload_const_str(tz))
    elif is_overload_constant_int(tz):
        caln__tqwwg = PandasTimestampType(get_overload_const_int(tz))
    else:
        raise_bodo_error(
            'pandas.Timestamp.now(): tz argument must be a constant string or integer literal if provided'
            )

    def impl(tz=None):
        with numba.objmode(d=caln__tqwwg):
            d = pd.Timestamp.now(tz)
        return d
    return impl


class CompDT64(ConcreteTemplate):
    cases = [signature(types.boolean, types.NPDatetime('ns'), types.
        NPDatetime('ns'))]


@infer_global(operator.lt)
class CmpOpLt(CompDT64):
    key = operator.lt


@infer_global(operator.le)
class CmpOpLe(CompDT64):
    key = operator.le


@infer_global(operator.gt)
class CmpOpGt(CompDT64):
    key = operator.gt


@infer_global(operator.ge)
class CmpOpGe(CompDT64):
    key = operator.ge


@infer_global(operator.eq)
class CmpOpEq(CompDT64):
    key = operator.eq


@infer_global(operator.ne)
class CmpOpNe(CompDT64):
    key = operator.ne


@typeof_impl.register(calendar._localized_month)
def typeof_python_calendar(val, c):
    return types.Tuple([types.StringLiteral(rnv__fsj) for rnv__fsj in val])


@overload(str)
def overload_datetime64_str(val):
    if val == bodo.datetime64ns:

        def impl(val):
            return (bodo.hiframes.pd_timestamp_ext.
                convert_datetime64_to_timestamp(val).isoformat('T'))
        return impl


timestamp_unsupported_attrs = ['asm8', 'components', 'freqstr', 'tz',
    'fold', 'tzinfo', 'freq']
timestamp_unsupported_methods = ['astimezone', 'ctime', 'dst', 'isoweekday',
    'replace', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz',
    'to_julian_date', 'to_numpy', 'to_period', 'to_pydatetime', 'tzname',
    'utcoffset', 'utctimetuple']


def _install_pd_timestamp_unsupported():
    from bodo.utils.typing import create_unsupported_overload
    for aib__zld in timestamp_unsupported_attrs:
        rum__gkonl = 'pandas.Timestamp.' + aib__zld
        overload_attribute(PandasTimestampType, aib__zld)(
            create_unsupported_overload(rum__gkonl))
    for owjxk__dcmrz in timestamp_unsupported_methods:
        rum__gkonl = 'pandas.Timestamp.' + owjxk__dcmrz
        overload_method(PandasTimestampType, owjxk__dcmrz)(
            create_unsupported_overload(rum__gkonl + '()'))


_install_pd_timestamp_unsupported()


@lower_builtin(numba.core.types.functions.NumberClass,
    pd_timestamp_tz_naive_type, types.StringLiteral)
def datetime64_constructor(context, builder, sig, args):

    def datetime64_constructor_impl(a, b):
        return integer_to_dt64(a.value)
    return context.compile_internal(builder, datetime64_constructor_impl,
        sig, args)
