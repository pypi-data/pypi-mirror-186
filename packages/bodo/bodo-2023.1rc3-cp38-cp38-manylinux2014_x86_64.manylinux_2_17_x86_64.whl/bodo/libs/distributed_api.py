import atexit
import datetime
import sys
import time
import warnings
from collections import defaultdict
from decimal import Decimal
from enum import Enum
import llvmlite.binding as ll
import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from mpi4py import MPI
from numba.core import cgutils, ir_utils, types
from numba.core.typing import signature
from numba.core.typing.builtins import IndexValueType
from numba.core.typing.templates import AbstractTemplate, infer_global
from numba.extending import intrinsic, overload, register_jitable
from numba.parfors.array_analysis import ArrayAnalysis
import bodo
from bodo.hiframes.datetime_date_ext import datetime_date_array_type
from bodo.hiframes.datetime_timedelta_ext import datetime_timedelta_array_type
from bodo.hiframes.pd_categorical_ext import CategoricalArrayType
from bodo.libs import hdist
from bodo.libs.array_item_arr_ext import ArrayItemArrayType, np_offset_type, offset_type
from bodo.libs.binary_arr_ext import binary_array_type
from bodo.libs.bool_arr_ext import boolean_array
from bodo.libs.decimal_arr_ext import DecimalArrayType
from bodo.libs.float_arr_ext import FloatingArrayType
from bodo.libs.int_arr_ext import IntegerArrayType, set_bit_to_arr
from bodo.libs.interval_arr_ext import IntervalArrayType
from bodo.libs.map_arr_ext import MapArrayType
from bodo.libs.pd_datetime_arr_ext import DatetimeArrayType
from bodo.libs.str_arr_ext import convert_len_arr_to_offset, get_bit_bitmap, get_data_ptr, get_null_bitmap_ptr, get_offset_ptr, num_total_chars, pre_alloc_string_array, set_bit_to, string_array_type
from bodo.libs.struct_arr_ext import StructArrayType
from bodo.libs.tuple_arr_ext import TupleArrayType
from bodo.utils.typing import BodoError, BodoWarning, ColNamesMetaType, decode_if_dict_array, is_overload_false, is_overload_none, is_str_arr_type
from bodo.utils.utils import CTypeEnum, check_and_propagate_cpp_exception, empty_like_type, is_array_typ, numba_to_c_type
ll.add_symbol('dist_get_time', hdist.dist_get_time)
ll.add_symbol('get_time', hdist.get_time)
ll.add_symbol('dist_reduce', hdist.dist_reduce)
ll.add_symbol('dist_arr_reduce', hdist.dist_arr_reduce)
ll.add_symbol('dist_exscan', hdist.dist_exscan)
ll.add_symbol('dist_irecv', hdist.dist_irecv)
ll.add_symbol('dist_isend', hdist.dist_isend)
ll.add_symbol('dist_wait', hdist.dist_wait)
ll.add_symbol('dist_get_item_pointer', hdist.dist_get_item_pointer)
ll.add_symbol('get_dummy_ptr', hdist.get_dummy_ptr)
ll.add_symbol('allgather', hdist.allgather)
ll.add_symbol('oneD_reshape_shuffle', hdist.oneD_reshape_shuffle)
ll.add_symbol('permutation_int', hdist.permutation_int)
ll.add_symbol('permutation_array_index', hdist.permutation_array_index)
ll.add_symbol('c_get_rank', hdist.dist_get_rank)
ll.add_symbol('c_get_size', hdist.dist_get_size)
ll.add_symbol('c_barrier', hdist.barrier)
ll.add_symbol('c_alltoall', hdist.c_alltoall)
ll.add_symbol('c_gather_scalar', hdist.c_gather_scalar)
ll.add_symbol('c_gatherv', hdist.c_gatherv)
ll.add_symbol('c_scatterv', hdist.c_scatterv)
ll.add_symbol('c_allgatherv', hdist.c_allgatherv)
ll.add_symbol('c_bcast', hdist.c_bcast)
ll.add_symbol('c_recv', hdist.dist_recv)
ll.add_symbol('c_send', hdist.dist_send)
mpi_req_numba_type = getattr(types, 'int' + str(8 * hdist.mpi_req_num_bytes))
MPI_ROOT = 0
ANY_SOURCE = np.int32(hdist.ANY_SOURCE)


class Reduce_Type(Enum):
    Sum = 0
    Prod = 1
    Min = 2
    Max = 3
    Argmin = 4
    Argmax = 5
    Or = 6
    Concat = 7
    No_Op = 8


_get_rank = types.ExternalFunction('c_get_rank', types.int32())
_get_size = types.ExternalFunction('c_get_size', types.int32())
_barrier = types.ExternalFunction('c_barrier', types.int32())


@numba.njit
def get_rank():
    return _get_rank()


@numba.njit
def get_size():
    return _get_size()


@numba.njit
def barrier():
    _barrier()


_get_time = types.ExternalFunction('get_time', types.float64())
dist_time = types.ExternalFunction('dist_get_time', types.float64())


@overload(time.time, no_unliteral=True)
def overload_time_time():
    return lambda : _get_time()


@numba.generated_jit(nopython=True)
def get_type_enum(arr):
    arr = arr.instance_type if isinstance(arr, types.TypeRef) else arr
    dtype = arr.dtype
    if isinstance(dtype, bodo.hiframes.pd_categorical_ext.PDCategoricalDtype):
        dtype = bodo.hiframes.pd_categorical_ext.get_categories_int_type(dtype)
    typ_val = numba_to_c_type(dtype)
    return lambda arr: np.int32(typ_val)


INT_MAX = np.iinfo(np.int32).max
_send = types.ExternalFunction('c_send', types.void(types.voidptr, types.
    int32, types.int32, types.int32, types.int32))


@numba.njit
def send(val, rank, tag):
    send_arr = np.full(1, val)
    ylpi__cnnz = get_type_enum(send_arr)
    _send(send_arr.ctypes, 1, ylpi__cnnz, rank, tag)


_recv = types.ExternalFunction('c_recv', types.void(types.voidptr, types.
    int32, types.int32, types.int32, types.int32))


@numba.njit
def recv(dtype, rank, tag):
    recv_arr = np.empty(1, dtype)
    ylpi__cnnz = get_type_enum(recv_arr)
    _recv(recv_arr.ctypes, 1, ylpi__cnnz, rank, tag)
    return recv_arr[0]


_isend = types.ExternalFunction('dist_isend', mpi_req_numba_type(types.
    voidptr, types.int32, types.int32, types.int32, types.int32, types.bool_))


@numba.generated_jit(nopython=True)
def isend(arr, size, pe, tag, cond=True):
    if isinstance(arr, types.Array):

        def impl(arr, size, pe, tag, cond=True):
            ylpi__cnnz = get_type_enum(arr)
            return _isend(arr.ctypes, size, ylpi__cnnz, pe, tag, cond)
        return impl
    if isinstance(arr, (IntegerArrayType, FloatingArrayType, DecimalArrayType)
        ) or arr in (boolean_array, datetime_date_array_type):
        ylpi__cnnz = np.int32(numba_to_c_type(arr.dtype))
        zjath__elc = np.int32(numba_to_c_type(types.uint8))

        def impl_nullable(arr, size, pe, tag, cond=True):
            npug__pgufh = size + 7 >> 3
            wfxm__lju = _isend(arr._data.ctypes, size, ylpi__cnnz, pe, tag,
                cond)
            rbgw__mqn = _isend(arr._null_bitmap.ctypes, npug__pgufh,
                zjath__elc, pe, tag, cond)
            return wfxm__lju, rbgw__mqn
        return impl_nullable
    if isinstance(arr, DatetimeArrayType):

        def impl_tz_arr(arr, size, pe, tag, cond=True):
            elxig__bbg = arr._data
            ylpi__cnnz = get_type_enum(elxig__bbg)
            return _isend(elxig__bbg.ctypes, size, ylpi__cnnz, pe, tag, cond)
        return impl_tz_arr
    if is_str_arr_type(arr) or arr == binary_array_type:
        tfcjx__wvv = np.int32(numba_to_c_type(offset_type))
        zjath__elc = np.int32(numba_to_c_type(types.uint8))

        def impl_str_arr(arr, size, pe, tag, cond=True):
            arr = decode_if_dict_array(arr)
            wuaml__otnnf = np.int64(bodo.libs.str_arr_ext.num_total_chars(arr))
            send(wuaml__otnnf, pe, tag - 1)
            npug__pgufh = size + 7 >> 3
            _send(bodo.libs.str_arr_ext.get_offset_ptr(arr), size + 1,
                tfcjx__wvv, pe, tag)
            _send(bodo.libs.str_arr_ext.get_data_ptr(arr), wuaml__otnnf,
                zjath__elc, pe, tag)
            _send(bodo.libs.str_arr_ext.get_null_bitmap_ptr(arr),
                npug__pgufh, zjath__elc, pe, tag)
            return None
        return impl_str_arr
    typ_enum = numba_to_c_type(types.uint8)

    def impl_voidptr(arr, size, pe, tag, cond=True):
        return _isend(arr, size, typ_enum, pe, tag, cond)
    return impl_voidptr


_irecv = types.ExternalFunction('dist_irecv', mpi_req_numba_type(types.
    voidptr, types.int32, types.int32, types.int32, types.int32, types.bool_))


@numba.generated_jit(nopython=True)
def irecv(arr, size, pe, tag, cond=True):
    if isinstance(arr, types.Array):

        def impl(arr, size, pe, tag, cond=True):
            ylpi__cnnz = get_type_enum(arr)
            return _irecv(arr.ctypes, size, ylpi__cnnz, pe, tag, cond)
        return impl
    if isinstance(arr, (IntegerArrayType, FloatingArrayType, DecimalArrayType)
        ) or arr in (boolean_array, datetime_date_array_type):
        ylpi__cnnz = np.int32(numba_to_c_type(arr.dtype))
        zjath__elc = np.int32(numba_to_c_type(types.uint8))

        def impl_nullable(arr, size, pe, tag, cond=True):
            npug__pgufh = size + 7 >> 3
            wfxm__lju = _irecv(arr._data.ctypes, size, ylpi__cnnz, pe, tag,
                cond)
            rbgw__mqn = _irecv(arr._null_bitmap.ctypes, npug__pgufh,
                zjath__elc, pe, tag, cond)
            return wfxm__lju, rbgw__mqn
        return impl_nullable
    if isinstance(arr, DatetimeArrayType):

        def impl_tz_arr(arr, size, pe, tag, cond=True):
            elxig__bbg = arr._data
            ylpi__cnnz = get_type_enum(elxig__bbg)
            return _irecv(elxig__bbg.ctypes, size, ylpi__cnnz, pe, tag, cond)
        return impl_tz_arr
    if arr in [binary_array_type, string_array_type]:
        tfcjx__wvv = np.int32(numba_to_c_type(offset_type))
        zjath__elc = np.int32(numba_to_c_type(types.uint8))
        if arr == binary_array_type:
            axvt__ibkby = 'bodo.libs.binary_arr_ext.pre_alloc_binary_array'
        else:
            axvt__ibkby = 'bodo.libs.str_arr_ext.pre_alloc_string_array'
        flehk__ujy = f"""def impl(arr, size, pe, tag, cond=True):
            # recv the number of string characters and resize buffer to proper size
            n_chars = bodo.libs.distributed_api.recv(np.int64, pe, tag - 1)
            new_arr = {axvt__ibkby}(size, n_chars)
            bodo.libs.str_arr_ext.move_str_binary_arr_payload(arr, new_arr)

            n_bytes = (size + 7) >> 3
            bodo.libs.distributed_api._recv(
                bodo.libs.str_arr_ext.get_offset_ptr(arr),
                size + 1,
                offset_typ_enum,
                pe,
                tag,
            )
            bodo.libs.distributed_api._recv(
                bodo.libs.str_arr_ext.get_data_ptr(arr), n_chars, char_typ_enum, pe, tag
            )
            bodo.libs.distributed_api._recv(
                bodo.libs.str_arr_ext.get_null_bitmap_ptr(arr),
                n_bytes,
                char_typ_enum,
                pe,
                tag,
            )
            return None"""
        jxgg__eewvo = dict()
        exec(flehk__ujy, {'bodo': bodo, 'np': np, 'offset_typ_enum':
            tfcjx__wvv, 'char_typ_enum': zjath__elc}, jxgg__eewvo)
        impl = jxgg__eewvo['impl']
        return impl
    raise BodoError(f'irecv(): array type {arr} not supported yet')


_alltoall = types.ExternalFunction('c_alltoall', types.void(types.voidptr,
    types.voidptr, types.int32, types.int32))


@numba.njit
def alltoall(send_arr, recv_arr, count):
    assert count < INT_MAX
    ylpi__cnnz = get_type_enum(send_arr)
    _alltoall(send_arr.ctypes, recv_arr.ctypes, np.int32(count), ylpi__cnnz)


@numba.generated_jit(nopython=True)
def gather_scalar(data, allgather=False, warn_if_rep=True, root=MPI_ROOT):
    data = types.unliteral(data)
    typ_val = numba_to_c_type(data)
    dtype = data

    def gather_scalar_impl(data, allgather=False, warn_if_rep=True, root=
        MPI_ROOT):
        n_pes = bodo.libs.distributed_api.get_size()
        rank = bodo.libs.distributed_api.get_rank()
        send = np.full(1, data, dtype)
        nvs__fpt = n_pes if rank == root or allgather else 0
        twca__bwjnn = np.empty(nvs__fpt, dtype)
        c_gather_scalar(send.ctypes, twca__bwjnn.ctypes, np.int32(typ_val),
            allgather, np.int32(root))
        return twca__bwjnn
    return gather_scalar_impl


c_gather_scalar = types.ExternalFunction('c_gather_scalar', types.void(
    types.voidptr, types.voidptr, types.int32, types.bool_, types.int32))
c_gatherv = types.ExternalFunction('c_gatherv', types.void(types.voidptr,
    types.int32, types.voidptr, types.voidptr, types.voidptr, types.int32,
    types.bool_, types.int32))
c_scatterv = types.ExternalFunction('c_scatterv', types.void(types.voidptr,
    types.voidptr, types.voidptr, types.voidptr, types.int32, types.int32))


@intrinsic
def value_to_ptr(typingctx, val_tp=None):

    def codegen(context, builder, sig, args):
        feh__eismc = cgutils.alloca_once(builder, args[0].type)
        builder.store(args[0], feh__eismc)
        return builder.bitcast(feh__eismc, lir.IntType(8).as_pointer())
    return types.voidptr(val_tp), codegen


@intrinsic
def load_val_ptr(typingctx, ptr_tp, val_tp=None):

    def codegen(context, builder, sig, args):
        feh__eismc = builder.bitcast(args[0], args[1].type.as_pointer())
        return builder.load(feh__eismc)
    return val_tp(ptr_tp, val_tp), codegen


_dist_reduce = types.ExternalFunction('dist_reduce', types.void(types.
    voidptr, types.voidptr, types.int32, types.int32))
_dist_arr_reduce = types.ExternalFunction('dist_arr_reduce', types.void(
    types.voidptr, types.int64, types.int32, types.int32))


@numba.generated_jit(nopython=True)
def dist_reduce(value, reduce_op):
    if isinstance(value, types.Array):
        typ_enum = np.int32(numba_to_c_type(value.dtype))

        def impl_arr(value, reduce_op):
            A = np.ascontiguousarray(value)
            _dist_arr_reduce(A.ctypes, A.size, reduce_op, typ_enum)
            return A
        return impl_arr
    ltuz__rapeb = types.unliteral(value)
    if isinstance(ltuz__rapeb, IndexValueType):
        ltuz__rapeb = ltuz__rapeb.val_typ
        yrvvm__nzqq = [types.bool_, types.uint8, types.int8, types.uint16,
            types.int16, types.uint32, types.int32, types.float32, types.
            float64]
        if not sys.platform.startswith('win'):
            yrvvm__nzqq.append(types.int64)
            yrvvm__nzqq.append(bodo.datetime64ns)
            yrvvm__nzqq.append(bodo.timedelta64ns)
            yrvvm__nzqq.append(bodo.datetime_date_type)
            yrvvm__nzqq.append(bodo.TimeType)
        if ltuz__rapeb not in yrvvm__nzqq:
            raise BodoError('argmin/argmax not supported for type {}'.
                format(ltuz__rapeb))
    typ_enum = np.int32(numba_to_c_type(ltuz__rapeb))

    def impl(value, reduce_op):
        nlsjx__zyrcn = value_to_ptr(value)
        vezq__umri = value_to_ptr(value)
        _dist_reduce(nlsjx__zyrcn, vezq__umri, reduce_op, typ_enum)
        return load_val_ptr(vezq__umri, value)
    return impl


_dist_exscan = types.ExternalFunction('dist_exscan', types.void(types.
    voidptr, types.voidptr, types.int32, types.int32))


@numba.generated_jit(nopython=True)
def dist_exscan(value, reduce_op):
    ltuz__rapeb = types.unliteral(value)
    typ_enum = np.int32(numba_to_c_type(ltuz__rapeb))
    ggrfo__bqqqm = ltuz__rapeb(0)

    def impl(value, reduce_op):
        nlsjx__zyrcn = value_to_ptr(value)
        vezq__umri = value_to_ptr(ggrfo__bqqqm)
        _dist_exscan(nlsjx__zyrcn, vezq__umri, reduce_op, typ_enum)
        return load_val_ptr(vezq__umri, value)
    return impl


@numba.njit
def get_bit(bits, i):
    return bits[i >> 3] >> (i & 7) & 1


@numba.njit
def copy_gathered_null_bytes(null_bitmap_ptr, tmp_null_bytes,
    recv_counts_nulls, recv_counts):
    aui__jtm = 0
    bnlg__hyu = 0
    for i in range(len(recv_counts)):
        tha__bcur = recv_counts[i]
        npug__pgufh = recv_counts_nulls[i]
        ikt__bpuwl = tmp_null_bytes[aui__jtm:aui__jtm + npug__pgufh]
        for rul__hllv in range(tha__bcur):
            set_bit_to(null_bitmap_ptr, bnlg__hyu, get_bit(ikt__bpuwl,
                rul__hllv))
            bnlg__hyu += 1
        aui__jtm += npug__pgufh


@numba.generated_jit(nopython=True)
def gatherv(data, allgather=False, warn_if_rep=True, root=MPI_ROOT):
    from bodo.libs.csr_matrix_ext import CSRMatrixType
    bodo.hiframes.pd_dataframe_ext.check_runtime_cols_unsupported(data,
        'bodo.gatherv()')
    if isinstance(data, CategoricalArrayType):

        def impl_cat(data, allgather=False, warn_if_rep=True, root=MPI_ROOT):
            osuc__hehj = bodo.gatherv(data.codes, allgather, root=root)
            return bodo.hiframes.pd_categorical_ext.init_categorical_array(
                osuc__hehj, data.dtype)
        return impl_cat
    if isinstance(data, types.Array):
        typ_val = numba_to_c_type(data.dtype)

        def gatherv_impl(data, allgather=False, warn_if_rep=True, root=MPI_ROOT
            ):
            data = np.ascontiguousarray(data)
            rank = bodo.libs.distributed_api.get_rank()
            hyy__wgt = data.size
            recv_counts = gather_scalar(np.int32(hyy__wgt), allgather, root
                =root)
            fog__jsiqw = recv_counts.sum()
            jtdeh__muu = empty_like_type(fog__jsiqw, data)
            jtgl__vap = np.empty(1, np.int32)
            if rank == root or allgather:
                jtgl__vap = bodo.ir.join.calc_disp(recv_counts)
            c_gatherv(data.ctypes, np.int32(hyy__wgt), jtdeh__muu.ctypes,
                recv_counts.ctypes, jtgl__vap.ctypes, np.int32(typ_val),
                allgather, np.int32(root))
            return jtdeh__muu.reshape((-1,) + data.shape[1:])
        return gatherv_impl
    if is_str_arr_type(data):

        def gatherv_str_arr_impl(data, allgather=False, warn_if_rep=True,
            root=MPI_ROOT):
            data = decode_if_dict_array(data)
            jtdeh__muu = bodo.gatherv(data._data, allgather, warn_if_rep, root)
            return bodo.libs.str_arr_ext.init_str_arr(jtdeh__muu)
        return gatherv_str_arr_impl
    if data == binary_array_type:

        def gatherv_binary_arr_impl(data, allgather=False, warn_if_rep=True,
            root=MPI_ROOT):
            jtdeh__muu = bodo.gatherv(data._data, allgather, warn_if_rep, root)
            return bodo.libs.binary_arr_ext.init_binary_arr(jtdeh__muu)
        return gatherv_binary_arr_impl
    if data == datetime_timedelta_array_type:
        typ_val = numba_to_c_type(types.int64)
        zjath__elc = np.int32(numba_to_c_type(types.uint8))

        def gatherv_impl_int_arr(data, allgather=False, warn_if_rep=True,
            root=MPI_ROOT):
            rank = bodo.libs.distributed_api.get_rank()
            hyy__wgt = len(data)
            npug__pgufh = hyy__wgt + 7 >> 3
            recv_counts = gather_scalar(np.int32(hyy__wgt), allgather, root
                =root)
            fog__jsiqw = recv_counts.sum()
            jtdeh__muu = empty_like_type(fog__jsiqw, data)
            jtgl__vap = np.empty(1, np.int32)
            recv_counts_nulls = np.empty(1, np.int32)
            oqok__bcv = np.empty(1, np.int32)
            tmp_null_bytes = np.empty(1, np.uint8)
            if rank == root or allgather:
                jtgl__vap = bodo.ir.join.calc_disp(recv_counts)
                recv_counts_nulls = np.empty(len(recv_counts), np.int32)
                for i in range(len(recv_counts)):
                    recv_counts_nulls[i] = recv_counts[i] + 7 >> 3
                oqok__bcv = bodo.ir.join.calc_disp(recv_counts_nulls)
                tmp_null_bytes = np.empty(recv_counts_nulls.sum(), np.uint8)
            c_gatherv(data._days_data.ctypes, np.int32(hyy__wgt),
                jtdeh__muu._days_data.ctypes, recv_counts.ctypes, jtgl__vap
                .ctypes, np.int32(typ_val), allgather, np.int32(root))
            c_gatherv(data._seconds_data.ctypes, np.int32(hyy__wgt),
                jtdeh__muu._seconds_data.ctypes, recv_counts.ctypes,
                jtgl__vap.ctypes, np.int32(typ_val), allgather, np.int32(root))
            c_gatherv(data._microseconds_data.ctypes, np.int32(hyy__wgt),
                jtdeh__muu._microseconds_data.ctypes, recv_counts.ctypes,
                jtgl__vap.ctypes, np.int32(typ_val), allgather, np.int32(root))
            c_gatherv(data._null_bitmap.ctypes, np.int32(npug__pgufh),
                tmp_null_bytes.ctypes, recv_counts_nulls.ctypes, oqok__bcv.
                ctypes, zjath__elc, allgather, np.int32(root))
            copy_gathered_null_bytes(jtdeh__muu._null_bitmap.ctypes,
                tmp_null_bytes, recv_counts_nulls, recv_counts)
            return jtdeh__muu
        return gatherv_impl_int_arr
    if isinstance(data, (IntegerArrayType, FloatingArrayType,
        DecimalArrayType, bodo.TimeArrayType)) or data in (boolean_array,
        datetime_date_array_type):
        typ_val = numba_to_c_type(data.dtype)
        zjath__elc = np.int32(numba_to_c_type(types.uint8))

        def gatherv_impl_int_arr(data, allgather=False, warn_if_rep=True,
            root=MPI_ROOT):
            rank = bodo.libs.distributed_api.get_rank()
            hyy__wgt = len(data)
            npug__pgufh = hyy__wgt + 7 >> 3
            recv_counts = gather_scalar(np.int32(hyy__wgt), allgather, root
                =root)
            fog__jsiqw = recv_counts.sum()
            jtdeh__muu = empty_like_type(fog__jsiqw, data)
            jtgl__vap = np.empty(1, np.int32)
            recv_counts_nulls = np.empty(1, np.int32)
            oqok__bcv = np.empty(1, np.int32)
            tmp_null_bytes = np.empty(1, np.uint8)
            if rank == root or allgather:
                jtgl__vap = bodo.ir.join.calc_disp(recv_counts)
                recv_counts_nulls = np.empty(len(recv_counts), np.int32)
                for i in range(len(recv_counts)):
                    recv_counts_nulls[i] = recv_counts[i] + 7 >> 3
                oqok__bcv = bodo.ir.join.calc_disp(recv_counts_nulls)
                tmp_null_bytes = np.empty(recv_counts_nulls.sum(), np.uint8)
            c_gatherv(data._data.ctypes, np.int32(hyy__wgt), jtdeh__muu.
                _data.ctypes, recv_counts.ctypes, jtgl__vap.ctypes, np.
                int32(typ_val), allgather, np.int32(root))
            c_gatherv(data._null_bitmap.ctypes, np.int32(npug__pgufh),
                tmp_null_bytes.ctypes, recv_counts_nulls.ctypes, oqok__bcv.
                ctypes, zjath__elc, allgather, np.int32(root))
            copy_gathered_null_bytes(jtdeh__muu._null_bitmap.ctypes,
                tmp_null_bytes, recv_counts_nulls, recv_counts)
            return jtdeh__muu
        return gatherv_impl_int_arr
    if isinstance(data, DatetimeArrayType):
        tbct__sutf = data.tz

        def impl_pd_datetime_arr(data, allgather=False, warn_if_rep=True,
            root=MPI_ROOT):
            bsc__vlkz = bodo.gatherv(data._data, allgather, warn_if_rep, root)
            return bodo.libs.pd_datetime_arr_ext.init_pandas_datetime_array(
                bsc__vlkz, tbct__sutf)
        return impl_pd_datetime_arr
    if isinstance(data, IntervalArrayType):

        def impl_interval_arr(data, allgather=False, warn_if_rep=True, root
            =MPI_ROOT):
            vbc__hklo = bodo.gatherv(data._left, allgather, warn_if_rep, root)
            gqr__slej = bodo.gatherv(data._right, allgather, warn_if_rep, root)
            return bodo.libs.interval_arr_ext.init_interval_array(vbc__hklo,
                gqr__slej)
        return impl_interval_arr
    if isinstance(data, bodo.hiframes.pd_series_ext.SeriesType):

        def impl(data, allgather=False, warn_if_rep=True, root=MPI_ROOT):
            arr = bodo.hiframes.pd_series_ext.get_series_data(data)
            index = bodo.hiframes.pd_series_ext.get_series_index(data)
            vfc__byp = bodo.hiframes.pd_series_ext.get_series_name(data)
            out_arr = bodo.libs.distributed_api.gatherv(arr, allgather,
                warn_if_rep, root)
            oqed__vkbre = bodo.gatherv(index, allgather, warn_if_rep, root)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                oqed__vkbre, vfc__byp)
        return impl
    if isinstance(data, bodo.hiframes.pd_index_ext.RangeIndexType):
        uwq__ihm = np.iinfo(np.int64).max
        fqfo__rej = np.iinfo(np.int64).min

        def impl_range_index(data, allgather=False, warn_if_rep=True, root=
            MPI_ROOT):
            rji__dnr = data._start
            piid__vnnk = data._stop
            if len(data) == 0:
                rji__dnr = uwq__ihm
                piid__vnnk = fqfo__rej
            rji__dnr = bodo.libs.distributed_api.dist_reduce(rji__dnr, np.
                int32(Reduce_Type.Min.value))
            piid__vnnk = bodo.libs.distributed_api.dist_reduce(piid__vnnk,
                np.int32(Reduce_Type.Max.value))
            total_len = bodo.libs.distributed_api.dist_reduce(len(data), np
                .int32(Reduce_Type.Sum.value))
            if rji__dnr == uwq__ihm and piid__vnnk == fqfo__rej:
                rji__dnr = 0
                piid__vnnk = 0
            ywxif__hflb = max(0, -(-(piid__vnnk - rji__dnr) // data._step))
            if ywxif__hflb < total_len:
                piid__vnnk = rji__dnr + data._step * total_len
            if bodo.get_rank() != root and not allgather:
                rji__dnr = 0
                piid__vnnk = 0
            return bodo.hiframes.pd_index_ext.init_range_index(rji__dnr,
                piid__vnnk, data._step, data._name)
        return impl_range_index
    if bodo.hiframes.pd_index_ext.is_pd_index_type(data):
        from bodo.hiframes.pd_index_ext import PeriodIndexType
        if isinstance(data, PeriodIndexType):
            vkam__lkx = data.freq

            def impl_pd_index(data, allgather=False, warn_if_rep=True, root
                =MPI_ROOT):
                arr = bodo.libs.distributed_api.gatherv(data._data,
                    allgather, root=root)
                return bodo.hiframes.pd_index_ext.init_period_index(arr,
                    data._name, vkam__lkx)
        else:

            def impl_pd_index(data, allgather=False, warn_if_rep=True, root
                =MPI_ROOT):
                arr = bodo.libs.distributed_api.gatherv(data._data,
                    allgather, root=root)
                return bodo.utils.conversion.index_from_array(arr, data._name)
        return impl_pd_index
    if isinstance(data, bodo.hiframes.pd_multi_index_ext.MultiIndexType):

        def impl_multi_index(data, allgather=False, warn_if_rep=True, root=
            MPI_ROOT):
            jtdeh__muu = bodo.gatherv(data._data, allgather, root=root)
            return bodo.hiframes.pd_multi_index_ext.init_multi_index(jtdeh__muu
                , data._names, data._name)
        return impl_multi_index
    if isinstance(data, bodo.hiframes.table.TableType):
        ysgjg__kjl = {'bodo': bodo, 'get_table_block': bodo.hiframes.table.
            get_table_block, 'ensure_column_unboxed': bodo.hiframes.table.
            ensure_column_unboxed, 'set_table_block': bodo.hiframes.table.
            set_table_block, 'set_table_len': bodo.hiframes.table.
            set_table_len, 'alloc_list_like': bodo.hiframes.table.
            alloc_list_like, 'init_table': bodo.hiframes.table.init_table,
            'decode_if_dict_ary': bodo.hiframes.table.init_table}
        flehk__ujy = (
            f'def impl_table(data, allgather=False, warn_if_rep=True, root={MPI_ROOT}):\n'
            )
        flehk__ujy += '  T = data\n'
        flehk__ujy += '  T2 = init_table(T, True)\n'
        mapr__otf = bodo.hiframes.table.get_init_table_output_type(data, True)
        gyza__wvg = (bodo.string_array_type in data.type_to_blk and bodo.
            dict_str_arr_type in data.type_to_blk)
        if gyza__wvg:
            flehk__ujy += (bodo.hiframes.table.
                gen_str_and_dict_enc_cols_to_one_block_fn_txt(data,
                mapr__otf, ysgjg__kjl, True))
        for qnlu__xqr, riegx__qiggl in data.type_to_blk.items():
            if gyza__wvg and qnlu__xqr in (bodo.string_array_type, bodo.
                dict_str_arr_type):
                continue
            elif qnlu__xqr == bodo.dict_str_arr_type:
                assert bodo.string_array_type in mapr__otf.type_to_blk, 'Error in gatherv: If encoded string type is present in the input, then non-encoded string type should be present in the output'
                oypbh__lftnl = mapr__otf.type_to_blk[bodo.string_array_type]
            else:
                assert qnlu__xqr in mapr__otf.type_to_blk, 'Error in gatherv: All non-encoded string types present in the input should be present in the output'
                oypbh__lftnl = mapr__otf.type_to_blk[qnlu__xqr]
            ysgjg__kjl[f'arr_inds_{riegx__qiggl}'] = np.array(data.
                block_to_arr_ind[riegx__qiggl], dtype=np.int64)
            flehk__ujy += (
                f'  arr_list_{riegx__qiggl} = get_table_block(T, {riegx__qiggl})\n'
                )
            flehk__ujy += f"""  out_arr_list_{riegx__qiggl} = alloc_list_like(arr_list_{riegx__qiggl}, len(arr_list_{riegx__qiggl}), True)
"""
            flehk__ujy += f'  for i in range(len(arr_list_{riegx__qiggl})):\n'
            flehk__ujy += (
                f'    arr_ind_{riegx__qiggl} = arr_inds_{riegx__qiggl}[i]\n')
            flehk__ujy += f"""    ensure_column_unboxed(T, arr_list_{riegx__qiggl}, i, arr_ind_{riegx__qiggl})
"""
            flehk__ujy += f"""    out_arr_{riegx__qiggl} = bodo.gatherv(arr_list_{riegx__qiggl}[i], allgather, warn_if_rep, root)
"""
            flehk__ujy += (
                f'    out_arr_list_{riegx__qiggl}[i] = out_arr_{riegx__qiggl}\n'
                )
            flehk__ujy += f"""  T2 = set_table_block(T2, out_arr_list_{riegx__qiggl}, {oypbh__lftnl})
"""
        flehk__ujy += (
            f'  length = T._len if bodo.get_rank() == root or allgather else 0\n'
            )
        flehk__ujy += f'  T2 = set_table_len(T2, length)\n'
        flehk__ujy += f'  return T2\n'
        jxgg__eewvo = {}
        exec(flehk__ujy, ysgjg__kjl, jxgg__eewvo)
        aezxs__kxg = jxgg__eewvo['impl_table']
        return aezxs__kxg
    if isinstance(data, bodo.hiframes.pd_dataframe_ext.DataFrameType):
        ura__wbj = len(data.columns)
        if ura__wbj == 0:
            upp__tiypn = ColNamesMetaType(())

            def impl(data, allgather=False, warn_if_rep=True, root=MPI_ROOT):
                index = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(data
                    )
                lktgf__ufptp = bodo.gatherv(index, allgather, warn_if_rep, root
                    )
                return bodo.hiframes.pd_dataframe_ext.init_dataframe((),
                    lktgf__ufptp, upp__tiypn)
            return impl
        jswp__bawxq = ', '.join(f'g_data_{i}' for i in range(ura__wbj))
        flehk__ujy = (
            'def impl_df(data, allgather=False, warn_if_rep=True, root={}):\n'
            .format(MPI_ROOT))
        if data.is_table_format:
            from bodo.transforms.distributed_analysis import Distribution
            wxa__kip = bodo.hiframes.pd_dataframe_ext.DataFrameType(data.
                data, data.index, data.columns, Distribution.REP, True)
            jswp__bawxq = 'T2'
            flehk__ujy += (
                '  T = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(data)\n'
                )
            flehk__ujy += (
                '  T2 = bodo.gatherv(T, allgather, warn_if_rep, root)\n')
        else:
            for i in range(ura__wbj):
                flehk__ujy += (
                    """  data_{} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(data, {})
"""
                    .format(i, i))
                flehk__ujy += (
                    '  g_data_{} = bodo.gatherv(data_{}, allgather, warn_if_rep, root)\n'
                    .format(i, i))
        flehk__ujy += (
            '  index = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(data)\n'
            )
        flehk__ujy += (
            '  g_index = bodo.gatherv(index, allgather, warn_if_rep, root)\n')
        flehk__ujy += (
            """  return bodo.hiframes.pd_dataframe_ext.init_dataframe(({},), g_index, __col_name_meta_value_gatherv_with_cols)
"""
            .format(jswp__bawxq))
        jxgg__eewvo = {}
        ysgjg__kjl = {'bodo': bodo,
            '__col_name_meta_value_gatherv_with_cols': ColNamesMetaType(
            data.columns)}
        exec(flehk__ujy, ysgjg__kjl, jxgg__eewvo)
        axgdo__yblsk = jxgg__eewvo['impl_df']
        return axgdo__yblsk
    if isinstance(data, ArrayItemArrayType):
        urmeo__yjhkj = np.int32(numba_to_c_type(types.int32))
        zjath__elc = np.int32(numba_to_c_type(types.uint8))

        def gatherv_array_item_arr_impl(data, allgather=False, warn_if_rep=
            True, root=MPI_ROOT):
            rank = bodo.libs.distributed_api.get_rank()
            oyda__fyadq = bodo.libs.array_item_arr_ext.get_offsets(data)
            elxig__bbg = bodo.libs.array_item_arr_ext.get_data(data)
            elxig__bbg = elxig__bbg[:oyda__fyadq[-1]]
            imtv__hwkkn = bodo.libs.array_item_arr_ext.get_null_bitmap(data)
            hyy__wgt = len(data)
            dkvu__wwark = np.empty(hyy__wgt, np.uint32)
            npug__pgufh = hyy__wgt + 7 >> 3
            for i in range(hyy__wgt):
                dkvu__wwark[i] = oyda__fyadq[i + 1] - oyda__fyadq[i]
            recv_counts = gather_scalar(np.int32(hyy__wgt), allgather, root
                =root)
            fog__jsiqw = recv_counts.sum()
            jtgl__vap = np.empty(1, np.int32)
            recv_counts_nulls = np.empty(1, np.int32)
            oqok__bcv = np.empty(1, np.int32)
            tmp_null_bytes = np.empty(1, np.uint8)
            if rank == root or allgather:
                jtgl__vap = bodo.ir.join.calc_disp(recv_counts)
                recv_counts_nulls = np.empty(len(recv_counts), np.int32)
                for lat__ujto in range(len(recv_counts)):
                    recv_counts_nulls[lat__ujto] = recv_counts[lat__ujto
                        ] + 7 >> 3
                oqok__bcv = bodo.ir.join.calc_disp(recv_counts_nulls)
                tmp_null_bytes = np.empty(recv_counts_nulls.sum(), np.uint8)
            iumx__agwq = np.empty(fog__jsiqw + 1, np.uint32)
            kxcql__wob = bodo.gatherv(elxig__bbg, allgather, warn_if_rep, root)
            bflr__vidp = np.empty(fog__jsiqw + 7 >> 3, np.uint8)
            c_gatherv(dkvu__wwark.ctypes, np.int32(hyy__wgt), iumx__agwq.
                ctypes, recv_counts.ctypes, jtgl__vap.ctypes, urmeo__yjhkj,
                allgather, np.int32(root))
            c_gatherv(imtv__hwkkn.ctypes, np.int32(npug__pgufh),
                tmp_null_bytes.ctypes, recv_counts_nulls.ctypes, oqok__bcv.
                ctypes, zjath__elc, allgather, np.int32(root))
            dummy_use(data)
            vby__swnn = np.empty(fog__jsiqw + 1, np.uint64)
            convert_len_arr_to_offset(iumx__agwq.ctypes, vby__swnn.ctypes,
                fog__jsiqw)
            copy_gathered_null_bytes(bflr__vidp.ctypes, tmp_null_bytes,
                recv_counts_nulls, recv_counts)
            out_arr = bodo.libs.array_item_arr_ext.init_array_item_array(
                fog__jsiqw, kxcql__wob, vby__swnn, bflr__vidp)
            return out_arr
        return gatherv_array_item_arr_impl
    if isinstance(data, StructArrayType):
        uxigh__qamz = data.names
        zjath__elc = np.int32(numba_to_c_type(types.uint8))

        def impl_struct_arr(data, allgather=False, warn_if_rep=True, root=
            MPI_ROOT):
            vjyt__ytwo = bodo.libs.struct_arr_ext.get_data(data)
            loxb__mlx = bodo.libs.struct_arr_ext.get_null_bitmap(data)
            ojuq__kbjzz = bodo.gatherv(vjyt__ytwo, allgather=allgather,
                root=root)
            rank = bodo.libs.distributed_api.get_rank()
            hyy__wgt = len(data)
            npug__pgufh = hyy__wgt + 7 >> 3
            recv_counts = gather_scalar(np.int32(hyy__wgt), allgather, root
                =root)
            fog__jsiqw = recv_counts.sum()
            avff__angk = np.empty(fog__jsiqw + 7 >> 3, np.uint8)
            recv_counts_nulls = np.empty(1, np.int32)
            oqok__bcv = np.empty(1, np.int32)
            tmp_null_bytes = np.empty(1, np.uint8)
            if rank == root or allgather:
                recv_counts_nulls = np.empty(len(recv_counts), np.int32)
                for i in range(len(recv_counts)):
                    recv_counts_nulls[i] = recv_counts[i] + 7 >> 3
                oqok__bcv = bodo.ir.join.calc_disp(recv_counts_nulls)
                tmp_null_bytes = np.empty(recv_counts_nulls.sum(), np.uint8)
            c_gatherv(loxb__mlx.ctypes, np.int32(npug__pgufh),
                tmp_null_bytes.ctypes, recv_counts_nulls.ctypes, oqok__bcv.
                ctypes, zjath__elc, allgather, np.int32(root))
            copy_gathered_null_bytes(avff__angk.ctypes, tmp_null_bytes,
                recv_counts_nulls, recv_counts)
            return bodo.libs.struct_arr_ext.init_struct_arr(ojuq__kbjzz,
                avff__angk, uxigh__qamz)
        return impl_struct_arr
    if data == binary_array_type:

        def impl_bin_arr(data, allgather=False, warn_if_rep=True, root=MPI_ROOT
            ):
            jtdeh__muu = bodo.gatherv(data._data, allgather, warn_if_rep, root)
            return bodo.libs.binary_arr_ext.init_binary_arr(jtdeh__muu)
        return impl_bin_arr
    if isinstance(data, TupleArrayType):

        def impl_tuple_arr(data, allgather=False, warn_if_rep=True, root=
            MPI_ROOT):
            jtdeh__muu = bodo.gatherv(data._data, allgather, warn_if_rep, root)
            return bodo.libs.tuple_arr_ext.init_tuple_arr(jtdeh__muu)
        return impl_tuple_arr
    if isinstance(data, MapArrayType):

        def impl_map_arr(data, allgather=False, warn_if_rep=True, root=MPI_ROOT
            ):
            jtdeh__muu = bodo.gatherv(data._data, allgather, warn_if_rep, root)
            return bodo.libs.map_arr_ext.init_map_arr(jtdeh__muu)
        return impl_map_arr
    if isinstance(data, CSRMatrixType):

        def impl_csr_matrix(data, allgather=False, warn_if_rep=True, root=
            MPI_ROOT):
            jtdeh__muu = bodo.gatherv(data.data, allgather, warn_if_rep, root)
            oqo__bjfr = bodo.gatherv(data.indices, allgather, warn_if_rep, root
                )
            zrpxd__hcph = bodo.gatherv(data.indptr, allgather, warn_if_rep,
                root)
            tlje__pzfnm = gather_scalar(data.shape[0], allgather, root=root)
            nlfg__glq = tlje__pzfnm.sum()
            ura__wbj = bodo.libs.distributed_api.dist_reduce(data.shape[1],
                np.int32(Reduce_Type.Max.value))
            ijv__peua = np.empty(nlfg__glq + 1, np.int64)
            oqo__bjfr = oqo__bjfr.astype(np.int64)
            ijv__peua[0] = 0
            jwpi__odowi = 1
            iujq__ecd = 0
            for vzxnw__admka in tlje__pzfnm:
                for tov__rlch in range(vzxnw__admka):
                    cocjv__ncq = zrpxd__hcph[iujq__ecd + 1] - zrpxd__hcph[
                        iujq__ecd]
                    ijv__peua[jwpi__odowi] = ijv__peua[jwpi__odowi - 1
                        ] + cocjv__ncq
                    jwpi__odowi += 1
                    iujq__ecd += 1
                iujq__ecd += 1
            return bodo.libs.csr_matrix_ext.init_csr_matrix(jtdeh__muu,
                oqo__bjfr, ijv__peua, (nlfg__glq, ura__wbj))
        return impl_csr_matrix
    if isinstance(data, types.BaseTuple):
        flehk__ujy = (
            'def impl_tuple(data, allgather=False, warn_if_rep=True, root={}):\n'
            .format(MPI_ROOT))
        flehk__ujy += '  return ({}{})\n'.format(', '.join(
            'bodo.gatherv(data[{}], allgather, warn_if_rep, root)'.format(i
            ) for i in range(len(data))), ',' if len(data) > 0 else '')
        jxgg__eewvo = {}
        exec(flehk__ujy, {'bodo': bodo}, jxgg__eewvo)
        xlk__chyw = jxgg__eewvo['impl_tuple']
        return xlk__chyw
    if data is types.none:
        return (lambda data, allgather=False, warn_if_rep=True, root=
            MPI_ROOT: None)
    try:
        import bodosql
        from bodosql.context_ext import BodoSQLContextType
    except ImportError as loude__clpx:
        BodoSQLContextType = None
    if BodoSQLContextType is not None and isinstance(data, BodoSQLContextType):
        flehk__ujy = f"""def impl_bodosql_context(data, allgather=False, warn_if_rep=True, root={MPI_ROOT}):
"""
        hcfi__igcvi = ', '.join([f"'{vfc__byp}'" for vfc__byp in data.names])
        lusx__nzdv = ', '.join([
            f'bodo.gatherv(data.dataframes[{i}], allgather, warn_if_rep, root)'
             for i in range(len(data.dataframes))])
        flehk__ujy += f"""  return bodosql.context_ext.init_sql_context(({hcfi__igcvi}, ), ({lusx__nzdv}, ), data.catalog)
"""
        jxgg__eewvo = {}
        exec(flehk__ujy, {'bodo': bodo, 'bodosql': bodosql}, jxgg__eewvo)
        lxtq__yusb = jxgg__eewvo['impl_bodosql_context']
        return lxtq__yusb
    try:
        import bodosql
        from bodosql import TablePathType
    except ImportError as loude__clpx:
        TablePathType = None
    if TablePathType is not None and isinstance(data, TablePathType):
        flehk__ujy = f"""def impl_table_path(data, allgather=False, warn_if_rep=True, root={MPI_ROOT}):
"""
        flehk__ujy += f'  return data\n'
        jxgg__eewvo = {}
        exec(flehk__ujy, {}, jxgg__eewvo)
        vhx__jyex = jxgg__eewvo['impl_table_path']
        return vhx__jyex
    raise BodoError('gatherv() not available for {}'.format(data))


@numba.generated_jit(nopython=True)
def rebalance(data, dests=None, random=False, random_seed=None, parallel=False
    ):
    bodo.hiframes.pd_dataframe_ext.check_runtime_cols_unsupported(data,
        'bodo.rebalance()')
    flehk__ujy = (
        'def impl(data, dests=None, random=False, random_seed=None, parallel=False):\n'
        )
    flehk__ujy += '    if random:\n'
    flehk__ujy += '        if random_seed is None:\n'
    flehk__ujy += '            random = 1\n'
    flehk__ujy += '        else:\n'
    flehk__ujy += '            random = 2\n'
    flehk__ujy += '    if random_seed is None:\n'
    flehk__ujy += '        random_seed = -1\n'
    if isinstance(data, bodo.hiframes.pd_dataframe_ext.DataFrameType):
        xybbz__ljvpv = data
        ura__wbj = len(xybbz__ljvpv.columns)
        for i in range(ura__wbj):
            flehk__ujy += f"""    data_{i} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(data, {i})
"""
        flehk__ujy += """    ind_arr = bodo.utils.conversion.index_to_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(data))
"""
        jswp__bawxq = ', '.join(f'data_{i}' for i in range(ura__wbj))
        flehk__ujy += ('    info_list_total = [{}, array_to_info(ind_arr)]\n'
            .format(', '.join('array_to_info(data_{})'.format(kyy__mzur) for
            kyy__mzur in range(ura__wbj))))
        flehk__ujy += (
            '    table_total = arr_info_list_to_table(info_list_total)\n')
        flehk__ujy += '    if dests is None:\n'
        flehk__ujy += """        out_table = shuffle_renormalization(table_total, random, random_seed, parallel)
"""
        flehk__ujy += '    else:\n'
        flehk__ujy += """        out_table = shuffle_renormalization_group(table_total, random, random_seed, parallel, len(dests), np.array(dests, dtype=np.int32).ctypes)
"""
        for ozzwd__bzqx in range(ura__wbj):
            flehk__ujy += (
                """    out_arr_{0} = info_to_array(info_from_table(out_table, {0}), data_{0})
"""
                .format(ozzwd__bzqx))
        flehk__ujy += (
            """    out_arr_index = info_to_array(info_from_table(out_table, {}), ind_arr)
"""
            .format(ura__wbj))
        flehk__ujy += '    delete_table(out_table)\n'
        flehk__ujy += '    if parallel:\n'
        flehk__ujy += '        delete_table(table_total)\n'
        jswp__bawxq = ', '.join('out_arr_{}'.format(i) for i in range(ura__wbj)
            )
        index = 'bodo.utils.conversion.index_from_array(out_arr_index)'
        flehk__ujy += (
            """    return bodo.hiframes.pd_dataframe_ext.init_dataframe(({},), {}, __col_name_meta_value_rebalance)
"""
            .format(jswp__bawxq, index))
    elif isinstance(data, bodo.hiframes.pd_series_ext.SeriesType):
        flehk__ujy += (
            '    data_0 = bodo.hiframes.pd_series_ext.get_series_data(data)\n')
        flehk__ujy += """    ind_arr = bodo.utils.conversion.index_to_array(bodo.hiframes.pd_series_ext.get_series_index(data))
"""
        flehk__ujy += (
            '    name = bodo.hiframes.pd_series_ext.get_series_name(data)\n')
        flehk__ujy += """    table_total = arr_info_list_to_table([array_to_info(data_0), array_to_info(ind_arr)])
"""
        flehk__ujy += '    if dests is None:\n'
        flehk__ujy += """        out_table = shuffle_renormalization(table_total, random, random_seed, parallel)
"""
        flehk__ujy += '    else:\n'
        flehk__ujy += """        out_table = shuffle_renormalization_group(table_total, random, random_seed, parallel, len(dests), np.array(dests, dtype=np.int32).ctypes)
"""
        flehk__ujy += (
            '    out_arr_0 = info_to_array(info_from_table(out_table, 0), data_0)\n'
            )
        flehk__ujy += (
            '    out_arr_index = info_to_array(info_from_table(out_table, 1), ind_arr)\n'
            )
        flehk__ujy += '    delete_table(out_table)\n'
        flehk__ujy += '    if parallel:\n'
        flehk__ujy += '        delete_table(table_total)\n'
        index = 'bodo.utils.conversion.index_from_array(out_arr_index)'
        flehk__ujy += f"""    return bodo.hiframes.pd_series_ext.init_series(out_arr_0, {index}, name)
"""
    elif isinstance(data, types.Array):
        assert is_overload_false(random
            ), 'Call random_shuffle instead of rebalance'
        flehk__ujy += '    if not parallel:\n'
        flehk__ujy += '        return data\n'
        flehk__ujy += """    dim0_global_size = bodo.libs.distributed_api.dist_reduce(data.shape[0], np.int32(bodo.libs.distributed_api.Reduce_Type.Sum.value))
"""
        flehk__ujy += '    if dests is None:\n'
        flehk__ujy += """        dim0_local_size = bodo.libs.distributed_api.get_node_portion(dim0_global_size, bodo.get_size(), bodo.get_rank())
"""
        flehk__ujy += '    elif bodo.get_rank() not in dests:\n'
        flehk__ujy += '        dim0_local_size = 0\n'
        flehk__ujy += '    else:\n'
        flehk__ujy += """        dim0_local_size = bodo.libs.distributed_api.get_node_portion(dim0_global_size, len(dests), dests.index(bodo.get_rank()))
"""
        flehk__ujy += """    out = np.empty((dim0_local_size,) + tuple(data.shape[1:]), dtype=data.dtype)
"""
        flehk__ujy += """    bodo.libs.distributed_api.dist_oneD_reshape_shuffle(out, data, dim0_global_size, dests)
"""
        flehk__ujy += '    return out\n'
    elif bodo.utils.utils.is_array_typ(data, False):
        flehk__ujy += (
            '    table_total = arr_info_list_to_table([array_to_info(data)])\n'
            )
        flehk__ujy += '    if dests is None:\n'
        flehk__ujy += """        out_table = shuffle_renormalization(table_total, random, random_seed, parallel)
"""
        flehk__ujy += '    else:\n'
        flehk__ujy += """        out_table = shuffle_renormalization_group(table_total, random, random_seed, parallel, len(dests), np.array(dests, dtype=np.int32).ctypes)
"""
        flehk__ujy += (
            '    out_arr = info_to_array(info_from_table(out_table, 0), data)\n'
            )
        flehk__ujy += '    delete_table(out_table)\n'
        flehk__ujy += '    if parallel:\n'
        flehk__ujy += '        delete_table(table_total)\n'
        flehk__ujy += '    return out_arr\n'
    else:
        raise BodoError(f'Type {data} not supported for bodo.rebalance')
    jxgg__eewvo = {}
    ysgjg__kjl = {'np': np, 'bodo': bodo, 'array_to_info': bodo.libs.array.
        array_to_info, 'shuffle_renormalization': bodo.libs.array.
        shuffle_renormalization, 'shuffle_renormalization_group': bodo.libs
        .array.shuffle_renormalization_group, 'arr_info_list_to_table':
        bodo.libs.array.arr_info_list_to_table, 'info_from_table': bodo.
        libs.array.info_from_table, 'info_to_array': bodo.libs.array.
        info_to_array, 'delete_table': bodo.libs.array.delete_table}
    if isinstance(data, bodo.hiframes.pd_dataframe_ext.DataFrameType):
        ysgjg__kjl.update({'__col_name_meta_value_rebalance':
            ColNamesMetaType(xybbz__ljvpv.columns)})
    exec(flehk__ujy, ysgjg__kjl, jxgg__eewvo)
    impl = jxgg__eewvo['impl']
    return impl


@numba.generated_jit(nopython=True)
def random_shuffle(data, seed=None, dests=None, n_samples=None, parallel=False
    ):
    flehk__ujy = (
        'def impl(data, seed=None, dests=None, n_samples=None, parallel=False):\n'
        )
    if isinstance(data, types.Array):
        if not is_overload_none(dests):
            raise BodoError('not supported')
        flehk__ujy += '    if seed is None:\n'
        flehk__ujy += """        seed = bodo.libs.distributed_api.bcast_scalar(np.random.randint(0, 2**31))
"""
        flehk__ujy += '    np.random.seed(seed)\n'
        flehk__ujy += '    if not parallel:\n'
        flehk__ujy += '        data = data.copy()\n'
        flehk__ujy += '        np.random.shuffle(data)\n'
        if not is_overload_none(n_samples):
            flehk__ujy += '        data = data[:n_samples]\n'
        flehk__ujy += '        return data\n'
        flehk__ujy += '    else:\n'
        flehk__ujy += """        dim0_global_size = bodo.libs.distributed_api.dist_reduce(data.shape[0], np.int32(bodo.libs.distributed_api.Reduce_Type.Sum.value))
"""
        flehk__ujy += '        permutation = np.arange(dim0_global_size)\n'
        flehk__ujy += '        np.random.shuffle(permutation)\n'
        if not is_overload_none(n_samples):
            flehk__ujy += (
                '        n_samples = max(0, min(dim0_global_size, n_samples))\n'
                )
        else:
            flehk__ujy += '        n_samples = dim0_global_size\n'
        flehk__ujy += """        dim0_local_size = bodo.libs.distributed_api.get_node_portion(dim0_global_size, bodo.get_size(), bodo.get_rank())
"""
        flehk__ujy += """        dim0_output_size = bodo.libs.distributed_api.get_node_portion(n_samples, bodo.get_size(), bodo.get_rank())
"""
        flehk__ujy += """        output = np.empty((dim0_output_size,) + tuple(data.shape[1:]), dtype=data.dtype)
"""
        flehk__ujy += (
            '        dtype_size = bodo.io.np_io.get_dtype_size(data.dtype)\n')
        flehk__ujy += """        bodo.libs.distributed_api.dist_permutation_array_index(output, dim0_global_size, dtype_size, data, permutation, len(permutation), n_samples)
"""
        flehk__ujy += '        return output\n'
    else:
        flehk__ujy += """    output = bodo.libs.distributed_api.rebalance(data, dests=dests, random=True, random_seed=seed, parallel=parallel)
"""
        if not is_overload_none(n_samples):
            flehk__ujy += """    local_n_samples = bodo.libs.distributed_api.get_node_portion(n_samples, bodo.get_size(), bodo.get_rank())
"""
            flehk__ujy += '    output = output[:local_n_samples]\n'
        flehk__ujy += '    return output\n'
    jxgg__eewvo = {}
    exec(flehk__ujy, {'np': np, 'bodo': bodo}, jxgg__eewvo)
    impl = jxgg__eewvo['impl']
    return impl


@numba.generated_jit(nopython=True)
def allgatherv(data, warn_if_rep=True, root=MPI_ROOT):
    return lambda data, warn_if_rep=True, root=MPI_ROOT: gatherv(data, True,
        warn_if_rep, root)


@numba.njit
def get_scatter_null_bytes_buff(null_bitmap_ptr, sendcounts, sendcounts_nulls):
    if bodo.get_rank() != MPI_ROOT:
        return np.empty(1, np.uint8)
    cmswb__dmo = np.empty(sendcounts_nulls.sum(), np.uint8)
    aui__jtm = 0
    bnlg__hyu = 0
    for geby__wmu in range(len(sendcounts)):
        tha__bcur = sendcounts[geby__wmu]
        npug__pgufh = sendcounts_nulls[geby__wmu]
        ikt__bpuwl = cmswb__dmo[aui__jtm:aui__jtm + npug__pgufh]
        for rul__hllv in range(tha__bcur):
            set_bit_to_arr(ikt__bpuwl, rul__hllv, get_bit_bitmap(
                null_bitmap_ptr, bnlg__hyu))
            bnlg__hyu += 1
        aui__jtm += npug__pgufh
    return cmswb__dmo


def _bcast_dtype(data, root=MPI_ROOT):
    try:
        from mpi4py import MPI
    except:
        raise BodoError('mpi4py is required for scatterv')
    xqx__ptpm = MPI.COMM_WORLD
    data = xqx__ptpm.bcast(data, root)
    return data


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def _get_scatterv_send_counts(send_counts, n_pes, n):
    if not is_overload_none(send_counts):
        return lambda send_counts, n_pes, n: send_counts

    def impl(send_counts, n_pes, n):
        send_counts = np.empty(n_pes, np.int32)
        for i in range(n_pes):
            send_counts[i] = get_node_portion(n, n_pes, i)
        return send_counts
    return impl


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def _scatterv_np(data, send_counts=None, warn_if_dist=True):
    typ_val = numba_to_c_type(data.dtype)
    jzv__inbrz = data.ndim
    dtype = data.dtype
    if dtype == types.NPDatetime('ns'):
        dtype = np.dtype('datetime64[ns]')
    elif dtype == types.NPTimedelta('ns'):
        dtype = np.dtype('timedelta64[ns]')
    tcfgh__qnk = (0,) * jzv__inbrz

    def scatterv_arr_impl(data, send_counts=None, warn_if_dist=True):
        rank = bodo.libs.distributed_api.get_rank()
        n_pes = bodo.libs.distributed_api.get_size()
        dcz__wjrt = np.ascontiguousarray(data)
        kll__zuhbv = data.ctypes
        ijl__zro = tcfgh__qnk
        if rank == MPI_ROOT:
            ijl__zro = dcz__wjrt.shape
        ijl__zro = bcast_tuple(ijl__zro)
        fgnah__dnllr = get_tuple_prod(ijl__zro[1:])
        send_counts = _get_scatterv_send_counts(send_counts, n_pes, ijl__zro[0]
            )
        send_counts *= fgnah__dnllr
        hyy__wgt = send_counts[rank]
        lkyh__eaw = np.empty(hyy__wgt, dtype)
        jtgl__vap = bodo.ir.join.calc_disp(send_counts)
        c_scatterv(kll__zuhbv, send_counts.ctypes, jtgl__vap.ctypes,
            lkyh__eaw.ctypes, np.int32(hyy__wgt), np.int32(typ_val))
        return lkyh__eaw.reshape((-1,) + ijl__zro[1:])
    return scatterv_arr_impl


def _get_name_value_for_type(name_typ):
    assert isinstance(name_typ, (types.UnicodeType, types.StringLiteral)
        ) or name_typ == types.none
    return None if name_typ == types.none else '_' + str(ir_utils.next_label())


def get_value_for_type(dtype):
    if isinstance(dtype, types.Array):
        return np.zeros((1,) * dtype.ndim, numba.np.numpy_support.as_dtype(
            dtype.dtype))
    if dtype == string_array_type:
        return pd.array(['A'], 'string')
    if dtype == bodo.dict_str_arr_type:
        import pyarrow as pa
        return pa.array(['a'], type=pa.dictionary(pa.int32(), pa.string()))
    if dtype == binary_array_type:
        return np.array([b'A'], dtype=object)
    if isinstance(dtype, IntegerArrayType):
        rxvwx__oof = '{}Int{}'.format('' if dtype.dtype.signed else 'U',
            dtype.dtype.bitwidth)
        return pd.array([3], rxvwx__oof)
    if isinstance(dtype, FloatingArrayType):
        rxvwx__oof = 'Float{}'.format(dtype.dtype.bitwidth)
        return pd.array([3.0], rxvwx__oof)
    if dtype == boolean_array:
        return pd.array([True], 'boolean')
    if isinstance(dtype, DecimalArrayType):
        return np.array([Decimal('32.1')])
    if dtype == datetime_date_array_type:
        return np.array([datetime.date(2011, 8, 9)])
    if dtype == datetime_timedelta_array_type:
        return np.array([datetime.timedelta(33)])
    if bodo.hiframes.pd_index_ext.is_pd_index_type(dtype):
        vfc__byp = _get_name_value_for_type(dtype.name_typ)
        if isinstance(dtype, bodo.hiframes.pd_index_ext.RangeIndexType):
            return pd.RangeIndex(1, name=vfc__byp)
        pzlg__bebf = bodo.utils.typing.get_index_data_arr_types(dtype)[0]
        arr = get_value_for_type(pzlg__bebf)
        return pd.Index(arr, name=vfc__byp)
    if isinstance(dtype, bodo.hiframes.pd_multi_index_ext.MultiIndexType):
        import pyarrow as pa
        vfc__byp = _get_name_value_for_type(dtype.name_typ)
        uxigh__qamz = tuple(_get_name_value_for_type(t) for t in dtype.
            names_typ)
        dlzn__oqfyt = tuple(get_value_for_type(t) for t in dtype.array_types)
        dlzn__oqfyt = tuple(a.to_numpy(False) if isinstance(a, pa.Array) else
            a for a in dlzn__oqfyt)
        val = pd.MultiIndex.from_arrays(dlzn__oqfyt, names=uxigh__qamz)
        val.name = vfc__byp
        return val
    if isinstance(dtype, bodo.hiframes.pd_series_ext.SeriesType):
        vfc__byp = _get_name_value_for_type(dtype.name_typ)
        arr = get_value_for_type(dtype.data)
        index = get_value_for_type(dtype.index)
        return pd.Series(arr, index, name=vfc__byp)
    if isinstance(dtype, bodo.hiframes.pd_dataframe_ext.DataFrameType):
        dlzn__oqfyt = tuple(get_value_for_type(t) for t in dtype.data)
        index = get_value_for_type(dtype.index)
        return pd.DataFrame({vfc__byp: arr for vfc__byp, arr in zip(dtype.
            columns, dlzn__oqfyt)}, index)
    if isinstance(dtype, CategoricalArrayType):
        return pd.Categorical.from_codes([0], dtype.dtype.categories)
    if isinstance(dtype, types.BaseTuple):
        return tuple(get_value_for_type(t) for t in dtype.types)
    if isinstance(dtype, ArrayItemArrayType):
        return pd.Series([get_value_for_type(dtype.dtype),
            get_value_for_type(dtype.dtype)]).values
    if isinstance(dtype, IntervalArrayType):
        pzlg__bebf = get_value_for_type(dtype.arr_type)
        return pd.arrays.IntervalArray([pd.Interval(pzlg__bebf[0],
            pzlg__bebf[0])])
    raise BodoError(f'get_value_for_type(dtype): Missing data type {dtype}')


def scatterv(data, send_counts=None, warn_if_dist=True):
    rank = bodo.libs.distributed_api.get_rank()
    if rank != MPI_ROOT and data is not None:
        warnings.warn(BodoWarning(
            "bodo.scatterv(): A non-None value for 'data' was found on a rank other than the root. This data won't be sent to any other ranks and will be overwritten with data from rank 0."
            ))
    dtype = bodo.typeof(data)
    dtype = _bcast_dtype(dtype)
    if rank != MPI_ROOT:
        data = get_value_for_type(dtype)
    return scatterv_impl(data, send_counts)


@overload(scatterv)
def scatterv_overload(data, send_counts=None, warn_if_dist=True):
    bodo.hiframes.pd_dataframe_ext.check_runtime_cols_unsupported(data,
        'bodo.scatterv()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(data,
        'bodo.scatterv()')
    return lambda data, send_counts=None, warn_if_dist=True: scatterv_impl(data
        , send_counts)


@numba.generated_jit(nopython=True)
def scatterv_impl(data, send_counts=None, warn_if_dist=True):
    if isinstance(data, types.Array):
        return lambda data, send_counts=None, warn_if_dist=True: _scatterv_np(
            data, send_counts)
    if data in (string_array_type, binary_array_type):
        urmeo__yjhkj = np.int32(numba_to_c_type(types.int32))
        zjath__elc = np.int32(numba_to_c_type(types.uint8))
        if data == binary_array_type:
            axvt__ibkby = 'bodo.libs.binary_arr_ext.pre_alloc_binary_array'
        else:
            axvt__ibkby = 'bodo.libs.str_arr_ext.pre_alloc_string_array'
        flehk__ujy = f"""def impl(
            data, send_counts=None, warn_if_dist=True
        ):  # pragma: no cover
            rank = bodo.libs.distributed_api.get_rank()
            n_pes = bodo.libs.distributed_api.get_size()
            n_all = bodo.libs.distributed_api.bcast_scalar(len(data))

            # convert offsets to lengths of strings
            send_arr_lens = np.empty(
                len(data), np.uint32
            )  # XXX offset type is offset_type, lengths for comm are uint32
            for i in range(len(data)):
                send_arr_lens[i] = bodo.libs.str_arr_ext.get_str_arr_item_length(
                    data, i
                )

            # ------- calculate buffer counts -------

            send_counts = bodo.libs.distributed_api._get_scatterv_send_counts(send_counts, n_pes, n_all)

            # displacements
            displs = bodo.ir.join.calc_disp(send_counts)

            # compute send counts for characters
            send_counts_char = np.empty(n_pes, np.int32)
            if rank == 0:
                curr_str = 0
                for i in range(n_pes):
                    c = 0
                    for _ in range(send_counts[i]):
                        c += send_arr_lens[curr_str]
                        curr_str += 1
                    send_counts_char[i] = c

            bodo.libs.distributed_api.bcast(send_counts_char)

            # displacements for characters
            displs_char = bodo.ir.join.calc_disp(send_counts_char)

            # compute send counts for nulls
            send_counts_nulls = np.empty(n_pes, np.int32)
            for i in range(n_pes):
                send_counts_nulls[i] = (send_counts[i] + 7) >> 3

            # displacements for nulls
            displs_nulls = bodo.ir.join.calc_disp(send_counts_nulls)

            # alloc output array
            n_loc = send_counts[rank]  # total number of elements on this PE
            n_loc_char = send_counts_char[rank]
            recv_arr = {axvt__ibkby}(n_loc, n_loc_char)

            # ----- string lengths -----------

            recv_lens = np.empty(n_loc, np.uint32)
            bodo.libs.distributed_api.c_scatterv(
                send_arr_lens.ctypes,
                send_counts.ctypes,
                displs.ctypes,
                recv_lens.ctypes,
                np.int32(n_loc),
                int32_typ_enum,
            )

            # TODO: don't hardcode offset type. Also, if offset is 32 bit we can
            # use the same buffer
            bodo.libs.str_arr_ext.convert_len_arr_to_offset(recv_lens.ctypes, bodo.libs.str_arr_ext.get_offset_ptr(recv_arr), n_loc)

            # ----- string characters -----------

            bodo.libs.distributed_api.c_scatterv(
                bodo.libs.str_arr_ext.get_data_ptr(data),
                send_counts_char.ctypes,
                displs_char.ctypes,
                bodo.libs.str_arr_ext.get_data_ptr(recv_arr),
                np.int32(n_loc_char),
                char_typ_enum,
            )

            # ----------- null bitmap -------------

            n_recv_bytes = (n_loc + 7) >> 3

            send_null_bitmap = bodo.libs.distributed_api.get_scatter_null_bytes_buff(
                bodo.libs.str_arr_ext.get_null_bitmap_ptr(data), send_counts, send_counts_nulls
            )

            bodo.libs.distributed_api.c_scatterv(
                send_null_bitmap.ctypes,
                send_counts_nulls.ctypes,
                displs_nulls.ctypes,
                bodo.libs.str_arr_ext.get_null_bitmap_ptr(recv_arr),
                np.int32(n_recv_bytes),
                char_typ_enum,
            )

            return recv_arr"""
        jxgg__eewvo = dict()
        exec(flehk__ujy, {'bodo': bodo, 'np': np, 'int32_typ_enum':
            urmeo__yjhkj, 'char_typ_enum': zjath__elc,
            'decode_if_dict_array': decode_if_dict_array}, jxgg__eewvo)
        impl = jxgg__eewvo['impl']
        return impl
    if isinstance(data, ArrayItemArrayType):
        urmeo__yjhkj = np.int32(numba_to_c_type(types.int32))
        zjath__elc = np.int32(numba_to_c_type(types.uint8))

        def scatterv_array_item_impl(data, send_counts=None, warn_if_dist=True
            ):
            sew__iizd = bodo.libs.array_item_arr_ext.get_offsets(data)
            zbu__sgow = bodo.libs.array_item_arr_ext.get_data(data)
            zbu__sgow = zbu__sgow[:sew__iizd[-1]]
            wyob__tycrg = bodo.libs.array_item_arr_ext.get_null_bitmap(data)
            rank = bodo.libs.distributed_api.get_rank()
            n_pes = bodo.libs.distributed_api.get_size()
            hheim__crvug = bcast_scalar(len(data))
            zlnn__esstp = np.empty(len(data), np.uint32)
            for i in range(len(data)):
                zlnn__esstp[i] = sew__iizd[i + 1] - sew__iizd[i]
            send_counts = _get_scatterv_send_counts(send_counts, n_pes,
                hheim__crvug)
            jtgl__vap = bodo.ir.join.calc_disp(send_counts)
            msiur__wrz = np.empty(n_pes, np.int32)
            if rank == 0:
                jfmmz__zmlxa = 0
                for i in range(n_pes):
                    wwbnh__fsnpn = 0
                    for tov__rlch in range(send_counts[i]):
                        wwbnh__fsnpn += zlnn__esstp[jfmmz__zmlxa]
                        jfmmz__zmlxa += 1
                    msiur__wrz[i] = wwbnh__fsnpn
            bcast(msiur__wrz)
            ghgdd__xlv = np.empty(n_pes, np.int32)
            for i in range(n_pes):
                ghgdd__xlv[i] = send_counts[i] + 7 >> 3
            oqok__bcv = bodo.ir.join.calc_disp(ghgdd__xlv)
            hyy__wgt = send_counts[rank]
            ezg__fgahy = np.empty(hyy__wgt + 1, np_offset_type)
            otax__cliax = bodo.libs.distributed_api.scatterv_impl(zbu__sgow,
                msiur__wrz)
            qnlp__ecgy = hyy__wgt + 7 >> 3
            qwz__shbjg = np.empty(qnlp__ecgy, np.uint8)
            dsx__rxol = np.empty(hyy__wgt, np.uint32)
            c_scatterv(zlnn__esstp.ctypes, send_counts.ctypes, jtgl__vap.
                ctypes, dsx__rxol.ctypes, np.int32(hyy__wgt), urmeo__yjhkj)
            convert_len_arr_to_offset(dsx__rxol.ctypes, ezg__fgahy.ctypes,
                hyy__wgt)
            yjc__eymo = get_scatter_null_bytes_buff(wyob__tycrg.ctypes,
                send_counts, ghgdd__xlv)
            c_scatterv(yjc__eymo.ctypes, ghgdd__xlv.ctypes, oqok__bcv.
                ctypes, qwz__shbjg.ctypes, np.int32(qnlp__ecgy), zjath__elc)
            return bodo.libs.array_item_arr_ext.init_array_item_array(hyy__wgt,
                otax__cliax, ezg__fgahy, qwz__shbjg)
        return scatterv_array_item_impl
    if isinstance(data, (IntegerArrayType, FloatingArrayType, DecimalArrayType)
        ) or data in (boolean_array, datetime_date_array_type):
        zjath__elc = np.int32(numba_to_c_type(types.uint8))
        if isinstance(data, IntegerArrayType):
            epns__wjnxm = bodo.libs.int_arr_ext.init_integer_array
        if isinstance(data, FloatingArrayType):
            epns__wjnxm = bodo.libs.float_arr_ext.init_float_array
        if isinstance(data, DecimalArrayType):
            precision = data.precision
            scale = data.scale
            epns__wjnxm = numba.njit(no_cpython_wrapper=True)(lambda d, b:
                bodo.libs.decimal_arr_ext.init_decimal_array(d, b,
                precision, scale))
        if data == boolean_array:
            epns__wjnxm = bodo.libs.bool_arr_ext.init_bool_array
        if data == datetime_date_array_type:
            epns__wjnxm = (bodo.hiframes.datetime_date_ext.
                init_datetime_date_array)

        def scatterv_impl_int_arr(data, send_counts=None, warn_if_dist=True):
            n_pes = bodo.libs.distributed_api.get_size()
            dcz__wjrt = data._data
            loxb__mlx = data._null_bitmap
            twx__goyp = len(dcz__wjrt)
            kkf__zzwg = _scatterv_np(dcz__wjrt, send_counts)
            hheim__crvug = bcast_scalar(twx__goyp)
            deyg__arfx = len(kkf__zzwg) + 7 >> 3
            pctml__dcndp = np.empty(deyg__arfx, np.uint8)
            send_counts = _get_scatterv_send_counts(send_counts, n_pes,
                hheim__crvug)
            ghgdd__xlv = np.empty(n_pes, np.int32)
            for i in range(n_pes):
                ghgdd__xlv[i] = send_counts[i] + 7 >> 3
            oqok__bcv = bodo.ir.join.calc_disp(ghgdd__xlv)
            yjc__eymo = get_scatter_null_bytes_buff(loxb__mlx.ctypes,
                send_counts, ghgdd__xlv)
            c_scatterv(yjc__eymo.ctypes, ghgdd__xlv.ctypes, oqok__bcv.
                ctypes, pctml__dcndp.ctypes, np.int32(deyg__arfx), zjath__elc)
            return epns__wjnxm(kkf__zzwg, pctml__dcndp)
        return scatterv_impl_int_arr
    if isinstance(data, IntervalArrayType):

        def impl_interval_arr(data, send_counts=None, warn_if_dist=True):
            sklb__nag = bodo.libs.distributed_api.scatterv_impl(data._left,
                send_counts)
            crxf__nhpa = bodo.libs.distributed_api.scatterv_impl(data.
                _right, send_counts)
            return bodo.libs.interval_arr_ext.init_interval_array(sklb__nag,
                crxf__nhpa)
        return impl_interval_arr
    if isinstance(data, bodo.hiframes.pd_index_ext.RangeIndexType):

        def impl_range_index(data, send_counts=None, warn_if_dist=True):
            rank = bodo.libs.distributed_api.get_rank()
            n_pes = bodo.libs.distributed_api.get_size()
            rji__dnr = data._start
            piid__vnnk = data._stop
            zizzs__eik = data._step
            vfc__byp = data._name
            vfc__byp = bcast_scalar(vfc__byp)
            rji__dnr = bcast_scalar(rji__dnr)
            piid__vnnk = bcast_scalar(piid__vnnk)
            zizzs__eik = bcast_scalar(zizzs__eik)
            qbp__xlo = bodo.libs.array_kernels.calc_nitems(rji__dnr,
                piid__vnnk, zizzs__eik)
            chunk_start = bodo.libs.distributed_api.get_start(qbp__xlo,
                n_pes, rank)
            oif__kdq = bodo.libs.distributed_api.get_node_portion(qbp__xlo,
                n_pes, rank)
            zrv__zulum = rji__dnr + zizzs__eik * chunk_start
            nhbel__ohw = rji__dnr + zizzs__eik * (chunk_start + oif__kdq)
            nhbel__ohw = min(nhbel__ohw, piid__vnnk)
            return bodo.hiframes.pd_index_ext.init_range_index(zrv__zulum,
                nhbel__ohw, zizzs__eik, vfc__byp)
        return impl_range_index
    if isinstance(data, bodo.hiframes.pd_index_ext.PeriodIndexType):
        vkam__lkx = data.freq

        def impl_period_index(data, send_counts=None, warn_if_dist=True):
            dcz__wjrt = data._data
            vfc__byp = data._name
            vfc__byp = bcast_scalar(vfc__byp)
            arr = bodo.libs.distributed_api.scatterv_impl(dcz__wjrt,
                send_counts)
            return bodo.hiframes.pd_index_ext.init_period_index(arr,
                vfc__byp, vkam__lkx)
        return impl_period_index
    if bodo.hiframes.pd_index_ext.is_pd_index_type(data):

        def impl_pd_index(data, send_counts=None, warn_if_dist=True):
            dcz__wjrt = data._data
            vfc__byp = data._name
            vfc__byp = bcast_scalar(vfc__byp)
            arr = bodo.libs.distributed_api.scatterv_impl(dcz__wjrt,
                send_counts)
            return bodo.utils.conversion.index_from_array(arr, vfc__byp)
        return impl_pd_index
    if isinstance(data, bodo.hiframes.pd_multi_index_ext.MultiIndexType):

        def impl_multi_index(data, send_counts=None, warn_if_dist=True):
            jtdeh__muu = bodo.libs.distributed_api.scatterv_impl(data._data,
                send_counts)
            vfc__byp = bcast_scalar(data._name)
            uxigh__qamz = bcast_tuple(data._names)
            return bodo.hiframes.pd_multi_index_ext.init_multi_index(jtdeh__muu
                , uxigh__qamz, vfc__byp)
        return impl_multi_index
    if isinstance(data, bodo.hiframes.pd_series_ext.SeriesType):

        def impl_series(data, send_counts=None, warn_if_dist=True):
            arr = bodo.hiframes.pd_series_ext.get_series_data(data)
            index = bodo.hiframes.pd_series_ext.get_series_index(data)
            vfc__byp = bodo.hiframes.pd_series_ext.get_series_name(data)
            ekini__slwvs = bcast_scalar(vfc__byp)
            out_arr = bodo.libs.distributed_api.scatterv_impl(arr, send_counts)
            oqed__vkbre = bodo.libs.distributed_api.scatterv_impl(index,
                send_counts)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                oqed__vkbre, ekini__slwvs)
        return impl_series
    if isinstance(data, bodo.hiframes.pd_dataframe_ext.DataFrameType):
        ura__wbj = len(data.columns)
        apze__cpp = ColNamesMetaType(data.columns)
        flehk__ujy = (
            'def impl_df(data, send_counts=None, warn_if_dist=True):\n')
        if data.is_table_format:
            flehk__ujy += (
                '  table = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(data)\n'
                )
            flehk__ujy += """  g_table = bodo.libs.distributed_api.scatterv_impl(table, send_counts)
"""
            jswp__bawxq = 'g_table'
        else:
            for i in range(ura__wbj):
                flehk__ujy += f"""  data_{i} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(data, {i})
"""
                flehk__ujy += f"""  g_data_{i} = bodo.libs.distributed_api.scatterv_impl(data_{i}, send_counts)
"""
            jswp__bawxq = ', '.join(f'g_data_{i}' for i in range(ura__wbj))
        flehk__ujy += (
            '  index = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(data)\n'
            )
        flehk__ujy += (
            '  g_index = bodo.libs.distributed_api.scatterv_impl(index, send_counts)\n'
            )
        flehk__ujy += f"""  return bodo.hiframes.pd_dataframe_ext.init_dataframe(({jswp__bawxq},), g_index, __col_name_meta_scaterv_impl)
"""
        jxgg__eewvo = {}
        exec(flehk__ujy, {'bodo': bodo, '__col_name_meta_scaterv_impl':
            apze__cpp}, jxgg__eewvo)
        axgdo__yblsk = jxgg__eewvo['impl_df']
        return axgdo__yblsk
    if isinstance(data, bodo.TableType):
        flehk__ujy = (
            'def impl_table(data, send_counts=None, warn_if_dist=True):\n')
        flehk__ujy += '  T = data\n'
        flehk__ujy += '  T2 = init_table(T, False)\n'
        flehk__ujy += '  l = 0\n'
        ysgjg__kjl = {}
        for znzo__gkoki in data.type_to_blk.values():
            ysgjg__kjl[f'arr_inds_{znzo__gkoki}'] = np.array(data.
                block_to_arr_ind[znzo__gkoki], dtype=np.int64)
            flehk__ujy += (
                f'  arr_list_{znzo__gkoki} = get_table_block(T, {znzo__gkoki})\n'
                )
            flehk__ujy += f"""  out_arr_list_{znzo__gkoki} = alloc_list_like(arr_list_{znzo__gkoki}, len(arr_list_{znzo__gkoki}), False)
"""
            flehk__ujy += f'  for i in range(len(arr_list_{znzo__gkoki})):\n'
            flehk__ujy += (
                f'    arr_ind_{znzo__gkoki} = arr_inds_{znzo__gkoki}[i]\n')
            flehk__ujy += f"""    ensure_column_unboxed(T, arr_list_{znzo__gkoki}, i, arr_ind_{znzo__gkoki})
"""
            flehk__ujy += f"""    out_arr_{znzo__gkoki} = bodo.libs.distributed_api.scatterv_impl(arr_list_{znzo__gkoki}[i], send_counts)
"""
            flehk__ujy += (
                f'    out_arr_list_{znzo__gkoki}[i] = out_arr_{znzo__gkoki}\n')
            flehk__ujy += f'    l = len(out_arr_{znzo__gkoki})\n'
            flehk__ujy += (
                f'  T2 = set_table_block(T2, out_arr_list_{znzo__gkoki}, {znzo__gkoki})\n'
                )
        flehk__ujy += f'  T2 = set_table_len(T2, l)\n'
        flehk__ujy += f'  return T2\n'
        ysgjg__kjl.update({'bodo': bodo, 'init_table': bodo.hiframes.table.
            init_table, 'get_table_block': bodo.hiframes.table.
            get_table_block, 'ensure_column_unboxed': bodo.hiframes.table.
            ensure_column_unboxed, 'set_table_block': bodo.hiframes.table.
            set_table_block, 'set_table_len': bodo.hiframes.table.
            set_table_len, 'alloc_list_like': bodo.hiframes.table.
            alloc_list_like})
        jxgg__eewvo = {}
        exec(flehk__ujy, ysgjg__kjl, jxgg__eewvo)
        return jxgg__eewvo['impl_table']
    if data == bodo.dict_str_arr_type:

        def impl_dict_arr(data, send_counts=None, warn_if_dist=True):
            if bodo.get_rank() == 0:
                rahew__rki = data._data
                bodo.libs.distributed_api.bcast_scalar(len(rahew__rki))
                bodo.libs.distributed_api.bcast_scalar(np.int64(bodo.libs.
                    str_arr_ext.num_total_chars(rahew__rki)))
            else:
                ywxif__hflb = bodo.libs.distributed_api.bcast_scalar(0)
                wuaml__otnnf = bodo.libs.distributed_api.bcast_scalar(0)
                rahew__rki = bodo.libs.str_arr_ext.pre_alloc_string_array(
                    ywxif__hflb, wuaml__otnnf)
            bodo.libs.distributed_api.bcast(rahew__rki)
            leat__pkft = bodo.libs.distributed_api.scatterv_impl(data.
                _indices, send_counts)
            return bodo.libs.dict_arr_ext.init_dict_arr(rahew__rki,
                leat__pkft, True, data._has_deduped_local_dictionary)
        return impl_dict_arr
    if isinstance(data, CategoricalArrayType):

        def impl_cat(data, send_counts=None, warn_if_dist=True):
            osuc__hehj = bodo.libs.distributed_api.scatterv_impl(data.codes,
                send_counts)
            return bodo.hiframes.pd_categorical_ext.init_categorical_array(
                osuc__hehj, data.dtype)
        return impl_cat
    if isinstance(data, types.BaseTuple):
        flehk__ujy = (
            'def impl_tuple(data, send_counts=None, warn_if_dist=True):\n')
        flehk__ujy += '  return ({}{})\n'.format(', '.join(
            f'bodo.libs.distributed_api.scatterv_impl(data[{i}], send_counts)'
             for i in range(len(data))), ',' if len(data) > 0 else '')
        jxgg__eewvo = {}
        exec(flehk__ujy, {'bodo': bodo}, jxgg__eewvo)
        xlk__chyw = jxgg__eewvo['impl_tuple']
        return xlk__chyw
    if data is types.none:
        return lambda data, send_counts=None, warn_if_dist=True: None
    raise BodoError('scatterv() not available for {}'.format(data))


@intrinsic
def cptr_to_voidptr(typingctx, cptr_tp=None):

    def codegen(context, builder, sig, args):
        return builder.bitcast(args[0], lir.IntType(8).as_pointer())
    return types.voidptr(cptr_tp), codegen


def bcast(data, root=MPI_ROOT):
    return


@overload(bcast, no_unliteral=True)
def bcast_overload(data, root=MPI_ROOT):
    if isinstance(data, types.Array):

        def bcast_impl(data, root=MPI_ROOT):
            typ_enum = get_type_enum(data)
            count = data.size
            assert count < INT_MAX
            c_bcast(data.ctypes, np.int32(count), typ_enum, np.array([-1]).
                ctypes, 0, np.int32(root))
            return
        return bcast_impl
    if isinstance(data, DecimalArrayType):

        def bcast_decimal_arr(data, root=MPI_ROOT):
            count = data._data.size
            assert count < INT_MAX
            c_bcast(data._data.ctypes, np.int32(count), CTypeEnum.Int128.
                value, np.array([-1]).ctypes, 0, np.int32(root))
            bcast(data._null_bitmap, root)
            return
        return bcast_decimal_arr
    if isinstance(data, (IntegerArrayType, FloatingArrayType)) or data in (
        boolean_array, datetime_date_array_type):

        def bcast_impl_int_arr(data, root=MPI_ROOT):
            bcast(data._data, root)
            bcast(data._null_bitmap, root)
            return
        return bcast_impl_int_arr
    if isinstance(data, DatetimeArrayType):

        def bcast_impl_tz_arr(data, root=MPI_ROOT):
            bcast(data._data, root)
            return
        return bcast_impl_tz_arr
    if is_str_arr_type(data) or data == binary_array_type:
        tfcjx__wvv = np.int32(numba_to_c_type(offset_type))
        zjath__elc = np.int32(numba_to_c_type(types.uint8))

        def bcast_str_impl(data, root=MPI_ROOT):
            data = decode_if_dict_array(data)
            hyy__wgt = len(data)
            zelpg__jkb = num_total_chars(data)
            assert hyy__wgt < INT_MAX
            assert zelpg__jkb < INT_MAX
            lofbf__hkmbn = get_offset_ptr(data)
            kll__zuhbv = get_data_ptr(data)
            null_bitmap_ptr = get_null_bitmap_ptr(data)
            npug__pgufh = hyy__wgt + 7 >> 3
            c_bcast(lofbf__hkmbn, np.int32(hyy__wgt + 1), tfcjx__wvv, np.
                array([-1]).ctypes, 0, np.int32(root))
            c_bcast(kll__zuhbv, np.int32(zelpg__jkb), zjath__elc, np.array(
                [-1]).ctypes, 0, np.int32(root))
            c_bcast(null_bitmap_ptr, np.int32(npug__pgufh), zjath__elc, np.
                array([-1]).ctypes, 0, np.int32(root))
        return bcast_str_impl


c_bcast = types.ExternalFunction('c_bcast', types.void(types.voidptr, types
    .int32, types.int32, types.voidptr, types.int32, types.int32))


@numba.generated_jit(nopython=True)
def bcast_scalar(val, root=MPI_ROOT):
    val = types.unliteral(val)
    if not (isinstance(val, (types.Integer, types.Float)) or val in [bodo.
        datetime64ns, bodo.timedelta64ns, bodo.string_type, types.none,
        types.bool_]):
        raise BodoError(
            f'bcast_scalar requires an argument of type Integer, Float, datetime64ns, timedelta64ns, string, None, or Bool. Found type {val}'
            )
    if val == types.none:
        return lambda val, root=MPI_ROOT: None
    if val == bodo.string_type:
        zjath__elc = np.int32(numba_to_c_type(types.uint8))

        def impl_str(val, root=MPI_ROOT):
            rank = bodo.libs.distributed_api.get_rank()
            if rank != root:
                kpgbr__tqd = 0
                hey__spvkw = np.empty(0, np.uint8).ctypes
            else:
                hey__spvkw, kpgbr__tqd = (bodo.libs.str_ext.
                    unicode_to_utf8_and_len(val))
            kpgbr__tqd = bodo.libs.distributed_api.bcast_scalar(kpgbr__tqd,
                root)
            if rank != root:
                rll__zhd = np.empty(kpgbr__tqd + 1, np.uint8)
                rll__zhd[kpgbr__tqd] = 0
                hey__spvkw = rll__zhd.ctypes
            c_bcast(hey__spvkw, np.int32(kpgbr__tqd), zjath__elc, np.array(
                [-1]).ctypes, 0, np.int32(root))
            return bodo.libs.str_arr_ext.decode_utf8(hey__spvkw, kpgbr__tqd)
        return impl_str
    typ_val = numba_to_c_type(val)
    flehk__ujy = f"""def bcast_scalar_impl(val, root={MPI_ROOT}):
  send = np.empty(1, dtype)
  send[0] = val
  c_bcast(send.ctypes, np.int32(1), np.int32({typ_val}), np.array([-1]).ctypes, 0, np.int32(root))
  return send[0]
"""
    dtype = numba.np.numpy_support.as_dtype(val)
    jxgg__eewvo = {}
    exec(flehk__ujy, {'bodo': bodo, 'np': np, 'c_bcast': c_bcast, 'dtype':
        dtype}, jxgg__eewvo)
    wdnqj__knaxg = jxgg__eewvo['bcast_scalar_impl']
    return wdnqj__knaxg


@numba.generated_jit(nopython=True)
def bcast_tuple(val, root=MPI_ROOT):
    assert isinstance(val, types.BaseTuple
        ), 'Internal Error: Argument to bcast tuple must be of type tuple'
    xumj__ymiz = len(val)
    flehk__ujy = f'def bcast_tuple_impl(val, root={MPI_ROOT}):\n'
    flehk__ujy += '  return ({}{})'.format(','.join(
        'bcast_scalar(val[{}], root)'.format(i) for i in range(xumj__ymiz)),
        ',' if xumj__ymiz else '')
    jxgg__eewvo = {}
    exec(flehk__ujy, {'bcast_scalar': bcast_scalar}, jxgg__eewvo)
    fkk__rextc = jxgg__eewvo['bcast_tuple_impl']
    return fkk__rextc


def prealloc_str_for_bcast(arr, root=MPI_ROOT):
    return arr


@overload(prealloc_str_for_bcast, no_unliteral=True)
def prealloc_str_for_bcast_overload(arr, root=MPI_ROOT):
    if arr == string_array_type:

        def prealloc_impl(arr, root=MPI_ROOT):
            rank = bodo.libs.distributed_api.get_rank()
            hyy__wgt = bcast_scalar(len(arr), root)
            xewn__zku = bcast_scalar(np.int64(num_total_chars(arr)), root)
            if rank != root:
                arr = pre_alloc_string_array(hyy__wgt, xewn__zku)
            return arr
        return prealloc_impl
    return lambda arr, root=MPI_ROOT: arr


def get_local_slice(idx, arr_start, total_len):
    return idx


@overload(get_local_slice, no_unliteral=True, jit_options={'cache': True,
    'no_cpython_wrapper': True})
def get_local_slice_overload(idx, arr_start, total_len):
    if not idx.has_step:

        def impl(idx, arr_start, total_len):
            slice_index = numba.cpython.unicode._normalize_slice(idx, total_len
                )
            zrv__zulum = max(arr_start, slice_index.start) - arr_start
            nhbel__ohw = max(slice_index.stop - arr_start, 0)
            return slice(zrv__zulum, nhbel__ohw)
    else:

        def impl(idx, arr_start, total_len):
            slice_index = numba.cpython.unicode._normalize_slice(idx, total_len
                )
            rji__dnr = slice_index.start
            zizzs__eik = slice_index.step
            brumg__tqkcm = (0 if zizzs__eik == 1 or rji__dnr > arr_start else
                abs(zizzs__eik - arr_start % zizzs__eik) % zizzs__eik)
            zrv__zulum = max(arr_start, slice_index.start
                ) - arr_start + brumg__tqkcm
            nhbel__ohw = max(slice_index.stop - arr_start, 0)
            return slice(zrv__zulum, nhbel__ohw, zizzs__eik)
    return impl


def slice_getitem(arr, slice_index, arr_start, total_len):
    return arr[slice_index]


@overload(slice_getitem, no_unliteral=True, jit_options={'cache': True})
def slice_getitem_overload(arr, slice_index, arr_start, total_len):

    def getitem_impl(arr, slice_index, arr_start, total_len):
        hwjxj__gmk = get_local_slice(slice_index, arr_start, total_len)
        return bodo.utils.conversion.ensure_contig_if_np(arr[hwjxj__gmk])
    return getitem_impl


dummy_use = numba.njit(lambda a: None)


def int_getitem(arr, ind, arr_start, total_len, is_1D):
    return arr[ind]


def transform_str_getitem_output(data, length):
    pass


@overload(transform_str_getitem_output)
def overload_transform_str_getitem_output(data, length):
    if data == bodo.string_type:
        return lambda data, length: bodo.libs.str_arr_ext.decode_utf8(data.
            _data, length)
    if data == types.Array(types.uint8, 1, 'C'):
        return lambda data, length: bodo.libs.binary_arr_ext.init_bytes_type(
            data, length)
    raise BodoError(
        f'Internal Error: Expected String or Uint8 Array, found {data}')


@overload(int_getitem, no_unliteral=True)
def int_getitem_overload(arr, ind, arr_start, total_len, is_1D):
    if is_str_arr_type(arr) or arr == bodo.binary_array_type:
        tuvaa__yxbf = numba.cpython.unicode.PY_UNICODE_1BYTE_KIND
        zjath__elc = np.int32(numba_to_c_type(types.uint8))
        pcvwp__qlr = arr.dtype

        def str_getitem_impl(arr, ind, arr_start, total_len, is_1D):
            if ind >= total_len:
                raise IndexError('index out of bounds')
            arr = decode_if_dict_array(arr)
            ind = ind % total_len
            root = np.int32(0)
            upyx__eef = np.int32(10)
            tag = np.int32(11)
            pmk__hgd = np.zeros(1, np.int64)
            if arr_start <= ind < arr_start + len(arr):
                ind = ind - arr_start
                elxig__bbg = arr._data
                eiutc__sfsc = bodo.libs.array_item_arr_ext.get_offsets_ind(
                    elxig__bbg, ind)
                orac__lnu = bodo.libs.array_item_arr_ext.get_offsets_ind(
                    elxig__bbg, ind + 1)
                length = orac__lnu - eiutc__sfsc
                feh__eismc = elxig__bbg[ind]
                pmk__hgd[0] = length
                isend(pmk__hgd, np.int32(1), root, upyx__eef, True)
                isend(feh__eismc, np.int32(length), root, tag, True)
            rank = bodo.libs.distributed_api.get_rank()
            val = bodo.libs.str_ext.alloc_empty_bytes_or_string_data(pcvwp__qlr
                , tuvaa__yxbf, 0, 1)
            ywxif__hflb = 0
            if rank == root:
                ywxif__hflb = recv(np.int64, ANY_SOURCE, upyx__eef)
                val = bodo.libs.str_ext.alloc_empty_bytes_or_string_data(
                    pcvwp__qlr, tuvaa__yxbf, ywxif__hflb, 1)
                kll__zuhbv = bodo.libs.str_ext.get_unicode_or_numpy_data(val)
                _recv(kll__zuhbv, np.int32(ywxif__hflb), zjath__elc,
                    ANY_SOURCE, tag)
            dummy_use(pmk__hgd)
            ywxif__hflb = bcast_scalar(ywxif__hflb)
            dummy_use(arr)
            if rank != root:
                val = bodo.libs.str_ext.alloc_empty_bytes_or_string_data(
                    pcvwp__qlr, tuvaa__yxbf, ywxif__hflb, 1)
            kll__zuhbv = bodo.libs.str_ext.get_unicode_or_numpy_data(val)
            c_bcast(kll__zuhbv, np.int32(ywxif__hflb), zjath__elc, np.array
                ([-1]).ctypes, 0, np.int32(root))
            val = transform_str_getitem_output(val, ywxif__hflb)
            return val
        return str_getitem_impl
    if isinstance(arr, bodo.CategoricalArrayType):
        igrs__ybz = bodo.hiframes.pd_categorical_ext.get_categories_int_type(
            arr.dtype)

        def cat_getitem_impl(arr, ind, arr_start, total_len, is_1D):
            if ind >= total_len:
                raise IndexError('index out of bounds')
            ind = ind % total_len
            root = np.int32(0)
            tag = np.int32(11)
            send_arr = np.zeros(1, igrs__ybz)
            if arr_start <= ind < arr_start + len(arr):
                osuc__hehj = (bodo.hiframes.pd_categorical_ext.
                    get_categorical_arr_codes(arr))
                data = osuc__hehj[ind - arr_start]
                send_arr = np.full(1, data, igrs__ybz)
                isend(send_arr, np.int32(1), root, tag, True)
            rank = bodo.libs.distributed_api.get_rank()
            val = igrs__ybz(-1)
            if rank == root:
                val = recv(igrs__ybz, ANY_SOURCE, tag)
            dummy_use(send_arr)
            val = bcast_scalar(val)
            sfpdv__ymf = arr.dtype.categories[max(val, 0)]
            return sfpdv__ymf
        return cat_getitem_impl
    if isinstance(arr, bodo.libs.pd_datetime_arr_ext.DatetimeArrayType):
        uso__hzp = arr.tz

        def tz_aware_getitem_impl(arr, ind, arr_start, total_len, is_1D):
            if ind >= total_len:
                raise IndexError('index out of bounds')
            ind = ind % total_len
            root = np.int32(0)
            tag = np.int32(11)
            send_arr = np.zeros(1, np.int64)
            if arr_start <= ind < arr_start + len(arr):
                data = arr[ind - arr_start].value
                send_arr = np.full(1, data)
                isend(send_arr, np.int32(1), root, tag, True)
            rank = bodo.libs.distributed_api.get_rank()
            val = 0
            if rank == root:
                val = recv(np.int64, ANY_SOURCE, tag)
            dummy_use(send_arr)
            val = bcast_scalar(val)
            return bodo.hiframes.pd_timestamp_ext.convert_val_to_timestamp(val,
                uso__hzp)
        return tz_aware_getitem_impl
    resq__alf = arr.dtype

    def getitem_impl(arr, ind, arr_start, total_len, is_1D):
        if ind >= total_len:
            raise IndexError('index out of bounds')
        ind = ind % total_len
        root = np.int32(0)
        tag = np.int32(11)
        send_arr = np.zeros(1, resq__alf)
        if arr_start <= ind < arr_start + len(arr):
            data = arr[ind - arr_start]
            send_arr = np.full(1, data)
            isend(send_arr, np.int32(1), root, tag, True)
        rank = bodo.libs.distributed_api.get_rank()
        val = np.zeros(1, resq__alf)[0]
        if rank == root:
            val = recv(resq__alf, ANY_SOURCE, tag)
        dummy_use(send_arr)
        val = bcast_scalar(val)
        return val
    return getitem_impl


def get_chunk_bounds(A):
    pass


@overload(get_chunk_bounds, jit_options={'cache': True})
def get_chunk_bounds_overload(A):
    if not (isinstance(A, types.Array) and isinstance(A.dtype, types.Integer)):
        raise BodoError(
            'get_chunk_bounds() only supports Numpy int input currently.')

    def impl(A):
        n_pes = get_size()
        daag__ydpxn = np.empty(n_pes, np.int64)
        kjet__uxvk = np.empty(n_pes, np.int8)
        val = numba.cpython.builtins.get_type_min_value(numba.core.types.int64)
        yjal__bifn = 1
        if len(A) != 0:
            val = A[-1]
            yjal__bifn = 0
        allgather(daag__ydpxn, np.int64(val))
        allgather(kjet__uxvk, yjal__bifn)
        for i, yjal__bifn in enumerate(kjet__uxvk):
            if yjal__bifn and i != 0:
                daag__ydpxn[i] = daag__ydpxn[i - 1]
        return daag__ydpxn
    return impl


c_alltoallv = types.ExternalFunction('c_alltoallv', types.void(types.
    voidptr, types.voidptr, types.voidptr, types.voidptr, types.voidptr,
    types.voidptr, types.int32))


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def alltoallv(send_data, out_data, send_counts, recv_counts, send_disp,
    recv_disp):
    typ_enum = get_type_enum(send_data)
    cdv__lvcz = get_type_enum(out_data)
    assert typ_enum == cdv__lvcz
    if isinstance(send_data, (IntegerArrayType, FloatingArrayType,
        DecimalArrayType)) or send_data in (boolean_array,
        datetime_date_array_type):
        return (lambda send_data, out_data, send_counts, recv_counts,
            send_disp, recv_disp: c_alltoallv(send_data._data.ctypes,
            out_data._data.ctypes, send_counts.ctypes, recv_counts.ctypes,
            send_disp.ctypes, recv_disp.ctypes, typ_enum))
    if isinstance(send_data, bodo.CategoricalArrayType):
        return (lambda send_data, out_data, send_counts, recv_counts,
            send_disp, recv_disp: c_alltoallv(send_data.codes.ctypes,
            out_data.codes.ctypes, send_counts.ctypes, recv_counts.ctypes,
            send_disp.ctypes, recv_disp.ctypes, typ_enum))
    return (lambda send_data, out_data, send_counts, recv_counts, send_disp,
        recv_disp: c_alltoallv(send_data.ctypes, out_data.ctypes,
        send_counts.ctypes, recv_counts.ctypes, send_disp.ctypes, recv_disp
        .ctypes, typ_enum))


def alltoallv_tup(send_data, out_data, send_counts, recv_counts, send_disp,
    recv_disp):
    return


@overload(alltoallv_tup, no_unliteral=True)
def alltoallv_tup_overload(send_data, out_data, send_counts, recv_counts,
    send_disp, recv_disp):
    count = send_data.count
    assert out_data.count == count
    flehk__ujy = (
        'def f(send_data, out_data, send_counts, recv_counts, send_disp, recv_disp):\n'
        )
    for i in range(count):
        flehk__ujy += (
            """  alltoallv(send_data[{}], out_data[{}], send_counts, recv_counts, send_disp, recv_disp)
"""
            .format(i, i))
    flehk__ujy += '  return\n'
    jxgg__eewvo = {}
    exec(flehk__ujy, {'alltoallv': alltoallv}, jxgg__eewvo)
    poobk__thg = jxgg__eewvo['f']
    return poobk__thg


@numba.njit
def get_start_count(n):
    rank = bodo.libs.distributed_api.get_rank()
    n_pes = bodo.libs.distributed_api.get_size()
    rji__dnr = bodo.libs.distributed_api.get_start(n, n_pes, rank)
    count = bodo.libs.distributed_api.get_node_portion(n, n_pes, rank)
    return rji__dnr, count


@numba.njit
def get_start(total_size, pes, rank):
    twca__bwjnn = total_size % pes
    grubl__yhcmn = (total_size - twca__bwjnn) // pes
    return rank * grubl__yhcmn + min(rank, twca__bwjnn)


@numba.njit
def get_end(total_size, pes, rank):
    twca__bwjnn = total_size % pes
    grubl__yhcmn = (total_size - twca__bwjnn) // pes
    return (rank + 1) * grubl__yhcmn + min(rank + 1, twca__bwjnn)


@numba.njit
def get_node_portion(total_size, pes, rank):
    twca__bwjnn = total_size % pes
    grubl__yhcmn = (total_size - twca__bwjnn) // pes
    if rank < twca__bwjnn:
        return grubl__yhcmn + 1
    else:
        return grubl__yhcmn


@numba.generated_jit(nopython=True)
def dist_cumsum(in_arr, out_arr):
    ggrfo__bqqqm = in_arr.dtype(0)
    zakl__nacq = np.int32(Reduce_Type.Sum.value)

    def cumsum_impl(in_arr, out_arr):
        wwbnh__fsnpn = ggrfo__bqqqm
        for uia__wqegx in np.nditer(in_arr):
            wwbnh__fsnpn += uia__wqegx.item()
        xadjt__nqqug = dist_exscan(wwbnh__fsnpn, zakl__nacq)
        for i in range(in_arr.size):
            xadjt__nqqug += in_arr[i]
            out_arr[i] = xadjt__nqqug
        return 0
    return cumsum_impl


@numba.generated_jit(nopython=True)
def dist_cumprod(in_arr, out_arr):
    uka__dyhk = in_arr.dtype(1)
    zakl__nacq = np.int32(Reduce_Type.Prod.value)

    def cumprod_impl(in_arr, out_arr):
        wwbnh__fsnpn = uka__dyhk
        for uia__wqegx in np.nditer(in_arr):
            wwbnh__fsnpn *= uia__wqegx.item()
        xadjt__nqqug = dist_exscan(wwbnh__fsnpn, zakl__nacq)
        if get_rank() == 0:
            xadjt__nqqug = uka__dyhk
        for i in range(in_arr.size):
            xadjt__nqqug *= in_arr[i]
            out_arr[i] = xadjt__nqqug
        return 0
    return cumprod_impl


@numba.generated_jit(nopython=True)
def dist_cummin(in_arr, out_arr):
    if isinstance(in_arr.dtype, types.Float):
        uka__dyhk = np.finfo(in_arr.dtype(1).dtype).max
    else:
        uka__dyhk = np.iinfo(in_arr.dtype(1).dtype).max
    zakl__nacq = np.int32(Reduce_Type.Min.value)

    def cummin_impl(in_arr, out_arr):
        wwbnh__fsnpn = uka__dyhk
        for uia__wqegx in np.nditer(in_arr):
            wwbnh__fsnpn = min(wwbnh__fsnpn, uia__wqegx.item())
        xadjt__nqqug = dist_exscan(wwbnh__fsnpn, zakl__nacq)
        if get_rank() == 0:
            xadjt__nqqug = uka__dyhk
        for i in range(in_arr.size):
            xadjt__nqqug = min(xadjt__nqqug, in_arr[i])
            out_arr[i] = xadjt__nqqug
        return 0
    return cummin_impl


@numba.generated_jit(nopython=True)
def dist_cummax(in_arr, out_arr):
    if isinstance(in_arr.dtype, types.Float):
        uka__dyhk = np.finfo(in_arr.dtype(1).dtype).min
    else:
        uka__dyhk = np.iinfo(in_arr.dtype(1).dtype).min
    uka__dyhk = in_arr.dtype(1)
    zakl__nacq = np.int32(Reduce_Type.Max.value)

    def cummax_impl(in_arr, out_arr):
        wwbnh__fsnpn = uka__dyhk
        for uia__wqegx in np.nditer(in_arr):
            wwbnh__fsnpn = max(wwbnh__fsnpn, uia__wqegx.item())
        xadjt__nqqug = dist_exscan(wwbnh__fsnpn, zakl__nacq)
        if get_rank() == 0:
            xadjt__nqqug = uka__dyhk
        for i in range(in_arr.size):
            xadjt__nqqug = max(xadjt__nqqug, in_arr[i])
            out_arr[i] = xadjt__nqqug
        return 0
    return cummax_impl


_allgather = types.ExternalFunction('allgather', types.void(types.voidptr,
    types.int32, types.voidptr, types.int32))


@numba.njit
def allgather(arr, val):
    ylpi__cnnz = get_type_enum(arr)
    _allgather(arr.ctypes, 1, value_to_ptr(val), ylpi__cnnz)


def dist_return(A):
    return A


def rep_return(A):
    return A


def dist_return_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 1 and not kws
    dccmf__fupoq = args[0]
    if equiv_set.has_shape(dccmf__fupoq):
        return ArrayAnalysis.AnalyzeResult(shape=dccmf__fupoq, pre=[])
    return None


ArrayAnalysis._analyze_op_call_bodo_libs_distributed_api_dist_return = (
    dist_return_equiv)
ArrayAnalysis._analyze_op_call_bodo_libs_distributed_api_rep_return = (
    dist_return_equiv)


def threaded_return(A):
    return A


@numba.njit
def set_arr_local(arr, ind, val):
    arr[ind] = val


@numba.njit
def local_alloc_size(n, in_arr):
    return n


@infer_global(threaded_return)
@infer_global(dist_return)
@infer_global(rep_return)
class ThreadedRetTyper(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        assert len(args) == 1
        return signature(args[0], *args)


@numba.njit
def parallel_print(*args):
    print(*args)


@numba.njit
def single_print(*args):
    if bodo.libs.distributed_api.get_rank() == 0:
        print(*args)


def print_if_not_empty(args):
    pass


@overload(print_if_not_empty)
def overload_print_if_not_empty(*args):
    mbw__nzcay = '(' + ' or '.join(['False'] + [f'len(args[{i}]) != 0' for 
        i, husiq__yeut in enumerate(args) if is_array_typ(husiq__yeut) or
        isinstance(husiq__yeut, bodo.hiframes.pd_dataframe_ext.DataFrameType)]
        ) + ')'
    flehk__ujy = f"""def impl(*args):
    if {mbw__nzcay} or bodo.get_rank() == 0:
        print(*args)"""
    jxgg__eewvo = {}
    exec(flehk__ujy, globals(), jxgg__eewvo)
    impl = jxgg__eewvo['impl']
    return impl


_wait = types.ExternalFunction('dist_wait', types.void(mpi_req_numba_type,
    types.bool_))


@numba.generated_jit(nopython=True)
def wait(req, cond=True):
    if isinstance(req, types.BaseTuple):
        count = len(req.types)
        lbs__mtmzg = ','.join(f'_wait(req[{i}], cond)' for i in range(count))
        flehk__ujy = 'def f(req, cond=True):\n'
        flehk__ujy += f'  return {lbs__mtmzg}\n'
        jxgg__eewvo = {}
        exec(flehk__ujy, {'_wait': _wait}, jxgg__eewvo)
        impl = jxgg__eewvo['f']
        return impl
    if is_overload_none(req):
        return lambda req, cond=True: None
    return lambda req, cond=True: _wait(req, cond)


@register_jitable
def _set_if_in_range(A, val, index, chunk_start):
    if index >= chunk_start and index < chunk_start + len(A):
        A[index - chunk_start] = val


@register_jitable
def _root_rank_select(old_val, new_val):
    if get_rank() == 0:
        return old_val
    return new_val


def get_tuple_prod(t):
    return np.prod(t)


@overload(get_tuple_prod, no_unliteral=True)
def get_tuple_prod_overload(t):
    if t == numba.core.types.containers.Tuple(()):
        return lambda t: 1

    def get_tuple_prod_impl(t):
        twca__bwjnn = 1
        for a in t:
            twca__bwjnn *= a
        return twca__bwjnn
    return get_tuple_prod_impl


sig = types.void(types.voidptr, types.voidptr, types.intp, types.intp,
    types.intp, types.intp, types.int32, types.voidptr)
oneD_reshape_shuffle = types.ExternalFunction('oneD_reshape_shuffle', sig)


@numba.njit(no_cpython_wrapper=True, cache=True)
def dist_oneD_reshape_shuffle(lhs, in_arr, new_dim0_global_len, dest_ranks=None
    ):
    mwzk__ojjz = np.ascontiguousarray(in_arr)
    ioez__fomq = get_tuple_prod(mwzk__ojjz.shape[1:])
    xjep__aakgi = get_tuple_prod(lhs.shape[1:])
    if dest_ranks is not None:
        gve__cwswm = np.array(dest_ranks, dtype=np.int32)
    else:
        gve__cwswm = np.empty(0, dtype=np.int32)
    dtype_size = bodo.io.np_io.get_dtype_size(in_arr.dtype)
    oneD_reshape_shuffle(lhs.ctypes, mwzk__ojjz.ctypes, new_dim0_global_len,
        len(in_arr), dtype_size * xjep__aakgi, dtype_size * ioez__fomq, len
        (gve__cwswm), gve__cwswm.ctypes)
    check_and_propagate_cpp_exception()


permutation_int = types.ExternalFunction('permutation_int', types.void(
    types.voidptr, types.intp))


@numba.njit
def dist_permutation_int(lhs, n):
    permutation_int(lhs.ctypes, n)


permutation_array_index = types.ExternalFunction('permutation_array_index',
    types.void(types.voidptr, types.intp, types.intp, types.voidptr, types.
    int64, types.voidptr, types.intp, types.int64))


@numba.njit
def dist_permutation_array_index(lhs, lhs_len, dtype_size, rhs, p, p_len,
    n_samples):
    pjv__zgzc = np.ascontiguousarray(rhs)
    pqk__rlehf = get_tuple_prod(pjv__zgzc.shape[1:])
    ccwo__aujzp = dtype_size * pqk__rlehf
    permutation_array_index(lhs.ctypes, lhs_len, ccwo__aujzp, pjv__zgzc.
        ctypes, pjv__zgzc.shape[0], p.ctypes, p_len, n_samples)
    check_and_propagate_cpp_exception()


from bodo.io import fsspec_reader, hdfs_reader
ll.add_symbol('finalize', hdist.finalize)
finalize = types.ExternalFunction('finalize', types.int32())
ll.add_symbol('finalize_fsspec', fsspec_reader.finalize_fsspec)
finalize_fsspec = types.ExternalFunction('finalize_fsspec', types.int32())
ll.add_symbol('disconnect_hdfs', hdfs_reader.disconnect_hdfs)
disconnect_hdfs = types.ExternalFunction('disconnect_hdfs', types.int32())


def _check_for_cpp_errors():
    pass


@overload(_check_for_cpp_errors)
def overload_check_for_cpp_errors():
    return lambda : check_and_propagate_cpp_exception()


@numba.njit
def disconnect_hdfs_njit():
    disconnect_hdfs()


@numba.njit
def call_finalize():
    finalize()
    finalize_fsspec()
    _check_for_cpp_errors()
    disconnect_hdfs()


def flush_stdout():
    if not sys.stdout.closed:
        sys.stdout.flush()


atexit.register(call_finalize)
atexit.register(flush_stdout)


def bcast_comm(data, comm_ranks, nranks, root=MPI_ROOT):
    rank = bodo.libs.distributed_api.get_rank()
    dtype = bodo.typeof(data)
    dtype = _bcast_dtype(dtype, root)
    if rank != MPI_ROOT:
        data = get_value_for_type(dtype)
    return bcast_comm_impl(data, comm_ranks, nranks, root)


@overload(bcast_comm)
def bcast_comm_overload(data, comm_ranks, nranks, root=MPI_ROOT):
    return lambda data, comm_ranks, nranks, root=MPI_ROOT: bcast_comm_impl(data
        , comm_ranks, nranks, root)


@numba.generated_jit(nopython=True)
def bcast_comm_impl(data, comm_ranks, nranks, root=MPI_ROOT):
    bodo.hiframes.pd_dataframe_ext.check_runtime_cols_unsupported(data,
        'bodo.bcast_comm()')
    if isinstance(data, (types.Integer, types.Float)):
        typ_val = numba_to_c_type(data)
        flehk__ujy = (
            f"""def bcast_scalar_impl(data, comm_ranks, nranks, root={MPI_ROOT}):
  send = np.empty(1, dtype)
  send[0] = data
  c_bcast(send.ctypes, np.int32(1), np.int32({{}}), comm_ranks,ctypes, np.int32({{}}), np.int32(root))
  return send[0]
"""
            .format(typ_val, nranks))
        dtype = numba.np.numpy_support.as_dtype(data)
        jxgg__eewvo = {}
        exec(flehk__ujy, {'bodo': bodo, 'np': np, 'c_bcast': c_bcast,
            'dtype': dtype}, jxgg__eewvo)
        wdnqj__knaxg = jxgg__eewvo['bcast_scalar_impl']
        return wdnqj__knaxg
    if isinstance(data, types.Array):
        return lambda data, comm_ranks, nranks, root=MPI_ROOT: _bcast_np(data,
            comm_ranks, nranks, root)
    if isinstance(data, bodo.hiframes.pd_dataframe_ext.DataFrameType):
        ura__wbj = len(data.columns)
        jswp__bawxq = ', '.join('g_data_{}'.format(i) for i in range(ura__wbj))
        ina__oisj = ColNamesMetaType(data.columns)
        flehk__ujy = (
            f'def impl_df(data, comm_ranks, nranks, root={MPI_ROOT}):\n')
        for i in range(ura__wbj):
            flehk__ujy += (
                """  data_{} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(data, {})
"""
                .format(i, i))
            flehk__ujy += (
                """  g_data_{} = bodo.libs.distributed_api.bcast_comm_impl(data_{}, comm_ranks, nranks, root)
"""
                .format(i, i))
        flehk__ujy += (
            '  index = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(data)\n'
            )
        flehk__ujy += """  g_index = bodo.libs.distributed_api.bcast_comm_impl(index, comm_ranks, nranks, root)
"""
        flehk__ujy += (
            """  return bodo.hiframes.pd_dataframe_ext.init_dataframe(({},), g_index, __col_name_meta_value_bcast_comm)
"""
            .format(jswp__bawxq))
        jxgg__eewvo = {}
        exec(flehk__ujy, {'bodo': bodo, '__col_name_meta_value_bcast_comm':
            ina__oisj}, jxgg__eewvo)
        axgdo__yblsk = jxgg__eewvo['impl_df']
        return axgdo__yblsk
    if isinstance(data, bodo.hiframes.pd_index_ext.RangeIndexType):

        def impl_range_index(data, comm_ranks, nranks, root=MPI_ROOT):
            rank = bodo.libs.distributed_api.get_rank()
            n_pes = bodo.libs.distributed_api.get_size()
            rji__dnr = data._start
            piid__vnnk = data._stop
            zizzs__eik = data._step
            vfc__byp = data._name
            vfc__byp = bcast_scalar(vfc__byp, root)
            rji__dnr = bcast_scalar(rji__dnr, root)
            piid__vnnk = bcast_scalar(piid__vnnk, root)
            zizzs__eik = bcast_scalar(zizzs__eik, root)
            qbp__xlo = bodo.libs.array_kernels.calc_nitems(rji__dnr,
                piid__vnnk, zizzs__eik)
            chunk_start = bodo.libs.distributed_api.get_start(qbp__xlo,
                n_pes, rank)
            oif__kdq = bodo.libs.distributed_api.get_node_portion(qbp__xlo,
                n_pes, rank)
            zrv__zulum = rji__dnr + zizzs__eik * chunk_start
            nhbel__ohw = rji__dnr + zizzs__eik * (chunk_start + oif__kdq)
            nhbel__ohw = min(nhbel__ohw, piid__vnnk)
            return bodo.hiframes.pd_index_ext.init_range_index(zrv__zulum,
                nhbel__ohw, zizzs__eik, vfc__byp)
        return impl_range_index
    if bodo.hiframes.pd_index_ext.is_pd_index_type(data):

        def impl_pd_index(data, comm_ranks, nranks, root=MPI_ROOT):
            dcz__wjrt = data._data
            vfc__byp = data._name
            arr = bodo.libs.distributed_api.bcast_comm_impl(dcz__wjrt,
                comm_ranks, nranks, root)
            return bodo.utils.conversion.index_from_array(arr, vfc__byp)
        return impl_pd_index
    if isinstance(data, bodo.hiframes.pd_series_ext.SeriesType):

        def impl_series(data, comm_ranks, nranks, root=MPI_ROOT):
            arr = bodo.hiframes.pd_series_ext.get_series_data(data)
            index = bodo.hiframes.pd_series_ext.get_series_index(data)
            vfc__byp = bodo.hiframes.pd_series_ext.get_series_name(data)
            ekini__slwvs = bodo.libs.distributed_api.bcast_comm_impl(vfc__byp,
                comm_ranks, nranks, root)
            out_arr = bodo.libs.distributed_api.bcast_comm_impl(arr,
                comm_ranks, nranks, root)
            oqed__vkbre = bodo.libs.distributed_api.bcast_comm_impl(index,
                comm_ranks, nranks, root)
            return bodo.hiframes.pd_series_ext.init_series(out_arr,
                oqed__vkbre, ekini__slwvs)
        return impl_series
    if isinstance(data, types.BaseTuple):
        flehk__ujy = (
            f'def impl_tuple(data, comm_ranks, nranks, root={MPI_ROOT}):\n')
        flehk__ujy += '  return ({}{})\n'.format(', '.join(
            'bcast_comm_impl(data[{}], comm_ranks, nranks, root)'.format(i) for
            i in range(len(data))), ',' if len(data) > 0 else '')
        jxgg__eewvo = {}
        exec(flehk__ujy, {'bcast_comm_impl': bcast_comm_impl}, jxgg__eewvo)
        xlk__chyw = jxgg__eewvo['impl_tuple']
        return xlk__chyw
    if data is types.none:
        return lambda data, comm_ranks, nranks, root=MPI_ROOT: None


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def _bcast_np(data, comm_ranks, nranks, root=MPI_ROOT):
    typ_val = numba_to_c_type(data.dtype)
    jzv__inbrz = data.ndim
    dtype = data.dtype
    if dtype == types.NPDatetime('ns'):
        dtype = np.dtype('datetime64[ns]')
    elif dtype == types.NPTimedelta('ns'):
        dtype = np.dtype('timedelta64[ns]')
    tcfgh__qnk = (0,) * jzv__inbrz

    def bcast_arr_impl(data, comm_ranks, nranks, root=MPI_ROOT):
        rank = bodo.libs.distributed_api.get_rank()
        dcz__wjrt = np.ascontiguousarray(data)
        kll__zuhbv = data.ctypes
        ijl__zro = tcfgh__qnk
        if rank == root:
            ijl__zro = dcz__wjrt.shape
        ijl__zro = bcast_tuple(ijl__zro, root)
        fgnah__dnllr = get_tuple_prod(ijl__zro[1:])
        send_counts = ijl__zro[0] * fgnah__dnllr
        lkyh__eaw = np.empty(send_counts, dtype)
        if rank == MPI_ROOT:
            c_bcast(kll__zuhbv, np.int32(send_counts), np.int32(typ_val),
                comm_ranks.ctypes, np.int32(nranks), np.int32(root))
            return data
        else:
            c_bcast(lkyh__eaw.ctypes, np.int32(send_counts), np.int32(
                typ_val), comm_ranks.ctypes, np.int32(nranks), np.int32(root))
            return lkyh__eaw.reshape((-1,) + ijl__zro[1:])
    return bcast_arr_impl


node_ranks = None


def get_host_ranks():
    global node_ranks
    if node_ranks is None:
        xqx__ptpm = MPI.COMM_WORLD
        zwzj__zyskl = MPI.Get_processor_name()
        hpslt__wve = xqx__ptpm.allgather(zwzj__zyskl)
        node_ranks = defaultdict(list)
        for i, dum__ycdt in enumerate(hpslt__wve):
            node_ranks[dum__ycdt].append(i)
    return node_ranks


def create_subcomm_mpi4py(comm_ranks):
    xqx__ptpm = MPI.COMM_WORLD
    wzlsm__iaapf = xqx__ptpm.Get_group()
    lsa__xnp = wzlsm__iaapf.Incl(comm_ranks)
    tmyz__sxt = xqx__ptpm.Create_group(lsa__xnp)
    return tmyz__sxt


def get_nodes_first_ranks():
    tqwct__iykx = get_host_ranks()
    return np.array([hbnpe__sbyu[0] for hbnpe__sbyu in tqwct__iykx.values()
        ], dtype='int32')


def get_num_nodes():
    return len(get_host_ranks())
