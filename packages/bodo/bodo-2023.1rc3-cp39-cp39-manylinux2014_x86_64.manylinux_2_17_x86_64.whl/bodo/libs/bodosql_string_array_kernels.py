"""
Implements string array kernels that are specific to BodoSQL
"""
import numba
import numpy as np
from numba.core import types
from numba.extending import overload, register_jitable
import bodo
from bodo.libs.bodosql_array_kernel_utils import *


@numba.generated_jit(nopython=True)
def char(arr):
    if isinstance(arr, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.char_util',
            ['arr'], 0)

    def impl(arr):
        return char_util(arr)
    return impl


@numba.generated_jit(nopython=True)
def contains(arr, pattern):
    args = [arr, pattern]
    for vmxp__ektdx in range(2):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.contains',
                ['arr', 'contains'], vmxp__ektdx)

    def impl(arr, pattern):
        return contains_util(arr, pattern)
    return impl


@numba.generated_jit(nopython=True)
def contains_util(arr, pattern):
    verify_string_binary_arg(arr, 'CONTAINS', 'arr')
    verify_string_binary_arg(pattern, 'CONTAINS', 'pattern')
    uex__xigg = bodo.boolean_array
    dplzz__pme = ['arr', 'pattern']
    nnu__wrnk = [arr, pattern]
    uhejw__gmgye = [True] * 2
    umgbb__yct = 'res[i] = arg1 in arg0\n'
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg)


@numba.generated_jit(nopython=True)
def editdistance_no_max(s, t):
    args = [s, t]
    for vmxp__ektdx in range(2):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument(
                'bodo.libs.bodosql_array_kernels.editdistance_no_max', ['s',
                't'], vmxp__ektdx)

    def impl(s, t):
        return editdistance_no_max_util(s, t)
    return impl


@numba.generated_jit(nopython=True)
def editdistance_with_max(s, t, maxDistance):
    args = [s, t, maxDistance]
    for vmxp__ektdx in range(3):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument(
                'bodo.libs.bodosql_array_kernels.editdistance_with_max', [
                's', 't', 'maxDistance'], vmxp__ektdx)

    def impl(s, t, maxDistance):
        return editdistance_with_max_util(s, t, maxDistance)
    return impl


@numba.generated_jit(nopython=True)
def endswith(source, suffix):
    args = [source, suffix]
    for vmxp__ektdx in range(2):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.endswith',
                ['source', 'suffix'], vmxp__ektdx)

    def impl(source, suffix):
        return endswith_util(source, suffix)
    return impl


@numba.generated_jit(nopython=True)
def format(arr, places):
    args = [arr, places]
    for vmxp__ektdx in range(2):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.format',
                ['arr', 'places'], vmxp__ektdx)

    def impl(arr, places):
        return format_util(arr, places)
    return impl


@numba.generated_jit(nopython=True)
def initcap(arr, delim):
    args = [arr, delim]
    for vmxp__ektdx in range(2):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.initcap',
                ['arr', 'delim'], vmxp__ektdx)

    def impl(arr, delim):
        return initcap_util(arr, delim)
    return impl


@numba.generated_jit(nopython=True)
def insert(source, pos, length, inject):
    args = [source, pos, length, inject]
    for vmxp__ektdx in range(4):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.insert',
                ['source', 'pos', 'length', 'inject'], vmxp__ektdx)

    def impl(source, pos, length, inject):
        return insert_util(source, pos, length, inject)
    return impl


@numba.generated_jit(nopython=True)
def instr(arr, target):
    args = [arr, target]
    for vmxp__ektdx in range(2):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.instr',
                ['arr', 'target'], vmxp__ektdx)

    def impl(arr, target):
        return instr_util(arr, target)
    return impl


def left(arr, n_chars):
    return


@overload(left)
def overload_left(arr, n_chars):
    args = [arr, n_chars]
    for vmxp__ektdx in range(2):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.left', [
                'arr', 'n_chars'], vmxp__ektdx)

    def impl(arr, n_chars):
        return left_util(arr, n_chars)
    return impl


def lpad(arr, length, padstr):
    return


@overload(lpad)
def overload_lpad(arr, length, padstr):
    args = [arr, length, padstr]
    for vmxp__ektdx in range(3):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.lpad', [
                'arr', 'length', 'padstr'], vmxp__ektdx)

    def impl(arr, length, padstr):
        return lpad_util(arr, length, padstr)
    return impl


@numba.generated_jit(nopython=True)
def ord_ascii(arr):
    if isinstance(arr, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.ord_ascii_util',
            ['arr'], 0)

    def impl(arr):
        return ord_ascii_util(arr)
    return impl


@numba.generated_jit(nopython=True)
def position(substr, source, start):
    args = [substr, source, start]
    for vmxp__ektdx in range(3):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.position',
                ['substr', 'source', 'start'], vmxp__ektdx)

    def impl(substr, source, start):
        return position_util(substr, source, start)
    return impl


@numba.generated_jit(nopython=True)
def repeat(arr, repeats):
    args = [arr, repeats]
    for vmxp__ektdx in range(2):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.repeat',
                ['arr', 'repeats'], vmxp__ektdx)

    def impl(arr, repeats):
        return repeat_util(arr, repeats)
    return impl


@numba.generated_jit(nopython=True)
def replace(arr, to_replace, replace_with):
    args = [arr, to_replace, replace_with]
    for vmxp__ektdx in range(3):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.replace',
                ['arr', 'to_replace', 'replace_with'], vmxp__ektdx)

    def impl(arr, to_replace, replace_with):
        return replace_util(arr, to_replace, replace_with)
    return impl


@numba.generated_jit(nopython=True)
def reverse(arr):
    if isinstance(arr, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.reverse_util',
            ['arr'], 0)

    def impl(arr):
        return reverse_util(arr)
    return impl


def right(arr, n_chars):
    return


@overload(right)
def overload_right(arr, n_chars):
    args = [arr, n_chars]
    for vmxp__ektdx in range(2):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.right',
                ['arr', 'n_chars'], vmxp__ektdx)

    def impl(arr, n_chars):
        return right_util(arr, n_chars)
    return impl


def rpad(arr, length, padstr):
    return


@overload(rpad)
def overload_rpad(arr, length, padstr):
    args = [arr, length, padstr]
    for vmxp__ektdx in range(3):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.rpad', [
                'arr', 'length', 'padstr'], vmxp__ektdx)

    def impl(arr, length, padstr):
        return rpad_util(arr, length, padstr)
    return impl


@numba.generated_jit(nopython=True)
def rtrimmed_length(arr):
    if isinstance(arr, types.optional):
        return unopt_argument(
            'bodo.libs.bodosql_array_kernels.rtrimmed_length_util', ['arr'], 0)

    def impl(arr):
        return rtrimmed_length_util(arr)
    return impl


@numba.generated_jit(nopython=True)
def space(n_chars):
    if isinstance(n_chars, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.space_util',
            ['n_chars'], 0)

    def impl(n_chars):
        return space_util(n_chars)
    return impl


@numba.generated_jit(nopython=True)
def split_part(source, delim, part):
    args = [source, delim, part]
    for vmxp__ektdx in range(3):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.split_part',
                ['source', 'delim', 'part'], vmxp__ektdx)

    def impl(source, delim, part):
        return split_part_util(source, delim, part)
    return impl


@numba.generated_jit(nopython=True)
def startswith(source, prefix):
    args = [source, prefix]
    for vmxp__ektdx in range(2):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.startswith',
                ['source', 'prefix'], vmxp__ektdx)

    def impl(source, prefix):
        return startswith_util(source, prefix)
    return impl


@numba.generated_jit(nopython=True)
def strcmp(arr0, arr1):
    args = [arr0, arr1]
    for vmxp__ektdx in range(2):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.strcmp',
                ['arr0', 'arr1'], vmxp__ektdx)

    def impl(arr0, arr1):
        return strcmp_util(arr0, arr1)
    return impl


@numba.generated_jit(nopython=True)
def strtok(source, delim, part):
    args = [source, delim, part]
    for vmxp__ektdx in range(3):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.strtok',
                ['source', 'delim', 'part'], vmxp__ektdx)

    def impl(source, delim, part):
        return strtok_util(source, delim, part)
    return impl


@numba.generated_jit(nopython=True)
def substring(arr, start, length):
    args = [arr, start, length]
    for vmxp__ektdx in range(3):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.substring',
                ['arr', 'start', 'length'], vmxp__ektdx)

    def impl(arr, start, length):
        return substring_util(arr, start, length)
    return impl


@numba.generated_jit(nopython=True)
def substring_index(arr, delimiter, occurrences):
    args = [arr, delimiter, occurrences]
    for vmxp__ektdx in range(3):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument(
                'bodo.libs.bodosql_array_kernels.substring_index', ['arr',
                'delimiter', 'occurrences'], vmxp__ektdx)

    def impl(arr, delimiter, occurrences):
        return substring_index_util(arr, delimiter, occurrences)
    return impl


@numba.generated_jit(nopython=True)
def translate(arr, source, target):
    args = [arr, source, target]
    for vmxp__ektdx in range(3):
        if isinstance(args[vmxp__ektdx], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.translate',
                ['arr', 'source', 'target'], vmxp__ektdx)

    def impl(arr, source, target):
        return translate_util(arr, source, target)
    return impl


@numba.generated_jit(nopython=True)
def char_util(arr):
    verify_int_arg(arr, 'CHAR', 'arr')
    dplzz__pme = ['arr']
    nnu__wrnk = [arr]
    uhejw__gmgye = [True]
    umgbb__yct = 'if 0 <= arg0 <= 127:\n'
    umgbb__yct += '   res[i] = chr(arg0)\n'
    umgbb__yct += 'else:\n'
    umgbb__yct += '   bodo.libs.array_kernels.setna(res, i)\n'
    uex__xigg = bodo.string_array_type
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg)


@numba.generated_jit(nopython=True)
def initcap_util(arr, delim):
    verify_string_arg(arr, 'INITCAP', 'arr')
    verify_string_arg(delim, 'INITCAP', 'delim')
    dplzz__pme = ['arr', 'delim']
    nnu__wrnk = [arr, delim]
    uhejw__gmgye = [True] * 2
    umgbb__yct = 'capitalized = arg0[:1].upper()\n'
    umgbb__yct += 'for j in range(1, len(arg0)):\n'
    umgbb__yct += '   if arg0[j-1] in arg1:\n'
    umgbb__yct += '      capitalized += arg0[j].upper()\n'
    umgbb__yct += '   else:\n'
    umgbb__yct += '      capitalized += arg0[j].lower()\n'
    umgbb__yct += 'res[i] = capitalized'
    uex__xigg = bodo.string_array_type
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg, may_cause_duplicate_dict_array_values=True)


@numba.generated_jit(nopython=True)
def instr_util(arr, target):
    verify_string_arg(arr, 'instr', 'arr')
    verify_string_arg(target, 'instr', 'target')
    dplzz__pme = ['arr', 'target']
    nnu__wrnk = [arr, target]
    uhejw__gmgye = [True] * 2
    umgbb__yct = 'res[i] = arg0.find(arg1) + 1'
    uex__xigg = bodo.libs.int_arr_ext.IntegerArrayType(types.int32)
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg)


@register_jitable
def min_edit_distance(s, t):
    if len(s) > len(t):
        s, t = t, s
    rbea__wmns, goyqp__dvtq = len(s), len(t)
    peqc__rxc, vbyq__sxwx = 1, 0
    arr = np.zeros((2, rbea__wmns + 1), dtype=np.uint32)
    arr[0, :] = np.arange(rbea__wmns + 1)
    for vmxp__ektdx in range(1, goyqp__dvtq + 1):
        arr[peqc__rxc, 0] = vmxp__ektdx
        for fhib__xyyue in range(1, rbea__wmns + 1):
            if s[fhib__xyyue - 1] == t[vmxp__ektdx - 1]:
                arr[peqc__rxc, fhib__xyyue] = arr[vbyq__sxwx, fhib__xyyue - 1]
            else:
                arr[peqc__rxc, fhib__xyyue] = 1 + min(arr[peqc__rxc, 
                    fhib__xyyue - 1], arr[vbyq__sxwx, fhib__xyyue], arr[
                    vbyq__sxwx, fhib__xyyue - 1])
        peqc__rxc, vbyq__sxwx = vbyq__sxwx, peqc__rxc
    return arr[goyqp__dvtq % 2, rbea__wmns]


@register_jitable
def min_edit_distance_with_max(s, t, maxDistance):
    if maxDistance < 0:
        return 0
    if len(s) > len(t):
        s, t = t, s
    rbea__wmns, goyqp__dvtq = len(s), len(t)
    if rbea__wmns <= maxDistance and goyqp__dvtq <= maxDistance:
        return min_edit_distance(s, t)
    peqc__rxc, vbyq__sxwx = 1, 0
    arr = np.zeros((2, rbea__wmns + 1), dtype=np.uint32)
    arr[0, :] = np.arange(rbea__wmns + 1)
    for vmxp__ektdx in range(1, goyqp__dvtq + 1):
        arr[peqc__rxc, 0] = vmxp__ektdx
        for fhib__xyyue in range(1, rbea__wmns + 1):
            if s[fhib__xyyue - 1] == t[vmxp__ektdx - 1]:
                arr[peqc__rxc, fhib__xyyue] = arr[vbyq__sxwx, fhib__xyyue - 1]
            else:
                arr[peqc__rxc, fhib__xyyue] = 1 + min(arr[peqc__rxc, 
                    fhib__xyyue - 1], arr[vbyq__sxwx, fhib__xyyue], arr[
                    vbyq__sxwx, fhib__xyyue - 1])
        if (arr[peqc__rxc] >= maxDistance).all():
            return maxDistance
        peqc__rxc, vbyq__sxwx = vbyq__sxwx, peqc__rxc
    return min(arr[goyqp__dvtq % 2, rbea__wmns], maxDistance)


@numba.generated_jit(nopython=True)
def editdistance_no_max_util(s, t):
    verify_string_arg(s, 'editdistance_no_max', 's')
    verify_string_arg(t, 'editdistance_no_max', 't')
    dplzz__pme = ['s', 't']
    nnu__wrnk = [s, t]
    uhejw__gmgye = [True] * 2
    umgbb__yct = (
        'res[i] = bodo.libs.bodosql_array_kernels.min_edit_distance(arg0, arg1)'
        )
    uex__xigg = bodo.libs.int_arr_ext.IntegerArrayType(types.int32)
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg)


@numba.generated_jit(nopython=True)
def editdistance_with_max_util(s, t, maxDistance):
    verify_string_arg(s, 'editdistance_no_max', 's')
    verify_string_arg(t, 'editdistance_no_max', 't')
    verify_int_arg(maxDistance, 'editdistance_no_max', 't')
    dplzz__pme = ['s', 't', 'maxDistance']
    nnu__wrnk = [s, t, maxDistance]
    uhejw__gmgye = [True] * 3
    umgbb__yct = (
        'res[i] = bodo.libs.bodosql_array_kernels.min_edit_distance_with_max(arg0, arg1, arg2)'
        )
    uex__xigg = bodo.libs.int_arr_ext.IntegerArrayType(types.int32)
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg)


@numba.generated_jit(nopython=True)
def endswith_util(source, suffix):
    hiku__uahz = verify_string_binary_arg(source, 'endswith', 'source')
    if hiku__uahz != verify_string_binary_arg(suffix, 'endswith', 'suffix'):
        raise bodo.utils.typing.BodoError(
            'String and suffix must both be strings or both binary')
    dplzz__pme = ['source', 'suffix']
    nnu__wrnk = [source, suffix]
    uhejw__gmgye = [True] * 2
    umgbb__yct = 'res[i] = arg0.endswith(arg1)'
    uex__xigg = bodo.boolean_array
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg)


@numba.generated_jit(nopython=True)
def format_util(arr, places):
    verify_int_float_arg(arr, 'FORMAT', 'arr')
    verify_int_arg(places, 'FORMAT', 'places')
    dplzz__pme = ['arr', 'places']
    nnu__wrnk = [arr, places]
    uhejw__gmgye = [True] * 2
    umgbb__yct = 'prec = max(arg1, 0)\n'
    umgbb__yct += "res[i] = format(arg0, f',.{prec}f')"
    uex__xigg = bodo.string_array_type
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg)


@numba.generated_jit(nopython=True)
def insert_util(arr, pos, length, inject):
    hiku__uahz = verify_string_binary_arg(arr, 'INSERT', 'arr')
    verify_int_arg(pos, 'INSERT', 'pos')
    verify_int_arg(length, 'INSERT', 'length')
    if hiku__uahz != verify_string_binary_arg(inject, 'INSERT', 'inject'):
        raise bodo.utils.typing.BodoError(
            'String and injected value must both be strings or both binary')
    dplzz__pme = ['arr', 'pos', 'length', 'inject']
    nnu__wrnk = [arr, pos, length, inject]
    uhejw__gmgye = [True] * 4
    umgbb__yct = 'prefixIndex = max(arg1-1, 0)\n'
    umgbb__yct += 'suffixIndex = prefixIndex + max(arg2, 0)\n'
    umgbb__yct += 'res[i] = arg0[:prefixIndex] + arg3 + arg0[suffixIndex:]'
    uex__xigg = (bodo.string_array_type if hiku__uahz else bodo.
        binary_array_type)
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg, may_cause_duplicate_dict_array_values=True)


def left_util(arr, n_chars):
    return


def right_util(arr, n_chars):
    return


def create_left_right_util_overload(func_name):

    def overload_left_right_util(arr, n_chars):
        hiku__uahz = verify_string_binary_arg(arr, func_name, 'arr')
        verify_int_arg(n_chars, func_name, 'n_chars')
        womxf__auig = "''" if hiku__uahz else "b''"
        dplzz__pme = ['arr', 'n_chars']
        nnu__wrnk = [arr, n_chars]
        uhejw__gmgye = [True] * 2
        umgbb__yct = 'if arg1 <= 0:\n'
        umgbb__yct += f'   res[i] = {womxf__auig}\n'
        umgbb__yct += 'else:\n'
        if func_name == 'LEFT':
            umgbb__yct += '   res[i] = arg0[:arg1]\n'
        elif func_name == 'RIGHT':
            umgbb__yct += '   res[i] = arg0[-arg1:]\n'
        uex__xigg = (bodo.string_array_type if hiku__uahz else bodo.
            binary_array_type)
        return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye,
            umgbb__yct, uex__xigg, may_cause_duplicate_dict_array_values=True)
    return overload_left_right_util


def _install_left_right_overload():
    for rnsrj__dfg, func_name in zip((left_util, right_util), ('LEFT', 'RIGHT')
        ):
        xuvgx__qkwo = create_left_right_util_overload(func_name)
        overload(rnsrj__dfg)(xuvgx__qkwo)


_install_left_right_overload()


def lpad_util(arr, length, padstr):
    return


def rpad_util(arr, length, padstr):
    return


def create_lpad_rpad_util_overload(func_name):

    def overload_lpad_rpad_util(arr, length, pad_string):
        itrif__nzax = verify_string_binary_arg(pad_string, func_name,
            'pad_string')
        hiku__uahz = verify_string_binary_arg(arr, func_name, 'arr')
        if hiku__uahz != itrif__nzax:
            raise bodo.utils.typing.BodoError(
                'Pad string and arr must be the same type!')
        uex__xigg = (bodo.string_array_type if hiku__uahz else bodo.
            binary_array_type)
        verify_int_arg(length, func_name, 'length')
        verify_string_binary_arg(pad_string, func_name,
            f'{func_name.lower()}_string')
        if func_name == 'LPAD':
            may__lzjjh = f'(arg2 * quotient) + arg2[:remainder] + arg0'
        elif func_name == 'RPAD':
            may__lzjjh = f'arg0 + (arg2 * quotient) + arg2[:remainder]'
        dplzz__pme = ['arr', 'length', 'pad_string']
        nnu__wrnk = [arr, length, pad_string]
        uhejw__gmgye = [True] * 3
        womxf__auig = "''" if hiku__uahz else "b''"
        umgbb__yct = f"""                if arg1 <= 0:
                    res[i] = {womxf__auig}
                elif len(arg2) == 0:
                    res[i] = arg0
                elif len(arg0) >= arg1:
                    res[i] = arg0[:arg1]
                else:
                    quotient = (arg1 - len(arg0)) // len(arg2)
                    remainder = (arg1 - len(arg0)) % len(arg2)
                    res[i] = {may__lzjjh}"""
        return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye,
            umgbb__yct, uex__xigg, may_cause_duplicate_dict_array_values=True)
    return overload_lpad_rpad_util


def _install_lpad_rpad_overload():
    for rnsrj__dfg, func_name in zip((lpad_util, rpad_util), ('LPAD', 'RPAD')):
        xuvgx__qkwo = create_lpad_rpad_util_overload(func_name)
        overload(rnsrj__dfg)(xuvgx__qkwo)


_install_lpad_rpad_overload()


@numba.generated_jit(nopython=True)
def ord_ascii_util(arr):
    verify_string_arg(arr, 'ORD', 'arr')
    dplzz__pme = ['arr']
    nnu__wrnk = [arr]
    uhejw__gmgye = [True]
    umgbb__yct = 'if len(arg0) == 0:\n'
    umgbb__yct += '   bodo.libs.array_kernels.setna(res, i)\n'
    umgbb__yct += 'else:\n'
    umgbb__yct += '   res[i] = ord(arg0[0])'
    uex__xigg = bodo.libs.int_arr_ext.IntegerArrayType(types.int32)
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg)


@numba.generated_jit(nopython=True)
def position_util(substr, source, start):
    jofte__pumd = verify_string_binary_arg(substr, 'POSITION', 'substr')
    if jofte__pumd != verify_string_binary_arg(source, 'POSITION', 'source'):
        raise bodo.utils.typing.BodoError(
            'Substring and source must be both strings or both binary')
    verify_int_arg(start, 'POSITION', 'start')
    assert jofte__pumd, '[BE-3717] Support binary find with 3 args'
    dplzz__pme = ['substr', 'source', 'start']
    nnu__wrnk = [substr, source, start]
    uhejw__gmgye = [True] * 3
    umgbb__yct = 'res[i] = arg1.find(arg0, arg2 - 1) + 1'
    uex__xigg = bodo.libs.int_arr_ext.IntegerArrayType(types.int32)
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg)


@numba.generated_jit(nopython=True)
def repeat_util(arr, repeats):
    verify_string_arg(arr, 'REPEAT', 'arr')
    verify_int_arg(repeats, 'REPEAT', 'repeats')
    dplzz__pme = ['arr', 'repeats']
    nnu__wrnk = [arr, repeats]
    uhejw__gmgye = [True] * 2
    umgbb__yct = 'if arg1 <= 0:\n'
    umgbb__yct += "   res[i] = ''\n"
    umgbb__yct += 'else:\n'
    umgbb__yct += '   res[i] = arg0 * arg1'
    uex__xigg = bodo.string_array_type
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg, may_cause_duplicate_dict_array_values=True)


@numba.generated_jit(nopython=True)
def replace_util(arr, to_replace, replace_with):
    verify_string_arg(arr, 'REPLACE', 'arr')
    verify_string_arg(to_replace, 'REPLACE', 'to_replace')
    verify_string_arg(replace_with, 'REPLACE', 'replace_with')
    dplzz__pme = ['arr', 'to_replace', 'replace_with']
    nnu__wrnk = [arr, to_replace, replace_with]
    uhejw__gmgye = [True] * 3
    umgbb__yct = "if arg1 == '':\n"
    umgbb__yct += '   res[i] = arg0\n'
    umgbb__yct += 'else:\n'
    umgbb__yct += '   res[i] = arg0.replace(arg1, arg2)'
    uex__xigg = bodo.string_array_type
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg, may_cause_duplicate_dict_array_values=True)


@numba.generated_jit(nopython=True)
def reverse_util(arr):
    hiku__uahz = verify_string_binary_arg(arr, 'REVERSE', 'arr')
    dplzz__pme = ['arr']
    nnu__wrnk = [arr]
    uhejw__gmgye = [True]
    umgbb__yct = 'res[i] = arg0[::-1]'
    uex__xigg = bodo.string_array_type
    uex__xigg = (bodo.string_array_type if hiku__uahz else bodo.
        binary_array_type)
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg)


@numba.generated_jit(nopython=True)
def rtrimmed_length_util(arr):
    verify_string_arg(arr, 'RTRIMMED_LENGTH', 'arr')
    dplzz__pme = ['arr']
    nnu__wrnk = [arr]
    uhejw__gmgye = [True]
    umgbb__yct = "res[i] = len(arg0.rstrip(' '))"
    uex__xigg = bodo.libs.int_arr_ext.IntegerArrayType(types.int32)
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg)


@numba.generated_jit(nopython=True)
def space_util(n_chars):
    verify_int_arg(n_chars, 'SPACE', 'n_chars')
    dplzz__pme = ['n_chars']
    nnu__wrnk = [n_chars]
    uhejw__gmgye = [True]
    umgbb__yct = 'if arg0 <= 0:\n'
    umgbb__yct += "   res[i] = ''\n"
    umgbb__yct += 'else:\n'
    umgbb__yct += "   res[i] = ' ' * arg0"
    uex__xigg = bodo.string_array_type
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg)


@numba.generated_jit(nopython=True)
def split_part_util(source, delim, part):
    verify_string_arg(source, 'SPLIT_PART', 'source')
    verify_string_arg(delim, 'SPLIT_PART', 'delim')
    verify_int_arg(part, 'SPLIT_PART', 'part')
    dplzz__pme = ['source', 'delim', 'part']
    nnu__wrnk = [source, delim, part]
    uhejw__gmgye = [True] * 3
    umgbb__yct = "tokens = arg0.split(arg1) if arg1 != '' else [arg0]\n"
    umgbb__yct += 'if abs(arg2) > len(tokens):\n'
    umgbb__yct += "    res[i] = ''\n"
    umgbb__yct += 'else:\n'
    umgbb__yct += '    res[i] = tokens[arg2 if arg2 <= 0 else arg2-1]\n'
    uex__xigg = bodo.string_array_type
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg, may_cause_duplicate_dict_array_values=True)


@numba.generated_jit(nopython=True)
def startswith_util(source, prefix):
    hiku__uahz = verify_string_binary_arg(source, 'startswith', 'source')
    if hiku__uahz != verify_string_binary_arg(prefix, 'startswith', 'prefix'):
        raise bodo.utils.typing.BodoError(
            'String and prefix must both be strings or both binary')
    dplzz__pme = ['source', 'prefix']
    nnu__wrnk = [source, prefix]
    uhejw__gmgye = [True] * 2
    umgbb__yct = 'res[i] = arg0.startswith(arg1)'
    uex__xigg = bodo.boolean_array
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg)


@numba.generated_jit(nopython=True)
def strcmp_util(arr0, arr1):
    verify_string_arg(arr0, 'strcmp', 'arr0')
    verify_string_arg(arr1, 'strcmp', 'arr1')
    dplzz__pme = ['arr0', 'arr1']
    nnu__wrnk = [arr0, arr1]
    uhejw__gmgye = [True] * 2
    umgbb__yct = 'if arg0 < arg1:\n'
    umgbb__yct += '   res[i] = -1\n'
    umgbb__yct += 'elif arg0 > arg1:\n'
    umgbb__yct += '   res[i] = 1\n'
    umgbb__yct += 'else:\n'
    umgbb__yct += '   res[i] = 0\n'
    uex__xigg = bodo.libs.int_arr_ext.IntegerArrayType(types.int32)
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg)


@numba.generated_jit(nopython=True)
def strtok_util(source, delim, part):
    verify_string_arg(source, 'STRTOK', 'source')
    verify_string_arg(delim, 'STRTOK', 'delim')
    verify_int_arg(part, 'STRTOK', 'part')
    dplzz__pme = ['source', 'delim', 'part']
    nnu__wrnk = [source, delim, part]
    uhejw__gmgye = [True] * 3
    umgbb__yct = "if (arg0 == '' and arg1 == '') or arg2 <= 0:\n"
    umgbb__yct += '   bodo.libs.array_kernels.setna(res, i)\n'
    umgbb__yct += 'else:\n'
    umgbb__yct += '   tokens = []\n'
    umgbb__yct += "   buffer = ''\n"
    umgbb__yct += '   for j in range(len(arg0)):\n'
    umgbb__yct += '      if arg0[j] in arg1:\n'
    umgbb__yct += "         if buffer != '':"
    umgbb__yct += '            tokens.append(buffer)\n'
    umgbb__yct += "         buffer = ''\n"
    umgbb__yct += '      else:\n'
    umgbb__yct += '         buffer += arg0[j]\n'
    umgbb__yct += "   if buffer != '':\n"
    umgbb__yct += '      tokens.append(buffer)\n'
    umgbb__yct += '   if arg2 > len(tokens):\n'
    umgbb__yct += '      bodo.libs.array_kernels.setna(res, i)\n'
    umgbb__yct += '   else:\n'
    umgbb__yct += '      res[i] = tokens[arg2-1]\n'
    uex__xigg = bodo.string_array_type
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg, may_cause_duplicate_dict_array_values=True)


@numba.generated_jit(nopython=True)
def substring_util(arr, start, length):
    hiku__uahz = verify_string_binary_arg(arr, 'SUBSTRING', 'arr')
    verify_int_arg(start, 'SUBSTRING', 'start')
    verify_int_arg(length, 'SUBSTRING', 'length')
    uex__xigg = (bodo.string_array_type if hiku__uahz else bodo.
        binary_array_type)
    dplzz__pme = ['arr', 'start', 'length']
    nnu__wrnk = [arr, start, length]
    uhejw__gmgye = [True] * 3
    umgbb__yct = 'if arg2 <= 0:\n'
    umgbb__yct += "   res[i] = ''\n" if hiku__uahz else "   res[i] = b''\n"
    umgbb__yct += 'elif arg1 < 0 and arg1 + arg2 >= 0:\n'
    umgbb__yct += '   res[i] = arg0[arg1:]\n'
    umgbb__yct += 'else:\n'
    umgbb__yct += '   if arg1 > 0: arg1 -= 1\n'
    umgbb__yct += '   res[i] = arg0[arg1:arg1+arg2]\n'
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg, may_cause_duplicate_dict_array_values=True)


@numba.generated_jit(nopython=True)
def substring_index_util(arr, delimiter, occurrences):
    verify_string_arg(arr, 'SUBSTRING_INDEX', 'arr')
    verify_string_arg(delimiter, 'SUBSTRING_INDEX', 'delimiter')
    verify_int_arg(occurrences, 'SUBSTRING_INDEX', 'occurrences')
    dplzz__pme = ['arr', 'delimiter', 'occurrences']
    nnu__wrnk = [arr, delimiter, occurrences]
    uhejw__gmgye = [True] * 3
    umgbb__yct = "if arg1 == '' or arg2 == 0:\n"
    umgbb__yct += "   res[i] = ''\n"
    umgbb__yct += 'elif arg2 >= 0:\n'
    umgbb__yct += '   res[i] = arg1.join(arg0.split(arg1, arg2+1)[:arg2])\n'
    umgbb__yct += 'else:\n'
    umgbb__yct += '   res[i] = arg1.join(arg0.split(arg1)[arg2:])\n'
    uex__xigg = bodo.string_array_type
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg, may_cause_duplicate_dict_array_values=True)


@numba.generated_jit(nopython=True)
def translate_util(arr, source, target):
    verify_string_arg(arr, 'translate', 'arr')
    verify_string_arg(source, 'translate', 'source')
    verify_string_arg(target, 'translate', 'target')
    dplzz__pme = ['arr', 'source', 'target']
    nnu__wrnk = [arr, source, target]
    uhejw__gmgye = [True] * 3
    umgbb__yct = "translated = ''\n"
    umgbb__yct += 'for char in arg0:\n'
    umgbb__yct += '   index = arg1.find(char)\n'
    umgbb__yct += '   if index == -1:\n'
    umgbb__yct += '      translated += char\n'
    umgbb__yct += '   elif index < len(arg2):\n'
    umgbb__yct += '      translated += arg2[index]\n'
    umgbb__yct += 'res[i] = translated'
    uex__xigg = bodo.string_array_type
    return gen_vectorized(dplzz__pme, nnu__wrnk, uhejw__gmgye, umgbb__yct,
        uex__xigg, may_cause_duplicate_dict_array_values=True)
