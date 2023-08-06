import enum
import operator
import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.imputils import lower_constant
from numba.extending import NativeValue, box, intrinsic, lower_cast, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_jitable, register_model, typeof_impl, unbox
from numba.parfors.array_analysis import ArrayAnalysis
import bodo
from bodo.utils.typing import NOT_CONSTANT, BodoError, MetaType, check_unsupported_args, dtype_to_array_type, get_literal_value, get_overload_const, get_overload_const_bool, is_common_scalar_dtype, is_iterable_type, is_list_like_index_type, is_literal_type, is_overload_constant_bool, is_overload_none, is_overload_true, is_scalar_type, raise_bodo_error


class PDCategoricalDtype(types.Opaque):

    def __init__(self, categories, elem_type, ordered, data=None, int_type=None
        ):
        self.categories = categories
        self.elem_type = elem_type
        self.ordered = ordered
        self.data = _get_cat_index_type(elem_type) if data is None else data
        self.int_type = int_type
        dxd__cdw = (
            f'PDCategoricalDtype({self.categories}, {self.elem_type}, {self.ordered}, {self.data}, {self.int_type})'
            )
        super(PDCategoricalDtype, self).__init__(name=dxd__cdw)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


@typeof_impl.register(pd.CategoricalDtype)
def _typeof_pd_cat_dtype(val, c):
    cknge__tsd = tuple(val.categories.values)
    elem_type = None if len(cknge__tsd) == 0 else bodo.typeof(val.
        categories.values).dtype
    int_type = getattr(val, '_int_type', None)
    return PDCategoricalDtype(cknge__tsd, elem_type, val.ordered, bodo.
        typeof(val.categories), int_type)


def _get_cat_index_type(elem_type):
    elem_type = bodo.string_type if elem_type is None else elem_type
    return bodo.utils.typing.get_index_type_from_dtype(elem_type)


@lower_constant(PDCategoricalDtype)
def lower_constant_categorical_type(context, builder, typ, pyval):
    categories = context.get_constant_generic(builder, bodo.typeof(pyval.
        categories), pyval.categories)
    ordered = context.get_constant(types.bool_, pyval.ordered)
    return lir.Constant.literal_struct([categories, ordered])


@register_model(PDCategoricalDtype)
class PDCategoricalDtypeModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        hut__cwd = [('categories', fe_type.data), ('ordered', types.bool_)]
        models.StructModel.__init__(self, dmm, fe_type, hut__cwd)


make_attribute_wrapper(PDCategoricalDtype, 'categories', 'categories')
make_attribute_wrapper(PDCategoricalDtype, 'ordered', 'ordered')


@intrinsic
def init_cat_dtype(typingctx, categories_typ, ordered_typ, int_type,
    cat_vals_typ=None):
    assert bodo.hiframes.pd_index_ext.is_index_type(categories_typ
        ), 'init_cat_dtype requires index type for categories'
    assert is_overload_constant_bool(ordered_typ
        ), 'init_cat_dtype requires constant ordered flag'
    txgv__opx = None if is_overload_none(int_type) else int_type.dtype
    assert is_overload_none(cat_vals_typ) or isinstance(cat_vals_typ, types
        .TypeRef), 'init_cat_dtype requires constant category values'
    kcgyl__zlit = None if is_overload_none(cat_vals_typ
        ) else cat_vals_typ.instance_type.meta

    def codegen(context, builder, sig, args):
        categories, ordered, ekvn__xpjp, ekvn__xpjp = args
        cat_dtype = cgutils.create_struct_proxy(sig.return_type)(context,
            builder)
        cat_dtype.categories = categories
        context.nrt.incref(builder, sig.args[0], categories)
        context.nrt.incref(builder, sig.args[1], ordered)
        cat_dtype.ordered = ordered
        return cat_dtype._getvalue()
    sxgwd__bdcw = PDCategoricalDtype(kcgyl__zlit, categories_typ.dtype,
        is_overload_true(ordered_typ), categories_typ, txgv__opx)
    return sxgwd__bdcw(categories_typ, ordered_typ, int_type, cat_vals_typ
        ), codegen


@unbox(PDCategoricalDtype)
def unbox_cat_dtype(typ, obj, c):
    cat_dtype = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    nzrh__aicwm = c.pyapi.object_getattr_string(obj, 'ordered')
    cat_dtype.ordered = c.pyapi.to_native_value(types.bool_, nzrh__aicwm).value
    c.pyapi.decref(nzrh__aicwm)
    pff__pssjm = c.pyapi.object_getattr_string(obj, 'categories')
    cat_dtype.categories = c.pyapi.to_native_value(typ.data, pff__pssjm).value
    c.pyapi.decref(pff__pssjm)
    gigxo__oyjg = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(cat_dtype._getvalue(), is_error=gigxo__oyjg)


@box(PDCategoricalDtype)
def box_cat_dtype(typ, val, c):
    cat_dtype = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    nzrh__aicwm = c.pyapi.from_native_value(types.bool_, cat_dtype.ordered,
        c.env_manager)
    c.context.nrt.incref(c.builder, typ.data, cat_dtype.categories)
    xzqyf__jtdxc = c.pyapi.from_native_value(typ.data, cat_dtype.categories,
        c.env_manager)
    nwk__vhb = c.context.insert_const_string(c.builder.module, 'pandas')
    nbla__jjp = c.pyapi.import_module_noblock(nwk__vhb)
    idgym__mky = c.pyapi.call_method(nbla__jjp, 'CategoricalDtype', (
        xzqyf__jtdxc, nzrh__aicwm))
    c.pyapi.decref(nzrh__aicwm)
    c.pyapi.decref(xzqyf__jtdxc)
    c.pyapi.decref(nbla__jjp)
    c.context.nrt.decref(c.builder, typ, val)
    return idgym__mky


@overload_attribute(PDCategoricalDtype, 'nbytes')
def pd_categorical_nbytes_overload(A):
    return lambda A: A.categories.nbytes + bodo.io.np_io.get_dtype_size(types
        .bool_)


class CategoricalArrayType(types.ArrayCompatible):

    def __init__(self, dtype):
        self.dtype = dtype
        super(CategoricalArrayType, self).__init__(name=
            f'CategoricalArrayType({dtype})')

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    def copy(self):
        return CategoricalArrayType(self.dtype)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


@typeof_impl.register(pd.Categorical)
def _typeof_pd_cat(val, c):
    return CategoricalArrayType(bodo.typeof(val.dtype))


@register_model(CategoricalArrayType)
class CategoricalArrayModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        har__vny = get_categories_int_type(fe_type.dtype)
        hut__cwd = [('dtype', fe_type.dtype), ('codes', types.Array(
            har__vny, 1, 'C'))]
        super(CategoricalArrayModel, self).__init__(dmm, fe_type, hut__cwd)


make_attribute_wrapper(CategoricalArrayType, 'codes', 'codes')
make_attribute_wrapper(CategoricalArrayType, 'dtype', 'dtype')


@unbox(CategoricalArrayType)
def unbox_categorical_array(typ, val, c):
    wlp__spkj = c.pyapi.object_getattr_string(val, 'codes')
    dtype = get_categories_int_type(typ.dtype)
    codes = c.pyapi.to_native_value(types.Array(dtype, 1, 'C'), wlp__spkj
        ).value
    c.pyapi.decref(wlp__spkj)
    idgym__mky = c.pyapi.object_getattr_string(val, 'dtype')
    exrx__irbfz = c.pyapi.to_native_value(typ.dtype, idgym__mky).value
    c.pyapi.decref(idgym__mky)
    llhf__msme = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    llhf__msme.codes = codes
    llhf__msme.dtype = exrx__irbfz
    return NativeValue(llhf__msme._getvalue())


@lower_constant(CategoricalArrayType)
def lower_constant_categorical_array(context, builder, typ, pyval):
    syfka__wwu = get_categories_int_type(typ.dtype)
    fxub__xmp = context.get_constant_generic(builder, types.Array(
        syfka__wwu, 1, 'C'), pyval.codes)
    cat_dtype = context.get_constant_generic(builder, typ.dtype, pyval.dtype)
    return lir.Constant.literal_struct([cat_dtype, fxub__xmp])


def get_categories_int_type(cat_dtype):
    dtype = types.int64
    if cat_dtype.int_type is not None:
        return cat_dtype.int_type
    if cat_dtype.categories is None:
        return types.int64
    sll__nxbno = len(cat_dtype.categories)
    if sll__nxbno < np.iinfo(np.int8).max:
        dtype = types.int8
    elif sll__nxbno < np.iinfo(np.int16).max:
        dtype = types.int16
    elif sll__nxbno < np.iinfo(np.int32).max:
        dtype = types.int32
    return dtype


@box(CategoricalArrayType)
def box_categorical_array(typ, val, c):
    dtype = typ.dtype
    nwk__vhb = c.context.insert_const_string(c.builder.module, 'pandas')
    nbla__jjp = c.pyapi.import_module_noblock(nwk__vhb)
    har__vny = get_categories_int_type(dtype)
    dth__php = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    bun__lkbos = types.Array(har__vny, 1, 'C')
    c.context.nrt.incref(c.builder, bun__lkbos, dth__php.codes)
    wlp__spkj = c.pyapi.from_native_value(bun__lkbos, dth__php.codes, c.
        env_manager)
    c.context.nrt.incref(c.builder, dtype, dth__php.dtype)
    idgym__mky = c.pyapi.from_native_value(dtype, dth__php.dtype, c.env_manager
        )
    jowb__ztpks = c.pyapi.borrow_none()
    qok__nscbx = c.pyapi.object_getattr_string(nbla__jjp, 'Categorical')
    qkjys__ejvp = c.pyapi.call_method(qok__nscbx, 'from_codes', (wlp__spkj,
        jowb__ztpks, jowb__ztpks, idgym__mky))
    c.pyapi.decref(qok__nscbx)
    c.pyapi.decref(wlp__spkj)
    c.pyapi.decref(idgym__mky)
    c.pyapi.decref(nbla__jjp)
    c.context.nrt.decref(c.builder, typ, val)
    return qkjys__ejvp


def _to_readonly(t):
    from bodo.hiframes.pd_index_ext import DatetimeIndexType, NumericIndexType, TimedeltaIndexType
    if isinstance(t, CategoricalArrayType):
        return CategoricalArrayType(_to_readonly(t.dtype))
    if isinstance(t, PDCategoricalDtype):
        return PDCategoricalDtype(t.categories, t.elem_type, t.ordered,
            _to_readonly(t.data), t.int_type)
    if isinstance(t, types.Array):
        return types.Array(t.dtype, t.ndim, 'C', True)
    if isinstance(t, NumericIndexType):
        return NumericIndexType(t.dtype, t.name_typ, _to_readonly(t.data))
    if isinstance(t, (DatetimeIndexType, TimedeltaIndexType)):
        return t.__class__(t.name_typ, _to_readonly(t.data))
    return t


@lower_cast(CategoricalArrayType, CategoricalArrayType)
def cast_cat_arr(context, builder, fromty, toty, val):
    if _to_readonly(toty) == fromty:
        return val
    raise BodoError(f'Cannot cast from {fromty} to {toty}')


def create_cmp_op_overload(op):

    def overload_cat_arr_cmp(A, other):
        if not isinstance(A, CategoricalArrayType):
            return
        if A.dtype.categories and is_literal_type(other) and types.unliteral(
            other) == A.dtype.elem_type:
            val = get_literal_value(other)
            fajjb__urf = list(A.dtype.categories).index(val
                ) if val in A.dtype.categories else -2

            def impl_lit(A, other):
                pkert__ubabs = op(bodo.hiframes.pd_categorical_ext.
                    get_categorical_arr_codes(A), fajjb__urf)
                return pkert__ubabs
            return impl_lit

        def impl(A, other):
            fajjb__urf = get_code_for_value(A.dtype, other)
            pkert__ubabs = op(bodo.hiframes.pd_categorical_ext.
                get_categorical_arr_codes(A), fajjb__urf)
            return pkert__ubabs
        return impl
    return overload_cat_arr_cmp


def _install_cmp_ops():
    for op in [operator.eq, operator.ne]:
        tnb__vwg = create_cmp_op_overload(op)
        overload(op, inline='always', no_unliteral=True)(tnb__vwg)


_install_cmp_ops()


@register_jitable
def get_code_for_value(cat_dtype, val):
    dth__php = cat_dtype.categories
    n = len(dth__php)
    for ojr__lioy in range(n):
        if dth__php[ojr__lioy] == val:
            return ojr__lioy
    return -2


@overload_method(CategoricalArrayType, 'astype', inline='always',
    no_unliteral=True)
def overload_cat_arr_astype(A, dtype, copy=True, _bodo_nan_to_str=True):
    if dtype == types.unicode_type:
        raise_bodo_error(
            "CategoricalArray.astype(): 'dtype' when passed as string must be a constant value"
            )
    sewsw__zjxp = bodo.utils.typing.parse_dtype(dtype,
        'CategoricalArray.astype')
    if sewsw__zjxp != A.dtype.elem_type and sewsw__zjxp != types.unicode_type:
        raise BodoError(
            f'Converting categorical array {A} to dtype {dtype} not supported yet'
            )
    if sewsw__zjxp == types.unicode_type:

        def impl(A, dtype, copy=True, _bodo_nan_to_str=True):
            codes = bodo.hiframes.pd_categorical_ext.get_categorical_arr_codes(
                A)
            categories = A.dtype.categories
            n = len(codes)
            pkert__ubabs = bodo.libs.str_arr_ext.pre_alloc_string_array(n, -1)
            for ojr__lioy in numba.parfors.parfor.internal_prange(n):
                bht__ccb = codes[ojr__lioy]
                if bht__ccb == -1:
                    if _bodo_nan_to_str:
                        bodo.libs.str_arr_ext.str_arr_setitem_NA_str(
                            pkert__ubabs, ojr__lioy)
                    else:
                        bodo.libs.array_kernels.setna(pkert__ubabs, ojr__lioy)
                    continue
                pkert__ubabs[ojr__lioy] = str(bodo.utils.conversion.
                    unbox_if_tz_naive_timestamp(categories[bht__ccb]))
            return pkert__ubabs
        return impl
    bun__lkbos = dtype_to_array_type(sewsw__zjxp)

    def impl(A, dtype, copy=True, _bodo_nan_to_str=True):
        codes = bodo.hiframes.pd_categorical_ext.get_categorical_arr_codes(A)
        categories = A.dtype.categories
        n = len(codes)
        pkert__ubabs = bodo.utils.utils.alloc_type(n, bun__lkbos, (-1,))
        for ojr__lioy in numba.parfors.parfor.internal_prange(n):
            bht__ccb = codes[ojr__lioy]
            if bht__ccb == -1:
                bodo.libs.array_kernels.setna(pkert__ubabs, ojr__lioy)
                continue
            pkert__ubabs[ojr__lioy
                ] = bodo.utils.conversion.unbox_if_tz_naive_timestamp(
                categories[bht__ccb])
        return pkert__ubabs
    return impl


@overload(pd.api.types.CategoricalDtype, no_unliteral=True)
def cat_overload_dummy(val_list):
    return lambda val_list: 1


@intrinsic
def init_categorical_array(typingctx, codes, cat_dtype=None):
    assert isinstance(codes, types.Array) and isinstance(codes.dtype, types
        .Integer)

    def codegen(context, builder, signature, args):
        viufp__ddlbp, exrx__irbfz = args
        dth__php = cgutils.create_struct_proxy(signature.return_type)(context,
            builder)
        dth__php.codes = viufp__ddlbp
        dth__php.dtype = exrx__irbfz
        context.nrt.incref(builder, signature.args[0], viufp__ddlbp)
        context.nrt.incref(builder, signature.args[1], exrx__irbfz)
        return dth__php._getvalue()
    dtknx__ptqng = CategoricalArrayType(cat_dtype)
    sig = dtknx__ptqng(codes, cat_dtype)
    return sig, codegen


def init_categorical_array_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 2 and not kws
    rlj__gwum = args[0]
    if equiv_set.has_shape(rlj__gwum):
        return ArrayAnalysis.AnalyzeResult(shape=rlj__gwum, pre=[])
    return None


(ArrayAnalysis.
    _analyze_op_call_bodo_hiframes_pd_categorical_ext_init_categorical_array
    ) = init_categorical_array_equiv


def alloc_categorical_array(n, cat_dtype):
    pass


@overload(alloc_categorical_array, no_unliteral=True)
def _alloc_categorical_array(n, cat_dtype):
    har__vny = get_categories_int_type(cat_dtype)

    def impl(n, cat_dtype):
        codes = np.empty(n, har__vny)
        return init_categorical_array(codes, cat_dtype)
    return impl


def alloc_categorical_array_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 2 and not kws
    return ArrayAnalysis.AnalyzeResult(shape=args[0], pre=[])


(ArrayAnalysis.
    _analyze_op_call_bodo_hiframes_pd_categorical_ext_alloc_categorical_array
    ) = alloc_categorical_array_equiv


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def get_categorical_arr_codes(A):
    return lambda A: A.codes


def alias_ext_dummy_func(lhs_name, args, alias_map, arg_aliases):
    assert len(args) >= 1
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)


numba.core.ir_utils.alias_func_extensions['init_categorical_array',
    'bodo.hiframes.pd_categorical_ext'] = alias_ext_dummy_func
numba.core.ir_utils.alias_func_extensions['get_categorical_arr_codes',
    'bodo.hiframes.pd_categorical_ext'] = alias_ext_dummy_func


@overload_method(CategoricalArrayType, 'copy', no_unliteral=True)
def cat_arr_copy_overload(arr):
    return lambda arr: init_categorical_array(arr.codes.copy(), arr.dtype)


def build_replace_dicts(to_replace, value, categories):
    return dict(), np.empty(len(categories) + 1), 0


@overload(build_replace_dicts, no_unliteral=True)
def _build_replace_dicts(to_replace, value, categories):
    if isinstance(to_replace, types.Number) or to_replace == bodo.string_type:

        def impl(to_replace, value, categories):
            return build_replace_dicts([to_replace], value, categories)
        return impl
    else:

        def impl(to_replace, value, categories):
            n = len(categories)
            dzmp__ezfrw = {}
            fxub__xmp = np.empty(n + 1, np.int64)
            wta__bvr = {}
            ywoe__vgt = []
            ykvn__nkop = {}
            for ojr__lioy in range(n):
                ykvn__nkop[categories[ojr__lioy]] = ojr__lioy
            for prt__rilmk in to_replace:
                if prt__rilmk != value:
                    if prt__rilmk in ykvn__nkop:
                        if value in ykvn__nkop:
                            dzmp__ezfrw[prt__rilmk] = prt__rilmk
                            hvb__pmnqx = ykvn__nkop[prt__rilmk]
                            wta__bvr[hvb__pmnqx] = ykvn__nkop[value]
                            ywoe__vgt.append(hvb__pmnqx)
                        else:
                            dzmp__ezfrw[prt__rilmk] = value
                            ykvn__nkop[value] = ykvn__nkop[prt__rilmk]
            cxs__zfl = np.sort(np.array(ywoe__vgt))
            ifyrg__flbxd = 0
            ynfp__qix = []
            for ytkts__oabvk in range(-1, n):
                while ifyrg__flbxd < len(cxs__zfl) and ytkts__oabvk > cxs__zfl[
                    ifyrg__flbxd]:
                    ifyrg__flbxd += 1
                ynfp__qix.append(ifyrg__flbxd)
            for ptg__wzhgu in range(-1, n):
                wxbl__jdapv = ptg__wzhgu
                if ptg__wzhgu in wta__bvr:
                    wxbl__jdapv = wta__bvr[ptg__wzhgu]
                fxub__xmp[ptg__wzhgu + 1] = wxbl__jdapv - ynfp__qix[
                    wxbl__jdapv + 1]
            return dzmp__ezfrw, fxub__xmp, len(cxs__zfl)
        return impl


@numba.njit
def python_build_replace_dicts(to_replace, value, categories):
    return build_replace_dicts(to_replace, value, categories)


@register_jitable
def reassign_codes(new_codes_arr, old_codes_arr, codes_map_arr):
    for ojr__lioy in range(len(new_codes_arr)):
        new_codes_arr[ojr__lioy] = codes_map_arr[old_codes_arr[ojr__lioy] + 1]


@overload_method(CategoricalArrayType, 'replace', inline='always',
    no_unliteral=True)
def overload_replace(arr, to_replace, value):

    def impl(arr, to_replace, value):
        return bodo.hiframes.pd_categorical_ext.cat_replace(arr, to_replace,
            value)
    return impl


def cat_replace(arr, to_replace, value):
    return


@overload(cat_replace, no_unliteral=True)
def cat_replace_overload(arr, to_replace, value):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(to_replace,
        'CategoricalArray.replace()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(value,
        'CategoricalArray.replace()')
    idrpq__bjkps = arr.dtype.ordered
    sso__buxwg = arr.dtype.elem_type
    yfi__inlli = get_overload_const(to_replace)
    klixw__uzay = get_overload_const(value)
    if (arr.dtype.categories is not None and yfi__inlli is not NOT_CONSTANT and
        klixw__uzay is not NOT_CONSTANT):
        emtu__hzt, codes_map_arr, ekvn__xpjp = python_build_replace_dicts(
            yfi__inlli, klixw__uzay, arr.dtype.categories)
        if len(emtu__hzt) == 0:
            return lambda arr, to_replace, value: arr.copy()
        zsq__ywvz = []
        for elrwt__qzpj in arr.dtype.categories:
            if elrwt__qzpj in emtu__hzt:
                wzvx__vppdd = emtu__hzt[elrwt__qzpj]
                if wzvx__vppdd != elrwt__qzpj:
                    zsq__ywvz.append(wzvx__vppdd)
            else:
                zsq__ywvz.append(elrwt__qzpj)
        dgub__rql = bodo.utils.utils.create_categorical_type(zsq__ywvz, arr
            .dtype.data.data, idrpq__bjkps)
        gsr__ajwhi = MetaType(tuple(dgub__rql))

        def impl_dtype(arr, to_replace, value):
            jalo__ety = init_cat_dtype(bodo.utils.conversion.
                index_from_array(dgub__rql), idrpq__bjkps, None, gsr__ajwhi)
            dth__php = alloc_categorical_array(len(arr.codes), jalo__ety)
            reassign_codes(dth__php.codes, arr.codes, codes_map_arr)
            return dth__php
        return impl_dtype
    sso__buxwg = arr.dtype.elem_type
    if sso__buxwg == types.unicode_type:

        def impl_str(arr, to_replace, value):
            categories = arr.dtype.categories
            dzmp__ezfrw, codes_map_arr, tmf__yyo = build_replace_dicts(
                to_replace, value, categories.values)
            if len(dzmp__ezfrw) == 0:
                return init_categorical_array(arr.codes.copy().astype(np.
                    int64), init_cat_dtype(categories.copy(), idrpq__bjkps,
                    None, None))
            n = len(categories)
            dgub__rql = bodo.libs.str_arr_ext.pre_alloc_string_array(n -
                tmf__yyo, -1)
            mbqtm__xjgus = 0
            for ytkts__oabvk in range(n):
                mggp__fhfbb = categories[ytkts__oabvk]
                if mggp__fhfbb in dzmp__ezfrw:
                    rfpk__zsv = dzmp__ezfrw[mggp__fhfbb]
                    if rfpk__zsv != mggp__fhfbb:
                        dgub__rql[mbqtm__xjgus] = rfpk__zsv
                        mbqtm__xjgus += 1
                else:
                    dgub__rql[mbqtm__xjgus] = mggp__fhfbb
                    mbqtm__xjgus += 1
            dth__php = alloc_categorical_array(len(arr.codes),
                init_cat_dtype(bodo.utils.conversion.index_from_array(
                dgub__rql), idrpq__bjkps, None, None))
            reassign_codes(dth__php.codes, arr.codes, codes_map_arr)
            return dth__php
        return impl_str
    kgg__gihzz = dtype_to_array_type(sso__buxwg)

    def impl(arr, to_replace, value):
        categories = arr.dtype.categories
        dzmp__ezfrw, codes_map_arr, tmf__yyo = build_replace_dicts(to_replace,
            value, categories.values)
        if len(dzmp__ezfrw) == 0:
            return init_categorical_array(arr.codes.copy().astype(np.int64),
                init_cat_dtype(categories.copy(), idrpq__bjkps, None, None))
        n = len(categories)
        dgub__rql = bodo.utils.utils.alloc_type(n - tmf__yyo, kgg__gihzz, None)
        mbqtm__xjgus = 0
        for ojr__lioy in range(n):
            mggp__fhfbb = categories[ojr__lioy]
            if mggp__fhfbb in dzmp__ezfrw:
                rfpk__zsv = dzmp__ezfrw[mggp__fhfbb]
                if rfpk__zsv != mggp__fhfbb:
                    dgub__rql[mbqtm__xjgus] = rfpk__zsv
                    mbqtm__xjgus += 1
            else:
                dgub__rql[mbqtm__xjgus] = mggp__fhfbb
                mbqtm__xjgus += 1
        dth__php = alloc_categorical_array(len(arr.codes), init_cat_dtype(
            bodo.utils.conversion.index_from_array(dgub__rql), idrpq__bjkps,
            None, None))
        reassign_codes(dth__php.codes, arr.codes, codes_map_arr)
        return dth__php
    return impl


@overload(len, no_unliteral=True)
def overload_cat_arr_len(A):
    if isinstance(A, CategoricalArrayType):
        return lambda A: len(A.codes)


@overload_attribute(CategoricalArrayType, 'shape')
def overload_cat_arr_shape(A):
    return lambda A: (len(A.codes),)


@overload_attribute(CategoricalArrayType, 'ndim')
def overload_cat_arr_ndim(A):
    return lambda A: 1


@overload_attribute(CategoricalArrayType, 'nbytes')
def cat_arr_nbytes_overload(A):
    return lambda A: A.codes.nbytes + A.dtype.nbytes


@register_jitable
def get_label_dict_from_categories(vals):
    xuo__bdstq = dict()
    lgzs__bqi = 0
    for ojr__lioy in range(len(vals)):
        val = vals[ojr__lioy]
        if val in xuo__bdstq:
            continue
        xuo__bdstq[val] = lgzs__bqi
        lgzs__bqi += 1
    return xuo__bdstq


@register_jitable
def get_label_dict_from_categories_no_duplicates(vals):
    xuo__bdstq = dict()
    for ojr__lioy in range(len(vals)):
        val = vals[ojr__lioy]
        xuo__bdstq[val] = ojr__lioy
    return xuo__bdstq


@overload(pd.Categorical, no_unliteral=True)
def pd_categorical_overload(values, categories=None, ordered=None, dtype=
    None, fastpath=False):
    wks__tien = dict(fastpath=fastpath)
    hondj__fcub = dict(fastpath=False)
    check_unsupported_args('pd.Categorical', wks__tien, hondj__fcub)
    if isinstance(dtype, bodo.hiframes.pd_categorical_ext.PDCategoricalDtype):

        def impl_dtype(values, categories=None, ordered=None, dtype=None,
            fastpath=False):
            data = bodo.utils.conversion.coerce_to_array(values)
            return bodo.utils.conversion.fix_arr_dtype(data, dtype)
        return impl_dtype
    if not is_overload_none(categories):
        xsc__fapd = get_overload_const(categories)
        if xsc__fapd is not NOT_CONSTANT and get_overload_const(ordered
            ) is not NOT_CONSTANT:
            if is_overload_none(ordered):
                bzla__rbinj = False
            else:
                bzla__rbinj = get_overload_const_bool(ordered)
            bpt__mas = pd.CategoricalDtype(pd.array(xsc__fapd), bzla__rbinj
                ).categories.array
            mhtil__cars = MetaType(tuple(bpt__mas))

            def impl_cats_const(values, categories=None, ordered=None,
                dtype=None, fastpath=False):
                data = bodo.utils.conversion.coerce_to_array(values)
                jalo__ety = init_cat_dtype(bodo.utils.conversion.
                    index_from_array(bpt__mas), bzla__rbinj, None, mhtil__cars)
                return bodo.utils.conversion.fix_arr_dtype(data, jalo__ety)
            return impl_cats_const

        def impl_cats(values, categories=None, ordered=None, dtype=None,
            fastpath=False):
            ordered = bodo.utils.conversion.false_if_none(ordered)
            data = bodo.utils.conversion.coerce_to_array(values)
            cknge__tsd = bodo.utils.conversion.convert_to_index(categories)
            cat_dtype = bodo.hiframes.pd_categorical_ext.init_cat_dtype(
                cknge__tsd, ordered, None, None)
            return bodo.utils.conversion.fix_arr_dtype(data, cat_dtype)
        return impl_cats
    elif is_overload_none(ordered):

        def impl_auto(values, categories=None, ordered=None, dtype=None,
            fastpath=False):
            data = bodo.utils.conversion.coerce_to_array(values)
            return bodo.utils.conversion.fix_arr_dtype(data, 'category')
        return impl_auto
    raise BodoError(
        f'pd.Categorical(): argument combination not supported yet: {values}, {categories}, {ordered}, {dtype}'
        )


@overload(operator.getitem, no_unliteral=True)
def categorical_array_getitem(arr, ind):
    if not isinstance(arr, CategoricalArrayType):
        return
    if isinstance(ind, types.Integer):

        def categorical_getitem_impl(arr, ind):
            phx__ppu = arr.codes[ind]
            return arr.dtype.categories[max(phx__ppu, 0)]
        return categorical_getitem_impl
    if ind != bodo.boolean_array and is_list_like_index_type(ind
        ) or isinstance(ind, types.SliceType):

        def impl_bool(arr, ind):
            return init_categorical_array(arr.codes[ind], arr.dtype)
        return impl_bool
    if ind != bodo.boolean_array:
        raise BodoError(
            f'getitem for CategoricalArrayType with indexing type {ind} not supported.'
            )


class CategoricalMatchingValues(enum.Enum):
    DIFFERENT_TYPES = -1
    DONT_MATCH = 0
    MAY_MATCH = 1
    DO_MATCH = 2


def categorical_arrs_match(arr1, arr2):
    if not (isinstance(arr1, CategoricalArrayType) and isinstance(arr2,
        CategoricalArrayType)):
        return CategoricalMatchingValues.DIFFERENT_TYPES
    if arr1.dtype.categories is None or arr2.dtype.categories is None:
        return CategoricalMatchingValues.MAY_MATCH
    return (CategoricalMatchingValues.DO_MATCH if arr1.dtype.categories ==
        arr2.dtype.categories and arr1.dtype.ordered == arr2.dtype.ordered else
        CategoricalMatchingValues.DONT_MATCH)


@register_jitable
def cat_dtype_equal(dtype1, dtype2):
    if dtype1.ordered != dtype2.ordered or len(dtype1.categories) != len(dtype2
        .categories):
        return False
    arr1 = dtype1.categories.values
    arr2 = dtype2.categories.values
    for ojr__lioy in range(len(arr1)):
        if arr1[ojr__lioy] != arr2[ojr__lioy]:
            return False
    return True


@overload(operator.setitem, no_unliteral=True)
def categorical_array_setitem(arr, ind, val):
    if not isinstance(arr, CategoricalArrayType):
        return
    if val == types.none or isinstance(val, types.optional):
        return
    islu__knlg = is_scalar_type(val) and is_common_scalar_dtype([types.
        unliteral(val), arr.dtype.elem_type]) and not (isinstance(arr.dtype
        .elem_type, types.Integer) and isinstance(val, types.Float))
    thz__jcot = not isinstance(val, CategoricalArrayType) and is_iterable_type(
        val) and is_common_scalar_dtype([val.dtype, arr.dtype.elem_type]
        ) and not (isinstance(arr.dtype.elem_type, types.Integer) and
        isinstance(val.dtype, types.Float))
    dlswr__oxrq = categorical_arrs_match(arr, val)
    dcr__oeeg = (
        f"setitem for CategoricalArrayType of dtype {arr.dtype} with indexing type {ind} received an incorrect 'value' type {val}."
        )
    tcfx__whlfm = (
        'Cannot set a Categorical with another, without identical categories')
    if isinstance(ind, types.Integer):
        if not islu__knlg:
            raise BodoError(dcr__oeeg)

        def impl_scalar(arr, ind, val):
            if val not in arr.dtype.categories:
                raise ValueError(
                    'Cannot setitem on a Categorical with a new category, set the categories first'
                    )
            phx__ppu = arr.dtype.categories.get_loc(val)
            arr.codes[ind] = phx__ppu
        return impl_scalar
    if is_list_like_index_type(ind) and isinstance(ind.dtype, types.Integer):
        if not (islu__knlg or thz__jcot or dlswr__oxrq !=
            CategoricalMatchingValues.DIFFERENT_TYPES):
            raise BodoError(dcr__oeeg)
        if dlswr__oxrq == CategoricalMatchingValues.DONT_MATCH:
            raise BodoError(tcfx__whlfm)
        if islu__knlg:

            def impl_scalar(arr, ind, val):
                if val not in arr.dtype.categories:
                    raise ValueError(
                        'Cannot setitem on a Categorical with a new category, set the categories first'
                        )
                wmx__puh = arr.dtype.categories.get_loc(val)
                n = len(ind)
                for ytkts__oabvk in range(n):
                    arr.codes[ind[ytkts__oabvk]] = wmx__puh
            return impl_scalar
        if dlswr__oxrq == CategoricalMatchingValues.DO_MATCH:

            def impl_arr_ind_mask(arr, ind, val):
                n = len(val.codes)
                for ojr__lioy in range(n):
                    arr.codes[ind[ojr__lioy]] = val.codes[ojr__lioy]
            return impl_arr_ind_mask
        if dlswr__oxrq == CategoricalMatchingValues.MAY_MATCH:

            def impl_arr_ind_mask(arr, ind, val):
                if not cat_dtype_equal(arr.dtype, val.dtype):
                    raise ValueError(tcfx__whlfm)
                n = len(val.codes)
                for ojr__lioy in range(n):
                    arr.codes[ind[ojr__lioy]] = val.codes[ojr__lioy]
            return impl_arr_ind_mask
        if thz__jcot:

            def impl_arr_ind_mask_cat_values(arr, ind, val):
                n = len(val)
                categories = arr.dtype.categories
                for ytkts__oabvk in range(n):
                    qnyay__lna = (bodo.utils.conversion.
                        unbox_if_tz_naive_timestamp(val[ytkts__oabvk]))
                    if qnyay__lna not in categories:
                        raise ValueError(
                            'Cannot setitem on a Categorical with a new category, set the categories first'
                            )
                    phx__ppu = categories.get_loc(qnyay__lna)
                    arr.codes[ind[ytkts__oabvk]] = phx__ppu
            return impl_arr_ind_mask_cat_values
    if is_list_like_index_type(ind) and ind.dtype == types.bool_:
        if not (islu__knlg or thz__jcot or dlswr__oxrq !=
            CategoricalMatchingValues.DIFFERENT_TYPES):
            raise BodoError(dcr__oeeg)
        if dlswr__oxrq == CategoricalMatchingValues.DONT_MATCH:
            raise BodoError(tcfx__whlfm)
        if islu__knlg:

            def impl_scalar(arr, ind, val):
                if val not in arr.dtype.categories:
                    raise ValueError(
                        'Cannot setitem on a Categorical with a new category, set the categories first'
                        )
                wmx__puh = arr.dtype.categories.get_loc(val)
                n = len(ind)
                for ytkts__oabvk in range(n):
                    if ind[ytkts__oabvk]:
                        arr.codes[ytkts__oabvk] = wmx__puh
            return impl_scalar
        if dlswr__oxrq == CategoricalMatchingValues.DO_MATCH:

            def impl_bool_ind_mask(arr, ind, val):
                n = len(ind)
                wbcua__ypy = 0
                for ojr__lioy in range(n):
                    if ind[ojr__lioy]:
                        arr.codes[ojr__lioy] = val.codes[wbcua__ypy]
                        wbcua__ypy += 1
            return impl_bool_ind_mask
        if dlswr__oxrq == CategoricalMatchingValues.MAY_MATCH:

            def impl_bool_ind_mask(arr, ind, val):
                if not cat_dtype_equal(arr.dtype, val.dtype):
                    raise ValueError(tcfx__whlfm)
                n = len(ind)
                wbcua__ypy = 0
                for ojr__lioy in range(n):
                    if ind[ojr__lioy]:
                        arr.codes[ojr__lioy] = val.codes[wbcua__ypy]
                        wbcua__ypy += 1
            return impl_bool_ind_mask
        if thz__jcot:

            def impl_bool_ind_mask_cat_values(arr, ind, val):
                n = len(ind)
                wbcua__ypy = 0
                categories = arr.dtype.categories
                for ytkts__oabvk in range(n):
                    if ind[ytkts__oabvk]:
                        qnyay__lna = (bodo.utils.conversion.
                            unbox_if_tz_naive_timestamp(val[wbcua__ypy]))
                        if qnyay__lna not in categories:
                            raise ValueError(
                                'Cannot setitem on a Categorical with a new category, set the categories first'
                                )
                        phx__ppu = categories.get_loc(qnyay__lna)
                        arr.codes[ytkts__oabvk] = phx__ppu
                        wbcua__ypy += 1
            return impl_bool_ind_mask_cat_values
    if isinstance(ind, types.SliceType):
        if not (islu__knlg or thz__jcot or dlswr__oxrq !=
            CategoricalMatchingValues.DIFFERENT_TYPES):
            raise BodoError(dcr__oeeg)
        if dlswr__oxrq == CategoricalMatchingValues.DONT_MATCH:
            raise BodoError(tcfx__whlfm)
        if islu__knlg:

            def impl_scalar(arr, ind, val):
                if val not in arr.dtype.categories:
                    raise ValueError(
                        'Cannot setitem on a Categorical with a new category, set the categories first'
                        )
                wmx__puh = arr.dtype.categories.get_loc(val)
                mtydh__wcu = numba.cpython.unicode._normalize_slice(ind,
                    len(arr))
                for ytkts__oabvk in range(mtydh__wcu.start, mtydh__wcu.stop,
                    mtydh__wcu.step):
                    arr.codes[ytkts__oabvk] = wmx__puh
            return impl_scalar
        if dlswr__oxrq == CategoricalMatchingValues.DO_MATCH:

            def impl_arr(arr, ind, val):
                arr.codes[ind] = val.codes
            return impl_arr
        if dlswr__oxrq == CategoricalMatchingValues.MAY_MATCH:

            def impl_arr(arr, ind, val):
                if not cat_dtype_equal(arr.dtype, val.dtype):
                    raise ValueError(tcfx__whlfm)
                arr.codes[ind] = val.codes
            return impl_arr
        if thz__jcot:

            def impl_slice_cat_values(arr, ind, val):
                categories = arr.dtype.categories
                mtydh__wcu = numba.cpython.unicode._normalize_slice(ind,
                    len(arr))
                wbcua__ypy = 0
                for ytkts__oabvk in range(mtydh__wcu.start, mtydh__wcu.stop,
                    mtydh__wcu.step):
                    qnyay__lna = (bodo.utils.conversion.
                        unbox_if_tz_naive_timestamp(val[wbcua__ypy]))
                    if qnyay__lna not in categories:
                        raise ValueError(
                            'Cannot setitem on a Categorical with a new category, set the categories first'
                            )
                    phx__ppu = categories.get_loc(qnyay__lna)
                    arr.codes[ytkts__oabvk] = phx__ppu
                    wbcua__ypy += 1
            return impl_slice_cat_values
    raise BodoError(
        f'setitem for CategoricalArrayType with indexing type {ind} not supported.'
        )
