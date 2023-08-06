"""
Support for Series.str methods
"""
import operator
import re
import numba
import numpy as np
import pandas as pd
from numba.core import cgutils, types
from numba.extending import intrinsic, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_model
import bodo
from bodo.hiframes.pd_dataframe_ext import DataFrameType
from bodo.hiframes.pd_index_ext import StringIndexType
from bodo.hiframes.pd_series_ext import SeriesType
from bodo.hiframes.split_impl import get_split_view_data_ptr, get_split_view_index, string_array_split_view_type
from bodo.libs.array import get_search_regex
from bodo.libs.array_item_arr_ext import ArrayItemArrayType
from bodo.libs.str_arr_ext import get_utf8_size, pre_alloc_string_array, string_array_type
from bodo.libs.str_ext import str_findall_count
from bodo.utils.typing import BodoError, create_unsupported_overload, get_overload_const_int, get_overload_const_list, get_overload_const_str, get_overload_const_str_len, is_bin_arr_type, is_list_like_index_type, is_overload_constant_bool, is_overload_constant_int, is_overload_constant_list, is_overload_constant_str, is_overload_false, is_overload_none, is_overload_true, is_str_arr_type, raise_bodo_error
from bodo.utils.utils import synchronize_error_njit


class SeriesStrMethodType(types.Type):

    def __init__(self, stype):
        self.stype = stype
        urlbe__eqg = 'SeriesStrMethodType({})'.format(stype)
        super(SeriesStrMethodType, self).__init__(urlbe__eqg)


@register_model(SeriesStrMethodType)
class SeriesStrModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        kcht__ikpuw = [('obj', fe_type.stype)]
        super(SeriesStrModel, self).__init__(dmm, fe_type, kcht__ikpuw)


make_attribute_wrapper(SeriesStrMethodType, 'obj', '_obj')


@intrinsic
def init_series_str_method(typingctx, obj=None):

    def codegen(context, builder, signature, args):
        oubjq__aif, = args
        fdrdc__orv = signature.return_type
        uhrau__djxp = cgutils.create_struct_proxy(fdrdc__orv)(context, builder)
        uhrau__djxp.obj = oubjq__aif
        context.nrt.incref(builder, signature.args[0], oubjq__aif)
        return uhrau__djxp._getvalue()
    return SeriesStrMethodType(obj)(obj), codegen


def str_arg_check(func_name, arg_name, arg):
    if not isinstance(arg, types.UnicodeType) and not is_overload_constant_str(
        arg):
        raise_bodo_error(
            "Series.str.{}(): parameter '{}' expected a string object, not {}"
            .format(func_name, arg_name, arg))


def int_arg_check(func_name, arg_name, arg):
    if not isinstance(arg, types.Integer) and not is_overload_constant_int(arg
        ):
        raise BodoError(
            "Series.str.{}(): parameter '{}' expected an int object, not {}"
            .format(func_name, arg_name, arg))


def not_supported_arg_check(func_name, arg_name, arg, defval):
    if arg_name == 'na':
        if not isinstance(arg, types.Omitted) and (not isinstance(arg,
            float) or not np.isnan(arg)):
            raise BodoError(
                "Series.str.{}(): parameter '{}' is not supported, default: np.nan"
                .format(func_name, arg_name))
    elif not isinstance(arg, types.Omitted) and arg != defval:
        raise BodoError(
            "Series.str.{}(): parameter '{}' is not supported, default: {}"
            .format(func_name, arg_name, defval))


def common_validate_padding(func_name, width, fillchar):
    if is_overload_constant_str(fillchar):
        if get_overload_const_str_len(fillchar) != 1:
            raise BodoError(
                'Series.str.{}(): fillchar must be a character, not str'.
                format(func_name))
    elif not isinstance(fillchar, types.UnicodeType):
        raise BodoError('Series.str.{}(): fillchar must be a character, not {}'
            .format(func_name, fillchar))
    int_arg_check(func_name, 'width', width)


@overload_attribute(SeriesType, 'str')
def overload_series_str(S):
    if not (is_str_arr_type(S.data) or S.data ==
        string_array_split_view_type or isinstance(S.data,
        ArrayItemArrayType) or is_bin_arr_type(S.data)):
        raise_bodo_error(
            'Series.str: input should be a series of string/binary or arrays')
    return lambda S: bodo.hiframes.series_str_impl.init_series_str_method(S)


@overload_method(SeriesStrMethodType, 'len', inline='always', no_unliteral=True
    )
def overload_str_method_len(S_str):
    if S_str.stype.data == bodo.dict_str_arr_type:

        def _str_len_dict_impl(S_str):
            S = S_str._obj
            yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            out_arr = bodo.libs.dict_arr_ext.str_len(yyhe__alze)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return _str_len_dict_impl

    def impl(S_str):
        S = S_str._obj
        yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
        xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
        urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
        out_arr = bodo.libs.array_kernels.get_arr_lens(yyhe__alze, False)
        return bodo.hiframes.pd_series_ext.init_series(out_arr, xci__nccl,
            urlbe__eqg)
    return impl


@overload_method(SeriesStrMethodType, 'split', inline='always',
    no_unliteral=True)
def overload_str_method_split(S_str, pat=None, n=-1, expand=False):
    if not is_overload_none(pat):
        str_arg_check('split', 'pat', pat)
    int_arg_check('split', 'n', n)
    not_supported_arg_check('split', 'expand', expand, False)
    if is_overload_constant_str(pat) and len(get_overload_const_str(pat)
        ) == 1 and get_overload_const_str(pat).isascii(
        ) and is_overload_constant_int(n) and get_overload_const_int(n
        ) == -1 and S_str.stype.data == string_array_type:

        def _str_split_view_impl(S_str, pat=None, n=-1, expand=False):
            S = S_str._obj
            yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            out_arr = bodo.hiframes.split_impl.compute_split_view(yyhe__alze,
                pat)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return _str_split_view_impl

    def _str_split_impl(S_str, pat=None, n=-1, expand=False):
        S = S_str._obj
        yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
        xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
        urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
        out_arr = bodo.libs.str_ext.str_split(yyhe__alze, pat, n)
        return bodo.hiframes.pd_series_ext.init_series(out_arr, xci__nccl,
            urlbe__eqg)
    return _str_split_impl


@overload_method(SeriesStrMethodType, 'get', no_unliteral=True)
def overload_str_method_get(S_str, i):
    akghe__jbet = S_str.stype.data
    if (akghe__jbet != string_array_split_view_type and not is_str_arr_type
        (akghe__jbet)) and not isinstance(akghe__jbet, ArrayItemArrayType):
        raise_bodo_error(
            'Series.str.get(): only supports input type of Series(array(item)) and Series(str)'
            )
    int_arg_check('get', 'i', i)
    if isinstance(akghe__jbet, ArrayItemArrayType):

        def _str_get_array_impl(S_str, i):
            S = S_str._obj
            yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            out_arr = bodo.libs.array_kernels.get(yyhe__alze, i)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return _str_get_array_impl
    if akghe__jbet == string_array_split_view_type:

        def _str_get_split_impl(S_str, i):
            S = S_str._obj
            yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            numba.parfors.parfor.init_prange()
            n = len(yyhe__alze)
            ity__xpn = 0
            for psxyx__mbpha in numba.parfors.parfor.internal_prange(n):
                wvbd__znd, wvbd__znd, qwr__wlb = get_split_view_index(
                    yyhe__alze, psxyx__mbpha, i)
                ity__xpn += qwr__wlb
            numba.parfors.parfor.init_prange()
            out_arr = pre_alloc_string_array(n, ity__xpn)
            for lcpph__hjlc in numba.parfors.parfor.internal_prange(n):
                sakz__ggfl, hljch__yspt, qwr__wlb = get_split_view_index(
                    yyhe__alze, lcpph__hjlc, i)
                if sakz__ggfl == 0:
                    bodo.libs.array_kernels.setna(out_arr, lcpph__hjlc)
                    bmedk__pfl = get_split_view_data_ptr(yyhe__alze, 0)
                else:
                    bodo.libs.str_arr_ext.str_arr_set_not_na(out_arr,
                        lcpph__hjlc)
                    bmedk__pfl = get_split_view_data_ptr(yyhe__alze,
                        hljch__yspt)
                bodo.libs.str_arr_ext.setitem_str_arr_ptr(out_arr,
                    lcpph__hjlc, bmedk__pfl, qwr__wlb)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return _str_get_split_impl
    if S_str.stype.data == bodo.dict_str_arr_type:

        def _str_get_dict_impl(S_str, i):
            S = S_str._obj
            yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            out_arr = bodo.libs.dict_arr_ext.str_get(yyhe__alze, i)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return _str_get_dict_impl

    def _str_get_impl(S_str, i):
        S = S_str._obj
        yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
        xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
        urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
        numba.parfors.parfor.init_prange()
        n = len(yyhe__alze)
        numba.parfors.parfor.init_prange()
        out_arr = pre_alloc_string_array(n, -1)
        for lcpph__hjlc in numba.parfors.parfor.internal_prange(n):
            if bodo.libs.array_kernels.isna(yyhe__alze, lcpph__hjlc
                ) or not len(yyhe__alze[lcpph__hjlc]) > i >= -len(yyhe__alze
                [lcpph__hjlc]):
                out_arr[lcpph__hjlc] = ''
                bodo.libs.array_kernels.setna(out_arr, lcpph__hjlc)
            else:
                out_arr[lcpph__hjlc] = yyhe__alze[lcpph__hjlc][i]
        return bodo.hiframes.pd_series_ext.init_series(out_arr, xci__nccl,
            urlbe__eqg)
    return _str_get_impl


@overload_method(SeriesStrMethodType, 'join', inline='always', no_unliteral
    =True)
def overload_str_method_join(S_str, sep):
    akghe__jbet = S_str.stype.data
    if (akghe__jbet != string_array_split_view_type and akghe__jbet !=
        ArrayItemArrayType(string_array_type) and not is_str_arr_type(
        akghe__jbet)):
        raise_bodo_error(
            'Series.str.join(): only supports input type of Series(list(str)) and Series(str)'
            )
    str_arg_check('join', 'sep', sep)

    def impl(S_str, sep):
        S = S_str._obj
        focn__xefsi = bodo.hiframes.pd_series_ext.get_series_data(S)
        urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
        xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
        numba.parfors.parfor.init_prange()
        n = len(focn__xefsi)
        out_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(n, -1)
        for lcpph__hjlc in numba.parfors.parfor.internal_prange(n):
            if bodo.libs.array_kernels.isna(focn__xefsi, lcpph__hjlc):
                out_arr[lcpph__hjlc] = ''
                bodo.libs.array_kernels.setna(out_arr, lcpph__hjlc)
            else:
                zar__jbpr = focn__xefsi[lcpph__hjlc]
                out_arr[lcpph__hjlc] = sep.join(zar__jbpr)
        return bodo.hiframes.pd_series_ext.init_series(out_arr, xci__nccl,
            urlbe__eqg)
    return impl


@overload_method(SeriesStrMethodType, 'replace', inline='always',
    no_unliteral=True)
def overload_str_method_replace(S_str, pat, repl, n=-1, case=None, flags=0,
    regex=True):
    not_supported_arg_check('replace', 'n', n, -1)
    not_supported_arg_check('replace', 'case', case, None)
    str_arg_check('replace', 'pat', pat)
    str_arg_check('replace', 'repl', repl)
    int_arg_check('replace', 'flags', flags)
    if S_str.stype.data == bodo.dict_str_arr_type:

        def _str_replace_dict_impl(S_str, pat, repl, n=-1, case=None, flags
            =0, regex=True):
            S = S_str._obj
            yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            out_arr = bodo.libs.dict_arr_ext.str_replace(yyhe__alze, pat,
                repl, flags, regex)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return _str_replace_dict_impl
    if is_overload_true(regex):

        def _str_replace_regex_impl(S_str, pat, repl, n=-1, case=None,
            flags=0, regex=True):
            S = S_str._obj
            yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            numba.parfors.parfor.init_prange()
            uvrvd__ouvs = re.compile(pat, flags)
            tfok__mzybv = len(yyhe__alze)
            out_arr = pre_alloc_string_array(tfok__mzybv, -1)
            for lcpph__hjlc in numba.parfors.parfor.internal_prange(tfok__mzybv
                ):
                if bodo.libs.array_kernels.isna(yyhe__alze, lcpph__hjlc):
                    out_arr[lcpph__hjlc] = ''
                    bodo.libs.array_kernels.setna(out_arr, lcpph__hjlc)
                    continue
                out_arr[lcpph__hjlc] = uvrvd__ouvs.sub(repl, yyhe__alze[
                    lcpph__hjlc])
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return _str_replace_regex_impl
    if not is_overload_false(regex):
        raise BodoError('Series.str.replace(): regex argument should be bool')

    def _str_replace_noregex_impl(S_str, pat, repl, n=-1, case=None, flags=
        0, regex=True):
        S = S_str._obj
        yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
        xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
        urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
        numba.parfors.parfor.init_prange()
        tfok__mzybv = len(yyhe__alze)
        numba.parfors.parfor.init_prange()
        out_arr = pre_alloc_string_array(tfok__mzybv, -1)
        for lcpph__hjlc in numba.parfors.parfor.internal_prange(tfok__mzybv):
            if bodo.libs.array_kernels.isna(yyhe__alze, lcpph__hjlc):
                out_arr[lcpph__hjlc] = ''
                bodo.libs.array_kernels.setna(out_arr, lcpph__hjlc)
                continue
            out_arr[lcpph__hjlc] = yyhe__alze[lcpph__hjlc].replace(pat, repl)
        return bodo.hiframes.pd_series_ext.init_series(out_arr, xci__nccl,
            urlbe__eqg)
    return _str_replace_noregex_impl


@numba.njit
def series_contains_regex(S, pat, case, flags, na, regex):
    with numba.objmode(out_arr=bodo.boolean_array):
        out_arr = pd.array(S.array, 'string')._str_contains(pat, case,
            flags, na, regex)
    return out_arr


@numba.njit
def series_match_regex(S, pat, case, flags, na):
    with numba.objmode(out_arr=bodo.boolean_array):
        out_arr = S.array._str_match(pat, case, flags, na)
    return out_arr


def is_regex_unsupported(pat):
    msd__wwnji = ['(?a', '(?i', '(?L', '(?m', '(?s', '(?u', '(?x', '(?#']
    if is_overload_constant_str(pat):
        if isinstance(pat, types.StringLiteral):
            pat = pat.literal_value
        return any([(pimp__ozx in pat) for pimp__ozx in msd__wwnji])
    else:
        return True


@overload_method(SeriesStrMethodType, 'contains', no_unliteral=True)
def overload_str_method_contains(S_str, pat, case=True, flags=0, na=np.nan,
    regex=True):
    not_supported_arg_check('contains', 'na', na, np.nan)
    str_arg_check('contains', 'pat', pat)
    int_arg_check('contains', 'flags', flags)
    if not is_overload_constant_bool(regex):
        raise BodoError(
            "Series.str.contains(): 'regex' argument should be a constant boolean"
            )
    if not is_overload_constant_bool(case):
        raise BodoError(
            "Series.str.contains(): 'case' argument should be a constant boolean"
            )
    talnc__khr = re.IGNORECASE.value
    rtnfg__hvbnl = 'def impl(\n'
    rtnfg__hvbnl += (
        '    S_str, pat, case=True, flags=0, na=np.nan, regex=True\n')
    rtnfg__hvbnl += '):\n'
    rtnfg__hvbnl += '  S = S_str._obj\n'
    rtnfg__hvbnl += '  arr = bodo.hiframes.pd_series_ext.get_series_data(S)\n'
    rtnfg__hvbnl += (
        '  index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
    rtnfg__hvbnl += '  name = bodo.hiframes.pd_series_ext.get_series_name(S)\n'
    rtnfg__hvbnl += '  l = len(arr)\n'
    rtnfg__hvbnl += '  out_arr = bodo.libs.bool_arr_ext.alloc_bool_array(l)\n'
    if is_overload_true(regex):
        if is_regex_unsupported(pat) or flags:
            if S_str.stype.data == bodo.dict_str_arr_type:
                rtnfg__hvbnl += """  out_arr = bodo.libs.dict_arr_ext.str_series_contains_regex(arr, pat, case, flags, na, regex)
"""
            else:
                rtnfg__hvbnl += """  out_arr = bodo.hiframes.series_str_impl.series_contains_regex(S, pat, case, flags, na, regex)
"""
        else:
            rtnfg__hvbnl += """  get_search_regex(arr, case, False, bodo.libs.str_ext.unicode_to_utf8(pat), out_arr)
"""
    elif S_str.stype.data == bodo.dict_str_arr_type:
        rtnfg__hvbnl += """  out_arr = bodo.libs.dict_arr_ext.str_contains_non_regex(arr, pat, case)
"""
    else:
        rtnfg__hvbnl += '  numba.parfors.parfor.init_prange()\n'
        if is_overload_false(case):
            rtnfg__hvbnl += '  upper_pat = pat.upper()\n'
        rtnfg__hvbnl += '  for i in numba.parfors.parfor.internal_prange(l):\n'
        rtnfg__hvbnl += '      if bodo.libs.array_kernels.isna(arr, i):\n'
        rtnfg__hvbnl += '          bodo.libs.array_kernels.setna(out_arr, i)\n'
        rtnfg__hvbnl += '      else: \n'
        if is_overload_true(case):
            rtnfg__hvbnl += '          out_arr[i] = pat in arr[i]\n'
        else:
            rtnfg__hvbnl += (
                '          out_arr[i] = upper_pat in arr[i].upper()\n')
    rtnfg__hvbnl += (
        '  return bodo.hiframes.pd_series_ext.init_series(out_arr, index, name)\n'
        )
    kps__dtfui = {}
    exec(rtnfg__hvbnl, {'re': re, 'bodo': bodo, 'numba': numba, 'np': np,
        're_ignorecase_value': talnc__khr, 'get_search_regex':
        get_search_regex}, kps__dtfui)
    impl = kps__dtfui['impl']
    return impl


@overload_method(SeriesStrMethodType, 'match', inline='always',
    no_unliteral=True)
def overload_str_method_match(S_str, pat, case=True, flags=0, na=np.nan):
    not_supported_arg_check('match', 'na', na, np.nan)
    str_arg_check('match', 'pat', pat)
    int_arg_check('match', 'flags', flags)
    if not is_overload_constant_bool(case):
        raise BodoError(
            "Series.str.match(): 'case' argument should be a constant boolean")
    talnc__khr = re.IGNORECASE.value
    rtnfg__hvbnl = 'def impl(S_str, pat, case=True, flags=0, na=np.nan):\n'
    rtnfg__hvbnl += '        S = S_str._obj\n'
    rtnfg__hvbnl += (
        '        arr = bodo.hiframes.pd_series_ext.get_series_data(S)\n')
    rtnfg__hvbnl += '        l = len(arr)\n'
    rtnfg__hvbnl += (
        '        index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
    rtnfg__hvbnl += (
        '        name = bodo.hiframes.pd_series_ext.get_series_name(S)\n')
    if not is_regex_unsupported(pat) and flags == 0:
        rtnfg__hvbnl += (
            '        out_arr = bodo.libs.bool_arr_ext.alloc_bool_array(l)\n')
        rtnfg__hvbnl += """        get_search_regex(arr, case, True, bodo.libs.str_ext.unicode_to_utf8(pat), out_arr)
"""
    elif S_str.stype.data == bodo.dict_str_arr_type:
        rtnfg__hvbnl += """        out_arr = bodo.libs.dict_arr_ext.str_match(arr, pat, case, flags, na)
"""
    else:
        rtnfg__hvbnl += (
            '        out_arr = series_match_regex(S, pat, case, flags, na)\n')
    rtnfg__hvbnl += """        return bodo.hiframes.pd_series_ext.init_series(out_arr, index, name)
"""
    kps__dtfui = {}
    exec(rtnfg__hvbnl, {'re': re, 'bodo': bodo, 'numba': numba, 'np': np,
        're_ignorecase_value': talnc__khr, 'get_search_regex':
        get_search_regex}, kps__dtfui)
    impl = kps__dtfui['impl']
    return impl


@overload_method(SeriesStrMethodType, 'cat', no_unliteral=True)
def overload_str_method_cat(S_str, others=None, sep=None, na_rep=None, join
    ='left'):
    if not isinstance(others, DataFrameType):
        raise_bodo_error(
            "Series.str.cat(): 'others' must be a DataFrame currently")
    if not is_overload_none(sep):
        str_arg_check('cat', 'sep', sep)
    if not is_overload_constant_str(join) or get_overload_const_str(join
        ) != 'left':
        raise_bodo_error("Series.str.cat(): 'join' not supported yet")
    rtnfg__hvbnl = (
        "def impl(S_str, others=None, sep=None, na_rep=None, join='left'):\n")
    rtnfg__hvbnl += '  S = S_str._obj\n'
    rtnfg__hvbnl += '  arr = bodo.hiframes.pd_series_ext.get_series_data(S)\n'
    rtnfg__hvbnl += (
        '  index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
    rtnfg__hvbnl += '  name = bodo.hiframes.pd_series_ext.get_series_name(S)\n'
    rtnfg__hvbnl += '  l = len(arr)\n'
    for i in range(len(others.columns)):
        rtnfg__hvbnl += f"""  data{i} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(others, {i})
"""
    if S_str.stype.data == bodo.dict_str_arr_type and all(wwjdq__qzq ==
        bodo.dict_str_arr_type for wwjdq__qzq in others.data):
        eskf__dcklz = ', '.join(f'data{i}' for i in range(len(others.columns)))
        rtnfg__hvbnl += f"""  out_arr = bodo.libs.dict_arr_ext.cat_dict_str((arr, {eskf__dcklz}), sep)
"""
    else:
        vkr__gfgay = ' or '.join(['bodo.libs.array_kernels.isna(arr, i)'] +
            [f'bodo.libs.array_kernels.isna(data{i}, i)' for i in range(len
            (others.columns))])
        rtnfg__hvbnl += (
            '  out_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(l, -1)\n'
            )
        rtnfg__hvbnl += '  numba.parfors.parfor.init_prange()\n'
        rtnfg__hvbnl += '  for i in numba.parfors.parfor.internal_prange(l):\n'
        rtnfg__hvbnl += f'      if {vkr__gfgay}:\n'
        rtnfg__hvbnl += '          bodo.libs.array_kernels.setna(out_arr, i)\n'
        rtnfg__hvbnl += '          continue\n'
        rbvmw__drm = ', '.join(['arr[i]'] + [f'data{i}[i]' for i in range(
            len(others.columns))])
        fdhe__pqoaz = "''" if is_overload_none(sep) else 'sep'
        rtnfg__hvbnl += (
            f'      out_arr[i] = {fdhe__pqoaz}.join([{rbvmw__drm}])\n')
    rtnfg__hvbnl += (
        '  return bodo.hiframes.pd_series_ext.init_series(out_arr, index, name)\n'
        )
    kps__dtfui = {}
    exec(rtnfg__hvbnl, {'bodo': bodo, 'numba': numba}, kps__dtfui)
    impl = kps__dtfui['impl']
    return impl


@overload_method(SeriesStrMethodType, 'count', inline='always',
    no_unliteral=True)
def overload_str_method_count(S_str, pat, flags=0):
    str_arg_check('count', 'pat', pat)
    int_arg_check('count', 'flags', flags)
    if S_str.stype.data == bodo.dict_str_arr_type:

        def _str_count_dict_impl(S_str, pat, flags=0):
            S = S_str._obj
            yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            out_arr = bodo.libs.dict_arr_ext.str_count(yyhe__alze, pat, flags)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return _str_count_dict_impl

    def impl(S_str, pat, flags=0):
        S = S_str._obj
        focn__xefsi = bodo.hiframes.pd_series_ext.get_series_data(S)
        urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
        xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
        uvrvd__ouvs = re.compile(pat, flags)
        numba.parfors.parfor.init_prange()
        tfok__mzybv = len(focn__xefsi)
        out_arr = bodo.libs.int_arr_ext.alloc_int_array(tfok__mzybv, np.int64)
        for i in numba.parfors.parfor.internal_prange(tfok__mzybv):
            if bodo.libs.array_kernels.isna(focn__xefsi, i):
                bodo.libs.array_kernels.setna(out_arr, i)
            else:
                out_arr[i] = str_findall_count(uvrvd__ouvs, focn__xefsi[i])
        return bodo.hiframes.pd_series_ext.init_series(out_arr, xci__nccl,
            urlbe__eqg)
    return impl


@overload_method(SeriesStrMethodType, 'find', inline='always', no_unliteral
    =True)
def overload_str_method_find(S_str, sub, start=0, end=None):
    str_arg_check('find', 'sub', sub)
    int_arg_check('find', 'start', start)
    if not is_overload_none(end):
        int_arg_check('find', 'end', end)
    if S_str.stype.data == bodo.dict_str_arr_type:

        def _str_find_dict_impl(S_str, sub, start=0, end=None):
            S = S_str._obj
            yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            out_arr = bodo.libs.dict_arr_ext.str_find(yyhe__alze, sub,
                start, end)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return _str_find_dict_impl

    def impl(S_str, sub, start=0, end=None):
        S = S_str._obj
        focn__xefsi = bodo.hiframes.pd_series_ext.get_series_data(S)
        urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
        xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
        numba.parfors.parfor.init_prange()
        tfok__mzybv = len(focn__xefsi)
        out_arr = bodo.libs.int_arr_ext.alloc_int_array(tfok__mzybv, np.int64)
        for i in numba.parfors.parfor.internal_prange(tfok__mzybv):
            if bodo.libs.array_kernels.isna(focn__xefsi, i):
                bodo.libs.array_kernels.setna(out_arr, i)
            else:
                out_arr[i] = focn__xefsi[i].find(sub, start, end)
        return bodo.hiframes.pd_series_ext.init_series(out_arr, xci__nccl,
            urlbe__eqg)
    return impl


@overload_method(SeriesStrMethodType, 'rfind', inline='always',
    no_unliteral=True)
def overload_str_method_rfind(S_str, sub, start=0, end=None):
    str_arg_check('rfind', 'sub', sub)
    if start != 0:
        int_arg_check('rfind', 'start', start)
    if not is_overload_none(end):
        int_arg_check('rfind', 'end', end)
    if S_str.stype.data == bodo.dict_str_arr_type:

        def _str_rfind_dict_impl(S_str, sub, start=0, end=None):
            S = S_str._obj
            yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            out_arr = bodo.libs.dict_arr_ext.str_rfind(yyhe__alze, sub,
                start, end)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return _str_rfind_dict_impl

    def impl(S_str, sub, start=0, end=None):
        S = S_str._obj
        focn__xefsi = bodo.hiframes.pd_series_ext.get_series_data(S)
        urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
        xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
        numba.parfors.parfor.init_prange()
        tfok__mzybv = len(focn__xefsi)
        out_arr = bodo.libs.int_arr_ext.alloc_int_array(tfok__mzybv, np.int64)
        for i in numba.parfors.parfor.internal_prange(tfok__mzybv):
            if bodo.libs.array_kernels.isna(focn__xefsi, i):
                bodo.libs.array_kernels.setna(out_arr, i)
            else:
                out_arr[i] = focn__xefsi[i].rfind(sub, start, end)
        return bodo.hiframes.pd_series_ext.init_series(out_arr, xci__nccl,
            urlbe__eqg)
    return impl


@overload_method(SeriesStrMethodType, 'index', inline='always',
    no_unliteral=True)
def overload_str_method_index(S_str, sub, start=0, end=None):
    str_arg_check('index', 'sub', sub)
    int_arg_check('index', 'start', start)
    if not is_overload_none(end):
        int_arg_check('index', 'end', end)
    if S_str.stype.data == bodo.dict_str_arr_type:

        def _str_index_dict_impl(S_str, sub, start=0, end=None):
            S = S_str._obj
            yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            out_arr = bodo.libs.dict_arr_ext.str_index(yyhe__alze, sub,
                start, end)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return _str_index_dict_impl

    def impl(S_str, sub, start=0, end=None):
        S = S_str._obj
        focn__xefsi = bodo.hiframes.pd_series_ext.get_series_data(S)
        urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
        xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
        tfok__mzybv = len(focn__xefsi)
        out_arr = bodo.libs.int_arr_ext.alloc_int_array(tfok__mzybv, np.int64)
        numba.parfors.parfor.init_prange()
        kco__useul = False
        for i in numba.parfors.parfor.internal_prange(tfok__mzybv):
            if bodo.libs.array_kernels.isna(focn__xefsi, i):
                bodo.libs.array_kernels.setna(out_arr, i)
            else:
                out_arr[i] = focn__xefsi[i].find(sub, start, end)
                if out_arr[i] == -1:
                    kco__useul = True
        vnol__wuxv = 'substring not found' if kco__useul else ''
        synchronize_error_njit('ValueError', vnol__wuxv)
        return bodo.hiframes.pd_series_ext.init_series(out_arr, xci__nccl,
            urlbe__eqg)
    return impl


@overload_method(SeriesStrMethodType, 'rindex', inline='always',
    no_unliteral=True)
def overload_str_method_rindex(S_str, sub, start=0, end=None):
    str_arg_check('rindex', 'sub', sub)
    int_arg_check('rindex', 'start', start)
    if not is_overload_none(end):
        int_arg_check('rindex', 'end', end)
    if S_str.stype.data == bodo.dict_str_arr_type:

        def _str_rindex_dict_impl(S_str, sub, start=0, end=None):
            S = S_str._obj
            yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            out_arr = bodo.libs.dict_arr_ext.str_rindex(yyhe__alze, sub,
                start, end)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return _str_rindex_dict_impl

    def impl(S_str, sub, start=0, end=None):
        S = S_str._obj
        focn__xefsi = bodo.hiframes.pd_series_ext.get_series_data(S)
        urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
        xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
        tfok__mzybv = len(focn__xefsi)
        out_arr = bodo.libs.int_arr_ext.alloc_int_array(tfok__mzybv, np.int64)
        numba.parfors.parfor.init_prange()
        kco__useul = False
        for i in numba.parfors.parfor.internal_prange(tfok__mzybv):
            if bodo.libs.array_kernels.isna(focn__xefsi, i):
                bodo.libs.array_kernels.setna(out_arr, i)
            else:
                out_arr[i] = focn__xefsi[i].rindex(sub, start, end)
                if out_arr[i] == -1:
                    kco__useul = True
        vnol__wuxv = 'substring not found' if kco__useul else ''
        synchronize_error_njit('ValueError', vnol__wuxv)
        return bodo.hiframes.pd_series_ext.init_series(out_arr, xci__nccl,
            urlbe__eqg)
    return impl


@overload_method(SeriesStrMethodType, 'slice_replace', inline='always',
    no_unliteral=True)
def overload_str_method_slice_replace(S_str, start=0, stop=None, repl=''):
    int_arg_check('slice_replace', 'start', start)
    if not is_overload_none(stop):
        int_arg_check('slice_replace', 'stop', stop)
    str_arg_check('slice_replace', 'repl', repl)

    def impl(S_str, start=0, stop=None, repl=''):
        S = S_str._obj
        focn__xefsi = bodo.hiframes.pd_series_ext.get_series_data(S)
        urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
        xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
        numba.parfors.parfor.init_prange()
        tfok__mzybv = len(focn__xefsi)
        out_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(tfok__mzybv, -1)
        for lcpph__hjlc in numba.parfors.parfor.internal_prange(tfok__mzybv):
            if bodo.libs.array_kernels.isna(focn__xefsi, lcpph__hjlc):
                bodo.libs.array_kernels.setna(out_arr, lcpph__hjlc)
            else:
                if stop is not None:
                    ggdq__sjkrz = focn__xefsi[lcpph__hjlc][stop:]
                else:
                    ggdq__sjkrz = ''
                out_arr[lcpph__hjlc] = focn__xefsi[lcpph__hjlc][:start
                    ] + repl + ggdq__sjkrz
        return bodo.hiframes.pd_series_ext.init_series(out_arr, xci__nccl,
            urlbe__eqg)
    return impl


@overload_method(SeriesStrMethodType, 'repeat', inline='always',
    no_unliteral=True)
def overload_str_method_repeat(S_str, repeats):
    if isinstance(repeats, types.Integer) or is_overload_constant_int(repeats):
        if S_str.stype.data == bodo.dict_str_arr_type:

            def _str_repeat_int_dict_impl(S_str, repeats):
                S = S_str._obj
                yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
                xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
                urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
                out_arr = bodo.libs.dict_arr_ext.str_repeat_int(yyhe__alze,
                    repeats)
                return bodo.hiframes.pd_series_ext.init_series(out_arr,
                    xci__nccl, urlbe__eqg)
            return _str_repeat_int_dict_impl

        def impl(S_str, repeats):
            S = S_str._obj
            focn__xefsi = bodo.hiframes.pd_series_ext.get_series_data(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            numba.parfors.parfor.init_prange()
            tfok__mzybv = len(focn__xefsi)
            out_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(tfok__mzybv,
                -1)
            for lcpph__hjlc in numba.parfors.parfor.internal_prange(tfok__mzybv
                ):
                if bodo.libs.array_kernels.isna(focn__xefsi, lcpph__hjlc):
                    bodo.libs.array_kernels.setna(out_arr, lcpph__hjlc)
                else:
                    out_arr[lcpph__hjlc] = focn__xefsi[lcpph__hjlc] * repeats
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return impl
    elif is_overload_constant_list(repeats):
        emn__dtax = get_overload_const_list(repeats)
        vbe__hocp = all([isinstance(dodr__ztlq, int) for dodr__ztlq in
            emn__dtax])
    elif is_list_like_index_type(repeats) and isinstance(repeats.dtype,
        types.Integer):
        vbe__hocp = True
    else:
        vbe__hocp = False
    if vbe__hocp:

        def impl(S_str, repeats):
            S = S_str._obj
            focn__xefsi = bodo.hiframes.pd_series_ext.get_series_data(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            obdv__egz = bodo.utils.conversion.coerce_to_array(repeats)
            numba.parfors.parfor.init_prange()
            tfok__mzybv = len(focn__xefsi)
            out_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(tfok__mzybv,
                -1)
            for lcpph__hjlc in numba.parfors.parfor.internal_prange(tfok__mzybv
                ):
                if bodo.libs.array_kernels.isna(focn__xefsi, lcpph__hjlc):
                    bodo.libs.array_kernels.setna(out_arr, lcpph__hjlc)
                else:
                    out_arr[lcpph__hjlc] = focn__xefsi[lcpph__hjlc
                        ] * obdv__egz[lcpph__hjlc]
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return impl
    else:
        raise BodoError(
            'Series.str.repeat(): repeats argument must either be an integer or a sequence of integers'
            )


def create_ljust_rjust_center_overload(func_name):
    rtnfg__hvbnl = f"""def dict_impl(S_str, width, fillchar=' '):
    S = S_str._obj
    arr = bodo.hiframes.pd_series_ext.get_series_data(S)
    index = bodo.hiframes.pd_series_ext.get_series_index(S)
    name = bodo.hiframes.pd_series_ext.get_series_name(S)
    out_arr = bodo.libs.dict_arr_ext.str_{func_name}(arr, width, fillchar)
    return bodo.hiframes.pd_series_ext.init_series(out_arr, index, name)
def impl(S_str, width, fillchar=' '):
    S = S_str._obj
    str_arr = bodo.hiframes.pd_series_ext.get_series_data(S)
    name = bodo.hiframes.pd_series_ext.get_series_name(S)
    index = bodo.hiframes.pd_series_ext.get_series_index(S)
    numba.parfors.parfor.init_prange()
    l = len(str_arr)
    out_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(l, -1)
    for j in numba.parfors.parfor.internal_prange(l):
        if bodo.libs.array_kernels.isna(str_arr, j):
            bodo.libs.array_kernels.setna(out_arr, j)
        else:
            out_arr[j] = str_arr[j].{func_name}(width, fillchar)
    return bodo.hiframes.pd_series_ext.init_series(out_arr, index, name)
"""
    kps__dtfui = {}
    jizls__haxaf = {'bodo': bodo, 'numba': numba}
    exec(rtnfg__hvbnl, jizls__haxaf, kps__dtfui)
    impl = kps__dtfui['impl']
    kejj__uuai = kps__dtfui['dict_impl']

    def overload_ljust_rjust_center_method(S_str, width, fillchar=' '):
        common_validate_padding(func_name, width, fillchar)
        if S_str.stype.data == bodo.dict_str_arr_type:
            return kejj__uuai
        return impl
    return overload_ljust_rjust_center_method


def _install_ljust_rjust_center():
    for enjp__hlq in ['ljust', 'rjust', 'center']:
        impl = create_ljust_rjust_center_overload(enjp__hlq)
        overload_method(SeriesStrMethodType, enjp__hlq, inline='always',
            no_unliteral=True)(impl)


_install_ljust_rjust_center()


@overload_method(SeriesStrMethodType, 'pad', no_unliteral=True)
def overload_str_method_pad(S_str, width, side='left', fillchar=' '):
    common_validate_padding('pad', width, fillchar)
    if is_overload_constant_str(side):
        if get_overload_const_str(side) not in ['left', 'right', 'both']:
            raise BodoError('Series.str.pad(): Invalid Side')
    else:
        raise BodoError('Series.str.pad(): Invalid Side')
    if S_str.stype.data == bodo.dict_str_arr_type:

        def _str_pad_dict_impl(S_str, width, side='left', fillchar=' '):
            S = S_str._obj
            yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            if side == 'left':
                out_arr = bodo.libs.dict_arr_ext.str_rjust(yyhe__alze,
                    width, fillchar)
            elif side == 'right':
                out_arr = bodo.libs.dict_arr_ext.str_ljust(yyhe__alze,
                    width, fillchar)
            elif side == 'both':
                out_arr = bodo.libs.dict_arr_ext.str_center(yyhe__alze,
                    width, fillchar)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return _str_pad_dict_impl

    def impl(S_str, width, side='left', fillchar=' '):
        S = S_str._obj
        focn__xefsi = bodo.hiframes.pd_series_ext.get_series_data(S)
        urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
        xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
        numba.parfors.parfor.init_prange()
        tfok__mzybv = len(focn__xefsi)
        out_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(tfok__mzybv, -1)
        for lcpph__hjlc in numba.parfors.parfor.internal_prange(tfok__mzybv):
            if bodo.libs.array_kernels.isna(focn__xefsi, lcpph__hjlc):
                out_arr[lcpph__hjlc] = ''
                bodo.libs.array_kernels.setna(out_arr, lcpph__hjlc)
            elif side == 'left':
                out_arr[lcpph__hjlc] = focn__xefsi[lcpph__hjlc].rjust(width,
                    fillchar)
            elif side == 'right':
                out_arr[lcpph__hjlc] = focn__xefsi[lcpph__hjlc].ljust(width,
                    fillchar)
            elif side == 'both':
                out_arr[lcpph__hjlc] = focn__xefsi[lcpph__hjlc].center(width,
                    fillchar)
        return bodo.hiframes.pd_series_ext.init_series(out_arr, xci__nccl,
            urlbe__eqg)
    return impl


@overload_method(SeriesStrMethodType, 'zfill', inline='always',
    no_unliteral=True)
def overload_str_method_zfill(S_str, width):
    int_arg_check('zfill', 'width', width)
    if S_str.stype.data == bodo.dict_str_arr_type:

        def _str_zfill_dict_impl(S_str, width):
            S = S_str._obj
            yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            out_arr = bodo.libs.dict_arr_ext.str_zfill(yyhe__alze, width)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return _str_zfill_dict_impl

    def impl(S_str, width):
        S = S_str._obj
        focn__xefsi = bodo.hiframes.pd_series_ext.get_series_data(S)
        urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
        xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
        numba.parfors.parfor.init_prange()
        tfok__mzybv = len(focn__xefsi)
        out_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(tfok__mzybv, -1)
        for lcpph__hjlc in numba.parfors.parfor.internal_prange(tfok__mzybv):
            if bodo.libs.array_kernels.isna(focn__xefsi, lcpph__hjlc):
                out_arr[lcpph__hjlc] = ''
                bodo.libs.array_kernels.setna(out_arr, lcpph__hjlc)
            else:
                out_arr[lcpph__hjlc] = focn__xefsi[lcpph__hjlc].zfill(width)
        return bodo.hiframes.pd_series_ext.init_series(out_arr, xci__nccl,
            urlbe__eqg)
    return impl


@overload_method(SeriesStrMethodType, 'slice', no_unliteral=True)
def overload_str_method_slice(S_str, start=None, stop=None, step=None):
    if not is_overload_none(start):
        int_arg_check('slice', 'start', start)
    if not is_overload_none(stop):
        int_arg_check('slice', 'stop', stop)
    if not is_overload_none(step):
        int_arg_check('slice', 'step', step)
    if S_str.stype.data == bodo.dict_str_arr_type:

        def _str_slice_dict_impl(S_str, start=None, stop=None, step=None):
            S = S_str._obj
            yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            out_arr = bodo.libs.dict_arr_ext.str_slice(yyhe__alze, start,
                stop, step)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return _str_slice_dict_impl

    def impl(S_str, start=None, stop=None, step=None):
        S = S_str._obj
        focn__xefsi = bodo.hiframes.pd_series_ext.get_series_data(S)
        urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
        xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
        numba.parfors.parfor.init_prange()
        tfok__mzybv = len(focn__xefsi)
        out_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(tfok__mzybv, -1)
        for lcpph__hjlc in numba.parfors.parfor.internal_prange(tfok__mzybv):
            if bodo.libs.array_kernels.isna(focn__xefsi, lcpph__hjlc):
                out_arr[lcpph__hjlc] = ''
                bodo.libs.array_kernels.setna(out_arr, lcpph__hjlc)
            else:
                out_arr[lcpph__hjlc] = focn__xefsi[lcpph__hjlc][start:stop:step
                    ]
        return bodo.hiframes.pd_series_ext.init_series(out_arr, xci__nccl,
            urlbe__eqg)
    return impl


@overload_method(SeriesStrMethodType, 'startswith', inline='always',
    no_unliteral=True)
def overload_str_method_startswith(S_str, pat, na=np.nan):
    not_supported_arg_check('startswith', 'na', na, np.nan)
    str_arg_check('startswith', 'pat', pat)
    if S_str.stype.data == bodo.dict_str_arr_type:

        def _str_startswith_dict_impl(S_str, pat, na=np.nan):
            S = S_str._obj
            yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            out_arr = bodo.libs.dict_arr_ext.str_startswith(yyhe__alze, pat, na
                )
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return _str_startswith_dict_impl

    def impl(S_str, pat, na=np.nan):
        S = S_str._obj
        focn__xefsi = bodo.hiframes.pd_series_ext.get_series_data(S)
        urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
        xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
        numba.parfors.parfor.init_prange()
        tfok__mzybv = len(focn__xefsi)
        out_arr = bodo.libs.bool_arr_ext.alloc_bool_array(tfok__mzybv)
        for i in numba.parfors.parfor.internal_prange(tfok__mzybv):
            if bodo.libs.array_kernels.isna(focn__xefsi, i):
                bodo.libs.array_kernels.setna(out_arr, i)
            else:
                out_arr[i] = focn__xefsi[i].startswith(pat)
        return bodo.hiframes.pd_series_ext.init_series(out_arr, xci__nccl,
            urlbe__eqg)
    return impl


@overload_method(SeriesStrMethodType, 'endswith', inline='always',
    no_unliteral=True)
def overload_str_method_endswith(S_str, pat, na=np.nan):
    not_supported_arg_check('endswith', 'na', na, np.nan)
    str_arg_check('endswith', 'pat', pat)
    if S_str.stype.data == bodo.dict_str_arr_type:

        def _str_endswith_dict_impl(S_str, pat, na=np.nan):
            S = S_str._obj
            yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
            xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
            urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
            out_arr = bodo.libs.dict_arr_ext.str_endswith(yyhe__alze, pat, na)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                xci__nccl, urlbe__eqg)
        return _str_endswith_dict_impl

    def impl(S_str, pat, na=np.nan):
        S = S_str._obj
        focn__xefsi = bodo.hiframes.pd_series_ext.get_series_data(S)
        urlbe__eqg = bodo.hiframes.pd_series_ext.get_series_name(S)
        xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
        numba.parfors.parfor.init_prange()
        tfok__mzybv = len(focn__xefsi)
        out_arr = bodo.libs.bool_arr_ext.alloc_bool_array(tfok__mzybv)
        for i in numba.parfors.parfor.internal_prange(tfok__mzybv):
            if bodo.libs.array_kernels.isna(focn__xefsi, i):
                bodo.libs.array_kernels.setna(out_arr, i)
            else:
                out_arr[i] = focn__xefsi[i].endswith(pat)
        return bodo.hiframes.pd_series_ext.init_series(out_arr, xci__nccl,
            urlbe__eqg)
    return impl


@overload(operator.getitem, no_unliteral=True)
def overload_str_method_getitem(S_str, ind):
    if not isinstance(S_str, SeriesStrMethodType):
        return
    if not isinstance(types.unliteral(ind), (types.SliceType, types.Integer)):
        raise BodoError(
            'index input to Series.str[] should be a slice or an integer')
    if isinstance(ind, types.SliceType):
        return lambda S_str, ind: S_str.slice(ind.start, ind.stop, ind.step)
    if isinstance(types.unliteral(ind), types.Integer):
        return lambda S_str, ind: S_str.get(ind)


@overload_method(SeriesStrMethodType, 'extract', inline='always',
    no_unliteral=True)
def overload_str_method_extract(S_str, pat, flags=0, expand=True):
    if not is_overload_constant_bool(expand):
        raise BodoError(
            "Series.str.extract(): 'expand' argument should be a constant bool"
            )
    fgnvs__waec, regex = _get_column_names_from_regex(pat, flags, 'extract')
    ewmmu__onrcb = len(fgnvs__waec)
    if S_str.stype.data == bodo.dict_str_arr_type:
        rtnfg__hvbnl = 'def impl(S_str, pat, flags=0, expand=True):\n'
        rtnfg__hvbnl += '  S = S_str._obj\n'
        rtnfg__hvbnl += (
            '  arr = bodo.hiframes.pd_series_ext.get_series_data(S)\n')
        rtnfg__hvbnl += (
            '  index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
        rtnfg__hvbnl += (
            '  name = bodo.hiframes.pd_series_ext.get_series_name(S)\n')
        rtnfg__hvbnl += f"""  out_arr_list = bodo.libs.dict_arr_ext.str_extract(arr, pat, flags, {ewmmu__onrcb})
"""
        for i in range(ewmmu__onrcb):
            rtnfg__hvbnl += f'  out_arr_{i} = out_arr_list[{i}]\n'
    else:
        rtnfg__hvbnl = 'def impl(S_str, pat, flags=0, expand=True):\n'
        rtnfg__hvbnl += '  regex = re.compile(pat, flags=flags)\n'
        rtnfg__hvbnl += '  S = S_str._obj\n'
        rtnfg__hvbnl += (
            '  str_arr = bodo.hiframes.pd_series_ext.get_series_data(S)\n')
        rtnfg__hvbnl += (
            '  index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
        rtnfg__hvbnl += (
            '  name = bodo.hiframes.pd_series_ext.get_series_name(S)\n')
        rtnfg__hvbnl += '  numba.parfors.parfor.init_prange()\n'
        rtnfg__hvbnl += '  n = len(str_arr)\n'
        for i in range(ewmmu__onrcb):
            rtnfg__hvbnl += (
                '  out_arr_{0} = bodo.libs.str_arr_ext.pre_alloc_string_array(n, -1)\n'
                .format(i))
        rtnfg__hvbnl += '  for j in numba.parfors.parfor.internal_prange(n):\n'
        rtnfg__hvbnl += '      if bodo.libs.array_kernels.isna(str_arr, j):\n'
        for i in range(ewmmu__onrcb):
            rtnfg__hvbnl += "          out_arr_{}[j] = ''\n".format(i)
            rtnfg__hvbnl += (
                '          bodo.libs.array_kernels.setna(out_arr_{}, j)\n'.
                format(i))
        rtnfg__hvbnl += '      else:\n'
        rtnfg__hvbnl += '          m = regex.search(str_arr[j])\n'
        rtnfg__hvbnl += '          if m:\n'
        rtnfg__hvbnl += '            g = m.groups()\n'
        for i in range(ewmmu__onrcb):
            rtnfg__hvbnl += '            out_arr_{0}[j] = g[{0}]\n'.format(i)
        rtnfg__hvbnl += '          else:\n'
        for i in range(ewmmu__onrcb):
            rtnfg__hvbnl += "            out_arr_{}[j] = ''\n".format(i)
            rtnfg__hvbnl += (
                '            bodo.libs.array_kernels.setna(out_arr_{}, j)\n'
                .format(i))
    if is_overload_false(expand) and regex.groups == 1:
        urlbe__eqg = "'{}'".format(list(regex.groupindex.keys()).pop()) if len(
            regex.groupindex.keys()) > 0 else 'name'
        rtnfg__hvbnl += (
            '  return bodo.hiframes.pd_series_ext.init_series(out_arr_0, index, {})\n'
            .format(urlbe__eqg))
        kps__dtfui = {}
        exec(rtnfg__hvbnl, {'re': re, 'bodo': bodo, 'numba': numba,
            'get_utf8_size': get_utf8_size}, kps__dtfui)
        impl = kps__dtfui['impl']
        return impl
    thgkk__rnqg = ', '.join('out_arr_{}'.format(i) for i in range(ewmmu__onrcb)
        )
    impl = bodo.hiframes.dataframe_impl._gen_init_df(rtnfg__hvbnl,
        fgnvs__waec, thgkk__rnqg, 'index', extra_globals={'get_utf8_size':
        get_utf8_size, 're': re})
    return impl


@overload_method(SeriesStrMethodType, 'extractall', inline='always',
    no_unliteral=True)
def overload_str_method_extractall(S_str, pat, flags=0):
    fgnvs__waec, wvbd__znd = _get_column_names_from_regex(pat, flags,
        'extractall')
    ewmmu__onrcb = len(fgnvs__waec)
    algn__qsmbx = isinstance(S_str.stype.index, StringIndexType)
    zgafr__qhp = ewmmu__onrcb > 1
    qewl__cug = '_multi' if zgafr__qhp else ''
    if S_str.stype.data == bodo.dict_str_arr_type:
        rtnfg__hvbnl = 'def impl(S_str, pat, flags=0):\n'
        rtnfg__hvbnl += '  S = S_str._obj\n'
        rtnfg__hvbnl += (
            '  arr = bodo.hiframes.pd_series_ext.get_series_data(S)\n')
        rtnfg__hvbnl += (
            '  index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
        rtnfg__hvbnl += (
            '  name = bodo.hiframes.pd_series_ext.get_series_name(S)\n')
        rtnfg__hvbnl += (
            '  index_arr = bodo.utils.conversion.index_to_array(index)\n')
        rtnfg__hvbnl += (
            '  index_name = bodo.hiframes.pd_index_ext.get_index_name(index)\n'
            )
        rtnfg__hvbnl += '  regex = re.compile(pat, flags=flags)\n'
        rtnfg__hvbnl += '  out_ind_arr, out_match_arr, out_arr_list = '
        rtnfg__hvbnl += f'bodo.libs.dict_arr_ext.str_extractall{qewl__cug}(\n'
        rtnfg__hvbnl += f'arr, regex, {ewmmu__onrcb}, index_arr)\n'
        for i in range(ewmmu__onrcb):
            rtnfg__hvbnl += f'  out_arr_{i} = out_arr_list[{i}]\n'
        rtnfg__hvbnl += (
            '  out_index = bodo.hiframes.pd_multi_index_ext.init_multi_index(\n'
            )
        rtnfg__hvbnl += (
            "    (out_ind_arr, out_match_arr), (index_name, 'match'))\n")
    else:
        rtnfg__hvbnl = 'def impl(S_str, pat, flags=0):\n'
        rtnfg__hvbnl += '  regex = re.compile(pat, flags=flags)\n'
        rtnfg__hvbnl += '  S = S_str._obj\n'
        rtnfg__hvbnl += (
            '  str_arr = bodo.hiframes.pd_series_ext.get_series_data(S)\n')
        rtnfg__hvbnl += (
            '  index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
        rtnfg__hvbnl += (
            '  name = bodo.hiframes.pd_series_ext.get_series_name(S)\n')
        rtnfg__hvbnl += (
            '  index_arr = bodo.utils.conversion.index_to_array(index)\n')
        rtnfg__hvbnl += (
            '  index_name = bodo.hiframes.pd_index_ext.get_index_name(index)\n'
            )
        rtnfg__hvbnl += '  numba.parfors.parfor.init_prange()\n'
        rtnfg__hvbnl += '  n = len(str_arr)\n'
        rtnfg__hvbnl += '  out_n_l = [0]\n'
        for i in range(ewmmu__onrcb):
            rtnfg__hvbnl += '  num_chars_{} = 0\n'.format(i)
        if algn__qsmbx:
            rtnfg__hvbnl += '  index_num_chars = 0\n'
        rtnfg__hvbnl += '  for i in numba.parfors.parfor.internal_prange(n):\n'
        if algn__qsmbx:
            rtnfg__hvbnl += (
                '      index_num_chars += get_utf8_size(index_arr[i])\n')
        rtnfg__hvbnl += '      if bodo.libs.array_kernels.isna(str_arr, i):\n'
        rtnfg__hvbnl += '          continue\n'
        rtnfg__hvbnl += '      m = regex.findall(str_arr[i])\n'
        rtnfg__hvbnl += '      out_n_l[0] += len(m)\n'
        for i in range(ewmmu__onrcb):
            rtnfg__hvbnl += '      l_{} = 0\n'.format(i)
        rtnfg__hvbnl += '      for s in m:\n'
        for i in range(ewmmu__onrcb):
            rtnfg__hvbnl += '        l_{} += get_utf8_size(s{})\n'.format(i,
                '[{}]'.format(i) if ewmmu__onrcb > 1 else '')
        for i in range(ewmmu__onrcb):
            rtnfg__hvbnl += '      num_chars_{0} += l_{0}\n'.format(i)
        rtnfg__hvbnl += """  out_n = bodo.libs.distributed_api.local_alloc_size(out_n_l[0], str_arr)
"""
        for i in range(ewmmu__onrcb):
            rtnfg__hvbnl += (
                """  out_arr_{0} = bodo.libs.str_arr_ext.pre_alloc_string_array(out_n, num_chars_{0})
"""
                .format(i))
        if algn__qsmbx:
            rtnfg__hvbnl += """  out_ind_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(out_n, index_num_chars)
"""
        else:
            rtnfg__hvbnl += (
                '  out_ind_arr = np.empty(out_n, index_arr.dtype)\n')
        rtnfg__hvbnl += '  out_match_arr = np.empty(out_n, np.int64)\n'
        rtnfg__hvbnl += '  out_ind = 0\n'
        rtnfg__hvbnl += '  for j in numba.parfors.parfor.internal_prange(n):\n'
        rtnfg__hvbnl += '      if bodo.libs.array_kernels.isna(str_arr, j):\n'
        rtnfg__hvbnl += '          continue\n'
        rtnfg__hvbnl += '      m = regex.findall(str_arr[j])\n'
        rtnfg__hvbnl += '      for k, s in enumerate(m):\n'
        for i in range(ewmmu__onrcb):
            rtnfg__hvbnl += (
                """        bodo.libs.distributed_api.set_arr_local(out_arr_{}, out_ind, s{})
"""
                .format(i, '[{}]'.format(i) if ewmmu__onrcb > 1 else ''))
        rtnfg__hvbnl += """        bodo.libs.distributed_api.set_arr_local(out_ind_arr, out_ind, index_arr[j])
"""
        rtnfg__hvbnl += """        bodo.libs.distributed_api.set_arr_local(out_match_arr, out_ind, k)
"""
        rtnfg__hvbnl += '        out_ind += 1\n'
        rtnfg__hvbnl += (
            '  out_index = bodo.hiframes.pd_multi_index_ext.init_multi_index(\n'
            )
        rtnfg__hvbnl += (
            "    (out_ind_arr, out_match_arr), (index_name, 'match'))\n")
    thgkk__rnqg = ', '.join('out_arr_{}'.format(i) for i in range(ewmmu__onrcb)
        )
    impl = bodo.hiframes.dataframe_impl._gen_init_df(rtnfg__hvbnl,
        fgnvs__waec, thgkk__rnqg, 'out_index', extra_globals={
        'get_utf8_size': get_utf8_size, 're': re})
    return impl


def _get_column_names_from_regex(pat, flags, func_name):
    if not is_overload_constant_str(pat):
        raise BodoError(
            "Series.str.{}(): 'pat' argument should be a constant string".
            format(func_name))
    if not is_overload_constant_int(flags):
        raise BodoError(
            "Series.str.{}(): 'flags' argument should be a constant int".
            format(func_name))
    pat = get_overload_const_str(pat)
    flags = get_overload_const_int(flags)
    regex = re.compile(pat, flags=flags)
    if regex.groups == 0:
        raise BodoError(
            'Series.str.{}(): pattern {} contains no capture groups'.format
            (func_name, pat))
    jmx__rdjs = dict(zip(regex.groupindex.values(), regex.groupindex.keys()))
    fgnvs__waec = [jmx__rdjs.get(1 + i, i) for i in range(regex.groups)]
    return fgnvs__waec, regex


def create_str2str_methods_overload(func_name):
    nxq__cgld = func_name in ['lstrip', 'rstrip', 'strip']
    rtnfg__hvbnl = f"""def f({'S_str, to_strip=None' if nxq__cgld else 'S_str'}):
    S = S_str._obj
    str_arr = bodo.hiframes.pd_series_ext.get_series_data(S)
    str_arr = decode_if_dict_array(str_arr)
    index = bodo.hiframes.pd_series_ext.get_series_index(S)
    name = bodo.hiframes.pd_series_ext.get_series_name(S)
    numba.parfors.parfor.init_prange()
    n = len(str_arr)
    num_chars = {'-1' if nxq__cgld else 'num_total_chars(str_arr)'}
    out_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(n, num_chars)
    for j in numba.parfors.parfor.internal_prange(n):
        if bodo.libs.array_kernels.isna(str_arr, j):
            out_arr[j] = ""
            bodo.libs.array_kernels.setna(out_arr, j)
        else:
            out_arr[j] = str_arr[j].{func_name}({'to_strip' if nxq__cgld else ''})
    return bodo.hiframes.pd_series_ext.init_series(out_arr, index, name)
"""
    rtnfg__hvbnl += f"""def _dict_impl({'S_str, to_strip=None' if nxq__cgld else 'S_str'}):
    S = S_str._obj
    arr = bodo.hiframes.pd_series_ext.get_series_data(S)
    index = bodo.hiframes.pd_series_ext.get_series_index(S)
    name = bodo.hiframes.pd_series_ext.get_series_name(S)
    out_arr = bodo.libs.dict_arr_ext.str_{func_name}({'arr, to_strip' if nxq__cgld else 'arr'})
    return bodo.hiframes.pd_series_ext.init_series(out_arr, index, name)
"""
    kps__dtfui = {}
    exec(rtnfg__hvbnl, {'bodo': bodo, 'numba': numba, 'num_total_chars':
        bodo.libs.str_arr_ext.num_total_chars, 'get_utf8_size': bodo.libs.
        str_arr_ext.get_utf8_size, 'decode_if_dict_array': bodo.utils.
        typing.decode_if_dict_array}, kps__dtfui)
    ezhtf__skp = kps__dtfui['f']
    noc__jtdgf = kps__dtfui['_dict_impl']
    if nxq__cgld:

        def overload_strip_method(S_str, to_strip=None):
            if not is_overload_none(to_strip):
                str_arg_check(func_name, 'to_strip', to_strip)
            if S_str.stype.data == bodo.dict_str_arr_type:
                return noc__jtdgf
            return ezhtf__skp
        return overload_strip_method
    else:

        def overload_str_method_dict_supported(S_str):
            if S_str.stype.data == bodo.dict_str_arr_type:
                return noc__jtdgf
            return ezhtf__skp
        return overload_str_method_dict_supported


def create_str2bool_methods_overload(func_name):
    rtnfg__hvbnl = 'def dict_impl(S_str):\n'
    rtnfg__hvbnl += '    S = S_str._obj\n'
    rtnfg__hvbnl += (
        '    arr = bodo.hiframes.pd_series_ext.get_series_data(S)\n')
    rtnfg__hvbnl += (
        '    index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
    rtnfg__hvbnl += (
        '    name = bodo.hiframes.pd_series_ext.get_series_name(S)\n')
    rtnfg__hvbnl += (
        f'    out_arr = bodo.libs.dict_arr_ext.str_{func_name}(arr)\n')
    rtnfg__hvbnl += (
        '    return bodo.hiframes.pd_series_ext.init_series(out_arr, index, name)\n'
        )
    rtnfg__hvbnl += 'def impl(S_str):\n'
    rtnfg__hvbnl += '    S = S_str._obj\n'
    rtnfg__hvbnl += (
        '    str_arr = bodo.hiframes.pd_series_ext.get_series_data(S)\n')
    rtnfg__hvbnl += (
        '    index = bodo.hiframes.pd_series_ext.get_series_index(S)\n')
    rtnfg__hvbnl += (
        '    name = bodo.hiframes.pd_series_ext.get_series_name(S)\n')
    rtnfg__hvbnl += '    numba.parfors.parfor.init_prange()\n'
    rtnfg__hvbnl += '    l = len(str_arr)\n'
    rtnfg__hvbnl += (
        '    out_arr = bodo.libs.bool_arr_ext.alloc_bool_array(l)\n')
    rtnfg__hvbnl += '    for i in numba.parfors.parfor.internal_prange(l):\n'
    rtnfg__hvbnl += '        if bodo.libs.array_kernels.isna(str_arr, i):\n'
    rtnfg__hvbnl += '            bodo.libs.array_kernels.setna(out_arr, i)\n'
    rtnfg__hvbnl += '        else:\n'
    rtnfg__hvbnl += ('            out_arr[i] = np.bool_(str_arr[i].{}())\n'
        .format(func_name))
    rtnfg__hvbnl += '    return bodo.hiframes.pd_series_ext.init_series(\n'
    rtnfg__hvbnl += '      out_arr,index, name)\n'
    kps__dtfui = {}
    exec(rtnfg__hvbnl, {'bodo': bodo, 'numba': numba, 'np': np}, kps__dtfui)
    impl = kps__dtfui['impl']
    kejj__uuai = kps__dtfui['dict_impl']

    def overload_str2bool_methods(S_str):
        if S_str.stype.data == bodo.dict_str_arr_type:
            return kejj__uuai
        return impl
    return overload_str2bool_methods


def _install_str2str_methods():
    for qtga__jwyp in bodo.hiframes.pd_series_ext.str2str_methods:
        ytfrc__ljxbj = create_str2str_methods_overload(qtga__jwyp)
        overload_method(SeriesStrMethodType, qtga__jwyp, inline='always',
            no_unliteral=True)(ytfrc__ljxbj)


def _install_str2bool_methods():
    for qtga__jwyp in bodo.hiframes.pd_series_ext.str2bool_methods:
        ytfrc__ljxbj = create_str2bool_methods_overload(qtga__jwyp)
        overload_method(SeriesStrMethodType, qtga__jwyp, inline='always',
            no_unliteral=True)(ytfrc__ljxbj)


_install_str2str_methods()
_install_str2bool_methods()


@overload_attribute(SeriesType, 'cat')
def overload_series_cat(s):
    if not isinstance(s.dtype, bodo.hiframes.pd_categorical_ext.
        PDCategoricalDtype):
        raise BodoError('Can only use .cat accessor with categorical values.')
    return lambda s: bodo.hiframes.series_str_impl.init_series_cat_method(s)


class SeriesCatMethodType(types.Type):

    def __init__(self, stype):
        self.stype = stype
        urlbe__eqg = 'SeriesCatMethodType({})'.format(stype)
        super(SeriesCatMethodType, self).__init__(urlbe__eqg)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


@register_model(SeriesCatMethodType)
class SeriesCatModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        kcht__ikpuw = [('obj', fe_type.stype)]
        super(SeriesCatModel, self).__init__(dmm, fe_type, kcht__ikpuw)


make_attribute_wrapper(SeriesCatMethodType, 'obj', '_obj')


@intrinsic
def init_series_cat_method(typingctx, obj=None):

    def codegen(context, builder, signature, args):
        oubjq__aif, = args
        niaa__czb = signature.return_type
        oorc__uauk = cgutils.create_struct_proxy(niaa__czb)(context, builder)
        oorc__uauk.obj = oubjq__aif
        context.nrt.incref(builder, signature.args[0], oubjq__aif)
        return oorc__uauk._getvalue()
    return SeriesCatMethodType(obj)(obj), codegen


@overload_attribute(SeriesCatMethodType, 'codes')
def series_cat_codes_overload(S_dt):

    def impl(S_dt):
        S = S_dt._obj
        yyhe__alze = bodo.hiframes.pd_series_ext.get_series_data(S)
        xci__nccl = bodo.hiframes.pd_series_ext.get_series_index(S)
        urlbe__eqg = None
        return bodo.hiframes.pd_series_ext.init_series(bodo.hiframes.
            pd_categorical_ext.get_categorical_arr_codes(yyhe__alze),
            xci__nccl, urlbe__eqg)
    return impl


unsupported_cat_attrs = {'categories', 'ordered'}
unsupported_cat_methods = {'rename_categories', 'reorder_categories',
    'add_categories', 'remove_categories', 'remove_unused_categories',
    'set_categories', 'as_ordered', 'as_unordered'}


def _install_catseries_unsupported():
    for wmwq__uaw in unsupported_cat_attrs:
        kpq__rbbon = 'Series.cat.' + wmwq__uaw
        overload_attribute(SeriesCatMethodType, wmwq__uaw)(
            create_unsupported_overload(kpq__rbbon))
    for hfub__skuve in unsupported_cat_methods:
        kpq__rbbon = 'Series.cat.' + hfub__skuve
        overload_method(SeriesCatMethodType, hfub__skuve)(
            create_unsupported_overload(kpq__rbbon))


_install_catseries_unsupported()
unsupported_str_methods = {'casefold', 'decode', 'encode', 'findall',
    'fullmatch', 'index', 'match', 'normalize', 'partition', 'rindex',
    'rpartition', 'slice_replace', 'rsplit', 'translate', 'wrap', 'get_dummies'
    }


def _install_strseries_unsupported():
    for hfub__skuve in unsupported_str_methods:
        kpq__rbbon = 'Series.str.' + hfub__skuve
        overload_method(SeriesStrMethodType, hfub__skuve)(
            create_unsupported_overload(kpq__rbbon))


_install_strseries_unsupported()
