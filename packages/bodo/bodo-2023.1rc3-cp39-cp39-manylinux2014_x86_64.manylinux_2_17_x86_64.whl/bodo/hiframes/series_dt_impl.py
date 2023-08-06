"""
Support for Series.dt attributes and methods
"""
import datetime
import operator
import numba
import numpy as np
from numba.core import cgutils, types
from numba.extending import intrinsic, make_attribute_wrapper, models, overload_attribute, overload_method, register_model
import bodo
from bodo.hiframes.pd_series_ext import SeriesType, get_series_data, get_series_index, get_series_name, init_series
from bodo.libs.pd_datetime_arr_ext import PandasDatetimeTZDtype
from bodo.utils.typing import BodoError, ColNamesMetaType, check_unsupported_args, create_unsupported_overload, raise_bodo_error
dt64_dtype = np.dtype('datetime64[ns]')
timedelta64_dtype = np.dtype('timedelta64[ns]')


class SeriesDatetimePropertiesType(types.Type):

    def __init__(self, stype):
        self.stype = stype
        wxwpc__gzr = 'SeriesDatetimePropertiesType({})'.format(stype)
        super(SeriesDatetimePropertiesType, self).__init__(wxwpc__gzr)


@register_model(SeriesDatetimePropertiesType)
class SeriesDtModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        qttc__dxcbh = [('obj', fe_type.stype)]
        super(SeriesDtModel, self).__init__(dmm, fe_type, qttc__dxcbh)


make_attribute_wrapper(SeriesDatetimePropertiesType, 'obj', '_obj')


@intrinsic
def init_series_dt_properties(typingctx, obj=None):

    def codegen(context, builder, signature, args):
        nbjt__tmwol, = args
        dpeq__cbk = signature.return_type
        hlpr__ysywu = cgutils.create_struct_proxy(dpeq__cbk)(context, builder)
        hlpr__ysywu.obj = nbjt__tmwol
        context.nrt.incref(builder, signature.args[0], nbjt__tmwol)
        return hlpr__ysywu._getvalue()
    return SeriesDatetimePropertiesType(obj)(obj), codegen


@overload_attribute(SeriesType, 'dt')
def overload_series_dt(s):
    if not (bodo.hiframes.pd_series_ext.is_dt64_series_typ(s) or bodo.
        hiframes.pd_series_ext.is_timedelta64_series_typ(s)):
        raise_bodo_error('Can only use .dt accessor with datetimelike values.')
    return lambda s: bodo.hiframes.series_dt_impl.init_series_dt_properties(s)


def create_date_field_overload(field):

    def overload_field(S_dt):
        if S_dt.stype.dtype != types.NPDatetime('ns') and not isinstance(S_dt
            .stype.dtype, PandasDatetimeTZDtype):
            return
        wkk__etl = isinstance(S_dt.stype.dtype, PandasDatetimeTZDtype)
        febvr__rddyt = ['year', 'quarter', 'month', 'week', 'day', 'hour',
            'minute', 'second', 'microsecond']
        if field not in febvr__rddyt:
            bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S_dt,
                f'Series.dt.{field}')
        kgq__uab = 'def impl(S_dt):\n'
        kgq__uab += '    S = S_dt._obj\n'
        kgq__uab += (
            '    arr = bodo.hiframes.pd_series_ext.get_series_data(S)\n')
        kgq__uab += (
            '    index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
        kgq__uab += (
            '    name = bodo.hiframes.pd_series_ext.get_series_name(S)\n')
        kgq__uab += '    numba.parfors.parfor.init_prange()\n'
        kgq__uab += '    n = len(arr)\n'
        if field in ('is_leap_year', 'is_month_start', 'is_month_end',
            'is_quarter_start', 'is_quarter_end', 'is_year_start',
            'is_year_end'):
            kgq__uab += '    out_arr = np.empty(n, np.bool_)\n'
        else:
            kgq__uab += (
                '    out_arr = bodo.libs.int_arr_ext.alloc_int_array(n, np.int64)\n'
                )
        kgq__uab += '    for i in numba.parfors.parfor.internal_prange(n):\n'
        kgq__uab += '        if bodo.libs.array_kernels.isna(arr, i):\n'
        kgq__uab += '            bodo.libs.array_kernels.setna(out_arr, i)\n'
        kgq__uab += '            continue\n'
        if not wkk__etl:
            kgq__uab += (
                '        dt64 = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(arr[i])\n'
                )
            kgq__uab += """        ts = bodo.hiframes.pd_timestamp_ext.convert_datetime64_to_timestamp(dt64)
"""
            if field == 'weekday':
                kgq__uab += '        out_arr[i] = ts.weekday()\n'
            else:
                kgq__uab += '        out_arr[i] = ts.' + field + '\n'
        else:
            kgq__uab += '        out_arr[i] = arr[i].{}\n'.format(field)
        kgq__uab += (
            '    return bodo.hiframes.pd_series_ext.init_series(out_arr, index, name)\n'
            )
        waa__tgafi = {}
        exec(kgq__uab, {'bodo': bodo, 'numba': numba, 'np': np}, waa__tgafi)
        impl = waa__tgafi['impl']
        return impl
    return overload_field


def _install_date_fields():
    for field in bodo.hiframes.pd_timestamp_ext.date_fields:
        rne__shwn = create_date_field_overload(field)
        overload_attribute(SeriesDatetimePropertiesType, field)(rne__shwn)


_install_date_fields()


def create_date_method_overload(method):
    byr__lemyx = method in ['day_name', 'month_name']
    if byr__lemyx:
        kgq__uab = 'def overload_method(S_dt, locale=None):\n'
        kgq__uab += '    unsupported_args = dict(locale=locale)\n'
        kgq__uab += '    arg_defaults = dict(locale=None)\n'
        kgq__uab += '    bodo.utils.typing.check_unsupported_args(\n'
        kgq__uab += f"        'Series.dt.{method}',\n"
        kgq__uab += '        unsupported_args,\n'
        kgq__uab += '        arg_defaults,\n'
        kgq__uab += "        package_name='pandas',\n"
        kgq__uab += "        module_name='Series',\n"
        kgq__uab += '    )\n'
    else:
        kgq__uab = 'def overload_method(S_dt):\n'
        kgq__uab += f"""    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S_dt, 'Series.dt.{method}()')
"""
    kgq__uab += """    if not (S_dt.stype.dtype == bodo.datetime64ns or isinstance(S_dt.stype.dtype, bodo.libs.pd_datetime_arr_ext.PandasDatetimeTZDtype)):
"""
    kgq__uab += '        return\n'
    if byr__lemyx:
        kgq__uab += '    def impl(S_dt, locale=None):\n'
    else:
        kgq__uab += '    def impl(S_dt):\n'
    kgq__uab += '        S = S_dt._obj\n'
    kgq__uab += (
        '        arr = bodo.hiframes.pd_series_ext.get_series_data(S)\n')
    kgq__uab += (
        '        index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
    kgq__uab += (
        '        name = bodo.hiframes.pd_series_ext.get_series_name(S)\n')
    kgq__uab += '        numba.parfors.parfor.init_prange()\n'
    kgq__uab += '        n = len(arr)\n'
    if byr__lemyx:
        kgq__uab += """        out_arr = bodo.utils.utils.alloc_type(n, bodo.string_array_type, (-1,))
"""
    else:
        kgq__uab += (
            "        out_arr = np.empty(n, np.dtype('datetime64[ns]'))\n")
    kgq__uab += '        for i in numba.parfors.parfor.internal_prange(n):\n'
    kgq__uab += '            if bodo.libs.array_kernels.isna(arr, i):\n'
    kgq__uab += '                bodo.libs.array_kernels.setna(out_arr, i)\n'
    kgq__uab += '                continue\n'
    kgq__uab += '            ts = bodo.utils.conversion.box_if_dt64(arr[i])\n'
    kgq__uab += f'            method_val = ts.{method}()\n'
    if byr__lemyx:
        kgq__uab += '            out_arr[i] = method_val\n'
    else:
        kgq__uab += """            out_arr[i] = bodo.hiframes.pd_timestamp_ext.integer_to_dt64(method_val.value)
"""
    kgq__uab += (
        '        return bodo.hiframes.pd_series_ext.init_series(out_arr, index, name)\n'
        )
    kgq__uab += '    return impl\n'
    waa__tgafi = {}
    exec(kgq__uab, {'bodo': bodo, 'numba': numba, 'np': np}, waa__tgafi)
    overload_method = waa__tgafi['overload_method']
    return overload_method


def _install_date_methods():
    for method in bodo.hiframes.pd_timestamp_ext.date_methods:
        rne__shwn = create_date_method_overload(method)
        overload_method(SeriesDatetimePropertiesType, method, inline='always')(
            rne__shwn)


_install_date_methods()


@overload_attribute(SeriesDatetimePropertiesType, 'date')
def series_dt_date_overload(S_dt):
    if not (S_dt.stype.dtype == types.NPDatetime('ns') or isinstance(S_dt.
        stype.dtype, bodo.libs.pd_datetime_arr_ext.PandasDatetimeTZDtype)):
        return

    def impl(S_dt):
        vchys__nsqua = S_dt._obj
        sqsi__eatiy = bodo.hiframes.pd_series_ext.get_series_data(vchys__nsqua)
        lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(vchys__nsqua)
        wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(vchys__nsqua)
        numba.parfors.parfor.init_prange()
        ide__oxwpc = len(sqsi__eatiy)
        jst__toua = bodo.hiframes.datetime_date_ext.alloc_datetime_date_array(
            ide__oxwpc)
        for qzan__oxgnu in numba.parfors.parfor.internal_prange(ide__oxwpc):
            xwxk__dlah = sqsi__eatiy[qzan__oxgnu]
            mfe__rpuhr = bodo.utils.conversion.box_if_dt64(xwxk__dlah)
            jst__toua[qzan__oxgnu] = datetime.date(mfe__rpuhr.year,
                mfe__rpuhr.month, mfe__rpuhr.day)
        return bodo.hiframes.pd_series_ext.init_series(jst__toua,
            lxinu__xrj, wxwpc__gzr)
    return impl


def create_series_dt_df_output_overload(attr):

    def series_dt_df_output_overload(S_dt):
        if not (attr == 'components' and S_dt.stype.dtype == types.
            NPTimedelta('ns') or attr == 'isocalendar' and (S_dt.stype.
            dtype == types.NPDatetime('ns') or isinstance(S_dt.stype.dtype,
            PandasDatetimeTZDtype))):
            return
        wkk__etl = isinstance(S_dt.stype.dtype, PandasDatetimeTZDtype)
        if attr != 'isocalendar':
            bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(S_dt,
                f'Series.dt.{attr}')
        if attr == 'components':
            niy__dbx = ['days', 'hours', 'minutes', 'seconds',
                'milliseconds', 'microseconds', 'nanoseconds']
            exx__yvp = 'convert_numpy_timedelta64_to_pd_timedelta'
            cpsg__dso = 'np.empty(n, np.int64)'
            idnet__nixq = attr
        elif attr == 'isocalendar':
            niy__dbx = ['year', 'week', 'day']
            if wkk__etl:
                exx__yvp = None
            else:
                exx__yvp = 'convert_datetime64_to_timestamp'
            cpsg__dso = 'bodo.libs.int_arr_ext.alloc_int_array(n, np.uint32)'
            idnet__nixq = attr + '()'
        kgq__uab = 'def impl(S_dt):\n'
        kgq__uab += '    S = S_dt._obj\n'
        kgq__uab += (
            '    arr = bodo.hiframes.pd_series_ext.get_series_data(S)\n')
        kgq__uab += (
            '    index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
        kgq__uab += '    numba.parfors.parfor.init_prange()\n'
        kgq__uab += '    n = len(arr)\n'
        for field in niy__dbx:
            kgq__uab += '    {} = {}\n'.format(field, cpsg__dso)
        kgq__uab += '    for i in numba.parfors.parfor.internal_prange(n):\n'
        kgq__uab += '        if bodo.libs.array_kernels.isna(arr, i):\n'
        for field in niy__dbx:
            kgq__uab += ('            bodo.libs.array_kernels.setna({}, i)\n'
                .format(field))
        kgq__uab += '            continue\n'
        rdr__rca = '(' + '[i], '.join(niy__dbx) + '[i])'
        if exx__yvp:
            cbsj__fetm = f'bodo.hiframes.pd_timestamp_ext.{exx__yvp}(arr[i])'
        else:
            cbsj__fetm = 'arr[i]'
        kgq__uab += f'        {rdr__rca} = {cbsj__fetm}.{idnet__nixq}\n'
        fhgh__dfmz = '(' + ', '.join(niy__dbx) + ')'
        kgq__uab += (
            """    return bodo.hiframes.pd_dataframe_ext.init_dataframe({}, index, __col_name_meta_value_series_dt_df_output)
"""
            .format(fhgh__dfmz))
        waa__tgafi = {}
        exec(kgq__uab, {'bodo': bodo, 'numba': numba, 'np': np,
            '__col_name_meta_value_series_dt_df_output': ColNamesMetaType(
            tuple(niy__dbx))}, waa__tgafi)
        impl = waa__tgafi['impl']
        return impl
    return series_dt_df_output_overload


def _install_df_output_overload():
    tgtdo__pph = [('components', overload_attribute), ('isocalendar',
        overload_method)]
    for attr, rjsl__gmat in tgtdo__pph:
        rne__shwn = create_series_dt_df_output_overload(attr)
        rjsl__gmat(SeriesDatetimePropertiesType, attr, inline='always')(
            rne__shwn)


_install_df_output_overload()


def create_timedelta_field_overload(field):

    def overload_field(S_dt):
        if not S_dt.stype.dtype == types.NPTimedelta('ns'):
            return
        kgq__uab = 'def impl(S_dt):\n'
        kgq__uab += '    S = S_dt._obj\n'
        kgq__uab += '    A = bodo.hiframes.pd_series_ext.get_series_data(S)\n'
        kgq__uab += (
            '    index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
        kgq__uab += (
            '    name = bodo.hiframes.pd_series_ext.get_series_name(S)\n')
        kgq__uab += '    numba.parfors.parfor.init_prange()\n'
        kgq__uab += '    n = len(A)\n'
        kgq__uab += (
            '    B = bodo.libs.int_arr_ext.alloc_int_array(n, np.int64)\n')
        kgq__uab += '    for i in numba.parfors.parfor.internal_prange(n):\n'
        kgq__uab += '        if bodo.libs.array_kernels.isna(A, i):\n'
        kgq__uab += '            bodo.libs.array_kernels.setna(B, i)\n'
        kgq__uab += '            continue\n'
        kgq__uab += (
            '        td64 = bodo.hiframes.pd_timestamp_ext.timedelta64_to_integer(A[i])\n'
            )
        if field == 'nanoseconds':
            kgq__uab += '        B[i] = td64 % 1000\n'
        elif field == 'microseconds':
            kgq__uab += '        B[i] = td64 // 1000 % 1000000\n'
        elif field == 'seconds':
            kgq__uab += (
                '        B[i] = td64 // (1000 * 1000000) % (60 * 60 * 24)\n')
        elif field == 'days':
            kgq__uab += (
                '        B[i] = td64 // (1000 * 1000000 * 60 * 60 * 24)\n')
        else:
            assert False, 'invalid timedelta field'
        kgq__uab += (
            '    return bodo.hiframes.pd_series_ext.init_series(B, index, name)\n'
            )
        waa__tgafi = {}
        exec(kgq__uab, {'numba': numba, 'np': np, 'bodo': bodo}, waa__tgafi)
        impl = waa__tgafi['impl']
        return impl
    return overload_field


def create_timedelta_method_overload(method):

    def overload_method(S_dt):
        if not S_dt.stype.dtype == types.NPTimedelta('ns'):
            return
        kgq__uab = 'def impl(S_dt):\n'
        kgq__uab += '    S = S_dt._obj\n'
        kgq__uab += '    A = bodo.hiframes.pd_series_ext.get_series_data(S)\n'
        kgq__uab += (
            '    index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
        kgq__uab += (
            '    name = bodo.hiframes.pd_series_ext.get_series_name(S)\n')
        kgq__uab += '    numba.parfors.parfor.init_prange()\n'
        kgq__uab += '    n = len(A)\n'
        if method == 'total_seconds':
            kgq__uab += '    B = np.empty(n, np.float64)\n'
        else:
            kgq__uab += """    B = bodo.hiframes.datetime_timedelta_ext.alloc_datetime_timedelta_array(n)
"""
        kgq__uab += '    for i in numba.parfors.parfor.internal_prange(n):\n'
        kgq__uab += '        if bodo.libs.array_kernels.isna(A, i):\n'
        kgq__uab += '            bodo.libs.array_kernels.setna(B, i)\n'
        kgq__uab += '            continue\n'
        kgq__uab += (
            '        td64 = bodo.hiframes.pd_timestamp_ext.timedelta64_to_integer(A[i])\n'
            )
        if method == 'total_seconds':
            kgq__uab += '        B[i] = td64 / (1000.0 * 1000000.0)\n'
        elif method == 'to_pytimedelta':
            kgq__uab += (
                '        B[i] = datetime.timedelta(microseconds=td64 // 1000)\n'
                )
        else:
            assert False, 'invalid timedelta method'
        if method == 'total_seconds':
            kgq__uab += (
                '    return bodo.hiframes.pd_series_ext.init_series(B, index, name)\n'
                )
        else:
            kgq__uab += '    return B\n'
        waa__tgafi = {}
        exec(kgq__uab, {'numba': numba, 'np': np, 'bodo': bodo, 'datetime':
            datetime}, waa__tgafi)
        impl = waa__tgafi['impl']
        return impl
    return overload_method


def _install_S_dt_timedelta_fields():
    for field in bodo.hiframes.pd_timestamp_ext.timedelta_fields:
        rne__shwn = create_timedelta_field_overload(field)
        overload_attribute(SeriesDatetimePropertiesType, field)(rne__shwn)


_install_S_dt_timedelta_fields()


def _install_S_dt_timedelta_methods():
    for method in bodo.hiframes.pd_timestamp_ext.timedelta_methods:
        rne__shwn = create_timedelta_method_overload(method)
        overload_method(SeriesDatetimePropertiesType, method, inline='always')(
            rne__shwn)


_install_S_dt_timedelta_methods()


@overload_method(SeriesDatetimePropertiesType, 'strftime', inline='always',
    no_unliteral=True)
def dt_strftime(S_dt, date_format):
    if not (S_dt.stype.dtype == types.NPDatetime('ns') or isinstance(S_dt.
        stype.dtype, bodo.libs.pd_datetime_arr_ext.PandasDatetimeTZDtype)):
        return
    if types.unliteral(date_format) != types.unicode_type:
        raise BodoError(
            "Series.str.strftime(): 'date_format' argument must be a string")

    def impl(S_dt, date_format):
        vchys__nsqua = S_dt._obj
        luzjr__gpsvn = bodo.hiframes.pd_series_ext.get_series_data(vchys__nsqua
            )
        lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(vchys__nsqua)
        wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(vchys__nsqua)
        numba.parfors.parfor.init_prange()
        ide__oxwpc = len(luzjr__gpsvn)
        ugugz__fyq = bodo.libs.str_arr_ext.pre_alloc_string_array(ide__oxwpc,
            -1)
        for qtaom__mxf in numba.parfors.parfor.internal_prange(ide__oxwpc):
            if bodo.libs.array_kernels.isna(luzjr__gpsvn, qtaom__mxf):
                bodo.libs.array_kernels.setna(ugugz__fyq, qtaom__mxf)
                continue
            ugugz__fyq[qtaom__mxf] = bodo.utils.conversion.box_if_dt64(
                luzjr__gpsvn[qtaom__mxf]).strftime(date_format)
        return bodo.hiframes.pd_series_ext.init_series(ugugz__fyq,
            lxinu__xrj, wxwpc__gzr)
    return impl


@overload_method(SeriesDatetimePropertiesType, 'tz_convert', inline=
    'always', no_unliteral=True)
def overload_dt_tz_convert(S_dt, tz):

    def impl(S_dt, tz):
        vchys__nsqua = S_dt._obj
        ojtxq__rxg = get_series_data(vchys__nsqua).tz_convert(tz)
        lxinu__xrj = get_series_index(vchys__nsqua)
        wxwpc__gzr = get_series_name(vchys__nsqua)
        return init_series(ojtxq__rxg, lxinu__xrj, wxwpc__gzr)
    return impl


def create_timedelta_freq_overload(method):

    def freq_overload(S_dt, freq, ambiguous='raise', nonexistent='raise'):
        if S_dt.stype.dtype != types.NPTimedelta('ns'
            ) and S_dt.stype.dtype != types.NPDatetime('ns'
            ) and not isinstance(S_dt.stype.dtype, bodo.libs.
            pd_datetime_arr_ext.PandasDatetimeTZDtype):
            return
        iehu__czx = isinstance(S_dt.stype.dtype, bodo.libs.
            pd_datetime_arr_ext.PandasDatetimeTZDtype)
        curoq__eyeg = dict(ambiguous=ambiguous, nonexistent=nonexistent)
        psup__vfr = dict(ambiguous='raise', nonexistent='raise')
        check_unsupported_args(f'Series.dt.{method}', curoq__eyeg,
            psup__vfr, package_name='pandas', module_name='Series')
        kgq__uab = (
            "def impl(S_dt, freq, ambiguous='raise', nonexistent='raise'):\n")
        kgq__uab += '    S = S_dt._obj\n'
        kgq__uab += '    A = bodo.hiframes.pd_series_ext.get_series_data(S)\n'
        kgq__uab += (
            '    index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
        kgq__uab += (
            '    name = bodo.hiframes.pd_series_ext.get_series_name(S)\n')
        kgq__uab += '    numba.parfors.parfor.init_prange()\n'
        kgq__uab += '    n = len(A)\n'
        if S_dt.stype.dtype == types.NPTimedelta('ns'):
            kgq__uab += "    B = np.empty(n, np.dtype('timedelta64[ns]'))\n"
        elif iehu__czx:
            kgq__uab += """    B = bodo.libs.pd_datetime_arr_ext.alloc_pd_datetime_array(n, tz_literal)
"""
        else:
            kgq__uab += "    B = np.empty(n, np.dtype('datetime64[ns]'))\n"
        kgq__uab += '    for i in numba.parfors.parfor.internal_prange(n):\n'
        kgq__uab += '        if bodo.libs.array_kernels.isna(A, i):\n'
        kgq__uab += '            bodo.libs.array_kernels.setna(B, i)\n'
        kgq__uab += '            continue\n'
        if S_dt.stype.dtype == types.NPTimedelta('ns'):
            yhix__fqkkl = (
                'bodo.hiframes.pd_timestamp_ext.convert_numpy_timedelta64_to_pd_timedelta'
                )
            cclxk__tuywo = (
                'bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64')
        else:
            yhix__fqkkl = (
                'bodo.hiframes.pd_timestamp_ext.convert_datetime64_to_timestamp'
                )
            cclxk__tuywo = 'bodo.hiframes.pd_timestamp_ext.integer_to_dt64'
        if iehu__czx:
            kgq__uab += f'        B[i] = A[i].{method}(freq)\n'
        else:
            kgq__uab += '        B[i] = {}({}(A[i]).{}(freq).value)\n'.format(
                cclxk__tuywo, yhix__fqkkl, method)
        kgq__uab += (
            '    return bodo.hiframes.pd_series_ext.init_series(B, index, name)\n'
            )
        waa__tgafi = {}
        wrh__dkl = None
        if iehu__czx:
            wrh__dkl = S_dt.stype.dtype.tz
        exec(kgq__uab, {'numba': numba, 'np': np, 'bodo': bodo,
            'tz_literal': wrh__dkl}, waa__tgafi)
        impl = waa__tgafi['impl']
        return impl
    return freq_overload


def _install_S_dt_timedelta_freq_methods():
    iuian__xlwxd = ['ceil', 'floor', 'round']
    for method in iuian__xlwxd:
        rne__shwn = create_timedelta_freq_overload(method)
        overload_method(SeriesDatetimePropertiesType, method, inline='always')(
            rne__shwn)


_install_S_dt_timedelta_freq_methods()


def create_bin_op_overload(op):

    def overload_series_dt_binop(lhs, rhs):
        if bodo.hiframes.pd_series_ext.is_dt64_series_typ(lhs
            ) and bodo.hiframes.pd_series_ext.is_dt64_series_typ(rhs):
            idq__tne = bodo.datetime64ns('NaT')

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                edh__kdjv = bodo.hiframes.pd_series_ext.get_series_data(lhs)
                huu__ghbio = bodo.libs.pd_datetime_arr_ext.unwrap_tz_array(
                    edh__kdjv)
                lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(lhs)
                wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(lhs)
                swt__ydl = bodo.hiframes.pd_series_ext.get_series_data(rhs)
                gyh__oxyt = bodo.libs.pd_datetime_arr_ext.unwrap_tz_array(
                    swt__ydl)
                ide__oxwpc = len(huu__ghbio)
                vchys__nsqua = np.empty(ide__oxwpc, timedelta64_dtype)
                yrhfy__oes = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    idq__tne)
                for qzan__oxgnu in numba.parfors.parfor.internal_prange(
                    ide__oxwpc):
                    thsd__qomtx = (bodo.hiframes.pd_timestamp_ext.
                        dt64_to_integer(huu__ghbio[qzan__oxgnu]))
                    xhr__lokn = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                        gyh__oxyt[qzan__oxgnu])
                    if thsd__qomtx == yrhfy__oes or xhr__lokn == yrhfy__oes:
                        fnh__tzsi = yrhfy__oes
                    else:
                        fnh__tzsi = op(thsd__qomtx, xhr__lokn)
                    vchys__nsqua[qzan__oxgnu
                        ] = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                        fnh__tzsi)
                return bodo.hiframes.pd_series_ext.init_series(vchys__nsqua,
                    lxinu__xrj, wxwpc__gzr)
            return impl
        if bodo.hiframes.pd_series_ext.is_dt64_series_typ(lhs
            ) and bodo.hiframes.pd_series_ext.is_timedelta64_series_typ(rhs):
            idq__tne = bodo.datetime64ns('NaT')

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                qvvr__robsq = bodo.hiframes.pd_series_ext.get_series_data(lhs)
                sqsi__eatiy = bodo.libs.pd_datetime_arr_ext.unwrap_tz_array(
                    qvvr__robsq)
                lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(lhs)
                wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(lhs)
                gyh__oxyt = bodo.hiframes.pd_series_ext.get_series_data(rhs)
                ide__oxwpc = len(sqsi__eatiy)
                vchys__nsqua = np.empty(ide__oxwpc, dt64_dtype)
                yrhfy__oes = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    idq__tne)
                for qzan__oxgnu in numba.parfors.parfor.internal_prange(
                    ide__oxwpc):
                    ann__wwb = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                        sqsi__eatiy[qzan__oxgnu])
                    mlem__ehy = (bodo.hiframes.pd_timestamp_ext.
                        timedelta64_to_integer(gyh__oxyt[qzan__oxgnu]))
                    if ann__wwb == yrhfy__oes or mlem__ehy == yrhfy__oes:
                        fnh__tzsi = yrhfy__oes
                    else:
                        fnh__tzsi = op(ann__wwb, mlem__ehy)
                    vchys__nsqua[qzan__oxgnu
                        ] = bodo.hiframes.pd_timestamp_ext.integer_to_dt64(
                        fnh__tzsi)
                return bodo.hiframes.pd_series_ext.init_series(vchys__nsqua,
                    lxinu__xrj, wxwpc__gzr)
            return impl
        if bodo.hiframes.pd_series_ext.is_dt64_series_typ(rhs
            ) and bodo.hiframes.pd_series_ext.is_timedelta64_series_typ(lhs):
            idq__tne = bodo.datetime64ns('NaT')

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                qvvr__robsq = bodo.hiframes.pd_series_ext.get_series_data(rhs)
                sqsi__eatiy = bodo.libs.pd_datetime_arr_ext.unwrap_tz_array(
                    qvvr__robsq)
                lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(rhs)
                wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(rhs)
                gyh__oxyt = bodo.hiframes.pd_series_ext.get_series_data(lhs)
                ide__oxwpc = len(sqsi__eatiy)
                vchys__nsqua = np.empty(ide__oxwpc, dt64_dtype)
                yrhfy__oes = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    idq__tne)
                for qzan__oxgnu in numba.parfors.parfor.internal_prange(
                    ide__oxwpc):
                    ann__wwb = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                        sqsi__eatiy[qzan__oxgnu])
                    mlem__ehy = (bodo.hiframes.pd_timestamp_ext.
                        timedelta64_to_integer(gyh__oxyt[qzan__oxgnu]))
                    if ann__wwb == yrhfy__oes or mlem__ehy == yrhfy__oes:
                        fnh__tzsi = yrhfy__oes
                    else:
                        fnh__tzsi = op(ann__wwb, mlem__ehy)
                    vchys__nsqua[qzan__oxgnu
                        ] = bodo.hiframes.pd_timestamp_ext.integer_to_dt64(
                        fnh__tzsi)
                return bodo.hiframes.pd_series_ext.init_series(vchys__nsqua,
                    lxinu__xrj, wxwpc__gzr)
            return impl
        if bodo.hiframes.pd_series_ext.is_dt64_series_typ(lhs
            ) and rhs == bodo.hiframes.pd_timestamp_ext.pd_timestamp_tz_naive_type:
            idq__tne = bodo.datetime64ns('NaT')

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                qvvr__robsq = bodo.hiframes.pd_series_ext.get_series_data(lhs)
                sqsi__eatiy = bodo.libs.pd_datetime_arr_ext.unwrap_tz_array(
                    qvvr__robsq)
                lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(lhs)
                wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(lhs)
                ide__oxwpc = len(sqsi__eatiy)
                vchys__nsqua = np.empty(ide__oxwpc, timedelta64_dtype)
                yrhfy__oes = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    idq__tne)
                xezxg__jguxx = rhs.value
                for qzan__oxgnu in numba.parfors.parfor.internal_prange(
                    ide__oxwpc):
                    ann__wwb = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                        sqsi__eatiy[qzan__oxgnu])
                    if ann__wwb == yrhfy__oes or xezxg__jguxx == yrhfy__oes:
                        fnh__tzsi = yrhfy__oes
                    else:
                        fnh__tzsi = op(ann__wwb, xezxg__jguxx)
                    vchys__nsqua[qzan__oxgnu
                        ] = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                        fnh__tzsi)
                return bodo.hiframes.pd_series_ext.init_series(vchys__nsqua,
                    lxinu__xrj, wxwpc__gzr)
            return impl
        if bodo.hiframes.pd_series_ext.is_dt64_series_typ(rhs
            ) and lhs == bodo.hiframes.pd_timestamp_ext.pd_timestamp_tz_naive_type:
            idq__tne = bodo.datetime64ns('NaT')

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                qvvr__robsq = bodo.hiframes.pd_series_ext.get_series_data(rhs)
                sqsi__eatiy = bodo.libs.pd_datetime_arr_ext.unwrap_tz_array(
                    qvvr__robsq)
                lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(rhs)
                wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(rhs)
                ide__oxwpc = len(sqsi__eatiy)
                vchys__nsqua = np.empty(ide__oxwpc, timedelta64_dtype)
                yrhfy__oes = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    idq__tne)
                xezxg__jguxx = lhs.value
                for qzan__oxgnu in numba.parfors.parfor.internal_prange(
                    ide__oxwpc):
                    ann__wwb = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                        sqsi__eatiy[qzan__oxgnu])
                    if xezxg__jguxx == yrhfy__oes or ann__wwb == yrhfy__oes:
                        fnh__tzsi = yrhfy__oes
                    else:
                        fnh__tzsi = op(xezxg__jguxx, ann__wwb)
                    vchys__nsqua[qzan__oxgnu
                        ] = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                        fnh__tzsi)
                return bodo.hiframes.pd_series_ext.init_series(vchys__nsqua,
                    lxinu__xrj, wxwpc__gzr)
            return impl
        if (bodo.hiframes.pd_series_ext.is_dt64_series_typ(lhs) and rhs ==
            bodo.hiframes.datetime_timedelta_ext.datetime_timedelta_type):
            idq__tne = bodo.datetime64ns('NaT')

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                qvvr__robsq = bodo.hiframes.pd_series_ext.get_series_data(lhs)
                sqsi__eatiy = bodo.libs.pd_datetime_arr_ext.unwrap_tz_array(
                    qvvr__robsq)
                lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(lhs)
                wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(lhs)
                ide__oxwpc = len(sqsi__eatiy)
                vchys__nsqua = np.empty(ide__oxwpc, dt64_dtype)
                yrhfy__oes = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    idq__tne)
                yycvu__pbqvg = (bodo.hiframes.pd_timestamp_ext.
                    datetime_timedelta_to_timedelta64(rhs))
                mlem__ehy = (bodo.hiframes.pd_timestamp_ext.
                    timedelta64_to_integer(yycvu__pbqvg))
                for qzan__oxgnu in numba.parfors.parfor.internal_prange(
                    ide__oxwpc):
                    ann__wwb = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                        sqsi__eatiy[qzan__oxgnu])
                    if ann__wwb == yrhfy__oes or mlem__ehy == yrhfy__oes:
                        fnh__tzsi = yrhfy__oes
                    else:
                        fnh__tzsi = op(ann__wwb, mlem__ehy)
                    vchys__nsqua[qzan__oxgnu
                        ] = bodo.hiframes.pd_timestamp_ext.integer_to_dt64(
                        fnh__tzsi)
                return bodo.hiframes.pd_series_ext.init_series(vchys__nsqua,
                    lxinu__xrj, wxwpc__gzr)
            return impl
        if (bodo.hiframes.pd_series_ext.is_dt64_series_typ(rhs) and lhs ==
            bodo.hiframes.datetime_timedelta_ext.datetime_timedelta_type):
            idq__tne = bodo.datetime64ns('NaT')

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                qvvr__robsq = bodo.hiframes.pd_series_ext.get_series_data(rhs)
                sqsi__eatiy = bodo.libs.pd_datetime_arr_ext.unwrap_tz_array(
                    qvvr__robsq)
                lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(rhs)
                wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(rhs)
                ide__oxwpc = len(sqsi__eatiy)
                vchys__nsqua = np.empty(ide__oxwpc, dt64_dtype)
                yrhfy__oes = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    idq__tne)
                yycvu__pbqvg = (bodo.hiframes.pd_timestamp_ext.
                    datetime_timedelta_to_timedelta64(lhs))
                mlem__ehy = (bodo.hiframes.pd_timestamp_ext.
                    timedelta64_to_integer(yycvu__pbqvg))
                for qzan__oxgnu in numba.parfors.parfor.internal_prange(
                    ide__oxwpc):
                    ann__wwb = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                        sqsi__eatiy[qzan__oxgnu])
                    if ann__wwb == yrhfy__oes or mlem__ehy == yrhfy__oes:
                        fnh__tzsi = yrhfy__oes
                    else:
                        fnh__tzsi = op(ann__wwb, mlem__ehy)
                    vchys__nsqua[qzan__oxgnu
                        ] = bodo.hiframes.pd_timestamp_ext.integer_to_dt64(
                        fnh__tzsi)
                return bodo.hiframes.pd_series_ext.init_series(vchys__nsqua,
                    lxinu__xrj, wxwpc__gzr)
            return impl
        if (bodo.hiframes.pd_series_ext.is_dt64_series_typ(lhs) and rhs ==
            bodo.hiframes.datetime_datetime_ext.datetime_datetime_type):
            idq__tne = bodo.datetime64ns('NaT')

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                qvvr__robsq = bodo.hiframes.pd_series_ext.get_series_data(lhs)
                sqsi__eatiy = bodo.libs.pd_datetime_arr_ext.unwrap_tz_array(
                    qvvr__robsq)
                lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(lhs)
                wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(lhs)
                ide__oxwpc = len(sqsi__eatiy)
                vchys__nsqua = np.empty(ide__oxwpc, timedelta64_dtype)
                yrhfy__oes = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    idq__tne)
                bzkd__gjwm = (bodo.hiframes.pd_timestamp_ext.
                    datetime_datetime_to_dt64(rhs))
                ann__wwb = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    bzkd__gjwm)
                for qzan__oxgnu in numba.parfors.parfor.internal_prange(
                    ide__oxwpc):
                    azowv__awhqe = (bodo.hiframes.pd_timestamp_ext.
                        dt64_to_integer(sqsi__eatiy[qzan__oxgnu]))
                    if azowv__awhqe == yrhfy__oes or ann__wwb == yrhfy__oes:
                        fnh__tzsi = yrhfy__oes
                    else:
                        fnh__tzsi = op(azowv__awhqe, ann__wwb)
                    vchys__nsqua[qzan__oxgnu
                        ] = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                        fnh__tzsi)
                return bodo.hiframes.pd_series_ext.init_series(vchys__nsqua,
                    lxinu__xrj, wxwpc__gzr)
            return impl
        if (bodo.hiframes.pd_series_ext.is_dt64_series_typ(rhs) and lhs ==
            bodo.hiframes.datetime_datetime_ext.datetime_datetime_type):
            idq__tne = bodo.datetime64ns('NaT')

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                qvvr__robsq = bodo.hiframes.pd_series_ext.get_series_data(rhs)
                sqsi__eatiy = bodo.libs.pd_datetime_arr_ext.unwrap_tz_array(
                    qvvr__robsq)
                lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(rhs)
                wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(rhs)
                ide__oxwpc = len(sqsi__eatiy)
                vchys__nsqua = np.empty(ide__oxwpc, timedelta64_dtype)
                yrhfy__oes = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    idq__tne)
                bzkd__gjwm = (bodo.hiframes.pd_timestamp_ext.
                    datetime_datetime_to_dt64(lhs))
                ann__wwb = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    bzkd__gjwm)
                for qzan__oxgnu in numba.parfors.parfor.internal_prange(
                    ide__oxwpc):
                    azowv__awhqe = (bodo.hiframes.pd_timestamp_ext.
                        dt64_to_integer(sqsi__eatiy[qzan__oxgnu]))
                    if ann__wwb == yrhfy__oes or azowv__awhqe == yrhfy__oes:
                        fnh__tzsi = yrhfy__oes
                    else:
                        fnh__tzsi = op(ann__wwb, azowv__awhqe)
                    vchys__nsqua[qzan__oxgnu
                        ] = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                        fnh__tzsi)
                return bodo.hiframes.pd_series_ext.init_series(vchys__nsqua,
                    lxinu__xrj, wxwpc__gzr)
            return impl
        if (bodo.hiframes.pd_series_ext.is_timedelta64_series_typ(lhs) and 
            rhs == bodo.hiframes.datetime_timedelta_ext.datetime_timedelta_type
            ):
            idq__tne = lhs.dtype('NaT')

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                sqsi__eatiy = bodo.hiframes.pd_series_ext.get_series_data(lhs)
                lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(lhs)
                wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(lhs)
                ide__oxwpc = len(sqsi__eatiy)
                vchys__nsqua = np.empty(ide__oxwpc, timedelta64_dtype)
                yrhfy__oes = (bodo.hiframes.pd_timestamp_ext.
                    timedelta64_to_integer(idq__tne))
                yycvu__pbqvg = (bodo.hiframes.pd_timestamp_ext.
                    datetime_timedelta_to_timedelta64(rhs))
                mlem__ehy = (bodo.hiframes.pd_timestamp_ext.
                    timedelta64_to_integer(yycvu__pbqvg))
                for qzan__oxgnu in numba.parfors.parfor.internal_prange(
                    ide__oxwpc):
                    nfeud__wnx = (bodo.hiframes.pd_timestamp_ext.
                        timedelta64_to_integer(sqsi__eatiy[qzan__oxgnu]))
                    if mlem__ehy == yrhfy__oes or nfeud__wnx == yrhfy__oes:
                        fnh__tzsi = yrhfy__oes
                    else:
                        fnh__tzsi = op(nfeud__wnx, mlem__ehy)
                    vchys__nsqua[qzan__oxgnu
                        ] = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                        fnh__tzsi)
                return bodo.hiframes.pd_series_ext.init_series(vchys__nsqua,
                    lxinu__xrj, wxwpc__gzr)
            return impl
        if (bodo.hiframes.pd_series_ext.is_timedelta64_series_typ(rhs) and 
            lhs == bodo.hiframes.datetime_timedelta_ext.datetime_timedelta_type
            ):
            idq__tne = rhs.dtype('NaT')

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                sqsi__eatiy = bodo.hiframes.pd_series_ext.get_series_data(rhs)
                lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(rhs)
                wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(rhs)
                ide__oxwpc = len(sqsi__eatiy)
                vchys__nsqua = np.empty(ide__oxwpc, timedelta64_dtype)
                yrhfy__oes = (bodo.hiframes.pd_timestamp_ext.
                    timedelta64_to_integer(idq__tne))
                yycvu__pbqvg = (bodo.hiframes.pd_timestamp_ext.
                    datetime_timedelta_to_timedelta64(lhs))
                mlem__ehy = (bodo.hiframes.pd_timestamp_ext.
                    timedelta64_to_integer(yycvu__pbqvg))
                for qzan__oxgnu in numba.parfors.parfor.internal_prange(
                    ide__oxwpc):
                    nfeud__wnx = (bodo.hiframes.pd_timestamp_ext.
                        timedelta64_to_integer(sqsi__eatiy[qzan__oxgnu]))
                    if mlem__ehy == yrhfy__oes or nfeud__wnx == yrhfy__oes:
                        fnh__tzsi = yrhfy__oes
                    else:
                        fnh__tzsi = op(mlem__ehy, nfeud__wnx)
                    vchys__nsqua[qzan__oxgnu
                        ] = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                        fnh__tzsi)
                return bodo.hiframes.pd_series_ext.init_series(vchys__nsqua,
                    lxinu__xrj, wxwpc__gzr)
            return impl
        raise BodoError(f'{op} not supported for data types {lhs} and {rhs}.')
    return overload_series_dt_binop


def create_cmp_op_overload(op):

    def overload_series_dt64_cmp(lhs, rhs):
        if op == operator.ne:
            mdd__ket = True
        else:
            mdd__ket = False
        if (bodo.hiframes.pd_series_ext.is_timedelta64_series_typ(lhs) and 
            rhs == bodo.hiframes.datetime_timedelta_ext.datetime_timedelta_type
            ):
            idq__tne = lhs.dtype('NaT')

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                sqsi__eatiy = bodo.hiframes.pd_series_ext.get_series_data(lhs)
                lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(lhs)
                wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(lhs)
                ide__oxwpc = len(sqsi__eatiy)
                jst__toua = bodo.libs.bool_arr_ext.alloc_bool_array(ide__oxwpc)
                yrhfy__oes = (bodo.hiframes.pd_timestamp_ext.
                    timedelta64_to_integer(idq__tne))
                ulu__knpai = (bodo.hiframes.pd_timestamp_ext.
                    datetime_timedelta_to_timedelta64(rhs))
                xwr__tuats = (bodo.hiframes.pd_timestamp_ext.
                    timedelta64_to_integer(ulu__knpai))
                for qzan__oxgnu in numba.parfors.parfor.internal_prange(
                    ide__oxwpc):
                    zyse__lnn = (bodo.hiframes.pd_timestamp_ext.
                        timedelta64_to_integer(sqsi__eatiy[qzan__oxgnu]))
                    if zyse__lnn == yrhfy__oes or xwr__tuats == yrhfy__oes:
                        fnh__tzsi = mdd__ket
                    else:
                        fnh__tzsi = op(zyse__lnn, xwr__tuats)
                    jst__toua[qzan__oxgnu] = fnh__tzsi
                return bodo.hiframes.pd_series_ext.init_series(jst__toua,
                    lxinu__xrj, wxwpc__gzr)
            return impl
        if (bodo.hiframes.pd_series_ext.is_timedelta64_series_typ(rhs) and 
            lhs == bodo.hiframes.datetime_timedelta_ext.datetime_timedelta_type
            ):
            idq__tne = rhs.dtype('NaT')

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                sqsi__eatiy = bodo.hiframes.pd_series_ext.get_series_data(rhs)
                lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(rhs)
                wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(rhs)
                ide__oxwpc = len(sqsi__eatiy)
                jst__toua = bodo.libs.bool_arr_ext.alloc_bool_array(ide__oxwpc)
                yrhfy__oes = (bodo.hiframes.pd_timestamp_ext.
                    timedelta64_to_integer(idq__tne))
                eflx__hcokh = (bodo.hiframes.pd_timestamp_ext.
                    datetime_timedelta_to_timedelta64(lhs))
                zyse__lnn = (bodo.hiframes.pd_timestamp_ext.
                    timedelta64_to_integer(eflx__hcokh))
                for qzan__oxgnu in numba.parfors.parfor.internal_prange(
                    ide__oxwpc):
                    xwr__tuats = (bodo.hiframes.pd_timestamp_ext.
                        timedelta64_to_integer(sqsi__eatiy[qzan__oxgnu]))
                    if zyse__lnn == yrhfy__oes or xwr__tuats == yrhfy__oes:
                        fnh__tzsi = mdd__ket
                    else:
                        fnh__tzsi = op(zyse__lnn, xwr__tuats)
                    jst__toua[qzan__oxgnu] = fnh__tzsi
                return bodo.hiframes.pd_series_ext.init_series(jst__toua,
                    lxinu__xrj, wxwpc__gzr)
            return impl
        if bodo.hiframes.pd_series_ext.is_dt64_series_typ(lhs
            ) and rhs == bodo.hiframes.pd_timestamp_ext.pd_timestamp_tz_naive_type:
            idq__tne = bodo.datetime64ns('NaT')

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                qvvr__robsq = bodo.hiframes.pd_series_ext.get_series_data(lhs)
                sqsi__eatiy = bodo.libs.pd_datetime_arr_ext.unwrap_tz_array(
                    qvvr__robsq)
                lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(lhs)
                wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(lhs)
                ide__oxwpc = len(sqsi__eatiy)
                jst__toua = bodo.libs.bool_arr_ext.alloc_bool_array(ide__oxwpc)
                yrhfy__oes = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    idq__tne)
                for qzan__oxgnu in numba.parfors.parfor.internal_prange(
                    ide__oxwpc):
                    zyse__lnn = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                        sqsi__eatiy[qzan__oxgnu])
                    if zyse__lnn == yrhfy__oes or rhs.value == yrhfy__oes:
                        fnh__tzsi = mdd__ket
                    else:
                        fnh__tzsi = op(zyse__lnn, rhs.value)
                    jst__toua[qzan__oxgnu] = fnh__tzsi
                return bodo.hiframes.pd_series_ext.init_series(jst__toua,
                    lxinu__xrj, wxwpc__gzr)
            return impl
        if (lhs == bodo.hiframes.pd_timestamp_ext.
            pd_timestamp_tz_naive_type and bodo.hiframes.pd_series_ext.
            is_dt64_series_typ(rhs)):
            idq__tne = bodo.datetime64ns('NaT')

            def impl(lhs, rhs):
                numba.parfors.parfor.init_prange()
                qvvr__robsq = bodo.hiframes.pd_series_ext.get_series_data(rhs)
                sqsi__eatiy = bodo.libs.pd_datetime_arr_ext.unwrap_tz_array(
                    qvvr__robsq)
                lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(rhs)
                wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(rhs)
                ide__oxwpc = len(sqsi__eatiy)
                jst__toua = bodo.libs.bool_arr_ext.alloc_bool_array(ide__oxwpc)
                yrhfy__oes = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    idq__tne)
                for qzan__oxgnu in numba.parfors.parfor.internal_prange(
                    ide__oxwpc):
                    xwr__tuats = (bodo.hiframes.pd_timestamp_ext.
                        dt64_to_integer(sqsi__eatiy[qzan__oxgnu]))
                    if xwr__tuats == yrhfy__oes or lhs.value == yrhfy__oes:
                        fnh__tzsi = mdd__ket
                    else:
                        fnh__tzsi = op(lhs.value, xwr__tuats)
                    jst__toua[qzan__oxgnu] = fnh__tzsi
                return bodo.hiframes.pd_series_ext.init_series(jst__toua,
                    lxinu__xrj, wxwpc__gzr)
            return impl
        if bodo.hiframes.pd_series_ext.is_dt64_series_typ(lhs) and (rhs ==
            bodo.libs.str_ext.string_type or bodo.utils.typing.
            is_overload_constant_str(rhs)):
            idq__tne = bodo.datetime64ns('NaT')

            def impl(lhs, rhs):
                qvvr__robsq = bodo.hiframes.pd_series_ext.get_series_data(lhs)
                sqsi__eatiy = bodo.libs.pd_datetime_arr_ext.unwrap_tz_array(
                    qvvr__robsq)
                lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(lhs)
                wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(lhs)
                numba.parfors.parfor.init_prange()
                ide__oxwpc = len(sqsi__eatiy)
                jst__toua = bodo.libs.bool_arr_ext.alloc_bool_array(ide__oxwpc)
                yrhfy__oes = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    idq__tne)
                dsq__acef = bodo.hiframes.pd_timestamp_ext.parse_datetime_str(
                    rhs)
                yis__abeak = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    dsq__acef)
                for qzan__oxgnu in numba.parfors.parfor.internal_prange(
                    ide__oxwpc):
                    zyse__lnn = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                        sqsi__eatiy[qzan__oxgnu])
                    if zyse__lnn == yrhfy__oes or yis__abeak == yrhfy__oes:
                        fnh__tzsi = mdd__ket
                    else:
                        fnh__tzsi = op(zyse__lnn, yis__abeak)
                    jst__toua[qzan__oxgnu] = fnh__tzsi
                return bodo.hiframes.pd_series_ext.init_series(jst__toua,
                    lxinu__xrj, wxwpc__gzr)
            return impl
        if bodo.hiframes.pd_series_ext.is_dt64_series_typ(rhs) and (lhs ==
            bodo.libs.str_ext.string_type or bodo.utils.typing.
            is_overload_constant_str(lhs)):
            idq__tne = bodo.datetime64ns('NaT')

            def impl(lhs, rhs):
                qvvr__robsq = bodo.hiframes.pd_series_ext.get_series_data(rhs)
                sqsi__eatiy = bodo.libs.pd_datetime_arr_ext.unwrap_tz_array(
                    qvvr__robsq)
                lxinu__xrj = bodo.hiframes.pd_series_ext.get_series_index(rhs)
                wxwpc__gzr = bodo.hiframes.pd_series_ext.get_series_name(rhs)
                numba.parfors.parfor.init_prange()
                ide__oxwpc = len(sqsi__eatiy)
                jst__toua = bodo.libs.bool_arr_ext.alloc_bool_array(ide__oxwpc)
                yrhfy__oes = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    idq__tne)
                dsq__acef = bodo.hiframes.pd_timestamp_ext.parse_datetime_str(
                    lhs)
                yis__abeak = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    dsq__acef)
                for qzan__oxgnu in numba.parfors.parfor.internal_prange(
                    ide__oxwpc):
                    bzkd__gjwm = (bodo.hiframes.pd_timestamp_ext.
                        dt64_to_integer(sqsi__eatiy[qzan__oxgnu]))
                    if bzkd__gjwm == yrhfy__oes or yis__abeak == yrhfy__oes:
                        fnh__tzsi = mdd__ket
                    else:
                        fnh__tzsi = op(yis__abeak, bzkd__gjwm)
                    jst__toua[qzan__oxgnu] = fnh__tzsi
                return bodo.hiframes.pd_series_ext.init_series(jst__toua,
                    lxinu__xrj, wxwpc__gzr)
            return impl
        raise BodoError(
            f'{op} operator not supported for data types {lhs} and {rhs}.')
    return overload_series_dt64_cmp


series_dt_unsupported_methods = {'to_period', 'to_pydatetime',
    'tz_localize', 'asfreq', 'to_timestamp'}
series_dt_unsupported_attrs = {'time', 'timetz', 'tz', 'freq', 'qyear',
    'start_time', 'end_time'}


def _install_series_dt_unsupported():
    for wgb__derqs in series_dt_unsupported_attrs:
        meadj__zpp = 'Series.dt.' + wgb__derqs
        overload_attribute(SeriesDatetimePropertiesType, wgb__derqs)(
            create_unsupported_overload(meadj__zpp))
    for zmf__lwh in series_dt_unsupported_methods:
        meadj__zpp = 'Series.dt.' + zmf__lwh
        overload_method(SeriesDatetimePropertiesType, zmf__lwh,
            no_unliteral=True)(create_unsupported_overload(meadj__zpp))


_install_series_dt_unsupported()
