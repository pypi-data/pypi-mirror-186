"""CSR Matrix data type implementation for scipy.sparse.csr_matrix
"""
import operator
import numba
import numpy as np
from numba.core import cgutils, types
from numba.extending import NativeValue, box, intrinsic, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_model, typeof_impl, unbox
import bodo
from bodo.utils.typing import BodoError


class CSRMatrixType(types.ArrayCompatible):
    ndim = 2

    def __init__(self, dtype, idx_dtype):
        self.dtype = dtype
        self.idx_dtype = idx_dtype
        super(CSRMatrixType, self).__init__(name=
            f'CSRMatrixType({dtype}, {idx_dtype})')

    @property
    def as_array(self):
        return types.Array(types.undefined, 2, 'C')

    def copy(self):
        return CSRMatrixType(self.dtype, self.idx_dtype)


@register_model(CSRMatrixType)
class CSRMatrixModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        odteo__zahe = [('data', types.Array(fe_type.dtype, 1, 'C')), (
            'indices', types.Array(fe_type.idx_dtype, 1, 'C')), ('indptr',
            types.Array(fe_type.idx_dtype, 1, 'C')), ('shape', types.
            UniTuple(types.int64, 2))]
        models.StructModel.__init__(self, dmm, fe_type, odteo__zahe)


make_attribute_wrapper(CSRMatrixType, 'data', 'data')
make_attribute_wrapper(CSRMatrixType, 'indices', 'indices')
make_attribute_wrapper(CSRMatrixType, 'indptr', 'indptr')
make_attribute_wrapper(CSRMatrixType, 'shape', 'shape')


@intrinsic
def init_csr_matrix(typingctx, data_t, indices_t, indptr_t, shape_t=None):
    assert isinstance(data_t, types.Array)
    assert isinstance(indices_t, types.Array) and isinstance(indices_t.
        dtype, types.Integer)
    assert indices_t == indptr_t

    def codegen(context, builder, signature, args):
        emth__rlw, zrfxx__fbb, tsbqe__riums, plnh__yelm = args
        bgsu__avo = cgutils.create_struct_proxy(signature.return_type)(context,
            builder)
        bgsu__avo.data = emth__rlw
        bgsu__avo.indices = zrfxx__fbb
        bgsu__avo.indptr = tsbqe__riums
        bgsu__avo.shape = plnh__yelm
        context.nrt.incref(builder, signature.args[0], emth__rlw)
        context.nrt.incref(builder, signature.args[1], zrfxx__fbb)
        context.nrt.incref(builder, signature.args[2], tsbqe__riums)
        return bgsu__avo._getvalue()
    clkix__dtydf = CSRMatrixType(data_t.dtype, indices_t.dtype)
    wwxbw__cnbd = clkix__dtydf(data_t, indices_t, indptr_t, types.UniTuple(
        types.int64, 2))
    return wwxbw__cnbd, codegen


if bodo.utils.utils.has_scipy():
    import scipy.sparse

    @typeof_impl.register(scipy.sparse.csr_matrix)
    def _typeof_csr_matrix(val, c):
        dtype = numba.from_dtype(val.dtype)
        idx_dtype = numba.from_dtype(val.indices.dtype)
        return CSRMatrixType(dtype, idx_dtype)


@unbox(CSRMatrixType)
def unbox_csr_matrix(typ, val, c):
    bgsu__avo = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    tqv__zqnr = c.pyapi.object_getattr_string(val, 'data')
    uqgo__hdiup = c.pyapi.object_getattr_string(val, 'indices')
    nyevr__dgb = c.pyapi.object_getattr_string(val, 'indptr')
    tzuud__kihn = c.pyapi.object_getattr_string(val, 'shape')
    bgsu__avo.data = c.pyapi.to_native_value(types.Array(typ.dtype, 1, 'C'),
        tqv__zqnr).value
    bgsu__avo.indices = c.pyapi.to_native_value(types.Array(typ.idx_dtype, 
        1, 'C'), uqgo__hdiup).value
    bgsu__avo.indptr = c.pyapi.to_native_value(types.Array(typ.idx_dtype, 1,
        'C'), nyevr__dgb).value
    bgsu__avo.shape = c.pyapi.to_native_value(types.UniTuple(types.int64, 2
        ), tzuud__kihn).value
    c.pyapi.decref(tqv__zqnr)
    c.pyapi.decref(uqgo__hdiup)
    c.pyapi.decref(nyevr__dgb)
    c.pyapi.decref(tzuud__kihn)
    hfn__hlscg = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(bgsu__avo._getvalue(), is_error=hfn__hlscg)


@box(CSRMatrixType)
def box_csr_matrix(typ, val, c):
    trorw__xdb = c.context.insert_const_string(c.builder.module, 'scipy.sparse'
        )
    kwzs__dcli = c.pyapi.import_module_noblock(trorw__xdb)
    bgsu__avo = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    c.context.nrt.incref(c.builder, types.Array(typ.dtype, 1, 'C'),
        bgsu__avo.data)
    tqv__zqnr = c.pyapi.from_native_value(types.Array(typ.dtype, 1, 'C'),
        bgsu__avo.data, c.env_manager)
    c.context.nrt.incref(c.builder, types.Array(typ.idx_dtype, 1, 'C'),
        bgsu__avo.indices)
    uqgo__hdiup = c.pyapi.from_native_value(types.Array(typ.idx_dtype, 1,
        'C'), bgsu__avo.indices, c.env_manager)
    c.context.nrt.incref(c.builder, types.Array(typ.idx_dtype, 1, 'C'),
        bgsu__avo.indptr)
    nyevr__dgb = c.pyapi.from_native_value(types.Array(typ.idx_dtype, 1,
        'C'), bgsu__avo.indptr, c.env_manager)
    tzuud__kihn = c.pyapi.from_native_value(types.UniTuple(types.int64, 2),
        bgsu__avo.shape, c.env_manager)
    uqcks__shbjw = c.pyapi.tuple_pack([tqv__zqnr, uqgo__hdiup, nyevr__dgb])
    efrh__wamtd = c.pyapi.call_method(kwzs__dcli, 'csr_matrix', (
        uqcks__shbjw, tzuud__kihn))
    c.pyapi.decref(uqcks__shbjw)
    c.pyapi.decref(tqv__zqnr)
    c.pyapi.decref(uqgo__hdiup)
    c.pyapi.decref(nyevr__dgb)
    c.pyapi.decref(tzuud__kihn)
    c.pyapi.decref(kwzs__dcli)
    c.context.nrt.decref(c.builder, typ, val)
    return efrh__wamtd


@overload(len, no_unliteral=True)
def overload_csr_matrix_len(A):
    if isinstance(A, CSRMatrixType):
        return lambda A: A.shape[0]


@overload_attribute(CSRMatrixType, 'ndim')
def overload_csr_matrix_ndim(A):
    return lambda A: 2


@overload_method(CSRMatrixType, 'copy', no_unliteral=True)
def overload_csr_matrix_copy(A):

    def copy_impl(A):
        return init_csr_matrix(A.data.copy(), A.indices.copy(), A.indptr.
            copy(), A.shape)
    return copy_impl


@overload(operator.getitem, no_unliteral=True)
def csr_matrix_getitem(A, idx):
    if not isinstance(A, CSRMatrixType):
        return
    idcmc__maq = A.dtype
    bmmf__ymcad = A.idx_dtype
    if isinstance(idx, types.BaseTuple) and len(idx) == 2 and isinstance(idx
        [0], types.SliceType) and isinstance(idx[1], types.SliceType):

        def impl(A, idx):
            xmew__wtntb, pur__cra = A.shape
            ajhyl__rwx = numba.cpython.unicode._normalize_slice(idx[0],
                xmew__wtntb)
            jregd__qrr = numba.cpython.unicode._normalize_slice(idx[1],
                pur__cra)
            if ajhyl__rwx.step != 1 or jregd__qrr.step != 1:
                raise ValueError(
                    'CSR matrix slice getitem only supports step=1 currently')
            suwkj__sthu = ajhyl__rwx.start
            ghn__vdtwd = ajhyl__rwx.stop
            ogt__puxt = jregd__qrr.start
            ccba__zohw = jregd__qrr.stop
            oknr__sbnp = A.indptr
            dhewd__wol = A.indices
            szeuf__dvba = A.data
            lnn__afml = ghn__vdtwd - suwkj__sthu
            qyc__qmqs = ccba__zohw - ogt__puxt
            jbakj__kde = 0
            mhuvh__zvcx = 0
            for ltj__jrpe in range(lnn__afml):
                qwvoo__tqwc = oknr__sbnp[suwkj__sthu + ltj__jrpe]
                onxab__ejvjq = oknr__sbnp[suwkj__sthu + ltj__jrpe + 1]
                for jmaov__fneia in range(qwvoo__tqwc, onxab__ejvjq):
                    if dhewd__wol[jmaov__fneia] >= ogt__puxt and dhewd__wol[
                        jmaov__fneia] < ccba__zohw:
                        jbakj__kde += 1
            pzbvf__onc = np.empty(lnn__afml + 1, bmmf__ymcad)
            sta__khp = np.empty(jbakj__kde, bmmf__ymcad)
            dale__kijlu = np.empty(jbakj__kde, idcmc__maq)
            pzbvf__onc[0] = 0
            for ltj__jrpe in range(lnn__afml):
                qwvoo__tqwc = oknr__sbnp[suwkj__sthu + ltj__jrpe]
                onxab__ejvjq = oknr__sbnp[suwkj__sthu + ltj__jrpe + 1]
                for jmaov__fneia in range(qwvoo__tqwc, onxab__ejvjq):
                    if dhewd__wol[jmaov__fneia] >= ogt__puxt and dhewd__wol[
                        jmaov__fneia] < ccba__zohw:
                        sta__khp[mhuvh__zvcx] = dhewd__wol[jmaov__fneia
                            ] - ogt__puxt
                        dale__kijlu[mhuvh__zvcx] = szeuf__dvba[jmaov__fneia]
                        mhuvh__zvcx += 1
                pzbvf__onc[ltj__jrpe + 1] = mhuvh__zvcx
            return init_csr_matrix(dale__kijlu, sta__khp, pzbvf__onc, (
                lnn__afml, qyc__qmqs))
        return impl
    elif isinstance(idx, types.Array
        ) and idx.ndim == 1 and idx.dtype == bmmf__ymcad:

        def impl(A, idx):
            xmew__wtntb, pur__cra = A.shape
            oknr__sbnp = A.indptr
            dhewd__wol = A.indices
            szeuf__dvba = A.data
            lnn__afml = len(idx)
            jbakj__kde = 0
            mhuvh__zvcx = 0
            for ltj__jrpe in range(lnn__afml):
                bpl__prfgx = idx[ltj__jrpe]
                qwvoo__tqwc = oknr__sbnp[bpl__prfgx]
                onxab__ejvjq = oknr__sbnp[bpl__prfgx + 1]
                jbakj__kde += onxab__ejvjq - qwvoo__tqwc
            pzbvf__onc = np.empty(lnn__afml + 1, bmmf__ymcad)
            sta__khp = np.empty(jbakj__kde, bmmf__ymcad)
            dale__kijlu = np.empty(jbakj__kde, idcmc__maq)
            pzbvf__onc[0] = 0
            for ltj__jrpe in range(lnn__afml):
                bpl__prfgx = idx[ltj__jrpe]
                qwvoo__tqwc = oknr__sbnp[bpl__prfgx]
                onxab__ejvjq = oknr__sbnp[bpl__prfgx + 1]
                sta__khp[mhuvh__zvcx:mhuvh__zvcx + onxab__ejvjq - qwvoo__tqwc
                    ] = dhewd__wol[qwvoo__tqwc:onxab__ejvjq]
                dale__kijlu[mhuvh__zvcx:mhuvh__zvcx + onxab__ejvjq -
                    qwvoo__tqwc] = szeuf__dvba[qwvoo__tqwc:onxab__ejvjq]
                mhuvh__zvcx += onxab__ejvjq - qwvoo__tqwc
                pzbvf__onc[ltj__jrpe + 1] = mhuvh__zvcx
            hgoz__jpxp = init_csr_matrix(dale__kijlu, sta__khp, pzbvf__onc,
                (lnn__afml, pur__cra))
            return hgoz__jpxp
        return impl
    raise BodoError(
        f'getitem for CSR matrix with index type {idx} not supported yet.')
