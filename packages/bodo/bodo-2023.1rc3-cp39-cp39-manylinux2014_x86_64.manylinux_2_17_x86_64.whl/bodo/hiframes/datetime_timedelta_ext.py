"""Numba extension support for datetime.timedelta objects and their arrays.
"""
import datetime
import operator
from collections import namedtuple
import llvmlite.binding as ll
import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.imputils import lower_constant
from numba.extending import NativeValue, box, intrinsic, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_jitable, register_model, typeof_impl, unbox
from numba.parfors.array_analysis import ArrayAnalysis
import bodo
from bodo.hiframes.datetime_datetime_ext import datetime_datetime_type
from bodo.libs import hdatetime_ext
from bodo.utils.indexing import get_new_null_mask_bool_index, get_new_null_mask_int_index, get_new_null_mask_slice_index, setitem_slice_index_null_bits
from bodo.utils.typing import BodoError, get_overload_const_str, is_iterable_type, is_list_like_index_type, is_overload_constant_str
ll.add_symbol('box_datetime_timedelta_array', hdatetime_ext.
    box_datetime_timedelta_array)
ll.add_symbol('unbox_datetime_timedelta_array', hdatetime_ext.
    unbox_datetime_timedelta_array)


class NoInput:
    pass


_no_input = NoInput()


class NoInputType(types.Type):

    def __init__(self):
        super(NoInputType, self).__init__(name='NoInput')


register_model(NoInputType)(models.OpaqueModel)


@typeof_impl.register(NoInput)
def _typ_no_input(val, c):
    return NoInputType()


@lower_constant(NoInputType)
def constant_no_input(context, builder, ty, pyval):
    return context.get_dummy_value()


class PDTimeDeltaType(types.Type):

    def __init__(self):
        super(PDTimeDeltaType, self).__init__(name='PDTimeDeltaType()')


pd_timedelta_type = PDTimeDeltaType()
types.pd_timedelta_type = pd_timedelta_type


@typeof_impl.register(pd.Timedelta)
def typeof_pd_timedelta(val, c):
    return pd_timedelta_type


@register_model(PDTimeDeltaType)
class PDTimeDeltaModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        obuoz__ryvqn = [('value', types.int64)]
        super(PDTimeDeltaModel, self).__init__(dmm, fe_type, obuoz__ryvqn)


@box(PDTimeDeltaType)
def box_pd_timedelta(typ, val, c):
    btnw__tom = cgutils.create_struct_proxy(typ)(c.context, c.builder,
        value=val)
    vqer__vjme = c.pyapi.long_from_longlong(btnw__tom.value)
    pslc__nfnu = c.pyapi.unserialize(c.pyapi.serialize_object(pd.Timedelta))
    res = c.pyapi.call_function_objargs(pslc__nfnu, (vqer__vjme,))
    c.pyapi.decref(vqer__vjme)
    c.pyapi.decref(pslc__nfnu)
    return res


@unbox(PDTimeDeltaType)
def unbox_pd_timedelta(typ, val, c):
    vqer__vjme = c.pyapi.object_getattr_string(val, 'value')
    kndr__invx = c.pyapi.long_as_longlong(vqer__vjme)
    btnw__tom = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    btnw__tom.value = kndr__invx
    c.pyapi.decref(vqer__vjme)
    kos__icv = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(btnw__tom._getvalue(), is_error=kos__icv)


@lower_constant(PDTimeDeltaType)
def lower_constant_pd_timedelta(context, builder, ty, pyval):
    value = context.get_constant(types.int64, pyval.value)
    return lir.Constant.literal_struct([value])


@overload(pd.Timedelta, no_unliteral=True)
def pd_timedelta(value=_no_input, unit='ns', days=0, seconds=0,
    microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
    if value == _no_input:

        def impl_timedelta_kw(value=_no_input, unit='ns', days=0, seconds=0,
            microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
            days += weeks * 7
            hours += days * 24
            minutes += 60 * hours
            seconds += 60 * minutes
            milliseconds += 1000 * seconds
            microseconds += 1000 * milliseconds
            zdcgn__dlzd = 1000 * microseconds
            return init_pd_timedelta(zdcgn__dlzd)
        return impl_timedelta_kw
    if value == bodo.string_type or is_overload_constant_str(value):

        def impl_str(value=_no_input, unit='ns', days=0, seconds=0,
            microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
            with numba.objmode(res='pd_timedelta_type'):
                res = pd.Timedelta(value)
            return res
        return impl_str
    if value == pd_timedelta_type:
        return (lambda value=_no_input, unit='ns', days=0, seconds=0,
            microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0: value)
    if value == datetime_timedelta_type:

        def impl_timedelta_datetime(value=_no_input, unit='ns', days=0,
            seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0,
            weeks=0):
            days = value.days
            seconds = 60 * 60 * 24 * days + value.seconds
            microseconds = 1000 * 1000 * seconds + value.microseconds
            zdcgn__dlzd = 1000 * microseconds
            return init_pd_timedelta(zdcgn__dlzd)
        return impl_timedelta_datetime
    if not is_overload_constant_str(unit):
        raise BodoError('pd.to_timedelta(): unit should be a constant string')
    unit = pd._libs.tslibs.timedeltas.parse_timedelta_unit(
        get_overload_const_str(unit))
    cluqh__mpfdf, ahop__nhq = pd._libs.tslibs.conversion.precision_from_unit(
        unit)

    def impl_timedelta(value=_no_input, unit='ns', days=0, seconds=0,
        microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
        return init_pd_timedelta(value * cluqh__mpfdf)
    return impl_timedelta


@intrinsic
def init_pd_timedelta(typingctx, value):

    def codegen(context, builder, signature, args):
        typ = signature.return_type
        timedelta = cgutils.create_struct_proxy(typ)(context, builder)
        timedelta.value = args[0]
        return timedelta._getvalue()
    return PDTimeDeltaType()(value), codegen


make_attribute_wrapper(PDTimeDeltaType, 'value', '_value')


@overload_attribute(PDTimeDeltaType, 'value')
@overload_attribute(PDTimeDeltaType, 'delta')
def pd_timedelta_get_value(td):

    def impl(td):
        return td._value
    return impl


@overload_attribute(PDTimeDeltaType, 'days')
def pd_timedelta_get_days(td):

    def impl(td):
        return td._value // (1000 * 1000 * 1000 * 60 * 60 * 24)
    return impl


@overload_attribute(PDTimeDeltaType, 'seconds')
def pd_timedelta_get_seconds(td):

    def impl(td):
        return td._value // (1000 * 1000 * 1000) % (60 * 60 * 24)
    return impl


@overload_attribute(PDTimeDeltaType, 'microseconds')
def pd_timedelta_get_microseconds(td):

    def impl(td):
        return td._value // 1000 % 1000000
    return impl


@overload_attribute(PDTimeDeltaType, 'nanoseconds')
def pd_timedelta_get_nanoseconds(td):

    def impl(td):
        return td._value % 1000
    return impl


@register_jitable
def _to_hours_pd_td(td):
    return td._value // (1000 * 1000 * 1000 * 60 * 60) % 24


@register_jitable
def _to_minutes_pd_td(td):
    return td._value // (1000 * 1000 * 1000 * 60) % 60


@register_jitable
def _to_seconds_pd_td(td):
    return td._value // (1000 * 1000 * 1000) % 60


@register_jitable
def _to_milliseconds_pd_td(td):
    return td._value // (1000 * 1000) % 1000


@register_jitable
def _to_microseconds_pd_td(td):
    return td._value // 1000 % 1000


Components = namedtuple('Components', ['days', 'hours', 'minutes',
    'seconds', 'milliseconds', 'microseconds', 'nanoseconds'], defaults=[0,
    0, 0, 0, 0, 0, 0])


@overload_attribute(PDTimeDeltaType, 'components', no_unliteral=True)
def pd_timedelta_get_components(td):

    def impl(td):
        a = Components(td.days, _to_hours_pd_td(td), _to_minutes_pd_td(td),
            _to_seconds_pd_td(td), _to_milliseconds_pd_td(td),
            _to_microseconds_pd_td(td), td.nanoseconds)
        return a
    return impl


@overload_method(PDTimeDeltaType, '__hash__', no_unliteral=True)
def pd_td___hash__(td):

    def impl(td):
        return hash(td._value)
    return impl


@overload_method(PDTimeDeltaType, 'to_numpy', no_unliteral=True)
@overload_method(PDTimeDeltaType, 'to_timedelta64', no_unliteral=True)
def pd_td_to_numpy(td):
    from bodo.hiframes.pd_timestamp_ext import integer_to_timedelta64

    def impl(td):
        return integer_to_timedelta64(td.value)
    return impl


@overload_method(PDTimeDeltaType, 'to_pytimedelta', no_unliteral=True)
def pd_td_to_pytimedelta(td):

    def impl(td):
        return datetime.timedelta(microseconds=np.int64(td._value / 1000))
    return impl


@overload_method(PDTimeDeltaType, 'total_seconds', no_unliteral=True)
def pd_td_total_seconds(td):

    def impl(td):
        return td._value // 1000 / 10 ** 6
    return impl


def overload_add_operator_datetime_timedelta(lhs, rhs):
    if lhs == pd_timedelta_type and rhs == pd_timedelta_type:

        def impl(lhs, rhs):
            val = lhs.value + rhs.value
            return pd.Timedelta(val)
        return impl
    if lhs == pd_timedelta_type and rhs == datetime_timedelta_type:

        def impl(lhs, rhs):
            woor__tvd = (rhs.microseconds + (rhs.seconds + rhs.days * 60 * 
                60 * 24) * 1000 * 1000) * 1000
            val = lhs.value + woor__tvd
            return pd.Timedelta(val)
        return impl
    if lhs == datetime_timedelta_type and rhs == pd_timedelta_type:

        def impl(lhs, rhs):
            qtbs__ocf = (lhs.microseconds + (lhs.seconds + lhs.days * 60 * 
                60 * 24) * 1000 * 1000) * 1000
            val = qtbs__ocf + rhs.value
            return pd.Timedelta(val)
        return impl
    if lhs == pd_timedelta_type and rhs == datetime_datetime_type:
        from bodo.hiframes.pd_timestamp_ext import compute_pd_timestamp

        def impl(lhs, rhs):
            nbach__ycz = rhs.toordinal()
            iru__pykw = rhs.second + rhs.minute * 60 + rhs.hour * 3600
            opgsm__tpa = rhs.microsecond
            eab__rce = lhs.value // 1000
            nir__jiy = lhs.nanoseconds
            tmzf__skohz = opgsm__tpa + eab__rce
            mfx__caag = 1000000 * (nbach__ycz * 86400 + iru__pykw
                ) + tmzf__skohz
            ers__mafcj = nir__jiy
            return compute_pd_timestamp(mfx__caag, ers__mafcj)
        return impl
    if lhs == datetime_datetime_type and rhs == pd_timedelta_type:

        def impl(lhs, rhs):
            return lhs + rhs.to_pytimedelta()
        return impl
    if lhs == datetime_timedelta_type and rhs == datetime_timedelta_type:

        def impl(lhs, rhs):
            d = lhs.days + rhs.days
            s = lhs.seconds + rhs.seconds
            us = lhs.microseconds + rhs.microseconds
            return datetime.timedelta(d, s, us)
        return impl
    if lhs == datetime_timedelta_type and rhs == datetime_datetime_type:

        def impl(lhs, rhs):
            orcta__whq = datetime.timedelta(rhs.toordinal(), hours=rhs.hour,
                minutes=rhs.minute, seconds=rhs.second, microseconds=rhs.
                microsecond)
            orcta__whq = orcta__whq + lhs
            bvd__ctgy, nqg__afr = divmod(orcta__whq.seconds, 3600)
            xccs__wpg, gxyhp__mjur = divmod(nqg__afr, 60)
            if 0 < orcta__whq.days <= _MAXORDINAL:
                d = bodo.hiframes.datetime_date_ext.fromordinal_impl(orcta__whq
                    .days)
                return datetime.datetime(d.year, d.month, d.day, bvd__ctgy,
                    xccs__wpg, gxyhp__mjur, orcta__whq.microseconds)
            raise OverflowError('result out of range')
        return impl
    if lhs == datetime_datetime_type and rhs == datetime_timedelta_type:

        def impl(lhs, rhs):
            orcta__whq = datetime.timedelta(lhs.toordinal(), hours=lhs.hour,
                minutes=lhs.minute, seconds=lhs.second, microseconds=lhs.
                microsecond)
            orcta__whq = orcta__whq + rhs
            bvd__ctgy, nqg__afr = divmod(orcta__whq.seconds, 3600)
            xccs__wpg, gxyhp__mjur = divmod(nqg__afr, 60)
            if 0 < orcta__whq.days <= _MAXORDINAL:
                d = bodo.hiframes.datetime_date_ext.fromordinal_impl(orcta__whq
                    .days)
                return datetime.datetime(d.year, d.month, d.day, bvd__ctgy,
                    xccs__wpg, gxyhp__mjur, orcta__whq.microseconds)
            raise OverflowError('result out of range')
        return impl


def overload_sub_operator_datetime_timedelta(lhs, rhs):
    if lhs == pd_timedelta_type and rhs == pd_timedelta_type:

        def impl(lhs, rhs):
            etibs__fmmca = lhs.value - rhs.value
            return pd.Timedelta(etibs__fmmca)
        return impl
    if lhs == pd_timedelta_type and rhs == datetime_timedelta_type:

        def impl(lhs, rhs):
            return lhs + -rhs
        return impl
    if lhs == datetime_timedelta_type and rhs == pd_timedelta_type:

        def impl(lhs, rhs):
            return lhs + -rhs
        return impl
    if lhs == datetime_datetime_type and rhs == pd_timedelta_type:

        def impl(lhs, rhs):
            return lhs + -rhs
        return impl
    if lhs == datetime_timedelta_type and rhs == datetime_timedelta_type:

        def impl(lhs, rhs):
            d = lhs.days - rhs.days
            s = lhs.seconds - rhs.seconds
            us = lhs.microseconds - rhs.microseconds
            return datetime.timedelta(d, s, us)
        return impl
    if lhs == datetime_datetime_type and rhs == datetime_timedelta_type:

        def impl(lhs, rhs):
            return lhs + -rhs
        return impl
    if lhs == datetime_timedelta_array_type and rhs == datetime_timedelta_type:

        def impl(lhs, rhs):
            sikyy__xuzze = lhs
            numba.parfors.parfor.init_prange()
            n = len(sikyy__xuzze)
            A = alloc_datetime_timedelta_array(n)
            for vfec__gft in numba.parfors.parfor.internal_prange(n):
                A[vfec__gft] = sikyy__xuzze[vfec__gft] - rhs
            return A
        return impl


def overload_mul_operator_timedelta(lhs, rhs):
    if lhs == pd_timedelta_type and isinstance(rhs, types.Integer):

        def impl(lhs, rhs):
            return pd.Timedelta(lhs.value * rhs)
        return impl
    elif isinstance(lhs, types.Integer) and rhs == pd_timedelta_type:

        def impl(lhs, rhs):
            return pd.Timedelta(rhs.value * lhs)
        return impl
    if lhs == datetime_timedelta_type and isinstance(rhs, types.Integer):

        def impl(lhs, rhs):
            d = lhs.days * rhs
            s = lhs.seconds * rhs
            us = lhs.microseconds * rhs
            return datetime.timedelta(d, s, us)
        return impl
    elif isinstance(lhs, types.Integer) and rhs == datetime_timedelta_type:

        def impl(lhs, rhs):
            d = lhs * rhs.days
            s = lhs * rhs.seconds
            us = lhs * rhs.microseconds
            return datetime.timedelta(d, s, us)
        return impl


def overload_floordiv_operator_pd_timedelta(lhs, rhs):
    if lhs == pd_timedelta_type and rhs == pd_timedelta_type:

        def impl(lhs, rhs):
            return lhs.value // rhs.value
        return impl
    elif lhs == pd_timedelta_type and isinstance(rhs, types.Integer):

        def impl(lhs, rhs):
            return pd.Timedelta(lhs.value // rhs)
        return impl


def overload_truediv_operator_pd_timedelta(lhs, rhs):
    if lhs == pd_timedelta_type and rhs == pd_timedelta_type:

        def impl(lhs, rhs):
            return lhs.value / rhs.value
        return impl
    elif lhs == pd_timedelta_type and isinstance(rhs, types.Integer):

        def impl(lhs, rhs):
            return pd.Timedelta(int(lhs.value / rhs))
        return impl


def overload_mod_operator_timedeltas(lhs, rhs):
    if lhs == pd_timedelta_type and rhs == pd_timedelta_type:

        def impl(lhs, rhs):
            return pd.Timedelta(lhs.value % rhs.value)
        return impl
    if lhs == datetime_timedelta_type and rhs == datetime_timedelta_type:

        def impl(lhs, rhs):
            kmu__gnrq = _to_microseconds(lhs) % _to_microseconds(rhs)
            return datetime.timedelta(0, 0, kmu__gnrq)
        return impl


def pd_create_cmp_op_overload(op):

    def overload_pd_timedelta_cmp(lhs, rhs):
        if lhs == pd_timedelta_type and rhs == pd_timedelta_type:

            def impl(lhs, rhs):
                return op(lhs.value, rhs.value)
            return impl
        if lhs == pd_timedelta_type and rhs == bodo.timedelta64ns:
            return lambda lhs, rhs: op(bodo.hiframes.pd_timestamp_ext.
                integer_to_timedelta64(lhs.value), rhs)
        if lhs == bodo.timedelta64ns and rhs == pd_timedelta_type:
            return lambda lhs, rhs: op(lhs, bodo.hiframes.pd_timestamp_ext.
                integer_to_timedelta64(rhs.value))
    return overload_pd_timedelta_cmp


@overload(operator.neg, no_unliteral=True)
def pd_timedelta_neg(lhs):
    if lhs == pd_timedelta_type:

        def impl(lhs):
            return pd.Timedelta(-lhs.value)
        return impl


@overload(operator.pos, no_unliteral=True)
def pd_timedelta_pos(lhs):
    if lhs == pd_timedelta_type:

        def impl(lhs):
            return lhs
        return impl


@overload(divmod, no_unliteral=True)
def pd_timedelta_divmod(lhs, rhs):
    if lhs == pd_timedelta_type and rhs == pd_timedelta_type:

        def impl(lhs, rhs):
            tffg__vax, kmu__gnrq = divmod(lhs.value, rhs.value)
            return tffg__vax, pd.Timedelta(kmu__gnrq)
        return impl


@overload(abs, no_unliteral=True)
def pd_timedelta_abs(lhs):
    if lhs == pd_timedelta_type:

        def impl(lhs):
            if lhs.value < 0:
                return -lhs
            else:
                return lhs
        return impl


class DatetimeTimeDeltaType(types.Type):

    def __init__(self):
        super(DatetimeTimeDeltaType, self).__init__(name=
            'DatetimeTimeDeltaType()')


datetime_timedelta_type = DatetimeTimeDeltaType()


@typeof_impl.register(datetime.timedelta)
def typeof_datetime_timedelta(val, c):
    return datetime_timedelta_type


@register_model(DatetimeTimeDeltaType)
class DatetimeTimeDeltaModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        obuoz__ryvqn = [('days', types.int64), ('seconds', types.int64), (
            'microseconds', types.int64)]
        super(DatetimeTimeDeltaModel, self).__init__(dmm, fe_type, obuoz__ryvqn
            )


@box(DatetimeTimeDeltaType)
def box_datetime_timedelta(typ, val, c):
    btnw__tom = cgutils.create_struct_proxy(typ)(c.context, c.builder,
        value=val)
    thu__nfu = c.pyapi.long_from_longlong(btnw__tom.days)
    hzk__wwg = c.pyapi.long_from_longlong(btnw__tom.seconds)
    jchg__ett = c.pyapi.long_from_longlong(btnw__tom.microseconds)
    pslc__nfnu = c.pyapi.unserialize(c.pyapi.serialize_object(datetime.
        timedelta))
    res = c.pyapi.call_function_objargs(pslc__nfnu, (thu__nfu, hzk__wwg,
        jchg__ett))
    c.pyapi.decref(thu__nfu)
    c.pyapi.decref(hzk__wwg)
    c.pyapi.decref(jchg__ett)
    c.pyapi.decref(pslc__nfnu)
    return res


@unbox(DatetimeTimeDeltaType)
def unbox_datetime_timedelta(typ, val, c):
    thu__nfu = c.pyapi.object_getattr_string(val, 'days')
    hzk__wwg = c.pyapi.object_getattr_string(val, 'seconds')
    jchg__ett = c.pyapi.object_getattr_string(val, 'microseconds')
    dcsv__tqivx = c.pyapi.long_as_longlong(thu__nfu)
    ccdwy__ftjcr = c.pyapi.long_as_longlong(hzk__wwg)
    yse__ggy = c.pyapi.long_as_longlong(jchg__ett)
    btnw__tom = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    btnw__tom.days = dcsv__tqivx
    btnw__tom.seconds = ccdwy__ftjcr
    btnw__tom.microseconds = yse__ggy
    c.pyapi.decref(thu__nfu)
    c.pyapi.decref(hzk__wwg)
    c.pyapi.decref(jchg__ett)
    kos__icv = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(btnw__tom._getvalue(), is_error=kos__icv)


@lower_constant(DatetimeTimeDeltaType)
def lower_constant_datetime_timedelta(context, builder, ty, pyval):
    days = context.get_constant(types.int64, pyval.days)
    seconds = context.get_constant(types.int64, pyval.seconds)
    microseconds = context.get_constant(types.int64, pyval.microseconds)
    return lir.Constant.literal_struct([days, seconds, microseconds])


@overload(datetime.timedelta, no_unliteral=True)
def datetime_timedelta(days=0, seconds=0, microseconds=0, milliseconds=0,
    minutes=0, hours=0, weeks=0):

    def impl_timedelta(days=0, seconds=0, microseconds=0, milliseconds=0,
        minutes=0, hours=0, weeks=0):
        d = s = us = 0
        days += weeks * 7
        seconds += minutes * 60 + hours * 3600
        microseconds += milliseconds * 1000
        d = days
        days, seconds = divmod(seconds, 24 * 3600)
        d += days
        s += int(seconds)
        seconds, us = divmod(microseconds, 1000000)
        days, seconds = divmod(seconds, 24 * 3600)
        d += days
        s += seconds
        return init_timedelta(d, s, us)
    return impl_timedelta


@intrinsic
def init_timedelta(typingctx, d, s, us):

    def codegen(context, builder, signature, args):
        typ = signature.return_type
        timedelta = cgutils.create_struct_proxy(typ)(context, builder)
        timedelta.days = args[0]
        timedelta.seconds = args[1]
        timedelta.microseconds = args[2]
        return timedelta._getvalue()
    return DatetimeTimeDeltaType()(d, s, us), codegen


make_attribute_wrapper(DatetimeTimeDeltaType, 'days', '_days')
make_attribute_wrapper(DatetimeTimeDeltaType, 'seconds', '_seconds')
make_attribute_wrapper(DatetimeTimeDeltaType, 'microseconds', '_microseconds')


@overload_attribute(DatetimeTimeDeltaType, 'days')
def timedelta_get_days(td):

    def impl(td):
        return td._days
    return impl


@overload_attribute(DatetimeTimeDeltaType, 'seconds')
def timedelta_get_seconds(td):

    def impl(td):
        return td._seconds
    return impl


@overload_attribute(DatetimeTimeDeltaType, 'microseconds')
def timedelta_get_microseconds(td):

    def impl(td):
        return td._microseconds
    return impl


@overload_method(DatetimeTimeDeltaType, 'total_seconds', no_unliteral=True)
def total_seconds(td):

    def impl(td):
        return ((td._days * 86400 + td._seconds) * 10 ** 6 + td._microseconds
            ) / 10 ** 6
    return impl


@overload_method(DatetimeTimeDeltaType, '__hash__', no_unliteral=True)
def __hash__(td):

    def impl(td):
        return hash((td._days, td._seconds, td._microseconds))
    return impl


@register_jitable
def _to_nanoseconds(td):
    return np.int64(((td._days * 86400 + td._seconds) * 1000000 + td.
        _microseconds) * 1000)


@register_jitable
def _to_microseconds(td):
    return (td._days * (24 * 3600) + td._seconds) * 1000000 + td._microseconds


@register_jitable
def _cmp(x, y):
    return 0 if x == y else 1 if x > y else -1


@register_jitable
def _getstate(td):
    return td._days, td._seconds, td._microseconds


@register_jitable
def _divide_and_round(a, b):
    tffg__vax, kmu__gnrq = divmod(a, b)
    kmu__gnrq *= 2
    wppbe__uef = kmu__gnrq > b if b > 0 else kmu__gnrq < b
    if wppbe__uef or kmu__gnrq == b and tffg__vax % 2 == 1:
        tffg__vax += 1
    return tffg__vax


_MAXORDINAL = 3652059


def overload_floordiv_operator_dt_timedelta(lhs, rhs):
    if lhs == datetime_timedelta_type and rhs == datetime_timedelta_type:

        def impl(lhs, rhs):
            us = _to_microseconds(lhs)
            return us // _to_microseconds(rhs)
        return impl
    elif lhs == datetime_timedelta_type and rhs == types.int64:

        def impl(lhs, rhs):
            us = _to_microseconds(lhs)
            return datetime.timedelta(0, 0, us // rhs)
        return impl


def overload_truediv_operator_dt_timedelta(lhs, rhs):
    if lhs == datetime_timedelta_type and rhs == datetime_timedelta_type:

        def impl(lhs, rhs):
            us = _to_microseconds(lhs)
            return us / _to_microseconds(rhs)
        return impl
    elif lhs == datetime_timedelta_type and rhs == types.int64:

        def impl(lhs, rhs):
            us = _to_microseconds(lhs)
            return datetime.timedelta(0, 0, _divide_and_round(us, rhs))
        return impl


def create_cmp_op_overload(op):

    def overload_timedelta_cmp(lhs, rhs):
        if lhs == datetime_timedelta_type and rhs == datetime_timedelta_type:

            def impl(lhs, rhs):
                ica__objz = _cmp(_getstate(lhs), _getstate(rhs))
                return op(ica__objz, 0)
            return impl
    return overload_timedelta_cmp


@overload(operator.neg, no_unliteral=True)
def timedelta_neg(lhs):
    if lhs == datetime_timedelta_type:

        def impl(lhs):
            return datetime.timedelta(-lhs.days, -lhs.seconds, -lhs.
                microseconds)
        return impl


@overload(operator.pos, no_unliteral=True)
def timedelta_pos(lhs):
    if lhs == datetime_timedelta_type:

        def impl(lhs):
            return lhs
        return impl


@overload(divmod, no_unliteral=True)
def timedelta_divmod(lhs, rhs):
    if lhs == datetime_timedelta_type and rhs == datetime_timedelta_type:

        def impl(lhs, rhs):
            tffg__vax, kmu__gnrq = divmod(_to_microseconds(lhs),
                _to_microseconds(rhs))
            return tffg__vax, datetime.timedelta(0, 0, kmu__gnrq)
        return impl


@overload(abs, no_unliteral=True)
def timedelta_abs(lhs):
    if lhs == datetime_timedelta_type:

        def impl(lhs):
            if lhs.days < 0:
                return -lhs
            else:
                return lhs
        return impl


@intrinsic
def cast_numpy_timedelta_to_int(typingctx, val=None):
    assert val in (types.NPTimedelta('ns'), types.int64)

    def codegen(context, builder, signature, args):
        return args[0]
    return types.int64(val), codegen


@overload(bool, no_unliteral=True)
def timedelta_to_bool(timedelta):
    if timedelta != datetime_timedelta_type:
        return
    nsm__sfpdh = datetime.timedelta(0)

    def impl(timedelta):
        return timedelta != nsm__sfpdh
    return impl


class DatetimeTimeDeltaArrayType(types.ArrayCompatible):

    def __init__(self):
        super(DatetimeTimeDeltaArrayType, self).__init__(name=
            'DatetimeTimeDeltaArrayType()')

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    @property
    def dtype(self):
        return datetime_timedelta_type

    def copy(self):
        return DatetimeTimeDeltaArrayType()


datetime_timedelta_array_type = DatetimeTimeDeltaArrayType()
types.datetime_timedelta_array_type = datetime_timedelta_array_type
days_data_type = types.Array(types.int64, 1, 'C')
seconds_data_type = types.Array(types.int64, 1, 'C')
microseconds_data_type = types.Array(types.int64, 1, 'C')
nulls_type = types.Array(types.uint8, 1, 'C')


@register_model(DatetimeTimeDeltaArrayType)
class DatetimeTimeDeltaArrayModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        obuoz__ryvqn = [('days_data', days_data_type), ('seconds_data',
            seconds_data_type), ('microseconds_data',
            microseconds_data_type), ('null_bitmap', nulls_type)]
        models.StructModel.__init__(self, dmm, fe_type, obuoz__ryvqn)


make_attribute_wrapper(DatetimeTimeDeltaArrayType, 'days_data', '_days_data')
make_attribute_wrapper(DatetimeTimeDeltaArrayType, 'seconds_data',
    '_seconds_data')
make_attribute_wrapper(DatetimeTimeDeltaArrayType, 'microseconds_data',
    '_microseconds_data')
make_attribute_wrapper(DatetimeTimeDeltaArrayType, 'null_bitmap',
    '_null_bitmap')


@overload_method(DatetimeTimeDeltaArrayType, 'copy', no_unliteral=True)
def overload_datetime_timedelta_arr_copy(A):
    return (lambda A: bodo.hiframes.datetime_timedelta_ext.
        init_datetime_timedelta_array(A._days_data.copy(), A._seconds_data.
        copy(), A._microseconds_data.copy(), A._null_bitmap.copy()))


@unbox(DatetimeTimeDeltaArrayType)
def unbox_datetime_timedelta_array(typ, val, c):
    n = bodo.utils.utils.object_length(c, val)
    ppy__zdbk = types.Array(types.intp, 1, 'C')
    alyg__tnspd = bodo.utils.utils._empty_nd_impl(c.context, c.builder,
        ppy__zdbk, [n])
    llq__ipbl = bodo.utils.utils._empty_nd_impl(c.context, c.builder,
        ppy__zdbk, [n])
    rjqf__zlnvi = bodo.utils.utils._empty_nd_impl(c.context, c.builder,
        ppy__zdbk, [n])
    muks__ejlm = c.builder.udiv(c.builder.add(n, lir.Constant(lir.IntType(
        64), 7)), lir.Constant(lir.IntType(64), 8))
    gehb__ydbp = bodo.utils.utils._empty_nd_impl(c.context, c.builder,
        types.Array(types.uint8, 1, 'C'), [muks__ejlm])
    kro__zdlt = lir.FunctionType(lir.VoidType(), [lir.IntType(8).as_pointer
        (), lir.IntType(64), lir.IntType(64).as_pointer(), lir.IntType(64).
        as_pointer(), lir.IntType(64).as_pointer(), lir.IntType(8).
        as_pointer()])
    bnf__furis = cgutils.get_or_insert_function(c.builder.module, kro__zdlt,
        name='unbox_datetime_timedelta_array')
    c.builder.call(bnf__furis, [val, n, alyg__tnspd.data, llq__ipbl.data,
        rjqf__zlnvi.data, gehb__ydbp.data])
    bfzh__deb = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    bfzh__deb.days_data = alyg__tnspd._getvalue()
    bfzh__deb.seconds_data = llq__ipbl._getvalue()
    bfzh__deb.microseconds_data = rjqf__zlnvi._getvalue()
    bfzh__deb.null_bitmap = gehb__ydbp._getvalue()
    kos__icv = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(bfzh__deb._getvalue(), is_error=kos__icv)


@box(DatetimeTimeDeltaArrayType)
def box_datetime_timedelta_array(typ, val, c):
    sikyy__xuzze = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    alyg__tnspd = c.context.make_array(types.Array(types.int64, 1, 'C'))(c.
        context, c.builder, sikyy__xuzze.days_data)
    llq__ipbl = c.context.make_array(types.Array(types.int64, 1, 'C'))(c.
        context, c.builder, sikyy__xuzze.seconds_data).data
    rjqf__zlnvi = c.context.make_array(types.Array(types.int64, 1, 'C'))(c.
        context, c.builder, sikyy__xuzze.microseconds_data).data
    rvg__cbik = c.context.make_array(types.Array(types.uint8, 1, 'C'))(c.
        context, c.builder, sikyy__xuzze.null_bitmap).data
    n = c.builder.extract_value(alyg__tnspd.shape, 0)
    kro__zdlt = lir.FunctionType(c.pyapi.pyobj, [lir.IntType(64), lir.
        IntType(64).as_pointer(), lir.IntType(64).as_pointer(), lir.IntType
        (64).as_pointer(), lir.IntType(8).as_pointer()])
    ezbgf__nyz = cgutils.get_or_insert_function(c.builder.module, kro__zdlt,
        name='box_datetime_timedelta_array')
    oxwjn__gdsxo = c.builder.call(ezbgf__nyz, [n, alyg__tnspd.data,
        llq__ipbl, rjqf__zlnvi, rvg__cbik])
    c.context.nrt.decref(c.builder, typ, val)
    return oxwjn__gdsxo


@intrinsic
def init_datetime_timedelta_array(typingctx, days_data, seconds_data,
    microseconds_data, nulls=None):
    assert days_data == types.Array(types.int64, 1, 'C')
    assert seconds_data == types.Array(types.int64, 1, 'C')
    assert microseconds_data == types.Array(types.int64, 1, 'C')
    assert nulls == types.Array(types.uint8, 1, 'C')

    def codegen(context, builder, signature, args):
        xsga__jfs, rxa__ywr, rnll__glq, hpn__aepm = args
        vpjt__ywrvo = cgutils.create_struct_proxy(signature.return_type)(
            context, builder)
        vpjt__ywrvo.days_data = xsga__jfs
        vpjt__ywrvo.seconds_data = rxa__ywr
        vpjt__ywrvo.microseconds_data = rnll__glq
        vpjt__ywrvo.null_bitmap = hpn__aepm
        context.nrt.incref(builder, signature.args[0], xsga__jfs)
        context.nrt.incref(builder, signature.args[1], rxa__ywr)
        context.nrt.incref(builder, signature.args[2], rnll__glq)
        context.nrt.incref(builder, signature.args[3], hpn__aepm)
        return vpjt__ywrvo._getvalue()
    ccq__ixgu = datetime_timedelta_array_type(days_data, seconds_data,
        microseconds_data, nulls)
    return ccq__ixgu, codegen


@lower_constant(DatetimeTimeDeltaArrayType)
def lower_constant_datetime_timedelta_arr(context, builder, typ, pyval):
    n = len(pyval)
    alyg__tnspd = np.empty(n, np.int64)
    llq__ipbl = np.empty(n, np.int64)
    rjqf__zlnvi = np.empty(n, np.int64)
    iggs__qpmmd = np.empty(n + 7 >> 3, np.uint8)
    for vfec__gft, s in enumerate(pyval):
        fjqkl__qju = pd.isna(s)
        bodo.libs.int_arr_ext.set_bit_to_arr(iggs__qpmmd, vfec__gft, int(
            not fjqkl__qju))
        if not fjqkl__qju:
            alyg__tnspd[vfec__gft] = s.days
            llq__ipbl[vfec__gft] = s.seconds
            rjqf__zlnvi[vfec__gft] = s.microseconds
    gca__ubx = context.get_constant_generic(builder, days_data_type,
        alyg__tnspd)
    rto__lih = context.get_constant_generic(builder, seconds_data_type,
        llq__ipbl)
    mkeru__mxvl = context.get_constant_generic(builder,
        microseconds_data_type, rjqf__zlnvi)
    ooh__drk = context.get_constant_generic(builder, nulls_type, iggs__qpmmd)
    return lir.Constant.literal_struct([gca__ubx, rto__lih, mkeru__mxvl,
        ooh__drk])


@numba.njit(no_cpython_wrapper=True)
def alloc_datetime_timedelta_array(n):
    alyg__tnspd = np.empty(n, dtype=np.int64)
    llq__ipbl = np.empty(n, dtype=np.int64)
    rjqf__zlnvi = np.empty(n, dtype=np.int64)
    nulls = np.full(n + 7 >> 3, 255, np.uint8)
    return init_datetime_timedelta_array(alyg__tnspd, llq__ipbl,
        rjqf__zlnvi, nulls)


def alloc_datetime_timedelta_array_equiv(self, scope, equiv_set, loc, args, kws
    ):
    assert len(args) == 1 and not kws
    return ArrayAnalysis.AnalyzeResult(shape=args[0], pre=[])


(ArrayAnalysis.
    _analyze_op_call_bodo_hiframes_datetime_timedelta_ext_alloc_datetime_timedelta_array
    ) = alloc_datetime_timedelta_array_equiv


@overload(operator.getitem, no_unliteral=True)
def dt_timedelta_arr_getitem(A, ind):
    if A != datetime_timedelta_array_type:
        return
    if isinstance(ind, types.Integer):

        def impl_int(A, ind):
            return datetime.timedelta(days=A._days_data[ind], seconds=A.
                _seconds_data[ind], microseconds=A._microseconds_data[ind])
        return impl_int
    if ind != bodo.boolean_array and is_list_like_index_type(ind
        ) and ind.dtype == types.bool_:

        def impl_bool(A, ind):
            rku__kseg = bodo.utils.conversion.coerce_to_array(ind)
            bet__buut = A._null_bitmap
            qdjx__flfg = A._days_data[rku__kseg]
            fejc__conkm = A._seconds_data[rku__kseg]
            okj__omqkh = A._microseconds_data[rku__kseg]
            n = len(qdjx__flfg)
            xcshi__bpd = get_new_null_mask_bool_index(bet__buut, ind, n)
            return init_datetime_timedelta_array(qdjx__flfg, fejc__conkm,
                okj__omqkh, xcshi__bpd)
        return impl_bool
    if is_list_like_index_type(ind) and isinstance(ind.dtype, types.Integer):

        def impl(A, ind):
            rku__kseg = bodo.utils.conversion.coerce_to_array(ind)
            bet__buut = A._null_bitmap
            qdjx__flfg = A._days_data[rku__kseg]
            fejc__conkm = A._seconds_data[rku__kseg]
            okj__omqkh = A._microseconds_data[rku__kseg]
            n = len(qdjx__flfg)
            xcshi__bpd = get_new_null_mask_int_index(bet__buut, rku__kseg, n)
            return init_datetime_timedelta_array(qdjx__flfg, fejc__conkm,
                okj__omqkh, xcshi__bpd)
        return impl
    if isinstance(ind, types.SliceType):

        def impl_slice(A, ind):
            n = len(A._days_data)
            bet__buut = A._null_bitmap
            qdjx__flfg = np.ascontiguousarray(A._days_data[ind])
            fejc__conkm = np.ascontiguousarray(A._seconds_data[ind])
            okj__omqkh = np.ascontiguousarray(A._microseconds_data[ind])
            xcshi__bpd = get_new_null_mask_slice_index(bet__buut, ind, n)
            return init_datetime_timedelta_array(qdjx__flfg, fejc__conkm,
                okj__omqkh, xcshi__bpd)
        return impl_slice
    if ind != bodo.boolean_array:
        raise BodoError(
            f'getitem for DatetimeTimedeltaArray with indexing type {ind} not supported.'
            )


@overload(operator.setitem, no_unliteral=True)
def dt_timedelta_arr_setitem(A, ind, val):
    if A != datetime_timedelta_array_type:
        return
    if val == types.none or isinstance(val, types.optional):
        return
    lug__ijhdh = (
        f"setitem for DatetimeTimedeltaArray with indexing type {ind} received an incorrect 'value' type {val}."
        )
    if isinstance(ind, types.Integer):
        if types.unliteral(val) == datetime_timedelta_type:

            def impl(A, ind, val):
                A._days_data[ind] = val._days
                A._seconds_data[ind] = val._seconds
                A._microseconds_data[ind] = val._microseconds
                bodo.libs.int_arr_ext.set_bit_to_arr(A._null_bitmap, ind, 1)
            return impl
        else:
            raise BodoError(lug__ijhdh)
    if not (is_iterable_type(val) and val.dtype == bodo.
        datetime_timedelta_type or types.unliteral(val) ==
        datetime_timedelta_type):
        raise BodoError(lug__ijhdh)
    if is_list_like_index_type(ind) and isinstance(ind.dtype, types.Integer):
        if types.unliteral(val) == datetime_timedelta_type:

            def impl_arr_ind_scalar(A, ind, val):
                n = len(A)
                for vfec__gft in range(n):
                    A._days_data[ind[vfec__gft]] = val._days
                    A._seconds_data[ind[vfec__gft]] = val._seconds
                    A._microseconds_data[ind[vfec__gft]] = val._microseconds
                    bodo.libs.int_arr_ext.set_bit_to_arr(A._null_bitmap,
                        ind[vfec__gft], 1)
            return impl_arr_ind_scalar
        else:

            def impl_arr_ind(A, ind, val):
                val = bodo.utils.conversion.coerce_to_array(val,
                    use_nullable_array=True)
                n = len(val._days_data)
                for vfec__gft in range(n):
                    A._days_data[ind[vfec__gft]] = val._days_data[vfec__gft]
                    A._seconds_data[ind[vfec__gft]] = val._seconds_data[
                        vfec__gft]
                    A._microseconds_data[ind[vfec__gft]
                        ] = val._microseconds_data[vfec__gft]
                    mfg__yxijf = bodo.libs.int_arr_ext.get_bit_bitmap_arr(val
                        ._null_bitmap, vfec__gft)
                    bodo.libs.int_arr_ext.set_bit_to_arr(A._null_bitmap,
                        ind[vfec__gft], mfg__yxijf)
            return impl_arr_ind
    if is_list_like_index_type(ind) and ind.dtype == types.bool_:
        if types.unliteral(val) == datetime_timedelta_type:

            def impl_bool_ind_mask_scalar(A, ind, val):
                n = len(ind)
                for vfec__gft in range(n):
                    if not bodo.libs.array_kernels.isna(ind, vfec__gft
                        ) and ind[vfec__gft]:
                        A._days_data[vfec__gft] = val._days
                        A._seconds_data[vfec__gft] = val._seconds
                        A._microseconds_data[vfec__gft] = val._microseconds
                        bodo.libs.int_arr_ext.set_bit_to_arr(A._null_bitmap,
                            vfec__gft, 1)
            return impl_bool_ind_mask_scalar
        else:

            def impl_bool_ind_mask(A, ind, val):
                val = bodo.utils.conversion.coerce_to_array(val,
                    use_nullable_array=True)
                n = len(ind)
                edawr__obp = 0
                for vfec__gft in range(n):
                    if not bodo.libs.array_kernels.isna(ind, vfec__gft
                        ) and ind[vfec__gft]:
                        A._days_data[vfec__gft] = val._days_data[edawr__obp]
                        A._seconds_data[vfec__gft] = val._seconds_data[
                            edawr__obp]
                        A._microseconds_data[vfec__gft
                            ] = val._microseconds_data[edawr__obp]
                        mfg__yxijf = bodo.libs.int_arr_ext.get_bit_bitmap_arr(
                            val._null_bitmap, edawr__obp)
                        bodo.libs.int_arr_ext.set_bit_to_arr(A._null_bitmap,
                            vfec__gft, mfg__yxijf)
                        edawr__obp += 1
            return impl_bool_ind_mask
    if isinstance(ind, types.SliceType):
        if types.unliteral(val) == datetime_timedelta_type:

            def impl_slice_scalar(A, ind, val):
                lcgm__ojs = numba.cpython.unicode._normalize_slice(ind, len(A))
                for vfec__gft in range(lcgm__ojs.start, lcgm__ojs.stop,
                    lcgm__ojs.step):
                    A._days_data[vfec__gft] = val._days
                    A._seconds_data[vfec__gft] = val._seconds
                    A._microseconds_data[vfec__gft] = val._microseconds
                    bodo.libs.int_arr_ext.set_bit_to_arr(A._null_bitmap,
                        vfec__gft, 1)
            return impl_slice_scalar
        else:

            def impl_slice_mask(A, ind, val):
                val = bodo.utils.conversion.coerce_to_array(val,
                    use_nullable_array=True)
                n = len(A._days_data)
                A._days_data[ind] = val._days_data
                A._seconds_data[ind] = val._seconds_data
                A._microseconds_data[ind] = val._microseconds_data
                igx__ekkw = val._null_bitmap.copy()
                setitem_slice_index_null_bits(A._null_bitmap, igx__ekkw, ind, n
                    )
            return impl_slice_mask
    raise BodoError(
        f'setitem for DatetimeTimedeltaArray with indexing type {ind} not supported.'
        )


@overload(len, no_unliteral=True)
def overload_len_datetime_timedelta_arr(A):
    if A == datetime_timedelta_array_type:
        return lambda A: len(A._days_data)


@overload_attribute(DatetimeTimeDeltaArrayType, 'shape')
def overload_datetime_timedelta_arr_shape(A):
    return lambda A: (len(A._days_data),)


@overload_attribute(DatetimeTimeDeltaArrayType, 'nbytes')
def timedelta_arr_nbytes_overload(A):
    return (lambda A: A._days_data.nbytes + A._seconds_data.nbytes + A.
        _microseconds_data.nbytes + A._null_bitmap.nbytes)


def overload_datetime_timedelta_arr_sub(arg1, arg2):
    if (arg1 == datetime_timedelta_array_type and arg2 ==
        datetime_timedelta_type):

        def impl(arg1, arg2):
            sikyy__xuzze = arg1
            numba.parfors.parfor.init_prange()
            n = len(sikyy__xuzze)
            A = alloc_datetime_timedelta_array(n)
            for vfec__gft in numba.parfors.parfor.internal_prange(n):
                A[vfec__gft] = sikyy__xuzze[vfec__gft] - arg2
            return A
        return impl


def create_cmp_op_overload_arr(op):

    def overload_date_arr_cmp(lhs, rhs):
        if op == operator.ne:
            ipa__tpy = True
        else:
            ipa__tpy = False
        if (lhs == datetime_timedelta_array_type and rhs ==
            datetime_timedelta_array_type):

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                n = len(lhs)
                bxx__madtc = bodo.libs.bool_arr_ext.alloc_bool_array(n)
                for vfec__gft in numba.parfors.parfor.internal_prange(n):
                    asb__rega = bodo.libs.array_kernels.isna(lhs, vfec__gft)
                    vthv__vwsd = bodo.libs.array_kernels.isna(rhs, vfec__gft)
                    if asb__rega or vthv__vwsd:
                        qybjo__gmhf = ipa__tpy
                    else:
                        qybjo__gmhf = op(lhs[vfec__gft], rhs[vfec__gft])
                    bxx__madtc[vfec__gft] = qybjo__gmhf
                return bxx__madtc
            return impl
        elif lhs == datetime_timedelta_array_type:

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                n = len(lhs)
                bxx__madtc = bodo.libs.bool_arr_ext.alloc_bool_array(n)
                for vfec__gft in numba.parfors.parfor.internal_prange(n):
                    mfg__yxijf = bodo.libs.array_kernels.isna(lhs, vfec__gft)
                    if mfg__yxijf:
                        qybjo__gmhf = ipa__tpy
                    else:
                        qybjo__gmhf = op(lhs[vfec__gft], rhs)
                    bxx__madtc[vfec__gft] = qybjo__gmhf
                return bxx__madtc
            return impl
        elif rhs == datetime_timedelta_array_type:

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                n = len(rhs)
                bxx__madtc = bodo.libs.bool_arr_ext.alloc_bool_array(n)
                for vfec__gft in numba.parfors.parfor.internal_prange(n):
                    mfg__yxijf = bodo.libs.array_kernels.isna(rhs, vfec__gft)
                    if mfg__yxijf:
                        qybjo__gmhf = ipa__tpy
                    else:
                        qybjo__gmhf = op(lhs, rhs[vfec__gft])
                    bxx__madtc[vfec__gft] = qybjo__gmhf
                return bxx__madtc
            return impl
    return overload_date_arr_cmp


timedelta_unsupported_attrs = ['asm8', 'resolution_string', 'freq',
    'is_populated']
timedelta_unsupported_methods = ['isoformat']


def _intstall_pd_timedelta_unsupported():
    from bodo.utils.typing import create_unsupported_overload
    for hdh__pqmmn in timedelta_unsupported_attrs:
        zsvgt__ehl = 'pandas.Timedelta.' + hdh__pqmmn
        overload_attribute(PDTimeDeltaType, hdh__pqmmn)(
            create_unsupported_overload(zsvgt__ehl))
    for gwyzq__utiw in timedelta_unsupported_methods:
        zsvgt__ehl = 'pandas.Timedelta.' + gwyzq__utiw
        overload_method(PDTimeDeltaType, gwyzq__utiw)(
            create_unsupported_overload(zsvgt__ehl + '()'))


_intstall_pd_timedelta_unsupported()
