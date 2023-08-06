"""helper functions for code generation with llvmlite
"""
import llvmlite.binding as ll
from llvmlite import ir as lir
from numba.core import cgutils, types
import bodo
from bodo.libs import array_ext, hdist
ll.add_symbol('array_getitem', array_ext.array_getitem)
ll.add_symbol('seq_getitem', array_ext.seq_getitem)
ll.add_symbol('list_check', array_ext.list_check)
ll.add_symbol('dict_keys', array_ext.dict_keys)
ll.add_symbol('dict_values', array_ext.dict_values)
ll.add_symbol('dict_merge_from_seq2', array_ext.dict_merge_from_seq2)
ll.add_symbol('is_na_value', array_ext.is_na_value)


def set_bitmap_bit(builder, null_bitmap_ptr, ind, val):
    wcs__rxy = builder.lshr(ind, lir.Constant(lir.IntType(64), 3))
    tmhhz__jvl = builder.urem(ind, lir.Constant(lir.IntType(64), 8))
    hrw__esttb = builder.gep(null_bitmap_ptr, [wcs__rxy], inbounds=True)
    vnld__irags = builder.load(hrw__esttb)
    layr__yhaq = lir.ArrayType(lir.IntType(8), 8)
    szqce__kon = cgutils.alloca_once_value(builder, lir.Constant(layr__yhaq,
        (1, 2, 4, 8, 16, 32, 64, 128)))
    nzbpe__jcigb = builder.load(builder.gep(szqce__kon, [lir.Constant(lir.
        IntType(64), 0), tmhhz__jvl], inbounds=True))
    if val:
        builder.store(builder.or_(vnld__irags, nzbpe__jcigb), hrw__esttb)
    else:
        nzbpe__jcigb = builder.xor(nzbpe__jcigb, lir.Constant(lir.IntType(8
            ), -1))
        builder.store(builder.and_(vnld__irags, nzbpe__jcigb), hrw__esttb)


def get_bitmap_bit(builder, null_bitmap_ptr, ind):
    wcs__rxy = builder.lshr(ind, lir.Constant(lir.IntType(64), 3))
    tmhhz__jvl = builder.urem(ind, lir.Constant(lir.IntType(64), 8))
    vnld__irags = builder.load(builder.gep(null_bitmap_ptr, [wcs__rxy],
        inbounds=True))
    layr__yhaq = lir.ArrayType(lir.IntType(8), 8)
    szqce__kon = cgutils.alloca_once_value(builder, lir.Constant(layr__yhaq,
        (1, 2, 4, 8, 16, 32, 64, 128)))
    nzbpe__jcigb = builder.load(builder.gep(szqce__kon, [lir.Constant(lir.
        IntType(64), 0), tmhhz__jvl], inbounds=True))
    return builder.and_(vnld__irags, nzbpe__jcigb)


def pyarray_check(builder, context, obj):
    fdw__gddcs = context.get_argument_type(types.pyobject)
    eqke__nth = lir.FunctionType(lir.IntType(32), [fdw__gddcs])
    ryr__nlxlz = cgutils.get_or_insert_function(builder.module, eqke__nth,
        name='is_np_array')
    return builder.call(ryr__nlxlz, [obj])


def pyarray_getitem(builder, context, arr_obj, ind):
    fdw__gddcs = context.get_argument_type(types.pyobject)
    gvow__bllu = context.get_value_type(types.intp)
    nfdpi__rhkcx = lir.FunctionType(lir.IntType(8).as_pointer(), [
        fdw__gddcs, gvow__bllu])
    esxyo__kzztz = cgutils.get_or_insert_function(builder.module,
        nfdpi__rhkcx, name='array_getptr1')
    njz__akr = lir.FunctionType(fdw__gddcs, [fdw__gddcs, lir.IntType(8).
        as_pointer()])
    mrhi__qtwzi = cgutils.get_or_insert_function(builder.module, njz__akr,
        name='array_getitem')
    jpw__dzw = builder.call(esxyo__kzztz, [arr_obj, ind])
    return builder.call(mrhi__qtwzi, [arr_obj, jpw__dzw])


def pyarray_setitem(builder, context, arr_obj, ind, val_obj):
    fdw__gddcs = context.get_argument_type(types.pyobject)
    gvow__bllu = context.get_value_type(types.intp)
    nfdpi__rhkcx = lir.FunctionType(lir.IntType(8).as_pointer(), [
        fdw__gddcs, gvow__bllu])
    esxyo__kzztz = cgutils.get_or_insert_function(builder.module,
        nfdpi__rhkcx, name='array_getptr1')
    noexz__cflg = lir.FunctionType(lir.VoidType(), [fdw__gddcs, lir.IntType
        (8).as_pointer(), fdw__gddcs])
    pkwkh__wkijy = cgutils.get_or_insert_function(builder.module,
        noexz__cflg, name='array_setitem')
    jpw__dzw = builder.call(esxyo__kzztz, [arr_obj, ind])
    builder.call(pkwkh__wkijy, [arr_obj, jpw__dzw, val_obj])


def seq_getitem(builder, context, obj, ind):
    fdw__gddcs = context.get_argument_type(types.pyobject)
    gvow__bllu = context.get_value_type(types.intp)
    alai__owe = lir.FunctionType(fdw__gddcs, [fdw__gddcs, gvow__bllu])
    kzpl__wlr = cgutils.get_or_insert_function(builder.module, alai__owe,
        name='seq_getitem')
    return builder.call(kzpl__wlr, [obj, ind])


def is_na_value(builder, context, val, C_NA):
    fdw__gddcs = context.get_argument_type(types.pyobject)
    adft__lafnf = lir.FunctionType(lir.IntType(32), [fdw__gddcs, fdw__gddcs])
    nvvhq__cdc = cgutils.get_or_insert_function(builder.module, adft__lafnf,
        name='is_na_value')
    return builder.call(nvvhq__cdc, [val, C_NA])


def list_check(builder, context, obj):
    fdw__gddcs = context.get_argument_type(types.pyobject)
    ldp__ipz = context.get_value_type(types.int32)
    rjl__zlkiy = lir.FunctionType(ldp__ipz, [fdw__gddcs])
    vhj__jfm = cgutils.get_or_insert_function(builder.module, rjl__zlkiy,
        name='list_check')
    return builder.call(vhj__jfm, [obj])


def dict_keys(builder, context, obj):
    fdw__gddcs = context.get_argument_type(types.pyobject)
    rjl__zlkiy = lir.FunctionType(fdw__gddcs, [fdw__gddcs])
    vhj__jfm = cgutils.get_or_insert_function(builder.module, rjl__zlkiy,
        name='dict_keys')
    return builder.call(vhj__jfm, [obj])


def dict_values(builder, context, obj):
    fdw__gddcs = context.get_argument_type(types.pyobject)
    rjl__zlkiy = lir.FunctionType(fdw__gddcs, [fdw__gddcs])
    vhj__jfm = cgutils.get_or_insert_function(builder.module, rjl__zlkiy,
        name='dict_values')
    return builder.call(vhj__jfm, [obj])


def dict_merge_from_seq2(builder, context, dict_obj, seq2_obj):
    fdw__gddcs = context.get_argument_type(types.pyobject)
    rjl__zlkiy = lir.FunctionType(lir.VoidType(), [fdw__gddcs, fdw__gddcs])
    vhj__jfm = cgutils.get_or_insert_function(builder.module, rjl__zlkiy,
        name='dict_merge_from_seq2')
    builder.call(vhj__jfm, [dict_obj, seq2_obj])


def to_arr_obj_if_list_obj(c, context, builder, val, typ):
    if not (isinstance(typ, types.List) or bodo.utils.utils.is_array_typ(
        typ, False)):
        return val
    lfqf__dha = cgutils.alloca_once_value(builder, val)
    vdgn__xwbf = list_check(builder, context, val)
    gihyt__ife = builder.icmp_unsigned('!=', vdgn__xwbf, lir.Constant(
        vdgn__xwbf.type, 0))
    with builder.if_then(gihyt__ife):
        bnza__sohdg = context.insert_const_string(builder.module, 'numpy')
        dnse__kbnt = c.pyapi.import_module_noblock(bnza__sohdg)
        hsd__vcox = 'object_'
        if isinstance(typ, types.Array) or isinstance(typ.dtype, types.Float):
            hsd__vcox = str(typ.dtype)
        uon__gtpo = c.pyapi.object_getattr_string(dnse__kbnt, hsd__vcox)
        dsm__pjaaz = builder.load(lfqf__dha)
        jtuu__mcwk = c.pyapi.call_method(dnse__kbnt, 'asarray', (dsm__pjaaz,
            uon__gtpo))
        builder.store(jtuu__mcwk, lfqf__dha)
        c.pyapi.decref(dnse__kbnt)
        c.pyapi.decref(uon__gtpo)
    val = builder.load(lfqf__dha)
    return val


def get_array_elem_counts(c, builder, context, arr_obj, typ):
    from bodo.libs.array_item_arr_ext import ArrayItemArrayType
    from bodo.libs.map_arr_ext import MapArrayType
    from bodo.libs.str_arr_ext import get_utf8_size, string_array_type
    from bodo.libs.struct_arr_ext import StructArrayType, StructType
    from bodo.libs.tuple_arr_ext import TupleArrayType
    if typ == bodo.string_type:
        kuezt__kmxyv = c.pyapi.to_native_value(bodo.string_type, arr_obj).value
        lxiie__zseo, yosye__xvp = c.pyapi.call_jit_code(lambda a:
            get_utf8_size(a), types.int64(bodo.string_type), [kuezt__kmxyv])
        context.nrt.decref(builder, typ, kuezt__kmxyv)
        return cgutils.pack_array(builder, [yosye__xvp])
    if isinstance(typ, (StructType, types.BaseTuple)):
        bnza__sohdg = context.insert_const_string(builder.module, 'pandas')
        sto__zybb = c.pyapi.import_module_noblock(bnza__sohdg)
        C_NA = c.pyapi.object_getattr_string(sto__zybb, 'NA')
        ecblz__oxn = bodo.utils.transform.get_type_alloc_counts(typ)
        rmv__mzcuf = context.make_tuple(builder, types.Tuple(ecblz__oxn * [
            types.int64]), ecblz__oxn * [context.get_constant(types.int64, 0)])
        sksdc__kxq = cgutils.alloca_once_value(builder, rmv__mzcuf)
        abr__bvuhp = 0
        sjzf__xsyq = typ.data if isinstance(typ, StructType) else typ.types
        for egqh__blorv, t in enumerate(sjzf__xsyq):
            uun__uubql = bodo.utils.transform.get_type_alloc_counts(t)
            if uun__uubql == 0:
                continue
            if isinstance(typ, StructType):
                val_obj = c.pyapi.dict_getitem_string(arr_obj, typ.names[
                    egqh__blorv])
            else:
                val_obj = c.pyapi.tuple_getitem(arr_obj, egqh__blorv)
            orbb__evsmv = is_na_value(builder, context, val_obj, C_NA)
            uwgrw__wtudo = builder.icmp_unsigned('!=', orbb__evsmv, lir.
                Constant(orbb__evsmv.type, 1))
            with builder.if_then(uwgrw__wtudo):
                rmv__mzcuf = builder.load(sksdc__kxq)
                jwdn__juk = get_array_elem_counts(c, builder, context,
                    val_obj, t)
                for egqh__blorv in range(uun__uubql):
                    iagz__mds = builder.extract_value(rmv__mzcuf, 
                        abr__bvuhp + egqh__blorv)
                    ugys__fdw = builder.extract_value(jwdn__juk, egqh__blorv)
                    rmv__mzcuf = builder.insert_value(rmv__mzcuf, builder.
                        add(iagz__mds, ugys__fdw), abr__bvuhp + egqh__blorv)
                builder.store(rmv__mzcuf, sksdc__kxq)
            abr__bvuhp += uun__uubql
        c.pyapi.decref(sto__zybb)
        c.pyapi.decref(C_NA)
        return builder.load(sksdc__kxq)
    if not bodo.utils.utils.is_array_typ(typ, False):
        return cgutils.pack_array(builder, [], lir.IntType(64))
    n = bodo.utils.utils.object_length(c, arr_obj)
    if not (isinstance(typ, (ArrayItemArrayType, StructArrayType,
        TupleArrayType, MapArrayType)) or typ == string_array_type):
        return cgutils.pack_array(builder, [n])
    bnza__sohdg = context.insert_const_string(builder.module, 'pandas')
    sto__zybb = c.pyapi.import_module_noblock(bnza__sohdg)
    C_NA = c.pyapi.object_getattr_string(sto__zybb, 'NA')
    ecblz__oxn = bodo.utils.transform.get_type_alloc_counts(typ)
    rmv__mzcuf = context.make_tuple(builder, types.Tuple(ecblz__oxn * [
        types.int64]), [n] + (ecblz__oxn - 1) * [context.get_constant(types
        .int64, 0)])
    sksdc__kxq = cgutils.alloca_once_value(builder, rmv__mzcuf)
    with cgutils.for_range(builder, n) as uud__dxsac:
        kbx__xczxd = uud__dxsac.index
        tan__xtfsk = seq_getitem(builder, context, arr_obj, kbx__xczxd)
        orbb__evsmv = is_na_value(builder, context, tan__xtfsk, C_NA)
        uwgrw__wtudo = builder.icmp_unsigned('!=', orbb__evsmv, lir.
            Constant(orbb__evsmv.type, 1))
        with builder.if_then(uwgrw__wtudo):
            if isinstance(typ, ArrayItemArrayType) or typ == string_array_type:
                rmv__mzcuf = builder.load(sksdc__kxq)
                jwdn__juk = get_array_elem_counts(c, builder, context,
                    tan__xtfsk, typ.dtype)
                for egqh__blorv in range(ecblz__oxn - 1):
                    iagz__mds = builder.extract_value(rmv__mzcuf, 
                        egqh__blorv + 1)
                    ugys__fdw = builder.extract_value(jwdn__juk, egqh__blorv)
                    rmv__mzcuf = builder.insert_value(rmv__mzcuf, builder.
                        add(iagz__mds, ugys__fdw), egqh__blorv + 1)
                builder.store(rmv__mzcuf, sksdc__kxq)
            elif isinstance(typ, (StructArrayType, TupleArrayType)):
                abr__bvuhp = 1
                for egqh__blorv, t in enumerate(typ.data):
                    uun__uubql = bodo.utils.transform.get_type_alloc_counts(t
                        .dtype)
                    if uun__uubql == 0:
                        continue
                    if isinstance(typ, TupleArrayType):
                        val_obj = c.pyapi.tuple_getitem(tan__xtfsk, egqh__blorv
                            )
                    else:
                        val_obj = c.pyapi.dict_getitem_string(tan__xtfsk,
                            typ.names[egqh__blorv])
                    orbb__evsmv = is_na_value(builder, context, val_obj, C_NA)
                    uwgrw__wtudo = builder.icmp_unsigned('!=', orbb__evsmv,
                        lir.Constant(orbb__evsmv.type, 1))
                    with builder.if_then(uwgrw__wtudo):
                        rmv__mzcuf = builder.load(sksdc__kxq)
                        jwdn__juk = get_array_elem_counts(c, builder,
                            context, val_obj, t.dtype)
                        for egqh__blorv in range(uun__uubql):
                            iagz__mds = builder.extract_value(rmv__mzcuf, 
                                abr__bvuhp + egqh__blorv)
                            ugys__fdw = builder.extract_value(jwdn__juk,
                                egqh__blorv)
                            rmv__mzcuf = builder.insert_value(rmv__mzcuf,
                                builder.add(iagz__mds, ugys__fdw), 
                                abr__bvuhp + egqh__blorv)
                        builder.store(rmv__mzcuf, sksdc__kxq)
                    abr__bvuhp += uun__uubql
            else:
                assert isinstance(typ, MapArrayType), typ
                rmv__mzcuf = builder.load(sksdc__kxq)
                mcxg__ung = dict_keys(builder, context, tan__xtfsk)
                rle__wwida = dict_values(builder, context, tan__xtfsk)
                ikk__mvnx = get_array_elem_counts(c, builder, context,
                    mcxg__ung, typ.key_arr_type)
                nxbho__alo = bodo.utils.transform.get_type_alloc_counts(typ
                    .key_arr_type)
                for egqh__blorv in range(1, nxbho__alo + 1):
                    iagz__mds = builder.extract_value(rmv__mzcuf, egqh__blorv)
                    ugys__fdw = builder.extract_value(ikk__mvnx, 
                        egqh__blorv - 1)
                    rmv__mzcuf = builder.insert_value(rmv__mzcuf, builder.
                        add(iagz__mds, ugys__fdw), egqh__blorv)
                dmaht__iby = get_array_elem_counts(c, builder, context,
                    rle__wwida, typ.value_arr_type)
                for egqh__blorv in range(nxbho__alo + 1, ecblz__oxn):
                    iagz__mds = builder.extract_value(rmv__mzcuf, egqh__blorv)
                    ugys__fdw = builder.extract_value(dmaht__iby, 
                        egqh__blorv - nxbho__alo)
                    rmv__mzcuf = builder.insert_value(rmv__mzcuf, builder.
                        add(iagz__mds, ugys__fdw), egqh__blorv)
                builder.store(rmv__mzcuf, sksdc__kxq)
                c.pyapi.decref(mcxg__ung)
                c.pyapi.decref(rle__wwida)
        c.pyapi.decref(tan__xtfsk)
    c.pyapi.decref(sto__zybb)
    c.pyapi.decref(C_NA)
    return builder.load(sksdc__kxq)


def gen_allocate_array(context, builder, arr_type, n_elems, c=None):
    xnlk__xxthg = n_elems.type.count
    assert xnlk__xxthg >= 1
    hmbdd__jsb = builder.extract_value(n_elems, 0)
    if xnlk__xxthg != 1:
        aiaxh__oro = cgutils.pack_array(builder, [builder.extract_value(
            n_elems, egqh__blorv) for egqh__blorv in range(1, xnlk__xxthg)])
        lmgvl__rkd = types.Tuple([types.int64] * (xnlk__xxthg - 1))
    else:
        aiaxh__oro = context.get_dummy_value()
        lmgvl__rkd = types.none
    hqnj__grgrb = types.TypeRef(arr_type)
    iser__bzppy = arr_type(types.int64, hqnj__grgrb, lmgvl__rkd)
    args = [hmbdd__jsb, context.get_dummy_value(), aiaxh__oro]
    ovixz__ppfxa = lambda n, t, s: bodo.utils.utils.alloc_type(n, t, s)
    if c:
        lxiie__zseo, qzn__mhr = c.pyapi.call_jit_code(ovixz__ppfxa,
            iser__bzppy, args)
    else:
        qzn__mhr = context.compile_internal(builder, ovixz__ppfxa,
            iser__bzppy, args)
    return qzn__mhr


def is_ll_eq(builder, val1, val2):
    xuz__ajtc = val1.type.pointee
    wjbs__lgwkd = val2.type.pointee
    assert xuz__ajtc == wjbs__lgwkd, 'invalid llvm value comparison'
    if isinstance(xuz__ajtc, (lir.BaseStructType, lir.ArrayType)):
        n_elems = len(xuz__ajtc.elements) if isinstance(xuz__ajtc, lir.
            BaseStructType) else xuz__ajtc.count
        wxqz__osot = lir.Constant(lir.IntType(1), 1)
        for egqh__blorv in range(n_elems):
            aho__xikx = lir.IntType(32)(0)
            vdd__zrbvx = lir.IntType(32)(egqh__blorv)
            rdveq__ozb = builder.gep(val1, [aho__xikx, vdd__zrbvx],
                inbounds=True)
            zui__toenj = builder.gep(val2, [aho__xikx, vdd__zrbvx],
                inbounds=True)
            wxqz__osot = builder.and_(wxqz__osot, is_ll_eq(builder,
                rdveq__ozb, zui__toenj))
        return wxqz__osot
    gndb__tfusx = builder.load(val1)
    yvbzv__gauiw = builder.load(val2)
    if gndb__tfusx.type in (lir.FloatType(), lir.DoubleType()):
        cgn__rmi = 32 if gndb__tfusx.type == lir.FloatType() else 64
        gndb__tfusx = builder.bitcast(gndb__tfusx, lir.IntType(cgn__rmi))
        yvbzv__gauiw = builder.bitcast(yvbzv__gauiw, lir.IntType(cgn__rmi))
    return builder.icmp_unsigned('==', gndb__tfusx, yvbzv__gauiw)
