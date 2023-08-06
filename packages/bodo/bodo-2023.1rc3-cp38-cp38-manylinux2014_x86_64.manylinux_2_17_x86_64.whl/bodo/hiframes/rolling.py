"""implementations of rolling window functions (sequential and parallel)
"""
import numba
import numpy as np
import pandas as pd
from numba.core import types
from numba.core.imputils import impl_ret_borrowed
from numba.core.typing import signature
from numba.core.typing.templates import AbstractTemplate, infer_global
from numba.extending import lower_builtin, overload, register_jitable
import bodo
from bodo.libs.distributed_api import Reduce_Type
from bodo.utils.typing import BodoError, decode_if_dict_array, get_overload_const_func, get_overload_const_str, is_const_func_type, is_overload_constant_bool, is_overload_constant_str, is_overload_none, is_overload_true
from bodo.utils.utils import unliteral_all
supported_rolling_funcs = ('sum', 'mean', 'var', 'std', 'count', 'median',
    'min', 'max', 'cov', 'corr', 'apply')
unsupported_rolling_methods = ['skew', 'kurt', 'aggregate', 'quantile', 'sem']


def rolling_fixed(arr, win):
    return arr


def rolling_variable(arr, on_arr, win):
    return arr


def rolling_cov(arr, arr2, win):
    return arr


def rolling_corr(arr, arr2, win):
    return arr


@infer_global(rolling_cov)
@infer_global(rolling_corr)
class RollingCovType(AbstractTemplate):

    def generic(self, args, kws):
        arr = args[0]
        levc__szx = arr.copy(dtype=types.float64)
        return signature(levc__szx, *unliteral_all(args))


@lower_builtin(rolling_corr, types.VarArg(types.Any))
@lower_builtin(rolling_cov, types.VarArg(types.Any))
def lower_rolling_corr_dummy(context, builder, sig, args):
    return context.get_constant_null(sig.return_type)


@overload(rolling_fixed, no_unliteral=True)
def overload_rolling_fixed(arr, index_arr, win, minp, center, fname, raw=
    True, parallel=False):
    assert is_overload_constant_bool(raw
        ), 'raw argument should be constant bool'
    if is_const_func_type(fname):
        func = _get_apply_func(fname)
        return (lambda arr, index_arr, win, minp, center, fname, raw=True,
            parallel=False: roll_fixed_apply(arr, index_arr, win, minp,
            center, parallel, func, raw))
    assert is_overload_constant_str(fname)
    aczvc__mmg = get_overload_const_str(fname)
    if aczvc__mmg not in ('sum', 'mean', 'var', 'std', 'count', 'median',
        'min', 'max'):
        raise BodoError('invalid rolling (fixed window) function {}'.format
            (aczvc__mmg))
    if aczvc__mmg in ('median', 'min', 'max'):
        uscz__tad = 'def kernel_func(A):\n'
        uscz__tad += '  if np.isnan(A).sum() != 0: return np.nan\n'
        uscz__tad += '  return np.{}(A)\n'.format(aczvc__mmg)
        uzu__erybw = {}
        exec(uscz__tad, {'np': np}, uzu__erybw)
        kernel_func = register_jitable(uzu__erybw['kernel_func'])
        return (lambda arr, index_arr, win, minp, center, fname, raw=True,
            parallel=False: roll_fixed_apply(arr, index_arr, win, minp,
            center, parallel, kernel_func))
    init_kernel, add_kernel, remove_kernel, calc_kernel = linear_kernels[
        aczvc__mmg]
    return (lambda arr, index_arr, win, minp, center, fname, raw=True,
        parallel=False: roll_fixed_linear_generic(arr, win, minp, center,
        parallel, init_kernel, add_kernel, remove_kernel, calc_kernel))


@overload(rolling_variable, no_unliteral=True)
def overload_rolling_variable(arr, on_arr, index_arr, win, minp, center,
    fname, raw=True, parallel=False):
    assert is_overload_constant_bool(raw)
    if is_const_func_type(fname):
        func = _get_apply_func(fname)
        return (lambda arr, on_arr, index_arr, win, minp, center, fname,
            raw=True, parallel=False: roll_variable_apply(arr, on_arr,
            index_arr, win, minp, center, parallel, func, raw))
    assert is_overload_constant_str(fname)
    aczvc__mmg = get_overload_const_str(fname)
    if aczvc__mmg not in ('sum', 'mean', 'var', 'std', 'count', 'median',
        'min', 'max'):
        raise BodoError('invalid rolling (variable window) function {}'.
            format(aczvc__mmg))
    if aczvc__mmg in ('median', 'min', 'max'):
        uscz__tad = 'def kernel_func(A):\n'
        uscz__tad += '  arr  = dropna(A)\n'
        uscz__tad += '  if len(arr) == 0: return np.nan\n'
        uscz__tad += '  return np.{}(arr)\n'.format(aczvc__mmg)
        uzu__erybw = {}
        exec(uscz__tad, {'np': np, 'dropna': _dropna}, uzu__erybw)
        kernel_func = register_jitable(uzu__erybw['kernel_func'])
        return (lambda arr, on_arr, index_arr, win, minp, center, fname,
            raw=True, parallel=False: roll_variable_apply(arr, on_arr,
            index_arr, win, minp, center, parallel, kernel_func))
    init_kernel, add_kernel, remove_kernel, calc_kernel = linear_kernels[
        aczvc__mmg]
    return (lambda arr, on_arr, index_arr, win, minp, center, fname, raw=
        True, parallel=False: roll_var_linear_generic(arr, on_arr, win,
        minp, center, parallel, init_kernel, add_kernel, remove_kernel,
        calc_kernel))


def _get_apply_func(f_type):
    func = get_overload_const_func(f_type, None)
    return bodo.compiler.udf_jit(func)


comm_border_tag = 22


@register_jitable
def roll_fixed_linear_generic(in_arr, win, minp, center, parallel,
    init_data, add_obs, remove_obs, calc_out):
    _validate_roll_fixed_args(win, minp)
    in_arr = prep_values(in_arr)
    rank = bodo.libs.distributed_api.get_rank()
    n_pes = bodo.libs.distributed_api.get_size()
    N = len(in_arr)
    offset = (win - 1) // 2 if center else 0
    if parallel:
        halo_size = np.int32(win // 2) if center else np.int32(win - 1)
        if _is_small_for_parallel(N, halo_size):
            return _handle_small_data(in_arr, win, minp, center, rank,
                n_pes, init_data, add_obs, remove_obs, calc_out)
        rpxj__qeap = _border_icomm(in_arr, rank, n_pes, halo_size, True, center
            )
        (l_recv_buff, r_recv_buff, l_send_req, r_send_req, l_recv_req,
            hhgs__xhhj) = rpxj__qeap
    output, data = roll_fixed_linear_generic_seq(in_arr, win, minp, center,
        init_data, add_obs, remove_obs, calc_out)
    if parallel:
        _border_send_wait(r_send_req, l_send_req, rank, n_pes, True, center)
        if center and rank != n_pes - 1:
            bodo.libs.distributed_api.wait(hhgs__xhhj, True)
            for ixoer__gce in range(0, halo_size):
                data = add_obs(r_recv_buff[ixoer__gce], *data)
                tvvz__phmr = in_arr[N + ixoer__gce - win]
                data = remove_obs(tvvz__phmr, *data)
                output[N + ixoer__gce - offset] = calc_out(minp, *data)
        if rank != 0:
            bodo.libs.distributed_api.wait(l_recv_req, True)
            data = init_data()
            for ixoer__gce in range(0, halo_size):
                data = add_obs(l_recv_buff[ixoer__gce], *data)
            for ixoer__gce in range(0, win - 1):
                data = add_obs(in_arr[ixoer__gce], *data)
                if ixoer__gce > offset:
                    tvvz__phmr = l_recv_buff[ixoer__gce - offset - 1]
                    data = remove_obs(tvvz__phmr, *data)
                if ixoer__gce >= offset:
                    output[ixoer__gce - offset] = calc_out(minp, *data)
    return output


@register_jitable
def roll_fixed_linear_generic_seq(in_arr, win, minp, center, init_data,
    add_obs, remove_obs, calc_out):
    data = init_data()
    N = len(in_arr)
    offset = (win - 1) // 2 if center else 0
    output = np.empty(N, dtype=np.float64)
    edb__woth = max(minp, 1) - 1
    edb__woth = min(edb__woth, N)
    for ixoer__gce in range(0, edb__woth):
        data = add_obs(in_arr[ixoer__gce], *data)
        if ixoer__gce >= offset:
            output[ixoer__gce - offset] = calc_out(minp, *data)
    for ixoer__gce in range(edb__woth, N):
        val = in_arr[ixoer__gce]
        data = add_obs(val, *data)
        if ixoer__gce > win - 1:
            tvvz__phmr = in_arr[ixoer__gce - win]
            data = remove_obs(tvvz__phmr, *data)
        output[ixoer__gce - offset] = calc_out(minp, *data)
    cdzt__temzq = data
    for ixoer__gce in range(N, N + offset):
        if ixoer__gce > win - 1:
            tvvz__phmr = in_arr[ixoer__gce - win]
            data = remove_obs(tvvz__phmr, *data)
        output[ixoer__gce - offset] = calc_out(minp, *data)
    return output, cdzt__temzq


def roll_fixed_apply(in_arr, index_arr, win, minp, center, parallel,
    kernel_func, raw=True):
    pass


@overload(roll_fixed_apply, no_unliteral=True)
def overload_roll_fixed_apply(in_arr, index_arr, win, minp, center,
    parallel, kernel_func, raw=True):
    assert is_overload_constant_bool(raw)
    return roll_fixed_apply_impl


def roll_fixed_apply_impl(in_arr, index_arr, win, minp, center, parallel,
    kernel_func, raw=True):
    _validate_roll_fixed_args(win, minp)
    in_arr = prep_values(in_arr)
    rank = bodo.libs.distributed_api.get_rank()
    n_pes = bodo.libs.distributed_api.get_size()
    N = len(in_arr)
    offset = (win - 1) // 2 if center else 0
    index_arr = fix_index_arr(index_arr)
    if parallel:
        halo_size = np.int32(win // 2) if center else np.int32(win - 1)
        if _is_small_for_parallel(N, halo_size):
            return _handle_small_data_apply(in_arr, index_arr, win, minp,
                center, rank, n_pes, kernel_func, raw)
        rpxj__qeap = _border_icomm(in_arr, rank, n_pes, halo_size, True, center
            )
        (l_recv_buff, r_recv_buff, l_send_req, r_send_req, l_recv_req,
            hhgs__xhhj) = rpxj__qeap
        if raw == False:
            nlaz__bavu = _border_icomm(index_arr, rank, n_pes, halo_size, 
                True, center)
            (l_recv_buff_idx, r_recv_buff_idx, ajif__ticy, kgza__fmrd,
                vgzt__szbl, ecuf__nedi) = nlaz__bavu
    output = roll_fixed_apply_seq(in_arr, index_arr, win, minp, center,
        kernel_func, raw)
    if parallel:
        _border_send_wait(r_send_req, l_send_req, rank, n_pes, True, center)
        if raw == False:
            _border_send_wait(kgza__fmrd, ajif__ticy, rank, n_pes, True, center
                )
        if center and rank != n_pes - 1:
            bodo.libs.distributed_api.wait(hhgs__xhhj, True)
            if raw == False:
                bodo.libs.distributed_api.wait(ecuf__nedi, True)
            recv_right_compute(output, in_arr, index_arr, N, win, minp,
                offset, r_recv_buff, r_recv_buff_idx, kernel_func, raw)
        if rank != 0:
            bodo.libs.distributed_api.wait(l_recv_req, True)
            if raw == False:
                bodo.libs.distributed_api.wait(vgzt__szbl, True)
            recv_left_compute(output, in_arr, index_arr, win, minp, offset,
                l_recv_buff, l_recv_buff_idx, kernel_func, raw)
    return output


def recv_right_compute(output, in_arr, index_arr, N, win, minp, offset,
    r_recv_buff, r_recv_buff_idx, kernel_func, raw):
    pass


@overload(recv_right_compute, no_unliteral=True)
def overload_recv_right_compute(output, in_arr, index_arr, N, win, minp,
    offset, r_recv_buff, r_recv_buff_idx, kernel_func, raw):
    assert is_overload_constant_bool(raw)
    if is_overload_true(raw):

        def impl(output, in_arr, index_arr, N, win, minp, offset,
            r_recv_buff, r_recv_buff_idx, kernel_func, raw):
            cdzt__temzq = np.concatenate((in_arr[N - win + 1:], r_recv_buff))
            gvdwj__gyu = 0
            for ixoer__gce in range(max(N - offset, 0), N):
                data = cdzt__temzq[gvdwj__gyu:gvdwj__gyu + win]
                if win - np.isnan(data).sum() < minp:
                    output[ixoer__gce] = np.nan
                else:
                    output[ixoer__gce] = kernel_func(data)
                gvdwj__gyu += 1
        return impl

    def impl_series(output, in_arr, index_arr, N, win, minp, offset,
        r_recv_buff, r_recv_buff_idx, kernel_func, raw):
        cdzt__temzq = np.concatenate((in_arr[N - win + 1:], r_recv_buff))
        thy__jcng = np.concatenate((index_arr[N - win + 1:], r_recv_buff_idx))
        gvdwj__gyu = 0
        for ixoer__gce in range(max(N - offset, 0), N):
            data = cdzt__temzq[gvdwj__gyu:gvdwj__gyu + win]
            if win - np.isnan(data).sum() < minp:
                output[ixoer__gce] = np.nan
            else:
                output[ixoer__gce] = kernel_func(pd.Series(data, thy__jcng[
                    gvdwj__gyu:gvdwj__gyu + win]))
            gvdwj__gyu += 1
    return impl_series


def recv_left_compute(output, in_arr, index_arr, win, minp, offset,
    l_recv_buff, l_recv_buff_idx, kernel_func, raw):
    pass


@overload(recv_left_compute, no_unliteral=True)
def overload_recv_left_compute(output, in_arr, index_arr, win, minp, offset,
    l_recv_buff, l_recv_buff_idx, kernel_func, raw):
    assert is_overload_constant_bool(raw)
    if is_overload_true(raw):

        def impl(output, in_arr, index_arr, win, minp, offset, l_recv_buff,
            l_recv_buff_idx, kernel_func, raw):
            cdzt__temzq = np.concatenate((l_recv_buff, in_arr[:win - 1]))
            for ixoer__gce in range(0, win - offset - 1):
                data = cdzt__temzq[ixoer__gce:ixoer__gce + win]
                if win - np.isnan(data).sum() < minp:
                    output[ixoer__gce] = np.nan
                else:
                    output[ixoer__gce] = kernel_func(data)
        return impl

    def impl_series(output, in_arr, index_arr, win, minp, offset,
        l_recv_buff, l_recv_buff_idx, kernel_func, raw):
        cdzt__temzq = np.concatenate((l_recv_buff, in_arr[:win - 1]))
        thy__jcng = np.concatenate((l_recv_buff_idx, index_arr[:win - 1]))
        for ixoer__gce in range(0, win - offset - 1):
            data = cdzt__temzq[ixoer__gce:ixoer__gce + win]
            if win - np.isnan(data).sum() < minp:
                output[ixoer__gce] = np.nan
            else:
                output[ixoer__gce] = kernel_func(pd.Series(data, thy__jcng[
                    ixoer__gce:ixoer__gce + win]))
    return impl_series


def roll_fixed_apply_seq(in_arr, index_arr, win, minp, center, kernel_func,
    raw=True):
    pass


@overload(roll_fixed_apply_seq, no_unliteral=True)
def overload_roll_fixed_apply_seq(in_arr, index_arr, win, minp, center,
    kernel_func, raw=True):
    assert is_overload_constant_bool(raw), "'raw' should be constant bool"

    def roll_fixed_apply_seq_impl(in_arr, index_arr, win, minp, center,
        kernel_func, raw=True):
        N = len(in_arr)
        output = np.empty(N, dtype=np.float64)
        offset = (win - 1) // 2 if center else 0
        for ixoer__gce in range(0, N):
            start = max(ixoer__gce - win + 1 + offset, 0)
            end = min(ixoer__gce + 1 + offset, N)
            data = in_arr[start:end]
            if end - start - np.isnan(data).sum() < minp:
                output[ixoer__gce] = np.nan
            else:
                output[ixoer__gce] = apply_func(kernel_func, data,
                    index_arr, start, end, raw)
        return output
    return roll_fixed_apply_seq_impl


def apply_func(kernel_func, data, index_arr, start, end, raw):
    return kernel_func(data)


@overload(apply_func, no_unliteral=True)
def overload_apply_func(kernel_func, data, index_arr, start, end, raw):
    assert is_overload_constant_bool(raw), "'raw' should be constant bool"
    if is_overload_true(raw):
        return (lambda kernel_func, data, index_arr, start, end, raw:
            kernel_func(data))
    return lambda kernel_func, data, index_arr, start, end, raw: kernel_func(pd
        .Series(data, index_arr[start:end]))


def fix_index_arr(A):
    return A


@overload(fix_index_arr)
def overload_fix_index_arr(A):
    if is_overload_none(A):
        return lambda A: np.zeros(3)
    return lambda A: A


def get_offset_nanos(w):
    out = status = 0
    try:
        out = pd.tseries.frequencies.to_offset(w).nanos
    except:
        status = 1
    return out, status


def offset_to_nanos(w):
    return w


@overload(offset_to_nanos)
def overload_offset_to_nanos(w):
    if isinstance(w, types.Integer):
        return lambda w: w

    def impl(w):
        with numba.objmode(out='int64', status='int64'):
            out, status = get_offset_nanos(w)
        if status != 0:
            raise ValueError('Invalid offset value')
        return out
    return impl


@register_jitable
def roll_var_linear_generic(in_arr, on_arr_dt, win, minp, center, parallel,
    init_data, add_obs, remove_obs, calc_out):
    _validate_roll_var_args(minp, center)
    in_arr = prep_values(in_arr)
    win = offset_to_nanos(win)
    rank = bodo.libs.distributed_api.get_rank()
    n_pes = bodo.libs.distributed_api.get_size()
    on_arr = cast_dt64_arr_to_int(on_arr_dt)
    N = len(in_arr)
    left_closed = False
    right_closed = True
    if parallel:
        if _is_small_for_parallel_variable(on_arr, win):
            return _handle_small_data_variable(in_arr, on_arr, win, minp,
                rank, n_pes, init_data, add_obs, remove_obs, calc_out)
        rpxj__qeap = _border_icomm_var(in_arr, on_arr, rank, n_pes, win)
        (l_recv_buff, l_recv_t_buff, r_send_req, kaxk__chxti, l_recv_req,
            tzk__ymin) = rpxj__qeap
    start, end = _build_indexer(on_arr, N, win, left_closed, right_closed)
    output = roll_var_linear_generic_seq(in_arr, on_arr, win, minp, start,
        end, init_data, add_obs, remove_obs, calc_out)
    if parallel:
        _border_send_wait(r_send_req, r_send_req, rank, n_pes, True, False)
        _border_send_wait(kaxk__chxti, kaxk__chxti, rank, n_pes, True, False)
        if rank != 0:
            bodo.libs.distributed_api.wait(l_recv_req, True)
            bodo.libs.distributed_api.wait(tzk__ymin, True)
            num_zero_starts = 0
            for ixoer__gce in range(0, N):
                if start[ixoer__gce] != 0:
                    break
                num_zero_starts += 1
            if num_zero_starts == 0:
                return output
            recv_starts = _get_var_recv_starts(on_arr, l_recv_t_buff,
                num_zero_starts, win)
            data = init_data()
            for tsmsk__rzvv in range(recv_starts[0], len(l_recv_t_buff)):
                data = add_obs(l_recv_buff[tsmsk__rzvv], *data)
            if right_closed:
                data = add_obs(in_arr[0], *data)
            output[0] = calc_out(minp, *data)
            for ixoer__gce in range(1, num_zero_starts):
                s = recv_starts[ixoer__gce]
                nrtr__mpne = end[ixoer__gce]
                for tsmsk__rzvv in range(recv_starts[ixoer__gce - 1], s):
                    data = remove_obs(l_recv_buff[tsmsk__rzvv], *data)
                for tsmsk__rzvv in range(end[ixoer__gce - 1], nrtr__mpne):
                    data = add_obs(in_arr[tsmsk__rzvv], *data)
                output[ixoer__gce] = calc_out(minp, *data)
    return output


@register_jitable(cache=True)
def _get_var_recv_starts(on_arr, l_recv_t_buff, num_zero_starts, win):
    recv_starts = np.zeros(num_zero_starts, np.int64)
    halo_size = len(l_recv_t_buff)
    bugd__cxvk = cast_dt64_arr_to_int(on_arr)
    left_closed = False
    rtiyp__ofau = bugd__cxvk[0] - win
    if left_closed:
        rtiyp__ofau -= 1
    recv_starts[0] = halo_size
    for tsmsk__rzvv in range(0, halo_size):
        if l_recv_t_buff[tsmsk__rzvv] > rtiyp__ofau:
            recv_starts[0] = tsmsk__rzvv
            break
    for ixoer__gce in range(1, num_zero_starts):
        rtiyp__ofau = bugd__cxvk[ixoer__gce] - win
        if left_closed:
            rtiyp__ofau -= 1
        recv_starts[ixoer__gce] = halo_size
        for tsmsk__rzvv in range(recv_starts[ixoer__gce - 1], halo_size):
            if l_recv_t_buff[tsmsk__rzvv] > rtiyp__ofau:
                recv_starts[ixoer__gce] = tsmsk__rzvv
                break
    return recv_starts


@register_jitable
def roll_var_linear_generic_seq(in_arr, on_arr, win, minp, start, end,
    init_data, add_obs, remove_obs, calc_out):
    N = len(in_arr)
    output = np.empty(N, np.float64)
    data = init_data()
    for tsmsk__rzvv in range(start[0], end[0]):
        data = add_obs(in_arr[tsmsk__rzvv], *data)
    output[0] = calc_out(minp, *data)
    for ixoer__gce in range(1, N):
        s = start[ixoer__gce]
        nrtr__mpne = end[ixoer__gce]
        for tsmsk__rzvv in range(start[ixoer__gce - 1], s):
            data = remove_obs(in_arr[tsmsk__rzvv], *data)
        for tsmsk__rzvv in range(end[ixoer__gce - 1], nrtr__mpne):
            data = add_obs(in_arr[tsmsk__rzvv], *data)
        output[ixoer__gce] = calc_out(minp, *data)
    return output


def roll_variable_apply(in_arr, on_arr_dt, index_arr, win, minp, center,
    parallel, kernel_func, raw=True):
    pass


@overload(roll_variable_apply, no_unliteral=True)
def overload_roll_variable_apply(in_arr, on_arr_dt, index_arr, win, minp,
    center, parallel, kernel_func, raw=True):
    assert is_overload_constant_bool(raw)
    return roll_variable_apply_impl


def roll_variable_apply_impl(in_arr, on_arr_dt, index_arr, win, minp,
    center, parallel, kernel_func, raw=True):
    _validate_roll_var_args(minp, center)
    in_arr = prep_values(in_arr)
    win = offset_to_nanos(win)
    rank = bodo.libs.distributed_api.get_rank()
    n_pes = bodo.libs.distributed_api.get_size()
    on_arr = cast_dt64_arr_to_int(on_arr_dt)
    index_arr = fix_index_arr(index_arr)
    N = len(in_arr)
    left_closed = False
    right_closed = True
    if parallel:
        if _is_small_for_parallel_variable(on_arr, win):
            return _handle_small_data_variable_apply(in_arr, on_arr,
                index_arr, win, minp, rank, n_pes, kernel_func, raw)
        rpxj__qeap = _border_icomm_var(in_arr, on_arr, rank, n_pes, win)
        (l_recv_buff, l_recv_t_buff, r_send_req, kaxk__chxti, l_recv_req,
            tzk__ymin) = rpxj__qeap
        if raw == False:
            nlaz__bavu = _border_icomm_var(index_arr, on_arr, rank, n_pes, win)
            (l_recv_buff_idx, otty__onibg, kgza__fmrd, oew__mtts,
                vgzt__szbl, olsn__ciihj) = nlaz__bavu
    start, end = _build_indexer(on_arr, N, win, left_closed, right_closed)
    output = roll_variable_apply_seq(in_arr, on_arr, index_arr, win, minp,
        start, end, kernel_func, raw)
    if parallel:
        _border_send_wait(r_send_req, r_send_req, rank, n_pes, True, False)
        _border_send_wait(kaxk__chxti, kaxk__chxti, rank, n_pes, True, False)
        if raw == False:
            _border_send_wait(kgza__fmrd, kgza__fmrd, rank, n_pes, True, False)
            _border_send_wait(oew__mtts, oew__mtts, rank, n_pes, True, False)
        if rank != 0:
            bodo.libs.distributed_api.wait(l_recv_req, True)
            bodo.libs.distributed_api.wait(tzk__ymin, True)
            if raw == False:
                bodo.libs.distributed_api.wait(vgzt__szbl, True)
                bodo.libs.distributed_api.wait(olsn__ciihj, True)
            num_zero_starts = 0
            for ixoer__gce in range(0, N):
                if start[ixoer__gce] != 0:
                    break
                num_zero_starts += 1
            if num_zero_starts == 0:
                return output
            recv_starts = _get_var_recv_starts(on_arr, l_recv_t_buff,
                num_zero_starts, win)
            recv_left_var_compute(output, in_arr, index_arr,
                num_zero_starts, recv_starts, l_recv_buff, l_recv_buff_idx,
                minp, kernel_func, raw)
    return output


def recv_left_var_compute(output, in_arr, index_arr, num_zero_starts,
    recv_starts, l_recv_buff, l_recv_buff_idx, minp, kernel_func, raw):
    pass


@overload(recv_left_var_compute)
def overload_recv_left_var_compute(output, in_arr, index_arr,
    num_zero_starts, recv_starts, l_recv_buff, l_recv_buff_idx, minp,
    kernel_func, raw):
    assert is_overload_constant_bool(raw)
    if is_overload_true(raw):

        def impl(output, in_arr, index_arr, num_zero_starts, recv_starts,
            l_recv_buff, l_recv_buff_idx, minp, kernel_func, raw):
            for ixoer__gce in range(0, num_zero_starts):
                ien__nulny = recv_starts[ixoer__gce]
                glev__ybygp = np.concatenate((l_recv_buff[ien__nulny:],
                    in_arr[:ixoer__gce + 1]))
                if len(glev__ybygp) - np.isnan(glev__ybygp).sum() >= minp:
                    output[ixoer__gce] = kernel_func(glev__ybygp)
                else:
                    output[ixoer__gce] = np.nan
        return impl

    def impl_series(output, in_arr, index_arr, num_zero_starts, recv_starts,
        l_recv_buff, l_recv_buff_idx, minp, kernel_func, raw):
        for ixoer__gce in range(0, num_zero_starts):
            ien__nulny = recv_starts[ixoer__gce]
            glev__ybygp = np.concatenate((l_recv_buff[ien__nulny:], in_arr[
                :ixoer__gce + 1]))
            vfn__hxyr = np.concatenate((l_recv_buff_idx[ien__nulny:],
                index_arr[:ixoer__gce + 1]))
            if len(glev__ybygp) - np.isnan(glev__ybygp).sum() >= minp:
                output[ixoer__gce] = kernel_func(pd.Series(glev__ybygp,
                    vfn__hxyr))
            else:
                output[ixoer__gce] = np.nan
    return impl_series


def roll_variable_apply_seq(in_arr, on_arr, index_arr, win, minp, start,
    end, kernel_func, raw):
    pass


@overload(roll_variable_apply_seq)
def overload_roll_variable_apply_seq(in_arr, on_arr, index_arr, win, minp,
    start, end, kernel_func, raw):
    assert is_overload_constant_bool(raw)
    if is_overload_true(raw):
        return roll_variable_apply_seq_impl
    return roll_variable_apply_seq_impl_series


def roll_variable_apply_seq_impl(in_arr, on_arr, index_arr, win, minp,
    start, end, kernel_func, raw):
    N = len(in_arr)
    output = np.empty(N, dtype=np.float64)
    for ixoer__gce in range(0, N):
        s = start[ixoer__gce]
        nrtr__mpne = end[ixoer__gce]
        data = in_arr[s:nrtr__mpne]
        if nrtr__mpne - s - np.isnan(data).sum() >= minp:
            output[ixoer__gce] = kernel_func(data)
        else:
            output[ixoer__gce] = np.nan
    return output


def roll_variable_apply_seq_impl_series(in_arr, on_arr, index_arr, win,
    minp, start, end, kernel_func, raw):
    N = len(in_arr)
    output = np.empty(N, dtype=np.float64)
    for ixoer__gce in range(0, N):
        s = start[ixoer__gce]
        nrtr__mpne = end[ixoer__gce]
        data = in_arr[s:nrtr__mpne]
        if nrtr__mpne - s - np.isnan(data).sum() >= minp:
            output[ixoer__gce] = kernel_func(pd.Series(data, index_arr[s:
                nrtr__mpne]))
        else:
            output[ixoer__gce] = np.nan
    return output


@register_jitable(cache=True)
def _build_indexer(on_arr, N, win, left_closed, right_closed):
    bugd__cxvk = cast_dt64_arr_to_int(on_arr)
    start = np.empty(N, np.int64)
    end = np.empty(N, np.int64)
    start[0] = 0
    if right_closed:
        end[0] = 1
    else:
        end[0] = 0
    for ixoer__gce in range(1, N):
        otuu__ojp = bugd__cxvk[ixoer__gce]
        rtiyp__ofau = bugd__cxvk[ixoer__gce] - win
        if left_closed:
            rtiyp__ofau -= 1
        start[ixoer__gce] = ixoer__gce
        for tsmsk__rzvv in range(start[ixoer__gce - 1], ixoer__gce):
            if bugd__cxvk[tsmsk__rzvv] > rtiyp__ofau:
                start[ixoer__gce] = tsmsk__rzvv
                break
        if bugd__cxvk[end[ixoer__gce - 1]] <= otuu__ojp:
            end[ixoer__gce] = ixoer__gce + 1
        else:
            end[ixoer__gce] = end[ixoer__gce - 1]
        if not right_closed:
            end[ixoer__gce] -= 1
    return start, end


@register_jitable
def init_data_sum():
    return 0, 0.0


@register_jitable
def add_sum(val, nobs, sum_x):
    if not np.isnan(val):
        nobs += 1
        sum_x += val
    return nobs, sum_x


@register_jitable
def remove_sum(val, nobs, sum_x):
    if not np.isnan(val):
        nobs -= 1
        sum_x -= val
    return nobs, sum_x


@register_jitable
def calc_sum(minp, nobs, sum_x):
    return sum_x if nobs >= minp else np.nan


@register_jitable
def init_data_mean():
    return 0, 0.0, 0


@register_jitable
def add_mean(val, nobs, sum_x, neg_ct):
    if not np.isnan(val):
        nobs += 1
        sum_x += val
        if val < 0:
            neg_ct += 1
    return nobs, sum_x, neg_ct


@register_jitable
def remove_mean(val, nobs, sum_x, neg_ct):
    if not np.isnan(val):
        nobs -= 1
        sum_x -= val
        if val < 0:
            neg_ct -= 1
    return nobs, sum_x, neg_ct


@register_jitable
def calc_mean(minp, nobs, sum_x, neg_ct):
    if nobs >= minp:
        tetjy__dlm = sum_x / nobs
        if neg_ct == 0 and tetjy__dlm < 0.0:
            tetjy__dlm = 0
        elif neg_ct == nobs and tetjy__dlm > 0.0:
            tetjy__dlm = 0
    else:
        tetjy__dlm = np.nan
    return tetjy__dlm


@register_jitable
def init_data_var():
    return 0, 0.0, 0.0


@register_jitable
def add_var(val, nobs, mean_x, ssqdm_x):
    if not np.isnan(val):
        nobs += 1
        zhlke__leo = val - mean_x
        mean_x += zhlke__leo / nobs
        ssqdm_x += (nobs - 1) * zhlke__leo ** 2 / nobs
    return nobs, mean_x, ssqdm_x


@register_jitable
def remove_var(val, nobs, mean_x, ssqdm_x):
    if not np.isnan(val):
        nobs -= 1
        if nobs != 0:
            zhlke__leo = val - mean_x
            mean_x -= zhlke__leo / nobs
            ssqdm_x -= (nobs + 1) * zhlke__leo ** 2 / nobs
        else:
            mean_x = 0.0
            ssqdm_x = 0.0
    return nobs, mean_x, ssqdm_x


@register_jitable
def calc_var(minp, nobs, mean_x, ssqdm_x):
    hlxy__kmt = 1.0
    tetjy__dlm = np.nan
    if nobs >= minp and nobs > hlxy__kmt:
        if nobs == 1:
            tetjy__dlm = 0.0
        else:
            tetjy__dlm = ssqdm_x / (nobs - hlxy__kmt)
            if tetjy__dlm < 0.0:
                tetjy__dlm = 0.0
    return tetjy__dlm


@register_jitable
def calc_std(minp, nobs, mean_x, ssqdm_x):
    xldyy__wgx = calc_var(minp, nobs, mean_x, ssqdm_x)
    return np.sqrt(xldyy__wgx)


@register_jitable
def init_data_count():
    return 0.0,


@register_jitable
def add_count(val, count_x):
    if not np.isnan(val):
        count_x += 1.0
    return count_x,


@register_jitable
def remove_count(val, count_x):
    if not np.isnan(val):
        count_x -= 1.0
    return count_x,


@register_jitable
def calc_count(minp, count_x):
    return count_x


@register_jitable
def calc_count_var(minp, count_x):
    return count_x if count_x >= minp else np.nan


linear_kernels = {'sum': (init_data_sum, add_sum, remove_sum, calc_sum),
    'mean': (init_data_mean, add_mean, remove_mean, calc_mean), 'var': (
    init_data_var, add_var, remove_var, calc_var), 'std': (init_data_var,
    add_var, remove_var, calc_std), 'count': (init_data_count, add_count,
    remove_count, calc_count)}


def shift(in_arr, shift, parallel, default_fill_value=None):
    return


@overload(shift, jit_options={'cache': True})
def shift_overload(in_arr, shift, parallel, default_fill_value=None):
    if not isinstance(parallel, types.Literal):
        return shift_impl


def shift_impl(in_arr, shift, parallel, default_fill_value=None):
    N = len(in_arr)
    in_arr = decode_if_dict_array(in_arr)
    output = alloc_shift(N, in_arr, (-1,), fill_value=default_fill_value)
    send_right = shift > 0
    send_left = shift <= 0
    is_parallel_str = False
    if parallel:
        rank = bodo.libs.distributed_api.get_rank()
        n_pes = bodo.libs.distributed_api.get_size()
        halo_size = np.int32(abs(shift))
        if _is_small_for_parallel(N, halo_size):
            return _handle_small_data_shift(in_arr, shift, rank, n_pes,
                default_fill_value)
        rpxj__qeap = _border_icomm(in_arr, rank, n_pes, halo_size,
            send_right, send_left)
        (l_recv_buff, r_recv_buff, l_send_req, r_send_req, l_recv_req,
            hhgs__xhhj) = rpxj__qeap
        if send_right and is_str_binary_array(in_arr):
            is_parallel_str = True
            shift_left_recv(r_send_req, l_send_req, rank, n_pes, halo_size,
                l_recv_req, l_recv_buff, output)
    shift_seq(in_arr, shift, output, is_parallel_str, default_fill_value)
    if parallel:
        if send_right:
            if not is_str_binary_array(in_arr):
                shift_left_recv(r_send_req, l_send_req, rank, n_pes,
                    halo_size, l_recv_req, l_recv_buff, output)
        else:
            _border_send_wait(r_send_req, l_send_req, rank, n_pes, False, True)
            if rank != n_pes - 1:
                bodo.libs.distributed_api.wait(hhgs__xhhj, True)
                for ixoer__gce in range(0, halo_size):
                    if bodo.libs.array_kernels.isna(r_recv_buff, ixoer__gce):
                        bodo.libs.array_kernels.setna(output, N - halo_size +
                            ixoer__gce)
                        continue
                    output[N - halo_size + ixoer__gce] = r_recv_buff[ixoer__gce
                        ]
    return output


@register_jitable(cache=True)
def shift_seq(in_arr, shift, output, is_parallel_str=False,
    default_fill_value=None):
    N = len(in_arr)
    qkix__kxc = 1 if shift > 0 else -1
    shift = qkix__kxc * min(abs(shift), N)
    if shift > 0 and (not is_parallel_str or bodo.get_rank() == 0):
        if default_fill_value is None:
            bodo.libs.array_kernels.setna_slice(output, slice(None, shift))
        else:
            for ixoer__gce in range(shift):
                output[ixoer__gce
                    ] = bodo.utils.conversion.unbox_if_tz_naive_timestamp(
                    default_fill_value)
    start = max(shift, 0)
    end = min(N, N + shift)
    for ixoer__gce in range(start, end):
        if bodo.libs.array_kernels.isna(in_arr, ixoer__gce - shift):
            bodo.libs.array_kernels.setna(output, ixoer__gce)
            continue
        output[ixoer__gce] = in_arr[ixoer__gce - shift]
    if shift < 0:
        if default_fill_value is None:
            bodo.libs.array_kernels.setna_slice(output, slice(shift, None))
        else:
            for ixoer__gce in range(end, N):
                output[ixoer__gce
                    ] = bodo.utils.conversion.unbox_if_tz_naive_timestamp(
                    default_fill_value)
    return output


@register_jitable
def shift_left_recv(r_send_req, l_send_req, rank, n_pes, halo_size,
    l_recv_req, l_recv_buff, output):
    _border_send_wait(r_send_req, l_send_req, rank, n_pes, True, False)
    if rank != 0:
        bodo.libs.distributed_api.wait(l_recv_req, True)
        for ixoer__gce in range(0, halo_size):
            if bodo.libs.array_kernels.isna(l_recv_buff, ixoer__gce):
                bodo.libs.array_kernels.setna(output, ixoer__gce)
                continue
            output[ixoer__gce] = l_recv_buff[ixoer__gce]


def is_str_binary_array(arr):
    return False


@overload(is_str_binary_array)
def overload_is_str_binary_array(arr):
    if arr in [bodo.string_array_type, bodo.binary_array_type]:
        return lambda arr: True
    return lambda arr: False


def is_supported_shift_array_type(arr_type):
    return isinstance(arr_type, types.Array) and (isinstance(arr_type.dtype,
        types.Number) or arr_type.dtype in [bodo.datetime64ns, bodo.
        timedelta64ns]) or isinstance(arr_type, (bodo.IntegerArrayType,
        bodo.FloatingArrayType, bodo.DecimalArrayType, bodo.DatetimeArrayType)
        ) or arr_type in (bodo.boolean_array, bodo.datetime_date_array_type,
        bodo.string_array_type, bodo.binary_array_type, bodo.dict_str_arr_type)


def pct_change():
    return


@overload(pct_change, jit_options={'cache': True})
def pct_change_overload(in_arr, shift, parallel):
    if not isinstance(parallel, types.Literal):
        return pct_change_impl


def pct_change_impl(in_arr, shift, parallel):
    N = len(in_arr)
    send_right = shift > 0
    send_left = shift <= 0
    if parallel:
        rank = bodo.libs.distributed_api.get_rank()
        n_pes = bodo.libs.distributed_api.get_size()
        halo_size = np.int32(abs(shift))
        if _is_small_for_parallel(N, halo_size):
            return _handle_small_data_pct_change(in_arr, shift, rank, n_pes)
        rpxj__qeap = _border_icomm(in_arr, rank, n_pes, halo_size,
            send_right, send_left)
        (l_recv_buff, r_recv_buff, l_send_req, r_send_req, l_recv_req,
            hhgs__xhhj) = rpxj__qeap
    output = pct_change_seq(in_arr, shift)
    if parallel:
        if send_right:
            _border_send_wait(r_send_req, l_send_req, rank, n_pes, True, False)
            if rank != 0:
                bodo.libs.distributed_api.wait(l_recv_req, True)
                for ixoer__gce in range(0, halo_size):
                    qmd__xximd = l_recv_buff[ixoer__gce]
                    output[ixoer__gce] = (in_arr[ixoer__gce] - qmd__xximd
                        ) / qmd__xximd
        else:
            _border_send_wait(r_send_req, l_send_req, rank, n_pes, False, True)
            if rank != n_pes - 1:
                bodo.libs.distributed_api.wait(hhgs__xhhj, True)
                for ixoer__gce in range(0, halo_size):
                    qmd__xximd = r_recv_buff[ixoer__gce]
                    output[N - halo_size + ixoer__gce] = (in_arr[N -
                        halo_size + ixoer__gce] - qmd__xximd) / qmd__xximd
    return output


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def get_first_non_na(arr):
    if isinstance(arr.dtype, (types.Integer, types.Boolean)):
        zero = arr.dtype(0)
        return lambda arr: zero if len(arr) == 0 else arr[0]
    assert isinstance(arr.dtype, types.Float)
    obial__iuve = np.nan
    if arr.dtype == types.float32:
        obial__iuve = np.float32('nan')

    def impl(arr):
        for ixoer__gce in range(len(arr)):
            if not bodo.libs.array_kernels.isna(arr, ixoer__gce):
                return arr[ixoer__gce]
        return obial__iuve
    return impl


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def get_last_non_na(arr):
    if isinstance(arr.dtype, (types.Integer, types.Boolean)):
        zero = arr.dtype(0)
        return lambda arr: zero if len(arr) == 0 else arr[-1]
    assert isinstance(arr.dtype, types.Float)
    obial__iuve = np.nan
    if arr.dtype == types.float32:
        obial__iuve = np.float32('nan')

    def impl(arr):
        lzen__sfa = len(arr)
        for ixoer__gce in range(len(arr)):
            gvdwj__gyu = lzen__sfa - ixoer__gce - 1
            if not bodo.libs.array_kernels.isna(arr, gvdwj__gyu):
                return arr[gvdwj__gyu]
        return obial__iuve
    return impl


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def get_one_from_arr_dtype(arr):
    one = arr.dtype(1)
    return lambda arr: one


@register_jitable(cache=True)
def pct_change_seq(in_arr, shift):
    N = len(in_arr)
    output = alloc_pct_change(N, in_arr)
    qkix__kxc = 1 if shift > 0 else -1
    shift = qkix__kxc * min(abs(shift), N)
    if shift > 0:
        bodo.libs.array_kernels.setna_slice(output, slice(None, shift))
    else:
        bodo.libs.array_kernels.setna_slice(output, slice(shift, None))
    if shift > 0:
        iub__eufe = get_first_non_na(in_arr[:shift])
        tsz__zda = get_last_non_na(in_arr[:shift])
    else:
        iub__eufe = get_last_non_na(in_arr[:-shift])
        tsz__zda = get_first_non_na(in_arr[:-shift])
    one = get_one_from_arr_dtype(output)
    start = max(shift, 0)
    end = min(N, N + shift)
    for ixoer__gce in range(start, end):
        qmd__xximd = in_arr[ixoer__gce - shift]
        if np.isnan(qmd__xximd):
            qmd__xximd = iub__eufe
        else:
            iub__eufe = qmd__xximd
        val = in_arr[ixoer__gce]
        if np.isnan(val):
            val = tsz__zda
        else:
            tsz__zda = val
        output[ixoer__gce] = val / qmd__xximd - one
    return output


@register_jitable(cache=True)
def _border_icomm(in_arr, rank, n_pes, halo_size, send_right=True,
    send_left=False):
    bli__hzqqk = np.int32(comm_border_tag)
    l_recv_buff = bodo.utils.utils.alloc_type(halo_size, in_arr, (-1,))
    r_recv_buff = bodo.utils.utils.alloc_type(halo_size, in_arr, (-1,))
    if send_right and rank != n_pes - 1:
        r_send_req = bodo.libs.distributed_api.isend(in_arr[-halo_size:],
            halo_size, np.int32(rank + 1), bli__hzqqk, True)
    if send_right and rank != 0:
        l_recv_req = bodo.libs.distributed_api.irecv(l_recv_buff, halo_size,
            np.int32(rank - 1), bli__hzqqk, True)
    if send_left and rank != 0:
        l_send_req = bodo.libs.distributed_api.isend(in_arr[:halo_size],
            halo_size, np.int32(rank - 1), bli__hzqqk, True)
    if send_left and rank != n_pes - 1:
        hhgs__xhhj = bodo.libs.distributed_api.irecv(r_recv_buff, halo_size,
            np.int32(rank + 1), bli__hzqqk, True)
    return (l_recv_buff, r_recv_buff, l_send_req, r_send_req, l_recv_req,
        hhgs__xhhj)


@register_jitable(cache=True)
def _border_icomm_var(in_arr, on_arr, rank, n_pes, win_size):
    bli__hzqqk = np.int32(comm_border_tag)
    N = len(on_arr)
    halo_size = N
    end = on_arr[-1]
    for tsmsk__rzvv in range(-2, -N, -1):
        ectvh__hudb = on_arr[tsmsk__rzvv]
        if end - ectvh__hudb >= win_size:
            halo_size = -tsmsk__rzvv
            break
    if rank != n_pes - 1:
        bodo.libs.distributed_api.send(halo_size, np.int32(rank + 1),
            bli__hzqqk)
        r_send_req = bodo.libs.distributed_api.isend(in_arr[-halo_size:],
            np.int32(halo_size), np.int32(rank + 1), bli__hzqqk, True)
        kaxk__chxti = bodo.libs.distributed_api.isend(on_arr[-halo_size:],
            np.int32(halo_size), np.int32(rank + 1), bli__hzqqk, True)
    if rank != 0:
        halo_size = bodo.libs.distributed_api.recv(np.int64, np.int32(rank -
            1), bli__hzqqk)
        l_recv_buff = bodo.utils.utils.alloc_type(halo_size, in_arr)
        l_recv_req = bodo.libs.distributed_api.irecv(l_recv_buff, np.int32(
            halo_size), np.int32(rank - 1), bli__hzqqk, True)
        l_recv_t_buff = np.empty(halo_size, np.int64)
        tzk__ymin = bodo.libs.distributed_api.irecv(l_recv_t_buff, np.int32
            (halo_size), np.int32(rank - 1), bli__hzqqk, True)
    return (l_recv_buff, l_recv_t_buff, r_send_req, kaxk__chxti, l_recv_req,
        tzk__ymin)


@register_jitable
def _border_send_wait(r_send_req, l_send_req, rank, n_pes, right, left):
    if right and rank != n_pes - 1:
        bodo.libs.distributed_api.wait(r_send_req, True)
    if left and rank != 0:
        bodo.libs.distributed_api.wait(l_send_req, True)


@register_jitable
def _is_small_for_parallel(N, halo_size):
    xtnsu__ofjy = bodo.libs.distributed_api.dist_reduce(int(N <= 2 *
        halo_size + 1), np.int32(Reduce_Type.Sum.value))
    return xtnsu__ofjy != 0


@register_jitable
def _handle_small_data(in_arr, win, minp, center, rank, n_pes, init_data,
    add_obs, remove_obs, calc_out):
    N = len(in_arr)
    csfbw__elcw = bodo.libs.distributed_api.dist_reduce(len(in_arr), np.
        int32(Reduce_Type.Sum.value))
    jbqdg__oyiip = bodo.libs.distributed_api.gatherv(in_arr)
    if rank == 0:
        yhx__ewot, qmyvm__uvp = roll_fixed_linear_generic_seq(jbqdg__oyiip,
            win, minp, center, init_data, add_obs, remove_obs, calc_out)
    else:
        yhx__ewot = np.empty(csfbw__elcw, np.float64)
    bodo.libs.distributed_api.bcast(yhx__ewot)
    start = bodo.libs.distributed_api.dist_exscan(N, np.int32(Reduce_Type.
        Sum.value))
    end = start + N
    return yhx__ewot[start:end]


@register_jitable
def _handle_small_data_apply(in_arr, index_arr, win, minp, center, rank,
    n_pes, kernel_func, raw=True):
    N = len(in_arr)
    csfbw__elcw = bodo.libs.distributed_api.dist_reduce(len(in_arr), np.
        int32(Reduce_Type.Sum.value))
    jbqdg__oyiip = bodo.libs.distributed_api.gatherv(in_arr)
    gojm__fut = bodo.libs.distributed_api.gatherv(index_arr)
    if rank == 0:
        yhx__ewot = roll_fixed_apply_seq(jbqdg__oyiip, gojm__fut, win, minp,
            center, kernel_func, raw)
    else:
        yhx__ewot = np.empty(csfbw__elcw, np.float64)
    bodo.libs.distributed_api.bcast(yhx__ewot)
    start = bodo.libs.distributed_api.dist_exscan(N, np.int32(Reduce_Type.
        Sum.value))
    end = start + N
    return yhx__ewot[start:end]


def bcast_n_chars_if_str_binary_arr(arr):
    pass


@overload(bcast_n_chars_if_str_binary_arr)
def overload_bcast_n_chars_if_str_binary_arr(arr):
    if arr in [bodo.binary_array_type, bodo.string_array_type]:

        def impl(arr):
            return bodo.libs.distributed_api.bcast_scalar(np.int64(bodo.
                libs.str_arr_ext.num_total_chars(arr)))
        return impl
    return lambda arr: -1


@register_jitable
def _handle_small_data_shift(in_arr, shift, rank, n_pes, default_fill_value):
    N = len(in_arr)
    csfbw__elcw = bodo.libs.distributed_api.dist_reduce(len(in_arr), np.
        int32(Reduce_Type.Sum.value))
    jbqdg__oyiip = bodo.libs.distributed_api.gatherv(in_arr)
    if rank == 0:
        yhx__ewot = alloc_shift(len(jbqdg__oyiip), jbqdg__oyiip, (-1,),
            fill_value=default_fill_value)
        shift_seq(jbqdg__oyiip, shift, yhx__ewot, default_fill_value=
            default_fill_value)
        gligt__dvvs = bcast_n_chars_if_str_binary_arr(yhx__ewot)
    else:
        gligt__dvvs = bcast_n_chars_if_str_binary_arr(in_arr)
        yhx__ewot = alloc_shift(csfbw__elcw, in_arr, (gligt__dvvs,),
            fill_value=default_fill_value)
    bodo.libs.distributed_api.bcast(yhx__ewot)
    start = bodo.libs.distributed_api.dist_exscan(N, np.int32(Reduce_Type.
        Sum.value))
    end = start + N
    return yhx__ewot[start:end]


@register_jitable
def _handle_small_data_pct_change(in_arr, shift, rank, n_pes):
    N = len(in_arr)
    csfbw__elcw = bodo.libs.distributed_api.dist_reduce(N, np.int32(
        Reduce_Type.Sum.value))
    jbqdg__oyiip = bodo.libs.distributed_api.gatherv(in_arr)
    if rank == 0:
        yhx__ewot = pct_change_seq(jbqdg__oyiip, shift)
    else:
        yhx__ewot = alloc_pct_change(csfbw__elcw, in_arr)
    bodo.libs.distributed_api.bcast(yhx__ewot)
    start = bodo.libs.distributed_api.dist_exscan(N, np.int32(Reduce_Type.
        Sum.value))
    end = start + N
    return yhx__ewot[start:end]


def cast_dt64_arr_to_int(arr):
    return arr


@infer_global(cast_dt64_arr_to_int)
class DtArrToIntType(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        assert len(args) == 1
        assert args[0] == types.Array(types.NPDatetime('ns'), 1, 'C') or args[0
            ] == types.Array(types.int64, 1, 'C')
        return signature(types.Array(types.int64, 1, 'C'), *args)


@lower_builtin(cast_dt64_arr_to_int, types.Array(types.NPDatetime('ns'), 1,
    'C'))
@lower_builtin(cast_dt64_arr_to_int, types.Array(types.int64, 1, 'C'))
def lower_cast_dt64_arr_to_int(context, builder, sig, args):
    return impl_ret_borrowed(context, builder, sig.return_type, args[0])


@register_jitable
def _is_small_for_parallel_variable(on_arr, win_size):
    if len(on_arr) < 2:
        ontw__edfqu = 1
    else:
        start = on_arr[0]
        end = on_arr[-1]
        vhp__xsb = end - start
        ontw__edfqu = int(vhp__xsb <= win_size)
    xtnsu__ofjy = bodo.libs.distributed_api.dist_reduce(ontw__edfqu, np.
        int32(Reduce_Type.Sum.value))
    return xtnsu__ofjy != 0


@register_jitable
def _handle_small_data_variable(in_arr, on_arr, win, minp, rank, n_pes,
    init_data, add_obs, remove_obs, calc_out):
    N = len(in_arr)
    csfbw__elcw = bodo.libs.distributed_api.dist_reduce(N, np.int32(
        Reduce_Type.Sum.value))
    jbqdg__oyiip = bodo.libs.distributed_api.gatherv(in_arr)
    wfi__fjn = bodo.libs.distributed_api.gatherv(on_arr)
    if rank == 0:
        start, end = _build_indexer(wfi__fjn, csfbw__elcw, win, False, True)
        yhx__ewot = roll_var_linear_generic_seq(jbqdg__oyiip, wfi__fjn, win,
            minp, start, end, init_data, add_obs, remove_obs, calc_out)
    else:
        yhx__ewot = np.empty(csfbw__elcw, np.float64)
    bodo.libs.distributed_api.bcast(yhx__ewot)
    start = bodo.libs.distributed_api.dist_exscan(N, np.int32(Reduce_Type.
        Sum.value))
    end = start + N
    return yhx__ewot[start:end]


@register_jitable
def _handle_small_data_variable_apply(in_arr, on_arr, index_arr, win, minp,
    rank, n_pes, kernel_func, raw):
    N = len(in_arr)
    csfbw__elcw = bodo.libs.distributed_api.dist_reduce(N, np.int32(
        Reduce_Type.Sum.value))
    jbqdg__oyiip = bodo.libs.distributed_api.gatherv(in_arr)
    wfi__fjn = bodo.libs.distributed_api.gatherv(on_arr)
    gojm__fut = bodo.libs.distributed_api.gatherv(index_arr)
    if rank == 0:
        start, end = _build_indexer(wfi__fjn, csfbw__elcw, win, False, True)
        yhx__ewot = roll_variable_apply_seq(jbqdg__oyiip, wfi__fjn,
            gojm__fut, win, minp, start, end, kernel_func, raw)
    else:
        yhx__ewot = np.empty(csfbw__elcw, np.float64)
    bodo.libs.distributed_api.bcast(yhx__ewot)
    start = bodo.libs.distributed_api.dist_exscan(N, np.int32(Reduce_Type.
        Sum.value))
    end = start + N
    return yhx__ewot[start:end]


@register_jitable(cache=True)
def _dropna(arr):
    ztld__bjfg = len(arr)
    mfo__eish = ztld__bjfg - np.isnan(arr).sum()
    A = np.empty(mfo__eish, arr.dtype)
    xpf__jfrg = 0
    for ixoer__gce in range(ztld__bjfg):
        val = arr[ixoer__gce]
        if not np.isnan(val):
            A[xpf__jfrg] = val
            xpf__jfrg += 1
    return A


def alloc_shift(n, A, s=None, fill_value=None):
    return np.empty(n, A.dtype)


@overload(alloc_shift, no_unliteral=True)
def alloc_shift_overload(n, A, s=None, fill_value=None):
    if not isinstance(A, types.Array):
        return (lambda n, A, s=None, fill_value=None: bodo.utils.utils.
            alloc_type(n, A, s))
    if isinstance(A.dtype, types.Integer) and not isinstance(fill_value,
        types.Integer):
        return lambda n, A, s=None, fill_value=None: np.empty(n, np.float64)
    return lambda n, A, s=None, fill_value=None: np.empty(n, A.dtype)


def alloc_pct_change(n, A):
    return np.empty(n, A.dtype)


@overload(alloc_pct_change, no_unliteral=True)
def alloc_pct_change_overload(n, A):
    if isinstance(A.dtype, types.Integer):
        return lambda n, A: np.empty(n, np.float64)
    return lambda n, A: bodo.utils.utils.alloc_type(n, A, (-1,))


def prep_values(A):
    return A.astype('float64')


@overload(prep_values, no_unliteral=True)
def prep_values_overload(A):
    if A == types.Array(types.float64, 1, 'C'):
        return lambda A: A
    return lambda A: A.astype(np.float64)


@register_jitable
def _validate_roll_fixed_args(win, minp):
    if win < 0:
        raise ValueError('window must be non-negative')
    if minp < 0:
        raise ValueError('min_periods must be >= 0')
    if minp > win:
        raise ValueError('min_periods must be <= window')


@register_jitable
def _validate_roll_var_args(minp, center):
    if minp < 0:
        raise ValueError('min_periods must be >= 0')
    if center:
        raise NotImplementedError(
            'rolling: center is not implemented for datetimelike and offset based windows'
            )
