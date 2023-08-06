"""
Implements a number of array kernels that handling casting functions for BodoSQL
"""
import numba
import numpy as np
import pandas as pd
from numba.core import types
from numba.extending import overload, register_jitable
import bodo
from bodo.libs.bodosql_array_kernel_utils import *
from bodo.utils.typing import get_literal_value, get_overload_const_bool, is_literal_type, is_overload_none, raise_bodo_error


@numba.generated_jit(nopython=True)
def try_to_boolean(arr):
    if isinstance(arr, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.to_boolean',
            ['arr'], 0)

    def impl(arr):
        return to_boolean_util(arr, numba.literally(True))
    return impl


@numba.generated_jit(nopython=True)
def to_boolean(arr):
    if isinstance(arr, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.to_boolean',
            ['arr'], 0)

    def impl(arr):
        return to_boolean_util(arr, numba.literally(False))
    return impl


@numba.generated_jit(nopython=True)
def to_boolean_util(arr, _try=False):
    verify_string_numeric_arg(arr, 'TO_BOOLEAN', 'arr')
    jeab__numzm = is_valid_string_arg(arr)
    xtnw__ksjlu = is_valid_float_arg(arr)
    _try = get_overload_const_bool(_try)
    if _try:
        djzm__yoy = 'bodo.libs.array_kernels.setna(res, i)\n'
    else:
        if jeab__numzm:
            bygdn__rpsad = (
                "string must be one of {'true', 't', 'yes', 'y', 'on', '1'} or {'false', 'f', 'no', 'n', 'off', '0'}"
                )
        else:
            bygdn__rpsad = 'value must be a valid numeric expression'
        djzm__yoy = (
            f'raise ValueError("invalid value for boolean conversion: {bygdn__rpsad}")'
            )
    djxqn__izw = ['arr', '_try']
    ixpz__gqd = [arr, _try]
    sodf__tdbx = [True, False]
    xnnms__mucfu = None
    if jeab__numzm:
        xnnms__mucfu = "true_vals = {'true', 't', 'yes', 'y', 'on', '1'}\n"
        xnnms__mucfu += "false_vals = {'false', 'f', 'no', 'n', 'off', '0'}"
    if jeab__numzm:
        vyfh__ckm = 's = arg0.lower()\n'
        vyfh__ckm += f'is_true_val = s in true_vals\n'
        vyfh__ckm += f'res[i] = is_true_val\n'
        vyfh__ckm += f'if not (is_true_val or s in false_vals):\n'
        vyfh__ckm += f'  {djzm__yoy}\n'
    elif xtnw__ksjlu:
        vyfh__ckm = 'if np.isinf(arg0) or np.isnan(arg0):\n'
        vyfh__ckm += f'  {djzm__yoy}\n'
        vyfh__ckm += 'else:\n'
        vyfh__ckm += f'  res[i] = bool(arg0)\n'
    else:
        vyfh__ckm = f'res[i] = bool(arg0)'
    djt__ofhge = bodo.libs.bool_arr_ext.boolean_array
    return gen_vectorized(djxqn__izw, ixpz__gqd, sodf__tdbx, vyfh__ckm,
        djt__ofhge, prefix_code=xnnms__mucfu)


@numba.generated_jit(nopython=True)
def try_to_date(conversionVal, optionalConversionFormatString):
    args = [conversionVal, optionalConversionFormatString]
    for jjsi__ckpj in range(2):
        if isinstance(args[jjsi__ckpj], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.try_to_date'
                , ['conversionVal', 'optionalConversionFormatString'],
                jjsi__ckpj)

    def impl(conversionVal, optionalConversionFormatString):
        return to_date_util(conversionVal, optionalConversionFormatString,
            numba.literally(False))
    return impl


@numba.generated_jit(nopython=True)
def to_date(conversionVal, optionalConversionFormatString):
    args = [conversionVal, optionalConversionFormatString]
    for jjsi__ckpj in range(2):
        if isinstance(args[jjsi__ckpj], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.to_date',
                ['conversionVal', 'optionalConversionFormatString'], jjsi__ckpj
                )

    def impl(conversionVal, optionalConversionFormatString):
        return to_date_util(conversionVal, optionalConversionFormatString,
            numba.literally(True))
    return impl


@numba.generated_jit(nopython=True)
def to_char(arr):
    if isinstance(arr, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.to_char', [
            'arr'], 0)

    def impl(arr):
        return to_char_util(arr)
    return impl


@numba.generated_jit(nopython=True)
def to_char_util(arr):
    djxqn__izw = ['arr']
    ixpz__gqd = [arr]
    sodf__tdbx = [True]
    if is_valid_binary_arg(arr):
        vyfh__ckm = 'with bodo.objmode(r=bodo.string_type):\n'
        vyfh__ckm += '  r = arg0.hex()\n'
        vyfh__ckm += 'res[i] = r'
    elif isinstance(arr, bodo.TimeType) or bodo.utils.utils.is_array_typ(arr
        ) and isinstance(arr.dtype, bodo.TimeType):
        vyfh__ckm = (
            "h_str = str(arg0.hour) if arg0.hour > 10 else '0' + str(arg0.hour)\n"
            )
        vyfh__ckm += (
            "m_str = str(arg0.minute) if arg0.minute > 10 else '0' + str(arg0.minute)\n"
            )
        vyfh__ckm += (
            "s_str = str(arg0.second) if arg0.second > 10 else '0' + str(arg0.second)\n"
            )
        vyfh__ckm += """ms_str = str(arg0.millisecond) if arg0.millisecond > 100 else ('0' + str(arg0.millisecond) if arg0.millisecond > 10 else '00' + str(arg0.millisecond))
"""
        vyfh__ckm += """us_str = str(arg0.microsecond) if arg0.microsecond > 100 else ('0' + str(arg0.microsecond) if arg0.microsecond > 10 else '00' + str(arg0.microsecond))
"""
        vyfh__ckm += """ns_str = str(arg0.nanosecond) if arg0.nanosecond > 100 else ('0' + str(arg0.nanosecond) if arg0.nanosecond > 10 else '00' + str(arg0.nanosecond))
"""
        vyfh__ckm += "part_str = h_str + ':' + m_str + ':' + s_str\n"
        vyfh__ckm += 'if arg0.nanosecond > 0:\n'
        vyfh__ckm += "  part_str = part_str + '.' + ms_str + us_str + ns_str\n"
        vyfh__ckm += 'elif arg0.microsecond > 0:\n'
        vyfh__ckm += "  part_str = part_str + '.' + ms_str + us_str\n"
        vyfh__ckm += 'elif arg0.millisecond > 0:\n'
        vyfh__ckm += "  part_str = part_str + '.' + ms_str\n"
        vyfh__ckm += 'res[i] = part_str'
    elif is_valid_timedelta_arg(arr):
        vyfh__ckm = (
            'v = bodo.utils.conversion.unbox_if_tz_naive_timestamp(arg0)\n')
        vyfh__ckm += 'with bodo.objmode(r=bodo.string_type):\n'
        vyfh__ckm += '    r = str(v)\n'
        vyfh__ckm += 'res[i] = r'
    elif is_valid_datetime_or_date_arg(arr):
        if is_valid_tz_aware_datetime_arg(arr):
            vyfh__ckm = "tz_raw = arg0.strftime('%z')\n"
            vyfh__ckm += 'tz = tz_raw[:3] + ":" + tz_raw[3:]\n'
            vyfh__ckm += "res[i] = arg0.isoformat(' ') + tz\n"
        else:
            vyfh__ckm = "res[i] = pd.Timestamp(arg0).isoformat(' ')\n"
    elif is_valid_float_arg(arr):
        vyfh__ckm = 'if np.isinf(arg0):\n'
        vyfh__ckm += "  res[i] = 'inf' if arg0 > 0 else '-inf'\n"
        vyfh__ckm += 'elif np.isnan(arg0):\n'
        vyfh__ckm += "  res[i] = 'NaN'\n"
        vyfh__ckm += 'else:\n'
        vyfh__ckm += '  res[i] = str(arg0)'
    elif is_valid_boolean_arg(arr):
        vyfh__ckm = "res[i] = 'true' if arg0 else 'false'"
    else:
        nhy__cte = {(8): np.int8, (16): np.int16, (32): np.int32, (64): np.
            int64}
        if is_valid_int_arg(arr):
            if hasattr(arr, 'dtype'):
                wpf__orwl = arr.dtype.bitwidth
            else:
                wpf__orwl = arr.bitwidth
            vyfh__ckm = f'if arg0 == {np.iinfo(nhy__cte[wpf__orwl]).min}:\n'
            vyfh__ckm += f"  res[i] = '{np.iinfo(nhy__cte[wpf__orwl]).min}'\n"
            vyfh__ckm += 'else:\n'
            vyfh__ckm += '  res[i] = str(arg0)'
        else:
            vyfh__ckm = 'res[i] = str(arg0)'
    djt__ofhge = bodo.string_array_type
    return gen_vectorized(djxqn__izw, ixpz__gqd, sodf__tdbx, vyfh__ckm,
        djt__ofhge)


@register_jitable
def convert_sql_date_format_str_to_py_format(val):
    raise RuntimeError(
        'Converting to date values with format strings not currently supported'
        )


@numba.generated_jit(nopython=True)
def int_to_datetime(val):

    def impl(val):
        if val < 31536000000:
            blf__gue = pd.to_datetime(val, unit='s')
        elif val < 31536000000000:
            blf__gue = pd.to_datetime(val, unit='ms')
        elif val < 31536000000000000:
            blf__gue = pd.to_datetime(val, unit='us')
        else:
            blf__gue = pd.to_datetime(val, unit='ns')
        return blf__gue
    return impl


@numba.generated_jit(nopython=True)
def float_to_datetime(val):

    def impl(val):
        if val < 31536000000:
            blf__gue = pd.Timestamp(val, unit='s')
        elif val < 31536000000000:
            blf__gue = pd.Timestamp(val, unit='ms')
        elif val < 31536000000000000:
            blf__gue = pd.Timestamp(val, unit='us')
        else:
            blf__gue = pd.Timestamp(val, unit='ns')
        return blf__gue
    return impl


@register_jitable
def pd_to_datetime_error_checked(val, dayfirst=False, yearfirst=False, utc=
    None, format=None, exact=True, unit=None, infer_datetime_format=False,
    origin='unix', cache=True):
    if val is not None:
        ymra__vjscn = val.split(' ')[0]
        if len(ymra__vjscn) < 10:
            return False, None
        else:
            spq__ljwa = ymra__vjscn.count('/') in [0, 2]
            nfys__jdsi = ymra__vjscn.count('-') in [0, 2]
            if not (spq__ljwa and nfys__jdsi):
                return False, None
    with numba.objmode(ret_val='pd_timestamp_tz_naive_type', success_flag=
        'bool_'):
        success_flag = True
        ret_val = pd.Timestamp(0)
        ker__wudb = pd.to_datetime(val, errors='coerce', dayfirst=dayfirst,
            yearfirst=yearfirst, utc=utc, format=format, exact=exact, unit=
            unit, infer_datetime_format=infer_datetime_format, origin=
            origin, cache=cache)
        if pd.isna(ker__wudb):
            success_flag = False
        else:
            ret_val = ker__wudb
    return success_flag, ret_val


@numba.generated_jit(nopython=True)
def to_date_util(conversionVal, optionalConversionFormatString, errorOnFail,
    _keep_time=False):
    errorOnFail = get_overload_const_bool(errorOnFail)
    _keep_time = get_overload_const_bool(_keep_time)
    if errorOnFail:
        yzxtt__wvde = (
            "raise ValueError('Invalid input while converting to date value')")
    else:
        yzxtt__wvde = 'bodo.libs.array_kernels.setna(res, i)'
    if _keep_time:
        pckv__par = ''
    else:
        pckv__par = '.normalize()'
    verify_string_arg(optionalConversionFormatString,
        'TO_DATE and TRY_TO_DATE', 'optionalConversionFormatString')
    fxyq__swqyn = bodo.utils.utils.is_array_typ(conversionVal, True
        ) or bodo.utils.utils.is_array_typ(optionalConversionFormatString, True
        )
    yenwe__keui = 'unbox_if_tz_naive_timestamp' if fxyq__swqyn else ''
    if not is_overload_none(optionalConversionFormatString):
        verify_string_arg(conversionVal, 'TO_DATE and TRY_TO_DATE',
            'optionalConversionFormatString')
        vyfh__ckm = (
            'py_format_str = convert_sql_date_format_str_to_py_format(arg1)\n')
        vyfh__ckm += """was_successful, tmp_val = pd_to_datetime_error_checked(arg0, format=py_format_str)
"""
        vyfh__ckm += 'if not was_successful:\n'
        vyfh__ckm += f'  {yzxtt__wvde}\n'
        vyfh__ckm += 'else:\n'
        vyfh__ckm += f'  res[i] = {yenwe__keui}(tmp_val{pckv__par})\n'
    elif is_valid_string_arg(conversionVal):
        """
        If no format string is specified, snowflake will use attempt to parse the string according to these date formats:
        https://docs.snowflake.com/en/user-guide/date-time-input-output.html#date-formats. All of the examples listed are
        handled by pd.to_datetime() in Bodo jit code.

        It will also check if the string is convertable to int, IE '12345' or '-4321'"""
        vyfh__ckm = 'arg0 = str(arg0)\n'
        vyfh__ckm += """if (arg0.isnumeric() or (len(arg0) > 1 and arg0[0] == '-' and arg0[1:].isnumeric())):
"""
        vyfh__ckm += (
            f'   res[i] = {yenwe__keui}(int_to_datetime(np.int64(arg0)){pckv__par})\n'
            )
        vyfh__ckm += 'else:\n'
        vyfh__ckm += (
            '   was_successful, tmp_val = pd_to_datetime_error_checked(arg0)\n'
            )
        vyfh__ckm += '   if not was_successful:\n'
        vyfh__ckm += f'      {yzxtt__wvde}\n'
        vyfh__ckm += '   else:\n'
        vyfh__ckm += f'      res[i] = {yenwe__keui}(tmp_val{pckv__par})\n'
    elif is_valid_int_arg(conversionVal):
        vyfh__ckm = (
            f'res[i] = {yenwe__keui}(int_to_datetime(arg0){pckv__par})\n')
    elif is_valid_float_arg(conversionVal):
        vyfh__ckm = (
            f'res[i] = {yenwe__keui}(float_to_datetime(arg0){pckv__par})\n')
    elif is_valid_datetime_or_date_arg(conversionVal):
        vyfh__ckm = f'res[i] = {yenwe__keui}(pd.Timestamp(arg0){pckv__par})\n'
    elif is_valid_tz_aware_datetime_arg(conversionVal):
        vyfh__ckm = f'res[i] = arg0{pckv__par}\n'
    else:
        raise raise_bodo_error(
            f'Internal error: unsupported type passed to to_date_util for argument conversionVal: {conversionVal}'
            )
    djxqn__izw = ['conversionVal', 'optionalConversionFormatString',
        'errorOnFail', '_keep_time']
    ixpz__gqd = [conversionVal, optionalConversionFormatString, errorOnFail,
        _keep_time]
    sodf__tdbx = [True, False, False, False]
    if isinstance(conversionVal, bodo.DatetimeArrayType) or isinstance(
        conversionVal, bodo.PandasTimestampType
        ) and conversionVal.tz is not None:
        djt__ofhge = bodo.DatetimeArrayType(conversionVal.tz)
    else:
        djt__ofhge = types.Array(bodo.datetime64ns, 1, 'C')
    fhx__mctw = {'pd_to_datetime_error_checked':
        pd_to_datetime_error_checked, 'int_to_datetime': int_to_datetime,
        'float_to_datetime': float_to_datetime,
        'convert_sql_date_format_str_to_py_format':
        convert_sql_date_format_str_to_py_format,
        'unbox_if_tz_naive_timestamp': bodo.utils.conversion.
        unbox_if_tz_naive_timestamp}
    return gen_vectorized(djxqn__izw, ixpz__gqd, sodf__tdbx, vyfh__ckm,
        djt__ofhge, extra_globals=fhx__mctw)


def cast_tz_naive_to_tz_aware(arr, tz):
    pass


@overload(cast_tz_naive_to_tz_aware, no_unliteral=True)
def overload_cast_tz_naive_to_tz_aware(arr, tz):
    if not is_literal_type(tz):
        raise_bodo_error(
            "cast_tz_naive_to_tz_aware(): 'tz' must be a literal value")
    if isinstance(arr, types.optional):
        return unopt_argument(
            'bodo.libs.bodosql_array_kernels.cast_tz_naive_to_tz_aware', [
            'arr', 'tz'], 0)

    def impl(arr, tz):
        return cast_tz_naive_to_tz_aware_util(arr, tz)
    return impl


def cast_tz_naive_to_tz_aware_util(arr, tz):
    pass


@overload(cast_tz_naive_to_tz_aware_util, no_unliteral=True)
def overload_cast_tz_naive_to_tz_aware_util(arr, tz):
    if not is_literal_type(tz):
        raise_bodo_error(
            "cast_tz_naive_to_tz_aware(): 'tz' must be a literal value")
    verify_datetime_arg(arr, 'cast_tz_naive_to_tz_aware', 'arr')
    djxqn__izw = ['arr', 'tz']
    ixpz__gqd = [arr, tz]
    sodf__tdbx = [True, False]
    utlhk__ayjjc = ('bodo.utils.conversion.box_if_dt64' if bodo.utils.utils
        .is_array_typ(arr) else '')
    vyfh__ckm = f'res[i] = {utlhk__ayjjc}(arg0).tz_localize(arg1)'
    tz = get_literal_value(tz)
    djt__ofhge = bodo.DatetimeArrayType(tz)
    return gen_vectorized(djxqn__izw, ixpz__gqd, sodf__tdbx, vyfh__ckm,
        djt__ofhge)


def cast_tz_aware_to_tz_naive(arr, normalize):
    pass


@overload(cast_tz_aware_to_tz_naive, no_unliteral=True)
def overload_cast_tz_aware_to_tz_naive(arr, normalize):
    if not is_overload_constant_bool(normalize):
        raise_bodo_error(
            "cast_tz_aware_to_tz_naive(): 'normalize' must be a literal value")
    if isinstance(arr, types.optional):
        return unopt_argument(
            'bodo.libs.bodosql_array_kernels.cast_tz_aware_to_tz_naive', [
            'arr', 'normalize'], 0)

    def impl(arr, normalize):
        return cast_tz_aware_to_tz_naive_util(arr, normalize)
    return impl


def cast_tz_aware_to_tz_naive_util(arr, normalize):
    pass


@overload(cast_tz_aware_to_tz_naive_util, no_unliteral=True)
def overload_cast_tz_aware_to_tz_naive_util(arr, normalize):
    if not is_overload_constant_bool(normalize):
        raise_bodo_error(
            "cast_tz_aware_to_tz_naive(): 'normalize' must be a literal value")
    normalize = get_overload_const_bool(normalize)
    verify_datetime_arg_require_tz(arr, 'cast_tz_aware_to_tz_naive', 'arr')
    djxqn__izw = ['arr', 'normalize']
    ixpz__gqd = [arr, normalize]
    sodf__tdbx = [True, False]
    yenwe__keui = ('bodo.utils.conversion.unbox_if_tz_naive_timestamp' if
        bodo.utils.utils.is_array_typ(arr) else '')
    vyfh__ckm = ''
    if normalize:
        vyfh__ckm += (
            'ts = pd.Timestamp(year=arg0.year, month=arg0.month, day=arg0.day)\n'
            )
    else:
        vyfh__ckm += 'ts = arg0.tz_localize(None)\n'
    vyfh__ckm += f'res[i] = {yenwe__keui}(ts)'
    djt__ofhge = types.Array(bodo.datetime64ns, 1, 'C')
    return gen_vectorized(djxqn__izw, ixpz__gqd, sodf__tdbx, vyfh__ckm,
        djt__ofhge)


def cast_str_to_tz_aware(arr, tz):
    pass


@overload(cast_str_to_tz_aware, no_unliteral=True)
def overload_cast_str_to_tz_aware(arr, tz):
    if not is_literal_type(tz):
        raise_bodo_error("cast_str_to_tz_aware(): 'tz' must be a literal value"
            )
    if isinstance(arr, types.optional):
        return unopt_argument(
            'bodo.libs.bodosql_array_kernels.cast_str_to_tz_aware', ['arr',
            'tz'], 0)

    def impl(arr, tz):
        return cast_str_to_tz_aware_util(arr, tz)
    return impl


def cast_str_to_tz_aware_util(arr, tz):
    pass


@overload(cast_str_to_tz_aware_util, no_unliteral=True)
def overload_cast_str_to_tz_aware_util(arr, tz):
    if not is_literal_type(tz):
        raise_bodo_error("cast_str_to_tz_aware(): 'tz' must be a literal value"
            )
    verify_string_arg(arr, 'cast_str_to_tz_aware', 'arr')
    djxqn__izw = ['arr', 'tz']
    ixpz__gqd = [arr, tz]
    sodf__tdbx = [True, False]
    vyfh__ckm = f'res[i] = pd.to_datetime(arg0).tz_localize(arg1)'
    tz = get_literal_value(tz)
    djt__ofhge = bodo.DatetimeArrayType(tz)
    return gen_vectorized(djxqn__izw, ixpz__gqd, sodf__tdbx, vyfh__ckm,
        djt__ofhge)
