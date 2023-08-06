"""Table data type for storing dataframe column arrays. Supports storing many columns
(e.g. >10k) efficiently.
"""
import operator
from collections import defaultdict
import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.imputils import impl_ret_borrowed, lower_constant
from numba.core.ir_utils import guard
from numba.core.typing.templates import signature
from numba.cpython.listobj import ListInstance
from numba.extending import NativeValue, box, infer_getattr, intrinsic, lower_builtin, lower_getattr, make_attribute_wrapper, models, overload, register_model, typeof_impl, unbox
from numba.np.arrayobj import _getitem_array_single_int
from numba.parfors.array_analysis import ArrayAnalysis
import bodo
from bodo.hiframes.pd_series_ext import SeriesType
from bodo.utils.cg_helpers import is_ll_eq
from bodo.utils.templates import OverloadedKeyAttributeTemplate
from bodo.utils.typing import BodoError, MetaType, decode_if_dict_array, get_overload_const_int, is_list_like_index_type, is_overload_constant_bool, is_overload_constant_int, is_overload_none, is_overload_true, raise_bodo_error, to_str_arr_if_dict_array, unwrap_typeref
from bodo.utils.utils import is_whole_slice


class Table:

    def __init__(self, arrs, usecols=None, num_arrs=-1):
        if usecols is not None:
            assert num_arrs != -1, 'num_arrs must be provided if usecols is not None'
            plocm__erjj = 0
            lah__mwx = []
            for i in range(usecols[-1] + 1):
                if i == usecols[plocm__erjj]:
                    lah__mwx.append(arrs[plocm__erjj])
                    plocm__erjj += 1
                else:
                    lah__mwx.append(None)
            for mbheb__cpypu in range(usecols[-1] + 1, num_arrs):
                lah__mwx.append(None)
            self.arrays = lah__mwx
        else:
            self.arrays = arrs
        self.block_0 = arrs

    def __eq__(self, other):
        return isinstance(other, Table) and len(self.arrays) == len(other.
            arrays) and all((mpbd__naiv == jooe__yiqla).all() for 
            mpbd__naiv, jooe__yiqla in zip(self.arrays, other.arrays))

    def __str__(self) ->str:
        return str(self.arrays)

    def to_pandas(self, index=None):
        dcvg__gfvbk = len(self.arrays)
        nsus__oraiv = dict(zip(range(dcvg__gfvbk), self.arrays))
        df = pd.DataFrame(nsus__oraiv, index)
        return df


class TableType(types.ArrayCompatible):

    def __init__(self, arr_types, has_runtime_cols=False):
        self.arr_types = arr_types
        self.has_runtime_cols = has_runtime_cols
        slah__dwh = []
        iemrz__eloi = []
        fuxfj__ahs = {}
        sio__hjx = {}
        iawsb__euxdl = defaultdict(int)
        xzylu__ndiis = defaultdict(list)
        if not has_runtime_cols:
            for i, t in enumerate(arr_types):
                if t not in fuxfj__ahs:
                    ggo__ojthp = len(fuxfj__ahs)
                    fuxfj__ahs[t] = ggo__ojthp
                    sio__hjx[ggo__ojthp] = t
                nfr__qnths = fuxfj__ahs[t]
                slah__dwh.append(nfr__qnths)
                iemrz__eloi.append(iawsb__euxdl[nfr__qnths])
                iawsb__euxdl[nfr__qnths] += 1
                xzylu__ndiis[nfr__qnths].append(i)
        self.block_nums = slah__dwh
        self.block_offsets = iemrz__eloi
        self.type_to_blk = fuxfj__ahs
        self.blk_to_type = sio__hjx
        self.block_to_arr_ind = xzylu__ndiis
        super(TableType, self).__init__(name=
            f'TableType({arr_types}, {has_runtime_cols})')

    @property
    def as_array(self):
        return types.Array(types.undefined, 2, 'C')

    @property
    def key(self):
        return self.arr_types, self.has_runtime_cols

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


@typeof_impl.register(Table)
def typeof_table(val, c):
    return TableType(tuple(numba.typeof(arr) for arr in val.arrays))


@register_model(TableType)
class TableTypeModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        if fe_type.has_runtime_cols:
            ybe__nox = [(f'block_{i}', types.List(t)) for i, t in enumerate
                (fe_type.arr_types)]
        else:
            ybe__nox = [(f'block_{nfr__qnths}', types.List(t)) for t,
                nfr__qnths in fe_type.type_to_blk.items()]
        ybe__nox.append(('parent', types.pyobject))
        ybe__nox.append(('len', types.int64))
        super(TableTypeModel, self).__init__(dmm, fe_type, ybe__nox)


make_attribute_wrapper(TableType, 'block_0', 'block_0')
make_attribute_wrapper(TableType, 'len', '_len')


@infer_getattr
class TableTypeAttribute(OverloadedKeyAttributeTemplate):
    key = TableType

    def resolve_shape(self, df):
        return types.Tuple([types.int64, types.int64])


@unbox(TableType)
def unbox_table(typ, val, c):
    wofj__vxit = c.pyapi.object_getattr_string(val, 'arrays')
    table = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    table.parent = cgutils.get_null_value(table.parent.type)
    air__lmep = c.pyapi.make_none()
    rrtx__tait = c.context.get_constant(types.int64, 0)
    vgwp__cufl = cgutils.alloca_once_value(c.builder, rrtx__tait)
    for t, nfr__qnths in typ.type_to_blk.items():
        jhsmx__hii = c.context.get_constant(types.int64, len(typ.
            block_to_arr_ind[nfr__qnths]))
        mbheb__cpypu, rycjc__ebko = ListInstance.allocate_ex(c.context, c.
            builder, types.List(t), jhsmx__hii)
        rycjc__ebko.size = jhsmx__hii
        eredo__jug = c.context.make_constant_array(c.builder, types.Array(
            types.int64, 1, 'C'), np.array(typ.block_to_arr_ind[nfr__qnths],
            dtype=np.int64))
        sir__jnzan = c.context.make_array(types.Array(types.int64, 1, 'C'))(c
            .context, c.builder, eredo__jug)
        with cgutils.for_range(c.builder, jhsmx__hii) as cafsd__acft:
            i = cafsd__acft.index
            qry__lhb = _getitem_array_single_int(c.context, c.builder,
                types.int64, types.Array(types.int64, 1, 'C'), sir__jnzan, i)
            kjesm__elphk = c.pyapi.long_from_longlong(qry__lhb)
            vbs__qizqp = c.pyapi.object_getitem(wofj__vxit, kjesm__elphk)
            xgdhv__jmzzi = c.builder.icmp_unsigned('==', vbs__qizqp, air__lmep)
            with c.builder.if_else(xgdhv__jmzzi) as (vonr__embt, hozqz__sashc):
                with vonr__embt:
                    cvknw__qegr = c.context.get_constant_null(t)
                    rycjc__ebko.inititem(i, cvknw__qegr, incref=False)
                with hozqz__sashc:
                    nith__lbjhq = c.pyapi.call_method(vbs__qizqp, '__len__', ()
                        )
                    lehxf__kdwos = c.pyapi.long_as_longlong(nith__lbjhq)
                    c.builder.store(lehxf__kdwos, vgwp__cufl)
                    c.pyapi.decref(nith__lbjhq)
                    arr = c.pyapi.to_native_value(t, vbs__qizqp).value
                    rycjc__ebko.inititem(i, arr, incref=False)
            c.pyapi.decref(vbs__qizqp)
            c.pyapi.decref(kjesm__elphk)
        setattr(table, f'block_{nfr__qnths}', rycjc__ebko.value)
    table.len = c.builder.load(vgwp__cufl)
    c.pyapi.decref(wofj__vxit)
    c.pyapi.decref(air__lmep)
    wdbuj__fxei = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(table._getvalue(), is_error=wdbuj__fxei)


@box(TableType)
def box_table(typ, val, c, ensure_unboxed=None):
    from bodo.hiframes.boxing import get_df_obj_column_codegen
    table = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    if typ.has_runtime_cols:
        kmk__enawb = c.context.get_constant(types.int64, 0)
        for i, t in enumerate(typ.arr_types):
            lah__mwx = getattr(table, f'block_{i}')
            phh__wmux = ListInstance(c.context, c.builder, types.List(t),
                lah__mwx)
            kmk__enawb = c.builder.add(kmk__enawb, phh__wmux.size)
        idl__zkfx = c.pyapi.list_new(kmk__enawb)
        oze__pqjrj = c.context.get_constant(types.int64, 0)
        for i, t in enumerate(typ.arr_types):
            lah__mwx = getattr(table, f'block_{i}')
            phh__wmux = ListInstance(c.context, c.builder, types.List(t),
                lah__mwx)
            with cgutils.for_range(c.builder, phh__wmux.size) as cafsd__acft:
                i = cafsd__acft.index
                arr = phh__wmux.getitem(i)
                c.context.nrt.incref(c.builder, t, arr)
                idx = c.builder.add(oze__pqjrj, i)
                c.pyapi.list_setitem(idl__zkfx, idx, c.pyapi.
                    from_native_value(t, arr, c.env_manager))
            oze__pqjrj = c.builder.add(oze__pqjrj, phh__wmux.size)
        mwn__skjwg = c.pyapi.unserialize(c.pyapi.serialize_object(Table))
        uws__xfj = c.pyapi.call_function_objargs(mwn__skjwg, (idl__zkfx,))
        c.pyapi.decref(mwn__skjwg)
        c.pyapi.decref(idl__zkfx)
        c.context.nrt.decref(c.builder, typ, val)
        return uws__xfj
    idl__zkfx = c.pyapi.list_new(c.context.get_constant(types.int64, len(
        typ.arr_types)))
    ssgpf__gwbx = cgutils.is_not_null(c.builder, table.parent)
    if ensure_unboxed is None:
        ensure_unboxed = c.context.get_constant(types.bool_, False)
    for t, nfr__qnths in typ.type_to_blk.items():
        lah__mwx = getattr(table, f'block_{nfr__qnths}')
        phh__wmux = ListInstance(c.context, c.builder, types.List(t), lah__mwx)
        eredo__jug = c.context.make_constant_array(c.builder, types.Array(
            types.int64, 1, 'C'), np.array(typ.block_to_arr_ind[nfr__qnths],
            dtype=np.int64))
        sir__jnzan = c.context.make_array(types.Array(types.int64, 1, 'C'))(c
            .context, c.builder, eredo__jug)
        with cgutils.for_range(c.builder, phh__wmux.size) as cafsd__acft:
            i = cafsd__acft.index
            qry__lhb = _getitem_array_single_int(c.context, c.builder,
                types.int64, types.Array(types.int64, 1, 'C'), sir__jnzan, i)
            arr = phh__wmux.getitem(i)
            oaz__lboif = cgutils.alloca_once_value(c.builder, arr)
            hbx__pgygw = cgutils.alloca_once_value(c.builder, c.context.
                get_constant_null(t))
            is_null = is_ll_eq(c.builder, oaz__lboif, hbx__pgygw)
            with c.builder.if_else(c.builder.and_(is_null, c.builder.not_(
                ensure_unboxed))) as (vonr__embt, hozqz__sashc):
                with vonr__embt:
                    air__lmep = c.pyapi.make_none()
                    c.pyapi.list_setitem(idl__zkfx, qry__lhb, air__lmep)
                with hozqz__sashc:
                    vbs__qizqp = cgutils.alloca_once(c.builder, c.context.
                        get_value_type(types.pyobject))
                    with c.builder.if_else(c.builder.and_(is_null, ssgpf__gwbx)
                        ) as (rwqw__jgdvk, jwx__mavqe):
                        with rwqw__jgdvk:
                            ytjfj__xmbw = get_df_obj_column_codegen(c.
                                context, c.builder, c.pyapi, table.parent,
                                qry__lhb, t)
                            c.builder.store(ytjfj__xmbw, vbs__qizqp)
                        with jwx__mavqe:
                            c.context.nrt.incref(c.builder, t, arr)
                            c.builder.store(c.pyapi.from_native_value(t,
                                arr, c.env_manager), vbs__qizqp)
                    c.pyapi.list_setitem(idl__zkfx, qry__lhb, c.builder.
                        load(vbs__qizqp))
    mwn__skjwg = c.pyapi.unserialize(c.pyapi.serialize_object(Table))
    uws__xfj = c.pyapi.call_function_objargs(mwn__skjwg, (idl__zkfx,))
    c.pyapi.decref(mwn__skjwg)
    c.pyapi.decref(idl__zkfx)
    c.context.nrt.decref(c.builder, typ, val)
    return uws__xfj


@lower_builtin(len, TableType)
def table_len_lower(context, builder, sig, args):
    impl = table_len_overload(*sig.args)
    return context.compile_internal(builder, impl, sig, args)


def table_len_overload(T):
    if not isinstance(T, TableType):
        return

    def impl(T):
        return T._len
    return impl


@lower_getattr(TableType, 'shape')
def lower_table_shape(context, builder, typ, val):
    impl = table_shape_overload(typ)
    return context.compile_internal(builder, impl, types.Tuple([types.int64,
        types.int64])(typ), (val,))


def table_shape_overload(T):
    if T.has_runtime_cols:

        def impl(T):
            return T._len, compute_num_runtime_columns(T)
        return impl
    ncols = len(T.arr_types)
    return lambda T: (T._len, types.int64(ncols))


@intrinsic
def compute_num_runtime_columns(typingctx, table_type):
    assert isinstance(table_type, TableType)

    def codegen(context, builder, sig, args):
        table_arg, = args
        table = cgutils.create_struct_proxy(table_type)(context, builder,
            table_arg)
        pjnwq__zjy = context.get_constant(types.int64, 0)
        for i, t in enumerate(table_type.arr_types):
            lah__mwx = getattr(table, f'block_{i}')
            phh__wmux = ListInstance(context, builder, types.List(t), lah__mwx)
            pjnwq__zjy = builder.add(pjnwq__zjy, phh__wmux.size)
        return pjnwq__zjy
    sig = types.int64(table_type)
    return sig, codegen


def get_table_data_codegen(context, builder, table_arg, col_ind, table_type):
    arr_type = table_type.arr_types[col_ind]
    table = cgutils.create_struct_proxy(table_type)(context, builder, table_arg
        )
    nfr__qnths = table_type.block_nums[col_ind]
    jxt__egjj = table_type.block_offsets[col_ind]
    lah__mwx = getattr(table, f'block_{nfr__qnths}')
    phd__jwf = types.none(table_type, types.List(arr_type), types.int64,
        types.int64)
    qxkez__oau = context.get_constant(types.int64, col_ind)
    sal__jxg = context.get_constant(types.int64, jxt__egjj)
    rcz__xlltt = table_arg, lah__mwx, sal__jxg, qxkez__oau
    ensure_column_unboxed_codegen(context, builder, phd__jwf, rcz__xlltt)
    phh__wmux = ListInstance(context, builder, types.List(arr_type), lah__mwx)
    arr = phh__wmux.getitem(jxt__egjj)
    return arr


@intrinsic
def get_table_data(typingctx, table_type, ind_typ):
    assert isinstance(table_type, TableType)
    assert is_overload_constant_int(ind_typ)
    col_ind = get_overload_const_int(ind_typ)
    arr_type = table_type.arr_types[col_ind]

    def codegen(context, builder, sig, args):
        table_arg, mbheb__cpypu = args
        arr = get_table_data_codegen(context, builder, table_arg, col_ind,
            table_type)
        return impl_ret_borrowed(context, builder, arr_type, arr)
    sig = arr_type(table_type, ind_typ)
    return sig, codegen


@intrinsic
def del_column(typingctx, table_type, ind_typ):
    assert isinstance(table_type, TableType
        ), 'Can only delete columns from a table'
    assert isinstance(ind_typ, types.TypeRef) and isinstance(ind_typ.
        instance_type, MetaType), 'ind_typ must be a typeref for a meta type'
    qvbm__fdz = list(ind_typ.instance_type.meta)
    xwoc__oasf = defaultdict(list)
    for ind in qvbm__fdz:
        xwoc__oasf[table_type.block_nums[ind]].append(table_type.
            block_offsets[ind])

    def codegen(context, builder, sig, args):
        table_arg, mbheb__cpypu = args
        table = cgutils.create_struct_proxy(table_type)(context, builder,
            table_arg)
        for nfr__qnths, lgylz__eewa in xwoc__oasf.items():
            arr_type = table_type.blk_to_type[nfr__qnths]
            lah__mwx = getattr(table, f'block_{nfr__qnths}')
            phh__wmux = ListInstance(context, builder, types.List(arr_type),
                lah__mwx)
            cvknw__qegr = context.get_constant_null(arr_type)
            if len(lgylz__eewa) == 1:
                jxt__egjj = lgylz__eewa[0]
                arr = phh__wmux.getitem(jxt__egjj)
                context.nrt.decref(builder, arr_type, arr)
                phh__wmux.inititem(jxt__egjj, cvknw__qegr, incref=False)
            else:
                jhsmx__hii = context.get_constant(types.int64, len(lgylz__eewa)
                    )
                mlo__hhpfv = context.make_constant_array(builder, types.
                    Array(types.int64, 1, 'C'), np.array(lgylz__eewa, dtype
                    =np.int64))
                att__xke = context.make_array(types.Array(types.int64, 1, 'C')
                    )(context, builder, mlo__hhpfv)
                with cgutils.for_range(builder, jhsmx__hii) as cafsd__acft:
                    i = cafsd__acft.index
                    jxt__egjj = _getitem_array_single_int(context, builder,
                        types.int64, types.Array(types.int64, 1, 'C'),
                        att__xke, i)
                    arr = phh__wmux.getitem(jxt__egjj)
                    context.nrt.decref(builder, arr_type, arr)
                    phh__wmux.inititem(jxt__egjj, cvknw__qegr, incref=False)
    sig = types.void(table_type, ind_typ)
    return sig, codegen


def set_table_data_codegen(context, builder, in_table_type, in_table,
    out_table_type, arr_type, arr_arg, col_ind, is_new_col):
    in_table = cgutils.create_struct_proxy(in_table_type)(context, builder,
        in_table)
    out_table = cgutils.create_struct_proxy(out_table_type)(context, builder)
    out_table.len = in_table.len
    out_table.parent = in_table.parent
    rrtx__tait = context.get_constant(types.int64, 0)
    mucb__fzwg = context.get_constant(types.int64, 1)
    kqthr__efgz = arr_type not in in_table_type.type_to_blk
    for t, nfr__qnths in out_table_type.type_to_blk.items():
        if t in in_table_type.type_to_blk:
            qhpim__aef = in_table_type.type_to_blk[t]
            rycjc__ebko = ListInstance(context, builder, types.List(t),
                getattr(in_table, f'block_{qhpim__aef}'))
            context.nrt.incref(builder, types.List(t), rycjc__ebko.value)
            setattr(out_table, f'block_{nfr__qnths}', rycjc__ebko.value)
    if kqthr__efgz:
        mbheb__cpypu, rycjc__ebko = ListInstance.allocate_ex(context,
            builder, types.List(arr_type), mucb__fzwg)
        rycjc__ebko.size = mucb__fzwg
        rycjc__ebko.inititem(rrtx__tait, arr_arg, incref=True)
        nfr__qnths = out_table_type.type_to_blk[arr_type]
        setattr(out_table, f'block_{nfr__qnths}', rycjc__ebko.value)
        if not is_new_col:
            _rm_old_array(col_ind, out_table_type, out_table, in_table_type,
                context, builder)
    else:
        nfr__qnths = out_table_type.type_to_blk[arr_type]
        rycjc__ebko = ListInstance(context, builder, types.List(arr_type),
            getattr(out_table, f'block_{nfr__qnths}'))
        if is_new_col:
            n = rycjc__ebko.size
            ciwcy__twsgu = builder.add(n, mucb__fzwg)
            rycjc__ebko.resize(ciwcy__twsgu)
            rycjc__ebko.inititem(n, arr_arg, incref=True)
        elif arr_type == in_table_type.arr_types[col_ind]:
            biji__xid = context.get_constant(types.int64, out_table_type.
                block_offsets[col_ind])
            rycjc__ebko.setitem(biji__xid, arr_arg, incref=True)
        else:
            _rm_old_array(col_ind, out_table_type, out_table, in_table_type,
                context, builder)
            biji__xid = context.get_constant(types.int64, out_table_type.
                block_offsets[col_ind])
            n = rycjc__ebko.size
            ciwcy__twsgu = builder.add(n, mucb__fzwg)
            rycjc__ebko.resize(ciwcy__twsgu)
            context.nrt.incref(builder, arr_type, rycjc__ebko.getitem(
                biji__xid))
            rycjc__ebko.move(builder.add(biji__xid, mucb__fzwg), biji__xid,
                builder.sub(n, biji__xid))
            rycjc__ebko.setitem(biji__xid, arr_arg, incref=True)
    return out_table._getvalue()


def _rm_old_array(col_ind, out_table_type, out_table, in_table_type,
    context, builder):
    pdi__slon = in_table_type.arr_types[col_ind]
    if pdi__slon in out_table_type.type_to_blk:
        nfr__qnths = out_table_type.type_to_blk[pdi__slon]
        tzu__pwj = getattr(out_table, f'block_{nfr__qnths}')
        csmjd__egnts = types.List(pdi__slon)
        biji__xid = context.get_constant(types.int64, in_table_type.
            block_offsets[col_ind])
        xtcd__eouw = csmjd__egnts.dtype(csmjd__egnts, types.intp)
        yfqoc__zac = context.compile_internal(builder, lambda lst, i: lst.
            pop(i), xtcd__eouw, (tzu__pwj, biji__xid))
        context.nrt.decref(builder, pdi__slon, yfqoc__zac)


def generate_set_table_data_code(table, ind, arr_type, used_cols, is_null=False
    ):
    cro__yxe = list(table.arr_types)
    if ind == len(cro__yxe):
        jtrh__zmre = None
        cro__yxe.append(arr_type)
    else:
        jtrh__zmre = table.arr_types[ind]
        cro__yxe[ind] = arr_type
    qzv__gzn = TableType(tuple(cro__yxe))
    glbls = {'init_table': init_table, 'get_table_block': get_table_block,
        'set_table_block': set_table_block, 'set_table_len': set_table_len,
        'set_table_parent': set_table_parent, 'alloc_list_like':
        alloc_list_like, 'out_table_typ': qzv__gzn}
    jto__qkm = 'def set_table_data(table, ind, arr, used_cols=None):\n'
    jto__qkm += f'  T2 = init_table(out_table_typ, False)\n'
    jto__qkm += f'  T2 = set_table_len(T2, len(table))\n'
    jto__qkm += f'  T2 = set_table_parent(T2, table)\n'
    for typ, nfr__qnths in qzv__gzn.type_to_blk.items():
        if typ in table.type_to_blk:
            yqqjz__pvy = table.type_to_blk[typ]
            jto__qkm += (
                f'  arr_list_{nfr__qnths} = get_table_block(table, {yqqjz__pvy})\n'
                )
            jto__qkm += f"""  out_arr_list_{nfr__qnths} = alloc_list_like(arr_list_{nfr__qnths}, {len(qzv__gzn.block_to_arr_ind[nfr__qnths])}, False)
"""
            if used_cols is None or set(table.block_to_arr_ind[yqqjz__pvy]
                ) & used_cols:
                jto__qkm += f'  for i in range(len(arr_list_{nfr__qnths})):\n'
                if typ not in (jtrh__zmre, arr_type):
                    jto__qkm += (
                        f'    out_arr_list_{nfr__qnths}[i] = arr_list_{nfr__qnths}[i]\n'
                        )
                else:
                    hpwc__utsr = table.block_to_arr_ind[yqqjz__pvy]
                    tpl__hxiup = np.empty(len(hpwc__utsr), np.int64)
                    rym__goox = False
                    for mxea__grgw, qry__lhb in enumerate(hpwc__utsr):
                        if qry__lhb != ind:
                            yberl__lonji = qzv__gzn.block_offsets[qry__lhb]
                        else:
                            yberl__lonji = -1
                            rym__goox = True
                        tpl__hxiup[mxea__grgw] = yberl__lonji
                    glbls[f'out_idxs_{nfr__qnths}'] = np.array(tpl__hxiup,
                        np.int64)
                    jto__qkm += f'    out_idx = out_idxs_{nfr__qnths}[i]\n'
                    if rym__goox:
                        jto__qkm += f'    if out_idx == -1:\n'
                        jto__qkm += f'      continue\n'
                    jto__qkm += f"""    out_arr_list_{nfr__qnths}[out_idx] = arr_list_{nfr__qnths}[i]
"""
            if typ == arr_type and not is_null:
                jto__qkm += (
                    f'  out_arr_list_{nfr__qnths}[{qzv__gzn.block_offsets[ind]}] = arr\n'
                    )
        else:
            glbls[f'arr_list_typ_{nfr__qnths}'] = types.List(arr_type)
            jto__qkm += f"""  out_arr_list_{nfr__qnths} = alloc_list_like(arr_list_typ_{nfr__qnths}, 1, False)
"""
            if not is_null:
                jto__qkm += f'  out_arr_list_{nfr__qnths}[0] = arr\n'
        jto__qkm += (
            f'  T2 = set_table_block(T2, out_arr_list_{nfr__qnths}, {nfr__qnths})\n'
            )
    jto__qkm += f'  return T2\n'
    ljmbp__epvr = {}
    exec(jto__qkm, glbls, ljmbp__epvr)
    return ljmbp__epvr['set_table_data']


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def set_table_data(table, ind, arr, used_cols=None):
    if is_overload_none(used_cols):
        stl__fiv = None
    else:
        stl__fiv = set(used_cols.instance_type.meta)
    utx__zlum = get_overload_const_int(ind)
    return generate_set_table_data_code(table, utx__zlum, arr, stl__fiv)


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def set_table_data_null(table, ind, arr, used_cols=None):
    utx__zlum = get_overload_const_int(ind)
    arr_type = arr.instance_type
    if is_overload_none(used_cols):
        stl__fiv = None
    else:
        stl__fiv = set(used_cols.instance_type.meta)
    return generate_set_table_data_code(table, utx__zlum, arr_type,
        stl__fiv, is_null=True)


def alias_ext_dummy_func(lhs_name, args, alias_map, arg_aliases):
    assert len(args) >= 1
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)


numba.core.ir_utils.alias_func_extensions['get_table_data',
    'bodo.hiframes.table'] = alias_ext_dummy_func


def get_table_data_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 2 and not kws
    dno__bwff = args[0]
    if equiv_set.has_shape(dno__bwff):
        return ArrayAnalysis.AnalyzeResult(shape=equiv_set.get_shape(
            dno__bwff)[0], pre=[])


ArrayAnalysis._analyze_op_call_bodo_hiframes_table_get_table_data = (
    get_table_data_equiv)


@lower_constant(TableType)
def lower_constant_table(context, builder, table_type, pyval):
    tiwwp__ajy = []
    for t, nfr__qnths in table_type.type_to_blk.items():
        xgkf__pjpo = len(table_type.block_to_arr_ind[nfr__qnths])
        dac__szxsi = []
        for i in range(xgkf__pjpo):
            qry__lhb = table_type.block_to_arr_ind[nfr__qnths][i]
            dac__szxsi.append(pyval.arrays[qry__lhb])
        tiwwp__ajy.append(context.get_constant_generic(builder, types.List(
            t), dac__szxsi))
    bgij__sdoo = context.get_constant_null(types.pyobject)
    njc__ldum = context.get_constant(types.int64, 0 if len(pyval.arrays) ==
        0 else len(pyval.arrays[0]))
    return lir.Constant.literal_struct(tiwwp__ajy + [bgij__sdoo, njc__ldum])


def get_init_table_output_type(table_type, to_str_if_dict_t):
    out_table_type = table_type.instance_type if isinstance(table_type,
        types.TypeRef) else table_type
    assert isinstance(out_table_type, TableType
        ), 'table type or typeref expected'
    assert is_overload_constant_bool(to_str_if_dict_t
        ), 'constant to_str_if_dict_t expected'
    if is_overload_true(to_str_if_dict_t):
        out_table_type = to_str_arr_if_dict_array(out_table_type)
    return out_table_type


@intrinsic
def init_table(typingctx, table_type, to_str_if_dict_t):
    out_table_type = get_init_table_output_type(table_type, to_str_if_dict_t)

    def codegen(context, builder, sig, args):
        table = cgutils.create_struct_proxy(out_table_type)(context, builder)
        for t, nfr__qnths in out_table_type.type_to_blk.items():
            ulat__nxu = context.get_constant_null(types.List(t))
            setattr(table, f'block_{nfr__qnths}', ulat__nxu)
        return table._getvalue()
    sig = out_table_type(table_type, to_str_if_dict_t)
    return sig, codegen


@intrinsic
def init_table_from_lists(typingctx, tuple_of_lists_type, table_type):
    assert isinstance(tuple_of_lists_type, types.BaseTuple
        ), 'Tuple of data expected'
    sksqj__fsc = {}
    for i, typ in enumerate(tuple_of_lists_type):
        assert isinstance(typ, types.List), 'Each tuple element must be a list'
        sksqj__fsc[typ.dtype] = i
    fut__wklz = table_type.instance_type if isinstance(table_type, types.
        TypeRef) else table_type
    assert isinstance(fut__wklz, TableType), 'table type expected'

    def codegen(context, builder, sig, args):
        wmezj__zapl, mbheb__cpypu = args
        table = cgutils.create_struct_proxy(fut__wklz)(context, builder)
        for t, nfr__qnths in fut__wklz.type_to_blk.items():
            idx = sksqj__fsc[t]
            kvy__khln = signature(types.List(t), tuple_of_lists_type, types
                .literal(idx))
            ablk__gqu = wmezj__zapl, idx
            qwe__ehhi = numba.cpython.tupleobj.static_getitem_tuple(context,
                builder, kvy__khln, ablk__gqu)
            setattr(table, f'block_{nfr__qnths}', qwe__ehhi)
        return table._getvalue()
    sig = fut__wklz(tuple_of_lists_type, table_type)
    return sig, codegen


@intrinsic
def get_table_block(typingctx, table_type, blk_type):
    assert isinstance(table_type, TableType), 'table type expected'
    assert is_overload_constant_int(blk_type)
    nfr__qnths = get_overload_const_int(blk_type)
    arr_type = None
    for t, jooe__yiqla in table_type.type_to_blk.items():
        if jooe__yiqla == nfr__qnths:
            arr_type = t
            break
    assert arr_type is not None, 'invalid table type block'
    jthp__rbdap = types.List(arr_type)

    def codegen(context, builder, sig, args):
        table = cgutils.create_struct_proxy(table_type)(context, builder,
            args[0])
        lah__mwx = getattr(table, f'block_{nfr__qnths}')
        return impl_ret_borrowed(context, builder, jthp__rbdap, lah__mwx)
    sig = jthp__rbdap(table_type, blk_type)
    return sig, codegen


@intrinsic
def ensure_table_unboxed(typingctx, table_type, used_cols_typ):

    def codegen(context, builder, sig, args):
        table_arg, dodz__ogrbi = args
        eikz__mpqoh = context.get_python_api(builder)
        dvvs__fdj = used_cols_typ == types.none
        if not dvvs__fdj:
            ejmsl__wvta = numba.cpython.setobj.SetInstance(context, builder,
                types.Set(types.int64), dodz__ogrbi)
        table = cgutils.create_struct_proxy(sig.args[0])(context, builder,
            table_arg)
        for t, nfr__qnths in table_type.type_to_blk.items():
            jhsmx__hii = context.get_constant(types.int64, len(table_type.
                block_to_arr_ind[nfr__qnths]))
            eredo__jug = context.make_constant_array(builder, types.Array(
                types.int64, 1, 'C'), np.array(table_type.block_to_arr_ind[
                nfr__qnths], dtype=np.int64))
            sir__jnzan = context.make_array(types.Array(types.int64, 1, 'C'))(
                context, builder, eredo__jug)
            lah__mwx = getattr(table, f'block_{nfr__qnths}')
            with cgutils.for_range(builder, jhsmx__hii) as cafsd__acft:
                i = cafsd__acft.index
                qry__lhb = _getitem_array_single_int(context, builder,
                    types.int64, types.Array(types.int64, 1, 'C'),
                    sir__jnzan, i)
                phd__jwf = types.none(table_type, types.List(t), types.
                    int64, types.int64)
                rcz__xlltt = table_arg, lah__mwx, i, qry__lhb
                if dvvs__fdj:
                    ensure_column_unboxed_codegen(context, builder,
                        phd__jwf, rcz__xlltt)
                else:
                    jfiuv__yui = ejmsl__wvta.contains(qry__lhb)
                    with builder.if_then(jfiuv__yui):
                        ensure_column_unboxed_codegen(context, builder,
                            phd__jwf, rcz__xlltt)
    assert isinstance(table_type, TableType), 'table type expected'
    sig = types.none(table_type, used_cols_typ)
    return sig, codegen


@intrinsic
def ensure_column_unboxed(typingctx, table_type, arr_list_t, ind_t, arr_ind_t):
    assert isinstance(table_type, TableType), 'table type expected'
    sig = types.none(table_type, arr_list_t, ind_t, arr_ind_t)
    return sig, ensure_column_unboxed_codegen


def ensure_column_unboxed_codegen(context, builder, sig, args):
    from bodo.hiframes.boxing import get_df_obj_column_codegen
    table_arg, wtnq__lrl, ayf__ptd, iduw__wfgc = args
    eikz__mpqoh = context.get_python_api(builder)
    table = cgutils.create_struct_proxy(sig.args[0])(context, builder,
        table_arg)
    ssgpf__gwbx = cgutils.is_not_null(builder, table.parent)
    phh__wmux = ListInstance(context, builder, sig.args[1], wtnq__lrl)
    bxb__fda = phh__wmux.getitem(ayf__ptd)
    oaz__lboif = cgutils.alloca_once_value(builder, bxb__fda)
    hbx__pgygw = cgutils.alloca_once_value(builder, context.
        get_constant_null(sig.args[1].dtype))
    is_null = is_ll_eq(builder, oaz__lboif, hbx__pgygw)
    with builder.if_then(is_null):
        with builder.if_else(ssgpf__gwbx) as (vonr__embt, hozqz__sashc):
            with vonr__embt:
                vbs__qizqp = get_df_obj_column_codegen(context, builder,
                    eikz__mpqoh, table.parent, iduw__wfgc, sig.args[1].dtype)
                arr = eikz__mpqoh.to_native_value(sig.args[1].dtype, vbs__qizqp
                    ).value
                phh__wmux.inititem(ayf__ptd, arr, incref=False)
                eikz__mpqoh.decref(vbs__qizqp)
            with hozqz__sashc:
                context.call_conv.return_user_exc(builder, BodoError, (
                    'unexpected null table column',))


@intrinsic
def set_table_block(typingctx, table_type, arr_list_type, blk_type):
    assert isinstance(table_type, TableType), 'table type expected'
    assert isinstance(arr_list_type, types.List), 'list type expected'
    assert is_overload_constant_int(blk_type), 'blk should be const int'
    nfr__qnths = get_overload_const_int(blk_type)

    def codegen(context, builder, sig, args):
        table_arg, bltfc__doscp, mbheb__cpypu = args
        in_table = cgutils.create_struct_proxy(table_type)(context, builder,
            table_arg)
        setattr(in_table, f'block_{nfr__qnths}', bltfc__doscp)
        return impl_ret_borrowed(context, builder, table_type, in_table.
            _getvalue())
    sig = table_type(table_type, arr_list_type, blk_type)
    return sig, codegen


@intrinsic
def set_table_len(typingctx, table_type, l_type):
    assert isinstance(table_type, TableType), 'table type expected'

    def codegen(context, builder, sig, args):
        table_arg, ymrgf__ucq = args
        in_table = cgutils.create_struct_proxy(table_type)(context, builder,
            table_arg)
        in_table.len = ymrgf__ucq
        return impl_ret_borrowed(context, builder, table_type, in_table.
            _getvalue())
    sig = table_type(table_type, l_type)
    return sig, codegen


@intrinsic
def set_table_parent(typingctx, out_table_type, in_table_type):
    assert isinstance(in_table_type, TableType), 'table type expected'
    assert isinstance(out_table_type, TableType), 'table type expected'

    def codegen(context, builder, sig, args):
        rtew__fuqbh, mwj__kxt = args
        in_table = cgutils.create_struct_proxy(in_table_type)(context,
            builder, mwj__kxt)
        out_table = cgutils.create_struct_proxy(out_table_type)(context,
            builder, rtew__fuqbh)
        out_table.parent = in_table.parent
        context.nrt.incref(builder, types.pyobject, out_table.parent)
        return impl_ret_borrowed(context, builder, out_table_type,
            out_table._getvalue())
    sig = out_table_type(out_table_type, in_table_type)
    return sig, codegen


@intrinsic
def alloc_list_like(typingctx, list_type, len_type, to_str_if_dict_t):
    jthp__rbdap = list_type.instance_type if isinstance(list_type, types.
        TypeRef) else list_type
    assert isinstance(jthp__rbdap, types.List), 'list type or typeref expected'
    assert isinstance(len_type, types.Integer), 'integer type expected'
    assert is_overload_constant_bool(to_str_if_dict_t
        ), 'constant to_str_if_dict_t expected'
    if is_overload_true(to_str_if_dict_t):
        jthp__rbdap = types.List(to_str_arr_if_dict_array(jthp__rbdap.dtype))

    def codegen(context, builder, sig, args):
        sfcpg__fcd = args[1]
        mbheb__cpypu, rycjc__ebko = ListInstance.allocate_ex(context,
            builder, jthp__rbdap, sfcpg__fcd)
        rycjc__ebko.size = sfcpg__fcd
        return rycjc__ebko.value
    sig = jthp__rbdap(list_type, len_type, to_str_if_dict_t)
    return sig, codegen


@intrinsic
def alloc_empty_list_type(typingctx, size_typ, data_typ):
    assert isinstance(size_typ, types.Integer), 'Size must be an integer'
    pmdzt__anfb = data_typ.instance_type if isinstance(data_typ, types.TypeRef
        ) else data_typ
    list_type = types.List(pmdzt__anfb)

    def codegen(context, builder, sig, args):
        sfcpg__fcd, mbheb__cpypu = args
        mbheb__cpypu, rycjc__ebko = ListInstance.allocate_ex(context,
            builder, list_type, sfcpg__fcd)
        rycjc__ebko.size = sfcpg__fcd
        return rycjc__ebko.value
    sig = list_type(size_typ, data_typ)
    return sig, codegen


def _get_idx_length(idx):
    pass


@overload(_get_idx_length)
def overload_get_idx_length(idx, n):
    if is_list_like_index_type(idx) and idx.dtype == types.bool_:
        return lambda idx, n: idx.sum()
    assert isinstance(idx, types.SliceType), 'slice index expected'

    def impl(idx, n):
        avv__rslh = numba.cpython.unicode._normalize_slice(idx, n)
        return numba.cpython.unicode._slice_span(avv__rslh)
    return impl


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def table_filter(T, idx, used_cols=None):
    from bodo.utils.conversion import ensure_contig_if_np
    glbls = {'init_table': init_table, 'get_table_block': get_table_block,
        'ensure_column_unboxed': ensure_column_unboxed, 'set_table_block':
        set_table_block, 'set_table_len': set_table_len, 'alloc_list_like':
        alloc_list_like, '_get_idx_length': _get_idx_length,
        'ensure_contig_if_np': ensure_contig_if_np}
    if not is_overload_none(used_cols):
        fsawh__djx = used_cols.instance_type
        obi__nhpn = np.array(fsawh__djx.meta, dtype=np.int64)
        glbls['used_cols_vals'] = obi__nhpn
        gub__jvae = set([T.block_nums[i] for i in obi__nhpn])
    else:
        obi__nhpn = None
    jto__qkm = 'def table_filter_func(T, idx, used_cols=None):\n'
    jto__qkm += f'  T2 = init_table(T, False)\n'
    jto__qkm += f'  l = 0\n'
    if obi__nhpn is not None and len(obi__nhpn) == 0:
        jto__qkm += f'  l = _get_idx_length(idx, len(T))\n'
        jto__qkm += f'  T2 = set_table_len(T2, l)\n'
        jto__qkm += f'  return T2\n'
        ljmbp__epvr = {}
        exec(jto__qkm, glbls, ljmbp__epvr)
        return ljmbp__epvr['table_filter_func']
    if obi__nhpn is not None:
        jto__qkm += f'  used_set = set(used_cols_vals)\n'
    for nfr__qnths in T.type_to_blk.values():
        jto__qkm += (
            f'  arr_list_{nfr__qnths} = get_table_block(T, {nfr__qnths})\n')
        jto__qkm += f"""  out_arr_list_{nfr__qnths} = alloc_list_like(arr_list_{nfr__qnths}, len(arr_list_{nfr__qnths}), False)
"""
        if obi__nhpn is None or nfr__qnths in gub__jvae:
            glbls[f'arr_inds_{nfr__qnths}'] = np.array(T.block_to_arr_ind[
                nfr__qnths], dtype=np.int64)
            jto__qkm += f'  for i in range(len(arr_list_{nfr__qnths})):\n'
            jto__qkm += (
                f'    arr_ind_{nfr__qnths} = arr_inds_{nfr__qnths}[i]\n')
            if obi__nhpn is not None:
                jto__qkm += (
                    f'    if arr_ind_{nfr__qnths} not in used_set: continue\n')
            jto__qkm += f"""    ensure_column_unboxed(T, arr_list_{nfr__qnths}, i, arr_ind_{nfr__qnths})
"""
            jto__qkm += f"""    out_arr_{nfr__qnths} = ensure_contig_if_np(arr_list_{nfr__qnths}[i][idx])
"""
            jto__qkm += f'    l = len(out_arr_{nfr__qnths})\n'
            jto__qkm += (
                f'    out_arr_list_{nfr__qnths}[i] = out_arr_{nfr__qnths}\n')
        jto__qkm += (
            f'  T2 = set_table_block(T2, out_arr_list_{nfr__qnths}, {nfr__qnths})\n'
            )
    jto__qkm += f'  T2 = set_table_len(T2, l)\n'
    jto__qkm += f'  return T2\n'
    ljmbp__epvr = {}
    exec(jto__qkm, glbls, ljmbp__epvr)
    return ljmbp__epvr['table_filter_func']


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def table_subset(T, idx, copy_arrs, used_cols=None):
    xjyvj__ztvx = list(idx.instance_type.meta)
    cro__yxe = tuple(np.array(T.arr_types, dtype=object)[xjyvj__ztvx])
    qzv__gzn = TableType(cro__yxe)
    if not is_overload_constant_bool(copy_arrs):
        raise_bodo_error('table_subset(): copy_arrs must be a constant')
    fdv__swcf = is_overload_true(copy_arrs)
    glbls = {'init_table': init_table, 'get_table_block': get_table_block,
        'ensure_column_unboxed': ensure_column_unboxed, 'set_table_block':
        set_table_block, 'set_table_len': set_table_len, 'alloc_list_like':
        alloc_list_like, 'out_table_typ': qzv__gzn}
    if not is_overload_none(used_cols):
        kept_cols = used_cols.instance_type.meta
        yfpa__dei = set(kept_cols)
        glbls['kept_cols'] = np.array(kept_cols, np.int64)
        vdeei__jfpl = True
    else:
        vdeei__jfpl = False
    nlom__xkg = {i: c for i, c in enumerate(xjyvj__ztvx)}
    jto__qkm = 'def table_subset(T, idx, copy_arrs, used_cols=None):\n'
    jto__qkm += f'  T2 = init_table(out_table_typ, False)\n'
    jto__qkm += f'  T2 = set_table_len(T2, len(T))\n'
    if vdeei__jfpl and len(yfpa__dei) == 0:
        jto__qkm += f'  return T2\n'
        ljmbp__epvr = {}
        exec(jto__qkm, glbls, ljmbp__epvr)
        return ljmbp__epvr['table_subset']
    if vdeei__jfpl:
        jto__qkm += f'  kept_cols_set = set(kept_cols)\n'
    for typ, nfr__qnths in qzv__gzn.type_to_blk.items():
        yqqjz__pvy = T.type_to_blk[typ]
        jto__qkm += (
            f'  arr_list_{nfr__qnths} = get_table_block(T, {yqqjz__pvy})\n')
        jto__qkm += f"""  out_arr_list_{nfr__qnths} = alloc_list_like(arr_list_{nfr__qnths}, {len(qzv__gzn.block_to_arr_ind[nfr__qnths])}, False)
"""
        nuoi__acgea = True
        if vdeei__jfpl:
            xvhcp__xjl = set(qzv__gzn.block_to_arr_ind[nfr__qnths])
            qvf__bkm = xvhcp__xjl & yfpa__dei
            nuoi__acgea = len(qvf__bkm) > 0
        if nuoi__acgea:
            glbls[f'out_arr_inds_{nfr__qnths}'] = np.array(qzv__gzn.
                block_to_arr_ind[nfr__qnths], dtype=np.int64)
            jto__qkm += f'  for i in range(len(out_arr_list_{nfr__qnths})):\n'
            jto__qkm += (
                f'    out_arr_ind_{nfr__qnths} = out_arr_inds_{nfr__qnths}[i]\n'
                )
            if vdeei__jfpl:
                jto__qkm += (
                    f'    if out_arr_ind_{nfr__qnths} not in kept_cols_set: continue\n'
                    )
            ncdpm__gxf = []
            hbw__vhh = []
            for xdo__fel in qzv__gzn.block_to_arr_ind[nfr__qnths]:
                ihvco__zeqwn = nlom__xkg[xdo__fel]
                ncdpm__gxf.append(ihvco__zeqwn)
                fwsis__stem = T.block_offsets[ihvco__zeqwn]
                hbw__vhh.append(fwsis__stem)
            glbls[f'in_logical_idx_{nfr__qnths}'] = np.array(ncdpm__gxf,
                dtype=np.int64)
            glbls[f'in_physical_idx_{nfr__qnths}'] = np.array(hbw__vhh,
                dtype=np.int64)
            jto__qkm += (
                f'    logical_idx_{nfr__qnths} = in_logical_idx_{nfr__qnths}[i]\n'
                )
            jto__qkm += (
                f'    physical_idx_{nfr__qnths} = in_physical_idx_{nfr__qnths}[i]\n'
                )
            jto__qkm += f"""    ensure_column_unboxed(T, arr_list_{nfr__qnths}, physical_idx_{nfr__qnths}, logical_idx_{nfr__qnths})
"""
            lkiss__qkq = '.copy()' if fdv__swcf else ''
            jto__qkm += f"""    out_arr_list_{nfr__qnths}[i] = arr_list_{nfr__qnths}[physical_idx_{nfr__qnths}]{lkiss__qkq}
"""
        jto__qkm += (
            f'  T2 = set_table_block(T2, out_arr_list_{nfr__qnths}, {nfr__qnths})\n'
            )
    jto__qkm += f'  return T2\n'
    ljmbp__epvr = {}
    exec(jto__qkm, glbls, ljmbp__epvr)
    return ljmbp__epvr['table_subset']


def table_filter_equiv(self, scope, equiv_set, loc, args, kws):
    dno__bwff = args[0]
    if equiv_set.has_shape(dno__bwff):
        if guard(is_whole_slice, self.typemap, self.func_ir, args[1]):
            return ArrayAnalysis.AnalyzeResult(shape=dno__bwff, pre=[])
        return ArrayAnalysis.AnalyzeResult(shape=(None, equiv_set.get_shape
            (dno__bwff)[1]), pre=[])
    return None


ArrayAnalysis._analyze_op_call_bodo_hiframes_table_table_filter = (
    table_filter_equiv)


def table_subset_equiv(self, scope, equiv_set, loc, args, kws):
    dno__bwff = args[0]
    if equiv_set.has_shape(dno__bwff):
        return ArrayAnalysis.AnalyzeResult(shape=(equiv_set.get_shape(
            dno__bwff)[0], None), pre=[])
    return None


ArrayAnalysis._analyze_op_call_bodo_hiframes_table_table_subset = (
    table_subset_equiv)


def gen_str_and_dict_enc_cols_to_one_block_fn_txt(in_table_type,
    out_table_type, glbls, is_gatherv=False):
    assert bodo.string_array_type in in_table_type.type_to_blk and bodo.string_array_type in in_table_type.type_to_blk, f'Error in gen_str_and_dict_enc_cols_to_one_block_fn_txt: Table type {in_table_type} does not contain both a string, and encoded string column'
    dbeg__mbwh = in_table_type.type_to_blk[bodo.string_array_type]
    wuavl__bhqqd = in_table_type.type_to_blk[bodo.dict_str_arr_type]
    xvhwc__pbtk = in_table_type.block_to_arr_ind.get(dbeg__mbwh)
    btr__yzmma = in_table_type.block_to_arr_ind.get(wuavl__bhqqd)
    qrm__zihk = []
    sksd__bgpy = []
    rwbqb__szs = 0
    lihdo__oelh = 0
    for roz__sstp in range(len(xvhwc__pbtk) + len(btr__yzmma)):
        if rwbqb__szs == len(xvhwc__pbtk):
            sksd__bgpy.append(roz__sstp)
            continue
        elif lihdo__oelh == len(btr__yzmma):
            qrm__zihk.append(roz__sstp)
            continue
        kxqss__yal = xvhwc__pbtk[rwbqb__szs]
        zccz__cifx = btr__yzmma[lihdo__oelh]
        if kxqss__yal < zccz__cifx:
            qrm__zihk.append(roz__sstp)
            rwbqb__szs += 1
        else:
            sksd__bgpy.append(roz__sstp)
            lihdo__oelh += 1
    assert 'output_table_str_arr_offsets_in_combined_block' not in glbls, "Error in gen_str_and_dict_enc_cols_to_one_block_fn_txt: key 'output_table_str_arr_idxs_in_combined_block' already present as a global variable"
    glbls['output_table_str_arr_offsets_in_combined_block'] = np.array(
        qrm__zihk)
    assert 'output_table_dict_enc_str_arr_offsets_in_combined_block' not in glbls, "Error in gen_str_and_dict_enc_cols_to_one_block_fn_txt: key 'output_table_str_arr_idxs_in_combined_block' already present as a global variable"
    glbls['output_table_dict_enc_str_arr_offsets_in_combined_block'
        ] = np.array(sksd__bgpy)
    glbls['decode_if_dict_array'] = decode_if_dict_array
    kvs__bmrmc = out_table_type.type_to_blk[bodo.string_array_type]
    assert f'arr_inds_{dbeg__mbwh}' not in glbls, f'Error in gen_str_and_dict_enc_cols_to_one_block_fn_txt: arr_inds_{dbeg__mbwh} already present in global variables'
    glbls[f'arr_inds_{dbeg__mbwh}'] = np.array(in_table_type.
        block_to_arr_ind[dbeg__mbwh], dtype=np.int64)
    assert f'arr_inds_{wuavl__bhqqd}' not in glbls, f'Error in gen_str_and_dict_enc_cols_to_one_block_fn_txt: arr_inds_{wuavl__bhqqd} already present in global variables'
    glbls[f'arr_inds_{wuavl__bhqqd}'] = np.array(in_table_type.
        block_to_arr_ind[wuavl__bhqqd], dtype=np.int64)
    jto__qkm = f'  input_str_arr_list = get_table_block(T, {dbeg__mbwh})\n'
    jto__qkm += (
        f'  input_dict_enc_str_arr_list = get_table_block(T, {wuavl__bhqqd})\n'
        )
    jto__qkm += f"""  out_arr_list_{kvs__bmrmc} = alloc_list_like(input_str_arr_list, {len(qrm__zihk) + len(sksd__bgpy)}, True)
"""
    jto__qkm += f"""  for input_str_ary_idx, output_str_arr_offset in enumerate(output_table_str_arr_offsets_in_combined_block):
"""
    jto__qkm += f'    arr_ind_str = arr_inds_{dbeg__mbwh}[input_str_ary_idx]\n'
    jto__qkm += f"""    ensure_column_unboxed(T, input_str_arr_list, input_str_ary_idx, arr_ind_str)
"""
    jto__qkm += f'    out_arr_str = input_str_arr_list[input_str_ary_idx]\n'
    if is_gatherv:
        jto__qkm += (
            f'    out_arr_str = bodo.gatherv(out_arr_str, allgather, warn_if_rep, root)\n'
            )
    jto__qkm += (
        f'    out_arr_list_{kvs__bmrmc}[output_str_arr_offset] = out_arr_str\n'
        )
    jto__qkm += f"""  for input_dict_enc_str_ary_idx, output_dict_enc_str_arr_offset in enumerate(output_table_dict_enc_str_arr_offsets_in_combined_block):
"""
    jto__qkm += (
        f'    arr_ind_dict_enc_str = arr_inds_{wuavl__bhqqd}[input_dict_enc_str_ary_idx]\n'
        )
    jto__qkm += f"""    ensure_column_unboxed(T, input_dict_enc_str_arr_list, input_dict_enc_str_ary_idx, arr_ind_dict_enc_str)
"""
    jto__qkm += f"""    out_arr_dict_enc_str = decode_if_dict_array(input_dict_enc_str_arr_list[input_dict_enc_str_ary_idx])
"""
    if is_gatherv:
        jto__qkm += f"""    out_arr_dict_enc_str = bodo.gatherv(out_arr_dict_enc_str, allgather, warn_if_rep, root)
"""
    jto__qkm += f"""    out_arr_list_{kvs__bmrmc}[output_dict_enc_str_arr_offset] = out_arr_dict_enc_str
"""
    jto__qkm += (
        f'  T2 = set_table_block(T2, out_arr_list_{kvs__bmrmc}, {kvs__bmrmc})\n'
        )
    return jto__qkm


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def decode_if_dict_table(T):
    jto__qkm = 'def impl(T):\n'
    jto__qkm += f'  T2 = init_table(T, True)\n'
    jto__qkm += f'  l = len(T)\n'
    glbls = {'init_table': init_table, 'get_table_block': get_table_block,
        'ensure_column_unboxed': ensure_column_unboxed, 'set_table_block':
        set_table_block, 'set_table_len': set_table_len, 'alloc_list_like':
        alloc_list_like, 'decode_if_dict_array': decode_if_dict_array}
    out_table_type = bodo.hiframes.table.get_init_table_output_type(T, True)
    vcgu__bqq = (bodo.string_array_type in T.type_to_blk and bodo.
        dict_str_arr_type in T.type_to_blk)
    if vcgu__bqq:
        jto__qkm += gen_str_and_dict_enc_cols_to_one_block_fn_txt(T,
            out_table_type, glbls)
    for typ, kzdgw__ehc in T.type_to_blk.items():
        if vcgu__bqq and typ in (bodo.string_array_type, bodo.dict_str_arr_type
            ):
            continue
        if typ == bodo.dict_str_arr_type:
            assert bodo.string_array_type in out_table_type.type_to_blk, 'Error in decode_if_dict_table: If encoded string type is present in the input, then non-encoded string type should be present in the output'
            vqt__rpj = out_table_type.type_to_blk[bodo.string_array_type]
        else:
            assert typ in out_table_type.type_to_blk, 'Error in decode_if_dict_table: All non-encoded string types present in the input should be present in the output'
            vqt__rpj = out_table_type.type_to_blk[typ]
        glbls[f'arr_inds_{kzdgw__ehc}'] = np.array(T.block_to_arr_ind[
            kzdgw__ehc], dtype=np.int64)
        jto__qkm += (
            f'  arr_list_{kzdgw__ehc} = get_table_block(T, {kzdgw__ehc})\n')
        jto__qkm += f"""  out_arr_list_{kzdgw__ehc} = alloc_list_like(arr_list_{kzdgw__ehc}, len(arr_list_{kzdgw__ehc}), True)
"""
        jto__qkm += f'  for i in range(len(arr_list_{kzdgw__ehc})):\n'
        jto__qkm += f'    arr_ind_{kzdgw__ehc} = arr_inds_{kzdgw__ehc}[i]\n'
        jto__qkm += f"""    ensure_column_unboxed(T, arr_list_{kzdgw__ehc}, i, arr_ind_{kzdgw__ehc})
"""
        jto__qkm += (
            f'    out_arr_{kzdgw__ehc} = decode_if_dict_array(arr_list_{kzdgw__ehc}[i])\n'
            )
        jto__qkm += (
            f'    out_arr_list_{kzdgw__ehc}[i] = out_arr_{kzdgw__ehc}\n')
        jto__qkm += (
            f'  T2 = set_table_block(T2, out_arr_list_{kzdgw__ehc}, {vqt__rpj})\n'
            )
    jto__qkm += f'  T2 = set_table_len(T2, l)\n'
    jto__qkm += f'  return T2\n'
    ljmbp__epvr = {}
    exec(jto__qkm, glbls, ljmbp__epvr)
    return ljmbp__epvr['impl']


@overload(operator.getitem, no_unliteral=True, inline='always')
def overload_table_getitem(T, idx):
    if not isinstance(T, TableType):
        return
    return lambda T, idx: table_filter(T, idx)


@intrinsic
def init_runtime_table_from_lists(typingctx, arr_list_tup_typ, nrows_typ=None):
    assert isinstance(arr_list_tup_typ, types.BaseTuple
        ), 'init_runtime_table_from_lists requires a tuple of list of arrays'
    if isinstance(arr_list_tup_typ, types.UniTuple):
        if arr_list_tup_typ.dtype.dtype == types.undefined:
            return
        rpdc__lsfm = [arr_list_tup_typ.dtype.dtype] * len(arr_list_tup_typ)
    else:
        rpdc__lsfm = []
        for typ in arr_list_tup_typ:
            if typ.dtype == types.undefined:
                return
            rpdc__lsfm.append(typ.dtype)
    assert isinstance(nrows_typ, types.Integer
        ), 'init_runtime_table_from_lists requires an integer length'

    def codegen(context, builder, sig, args):
        onp__nfkk, vxo__ljdd = args
        table = cgutils.create_struct_proxy(table_type)(context, builder)
        table.len = vxo__ljdd
        tiwwp__ajy = cgutils.unpack_tuple(builder, onp__nfkk)
        for i, lah__mwx in enumerate(tiwwp__ajy):
            setattr(table, f'block_{i}', lah__mwx)
            context.nrt.incref(builder, types.List(rpdc__lsfm[i]), lah__mwx)
        return table._getvalue()
    table_type = TableType(tuple(rpdc__lsfm), True)
    sig = table_type(arr_list_tup_typ, nrows_typ)
    return sig, codegen


def _to_arr_if_series(t):
    return t.data if isinstance(t, SeriesType) else t


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def logical_table_to_table(in_table_t, extra_arrs_t, in_col_inds_t,
    n_table_cols_t, out_table_type_t=None, used_cols=None):
    in_col_inds = in_col_inds_t.instance_type.meta
    assert isinstance(in_table_t, (TableType, types.BaseTuple, types.NoneType)
        ), 'logical_table_to_table: input table must be a TableType or tuple of arrays or None (for dead table)'
    glbls = {}
    if not is_overload_none(used_cols):
        kept_cols = set(used_cols.instance_type.meta)
        glbls['kept_cols'] = np.array(list(kept_cols), np.int64)
        vdeei__jfpl = True
    else:
        kept_cols = set(np.arange(len(in_col_inds)))
        vdeei__jfpl = False
    extra_arrs_no_series = ', '.join(f'get_series_data(extra_arrs_t[{i}])' if
        isinstance(extra_arrs_t[i], SeriesType) else f'extra_arrs_t[{i}]' for
        i in range(len(extra_arrs_t)))
    extra_arrs_no_series = (
        f"({extra_arrs_no_series}{',' if len(extra_arrs_t) == 1 else ''})")
    if isinstance(in_table_t, (types.BaseTuple, types.NoneType)):
        return _logical_tuple_table_to_table_codegen(in_table_t,
            extra_arrs_t, in_col_inds, kept_cols, n_table_cols_t,
            out_table_type_t, extra_arrs_no_series)
    rtp__yyffc = len(in_table_t.arr_types)
    out_table_type = TableType(tuple(in_table_t.arr_types[i] if i <
        rtp__yyffc else _to_arr_if_series(extra_arrs_t.types[i - rtp__yyffc
        ]) for i in in_col_inds)) if is_overload_none(out_table_type_t
        ) else unwrap_typeref(out_table_type_t)
    glbls.update({'init_table': init_table, 'set_table_len': set_table_len,
        'out_table_type': out_table_type})
    jto__qkm = """def impl(in_table_t, extra_arrs_t, in_col_inds_t, n_table_cols_t, out_table_type_t=None, used_cols=None):
"""
    if any(isinstance(t, SeriesType) for t in extra_arrs_t.types):
        jto__qkm += f'  extra_arrs_t = {extra_arrs_no_series}\n'
    jto__qkm += f'  T1 = in_table_t\n'
    jto__qkm += f'  T2 = init_table(out_table_type, False)\n'
    jto__qkm += f'  T2 = set_table_len(T2, len(T1))\n'
    if vdeei__jfpl and len(kept_cols) == 0:
        jto__qkm += f'  return T2\n'
        ljmbp__epvr = {}
        exec(jto__qkm, glbls, ljmbp__epvr)
        return ljmbp__epvr['impl']
    if vdeei__jfpl:
        jto__qkm += f'  kept_cols_set = set(kept_cols)\n'
    for typ, nfr__qnths in out_table_type.type_to_blk.items():
        glbls[f'arr_list_typ_{nfr__qnths}'] = types.List(typ)
        jhsmx__hii = len(out_table_type.block_to_arr_ind[nfr__qnths])
        jto__qkm += f"""  out_arr_list_{nfr__qnths} = alloc_list_like(arr_list_typ_{nfr__qnths}, {jhsmx__hii}, False)
"""
        if typ in in_table_t.type_to_blk:
            xyrla__tco = in_table_t.type_to_blk[typ]
            beik__nsfh = []
            jyot__wstco = []
            for knv__pcve in out_table_type.block_to_arr_ind[nfr__qnths]:
                rjer__iee = in_col_inds[knv__pcve]
                if rjer__iee < rtp__yyffc:
                    beik__nsfh.append(in_table_t.block_offsets[rjer__iee])
                    jyot__wstco.append(rjer__iee)
                else:
                    beik__nsfh.append(-1)
                    jyot__wstco.append(-1)
            glbls[f'in_idxs_{nfr__qnths}'] = np.array(beik__nsfh, np.int64)
            glbls[f'in_arr_inds_{nfr__qnths}'] = np.array(jyot__wstco, np.int64
                )
            if vdeei__jfpl:
                glbls[f'out_arr_inds_{nfr__qnths}'] = np.array(out_table_type
                    .block_to_arr_ind[nfr__qnths], dtype=np.int64)
            jto__qkm += (
                f'  in_arr_list_{nfr__qnths} = get_table_block(T1, {xyrla__tco})\n'
                )
            jto__qkm += f'  for i in range(len(out_arr_list_{nfr__qnths})):\n'
            jto__qkm += (
                f'    in_offset_{nfr__qnths} = in_idxs_{nfr__qnths}[i]\n')
            jto__qkm += f'    if in_offset_{nfr__qnths} == -1:\n'
            jto__qkm += f'      continue\n'
            jto__qkm += (
                f'    in_arr_ind_{nfr__qnths} = in_arr_inds_{nfr__qnths}[i]\n')
            if vdeei__jfpl:
                jto__qkm += (
                    f'    if out_arr_inds_{nfr__qnths}[i] not in kept_cols_set: continue\n'
                    )
            jto__qkm += f"""    ensure_column_unboxed(T1, in_arr_list_{nfr__qnths}, in_offset_{nfr__qnths}, in_arr_ind_{nfr__qnths})
"""
            jto__qkm += f"""    out_arr_list_{nfr__qnths}[i] = in_arr_list_{nfr__qnths}[in_offset_{nfr__qnths}]
"""
        for i, knv__pcve in enumerate(out_table_type.block_to_arr_ind[
            nfr__qnths]):
            if knv__pcve not in kept_cols:
                continue
            rjer__iee = in_col_inds[knv__pcve]
            if rjer__iee >= rtp__yyffc:
                jto__qkm += f"""  out_arr_list_{nfr__qnths}[{i}] = extra_arrs_t[{rjer__iee - rtp__yyffc}]
"""
        jto__qkm += (
            f'  T2 = set_table_block(T2, out_arr_list_{nfr__qnths}, {nfr__qnths})\n'
            )
    jto__qkm += f'  return T2\n'
    glbls.update({'alloc_list_like': alloc_list_like, 'set_table_block':
        set_table_block, 'get_table_block': get_table_block,
        'ensure_column_unboxed': ensure_column_unboxed, 'get_series_data':
        bodo.hiframes.pd_series_ext.get_series_data})
    ljmbp__epvr = {}
    exec(jto__qkm, glbls, ljmbp__epvr)
    return ljmbp__epvr['impl']


def _logical_tuple_table_to_table_codegen(in_table_t, extra_arrs_t,
    in_col_inds, kept_cols, n_table_cols_t, out_table_type_t,
    extra_arrs_no_series):
    rtp__yyffc = get_overload_const_int(n_table_cols_t
        ) if is_overload_constant_int(n_table_cols_t) else len(in_table_t.types
        )
    out_table_type = TableType(tuple(in_table_t.types[i] if i < rtp__yyffc else
        _to_arr_if_series(extra_arrs_t.types[i - rtp__yyffc]) for i in
        in_col_inds)) if is_overload_none(out_table_type_t
        ) else unwrap_typeref(out_table_type_t)
    unvok__cafi = None
    if not is_overload_none(in_table_t):
        for i, t in enumerate(in_table_t.types):
            if t != types.none:
                unvok__cafi = f'in_table_t[{i}]'
                break
    if unvok__cafi is None:
        for i, t in enumerate(extra_arrs_t.types):
            if t != types.none:
                unvok__cafi = f'extra_arrs_t[{i}]'
                break
    assert unvok__cafi is not None, 'no array found in input data'
    jto__qkm = """def impl(in_table_t, extra_arrs_t, in_col_inds_t, n_table_cols_t, out_table_type_t=None, used_cols=None):
"""
    if any(isinstance(t, SeriesType) for t in extra_arrs_t.types):
        jto__qkm += f'  extra_arrs_t = {extra_arrs_no_series}\n'
    jto__qkm += f'  T1 = in_table_t\n'
    jto__qkm += f'  T2 = init_table(out_table_type, False)\n'
    jto__qkm += f'  T2 = set_table_len(T2, len({unvok__cafi}))\n'
    glbls = {}
    for typ, nfr__qnths in out_table_type.type_to_blk.items():
        glbls[f'arr_list_typ_{nfr__qnths}'] = types.List(typ)
        jhsmx__hii = len(out_table_type.block_to_arr_ind[nfr__qnths])
        jto__qkm += f"""  out_arr_list_{nfr__qnths} = alloc_list_like(arr_list_typ_{nfr__qnths}, {jhsmx__hii}, False)
"""
        for i, knv__pcve in enumerate(out_table_type.block_to_arr_ind[
            nfr__qnths]):
            if knv__pcve not in kept_cols:
                continue
            rjer__iee = in_col_inds[knv__pcve]
            if rjer__iee < rtp__yyffc:
                jto__qkm += (
                    f'  out_arr_list_{nfr__qnths}[{i}] = T1[{rjer__iee}]\n')
            else:
                jto__qkm += f"""  out_arr_list_{nfr__qnths}[{i}] = extra_arrs_t[{rjer__iee - rtp__yyffc}]
"""
        jto__qkm += (
            f'  T2 = set_table_block(T2, out_arr_list_{nfr__qnths}, {nfr__qnths})\n'
            )
    jto__qkm += f'  return T2\n'
    glbls.update({'init_table': init_table, 'alloc_list_like':
        alloc_list_like, 'set_table_block': set_table_block,
        'set_table_len': set_table_len, 'out_table_type': out_table_type,
        'get_series_data': bodo.hiframes.pd_series_ext.get_series_data})
    ljmbp__epvr = {}
    exec(jto__qkm, glbls, ljmbp__epvr)
    return ljmbp__epvr['impl']


def logical_table_to_table_equiv(self, scope, equiv_set, loc, args, kws):
    gvk__vkd = args[0]
    mstya__fve = args[1]
    if equiv_set.has_shape(gvk__vkd):
        return ArrayAnalysis.AnalyzeResult(shape=(equiv_set.get_shape(
            gvk__vkd)[0], None), pre=[])
    if equiv_set.has_shape(mstya__fve):
        return ArrayAnalysis.AnalyzeResult(shape=(equiv_set.get_shape(
            mstya__fve)[0], None), pre=[])


(ArrayAnalysis._analyze_op_call_bodo_hiframes_table_logical_table_to_table
    ) = logical_table_to_table_equiv


def alias_ext_logical_table_to_table(lhs_name, args, alias_map, arg_aliases):
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)
    numba.core.ir_utils._add_alias(lhs_name, args[1].name, alias_map,
        arg_aliases)


numba.core.ir_utils.alias_func_extensions['logical_table_to_table',
    'bodo.hiframes.table'] = alias_ext_logical_table_to_table
