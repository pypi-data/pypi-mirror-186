import datetime
import numba
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.imputils import lower_constant
from numba.extending import NativeValue, box, intrinsic, lower_cast, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_jitable, register_model, typeof_impl, unbox
"""
Implementation is based on
https://github.com/python/cpython/blob/39a5c889d30d03a88102e56f03ee0c95db198fb3/Lib/datetime.py
"""


class DatetimeDatetimeType(types.Type):

    def __init__(self):
        super(DatetimeDatetimeType, self).__init__(name=
            'DatetimeDatetimeType()')


datetime_datetime_type = DatetimeDatetimeType()
types.datetime_datetime_type = datetime_datetime_type


@typeof_impl.register(datetime.datetime)
def typeof_datetime_datetime(val, c):
    return datetime_datetime_type


@register_model(DatetimeDatetimeType)
class DatetimeDateTimeModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        mgq__edrb = [('year', types.int64), ('month', types.int64), ('day',
            types.int64), ('hour', types.int64), ('minute', types.int64), (
            'second', types.int64), ('microsecond', types.int64)]
        super(DatetimeDateTimeModel, self).__init__(dmm, fe_type, mgq__edrb)


@box(DatetimeDatetimeType)
def box_datetime_datetime(typ, val, c):
    wlm__xfi = cgutils.create_struct_proxy(typ)(c.context, c.builder, value=val
        )
    yba__ieppp = c.pyapi.long_from_longlong(wlm__xfi.year)
    xquuw__xoj = c.pyapi.long_from_longlong(wlm__xfi.month)
    iqj__ftaos = c.pyapi.long_from_longlong(wlm__xfi.day)
    tmcks__suayo = c.pyapi.long_from_longlong(wlm__xfi.hour)
    rmrr__zxkf = c.pyapi.long_from_longlong(wlm__xfi.minute)
    sdsy__mmm = c.pyapi.long_from_longlong(wlm__xfi.second)
    tcdzb__laaql = c.pyapi.long_from_longlong(wlm__xfi.microsecond)
    gheka__kaxo = c.pyapi.unserialize(c.pyapi.serialize_object(datetime.
        datetime))
    ktskp__qqe = c.pyapi.call_function_objargs(gheka__kaxo, (yba__ieppp,
        xquuw__xoj, iqj__ftaos, tmcks__suayo, rmrr__zxkf, sdsy__mmm,
        tcdzb__laaql))
    c.pyapi.decref(yba__ieppp)
    c.pyapi.decref(xquuw__xoj)
    c.pyapi.decref(iqj__ftaos)
    c.pyapi.decref(tmcks__suayo)
    c.pyapi.decref(rmrr__zxkf)
    c.pyapi.decref(sdsy__mmm)
    c.pyapi.decref(tcdzb__laaql)
    c.pyapi.decref(gheka__kaxo)
    return ktskp__qqe


@unbox(DatetimeDatetimeType)
def unbox_datetime_datetime(typ, val, c):
    yba__ieppp = c.pyapi.object_getattr_string(val, 'year')
    xquuw__xoj = c.pyapi.object_getattr_string(val, 'month')
    iqj__ftaos = c.pyapi.object_getattr_string(val, 'day')
    tmcks__suayo = c.pyapi.object_getattr_string(val, 'hour')
    rmrr__zxkf = c.pyapi.object_getattr_string(val, 'minute')
    sdsy__mmm = c.pyapi.object_getattr_string(val, 'second')
    tcdzb__laaql = c.pyapi.object_getattr_string(val, 'microsecond')
    wlm__xfi = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    wlm__xfi.year = c.pyapi.long_as_longlong(yba__ieppp)
    wlm__xfi.month = c.pyapi.long_as_longlong(xquuw__xoj)
    wlm__xfi.day = c.pyapi.long_as_longlong(iqj__ftaos)
    wlm__xfi.hour = c.pyapi.long_as_longlong(tmcks__suayo)
    wlm__xfi.minute = c.pyapi.long_as_longlong(rmrr__zxkf)
    wlm__xfi.second = c.pyapi.long_as_longlong(sdsy__mmm)
    wlm__xfi.microsecond = c.pyapi.long_as_longlong(tcdzb__laaql)
    c.pyapi.decref(yba__ieppp)
    c.pyapi.decref(xquuw__xoj)
    c.pyapi.decref(iqj__ftaos)
    c.pyapi.decref(tmcks__suayo)
    c.pyapi.decref(rmrr__zxkf)
    c.pyapi.decref(sdsy__mmm)
    c.pyapi.decref(tcdzb__laaql)
    pusu__hxh = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(wlm__xfi._getvalue(), is_error=pusu__hxh)


@lower_constant(DatetimeDatetimeType)
def constant_datetime(context, builder, ty, pyval):
    year = context.get_constant(types.int64, pyval.year)
    month = context.get_constant(types.int64, pyval.month)
    day = context.get_constant(types.int64, pyval.day)
    hour = context.get_constant(types.int64, pyval.hour)
    minute = context.get_constant(types.int64, pyval.minute)
    second = context.get_constant(types.int64, pyval.second)
    microsecond = context.get_constant(types.int64, pyval.microsecond)
    return lir.Constant.literal_struct([year, month, day, hour, minute,
        second, microsecond])


@overload(datetime.datetime, no_unliteral=True)
def datetime_datetime(year, month, day, hour=0, minute=0, second=0,
    microsecond=0):

    def impl_datetime(year, month, day, hour=0, minute=0, second=0,
        microsecond=0):
        return init_datetime(year, month, day, hour, minute, second,
            microsecond)
    return impl_datetime


@intrinsic
def init_datetime(typingctx, year, month, day, hour, minute, second,
    microsecond):

    def codegen(context, builder, signature, args):
        typ = signature.return_type
        wlm__xfi = cgutils.create_struct_proxy(typ)(context, builder)
        wlm__xfi.year = args[0]
        wlm__xfi.month = args[1]
        wlm__xfi.day = args[2]
        wlm__xfi.hour = args[3]
        wlm__xfi.minute = args[4]
        wlm__xfi.second = args[5]
        wlm__xfi.microsecond = args[6]
        return wlm__xfi._getvalue()
    return DatetimeDatetimeType()(year, month, day, hour, minute, second,
        microsecond), codegen


make_attribute_wrapper(DatetimeDatetimeType, 'year', '_year')
make_attribute_wrapper(DatetimeDatetimeType, 'month', '_month')
make_attribute_wrapper(DatetimeDatetimeType, 'day', '_day')
make_attribute_wrapper(DatetimeDatetimeType, 'hour', '_hour')
make_attribute_wrapper(DatetimeDatetimeType, 'minute', '_minute')
make_attribute_wrapper(DatetimeDatetimeType, 'second', '_second')
make_attribute_wrapper(DatetimeDatetimeType, 'microsecond', '_microsecond')


@overload_attribute(DatetimeDatetimeType, 'year')
def datetime_get_year(dt):

    def impl(dt):
        return dt._year
    return impl


@overload_attribute(DatetimeDatetimeType, 'month')
def datetime_get_month(dt):

    def impl(dt):
        return dt._month
    return impl


@overload_attribute(DatetimeDatetimeType, 'day')
def datetime_get_day(dt):

    def impl(dt):
        return dt._day
    return impl


@overload_attribute(DatetimeDatetimeType, 'hour')
def datetime_get_hour(dt):

    def impl(dt):
        return dt._hour
    return impl


@overload_attribute(DatetimeDatetimeType, 'minute')
def datetime_get_minute(dt):

    def impl(dt):
        return dt._minute
    return impl


@overload_attribute(DatetimeDatetimeType, 'second')
def datetime_get_second(dt):

    def impl(dt):
        return dt._second
    return impl


@overload_attribute(DatetimeDatetimeType, 'microsecond')
def datetime_get_microsecond(dt):

    def impl(dt):
        return dt._microsecond
    return impl


@overload_method(DatetimeDatetimeType, 'date', no_unliteral=True)
def date(dt):

    def impl(dt):
        return datetime.date(dt.year, dt.month, dt.day)
    return impl


@register_jitable
def now_impl():
    with numba.objmode(d='datetime_datetime_type'):
        d = datetime.datetime.now()
    return d


@register_jitable
def today_impl():
    with numba.objmode(d='datetime_datetime_type'):
        d = datetime.datetime.today()
    return d


@register_jitable
def strptime_impl(date_string, dtformat):
    with numba.objmode(d='datetime_datetime_type'):
        d = datetime.datetime.strptime(date_string, dtformat)
    return d


@register_jitable
def _cmp(x, y):
    return 0 if x == y else 1 if x > y else -1


def create_cmp_op_overload(op):

    def overload_datetime_cmp(lhs, rhs):
        if lhs == datetime_datetime_type and rhs == datetime_datetime_type:

            def impl(lhs, rhs):
                y, sql__ppcgv = lhs.year, rhs.year
                huboi__hhyum, hpe__ogaxd = lhs.month, rhs.month
                d, ovwen__wjyd = lhs.day, rhs.day
                clqk__smks, oliw__axlg = lhs.hour, rhs.hour
                lfn__vrd, zaw__xnkn = lhs.minute, rhs.minute
                yhsq__kqz, yyk__uajfh = lhs.second, rhs.second
                yke__uptn, oeac__ygeez = lhs.microsecond, rhs.microsecond
                return op(_cmp((y, huboi__hhyum, d, clqk__smks, lfn__vrd,
                    yhsq__kqz, yke__uptn), (sql__ppcgv, hpe__ogaxd,
                    ovwen__wjyd, oliw__axlg, zaw__xnkn, yyk__uajfh,
                    oeac__ygeez)), 0)
            return impl
    return overload_datetime_cmp


def overload_sub_operator_datetime_datetime(lhs, rhs):
    if lhs == datetime_datetime_type and rhs == datetime_datetime_type:

        def impl(lhs, rhs):
            mwv__qmsg = lhs.toordinal()
            ljggb__fzw = rhs.toordinal()
            hki__uctha = lhs.second + lhs.minute * 60 + lhs.hour * 3600
            kdix__ygrmi = rhs.second + rhs.minute * 60 + rhs.hour * 3600
            yhacl__ggf = datetime.timedelta(mwv__qmsg - ljggb__fzw, 
                hki__uctha - kdix__ygrmi, lhs.microsecond - rhs.microsecond)
            return yhacl__ggf
        return impl


@lower_cast(types.Optional(numba.core.types.NPTimedelta('ns')), numba.core.
    types.NPTimedelta('ns'))
@lower_cast(types.Optional(numba.core.types.NPDatetime('ns')), numba.core.
    types.NPDatetime('ns'))
def optional_dt64_to_dt64(context, builder, fromty, toty, val):
    exkzj__lse = context.make_helper(builder, fromty, value=val)
    alcg__dpx = cgutils.as_bool_bit(builder, exkzj__lse.valid)
    with builder.if_else(alcg__dpx) as (gbdm__krx, cew__pnty):
        with gbdm__krx:
            kyae__vempf = context.cast(builder, exkzj__lse.data, fromty.
                type, toty)
            qsbgf__bgxn = builder.block
        with cew__pnty:
            wtyd__qjznt = numba.np.npdatetime.NAT
            egey__mvd = builder.block
    ktskp__qqe = builder.phi(kyae__vempf.type)
    ktskp__qqe.add_incoming(kyae__vempf, qsbgf__bgxn)
    ktskp__qqe.add_incoming(wtyd__qjznt, egey__mvd)
    return ktskp__qqe
