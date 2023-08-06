import operator
import llvmlite.binding as ll
import numba
import numba.core.typing.typeof
import numpy as np
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.imputils import impl_ret_borrowed, impl_ret_new_ref
from numba.extending import box, intrinsic, make_attribute_wrapper, models, overload, overload_attribute, register_model
import bodo
from bodo.libs import hstr_ext
from bodo.libs.array_item_arr_ext import offset_type
from bodo.libs.str_arr_ext import _get_str_binary_arr_payload, _memcpy, char_arr_type, get_data_ptr, null_bitmap_arr_type, offset_arr_type, string_array_type
ll.add_symbol('array_setitem', hstr_ext.array_setitem)
ll.add_symbol('array_getptr1', hstr_ext.array_getptr1)
ll.add_symbol('dtor_str_arr_split_view', hstr_ext.dtor_str_arr_split_view)
ll.add_symbol('str_arr_split_view_impl', hstr_ext.str_arr_split_view_impl)
ll.add_symbol('str_arr_split_view_alloc', hstr_ext.str_arr_split_view_alloc)
char_typ = types.uint8
data_ctypes_type = types.ArrayCTypes(types.Array(char_typ, 1, 'C'))
offset_ctypes_type = types.ArrayCTypes(types.Array(offset_type, 1, 'C'))


class StringArraySplitViewType(types.ArrayCompatible):

    def __init__(self):
        super(StringArraySplitViewType, self).__init__(name=
            'StringArraySplitViewType()')

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    @property
    def dtype(self):
        return string_array_type

    def copy(self):
        return StringArraySplitViewType()


string_array_split_view_type = StringArraySplitViewType()


class StringArraySplitViewPayloadType(types.Type):

    def __init__(self):
        super(StringArraySplitViewPayloadType, self).__init__(name=
            'StringArraySplitViewPayloadType()')


str_arr_split_view_payload_type = StringArraySplitViewPayloadType()


@register_model(StringArraySplitViewPayloadType)
class StringArrayPayloadModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        hfm__zpbgj = [('index_offsets', types.CPointer(offset_type)), (
            'data_offsets', types.CPointer(offset_type)), ('null_bitmap',
            types.CPointer(char_typ))]
        models.StructModel.__init__(self, dmm, fe_type, hfm__zpbgj)


str_arr_model_members = [('num_items', types.uint64), ('index_offsets',
    types.CPointer(offset_type)), ('data_offsets', types.CPointer(
    offset_type)), ('data', data_ctypes_type), ('null_bitmap', types.
    CPointer(char_typ)), ('meminfo', types.MemInfoPointer(
    str_arr_split_view_payload_type))]


@register_model(StringArraySplitViewType)
class StringArrayModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        models.StructModel.__init__(self, dmm, fe_type, str_arr_model_members)


make_attribute_wrapper(StringArraySplitViewType, 'num_items', '_num_items')
make_attribute_wrapper(StringArraySplitViewType, 'index_offsets',
    '_index_offsets')
make_attribute_wrapper(StringArraySplitViewType, 'data_offsets',
    '_data_offsets')
make_attribute_wrapper(StringArraySplitViewType, 'data', '_data')
make_attribute_wrapper(StringArraySplitViewType, 'null_bitmap', '_null_bitmap')


def construct_str_arr_split_view(context, builder):
    ultux__glhi = context.get_value_type(str_arr_split_view_payload_type)
    gofe__lvpe = context.get_abi_sizeof(ultux__glhi)
    mzkkj__axss = context.get_value_type(types.voidptr)
    tnxyf__oxij = context.get_value_type(types.uintp)
    vnpwo__ikiww = lir.FunctionType(lir.VoidType(), [mzkkj__axss,
        tnxyf__oxij, mzkkj__axss])
    zgxw__ugwpt = cgutils.get_or_insert_function(builder.module,
        vnpwo__ikiww, name='dtor_str_arr_split_view')
    qwra__iow = context.nrt.meminfo_alloc_dtor(builder, context.
        get_constant(types.uintp, gofe__lvpe), zgxw__ugwpt)
    pufx__pgwlj = context.nrt.meminfo_data(builder, qwra__iow)
    pqsz__hax = builder.bitcast(pufx__pgwlj, ultux__glhi.as_pointer())
    return qwra__iow, pqsz__hax


@intrinsic
def compute_split_view(typingctx, str_arr_typ, sep_typ=None):
    assert str_arr_typ == string_array_type and isinstance(sep_typ, types.
        StringLiteral)

    def codegen(context, builder, sig, args):
        ohe__tbia, ihj__bns = args
        qwra__iow, pqsz__hax = construct_str_arr_split_view(context, builder)
        bbdj__lvvf = _get_str_binary_arr_payload(context, builder,
            ohe__tbia, string_array_type)
        hitp__ate = lir.FunctionType(lir.VoidType(), [pqsz__hax.type, lir.
            IntType(64), lir.IntType(offset_type.bitwidth).as_pointer(),
            lir.IntType(8).as_pointer(), lir.IntType(8).as_pointer(), lir.
            IntType(8)])
        fmo__qgh = cgutils.get_or_insert_function(builder.module, hitp__ate,
            name='str_arr_split_view_impl')
        wss__yki = context.make_helper(builder, offset_arr_type, bbdj__lvvf
            .offsets).data
        vfiy__het = context.make_helper(builder, char_arr_type, bbdj__lvvf.data
            ).data
        dny__fflo = context.make_helper(builder, null_bitmap_arr_type,
            bbdj__lvvf.null_bitmap).data
        yruu__scrzv = context.get_constant(types.int8, ord(sep_typ.
            literal_value))
        builder.call(fmo__qgh, [pqsz__hax, bbdj__lvvf.n_arrays, wss__yki,
            vfiy__het, dny__fflo, yruu__scrzv])
        opolj__qgca = cgutils.create_struct_proxy(
            str_arr_split_view_payload_type)(context, builder, value=
            builder.load(pqsz__hax))
        dmt__gtfrm = context.make_helper(builder, string_array_split_view_type)
        dmt__gtfrm.num_items = bbdj__lvvf.n_arrays
        dmt__gtfrm.index_offsets = opolj__qgca.index_offsets
        dmt__gtfrm.data_offsets = opolj__qgca.data_offsets
        dmt__gtfrm.data = context.compile_internal(builder, lambda S:
            get_data_ptr(S), data_ctypes_type(string_array_type), [ohe__tbia])
        dmt__gtfrm.null_bitmap = opolj__qgca.null_bitmap
        dmt__gtfrm.meminfo = qwra__iow
        zwv__rzcmx = dmt__gtfrm._getvalue()
        return impl_ret_new_ref(context, builder,
            string_array_split_view_type, zwv__rzcmx)
    return string_array_split_view_type(string_array_type, sep_typ), codegen


@box(StringArraySplitViewType)
def box_str_arr_split_view(typ, val, c):
    context = c.context
    builder = c.builder
    eop__zcpz = context.make_helper(builder, string_array_split_view_type, val)
    prp__uja = context.insert_const_string(builder.module, 'numpy')
    dpzww__afxuu = c.pyapi.import_module_noblock(prp__uja)
    dtype = c.pyapi.object_getattr_string(dpzww__afxuu, 'object_')
    wgcs__wbuf = builder.sext(eop__zcpz.num_items, c.pyapi.longlong)
    qndcw__isk = c.pyapi.long_from_longlong(wgcs__wbuf)
    wsibf__nryr = c.pyapi.call_method(dpzww__afxuu, 'ndarray', (qndcw__isk,
        dtype))
    nshuz__pcku = lir.FunctionType(lir.IntType(8).as_pointer(), [c.pyapi.
        pyobj, c.pyapi.py_ssize_t])
    oaccp__hwkz = c.pyapi._get_function(nshuz__pcku, name='array_getptr1')
    gwiy__jwok = lir.FunctionType(lir.VoidType(), [c.pyapi.pyobj, lir.
        IntType(8).as_pointer(), c.pyapi.pyobj])
    gdi__xyno = c.pyapi._get_function(gwiy__jwok, name='array_setitem')
    yoa__oqgw = c.pyapi.object_getattr_string(dpzww__afxuu, 'nan')
    with cgutils.for_range(builder, eop__zcpz.num_items) as jixo__ebchs:
        str_ind = jixo__ebchs.index
        imc__eizi = builder.sext(builder.load(builder.gep(eop__zcpz.
            index_offsets, [str_ind])), lir.IntType(64))
        fqw__kmuxg = builder.sext(builder.load(builder.gep(eop__zcpz.
            index_offsets, [builder.add(str_ind, str_ind.type(1))])), lir.
            IntType(64))
        abnd__dynqj = builder.lshr(str_ind, lir.Constant(lir.IntType(64), 3))
        dkrx__wgofy = builder.gep(eop__zcpz.null_bitmap, [abnd__dynqj])
        ddxp__slzv = builder.load(dkrx__wgofy)
        wwy__lypu = builder.trunc(builder.and_(str_ind, lir.Constant(lir.
            IntType(64), 7)), lir.IntType(8))
        val = builder.and_(builder.lshr(ddxp__slzv, wwy__lypu), lir.
            Constant(lir.IntType(8), 1))
        qcz__dckq = builder.sub(fqw__kmuxg, imc__eizi)
        qcz__dckq = builder.sub(qcz__dckq, qcz__dckq.type(1))
        nfdkl__yxnmz = builder.call(oaccp__hwkz, [wsibf__nryr, str_ind])
        afz__lohux = c.builder.icmp_unsigned('!=', val, val.type(0))
        with c.builder.if_else(afz__lohux) as (hxo__ltfk, bcs__uijs):
            with hxo__ltfk:
                foa__eek = c.pyapi.list_new(qcz__dckq)
                with c.builder.if_then(cgutils.is_not_null(c.builder,
                    foa__eek), likely=True):
                    with cgutils.for_range(c.builder, qcz__dckq
                        ) as jixo__ebchs:
                        fkilm__pvlsa = builder.add(imc__eizi, jixo__ebchs.index
                            )
                        data_start = builder.load(builder.gep(eop__zcpz.
                            data_offsets, [fkilm__pvlsa]))
                        data_start = builder.add(data_start, data_start.type(1)
                            )
                        ehsz__gsc = builder.load(builder.gep(eop__zcpz.
                            data_offsets, [builder.add(fkilm__pvlsa,
                            fkilm__pvlsa.type(1))]))
                        ylx__eqahe = builder.gep(builder.extract_value(
                            eop__zcpz.data, 0), [data_start])
                        jdj__zgn = builder.sext(builder.sub(ehsz__gsc,
                            data_start), lir.IntType(64))
                        tbgob__ztdef = c.pyapi.string_from_string_and_size(
                            ylx__eqahe, jdj__zgn)
                        c.pyapi.list_setitem(foa__eek, jixo__ebchs.index,
                            tbgob__ztdef)
                builder.call(gdi__xyno, [wsibf__nryr, nfdkl__yxnmz, foa__eek])
            with bcs__uijs:
                builder.call(gdi__xyno, [wsibf__nryr, nfdkl__yxnmz, yoa__oqgw])
    c.pyapi.decref(dpzww__afxuu)
    c.pyapi.decref(dtype)
    c.pyapi.decref(yoa__oqgw)
    return wsibf__nryr


@intrinsic
def pre_alloc_str_arr_view(typingctx, num_items_t, num_offsets_t, data_t=None):
    assert num_items_t == types.intp and num_offsets_t == types.intp

    def codegen(context, builder, sig, args):
        asbhj__zevro, zguv__ufh, ylx__eqahe = args
        qwra__iow, pqsz__hax = construct_str_arr_split_view(context, builder)
        hitp__ate = lir.FunctionType(lir.VoidType(), [pqsz__hax.type, lir.
            IntType(64), lir.IntType(64)])
        fmo__qgh = cgutils.get_or_insert_function(builder.module, hitp__ate,
            name='str_arr_split_view_alloc')
        builder.call(fmo__qgh, [pqsz__hax, asbhj__zevro, zguv__ufh])
        opolj__qgca = cgutils.create_struct_proxy(
            str_arr_split_view_payload_type)(context, builder, value=
            builder.load(pqsz__hax))
        dmt__gtfrm = context.make_helper(builder, string_array_split_view_type)
        dmt__gtfrm.num_items = asbhj__zevro
        dmt__gtfrm.index_offsets = opolj__qgca.index_offsets
        dmt__gtfrm.data_offsets = opolj__qgca.data_offsets
        dmt__gtfrm.data = ylx__eqahe
        dmt__gtfrm.null_bitmap = opolj__qgca.null_bitmap
        context.nrt.incref(builder, data_t, ylx__eqahe)
        dmt__gtfrm.meminfo = qwra__iow
        zwv__rzcmx = dmt__gtfrm._getvalue()
        return impl_ret_new_ref(context, builder,
            string_array_split_view_type, zwv__rzcmx)
    return string_array_split_view_type(types.intp, types.intp, data_t
        ), codegen


@intrinsic
def get_c_arr_ptr(typingctx, c_arr, ind_t=None):
    assert isinstance(c_arr, (types.CPointer, types.ArrayCTypes))

    def codegen(context, builder, sig, args):
        daw__lbno, ind = args
        if isinstance(sig.args[0], types.ArrayCTypes):
            daw__lbno = builder.extract_value(daw__lbno, 0)
        return builder.bitcast(builder.gep(daw__lbno, [ind]), lir.IntType(8
            ).as_pointer())
    return types.voidptr(c_arr, ind_t), codegen


@intrinsic
def getitem_c_arr(typingctx, c_arr, ind_t=None):

    def codegen(context, builder, sig, args):
        daw__lbno, ind = args
        if isinstance(sig.args[0], types.ArrayCTypes):
            daw__lbno = builder.extract_value(daw__lbno, 0)
        return builder.load(builder.gep(daw__lbno, [ind]))
    return c_arr.dtype(c_arr, ind_t), codegen


@intrinsic
def setitem_c_arr(typingctx, c_arr, ind_t, item_t=None):

    def codegen(context, builder, sig, args):
        daw__lbno, ind, dugjh__wtmwv = args
        rqp__pbcj = builder.gep(daw__lbno, [ind])
        builder.store(dugjh__wtmwv, rqp__pbcj)
    return types.void(c_arr, ind_t, c_arr.dtype), codegen


@intrinsic
def get_array_ctypes_ptr(typingctx, arr_ctypes_t, ind_t=None):

    def codegen(context, builder, sig, args):
        ssbq__ubcpt, ind = args
        zvm__izlpd = context.make_helper(builder, arr_ctypes_t, ssbq__ubcpt)
        mip__lmx = context.make_helper(builder, arr_ctypes_t)
        mip__lmx.data = builder.gep(zvm__izlpd.data, [ind])
        mip__lmx.meminfo = zvm__izlpd.meminfo
        ykk__naa = mip__lmx._getvalue()
        return impl_ret_borrowed(context, builder, arr_ctypes_t, ykk__naa)
    return arr_ctypes_t(arr_ctypes_t, ind_t), codegen


@numba.njit(no_cpython_wrapper=True)
def get_split_view_index(arr, item_ind, str_ind):
    yquv__zkm = bodo.libs.int_arr_ext.get_bit_bitmap_arr(arr._null_bitmap,
        item_ind)
    if not yquv__zkm:
        return 0, 0, 0
    fkilm__pvlsa = getitem_c_arr(arr._index_offsets, item_ind)
    pigza__upa = getitem_c_arr(arr._index_offsets, item_ind + 1) - 1
    aoodu__ohsm = pigza__upa - fkilm__pvlsa
    if str_ind >= aoodu__ohsm:
        return 0, 0, 0
    data_start = getitem_c_arr(arr._data_offsets, fkilm__pvlsa + str_ind)
    data_start += 1
    if fkilm__pvlsa + str_ind == 0:
        data_start = 0
    ehsz__gsc = getitem_c_arr(arr._data_offsets, fkilm__pvlsa + str_ind + 1)
    ywftf__wojj = ehsz__gsc - data_start
    return 1, data_start, ywftf__wojj


@numba.njit(no_cpython_wrapper=True)
def get_split_view_data_ptr(arr, data_start):
    return get_array_ctypes_ptr(arr._data, data_start)


@overload(len, no_unliteral=True)
def str_arr_split_view_len_overload(arr):
    if arr == string_array_split_view_type:
        return lambda arr: np.int64(arr._num_items)


@overload_attribute(StringArraySplitViewType, 'shape')
def overload_split_view_arr_shape(A):
    return lambda A: (np.int64(A._num_items),)


@overload(operator.getitem, no_unliteral=True)
def str_arr_split_view_getitem_overload(A, ind):
    if A != string_array_split_view_type:
        return
    if A == string_array_split_view_type and isinstance(ind, types.Integer):
        hxuu__uhfv = numba.cpython.unicode.PY_UNICODE_1BYTE_KIND

        def _impl(A, ind):
            fkilm__pvlsa = getitem_c_arr(A._index_offsets, ind)
            pigza__upa = getitem_c_arr(A._index_offsets, ind + 1)
            olrdy__fue = pigza__upa - fkilm__pvlsa - 1
            ohe__tbia = bodo.libs.str_arr_ext.pre_alloc_string_array(olrdy__fue
                , -1)
            for jneu__xlae in range(olrdy__fue):
                data_start = getitem_c_arr(A._data_offsets, fkilm__pvlsa +
                    jneu__xlae)
                data_start += 1
                if fkilm__pvlsa + jneu__xlae == 0:
                    data_start = 0
                ehsz__gsc = getitem_c_arr(A._data_offsets, fkilm__pvlsa +
                    jneu__xlae + 1)
                ywftf__wojj = ehsz__gsc - data_start
                rqp__pbcj = get_array_ctypes_ptr(A._data, data_start)
                uuurs__pxbm = bodo.libs.str_arr_ext.decode_utf8(rqp__pbcj,
                    ywftf__wojj)
                ohe__tbia[jneu__xlae] = uuurs__pxbm
            return ohe__tbia
        return _impl
    if A == string_array_split_view_type and ind == types.Array(types.bool_,
        1, 'C'):
        vfeok__ukb = offset_type.bitwidth // 8

        def _impl(A, ind):
            olrdy__fue = len(A)
            if olrdy__fue != len(ind):
                raise IndexError(
                    'boolean index did not match indexed array along dimension 0'
                    )
            asbhj__zevro = 0
            zguv__ufh = 0
            for jneu__xlae in range(olrdy__fue):
                if ind[jneu__xlae]:
                    asbhj__zevro += 1
                    fkilm__pvlsa = getitem_c_arr(A._index_offsets, jneu__xlae)
                    pigza__upa = getitem_c_arr(A._index_offsets, jneu__xlae + 1
                        )
                    zguv__ufh += pigza__upa - fkilm__pvlsa
            wsibf__nryr = pre_alloc_str_arr_view(asbhj__zevro, zguv__ufh, A
                ._data)
            item_ind = 0
            ntfc__dizj = 0
            for jneu__xlae in range(olrdy__fue):
                if ind[jneu__xlae]:
                    fkilm__pvlsa = getitem_c_arr(A._index_offsets, jneu__xlae)
                    pigza__upa = getitem_c_arr(A._index_offsets, jneu__xlae + 1
                        )
                    bdl__ptvx = pigza__upa - fkilm__pvlsa
                    setitem_c_arr(wsibf__nryr._index_offsets, item_ind,
                        ntfc__dizj)
                    rqp__pbcj = get_c_arr_ptr(A._data_offsets, fkilm__pvlsa)
                    der__tvbp = get_c_arr_ptr(wsibf__nryr._data_offsets,
                        ntfc__dizj)
                    _memcpy(der__tvbp, rqp__pbcj, bdl__ptvx, vfeok__ukb)
                    yquv__zkm = bodo.libs.int_arr_ext.get_bit_bitmap_arr(A.
                        _null_bitmap, jneu__xlae)
                    bodo.libs.int_arr_ext.set_bit_to_arr(wsibf__nryr.
                        _null_bitmap, item_ind, yquv__zkm)
                    item_ind += 1
                    ntfc__dizj += bdl__ptvx
            setitem_c_arr(wsibf__nryr._index_offsets, item_ind, ntfc__dizj)
            return wsibf__nryr
        return _impl
