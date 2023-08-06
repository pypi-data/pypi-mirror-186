"""
Implements numerical array kernels that are specific to BodoSQL
"""
import numba
from numba.core import types
from numba.extending import overload
import bodo
from bodo.libs.bodosql_array_kernel_utils import *
from bodo.utils.utils import is_array_typ


def cbrt(arr):
    return


def ceil(arr):
    return


def factorial(arr):
    return


def floor(arr):
    return


def mod(arr0, arr1):
    return


def sign(arr):
    return


def sqrt(arr):
    return


def round(arr0, arr1):
    return


def trunc(arr0, arr1):
    return


def abs(arr):
    return


def ln(arr):
    return


def log2(arr):
    return


def log10(arr):
    return


def exp(arr):
    return


def power(arr0, arr1):
    return


def sqrt_util(arr):
    return


def square(arr):
    return


def cbrt_util(arr):
    return


def ceil_util(arr):
    return


def factorial_util(arr):
    return


def floor_util(arr):
    return


def mod_util(arr0, arr1):
    return


def sign_util(arr):
    return


def round_util(arr0, arr1):
    return


def trunc_util(arr0, arr1):
    return


def abs_util(arr):
    return


def ln_util(arr):
    return


def log2_util(arr):
    return


def log10_util(arr):
    return


def exp_util(arr):
    return


def power_util(arr0, arr1):
    return


def square_util(arr):
    return


funcs_utils_names = (abs, abs_util, 'ABS'), (cbrt, cbrt_util, 'CBRT'), (ceil,
    ceil_util, 'CEIL'), (factorial, factorial_util, 'FACTORIAL'), (floor,
    floor_util, 'FLOOR'), (ln, ln_util, 'LN'), (log2, log2_util, 'LOG2'), (
    log10, log10_util, 'LOG10'), (mod, mod_util, 'MOD'), (sign, sign_util,
    'SIGN'), (round, round_util, 'ROUND'), (trunc, trunc_util, 'TRUNC'), (exp,
    exp_util, 'EXP'), (power, power_util, 'POWER'), (sqrt, sqrt_util, 'SQRT'
    ), (square, square_util, 'SQUARE')
double_arg_funcs = 'MOD', 'TRUNC', 'POWER', 'ROUND'
single_arg_funcs = set(a[2] for a in funcs_utils_names if a[2] not in
    double_arg_funcs)
_float = {(16): types.float16, (32): types.float32, (64): types.float64}
_int = {(8): types.int8, (16): types.int16, (32): types.int32, (64): types.
    int64}
_uint = {(8): types.uint8, (16): types.uint16, (32): types.uint32, (64):
    types.uint64}


def _get_numeric_output_dtype(func_name, arr0, arr1=None):
    rnkpj__qqluy = arr0.dtype if is_array_typ(arr0) else arr0
    kran__ypt = arr1.dtype if is_array_typ(arr1) else arr1
    hxeu__bpesb = bodo.float64
    if (arr0 is None or rnkpj__qqluy == bodo.none
        ) or func_name in double_arg_funcs and (arr1 is None or kran__ypt ==
        bodo.none):
        return types.Array(hxeu__bpesb, 1, 'C')
    if isinstance(rnkpj__qqluy, types.Float):
        if isinstance(kran__ypt, types.Float):
            hxeu__bpesb = _float[max(rnkpj__qqluy.bitwidth, kran__ypt.bitwidth)
                ]
        else:
            hxeu__bpesb = rnkpj__qqluy
    if func_name == 'SIGN':
        if isinstance(rnkpj__qqluy, types.Integer):
            hxeu__bpesb = rnkpj__qqluy
    elif func_name == 'MOD':
        if isinstance(rnkpj__qqluy, types.Integer) and isinstance(kran__ypt,
            types.Integer):
            if rnkpj__qqluy.signed:
                if kran__ypt.signed:
                    hxeu__bpesb = kran__ypt
                else:
                    hxeu__bpesb = _int[min(64, kran__ypt.bitwidth * 2)]
            else:
                hxeu__bpesb = kran__ypt
    elif func_name == 'ABS':
        if isinstance(rnkpj__qqluy, types.Integer):
            if rnkpj__qqluy.signed:
                hxeu__bpesb = _uint[min(64, rnkpj__qqluy.bitwidth * 2)]
            else:
                hxeu__bpesb = rnkpj__qqluy
    elif func_name == 'ROUND':
        if isinstance(rnkpj__qqluy, (types.Float, types.Integer)):
            hxeu__bpesb = rnkpj__qqluy
    elif func_name == 'FACTORIAL':
        hxeu__bpesb = bodo.int64
    if isinstance(hxeu__bpesb, types.Integer):
        return bodo.libs.int_arr_ext.IntegerArrayType(hxeu__bpesb)
    else:
        return types.Array(hxeu__bpesb, 1, 'C')


def create_numeric_func_overload(func_name):
    if func_name not in double_arg_funcs:
        func_name = func_name.lower()

        def overload_func(arr):
            if isinstance(arr, types.optional):
                return unopt_argument(
                    f'bodo.libs.bodosql_array_kernels.{func_name}', ['arr'], 0)
            lytk__zybn = 'def impl(arr):\n'
            lytk__zybn += (
                f'  return bodo.libs.bodosql_array_kernels.{func_name}_util(arr)'
                )
            erb__ytkbx = {}
            exec(lytk__zybn, {'bodo': bodo}, erb__ytkbx)
            return erb__ytkbx['impl']
    else:
        func_name = func_name.lower()

        def overload_func(arr0, arr1):
            args = [arr0, arr1]
            for hofc__traj in range(2):
                if isinstance(args[hofc__traj], types.optional):
                    return unopt_argument(
                        f'bodo.libs.bodosql_array_kernels.{func_name}', [
                        'arr0', 'arr1'], hofc__traj)
            lytk__zybn = 'def impl(arr0, arr1):\n'
            lytk__zybn += (
                f'  return bodo.libs.bodosql_array_kernels.{func_name}_util(arr0, arr1)'
                )
            erb__ytkbx = {}
            exec(lytk__zybn, {'bodo': bodo}, erb__ytkbx)
            return erb__ytkbx['impl']
    return overload_func


def create_numeric_util_overload(func_name):
    if func_name not in double_arg_funcs:

        def overload_numeric_util(arr):
            verify_int_float_arg(arr, func_name, 'arr')
            qekdq__jisuz = ['arr']
            pmgl__ceb = [arr]
            twcm__dqkxv = [True]
            xfz__iftjx = ''
            if func_name in single_arg_funcs:
                if func_name == 'FACTORIAL':
                    xfz__iftjx += (
                        'if arg0 > 20 or np.abs(np.int64(arg0)) != arg0:\n')
                    xfz__iftjx += '  bodo.libs.array_kernels.setna(res, i)\n'
                    xfz__iftjx += 'else:\n'
                    xfz__iftjx += (
                        f'  res[i] = np.math.factorial(np.int64(arg0))')
                elif func_name == 'LN':
                    xfz__iftjx += f'res[i] = np.log(arg0)'
                else:
                    xfz__iftjx += f'res[i] = np.{func_name.lower()}(arg0)'
            else:
                ValueError(f'Unknown function name: {func_name}')
            hxeu__bpesb = _get_numeric_output_dtype(func_name, arr)
            return gen_vectorized(qekdq__jisuz, pmgl__ceb, twcm__dqkxv,
                xfz__iftjx, hxeu__bpesb)
    else:

        def overload_numeric_util(arr0, arr1):
            verify_int_float_arg(arr0, func_name, 'arr0')
            verify_int_float_arg(arr0, func_name, 'arr1')
            qekdq__jisuz = ['arr0', 'arr1']
            pmgl__ceb = [arr0, arr1]
            twcm__dqkxv = [True, True]
            hxeu__bpesb = _get_numeric_output_dtype(func_name, arr0, arr1)
            xfz__iftjx = ''
            if func_name == 'MOD':
                xfz__iftjx += 'if arg1 == 0:\n'
                xfz__iftjx += '  bodo.libs.array_kernels.setna(res, i)\n'
                xfz__iftjx += 'else:\n'
                xfz__iftjx += (
                    '  res[i] = np.sign(arg0) * np.mod(np.abs(arg0), np.abs(arg1))'
                    )
            elif func_name == 'POWER':
                xfz__iftjx += 'res[i] = np.power(np.float64(arg0), arg1)'
            elif func_name == 'ROUND':
                xfz__iftjx += 'res[i] = np.round(arg0, arg1)'
            elif func_name == 'TRUNC':
                xfz__iftjx += 'if int(arg1) == arg1:\n'
                xfz__iftjx += (
                    '  res[i] = np.trunc(arg0 * (10.0 ** arg1)) * (10.0 ** -arg1)\n'
                    )
                xfz__iftjx += 'else:\n'
                xfz__iftjx += '  bodo.libs.array_kernels.setna(res, i)'
            else:
                raise ValueError(f'Unknown function name: {func_name}')
            return gen_vectorized(qekdq__jisuz, pmgl__ceb, twcm__dqkxv,
                xfz__iftjx, hxeu__bpesb)
    return overload_numeric_util


def _install_numeric_overload(funcs_utils_names):
    for vku__xyi, eida__rvmgb, func_name in funcs_utils_names:
        vmcf__tpey = create_numeric_func_overload(func_name)
        overload(vku__xyi)(vmcf__tpey)
        asrq__uik = create_numeric_util_overload(func_name)
        overload(eida__rvmgb)(asrq__uik)


_install_numeric_overload(funcs_utils_names)


@numba.generated_jit(nopython=True)
def bitand(A, B):
    args = [A, B]
    for hofc__traj in range(2):
        if isinstance(args[hofc__traj], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.bitand',
                ['A', 'B'], hofc__traj)

    def impl(A, B):
        return bitand_util(A, B)
    return impl


@numba.generated_jit(nopython=True)
def bitshiftleft(A, B):
    args = [A, B]
    for hofc__traj in range(2):
        if isinstance(args[hofc__traj], types.optional):
            return unopt_argument(
                'bodo.libs.bodosql_array_kernels.bitshiftleft', ['A', 'B'],
                hofc__traj)

    def impl(A, B):
        return bitshiftleft_util(A, B)
    return impl


@numba.generated_jit(nopython=True)
def bitnot(A):
    if isinstance(A, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.bitnot_util',
            ['A'], 0)

    def impl(A):
        return bitnot_util(A)
    return impl


@numba.generated_jit(nopython=True)
def bitor(A, B):
    args = [A, B]
    for hofc__traj in range(2):
        if isinstance(args[hofc__traj], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.bitor',
                ['A', 'B'], hofc__traj)

    def impl(A, B):
        return bitor_util(A, B)
    return impl


@numba.generated_jit(nopython=True)
def bitshiftright(A, B):
    args = [A, B]
    for hofc__traj in range(2):
        if isinstance(args[hofc__traj], types.optional):
            return unopt_argument(
                'bodo.libs.bodosql_array_kernels.bitshiftright', ['A', 'B'],
                hofc__traj)

    def impl(A, B):
        return bitshiftright_util(A, B)
    return impl


@numba.generated_jit(nopython=True)
def bitxor(A, B):
    args = [A, B]
    for hofc__traj in range(2):
        if isinstance(args[hofc__traj], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.bitxor',
                ['A', 'B'], hofc__traj)

    def impl(A, B):
        return bitxor_util(A, B)
    return impl


@numba.generated_jit(nopython=True)
def conv(arr, old_base, new_base):
    args = [arr, old_base, new_base]
    for hofc__traj in range(3):
        if isinstance(args[hofc__traj], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.conv', [
                'arr', 'old_base', 'new_base'], hofc__traj)

    def impl(arr, old_base, new_base):
        return conv_util(arr, old_base, new_base)
    return impl


@numba.generated_jit(nopython=True)
def getbit(A, B):
    args = [A, B]
    for hofc__traj in range(2):
        if isinstance(args[hofc__traj], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.getbit',
                ['A', 'B'], hofc__traj)

    def impl(A, B):
        return getbit_util(A, B)
    return impl


@numba.generated_jit(nopython=True)
def haversine(lat1, lon1, lat2, lon2):
    args = [lat1, lon1, lat2, lon2]
    for hofc__traj in range(4):
        if isinstance(args[hofc__traj], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.haversine',
                ['lat1', 'lon1', 'lat2', 'lon2'], hofc__traj)

    def impl(lat1, lon1, lat2, lon2):
        return haversine_util(lat1, lon1, lat2, lon2)
    return impl


@numba.generated_jit(nopython=True)
def div0(arr, divisor):
    args = [arr, divisor]
    for hofc__traj in range(2):
        if isinstance(args[hofc__traj], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.div0', [
                'arr', 'divisor'], hofc__traj)

    def impl(arr, divisor):
        return div0_util(arr, divisor)
    return impl


@numba.generated_jit(nopython=True)
def log(arr, base):
    args = [arr, base]
    for hofc__traj in range(2):
        if isinstance(args[hofc__traj], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.log', [
                'arr', 'base'], hofc__traj)

    def impl(arr, base):
        return log_util(arr, base)
    return impl


@numba.generated_jit(nopython=True)
def negate(arr):
    if isinstance(arr, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.negate_util',
            ['arr'], 0)

    def impl(arr):
        return negate_util(arr)
    return impl


@numba.generated_jit(nopython=True)
def width_bucket(arr, min_val, max_val, num_buckets):
    args = [arr, min_val, max_val, num_buckets]
    for hofc__traj in range(4):
        if isinstance(args[hofc__traj], types.optional):
            return unopt_argument(
                'bodo.libs.bodosql_array_kernels.width_bucket', ['arr',
                'min_val', 'max_val', 'num_buckets'], hofc__traj)

    def impl(arr, min_val, max_val, num_buckets):
        return width_bucket_util(arr, min_val, max_val, num_buckets)
    return impl


@numba.generated_jit(nopython=True)
def bitand_util(A, B):
    verify_int_arg(A, 'bitand', 'A')
    verify_int_arg(B, 'bitand', 'B')
    qekdq__jisuz = ['A', 'B']
    pmgl__ceb = [A, B]
    twcm__dqkxv = [True] * 2
    xfz__iftjx = 'res[i] = arg0 & arg1'
    hxeu__bpesb = get_common_broadcasted_type([A, B], 'bitand')
    return gen_vectorized(qekdq__jisuz, pmgl__ceb, twcm__dqkxv, xfz__iftjx,
        hxeu__bpesb)


@numba.generated_jit(nopython=True)
def bitshiftleft_util(A, B):
    verify_int_arg(A, 'bitshiftleft', 'A')
    verify_int_arg(B, 'bitshiftleft', 'B')
    qekdq__jisuz = ['A', 'B']
    pmgl__ceb = [A, B]
    twcm__dqkxv = [True] * 2
    xfz__iftjx = 'res[i] = arg0 << arg1'
    hxeu__bpesb = bodo.libs.int_arr_ext.IntegerArrayType(types.int64)
    return gen_vectorized(qekdq__jisuz, pmgl__ceb, twcm__dqkxv, xfz__iftjx,
        hxeu__bpesb)


@numba.generated_jit(nopython=True)
def bitnot_util(A):
    verify_int_arg(A, 'bitnot', 'A')
    qekdq__jisuz = ['A']
    pmgl__ceb = [A]
    twcm__dqkxv = [True]
    xfz__iftjx = 'res[i] = ~arg0'
    if A == bodo.none:
        hxeu__bpesb = bodo.none
    else:
        if bodo.utils.utils.is_array_typ(A, True):
            ckbzc__znlhu = A.dtype
        else:
            ckbzc__znlhu = A
        hxeu__bpesb = bodo.libs.int_arr_ext.IntegerArrayType(ckbzc__znlhu)
    return gen_vectorized(qekdq__jisuz, pmgl__ceb, twcm__dqkxv, xfz__iftjx,
        hxeu__bpesb)


@numba.generated_jit(nopython=True)
def bitor_util(A, B):
    verify_int_arg(A, 'bitor', 'A')
    verify_int_arg(B, 'bitor', 'B')
    qekdq__jisuz = ['A', 'B']
    pmgl__ceb = [A, B]
    twcm__dqkxv = [True] * 2
    xfz__iftjx = 'res[i] = arg0 | arg1'
    hxeu__bpesb = get_common_broadcasted_type([A, B], 'bitor')
    return gen_vectorized(qekdq__jisuz, pmgl__ceb, twcm__dqkxv, xfz__iftjx,
        hxeu__bpesb)


@numba.generated_jit(nopython=True)
def bitshiftright_util(A, B):
    verify_int_arg(A, 'bitshiftright', 'A')
    verify_int_arg(B, 'bitshiftright', 'B')
    qekdq__jisuz = ['A', 'B']
    pmgl__ceb = [A, B]
    twcm__dqkxv = [True] * 2
    if A == bodo.none:
        ckbzc__znlhu = hxeu__bpesb = bodo.none
    else:
        if bodo.utils.utils.is_array_typ(A, True):
            ckbzc__znlhu = A.dtype
        else:
            ckbzc__znlhu = A
        hxeu__bpesb = bodo.libs.int_arr_ext.IntegerArrayType(ckbzc__znlhu)
    xfz__iftjx = f'res[i] = arg0 >> arg1\n'
    return gen_vectorized(qekdq__jisuz, pmgl__ceb, twcm__dqkxv, xfz__iftjx,
        hxeu__bpesb)


@numba.generated_jit(nopython=True)
def bitxor_util(A, B):
    verify_int_arg(A, 'bitxor', 'A')
    verify_int_arg(B, 'bitxor', 'B')
    qekdq__jisuz = ['A', 'B']
    pmgl__ceb = [A, B]
    twcm__dqkxv = [True] * 2
    xfz__iftjx = 'res[i] = arg0 ^ arg1'
    hxeu__bpesb = get_common_broadcasted_type([A, B], 'bitxor')
    return gen_vectorized(qekdq__jisuz, pmgl__ceb, twcm__dqkxv, xfz__iftjx,
        hxeu__bpesb)


@numba.generated_jit(nopython=True)
def conv_util(arr, old_base, new_base):
    verify_string_arg(arr, 'CONV', 'arr')
    verify_int_arg(old_base, 'CONV', 'old_base')
    verify_int_arg(new_base, 'CONV', 'new_base')
    qekdq__jisuz = ['arr', 'old_base', 'new_base']
    pmgl__ceb = [arr, old_base, new_base]
    twcm__dqkxv = [True] * 3
    xfz__iftjx = 'old_val = int(arg0, arg1)\n'
    xfz__iftjx += 'if arg2 == 2:\n'
    xfz__iftjx += "   res[i] = format(old_val, 'b')\n"
    xfz__iftjx += 'elif arg2 == 8:\n'
    xfz__iftjx += "   res[i] = format(old_val, 'o')\n"
    xfz__iftjx += 'elif arg2 == 10:\n'
    xfz__iftjx += "   res[i] = format(old_val, 'd')\n"
    xfz__iftjx += 'elif arg2 == 16:\n'
    xfz__iftjx += "   res[i] = format(old_val, 'x')\n"
    xfz__iftjx += 'else:\n'
    xfz__iftjx += '   bodo.libs.array_kernels.setna(res, i)\n'
    hxeu__bpesb = bodo.string_array_type
    return gen_vectorized(qekdq__jisuz, pmgl__ceb, twcm__dqkxv, xfz__iftjx,
        hxeu__bpesb)


@numba.generated_jit(nopython=True)
def getbit_util(A, B):
    verify_int_arg(A, 'bitshiftright', 'A')
    verify_int_arg(B, 'bitshiftright', 'B')
    qekdq__jisuz = ['A', 'B']
    pmgl__ceb = [A, B]
    twcm__dqkxv = [True] * 2
    xfz__iftjx = 'res[i] = (arg0 >> arg1) & 1'
    hxeu__bpesb = bodo.libs.int_arr_ext.IntegerArrayType(types.uint8)
    return gen_vectorized(qekdq__jisuz, pmgl__ceb, twcm__dqkxv, xfz__iftjx,
        hxeu__bpesb)


@numba.generated_jit(nopython=True)
def haversine_util(lat1, lon1, lat2, lon2):
    verify_int_float_arg(lat1, 'HAVERSINE', 'lat1')
    verify_int_float_arg(lon1, 'HAVERSINE', 'lon1')
    verify_int_float_arg(lat2, 'HAVERSINE', 'lat2')
    verify_int_float_arg(lon2, 'HAVERSINE', 'lon2')
    qekdq__jisuz = ['lat1', 'lon1', 'lat2', 'lon2']
    pmgl__ceb = [lat1, lon1, lat2, lon2]
    nhhh__xbw = [True] * 4
    xfz__iftjx = (
        'arg0, arg1, arg2, arg3 = map(np.radians, (arg0, arg1, arg2, arg3))\n')
    kmrel__gee = '(arg2 - arg0) * 0.5'
    ghu__nsayy = '(arg3 - arg1) * 0.5'
    vfb__plcj = (
        f'np.square(np.sin({kmrel__gee})) + (np.cos(arg0) * np.cos(arg2) * np.square(np.sin({ghu__nsayy})))'
        )
    xfz__iftjx += f'res[i] = 12742.0 * np.arcsin(np.sqrt({vfb__plcj}))\n'
    hxeu__bpesb = types.Array(bodo.float64, 1, 'C')
    return gen_vectorized(qekdq__jisuz, pmgl__ceb, nhhh__xbw, xfz__iftjx,
        hxeu__bpesb)


@numba.generated_jit(nopython=True)
def div0_util(arr, divisor):
    verify_int_float_arg(arr, 'DIV0', 'arr')
    verify_int_float_arg(divisor, 'DIV0', 'divisor')
    qekdq__jisuz = ['arr', 'divisor']
    pmgl__ceb = [arr, divisor]
    nhhh__xbw = [True] * 2
    xfz__iftjx = 'res[i] = arg0 / arg1 if arg1 else 0\n'
    hxeu__bpesb = types.Array(bodo.float64, 1, 'C')
    return gen_vectorized(qekdq__jisuz, pmgl__ceb, nhhh__xbw, xfz__iftjx,
        hxeu__bpesb)


@numba.generated_jit(nopython=True)
def log_util(arr, base):
    verify_int_float_arg(arr, 'log', 'arr')
    verify_int_float_arg(base, 'log', 'base')
    qekdq__jisuz = ['arr', 'base']
    pmgl__ceb = [arr, base]
    twcm__dqkxv = [True] * 2
    xfz__iftjx = 'res[i] = np.log(arg0) / np.log(arg1)'
    hxeu__bpesb = types.Array(bodo.float64, 1, 'C')
    return gen_vectorized(qekdq__jisuz, pmgl__ceb, twcm__dqkxv, xfz__iftjx,
        hxeu__bpesb)


@numba.generated_jit(nopython=True)
def negate_util(arr):
    qekdq__jisuz = ['arr']
    pmgl__ceb = [arr]
    twcm__dqkxv = [True]
    if bodo.utils.utils.is_array_typ(arr, False):
        ckbzc__znlhu = arr.dtype
    elif bodo.utils.utils.is_array_typ(arr, True):
        ckbzc__znlhu = arr.data.dtype
    else:
        ckbzc__znlhu = arr
    xfz__iftjx = {types.uint8: 'res[i] = -np.int16(arg0)', types.uint16:
        'res[i] = -np.int32(arg0)', types.uint32: 'res[i] = -np.int64(arg0)'
        }.get(ckbzc__znlhu, 'res[i] = -arg0')
    ckbzc__znlhu = {types.uint8: types.int16, types.uint16: types.int32,
        types.uint32: types.int64, types.uint64: types.int64}.get(ckbzc__znlhu,
        ckbzc__znlhu)
    if isinstance(ckbzc__znlhu, types.Integer):
        hxeu__bpesb = bodo.utils.typing.dtype_to_array_type(ckbzc__znlhu)
    else:
        hxeu__bpesb = arr
    hxeu__bpesb = bodo.utils.typing.to_nullable_type(hxeu__bpesb)
    return gen_vectorized(qekdq__jisuz, pmgl__ceb, twcm__dqkxv, xfz__iftjx,
        hxeu__bpesb)


@numba.generated_jit(nopython=True)
def width_bucket_util(arr, min_val, max_val, num_buckets):
    verify_int_float_arg(arr, 'WIDTH_BUCKET', 'arr')
    verify_int_float_arg(min_val, 'WIDTH_BUCKET', 'min_val')
    verify_int_float_arg(max_val, 'WIDTH_BUCKET', 'max_val')
    verify_int_arg(num_buckets, 'WIDTH_BUCKET', 'num_buckets')
    qekdq__jisuz = ['arr', 'min_val', 'max_val', 'num_buckets']
    pmgl__ceb = [arr, min_val, max_val, num_buckets]
    twcm__dqkxv = [True] * 4
    xfz__iftjx = (
        "if arg1 >= arg2: raise ValueError('min_val must be less than max_val')\n"
        )
    xfz__iftjx += (
        "if arg3 <= 0: raise ValueError('num_buckets must be a positive integer')\n"
        )
    xfz__iftjx += (
        'res[i] = min(max(-1.0, math.floor((arg0 - arg1) / ((arg2 - arg1) / arg3))), arg3) + 1.0'
        )
    hxeu__bpesb = bodo.libs.int_arr_ext.IntegerArrayType(types.int64)
    return gen_vectorized(qekdq__jisuz, pmgl__ceb, twcm__dqkxv, xfz__iftjx,
        hxeu__bpesb)
