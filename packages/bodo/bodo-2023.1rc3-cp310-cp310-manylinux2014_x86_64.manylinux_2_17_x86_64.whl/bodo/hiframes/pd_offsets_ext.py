"""
Implement support for the various classes in pd.tseries.offsets.
"""
import operator
import llvmlite.binding as ll
import numpy as np
import pandas as pd
import pytz
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.imputils import lower_constant
from numba.extending import NativeValue, box, intrinsic, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_jitable, register_model, typeof_impl, unbox
from bodo.hiframes.datetime_date_ext import datetime_date_type
from bodo.hiframes.datetime_datetime_ext import datetime_datetime_type
from bodo.hiframes.pd_timestamp_ext import PandasTimestampType, get_days_in_month, pd_timestamp_tz_naive_type, tz_has_transition_times
from bodo.libs import hdatetime_ext
from bodo.utils.typing import BodoError, create_unsupported_overload, is_overload_none
ll.add_symbol('box_date_offset', hdatetime_ext.box_date_offset)
ll.add_symbol('unbox_date_offset', hdatetime_ext.unbox_date_offset)


class MonthBeginType(types.Type):

    def __init__(self):
        super(MonthBeginType, self).__init__(name='MonthBeginType()')


month_begin_type = MonthBeginType()


@typeof_impl.register(pd.tseries.offsets.MonthBegin)
def typeof_month_begin(val, c):
    return month_begin_type


@register_model(MonthBeginType)
class MonthBeginModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        obruf__vkgii = [('n', types.int64), ('normalize', types.boolean)]
        super(MonthBeginModel, self).__init__(dmm, fe_type, obruf__vkgii)


@box(MonthBeginType)
def box_month_begin(typ, val, c):
    shgp__gkwy = cgutils.create_struct_proxy(typ)(c.context, c.builder,
        value=val)
    ryd__gjvy = c.pyapi.long_from_longlong(shgp__gkwy.n)
    bvmt__sum = c.pyapi.from_native_value(types.boolean, shgp__gkwy.
        normalize, c.env_manager)
    hfgm__ayfap = c.pyapi.unserialize(c.pyapi.serialize_object(pd.tseries.
        offsets.MonthBegin))
    mlz__lgfez = c.pyapi.call_function_objargs(hfgm__ayfap, (ryd__gjvy,
        bvmt__sum))
    c.pyapi.decref(ryd__gjvy)
    c.pyapi.decref(bvmt__sum)
    c.pyapi.decref(hfgm__ayfap)
    return mlz__lgfez


@unbox(MonthBeginType)
def unbox_month_begin(typ, val, c):
    ryd__gjvy = c.pyapi.object_getattr_string(val, 'n')
    bvmt__sum = c.pyapi.object_getattr_string(val, 'normalize')
    n = c.pyapi.long_as_longlong(ryd__gjvy)
    normalize = c.pyapi.to_native_value(types.bool_, bvmt__sum).value
    shgp__gkwy = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    shgp__gkwy.n = n
    shgp__gkwy.normalize = normalize
    c.pyapi.decref(ryd__gjvy)
    c.pyapi.decref(bvmt__sum)
    vhigb__juk = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(shgp__gkwy._getvalue(), is_error=vhigb__juk)


@overload(pd.tseries.offsets.MonthBegin, no_unliteral=True)
def MonthBegin(n=1, normalize=False):

    def impl(n=1, normalize=False):
        return init_month_begin(n, normalize)
    return impl


@intrinsic
def init_month_begin(typingctx, n, normalize):

    def codegen(context, builder, signature, args):
        typ = signature.return_type
        shgp__gkwy = cgutils.create_struct_proxy(typ)(context, builder)
        shgp__gkwy.n = args[0]
        shgp__gkwy.normalize = args[1]
        return shgp__gkwy._getvalue()
    return MonthBeginType()(n, normalize), codegen


make_attribute_wrapper(MonthBeginType, 'n', 'n')
make_attribute_wrapper(MonthBeginType, 'normalize', 'normalize')


@register_jitable
def calculate_month_begin_date(year, month, day, n):
    if n <= 0:
        if day > 1:
            n += 1
    month = month + n
    month -= 1
    year += month // 12
    month = month % 12 + 1
    day = 1
    return year, month, day


def overload_add_operator_month_begin_offset_type(lhs, rhs):
    if lhs == month_begin_type and rhs == datetime_datetime_type:

        def impl(lhs, rhs):
            year, month, day = calculate_month_begin_date(rhs.year, rhs.
                month, rhs.day, lhs.n)
            if lhs.normalize:
                return pd.Timestamp(year=year, month=month, day=day)
            else:
                return pd.Timestamp(year=year, month=month, day=day, hour=
                    rhs.hour, minute=rhs.minute, second=rhs.second,
                    microsecond=rhs.microsecond)
        return impl
    if lhs == month_begin_type and isinstance(rhs, PandasTimestampType):
        mnrr__vuzo = rhs.tz

        def impl(lhs, rhs):
            year, month, day = calculate_month_begin_date(rhs.year, rhs.
                month, rhs.day, lhs.n)
            if lhs.normalize:
                return pd.Timestamp(year=year, month=month, day=day, tz=
                    mnrr__vuzo)
            else:
                return pd.Timestamp(year=year, month=month, day=day, hour=
                    rhs.hour, minute=rhs.minute, second=rhs.second,
                    microsecond=rhs.microsecond, nanosecond=rhs.nanosecond,
                    tz=mnrr__vuzo)
        return impl
    if lhs == month_begin_type and rhs == datetime_date_type:

        def impl(lhs, rhs):
            year, month, day = calculate_month_begin_date(rhs.year, rhs.
                month, rhs.day, lhs.n)
            return pd.Timestamp(year=year, month=month, day=day)
        return impl
    if (isinstance(lhs, PandasTimestampType) or lhs in [
        datetime_datetime_type, datetime_date_type]
        ) and rhs == month_begin_type:

        def impl(lhs, rhs):
            return rhs + lhs
        return impl
    raise BodoError(
        f'add operator not supported for data types {lhs} and {rhs}.')


class MonthEndType(types.Type):

    def __init__(self):
        super(MonthEndType, self).__init__(name='MonthEndType()')


month_end_type = MonthEndType()


@typeof_impl.register(pd.tseries.offsets.MonthEnd)
def typeof_month_end(val, c):
    return month_end_type


@register_model(MonthEndType)
class MonthEndModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        obruf__vkgii = [('n', types.int64), ('normalize', types.boolean)]
        super(MonthEndModel, self).__init__(dmm, fe_type, obruf__vkgii)


@box(MonthEndType)
def box_month_end(typ, val, c):
    uub__uuhpo = cgutils.create_struct_proxy(typ)(c.context, c.builder,
        value=val)
    ryd__gjvy = c.pyapi.long_from_longlong(uub__uuhpo.n)
    bvmt__sum = c.pyapi.from_native_value(types.boolean, uub__uuhpo.
        normalize, c.env_manager)
    wqew__inzdb = c.pyapi.unserialize(c.pyapi.serialize_object(pd.tseries.
        offsets.MonthEnd))
    mlz__lgfez = c.pyapi.call_function_objargs(wqew__inzdb, (ryd__gjvy,
        bvmt__sum))
    c.pyapi.decref(ryd__gjvy)
    c.pyapi.decref(bvmt__sum)
    c.pyapi.decref(wqew__inzdb)
    return mlz__lgfez


@unbox(MonthEndType)
def unbox_month_end(typ, val, c):
    ryd__gjvy = c.pyapi.object_getattr_string(val, 'n')
    bvmt__sum = c.pyapi.object_getattr_string(val, 'normalize')
    n = c.pyapi.long_as_longlong(ryd__gjvy)
    normalize = c.pyapi.to_native_value(types.bool_, bvmt__sum).value
    uub__uuhpo = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    uub__uuhpo.n = n
    uub__uuhpo.normalize = normalize
    c.pyapi.decref(ryd__gjvy)
    c.pyapi.decref(bvmt__sum)
    vhigb__juk = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(uub__uuhpo._getvalue(), is_error=vhigb__juk)


@overload(pd.tseries.offsets.MonthEnd, no_unliteral=True)
def MonthEnd(n=1, normalize=False):

    def impl(n=1, normalize=False):
        return init_month_end(n, normalize)
    return impl


@intrinsic
def init_month_end(typingctx, n, normalize):

    def codegen(context, builder, signature, args):
        typ = signature.return_type
        uub__uuhpo = cgutils.create_struct_proxy(typ)(context, builder)
        uub__uuhpo.n = args[0]
        uub__uuhpo.normalize = args[1]
        return uub__uuhpo._getvalue()
    return MonthEndType()(n, normalize), codegen


make_attribute_wrapper(MonthEndType, 'n', 'n')
make_attribute_wrapper(MonthEndType, 'normalize', 'normalize')


@lower_constant(MonthBeginType)
@lower_constant(MonthEndType)
def lower_constant_month_end(context, builder, ty, pyval):
    n = context.get_constant(types.int64, pyval.n)
    normalize = context.get_constant(types.boolean, pyval.normalize)
    return lir.Constant.literal_struct([n, normalize])


@register_jitable
def calculate_month_end_date(year, month, day, n):
    if n > 0:
        uub__uuhpo = get_days_in_month(year, month)
        if uub__uuhpo > day:
            n -= 1
    month = month + n
    month -= 1
    year += month // 12
    month = month % 12 + 1
    day = get_days_in_month(year, month)
    return year, month, day


def overload_add_operator_month_end_offset_type(lhs, rhs):
    if lhs == month_end_type and rhs == datetime_datetime_type:

        def impl(lhs, rhs):
            year, month, day = calculate_month_end_date(rhs.year, rhs.month,
                rhs.day, lhs.n)
            if lhs.normalize:
                return pd.Timestamp(year=year, month=month, day=day)
            else:
                return pd.Timestamp(year=year, month=month, day=day, hour=
                    rhs.hour, minute=rhs.minute, second=rhs.second,
                    microsecond=rhs.microsecond)
        return impl
    if lhs == month_end_type and isinstance(rhs, PandasTimestampType):
        mnrr__vuzo = rhs.tz

        def impl(lhs, rhs):
            year, month, day = calculate_month_end_date(rhs.year, rhs.month,
                rhs.day, lhs.n)
            if lhs.normalize:
                return pd.Timestamp(year=year, month=month, day=day, tz=
                    mnrr__vuzo)
            else:
                return pd.Timestamp(year=year, month=month, day=day, hour=
                    rhs.hour, minute=rhs.minute, second=rhs.second,
                    microsecond=rhs.microsecond, nanosecond=rhs.nanosecond,
                    tz=mnrr__vuzo)
        return impl
    if lhs == month_end_type and rhs == datetime_date_type:

        def impl(lhs, rhs):
            year, month, day = calculate_month_end_date(rhs.year, rhs.month,
                rhs.day, lhs.n)
            return pd.Timestamp(year=year, month=month, day=day)
        return impl
    if (isinstance(lhs, PandasTimestampType) or lhs in [
        datetime_datetime_type, datetime_date_type]) and rhs == month_end_type:

        def impl(lhs, rhs):
            return rhs + lhs
        return impl
    raise BodoError(
        f'add operator not supported for data types {lhs} and {rhs}.')


def overload_mul_date_offset_types(lhs, rhs):
    if lhs == month_begin_type:

        def impl(lhs, rhs):
            return pd.tseries.offsets.MonthBegin(lhs.n * rhs, lhs.normalize)
    if lhs == month_end_type:

        def impl(lhs, rhs):
            return pd.tseries.offsets.MonthEnd(lhs.n * rhs, lhs.normalize)
    if lhs == week_type:

        def impl(lhs, rhs):
            return pd.tseries.offsets.Week(lhs.n * rhs, lhs.normalize, lhs.
                weekday)
    if lhs == date_offset_type:

        def impl(lhs, rhs):
            n = lhs.n * rhs
            normalize = lhs.normalize
            if lhs._has_kws:
                years = lhs._years
                months = lhs._months
                weeks = lhs._weeks
                days = lhs._days
                hours = lhs._hours
                minutes = lhs._minutes
                seconds = lhs._seconds
                microseconds = lhs._microseconds
                year = lhs._year
                month = lhs._month
                day = lhs._day
                weekday = lhs._weekday
                hour = lhs._hour
                minute = lhs._minute
                second = lhs._second
                microsecond = lhs._microsecond
                nanoseconds = lhs._nanoseconds
                nanosecond = lhs._nanosecond
                return pd.tseries.offsets.DateOffset(n, normalize, years,
                    months, weeks, days, hours, minutes, seconds,
                    microseconds, nanoseconds, year, month, day, weekday,
                    hour, minute, second, microsecond, nanosecond)
            else:
                return pd.tseries.offsets.DateOffset(n, normalize)
    if rhs in [week_type, month_end_type, month_begin_type, date_offset_type]:

        def impl(lhs, rhs):
            return rhs * lhs
        return impl
    return impl


class DateOffsetType(types.Type):

    def __init__(self):
        super(DateOffsetType, self).__init__(name='DateOffsetType()')


date_offset_type = DateOffsetType()
date_offset_fields = ['years', 'months', 'weeks', 'days', 'hours',
    'minutes', 'seconds', 'microseconds', 'nanoseconds', 'year', 'month',
    'day', 'weekday', 'hour', 'minute', 'second', 'microsecond', 'nanosecond']


@typeof_impl.register(pd.tseries.offsets.DateOffset)
def type_of_date_offset(val, c):
    return date_offset_type


@register_model(DateOffsetType)
class DateOffsetModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        obruf__vkgii = [('n', types.int64), ('normalize', types.boolean), (
            'years', types.int64), ('months', types.int64), ('weeks', types
            .int64), ('days', types.int64), ('hours', types.int64), (
            'minutes', types.int64), ('seconds', types.int64), (
            'microseconds', types.int64), ('nanoseconds', types.int64), (
            'year', types.int64), ('month', types.int64), ('day', types.
            int64), ('weekday', types.int64), ('hour', types.int64), (
            'minute', types.int64), ('second', types.int64), ('microsecond',
            types.int64), ('nanosecond', types.int64), ('has_kws', types.
            boolean)]
        super(DateOffsetModel, self).__init__(dmm, fe_type, obruf__vkgii)


@box(DateOffsetType)
def box_date_offset(typ, val, c):
    civ__qxhe = cgutils.create_struct_proxy(typ)(c.context, c.builder,
        value=val)
    eim__rbfo = c.builder.alloca(lir.IntType(64), size=lir.Constant(lir.
        IntType(64), 18))
    for vvuv__eby, mmhry__uxm in enumerate(date_offset_fields):
        c.builder.store(getattr(civ__qxhe, mmhry__uxm), c.builder.inttoptr(
            c.builder.add(c.builder.ptrtoint(eim__rbfo, lir.IntType(64)),
            lir.Constant(lir.IntType(64), 8 * vvuv__eby)), lir.IntType(64).
            as_pointer()))
    dzy__tcfuh = lir.FunctionType(c.pyapi.pyobj, [lir.IntType(64), lir.
        IntType(1), lir.IntType(64).as_pointer(), lir.IntType(1)])
    qbdrr__gaa = cgutils.get_or_insert_function(c.builder.module,
        dzy__tcfuh, name='box_date_offset')
    nenck__gqiq = c.builder.call(qbdrr__gaa, [civ__qxhe.n, civ__qxhe.
        normalize, eim__rbfo, civ__qxhe.has_kws])
    c.context.nrt.decref(c.builder, typ, val)
    return nenck__gqiq


@unbox(DateOffsetType)
def unbox_date_offset(typ, val, c):
    ryd__gjvy = c.pyapi.object_getattr_string(val, 'n')
    bvmt__sum = c.pyapi.object_getattr_string(val, 'normalize')
    n = c.pyapi.long_as_longlong(ryd__gjvy)
    normalize = c.pyapi.to_native_value(types.bool_, bvmt__sum).value
    eim__rbfo = c.builder.alloca(lir.IntType(64), size=lir.Constant(lir.
        IntType(64), 18))
    dzy__tcfuh = lir.FunctionType(lir.IntType(1), [lir.IntType(8).
        as_pointer(), lir.IntType(64).as_pointer()])
    kpx__xkzw = cgutils.get_or_insert_function(c.builder.module, dzy__tcfuh,
        name='unbox_date_offset')
    has_kws = c.builder.call(kpx__xkzw, [val, eim__rbfo])
    civ__qxhe = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    civ__qxhe.n = n
    civ__qxhe.normalize = normalize
    for vvuv__eby, mmhry__uxm in enumerate(date_offset_fields):
        setattr(civ__qxhe, mmhry__uxm, c.builder.load(c.builder.inttoptr(c.
            builder.add(c.builder.ptrtoint(eim__rbfo, lir.IntType(64)), lir
            .Constant(lir.IntType(64), 8 * vvuv__eby)), lir.IntType(64).
            as_pointer())))
    civ__qxhe.has_kws = has_kws
    c.pyapi.decref(ryd__gjvy)
    c.pyapi.decref(bvmt__sum)
    vhigb__juk = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(civ__qxhe._getvalue(), is_error=vhigb__juk)


@lower_constant(DateOffsetType)
def lower_constant_date_offset(context, builder, ty, pyval):
    n = context.get_constant(types.int64, pyval.n)
    normalize = context.get_constant(types.boolean, pyval.normalize)
    oep__hbvy = [n, normalize]
    has_kws = False
    zxo__albgx = [0] * 9 + [-1] * 9
    for vvuv__eby, mmhry__uxm in enumerate(date_offset_fields):
        if hasattr(pyval, mmhry__uxm):
            ldv__wpmk = context.get_constant(types.int64, getattr(pyval,
                mmhry__uxm))
            has_kws = True
        else:
            ldv__wpmk = context.get_constant(types.int64, zxo__albgx[vvuv__eby]
                )
        oep__hbvy.append(ldv__wpmk)
    has_kws = context.get_constant(types.boolean, has_kws)
    oep__hbvy.append(has_kws)
    return lir.Constant.literal_struct(oep__hbvy)


@overload(pd.tseries.offsets.DateOffset, no_unliteral=True)
def DateOffset(n=1, normalize=False, years=None, months=None, weeks=None,
    days=None, hours=None, minutes=None, seconds=None, microseconds=None,
    nanoseconds=None, year=None, month=None, day=None, weekday=None, hour=
    None, minute=None, second=None, microsecond=None, nanosecond=None):
    has_kws = False
    arzz__taq = [years, months, weeks, days, hours, minutes, seconds,
        microseconds, year, month, day, weekday, hour, minute, second,
        microsecond]
    for rnlw__xzakv in arzz__taq:
        if not is_overload_none(rnlw__xzakv):
            has_kws = True
            break

    def impl(n=1, normalize=False, years=None, months=None, weeks=None,
        days=None, hours=None, minutes=None, seconds=None, microseconds=
        None, nanoseconds=None, year=None, month=None, day=None, weekday=
        None, hour=None, minute=None, second=None, microsecond=None,
        nanosecond=None):
        years = 0 if years is None else years
        months = 0 if months is None else months
        weeks = 0 if weeks is None else weeks
        days = 0 if days is None else days
        hours = 0 if hours is None else hours
        minutes = 0 if minutes is None else minutes
        seconds = 0 if seconds is None else seconds
        microseconds = 0 if microseconds is None else microseconds
        nanoseconds = 0 if nanoseconds is None else nanoseconds
        year = -1 if year is None else year
        month = -1 if month is None else month
        weekday = -1 if weekday is None else weekday
        day = -1 if day is None else day
        hour = -1 if hour is None else hour
        minute = -1 if minute is None else minute
        second = -1 if second is None else second
        microsecond = -1 if microsecond is None else microsecond
        nanosecond = -1 if nanosecond is None else nanosecond
        return init_date_offset(n, normalize, years, months, weeks, days,
            hours, minutes, seconds, microseconds, nanoseconds, year, month,
            day, weekday, hour, minute, second, microsecond, nanosecond,
            has_kws)
    return impl


@intrinsic
def init_date_offset(typingctx, n, normalize, years, months, weeks, days,
    hours, minutes, seconds, microseconds, nanoseconds, year, month, day,
    weekday, hour, minute, second, microsecond, nanosecond, has_kws):

    def codegen(context, builder, signature, args):
        typ = signature.return_type
        civ__qxhe = cgutils.create_struct_proxy(typ)(context, builder)
        civ__qxhe.n = args[0]
        civ__qxhe.normalize = args[1]
        civ__qxhe.years = args[2]
        civ__qxhe.months = args[3]
        civ__qxhe.weeks = args[4]
        civ__qxhe.days = args[5]
        civ__qxhe.hours = args[6]
        civ__qxhe.minutes = args[7]
        civ__qxhe.seconds = args[8]
        civ__qxhe.microseconds = args[9]
        civ__qxhe.nanoseconds = args[10]
        civ__qxhe.year = args[11]
        civ__qxhe.month = args[12]
        civ__qxhe.day = args[13]
        civ__qxhe.weekday = args[14]
        civ__qxhe.hour = args[15]
        civ__qxhe.minute = args[16]
        civ__qxhe.second = args[17]
        civ__qxhe.microsecond = args[18]
        civ__qxhe.nanosecond = args[19]
        civ__qxhe.has_kws = args[20]
        return civ__qxhe._getvalue()
    return DateOffsetType()(n, normalize, years, months, weeks, days, hours,
        minutes, seconds, microseconds, nanoseconds, year, month, day,
        weekday, hour, minute, second, microsecond, nanosecond, has_kws
        ), codegen


make_attribute_wrapper(DateOffsetType, 'n', 'n')
make_attribute_wrapper(DateOffsetType, 'normalize', 'normalize')
make_attribute_wrapper(DateOffsetType, 'years', '_years')
make_attribute_wrapper(DateOffsetType, 'months', '_months')
make_attribute_wrapper(DateOffsetType, 'weeks', '_weeks')
make_attribute_wrapper(DateOffsetType, 'days', '_days')
make_attribute_wrapper(DateOffsetType, 'hours', '_hours')
make_attribute_wrapper(DateOffsetType, 'minutes', '_minutes')
make_attribute_wrapper(DateOffsetType, 'seconds', '_seconds')
make_attribute_wrapper(DateOffsetType, 'microseconds', '_microseconds')
make_attribute_wrapper(DateOffsetType, 'nanoseconds', '_nanoseconds')
make_attribute_wrapper(DateOffsetType, 'year', '_year')
make_attribute_wrapper(DateOffsetType, 'month', '_month')
make_attribute_wrapper(DateOffsetType, 'weekday', '_weekday')
make_attribute_wrapper(DateOffsetType, 'day', '_day')
make_attribute_wrapper(DateOffsetType, 'hour', '_hour')
make_attribute_wrapper(DateOffsetType, 'minute', '_minute')
make_attribute_wrapper(DateOffsetType, 'second', '_second')
make_attribute_wrapper(DateOffsetType, 'microsecond', '_microsecond')
make_attribute_wrapper(DateOffsetType, 'nanosecond', '_nanosecond')
make_attribute_wrapper(DateOffsetType, 'has_kws', '_has_kws')


@register_jitable
def relative_delta_addition(dateoffset, ts):
    if dateoffset._has_kws:
        llt__pbev = -1 if dateoffset.n < 0 else 1
        for szdxq__fzg in range(np.abs(dateoffset.n)):
            year = ts.year
            month = ts.month
            day = ts.day
            hour = ts.hour
            minute = ts.minute
            second = ts.second
            microsecond = ts.microsecond
            nanosecond = ts.nanosecond
            if dateoffset._year != -1:
                year = dateoffset._year
            year += llt__pbev * dateoffset._years
            if dateoffset._month != -1:
                month = dateoffset._month
            month += llt__pbev * dateoffset._months
            year, month, ecexz__nzj = calculate_month_end_date(year, month,
                day, 0)
            if day > ecexz__nzj:
                day = ecexz__nzj
            if dateoffset._day != -1:
                day = dateoffset._day
            if dateoffset._hour != -1:
                hour = dateoffset._hour
            if dateoffset._minute != -1:
                minute = dateoffset._minute
            if dateoffset._second != -1:
                second = dateoffset._second
            if dateoffset._microsecond != -1:
                microsecond = dateoffset._microsecond
            if dateoffset._nanosecond != -1:
                nanosecond = dateoffset._nanosecond
            ts = pd.Timestamp(year=year, month=month, day=day, hour=hour,
                minute=minute, second=second, microsecond=microsecond,
                nanosecond=nanosecond)
            td = pd.Timedelta(days=dateoffset._days + 7 * dateoffset._weeks,
                hours=dateoffset._hours, minutes=dateoffset._minutes,
                seconds=dateoffset._seconds, microseconds=dateoffset.
                _microseconds)
            td = td + pd.Timedelta(dateoffset._nanoseconds, unit='ns')
            if llt__pbev == -1:
                td = -td
            ts = ts + td
            if dateoffset._weekday != -1:
                hdxu__gogqp = ts.weekday()
                cklgd__eqm = (dateoffset._weekday - hdxu__gogqp) % 7
                ts = ts + pd.Timedelta(days=cklgd__eqm)
        return ts
    else:
        return pd.Timedelta(days=dateoffset.n) + ts


def overload_add_operator_date_offset_type(lhs, rhs):
    if lhs == date_offset_type and rhs == pd_timestamp_tz_naive_type:

        def impl(lhs, rhs):
            ts = relative_delta_addition(lhs, rhs)
            if lhs.normalize:
                return ts.normalize()
            return ts
        return impl
    if lhs == date_offset_type and rhs in [datetime_date_type,
        datetime_datetime_type]:

        def impl(lhs, rhs):
            ts = relative_delta_addition(lhs, pd.Timestamp(rhs))
            if lhs.normalize:
                return ts.normalize()
            return ts
        return impl
    if lhs in [datetime_datetime_type, pd_timestamp_tz_naive_type,
        datetime_date_type] and rhs == date_offset_type:

        def impl(lhs, rhs):
            return rhs + lhs
        return impl
    raise BodoError(
        f'add operator not supported for data types {lhs} and {rhs}.')


def overload_sub_operator_offsets(lhs, rhs):
    if (lhs in [datetime_datetime_type, datetime_date_type] or isinstance(
        lhs, PandasTimestampType)) and rhs in [date_offset_type,
        month_begin_type, month_end_type, week_type]:

        def impl(lhs, rhs):
            return lhs + -rhs
        return impl


@overload(operator.neg, no_unliteral=True)
def overload_neg(lhs):
    if lhs == month_begin_type:

        def impl(lhs):
            return pd.tseries.offsets.MonthBegin(-lhs.n, lhs.normalize)
    elif lhs == month_end_type:

        def impl(lhs):
            return pd.tseries.offsets.MonthEnd(-lhs.n, lhs.normalize)
    elif lhs == week_type:

        def impl(lhs):
            return pd.tseries.offsets.Week(-lhs.n, lhs.normalize, lhs.weekday)
    elif lhs == date_offset_type:

        def impl(lhs):
            n = -lhs.n
            normalize = lhs.normalize
            if lhs._has_kws:
                years = lhs._years
                months = lhs._months
                weeks = lhs._weeks
                days = lhs._days
                hours = lhs._hours
                minutes = lhs._minutes
                seconds = lhs._seconds
                microseconds = lhs._microseconds
                year = lhs._year
                month = lhs._month
                day = lhs._day
                weekday = lhs._weekday
                hour = lhs._hour
                minute = lhs._minute
                second = lhs._second
                microsecond = lhs._microsecond
                nanoseconds = lhs._nanoseconds
                nanosecond = lhs._nanosecond
                return pd.tseries.offsets.DateOffset(n, normalize, years,
                    months, weeks, days, hours, minutes, seconds,
                    microseconds, nanoseconds, year, month, day, weekday,
                    hour, minute, second, microsecond, nanosecond)
            else:
                return pd.tseries.offsets.DateOffset(n, normalize)
    else:
        return
    return impl


def is_offsets_type(val):
    return val in [date_offset_type, month_begin_type, month_end_type,
        week_type]


class WeekType(types.Type):

    def __init__(self):
        super(WeekType, self).__init__(name='WeekType()')


week_type = WeekType()


@typeof_impl.register(pd.tseries.offsets.Week)
def typeof_week(val, c):
    return week_type


@register_model(WeekType)
class WeekModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        obruf__vkgii = [('n', types.int64), ('normalize', types.boolean), (
            'weekday', types.int64)]
        super(WeekModel, self).__init__(dmm, fe_type, obruf__vkgii)


make_attribute_wrapper(WeekType, 'n', 'n')
make_attribute_wrapper(WeekType, 'normalize', 'normalize')
make_attribute_wrapper(WeekType, 'weekday', 'weekday')


@overload(pd.tseries.offsets.Week, no_unliteral=True)
def Week(n=1, normalize=False, weekday=None):

    def impl(n=1, normalize=False, weekday=None):
        llobr__bofl = -1 if weekday is None else weekday
        return init_week(n, normalize, llobr__bofl)
    return impl


@intrinsic
def init_week(typingctx, n, normalize, weekday):

    def codegen(context, builder, signature, args):
        typ = signature.return_type
        aomt__ngrat = cgutils.create_struct_proxy(typ)(context, builder)
        aomt__ngrat.n = args[0]
        aomt__ngrat.normalize = args[1]
        aomt__ngrat.weekday = args[2]
        return aomt__ngrat._getvalue()
    return WeekType()(n, normalize, weekday), codegen


@lower_constant(WeekType)
def lower_constant_week(context, builder, ty, pyval):
    n = context.get_constant(types.int64, pyval.n)
    normalize = context.get_constant(types.boolean, pyval.normalize)
    if pyval.weekday is not None:
        weekday = context.get_constant(types.int64, pyval.weekday)
    else:
        weekday = context.get_constant(types.int64, -1)
    return lir.Constant.literal_struct([n, normalize, weekday])


@box(WeekType)
def box_week(typ, val, c):
    aomt__ngrat = cgutils.create_struct_proxy(typ)(c.context, c.builder,
        value=val)
    ryd__gjvy = c.pyapi.long_from_longlong(aomt__ngrat.n)
    bvmt__sum = c.pyapi.from_native_value(types.boolean, aomt__ngrat.
        normalize, c.env_manager)
    hji__lyfp = c.pyapi.long_from_longlong(aomt__ngrat.weekday)
    rlync__dgits = c.pyapi.unserialize(c.pyapi.serialize_object(pd.tseries.
        offsets.Week))
    svgg__rljzs = c.builder.icmp_signed('!=', lir.Constant(lir.IntType(64),
        -1), aomt__ngrat.weekday)
    with c.builder.if_else(svgg__rljzs) as (ngzwn__pec, jktw__xzk):
        with ngzwn__pec:
            vxn__fzktj = c.pyapi.call_function_objargs(rlync__dgits, (
                ryd__gjvy, bvmt__sum, hji__lyfp))
            cfw__ctoij = c.builder.block
        with jktw__xzk:
            dyhy__lsbbu = c.pyapi.call_function_objargs(rlync__dgits, (
                ryd__gjvy, bvmt__sum))
            ixj__ticw = c.builder.block
    mlz__lgfez = c.builder.phi(vxn__fzktj.type)
    mlz__lgfez.add_incoming(vxn__fzktj, cfw__ctoij)
    mlz__lgfez.add_incoming(dyhy__lsbbu, ixj__ticw)
    c.pyapi.decref(hji__lyfp)
    c.pyapi.decref(ryd__gjvy)
    c.pyapi.decref(bvmt__sum)
    c.pyapi.decref(rlync__dgits)
    return mlz__lgfez


@unbox(WeekType)
def unbox_week(typ, val, c):
    ryd__gjvy = c.pyapi.object_getattr_string(val, 'n')
    bvmt__sum = c.pyapi.object_getattr_string(val, 'normalize')
    hji__lyfp = c.pyapi.object_getattr_string(val, 'weekday')
    n = c.pyapi.long_as_longlong(ryd__gjvy)
    normalize = c.pyapi.to_native_value(types.bool_, bvmt__sum).value
    hpxsi__fflsd = c.pyapi.make_none()
    xxy__yab = c.builder.icmp_unsigned('==', hji__lyfp, hpxsi__fflsd)
    with c.builder.if_else(xxy__yab) as (jktw__xzk, ngzwn__pec):
        with ngzwn__pec:
            vxn__fzktj = c.pyapi.long_as_longlong(hji__lyfp)
            cfw__ctoij = c.builder.block
        with jktw__xzk:
            dyhy__lsbbu = lir.Constant(lir.IntType(64), -1)
            ixj__ticw = c.builder.block
    mlz__lgfez = c.builder.phi(vxn__fzktj.type)
    mlz__lgfez.add_incoming(vxn__fzktj, cfw__ctoij)
    mlz__lgfez.add_incoming(dyhy__lsbbu, ixj__ticw)
    aomt__ngrat = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    aomt__ngrat.n = n
    aomt__ngrat.normalize = normalize
    aomt__ngrat.weekday = mlz__lgfez
    c.pyapi.decref(ryd__gjvy)
    c.pyapi.decref(bvmt__sum)
    c.pyapi.decref(hji__lyfp)
    vhigb__juk = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(aomt__ngrat._getvalue(), is_error=vhigb__juk)


def overload_add_operator_week_offset_type(lhs, rhs):
    if lhs == week_type and isinstance(rhs, PandasTimestampType):

        def impl(lhs, rhs):
            if lhs.normalize:
                aadu__vwdmb = rhs.normalize()
            else:
                aadu__vwdmb = rhs
            uhq__jykrl = calculate_week_date(lhs.n, lhs.weekday, aadu__vwdmb)
            return aadu__vwdmb + uhq__jykrl
        return impl
    if lhs == week_type and rhs == datetime_datetime_type:

        def impl(lhs, rhs):
            if lhs.normalize:
                aadu__vwdmb = pd.Timestamp(year=rhs.year, month=rhs.month,
                    day=rhs.day)
            else:
                aadu__vwdmb = pd.Timestamp(year=rhs.year, month=rhs.month,
                    day=rhs.day, hour=rhs.hour, minute=rhs.minute, second=
                    rhs.second, microsecond=rhs.microsecond)
            uhq__jykrl = calculate_week_date(lhs.n, lhs.weekday, aadu__vwdmb)
            return aadu__vwdmb + uhq__jykrl
        return impl
    if lhs == week_type and rhs == datetime_date_type:

        def impl(lhs, rhs):
            uhq__jykrl = calculate_week_date(lhs.n, lhs.weekday, rhs)
            return rhs + uhq__jykrl
        return impl
    if (lhs in [datetime_datetime_type, datetime_date_type] or isinstance(
        lhs, PandasTimestampType)) and rhs == week_type:

        def impl(lhs, rhs):
            return rhs + lhs
        return impl
    raise BodoError(
        f'add operator not supported for data types {lhs} and {rhs}.')


def calculate_week_date(n, weekday, input_date_or_ts):
    pass


@overload(calculate_week_date)
def overload_calculate_week_date(n, weekday, input_date_or_ts):
    if isinstance(input_date_or_ts, PandasTimestampType
        ) and tz_has_transition_times(input_date_or_ts.tz):

        def impl_tz_aware(n, weekday, input_date_or_ts):
            if weekday == -1:
                td = pd.Timedelta(weeks=n)
            else:
                fauh__oljz = input_date_or_ts.weekday()
                if weekday != fauh__oljz:
                    dfqwn__cdhsv = (weekday - fauh__oljz) % 7
                    if n > 0:
                        n = n - 1
                td = pd.Timedelta(weeks=n, days=dfqwn__cdhsv)
            return update_timedelta_with_transition(input_date_or_ts, td)
        return impl_tz_aware
    else:

        def impl(n, weekday, input_date_or_ts):
            if weekday == -1:
                return pd.Timedelta(weeks=n)
            fauh__oljz = input_date_or_ts.weekday()
            if weekday != fauh__oljz:
                dfqwn__cdhsv = (weekday - fauh__oljz) % 7
                if n > 0:
                    n = n - 1
            return pd.Timedelta(weeks=n, days=dfqwn__cdhsv)
        return impl


def update_timedelta_with_transition(ts_value, timedelta):
    pass


@overload(update_timedelta_with_transition)
def overload_update_timedelta_with_transition(ts, td):
    if tz_has_transition_times(ts.tz):
        hvma__wyitj = pytz.timezone(ts.tz)
        mzm__ywxy = np.array(hvma__wyitj._utc_transition_times, dtype='M8[ns]'
            ).view('i8')
        qyc__ikw = np.array(hvma__wyitj._transition_info)[:, 0]
        qyc__ikw = (pd.Series(qyc__ikw).dt.total_seconds() * 1000000000
            ).astype(np.int64).values

        def impl_tz_aware(ts, td):
            ncu__csrv = ts.value
            vmxq__pnb = ncu__csrv + td.value
            kak__dcwoe = np.searchsorted(mzm__ywxy, ncu__csrv, side='right'
                ) - 1
            tivia__welpw = np.searchsorted(mzm__ywxy, vmxq__pnb, side='right'
                ) - 1
            dfqwn__cdhsv = qyc__ikw[kak__dcwoe] - qyc__ikw[tivia__welpw]
            return pd.Timedelta(td.value + dfqwn__cdhsv)
        return impl_tz_aware
    else:
        return lambda ts, td: td


date_offset_unsupported_attrs = {'base', 'freqstr', 'kwds', 'name', 'nanos',
    'rule_code'}
date_offset_unsupported = {'__call__', 'rollback', 'rollforward',
    'is_month_start', 'is_month_end', 'apply', 'apply_index', 'copy',
    'isAnchored', 'onOffset', 'is_anchored', 'is_on_offset',
    'is_quarter_start', 'is_quarter_end', 'is_year_start', 'is_year_end'}
month_end_unsupported_attrs = {'base', 'freqstr', 'kwds', 'name', 'nanos',
    'rule_code'}
month_end_unsupported = {'__call__', 'rollback', 'rollforward', 'apply',
    'apply_index', 'copy', 'isAnchored', 'onOffset', 'is_anchored',
    'is_on_offset', 'is_month_start', 'is_month_end', 'is_quarter_start',
    'is_quarter_end', 'is_year_start', 'is_year_end'}
month_begin_unsupported_attrs = {'basefreqstr', 'kwds', 'name', 'nanos',
    'rule_code'}
month_begin_unsupported = {'__call__', 'rollback', 'rollforward', 'apply',
    'apply_index', 'copy', 'isAnchored', 'onOffset', 'is_anchored',
    'is_on_offset', 'is_month_start', 'is_month_end', 'is_quarter_start',
    'is_quarter_end', 'is_year_start', 'is_year_end'}
week_unsupported_attrs = {'basefreqstr', 'kwds', 'name', 'nanos', 'rule_code'}
week_unsupported = {'__call__', 'rollback', 'rollforward', 'apply',
    'apply_index', 'copy', 'isAnchored', 'onOffset', 'is_anchored',
    'is_on_offset', 'is_month_start', 'is_month_end', 'is_quarter_start',
    'is_quarter_end', 'is_year_start', 'is_year_end'}
offsets_unsupported = {pd.tseries.offsets.BusinessDay, pd.tseries.offsets.
    BDay, pd.tseries.offsets.BusinessHour, pd.tseries.offsets.
    CustomBusinessDay, pd.tseries.offsets.CDay, pd.tseries.offsets.
    CustomBusinessHour, pd.tseries.offsets.BusinessMonthEnd, pd.tseries.
    offsets.BMonthEnd, pd.tseries.offsets.BusinessMonthBegin, pd.tseries.
    offsets.BMonthBegin, pd.tseries.offsets.CustomBusinessMonthEnd, pd.
    tseries.offsets.CBMonthEnd, pd.tseries.offsets.CustomBusinessMonthBegin,
    pd.tseries.offsets.CBMonthBegin, pd.tseries.offsets.SemiMonthEnd, pd.
    tseries.offsets.SemiMonthBegin, pd.tseries.offsets.WeekOfMonth, pd.
    tseries.offsets.LastWeekOfMonth, pd.tseries.offsets.BQuarterEnd, pd.
    tseries.offsets.BQuarterBegin, pd.tseries.offsets.QuarterEnd, pd.
    tseries.offsets.QuarterBegin, pd.tseries.offsets.BYearEnd, pd.tseries.
    offsets.BYearBegin, pd.tseries.offsets.YearEnd, pd.tseries.offsets.
    YearBegin, pd.tseries.offsets.FY5253, pd.tseries.offsets.FY5253Quarter,
    pd.tseries.offsets.Easter, pd.tseries.offsets.Tick, pd.tseries.offsets.
    Day, pd.tseries.offsets.Hour, pd.tseries.offsets.Minute, pd.tseries.
    offsets.Second, pd.tseries.offsets.Milli, pd.tseries.offsets.Micro, pd.
    tseries.offsets.Nano}
frequencies_unsupported = {pd.tseries.frequencies.to_offset}


def _install_date_offsets_unsupported():
    for gxyl__sft in date_offset_unsupported_attrs:
        pdo__jjtmx = 'pandas.tseries.offsets.DateOffset.' + gxyl__sft
        overload_attribute(DateOffsetType, gxyl__sft)(
            create_unsupported_overload(pdo__jjtmx))
    for gxyl__sft in date_offset_unsupported:
        pdo__jjtmx = 'pandas.tseries.offsets.DateOffset.' + gxyl__sft
        overload_method(DateOffsetType, gxyl__sft)(create_unsupported_overload
            (pdo__jjtmx))


def _install_month_begin_unsupported():
    for gxyl__sft in month_begin_unsupported_attrs:
        pdo__jjtmx = 'pandas.tseries.offsets.MonthBegin.' + gxyl__sft
        overload_attribute(MonthBeginType, gxyl__sft)(
            create_unsupported_overload(pdo__jjtmx))
    for gxyl__sft in month_begin_unsupported:
        pdo__jjtmx = 'pandas.tseries.offsets.MonthBegin.' + gxyl__sft
        overload_method(MonthBeginType, gxyl__sft)(create_unsupported_overload
            (pdo__jjtmx))


def _install_month_end_unsupported():
    for gxyl__sft in date_offset_unsupported_attrs:
        pdo__jjtmx = 'pandas.tseries.offsets.MonthEnd.' + gxyl__sft
        overload_attribute(MonthEndType, gxyl__sft)(create_unsupported_overload
            (pdo__jjtmx))
    for gxyl__sft in date_offset_unsupported:
        pdo__jjtmx = 'pandas.tseries.offsets.MonthEnd.' + gxyl__sft
        overload_method(MonthEndType, gxyl__sft)(create_unsupported_overload
            (pdo__jjtmx))


def _install_week_unsupported():
    for gxyl__sft in week_unsupported_attrs:
        pdo__jjtmx = 'pandas.tseries.offsets.Week.' + gxyl__sft
        overload_attribute(WeekType, gxyl__sft)(create_unsupported_overload
            (pdo__jjtmx))
    for gxyl__sft in week_unsupported:
        pdo__jjtmx = 'pandas.tseries.offsets.Week.' + gxyl__sft
        overload_method(WeekType, gxyl__sft)(create_unsupported_overload(
            pdo__jjtmx))


def _install_offsets_unsupported():
    for ldv__wpmk in offsets_unsupported:
        pdo__jjtmx = 'pandas.tseries.offsets.' + ldv__wpmk.__name__
        overload(ldv__wpmk)(create_unsupported_overload(pdo__jjtmx))


def _install_frequencies_unsupported():
    for ldv__wpmk in frequencies_unsupported:
        pdo__jjtmx = 'pandas.tseries.frequencies.' + ldv__wpmk.__name__
        overload(ldv__wpmk)(create_unsupported_overload(pdo__jjtmx))


_install_date_offsets_unsupported()
_install_month_begin_unsupported()
_install_month_end_unsupported()
_install_week_unsupported()
_install_offsets_unsupported()
_install_frequencies_unsupported()
