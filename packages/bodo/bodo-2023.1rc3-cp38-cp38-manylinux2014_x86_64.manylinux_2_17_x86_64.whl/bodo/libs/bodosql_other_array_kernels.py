"""
Implements miscellaneous array kernels that are specific to BodoSQL
"""
import numba
from numba.core import types
import bodo
from bodo.libs.bodosql_array_kernel_utils import *
from bodo.utils.typing import raise_bodo_error


@numba.generated_jit(nopython=True)
def booland(A, B):
    args = [A, B]
    for stmu__yzl in range(2):
        if isinstance(args[stmu__yzl], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.booland',
                ['A', 'B'], stmu__yzl)

    def impl(A, B):
        return booland_util(A, B)
    return impl


@numba.generated_jit(nopython=True)
def boolor(A, B):
    args = [A, B]
    for stmu__yzl in range(2):
        if isinstance(args[stmu__yzl], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.boolor',
                ['A', 'B'], stmu__yzl)

    def impl(A, B):
        return boolor_util(A, B)
    return impl


@numba.generated_jit(nopython=True)
def boolxor(A, B):
    args = [A, B]
    for stmu__yzl in range(2):
        if isinstance(args[stmu__yzl], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.boolxor',
                ['A', 'B'], stmu__yzl)

    def impl(A, B):
        return boolxor_util(A, B)
    return impl


@numba.generated_jit(nopython=True)
def boolnot(A):
    if isinstance(A, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.boolnot_util',
            ['A'], 0)

    def impl(A):
        return boolnot_util(A)
    return impl


@numba.generated_jit(nopython=True)
def cond(arr, ifbranch, elsebranch):
    args = [arr, ifbranch, elsebranch]
    for stmu__yzl in range(3):
        if isinstance(args[stmu__yzl], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.cond', [
                'arr', 'ifbranch', 'elsebranch'], stmu__yzl)

    def impl(arr, ifbranch, elsebranch):
        return cond_util(arr, ifbranch, elsebranch)
    return impl


@numba.generated_jit(nopython=True)
def equal_null(A, B):
    args = [A, B]
    for stmu__yzl in range(2):
        if isinstance(args[stmu__yzl], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.equal_null',
                ['A', 'B'], stmu__yzl)

    def impl(A, B):
        return equal_null_util(A, B)
    return impl


@numba.generated_jit(nopython=True)
def booland_util(A, B):
    verify_int_float_arg(A, 'BOOLAND', 'A')
    verify_int_float_arg(B, 'BOOLAND', 'B')
    jgnfl__uyd = ['A', 'B']
    gdkio__wnnp = [A, B]
    wak__xyxr = [False] * 2
    if A == bodo.none:
        wak__xyxr = [False, True]
        zdkj__vicfu = 'if arg1 != 0:\n'
        zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)\n'
        zdkj__vicfu += 'else:\n'
        zdkj__vicfu += '   res[i] = False\n'
    elif B == bodo.none:
        wak__xyxr = [True, False]
        zdkj__vicfu = 'if arg0 != 0:\n'
        zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)\n'
        zdkj__vicfu += 'else:\n'
        zdkj__vicfu += '   res[i] = False\n'
    elif bodo.utils.utils.is_array_typ(A, True):
        if bodo.utils.utils.is_array_typ(B, True):
            zdkj__vicfu = """if bodo.libs.array_kernels.isna(A, i) and bodo.libs.array_kernels.isna(B, i):
"""
            zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)\n'
            zdkj__vicfu += (
                'elif bodo.libs.array_kernels.isna(A, i) and arg1 != 0:\n')
            zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)\n'
            zdkj__vicfu += (
                'elif bodo.libs.array_kernels.isna(B, i) and arg0 != 0:\n')
            zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)\n'
            zdkj__vicfu += 'else:\n'
            zdkj__vicfu += '   res[i] = (arg0 != 0) and (arg1 != 0)'
        else:
            zdkj__vicfu = (
                'if bodo.libs.array_kernels.isna(A, i) and arg1 != 0:\n')
            zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)\n'
            zdkj__vicfu += 'else:\n'
            zdkj__vicfu += '   res[i] = (arg0 != 0) and (arg1 != 0)'
    elif bodo.utils.utils.is_array_typ(B, True):
        zdkj__vicfu = 'if bodo.libs.array_kernels.isna(B, i) and arg0 != 0:\n'
        zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)\n'
        zdkj__vicfu += 'else:\n'
        zdkj__vicfu += '   res[i] = (arg0 != 0) and (arg1 != 0)'
    else:
        zdkj__vicfu = 'res[i] = (arg0 != 0) and (arg1 != 0)'
    exis__bpzj = bodo.libs.bool_arr_ext.boolean_array
    return gen_vectorized(jgnfl__uyd, gdkio__wnnp, wak__xyxr, zdkj__vicfu,
        exis__bpzj)


@numba.generated_jit(nopython=True)
def boolor_util(A, B):
    verify_int_float_arg(A, 'BOOLOR', 'A')
    verify_int_float_arg(B, 'BOOLOR', 'B')
    jgnfl__uyd = ['A', 'B']
    gdkio__wnnp = [A, B]
    wak__xyxr = [False] * 2
    if A == bodo.none:
        wak__xyxr = [False, True]
        zdkj__vicfu = 'if arg1 == 0:\n'
        zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)\n'
        zdkj__vicfu += 'else:\n'
        zdkj__vicfu += '   res[i] = True\n'
    elif B == bodo.none:
        wak__xyxr = [True, False]
        zdkj__vicfu = 'if arg0 == 0:\n'
        zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)\n'
        zdkj__vicfu += 'else:\n'
        zdkj__vicfu += '   res[i] = True\n'
    elif bodo.utils.utils.is_array_typ(A, True):
        if bodo.utils.utils.is_array_typ(B, True):
            zdkj__vicfu = """if bodo.libs.array_kernels.isna(A, i) and bodo.libs.array_kernels.isna(B, i):
"""
            zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)\n'
            zdkj__vicfu += (
                'elif bodo.libs.array_kernels.isna(A, i) and arg1 != 0:\n')
            zdkj__vicfu += '   res[i] = True\n'
            zdkj__vicfu += (
                'elif bodo.libs.array_kernels.isna(A, i) and arg1 == 0:\n')
            zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)\n'
            zdkj__vicfu += (
                'elif bodo.libs.array_kernels.isna(B, i) and arg0 != 0:\n')
            zdkj__vicfu += '   res[i] = True\n'
            zdkj__vicfu += (
                'elif bodo.libs.array_kernels.isna(B, i) and arg0 == 0:\n')
            zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)\n'
            zdkj__vicfu += 'else:\n'
            zdkj__vicfu += '   res[i] = (arg0 != 0) or (arg1 != 0)'
        else:
            zdkj__vicfu = (
                'if bodo.libs.array_kernels.isna(A, i) and arg1 != 0:\n')
            zdkj__vicfu += '   res[i] = True\n'
            zdkj__vicfu += (
                'elif bodo.libs.array_kernels.isna(A, i) and arg1 == 0:\n')
            zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)\n'
            zdkj__vicfu += 'else:\n'
            zdkj__vicfu += '   res[i] = (arg0 != 0) or (arg1 != 0)'
    elif bodo.utils.utils.is_array_typ(B, True):
        zdkj__vicfu = 'if bodo.libs.array_kernels.isna(B, i) and arg0 != 0:\n'
        zdkj__vicfu += '   res[i] = True\n'
        zdkj__vicfu += (
            'elif bodo.libs.array_kernels.isna(B, i) and arg0 == 0:\n')
        zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)\n'
        zdkj__vicfu += 'else:\n'
        zdkj__vicfu += '   res[i] = (arg0 != 0) or (arg1 != 0)'
    else:
        zdkj__vicfu = 'res[i] = (arg0 != 0) or (arg1 != 0)'
    exis__bpzj = bodo.libs.bool_arr_ext.boolean_array
    return gen_vectorized(jgnfl__uyd, gdkio__wnnp, wak__xyxr, zdkj__vicfu,
        exis__bpzj)


@numba.generated_jit(nopython=True)
def boolxor_util(A, B):
    verify_int_float_arg(A, 'BOOLXOR', 'A')
    verify_int_float_arg(B, 'BOOLXOR', 'B')
    jgnfl__uyd = ['A', 'B']
    gdkio__wnnp = [A, B]
    wak__xyxr = [True] * 2
    zdkj__vicfu = 'res[i] = (arg0 == 0) != (arg1 == 0)'
    exis__bpzj = bodo.libs.bool_arr_ext.boolean_array
    return gen_vectorized(jgnfl__uyd, gdkio__wnnp, wak__xyxr, zdkj__vicfu,
        exis__bpzj)


@numba.generated_jit(nopython=True)
def boolnot_util(A):
    verify_int_float_arg(A, 'BOOLNOT', 'A')
    jgnfl__uyd = ['A']
    gdkio__wnnp = [A]
    wak__xyxr = [True]
    zdkj__vicfu = 'res[i] = arg0 == 0'
    exis__bpzj = bodo.libs.bool_arr_ext.boolean_array
    return gen_vectorized(jgnfl__uyd, gdkio__wnnp, wak__xyxr, zdkj__vicfu,
        exis__bpzj)


@numba.generated_jit(nopython=True)
def nullif(arr0, arr1):
    args = [arr0, arr1]
    for stmu__yzl in range(2):
        if isinstance(args[stmu__yzl], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.nullif',
                ['arr0', 'arr1'], stmu__yzl)

    def impl(arr0, arr1):
        return nullif_util(arr0, arr1)
    return impl


@numba.generated_jit(nopython=True)
def regr_valx(y, x):
    args = [y, x]
    for stmu__yzl in range(2):
        if isinstance(args[stmu__yzl], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.regr_valx',
                ['y', 'x'], stmu__yzl)

    def impl(y, x):
        return regr_valx_util(y, x)
    return impl


@numba.generated_jit(nopython=True)
def regr_valy(y, x):
    args = [y, x]
    for stmu__yzl in range(2):
        if isinstance(args[stmu__yzl], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.regr_valy',
                ['y', 'x'], stmu__yzl)

    def impl(y, x):
        return regr_valx(x, y)
    return impl


@numba.generated_jit(nopython=True)
def cond_util(arr, ifbranch, elsebranch):
    verify_boolean_arg(arr, 'cond', 'arr')
    if bodo.utils.utils.is_array_typ(arr, True
        ) and ifbranch == bodo.none and elsebranch == bodo.none:
        raise_bodo_error('Both branches of IF() cannot be scalar NULL')
    jgnfl__uyd = ['arr', 'ifbranch', 'elsebranch']
    gdkio__wnnp = [arr, ifbranch, elsebranch]
    wak__xyxr = [False] * 3
    if bodo.utils.utils.is_array_typ(arr, True):
        zdkj__vicfu = (
            'if (not bodo.libs.array_kernels.isna(arr, i)) and arg0:\n')
    elif arr != bodo.none:
        zdkj__vicfu = 'if arg0:\n'
    else:
        zdkj__vicfu = ''
    if arr != bodo.none:
        if bodo.utils.utils.is_array_typ(ifbranch, True):
            zdkj__vicfu += '   if bodo.libs.array_kernels.isna(ifbranch, i):\n'
            zdkj__vicfu += '      bodo.libs.array_kernels.setna(res, i)\n'
            zdkj__vicfu += '   else:\n'
            zdkj__vicfu += '      res[i] = arg1\n'
        elif ifbranch == bodo.none:
            zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)\n'
        else:
            zdkj__vicfu += '   res[i] = arg1\n'
        zdkj__vicfu += 'else:\n'
    if bodo.utils.utils.is_array_typ(elsebranch, True):
        zdkj__vicfu += '   if bodo.libs.array_kernels.isna(elsebranch, i):\n'
        zdkj__vicfu += '      bodo.libs.array_kernels.setna(res, i)\n'
        zdkj__vicfu += '   else:\n'
        zdkj__vicfu += '      res[i] = arg2\n'
    elif elsebranch == bodo.none:
        zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)\n'
    else:
        zdkj__vicfu += '   res[i] = arg2\n'
    exis__bpzj = get_common_broadcasted_type([ifbranch, elsebranch], 'IF')
    return gen_vectorized(jgnfl__uyd, gdkio__wnnp, wak__xyxr, zdkj__vicfu,
        exis__bpzj)


@numba.generated_jit(nopython=True)
def equal_null_util(A, B):
    get_common_broadcasted_type([A, B], 'EQUAL_NULL')
    jgnfl__uyd = ['A', 'B']
    gdkio__wnnp = [A, B]
    wak__xyxr = [False] * 2
    if A == bodo.none:
        if B == bodo.none:
            zdkj__vicfu = 'res[i] = True'
        elif bodo.utils.utils.is_array_typ(B, True):
            zdkj__vicfu = 'res[i] = bodo.libs.array_kernels.isna(B, i)'
        else:
            zdkj__vicfu = 'res[i] = False'
    elif B == bodo.none:
        if bodo.utils.utils.is_array_typ(A, True):
            zdkj__vicfu = 'res[i] = bodo.libs.array_kernels.isna(A, i)'
        else:
            zdkj__vicfu = 'res[i] = False'
    elif bodo.utils.utils.is_array_typ(A, True):
        if bodo.utils.utils.is_array_typ(B, True):
            zdkj__vicfu = """if bodo.libs.array_kernels.isna(A, i) and bodo.libs.array_kernels.isna(B, i):
"""
            zdkj__vicfu += '   res[i] = True\n'
            zdkj__vicfu += """elif bodo.libs.array_kernels.isna(A, i) or bodo.libs.array_kernels.isna(B, i):
"""
            zdkj__vicfu += '   res[i] = False\n'
            zdkj__vicfu += 'else:\n'
            zdkj__vicfu += '   res[i] = arg0 == arg1'
        else:
            zdkj__vicfu = (
                'res[i] = (not bodo.libs.array_kernels.isna(A, i)) and arg0 == arg1'
                )
    elif bodo.utils.utils.is_array_typ(B, True):
        zdkj__vicfu = (
            'res[i] = (not bodo.libs.array_kernels.isna(B, i)) and arg0 == arg1'
            )
    else:
        zdkj__vicfu = 'res[i] = arg0 == arg1'
    exis__bpzj = bodo.libs.bool_arr_ext.boolean_array
    return gen_vectorized(jgnfl__uyd, gdkio__wnnp, wak__xyxr, zdkj__vicfu,
        exis__bpzj)


@numba.generated_jit(nopython=True)
def nullif_util(arr0, arr1):
    jgnfl__uyd = ['arr0', 'arr1']
    gdkio__wnnp = [arr0, arr1]
    wak__xyxr = [True, False]
    if arr1 == bodo.none:
        zdkj__vicfu = 'res[i] = arg0\n'
    elif bodo.utils.utils.is_array_typ(arr1, True):
        zdkj__vicfu = (
            'if bodo.libs.array_kernels.isna(arr1, i) or arg0 != arg1:\n')
        zdkj__vicfu += '   res[i] = arg0\n'
        zdkj__vicfu += 'else:\n'
        zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)'
    else:
        zdkj__vicfu = 'if arg0 != arg1:\n'
        zdkj__vicfu += '   res[i] = arg0\n'
        zdkj__vicfu += 'else:\n'
        zdkj__vicfu += '   bodo.libs.array_kernels.setna(res, i)'
    exis__bpzj = get_common_broadcasted_type([arr0, arr1], 'NULLIF')
    return gen_vectorized(jgnfl__uyd, gdkio__wnnp, wak__xyxr, zdkj__vicfu,
        exis__bpzj)


@numba.generated_jit(nopython=True)
def regr_valx_util(y, x):
    verify_int_float_arg(y, 'regr_valx', 'y')
    verify_int_float_arg(x, 'regr_valx', 'x')
    jgnfl__uyd = ['y', 'x']
    gdkio__wnnp = [y, x]
    nvx__nchw = [True] * 2
    zdkj__vicfu = 'res[i] = arg1'
    exis__bpzj = types.Array(bodo.float64, 1, 'C')
    return gen_vectorized(jgnfl__uyd, gdkio__wnnp, nvx__nchw, zdkj__vicfu,
        exis__bpzj)
