"""
Collection of utility functions. Needs to be refactored in separate files.
"""
import hashlib
import inspect
import keyword
import re
import warnings
from enum import Enum
import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from mpi4py import MPI
from numba.core import cgutils, ir, ir_utils, types
from numba.core.imputils import lower_builtin, lower_constant
from numba.core.ir_utils import find_callname, find_const, get_definition, guard, mk_unique_var, require
from numba.core.typing import signature
from numba.core.typing.templates import AbstractTemplate, infer_global
from numba.extending import intrinsic, overload
from numba.np.arrayobj import get_itemsize, make_array, populate_array
from numba.np.numpy_support import as_dtype
import bodo
from bodo.hiframes.time_ext import TimeArrayType
from bodo.libs.binary_arr_ext import bytes_type
from bodo.libs.bool_arr_ext import boolean_array
from bodo.libs.decimal_arr_ext import DecimalArrayType
from bodo.libs.float_arr_ext import FloatingArrayType
from bodo.libs.int_arr_ext import IntegerArrayType
from bodo.libs.str_arr_ext import num_total_chars, pre_alloc_string_array, string_array_type
from bodo.libs.str_ext import string_type
from bodo.utils.cg_helpers import is_ll_eq
from bodo.utils.typing import NOT_CONSTANT, BodoError, BodoWarning, MetaType, is_str_arr_type
int128_type = types.Integer('int128', 128)


class CTypeEnum(Enum):
    Int8 = 0
    UInt8 = 1
    Int32 = 2
    UInt32 = 3
    Int64 = 4
    UInt64 = 7
    Float32 = 5
    Float64 = 6
    Int16 = 8
    UInt16 = 9
    STRING = 10
    Bool = 11
    Decimal = 12
    Date = 13
    Time = 14
    Datetime = 15
    Timedelta = 16
    Int128 = 17
    LIST = 19
    STRUCT = 20
    BINARY = 21


_numba_to_c_type_map = {types.int8: CTypeEnum.Int8.value, types.uint8:
    CTypeEnum.UInt8.value, types.int32: CTypeEnum.Int32.value, types.uint32:
    CTypeEnum.UInt32.value, types.int64: CTypeEnum.Int64.value, types.
    uint64: CTypeEnum.UInt64.value, types.float32: CTypeEnum.Float32.value,
    types.float64: CTypeEnum.Float64.value, types.NPDatetime('ns'):
    CTypeEnum.Datetime.value, types.NPTimedelta('ns'): CTypeEnum.Timedelta.
    value, types.bool_: CTypeEnum.Bool.value, types.int16: CTypeEnum.Int16.
    value, types.uint16: CTypeEnum.UInt16.value, int128_type: CTypeEnum.
    Int128.value}
numba.core.errors.error_extras = {'unsupported_error': '', 'typing': '',
    'reportable': '', 'interpreter': '', 'constant_inference': ''}
np_alloc_callnames = 'empty', 'zeros', 'ones', 'full'
CONST_DICT_SLOW_WARN_THRESHOLD = 100
CONST_LIST_SLOW_WARN_THRESHOLD = 100000


def unliteral_all(args):
    return tuple(types.unliteral(a) for a in args)


def get_constant(func_ir, var, default=NOT_CONSTANT):
    bur__rdk = guard(get_definition, func_ir, var)
    if bur__rdk is None:
        return default
    if isinstance(bur__rdk, ir.Const):
        return bur__rdk.value
    if isinstance(bur__rdk, ir.Var):
        return get_constant(func_ir, bur__rdk, default)
    return default


def numba_to_c_type(t):
    if isinstance(t, bodo.libs.decimal_arr_ext.Decimal128Type):
        return CTypeEnum.Decimal.value
    if t == bodo.hiframes.datetime_date_ext.datetime_date_type:
        return CTypeEnum.Date.value
    if isinstance(t, bodo.hiframes.time_ext.TimeType):
        return CTypeEnum.Time.value
    return _numba_to_c_type_map[t]


def is_alloc_callname(func_name, mod_name):
    return isinstance(mod_name, str) and (mod_name == 'numpy' and func_name in
        np_alloc_callnames or func_name == 'empty_inferred' and mod_name in
        ('numba.extending', 'numba.np.unsafe.ndarray') or func_name ==
        'pre_alloc_string_array' and mod_name == 'bodo.libs.str_arr_ext' or
        func_name == 'pre_alloc_binary_array' and mod_name ==
        'bodo.libs.binary_arr_ext' or func_name ==
        'alloc_random_access_string_array' and mod_name ==
        'bodo.libs.str_ext' or func_name == 'pre_alloc_array_item_array' and
        mod_name == 'bodo.libs.array_item_arr_ext' or func_name ==
        'pre_alloc_struct_array' and mod_name == 'bodo.libs.struct_arr_ext' or
        func_name == 'pre_alloc_map_array' and mod_name ==
        'bodo.libs.map_arr_ext' or func_name == 'pre_alloc_tuple_array' and
        mod_name == 'bodo.libs.tuple_arr_ext' or func_name ==
        'alloc_bool_array' and mod_name == 'bodo.libs.bool_arr_ext' or 
        func_name == 'alloc_int_array' and mod_name ==
        'bodo.libs.int_arr_ext' or func_name == 'alloc_float_array' and 
        mod_name == 'bodo.libs.float_arr_ext' or func_name ==
        'alloc_datetime_date_array' and mod_name ==
        'bodo.hiframes.datetime_date_ext' or func_name ==
        'alloc_datetime_timedelta_array' and mod_name ==
        'bodo.hiframes.datetime_timedelta_ext' or func_name ==
        'alloc_decimal_array' and mod_name == 'bodo.libs.decimal_arr_ext' or
        func_name == 'alloc_categorical_array' and mod_name ==
        'bodo.hiframes.pd_categorical_ext' or func_name == 'gen_na_array' and
        mod_name == 'bodo.libs.array_kernels' or func_name ==
        'alloc_pd_datetime_array' and mod_name ==
        'bodo.libs.pd_datetime_arr_ext')


def find_build_tuple(func_ir, var):
    require(isinstance(var, (ir.Var, str)))
    uzpf__abbk = get_definition(func_ir, var)
    require(isinstance(uzpf__abbk, ir.Expr))
    require(uzpf__abbk.op == 'build_tuple')
    return uzpf__abbk.items


def cprint(*s):
    print(*s)


@infer_global(cprint)
class CprintInfer(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        return signature(types.none, *unliteral_all(args))


typ_to_format = {types.int32: 'd', types.uint32: 'u', types.int64: 'lld',
    types.uint64: 'llu', types.float32: 'f', types.float64: 'lf', types.
    voidptr: 's'}


@lower_builtin(cprint, types.VarArg(types.Any))
def cprint_lower(context, builder, sig, args):
    for wnib__yzuf, val in enumerate(args):
        typ = sig.args[wnib__yzuf]
        if isinstance(typ, types.ArrayCTypes):
            cgutils.printf(builder, '%p ', val)
            continue
        fik__hog = typ_to_format[typ]
        cgutils.printf(builder, '%{} '.format(fik__hog), val)
    cgutils.printf(builder, '\n')
    return context.get_dummy_value()


def is_whole_slice(typemap, func_ir, var, accept_stride=False):
    require(typemap[var.name] == types.slice2_type or accept_stride and 
        typemap[var.name] == types.slice3_type)
    jhdxn__iale = get_definition(func_ir, var)
    require(isinstance(jhdxn__iale, ir.Expr) and jhdxn__iale.op == 'call')
    assert len(jhdxn__iale.args) == 2 or accept_stride and len(jhdxn__iale.args
        ) == 3
    assert find_callname(func_ir, jhdxn__iale) == ('slice', 'builtins')
    fsejc__kvba = get_definition(func_ir, jhdxn__iale.args[0])
    bhcgr__idsx = get_definition(func_ir, jhdxn__iale.args[1])
    require(isinstance(fsejc__kvba, ir.Const) and fsejc__kvba.value == None)
    require(isinstance(bhcgr__idsx, ir.Const) and bhcgr__idsx.value == None)
    return True


def is_slice_equiv_arr(arr_var, index_var, func_ir, equiv_set,
    accept_stride=False):
    yybtc__tjg = get_definition(func_ir, index_var)
    require(find_callname(func_ir, yybtc__tjg) == ('slice', 'builtins'))
    require(len(yybtc__tjg.args) in (2, 3))
    require(find_const(func_ir, yybtc__tjg.args[0]) in (0, None))
    require(equiv_set.is_equiv(yybtc__tjg.args[1], arr_var.name + '#0'))
    require(accept_stride or len(yybtc__tjg.args) == 2 or find_const(
        func_ir, yybtc__tjg.args[2]) == 1)
    return True


def get_slice_step(typemap, func_ir, var):
    require(typemap[var.name] == types.slice3_type)
    jhdxn__iale = get_definition(func_ir, var)
    require(isinstance(jhdxn__iale, ir.Expr) and jhdxn__iale.op == 'call')
    assert len(jhdxn__iale.args) == 3
    return jhdxn__iale.args[2]


def is_array_typ(var_typ, include_index_series=True):
    return is_np_array_typ(var_typ) or var_typ in (string_array_type, bodo.
        binary_array_type, bodo.dict_str_arr_type, bodo.hiframes.split_impl
        .string_array_split_view_type, bodo.hiframes.datetime_date_ext.
        datetime_date_array_type, bodo.hiframes.datetime_timedelta_ext.
        datetime_timedelta_array_type, boolean_array, bodo.libs.str_ext.
        random_access_string_array, bodo.libs.interval_arr_ext.
        IntervalArrayType) or isinstance(var_typ, (IntegerArrayType,
        FloatingArrayType, bodo.libs.decimal_arr_ext.DecimalArrayType, bodo
        .hiframes.pd_categorical_ext.CategoricalArrayType, bodo.libs.
        array_item_arr_ext.ArrayItemArrayType, bodo.libs.struct_arr_ext.
        StructArrayType, bodo.libs.interval_arr_ext.IntervalArrayType, bodo
        .libs.tuple_arr_ext.TupleArrayType, bodo.libs.map_arr_ext.
        MapArrayType, bodo.libs.csr_matrix_ext.CSRMatrixType, bodo.
        DatetimeArrayType, TimeArrayType)) or include_index_series and (
        isinstance(var_typ, (bodo.hiframes.pd_series_ext.SeriesType, bodo.
        hiframes.pd_multi_index_ext.MultiIndexType)) or bodo.hiframes.
        pd_index_ext.is_pd_index_type(var_typ))


def is_np_array_typ(var_typ):
    return isinstance(var_typ, types.Array)


def is_distributable_typ(var_typ):
    return is_array_typ(var_typ) or isinstance(var_typ, bodo.hiframes.table
        .TableType) or isinstance(var_typ, bodo.hiframes.pd_dataframe_ext.
        DataFrameType) or isinstance(var_typ, types.List
        ) and is_distributable_typ(var_typ.dtype) or isinstance(var_typ,
        types.DictType) and is_distributable_typ(var_typ.value_type)


def is_distributable_tuple_typ(var_typ):
    try:
        from bodosql.context_ext import BodoSQLContextType
    except ImportError as gqsx__qcji:
        BodoSQLContextType = None
    return isinstance(var_typ, types.BaseTuple) and any(
        is_distributable_typ(t) or is_distributable_tuple_typ(t) for t in
        var_typ.types) or isinstance(var_typ, types.List
        ) and is_distributable_tuple_typ(var_typ.dtype) or isinstance(var_typ,
        types.DictType) and is_distributable_tuple_typ(var_typ.value_type
        ) or isinstance(var_typ, types.iterators.EnumerateType) and (
        is_distributable_typ(var_typ.yield_type[1]) or
        is_distributable_tuple_typ(var_typ.yield_type[1])
        ) or BodoSQLContextType is not None and isinstance(var_typ,
        BodoSQLContextType) and any([is_distributable_typ(ugy__nxys) for
        ugy__nxys in var_typ.dataframes])


@numba.generated_jit(nopython=True, cache=True)
def build_set_seen_na(A):

    def impl(A):
        s = dict()
        xpx__yrdk = False
        for wnib__yzuf in range(len(A)):
            if bodo.libs.array_kernels.isna(A, wnib__yzuf):
                xpx__yrdk = True
                continue
            s[A[wnib__yzuf]] = 0
        return s, xpx__yrdk
    return impl


def empty_like_type(n, arr):
    return np.empty(n, arr.dtype)


@overload(empty_like_type, no_unliteral=True)
def empty_like_type_overload(n, arr):
    if isinstance(arr, bodo.hiframes.pd_categorical_ext.CategoricalArrayType):
        return (lambda n, arr: bodo.hiframes.pd_categorical_ext.
            alloc_categorical_array(n, arr.dtype))
    if isinstance(arr, types.Array):
        return lambda n, arr: np.empty(n, arr.dtype)
    if isinstance(arr, types.List) and arr.dtype == string_type:

        def empty_like_type_str_list(n, arr):
            return [''] * n
        return empty_like_type_str_list
    if isinstance(arr, types.List) and arr.dtype == bytes_type:

        def empty_like_type_binary_list(n, arr):
            return [b''] * n
        return empty_like_type_binary_list
    if isinstance(arr, IntegerArrayType):
        oenps__ivg = arr.dtype

        def empty_like_type_int_arr(n, arr):
            return bodo.libs.int_arr_ext.alloc_int_array(n, oenps__ivg)
        return empty_like_type_int_arr
    if isinstance(arr, FloatingArrayType):
        oenps__ivg = arr.dtype

        def empty_like_type_float_arr(n, arr):
            return bodo.libs.float_arr_ext.alloc_float_array(n, oenps__ivg)
        return empty_like_type_float_arr
    if arr == boolean_array:

        def empty_like_type_bool_arr(n, arr):
            return bodo.libs.bool_arr_ext.alloc_bool_array(n)
        return empty_like_type_bool_arr
    if arr == bodo.hiframes.datetime_date_ext.datetime_date_array_type:

        def empty_like_type_datetime_date_arr(n, arr):
            return bodo.hiframes.datetime_date_ext.alloc_datetime_date_array(n)
        return empty_like_type_datetime_date_arr
    if isinstance(arr, bodo.hiframes.time_ext.TimeArrayType):
        precision = arr.precision

        def empty_like_type_time_arr(n, arr):
            return bodo.hiframes.time_ext.alloc_time_array(n, precision)
        return empty_like_type_time_arr
    if (arr == bodo.hiframes.datetime_timedelta_ext.
        datetime_timedelta_array_type):

        def empty_like_type_datetime_timedelta_arr(n, arr):
            return (bodo.hiframes.datetime_timedelta_ext.
                alloc_datetime_timedelta_array(n))
        return empty_like_type_datetime_timedelta_arr
    if isinstance(arr, bodo.libs.decimal_arr_ext.DecimalArrayType):
        precision = arr.precision
        scale = arr.scale

        def empty_like_type_decimal_arr(n, arr):
            return bodo.libs.decimal_arr_ext.alloc_decimal_array(n,
                precision, scale)
        return empty_like_type_decimal_arr
    assert arr == string_array_type

    def empty_like_type_str_arr(n, arr):
        yvcq__jbjwv = 20
        if len(arr) != 0:
            yvcq__jbjwv = num_total_chars(arr) // len(arr)
        return pre_alloc_string_array(n, n * yvcq__jbjwv)
    return empty_like_type_str_arr


def _empty_nd_impl(context, builder, arrtype, shapes):
    fcwyh__nlitx = make_array(arrtype)
    ouae__chyvw = fcwyh__nlitx(context, builder)
    ubpec__guwi = context.get_data_type(arrtype.dtype)
    rpc__tague = context.get_constant(types.intp, get_itemsize(context,
        arrtype))
    qbke__zuntu = context.get_constant(types.intp, 1)
    cegfi__zqxpm = lir.Constant(lir.IntType(1), 0)
    for s in shapes:
        ldtyv__egy = builder.smul_with_overflow(qbke__zuntu, s)
        qbke__zuntu = builder.extract_value(ldtyv__egy, 0)
        cegfi__zqxpm = builder.or_(cegfi__zqxpm, builder.extract_value(
            ldtyv__egy, 1))
    if arrtype.ndim == 0:
        pqym__thzfm = ()
    elif arrtype.layout == 'C':
        pqym__thzfm = [rpc__tague]
        for hjf__tfuud in reversed(shapes[1:]):
            pqym__thzfm.append(builder.mul(pqym__thzfm[-1], hjf__tfuud))
        pqym__thzfm = tuple(reversed(pqym__thzfm))
    elif arrtype.layout == 'F':
        pqym__thzfm = [rpc__tague]
        for hjf__tfuud in shapes[:-1]:
            pqym__thzfm.append(builder.mul(pqym__thzfm[-1], hjf__tfuud))
        pqym__thzfm = tuple(pqym__thzfm)
    else:
        raise NotImplementedError(
            "Don't know how to allocate array with layout '{0}'.".format(
            arrtype.layout))
    lrmo__nmgra = builder.smul_with_overflow(qbke__zuntu, rpc__tague)
    qbyuu__nzv = builder.extract_value(lrmo__nmgra, 0)
    cegfi__zqxpm = builder.or_(cegfi__zqxpm, builder.extract_value(
        lrmo__nmgra, 1))
    with builder.if_then(cegfi__zqxpm, likely=False):
        cgutils.printf(builder,
            'array is too big; `arr.size * arr.dtype.itemsize` is larger than the maximum possible size.'
            )
    dtype = arrtype.dtype
    wtquj__iqba = context.get_preferred_array_alignment(dtype)
    nvww__ouqky = context.get_constant(types.uint32, wtquj__iqba)
    oixd__rej = context.nrt.meminfo_alloc_aligned(builder, size=qbyuu__nzv,
        align=nvww__ouqky)
    data = context.nrt.meminfo_data(builder, oixd__rej)
    qzers__jspvf = context.get_value_type(types.intp)
    qiiny__woxz = cgutils.pack_array(builder, shapes, ty=qzers__jspvf)
    xuyl__jmese = cgutils.pack_array(builder, pqym__thzfm, ty=qzers__jspvf)
    populate_array(ouae__chyvw, data=builder.bitcast(data, ubpec__guwi.
        as_pointer()), shape=qiiny__woxz, strides=xuyl__jmese, itemsize=
        rpc__tague, meminfo=oixd__rej)
    return ouae__chyvw


if bodo.numba_compat._check_numba_change:
    lines = inspect.getsource(numba.np.arrayobj._empty_nd_impl)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'b6a998927680caa35917a553c79704e9d813d8f1873d83a5f8513837c159fa29':
        warnings.warn('numba.np.arrayobj._empty_nd_impl has changed')


def alloc_arr_tup(n, arr_tup, init_vals=()):
    qijh__endi = []
    for uglfg__noz in arr_tup:
        qijh__endi.append(np.empty(n, uglfg__noz.dtype))
    return tuple(qijh__endi)


@overload(alloc_arr_tup, no_unliteral=True)
def alloc_arr_tup_overload(n, data, init_vals=()):
    dyx__xnl = data.count
    ubmq__hrmbg = ','.join(['empty_like_type(n, data[{}])'.format(
        wnib__yzuf) for wnib__yzuf in range(dyx__xnl)])
    if init_vals != ():
        ubmq__hrmbg = ','.join(['np.full(n, init_vals[{}], data[{}].dtype)'
            .format(wnib__yzuf, wnib__yzuf) for wnib__yzuf in range(dyx__xnl)])
    uqfa__owjb = 'def f(n, data, init_vals=()):\n'
    uqfa__owjb += '  return ({}{})\n'.format(ubmq__hrmbg, ',' if dyx__xnl ==
        1 else '')
    jiss__pea = {}
    exec(uqfa__owjb, {'empty_like_type': empty_like_type, 'np': np}, jiss__pea)
    oul__ceef = jiss__pea['f']
    return oul__ceef


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def tuple_to_scalar(n):
    if isinstance(n, types.BaseTuple) and len(n.types) == 1:
        return lambda n: n[0]
    return lambda n: n


def create_categorical_type(categories, data, is_ordered):
    if data == bodo.string_array_type or bodo.utils.typing.is_dtype_nullable(
        data):
        new_cats_arr = pd.CategoricalDtype(pd.array(categories), is_ordered
            ).categories.array
        if isinstance(data.dtype, types.Number):
            new_cats_arr = new_cats_arr.astype(data.
                get_pandas_scalar_type_instance)
    else:
        new_cats_arr = pd.CategoricalDtype(categories, is_ordered
            ).categories.values
        if isinstance(data.dtype, types.Number):
            new_cats_arr = new_cats_arr.astype(as_dtype(data.dtype))
    return new_cats_arr


def alloc_type(n, t, s=None):
    return np.empty(n, t.dtype)


@overload(alloc_type)
def overload_alloc_type(n, t, s=None):
    typ = t.instance_type if isinstance(t, types.TypeRef) else t
    if is_str_arr_type(typ):
        return (lambda n, t, s=None: bodo.libs.str_arr_ext.
            pre_alloc_string_array(n, s[0]))
    if typ == bodo.binary_array_type:
        return (lambda n, t, s=None: bodo.libs.binary_arr_ext.
            pre_alloc_binary_array(n, s[0]))
    if isinstance(typ, bodo.libs.array_item_arr_ext.ArrayItemArrayType):
        dtype = typ.dtype
        return (lambda n, t, s=None: bodo.libs.array_item_arr_ext.
            pre_alloc_array_item_array(n, s, dtype))
    if isinstance(typ, bodo.libs.struct_arr_ext.StructArrayType):
        dtypes = typ.data
        names = typ.names
        return (lambda n, t, s=None: bodo.libs.struct_arr_ext.
            pre_alloc_struct_array(n, s, dtypes, names))
    if isinstance(typ, bodo.libs.map_arr_ext.MapArrayType):
        struct_typ = bodo.libs.struct_arr_ext.StructArrayType((typ.
            key_arr_type, typ.value_arr_type), ('key', 'value'))
        return lambda n, t, s=None: bodo.libs.map_arr_ext.pre_alloc_map_array(n
            , s, struct_typ)
    if isinstance(typ, bodo.libs.tuple_arr_ext.TupleArrayType):
        dtypes = typ.data
        return (lambda n, t, s=None: bodo.libs.tuple_arr_ext.
            pre_alloc_tuple_array(n, s, dtypes))
    if isinstance(typ, bodo.hiframes.pd_categorical_ext.CategoricalArrayType):
        if isinstance(t, types.TypeRef):
            if typ.dtype.categories is None:
                raise BodoError(
                    'UDFs or Groupbys that return Categorical values must have categories known at compile time.'
                    )
            is_ordered = typ.dtype.ordered
            int_type = typ.dtype.int_type
            new_cats_arr = create_categorical_type(typ.dtype.categories,
                typ.dtype.data.data, is_ordered)
            new_cats_tup = MetaType(tuple(new_cats_arr))
            return (lambda n, t, s=None: bodo.hiframes.pd_categorical_ext.
                alloc_categorical_array(n, bodo.hiframes.pd_categorical_ext
                .init_cat_dtype(bodo.utils.conversion.index_from_array(
                new_cats_arr), is_ordered, int_type, new_cats_tup)))
        else:
            return (lambda n, t, s=None: bodo.hiframes.pd_categorical_ext.
                alloc_categorical_array(n, t.dtype))
    if typ.dtype == bodo.hiframes.datetime_date_ext.datetime_date_type:
        return (lambda n, t, s=None: bodo.hiframes.datetime_date_ext.
            alloc_datetime_date_array(n))
    if isinstance(typ.dtype, bodo.hiframes.time_ext.TimeType):
        precision = typ.dtype.precision
        return lambda n, t, s=None: bodo.hiframes.time_ext.alloc_time_array(n,
            precision)
    if (typ.dtype == bodo.hiframes.datetime_timedelta_ext.
        datetime_timedelta_type):
        return (lambda n, t, s=None: bodo.hiframes.datetime_timedelta_ext.
            alloc_datetime_timedelta_array(n))
    if isinstance(typ, DecimalArrayType):
        precision = typ.dtype.precision
        scale = typ.dtype.scale
        return (lambda n, t, s=None: bodo.libs.decimal_arr_ext.
            alloc_decimal_array(n, precision, scale))
    if isinstance(typ, bodo.DatetimeArrayType):
        tz_literal = typ.tz
        return (lambda n, t, s=None: bodo.libs.pd_datetime_arr_ext.
            alloc_pd_datetime_array(n, tz_literal))
    dtype = numba.np.numpy_support.as_dtype(typ.dtype)
    if isinstance(typ, IntegerArrayType):
        return lambda n, t, s=None: bodo.libs.int_arr_ext.alloc_int_array(n,
            dtype)
    if isinstance(typ, FloatingArrayType):
        return lambda n, t, s=None: bodo.libs.float_arr_ext.alloc_float_array(n
            , dtype)
    if typ == boolean_array:
        return lambda n, t, s=None: bodo.libs.bool_arr_ext.alloc_bool_array(n)
    return lambda n, t, s=None: np.empty(n, dtype)


def astype(A, t):
    return A.astype(t.dtype)


@overload(astype, no_unliteral=True)
def overload_astype(A, t):
    typ = t.instance_type if isinstance(t, types.TypeRef) else t
    dtype = typ.dtype
    if A == typ:
        return lambda A, t: A
    if isinstance(A, (types.Array, IntegerArrayType, FloatingArrayType)
        ) and isinstance(typ, types.Array):
        return lambda A, t: A.astype(dtype)
    if isinstance(typ, IntegerArrayType):
        return lambda A, t: bodo.libs.int_arr_ext.init_integer_array(A.
            astype(dtype), np.full(len(A) + 7 >> 3, 255, np.uint8))
    if isinstance(typ, FloatingArrayType):
        return lambda A, t: bodo.libs.float_arr_ext.init_float_array(A.
            astype(dtype), np.full(len(A) + 7 >> 3, 255, np.uint8))
    if (A == bodo.libs.dict_arr_ext.dict_str_arr_type and typ == bodo.
        string_array_type):
        return lambda A, t: bodo.utils.typing.decode_if_dict_array(A)
    raise BodoError(f'cannot convert array type {A} to {typ}')


def full_type(n, val, t):
    return np.full(n, val, t.dtype)


@overload(full_type, no_unliteral=True)
def overload_full_type(n, val, t):
    typ = t.instance_type if isinstance(t, types.TypeRef) else t
    if isinstance(typ, types.Array):
        dtype = numba.np.numpy_support.as_dtype(typ.dtype)
        return lambda n, val, t: np.full(n, val, dtype)
    if isinstance(typ, IntegerArrayType):
        dtype = numba.np.numpy_support.as_dtype(typ.dtype)
        return lambda n, val, t: bodo.libs.int_arr_ext.init_integer_array(np
            .full(n, val, dtype), np.full(tuple_to_scalar(n) + 7 >> 3, 255,
            np.uint8))
    if isinstance(typ, FloatingArrayType):
        dtype = numba.np.numpy_support.as_dtype(typ.dtype)
        return lambda n, val, t: bodo.libs.float_arr_ext.init_float_array(np
            .full(n, val, dtype), np.full(tuple_to_scalar(n) + 7 >> 3, 255,
            np.uint8))
    if typ == boolean_array:
        return lambda n, val, t: bodo.libs.bool_arr_ext.init_bool_array(np.
            full(n, val, np.bool_), np.full(tuple_to_scalar(n) + 7 >> 3, 
            255, np.uint8))
    if typ == string_array_type:

        def impl_str(n, val, t):
            hed__kgfo = n * bodo.libs.str_arr_ext.get_utf8_size(val)
            A = pre_alloc_string_array(n, hed__kgfo)
            for wnib__yzuf in range(n):
                A[wnib__yzuf] = val
            return A
        return impl_str

    def impl(n, val, t):
        A = alloc_type(n, typ, (-1,))
        for wnib__yzuf in range(n):
            A[wnib__yzuf] = val
        return A
    return impl


@intrinsic
def is_null_pointer(typingctx, ptr_typ=None):

    def codegen(context, builder, signature, args):
        ztae__gjug, = args
        vqmqs__bsp = context.get_constant_null(ptr_typ)
        return builder.icmp_unsigned('==', ztae__gjug, vqmqs__bsp)
    return types.bool_(ptr_typ), codegen


@intrinsic
def is_null_value(typingctx, val_typ=None):

    def codegen(context, builder, signature, args):
        val, = args
        qmr__xpiwz = cgutils.alloca_once_value(builder, val)
        bspnx__lcp = cgutils.alloca_once_value(builder, context.
            get_constant_null(val_typ))
        return is_ll_eq(builder, qmr__xpiwz, bspnx__lcp)
    return types.bool_(val_typ), codegen


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def tuple_list_to_array(A, data, elem_type):
    elem_type = elem_type.instance_type if isinstance(elem_type, types.TypeRef
        ) else elem_type
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(A,
        'tuple_list_to_array()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(elem_type,
        'tuple_list_to_array()')
    uqfa__owjb = 'def impl(A, data, elem_type):\n'
    uqfa__owjb += '  for i, d in enumerate(data):\n'
    if elem_type == bodo.hiframes.pd_timestamp_ext.pd_timestamp_tz_naive_type:
        uqfa__owjb += (
            '    A[i] = bodo.utils.conversion.unbox_if_tz_naive_timestamp(d)\n'
            )
    else:
        uqfa__owjb += '    A[i] = d\n'
    jiss__pea = {}
    exec(uqfa__owjb, {'bodo': bodo}, jiss__pea)
    impl = jiss__pea['impl']
    return impl


def object_length(c, obj):
    byb__jpvd = c.context.get_argument_type(types.pyobject)
    wyft__cax = lir.FunctionType(lir.IntType(64), [byb__jpvd])
    zuns__igsvn = cgutils.get_or_insert_function(c.builder.module,
        wyft__cax, name='PyObject_Length')
    return c.builder.call(zuns__igsvn, (obj,))


@intrinsic
def incref(typingctx, data=None):

    def codegen(context, builder, signature, args):
        acv__kdl, = args
        context.nrt.incref(builder, signature.args[0], acv__kdl)
    return types.void(data), codegen


def gen_getitem(out_var, in_var, ind, calltypes, nodes):
    cqxnc__tpvs = out_var.loc
    ezow__vvkzx = ir.Expr.static_getitem(in_var, ind, None, cqxnc__tpvs)
    calltypes[ezow__vvkzx] = None
    nodes.append(ir.Assign(ezow__vvkzx, out_var, cqxnc__tpvs))


def is_static_getsetitem(node):
    return is_expr(node, 'static_getitem') or isinstance(node, ir.StaticSetItem
        )


def get_getsetitem_index_var(node, typemap, nodes):
    index_var = node.index_var if is_static_getsetitem(node) else node.index
    if index_var is None:
        assert is_static_getsetitem(node)
        try:
            mya__gcu = types.literal(node.index)
        except:
            mya__gcu = numba.typeof(node.index)
        index_var = ir.Var(node.value.scope, ir_utils.mk_unique_var(
            'dummy_index'), node.loc)
        typemap[index_var.name] = mya__gcu
        nodes.append(ir.Assign(ir.Const(node.index, node.loc), index_var,
            node.loc))
    return index_var


import copy
ir.Const.__deepcopy__ = lambda self, memo: ir.Const(self.value, copy.
    deepcopy(self.loc))


def is_call_assign(stmt):
    return isinstance(stmt, ir.Assign) and isinstance(stmt.value, ir.Expr
        ) and stmt.value.op == 'call'


def is_call(expr) ->bool:
    return isinstance(expr, ir.Expr) and expr.op == 'call'


def is_var_assign(inst):
    return isinstance(inst, ir.Assign) and isinstance(inst.value, ir.Var)


def is_assign(inst) ->bool:
    return isinstance(inst, ir.Assign)


def is_expr(val, op) ->bool:
    return isinstance(val, ir.Expr) and val.op == op


def sanitize_varname(varname):
    if isinstance(varname, (tuple, list)):
        varname = '_'.join(sanitize_varname(v) for v in varname)
    varname = str(varname)
    mevsr__kpk = re.sub('\\W+', '_', varname)
    if not mevsr__kpk or not mevsr__kpk[0].isalpha():
        mevsr__kpk = '_' + mevsr__kpk
    if not mevsr__kpk.isidentifier() or keyword.iskeyword(mevsr__kpk):
        mevsr__kpk = mk_unique_var('new_name').replace('.', '_')
    return mevsr__kpk


def dump_node_list(node_list):
    for n in node_list:
        print('   ', n)


def debug_prints():
    return numba.core.config.DEBUG_ARRAY_OPT == 1


@overload(reversed)
def list_reverse(A):
    if isinstance(A, types.List):

        def impl_reversed(A):
            zdev__tkjcq = len(A)
            for wnib__yzuf in range(zdev__tkjcq):
                yield A[zdev__tkjcq - 1 - wnib__yzuf]
        return impl_reversed


@numba.njit
def count_nonnan(a):
    return np.count_nonzero(~np.isnan(a))


@numba.njit
def nanvar_ddof1(a):
    eqpv__tqins = count_nonnan(a)
    if eqpv__tqins <= 1:
        return np.nan
    return np.nanvar(a) * (eqpv__tqins / (eqpv__tqins - 1))


@numba.njit
def nanstd_ddof1(a):
    return np.sqrt(nanvar_ddof1(a))


def has_supported_h5py():
    try:
        import h5py
        from bodo.io import _hdf5
    except ImportError as gqsx__qcji:
        ade__anytf = False
    else:
        ade__anytf = h5py.version.hdf5_version_tuple[1] in (10, 12)
    return ade__anytf


def check_h5py():
    if not has_supported_h5py():
        raise BodoError("install 'h5py' package to enable hdf5 support")


def has_pyarrow():
    try:
        import pyarrow
    except ImportError as gqsx__qcji:
        ivl__wknhs = False
    else:
        ivl__wknhs = True
    return ivl__wknhs


def has_scipy():
    try:
        import scipy
    except ImportError as gqsx__qcji:
        dwpzt__ypuel = False
    else:
        dwpzt__ypuel = True
    return dwpzt__ypuel


@intrinsic
def check_and_propagate_cpp_exception(typingctx):

    def codegen(context, builder, sig, args):
        yexh__set = context.get_python_api(builder)
        mizmg__bjfvf = yexh__set.err_occurred()
        kfsmm__uemut = cgutils.is_not_null(builder, mizmg__bjfvf)
        with builder.if_then(kfsmm__uemut):
            builder.ret(numba.core.callconv.RETCODE_EXC)
    return types.void(), codegen


def inlined_check_and_propagate_cpp_exception(context, builder):
    yexh__set = context.get_python_api(builder)
    mizmg__bjfvf = yexh__set.err_occurred()
    kfsmm__uemut = cgutils.is_not_null(builder, mizmg__bjfvf)
    with builder.if_then(kfsmm__uemut):
        builder.ret(numba.core.callconv.RETCODE_EXC)


@numba.njit
def check_java_installation(fname):
    with numba.objmode():
        check_java_installation_(fname)


def check_java_installation_(fname):
    if not fname.startswith('hdfs://'):
        return
    import shutil
    if not shutil.which('java'):
        zai__qho = (
            "Java not found. Make sure openjdk is installed for hdfs. openjdk can be installed by calling 'conda install 'openjdk>=9.0,<12' -c conda-forge'."
            )
        raise BodoError(zai__qho)


dt_err = """
        If you are trying to set NULL values for timedelta64 in regular Python, 

        consider using np.timedelta64('nat') instead of None
        """


@lower_constant(types.List)
def lower_constant_list(context, builder, typ, pyval):
    if len(pyval) > CONST_LIST_SLOW_WARN_THRESHOLD:
        warnings.warn(BodoWarning(
            'Using large global lists can result in long compilation times. Please pass large lists as arguments to JIT functions or use arrays.'
            ))
    rym__trbrs = []
    for a in pyval:
        if bodo.typeof(a) != typ.dtype:
            raise BodoError(
                f'Values in list must have the same data type for type stability. Expected: {typ.dtype}, Actual: {bodo.typeof(a)}'
                )
        rym__trbrs.append(context.get_constant_generic(builder, typ.dtype, a))
    avx__jfu = context.get_constant_generic(builder, types.int64, len(pyval))
    fbgt__kdvn = context.get_constant_generic(builder, types.bool_, False)
    syham__jyuw = context.get_constant_null(types.pyobject)
    vfjhs__rarwk = lir.Constant.literal_struct([avx__jfu, avx__jfu,
        fbgt__kdvn] + rym__trbrs)
    vfjhs__rarwk = cgutils.global_constant(builder, '.const.payload',
        vfjhs__rarwk).bitcast(cgutils.voidptr_t)
    vcpn__gplib = context.get_constant(types.int64, -1)
    yjx__qde = context.get_constant_null(types.voidptr)
    oixd__rej = lir.Constant.literal_struct([vcpn__gplib, yjx__qde,
        yjx__qde, vfjhs__rarwk, vcpn__gplib])
    oixd__rej = cgutils.global_constant(builder, '.const.meminfo', oixd__rej
        ).bitcast(cgutils.voidptr_t)
    return lir.Constant.literal_struct([oixd__rej, syham__jyuw])


@lower_constant(types.Set)
def lower_constant_set(context, builder, typ, pyval):
    for a in pyval:
        if bodo.typeof(a) != typ.dtype:
            raise BodoError(
                f'Values in set must have the same data type for type stability. Expected: {typ.dtype}, Actual: {bodo.typeof(a)}'
                )
    ivdut__nuvhi = types.List(typ.dtype)
    ivpkp__kzo = context.get_constant_generic(builder, ivdut__nuvhi, list(
        pyval))
    fepay__pyx = context.compile_internal(builder, lambda l: set(l), types.
        Set(typ.dtype)(ivdut__nuvhi), [ivpkp__kzo])
    return fepay__pyx


def lower_const_dict_fast_path(context, builder, typ, pyval):
    from bodo.utils.typing import can_replace
    nkq__jiigb = pd.Series(pyval.keys()).values
    ikw__gijb = pd.Series(pyval.values()).values
    fwja__tgsk = bodo.typeof(nkq__jiigb)
    pje__hgmj = bodo.typeof(ikw__gijb)
    require(fwja__tgsk.dtype == typ.key_type or can_replace(typ.key_type,
        fwja__tgsk.dtype))
    require(pje__hgmj.dtype == typ.value_type or can_replace(typ.value_type,
        pje__hgmj.dtype))
    ejt__lxjrn = context.get_constant_generic(builder, fwja__tgsk, nkq__jiigb)
    xgl__ffl = context.get_constant_generic(builder, pje__hgmj, ikw__gijb)

    def create_dict(keys, vals):
        qlof__htd = {}
        for k, v in zip(keys, vals):
            qlof__htd[k] = v
        return qlof__htd
    uqji__xkgo = context.compile_internal(builder, create_dict, typ(
        fwja__tgsk, pje__hgmj), [ejt__lxjrn, xgl__ffl])
    return uqji__xkgo


@lower_constant(types.DictType)
def lower_constant_dict(context, builder, typ, pyval):
    try:
        return lower_const_dict_fast_path(context, builder, typ, pyval)
    except:
        pass
    if len(pyval) > CONST_DICT_SLOW_WARN_THRESHOLD:
        warnings.warn(BodoWarning(
            'Using large global dictionaries can result in long compilation times. Please pass large dictionaries as arguments to JIT functions.'
            ))
    tvcwi__vhhkt = typ.key_type
    gbl__mcj = typ.value_type

    def make_dict():
        return numba.typed.Dict.empty(tvcwi__vhhkt, gbl__mcj)
    uqji__xkgo = context.compile_internal(builder, make_dict, typ(), [])

    def set_dict_val(d, k, v):
        d[k] = v
    for k, v in pyval.items():
        rbddv__hwss = context.get_constant_generic(builder, tvcwi__vhhkt, k)
        wqok__sge = context.get_constant_generic(builder, gbl__mcj, v)
        context.compile_internal(builder, set_dict_val, types.none(typ,
            tvcwi__vhhkt, gbl__mcj), [uqji__xkgo, rbddv__hwss, wqok__sge])
    return uqji__xkgo


def synchronize_error(exception_str, error_message):
    if exception_str == 'ValueError':
        eidkz__txit = ValueError
    else:
        eidkz__txit = RuntimeError
    fsl__kbmng = MPI.COMM_WORLD
    if fsl__kbmng.allreduce(error_message != '', op=MPI.LOR):
        for error_message in fsl__kbmng.allgather(error_message):
            if error_message:
                raise eidkz__txit(error_message)


@numba.njit
def synchronize_error_njit(exception_str, error_message):
    with numba.objmode():
        synchronize_error(exception_str, error_message)
