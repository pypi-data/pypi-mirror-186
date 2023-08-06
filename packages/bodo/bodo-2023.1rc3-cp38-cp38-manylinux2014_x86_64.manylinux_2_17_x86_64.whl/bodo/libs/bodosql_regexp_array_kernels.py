"""
Implements regexp array kernels that are specific to BodoSQL
"""
import re
import numba
from numba.core import types
import bodo
from bodo.libs.bodosql_array_kernel_utils import *


def posix_to_re(pattern):
    cvas__vysns = {'[:alnum:]': 'A-Za-z0-9', '[:alpha:]': 'A-Za-z',
        '[:ascii:]': '\x01-\x7f', '[:blank:]': ' \t', '[:cntrl:]':
        '\x01-\x1f\x7f', '[:digit:]': '0-9', '[:graph:]': '!-~',
        '[:lower:]': 'a-z', '[:print:]': ' -~', '[:punct:]':
        '\\]\\[!"#$%&\'()*+,./:;<=>?@\\^_`{|}~-', '[:space:]':
        ' \t\r\n\x0b\x0c', '[:upper:]': 'A-Z', '[:word:]': 'A-Za-z0-9_',
        '[:xdigit:]': 'A-Fa-f0-9'}
    for fcr__jkxk in cvas__vysns:
        pattern = pattern.replace(fcr__jkxk, cvas__vysns[fcr__jkxk])
    return pattern


def make_flag_bitvector(flags):
    ccm__vkm = 0
    if 'i' in flags:
        if 'c' not in flags or flags.rindex('i') > flags.rindex('c'):
            ccm__vkm = ccm__vkm | re.I
    if 'm' in flags:
        ccm__vkm = ccm__vkm | re.M
    if 's' in flags:
        ccm__vkm = ccm__vkm | re.S
    return ccm__vkm


@numba.generated_jit(nopython=True)
def regexp_count(arr, pattern, position, flags):
    args = [arr, pattern, position, flags]
    for neop__erkx in range(4):
        if isinstance(args[neop__erkx], types.optional):
            return unopt_argument(
                'bodo.libs.bodosql_array_kernels.regexp_count', ['arr',
                'pattern', 'position', 'flags'], neop__erkx)

    def impl(arr, pattern, position, flags):
        return regexp_count_util(arr, numba.literally(pattern), position,
            numba.literally(flags))
    return impl


@numba.generated_jit(nopython=True)
def regexp_instr(arr, pattern, position, occurrence, option, flags, group):
    args = [arr, pattern, position, occurrence, option, flags, group]
    for neop__erkx in range(7):
        if isinstance(args[neop__erkx], types.optional):
            return unopt_argument(
                'bodo.libs.bodosql_array_kernels.regexp_instr', ['arr',
                'pattern', 'position', 'occurrence', 'option', 'flags',
                'group'], neop__erkx)

    def impl(arr, pattern, position, occurrence, option, flags, group):
        return regexp_instr_util(arr, numba.literally(pattern), position,
            occurrence, option, numba.literally(flags), group)
    return impl


@numba.generated_jit(nopython=True)
def regexp_like(arr, pattern, flags):
    args = [arr, pattern, flags]
    for neop__erkx in range(3):
        if isinstance(args[neop__erkx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.regexp_like'
                , ['arr', 'pattern', 'flags'], neop__erkx)

    def impl(arr, pattern, flags):
        return regexp_like_util(arr, numba.literally(pattern), numba.
            literally(flags))
    return impl


@numba.generated_jit(nopython=True)
def regexp_replace(arr, pattern, replacement, position, occurrence, flags):
    args = [arr, pattern, replacement, position, occurrence, flags]
    for neop__erkx in range(6):
        if isinstance(args[neop__erkx], types.optional):
            return unopt_argument(
                'bodo.libs.bodosql_array_kernels.regexp_replace', ['arr',
                'pattern', 'replacement', 'position', 'occurrence', 'flags'
                ], neop__erkx)

    def impl(arr, pattern, replacement, position, occurrence, flags):
        return regexp_replace_util(arr, numba.literally(pattern),
            replacement, position, occurrence, numba.literally(flags))
    return impl


@numba.generated_jit(nopython=True)
def regexp_substr(arr, pattern, position, occurrence, flags, group):
    args = [arr, pattern, position, occurrence, flags, group]
    for neop__erkx in range(6):
        if isinstance(args[neop__erkx], types.optional):
            return unopt_argument(
                'bodo.libs.bodosql_array_kernels.regexp_substr', ['arr',
                'pattern', 'position', 'occurrence', 'flags', 'group'],
                neop__erkx)

    def impl(arr, pattern, position, occurrence, flags, group):
        return regexp_substr_util(arr, numba.literally(pattern), position,
            occurrence, numba.literally(flags), group)
    return impl


@numba.generated_jit(nopython=True)
def regexp_count_util(arr, pattern, position, flags):
    verify_string_arg(arr, 'REGEXP_COUNT', 'arr')
    verify_scalar_string_arg(pattern, 'REGEXP_COUNT', 'pattern')
    verify_int_arg(position, 'REGEXP_COUNT', 'position')
    verify_scalar_string_arg(flags, 'REGEXP_COUNT', 'flags')
    xcg__hqv = ['arr', 'pattern', 'position', 'flags']
    mme__raem = [arr, pattern, position, flags]
    wen__lhwpw = [True] * 4
    okwgj__wdbnl = bodo.utils.typing.get_overload_const_str(pattern)
    xvsl__zvw = posix_to_re(okwgj__wdbnl)
    uvwm__ggatb = bodo.utils.typing.get_overload_const_str(flags)
    ungr__snqym = make_flag_bitvector(uvwm__ggatb)
    gcpoh__oii = '\n'
    vze__rvx = ''
    if bodo.utils.utils.is_array_typ(position, True):
        vze__rvx += (
            "if arg2 <= 0: raise ValueError('REGEXP_COUNT requires a positive position')\n"
            )
    else:
        gcpoh__oii += """if position <= 0: raise ValueError('REGEXP_COUNT requires a positive position')
"""
    if xvsl__zvw == '':
        vze__rvx += 'res[i] = 0'
    else:
        gcpoh__oii += f'r = re.compile({repr(xvsl__zvw)}, {ungr__snqym})'
        vze__rvx += 'res[i] = len(r.findall(arg0[arg2-1:]))'
    oas__cnbc = bodo.libs.int_arr_ext.IntegerArrayType(types.int32)
    return gen_vectorized(xcg__hqv, mme__raem, wen__lhwpw, vze__rvx,
        oas__cnbc, prefix_code=gcpoh__oii)


@numba.generated_jit(nopython=True)
def regexp_instr_util(arr, pattern, position, occurrence, option, flags, group
    ):
    verify_string_arg(arr, 'REGEXP_INSTR', 'arr')
    verify_scalar_string_arg(pattern, 'REGEXP_INSTR', 'pattern')
    verify_int_arg(position, 'REGEXP_INSTR', 'position')
    verify_int_arg(occurrence, 'REGEXP_INSTR', 'occurrence')
    verify_int_arg(option, 'REGEXP_INSTR', 'option')
    verify_scalar_string_arg(flags, 'REGEXP_INSTR', 'flags')
    verify_int_arg(group, 'REGEXP_INSTR', 'group')
    xcg__hqv = ['arr', 'pattern', 'position', 'occurrence', 'option',
        'flags', 'group']
    mme__raem = [arr, pattern, position, occurrence, option, flags, group]
    wen__lhwpw = [True] * 7
    okwgj__wdbnl = bodo.utils.typing.get_overload_const_str(pattern)
    xvsl__zvw = posix_to_re(okwgj__wdbnl)
    ore__exuu = re.compile(okwgj__wdbnl).groups
    uvwm__ggatb = bodo.utils.typing.get_overload_const_str(flags)
    ungr__snqym = make_flag_bitvector(uvwm__ggatb)
    gcpoh__oii = '\n'
    vze__rvx = ''
    if bodo.utils.utils.is_array_typ(position, True):
        vze__rvx += (
            "if arg2 <= 0: raise ValueError('REGEXP_INSTR requires a positive position')\n"
            )
    else:
        gcpoh__oii += """if position <= 0: raise ValueError('REGEXP_INSTR requires a positive position')
"""
    if bodo.utils.utils.is_array_typ(occurrence, True):
        vze__rvx += """if arg3 <= 0: raise ValueError('REGEXP_INSTR requires a positive occurrence')
"""
    else:
        gcpoh__oii += """if occurrence <= 0: raise ValueError('REGEXP_INSTR requires a positive occurrence')
"""
    if bodo.utils.utils.is_array_typ(option, True):
        vze__rvx += """if arg4 != 0 and arg4 != 1: raise ValueError('REGEXP_INSTR requires option to be 0 or 1')
"""
    else:
        gcpoh__oii += """if option != 0 and option != 1: raise ValueError('REGEXP_INSTR requires option to be 0 or 1')
"""
    if 'e' in uvwm__ggatb:
        if bodo.utils.utils.is_array_typ(group, True):
            vze__rvx += f"""if not (1 <= arg6 <= {ore__exuu}): raise ValueError('REGEXP_INSTR requires a valid group number')
"""
        else:
            gcpoh__oii += f"""if not (1 <= group <= {ore__exuu}): raise ValueError('REGEXP_INSTR requires a valid group number')
"""
    if xvsl__zvw == '':
        vze__rvx += 'res[i] = 0'
    else:
        gcpoh__oii += f'r = re.compile({repr(xvsl__zvw)}, {ungr__snqym})'
        vze__rvx += 'arg0 = arg0[arg2-1:]\n'
        vze__rvx += 'res[i] = 0\n'
        vze__rvx += 'offset = arg2\n'
        vze__rvx += 'for j in range(arg3):\n'
        vze__rvx += '   match = r.search(arg0)\n'
        vze__rvx += '   if match is None:\n'
        vze__rvx += '      res[i] = 0\n'
        vze__rvx += '      break\n'
        vze__rvx += '   start, end = match.span()\n'
        vze__rvx += '   if j == arg3 - 1:\n'
        if 'e' in uvwm__ggatb:
            vze__rvx += '      res[i] = offset + match.span(arg6)[arg4]\n'
        else:
            vze__rvx += '      res[i] = offset + match.span()[arg4]\n'
        vze__rvx += '   else:\n'
        vze__rvx += '      offset += end\n'
        vze__rvx += '      arg0 = arg0[end:]\n'
    oas__cnbc = bodo.libs.int_arr_ext.IntegerArrayType(types.int32)
    return gen_vectorized(xcg__hqv, mme__raem, wen__lhwpw, vze__rvx,
        oas__cnbc, prefix_code=gcpoh__oii)


@numba.generated_jit(nopython=True)
def regexp_like_util(arr, pattern, flags):
    verify_string_arg(arr, 'REGEXP_LIKE', 'arr')
    verify_scalar_string_arg(pattern, 'REGEXP_LIKE', 'pattern')
    verify_scalar_string_arg(flags, 'REGEXP_LIKE', 'flags')
    xcg__hqv = ['arr', 'pattern', 'flags']
    mme__raem = [arr, pattern, flags]
    wen__lhwpw = [True] * 3
    okwgj__wdbnl = bodo.utils.typing.get_overload_const_str(pattern)
    xvsl__zvw = posix_to_re(okwgj__wdbnl)
    uvwm__ggatb = bodo.utils.typing.get_overload_const_str(flags)
    ungr__snqym = make_flag_bitvector(uvwm__ggatb)
    if xvsl__zvw == '':
        gcpoh__oii = None
        vze__rvx = 'res[i] = len(arg0) == 0'
    else:
        gcpoh__oii = f'r = re.compile({repr(xvsl__zvw)}, {ungr__snqym})'
        vze__rvx = 'if r.fullmatch(arg0) is None:\n'
        vze__rvx += '   res[i] = False\n'
        vze__rvx += 'else:\n'
        vze__rvx += '   res[i] = True\n'
    oas__cnbc = bodo.libs.bool_arr_ext.boolean_array
    return gen_vectorized(xcg__hqv, mme__raem, wen__lhwpw, vze__rvx,
        oas__cnbc, prefix_code=gcpoh__oii)


@numba.generated_jit(nopython=True)
def regexp_replace_util(arr, pattern, replacement, position, occurrence, flags
    ):
    verify_string_arg(arr, 'REGEXP_REPLACE', 'arr')
    verify_scalar_string_arg(pattern, 'REGEXP_REPLACE', 'pattern')
    verify_string_arg(replacement, 'REGEXP_REPLACE', 'replacement')
    verify_int_arg(position, 'REGEXP_REPLACE', 'position')
    verify_int_arg(occurrence, 'REGEXP_REPLACE', 'occurrence')
    verify_scalar_string_arg(flags, 'REGEXP_REPLACE', 'flags')
    xcg__hqv = ['arr', 'pattern', 'replacement', 'position', 'occurrence',
        'flags']
    mme__raem = [arr, pattern, replacement, position, occurrence, flags]
    wen__lhwpw = [True] * 6
    okwgj__wdbnl = bodo.utils.typing.get_overload_const_str(pattern)
    xvsl__zvw = posix_to_re(okwgj__wdbnl)
    uvwm__ggatb = bodo.utils.typing.get_overload_const_str(flags)
    ungr__snqym = make_flag_bitvector(uvwm__ggatb)
    gcpoh__oii = '\n'
    vze__rvx = ''
    if bodo.utils.utils.is_array_typ(position, True):
        vze__rvx += """if arg3 <= 0: raise ValueError('REGEXP_REPLACE requires a positive position')
"""
    else:
        gcpoh__oii += """if position <= 0: raise ValueError('REGEXP_REPLACE requires a positive position')
"""
    if bodo.utils.utils.is_array_typ(occurrence, True):
        vze__rvx += """if arg4 < 0: raise ValueError('REGEXP_REPLACE requires a non-negative occurrence')
"""
    else:
        gcpoh__oii += """if occurrence < 0: raise ValueError('REGEXP_REPLACE requires a non-negative occurrence')
"""
    if xvsl__zvw == '':
        vze__rvx += 'res[i] = arg0'
    else:
        gcpoh__oii += f'r = re.compile({repr(xvsl__zvw)}, {ungr__snqym})'
        vze__rvx += 'result = arg0[:arg3-1]\n'
        vze__rvx += 'arg0 = arg0[arg3-1:]\n'
        vze__rvx += 'if arg4 == 0:\n'
        vze__rvx += '   res[i] = result + r.sub(arg2, arg0)\n'
        vze__rvx += 'else:\n'
        vze__rvx += '   nomatch = False\n'
        vze__rvx += '   for j in range(arg4 - 1):\n'
        vze__rvx += '      match = r.search(arg0)\n'
        vze__rvx += '      if match is None:\n'
        vze__rvx += '         res[i] = result + arg0\n'
        vze__rvx += '         nomatch = True\n'
        vze__rvx += '         break\n'
        vze__rvx += '      _, end = match.span()\n'
        vze__rvx += '      result += arg0[:end]\n'
        vze__rvx += '      arg0 = arg0[end:]\n'
        vze__rvx += '   if nomatch == False:\n'
        vze__rvx += '      result += r.sub(arg2, arg0, count=1)\n'
        vze__rvx += '      res[i] = result'
    oas__cnbc = bodo.string_array_type
    return gen_vectorized(xcg__hqv, mme__raem, wen__lhwpw, vze__rvx,
        oas__cnbc, prefix_code=gcpoh__oii)


@numba.generated_jit(nopython=True)
def regexp_substr_util(arr, pattern, position, occurrence, flags, group):
    verify_string_arg(arr, 'REGEXP_SUBSTR', 'arr')
    verify_scalar_string_arg(pattern, 'REGEXP_SUBSTR', 'pattern')
    verify_int_arg(position, 'REGEXP_SUBSTR', 'position')
    verify_int_arg(occurrence, 'REGEXP_SUBSTR', 'occurrence')
    verify_scalar_string_arg(flags, 'REGEXP_SUBSTR', 'flags')
    verify_int_arg(group, 'REGEXP_SUBSTR', 'group')
    xcg__hqv = ['arr', 'pattern', 'position', 'occurrence', 'flags', 'group']
    mme__raem = [arr, pattern, position, occurrence, flags, group]
    wen__lhwpw = [True] * 6
    okwgj__wdbnl = bodo.utils.typing.get_overload_const_str(pattern)
    xvsl__zvw = posix_to_re(okwgj__wdbnl)
    ore__exuu = re.compile(okwgj__wdbnl).groups
    uvwm__ggatb = bodo.utils.typing.get_overload_const_str(flags)
    ungr__snqym = make_flag_bitvector(uvwm__ggatb)
    gcpoh__oii = '\n'
    vze__rvx = ''
    if bodo.utils.utils.is_array_typ(position, True):
        vze__rvx += """if arg2 <= 0: raise ValueError('REGEXP_SUBSTR requires a positive position')
"""
    else:
        gcpoh__oii += """if position <= 0: raise ValueError('REGEXP_SUBSTR requires a positive position')
"""
    if bodo.utils.utils.is_array_typ(occurrence, True):
        vze__rvx += """if arg3 <= 0: raise ValueError('REGEXP_SUBSTR requires a positive occurrence')
"""
    else:
        gcpoh__oii += """if occurrence <= 0: raise ValueError('REGEXP_SUBSTR requires a positive occurrence')
"""
    if 'e' in uvwm__ggatb:
        if bodo.utils.utils.is_array_typ(group, True):
            vze__rvx += f"""if not (1 <= arg5 <= {ore__exuu}): raise ValueError('REGEXP_SUBSTR requires a valid group number')
"""
        else:
            gcpoh__oii += f"""if not (1 <= group <= {ore__exuu}): raise ValueError('REGEXP_SUBSTR requires a valid group number')
"""
    if xvsl__zvw == '':
        vze__rvx += 'bodo.libs.array_kernels.setna(res, i)'
    else:
        gcpoh__oii += f'r = re.compile({repr(xvsl__zvw)}, {ungr__snqym})'
        if 'e' in uvwm__ggatb:
            vze__rvx += 'matches = r.findall(arg0[arg2-1:])\n'
            vze__rvx += f'if len(matches) < arg3:\n'
            vze__rvx += '   bodo.libs.array_kernels.setna(res, i)\n'
            vze__rvx += 'else:\n'
            if ore__exuu == 1:
                vze__rvx += '   res[i] = matches[arg3-1]\n'
            else:
                vze__rvx += '   res[i] = matches[arg3-1][arg5-1]\n'
        else:
            vze__rvx += 'arg0 = str(arg0)[arg2-1:]\n'
            vze__rvx += 'for j in range(arg3):\n'
            vze__rvx += '   match = r.search(arg0)\n'
            vze__rvx += '   if match is None:\n'
            vze__rvx += '      bodo.libs.array_kernels.setna(res, i)\n'
            vze__rvx += '      break\n'
            vze__rvx += '   start, end = match.span()\n'
            vze__rvx += '   if j == arg3 - 1:\n'
            vze__rvx += '      res[i] = arg0[start:end]\n'
            vze__rvx += '   else:\n'
            vze__rvx += '      arg0 = arg0[end:]\n'
    oas__cnbc = bodo.string_array_type
    return gen_vectorized(xcg__hqv, mme__raem, wen__lhwpw, vze__rvx,
        oas__cnbc, prefix_code=gcpoh__oii)
