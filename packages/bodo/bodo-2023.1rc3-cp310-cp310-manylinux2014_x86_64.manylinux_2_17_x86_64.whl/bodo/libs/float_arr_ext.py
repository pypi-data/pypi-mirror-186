"""Nullable float array corresponding to Pandas FloatingArray.
However, nulls are stored in bit arrays similar to Arrow's arrays.
"""
import operator
import os
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
from bodo.libs import array_ext, hstr_ext
ll.add_symbol('is_pd_float_array', array_ext.is_pd_float_array)
ll.add_symbol('float_array_from_sequence', array_ext.float_array_from_sequence)
from bodo.utils.indexing import array_getitem_bool_index, array_getitem_int_index, array_getitem_slice_index, array_setitem_bool_index, array_setitem_int_index, array_setitem_slice_index
from bodo.utils.typing import BodoError, check_unsupported_args, is_iterable_type, is_list_like_index_type, is_overload_false, is_overload_none, is_overload_true, parse_dtype, raise_bodo_error
_use_nullable_float = int(os.environ.get('BODO_USE_NULLABLE_FLOAT', '0'))


class FloatingArrayType(types.ArrayCompatible):

    def __init__(self, dtype):
        self.dtype = dtype
        super(FloatingArrayType, self).__init__(name=
            f'FloatingArrayType({dtype})')

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    def copy(self):
        return FloatingArrayType(self.dtype)

    @property
    def get_pandas_scalar_type_instance(self):
        return pd.Float64Dtype(
            ) if self.dtype == types.float64 else pd.Float32Dtype()


@register_model(FloatingArrayType)
class FloatingArrayModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        wudt__psvqp = [('data', types.Array(fe_type.dtype, 1, 'C')), (
            'null_bitmap', types.Array(types.uint8, 1, 'C'))]
        models.StructModel.__init__(self, dmm, fe_type, wudt__psvqp)


make_attribute_wrapper(FloatingArrayType, 'data', '_data')
make_attribute_wrapper(FloatingArrayType, 'null_bitmap', '_null_bitmap')


@typeof_impl.register(pd.arrays.FloatingArray)
def _typeof_pd_float_array(val, c):
    dtype = types.float32 if val.dtype == pd.Float32Dtype() else types.float64
    return FloatingArrayType(dtype)


class FloatDtype(types.Number):

    def __init__(self, dtype):
        assert isinstance(dtype, types.Float)
        self.dtype = dtype
        vqz__aod = f'Float{dtype.bitwidth}Dtype()'
        super(FloatDtype, self).__init__(vqz__aod)


register_model(FloatDtype)(models.OpaqueModel)


@box(FloatDtype)
def box_floatdtype(typ, val, c):
    rzrwo__bizq = c.context.insert_const_string(c.builder.module, 'pandas')
    aft__onz = c.pyapi.import_module_noblock(rzrwo__bizq)
    fdbux__xozmg = c.pyapi.call_method(aft__onz, str(typ)[:-2], ())
    c.pyapi.decref(aft__onz)
    return fdbux__xozmg


@unbox(FloatDtype)
def unbox_floatdtype(typ, val, c):
    return NativeValue(c.context.get_dummy_value())


def typeof_pd_float_dtype(val, c):
    dtype = types.float32 if val == pd.Float32Dtype() else types.float64
    return FloatDtype(dtype)


def _register_float_dtype(t):
    typeof_impl.register(t)(typeof_pd_float_dtype)
    float_dtype = typeof_pd_float_dtype(t(), None)
    type_callable(t)(lambda c: lambda : float_dtype)
    lower_builtin(t)(lambda c, b, s, a: c.get_dummy_value())


_register_float_dtype(pd.Float32Dtype)
_register_float_dtype(pd.Float64Dtype)


@unbox(FloatingArrayType)
def unbox_float_array(typ, obj, c):
    resm__bjw = c.pyapi.call_method(obj, '__len__', ())
    n = c.pyapi.long_as_longlong(resm__bjw)
    c.pyapi.decref(resm__bjw)
    mfciq__orkc = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    jvdj__yryv = c.builder.udiv(c.builder.add(n, lir.Constant(lir.IntType(
        64), 7)), lir.Constant(lir.IntType(64), 8))
    atfn__uah = bodo.utils.utils._empty_nd_impl(c.context, c.builder, types
        .Array(types.uint8, 1, 'C'), [jvdj__yryv])
    qkh__wrohk = lir.FunctionType(lir.IntType(32), [lir.IntType(8).
        as_pointer()])
    yrid__mwgl = cgutils.get_or_insert_function(c.builder.module,
        qkh__wrohk, name='is_pd_float_array')
    eymvl__hqz = c.builder.call(yrid__mwgl, [obj])
    tntwr__vtmzc = c.builder.icmp_unsigned('!=', eymvl__hqz, eymvl__hqz.type(0)
        )
    with c.builder.if_else(tntwr__vtmzc) as (msa__rjd, brpt__memp):
        with msa__rjd:
            llw__ntqs = c.pyapi.object_getattr_string(obj, '_data')
            mfciq__orkc.data = c.pyapi.to_native_value(types.Array(typ.
                dtype, 1, 'C'), llw__ntqs).value
            scs__oeqhh = c.pyapi.object_getattr_string(obj, '_mask')
            gyhu__uuev = c.pyapi.to_native_value(types.Array(types.bool_, 1,
                'C'), scs__oeqhh).value
            c.pyapi.decref(llw__ntqs)
            c.pyapi.decref(scs__oeqhh)
            wmwn__lazab = c.context.make_array(types.Array(types.bool_, 1, 'C')
                )(c.context, c.builder, gyhu__uuev)
            qkh__wrohk = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
                as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(64)])
            yrid__mwgl = cgutils.get_or_insert_function(c.builder.module,
                qkh__wrohk, name='mask_arr_to_bitmap')
            c.builder.call(yrid__mwgl, [atfn__uah.data, wmwn__lazab.data, n])
            c.context.nrt.decref(c.builder, types.Array(types.bool_, 1, 'C'
                ), gyhu__uuev)
        with brpt__memp:
            exomv__ksa = bodo.utils.utils._empty_nd_impl(c.context, c.
                builder, types.Array(typ.dtype, 1, 'C'), [n])
            qkh__wrohk = lir.FunctionType(lir.IntType(32), [lir.IntType(8).
                as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(8).
                as_pointer()])
            jreu__fctlg = cgutils.get_or_insert_function(c.builder.module,
                qkh__wrohk, name='float_array_from_sequence')
            c.builder.call(jreu__fctlg, [obj, c.builder.bitcast(exomv__ksa.
                data, lir.IntType(8).as_pointer()), atfn__uah.data])
            mfciq__orkc.data = exomv__ksa._getvalue()
    mfciq__orkc.null_bitmap = atfn__uah._getvalue()
    llku__sdlhs = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(mfciq__orkc._getvalue(), is_error=llku__sdlhs)


@box(FloatingArrayType)
def box_float_array(typ, val, c):
    mfciq__orkc = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    data = c.pyapi.from_native_value(types.Array(typ.dtype, 1, 'C'),
        mfciq__orkc.data, c.env_manager)
    fjk__ebg = c.context.make_array(types.Array(types.uint8, 1, 'C'))(c.
        context, c.builder, mfciq__orkc.null_bitmap).data
    resm__bjw = c.pyapi.call_method(data, '__len__', ())
    n = c.pyapi.long_as_longlong(resm__bjw)
    rzrwo__bizq = c.context.insert_const_string(c.builder.module, 'numpy')
    swzq__mftkm = c.pyapi.import_module_noblock(rzrwo__bizq)
    lztzg__cssoy = c.pyapi.object_getattr_string(swzq__mftkm, 'bool_')
    gyhu__uuev = c.pyapi.call_method(swzq__mftkm, 'empty', (resm__bjw,
        lztzg__cssoy))
    etke__udd = c.pyapi.object_getattr_string(gyhu__uuev, 'ctypes')
    gabmh__ifnqd = c.pyapi.object_getattr_string(etke__udd, 'data')
    vcvj__agx = c.builder.inttoptr(c.pyapi.long_as_longlong(gabmh__ifnqd),
        lir.IntType(8).as_pointer())
    with cgutils.for_range(c.builder, n) as xalal__hjqvi:
        jrj__msmkc = xalal__hjqvi.index
        rlzio__jiaf = c.builder.lshr(jrj__msmkc, lir.Constant(lir.IntType(
            64), 3))
        ork__rpncz = c.builder.load(cgutils.gep(c.builder, fjk__ebg,
            rlzio__jiaf))
        exyfe__vhds = c.builder.trunc(c.builder.and_(jrj__msmkc, lir.
            Constant(lir.IntType(64), 7)), lir.IntType(8))
        val = c.builder.and_(c.builder.lshr(ork__rpncz, exyfe__vhds), lir.
            Constant(lir.IntType(8), 1))
        val = c.builder.xor(val, lir.Constant(lir.IntType(8), 1))
        ukr__xwzxa = cgutils.gep(c.builder, vcvj__agx, jrj__msmkc)
        c.builder.store(val, ukr__xwzxa)
    c.context.nrt.decref(c.builder, types.Array(types.uint8, 1, 'C'),
        mfciq__orkc.null_bitmap)
    rzrwo__bizq = c.context.insert_const_string(c.builder.module, 'pandas')
    aft__onz = c.pyapi.import_module_noblock(rzrwo__bizq)
    ozzmf__vsqgy = c.pyapi.object_getattr_string(aft__onz, 'arrays')
    fdbux__xozmg = c.pyapi.call_method(ozzmf__vsqgy, 'FloatingArray', (data,
        gyhu__uuev))
    c.pyapi.decref(aft__onz)
    c.pyapi.decref(resm__bjw)
    c.pyapi.decref(swzq__mftkm)
    c.pyapi.decref(lztzg__cssoy)
    c.pyapi.decref(etke__udd)
    c.pyapi.decref(gabmh__ifnqd)
    c.pyapi.decref(ozzmf__vsqgy)
    c.pyapi.decref(data)
    c.pyapi.decref(gyhu__uuev)
    return fdbux__xozmg


@intrinsic
def init_float_array(typingctx, data, null_bitmap=None):
    assert isinstance(data, types.Array)
    assert null_bitmap == types.Array(types.uint8, 1, 'C')

    def codegen(context, builder, signature, args):
        pzp__lret, nucd__upa = args
        mfciq__orkc = cgutils.create_struct_proxy(signature.return_type)(
            context, builder)
        mfciq__orkc.data = pzp__lret
        mfciq__orkc.null_bitmap = nucd__upa
        context.nrt.incref(builder, signature.args[0], pzp__lret)
        context.nrt.incref(builder, signature.args[1], nucd__upa)
        return mfciq__orkc._getvalue()
    zcz__mrjph = FloatingArrayType(data.dtype)
    gxya__lby = zcz__mrjph(data, null_bitmap)
    return gxya__lby, codegen


@lower_constant(FloatingArrayType)
def lower_constant_float_arr(context, builder, typ, pyval):
    n = len(pyval)
    cxh__ple = np.empty(n, pyval.dtype.type)
    gvtt__mfkce = np.empty(n + 7 >> 3, np.uint8)
    for jrj__msmkc, s in enumerate(pyval):
        rbwd__fokaj = pd.isna(s)
        bodo.libs.int_arr_ext.set_bit_to_arr(gvtt__mfkce, jrj__msmkc, int(
            not rbwd__fokaj))
        if not rbwd__fokaj:
            cxh__ple[jrj__msmkc] = s
    bqik__ymb = context.get_constant_generic(builder, types.Array(typ.dtype,
        1, 'C'), cxh__ple)
    lfsz__kxur = context.get_constant_generic(builder, types.Array(types.
        uint8, 1, 'C'), gvtt__mfkce)
    return lir.Constant.literal_struct([bqik__ymb, lfsz__kxur])


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def get_float_arr_data(A):
    return lambda A: A._data


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def get_float_arr_bitmap(A):
    return lambda A: A._null_bitmap


def get_float_arr_data_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 1 and not kws
    dmlxf__bujk = args[0]
    if equiv_set.has_shape(dmlxf__bujk):
        return ArrayAnalysis.AnalyzeResult(shape=dmlxf__bujk, pre=[])
    return None


(ArrayAnalysis._analyze_op_call_bodo_libs_float_arr_ext_get_float_arr_data
    ) = get_float_arr_data_equiv


def init_float_array_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 2 and not kws
    dmlxf__bujk = args[0]
    if equiv_set.has_shape(dmlxf__bujk):
        return ArrayAnalysis.AnalyzeResult(shape=dmlxf__bujk, pre=[])
    return None


ArrayAnalysis._analyze_op_call_bodo_libs_float_arr_ext_init_float_array = (
    init_float_array_equiv)


def alias_ext_dummy_func(lhs_name, args, alias_map, arg_aliases):
    assert len(args) >= 1
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)


def alias_ext_init_float_array(lhs_name, args, alias_map, arg_aliases):
    assert len(args) == 2
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)
    numba.core.ir_utils._add_alias(lhs_name, args[1].name, alias_map,
        arg_aliases)


numba.core.ir_utils.alias_func_extensions['init_float_array',
    'bodo.libs.float_arr_ext'] = alias_ext_init_float_array
numba.core.ir_utils.alias_func_extensions['get_float_arr_data',
    'bodo.libs.float_arr_ext'] = alias_ext_dummy_func
numba.core.ir_utils.alias_func_extensions['get_float_arr_bitmap',
    'bodo.libs.float_arr_ext'] = alias_ext_dummy_func


@numba.njit(no_cpython_wrapper=True)
def alloc_float_array(n, dtype):
    cxh__ple = np.empty(n, dtype)
    hnc__hlws = np.empty(n + 7 >> 3, dtype=np.uint8)
    return init_float_array(cxh__ple, hnc__hlws)


def alloc_float_array_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 2 and not kws
    return ArrayAnalysis.AnalyzeResult(shape=args[0], pre=[])


(ArrayAnalysis._analyze_op_call_bodo_libs_float_arr_ext_alloc_float_array
    ) = alloc_float_array_equiv


@overload(operator.getitem, no_unliteral=True)
def float_arr_getitem(A, ind):
    if not isinstance(A, FloatingArrayType):
        return
    if isinstance(ind, types.Integer):
        return lambda A, ind: A._data[ind]
    if ind != bodo.boolean_array and is_list_like_index_type(ind
        ) and ind.dtype == types.bool_:

        def impl_bool(A, ind):
            aeily__mao, kdhzj__hptyb = array_getitem_bool_index(A, ind)
            return init_float_array(aeily__mao, kdhzj__hptyb)
        return impl_bool
    if is_list_like_index_type(ind) and isinstance(ind.dtype, types.Integer):

        def impl(A, ind):
            aeily__mao, kdhzj__hptyb = array_getitem_int_index(A, ind)
            return init_float_array(aeily__mao, kdhzj__hptyb)
        return impl
    if isinstance(ind, types.SliceType):

        def impl_slice(A, ind):
            aeily__mao, kdhzj__hptyb = array_getitem_slice_index(A, ind)
            return init_float_array(aeily__mao, kdhzj__hptyb)
        return impl_slice
    if ind != bodo.boolean_array:
        raise BodoError(
            f'getitem for IntegerArray with indexing type {ind} not supported.'
            )


@overload(operator.setitem, no_unliteral=True)
def float_arr_setitem(A, idx, val):
    if not isinstance(A, FloatingArrayType):
        return
    if val == types.none or isinstance(val, types.optional):
        return
    zzygy__uwnc = (
        f"setitem for FloatingArray with indexing type {idx} received an incorrect 'value' type {val}."
        )
    qstlh__xpj = isinstance(val, (types.Integer, types.Boolean, types.Float))
    if isinstance(idx, types.Integer):
        if qstlh__xpj:

            def impl_scalar(A, idx, val):
                A._data[idx] = val
                bodo.libs.int_arr_ext.set_bit_to_arr(A._null_bitmap, idx, 1)
            return impl_scalar
        else:
            raise BodoError(zzygy__uwnc)
    if not (is_iterable_type(val) and isinstance(val.dtype, (types.Integer,
        types.Boolean, types.Float)) or qstlh__xpj):
        raise BodoError(zzygy__uwnc)
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
        f'setitem for FloatingArray with indexing type {idx} not supported.')


@overload(len, no_unliteral=True)
def overload_float_arr_len(A):
    if isinstance(A, FloatingArrayType):
        return lambda A: len(A._data)


@overload_attribute(FloatingArrayType, 'shape')
def overload_float_arr_shape(A):
    return lambda A: (len(A._data),)


@overload_attribute(FloatingArrayType, 'dtype')
def overload_float_arr_dtype(A):
    dtype_class = (pd.Float32Dtype if A.dtype == types.float32 else pd.
        Float64Dtype)
    return lambda A: dtype_class()


@overload_attribute(FloatingArrayType, 'ndim')
def overload_float_arr_ndim(A):
    return lambda A: 1


@overload_attribute(FloatingArrayType, 'size')
def overload_float_size(A):
    return lambda A: len(A._data)


@overload_attribute(FloatingArrayType, 'nbytes')
def float_arr_nbytes_overload(A):
    return lambda A: A._data.nbytes + A._null_bitmap.nbytes


@overload_method(FloatingArrayType, 'copy', no_unliteral=True)
def overload_float_arr_copy(A, dtype=None):
    if not is_overload_none(dtype):
        return lambda A, dtype=None: A.astype(dtype, copy=True)
    else:
        return lambda A, dtype=None: bodo.libs.float_arr_ext.init_float_array(
            bodo.libs.float_arr_ext.get_float_arr_data(A).copy(), bodo.libs
            .float_arr_ext.get_float_arr_bitmap(A).copy())


@overload_method(FloatingArrayType, 'astype', no_unliteral=True)
def overload_float_arr_astype(A, dtype, copy=True):
    if dtype == types.unicode_type:
        raise_bodo_error(
            "FloatingArray.astype(): 'dtype' when passed as string must be a constant value"
            )
    if isinstance(dtype, types.NumberClass):
        dtype = dtype.dtype
    if isinstance(dtype, FloatDtype) and A.dtype == dtype.dtype:
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
    if isinstance(dtype, FloatDtype):
        np_dtype = dtype.dtype
        return (lambda A, dtype, copy=True: bodo.libs.float_arr_ext.
            init_float_array(bodo.libs.float_arr_ext.get_float_arr_data(A).
            astype(np_dtype), bodo.libs.float_arr_ext.get_float_arr_bitmap(
            A).copy()))
    if isinstance(dtype, bodo.libs.int_arr_ext.IntDtype):
        np_dtype = dtype.dtype
        return (lambda A, dtype, copy=True: bodo.libs.int_arr_ext.
            init_integer_array(bodo.libs.float_arr_ext.get_float_arr_data(A
            ).astype(np_dtype), bodo.libs.float_arr_ext.
            get_float_arr_bitmap(A).copy()))
    nb_dtype = parse_dtype(dtype, 'FloatingArray.astype')
    if isinstance(nb_dtype, types.Float):

        def impl_float(A, dtype, copy=True):
            data = bodo.libs.float_arr_ext.get_float_arr_data(A)
            n = len(data)
            wmxl__rcl = np.empty(n, nb_dtype)
            for jrj__msmkc in numba.parfors.parfor.internal_prange(n):
                wmxl__rcl[jrj__msmkc] = data[jrj__msmkc]
                if bodo.libs.array_kernels.isna(A, jrj__msmkc):
                    wmxl__rcl[jrj__msmkc] = np.nan
            return wmxl__rcl
        return impl_float
    return (lambda A, dtype, copy=True: bodo.libs.float_arr_ext.
        get_float_arr_data(A).astype(nb_dtype))


ufunc_aliases = {'subtract': 'sub', 'multiply': 'mul', 'floor_divide':
    'floordiv', 'true_divide': 'truediv', 'power': 'pow', 'remainder':
    'mod', 'divide': 'div', 'equal': 'eq', 'not_equal': 'ne', 'less': 'lt',
    'less_equal': 'le', 'greater': 'gt', 'greater_equal': 'ge'}


def create_op_overload(op, n_inputs):
    if n_inputs == 1:

        def overload_float_arr_op_nin_1(A):
            if isinstance(A, FloatingArrayType):
                return bodo.libs.int_arr_ext.get_nullable_array_unary_impl(op,
                    A)
        return overload_float_arr_op_nin_1
    elif n_inputs == 2:

        def overload_series_op_nin_2(lhs, rhs):
            if isinstance(lhs, FloatingArrayType) or isinstance(rhs,
                FloatingArrayType):
                return bodo.libs.int_arr_ext.get_nullable_array_binary_impl(op,
                    lhs, rhs)
        return overload_series_op_nin_2
    else:
        raise RuntimeError(
            "Don't know how to register ufuncs from ufunc_db with arity > 2")


def _install_np_ufuncs():
    import numba.np.ufunc_db
    for ptwo__qmu in numba.np.ufunc_db.get_ufuncs():
        cnw__jiz = create_op_overload(ptwo__qmu, ptwo__qmu.nin)
        overload(ptwo__qmu, no_unliteral=True)(cnw__jiz)


_install_np_ufuncs()
skips = [operator.lt, operator.le, operator.eq, operator.ne, operator.gt,
    operator.ge, operator.add, operator.sub, operator.mul, operator.truediv,
    operator.floordiv, operator.pow, operator.mod]


def _install_binary_ops():
    for op in numba.core.typing.npydecl.NumpyRulesArrayOperator._op_map.keys():
        if op in skips:
            continue
        cnw__jiz = create_op_overload(op, 2)
        overload(op)(cnw__jiz)


_install_binary_ops()


def _install_inplace_binary_ops():
    for op in numba.core.typing.npydecl.NumpyRulesInplaceArrayOperator._op_map.keys(
        ):
        cnw__jiz = create_op_overload(op, 2)
        overload(op, no_unliteral=True)(cnw__jiz)


_install_inplace_binary_ops()


def _install_unary_ops():
    for op in (operator.neg, operator.invert, operator.pos):
        cnw__jiz = create_op_overload(op, 1)
        overload(op, no_unliteral=True)(cnw__jiz)


_install_unary_ops()


@overload_method(FloatingArrayType, 'sum', no_unliteral=True)
def overload_float_arr_sum(A, skipna=True, min_count=0):
    uzn__hgt = dict(skipna=skipna, min_count=min_count)
    jen__zzgl = dict(skipna=True, min_count=0)
    check_unsupported_args('FloatingArray.sum', uzn__hgt, jen__zzgl)

    def impl(A, skipna=True, min_count=0):
        numba.parfors.parfor.init_prange()
        s = 0.0
        for jrj__msmkc in numba.parfors.parfor.internal_prange(len(A)):
            val = 0.0
            if not bodo.libs.array_kernels.isna(A, jrj__msmkc):
                val = A[jrj__msmkc]
            s += val
        return s
    return impl


@overload_method(FloatingArrayType, 'unique', no_unliteral=True)
def overload_unique(A):
    dtype = A.dtype

    def impl_float_arr(A):
        data = []
        exyfe__vhds = []
        jvtt__lyelb = False
        s = set()
        for jrj__msmkc in range(len(A)):
            val = A[jrj__msmkc]
            if bodo.libs.array_kernels.isna(A, jrj__msmkc):
                if not jvtt__lyelb:
                    data.append(dtype(1))
                    exyfe__vhds.append(False)
                    jvtt__lyelb = True
                continue
            if val not in s:
                s.add(val)
                data.append(val)
                exyfe__vhds.append(True)
        aeily__mao = np.array(data)
        n = len(aeily__mao)
        jvdj__yryv = n + 7 >> 3
        kdhzj__hptyb = np.empty(jvdj__yryv, np.uint8)
        for duog__cvso in range(n):
            bodo.libs.int_arr_ext.set_bit_to_arr(kdhzj__hptyb, duog__cvso,
                exyfe__vhds[duog__cvso])
        return init_float_array(aeily__mao, kdhzj__hptyb)
    return impl_float_arr
