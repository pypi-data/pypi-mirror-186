"""
Common utilities for all BodoSQL array kernels
"""
import math
import re
import numba
import numpy as np
import pandas as pd
import pyarrow as pa
from numba.core import types
import bodo
from bodo.hiframes.datetime_timedelta_ext import PDTimeDeltaType
from bodo.hiframes.pd_series_ext import is_datetime_date_series_typ, is_timedelta64_series_typ, pd_timedelta_type, pd_timestamp_tz_naive_type
from bodo.utils.typing import is_overload_bool, is_overload_constant_bool, is_overload_constant_bytes, is_overload_constant_number, is_overload_constant_str, is_overload_float, is_overload_int, is_overload_none, raise_bodo_error


def indent_block(text, indentation):
    if text is None:
        return ''
    zexra__rnyg = text.splitlines()[0]
    i = len(zexra__rnyg) - len(zexra__rnyg.lstrip())
    return '\n'.join([(' ' * indentation + ykyyx__xfncf[i:]) for
        ykyyx__xfncf in text.splitlines()]) + '\n'


def gen_vectorized(arg_names, arg_types, propagate_null, scalar_text,
    out_dtype, arg_string=None, arg_sources=None, array_override=None,
    support_dict_encoding=True, may_cause_duplicate_dict_array_values=False,
    prefix_code=None, suffix_code=None, res_list=False, extra_globals=None,
    alloc_array_scalars=True, synthesize_dict_if_vector=None,
    synthesize_dict_setup_text=None, synthesize_dict_scalar_text=None,
    synthesize_dict_global=False, synthesize_dict_unique=False):
    assert not (res_list and support_dict_encoding
        ), 'Cannot use res_list with support_dict_encoding'
    evo__atdy = [bodo.utils.utils.is_array_typ(dzyb__orptk, True) for
        dzyb__orptk in arg_types]
    joq__ezebc = not any(evo__atdy)
    bgh__fvupx = any([propagate_null[i] for i in range(len(arg_types)) if 
        arg_types[i] == bodo.none])
    cwwcx__upo = False
    if synthesize_dict_if_vector is not None:
        assert synthesize_dict_setup_text is not None, 'synthesize_dict_setup_text must be provided if synthesize_dict_if_vector is provided'
        assert synthesize_dict_scalar_text is not None, 'synthesize_dict_scalar_text must be provided if synthesize_dict_if_vector is provided'
        cwwcx__upo = True
        for i in range(len(arg_types)):
            if evo__atdy[i] and synthesize_dict_if_vector[i] == 'S':
                cwwcx__upo = False
            if not evo__atdy[i] and synthesize_dict_if_vector[i] == 'V':
                cwwcx__upo = False
    ombs__etywu = 0
    qifes__zjao = -1
    for i in range(len(arg_types)):
        if bodo.utils.utils.is_array_typ(arg_types[i], False):
            ombs__etywu += 1
            if arg_types[i] == bodo.dict_str_arr_type:
                qifes__zjao = i
        elif bodo.utils.utils.is_array_typ(arg_types[i], True):
            ombs__etywu += 1
            if arg_types[i].data == bodo.dict_str_arr_type:
                qifes__zjao = i
    ceac__ncynf = (support_dict_encoding and ombs__etywu == 1 and 
        qifes__zjao >= 0)
    vesj__fcc = ceac__ncynf and out_dtype == bodo.string_array_type and (any
        (arg_types[i] == bodo.none and propagate_null[i] for i in range(len
        (arg_types))) or 'bodo.libs.array_kernels.setna' in scalar_text)
    if arg_string is None:
        arg_string = ', '.join(arg_names)
    gaa__ywzw = f'def impl({arg_string}):\n'
    if arg_sources is not None:
        for hjqb__iki, rafgk__pdkr in arg_sources.items():
            gaa__ywzw += f'   {hjqb__iki} = {rafgk__pdkr}\n'
    if joq__ezebc and array_override == None:
        if bgh__fvupx:
            gaa__ywzw += '   return None'
        else:
            gaa__ywzw += indent_block(prefix_code, 3)
            for i in range(len(arg_names)):
                gaa__ywzw += f'   arg{i} = {arg_names[i]}\n'
            sdrqh__wsa = scalar_text.replace('res[i] =', 'answer =').replace(
                'bodo.libs.array_kernels.setna(res, i)', 'return None')
            gaa__ywzw += indent_block(sdrqh__wsa, 3)
            gaa__ywzw += '   return answer'
    else:
        for i in range(len(arg_names)):
            if bodo.hiframes.pd_series_ext.is_series_type(arg_types[i]):
                gaa__ywzw += f"""   {arg_names[i]} = bodo.hiframes.pd_series_ext.get_series_data({arg_names[i]})
"""
        if array_override != None:
            dxry__wmnq = f'len({array_override})'
        else:
            for i in range(len(arg_names)):
                if evo__atdy[i]:
                    dxry__wmnq = f'len({arg_names[i]})'
                    break
        if ceac__ncynf:
            if out_dtype == bodo.string_array_type:
                gaa__ywzw += (
                    f'   indices = {arg_names[qifes__zjao]}._indices.copy()\n')
                gaa__ywzw += (
                    f'   has_global = {arg_names[qifes__zjao]}._has_global_dictionary\n'
                    )
                if may_cause_duplicate_dict_array_values:
                    gaa__ywzw += f'   is_dict_unique = False\n'
                else:
                    gaa__ywzw += f"""   is_dict_unique = {arg_names[qifes__zjao]}._has_deduped_local_dictionary
"""
                gaa__ywzw += (
                    f'   {arg_names[i]} = {arg_names[qifes__zjao]}._data\n')
            else:
                gaa__ywzw += (
                    f'   indices = {arg_names[qifes__zjao]}._indices\n')
                gaa__ywzw += (
                    f'   {arg_names[i]} = {arg_names[qifes__zjao]}._data\n')
        gaa__ywzw += f'   n = {dxry__wmnq}\n'
        if prefix_code is not None and not bgh__fvupx:
            gaa__ywzw += indent_block(prefix_code, 3)
        if cwwcx__upo:
            gaa__ywzw += indent_block(synthesize_dict_setup_text, 3)
            out_dtype = bodo.libs.dict_arr_ext.dict_indices_arr_type
            gaa__ywzw += (
                '   res = bodo.utils.utils.alloc_type(n, out_dtype, (-1,))\n')
            gaa__ywzw += '   numba.parfors.parfor.init_prange()\n'
            gaa__ywzw += (
                '   for i in numba.parfors.parfor.internal_prange(n):\n')
        elif ceac__ncynf:
            suuqg__efq = 'n' if propagate_null[qifes__zjao] else '(n + 1)'
            if not propagate_null[qifes__zjao]:
                zvez__ybwag = arg_names[qifes__zjao]
                gaa__ywzw += f"""   {zvez__ybwag} = bodo.libs.array_kernels.concat([{zvez__ybwag}, bodo.libs.array_kernels.gen_na_array(1, {zvez__ybwag})])
"""
            if out_dtype == bodo.string_array_type:
                gaa__ywzw += f"""   res = bodo.libs.str_arr_ext.pre_alloc_string_array({suuqg__efq}, -1)
"""
            else:
                gaa__ywzw += f"""   res = bodo.utils.utils.alloc_type({suuqg__efq}, out_dtype, (-1,))
"""
            gaa__ywzw += f'   for i in range({suuqg__efq}):\n'
        elif res_list:
            gaa__ywzw += '   res = []\n'
            gaa__ywzw += '   for i in range(n):\n'
        else:
            gaa__ywzw += (
                '   res = bodo.utils.utils.alloc_type(n, out_dtype, (-1,))\n')
            gaa__ywzw += '   numba.parfors.parfor.init_prange()\n'
            gaa__ywzw += (
                '   for i in numba.parfors.parfor.internal_prange(n):\n')
        if bgh__fvupx:
            gaa__ywzw += f'      bodo.libs.array_kernels.setna(res, i)\n'
        else:
            for i in range(len(arg_names)):
                if evo__atdy[i]:
                    if propagate_null[i]:
                        gaa__ywzw += (
                            f'      if bodo.libs.array_kernels.isna({arg_names[i]}, i):\n'
                            )
                        if res_list:
                            gaa__ywzw += '         res.append(None)\n'
                        else:
                            gaa__ywzw += (
                                '         bodo.libs.array_kernels.setna(res, i)\n'
                                )
                        gaa__ywzw += '         continue\n'
            for i in range(len(arg_names)):
                if evo__atdy[i]:
                    if alloc_array_scalars:
                        gaa__ywzw += f'      arg{i} = {arg_names[i]}[i]\n'
                else:
                    gaa__ywzw += f'      arg{i} = {arg_names[i]}\n'
            if not cwwcx__upo:
                gaa__ywzw += indent_block(scalar_text, 6)
            else:
                gaa__ywzw += indent_block(synthesize_dict_scalar_text, 6)
        if ceac__ncynf:
            if vesj__fcc:
                gaa__ywzw += '   numba.parfors.parfor.init_prange()\n'
                gaa__ywzw += (
                    '   for i in numba.parfors.parfor.internal_prange(len(indices)):\n'
                    )
                gaa__ywzw += (
                    '      if not bodo.libs.array_kernels.isna(indices, i):\n')
                gaa__ywzw += '         loc = indices[i]\n'
                gaa__ywzw += (
                    '         if bodo.libs.array_kernels.isna(res, loc):\n')
                gaa__ywzw += (
                    '            bodo.libs.array_kernels.setna(indices, i)\n')
            if out_dtype == bodo.string_array_type:
                gaa__ywzw += """   res = bodo.libs.dict_arr_ext.init_dict_arr(res, indices, has_global, is_dict_unique)
"""
            else:
                gaa__ywzw += """   res2 = bodo.utils.utils.alloc_type(len(indices), out_dtype, (-1,))
"""
                gaa__ywzw += '   numba.parfors.parfor.init_prange()\n'
                gaa__ywzw += (
                    '   for i in numba.parfors.parfor.internal_prange(len(indices)):\n'
                    )
                if propagate_null[qifes__zjao]:
                    gaa__ywzw += (
                        '      if bodo.libs.array_kernels.isna(indices, i):\n')
                    gaa__ywzw += (
                        '         bodo.libs.array_kernels.setna(res2, i)\n')
                    gaa__ywzw += '         continue\n'
                    gaa__ywzw += '      loc = indices[i]\n'
                else:
                    gaa__ywzw += """      loc = n if bodo.libs.array_kernels.isna(indices, i) else indices[i]
"""
                gaa__ywzw += (
                    '      if bodo.libs.array_kernels.isna(res, loc):\n')
                gaa__ywzw += (
                    '         bodo.libs.array_kernels.setna(res2, i)\n')
                gaa__ywzw += '      else:\n'
                gaa__ywzw += '         res2[i] = res[loc]\n'
                gaa__ywzw += '   res = res2\n'
        gaa__ywzw += indent_block(suffix_code, 3)
        if cwwcx__upo:
            gaa__ywzw += f"""   return bodo.libs.dict_arr_ext.init_dict_arr(dict_res, res, {synthesize_dict_global}, {synthesize_dict_unique})
"""
        else:
            gaa__ywzw += '   return res'
    qdhlp__tmd = {}
    rxxbm__osvel = {'bodo': bodo, 'math': math, 'numba': numba, 're': re,
        'np': np, 'out_dtype': out_dtype, 'pd': pd}
    if not extra_globals is None:
        rxxbm__osvel.update(extra_globals)
    exec(gaa__ywzw, rxxbm__osvel, qdhlp__tmd)
    kmtq__gmra = qdhlp__tmd['impl']
    return kmtq__gmra


def unopt_argument(func_name, arg_names, i, container_arg=0,
    container_length=None):
    if container_length != None:
        kyn__yivs = [(f'{arg_names[i]}{[ufmx__tpdd]}' if ufmx__tpdd !=
            container_arg else 'None') for ufmx__tpdd in range(
            container_length)]
        cbxio__mxgqb = ',' if container_length != 0 else ''
        mhti__innx = f"({', '.join(kyn__yivs)}{cbxio__mxgqb})"
        vyka__oddr = [(f'{arg_names[i]}{[ufmx__tpdd]}' if ufmx__tpdd !=
            container_arg else
            f'bodo.utils.indexing.unoptional({arg_names[i]}[{ufmx__tpdd}])'
            ) for ufmx__tpdd in range(container_length)]
        gvbo__kcox = f"({', '.join(vyka__oddr)}{cbxio__mxgqb})"
        hndlz__zcxo = [(arg_names[ufmx__tpdd] if ufmx__tpdd != i else
            mhti__innx) for ufmx__tpdd in range(len(arg_names))]
        atyi__ely = [(arg_names[ufmx__tpdd] if ufmx__tpdd != i else
            gvbo__kcox) for ufmx__tpdd in range(len(arg_names))]
        gaa__ywzw = f"def impl({', '.join(arg_names)}):\n"
        gaa__ywzw += f'   if {arg_names[i]}[{container_arg}] is None:\n'
        gaa__ywzw += f"      return {func_name}({', '.join(hndlz__zcxo)})\n"
        gaa__ywzw += f'   else:\n'
        gaa__ywzw += f"      return {func_name}({', '.join(atyi__ely)})\n"
    else:
        kyn__yivs = [(arg_names[ufmx__tpdd] if ufmx__tpdd != i else 'None') for
            ufmx__tpdd in range(len(arg_names))]
        vyka__oddr = [(arg_names[ufmx__tpdd] if ufmx__tpdd != i else
            f'bodo.utils.indexing.unoptional({arg_names[ufmx__tpdd]})') for
            ufmx__tpdd in range(len(arg_names))]
        gaa__ywzw = f"def impl({', '.join(arg_names)}):\n"
        gaa__ywzw += f'   if {arg_names[i]} is None:\n'
        gaa__ywzw += f"      return {func_name}({', '.join(kyn__yivs)})\n"
        gaa__ywzw += f'   else:\n'
        gaa__ywzw += f"      return {func_name}({', '.join(vyka__oddr)})\n"
    qdhlp__tmd = {}
    exec(gaa__ywzw, {'bodo': bodo, 'numba': numba}, qdhlp__tmd)
    kmtq__gmra = qdhlp__tmd['impl']
    return kmtq__gmra


def is_valid_int_arg(arg):
    return not (arg != types.none and not isinstance(arg, types.Integer) and
        not (bodo.utils.utils.is_array_typ(arg, True) and isinstance(arg.
        dtype, types.Integer)) and not is_overload_int(arg))


def is_valid_float_arg(arg):
    return not (arg != types.none and not isinstance(arg, types.Float) and 
        not (bodo.utils.utils.is_array_typ(arg, True) and isinstance(arg.
        dtype, types.Float)) and not is_overload_float(arg))


def is_valid_numeric_bool(arg):
    return not (arg != types.none and not isinstance(arg, (types.Integer,
        types.Float, types.Boolean)) and not (bodo.utils.utils.is_array_typ
        (arg, True) and isinstance(arg.dtype, (types.Integer, types.Float,
        types.Boolean))) and not is_overload_constant_number(arg) and not
        is_overload_constant_bool(arg))


def verify_int_arg(arg, f_name, a_name):
    if not is_valid_int_arg(arg):
        raise_bodo_error(
            f'{f_name} {a_name} argument must be an integer, integer column, or null'
            )


def verify_int_float_arg(arg, f_name, a_name):
    if arg != types.none and not isinstance(arg, (types.Integer, types.
        Float, types.Boolean)) and not (bodo.utils.utils.is_array_typ(arg, 
        True) and isinstance(arg.dtype, (types.Integer, types.Float, types.
        Boolean))) and not is_overload_constant_number(arg):
        raise_bodo_error(
            f'{f_name} {a_name} argument must be a numeric, numeric column, or null'
            )


def is_valid_string_arg(arg):
    arg = types.unliteral(arg)
    return not (arg not in (types.none, types.unicode_type) and not (bodo.
        utils.utils.is_array_typ(arg, True) and arg.dtype == types.
        unicode_type) and not is_overload_constant_str(arg))


def is_valid_binary_arg(arg):
    return not (arg != bodo.bytes_type and not (bodo.utils.utils.
        is_array_typ(arg, True) and arg.dtype == bodo.bytes_type) and not
        is_overload_constant_bytes(arg) and not isinstance(arg, types.Bytes))


def is_valid_datetime_or_date_arg(arg):
    return arg == pd_timestamp_tz_naive_type or bodo.utils.utils.is_array_typ(
        arg, True) and (is_datetime_date_series_typ(arg) or isinstance(arg,
        bodo.DatetimeArrayType) or arg.dtype == bodo.datetime64ns)


def is_valid_timedelta_arg(arg):
    return arg == pd_timedelta_type or bodo.utils.utils.is_array_typ(arg, True
        ) and (is_timedelta64_series_typ(arg) or isinstance(arg,
        PDTimeDeltaType) or arg.dtype == bodo.timedelta64ns)


def is_valid_boolean_arg(arg):
    return not (arg != types.boolean and not (bodo.utils.utils.is_array_typ
        (arg, True) and arg.dtype == types.boolean) and not
        is_overload_constant_bool(arg))


def verify_string_arg(arg, f_name, a_name):
    if not is_valid_string_arg(arg):
        raise_bodo_error(
            f'{f_name} {a_name} argument must be a string, string column, or null'
            )


def verify_scalar_string_arg(arg, f_name, a_name):
    if arg not in (types.unicode_type, bodo.none) and not isinstance(arg,
        types.StringLiteral):
        raise_bodo_error(f'{f_name} {a_name} argument must be a scalar string')


def verify_binary_arg(arg, f_name, a_name):
    if not is_valid_binary_arg(arg):
        raise_bodo_error(
            f'{f_name} {a_name} argument must be binary data or null')


def verify_string_binary_arg(arg, f_name, a_name):
    diqp__rov = is_valid_string_arg(arg)
    rka__qeg = is_valid_binary_arg(arg)
    if diqp__rov or rka__qeg:
        return diqp__rov
    else:
        raise_bodo_error(
            f'{f_name} {a_name} argument must be a binary data, string, string column, or null'
            )


def verify_string_numeric_arg(arg, f_name, a_name):
    if not is_valid_string_arg(arg) and not is_valid_numeric_bool(arg):
        raise_bodo_error(
            f'{f_name} {a_name} argument must be a string, integer, float, boolean, string column, integer column, float column, or boolean column'
            )


def verify_boolean_arg(arg, f_name, a_name):
    if arg not in (types.none, types.boolean) and not (bodo.utils.utils.
        is_array_typ(arg, True) and arg.dtype == types.boolean
        ) and not is_overload_bool(arg):
        raise_bodo_error(
            f'{f_name} {a_name} argument must be a boolean, boolean column, or null'
            )


def is_valid_date_arg(arg):
    return arg == bodo.datetime_date_type or bodo.utils.utils.is_array_typ(arg,
        True) and arg.dtype == bodo.datetime_date_type


def is_valid_tz_naive_datetime_arg(arg):
    return arg in (bodo.datetime64ns, bodo.pd_timestamp_tz_naive_type
        ) or bodo.utils.utils.is_array_typ(arg, True
        ) and arg.dtype == bodo.datetime64ns


def is_valid_tz_aware_datetime_arg(arg):
    return isinstance(arg, bodo.PandasTimestampType
        ) and arg.tz is not None or bodo.utils.utils.is_array_typ(arg, True
        ) and isinstance(arg.dtype, bodo.libs.pd_datetime_arr_ext.
        PandasDatetimeTZDtype)


def verify_datetime_arg(arg, f_name, a_name):
    if not (is_overload_none(arg) or is_valid_date_arg(arg) or
        is_valid_tz_naive_datetime_arg(arg)):
        raise_bodo_error(
            f'{f_name} {a_name} argument must be a datetime, datetime column, or null without a tz'
            )


def verify_datetime_arg_allow_tz(arg, f_name, a_name):
    if not (is_overload_none(arg) or is_valid_date_arg(arg) or
        is_valid_tz_naive_datetime_arg(arg) or
        is_valid_tz_aware_datetime_arg(arg)):
        raise_bodo_error(
            f'{f_name} {a_name} argument must be a datetime, datetime column, or null'
            )


def verify_datetime_arg_require_tz(arg, f_name, a_name):
    if not (is_overload_none(arg) or is_valid_tz_aware_datetime_arg(arg)):
        raise_bodo_error(
            f'{f_name} {a_name} argument must be a tz-aware datetime, datetime column, or null'
            )


def verify_sql_interval(arg, f_name, a_name):
    if not (is_overload_none(arg) or is_valid_timedelta_arg(arg) or arg ==
        bodo.date_offset_type):
        raise_bodo_error(
            f'{f_name} {a_name} argument must be a Timedelta scalar/column, DateOffset, or null'
            )


def get_tz_if_exists(arg):
    if is_valid_tz_aware_datetime_arg(arg):
        if bodo.utils.utils.is_array_typ(arg, True):
            return arg.dtype.tz
        else:
            return arg.tz
    return None


def is_valid_time_arg(arg):
    return isinstance(arg, bodo.TimeType) or bodo.utils.utils.is_array_typ(arg,
        True) and isinstance(arg.dtype, bodo.bodo.TimeType)


def verify_time_or_datetime_arg_allow_tz(arg, f_name, a_name):
    if not (is_overload_none(arg) or is_valid_date_arg(arg) or
        is_valid_time_arg(arg) or is_valid_tz_naive_datetime_arg(arg) or
        is_valid_tz_aware_datetime_arg(arg)):
        raise_bodo_error(
            f'{f_name} {a_name} argument must be a time/datetime, time/datetime column, or null without a tz'
            )


def get_common_broadcasted_type(arg_types, func_name):
    wvpim__qwnii = []
    for i in range(len(arg_types)):
        if bodo.utils.utils.is_array_typ(arg_types[i], False):
            wvpim__qwnii.append(arg_types[i])
        elif bodo.utils.utils.is_array_typ(arg_types[i], True):
            wvpim__qwnii.append(arg_types[i].data)
        else:
            wvpim__qwnii.append(arg_types[i])
    if len(wvpim__qwnii) == 0:
        return bodo.none
    elif len(wvpim__qwnii) == 1:
        if bodo.utils.utils.is_array_typ(wvpim__qwnii[0]):
            return bodo.utils.typing.to_nullable_type(wvpim__qwnii[0])
        elif wvpim__qwnii[0] == bodo.none:
            return bodo.none
        else:
            return bodo.utils.typing.to_nullable_type(bodo.utils.typing.
                dtype_to_array_type(wvpim__qwnii[0]))
    else:
        gyn__ublfz = []
        for i in range(len(arg_types)):
            if bodo.utils.utils.is_array_typ(arg_types[i]):
                gyn__ublfz.append(wvpim__qwnii[i].dtype)
            elif wvpim__qwnii[i] == bodo.none:
                pass
            else:
                gyn__ublfz.append(wvpim__qwnii[i])
        if len(gyn__ublfz) == 0:
            return bodo.none
        nna__vghu, vvab__bgoe = bodo.utils.typing.get_common_scalar_dtype(
            gyn__ublfz)
        if not vvab__bgoe:
            raise_bodo_error(
                f'Cannot call {func_name} on columns with different dtypes')
        return bodo.utils.typing.to_nullable_type(bodo.utils.typing.
            dtype_to_array_type(nna__vghu))


def vectorized_sol(args, scalar_fn, dtype, manual_coercion=False):
    xww__tdq = -1
    for arg in args:
        if isinstance(arg, (pd.core.arrays.base.ExtensionArray, pd.Series,
            np.ndarray, pa.Array)):
            xww__tdq = len(arg)
            break
    if xww__tdq == -1:
        return dtype(scalar_fn(*args)) if manual_coercion else scalar_fn(*args)
    sopbn__nyzg = []
    for arg in args:
        if isinstance(arg, (pd.core.arrays.base.ExtensionArray, pd.Series,
            np.ndarray, pa.Array)):
            sopbn__nyzg.append(arg)
        else:
            sopbn__nyzg.append([arg] * xww__tdq)
    if manual_coercion:
        return pd.Series([dtype(scalar_fn(*wdffe__mqul)) for wdffe__mqul in
            zip(*sopbn__nyzg)])
    else:
        return pd.Series([scalar_fn(*wdffe__mqul) for wdffe__mqul in zip(*
            sopbn__nyzg)], dtype=dtype)


def gen_windowed(calculate_block, constant_block, out_dtype, setup_block=
    None, enter_block=None, exit_block=None, empty_block=None):
    hnw__mnai = calculate_block.splitlines()
    kbkuu__wrndw = len(hnw__mnai[0]) - len(hnw__mnai[0].lstrip())
    if constant_block != None:
        jae__xcm = constant_block.splitlines()
        tyjf__waol = len(jae__xcm[0]) - len(jae__xcm[0].lstrip())
    if setup_block != None:
        unwhe__tlr = setup_block.splitlines()
        waf__nohvz = len(unwhe__tlr[0]) - len(unwhe__tlr[0].lstrip())
    if enter_block != None:
        bcsog__blrd = enter_block.splitlines()
        bci__rhbg = len(bcsog__blrd[0]) - len(bcsog__blrd[0].lstrip())
    if exit_block != None:
        azpwn__enb = exit_block.splitlines()
        ydjw__kpsi = len(azpwn__enb[0]) - len(azpwn__enb[0].lstrip())
    if empty_block == None:
        empty_block = 'bodo.libs.array_kernels.setna(res, i)'
    fime__ajoj = empty_block.splitlines()
    bwjz__algkq = len(fime__ajoj[0]) - len(fime__ajoj[0].lstrip())
    gaa__ywzw = 'def impl(S, lower_bound, upper_bound):\n'
    gaa__ywzw += '   n = len(S)\n'
    gaa__ywzw += '   arr = bodo.utils.conversion.coerce_to_array(S)\n'
    gaa__ywzw += '   res = bodo.utils.utils.alloc_type(n, out_dtype, (-1,))\n'
    gaa__ywzw += '   if upper_bound < lower_bound:\n'
    gaa__ywzw += '      for i in range(n):\n'
    gaa__ywzw += '         bodo.libs.array_kernels.setna(res, i)\n'
    if constant_block != None:
        gaa__ywzw += '   elif lower_bound <= -n+1 and n-1 <= upper_bound:\n'
        gaa__ywzw += '      if S.count() == 0:\n'
        gaa__ywzw += '         for i in range(n):\n'
        gaa__ywzw += '\n'.join([(' ' * 12 + ykyyx__xfncf[bwjz__algkq:]) for
            ykyyx__xfncf in fime__ajoj]) + '\n'
        gaa__ywzw += '      else:\n'
        gaa__ywzw += '\n'.join([(' ' * 9 + ykyyx__xfncf[tyjf__waol:]) for
            ykyyx__xfncf in jae__xcm]) + '\n'
        gaa__ywzw += '         for i in range(n):\n'
        gaa__ywzw += '            res[i] = constant_value\n'
    gaa__ywzw += '   else:\n'
    gaa__ywzw += '      exiting = lower_bound\n'
    gaa__ywzw += '      entering = upper_bound\n'
    gaa__ywzw += '      in_window = 0\n'
    if setup_block != None:
        gaa__ywzw += '\n'.join([(' ' * 6 + ykyyx__xfncf[waf__nohvz:]) for
            ykyyx__xfncf in unwhe__tlr]) + '\n'
    gaa__ywzw += (
        '      for i in range(min(max(0, exiting), n), min(max(0, entering + 1), n)):\n'
        )
    gaa__ywzw += '         if not bodo.libs.array_kernels.isna(arr, i):\n'
    gaa__ywzw += '            in_window += 1\n'
    if enter_block != None:
        if 'elem' in enter_block:
            gaa__ywzw += '            elem = arr[i]\n'
        gaa__ywzw += '\n'.join([(' ' * 12 + ykyyx__xfncf[bci__rhbg:]) for
            ykyyx__xfncf in bcsog__blrd]) + '\n'
    gaa__ywzw += '      for i in range(n):\n'
    gaa__ywzw += '         if in_window == 0:\n'
    gaa__ywzw += '\n'.join([(' ' * 12 + ykyyx__xfncf[bwjz__algkq:]) for
        ykyyx__xfncf in fime__ajoj]) + '\n'
    gaa__ywzw += '         else:\n'
    gaa__ywzw += '\n'.join([(' ' * 12 + ykyyx__xfncf[kbkuu__wrndw:]) for
        ykyyx__xfncf in hnw__mnai]) + '\n'
    gaa__ywzw += '         if 0 <= exiting < n:\n'
    gaa__ywzw += (
        '            if not bodo.libs.array_kernels.isna(arr, exiting):\n')
    gaa__ywzw += '               in_window -= 1\n'
    if exit_block != None:
        if 'elem' in exit_block:
            gaa__ywzw += '               elem = arr[exiting]\n'
        gaa__ywzw += '\n'.join([(' ' * 15 + ykyyx__xfncf[ydjw__kpsi:]) for
            ykyyx__xfncf in azpwn__enb]) + '\n'
    gaa__ywzw += '         exiting += 1\n'
    gaa__ywzw += '         entering += 1\n'
    gaa__ywzw += '         if 0 <= entering < n:\n'
    gaa__ywzw += (
        '            if not bodo.libs.array_kernels.isna(arr, entering):\n')
    gaa__ywzw += '               in_window += 1\n'
    if enter_block != None:
        if 'elem' in enter_block:
            gaa__ywzw += '               elem = arr[entering]\n'
        gaa__ywzw += '\n'.join([(' ' * 15 + ykyyx__xfncf[bci__rhbg:]) for
            ykyyx__xfncf in bcsog__blrd]) + '\n'
    gaa__ywzw += '   return res'
    qdhlp__tmd = {}
    exec(gaa__ywzw, {'bodo': bodo, 'numba': numba, 'np': np, 'out_dtype':
        out_dtype, 'pd': pd}, qdhlp__tmd)
    kmtq__gmra = qdhlp__tmd['impl']
    return kmtq__gmra
