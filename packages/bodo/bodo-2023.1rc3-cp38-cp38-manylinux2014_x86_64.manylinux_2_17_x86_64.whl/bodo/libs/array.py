"""Tools for handling bodo arrays, e.g. passing to C/C++ code
"""
from collections import defaultdict
import llvmlite.binding as ll
import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.imputils import lower_cast
from numba.core.typing.templates import signature
from numba.cpython.listobj import ListInstance
from numba.extending import intrinsic, models, register_model
from numba.np.arrayobj import _getitem_array_single_int
import bodo
from bodo.hiframes.datetime_date_ext import datetime_date_array_type
from bodo.hiframes.pd_categorical_ext import CategoricalArrayType, get_categories_int_type
from bodo.hiframes.time_ext import TimeArrayType, TimeType
from bodo.libs import array_ext
from bodo.libs.array_item_arr_ext import ArrayItemArrayPayloadType, ArrayItemArrayType, _get_array_item_arr_payload, define_array_item_dtor, offset_type
from bodo.libs.binary_arr_ext import binary_array_type
from bodo.libs.bool_arr_ext import boolean_array
from bodo.libs.decimal_arr_ext import DecimalArrayType, int128_type
from bodo.libs.float_arr_ext import FloatingArrayType
from bodo.libs.int_arr_ext import IntegerArrayType
from bodo.libs.interval_arr_ext import IntervalArrayType
from bodo.libs.map_arr_ext import MapArrayType, _get_map_arr_data_type, init_map_arr_codegen
from bodo.libs.str_arr_ext import _get_str_binary_arr_payload, char_arr_type, null_bitmap_arr_type, offset_arr_type, string_array_type
from bodo.libs.struct_arr_ext import StructArrayPayloadType, StructArrayType, StructType, _get_struct_arr_payload, define_struct_arr_dtor
from bodo.libs.tuple_arr_ext import TupleArrayType
from bodo.utils.typing import BodoError, MetaType, decode_if_dict_array, get_overload_const_int, is_overload_none, is_str_arr_type, raise_bodo_error, type_has_unknown_cats, unwrap_typeref
from bodo.utils.utils import CTypeEnum, check_and_propagate_cpp_exception, numba_to_c_type
ll.add_symbol('list_string_array_to_info', array_ext.list_string_array_to_info)
ll.add_symbol('nested_array_to_info', array_ext.nested_array_to_info)
ll.add_symbol('string_array_to_info', array_ext.string_array_to_info)
ll.add_symbol('dict_str_array_to_info', array_ext.dict_str_array_to_info)
ll.add_symbol('get_nested_info', array_ext.get_nested_info)
ll.add_symbol('get_has_global_dictionary', array_ext.get_has_global_dictionary)
ll.add_symbol('get_has_deduped_local_dictionary', array_ext.
    get_has_deduped_local_dictionary)
ll.add_symbol('numpy_array_to_info', array_ext.numpy_array_to_info)
ll.add_symbol('categorical_array_to_info', array_ext.categorical_array_to_info)
ll.add_symbol('nullable_array_to_info', array_ext.nullable_array_to_info)
ll.add_symbol('interval_array_to_info', array_ext.interval_array_to_info)
ll.add_symbol('decimal_array_to_info', array_ext.decimal_array_to_info)
ll.add_symbol('time_array_to_info', array_ext.time_array_to_info)
ll.add_symbol('info_to_nested_array', array_ext.info_to_nested_array)
ll.add_symbol('info_to_list_string_array', array_ext.info_to_list_string_array)
ll.add_symbol('info_to_string_array', array_ext.info_to_string_array)
ll.add_symbol('info_to_numpy_array', array_ext.info_to_numpy_array)
ll.add_symbol('info_to_nullable_array', array_ext.info_to_nullable_array)
ll.add_symbol('info_to_interval_array', array_ext.info_to_interval_array)
ll.add_symbol('alloc_numpy', array_ext.alloc_numpy)
ll.add_symbol('alloc_string_array', array_ext.alloc_string_array)
ll.add_symbol('arr_info_list_to_table', array_ext.arr_info_list_to_table)
ll.add_symbol('info_from_table', array_ext.info_from_table)
ll.add_symbol('delete_info_decref_array', array_ext.delete_info_decref_array)
ll.add_symbol('delete_table_decref_arrays', array_ext.
    delete_table_decref_arrays)
ll.add_symbol('decref_table_array', array_ext.decref_table_array)
ll.add_symbol('delete_table', array_ext.delete_table)
ll.add_symbol('shuffle_table', array_ext.shuffle_table)
ll.add_symbol('get_shuffle_info', array_ext.get_shuffle_info)
ll.add_symbol('delete_shuffle_info', array_ext.delete_shuffle_info)
ll.add_symbol('reverse_shuffle_table', array_ext.reverse_shuffle_table)
ll.add_symbol('hash_join_table', array_ext.hash_join_table)
ll.add_symbol('cross_join_table', array_ext.cross_join_table)
ll.add_symbol('drop_duplicates_table', array_ext.drop_duplicates_table)
ll.add_symbol('sort_values_table', array_ext.sort_values_table)
ll.add_symbol('sample_table', array_ext.sample_table)
ll.add_symbol('shuffle_renormalization', array_ext.shuffle_renormalization)
ll.add_symbol('shuffle_renormalization_group', array_ext.
    shuffle_renormalization_group)
ll.add_symbol('groupby_and_aggregate', array_ext.groupby_and_aggregate)
ll.add_symbol('convert_local_dictionary_to_global', array_ext.
    convert_local_dictionary_to_global)
ll.add_symbol('drop_duplicates_local_dictionary', array_ext.
    drop_duplicates_local_dictionary)
ll.add_symbol('get_groupby_labels', array_ext.get_groupby_labels)
ll.add_symbol('array_isin', array_ext.array_isin)
ll.add_symbol('get_search_regex', array_ext.get_search_regex)
ll.add_symbol('array_info_getitem', array_ext.array_info_getitem)
ll.add_symbol('array_info_getdata1', array_ext.array_info_getdata1)


class ArrayInfoType(types.Type):

    def __init__(self):
        super(ArrayInfoType, self).__init__(name='ArrayInfoType()')


array_info_type = ArrayInfoType()
register_model(ArrayInfoType)(models.OpaqueModel)


class TableTypeCPP(types.Type):

    def __init__(self):
        super(TableTypeCPP, self).__init__(name='TableTypeCPP()')


table_type = TableTypeCPP()
register_model(TableTypeCPP)(models.OpaqueModel)


@lower_cast(table_type, types.voidptr)
def lower_table_type(context, builder, fromty, toty, val):
    return val


@intrinsic
def array_to_info(typingctx, arr_type_t=None):
    return array_info_type(arr_type_t), array_to_info_codegen


def array_to_info_codegen(context, builder, sig, args, incref=True):
    in_arr, = args
    arr_type = sig.args[0]
    if incref:
        context.nrt.incref(builder, arr_type, in_arr)
    if isinstance(arr_type, TupleArrayType):
        xklis__cdos = context.make_helper(builder, arr_type, in_arr)
        in_arr = xklis__cdos.data
        arr_type = StructArrayType(arr_type.data, ('dummy',) * len(arr_type
            .data))
    if isinstance(arr_type, ArrayItemArrayType
        ) and arr_type.dtype == string_array_type:
        wos__zzgt = context.make_helper(builder, arr_type, in_arr)
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer()])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='list_string_array_to_info')
        return builder.call(sgt__jar, [wos__zzgt.meminfo])
    if isinstance(arr_type, (MapArrayType, ArrayItemArrayType, StructArrayType)
        ):

        def get_types(arr_typ):
            if isinstance(arr_typ, MapArrayType):
                return get_types(_get_map_arr_data_type(arr_typ))
            elif isinstance(arr_typ, ArrayItemArrayType):
                return [CTypeEnum.LIST.value] + get_types(arr_typ.dtype)
            elif isinstance(arr_typ, (StructType, StructArrayType)):
                rqe__dqr = [CTypeEnum.STRUCT.value, len(arr_typ.names)]
                for wcf__necq in arr_typ.data:
                    rqe__dqr += get_types(wcf__necq)
                return rqe__dqr
            elif isinstance(arr_typ, (types.Array, IntegerArrayType,
                FloatingArrayType)) or arr_typ == boolean_array:
                return get_types(arr_typ.dtype)
            elif arr_typ == string_array_type:
                return [CTypeEnum.STRING.value]
            elif arr_typ == binary_array_type:
                return [CTypeEnum.BINARY.value]
            elif isinstance(arr_typ, DecimalArrayType):
                return [CTypeEnum.Decimal.value, arr_typ.precision, arr_typ
                    .scale]
            else:
                return [numba_to_c_type(arr_typ)]

        def get_lengths(arr_typ, arr):
            length = context.compile_internal(builder, lambda a: len(a),
                types.intp(arr_typ), [arr])
            if isinstance(arr_typ, MapArrayType):
                ftl__wan = context.make_helper(builder, arr_typ, value=arr)
                ogveo__apu = get_lengths(_get_map_arr_data_type(arr_typ),
                    ftl__wan.data)
            elif isinstance(arr_typ, ArrayItemArrayType):
                rivfm__bbi = _get_array_item_arr_payload(context, builder,
                    arr_typ, arr)
                ogveo__apu = get_lengths(arr_typ.dtype, rivfm__bbi.data)
                ogveo__apu = cgutils.pack_array(builder, [rivfm__bbi.
                    n_arrays] + [builder.extract_value(ogveo__apu,
                    yeh__satbe) for yeh__satbe in range(ogveo__apu.type.count)]
                    )
            elif isinstance(arr_typ, StructArrayType):
                rivfm__bbi = _get_struct_arr_payload(context, builder,
                    arr_typ, arr)
                ogveo__apu = []
                for yeh__satbe, wcf__necq in enumerate(arr_typ.data):
                    uvis__eaky = get_lengths(wcf__necq, builder.
                        extract_value(rivfm__bbi.data, yeh__satbe))
                    ogveo__apu += [builder.extract_value(uvis__eaky,
                        fvf__ssr) for fvf__ssr in range(uvis__eaky.type.count)]
                ogveo__apu = cgutils.pack_array(builder, [length, context.
                    get_constant(types.int64, -1)] + ogveo__apu)
            elif isinstance(arr_typ, (IntegerArrayType, FloatingArrayType,
                DecimalArrayType, types.Array)) or arr_typ in (boolean_array,
                datetime_date_array_type, string_array_type, binary_array_type
                ):
                ogveo__apu = cgutils.pack_array(builder, [length])
            else:
                raise BodoError(
                    f'array_to_info: unsupported type for subarray {arr_typ}')
            return ogveo__apu

        def get_buffers(arr_typ, arr):
            if isinstance(arr_typ, MapArrayType):
                ftl__wan = context.make_helper(builder, arr_typ, value=arr)
                ffcuy__seee = get_buffers(_get_map_arr_data_type(arr_typ),
                    ftl__wan.data)
            elif isinstance(arr_typ, ArrayItemArrayType):
                rivfm__bbi = _get_array_item_arr_payload(context, builder,
                    arr_typ, arr)
                gxnbn__mojn = get_buffers(arr_typ.dtype, rivfm__bbi.data)
                dyf__uvdn = context.make_array(types.Array(offset_type, 1, 'C')
                    )(context, builder, rivfm__bbi.offsets)
                qozve__qfksd = builder.bitcast(dyf__uvdn.data, lir.IntType(
                    8).as_pointer())
                cpej__nrupt = context.make_array(types.Array(types.uint8, 1,
                    'C'))(context, builder, rivfm__bbi.null_bitmap)
                xlx__gym = builder.bitcast(cpej__nrupt.data, lir.IntType(8)
                    .as_pointer())
                ffcuy__seee = cgutils.pack_array(builder, [qozve__qfksd,
                    xlx__gym] + [builder.extract_value(gxnbn__mojn,
                    yeh__satbe) for yeh__satbe in range(gxnbn__mojn.type.
                    count)])
            elif isinstance(arr_typ, StructArrayType):
                rivfm__bbi = _get_struct_arr_payload(context, builder,
                    arr_typ, arr)
                gxnbn__mojn = []
                for yeh__satbe, wcf__necq in enumerate(arr_typ.data):
                    ono__lqspt = get_buffers(wcf__necq, builder.
                        extract_value(rivfm__bbi.data, yeh__satbe))
                    gxnbn__mojn += [builder.extract_value(ono__lqspt,
                        fvf__ssr) for fvf__ssr in range(ono__lqspt.type.count)]
                cpej__nrupt = context.make_array(types.Array(types.uint8, 1,
                    'C'))(context, builder, rivfm__bbi.null_bitmap)
                xlx__gym = builder.bitcast(cpej__nrupt.data, lir.IntType(8)
                    .as_pointer())
                ffcuy__seee = cgutils.pack_array(builder, [xlx__gym] +
                    gxnbn__mojn)
            elif isinstance(arr_typ, (IntegerArrayType, FloatingArrayType,
                DecimalArrayType)) or arr_typ in (boolean_array,
                datetime_date_array_type):
                fbgd__scht = arr_typ.dtype
                if isinstance(arr_typ, DecimalArrayType):
                    fbgd__scht = int128_type
                elif arr_typ == datetime_date_array_type:
                    fbgd__scht = types.int64
                arr = cgutils.create_struct_proxy(arr_typ)(context, builder,
                    arr)
                yhgmp__fsn = context.make_array(types.Array(fbgd__scht, 1, 'C')
                    )(context, builder, arr.data)
                cpej__nrupt = context.make_array(types.Array(types.uint8, 1,
                    'C'))(context, builder, arr.null_bitmap)
                yci__xjpy = builder.bitcast(yhgmp__fsn.data, lir.IntType(8)
                    .as_pointer())
                xlx__gym = builder.bitcast(cpej__nrupt.data, lir.IntType(8)
                    .as_pointer())
                ffcuy__seee = cgutils.pack_array(builder, [xlx__gym, yci__xjpy]
                    )
            elif arr_typ in (string_array_type, binary_array_type):
                rivfm__bbi = _get_str_binary_arr_payload(context, builder,
                    arr, arr_typ)
                bylb__twd = context.make_helper(builder, offset_arr_type,
                    rivfm__bbi.offsets).data
                data = context.make_helper(builder, char_arr_type,
                    rivfm__bbi.data).data
                jmtva__zzqdu = context.make_helper(builder,
                    null_bitmap_arr_type, rivfm__bbi.null_bitmap).data
                ffcuy__seee = cgutils.pack_array(builder, [builder.bitcast(
                    bylb__twd, lir.IntType(8).as_pointer()), builder.
                    bitcast(jmtva__zzqdu, lir.IntType(8).as_pointer()),
                    builder.bitcast(data, lir.IntType(8).as_pointer())])
            elif isinstance(arr_typ, types.Array):
                arr = context.make_array(arr_typ)(context, builder, arr)
                yci__xjpy = builder.bitcast(arr.data, lir.IntType(8).
                    as_pointer())
                dhhxv__zppdo = lir.Constant(lir.IntType(8).as_pointer(), None)
                ffcuy__seee = cgutils.pack_array(builder, [dhhxv__zppdo,
                    yci__xjpy])
            else:
                raise RuntimeError(
                    'array_to_info: unsupported type for subarray ' + str(
                    arr_typ))
            return ffcuy__seee

        def get_field_names(arr_typ):
            uuucj__eki = []
            if isinstance(arr_typ, StructArrayType):
                for yjva__rgxn, lzr__qmi in zip(arr_typ.dtype.names,
                    arr_typ.data):
                    uuucj__eki.append(yjva__rgxn)
                    uuucj__eki += get_field_names(lzr__qmi)
            elif isinstance(arr_typ, ArrayItemArrayType):
                uuucj__eki += get_field_names(arr_typ.dtype)
            elif isinstance(arr_typ, MapArrayType):
                uuucj__eki += get_field_names(_get_map_arr_data_type(arr_typ))
            return uuucj__eki
        rqe__dqr = get_types(arr_type)
        hxxwu__iro = cgutils.pack_array(builder, [context.get_constant(
            types.int32, t) for t in rqe__dqr])
        locdz__vwipy = cgutils.alloca_once_value(builder, hxxwu__iro)
        ogveo__apu = get_lengths(arr_type, in_arr)
        lengths_ptr = cgutils.alloca_once_value(builder, ogveo__apu)
        ffcuy__seee = get_buffers(arr_type, in_arr)
        qrs__nwg = cgutils.alloca_once_value(builder, ffcuy__seee)
        uuucj__eki = get_field_names(arr_type)
        if len(uuucj__eki) == 0:
            uuucj__eki = ['irrelevant']
        lkpre__ggpzh = cgutils.pack_array(builder, [context.
            insert_const_string(builder.module, a) for a in uuucj__eki])
        jmst__pddmv = cgutils.alloca_once_value(builder, lkpre__ggpzh)
        if isinstance(arr_type, MapArrayType):
            egv__lzn = _get_map_arr_data_type(arr_type)
            gpi__lylti = context.make_helper(builder, arr_type, value=in_arr)
            dsdci__agvt = gpi__lylti.data
        else:
            egv__lzn = arr_type
            dsdci__agvt = in_arr
        luf__iabc = context.make_helper(builder, egv__lzn, dsdci__agvt)
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(32).as_pointer(), lir.IntType(8).as_pointer().
            as_pointer(), lir.IntType(64).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer()])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='nested_array_to_info')
        upm__xeqs = builder.call(sgt__jar, [builder.bitcast(locdz__vwipy,
            lir.IntType(32).as_pointer()), builder.bitcast(qrs__nwg, lir.
            IntType(8).as_pointer().as_pointer()), builder.bitcast(
            lengths_ptr, lir.IntType(64).as_pointer()), builder.bitcast(
            jmst__pddmv, lir.IntType(8).as_pointer()), luf__iabc.meminfo])
        context.compile_internal(builder, lambda :
            check_and_propagate_cpp_exception(), types.none(), [])
        return upm__xeqs
    if arr_type in (string_array_type, binary_array_type):
        znt__dzlpm = context.make_helper(builder, arr_type, in_arr)
        weke__jmm = ArrayItemArrayType(char_arr_type)
        wos__zzgt = context.make_helper(builder, weke__jmm, znt__dzlpm.data)
        rivfm__bbi = _get_str_binary_arr_payload(context, builder, in_arr,
            arr_type)
        bylb__twd = context.make_helper(builder, offset_arr_type,
            rivfm__bbi.offsets).data
        data = context.make_helper(builder, char_arr_type, rivfm__bbi.data
            ).data
        jmtva__zzqdu = context.make_helper(builder, null_bitmap_arr_type,
            rivfm__bbi.null_bitmap).data
        sbj__yupyc = builder.zext(builder.load(builder.gep(bylb__twd, [
            rivfm__bbi.n_arrays])), lir.IntType(64))
        iqye__rxh = context.get_constant(types.int32, int(arr_type ==
            binary_array_type))
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(64), lir.IntType(64), lir.IntType(8).as_pointer(), lir.
            IntType(offset_type.bitwidth).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(32)])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='string_array_to_info')
        return builder.call(sgt__jar, [rivfm__bbi.n_arrays, sbj__yupyc,
            data, bylb__twd, jmtva__zzqdu, wos__zzgt.meminfo, iqye__rxh])
    if arr_type == bodo.dict_str_arr_type:
        arr = cgutils.create_struct_proxy(arr_type)(context, builder, in_arr)
        ktb__prz = arr.data
        gnc__qtjcc = arr.indices
        sig = array_info_type(arr_type.data)
        bniei__wmwwc = array_to_info_codegen(context, builder, sig, (
            ktb__prz,), False)
        sig = array_info_type(bodo.libs.dict_arr_ext.dict_indices_arr_type)
        vva__yygao = array_to_info_codegen(context, builder, sig, (
            gnc__qtjcc,), False)
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(8).as_pointer(), lir.
            IntType(32), lir.IntType(32)])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='dict_str_array_to_info')
        ain__qld = builder.zext(arr.has_global_dictionary, lir.IntType(32))
        citww__jxrja = builder.zext(arr.has_deduped_local_dictionary, lir.
            IntType(32))
        return builder.call(sgt__jar, [bniei__wmwwc, vva__yygao, ain__qld,
            citww__jxrja])
    yig__vitf = False
    if isinstance(arr_type, CategoricalArrayType):
        context.nrt.decref(builder, arr_type, in_arr)
        ijnli__plyo = context.compile_internal(builder, lambda a: len(a.
            dtype.categories), types.intp(arr_type), [in_arr])
        in_arr = cgutils.create_struct_proxy(arr_type)(context, builder, in_arr
            ).codes
        hzbyy__krou = get_categories_int_type(arr_type.dtype)
        arr_type = types.Array(hzbyy__krou, 1, 'C')
        yig__vitf = True
        context.nrt.incref(builder, arr_type, in_arr)
    if isinstance(arr_type, bodo.DatetimeArrayType):
        if yig__vitf:
            raise BodoError(
                'array_to_info(): Categorical PandasDatetimeArrayType not supported'
                )
        in_arr = cgutils.create_struct_proxy(arr_type)(context, builder, in_arr
            ).data
        arr_type = arr_type.data_array_type
    if isinstance(arr_type, types.Array):
        arr = context.make_array(arr_type)(context, builder, in_arr)
        assert arr_type.ndim == 1, 'only 1D array shuffle supported'
        length = builder.extract_value(arr.shape, 0)
        ahz__epvq = arr_type.dtype
        mufnf__ufumn = numba_to_c_type(ahz__epvq)
        cbvme__bnqr = cgutils.alloca_once_value(builder, lir.Constant(lir.
            IntType(32), mufnf__ufumn))
        if yig__vitf:
            jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [
                lir.IntType(64), lir.IntType(8).as_pointer(), lir.IntType(
                32), lir.IntType(64), lir.IntType(8).as_pointer()])
            sgt__jar = cgutils.get_or_insert_function(builder.module,
                jhakg__yvqke, name='categorical_array_to_info')
            return builder.call(sgt__jar, [length, builder.bitcast(arr.data,
                lir.IntType(8).as_pointer()), builder.load(cbvme__bnqr),
                ijnli__plyo, arr.meminfo])
        else:
            jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [
                lir.IntType(64), lir.IntType(8).as_pointer(), lir.IntType(
                32), lir.IntType(8).as_pointer()])
            sgt__jar = cgutils.get_or_insert_function(builder.module,
                jhakg__yvqke, name='numpy_array_to_info')
            return builder.call(sgt__jar, [length, builder.bitcast(arr.data,
                lir.IntType(8).as_pointer()), builder.load(cbvme__bnqr),
                arr.meminfo])
    if isinstance(arr_type, (IntegerArrayType, FloatingArrayType,
        DecimalArrayType, TimeArrayType)) or arr_type in (boolean_array,
        datetime_date_array_type):
        arr = cgutils.create_struct_proxy(arr_type)(context, builder, in_arr)
        ahz__epvq = arr_type.dtype
        fbgd__scht = ahz__epvq
        if isinstance(arr_type, DecimalArrayType):
            fbgd__scht = int128_type
        if arr_type == datetime_date_array_type:
            fbgd__scht = types.int64
        yhgmp__fsn = context.make_array(types.Array(fbgd__scht, 1, 'C'))(
            context, builder, arr.data)
        length = builder.extract_value(yhgmp__fsn.shape, 0)
        vcb__wgxgs = context.make_array(types.Array(types.uint8, 1, 'C'))(
            context, builder, arr.null_bitmap)
        mufnf__ufumn = numba_to_c_type(ahz__epvq)
        cbvme__bnqr = cgutils.alloca_once_value(builder, lir.Constant(lir.
            IntType(32), mufnf__ufumn))
        if isinstance(arr_type, DecimalArrayType):
            jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [
                lir.IntType(64), lir.IntType(8).as_pointer(), lir.IntType(
                32), lir.IntType(8).as_pointer(), lir.IntType(8).as_pointer
                (), lir.IntType(8).as_pointer(), lir.IntType(32), lir.
                IntType(32)])
            sgt__jar = cgutils.get_or_insert_function(builder.module,
                jhakg__yvqke, name='decimal_array_to_info')
            return builder.call(sgt__jar, [length, builder.bitcast(
                yhgmp__fsn.data, lir.IntType(8).as_pointer()), builder.load
                (cbvme__bnqr), builder.bitcast(vcb__wgxgs.data, lir.IntType
                (8).as_pointer()), yhgmp__fsn.meminfo, vcb__wgxgs.meminfo,
                context.get_constant(types.int32, arr_type.precision),
                context.get_constant(types.int32, arr_type.scale)])
        elif isinstance(arr_type, TimeArrayType):
            jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [
                lir.IntType(64), lir.IntType(8).as_pointer(), lir.IntType(
                32), lir.IntType(8).as_pointer(), lir.IntType(8).as_pointer
                (), lir.IntType(8).as_pointer(), lir.IntType(32)])
            sgt__jar = cgutils.get_or_insert_function(builder.module,
                jhakg__yvqke, name='time_array_to_info')
            return builder.call(sgt__jar, [length, builder.bitcast(
                yhgmp__fsn.data, lir.IntType(8).as_pointer()), builder.load
                (cbvme__bnqr), builder.bitcast(vcb__wgxgs.data, lir.IntType
                (8).as_pointer()), yhgmp__fsn.meminfo, vcb__wgxgs.meminfo,
                lir.Constant(lir.IntType(32), arr_type.precision)])
        else:
            jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [
                lir.IntType(64), lir.IntType(8).as_pointer(), lir.IntType(
                32), lir.IntType(8).as_pointer(), lir.IntType(8).as_pointer
                (), lir.IntType(8).as_pointer()])
            sgt__jar = cgutils.get_or_insert_function(builder.module,
                jhakg__yvqke, name='nullable_array_to_info')
            return builder.call(sgt__jar, [length, builder.bitcast(
                yhgmp__fsn.data, lir.IntType(8).as_pointer()), builder.load
                (cbvme__bnqr), builder.bitcast(vcb__wgxgs.data, lir.IntType
                (8).as_pointer()), yhgmp__fsn.meminfo, vcb__wgxgs.meminfo])
    if isinstance(arr_type, IntervalArrayType):
        assert isinstance(arr_type.arr_type, types.Array
            ), 'array_to_info(): only IntervalArrayType with Numpy arrays supported'
        arr = cgutils.create_struct_proxy(arr_type)(context, builder, in_arr)
        gcv__yzeg = context.make_array(arr_type.arr_type)(context, builder,
            arr.left)
        srxzj__mqcn = context.make_array(arr_type.arr_type)(context,
            builder, arr.right)
        length = builder.extract_value(gcv__yzeg.shape, 0)
        mufnf__ufumn = numba_to_c_type(arr_type.arr_type.dtype)
        cbvme__bnqr = cgutils.alloca_once_value(builder, lir.Constant(lir.
            IntType(32), mufnf__ufumn))
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(64), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(32), lir.IntType(8).as_pointer(), lir
            .IntType(8).as_pointer()])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='interval_array_to_info')
        return builder.call(sgt__jar, [length, builder.bitcast(gcv__yzeg.
            data, lir.IntType(8).as_pointer()), builder.bitcast(srxzj__mqcn
            .data, lir.IntType(8).as_pointer()), builder.load(cbvme__bnqr),
            gcv__yzeg.meminfo, srxzj__mqcn.meminfo])
    raise_bodo_error(f'array_to_info(): array type {arr_type} is not supported'
        )


def _lower_info_to_array_numpy(arr_type, context, builder, in_info):
    assert arr_type.ndim == 1, 'only 1D array supported'
    arr = context.make_array(arr_type)(context, builder)
    ltdd__sfn = cgutils.alloca_once(builder, lir.IntType(64))
    yci__xjpy = cgutils.alloca_once(builder, lir.IntType(8).as_pointer())
    hdylv__ysst = cgutils.alloca_once(builder, lir.IntType(8).as_pointer())
    jhakg__yvqke = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
        as_pointer(), lir.IntType(64).as_pointer(), lir.IntType(8).
        as_pointer().as_pointer(), lir.IntType(8).as_pointer().as_pointer()])
    sgt__jar = cgutils.get_or_insert_function(builder.module, jhakg__yvqke,
        name='info_to_numpy_array')
    builder.call(sgt__jar, [in_info, ltdd__sfn, yci__xjpy, hdylv__ysst])
    context.compile_internal(builder, lambda :
        check_and_propagate_cpp_exception(), types.none(), [])
    aukd__ued = context.get_value_type(types.intp)
    xcy__xjswi = cgutils.pack_array(builder, [builder.load(ltdd__sfn)], ty=
        aukd__ued)
    evi__xncp = context.get_constant(types.intp, context.get_abi_sizeof(
        context.get_data_type(arr_type.dtype)))
    zpi__kplc = cgutils.pack_array(builder, [evi__xncp], ty=aukd__ued)
    data = builder.bitcast(builder.load(yci__xjpy), context.get_data_type(
        arr_type.dtype).as_pointer())
    numba.np.arrayobj.populate_array(arr, data=data, shape=xcy__xjswi,
        strides=zpi__kplc, itemsize=evi__xncp, meminfo=builder.load(
        hdylv__ysst))
    return arr._getvalue()


def _lower_info_to_array_list_string_array(arr_type, context, builder, in_info
    ):
    aqd__kqauz = context.make_helper(builder, arr_type)
    jhakg__yvqke = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
        as_pointer(), lir.IntType(8).as_pointer().as_pointer()])
    sgt__jar = cgutils.get_or_insert_function(builder.module, jhakg__yvqke,
        name='info_to_list_string_array')
    builder.call(sgt__jar, [in_info, aqd__kqauz._get_ptr_by_name('meminfo')])
    context.compile_internal(builder, lambda :
        check_and_propagate_cpp_exception(), types.none(), [])
    return aqd__kqauz._getvalue()


def nested_to_array(context, builder, arr_typ, lengths_ptr, array_infos_ptr,
    lengths_pos, infos_pos):
    rzod__lbh = context.get_data_type(array_info_type)
    if isinstance(arr_typ, ArrayItemArrayType):
        bqy__wbl = lengths_pos
        fxxe__dfagr = infos_pos
        ruej__avwlk, lengths_pos, infos_pos = nested_to_array(context,
            builder, arr_typ.dtype, lengths_ptr, array_infos_ptr, 
            lengths_pos + 1, infos_pos + 2)
        fsnwq__vjt = ArrayItemArrayPayloadType(arr_typ)
        mppp__pqrwj = context.get_data_type(fsnwq__vjt)
        qigw__nkqx = context.get_abi_sizeof(mppp__pqrwj)
        qqdgx__dso = define_array_item_dtor(context, builder, arr_typ,
            fsnwq__vjt)
        lxw__aoye = context.nrt.meminfo_alloc_dtor(builder, context.
            get_constant(types.uintp, qigw__nkqx), qqdgx__dso)
        fwcm__ril = context.nrt.meminfo_data(builder, lxw__aoye)
        aubk__kgp = builder.bitcast(fwcm__ril, mppp__pqrwj.as_pointer())
        rivfm__bbi = cgutils.create_struct_proxy(fsnwq__vjt)(context, builder)
        rivfm__bbi.n_arrays = builder.extract_value(builder.load(
            lengths_ptr), bqy__wbl)
        rivfm__bbi.data = ruej__avwlk
        wyr__nxmob = builder.load(array_infos_ptr)
        mwnos__allb = builder.bitcast(builder.extract_value(wyr__nxmob,
            fxxe__dfagr), rzod__lbh)
        rivfm__bbi.offsets = _lower_info_to_array_numpy(types.Array(
            offset_type, 1, 'C'), context, builder, mwnos__allb)
        uut__iaee = builder.bitcast(builder.extract_value(wyr__nxmob, 
            fxxe__dfagr + 1), rzod__lbh)
        rivfm__bbi.null_bitmap = _lower_info_to_array_numpy(types.Array(
            types.uint8, 1, 'C'), context, builder, uut__iaee)
        builder.store(rivfm__bbi._getvalue(), aubk__kgp)
        wos__zzgt = context.make_helper(builder, arr_typ)
        wos__zzgt.meminfo = lxw__aoye
        return wos__zzgt._getvalue(), lengths_pos, infos_pos
    elif isinstance(arr_typ, StructArrayType):
        lbypg__ohzc = []
        fxxe__dfagr = infos_pos
        lengths_pos += 1
        infos_pos += 1
        for modp__iecqh in arr_typ.data:
            ruej__avwlk, lengths_pos, infos_pos = nested_to_array(context,
                builder, modp__iecqh, lengths_ptr, array_infos_ptr,
                lengths_pos, infos_pos)
            lbypg__ohzc.append(ruej__avwlk)
        fsnwq__vjt = StructArrayPayloadType(arr_typ.data)
        mppp__pqrwj = context.get_value_type(fsnwq__vjt)
        qigw__nkqx = context.get_abi_sizeof(mppp__pqrwj)
        qqdgx__dso = define_struct_arr_dtor(context, builder, arr_typ,
            fsnwq__vjt)
        lxw__aoye = context.nrt.meminfo_alloc_dtor(builder, context.
            get_constant(types.uintp, qigw__nkqx), qqdgx__dso)
        fwcm__ril = context.nrt.meminfo_data(builder, lxw__aoye)
        aubk__kgp = builder.bitcast(fwcm__ril, mppp__pqrwj.as_pointer())
        rivfm__bbi = cgutils.create_struct_proxy(fsnwq__vjt)(context, builder)
        rivfm__bbi.data = cgutils.pack_array(builder, lbypg__ohzc
            ) if types.is_homogeneous(*arr_typ.data) else cgutils.pack_struct(
            builder, lbypg__ohzc)
        wyr__nxmob = builder.load(array_infos_ptr)
        uut__iaee = builder.bitcast(builder.extract_value(wyr__nxmob,
            fxxe__dfagr), rzod__lbh)
        rivfm__bbi.null_bitmap = _lower_info_to_array_numpy(types.Array(
            types.uint8, 1, 'C'), context, builder, uut__iaee)
        builder.store(rivfm__bbi._getvalue(), aubk__kgp)
        ovyxb__sscb = context.make_helper(builder, arr_typ)
        ovyxb__sscb.meminfo = lxw__aoye
        return ovyxb__sscb._getvalue(), lengths_pos, infos_pos
    elif arr_typ in (string_array_type, binary_array_type):
        wyr__nxmob = builder.load(array_infos_ptr)
        iaxyi__pkwd = builder.bitcast(builder.extract_value(wyr__nxmob,
            infos_pos), rzod__lbh)
        znt__dzlpm = context.make_helper(builder, arr_typ)
        weke__jmm = ArrayItemArrayType(char_arr_type)
        wos__zzgt = context.make_helper(builder, weke__jmm)
        jhakg__yvqke = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer().as_pointer()])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='info_to_string_array')
        builder.call(sgt__jar, [iaxyi__pkwd, wos__zzgt._get_ptr_by_name(
            'meminfo')])
        context.compile_internal(builder, lambda :
            check_and_propagate_cpp_exception(), types.none(), [])
        znt__dzlpm.data = wos__zzgt._getvalue()
        return znt__dzlpm._getvalue(), lengths_pos + 1, infos_pos + 1
    elif isinstance(arr_typ, types.Array):
        wyr__nxmob = builder.load(array_infos_ptr)
        fwse__fxjt = builder.bitcast(builder.extract_value(wyr__nxmob, 
            infos_pos + 1), rzod__lbh)
        return _lower_info_to_array_numpy(arr_typ, context, builder, fwse__fxjt
            ), lengths_pos + 1, infos_pos + 2
    elif isinstance(arr_typ, (IntegerArrayType, FloatingArrayType,
        DecimalArrayType)) or arr_typ in (boolean_array,
        datetime_date_array_type):
        arr = cgutils.create_struct_proxy(arr_typ)(context, builder)
        fbgd__scht = arr_typ.dtype
        if isinstance(arr_typ, DecimalArrayType):
            fbgd__scht = int128_type
        elif arr_typ == datetime_date_array_type:
            fbgd__scht = types.int64
        wyr__nxmob = builder.load(array_infos_ptr)
        uut__iaee = builder.bitcast(builder.extract_value(wyr__nxmob,
            infos_pos), rzod__lbh)
        arr.null_bitmap = _lower_info_to_array_numpy(types.Array(types.
            uint8, 1, 'C'), context, builder, uut__iaee)
        fwse__fxjt = builder.bitcast(builder.extract_value(wyr__nxmob, 
            infos_pos + 1), rzod__lbh)
        arr.data = _lower_info_to_array_numpy(types.Array(fbgd__scht, 1,
            'C'), context, builder, fwse__fxjt)
        return arr._getvalue(), lengths_pos + 1, infos_pos + 2


def info_to_array_codegen(context, builder, sig, args):
    array_type = sig.args[1]
    arr_type = array_type.instance_type if isinstance(array_type, types.TypeRef
        ) else array_type
    in_info, omlcf__mgbfd = args
    if isinstance(arr_type, ArrayItemArrayType
        ) and arr_type.dtype == string_array_type:
        return _lower_info_to_array_list_string_array(arr_type, context,
            builder, in_info)
    if isinstance(arr_type, (MapArrayType, ArrayItemArrayType,
        StructArrayType, TupleArrayType)):

        def get_num_arrays(arr_typ):
            if isinstance(arr_typ, ArrayItemArrayType):
                return 1 + get_num_arrays(arr_typ.dtype)
            elif isinstance(arr_typ, StructArrayType):
                return 1 + sum([get_num_arrays(modp__iecqh) for modp__iecqh in
                    arr_typ.data])
            else:
                return 1

        def get_num_infos(arr_typ):
            if isinstance(arr_typ, ArrayItemArrayType):
                return 2 + get_num_infos(arr_typ.dtype)
            elif isinstance(arr_typ, StructArrayType):
                return 1 + sum([get_num_infos(modp__iecqh) for modp__iecqh in
                    arr_typ.data])
            elif arr_typ in (string_array_type, binary_array_type):
                return 1
            else:
                return 2
        if isinstance(arr_type, TupleArrayType):
            abczp__nnm = StructArrayType(arr_type.data, ('dummy',) * len(
                arr_type.data))
        elif isinstance(arr_type, MapArrayType):
            abczp__nnm = _get_map_arr_data_type(arr_type)
        else:
            abczp__nnm = arr_type
        eyid__aviq = get_num_arrays(abczp__nnm)
        ogveo__apu = cgutils.pack_array(builder, [lir.Constant(lir.IntType(
            64), 0) for omlcf__mgbfd in range(eyid__aviq)])
        lengths_ptr = cgutils.alloca_once_value(builder, ogveo__apu)
        dhhxv__zppdo = lir.Constant(lir.IntType(8).as_pointer(), None)
        dwvlx__rjv = cgutils.pack_array(builder, [dhhxv__zppdo for
            omlcf__mgbfd in range(get_num_infos(abczp__nnm))])
        array_infos_ptr = cgutils.alloca_once_value(builder, dwvlx__rjv)
        jhakg__yvqke = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
            as_pointer(), lir.IntType(64).as_pointer(), lir.IntType(8).
            as_pointer().as_pointer()])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='info_to_nested_array')
        builder.call(sgt__jar, [in_info, builder.bitcast(lengths_ptr, lir.
            IntType(64).as_pointer()), builder.bitcast(array_infos_ptr, lir
            .IntType(8).as_pointer().as_pointer())])
        context.compile_internal(builder, lambda :
            check_and_propagate_cpp_exception(), types.none(), [])
        arr, omlcf__mgbfd, omlcf__mgbfd = nested_to_array(context, builder,
            abczp__nnm, lengths_ptr, array_infos_ptr, 0, 0)
        if isinstance(arr_type, TupleArrayType):
            xklis__cdos = context.make_helper(builder, arr_type)
            xklis__cdos.data = arr
            context.nrt.incref(builder, abczp__nnm, arr)
            arr = xklis__cdos._getvalue()
        elif isinstance(arr_type, MapArrayType):
            sig = signature(arr_type, abczp__nnm)
            arr = init_map_arr_codegen(context, builder, sig, (arr,))
        return arr
    if arr_type in (string_array_type, binary_array_type):
        znt__dzlpm = context.make_helper(builder, arr_type)
        weke__jmm = ArrayItemArrayType(char_arr_type)
        wos__zzgt = context.make_helper(builder, weke__jmm)
        jhakg__yvqke = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer().as_pointer()])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='info_to_string_array')
        builder.call(sgt__jar, [in_info, wos__zzgt._get_ptr_by_name('meminfo')]
            )
        context.compile_internal(builder, lambda :
            check_and_propagate_cpp_exception(), types.none(), [])
        znt__dzlpm.data = wos__zzgt._getvalue()
        return znt__dzlpm._getvalue()
    if arr_type == bodo.dict_str_arr_type:
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(32)])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='get_nested_info')
        bniei__wmwwc = builder.call(sgt__jar, [in_info, lir.Constant(lir.
            IntType(32), 1)])
        vva__yygao = builder.call(sgt__jar, [in_info, lir.Constant(lir.
            IntType(32), 2)])
        xzjue__xtljq = context.make_helper(builder, arr_type)
        sig = arr_type.data(array_info_type, arr_type.data)
        xzjue__xtljq.data = info_to_array_codegen(context, builder, sig, (
            bniei__wmwwc, context.get_constant_null(arr_type.data)))
        rhsv__hbn = bodo.libs.dict_arr_ext.dict_indices_arr_type
        sig = rhsv__hbn(array_info_type, rhsv__hbn)
        xzjue__xtljq.indices = info_to_array_codegen(context, builder, sig,
            (vva__yygao, context.get_constant_null(rhsv__hbn)))
        jhakg__yvqke = lir.FunctionType(lir.IntType(32), [lir.IntType(8).
            as_pointer()])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='get_has_global_dictionary')
        ain__qld = builder.call(sgt__jar, [in_info])
        xzjue__xtljq.has_global_dictionary = builder.trunc(ain__qld,
            cgutils.bool_t)
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='get_has_deduped_local_dictionary')
        citww__jxrja = builder.call(sgt__jar, [in_info])
        xzjue__xtljq.has_deduped_local_dictionary = builder.trunc(citww__jxrja,
            cgutils.bool_t)
        return xzjue__xtljq._getvalue()
    if isinstance(arr_type, CategoricalArrayType):
        out_arr = cgutils.create_struct_proxy(arr_type)(context, builder)
        hzbyy__krou = get_categories_int_type(arr_type.dtype)
        bfbqj__qhxg = types.Array(hzbyy__krou, 1, 'C')
        out_arr.codes = _lower_info_to_array_numpy(bfbqj__qhxg, context,
            builder, in_info)
        if isinstance(array_type, types.TypeRef):
            assert arr_type.dtype.categories is not None, 'info_to_array: unknown categories'
            is_ordered = arr_type.dtype.ordered
            cyw__knyr = bodo.utils.utils.create_categorical_type(arr_type.
                dtype.categories, arr_type.dtype.data.data, is_ordered)
            new_cats_tup = MetaType(tuple(cyw__knyr))
            int_type = arr_type.dtype.int_type
            cogfi__kwr = arr_type.dtype.data.data
            tnqd__klp = context.get_constant_generic(builder, cogfi__kwr,
                cyw__knyr)
            ahz__epvq = context.compile_internal(builder, lambda c_arr:
                bodo.hiframes.pd_categorical_ext.init_cat_dtype(bodo.utils.
                conversion.index_from_array(c_arr), is_ordered, int_type,
                new_cats_tup), arr_type.dtype(cogfi__kwr), [tnqd__klp])
        else:
            ahz__epvq = cgutils.create_struct_proxy(arr_type)(context,
                builder, args[1]).dtype
            context.nrt.incref(builder, arr_type.dtype, ahz__epvq)
        out_arr.dtype = ahz__epvq
        return out_arr._getvalue()
    if isinstance(arr_type, bodo.DatetimeArrayType):
        arr = cgutils.create_struct_proxy(arr_type)(context, builder)
        data = _lower_info_to_array_numpy(arr_type.data_array_type, context,
            builder, in_info)
        arr.data = data
        return arr._getvalue()
    if isinstance(arr_type, types.Array):
        return _lower_info_to_array_numpy(arr_type, context, builder, in_info)
    if isinstance(arr_type, (IntegerArrayType, FloatingArrayType,
        DecimalArrayType, TimeArrayType)) or arr_type in (boolean_array,
        datetime_date_array_type):
        arr = cgutils.create_struct_proxy(arr_type)(context, builder)
        fbgd__scht = arr_type.dtype
        if isinstance(arr_type, DecimalArrayType):
            fbgd__scht = int128_type
        elif arr_type == datetime_date_array_type:
            fbgd__scht = types.int64
        jxd__ghxiy = types.Array(fbgd__scht, 1, 'C')
        yhgmp__fsn = context.make_array(jxd__ghxiy)(context, builder)
        nyii__ioegr = types.Array(types.uint8, 1, 'C')
        anm__qma = context.make_array(nyii__ioegr)(context, builder)
        ltdd__sfn = cgutils.alloca_once(builder, lir.IntType(64))
        gwaq__rtro = cgutils.alloca_once(builder, lir.IntType(64))
        yci__xjpy = cgutils.alloca_once(builder, lir.IntType(8).as_pointer())
        rlq__rpis = cgutils.alloca_once(builder, lir.IntType(8).as_pointer())
        hdylv__ysst = cgutils.alloca_once(builder, lir.IntType(8).as_pointer())
        gwxsy__tijgx = cgutils.alloca_once(builder, lir.IntType(8).as_pointer()
            )
        jhakg__yvqke = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
            as_pointer(), lir.IntType(64).as_pointer(), lir.IntType(64).
            as_pointer(), lir.IntType(8).as_pointer().as_pointer(), lir.
            IntType(8).as_pointer().as_pointer(), lir.IntType(8).as_pointer
            ().as_pointer(), lir.IntType(8).as_pointer().as_pointer()])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='info_to_nullable_array')
        builder.call(sgt__jar, [in_info, ltdd__sfn, gwaq__rtro, yci__xjpy,
            rlq__rpis, hdylv__ysst, gwxsy__tijgx])
        context.compile_internal(builder, lambda :
            check_and_propagate_cpp_exception(), types.none(), [])
        aukd__ued = context.get_value_type(types.intp)
        xcy__xjswi = cgutils.pack_array(builder, [builder.load(ltdd__sfn)],
            ty=aukd__ued)
        evi__xncp = context.get_constant(types.intp, context.get_abi_sizeof
            (context.get_data_type(fbgd__scht)))
        zpi__kplc = cgutils.pack_array(builder, [evi__xncp], ty=aukd__ued)
        data = builder.bitcast(builder.load(yci__xjpy), context.
            get_data_type(fbgd__scht).as_pointer())
        numba.np.arrayobj.populate_array(yhgmp__fsn, data=data, shape=
            xcy__xjswi, strides=zpi__kplc, itemsize=evi__xncp, meminfo=
            builder.load(hdylv__ysst))
        arr.data = yhgmp__fsn._getvalue()
        xcy__xjswi = cgutils.pack_array(builder, [builder.load(gwaq__rtro)],
            ty=aukd__ued)
        evi__xncp = context.get_constant(types.intp, context.get_abi_sizeof
            (context.get_data_type(types.uint8)))
        zpi__kplc = cgutils.pack_array(builder, [evi__xncp], ty=aukd__ued)
        data = builder.bitcast(builder.load(rlq__rpis), context.
            get_data_type(types.uint8).as_pointer())
        numba.np.arrayobj.populate_array(anm__qma, data=data, shape=
            xcy__xjswi, strides=zpi__kplc, itemsize=evi__xncp, meminfo=
            builder.load(gwxsy__tijgx))
        arr.null_bitmap = anm__qma._getvalue()
        return arr._getvalue()
    if isinstance(arr_type, IntervalArrayType):
        arr = cgutils.create_struct_proxy(arr_type)(context, builder)
        gcv__yzeg = context.make_array(arr_type.arr_type)(context, builder)
        srxzj__mqcn = context.make_array(arr_type.arr_type)(context, builder)
        ltdd__sfn = cgutils.alloca_once(builder, lir.IntType(64))
        sbkr__qsul = cgutils.alloca_once(builder, lir.IntType(8).as_pointer())
        koza__mml = cgutils.alloca_once(builder, lir.IntType(8).as_pointer())
        hhyu__jbz = cgutils.alloca_once(builder, lir.IntType(8).as_pointer())
        sailh__wtjgh = cgutils.alloca_once(builder, lir.IntType(8).as_pointer()
            )
        jhakg__yvqke = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
            as_pointer(), lir.IntType(64).as_pointer(), lir.IntType(8).
            as_pointer().as_pointer(), lir.IntType(8).as_pointer().
            as_pointer(), lir.IntType(8).as_pointer().as_pointer(), lir.
            IntType(8).as_pointer().as_pointer()])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='info_to_interval_array')
        builder.call(sgt__jar, [in_info, ltdd__sfn, sbkr__qsul, koza__mml,
            hhyu__jbz, sailh__wtjgh])
        context.compile_internal(builder, lambda :
            check_and_propagate_cpp_exception(), types.none(), [])
        aukd__ued = context.get_value_type(types.intp)
        xcy__xjswi = cgutils.pack_array(builder, [builder.load(ltdd__sfn)],
            ty=aukd__ued)
        evi__xncp = context.get_constant(types.intp, context.get_abi_sizeof
            (context.get_data_type(arr_type.arr_type.dtype)))
        zpi__kplc = cgutils.pack_array(builder, [evi__xncp], ty=aukd__ued)
        nyqzy__yfe = builder.bitcast(builder.load(sbkr__qsul), context.
            get_data_type(arr_type.arr_type.dtype).as_pointer())
        numba.np.arrayobj.populate_array(gcv__yzeg, data=nyqzy__yfe, shape=
            xcy__xjswi, strides=zpi__kplc, itemsize=evi__xncp, meminfo=
            builder.load(hhyu__jbz))
        arr.left = gcv__yzeg._getvalue()
        upo__stka = builder.bitcast(builder.load(koza__mml), context.
            get_data_type(arr_type.arr_type.dtype).as_pointer())
        numba.np.arrayobj.populate_array(srxzj__mqcn, data=upo__stka, shape
            =xcy__xjswi, strides=zpi__kplc, itemsize=evi__xncp, meminfo=
            builder.load(sailh__wtjgh))
        arr.right = srxzj__mqcn._getvalue()
        return arr._getvalue()
    raise_bodo_error(f'info_to_array(): array type {arr_type} is not supported'
        )


@intrinsic
def info_to_array(typingctx, info_type, array_type):
    arr_type = array_type.instance_type if isinstance(array_type, types.TypeRef
        ) else array_type
    assert info_type == array_info_type, 'info_to_array: expected info type'
    return arr_type(info_type, array_type), info_to_array_codegen


@intrinsic
def test_alloc_np(typingctx, len_typ, arr_type):
    array_type = arr_type.instance_type if isinstance(arr_type, types.TypeRef
        ) else arr_type

    def codegen(context, builder, sig, args):
        length, omlcf__mgbfd = args
        mufnf__ufumn = numba_to_c_type(array_type.dtype)
        cbvme__bnqr = cgutils.alloca_once_value(builder, lir.Constant(lir.
            IntType(32), mufnf__ufumn))
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(64), lir.IntType(32)])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='alloc_numpy')
        return builder.call(sgt__jar, [length, builder.load(cbvme__bnqr)])
    return array_info_type(len_typ, arr_type), codegen


@intrinsic
def test_alloc_string(typingctx, len_typ, n_chars_typ):

    def codegen(context, builder, sig, args):
        length, fpgag__wxrw = args
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(64), lir.IntType(64)])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='alloc_string_array')
        return builder.call(sgt__jar, [length, fpgag__wxrw])
    return array_info_type(len_typ, n_chars_typ), codegen


@intrinsic
def arr_info_list_to_table(typingctx, list_arr_info_typ=None):
    assert list_arr_info_typ == types.List(array_info_type)
    return table_type(list_arr_info_typ), arr_info_list_to_table_codegen


def arr_info_list_to_table_codegen(context, builder, sig, args):
    qluzb__vwag, = args
    qpsa__tszp = numba.cpython.listobj.ListInstance(context, builder, sig.
        args[0], qluzb__vwag)
    jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
        IntType(8).as_pointer().as_pointer(), lir.IntType(64)])
    sgt__jar = cgutils.get_or_insert_function(builder.module, jhakg__yvqke,
        name='arr_info_list_to_table')
    return builder.call(sgt__jar, [qpsa__tszp.data, qpsa__tszp.size])


@intrinsic
def info_from_table(typingctx, table_t, ind_t):

    def codegen(context, builder, sig, args):
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(64)])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='info_from_table')
        return builder.call(sgt__jar, args)
    return array_info_type(table_t, ind_t), codegen


@intrinsic
def cpp_table_to_py_table(typingctx, cpp_table_t, table_idx_arr_t,
    py_table_type_t):
    assert cpp_table_t == table_type, 'invalid cpp table type'
    assert isinstance(table_idx_arr_t, types.Array
        ) and table_idx_arr_t.dtype == types.int64, 'invalid table index array'
    assert isinstance(py_table_type_t, types.TypeRef), 'invalid py table ref'
    theoo__nkgx = py_table_type_t.instance_type

    def codegen(context, builder, sig, args):
        cpp_table, unsoa__tajja, omlcf__mgbfd = args
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(64)])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='info_from_table')
        bwot__brxca = cgutils.create_struct_proxy(theoo__nkgx)(context, builder
            )
        bwot__brxca.parent = cgutils.get_null_value(bwot__brxca.parent.type)
        wjvsf__woyp = context.make_array(table_idx_arr_t)(context, builder,
            unsoa__tajja)
        mmclk__ofow = context.get_constant(types.int64, -1)
        ewul__ydkt = context.get_constant(types.int64, 0)
        bkcr__zrz = cgutils.alloca_once_value(builder, ewul__ydkt)
        for t, rnxj__xiali in theoo__nkgx.type_to_blk.items():
            kloi__wcnrp = context.get_constant(types.int64, len(theoo__nkgx
                .block_to_arr_ind[rnxj__xiali]))
            omlcf__mgbfd, ydh__xsfpk = ListInstance.allocate_ex(context,
                builder, types.List(t), kloi__wcnrp)
            ydh__xsfpk.size = kloi__wcnrp
            csu__fqxm = context.make_constant_array(builder, types.Array(
                types.int64, 1, 'C'), np.array(theoo__nkgx.block_to_arr_ind
                [rnxj__xiali], dtype=np.int64))
            cvsgs__czbl = context.make_array(types.Array(types.int64, 1, 'C'))(
                context, builder, csu__fqxm)
            with cgutils.for_range(builder, kloi__wcnrp) as mpiyu__cgiiz:
                yeh__satbe = mpiyu__cgiiz.index
                qjva__jhi = _getitem_array_single_int(context, builder,
                    types.int64, types.Array(types.int64, 1, 'C'),
                    cvsgs__czbl, yeh__satbe)
                cylgk__tnin = _getitem_array_single_int(context, builder,
                    types.int64, table_idx_arr_t, wjvsf__woyp, qjva__jhi)
                rfat__vmgtq = builder.icmp_unsigned('!=', cylgk__tnin,
                    mmclk__ofow)
                with builder.if_else(rfat__vmgtq) as (mkk__ere, qyvl__snzc):
                    with mkk__ere:
                        nteh__lwig = builder.call(sgt__jar, [cpp_table,
                            cylgk__tnin])
                        arr = context.compile_internal(builder, lambda info:
                            info_to_array(info, t), t(array_info_type), [
                            nteh__lwig])
                        ydh__xsfpk.inititem(yeh__satbe, arr, incref=False)
                        length = context.compile_internal(builder, lambda
                            arr: len(arr), types.int64(t), [arr])
                        builder.store(length, bkcr__zrz)
                    with qyvl__snzc:
                        zkip__fslp = context.get_constant_null(t)
                        ydh__xsfpk.inititem(yeh__satbe, zkip__fslp, incref=
                            False)
            setattr(bwot__brxca, f'block_{rnxj__xiali}', ydh__xsfpk.value)
        bwot__brxca.len = builder.load(bkcr__zrz)
        return bwot__brxca._getvalue()
    return theoo__nkgx(cpp_table_t, table_idx_arr_t, py_table_type_t), codegen


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def cpp_table_to_py_data(cpp_table, out_col_inds_t, out_types_t, n_rows_t,
    n_table_cols_t, unknown_cat_arrs_t=None, cat_inds_t=None):
    tepr__xvuzc = out_col_inds_t.instance_type.meta
    theoo__nkgx = unwrap_typeref(out_types_t.types[0])
    ejp__dmylm = [unwrap_typeref(out_types_t.types[yeh__satbe]) for
        yeh__satbe in range(1, len(out_types_t.types))]
    flzs__waauj = {}
    omp__cuav = get_overload_const_int(n_table_cols_t)
    zfh__mpjle = {sxmy__phnzi: yeh__satbe for yeh__satbe, sxmy__phnzi in
        enumerate(tepr__xvuzc)}
    if not is_overload_none(unknown_cat_arrs_t):
        wzcvw__aorky = {abfuv__twha: yeh__satbe for yeh__satbe, abfuv__twha in
            enumerate(cat_inds_t.instance_type.meta)}
    vkcv__jmuij = []
    cxqc__lmw = """def impl(cpp_table, out_col_inds_t, out_types_t, n_rows_t, n_table_cols_t, unknown_cat_arrs_t=None, cat_inds_t=None):
"""
    if isinstance(theoo__nkgx, bodo.TableType):
        cxqc__lmw += f'  py_table = init_table(py_table_type, False)\n'
        cxqc__lmw += f'  py_table = set_table_len(py_table, n_rows_t)\n'
        for tohe__buuw, rnxj__xiali in theoo__nkgx.type_to_blk.items():
            ivimr__yrr = [zfh__mpjle.get(yeh__satbe, -1) for yeh__satbe in
                theoo__nkgx.block_to_arr_ind[rnxj__xiali]]
            flzs__waauj[f'out_inds_{rnxj__xiali}'] = np.array(ivimr__yrr,
                np.int64)
            flzs__waauj[f'out_type_{rnxj__xiali}'] = tohe__buuw
            flzs__waauj[f'typ_list_{rnxj__xiali}'] = types.List(tohe__buuw)
            oevny__tgge = f'out_type_{rnxj__xiali}'
            if type_has_unknown_cats(tohe__buuw):
                if is_overload_none(unknown_cat_arrs_t):
                    cxqc__lmw += f"""  in_arr_list_{rnxj__xiali} = get_table_block(out_types_t[0], {rnxj__xiali})
"""
                    oevny__tgge = f'in_arr_list_{rnxj__xiali}[i]'
                else:
                    flzs__waauj[f'cat_arr_inds_{rnxj__xiali}'] = np.array([
                        wzcvw__aorky.get(yeh__satbe, -1) for yeh__satbe in
                        theoo__nkgx.block_to_arr_ind[rnxj__xiali]], np.int64)
                    oevny__tgge = (
                        f'unknown_cat_arrs_t[cat_arr_inds_{rnxj__xiali}[i]]')
            kloi__wcnrp = len(theoo__nkgx.block_to_arr_ind[rnxj__xiali])
            cxqc__lmw += f"""  arr_list_{rnxj__xiali} = alloc_list_like(typ_list_{rnxj__xiali}, {kloi__wcnrp}, False)
"""
            cxqc__lmw += f'  for i in range(len(arr_list_{rnxj__xiali})):\n'
            cxqc__lmw += (
                f'    cpp_ind_{rnxj__xiali} = out_inds_{rnxj__xiali}[i]\n')
            cxqc__lmw += f'    if cpp_ind_{rnxj__xiali} == -1:\n'
            cxqc__lmw += f'      continue\n'
            cxqc__lmw += f"""    arr_{rnxj__xiali} = info_to_array(info_from_table(cpp_table, cpp_ind_{rnxj__xiali}), {oevny__tgge})
"""
            cxqc__lmw += f'    arr_list_{rnxj__xiali}[i] = arr_{rnxj__xiali}\n'
            cxqc__lmw += f"""  py_table = set_table_block(py_table, arr_list_{rnxj__xiali}, {rnxj__xiali})
"""
        vkcv__jmuij.append('py_table')
    elif theoo__nkgx != types.none:
        glknf__uoozn = zfh__mpjle.get(0, -1)
        if glknf__uoozn != -1:
            flzs__waauj[f'arr_typ_arg0'] = theoo__nkgx
            oevny__tgge = f'arr_typ_arg0'
            if type_has_unknown_cats(theoo__nkgx):
                if is_overload_none(unknown_cat_arrs_t):
                    oevny__tgge = f'out_types_t[0]'
                else:
                    oevny__tgge = f'unknown_cat_arrs_t[{wzcvw__aorky[0]}]'
            cxqc__lmw += f"""  out_arg0 = info_to_array(info_from_table(cpp_table, {glknf__uoozn}), {oevny__tgge})
"""
            vkcv__jmuij.append('out_arg0')
    for yeh__satbe, t in enumerate(ejp__dmylm):
        glknf__uoozn = zfh__mpjle.get(omp__cuav + yeh__satbe, -1)
        if glknf__uoozn != -1:
            flzs__waauj[f'extra_arr_type_{yeh__satbe}'] = t
            oevny__tgge = f'extra_arr_type_{yeh__satbe}'
            if type_has_unknown_cats(t):
                if is_overload_none(unknown_cat_arrs_t):
                    oevny__tgge = f'out_types_t[{yeh__satbe + 1}]'
                else:
                    oevny__tgge = (
                        f'unknown_cat_arrs_t[{wzcvw__aorky[omp__cuav + yeh__satbe]}]'
                        )
            cxqc__lmw += f"""  out_{yeh__satbe} = info_to_array(info_from_table(cpp_table, {glknf__uoozn}), {oevny__tgge})
"""
            vkcv__jmuij.append(f'out_{yeh__satbe}')
    zlt__npr = ',' if len(vkcv__jmuij) == 1 else ''
    cxqc__lmw += f"  return ({', '.join(vkcv__jmuij)}{zlt__npr})\n"
    flzs__waauj.update({'init_table': bodo.hiframes.table.init_table,
        'alloc_list_like': bodo.hiframes.table.alloc_list_like,
        'set_table_block': bodo.hiframes.table.set_table_block,
        'set_table_len': bodo.hiframes.table.set_table_len,
        'get_table_block': bodo.hiframes.table.get_table_block,
        'info_to_array': info_to_array, 'info_from_table': info_from_table,
        'out_col_inds': list(tepr__xvuzc), 'py_table_type': theoo__nkgx})
    aevbi__fur = {}
    exec(cxqc__lmw, flzs__waauj, aevbi__fur)
    return aevbi__fur['impl']


@intrinsic
def py_table_to_cpp_table(typingctx, py_table_t, py_table_type_t):
    assert isinstance(py_table_t, bodo.hiframes.table.TableType
        ), 'invalid py table type'
    assert isinstance(py_table_type_t, types.TypeRef), 'invalid py table ref'
    theoo__nkgx = py_table_type_t.instance_type

    def codegen(context, builder, sig, args):
        py_table, omlcf__mgbfd = args
        ifokv__vsx = cgutils.create_struct_proxy(theoo__nkgx)(context,
            builder, py_table)
        if theoo__nkgx.has_runtime_cols:
            gxz__rmk = lir.Constant(lir.IntType(64), 0)
            for rnxj__xiali, t in enumerate(theoo__nkgx.arr_types):
                zxprf__paqww = getattr(ifokv__vsx, f'block_{rnxj__xiali}')
                rio__yasuy = ListInstance(context, builder, types.List(t),
                    zxprf__paqww)
                gxz__rmk = builder.add(gxz__rmk, rio__yasuy.size)
        else:
            gxz__rmk = lir.Constant(lir.IntType(64), len(theoo__nkgx.arr_types)
                )
        omlcf__mgbfd, lpzeh__tlo = ListInstance.allocate_ex(context,
            builder, types.List(array_info_type), gxz__rmk)
        lpzeh__tlo.size = gxz__rmk
        if theoo__nkgx.has_runtime_cols:
            evvj__zpn = lir.Constant(lir.IntType(64), 0)
            for rnxj__xiali, t in enumerate(theoo__nkgx.arr_types):
                zxprf__paqww = getattr(ifokv__vsx, f'block_{rnxj__xiali}')
                rio__yasuy = ListInstance(context, builder, types.List(t),
                    zxprf__paqww)
                kloi__wcnrp = rio__yasuy.size
                with cgutils.for_range(builder, kloi__wcnrp) as mpiyu__cgiiz:
                    yeh__satbe = mpiyu__cgiiz.index
                    arr = rio__yasuy.getitem(yeh__satbe)
                    qbf__drrgj = signature(array_info_type, t)
                    hch__zhq = arr,
                    emdxs__dtxw = array_to_info_codegen(context, builder,
                        qbf__drrgj, hch__zhq)
                    lpzeh__tlo.inititem(builder.add(evvj__zpn, yeh__satbe),
                        emdxs__dtxw, incref=False)
                evvj__zpn = builder.add(evvj__zpn, kloi__wcnrp)
        else:
            for t, rnxj__xiali in theoo__nkgx.type_to_blk.items():
                kloi__wcnrp = context.get_constant(types.int64, len(
                    theoo__nkgx.block_to_arr_ind[rnxj__xiali]))
                zxprf__paqww = getattr(ifokv__vsx, f'block_{rnxj__xiali}')
                rio__yasuy = ListInstance(context, builder, types.List(t),
                    zxprf__paqww)
                csu__fqxm = context.make_constant_array(builder, types.
                    Array(types.int64, 1, 'C'), np.array(theoo__nkgx.
                    block_to_arr_ind[rnxj__xiali], dtype=np.int64))
                cvsgs__czbl = context.make_array(types.Array(types.int64, 1,
                    'C'))(context, builder, csu__fqxm)
                with cgutils.for_range(builder, kloi__wcnrp) as mpiyu__cgiiz:
                    yeh__satbe = mpiyu__cgiiz.index
                    qjva__jhi = _getitem_array_single_int(context, builder,
                        types.int64, types.Array(types.int64, 1, 'C'),
                        cvsgs__czbl, yeh__satbe)
                    wkygz__imfl = signature(types.none, theoo__nkgx, types.
                        List(t), types.int64, types.int64)
                    ooy__pbxn = py_table, zxprf__paqww, yeh__satbe, qjva__jhi
                    bodo.hiframes.table.ensure_column_unboxed_codegen(context,
                        builder, wkygz__imfl, ooy__pbxn)
                    arr = rio__yasuy.getitem(yeh__satbe)
                    qbf__drrgj = signature(array_info_type, t)
                    hch__zhq = arr,
                    emdxs__dtxw = array_to_info_codegen(context, builder,
                        qbf__drrgj, hch__zhq)
                    lpzeh__tlo.inititem(qjva__jhi, emdxs__dtxw, incref=False)
        jvah__pduc = lpzeh__tlo.value
        oyn__htxfs = signature(table_type, types.List(array_info_type))
        tyed__ijq = jvah__pduc,
        cpp_table = arr_info_list_to_table_codegen(context, builder,
            oyn__htxfs, tyed__ijq)
        context.nrt.decref(builder, types.List(array_info_type), jvah__pduc)
        return cpp_table
    return table_type(theoo__nkgx, py_table_type_t), codegen


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def py_data_to_cpp_table(py_table, extra_arrs_tup, in_col_inds_t,
    n_table_cols_t):
    muv__arvw = in_col_inds_t.instance_type.meta
    flzs__waauj = {}
    omp__cuav = get_overload_const_int(n_table_cols_t)
    nlgu__lbgrt = defaultdict(list)
    zfh__mpjle = {}
    for yeh__satbe, sxmy__phnzi in enumerate(muv__arvw):
        if sxmy__phnzi in zfh__mpjle:
            nlgu__lbgrt[sxmy__phnzi].append(yeh__satbe)
        else:
            zfh__mpjle[sxmy__phnzi] = yeh__satbe
    cxqc__lmw = (
        'def impl(py_table, extra_arrs_tup, in_col_inds_t, n_table_cols_t):\n')
    cxqc__lmw += (
        f'  cpp_arr_list = alloc_empty_list_type({len(muv__arvw)}, array_info_type)\n'
        )
    if py_table != types.none:
        for rnxj__xiali in py_table.type_to_blk.values():
            ivimr__yrr = [zfh__mpjle.get(yeh__satbe, -1) for yeh__satbe in
                py_table.block_to_arr_ind[rnxj__xiali]]
            flzs__waauj[f'out_inds_{rnxj__xiali}'] = np.array(ivimr__yrr,
                np.int64)
            flzs__waauj[f'arr_inds_{rnxj__xiali}'] = np.array(py_table.
                block_to_arr_ind[rnxj__xiali], np.int64)
            cxqc__lmw += (
                f'  arr_list_{rnxj__xiali} = get_table_block(py_table, {rnxj__xiali})\n'
                )
            cxqc__lmw += f'  for i in range(len(arr_list_{rnxj__xiali})):\n'
            cxqc__lmw += (
                f'    out_arr_ind_{rnxj__xiali} = out_inds_{rnxj__xiali}[i]\n')
            cxqc__lmw += f'    if out_arr_ind_{rnxj__xiali} == -1:\n'
            cxqc__lmw += f'      continue\n'
            cxqc__lmw += (
                f'    arr_ind_{rnxj__xiali} = arr_inds_{rnxj__xiali}[i]\n')
            cxqc__lmw += f"""    ensure_column_unboxed(py_table, arr_list_{rnxj__xiali}, i, arr_ind_{rnxj__xiali})
"""
            cxqc__lmw += f"""    cpp_arr_list[out_arr_ind_{rnxj__xiali}] = array_to_info(arr_list_{rnxj__xiali}[i])
"""
        for adq__jnnlr, atvzo__idwl in nlgu__lbgrt.items():
            if adq__jnnlr < omp__cuav:
                rnxj__xiali = py_table.block_nums[adq__jnnlr]
                jeed__rzs = py_table.block_offsets[adq__jnnlr]
                for glknf__uoozn in atvzo__idwl:
                    cxqc__lmw += f"""  cpp_arr_list[{glknf__uoozn}] = array_to_info(arr_list_{rnxj__xiali}[{jeed__rzs}])
"""
    for yeh__satbe in range(len(extra_arrs_tup)):
        yozha__fiiy = zfh__mpjle.get(omp__cuav + yeh__satbe, -1)
        if yozha__fiiy != -1:
            rnoe__ndgox = [yozha__fiiy] + nlgu__lbgrt.get(omp__cuav +
                yeh__satbe, [])
            for glknf__uoozn in rnoe__ndgox:
                cxqc__lmw += f"""  cpp_arr_list[{glknf__uoozn}] = array_to_info(extra_arrs_tup[{yeh__satbe}])
"""
    cxqc__lmw += f'  return arr_info_list_to_table(cpp_arr_list)\n'
    flzs__waauj.update({'array_info_type': array_info_type,
        'alloc_empty_list_type': bodo.hiframes.table.alloc_empty_list_type,
        'get_table_block': bodo.hiframes.table.get_table_block,
        'ensure_column_unboxed': bodo.hiframes.table.ensure_column_unboxed,
        'array_to_info': array_to_info, 'arr_info_list_to_table':
        arr_info_list_to_table})
    aevbi__fur = {}
    exec(cxqc__lmw, flzs__waauj, aevbi__fur)
    return aevbi__fur['impl']


delete_info_decref_array = types.ExternalFunction('delete_info_decref_array',
    types.void(array_info_type))
delete_table_decref_arrays = types.ExternalFunction(
    'delete_table_decref_arrays', types.void(table_type))
decref_table_array = types.ExternalFunction('decref_table_array', types.
    void(table_type, types.int32))


@intrinsic
def delete_table(typingctx, table_t=None):
    assert table_t == table_type

    def codegen(context, builder, sig, args):
        jhakg__yvqke = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
            as_pointer()])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='delete_table')
        builder.call(sgt__jar, args)
    return types.void(table_t), codegen


@intrinsic
def shuffle_table(typingctx, table_t, n_keys_t, _is_parallel, keep_comm_info_t
    ):
    assert table_t == table_type

    def codegen(context, builder, sig, args):
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(64), lir.IntType(1), lir.
            IntType(32)])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='shuffle_table')
        upm__xeqs = builder.call(sgt__jar, args)
        context.compile_internal(builder, lambda :
            check_and_propagate_cpp_exception(), types.none(), [])
        return upm__xeqs
    return table_type(table_t, types.int64, types.boolean, types.int32
        ), codegen


class ShuffleInfoType(types.Type):

    def __init__(self):
        super(ShuffleInfoType, self).__init__(name='ShuffleInfoType()')


shuffle_info_type = ShuffleInfoType()
register_model(ShuffleInfoType)(models.OpaqueModel)
get_shuffle_info = types.ExternalFunction('get_shuffle_info',
    shuffle_info_type(table_type))


@intrinsic
def delete_shuffle_info(typingctx, shuffle_info_t=None):

    def codegen(context, builder, sig, args):
        if sig.args[0] == types.none:
            return
        jhakg__yvqke = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
            as_pointer()])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='delete_shuffle_info')
        return builder.call(sgt__jar, args)
    return types.void(shuffle_info_t), codegen


@intrinsic
def reverse_shuffle_table(typingctx, table_t, shuffle_info_t=None):

    def codegen(context, builder, sig, args):
        if sig.args[-1] == types.none:
            return context.get_constant_null(table_type)
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(8).as_pointer()])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='reverse_shuffle_table')
        return builder.call(sgt__jar, args)
    return table_type(table_type, shuffle_info_t), codegen


@intrinsic
def get_null_shuffle_info(typingctx):

    def codegen(context, builder, sig, args):
        return context.get_constant_null(sig.return_type)
    return shuffle_info_type(), codegen


@intrinsic
def hash_join_table(typingctx, left_table_t, right_table_t, left_parallel_t,
    right_parallel_t, n_keys_t, n_data_left_t, n_data_right_t, same_vect_t,
    key_in_out_t, same_need_typechange_t, is_left_t, is_right_t, is_join_t,
    extra_data_col_t, indicator, _bodo_na_equal, cond_func, left_col_nums,
    left_col_nums_len, right_col_nums, right_col_nums_len, num_rows_ptr_t):
    assert left_table_t == table_type
    assert right_table_t == table_type

    def codegen(context, builder, sig, args):
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(8).as_pointer(), lir.
            IntType(1), lir.IntType(1), lir.IntType(64), lir.IntType(64),
            lir.IntType(64), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(1), lir.
            IntType(1), lir.IntType(1), lir.IntType(1), lir.IntType(1), lir
            .IntType(1), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(64), lir.IntType(8).as_pointer(), lir
            .IntType(64), lir.IntType(8).as_pointer()])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='hash_join_table')
        upm__xeqs = builder.call(sgt__jar, args)
        context.compile_internal(builder, lambda :
            check_and_propagate_cpp_exception(), types.none(), [])
        return upm__xeqs
    return table_type(left_table_t, right_table_t, types.boolean, types.
        boolean, types.int64, types.int64, types.int64, types.voidptr,
        types.voidptr, types.voidptr, types.boolean, types.boolean, types.
        boolean, types.boolean, types.boolean, types.boolean, types.voidptr,
        types.voidptr, types.int64, types.voidptr, types.int64, types.voidptr
        ), codegen


@intrinsic
def cross_join_table(typingctx, left_table_t, right_table_t,
    left_parallel_t, right_parallel_t, is_left_t, is_right_t,
    key_in_output_t, need_typechange_t, cond_func, left_col_nums,
    left_col_nums_len, right_col_nums, right_col_nums_len, num_rows_ptr_t):
    assert left_table_t == table_type, 'cross_join_table: cpp table type expected'
    assert right_table_t == table_type, 'cross_join_table: cpp table type expected'

    def codegen(context, builder, sig, args):
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(8).as_pointer(), lir.
            IntType(1), lir.IntType(1), lir.IntType(1), lir.IntType(1), lir
            .IntType(8).as_pointer(), lir.IntType(8).as_pointer(), lir.
            IntType(8).as_pointer(), lir.IntType(8).as_pointer(), lir.
            IntType(64), lir.IntType(8).as_pointer(), lir.IntType(64), lir.
            IntType(8).as_pointer()])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='cross_join_table')
        upm__xeqs = builder.call(sgt__jar, args)
        bodo.utils.utils.inlined_check_and_propagate_cpp_exception(context,
            builder)
        return upm__xeqs
    return table_type(left_table_t, right_table_t, types.boolean, types.
        boolean, types.boolean, types.boolean, types.voidptr, types.voidptr,
        types.voidptr, types.voidptr, types.int64, types.voidptr, types.
        int64, types.voidptr), codegen


@intrinsic
def sort_values_table(typingctx, table_t, n_keys_t, vect_ascending_t,
    na_position_b_t, dead_keys_t, n_rows_t, bounds_t, parallel_t):
    assert table_t == table_type, 'C++ table type expected'

    def codegen(context, builder, sig, args):
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(64), lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(1)])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='sort_values_table')
        upm__xeqs = builder.call(sgt__jar, args)
        context.compile_internal(builder, lambda :
            check_and_propagate_cpp_exception(), types.none(), [])
        return upm__xeqs
    return table_type(table_t, types.int64, types.voidptr, types.voidptr,
        types.voidptr, types.voidptr, types.voidptr, types.boolean), codegen


@intrinsic
def sample_table(typingctx, table_t, n_keys_t, frac_t, replace_t, parallel_t):
    assert table_t == table_type

    def codegen(context, builder, sig, args):
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(64), lir.DoubleType(), lir
            .IntType(1), lir.IntType(1)])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='sample_table')
        upm__xeqs = builder.call(sgt__jar, args)
        context.compile_internal(builder, lambda :
            check_and_propagate_cpp_exception(), types.none(), [])
        return upm__xeqs
    return table_type(table_t, types.int64, types.float64, types.boolean,
        types.boolean), codegen


@intrinsic
def shuffle_renormalization(typingctx, table_t, random_t, random_seed_t,
    is_parallel_t):
    assert table_t == table_type

    def codegen(context, builder, sig, args):
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(32), lir.IntType(64), lir.
            IntType(1)])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='shuffle_renormalization')
        upm__xeqs = builder.call(sgt__jar, args)
        context.compile_internal(builder, lambda :
            check_and_propagate_cpp_exception(), types.none(), [])
        return upm__xeqs
    return table_type(table_t, types.int32, types.int64, types.boolean
        ), codegen


@intrinsic
def shuffle_renormalization_group(typingctx, table_t, random_t,
    random_seed_t, is_parallel_t, num_ranks_t, ranks_t):
    assert table_t == table_type

    def codegen(context, builder, sig, args):
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(32), lir.IntType(64), lir.
            IntType(1), lir.IntType(64), lir.IntType(8).as_pointer()])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='shuffle_renormalization_group')
        upm__xeqs = builder.call(sgt__jar, args)
        context.compile_internal(builder, lambda :
            check_and_propagate_cpp_exception(), types.none(), [])
        return upm__xeqs
    return table_type(table_t, types.int32, types.int64, types.boolean,
        types.int64, types.voidptr), codegen


@intrinsic
def drop_duplicates_table(typingctx, table_t, parallel_t, nkey_t, keep_t,
    dropna, drop_local_first):
    assert table_t == table_type

    def codegen(context, builder, sig, args):
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(1), lir.IntType(64), lir.
            IntType(64), lir.IntType(1), lir.IntType(1)])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='drop_duplicates_table')
        upm__xeqs = builder.call(sgt__jar, args)
        context.compile_internal(builder, lambda :
            check_and_propagate_cpp_exception(), types.none(), [])
        return upm__xeqs
    return table_type(table_t, types.boolean, types.int64, types.int64,
        types.boolean, types.boolean), codegen


@intrinsic
def groupby_and_aggregate(typingctx, table_t, n_keys_t, input_has_index,
    ftypes, func_offsets, udf_n_redvars, is_parallel, skipdropna_t,
    shift_periods_t, transform_func, head_n, return_keys, return_index,
    dropna, update_cb, combine_cb, eval_cb, general_udfs_cb,
    udf_table_dummy_t, n_out_rows_t, n_shuffle_keys_t):
    assert table_t == table_type
    assert udf_table_dummy_t == table_type

    def codegen(context, builder, sig, args):
        jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(64), lir.IntType(1), lir.
            IntType(8).as_pointer(), lir.IntType(8).as_pointer(), lir.
            IntType(8).as_pointer(), lir.IntType(1), lir.IntType(1), lir.
            IntType(64), lir.IntType(64), lir.IntType(64), lir.IntType(1),
            lir.IntType(1), lir.IntType(1), lir.IntType(8).as_pointer(),
            lir.IntType(8).as_pointer(), lir.IntType(8).as_pointer(), lir.
            IntType(8).as_pointer(), lir.IntType(8).as_pointer(), lir.
            IntType(8).as_pointer(), lir.IntType(64)])
        sgt__jar = cgutils.get_or_insert_function(builder.module,
            jhakg__yvqke, name='groupby_and_aggregate')
        upm__xeqs = builder.call(sgt__jar, args)
        context.compile_internal(builder, lambda :
            check_and_propagate_cpp_exception(), types.none(), [])
        return upm__xeqs
    return table_type(table_t, types.int64, types.boolean, types.voidptr,
        types.voidptr, types.voidptr, types.boolean, types.boolean, types.
        int64, types.int64, types.int64, types.boolean, types.boolean,
        types.boolean, types.voidptr, types.voidptr, types.voidptr, types.
        voidptr, table_t, types.voidptr, types.int64), codegen


_drop_duplicates_local_dictionary = types.ExternalFunction(
    'drop_duplicates_local_dictionary', types.void(array_info_type, types.
    bool_))


@numba.njit(no_cpython_wrapper=True)
def drop_duplicates_local_dictionary(dict_arr, sort_dictionary):
    mfq__btk = array_to_info(dict_arr)
    _drop_duplicates_local_dictionary(mfq__btk, sort_dictionary)
    check_and_propagate_cpp_exception()
    out_arr = info_to_array(mfq__btk, bodo.dict_str_arr_type)
    return out_arr


_convert_local_dictionary_to_global = types.ExternalFunction(
    'convert_local_dictionary_to_global', types.void(array_info_type, types
    .bool_, types.bool_))


@numba.njit(no_cpython_wrapper=True)
def convert_local_dictionary_to_global(dict_arr, sort_dictionary,
    is_parallel=False):
    mfq__btk = array_to_info(dict_arr)
    _convert_local_dictionary_to_global(mfq__btk, is_parallel, sort_dictionary)
    check_and_propagate_cpp_exception()
    out_arr = info_to_array(mfq__btk, bodo.dict_str_arr_type)
    return out_arr


get_groupby_labels = types.ExternalFunction('get_groupby_labels', types.
    int64(table_type, types.voidptr, types.voidptr, types.boolean, types.bool_)
    )
_array_isin = types.ExternalFunction('array_isin', types.void(
    array_info_type, array_info_type, array_info_type, types.bool_))


@numba.njit(no_cpython_wrapper=True)
def array_isin(out_arr, in_arr, in_values, is_parallel):
    in_arr = decode_if_dict_array(in_arr)
    in_values = decode_if_dict_array(in_values)
    ait__fdy = array_to_info(in_arr)
    qrhrd__lkze = array_to_info(in_values)
    pglwj__adqec = array_to_info(out_arr)
    xrrgk__oekde = arr_info_list_to_table([ait__fdy, qrhrd__lkze, pglwj__adqec]
        )
    _array_isin(pglwj__adqec, ait__fdy, qrhrd__lkze, is_parallel)
    check_and_propagate_cpp_exception()
    delete_table(xrrgk__oekde)


_get_search_regex = types.ExternalFunction('get_search_regex', types.void(
    array_info_type, types.bool_, types.bool_, types.voidptr, array_info_type))


@numba.njit(no_cpython_wrapper=True)
def get_search_regex(in_arr, case, match, pat, out_arr):
    ait__fdy = array_to_info(in_arr)
    pglwj__adqec = array_to_info(out_arr)
    _get_search_regex(ait__fdy, case, match, pat, pglwj__adqec)
    check_and_propagate_cpp_exception()


def _gen_row_access_intrinsic(col_array_typ, c_ind):
    from llvmlite import ir as lir
    vgv__tbj = col_array_typ.dtype
    if isinstance(vgv__tbj, (types.Number, TimeType, bodo.libs.
        pd_datetime_arr_ext.PandasDatetimeTZDtype)) or vgv__tbj in [bodo.
        datetime_date_type, bodo.datetime64ns, bodo.timedelta64ns, types.bool_
        ]:
        if isinstance(vgv__tbj, bodo.libs.pd_datetime_arr_ext.
            PandasDatetimeTZDtype):
            vgv__tbj = bodo.datetime64ns

        @intrinsic
        def getitem_func(typingctx, table_t, ind_t):

            def codegen(context, builder, sig, args):
                bwot__brxca, yixo__vfh = args
                bwot__brxca = builder.bitcast(bwot__brxca, lir.IntType(8).
                    as_pointer().as_pointer())
                qoq__hht = lir.Constant(lir.IntType(64), c_ind)
                gtcxi__ewusb = builder.load(builder.gep(bwot__brxca, [
                    qoq__hht]))
                gtcxi__ewusb = builder.bitcast(gtcxi__ewusb, context.
                    get_data_type(vgv__tbj).as_pointer())
                return context.unpack_value(builder, vgv__tbj, builder.gep(
                    gtcxi__ewusb, [yixo__vfh]))
            return vgv__tbj(types.voidptr, types.int64), codegen
        return getitem_func
    if col_array_typ in (bodo.string_array_type, bodo.binary_array_type):

        @intrinsic
        def getitem_func(typingctx, table_t, ind_t):

            def codegen(context, builder, sig, args):
                bwot__brxca, yixo__vfh = args
                bwot__brxca = builder.bitcast(bwot__brxca, lir.IntType(8).
                    as_pointer().as_pointer())
                qoq__hht = lir.Constant(lir.IntType(64), c_ind)
                gtcxi__ewusb = builder.load(builder.gep(bwot__brxca, [
                    qoq__hht]))
                jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(),
                    [lir.IntType(8).as_pointer(), lir.IntType(64), lir.
                    IntType(64).as_pointer()])
                awp__arz = cgutils.get_or_insert_function(builder.module,
                    jhakg__yvqke, name='array_info_getitem')
                tpe__zojef = cgutils.alloca_once(builder, lir.IntType(64))
                args = gtcxi__ewusb, yixo__vfh, tpe__zojef
                yci__xjpy = builder.call(awp__arz, args)
                ynyth__bzf = bodo.string_type(types.voidptr, types.int64)
                return context.compile_internal(builder, lambda data,
                    length: bodo.libs.str_arr_ext.decode_utf8(data, length),
                    ynyth__bzf, [yci__xjpy, builder.load(tpe__zojef)])
            return bodo.string_type(types.voidptr, types.int64), codegen
        return getitem_func
    if col_array_typ == bodo.libs.dict_arr_ext.dict_str_arr_type:

        @intrinsic
        def getitem_func(typingctx, table_t, ind_t):

            def codegen(context, builder, sig, args):
                dde__aib = lir.Constant(lir.IntType(64), 1)
                whaz__tgjz = lir.Constant(lir.IntType(64), 2)
                bwot__brxca, yixo__vfh = args
                bwot__brxca = builder.bitcast(bwot__brxca, lir.IntType(8).
                    as_pointer().as_pointer())
                qoq__hht = lir.Constant(lir.IntType(64), c_ind)
                gtcxi__ewusb = builder.load(builder.gep(bwot__brxca, [
                    qoq__hht]))
                jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(),
                    [lir.IntType(8).as_pointer(), lir.IntType(64)])
                hijk__psnv = cgutils.get_or_insert_function(builder.module,
                    jhakg__yvqke, name='get_nested_info')
                args = gtcxi__ewusb, whaz__tgjz
                odkp__mvydp = builder.call(hijk__psnv, args)
                jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(),
                    [lir.IntType(8).as_pointer()])
                wgfv__vru = cgutils.get_or_insert_function(builder.module,
                    jhakg__yvqke, name='array_info_getdata1')
                args = odkp__mvydp,
                uhxsx__ygz = builder.call(wgfv__vru, args)
                uhxsx__ygz = builder.bitcast(uhxsx__ygz, context.
                    get_data_type(col_array_typ.indices_dtype).as_pointer())
                tyqh__zceh = builder.sext(builder.load(builder.gep(
                    uhxsx__ygz, [yixo__vfh])), lir.IntType(64))
                args = gtcxi__ewusb, dde__aib
                yiqlc__azvql = builder.call(hijk__psnv, args)
                jhakg__yvqke = lir.FunctionType(lir.IntType(8).as_pointer(),
                    [lir.IntType(8).as_pointer(), lir.IntType(64), lir.
                    IntType(64).as_pointer()])
                awp__arz = cgutils.get_or_insert_function(builder.module,
                    jhakg__yvqke, name='array_info_getitem')
                tpe__zojef = cgutils.alloca_once(builder, lir.IntType(64))
                args = yiqlc__azvql, tyqh__zceh, tpe__zojef
                yci__xjpy = builder.call(awp__arz, args)
                ynyth__bzf = bodo.string_type(types.voidptr, types.int64)
                return context.compile_internal(builder, lambda data,
                    length: bodo.libs.str_arr_ext.decode_utf8(data, length),
                    ynyth__bzf, [yci__xjpy, builder.load(tpe__zojef)])
            return bodo.string_type(types.voidptr, types.int64), codegen
        return getitem_func
    raise BodoError(
        f"General Join Conditions with '{vgv__tbj}' column data type not supported"
        )


def _gen_row_na_check_intrinsic(col_array_dtype, c_ind):
    if isinstance(col_array_dtype, (IntegerArrayType, FloatingArrayType,
        bodo.TimeArrayType)) or col_array_dtype in (bodo.libs.bool_arr_ext.
        boolean_array, bodo.binary_array_type, bodo.datetime_date_array_type
        ) or is_str_arr_type(col_array_dtype):

        @intrinsic
        def checkna_func(typingctx, table_t, ind_t):

            def codegen(context, builder, sig, args):
                bdc__twggf, yixo__vfh = args
                bdc__twggf = builder.bitcast(bdc__twggf, lir.IntType(8).
                    as_pointer().as_pointer())
                qoq__hht = lir.Constant(lir.IntType(64), c_ind)
                gtcxi__ewusb = builder.load(builder.gep(bdc__twggf, [qoq__hht])
                    )
                jmtva__zzqdu = builder.bitcast(gtcxi__ewusb, context.
                    get_data_type(types.bool_).as_pointer())
                bemfo__trs = bodo.utils.cg_helpers.get_bitmap_bit(builder,
                    jmtva__zzqdu, yixo__vfh)
                wwa__oomin = builder.icmp_unsigned('!=', bemfo__trs, lir.
                    Constant(lir.IntType(8), 0))
                return builder.sext(wwa__oomin, lir.IntType(8))
            return types.int8(types.voidptr, types.int64), codegen
        return checkna_func
    elif isinstance(col_array_dtype, (types.Array, bodo.DatetimeArrayType)):
        vgv__tbj = col_array_dtype.dtype
        if vgv__tbj in [bodo.datetime64ns, bodo.timedelta64ns] or isinstance(
            vgv__tbj, bodo.libs.pd_datetime_arr_ext.PandasDatetimeTZDtype):
            if isinstance(vgv__tbj, bodo.libs.pd_datetime_arr_ext.
                PandasDatetimeTZDtype):
                vgv__tbj = bodo.datetime64ns

            @intrinsic
            def checkna_func(typingctx, table_t, ind_t):

                def codegen(context, builder, sig, args):
                    bwot__brxca, yixo__vfh = args
                    bwot__brxca = builder.bitcast(bwot__brxca, lir.IntType(
                        8).as_pointer().as_pointer())
                    qoq__hht = lir.Constant(lir.IntType(64), c_ind)
                    gtcxi__ewusb = builder.load(builder.gep(bwot__brxca, [
                        qoq__hht]))
                    gtcxi__ewusb = builder.bitcast(gtcxi__ewusb, context.
                        get_data_type(vgv__tbj).as_pointer())
                    acnsk__wxu = builder.load(builder.gep(gtcxi__ewusb, [
                        yixo__vfh]))
                    wwa__oomin = builder.icmp_unsigned('!=', acnsk__wxu,
                        lir.Constant(lir.IntType(64), pd._libs.iNaT))
                    return builder.sext(wwa__oomin, lir.IntType(8))
                return types.int8(types.voidptr, types.int64), codegen
            return checkna_func
        elif isinstance(vgv__tbj, types.Float):

            @intrinsic
            def checkna_func(typingctx, table_t, ind_t):

                def codegen(context, builder, sig, args):
                    bwot__brxca, yixo__vfh = args
                    bwot__brxca = builder.bitcast(bwot__brxca, lir.IntType(
                        8).as_pointer().as_pointer())
                    qoq__hht = lir.Constant(lir.IntType(64), c_ind)
                    gtcxi__ewusb = builder.load(builder.gep(bwot__brxca, [
                        qoq__hht]))
                    gtcxi__ewusb = builder.bitcast(gtcxi__ewusb, context.
                        get_data_type(vgv__tbj).as_pointer())
                    acnsk__wxu = builder.load(builder.gep(gtcxi__ewusb, [
                        yixo__vfh]))
                    vvejz__zkpev = signature(types.bool_, vgv__tbj)
                    bemfo__trs = numba.np.npyfuncs.np_real_isnan_impl(context,
                        builder, vvejz__zkpev, (acnsk__wxu,))
                    return builder.not_(builder.sext(bemfo__trs, lir.
                        IntType(8)))
                return types.int8(types.voidptr, types.int64), codegen
            return checkna_func
    raise BodoError(
        f"General Join Conditions with '{col_array_dtype}' column type not supported"
        )
