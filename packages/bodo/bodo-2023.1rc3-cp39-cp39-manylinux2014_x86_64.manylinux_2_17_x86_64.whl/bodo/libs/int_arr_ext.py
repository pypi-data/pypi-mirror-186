"""Nullable integer array corresponding to Pandas IntegerArray.
However, nulls are stored in bit arrays similar to Arrow's arrays.
"""
import operator
import llvmlite.binding as ll
import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.imputils import lower_constant
from numba.extending import NativeValue, box, intrinsic, lower_builtin, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_model, type_callable, typeof_impl, unbox
from numba.parfors.array_analysis import ArrayAnalysis
import bodo
from bodo.libs.str_arr_ext import kBitmask
from bodo.libs import array_ext, hstr_ext
ll.add_symbol('mask_arr_to_bitmap', hstr_ext.mask_arr_to_bitmap)
ll.add_symbol('is_pd_int_array', array_ext.is_pd_int_array)
ll.add_symbol('int_array_from_sequence', array_ext.int_array_from_sequence)
from bodo.hiframes.datetime_timedelta_ext import pd_timedelta_type
from bodo.utils.indexing import array_getitem_bool_index, array_getitem_int_index, array_getitem_slice_index, array_setitem_bool_index, array_setitem_int_index, array_setitem_slice_index
from bodo.utils.typing import BodoError, check_unsupported_args, is_iterable_type, is_list_like_index_type, is_overload_false, is_overload_none, is_overload_true, parse_dtype, raise_bodo_error, to_nullable_type


class IntegerArrayType(types.ArrayCompatible):

    def __init__(self, dtype):
        self.dtype = dtype
        super(IntegerArrayType, self).__init__(name=
            f'IntegerArrayType({dtype})')

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    def copy(self):
        return IntegerArrayType(self.dtype)

    @property
    def get_pandas_scalar_type_instance(self):
        xyy__rbfqu = int(np.log2(self.dtype.bitwidth // 8))
        fbs__cgta = 0 if self.dtype.signed else 4
        idx = xyy__rbfqu + fbs__cgta
        return pd_int_dtype_classes[idx]()


@register_model(IntegerArrayType)
class IntegerArrayModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        ukw__pui = [('data', types.Array(fe_type.dtype, 1, 'C')), (
            'null_bitmap', types.Array(types.uint8, 1, 'C'))]
        models.StructModel.__init__(self, dmm, fe_type, ukw__pui)


make_attribute_wrapper(IntegerArrayType, 'data', '_data')
make_attribute_wrapper(IntegerArrayType, 'null_bitmap', '_null_bitmap')


@typeof_impl.register(pd.arrays.IntegerArray)
def _typeof_pd_int_array(val, c):
    gsep__vads = 8 * val.dtype.itemsize
    oxqm__zdox = '' if val.dtype.kind == 'i' else 'u'
    dtype = getattr(types, '{}int{}'.format(oxqm__zdox, gsep__vads))
    return IntegerArrayType(dtype)


class IntDtype(types.Number):

    def __init__(self, dtype):
        assert isinstance(dtype, types.Integer)
        self.dtype = dtype
        rqfo__gyisr = '{}Int{}Dtype()'.format('' if dtype.signed else 'U',
            dtype.bitwidth)
        super(IntDtype, self).__init__(rqfo__gyisr)


register_model(IntDtype)(models.OpaqueModel)


@box(IntDtype)
def box_intdtype(typ, val, c):
    cout__yezf = c.context.insert_const_string(c.builder.module, 'pandas')
    bbmyt__spgk = c.pyapi.import_module_noblock(cout__yezf)
    wfx__qmrl = c.pyapi.call_method(bbmyt__spgk, str(typ)[:-2], ())
    c.pyapi.decref(bbmyt__spgk)
    return wfx__qmrl


@unbox(IntDtype)
def unbox_intdtype(typ, val, c):
    return NativeValue(c.context.get_dummy_value())


def typeof_pd_int_dtype(val, c):
    gsep__vads = 8 * val.itemsize
    oxqm__zdox = '' if val.kind == 'i' else 'u'
    dtype = getattr(types, '{}int{}'.format(oxqm__zdox, gsep__vads))
    return IntDtype(dtype)


def _register_int_dtype(t):
    typeof_impl.register(t)(typeof_pd_int_dtype)
    int_dtype = typeof_pd_int_dtype(t(), None)
    type_callable(t)(lambda c: lambda : int_dtype)
    lower_builtin(t)(lambda c, b, s, a: c.get_dummy_value())


pd_int_dtype_classes = (pd.Int8Dtype, pd.Int16Dtype, pd.Int32Dtype, pd.
    Int64Dtype, pd.UInt8Dtype, pd.UInt16Dtype, pd.UInt32Dtype, pd.UInt64Dtype)
for t in pd_int_dtype_classes:
    _register_int_dtype(t)


@numba.extending.register_jitable
def mask_arr_to_bitmap(mask_arr):
    n = len(mask_arr)
    eww__ucgfj = n + 7 >> 3
    ujmxj__bjaaf = np.empty(eww__ucgfj, np.uint8)
    for i in range(n):
        pamz__tfrpz = i // 8
        ujmxj__bjaaf[pamz__tfrpz] ^= np.uint8(-np.uint8(not mask_arr[i]) ^
            ujmxj__bjaaf[pamz__tfrpz]) & kBitmask[i % 8]
    return ujmxj__bjaaf


@unbox(IntegerArrayType)
def unbox_int_array(typ, obj, c):
    hlcz__rou = c.pyapi.call_method(obj, '__len__', ())
    n = c.pyapi.long_as_longlong(hlcz__rou)
    c.pyapi.decref(hlcz__rou)
    gpn__sfgjb = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    eww__ucgfj = c.builder.udiv(c.builder.add(n, lir.Constant(lir.IntType(
        64), 7)), lir.Constant(lir.IntType(64), 8))
    peb__yxy = bodo.utils.utils._empty_nd_impl(c.context, c.builder, types.
        Array(types.uint8, 1, 'C'), [eww__ucgfj])
    wni__nonu = lir.FunctionType(lir.IntType(32), [lir.IntType(8).as_pointer()]
        )
    wtnqu__hiapl = cgutils.get_or_insert_function(c.builder.module,
        wni__nonu, name='is_pd_int_array')
    focd__uktqh = c.builder.call(wtnqu__hiapl, [obj])
    fvdhz__qdy = c.builder.icmp_unsigned('!=', focd__uktqh, focd__uktqh.type(0)
        )
    with c.builder.if_else(fvdhz__qdy) as (vcvth__dstdc, tjypj__czu):
        with vcvth__dstdc:
            fkd__asi = c.pyapi.object_getattr_string(obj, '_data')
            gpn__sfgjb.data = c.pyapi.to_native_value(types.Array(typ.dtype,
                1, 'C'), fkd__asi).value
            fmgx__gle = c.pyapi.object_getattr_string(obj, '_mask')
            mask_arr = c.pyapi.to_native_value(types.Array(types.bool_, 1,
                'C'), fmgx__gle).value
            c.pyapi.decref(fkd__asi)
            c.pyapi.decref(fmgx__gle)
            famr__lfxb = c.context.make_array(types.Array(types.bool_, 1, 'C')
                )(c.context, c.builder, mask_arr)
            wni__nonu = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
                as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(64)])
            wtnqu__hiapl = cgutils.get_or_insert_function(c.builder.module,
                wni__nonu, name='mask_arr_to_bitmap')
            c.builder.call(wtnqu__hiapl, [peb__yxy.data, famr__lfxb.data, n])
            c.context.nrt.decref(c.builder, types.Array(types.bool_, 1, 'C'
                ), mask_arr)
        with tjypj__czu:
            azjq__auyju = bodo.utils.utils._empty_nd_impl(c.context, c.
                builder, types.Array(typ.dtype, 1, 'C'), [n])
            wni__nonu = lir.FunctionType(lir.IntType(32), [lir.IntType(8).
                as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(8).
                as_pointer()])
            pdm__mdhhn = cgutils.get_or_insert_function(c.builder.module,
                wni__nonu, name='int_array_from_sequence')
            c.builder.call(pdm__mdhhn, [obj, c.builder.bitcast(azjq__auyju.
                data, lir.IntType(8).as_pointer()), peb__yxy.data])
            gpn__sfgjb.data = azjq__auyju._getvalue()
    gpn__sfgjb.null_bitmap = peb__yxy._getvalue()
    hong__ubpuu = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(gpn__sfgjb._getvalue(), is_error=hong__ubpuu)


@box(IntegerArrayType)
def box_int_arr(typ, val, c):
    gpn__sfgjb = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    data = c.pyapi.from_native_value(types.Array(typ.dtype, 1, 'C'),
        gpn__sfgjb.data, c.env_manager)
    tlm__dgep = c.context.make_array(types.Array(types.uint8, 1, 'C'))(c.
        context, c.builder, gpn__sfgjb.null_bitmap).data
    hlcz__rou = c.pyapi.call_method(data, '__len__', ())
    n = c.pyapi.long_as_longlong(hlcz__rou)
    cout__yezf = c.context.insert_const_string(c.builder.module, 'numpy')
    hpfw__mcqb = c.pyapi.import_module_noblock(cout__yezf)
    nsirr__auv = c.pyapi.object_getattr_string(hpfw__mcqb, 'bool_')
    mask_arr = c.pyapi.call_method(hpfw__mcqb, 'empty', (hlcz__rou, nsirr__auv)
        )
    igid__nou = c.pyapi.object_getattr_string(mask_arr, 'ctypes')
    ovmyb__zap = c.pyapi.object_getattr_string(igid__nou, 'data')
    jbdd__rmive = c.builder.inttoptr(c.pyapi.long_as_longlong(ovmyb__zap),
        lir.IntType(8).as_pointer())
    with cgutils.for_range(c.builder, n) as ayyjo__dziq:
        i = ayyjo__dziq.index
        ypc__vrli = c.builder.lshr(i, lir.Constant(lir.IntType(64), 3))
        sfk__fbng = c.builder.load(cgutils.gep(c.builder, tlm__dgep, ypc__vrli)
            )
        uat__fttr = c.builder.trunc(c.builder.and_(i, lir.Constant(lir.
            IntType(64), 7)), lir.IntType(8))
        val = c.builder.and_(c.builder.lshr(sfk__fbng, uat__fttr), lir.
            Constant(lir.IntType(8), 1))
        val = c.builder.xor(val, lir.Constant(lir.IntType(8), 1))
        uuzvc__nmdoh = cgutils.gep(c.builder, jbdd__rmive, i)
        c.builder.store(val, uuzvc__nmdoh)
    c.context.nrt.decref(c.builder, types.Array(types.uint8, 1, 'C'),
        gpn__sfgjb.null_bitmap)
    cout__yezf = c.context.insert_const_string(c.builder.module, 'pandas')
    bbmyt__spgk = c.pyapi.import_module_noblock(cout__yezf)
    unjpa__qywl = c.pyapi.object_getattr_string(bbmyt__spgk, 'arrays')
    wfx__qmrl = c.pyapi.call_method(unjpa__qywl, 'IntegerArray', (data,
        mask_arr))
    c.pyapi.decref(bbmyt__spgk)
    c.pyapi.decref(hlcz__rou)
    c.pyapi.decref(hpfw__mcqb)
    c.pyapi.decref(nsirr__auv)
    c.pyapi.decref(igid__nou)
    c.pyapi.decref(ovmyb__zap)
    c.pyapi.decref(unjpa__qywl)
    c.pyapi.decref(data)
    c.pyapi.decref(mask_arr)
    return wfx__qmrl


@intrinsic
def init_integer_array(typingctx, data, null_bitmap=None):
    assert isinstance(data, types.Array)
    assert null_bitmap == types.Array(types.uint8, 1, 'C')

    def codegen(context, builder, signature, args):
        ltbi__cbxs, nojh__rgzhz = args
        gpn__sfgjb = cgutils.create_struct_proxy(signature.return_type)(context
            , builder)
        gpn__sfgjb.data = ltbi__cbxs
        gpn__sfgjb.null_bitmap = nojh__rgzhz
        context.nrt.incref(builder, signature.args[0], ltbi__cbxs)
        context.nrt.incref(builder, signature.args[1], nojh__rgzhz)
        return gpn__sfgjb._getvalue()
    mlab__vbrfq = IntegerArrayType(data.dtype)
    tvvsm__ytac = mlab__vbrfq(data, null_bitmap)
    return tvvsm__ytac, codegen


@lower_constant(IntegerArrayType)
def lower_constant_int_arr(context, builder, typ, pyval):
    n = len(pyval)
    ius__kfkq = np.empty(n, pyval.dtype.type)
    rpgbx__eky = np.empty(n + 7 >> 3, np.uint8)
    for i, s in enumerate(pyval):
        giw__xehk = pd.isna(s)
        bodo.libs.int_arr_ext.set_bit_to_arr(rpgbx__eky, i, int(not giw__xehk))
        if not giw__xehk:
            ius__kfkq[i] = s
    yda__zqbg = context.get_constant_generic(builder, types.Array(typ.dtype,
        1, 'C'), ius__kfkq)
    obli__hibj = context.get_constant_generic(builder, types.Array(types.
        uint8, 1, 'C'), rpgbx__eky)
    return lir.Constant.literal_struct([yda__zqbg, obli__hibj])


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def get_int_arr_data(A):
    return lambda A: A._data


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def get_int_arr_bitmap(A):
    return lambda A: A._null_bitmap


def get_int_arr_data_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 1 and not kws
    jtkdk__ict = args[0]
    if equiv_set.has_shape(jtkdk__ict):
        return ArrayAnalysis.AnalyzeResult(shape=jtkdk__ict, pre=[])
    return None


ArrayAnalysis._analyze_op_call_bodo_libs_int_arr_ext_get_int_arr_data = (
    get_int_arr_data_equiv)


def init_integer_array_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 2 and not kws
    jtkdk__ict = args[0]
    if equiv_set.has_shape(jtkdk__ict):
        return ArrayAnalysis.AnalyzeResult(shape=jtkdk__ict, pre=[])
    return None


ArrayAnalysis._analyze_op_call_bodo_libs_int_arr_ext_init_integer_array = (
    init_integer_array_equiv)


def alias_ext_dummy_func(lhs_name, args, alias_map, arg_aliases):
    assert len(args) >= 1
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)


def alias_ext_init_integer_array(lhs_name, args, alias_map, arg_aliases):
    assert len(args) == 2
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)
    numba.core.ir_utils._add_alias(lhs_name, args[1].name, alias_map,
        arg_aliases)


numba.core.ir_utils.alias_func_extensions['init_integer_array',
    'bodo.libs.int_arr_ext'] = alias_ext_init_integer_array
numba.core.ir_utils.alias_func_extensions['get_int_arr_data',
    'bodo.libs.int_arr_ext'] = alias_ext_dummy_func
numba.core.ir_utils.alias_func_extensions['get_int_arr_bitmap',
    'bodo.libs.int_arr_ext'] = alias_ext_dummy_func


@numba.njit(no_cpython_wrapper=True)
def alloc_int_array(n, dtype):
    ius__kfkq = np.empty(n, dtype)
    zyspl__yho = np.empty(n + 7 >> 3, dtype=np.uint8)
    return init_integer_array(ius__kfkq, zyspl__yho)


def alloc_int_array_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 2 and not kws
    return ArrayAnalysis.AnalyzeResult(shape=args[0], pre=[])


ArrayAnalysis._analyze_op_call_bodo_libs_int_arr_ext_alloc_int_array = (
    alloc_int_array_equiv)


@numba.extending.register_jitable
def set_bit_to_arr(bits, i, bit_is_set):
    bits[i // 8] ^= np.uint8(-np.uint8(bit_is_set) ^ bits[i // 8]) & kBitmask[
        i % 8]


@numba.extending.register_jitable
def get_bit_bitmap_arr(bits, i):
    return bits[i >> 3] >> (i & 7) & 1


@overload(operator.getitem, no_unliteral=True)
def int_arr_getitem(A, ind):
    if not isinstance(A, IntegerArrayType):
        return
    if isinstance(ind, types.Integer):
        return lambda A, ind: A._data[ind]
    if ind != bodo.boolean_array and is_list_like_index_type(ind
        ) and ind.dtype == types.bool_:

        def impl_bool(A, ind):
            qqmwo__oyql, vwtag__hclls = array_getitem_bool_index(A, ind)
            return init_integer_array(qqmwo__oyql, vwtag__hclls)
        return impl_bool
    if is_list_like_index_type(ind) and isinstance(ind.dtype, types.Integer):

        def impl(A, ind):
            qqmwo__oyql, vwtag__hclls = array_getitem_int_index(A, ind)
            return init_integer_array(qqmwo__oyql, vwtag__hclls)
        return impl
    if isinstance(ind, types.SliceType):

        def impl_slice(A, ind):
            qqmwo__oyql, vwtag__hclls = array_getitem_slice_index(A, ind)
            return init_integer_array(qqmwo__oyql, vwtag__hclls)
        return impl_slice
    if ind != bodo.boolean_array:
        raise BodoError(
            f'getitem for IntegerArray with indexing type {ind} not supported.'
            )


@overload(operator.setitem, no_unliteral=True)
def int_arr_setitem(A, idx, val):
    if not isinstance(A, IntegerArrayType):
        return
    if val == types.none or isinstance(val, types.optional):
        return
    liv__eelva = (
        f"setitem for IntegerArray with indexing type {idx} received an incorrect 'value' type {val}."
        )
    pqla__yaug = isinstance(val, (types.Integer, types.Boolean, types.Float))
    if isinstance(idx, types.Integer):
        if pqla__yaug:

            def impl_scalar(A, idx, val):
                A._data[idx] = val
                bodo.libs.int_arr_ext.set_bit_to_arr(A._null_bitmap, idx, 1)
            return impl_scalar
        else:
            raise BodoError(liv__eelva)
    if not (is_iterable_type(val) and isinstance(val.dtype, (types.Integer,
        types.Boolean)) or pqla__yaug):
        raise BodoError(liv__eelva)
    if is_list_like_index_type(idx) and isinstance(idx.dtype, types.Integer):

        def impl_arr_ind_mask(A, idx, val):
            array_setitem_int_index(A, idx, val)
        return impl_arr_ind_mask
    if is_list_like_index_type(idx) and idx.dtype == types.bool_:

        def impl_bool_ind_mask(A, idx, val):
            array_setitem_bool_index(A, idx, val)
        return impl_bool_ind_mask
    if isinstance(idx, types.SliceType):

        def impl_slice_mask(A, idx, val):
            array_setitem_slice_index(A, idx, val)
        return impl_slice_mask
    raise BodoError(
        f'setitem for IntegerArray with indexing type {idx} not supported.')


@overload(len, no_unliteral=True)
def overload_int_arr_len(A):
    if isinstance(A, IntegerArrayType):
        return lambda A: len(A._data)


@overload_attribute(IntegerArrayType, 'shape')
def overload_int_arr_shape(A):
    return lambda A: (len(A._data),)


@overload_attribute(IntegerArrayType, 'dtype')
def overload_int_arr_dtype(A):
    dtype_class = getattr(pd, '{}Int{}Dtype'.format('' if A.dtype.signed else
        'U', A.dtype.bitwidth))
    return lambda A: dtype_class()


@overload_attribute(IntegerArrayType, 'ndim')
def overload_int_arr_ndim(A):
    return lambda A: 1


@overload_attribute(IntegerArrayType, 'nbytes')
def int_arr_nbytes_overload(A):
    return lambda A: A._data.nbytes + A._null_bitmap.nbytes


@overload_method(IntegerArrayType, 'copy', no_unliteral=True)
def overload_int_arr_copy(A, dtype=None):
    if not is_overload_none(dtype):
        return lambda A, dtype=None: A.astype(dtype, copy=True)
    else:
        return lambda A, dtype=None: bodo.libs.int_arr_ext.init_integer_array(
            bodo.libs.int_arr_ext.get_int_arr_data(A).copy(), bodo.libs.
            int_arr_ext.get_int_arr_bitmap(A).copy())


@overload_method(IntegerArrayType, 'astype', no_unliteral=True)
def overload_int_arr_astype(A, dtype, copy=True):
    if isinstance(dtype, types.TypeRef):
        dtype = dtype.instance_type
    if dtype == types.unicode_type:
        raise_bodo_error(
            "IntegerArray.astype(): 'dtype' when passed as string must be a constant value"
            )
    if isinstance(dtype, types.NumberClass):
        dtype = dtype.dtype
    if isinstance(dtype, IntDtype) and A.dtype == dtype.dtype:
        if is_overload_false(copy):
            return lambda A, dtype, copy=True: A
        elif is_overload_true(copy):
            return lambda A, dtype, copy=True: A.copy()
        else:

            def impl(A, dtype, copy=True):
                if copy:
                    return A.copy()
                else:
                    return A
            return impl
    if isinstance(dtype, IntDtype):
        np_dtype = dtype.dtype
        return (lambda A, dtype, copy=True: bodo.libs.int_arr_ext.
            init_integer_array(bodo.libs.int_arr_ext.get_int_arr_data(A).
            astype(np_dtype), bodo.libs.int_arr_ext.get_int_arr_bitmap(A).
            copy()))
    nb_dtype = parse_dtype(dtype, 'IntegerArray.astype')
    if isinstance(nb_dtype, types.Float):

        def impl_float(A, dtype, copy=True):
            data = bodo.libs.int_arr_ext.get_int_arr_data(A)
            n = len(data)
            chflt__eiy = np.empty(n, nb_dtype)
            for i in numba.parfors.parfor.internal_prange(n):
                chflt__eiy[i] = data[i]
                if bodo.libs.array_kernels.isna(A, i):
                    chflt__eiy[i] = np.nan
            return chflt__eiy
        return impl_float
    return lambda A, dtype, copy=True: bodo.libs.int_arr_ext.get_int_arr_data(A
        ).astype(nb_dtype)


ufunc_aliases = {'subtract': 'sub', 'multiply': 'mul', 'floor_divide':
    'floordiv', 'true_divide': 'truediv', 'power': 'pow', 'remainder':
    'mod', 'divide': 'div', 'equal': 'eq', 'not_equal': 'ne', 'less': 'lt',
    'less_equal': 'le', 'greater': 'gt', 'greater_equal': 'ge'}


def create_op_overload(op, n_inputs):
    if n_inputs == 1:

        def overload_int_arr_op_nin_1(A):
            if isinstance(A, IntegerArrayType):
                return get_nullable_array_unary_impl(op, A)
        return overload_int_arr_op_nin_1
    elif n_inputs == 2:

        def overload_series_op_nin_2(lhs, rhs):
            if isinstance(lhs, IntegerArrayType) or isinstance(rhs,
                IntegerArrayType):
                return get_nullable_array_binary_impl(op, lhs, rhs)
        return overload_series_op_nin_2
    else:
        raise RuntimeError(
            "Don't know how to register ufuncs from ufunc_db with arity > 2")


def _install_np_ufuncs():
    import numba.np.ufunc_db
    for jibzh__gbcog in numba.np.ufunc_db.get_ufuncs():
        kzm__eps = create_op_overload(jibzh__gbcog, jibzh__gbcog.nin)
        overload(jibzh__gbcog, no_unliteral=True)(kzm__eps)


_install_np_ufuncs()
skips = [operator.lt, operator.le, operator.eq, operator.ne, operator.gt,
    operator.ge, operator.add, operator.sub, operator.mul, operator.truediv,
    operator.floordiv, operator.pow, operator.mod]


def _install_binary_ops():
    for op in numba.core.typing.npydecl.NumpyRulesArrayOperator._op_map.keys():
        if op in skips:
            continue
        kzm__eps = create_op_overload(op, 2)
        overload(op)(kzm__eps)


_install_binary_ops()


def _install_inplace_binary_ops():
    for op in numba.core.typing.npydecl.NumpyRulesInplaceArrayOperator._op_map.keys(
        ):
        kzm__eps = create_op_overload(op, 2)
        overload(op, no_unliteral=True)(kzm__eps)


_install_inplace_binary_ops()


def _install_unary_ops():
    for op in (operator.neg, operator.invert, operator.pos):
        kzm__eps = create_op_overload(op, 1)
        overload(op, no_unliteral=True)(kzm__eps)


_install_unary_ops()


@overload_method(IntegerArrayType, 'sum', no_unliteral=True)
def overload_int_arr_sum(A, skipna=True, min_count=0):
    lij__sfjlg = dict(skipna=skipna, min_count=min_count)
    dvwg__bqn = dict(skipna=True, min_count=0)
    check_unsupported_args('IntegerArray.sum', lij__sfjlg, dvwg__bqn)

    def impl(A, skipna=True, min_count=0):
        numba.parfors.parfor.init_prange()
        s = 0
        for i in numba.parfors.parfor.internal_prange(len(A)):
            val = 0
            if not bodo.libs.array_kernels.isna(A, i):
                val = A[i]
            s += val
        return s
    return impl


@overload_method(IntegerArrayType, 'unique', no_unliteral=True)
def overload_unique(A):
    dtype = A.dtype

    def impl_int_arr(A):
        data = []
        uat__fttr = []
        mdyhy__clms = False
        s = set()
        for i in range(len(A)):
            val = A[i]
            if bodo.libs.array_kernels.isna(A, i):
                if not mdyhy__clms:
                    data.append(dtype(1))
                    uat__fttr.append(False)
                    mdyhy__clms = True
                continue
            if val not in s:
                s.add(val)
                data.append(val)
                uat__fttr.append(True)
        qqmwo__oyql = np.array(data)
        n = len(qqmwo__oyql)
        eww__ucgfj = n + 7 >> 3
        vwtag__hclls = np.empty(eww__ucgfj, np.uint8)
        for ypdtv__znpwo in range(n):
            set_bit_to_arr(vwtag__hclls, ypdtv__znpwo, uat__fttr[ypdtv__znpwo])
        return init_integer_array(qqmwo__oyql, vwtag__hclls)
    return impl_int_arr


def get_nullable_array_unary_impl(op, A):
    gho__meorf = numba.core.registry.cpu_target.typing_context
    uhala__ioom = gho__meorf.resolve_function_type(op, (types.Array(A.dtype,
        1, 'C'),), {}).return_type
    uhala__ioom = to_nullable_type(uhala__ioom)

    def impl(A):
        n = len(A)
        scpj__ephwr = bodo.utils.utils.alloc_type(n, uhala__ioom, None)
        for i in numba.parfors.parfor.internal_prange(n):
            if bodo.libs.array_kernels.isna(A, i):
                bodo.libs.array_kernels.setna(scpj__ephwr, i)
                continue
            scpj__ephwr[i] = op(A[i])
        return scpj__ephwr
    return impl


def get_nullable_array_binary_impl(op, lhs, rhs):
    oge__xsj = (op in numba.core.typing.npydecl.
        NumpyRulesInplaceArrayOperator._op_map.keys())
    zmyd__rdxu = isinstance(lhs, (types.Number, types.Boolean))
    gwz__hklh = isinstance(rhs, (types.Number, types.Boolean))
    yldog__jkpuc = types.Array(getattr(lhs, 'dtype', lhs), 1, 'C')
    bdkh__hifz = types.Array(getattr(rhs, 'dtype', rhs), 1, 'C')
    gho__meorf = numba.core.registry.cpu_target.typing_context
    uhala__ioom = gho__meorf.resolve_function_type(op, (yldog__jkpuc,
        bdkh__hifz), {}).return_type
    uhala__ioom = to_nullable_type(uhala__ioom)
    if op in (operator.truediv, operator.itruediv):
        op = np.true_divide
    elif op in (operator.floordiv, operator.ifloordiv):
        op = np.floor_divide
    jukww__wxxu = 'lhs' if zmyd__rdxu else 'lhs[i]'
    hfuk__kpd = 'rhs' if gwz__hklh else 'rhs[i]'
    kec__jjie = ('False' if zmyd__rdxu else
        'bodo.libs.array_kernels.isna(lhs, i)')
    qqqw__ivc = ('False' if gwz__hklh else
        'bodo.libs.array_kernels.isna(rhs, i)')
    ets__sxdzu = 'def impl(lhs, rhs):\n'
    ets__sxdzu += '  n = len({})\n'.format('lhs' if not zmyd__rdxu else 'rhs')
    if oge__xsj:
        ets__sxdzu += '  out_arr = {}\n'.format('lhs' if not zmyd__rdxu else
            'rhs')
    else:
        ets__sxdzu += (
            '  out_arr = bodo.utils.utils.alloc_type(n, ret_dtype, None)\n')
    ets__sxdzu += '  for i in numba.parfors.parfor.internal_prange(n):\n'
    ets__sxdzu += '    if ({}\n'.format(kec__jjie)
    ets__sxdzu += '        or {}):\n'.format(qqqw__ivc)
    ets__sxdzu += '      bodo.libs.array_kernels.setna(out_arr, i)\n'
    ets__sxdzu += '      continue\n'
    ets__sxdzu += (
        """    out_arr[i] = bodo.utils.conversion.unbox_if_tz_naive_timestamp(op({}, {}))
"""
        .format(jukww__wxxu, hfuk__kpd))
    ets__sxdzu += '  return out_arr\n'
    ebc__xcd = {}
    exec(ets__sxdzu, {'bodo': bodo, 'numba': numba, 'np': np, 'ret_dtype':
        uhala__ioom, 'op': op}, ebc__xcd)
    impl = ebc__xcd['impl']
    return impl


def get_int_array_op_pd_td(op):

    def impl(lhs, rhs):
        zmyd__rdxu = lhs in [pd_timedelta_type]
        gwz__hklh = rhs in [pd_timedelta_type]
        if zmyd__rdxu:

            def impl(lhs, rhs):
                n = len(rhs)
                scpj__ephwr = np.empty(n, 'timedelta64[ns]')
                for i in numba.parfors.parfor.internal_prange(n):
                    if bodo.libs.array_kernels.isna(rhs, i):
                        bodo.libs.array_kernels.setna(scpj__ephwr, i)
                        continue
                    scpj__ephwr[i
                        ] = bodo.utils.conversion.unbox_if_tz_naive_timestamp(
                        op(lhs, rhs[i]))
                return scpj__ephwr
            return impl
        elif gwz__hklh:

            def impl(lhs, rhs):
                n = len(lhs)
                scpj__ephwr = np.empty(n, 'timedelta64[ns]')
                for i in numba.parfors.parfor.internal_prange(n):
                    if bodo.libs.array_kernels.isna(lhs, i):
                        bodo.libs.array_kernels.setna(scpj__ephwr, i)
                        continue
                    scpj__ephwr[i
                        ] = bodo.utils.conversion.unbox_if_tz_naive_timestamp(
                        op(lhs[i], rhs))
                return scpj__ephwr
            return impl
    return impl
