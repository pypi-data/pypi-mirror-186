"""
Implements window/aggregation array kernels that are specific to BodoSQL.
Specifically, window/aggregation array kernels that do not concern window
frames.
"""
import numba
import numpy as np
import pandas as pd
from numba.core import types
from numba.extending import overload
import bodo
from bodo.libs.bodosql_array_kernel_utils import *
from bodo.utils.typing import get_overload_const_bool, get_overload_const_str, is_overload_constant_bool, is_overload_constant_str, raise_bodo_error


def rank_sql(arr_tup, method='average', pct=False):
    return


@overload(rank_sql, no_unliteral=True)
def overload_rank_sql(arr_tup, method='average', pct=False):
    if not is_overload_constant_str(method):
        raise_bodo_error(
            "Series.rank(): 'method' argument must be a constant string")
    method = get_overload_const_str(method)
    if not is_overload_constant_bool(pct):
        raise_bodo_error(
            "Series.rank(): 'pct' argument must be a constant boolean")
    pct = get_overload_const_bool(pct)
    fxkb__fkec = 'def impl(arr_tup, method="average", pct=False):\n'
    if method == 'first':
        fxkb__fkec += '  ret = np.arange(1, n + 1, 1, np.float64)\n'
    else:
        fxkb__fkec += (
            '  obs = bodo.libs.array_kernels._rank_detect_ties(arr_tup[0])\n')
        for meal__wrttb in range(1, len(arr_tup)):
            fxkb__fkec += f"""  obs = obs | bodo.libs.array_kernels._rank_detect_ties(arr_tup[{meal__wrttb}]) 
"""
        fxkb__fkec += '  dense = obs.cumsum()\n'
        if method == 'dense':
            fxkb__fkec += '  ret = bodo.utils.conversion.fix_arr_dtype(\n'
            fxkb__fkec += '    dense,\n'
            fxkb__fkec += '    new_dtype=np.float64,\n'
            fxkb__fkec += '    copy=True,\n'
            fxkb__fkec += '    nan_to_str=False,\n'
            fxkb__fkec += '    from_series=True,\n'
            fxkb__fkec += '  )\n'
        else:
            fxkb__fkec += (
                '  count = np.concatenate((np.nonzero(obs)[0], np.array([len(obs)])))\n'
                )
            fxkb__fkec += """  count_float = bodo.utils.conversion.fix_arr_dtype(count, new_dtype=np.float64, copy=True, nan_to_str=False, from_series=True)
"""
            if method == 'max':
                fxkb__fkec += '  ret = count_float[dense]\n'
            elif method == 'min':
                fxkb__fkec += '  ret = count_float[dense - 1] + 1\n'
            else:
                fxkb__fkec += (
                    '  ret = 0.5 * (count_float[dense] + count_float[dense - 1] + 1)\n'
                    )
    if pct:
        if method == 'dense':
            fxkb__fkec += '  div_val = np.max(ret)\n'
        else:
            fxkb__fkec += '  div_val = len(arr_tup[0])\n'
        fxkb__fkec += '  for i in range(len(ret)):\n'
        fxkb__fkec += '    ret[i] = ret[i] / div_val\n'
    fxkb__fkec += '  return ret\n'
    iikp__dtnlb = {}
    exec(fxkb__fkec, {'np': np, 'pd': pd, 'bodo': bodo}, iikp__dtnlb)
    return iikp__dtnlb['impl']


@numba.generated_jit(nopython=True)
def change_event(S):

    def impl(S):
        lksw__spx = bodo.hiframes.pd_series_ext.get_series_data(S)
        inkt__qachv = len(lksw__spx)
        phv__erku = bodo.utils.utils.alloc_type(inkt__qachv, types.uint64, -1)
        atbwh__kjlrn = -1
        for meal__wrttb in range(inkt__qachv):
            phv__erku[meal__wrttb] = 0
            if not bodo.libs.array_kernels.isna(lksw__spx, meal__wrttb):
                atbwh__kjlrn = meal__wrttb
                break
        if atbwh__kjlrn != -1:
            pgxml__eeh = lksw__spx[atbwh__kjlrn]
            for meal__wrttb in range(atbwh__kjlrn + 1, inkt__qachv):
                if bodo.libs.array_kernels.isna(lksw__spx, meal__wrttb
                    ) or lksw__spx[meal__wrttb] == pgxml__eeh:
                    phv__erku[meal__wrttb] = phv__erku[meal__wrttb - 1]
                else:
                    pgxml__eeh = lksw__spx[meal__wrttb]
                    phv__erku[meal__wrttb] = phv__erku[meal__wrttb - 1] + 1
        return bodo.hiframes.pd_series_ext.init_series(phv__erku, bodo.
            hiframes.pd_index_ext.init_range_index(0, inkt__qachv, 1), None)
    return impl


@numba.generated_jit(nopython=True)
def windowed_sum(S, lower_bound, upper_bound):
    verify_int_float_arg(S, 'windowed_sum', S)
    if not bodo.utils.utils.is_array_typ(S, True):
        raise_bodo_error('Input must be an array type')
    wozeg__oubj = 'res[i] = total'
    nbvn__pgtx = 'constant_value = S.sum()'
    ffc__oxpf = 'total = 0'
    btfte__snxdf = 'total += elem'
    qyj__mybr = 'total -= elem'
    if isinstance(S.dtype, types.Integer):
        sxgu__nsirm = bodo.libs.int_arr_ext.IntegerArrayType(types.int64)
    else:
        sxgu__nsirm = types.Array(bodo.float64, 1, 'C')
    return gen_windowed(wozeg__oubj, nbvn__pgtx, sxgu__nsirm, setup_block=
        ffc__oxpf, enter_block=btfte__snxdf, exit_block=qyj__mybr)


@numba.generated_jit(nopython=True)
def windowed_count(S, lower_bound, upper_bound):
    if not bodo.utils.utils.is_array_typ(S, True):
        raise_bodo_error('Input must be an array type')
    wozeg__oubj = 'res[i] = in_window'
    nbvn__pgtx = 'constant_value = S.count()'
    zqn__lsih = 'res[i] = 0'
    sxgu__nsirm = bodo.libs.int_arr_ext.IntegerArrayType(types.int64)
    return gen_windowed(wozeg__oubj, nbvn__pgtx, sxgu__nsirm, empty_block=
        zqn__lsih)


@numba.generated_jit(nopython=True)
def windowed_avg(S, lower_bound, upper_bound):
    verify_int_float_arg(S, 'windowed_avg', S)
    if not bodo.utils.utils.is_array_typ(S, True):
        raise_bodo_error('Input must be an array type')
    wozeg__oubj = 'res[i] = total / in_window'
    nbvn__pgtx = 'constant_value = S.mean()'
    sxgu__nsirm = types.Array(bodo.float64, 1, 'C')
    ffc__oxpf = 'total = 0'
    btfte__snxdf = 'total += elem'
    qyj__mybr = 'total -= elem'
    return gen_windowed(wozeg__oubj, nbvn__pgtx, sxgu__nsirm, setup_block=
        ffc__oxpf, enter_block=btfte__snxdf, exit_block=qyj__mybr)


@numba.generated_jit(nopython=True)
def windowed_median(S, lower_bound, upper_bound):
    verify_int_float_arg(S, 'windowed_median', S)
    if not bodo.utils.utils.is_array_typ(S, True):
        raise_bodo_error('Input must be an array type')
    wozeg__oubj = 'res[i] = np.median(arr2)'
    nbvn__pgtx = 'constant_value = S.median()'
    sxgu__nsirm = types.Array(bodo.float64, 1, 'C')
    ffc__oxpf = 'arr2 = np.zeros(0, dtype=np.float64)'
    btfte__snxdf = 'arr2 = np.append(arr2, elem)'
    qyj__mybr = 'arr2 = np.delete(arr2, np.argwhere(arr2 == elem)[0])'
    return gen_windowed(wozeg__oubj, nbvn__pgtx, sxgu__nsirm, setup_block=
        ffc__oxpf, enter_block=btfte__snxdf, exit_block=qyj__mybr)


@numba.generated_jit(nopython=True)
def windowed_mode(S, lower_bound, upper_bound):
    if not bodo.utils.utils.is_array_typ(S, True):
        raise_bodo_error('Input must be an array type')
    if isinstance(S, bodo.SeriesType):
        sxgu__nsirm = S.data
    else:
        sxgu__nsirm = S
    wozeg__oubj = 'bestVal, bestCount = None, 0\n'
    wozeg__oubj += 'for key in counts:\n'
    wozeg__oubj += '   if counts[key] > bestCount:\n'
    wozeg__oubj += '      bestVal, bestCount = key, counts[key]\n'
    wozeg__oubj += 'res[i] = bestVal'
    nbvn__pgtx = 'counts = {arr[0]: 0}\n'
    nbvn__pgtx += 'for i in range(len(S)):\n'
    nbvn__pgtx += '   if not bodo.libs.array_kernels.isna(arr, i):\n'
    nbvn__pgtx += '      counts[arr[i]] = counts.get(arr[i], 0) + 1\n'
    nbvn__pgtx += wozeg__oubj.replace('res[i]', 'constant_value')
    ffc__oxpf = 'counts = {arr[0]: 0}'
    btfte__snxdf = 'counts[elem] = counts.get(elem, 0) + 1'
    qyj__mybr = 'counts[elem] = counts.get(elem, 0) - 1'
    return gen_windowed(wozeg__oubj, nbvn__pgtx, sxgu__nsirm, setup_block=
        ffc__oxpf, enter_block=btfte__snxdf, exit_block=qyj__mybr)


@numba.generated_jit(nopython=True)
def windowed_ratio_to_report(S, lower_bound, upper_bound):
    verify_int_float_arg(S, 'ratio_to_report', S)
    if not bodo.utils.utils.is_array_typ(S, True):
        raise_bodo_error('Input must be an array type')
    wozeg__oubj = 'if total == 0 or bodo.libs.array_kernels.isna(arr, i):\n'
    wozeg__oubj += '   bodo.libs.array_kernels.setna(res, i)\n'
    wozeg__oubj += 'else:\n'
    wozeg__oubj += '   res[i] = arr[i] / total'
    nbvn__pgtx = None
    sxgu__nsirm = types.Array(bodo.float64, 1, 'C')
    ffc__oxpf = 'total = 0'
    btfte__snxdf = 'total += elem'
    qyj__mybr = 'total -= elem'
    return gen_windowed(wozeg__oubj, nbvn__pgtx, sxgu__nsirm, setup_block=
        ffc__oxpf, enter_block=btfte__snxdf, exit_block=qyj__mybr)
