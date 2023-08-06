"""
Implements datetime array kernels that are specific to BodoSQL
"""
import numba
import numpy as np
import pandas as pd
import pytz
from numba.core import types
from numba.extending import overload, register_jitable
import bodo
from bodo.libs.bodosql_array_kernel_utils import *
from bodo.utils.typing import raise_bodo_error


def standardize_snowflake_date_time_part(part_str):
    pass


@overload(standardize_snowflake_date_time_part)
def overload_standardize_snowflake_date_time_part(part_str):
    cceyl__boi = pd.array(['year', 'y', 'yy', 'yyy', 'yyyy', 'yr', 'years',
        'yrs'])
    soc__dfm = pd.array(['month', 'mm', 'mon', 'mons', 'months'])
    qzwd__yxfm = pd.array(['day', 'd', 'dd', 'days', 'dayofmonth'])
    wfm__peg = pd.array(['dayofweek', 'weekday', 'dow', 'dw'])
    pdn__rsbdi = pd.array(['week', 'w', 'wk', 'weekofyear', 'woy', 'wy'])
    vpmg__esb = pd.array(['weekiso', 'week_iso', 'weekofyeariso',
        'weekofyear_iso'])
    axf__vcfn = pd.array(['quarter', 'q', 'qtr', 'qtrs', 'quarters'])
    qex__woduo = pd.array(['hour', 'h', 'hh', 'hr', 'hours', 'hrs'])
    nky__onjwy = pd.array(['minute', 'm', 'mi', 'min', 'minutes', 'mins'])
    inkt__gorgi = pd.array(['second', 's', 'sec', 'seconds', 'secs'])
    gljkv__svi = pd.array(['millisecond', 'ms', 'msec', 'milliseconds'])
    azxo__djcp = pd.array(['microsecond', 'us', 'usec', 'microseconds'])
    tyqgm__enor = pd.array(['nanosecond', 'ns', 'nsec', 'nanosec',
        'nsecond', 'nanoseconds', 'nanosecs', 'nseconds'])
    nmdl__rdyap = pd.array(['epoch_second', 'epoch', 'epoch_seconds'])
    boio__epeab = pd.array(['epoch_millisecond', 'epoch_milliseconds'])
    bzayw__cixgd = pd.array(['epoch_microsecond', 'epoch_microseconds'])
    vhg__nxzs = pd.array(['epoch_nanosecond', 'epoch_nanoseconds'])
    omgi__snvmk = pd.array(['timezone_hour', 'tzh'])
    oaf__szhre = pd.array(['timezone_minute', 'tzm'])
    xepo__hod = pd.array(['yearofweek', 'yearofweekiso'])

    def impl(part_str):
        part_str = part_str.lower()
        if part_str in cceyl__boi:
            return 'year'
        elif part_str in soc__dfm:
            return 'month'
        elif part_str in qzwd__yxfm:
            return 'day'
        elif part_str in wfm__peg:
            return 'dayofweek'
        elif part_str in pdn__rsbdi:
            return 'week'
        elif part_str in vpmg__esb:
            return 'weekiso'
        elif part_str in axf__vcfn:
            return 'quarter'
        elif part_str in qex__woduo:
            return 'hour'
        elif part_str in nky__onjwy:
            return 'minute'
        elif part_str in inkt__gorgi:
            return 'second'
        elif part_str in gljkv__svi:
            return 'millisecond'
        elif part_str in azxo__djcp:
            return 'microsecond'
        elif part_str in tyqgm__enor:
            return 'nanosecond'
        elif part_str in nmdl__rdyap:
            return 'epoch_second'
        elif part_str in boio__epeab:
            return 'epoch_millisecond'
        elif part_str in bzayw__cixgd:
            return 'epoch_microsecond'
        elif part_str in vhg__nxzs:
            return 'epoch_nanosecond'
        elif part_str in omgi__snvmk:
            return 'timezone_hour'
        elif part_str in oaf__szhre:
            return 'timezone_minute'
        elif part_str in xepo__hod:
            return part_str
        else:
            raise ValueError(
                'Invalid date or time part passed into Snowflake array kernel')
    return impl


@numba.generated_jit(nopython=True)
def add_interval(start_dt, interval):
    args = [start_dt, interval]
    for xadjc__qjs in range(len(args)):
        if isinstance(args[xadjc__qjs], types.optional):
            return unopt_argument(
                'bodo.libs.bodosql_array_kernels.add_interval_util', ['arr'
                ], xadjc__qjs)

    def impl(start_dt, interval):
        return add_interval_util(start_dt, interval)
    return impl


def add_interval_years(amount, start_dt):
    return


def add_interval_quarters(amount, start_dt):
    return


def add_interval_months(amount, start_dt):
    return


def add_interval_weeks(amount, start_dt):
    return


def add_interval_days(amount, start_dt):
    return


def add_interval_hours(amount, start_dt):
    return


def add_interval_minutes(amount, start_dt):
    return


def add_interval_seconds(amount, start_dt):
    return


def add_interval_milliseconds(amount, start_dt):
    return


def add_interval_microseconds(amount, start_dt):
    return


def add_interval_nanoseconds(amount, start_dt):
    return


@numba.generated_jit(nopython=True)
def dayname(arr):
    if isinstance(arr, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.dayname_util',
            ['arr'], 0)

    def impl(arr):
        return dayname_util(arr)
    return impl


def dayofmonth(arr):
    return


def dayofweek(arr):
    return


def dayofweekiso(arr):
    return


def dayofyear(arr):
    return


def diff_day(arr0, arr1):
    return


def diff_hour(arr0, arr1):
    return


def diff_microsecond(arr0, arr1):
    return


def diff_minute(arr0, arr1):
    return


def diff_month(arr0, arr1):
    return


def diff_nanosecond(arr0, arr1):
    return


def diff_quarter(arr0, arr1):
    return


def diff_second(arr0, arr1):
    return


def diff_week(arr0, arr1):
    return


def diff_year(arr0, arr1):
    return


def get_year(arr):
    return


def get_quarter(arr):
    return


def get_month(arr):
    return


def get_week(arr):
    return


def get_hour(arr):
    return


def get_minute(arr):
    return


def get_second(arr):
    return


def get_millisecond(arr):
    return


def get_microsecond(arr):
    return


def get_nanosecond(arr):
    return


@numba.generated_jit(nopython=True)
def int_to_days(arr):
    if isinstance(arr, types.optional):
        return unopt_argument(
            'bodo.libs.bodosql_array_kernels.int_to_days_util', ['arr'], 0)

    def impl(arr):
        return int_to_days_util(arr)
    return impl


@numba.generated_jit(nopython=True)
def last_day(arr):
    if isinstance(arr, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.last_day_util',
            ['arr'], 0)

    def impl(arr):
        return last_day_util(arr)
    return impl


@numba.generated_jit(nopython=True)
def makedate(year, day):
    args = [year, day]
    for xadjc__qjs in range(2):
        if isinstance(args[xadjc__qjs], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.makedate',
                ['year', 'day'], xadjc__qjs)

    def impl(year, day):
        return makedate_util(year, day)
    return impl


@numba.generated_jit(nopython=True)
def monthname(arr):
    if isinstance(arr, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.monthname_util',
            ['arr'], 0)

    def impl(arr):
        return monthname_util(arr)
    return impl


@numba.generated_jit(nopython=True)
def next_day(arr0, arr1):
    args = [arr0, arr1]
    for xadjc__qjs in range(2):
        if isinstance(args[xadjc__qjs], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.next_day',
                ['arr0', 'arr1'], xadjc__qjs)

    def impl(arr0, arr1):
        return next_day_util(arr0, arr1)
    return impl


@numba.generated_jit(nopython=True)
def previous_day(arr0, arr1):
    args = [arr0, arr1]
    for xadjc__qjs in range(2):
        if isinstance(args[xadjc__qjs], types.optional):
            return unopt_argument(
                'bodo.libs.bodosql_array_kernels.previous_day', ['arr0',
                'arr1'], xadjc__qjs)

    def impl(arr0, arr1):
        return previous_day_util(arr0, arr1)
    return impl


@numba.generated_jit(nopython=True)
def second_timestamp(arr):
    if isinstance(arr, types.optional):
        return unopt_argument(
            'bodo.libs.bodosql_array_kernels.second_timestamp_util', ['arr'], 0
            )

    def impl(arr):
        return second_timestamp_util(arr)
    return impl


@numba.generated_jit(nopython=True)
def weekday(arr):
    if isinstance(arr, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.weekday_util',
            ['arr'], 0)

    def impl(arr):
        return weekday_util(arr)
    return impl


@numba.generated_jit(nopython=True)
def yearofweekiso(arr):
    if isinstance(arr, types.optional):
        return unopt_argument(
            'bodo.libs.bodosql_array_kernels.yearofweekiso_util', ['arr'], 0)

    def impl(arr):
        return yearofweekiso_util(arr)
    return impl


@numba.generated_jit(nopython=True)
def add_interval_util(start_dt, interval):
    verify_datetime_arg_allow_tz(start_dt, 'add_interval', 'start_dt')
    ehdv__fac = get_tz_if_exists(start_dt)
    koye__cgie = ['start_dt', 'interval']
    had__nprad = [start_dt, interval]
    ropf__myt = [True] * 2
    nql__qghjk = ''
    knev__pux = bodo.utils.utils.is_array_typ(interval, True
        ) or bodo.utils.utils.is_array_typ(start_dt, True)
    kqo__buuy = None
    if ehdv__fac is not None:
        if bodo.hiframes.pd_offsets_ext.tz_has_transition_times(ehdv__fac):
            bvv__pfmiq = pytz.timezone(ehdv__fac)
            ays__vmame = np.array(bvv__pfmiq._utc_transition_times, dtype=
                'M8[ns]').view('i8')
            sjzzu__rvag = np.array(bvv__pfmiq._transition_info)[:, 0]
            sjzzu__rvag = (pd.Series(sjzzu__rvag).dt.total_seconds() * 
                1000000000).astype(np.int64).values
            kqo__buuy = {'trans': ays__vmame, 'deltas': sjzzu__rvag}
            nql__qghjk += f'start_value = arg0.value\n'
            nql__qghjk += 'end_value = start_value + arg0.value\n'
            nql__qghjk += (
                "start_trans = np.searchsorted(trans, start_value, side='right') - 1\n"
                )
            nql__qghjk += (
                "end_trans = np.searchsorted(trans, end_value, side='right') - 1\n"
                )
            nql__qghjk += 'offset = deltas[start_trans] - deltas[end_trans]\n'
            nql__qghjk += 'arg1 = pd.Timedelta(arg1.value + offset)\n'
        nql__qghjk += f'res[i] = arg0 + arg1\n'
        swc__xdqk = bodo.DatetimeArrayType(ehdv__fac)
    else:
        rkqd__jojgu = ('bodo.utils.conversion.unbox_if_tz_naive_timestamp' if
            knev__pux else '')
        jpx__ljyj = 'bodo.utils.conversion.box_if_dt64' if knev__pux else ''
        nql__qghjk = f'res[i] = {rkqd__jojgu}({jpx__ljyj}(arg0) + arg1)\n'
        swc__xdqk = types.Array(bodo.datetime64ns, 1, 'C')
    return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
        swc__xdqk, extra_globals=kqo__buuy)


def add_interval_years_util(amount, start_dt):
    return


def add_interval_quarters_util(amount, start_dt):
    return


def add_interval_months_util(amount, start_dt):
    return


def add_interval_weeks_util(amount, start_dt):
    return


def add_interval_days_util(amount, start_dt):
    return


def add_interval_hours_util(amount, start_dt):
    return


def add_interval_minutes_util(amount, start_dt):
    return


def add_interval_seconds_util(amount, start_dt):
    return


def add_interval_milliseconds_util(amount, start_dt):
    return


def add_interval_microseconds_util(amount, start_dt):
    return


def add_interval_nanoseconds_util(amount, start_dt):
    return


def create_add_interval_func_overload(unit):

    def overload_func(amount, start_dt):
        args = [amount, start_dt]
        for xadjc__qjs in range(2):
            if isinstance(args[xadjc__qjs], types.optional):
                return unopt_argument(
                    f'bodo.libs.bodosql_array_kernels.add_interval_{unit}',
                    ['amount', 'start_dt'], xadjc__qjs)
        muh__wlbxr = 'def impl(amount, start_dt):\n'
        muh__wlbxr += (
            f'  return bodo.libs.bodosql_array_kernels.add_interval_{unit}_util(amount, start_dt)'
            )
        gjob__xec = {}
        exec(muh__wlbxr, {'bodo': bodo}, gjob__xec)
        return gjob__xec['impl']
    return overload_func


def create_add_interval_util_overload(unit):

    def overload_add_datetime_interval_util(amount, start_dt):
        verify_int_arg(amount, 'add_interval_' + unit, 'amount')
        if unit in ('hours', 'minutes', 'seconds', 'milliseconds',
            'microseconds', 'nanoseconds'):
            verify_time_or_datetime_arg_allow_tz(start_dt, 'add_interval_' +
                unit, 'start_dt')
        else:
            verify_datetime_arg_allow_tz(start_dt, 'add_interval_' + unit,
                'start_dt')
        ehdv__fac = get_tz_if_exists(start_dt)
        koye__cgie = ['amount', 'start_dt']
        had__nprad = [amount, start_dt]
        ropf__myt = [True] * 2
        knev__pux = bodo.utils.utils.is_array_typ(amount, True
            ) or bodo.utils.utils.is_array_typ(start_dt, True)
        kqo__buuy = None
        if is_valid_time_arg(start_dt):
            vvgd__kar = start_dt.precision
            if unit == 'hours':
                ucups__tuoj = 3600000000000
            elif unit == 'minutes':
                ucups__tuoj = 60000000000
            elif unit == 'seconds':
                ucups__tuoj = 1000000000
            elif unit == 'milliseconds':
                vvgd__kar = max(vvgd__kar, 3)
                ucups__tuoj = 1000000
            elif unit == 'microseconds':
                vvgd__kar = max(vvgd__kar, 6)
                ucups__tuoj = 1000
            elif unit == 'nanoseconds':
                vvgd__kar = max(vvgd__kar, 9)
                ucups__tuoj = 1
            nql__qghjk = f"""amt = bodo.hiframes.time_ext.cast_time_to_int(arg1) + {ucups__tuoj} * arg0
"""
            nql__qghjk += (
                f'res[i] = bodo.hiframes.time_ext.cast_int_to_time(amt % 86400000000000, precision={vvgd__kar})'
                )
            swc__xdqk = types.Array(bodo.hiframes.time_ext.TimeType(
                vvgd__kar), 1, 'C')
        elif ehdv__fac is not None:
            if bodo.hiframes.pd_offsets_ext.tz_has_transition_times(ehdv__fac):
                bvv__pfmiq = pytz.timezone(ehdv__fac)
                ays__vmame = np.array(bvv__pfmiq._utc_transition_times,
                    dtype='M8[ns]').view('i8')
                sjzzu__rvag = np.array(bvv__pfmiq._transition_info)[:, 0]
                sjzzu__rvag = (pd.Series(sjzzu__rvag).dt.total_seconds() * 
                    1000000000).astype(np.int64).values
                kqo__buuy = {'trans': ays__vmame, 'deltas': sjzzu__rvag}
            if unit in ('months', 'quarters', 'years'):
                if unit == 'quarters':
                    nql__qghjk = f'td = pd.DateOffset(months=3*arg0)\n'
                else:
                    nql__qghjk = f'td = pd.DateOffset({unit}=arg0)\n'
                nql__qghjk += f'start_value = arg1.value\n'
                nql__qghjk += (
                    'end_value = (pd.Timestamp(arg1.value) + td).value\n')
                if bodo.hiframes.pd_offsets_ext.tz_has_transition_times(
                    ehdv__fac):
                    nql__qghjk += """start_trans = np.searchsorted(trans, start_value, side='right') - 1
"""
                    nql__qghjk += """end_trans = np.searchsorted(trans, end_value, side='right') - 1
"""
                    nql__qghjk += (
                        'offset = deltas[start_trans] - deltas[end_trans]\n')
                    nql__qghjk += (
                        'td = pd.Timedelta(end_value - start_value + offset)\n'
                        )
                else:
                    nql__qghjk += (
                        'td = pd.Timedelta(end_value - start_value)\n')
            else:
                if unit == 'nanoseconds':
                    nql__qghjk = 'td = pd.Timedelta(arg0)\n'
                else:
                    nql__qghjk = f'td = pd.Timedelta({unit}=arg0)\n'
                if bodo.hiframes.pd_offsets_ext.tz_has_transition_times(
                    ehdv__fac):
                    nql__qghjk += f'start_value = arg1.value\n'
                    nql__qghjk += 'end_value = start_value + td.value\n'
                    nql__qghjk += """start_trans = np.searchsorted(trans, start_value, side='right') - 1
"""
                    nql__qghjk += """end_trans = np.searchsorted(trans, end_value, side='right') - 1
"""
                    nql__qghjk += (
                        'offset = deltas[start_trans] - deltas[end_trans]\n')
                    nql__qghjk += 'td = pd.Timedelta(td.value + offset)\n'
            nql__qghjk += f'res[i] = arg1 + td\n'
            swc__xdqk = bodo.DatetimeArrayType(ehdv__fac)
        else:
            rkqd__jojgu = (
                'bodo.utils.conversion.unbox_if_tz_naive_timestamp' if
                knev__pux else '')
            jpx__ljyj = ('bodo.utils.conversion.box_if_dt64' if knev__pux else
                '')
            if unit in ('months', 'years'):
                nql__qghjk = f"""res[i] = {rkqd__jojgu}({jpx__ljyj}(arg1) + pd.DateOffset({unit}=arg0))
"""
            elif unit == 'quarters':
                nql__qghjk = f"""res[i] = {rkqd__jojgu}({jpx__ljyj}(arg1) + pd.DateOffset(months=3*arg0))
"""
            elif unit == 'nanoseconds':
                nql__qghjk = (
                    f'res[i] = {rkqd__jojgu}({jpx__ljyj}(arg1) + pd.Timedelta(arg0))\n'
                    )
            else:
                nql__qghjk = f"""res[i] = {rkqd__jojgu}({jpx__ljyj}(arg1) + pd.Timedelta({unit}=arg0))
"""
            swc__xdqk = types.Array(bodo.datetime64ns, 1, 'C')
        return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
            swc__xdqk, extra_globals=kqo__buuy)
    return overload_add_datetime_interval_util


def _install_add_interval_overload():
    yuaq__jxwtm = [('years', add_interval_years, add_interval_years_util),
        ('quarters', add_interval_quarters, add_interval_quarters_util), (
        'months', add_interval_months, add_interval_months_util), ('weeks',
        add_interval_weeks, add_interval_weeks_util), ('days',
        add_interval_days, add_interval_days_util), ('hours',
        add_interval_hours, add_interval_hours_util), ('minutes',
        add_interval_minutes, add_interval_minutes_util), ('seconds',
        add_interval_seconds, add_interval_seconds_util), ('milliseconds',
        add_interval_milliseconds, add_interval_milliseconds_util), (
        'microseconds', add_interval_microseconds,
        add_interval_microseconds_util), ('nanoseconds',
        add_interval_nanoseconds, add_interval_nanoseconds_util)]
    for unit, xbh__impx, cywum__xlla in yuaq__jxwtm:
        gqyjp__xjg = create_add_interval_func_overload(unit)
        overload(xbh__impx)(gqyjp__xjg)
        nedh__mvf = create_add_interval_util_overload(unit)
        overload(cywum__xlla)(nedh__mvf)


_install_add_interval_overload()


def dayofmonth_util(arr):
    return


def dayofweek_util(arr):
    return


def dayofweekiso_util(arr):
    return


def dayofyear_util(arr):
    return


def get_year_util(arr):
    return


def get_quarter_util(arr):
    return


def get_month_util(arr):
    return


def get_week_util(arr):
    return


def get_hour_util(arr):
    return


def get_minute_util(arr):
    return


def get_second_util(arr):
    return


def get_millisecond_util(arr):
    return


def get_microsecond_util(arr):
    return


def get_nanosecond_util(arr):
    return


def create_dt_extract_fn_overload(fn_name):

    def overload_func(arr):
        if isinstance(arr, types.optional):
            return unopt_argument(f'bodo.libs.bodosql_array_kernels.{fn_name}',
                ['arr'], 0)
        muh__wlbxr = 'def impl(arr):\n'
        muh__wlbxr += (
            f'  return bodo.libs.bodosql_array_kernels.{fn_name}_util(arr)')
        gjob__xec = {}
        exec(muh__wlbxr, {'bodo': bodo}, gjob__xec)
        return gjob__xec['impl']
    return overload_func


def create_dt_extract_fn_util_overload(fn_name):

    def overload_dt_extract_fn(arr):
        if fn_name in ('get_hour', 'get_minute', 'get_second',
            'get_microsecond', 'get_millisecond', 'get_nanosecond'):
            verify_time_or_datetime_arg_allow_tz(arr, fn_name, 'arr')
        else:
            verify_datetime_arg_allow_tz(arr, fn_name, 'arr')
        dkrd__cigss = get_tz_if_exists(arr)
        jpx__ljyj = ('bodo.utils.conversion.box_if_dt64' if dkrd__cigss is
            None else '')
        miv__wxnp = 'microsecond // 1000' if not is_valid_time_arg(arr
            ) else 'millisecond'
        rhq__ihk = {'get_year': f'{jpx__ljyj}(arg0).year', 'get_quarter':
            f'{jpx__ljyj}(arg0).quarter', 'get_month':
            f'{jpx__ljyj}(arg0).month', 'get_week':
            f'{jpx__ljyj}(arg0).week', 'get_hour':
            f'{jpx__ljyj}(arg0).hour', 'get_minute':
            f'{jpx__ljyj}(arg0).minute', 'get_second':
            f'{jpx__ljyj}(arg0).second', 'get_millisecond':
            f'{jpx__ljyj}(arg0).{miv__wxnp}', 'get_microsecond':
            f'{jpx__ljyj}(arg0).microsecond', 'get_nanosecond':
            f'{jpx__ljyj}(arg0).nanosecond', 'dayofmonth':
            f'{jpx__ljyj}(arg0).day', 'dayofweek':
            f'({jpx__ljyj}(arg0).dayofweek + 1) % 7', 'dayofweekiso':
            f'{jpx__ljyj}(arg0).dayofweek + 1', 'dayofyear':
            f'{jpx__ljyj}(arg0).dayofyear'}
        koye__cgie = ['arr']
        had__nprad = [arr]
        ropf__myt = [True]
        nql__qghjk = f'res[i] = {rhq__ihk[fn_name]}'
        swc__xdqk = bodo.libs.int_arr_ext.IntegerArrayType(types.int64)
        return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
            swc__xdqk)
    return overload_dt_extract_fn


def _install_dt_extract_fn_overload():
    yuaq__jxwtm = [('get_year', get_year, get_year_util), ('get_quarter',
        get_quarter, get_quarter_util), ('get_month', get_month,
        get_month_util), ('get_week', get_week, get_week_util), ('get_hour',
        get_hour, get_hour_util), ('get_minute', get_minute,
        get_minute_util), ('get_second', get_second, get_second_util), (
        'get_millisecond', get_millisecond, get_millisecond_util), (
        'get_microsecond', get_microsecond, get_microsecond_util), (
        'get_nanosecond', get_nanosecond, get_nanosecond_util), (
        'dayofmonth', dayofmonth, dayofmonth_util), ('dayofweek', dayofweek,
        dayofweek_util), ('dayofweekiso', dayofweekiso, dayofweekiso_util),
        ('dayofyear', dayofyear, dayofyear_util)]
    for fn_name, xbh__impx, cywum__xlla in yuaq__jxwtm:
        gqyjp__xjg = create_dt_extract_fn_overload(fn_name)
        overload(xbh__impx)(gqyjp__xjg)
        nedh__mvf = create_dt_extract_fn_util_overload(fn_name)
        overload(cywum__xlla)(nedh__mvf)


_install_dt_extract_fn_overload()


def diff_day_util(arr0, arr1):
    return


def diff_hour_util(arr0, arr1):
    return


def diff_microsecond_util(arr0, arr1):
    return


def diff_minute_util(arr0, arr1):
    return


def diff_month_util(arr0, arr1):
    return


def diff_nanosecond_util(arr0, arr1):
    return


def diff_quarter_util(arr0, arr1):
    return


def diff_second_util(arr0, arr1):
    return


def diff_week_util(arr0, arr1):
    return


def diff_year_util(arr0, arr1):
    return


@register_jitable
def get_iso_weeks_between_years(year0, year1):
    pizoz__mbh = 1
    if year1 < year0:
        year0, year1 = year1, year0
        pizoz__mbh = -1
    ebztb__jczza = 0
    for xljzh__mfbu in range(year0, year1):
        ebztb__jczza += 52
        onkf__plg = (xljzh__mfbu + xljzh__mfbu // 4 - xljzh__mfbu // 100 + 
            xljzh__mfbu // 400) % 7
        heeta__mke = (xljzh__mfbu - 1 + (xljzh__mfbu - 1) // 4 - (
            xljzh__mfbu - 1) // 100 + (xljzh__mfbu - 1) // 400) % 7
        if onkf__plg == 4 or heeta__mke == 3:
            ebztb__jczza += 1
    return pizoz__mbh * ebztb__jczza


def create_dt_diff_fn_overload(unit):

    def overload_func(arr0, arr1):
        args = [arr0, arr1]
        for xadjc__qjs in range(len(args)):
            if isinstance(args[xadjc__qjs], types.optional):
                return unopt_argument(
                    f'bodo.libs.bodosql_array_kernels.diff_{unit}', ['arr0',
                    'arr1'], xadjc__qjs)
        muh__wlbxr = 'def impl(arr0, arr1):\n'
        muh__wlbxr += (
            f'  return bodo.libs.bodosql_array_kernels.diff_{unit}_util(arr0, arr1)'
            )
        gjob__xec = {}
        exec(muh__wlbxr, {'bodo': bodo}, gjob__xec)
        return gjob__xec['impl']
    return overload_func


def create_dt_diff_fn_util_overload(unit):

    def overload_dt_diff_fn(arr0, arr1):
        verify_datetime_arg_allow_tz(arr0, 'diff_' + unit, 'arr0')
        verify_datetime_arg_allow_tz(arr1, 'diff_' + unit, 'arr1')
        dkrd__cigss = get_tz_if_exists(arr0)
        if get_tz_if_exists(arr1) != dkrd__cigss:
            raise_bodo_error(
                f'diff_{unit}: both arguments must have the same timezone')
        koye__cgie = ['arr0', 'arr1']
        had__nprad = [arr0, arr1]
        ropf__myt = [True] * 2
        kqo__buuy = None
        cusox__agnm = {'yr_diff': 'arg1.year - arg0.year', 'qu_diff':
            'arg1.quarter - arg0.quarter', 'mo_diff':
            'arg1.month - arg0.month', 'y0, w0, _': 'arg0.isocalendar()',
            'y1, w1, _': 'arg1.isocalendar()', 'iso_yr_diff':
            'bodo.libs.bodosql_array_kernels.get_iso_weeks_between_years(y0, y1)'
            , 'wk_diff': 'w1 - w0', 'da_diff':
            '(pd.Timestamp(arg1.year, arg1.month, arg1.day) - pd.Timestamp(arg0.year, arg0.month, arg0.day)).days'
            , 'ns_diff': 'arg1.value - arg0.value'}
        xxups__mawn = {'year': ['yr_diff'], 'quarter': ['yr_diff',
            'qu_diff'], 'month': ['yr_diff', 'mo_diff'], 'week': [
            'y0, w0, _', 'y1, w1, _', 'iso_yr_diff', 'wk_diff'], 'day': [
            'da_diff'], 'nanosecond': ['ns_diff']}
        nql__qghjk = ''
        if dkrd__cigss == None:
            nql__qghjk += 'arg0 = bodo.utils.conversion.box_if_dt64(arg0)\n'
            nql__qghjk += 'arg1 = bodo.utils.conversion.box_if_dt64(arg1)\n'
        for emwt__nmmr in xxups__mawn.get(unit, []):
            nql__qghjk += f'{emwt__nmmr} = {cusox__agnm[emwt__nmmr]}\n'
        if unit == 'nanosecond':
            swc__xdqk = bodo.libs.int_arr_ext.IntegerArrayType(types.int64)
        else:
            swc__xdqk = bodo.libs.int_arr_ext.IntegerArrayType(types.int32)
        if unit == 'year':
            nql__qghjk += 'res[i] = yr_diff'
        elif unit == 'quarter':
            nql__qghjk += 'res[i] = 4 * yr_diff + qu_diff'
        elif unit == 'month':
            nql__qghjk += 'res[i] = 12 * yr_diff + mo_diff'
        elif unit == 'week':
            nql__qghjk += 'res[i] = iso_yr_diff + wk_diff'
        elif unit == 'day':
            nql__qghjk += 'res[i] = da_diff'
        elif unit == 'nanosecond':
            nql__qghjk += 'res[i] = ns_diff'
        else:
            if unit == 'hour':
                lcen__rpatf = 3600000000000
            if unit == 'minute':
                lcen__rpatf = 60000000000
            if unit == 'second':
                lcen__rpatf = 1000000000
            if unit == 'microsecond':
                lcen__rpatf = 1000
            nql__qghjk += f"""res[i] = np.floor_divide((arg1.value), ({lcen__rpatf})) - np.floor_divide((arg0.value), ({lcen__rpatf}))
"""
        return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
            swc__xdqk, extra_globals=kqo__buuy)
    return overload_dt_diff_fn


def _install_dt_diff_fn_overload():
    yuaq__jxwtm = [('day', diff_day, diff_day_util), ('hour', diff_hour,
        diff_hour_util), ('microsecond', diff_microsecond,
        diff_microsecond_util), ('minute', diff_minute, diff_minute_util),
        ('month', diff_month, diff_month_util), ('nanosecond',
        diff_nanosecond, diff_nanosecond_util), ('quarter', diff_quarter,
        diff_quarter), ('second', diff_second, diff_second_util), ('week',
        diff_week, diff_week_util), ('year', diff_year, diff_year_util)]
    for unit, xbh__impx, cywum__xlla in yuaq__jxwtm:
        gqyjp__xjg = create_dt_diff_fn_overload(unit)
        overload(xbh__impx)(gqyjp__xjg)
        nedh__mvf = create_dt_diff_fn_util_overload(unit)
        overload(cywum__xlla)(nedh__mvf)


_install_dt_diff_fn_overload()


def date_trunc(date_or_time_part, ts_arg):
    pass


@overload(date_trunc)
def overload_date_trunc(date_or_time_part, ts_arg):
    if isinstance(date_or_time_part, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.date_trunc',
            ['date_or_time_part', 'ts_arg'], 0)
    if isinstance(ts_arg, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.date_trunc',
            ['date_or_time_part', 'ts_arg'], 1)

    def impl(date_or_time_part, ts_arg):
        return date_trunc_util(date_or_time_part, ts_arg)
    return impl


def date_trunc_util(date_or_time_part, ts_arg):
    pass


@overload(date_trunc_util)
def overload_date_trunc_util(date_or_time_part, ts_arg):
    verify_string_arg(date_or_time_part, 'DATE_TRUNC', 'date_or_time_part')
    verify_datetime_arg_allow_tz(ts_arg, 'DATE_TRUNC', 'ts_arg')
    trth__jlnb = get_tz_if_exists(ts_arg)
    koye__cgie = ['date_or_time_part', 'ts_arg']
    had__nprad = [date_or_time_part, ts_arg]
    ropf__myt = [True, True]
    jpx__ljyj = ('bodo.utils.conversion.box_if_dt64' if bodo.utils.utils.
        is_array_typ(ts_arg, True) else '')
    rkqd__jojgu = ('bodo.utils.conversion.unbox_if_tz_naive_timestamp' if
        bodo.utils.utils.is_array_typ(ts_arg, True) else '')
    nql__qghjk = """part_str = bodo.libs.bodosql_array_kernels.standardize_snowflake_date_time_part(arg0)
"""
    if trth__jlnb is None:
        nql__qghjk += f'arg1 = {jpx__ljyj}(arg1)\n'
    nql__qghjk += "if part_str == 'quarter':\n"
    nql__qghjk += """    out_val = pd.Timestamp(year=arg1.year, month= (3*(arg1.quarter - 1)) + 1, day=1, tz=tz_literal)
"""
    nql__qghjk += "elif part_str == 'year':\n"
    nql__qghjk += (
        '    out_val = pd.Timestamp(year=arg1.year, month=1, day=1, tz=tz_literal)\n'
        )
    nql__qghjk += "elif part_str == 'month':\n"
    nql__qghjk += """    out_val = pd.Timestamp(year=arg1.year, month=arg1.month, day=1, tz=tz_literal)
"""
    nql__qghjk += "elif part_str == 'day':\n"
    nql__qghjk += '    out_val = arg1.normalize()\n'
    nql__qghjk += "elif part_str == 'week':\n"
    nql__qghjk += '    if arg1.dayofweek == 0:\n'
    nql__qghjk += '        out_val = arg1.normalize()\n'
    nql__qghjk += '    else:\n'
    nql__qghjk += (
        '        out_val = arg1.normalize() - pd.tseries.offsets.Week(n=1, weekday=0)\n'
        )
    nql__qghjk += "elif part_str == 'hour':\n"
    nql__qghjk += "    out_val = arg1.floor('H')\n"
    nql__qghjk += "elif part_str == 'minute':\n"
    nql__qghjk += "    out_val = arg1.floor('min')\n"
    nql__qghjk += "elif part_str == 'second':\n"
    nql__qghjk += "    out_val = arg1.floor('S')\n"
    nql__qghjk += "elif part_str == 'millisecond':\n"
    nql__qghjk += "    out_val = arg1.floor('ms')\n"
    nql__qghjk += "elif part_str == 'microsecond':\n"
    nql__qghjk += "    out_val = arg1.floor('us')\n"
    nql__qghjk += "elif part_str == 'nanosecond':\n"
    nql__qghjk += '    out_val = arg1\n'
    nql__qghjk += 'else:\n'
    nql__qghjk += (
        "    raise ValueError('Invalid date or time part for DATE_TRUNC')\n")
    if trth__jlnb is None:
        nql__qghjk += f'res[i] = {rkqd__jojgu}(out_val)\n'
    else:
        nql__qghjk += f'res[i] = out_val\n'
    if trth__jlnb is None:
        swc__xdqk = types.Array(bodo.datetime64ns, 1, 'C')
    else:
        swc__xdqk = bodo.DatetimeArrayType(trth__jlnb)
    return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
        swc__xdqk, extra_globals={'tz_literal': trth__jlnb})


@numba.generated_jit(nopython=True)
def dayname_util(arr):
    verify_datetime_arg_allow_tz(arr, 'dayname', 'arr')
    dkrd__cigss = get_tz_if_exists(arr)
    jpx__ljyj = ('bodo.utils.conversion.box_if_dt64' if dkrd__cigss is None
         else '')
    koye__cgie = ['arr']
    had__nprad = [arr]
    ropf__myt = [True]
    nql__qghjk = f'res[i] = {jpx__ljyj}(arg0).day_name()'
    swc__xdqk = bodo.string_array_type
    tpisy__cesqq = ['V']
    hwf__szmk = pd.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'])
    kqo__buuy = {'day_of_week_dict_arr': hwf__szmk}
    blimx__midod = 'dict_res = day_of_week_dict_arr'
    gyn__vke = f'res[i] = {jpx__ljyj}(arg0).dayofweek'
    return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
        swc__xdqk, synthesize_dict_if_vector=tpisy__cesqq,
        synthesize_dict_setup_text=blimx__midod,
        synthesize_dict_scalar_text=gyn__vke, extra_globals=kqo__buuy,
        synthesize_dict_global=True, synthesize_dict_unique=True)


@numba.generated_jit(nopython=True)
def int_to_days_util(arr):
    verify_int_arg(arr, 'int_to_days', 'arr')
    rkqd__jojgu = ('bodo.utils.conversion.unbox_if_tz_naive_timestamp' if
        bodo.utils.utils.is_array_typ(arr, True) else '')
    koye__cgie = ['arr']
    had__nprad = [arr]
    ropf__myt = [True]
    nql__qghjk = f'res[i] = {rkqd__jojgu}(pd.Timedelta(days=arg0))'
    swc__xdqk = np.dtype('timedelta64[ns]')
    return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
        swc__xdqk)


@numba.generated_jit(nopython=True)
def last_day_util(arr):
    verify_datetime_arg_allow_tz(arr, 'LAST_DAY', 'arr')
    ehdv__fac = get_tz_if_exists(arr)
    jpx__ljyj = ('bodo.utils.conversion.box_if_dt64' if bodo.utils.utils.
        is_array_typ(arr, True) else '')
    rkqd__jojgu = ('bodo.utils.conversion.unbox_if_tz_naive_timestamp' if
        bodo.utils.utils.is_array_typ(arr, True) else '')
    koye__cgie = ['arr']
    had__nprad = [arr]
    ropf__myt = [True]
    if ehdv__fac is None:
        nql__qghjk = (
            f'res[i] = {rkqd__jojgu}({jpx__ljyj}(arg0) + pd.tseries.offsets.MonthEnd(n=0, normalize=True))'
            )
        swc__xdqk = np.dtype('datetime64[ns]')
    else:
        nql__qghjk = 'y = arg0.year\n'
        nql__qghjk += 'm = arg0.month\n'
        nql__qghjk += (
            'd = bodo.hiframes.pd_offsets_ext.get_days_in_month(y, m)\n')
        nql__qghjk += (
            f'res[i] = pd.Timestamp(year=y, month=m, day=d, tz={repr(ehdv__fac)})\n'
            )
        swc__xdqk = bodo.DatetimeArrayType(ehdv__fac)
    return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
        swc__xdqk)


@numba.generated_jit(nopython=True)
def makedate_util(year, day):
    verify_int_arg(year, 'MAKEDATE', 'year')
    verify_int_arg(day, 'MAKEDATE', 'day')
    rkqd__jojgu = ('bodo.utils.conversion.unbox_if_tz_naive_timestamp' if 
        bodo.utils.utils.is_array_typ(year, True) or bodo.utils.utils.
        is_array_typ(day, True) else '')
    koye__cgie = ['year', 'day']
    had__nprad = [year, day]
    ropf__myt = [True] * 2
    nql__qghjk = (
        f'res[i] = {rkqd__jojgu}(pd.Timestamp(year=arg0, month=1, day=1) + pd.Timedelta(days=arg1-1))'
        )
    swc__xdqk = np.dtype('datetime64[ns]')
    return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
        swc__xdqk)


@numba.generated_jit(nopython=True)
def monthname_util(arr):
    verify_datetime_arg_allow_tz(arr, 'monthname', 'arr')
    dkrd__cigss = get_tz_if_exists(arr)
    jpx__ljyj = ('bodo.utils.conversion.box_if_dt64' if dkrd__cigss is None
         else '')
    koye__cgie = ['arr']
    had__nprad = [arr]
    ropf__myt = [True]
    nql__qghjk = f'res[i] = {jpx__ljyj}(arg0).month_name()'
    swc__xdqk = bodo.string_array_type
    tpisy__cesqq = ['V']
    rnbw__burl = pd.array(['January', 'February', 'March', 'April', 'May',
        'June', 'July', 'August', 'September', 'October', 'November',
        'December'])
    kqo__buuy = {'month_names_dict_arr': rnbw__burl}
    blimx__midod = 'dict_res = month_names_dict_arr'
    gyn__vke = f'res[i] = {jpx__ljyj}(arg0).month - 1'
    return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
        swc__xdqk, synthesize_dict_if_vector=tpisy__cesqq,
        synthesize_dict_setup_text=blimx__midod,
        synthesize_dict_scalar_text=gyn__vke, extra_globals=kqo__buuy,
        synthesize_dict_global=True, synthesize_dict_unique=True)


@numba.generated_jit(nopython=True)
def next_day_util(arr0, arr1):
    verify_datetime_arg_allow_tz(arr0, 'NEXT_DAY', 'arr0')
    verify_string_arg(arr1, 'NEXT_DAY', 'arr1')
    rycab__vvh = is_valid_tz_aware_datetime_arg(arr0)
    rkqd__jojgu = ('bodo.utils.conversion.unbox_if_tz_naive_timestamp' if 
        bodo.utils.utils.is_array_typ(arr0, True) or bodo.utils.utils.
        is_array_typ(arr1, True) else '')
    koye__cgie = ['arr0', 'arr1']
    had__nprad = [arr0, arr1]
    ropf__myt = [True] * 2
    zlzjl__oybbg = (
        "dow_map = {'mo': 0, 'tu': 1, 'we': 2, 'th': 3, 'fr': 4, 'sa': 5, 'su': 6}"
        )
    nql__qghjk = f'arg1_trimmed = arg1.lstrip()[:2].lower()\n'
    if rycab__vvh:
        kucaj__mzu = 'arg0'
    else:
        kucaj__mzu = 'bodo.utils.conversion.box_if_dt64(arg0)'
    nql__qghjk += f"""new_timestamp = {kucaj__mzu}.normalize() + pd.tseries.offsets.Week(weekday=dow_map[arg1_trimmed])
"""
    nql__qghjk += f'res[i] = {rkqd__jojgu}(new_timestamp.tz_localize(None))\n'
    swc__xdqk = types.Array(bodo.datetime64ns, 1, 'C')
    return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
        swc__xdqk, prefix_code=zlzjl__oybbg)


@numba.generated_jit(nopython=True)
def previous_day_util(arr0, arr1):
    verify_datetime_arg_allow_tz(arr0, 'PREVIOUS_DAY', 'arr0')
    verify_string_arg(arr1, 'PREVIOUS_DAY', 'arr1')
    rycab__vvh = is_valid_tz_aware_datetime_arg(arr0)
    rkqd__jojgu = ('bodo.utils.conversion.unbox_if_tz_naive_timestamp' if 
        bodo.utils.utils.is_array_typ(arr0, True) or bodo.utils.utils.
        is_array_typ(arr1, True) else '')
    koye__cgie = ['arr0', 'arr1']
    had__nprad = [arr0, arr1]
    ropf__myt = [True] * 2
    zlzjl__oybbg = (
        "dow_map = {'mo': 0, 'tu': 1, 'we': 2, 'th': 3, 'fr': 4, 'sa': 5, 'su': 6}"
        )
    nql__qghjk = f'arg1_trimmed = arg1.lstrip()[:2].lower()\n'
    if rycab__vvh:
        kucaj__mzu = 'arg0'
    else:
        kucaj__mzu = 'bodo.utils.conversion.box_if_dt64(arg0)'
    nql__qghjk += f"""new_timestamp = {kucaj__mzu}.normalize() - pd.tseries.offsets.Week(weekday=dow_map[arg1_trimmed])
"""
    nql__qghjk += f'res[i] = {rkqd__jojgu}(new_timestamp.tz_localize(None))\n'
    swc__xdqk = types.Array(bodo.datetime64ns, 1, 'C')
    return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
        swc__xdqk, prefix_code=zlzjl__oybbg)


@numba.generated_jit(nopython=True)
def second_timestamp_util(arr):
    verify_int_arg(arr, 'second_timestamp', 'arr')
    rkqd__jojgu = ('bodo.utils.conversion.unbox_if_tz_naive_timestamp' if
        bodo.utils.utils.is_array_typ(arr, True) else '')
    koye__cgie = ['arr']
    had__nprad = [arr]
    ropf__myt = [True]
    nql__qghjk = f"res[i] = {rkqd__jojgu}(pd.Timestamp(arg0, unit='s'))"
    swc__xdqk = np.dtype('datetime64[ns]')
    return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
        swc__xdqk)


@numba.generated_jit(nopython=True)
def weekday_util(arr):
    verify_datetime_arg(arr, 'WEEKDAY', 'arr')
    koye__cgie = ['arr']
    had__nprad = [arr]
    ropf__myt = [True]
    jpx__ljyj = ('bodo.utils.conversion.box_if_dt64' if bodo.utils.utils.
        is_array_typ(arr, True) else '')
    nql__qghjk = f'dt = {jpx__ljyj}(arg0)\n'
    nql__qghjk += (
        'res[i] = bodo.hiframes.pd_timestamp_ext.get_day_of_week(dt.year, dt.month, dt.day)'
        )
    swc__xdqk = bodo.libs.int_arr_ext.IntegerArrayType(types.int32)
    return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
        swc__xdqk)


@numba.generated_jit(nopython=True)
def yearofweekiso_util(arr):
    verify_datetime_arg_allow_tz(arr, 'YEAROFWEEKISO', 'arr')
    koye__cgie = ['arr']
    had__nprad = [arr]
    ropf__myt = [True]
    jpx__ljyj = ('bodo.utils.conversion.box_if_dt64' if bodo.utils.utils.
        is_array_typ(arr, True) else '')
    nql__qghjk = f'dt = {jpx__ljyj}(arg0)\n'
    nql__qghjk += 'res[i] = dt.isocalendar()[0]'
    swc__xdqk = bodo.libs.int_arr_ext.IntegerArrayType(types.int32)
    return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
        swc__xdqk)


def to_days(arr):
    pass


@overload(to_days)
def overload_to_days(arr):
    if isinstance(arr, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.to_days_util',
            ['arr'], 0)

    def impl(arr):
        return to_days_util(arr)
    return impl


def to_days_util(arr):
    pass


@overload(to_days_util)
def overload_to_days_util(arr):
    verify_datetime_arg(arr, 'TO_DAYS', 'arr')
    koye__cgie = ['arr']
    had__nprad = [arr]
    ropf__myt = [True]
    zlzjl__oybbg = 'unix_days_to_year_zero = 719528\n'
    zlzjl__oybbg += 'nanoseconds_divisor = 86400000000000\n'
    swc__xdqk = bodo.IntegerArrayType(types.int64)
    uex__lkz = bodo.utils.utils.is_array_typ(arr, False)
    if uex__lkz:
        nql__qghjk = (
            '  in_value = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(arg0)\n'
            )
    else:
        nql__qghjk = '  in_value = arg0.value\n'
    nql__qghjk += (
        '  res[i] = (in_value // nanoseconds_divisor) + unix_days_to_year_zero\n'
        )
    return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
        swc__xdqk, prefix_code=zlzjl__oybbg)


def from_days(arr):
    pass


@overload(from_days)
def overload_from_days(arr):
    if isinstance(arr, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.from_days_util',
            ['arr'], 0)

    def impl(arr):
        return from_days_util(arr)
    return impl


def from_days_util(arr):
    pass


@overload(from_days_util)
def overload_from_days_util(arr):
    verify_int_arg(arr, 'TO_DAYS', 'arr')
    koye__cgie = ['arr']
    had__nprad = [arr]
    ropf__myt = [True]
    uex__lkz = bodo.utils.utils.is_array_typ(arr, False)
    if uex__lkz:
        swc__xdqk = types.Array(bodo.datetime64ns, 1, 'C')
    else:
        swc__xdqk = bodo.pd_timestamp_tz_naive_type
    zlzjl__oybbg = 'unix_days_to_year_zero = 719528\n'
    zlzjl__oybbg += 'nanoseconds_divisor = 86400000000000\n'
    nql__qghjk = (
        '  nanoseconds = (arg0 - unix_days_to_year_zero) * nanoseconds_divisor\n'
        )
    if uex__lkz:
        nql__qghjk += (
            '  res[i] = bodo.hiframes.pd_timestamp_ext.integer_to_dt64(nanoseconds)\n'
            )
    else:
        nql__qghjk += '  res[i] = pd.Timestamp(nanoseconds)\n'
    return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
        swc__xdqk, prefix_code=zlzjl__oybbg)


def to_seconds(arr):
    pass


@overload(to_seconds)
def overload_to_seconds(arr):
    if isinstance(arr, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.to_seconds_util'
            , ['arr'], 0)

    def impl(arr):
        return to_seconds_util(arr)
    return impl


def to_seconds_util(arr):
    pass


@overload(to_seconds_util)
def overload_to_seconds_util(arr):
    verify_datetime_arg_allow_tz(arr, 'TO_SECONDS', 'arr')
    dybb__zocc = get_tz_if_exists(arr)
    koye__cgie = ['arr']
    had__nprad = [arr]
    ropf__myt = [True]
    zlzjl__oybbg = 'unix_seconds_to_year_zero = 62167219200\n'
    zlzjl__oybbg += 'nanoseconds_divisor = 1000000000\n'
    swc__xdqk = bodo.IntegerArrayType(types.int64)
    uex__lkz = bodo.utils.utils.is_array_typ(arr, False)
    if uex__lkz and not dybb__zocc:
        nql__qghjk = (
            f'  in_value = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(arg0)\n'
            )
    else:
        nql__qghjk = f'  in_value = arg0.value\n'
    nql__qghjk += (
        '  res[i] = (in_value // nanoseconds_divisor) + unix_seconds_to_year_zero\n'
        )
    return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
        swc__xdqk, prefix_code=zlzjl__oybbg)


def tz_aware_interval_add(tz_arg, interval_arg):
    pass


@overload(tz_aware_interval_add)
def overload_tz_aware_interval_add(tz_arg, interval_arg):
    if isinstance(tz_arg, types.optional):
        return unopt_argument(
            'bodo.libs.bodosql_array_kernels.tz_aware_interval_add', [
            'tz_arg', 'interval_arg'], 0)
    if isinstance(interval_arg, types.optional):
        return unopt_argument(
            'bodo.libs.bodosql_array_kernels.tz_aware_interval_add', [
            'tz_arg', 'interval_arg'], 1)

    def impl(tz_arg, interval_arg):
        return tz_aware_interval_add_util(tz_arg, interval_arg)
    return impl


def tz_aware_interval_add_util(tz_arg, interval_arg):
    pass


@overload(tz_aware_interval_add_util)
def overload_tz_aware_interval_add_util(tz_arg, interval_arg):
    verify_datetime_arg_require_tz(tz_arg, 'INTERVAL_ADD', 'tz_arg')
    verify_sql_interval(interval_arg, 'INTERVAL_ADD', 'interval_arg')
    dybb__zocc = get_tz_if_exists(tz_arg)
    koye__cgie = ['tz_arg', 'interval_arg']
    had__nprad = [tz_arg, interval_arg]
    ropf__myt = [True, True]
    if dybb__zocc is not None:
        swc__xdqk = bodo.DatetimeArrayType(dybb__zocc)
    else:
        swc__xdqk = bodo.datetime64ns
    if interval_arg == bodo.date_offset_type:
        nql__qghjk = """  timedelta = bodo.libs.pd_datetime_arr_ext.convert_months_offset_to_days(arg0.year, arg0.month, arg0.day, ((arg1._years * 12) + arg1._months) * arg1.n)
"""
    else:
        nql__qghjk = '  timedelta = arg1\n'
    nql__qghjk += """  timedelta = bodo.hiframes.pd_offsets_ext.update_timedelta_with_transition(arg0, timedelta)
"""
    nql__qghjk += '  res[i] = arg0 + timedelta\n'
    return gen_vectorized(koye__cgie, had__nprad, ropf__myt, nql__qghjk,
        swc__xdqk)
