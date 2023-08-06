"""Nullable boolean array that stores data in Numpy format (1 byte per value)
but nulls are stored in bit arrays (1 bit per value) similar to Arrow's nulls.
Pandas converts boolean array to object when NAs are introduced.
"""
import operator
import llvmlite.binding as ll
import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.imputils import impl_ret_borrowed, lower_constant
from numba.core.typing.templates import AbstractTemplate, infer_global
from numba.extending import NativeValue, box, intrinsic, lower_builtin, lower_cast, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_model, type_callable, typeof_impl, unbox
from numba.parfors.array_analysis import ArrayAnalysis
import bodo
from bodo.libs import hstr_ext
from bodo.libs.str_arr_ext import string_array_type
from bodo.utils.typing import is_list_like_index_type
ll.add_symbol('is_bool_array', hstr_ext.is_bool_array)
ll.add_symbol('is_pd_boolean_array', hstr_ext.is_pd_boolean_array)
ll.add_symbol('unbox_bool_array_obj', hstr_ext.unbox_bool_array_obj)
from bodo.utils.indexing import array_getitem_bool_index, array_getitem_int_index, array_getitem_slice_index, array_setitem_bool_index, array_setitem_int_index, array_setitem_slice_index
from bodo.utils.typing import BodoError, is_iterable_type, is_overload_false, is_overload_true, parse_dtype, raise_bodo_error


class BooleanArrayType(types.ArrayCompatible):

    def __init__(self):
        super(BooleanArrayType, self).__init__(name='BooleanArrayType()')

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    @property
    def dtype(self):
        return types.bool_

    def copy(self):
        return BooleanArrayType()


boolean_array = BooleanArrayType()


@typeof_impl.register(pd.arrays.BooleanArray)
def typeof_boolean_array(val, c):
    return boolean_array


data_type = types.Array(types.bool_, 1, 'C')
nulls_type = types.Array(types.uint8, 1, 'C')


@register_model(BooleanArrayType)
class BooleanArrayModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        riy__cwdr = [('data', data_type), ('null_bitmap', nulls_type)]
        models.StructModel.__init__(self, dmm, fe_type, riy__cwdr)


make_attribute_wrapper(BooleanArrayType, 'data', '_data')
make_attribute_wrapper(BooleanArrayType, 'null_bitmap', '_null_bitmap')


class BooleanDtype(types.Number):

    def __init__(self):
        self.dtype = types.bool_
        super(BooleanDtype, self).__init__('BooleanDtype')


boolean_dtype = BooleanDtype()
register_model(BooleanDtype)(models.OpaqueModel)


@box(BooleanDtype)
def box_boolean_dtype(typ, val, c):
    byak__aqrz = c.context.insert_const_string(c.builder.module, 'pandas')
    czdh__gdu = c.pyapi.import_module_noblock(byak__aqrz)
    aguxm__fvq = c.pyapi.call_method(czdh__gdu, 'BooleanDtype', ())
    c.pyapi.decref(czdh__gdu)
    return aguxm__fvq


@unbox(BooleanDtype)
def unbox_boolean_dtype(typ, val, c):
    return NativeValue(c.context.get_dummy_value())


typeof_impl.register(pd.BooleanDtype)(lambda a, b: boolean_dtype)
type_callable(pd.BooleanDtype)(lambda c: lambda : boolean_dtype)
lower_builtin(pd.BooleanDtype)(lambda c, b, s, a: c.get_dummy_value())


@numba.njit
def gen_full_bitmap(n):
    bzvs__coqr = n + 7 >> 3
    return np.full(bzvs__coqr, 255, np.uint8)


def call_func_in_unbox(func, args, arg_typs, c):
    felr__lxdwo = c.context.typing_context.resolve_value_type(func)
    jgz__dpbir = felr__lxdwo.get_call_type(c.context.typing_context,
        arg_typs, {})
    adrou__zjf = c.context.get_function(felr__lxdwo, jgz__dpbir)
    bcqa__edt = c.context.call_conv.get_function_type(jgz__dpbir.
        return_type, jgz__dpbir.args)
    fypi__gvsh = c.builder.module
    ezgq__xdamm = lir.Function(fypi__gvsh, bcqa__edt, name=fypi__gvsh.
        get_unique_name('.func_conv'))
    ezgq__xdamm.linkage = 'internal'
    cwgh__qqbg = lir.IRBuilder(ezgq__xdamm.append_basic_block())
    qwn__dtpe = c.context.call_conv.decode_arguments(cwgh__qqbg, jgz__dpbir
        .args, ezgq__xdamm)
    cwivh__tiylt = adrou__zjf(cwgh__qqbg, qwn__dtpe)
    c.context.call_conv.return_value(cwgh__qqbg, cwivh__tiylt)
    wagr__lpzjs, uem__plrpy = c.context.call_conv.call_function(c.builder,
        ezgq__xdamm, jgz__dpbir.return_type, jgz__dpbir.args, args)
    return uem__plrpy


@unbox(BooleanArrayType)
def unbox_bool_array(typ, obj, c):
    rgrkt__qst = c.pyapi.call_method(obj, '__len__', ())
    n = c.pyapi.long_as_longlong(rgrkt__qst)
    c.pyapi.decref(rgrkt__qst)
    bcqa__edt = lir.FunctionType(lir.IntType(32), [lir.IntType(8).as_pointer()]
        )
    pgugn__wpmpo = cgutils.get_or_insert_function(c.builder.module,
        bcqa__edt, name='is_bool_array')
    bcqa__edt = lir.FunctionType(lir.IntType(32), [lir.IntType(8).as_pointer()]
        )
    ezgq__xdamm = cgutils.get_or_insert_function(c.builder.module,
        bcqa__edt, name='is_pd_boolean_array')
    lzdcn__vgz = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    ckn__wqewd = c.builder.call(ezgq__xdamm, [obj])
    ztd__fxjjc = c.builder.icmp_unsigned('!=', ckn__wqewd, ckn__wqewd.type(0))
    with c.builder.if_else(ztd__fxjjc) as (woj__cncnk, rgfo__bqxjy):
        with woj__cncnk:
            foksd__fvxlh = c.pyapi.object_getattr_string(obj, '_data')
            lzdcn__vgz.data = c.pyapi.to_native_value(types.Array(types.
                bool_, 1, 'C'), foksd__fvxlh).value
            rmmtn__ikt = c.pyapi.object_getattr_string(obj, '_mask')
            cfgr__htcc = c.pyapi.to_native_value(types.Array(types.bool_, 1,
                'C'), rmmtn__ikt).value
            bzvs__coqr = c.builder.udiv(c.builder.add(n, lir.Constant(lir.
                IntType(64), 7)), lir.Constant(lir.IntType(64), 8))
            tljlb__pow = c.context.make_array(types.Array(types.bool_, 1, 'C')
                )(c.context, c.builder, cfgr__htcc)
            nhy__bxcj = bodo.utils.utils._empty_nd_impl(c.context, c.
                builder, types.Array(types.uint8, 1, 'C'), [bzvs__coqr])
            bcqa__edt = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
                as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(64)])
            ezgq__xdamm = cgutils.get_or_insert_function(c.builder.module,
                bcqa__edt, name='mask_arr_to_bitmap')
            c.builder.call(ezgq__xdamm, [nhy__bxcj.data, tljlb__pow.data, n])
            lzdcn__vgz.null_bitmap = nhy__bxcj._getvalue()
            c.context.nrt.decref(c.builder, types.Array(types.bool_, 1, 'C'
                ), cfgr__htcc)
            c.pyapi.decref(foksd__fvxlh)
            c.pyapi.decref(rmmtn__ikt)
        with rgfo__bqxjy:
            kebxn__twm = c.builder.call(pgugn__wpmpo, [obj])
            rhfo__aet = c.builder.icmp_unsigned('!=', kebxn__twm,
                kebxn__twm.type(0))
            with c.builder.if_else(rhfo__aet) as (lmatg__hztsg, lpdc__qohgk):
                with lmatg__hztsg:
                    lzdcn__vgz.data = c.pyapi.to_native_value(types.Array(
                        types.bool_, 1, 'C'), obj).value
                    lzdcn__vgz.null_bitmap = call_func_in_unbox(gen_full_bitmap
                        , (n,), (types.int64,), c)
                with lpdc__qohgk:
                    lzdcn__vgz.data = bodo.utils.utils._empty_nd_impl(c.
                        context, c.builder, types.Array(types.bool_, 1, 'C'
                        ), [n])._getvalue()
                    bzvs__coqr = c.builder.udiv(c.builder.add(n, lir.
                        Constant(lir.IntType(64), 7)), lir.Constant(lir.
                        IntType(64), 8))
                    lzdcn__vgz.null_bitmap = bodo.utils.utils._empty_nd_impl(c
                        .context, c.builder, types.Array(types.uint8, 1,
                        'C'), [bzvs__coqr])._getvalue()
                    gdx__uxz = c.context.make_array(types.Array(types.bool_,
                        1, 'C'))(c.context, c.builder, lzdcn__vgz.data).data
                    cmtqb__zhsm = c.context.make_array(types.Array(types.
                        uint8, 1, 'C'))(c.context, c.builder, lzdcn__vgz.
                        null_bitmap).data
                    bcqa__edt = lir.FunctionType(lir.VoidType(), [lir.
                        IntType(8).as_pointer(), lir.IntType(8).as_pointer(
                        ), lir.IntType(8).as_pointer(), lir.IntType(64)])
                    ezgq__xdamm = cgutils.get_or_insert_function(c.builder.
                        module, bcqa__edt, name='unbox_bool_array_obj')
                    c.builder.call(ezgq__xdamm, [obj, gdx__uxz, cmtqb__zhsm, n]
                        )
    return NativeValue(lzdcn__vgz._getvalue())


@box(BooleanArrayType)
def box_bool_arr(typ, val, c):
    lzdcn__vgz = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    data = c.pyapi.from_native_value(types.Array(typ.dtype, 1, 'C'),
        lzdcn__vgz.data, c.env_manager)
    rpfz__xtis = c.context.make_array(types.Array(types.uint8, 1, 'C'))(c.
        context, c.builder, lzdcn__vgz.null_bitmap).data
    rgrkt__qst = c.pyapi.call_method(data, '__len__', ())
    n = c.pyapi.long_as_longlong(rgrkt__qst)
    byak__aqrz = c.context.insert_const_string(c.builder.module, 'numpy')
    oii__nxxgx = c.pyapi.import_module_noblock(byak__aqrz)
    hiw__dow = c.pyapi.object_getattr_string(oii__nxxgx, 'bool_')
    cfgr__htcc = c.pyapi.call_method(oii__nxxgx, 'empty', (rgrkt__qst,
        hiw__dow))
    obh__exf = c.pyapi.object_getattr_string(cfgr__htcc, 'ctypes')
    rsw__nghlu = c.pyapi.object_getattr_string(obh__exf, 'data')
    dcoff__mcdn = c.builder.inttoptr(c.pyapi.long_as_longlong(rsw__nghlu),
        lir.IntType(8).as_pointer())
    with cgutils.for_range(c.builder, n) as klix__tmpwn:
        edx__soca = klix__tmpwn.index
        vodx__kwski = c.builder.lshr(edx__soca, lir.Constant(lir.IntType(64
            ), 3))
        sgh__ihez = c.builder.load(cgutils.gep(c.builder, rpfz__xtis,
            vodx__kwski))
        bbxye__qiuak = c.builder.trunc(c.builder.and_(edx__soca, lir.
            Constant(lir.IntType(64), 7)), lir.IntType(8))
        val = c.builder.and_(c.builder.lshr(sgh__ihez, bbxye__qiuak), lir.
            Constant(lir.IntType(8), 1))
        val = c.builder.xor(val, lir.Constant(lir.IntType(8), 1))
        pwgc__auwma = cgutils.gep(c.builder, dcoff__mcdn, edx__soca)
        c.builder.store(val, pwgc__auwma)
    c.context.nrt.decref(c.builder, types.Array(types.uint8, 1, 'C'),
        lzdcn__vgz.null_bitmap)
    byak__aqrz = c.context.insert_const_string(c.builder.module, 'pandas')
    czdh__gdu = c.pyapi.import_module_noblock(byak__aqrz)
    xyh__scqbf = c.pyapi.object_getattr_string(czdh__gdu, 'arrays')
    aguxm__fvq = c.pyapi.call_method(xyh__scqbf, 'BooleanArray', (data,
        cfgr__htcc))
    c.pyapi.decref(czdh__gdu)
    c.pyapi.decref(rgrkt__qst)
    c.pyapi.decref(oii__nxxgx)
    c.pyapi.decref(hiw__dow)
    c.pyapi.decref(obh__exf)
    c.pyapi.decref(rsw__nghlu)
    c.pyapi.decref(xyh__scqbf)
    c.pyapi.decref(data)
    c.pyapi.decref(cfgr__htcc)
    return aguxm__fvq


@lower_constant(BooleanArrayType)
def lower_constant_bool_arr(context, builder, typ, pyval):
    n = len(pyval)
    drzn__bbobx = np.empty(n, np.bool_)
    cdlq__aioqh = np.empty(n + 7 >> 3, np.uint8)
    for edx__soca, s in enumerate(pyval):
        gank__ruaw = pd.isna(s)
        bodo.libs.int_arr_ext.set_bit_to_arr(cdlq__aioqh, edx__soca, int(
            not gank__ruaw))
        if not gank__ruaw:
            drzn__bbobx[edx__soca] = s
    iyezl__uutyy = context.get_constant_generic(builder, data_type, drzn__bbobx
        )
    tmndr__ylydl = context.get_constant_generic(builder, nulls_type,
        cdlq__aioqh)
    return lir.Constant.literal_struct([iyezl__uutyy, tmndr__ylydl])


def lower_init_bool_array(context, builder, signature, args):
    fkzt__ieeq, envf__nsrvg = args
    lzdcn__vgz = cgutils.create_struct_proxy(signature.return_type)(context,
        builder)
    lzdcn__vgz.data = fkzt__ieeq
    lzdcn__vgz.null_bitmap = envf__nsrvg
    context.nrt.incref(builder, signature.args[0], fkzt__ieeq)
    context.nrt.incref(builder, signature.args[1], envf__nsrvg)
    return lzdcn__vgz._getvalue()


@intrinsic
def init_bool_array(typingctx, data, null_bitmap=None):
    assert data == types.Array(types.bool_, 1, 'C')
    assert null_bitmap == types.Array(types.uint8, 1, 'C')
    sig = boolean_array(data, null_bitmap)
    return sig, lower_init_bool_array


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def get_bool_arr_data(A):
    return lambda A: A._data


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def get_bool_arr_bitmap(A):
    return lambda A: A._null_bitmap


def get_bool_arr_data_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 1 and not kws
    wlu__aorpc = args[0]
    if equiv_set.has_shape(wlu__aorpc):
        return ArrayAnalysis.AnalyzeResult(shape=wlu__aorpc, pre=[])
    return None


ArrayAnalysis._analyze_op_call_bodo_libs_bool_arr_ext_get_bool_arr_data = (
    get_bool_arr_data_equiv)


def init_bool_array_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 2 and not kws
    wlu__aorpc = args[0]
    if equiv_set.has_shape(wlu__aorpc):
        return ArrayAnalysis.AnalyzeResult(shape=wlu__aorpc, pre=[])
    return None


ArrayAnalysis._analyze_op_call_bodo_libs_bool_arr_ext_init_bool_array = (
    init_bool_array_equiv)


def alias_ext_dummy_func(lhs_name, args, alias_map, arg_aliases):
    assert len(args) >= 1
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)


def alias_ext_init_bool_array(lhs_name, args, alias_map, arg_aliases):
    assert len(args) == 2
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)
    numba.core.ir_utils._add_alias(lhs_name, args[1].name, alias_map,
        arg_aliases)


numba.core.ir_utils.alias_func_extensions['init_bool_array',
    'bodo.libs.bool_arr_ext'] = alias_ext_init_bool_array
numba.core.ir_utils.alias_func_extensions['get_bool_arr_data',
    'bodo.libs.bool_arr_ext'] = alias_ext_dummy_func
numba.core.ir_utils.alias_func_extensions['get_bool_arr_bitmap',
    'bodo.libs.bool_arr_ext'] = alias_ext_dummy_func


@numba.njit(no_cpython_wrapper=True)
def alloc_bool_array(n):
    drzn__bbobx = np.empty(n, dtype=np.bool_)
    aqfwe__wcbre = np.empty(n + 7 >> 3, dtype=np.uint8)
    return init_bool_array(drzn__bbobx, aqfwe__wcbre)


def alloc_bool_array_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 1 and not kws
    return ArrayAnalysis.AnalyzeResult(shape=args[0], pre=[])


ArrayAnalysis._analyze_op_call_bodo_libs_bool_arr_ext_alloc_bool_array = (
    alloc_bool_array_equiv)


@overload(operator.getitem, no_unliteral=True)
def bool_arr_getitem(A, ind):
    if A != boolean_array:
        return
    if isinstance(types.unliteral(ind), types.Integer):
        return lambda A, ind: A._data[ind]
    if ind != boolean_array and is_list_like_index_type(ind
        ) and ind.dtype == types.bool_:

        def impl_bool(A, ind):
            ywm__odgk, tjwoy__mtkj = array_getitem_bool_index(A, ind)
            return init_bool_array(ywm__odgk, tjwoy__mtkj)
        return impl_bool
    if is_list_like_index_type(ind) and isinstance(ind.dtype, types.Integer):

        def impl(A, ind):
            ywm__odgk, tjwoy__mtkj = array_getitem_int_index(A, ind)
            return init_bool_array(ywm__odgk, tjwoy__mtkj)
        return impl
    if isinstance(ind, types.SliceType):

        def impl_slice(A, ind):
            ywm__odgk, tjwoy__mtkj = array_getitem_slice_index(A, ind)
            return init_bool_array(ywm__odgk, tjwoy__mtkj)
        return impl_slice
    if ind != boolean_array:
        raise BodoError(
            f'getitem for BooleanArray with indexing type {ind} not supported.'
            )


@overload(operator.setitem, no_unliteral=True)
def bool_arr_setitem(A, idx, val):
    if A != boolean_array:
        return
    if val == types.none or isinstance(val, types.optional):
        return
    zbgct__hyfq = (
        f"setitem for BooleanArray with indexing type {idx} received an incorrect 'value' type {val}."
        )
    if isinstance(idx, types.Integer):
        if types.unliteral(val) == types.bool_:

            def impl_scalar(A, idx, val):
                A._data[idx] = val
                bodo.libs.int_arr_ext.set_bit_to_arr(A._null_bitmap, idx, 1)
            return impl_scalar
        else:
            raise BodoError(zbgct__hyfq)
    if not (is_iterable_type(val) and val.dtype == types.bool_ or types.
        unliteral(val) == types.bool_):
        raise BodoError(zbgct__hyfq)
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
        f'setitem for BooleanArray with indexing type {idx} not supported.')


@overload(len, no_unliteral=True)
def overload_bool_arr_len(A):
    if A == boolean_array:
        return lambda A: len(A._data)


@overload_attribute(BooleanArrayType, 'size')
def overload_bool_arr_size(A):
    return lambda A: len(A._data)


@overload_attribute(BooleanArrayType, 'shape')
def overload_bool_arr_shape(A):
    return lambda A: (len(A._data),)


@overload_attribute(BooleanArrayType, 'dtype')
def overload_bool_arr_dtype(A):
    return lambda A: pd.BooleanDtype()


@overload_attribute(BooleanArrayType, 'ndim')
def overload_bool_arr_ndim(A):
    return lambda A: 1


@overload_attribute(BooleanArrayType, 'nbytes')
def bool_arr_nbytes_overload(A):
    return lambda A: A._data.nbytes + A._null_bitmap.nbytes


@overload_method(BooleanArrayType, 'copy', no_unliteral=True)
def overload_bool_arr_copy(A):
    return lambda A: bodo.libs.bool_arr_ext.init_bool_array(bodo.libs.
        bool_arr_ext.get_bool_arr_data(A).copy(), bodo.libs.bool_arr_ext.
        get_bool_arr_bitmap(A).copy())


@overload_method(BooleanArrayType, 'sum', no_unliteral=True, inline='always')
def overload_bool_sum(A):

    def impl(A):
        numba.parfors.parfor.init_prange()
        s = 0
        for edx__soca in numba.parfors.parfor.internal_prange(len(A)):
            val = 0
            if not bodo.libs.array_kernels.isna(A, edx__soca):
                val = A[edx__soca]
            s += val
        return s
    return impl


@overload_method(BooleanArrayType, 'astype', no_unliteral=True)
def overload_bool_arr_astype(A, dtype, copy=True):
    if dtype == types.unicode_type:
        raise_bodo_error(
            "BooleanArray.astype(): 'dtype' when passed as string must be a constant value"
            )
    if dtype == types.bool_:
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
    nb_dtype = parse_dtype(dtype, 'BooleanArray.astype')
    if isinstance(nb_dtype, types.Float):

        def impl_float(A, dtype, copy=True):
            data = bodo.libs.bool_arr_ext.get_bool_arr_data(A)
            n = len(data)
            lfbp__xuxk = np.empty(n, nb_dtype)
            for edx__soca in numba.parfors.parfor.internal_prange(n):
                lfbp__xuxk[edx__soca] = data[edx__soca]
                if bodo.libs.array_kernels.isna(A, edx__soca):
                    lfbp__xuxk[edx__soca] = np.nan
            return lfbp__xuxk
        return impl_float
    return (lambda A, dtype, copy=True: bodo.libs.bool_arr_ext.
        get_bool_arr_data(A).astype(nb_dtype))


@overload_method(BooleanArrayType, 'fillna', no_unliteral=True)
def overload_bool_fillna(A, value=None, method=None, limit=None):

    def impl(A, value=None, method=None, limit=None):
        data = bodo.libs.bool_arr_ext.get_bool_arr_data(A)
        n = len(data)
        lfbp__xuxk = np.empty(n, dtype=np.bool_)
        for edx__soca in numba.parfors.parfor.internal_prange(n):
            lfbp__xuxk[edx__soca] = data[edx__soca]
            if bodo.libs.array_kernels.isna(A, edx__soca):
                lfbp__xuxk[edx__soca] = value
        return lfbp__xuxk
    return impl


@overload(str, no_unliteral=True)
def overload_str_bool(val):
    if val == types.bool_:

        def impl(val):
            if val:
                return 'True'
            return 'False'
        return impl


ufunc_aliases = {'equal': 'eq', 'not_equal': 'ne', 'less': 'lt',
    'less_equal': 'le', 'greater': 'gt', 'greater_equal': 'ge'}


def create_op_overload(op, n_inputs):
    ppede__nqyfv = op.__name__
    ppede__nqyfv = ufunc_aliases.get(ppede__nqyfv, ppede__nqyfv)
    if n_inputs == 1:

        def overload_bool_arr_op_nin_1(A):
            if isinstance(A, BooleanArrayType):
                return bodo.libs.int_arr_ext.get_nullable_array_unary_impl(op,
                    A)
        return overload_bool_arr_op_nin_1
    elif n_inputs == 2:

        def overload_bool_arr_op_nin_2(lhs, rhs):
            if lhs == boolean_array or rhs == boolean_array:
                return bodo.libs.int_arr_ext.get_nullable_array_binary_impl(op,
                    lhs, rhs)
        return overload_bool_arr_op_nin_2
    else:
        raise RuntimeError(
            "Don't know how to register ufuncs from ufunc_db with arity > 2")


def _install_np_ufuncs():
    import numba.np.ufunc_db
    for kje__mgat in numba.np.ufunc_db.get_ufuncs():
        taie__tmqeg = create_op_overload(kje__mgat, kje__mgat.nin)
        overload(kje__mgat, no_unliteral=True)(taie__tmqeg)


_install_np_ufuncs()
skips = [operator.lt, operator.le, operator.eq, operator.ne, operator.gt,
    operator.ge, operator.add, operator.sub, operator.mul, operator.truediv,
    operator.floordiv, operator.pow, operator.mod, operator.or_, operator.and_]


def _install_binary_ops():
    for op in numba.core.typing.npydecl.NumpyRulesArrayOperator._op_map.keys():
        if op in skips:
            continue
        taie__tmqeg = create_op_overload(op, 2)
        overload(op, no_unliteral=True)(taie__tmqeg)


_install_binary_ops()


def _install_inplace_binary_ops():
    for op in numba.core.typing.npydecl.NumpyRulesInplaceArrayOperator._op_map.keys(
        ):
        taie__tmqeg = create_op_overload(op, 2)
        overload(op, no_unliteral=True)(taie__tmqeg)


_install_inplace_binary_ops()


def _install_unary_ops():
    for op in (operator.neg, operator.invert, operator.pos):
        taie__tmqeg = create_op_overload(op, 1)
        overload(op, no_unliteral=True)(taie__tmqeg)


_install_unary_ops()


@overload_method(BooleanArrayType, 'unique', no_unliteral=True)
def overload_unique(A):

    def impl_bool_arr(A):
        data = []
        bbxye__qiuak = []
        sqm__gka = False
        ffai__tgy = False
        etigw__xvoxx = False
        for edx__soca in range(len(A)):
            if bodo.libs.array_kernels.isna(A, edx__soca):
                if not sqm__gka:
                    data.append(False)
                    bbxye__qiuak.append(False)
                    sqm__gka = True
                continue
            val = A[edx__soca]
            if val and not ffai__tgy:
                data.append(True)
                bbxye__qiuak.append(True)
                ffai__tgy = True
            if not val and not etigw__xvoxx:
                data.append(False)
                bbxye__qiuak.append(True)
                etigw__xvoxx = True
            if sqm__gka and ffai__tgy and etigw__xvoxx:
                break
        ywm__odgk = np.array(data)
        n = len(ywm__odgk)
        bzvs__coqr = 1
        tjwoy__mtkj = np.empty(bzvs__coqr, np.uint8)
        for jgoa__wdmv in range(n):
            bodo.libs.int_arr_ext.set_bit_to_arr(tjwoy__mtkj, jgoa__wdmv,
                bbxye__qiuak[jgoa__wdmv])
        return init_bool_array(ywm__odgk, tjwoy__mtkj)
    return impl_bool_arr


@overload(operator.getitem, no_unliteral=True)
def bool_arr_ind_getitem(A, ind):
    if ind == boolean_array and (isinstance(A, (types.Array, bodo.libs.
        int_arr_ext.IntegerArrayType, bodo.libs.float_arr_ext.
        FloatingArrayType, bodo.libs.struct_arr_ext.StructArrayType, bodo.
        libs.array_item_arr_ext.ArrayItemArrayType, bodo.libs.map_arr_ext.
        MapArrayType, bodo.libs.tuple_arr_ext.TupleArrayType, bodo.
        CategoricalArrayType, bodo.TimeArrayType, bodo.DecimalArrayType,
        bodo.DatetimeArrayType)) or A in (string_array_type, bodo.hiframes.
        split_impl.string_array_split_view_type, boolean_array, bodo.
        datetime_date_array_type, bodo.datetime_timedelta_array_type, bodo.
        binary_array_type)):

        def impl(A, ind):
            ymcns__cws = bodo.utils.conversion.nullable_bool_to_bool_na_false(
                ind)
            return A[ymcns__cws]
        return impl


@lower_cast(types.Array(types.bool_, 1, 'C'), boolean_array)
def cast_np_bool_arr_to_bool_arr(context, builder, fromty, toty, val):
    func = lambda A: bodo.libs.bool_arr_ext.init_bool_array(A, np.full(len(
        A) + 7 >> 3, 255, np.uint8))
    aguxm__fvq = context.compile_internal(builder, func, toty(fromty), [val])
    return impl_ret_borrowed(context, builder, toty, aguxm__fvq)


@overload(operator.setitem, no_unliteral=True)
def overload_np_array_setitem_bool_arr(A, idx, val):
    if isinstance(A, types.Array) and idx == boolean_array:

        def impl(A, idx, val):
            A[idx._data] = val
        return impl


def create_nullable_logical_op_overload(op):
    aqwqt__vpxy = op == operator.or_

    def bool_array_impl(val1, val2):
        if not is_valid_boolean_array_logical_op(val1, val2):
            return
        phe__auijn = bodo.utils.utils.is_array_typ(val1, False)
        bdv__hzar = bodo.utils.utils.is_array_typ(val2, False)
        xdbd__arw = 'val1' if phe__auijn else 'val2'
        sqdj__opjj = 'def impl(val1, val2):\n'
        sqdj__opjj += f'  n = len({xdbd__arw})\n'
        sqdj__opjj += (
            '  out_arr = bodo.utils.utils.alloc_type(n, bodo.boolean_array, (-1,))\n'
            )
        sqdj__opjj += '  for i in numba.parfors.parfor.internal_prange(n):\n'
        if phe__auijn:
            null1 = 'bodo.libs.array_kernels.isna(val1, i)\n'
            jjaf__gry = 'val1[i]'
        else:
            null1 = 'False\n'
            jjaf__gry = 'val1'
        if bdv__hzar:
            null2 = 'bodo.libs.array_kernels.isna(val2, i)\n'
            ngyh__ekxh = 'val2[i]'
        else:
            null2 = 'False\n'
            ngyh__ekxh = 'val2'
        if aqwqt__vpxy:
            sqdj__opjj += f"""    result, isna_val = compute_or_body({null1}, {null2}, {jjaf__gry}, {ngyh__ekxh})
"""
        else:
            sqdj__opjj += f"""    result, isna_val = compute_and_body({null1}, {null2}, {jjaf__gry}, {ngyh__ekxh})
"""
        sqdj__opjj += '    out_arr[i] = result\n'
        sqdj__opjj += '    if isna_val:\n'
        sqdj__opjj += '      bodo.libs.array_kernels.setna(out_arr, i)\n'
        sqdj__opjj += '      continue\n'
        sqdj__opjj += '  return out_arr\n'
        djhq__mxgj = {}
        exec(sqdj__opjj, {'bodo': bodo, 'numba': numba, 'compute_and_body':
            compute_and_body, 'compute_or_body': compute_or_body}, djhq__mxgj)
        impl = djhq__mxgj['impl']
        return impl
    return bool_array_impl


def compute_or_body(null1, null2, val1, val2):
    pass


@overload(compute_or_body)
def overload_compute_or_body(null1, null2, val1, val2):

    def impl(null1, null2, val1, val2):
        if null1 and null2:
            return False, True
        elif null1:
            return val2, val2 == False
        elif null2:
            return val1, val1 == False
        else:
            return val1 | val2, False
    return impl


def compute_and_body(null1, null2, val1, val2):
    pass


@overload(compute_and_body)
def overload_compute_and_body(null1, null2, val1, val2):

    def impl(null1, null2, val1, val2):
        if null1 and null2:
            return False, True
        elif null1:
            return val2, val2 == True
        elif null2:
            return val1, val1 == True
        else:
            return val1 & val2, False
    return impl


def create_boolean_array_logical_lower_impl(op):

    def logical_lower_impl(context, builder, sig, args):
        impl = create_nullable_logical_op_overload(op)(*sig.args)
        return context.compile_internal(builder, impl, sig, args)
    return logical_lower_impl


class BooleanArrayLogicalOperatorTemplate(AbstractTemplate):

    def generic(self, args, kws):
        assert len(args) == 2
        assert not kws
        if not is_valid_boolean_array_logical_op(args[0], args[1]):
            return
        kbd__nbmzl = boolean_array
        return kbd__nbmzl(*args)


def is_valid_boolean_array_logical_op(typ1, typ2):
    ayf__iyfk = (typ1 == bodo.boolean_array or typ2 == bodo.boolean_array
        ) and (bodo.utils.utils.is_array_typ(typ1, False) and typ1.dtype ==
        types.bool_ or typ1 == types.bool_) and (bodo.utils.utils.
        is_array_typ(typ2, False) and typ2.dtype == types.bool_ or typ2 ==
        types.bool_)
    return ayf__iyfk


def _install_nullable_logical_lowering():
    for op in (operator.and_, operator.or_):
        lss__jgay = create_boolean_array_logical_lower_impl(op)
        infer_global(op)(BooleanArrayLogicalOperatorTemplate)
        for typ1, typ2 in [(boolean_array, boolean_array), (boolean_array,
            types.bool_), (boolean_array, types.Array(types.bool_, 1, 'C'))]:
            lower_builtin(op, typ1, typ2)(lss__jgay)
            if typ1 != typ2:
                lower_builtin(op, typ2, typ1)(lss__jgay)


_install_nullable_logical_lowering()
