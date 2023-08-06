"""
Boxing and unboxing support for DataFrame, Series, etc.
"""
import datetime
import decimal
import warnings
from enum import Enum
import llvmlite.binding as ll
import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.ir_utils import GuardException, guard
from numba.core.typing import signature
from numba.cpython.listobj import ListInstance
from numba.extending import NativeValue, box, intrinsic, typeof_impl, unbox
from numba.np.arrayobj import _getitem_array_single_int
from numba.typed.typeddict import Dict
import bodo
from bodo.hiframes.datetime_date_ext import datetime_date_array_type
from bodo.hiframes.datetime_timedelta_ext import datetime_timedelta_array_type
from bodo.hiframes.pd_categorical_ext import PDCategoricalDtype
from bodo.hiframes.pd_dataframe_ext import DataFramePayloadType, DataFrameType, check_runtime_cols_unsupported, construct_dataframe
from bodo.hiframes.pd_index_ext import BinaryIndexType, CategoricalIndexType, DatetimeIndexType, NumericIndexType, PeriodIndexType, RangeIndexType, StringIndexType, TimedeltaIndexType
from bodo.hiframes.pd_series_ext import HeterogeneousSeriesType, SeriesType
from bodo.hiframes.split_impl import string_array_split_view_type
from bodo.hiframes.time_ext import TimeArrayType
from bodo.libs import hstr_ext
from bodo.libs.array_item_arr_ext import ArrayItemArrayType
from bodo.libs.binary_arr_ext import binary_array_type, bytes_type
from bodo.libs.decimal_arr_ext import Decimal128Type, DecimalArrayType
from bodo.libs.float_arr_ext import FloatDtype, FloatingArrayType
from bodo.libs.int_arr_ext import IntDtype, IntegerArrayType
from bodo.libs.map_arr_ext import MapArrayType
from bodo.libs.str_arr_ext import string_array_type, string_type
from bodo.libs.str_ext import string_type
from bodo.libs.struct_arr_ext import StructArrayType, StructType
from bodo.libs.tuple_arr_ext import TupleArrayType
from bodo.utils.cg_helpers import is_ll_eq
from bodo.utils.typing import BodoError, BodoWarning, dtype_to_array_type, get_overload_const_bool, get_overload_const_int, get_overload_const_str, is_overload_constant_bool, is_overload_constant_int, is_overload_constant_str, raise_bodo_error, to_nullable_type, to_str_arr_if_dict_array
ll.add_symbol('is_np_array', hstr_ext.is_np_array)
ll.add_symbol('array_size', hstr_ext.array_size)
ll.add_symbol('array_getptr1', hstr_ext.array_getptr1)
TABLE_FORMAT_THRESHOLD = 20
_use_dict_str_type = False


def _set_bodo_meta_in_pandas():
    if '_bodo_meta' not in pd.Series._metadata:
        pd.Series._metadata.append('_bodo_meta')
    if '_bodo_meta' not in pd.DataFrame._metadata:
        pd.DataFrame._metadata.append('_bodo_meta')


_set_bodo_meta_in_pandas()


@typeof_impl.register(pd.DataFrame)
def typeof_pd_dataframe(val, c):
    from bodo.transforms.distributed_analysis import Distribution
    lbfct__jaam = tuple(val.columns.to_list())
    hymb__yhao = get_hiframes_dtypes(val)
    if (len(val.index) == 0 and val.index.dtype == np.dtype('O') and
        hasattr(val, '_bodo_meta') and val._bodo_meta is not None and 
        'type_metadata' in val._bodo_meta and val._bodo_meta[
        'type_metadata'] is not None and len(val._bodo_meta['type_metadata'
        ][1]) == len(val.columns) and val._bodo_meta['type_metadata'][0] is not
        None):
        xtxkr__bajg = _dtype_from_type_enum_list(val._bodo_meta[
            'type_metadata'][0])
    else:
        xtxkr__bajg = numba.typeof(val.index)
    rccud__dmfht = Distribution(val._bodo_meta['dist']) if hasattr(val,
        '_bodo_meta') and val._bodo_meta is not None else Distribution.REP
    skxf__qbh = len(hymb__yhao) >= TABLE_FORMAT_THRESHOLD
    return DataFrameType(hymb__yhao, xtxkr__bajg, lbfct__jaam, rccud__dmfht,
        is_table_format=skxf__qbh)


@typeof_impl.register(pd.Series)
def typeof_pd_series(val, c):
    from bodo.transforms.distributed_analysis import Distribution
    rccud__dmfht = Distribution(val._bodo_meta['dist']) if hasattr(val,
        '_bodo_meta') and val._bodo_meta is not None else Distribution.REP
    if (len(val.index) == 0 and val.index.dtype == np.dtype('O') and
        hasattr(val, '_bodo_meta') and val._bodo_meta is not None and 
        'type_metadata' in val._bodo_meta and val._bodo_meta[
        'type_metadata'] is not None and val._bodo_meta['type_metadata'][0]
         is not None):
        ymrj__hbapv = _dtype_from_type_enum_list(val._bodo_meta[
            'type_metadata'][0])
    else:
        ymrj__hbapv = numba.typeof(val.index)
    pot__qpja = _infer_series_arr_type(val)
    if _use_dict_str_type and pot__qpja == string_array_type:
        pot__qpja = bodo.dict_str_arr_type
    return SeriesType(pot__qpja.dtype, data=pot__qpja, index=ymrj__hbapv,
        name_typ=numba.typeof(val.name), dist=rccud__dmfht)


@unbox(DataFrameType)
def unbox_dataframe(typ, val, c):
    check_runtime_cols_unsupported(typ, 'Unboxing')
    zdv__kcxgm = c.pyapi.object_getattr_string(val, 'index')
    aszo__rrs = c.pyapi.to_native_value(typ.index, zdv__kcxgm).value
    c.pyapi.decref(zdv__kcxgm)
    if typ.is_table_format:
        hohw__gbvfn = cgutils.create_struct_proxy(typ.table_type)(c.context,
            c.builder)
        hohw__gbvfn.parent = val
        for ivl__ybwc, wwumq__zcv in typ.table_type.type_to_blk.items():
            gqsgq__tpbv = c.context.get_constant(types.int64, len(typ.
                table_type.block_to_arr_ind[wwumq__zcv]))
            jnyr__znaap, barq__akyme = ListInstance.allocate_ex(c.context,
                c.builder, types.List(ivl__ybwc), gqsgq__tpbv)
            barq__akyme.size = gqsgq__tpbv
            setattr(hohw__gbvfn, f'block_{wwumq__zcv}', barq__akyme.value)
        lxq__ptd = c.pyapi.call_method(val, '__len__', ())
        pwwd__eulm = c.pyapi.long_as_longlong(lxq__ptd)
        c.pyapi.decref(lxq__ptd)
        hohw__gbvfn.len = pwwd__eulm
        sjp__xbd = c.context.make_tuple(c.builder, types.Tuple([typ.
            table_type]), [hohw__gbvfn._getvalue()])
    else:
        trko__olwq = [c.context.get_constant_null(ivl__ybwc) for ivl__ybwc in
            typ.data]
        sjp__xbd = c.context.make_tuple(c.builder, types.Tuple(typ.data),
            trko__olwq)
    ykm__xbf = construct_dataframe(c.context, c.builder, typ, sjp__xbd,
        aszo__rrs, val, None)
    return NativeValue(ykm__xbf)


def get_hiframes_dtypes(df):
    if (hasattr(df, '_bodo_meta') and df._bodo_meta is not None and 
        'type_metadata' in df._bodo_meta and df._bodo_meta['type_metadata']
         is not None and len(df._bodo_meta['type_metadata'][1]) == len(df.
        columns)):
        yyz__uvfk = df._bodo_meta['type_metadata'][1]
    else:
        yyz__uvfk = [None] * len(df.columns)
    qjc__cneya = [_infer_series_arr_type(df.iloc[:, i], array_metadata=
        yyz__uvfk[i]) for i in range(len(df.columns))]
    qjc__cneya = [(bodo.dict_str_arr_type if _use_dict_str_type and 
        ivl__ybwc == string_array_type else ivl__ybwc) for ivl__ybwc in
        qjc__cneya]
    return tuple(qjc__cneya)


class SeriesDtypeEnum(Enum):
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
    Datime_Date = 13
    NP_Datetime64ns = 14
    NP_Timedelta64ns = 15
    Int128 = 16
    LIST = 18
    STRUCT = 19
    BINARY = 21
    ARRAY = 22
    PD_nullable_Int8 = 23
    PD_nullable_UInt8 = 24
    PD_nullable_Int16 = 25
    PD_nullable_UInt16 = 26
    PD_nullable_Int32 = 27
    PD_nullable_UInt32 = 28
    PD_nullable_Int64 = 29
    PD_nullable_UInt64 = 30
    PD_nullable_bool = 31
    CategoricalType = 32
    NoneType = 33
    Literal = 34
    IntegerArray = 35
    RangeIndexType = 36
    DatetimeIndexType = 37
    NumericIndexType = 38
    PeriodIndexType = 39
    IntervalIndexType = 40
    CategoricalIndexType = 41
    StringIndexType = 42
    BinaryIndexType = 43
    TimedeltaIndexType = 44
    LiteralType = 45
    PD_nullable_Float32 = 46
    PD_nullable_Float64 = 47
    FloatingArray = 48


_one_to_one_type_to_enum_map = {types.int8: SeriesDtypeEnum.Int8.value,
    types.uint8: SeriesDtypeEnum.UInt8.value, types.int32: SeriesDtypeEnum.
    Int32.value, types.uint32: SeriesDtypeEnum.UInt32.value, types.int64:
    SeriesDtypeEnum.Int64.value, types.uint64: SeriesDtypeEnum.UInt64.value,
    types.float32: SeriesDtypeEnum.Float32.value, types.float64:
    SeriesDtypeEnum.Float64.value, types.NPDatetime('ns'): SeriesDtypeEnum.
    NP_Datetime64ns.value, types.NPTimedelta('ns'): SeriesDtypeEnum.
    NP_Timedelta64ns.value, types.bool_: SeriesDtypeEnum.Bool.value, types.
    int16: SeriesDtypeEnum.Int16.value, types.uint16: SeriesDtypeEnum.
    UInt16.value, types.Integer('int128', 128): SeriesDtypeEnum.Int128.
    value, bodo.hiframes.datetime_date_ext.datetime_date_type:
    SeriesDtypeEnum.Datime_Date.value, IntDtype(types.int8):
    SeriesDtypeEnum.PD_nullable_Int8.value, IntDtype(types.uint8):
    SeriesDtypeEnum.PD_nullable_UInt8.value, IntDtype(types.int16):
    SeriesDtypeEnum.PD_nullable_Int16.value, IntDtype(types.uint16):
    SeriesDtypeEnum.PD_nullable_UInt16.value, IntDtype(types.int32):
    SeriesDtypeEnum.PD_nullable_Int32.value, IntDtype(types.uint32):
    SeriesDtypeEnum.PD_nullable_UInt32.value, IntDtype(types.int64):
    SeriesDtypeEnum.PD_nullable_Int64.value, IntDtype(types.uint64):
    SeriesDtypeEnum.PD_nullable_UInt64.value, FloatDtype(types.float32):
    SeriesDtypeEnum.PD_nullable_Float32.value, FloatDtype(types.float64):
    SeriesDtypeEnum.PD_nullable_Float64.value, bytes_type: SeriesDtypeEnum.
    BINARY.value, string_type: SeriesDtypeEnum.STRING.value, bodo.bool_:
    SeriesDtypeEnum.Bool.value, types.none: SeriesDtypeEnum.NoneType.value}
_one_to_one_enum_to_type_map = {SeriesDtypeEnum.Int8.value: types.int8,
    SeriesDtypeEnum.UInt8.value: types.uint8, SeriesDtypeEnum.Int32.value:
    types.int32, SeriesDtypeEnum.UInt32.value: types.uint32,
    SeriesDtypeEnum.Int64.value: types.int64, SeriesDtypeEnum.UInt64.value:
    types.uint64, SeriesDtypeEnum.Float32.value: types.float32,
    SeriesDtypeEnum.Float64.value: types.float64, SeriesDtypeEnum.
    NP_Datetime64ns.value: types.NPDatetime('ns'), SeriesDtypeEnum.
    NP_Timedelta64ns.value: types.NPTimedelta('ns'), SeriesDtypeEnum.Int16.
    value: types.int16, SeriesDtypeEnum.UInt16.value: types.uint16,
    SeriesDtypeEnum.Int128.value: types.Integer('int128', 128),
    SeriesDtypeEnum.Datime_Date.value: bodo.hiframes.datetime_date_ext.
    datetime_date_type, SeriesDtypeEnum.PD_nullable_Int8.value: IntDtype(
    types.int8), SeriesDtypeEnum.PD_nullable_UInt8.value: IntDtype(types.
    uint8), SeriesDtypeEnum.PD_nullable_Int16.value: IntDtype(types.int16),
    SeriesDtypeEnum.PD_nullable_UInt16.value: IntDtype(types.uint16),
    SeriesDtypeEnum.PD_nullable_Int32.value: IntDtype(types.int32),
    SeriesDtypeEnum.PD_nullable_UInt32.value: IntDtype(types.uint32),
    SeriesDtypeEnum.PD_nullable_Int64.value: IntDtype(types.int64),
    SeriesDtypeEnum.PD_nullable_UInt64.value: IntDtype(types.uint64),
    SeriesDtypeEnum.PD_nullable_Float32.value: FloatDtype(types.float32),
    SeriesDtypeEnum.PD_nullable_Float64.value: FloatDtype(types.float64),
    SeriesDtypeEnum.BINARY.value: bytes_type, SeriesDtypeEnum.STRING.value:
    string_type, SeriesDtypeEnum.Bool.value: bodo.bool_, SeriesDtypeEnum.
    NoneType.value: types.none}


def _dtype_from_type_enum_list(typ_enum_list):
    nnxvv__xbkmc, typ = _dtype_from_type_enum_list_recursor(typ_enum_list)
    if len(nnxvv__xbkmc) != 0:
        raise_bodo_error(
            f"""Unexpected Internal Error while converting typing metadata: Dtype list was not fully consumed.
 Input typ_enum_list: {typ_enum_list}.
Remainder: {nnxvv__xbkmc}. Please file the error here: https://github.com/Bodo-inc/Feedback"""
            )
    return typ


def _dtype_from_type_enum_list_recursor(typ_enum_list):
    if len(typ_enum_list) == 0:
        raise_bodo_error('Unable to infer dtype from empty typ_enum_list')
    elif typ_enum_list[0] in _one_to_one_enum_to_type_map:
        return typ_enum_list[1:], _one_to_one_enum_to_type_map[typ_enum_list[0]
            ]
    elif typ_enum_list[0] == SeriesDtypeEnum.IntegerArray.value:
        gfemv__wgxlx, typ = _dtype_from_type_enum_list_recursor(typ_enum_list
            [1:])
        return gfemv__wgxlx, IntegerArrayType(typ)
    elif typ_enum_list[0] == SeriesDtypeEnum.FloatingArray.value:
        gfemv__wgxlx, typ = _dtype_from_type_enum_list_recursor(typ_enum_list
            [1:])
        return gfemv__wgxlx, FloatingArrayType(typ)
    elif typ_enum_list[0] == SeriesDtypeEnum.ARRAY.value:
        gfemv__wgxlx, typ = _dtype_from_type_enum_list_recursor(typ_enum_list
            [1:])
        return gfemv__wgxlx, dtype_to_array_type(typ)
    elif typ_enum_list[0] == SeriesDtypeEnum.Decimal.value:
        zcyq__gbwaj = typ_enum_list[1]
        bmn__tfkkd = typ_enum_list[2]
        return typ_enum_list[3:], Decimal128Type(zcyq__gbwaj, bmn__tfkkd)
    elif typ_enum_list[0] == SeriesDtypeEnum.STRUCT.value:
        cdp__joi = typ_enum_list[1]
        lex__ovql = tuple(typ_enum_list[2:2 + cdp__joi])
        ogjyg__sux = typ_enum_list[2 + cdp__joi:]
        eub__onx = []
        for i in range(cdp__joi):
            ogjyg__sux, ayt__ydwy = _dtype_from_type_enum_list_recursor(
                ogjyg__sux)
            eub__onx.append(ayt__ydwy)
        return ogjyg__sux, StructType(tuple(eub__onx), lex__ovql)
    elif typ_enum_list[0] == SeriesDtypeEnum.Literal.value:
        if len(typ_enum_list) == 1:
            raise_bodo_error(
                f"Unexpected Internal Error while converting typing metadata: Encountered 'Literal' internal enum value with no value following it. Please file the error here: https://github.com/Bodo-inc/Feedback"
                )
        fais__ghh = typ_enum_list[1]
        ogjyg__sux = typ_enum_list[2:]
        return ogjyg__sux, fais__ghh
    elif typ_enum_list[0] == SeriesDtypeEnum.LiteralType.value:
        if len(typ_enum_list) == 1:
            raise_bodo_error(
                f"Unexpected Internal Error while converting typing metadata: Encountered 'LiteralType' internal enum value with no value following it. Please file the error here: https://github.com/Bodo-inc/Feedback"
                )
        fais__ghh = typ_enum_list[1]
        ogjyg__sux = typ_enum_list[2:]
        return ogjyg__sux, numba.types.literal(fais__ghh)
    elif typ_enum_list[0] == SeriesDtypeEnum.CategoricalType.value:
        ogjyg__sux, vsmiz__gqt = _dtype_from_type_enum_list_recursor(
            typ_enum_list[1:])
        ogjyg__sux, vrf__qzg = _dtype_from_type_enum_list_recursor(ogjyg__sux)
        ogjyg__sux, aiedu__dtjb = _dtype_from_type_enum_list_recursor(
            ogjyg__sux)
        ogjyg__sux, xxnuu__ffnp = _dtype_from_type_enum_list_recursor(
            ogjyg__sux)
        ogjyg__sux, cbo__anse = _dtype_from_type_enum_list_recursor(ogjyg__sux)
        return ogjyg__sux, PDCategoricalDtype(vsmiz__gqt, vrf__qzg,
            aiedu__dtjb, xxnuu__ffnp, cbo__anse)
    elif typ_enum_list[0] == SeriesDtypeEnum.DatetimeIndexType.value:
        ogjyg__sux, tevpr__ocyq = _dtype_from_type_enum_list_recursor(
            typ_enum_list[1:])
        return ogjyg__sux, DatetimeIndexType(tevpr__ocyq)
    elif typ_enum_list[0] == SeriesDtypeEnum.NumericIndexType.value:
        ogjyg__sux, dtype = _dtype_from_type_enum_list_recursor(typ_enum_list
            [1:])
        ogjyg__sux, tevpr__ocyq = _dtype_from_type_enum_list_recursor(
            ogjyg__sux)
        ogjyg__sux, xxnuu__ffnp = _dtype_from_type_enum_list_recursor(
            ogjyg__sux)
        return ogjyg__sux, NumericIndexType(dtype, tevpr__ocyq, xxnuu__ffnp)
    elif typ_enum_list[0] == SeriesDtypeEnum.PeriodIndexType.value:
        ogjyg__sux, skm__tyfxx = _dtype_from_type_enum_list_recursor(
            typ_enum_list[1:])
        ogjyg__sux, tevpr__ocyq = _dtype_from_type_enum_list_recursor(
            ogjyg__sux)
        return ogjyg__sux, PeriodIndexType(skm__tyfxx, tevpr__ocyq)
    elif typ_enum_list[0] == SeriesDtypeEnum.CategoricalIndexType.value:
        ogjyg__sux, xxnuu__ffnp = _dtype_from_type_enum_list_recursor(
            typ_enum_list[1:])
        ogjyg__sux, tevpr__ocyq = _dtype_from_type_enum_list_recursor(
            ogjyg__sux)
        return ogjyg__sux, CategoricalIndexType(xxnuu__ffnp, tevpr__ocyq)
    elif typ_enum_list[0] == SeriesDtypeEnum.RangeIndexType.value:
        ogjyg__sux, tevpr__ocyq = _dtype_from_type_enum_list_recursor(
            typ_enum_list[1:])
        return ogjyg__sux, RangeIndexType(tevpr__ocyq)
    elif typ_enum_list[0] == SeriesDtypeEnum.StringIndexType.value:
        ogjyg__sux, tevpr__ocyq = _dtype_from_type_enum_list_recursor(
            typ_enum_list[1:])
        return ogjyg__sux, StringIndexType(tevpr__ocyq)
    elif typ_enum_list[0] == SeriesDtypeEnum.BinaryIndexType.value:
        ogjyg__sux, tevpr__ocyq = _dtype_from_type_enum_list_recursor(
            typ_enum_list[1:])
        return ogjyg__sux, BinaryIndexType(tevpr__ocyq)
    elif typ_enum_list[0] == SeriesDtypeEnum.TimedeltaIndexType.value:
        ogjyg__sux, tevpr__ocyq = _dtype_from_type_enum_list_recursor(
            typ_enum_list[1:])
        return ogjyg__sux, TimedeltaIndexType(tevpr__ocyq)
    else:
        raise_bodo_error(
            f'Unexpected Internal Error while converting typing metadata: unable to infer dtype for type enum {typ_enum_list[0]}. Please file the error here: https://github.com/Bodo-inc/Feedback'
            )


def _dtype_to_type_enum_list(typ):
    return guard(_dtype_to_type_enum_list_recursor, typ)


def _dtype_to_type_enum_list_recursor(typ, upcast_numeric_index=True):
    if typ.__hash__ and typ in _one_to_one_type_to_enum_map:
        return [_one_to_one_type_to_enum_map[typ]]
    if isinstance(typ, (dict, int, list, tuple, str, bool, bytes, float)):
        return [SeriesDtypeEnum.Literal.value, typ]
    elif typ is None:
        return [SeriesDtypeEnum.Literal.value, typ]
    elif is_overload_constant_int(typ):
        mfxmg__ldue = get_overload_const_int(typ)
        if numba.types.maybe_literal(mfxmg__ldue) == typ:
            return [SeriesDtypeEnum.LiteralType.value, mfxmg__ldue]
    elif is_overload_constant_str(typ):
        mfxmg__ldue = get_overload_const_str(typ)
        if numba.types.maybe_literal(mfxmg__ldue) == typ:
            return [SeriesDtypeEnum.LiteralType.value, mfxmg__ldue]
    elif is_overload_constant_bool(typ):
        mfxmg__ldue = get_overload_const_bool(typ)
        if numba.types.maybe_literal(mfxmg__ldue) == typ:
            return [SeriesDtypeEnum.LiteralType.value, mfxmg__ldue]
    elif isinstance(typ, IntegerArrayType):
        return [SeriesDtypeEnum.IntegerArray.value
            ] + _dtype_to_type_enum_list_recursor(typ.dtype)
    elif isinstance(typ, FloatingArrayType):
        return [SeriesDtypeEnum.FloatingArray.value
            ] + _dtype_to_type_enum_list_recursor(typ.dtype)
    elif bodo.utils.utils.is_array_typ(typ, False):
        return [SeriesDtypeEnum.ARRAY.value
            ] + _dtype_to_type_enum_list_recursor(typ.dtype)
    elif isinstance(typ, StructType):
        jtp__kfy = [SeriesDtypeEnum.STRUCT.value, len(typ.names)]
        for mkpwf__frbyq in typ.names:
            jtp__kfy.append(mkpwf__frbyq)
        for etq__wfo in typ.data:
            jtp__kfy += _dtype_to_type_enum_list_recursor(etq__wfo)
        return jtp__kfy
    elif isinstance(typ, bodo.libs.decimal_arr_ext.Decimal128Type):
        return [SeriesDtypeEnum.Decimal.value, typ.precision, typ.scale]
    elif isinstance(typ, PDCategoricalDtype):
        dgp__mwie = _dtype_to_type_enum_list_recursor(typ.categories)
        tygz__gfgoh = _dtype_to_type_enum_list_recursor(typ.elem_type)
        vgor__dcto = _dtype_to_type_enum_list_recursor(typ.ordered)
        raox__ykda = _dtype_to_type_enum_list_recursor(typ.data)
        zwsx__jzuf = _dtype_to_type_enum_list_recursor(typ.int_type)
        return [SeriesDtypeEnum.CategoricalType.value
            ] + dgp__mwie + tygz__gfgoh + vgor__dcto + raox__ykda + zwsx__jzuf
    elif isinstance(typ, DatetimeIndexType):
        return [SeriesDtypeEnum.DatetimeIndexType.value
            ] + _dtype_to_type_enum_list_recursor(typ.name_typ)
    elif isinstance(typ, NumericIndexType):
        if upcast_numeric_index:
            if isinstance(typ.dtype, types.Float):
                nsasd__wfbvd = types.float64
                if isinstance(typ.data, FloatingArrayType):
                    tenu__wzjo = FloatingArrayType(nsasd__wfbvd)
                else:
                    tenu__wzjo = types.Array(nsasd__wfbvd, 1, 'C')
            elif typ.dtype in {types.int8, types.int16, types.int32, types.
                int64}:
                nsasd__wfbvd = types.int64
                if isinstance(typ.data, IntegerArrayType):
                    tenu__wzjo = IntegerArrayType(nsasd__wfbvd)
                else:
                    tenu__wzjo = types.Array(nsasd__wfbvd, 1, 'C')
            elif typ.dtype in {types.uint8, types.uint16, types.uint32,
                types.uint64}:
                nsasd__wfbvd = types.uint64
                if isinstance(typ.data, IntegerArrayType):
                    tenu__wzjo = IntegerArrayType(nsasd__wfbvd)
                else:
                    tenu__wzjo = types.Array(nsasd__wfbvd, 1, 'C')
            elif typ.dtype == types.bool_:
                nsasd__wfbvd = typ.dtype
                tenu__wzjo = typ.data
            else:
                raise GuardException('Unable to convert type')
            return [SeriesDtypeEnum.NumericIndexType.value
                ] + _dtype_to_type_enum_list_recursor(nsasd__wfbvd
                ) + _dtype_to_type_enum_list_recursor(typ.name_typ
                ) + _dtype_to_type_enum_list_recursor(tenu__wzjo)
        else:
            return [SeriesDtypeEnum.NumericIndexType.value
                ] + _dtype_to_type_enum_list_recursor(typ.dtype
                ) + _dtype_to_type_enum_list_recursor(typ.name_typ
                ) + _dtype_to_type_enum_list_recursor(typ.data)
    elif isinstance(typ, PeriodIndexType):
        return [SeriesDtypeEnum.PeriodIndexType.value
            ] + _dtype_to_type_enum_list_recursor(typ.freq
            ) + _dtype_to_type_enum_list_recursor(typ.name_typ)
    elif isinstance(typ, CategoricalIndexType):
        return [SeriesDtypeEnum.CategoricalIndexType.value
            ] + _dtype_to_type_enum_list_recursor(typ.data
            ) + _dtype_to_type_enum_list_recursor(typ.name_typ)
    elif isinstance(typ, RangeIndexType):
        return [SeriesDtypeEnum.RangeIndexType.value
            ] + _dtype_to_type_enum_list_recursor(typ.name_typ)
    elif isinstance(typ, StringIndexType):
        return [SeriesDtypeEnum.StringIndexType.value
            ] + _dtype_to_type_enum_list_recursor(typ.name_typ)
    elif isinstance(typ, BinaryIndexType):
        return [SeriesDtypeEnum.BinaryIndexType.value
            ] + _dtype_to_type_enum_list_recursor(typ.name_typ)
    elif isinstance(typ, TimedeltaIndexType):
        return [SeriesDtypeEnum.TimedeltaIndexType.value
            ] + _dtype_to_type_enum_list_recursor(typ.name_typ)
    else:
        raise GuardException('Unable to convert type')


def _is_wrapper_pd_arr(arr):
    if isinstance(arr, pd.arrays.StringArray):
        return False
    return isinstance(arr, (pd.arrays.PandasArray, pd.arrays.TimedeltaArray)
        ) or isinstance(arr, pd.arrays.DatetimeArray) and arr.tz is None


def unwrap_pd_arr(arr):
    if _is_wrapper_pd_arr(arr):
        return np.ascontiguousarray(arr._ndarray)
    return arr


def _fix_series_arr_type(pd_arr):
    if _is_wrapper_pd_arr(pd_arr):
        return pd_arr._ndarray
    return pd_arr


def _infer_series_arr_type(S, array_metadata=None):
    if S.dtype == np.dtype('O'):
        if len(S.array) == 0 or S.isna().sum() == len(S):
            if array_metadata is not None:
                return _dtype_from_type_enum_list(array_metadata)
            elif hasattr(S, '_bodo_meta'
                ) and S._bodo_meta is not None and 'type_metadata' in S._bodo_meta and S._bodo_meta[
                'type_metadata'][1] is not None:
                jlqvm__nnl = S._bodo_meta['type_metadata'][1]
                return dtype_to_array_type(_dtype_from_type_enum_list(
                    jlqvm__nnl))
        return bodo.typeof(_fix_series_arr_type(S.array))
    try:
        cxi__jrmkd = bodo.typeof(_fix_series_arr_type(S.array))
        if cxi__jrmkd == types.Array(types.bool_, 1, 'C'):
            cxi__jrmkd = bodo.boolean_array
        if isinstance(cxi__jrmkd, types.Array):
            assert cxi__jrmkd.ndim == 1, 'invalid numpy array type in Series'
            cxi__jrmkd = types.Array(cxi__jrmkd.dtype, 1, 'C')
        return cxi__jrmkd
    except:
        raise BodoError(
            f'data type {S.dtype} for column {S.name} not supported yet')


def _get_use_df_parent_obj_flag(builder, context, pyapi, parent_obj, n_cols):
    if n_cols is None:
        return context.get_constant(types.bool_, False)
    fugy__dkxgx = cgutils.is_not_null(builder, parent_obj)
    vxal__enryr = cgutils.alloca_once_value(builder, context.get_constant(
        types.int64, 0))
    with builder.if_then(fugy__dkxgx):
        djey__gtlaq = pyapi.object_getattr_string(parent_obj, 'columns')
        lxq__ptd = pyapi.call_method(djey__gtlaq, '__len__', ())
        builder.store(pyapi.long_as_longlong(lxq__ptd), vxal__enryr)
        pyapi.decref(lxq__ptd)
        pyapi.decref(djey__gtlaq)
    use_parent_obj = builder.and_(fugy__dkxgx, builder.icmp_unsigned('==',
        builder.load(vxal__enryr), context.get_constant(types.int64, n_cols)))
    return use_parent_obj


def _get_df_columns_obj(c, builder, context, pyapi, df_typ, dataframe_payload):
    if df_typ.has_runtime_cols:
        khmay__vcw = df_typ.runtime_colname_typ
        context.nrt.incref(builder, khmay__vcw, dataframe_payload.columns)
        return pyapi.from_native_value(khmay__vcw, dataframe_payload.
            columns, c.env_manager)
    if all(isinstance(c, str) for c in df_typ.columns):
        lylv__hok = pd.array(df_typ.columns, 'string')
    elif all(isinstance(c, int) for c in df_typ.columns):
        lylv__hok = np.array(df_typ.columns, 'int64')
    else:
        lylv__hok = df_typ.columns
    dxr__untt = numba.typeof(lylv__hok)
    lnjfq__bwjfm = context.get_constant_generic(builder, dxr__untt, lylv__hok)
    tazk__bmwnc = pyapi.from_native_value(dxr__untt, lnjfq__bwjfm, c.
        env_manager)
    if (dxr__untt == bodo.string_array_type and bodo.libs.str_arr_ext.
        use_pd_pyarrow_string_array):
        duc__jycre = tazk__bmwnc
        tazk__bmwnc = pyapi.call_method(tazk__bmwnc, 'to_numpy', ())
        pyapi.decref(duc__jycre)
    return tazk__bmwnc


def _create_initial_df_object(builder, context, pyapi, c, df_typ, obj,
    dataframe_payload, res, use_parent_obj):
    with c.builder.if_else(use_parent_obj) as (bpfab__cssa, trx__hohjb):
        with bpfab__cssa:
            pyapi.incref(obj)
            emhal__ppyk = context.insert_const_string(c.builder.module, 'numpy'
                )
            daavf__cucwx = pyapi.import_module_noblock(emhal__ppyk)
            if df_typ.has_runtime_cols:
                rhvkq__yvltz = 0
            else:
                rhvkq__yvltz = len(df_typ.columns)
            ebv__soah = pyapi.long_from_longlong(lir.Constant(lir.IntType(
                64), rhvkq__yvltz))
            gdjmt__defli = pyapi.call_method(daavf__cucwx, 'arange', (
                ebv__soah,))
            pyapi.object_setattr_string(obj, 'columns', gdjmt__defli)
            pyapi.decref(daavf__cucwx)
            pyapi.decref(gdjmt__defli)
            pyapi.decref(ebv__soah)
        with trx__hohjb:
            context.nrt.incref(builder, df_typ.index, dataframe_payload.index)
            upk__njfus = c.pyapi.from_native_value(df_typ.index,
                dataframe_payload.index, c.env_manager)
            emhal__ppyk = context.insert_const_string(c.builder.module,
                'pandas')
            daavf__cucwx = pyapi.import_module_noblock(emhal__ppyk)
            df_obj = pyapi.call_method(daavf__cucwx, 'DataFrame', (pyapi.
                borrow_none(), upk__njfus))
            pyapi.decref(daavf__cucwx)
            pyapi.decref(upk__njfus)
            builder.store(df_obj, res)


@box(DataFrameType)
def box_dataframe(typ, val, c):
    from bodo.hiframes.table import box_table
    context = c.context
    builder = c.builder
    pyapi = c.pyapi
    dataframe_payload = bodo.hiframes.pd_dataframe_ext.get_dataframe_payload(c
        .context, c.builder, typ, val)
    owjq__xlxtm = cgutils.create_struct_proxy(typ)(context, builder, value=val)
    n_cols = len(typ.columns) if not typ.has_runtime_cols else None
    obj = owjq__xlxtm.parent
    res = cgutils.alloca_once_value(builder, obj)
    use_parent_obj = _get_use_df_parent_obj_flag(builder, context, pyapi,
        obj, n_cols)
    _create_initial_df_object(builder, context, pyapi, c, typ, obj,
        dataframe_payload, res, use_parent_obj)
    if typ.is_table_format:
        zwet__hatkk = typ.table_type
        hohw__gbvfn = builder.extract_value(dataframe_payload.data, 0)
        context.nrt.incref(builder, zwet__hatkk, hohw__gbvfn)
        jrihh__bme = box_table(zwet__hatkk, hohw__gbvfn, c, builder.not_(
            use_parent_obj))
        with builder.if_else(use_parent_obj) as (dec__whtnz, olani__mzm):
            with dec__whtnz:
                wsma__nrt = pyapi.object_getattr_string(jrihh__bme, 'arrays')
                oqe__luq = c.pyapi.make_none()
                if n_cols is None:
                    lxq__ptd = pyapi.call_method(wsma__nrt, '__len__', ())
                    gqsgq__tpbv = pyapi.long_as_longlong(lxq__ptd)
                    pyapi.decref(lxq__ptd)
                else:
                    gqsgq__tpbv = context.get_constant(types.int64, n_cols)
                with cgutils.for_range(builder, gqsgq__tpbv) as ler__tpuqq:
                    i = ler__tpuqq.index
                    plbk__hwcz = pyapi.list_getitem(wsma__nrt, i)
                    pfjwk__rqhq = c.builder.icmp_unsigned('!=', plbk__hwcz,
                        oqe__luq)
                    with builder.if_then(pfjwk__rqhq):
                        nfiju__rxtt = pyapi.long_from_longlong(i)
                        df_obj = builder.load(res)
                        pyapi.object_setitem(df_obj, nfiju__rxtt, plbk__hwcz)
                        pyapi.decref(nfiju__rxtt)
                pyapi.decref(wsma__nrt)
                pyapi.decref(oqe__luq)
            with olani__mzm:
                df_obj = builder.load(res)
                upk__njfus = pyapi.object_getattr_string(df_obj, 'index')
                syf__stif = c.pyapi.call_method(jrihh__bme, 'to_pandas', (
                    upk__njfus,))
                builder.store(syf__stif, res)
                pyapi.decref(df_obj)
                pyapi.decref(upk__njfus)
        pyapi.decref(jrihh__bme)
    else:
        vsd__kkc = [builder.extract_value(dataframe_payload.data, i) for i in
            range(n_cols)]
        okyh__mstig = typ.data
        for i, arr, pot__qpja in zip(range(n_cols), vsd__kkc, okyh__mstig):
            rio__rgfe = cgutils.alloca_once_value(builder, arr)
            jzz__kqpmq = cgutils.alloca_once_value(builder, context.
                get_constant_null(pot__qpja))
            pfjwk__rqhq = builder.not_(is_ll_eq(builder, rio__rgfe, jzz__kqpmq)
                )
            kme__jsn = builder.or_(builder.not_(use_parent_obj), builder.
                and_(use_parent_obj, pfjwk__rqhq))
            with builder.if_then(kme__jsn):
                nfiju__rxtt = pyapi.long_from_longlong(context.get_constant
                    (types.int64, i))
                context.nrt.incref(builder, pot__qpja, arr)
                arr_obj = pyapi.from_native_value(pot__qpja, arr, c.env_manager
                    )
                df_obj = builder.load(res)
                pyapi.object_setitem(df_obj, nfiju__rxtt, arr_obj)
                pyapi.decref(arr_obj)
                pyapi.decref(nfiju__rxtt)
    df_obj = builder.load(res)
    tazk__bmwnc = _get_df_columns_obj(c, builder, context, pyapi, typ,
        dataframe_payload)
    pyapi.object_setattr_string(df_obj, 'columns', tazk__bmwnc)
    pyapi.decref(tazk__bmwnc)
    _set_bodo_meta_dataframe(c, df_obj, typ)
    c.context.nrt.decref(c.builder, typ, val)
    return df_obj


def get_df_obj_column_codegen(context, builder, pyapi, df_obj, col_ind,
    data_typ):
    oqe__luq = pyapi.borrow_none()
    cqf__igwdl = pyapi.unserialize(pyapi.serialize_object(slice))
    dha__rvsn = pyapi.call_function_objargs(cqf__igwdl, [oqe__luq])
    uhvtp__mzr = pyapi.long_from_longlong(col_ind)
    weblg__avhk = pyapi.tuple_pack([dha__rvsn, uhvtp__mzr])
    red__ruewg = pyapi.object_getattr_string(df_obj, 'iloc')
    usb__lwx = pyapi.object_getitem(red__ruewg, weblg__avhk)
    sldp__wku = pyapi.object_getattr_string(usb__lwx, 'array')
    hkvb__cjzft = pyapi.unserialize(pyapi.serialize_object(unwrap_pd_arr))
    arr_obj = pyapi.call_function_objargs(hkvb__cjzft, [sldp__wku])
    pyapi.decref(sldp__wku)
    pyapi.decref(hkvb__cjzft)
    pyapi.decref(cqf__igwdl)
    pyapi.decref(dha__rvsn)
    pyapi.decref(uhvtp__mzr)
    pyapi.decref(weblg__avhk)
    pyapi.decref(red__ruewg)
    pyapi.decref(usb__lwx)
    return arr_obj


@intrinsic
def unbox_dataframe_column(typingctx, df, i=None):
    assert isinstance(df, DataFrameType) and is_overload_constant_int(i)

    def codegen(context, builder, sig, args):
        pyapi = context.get_python_api(builder)
        c = numba.core.pythonapi._UnboxContext(context, builder, pyapi)
        df_typ = sig.args[0]
        col_ind = get_overload_const_int(sig.args[1])
        data_typ = df_typ.data[col_ind]
        owjq__xlxtm = cgutils.create_struct_proxy(sig.args[0])(context,
            builder, value=args[0])
        arr_obj = get_df_obj_column_codegen(context, builder, pyapi,
            owjq__xlxtm.parent, args[1], data_typ)
        fidnu__aes = _unbox_series_data(data_typ.dtype, data_typ, arr_obj, c)
        c.pyapi.decref(arr_obj)
        dataframe_payload = (bodo.hiframes.pd_dataframe_ext.
            get_dataframe_payload(c.context, c.builder, df_typ, args[0]))
        if df_typ.is_table_format:
            hohw__gbvfn = cgutils.create_struct_proxy(df_typ.table_type)(c.
                context, c.builder, builder.extract_value(dataframe_payload
                .data, 0))
            wwumq__zcv = df_typ.table_type.type_to_blk[data_typ]
            ako__ati = getattr(hohw__gbvfn, f'block_{wwumq__zcv}')
            outyi__rqt = ListInstance(c.context, c.builder, types.List(
                data_typ), ako__ati)
            pjx__fpl = context.get_constant(types.int64, df_typ.table_type.
                block_offsets[col_ind])
            outyi__rqt.inititem(pjx__fpl, fidnu__aes.value, incref=False)
        else:
            dataframe_payload.data = builder.insert_value(dataframe_payload
                .data, fidnu__aes.value, col_ind)
        yvrjz__ecoav = DataFramePayloadType(df_typ)
        zyg__lfd = context.nrt.meminfo_data(builder, owjq__xlxtm.meminfo)
        txar__qbf = context.get_value_type(yvrjz__ecoav).as_pointer()
        zyg__lfd = builder.bitcast(zyg__lfd, txar__qbf)
        builder.store(dataframe_payload._getvalue(), zyg__lfd)
    return signature(types.none, df, i), codegen


@numba.njit
def unbox_col_if_needed(df, i):
    if bodo.hiframes.pd_dataframe_ext.has_parent(df
        ) and bodo.hiframes.pd_dataframe_ext._column_needs_unboxing(df, i):
        bodo.hiframes.boxing.unbox_dataframe_column(df, i)


@unbox(SeriesType)
def unbox_series(typ, val, c):
    sldp__wku = c.pyapi.object_getattr_string(val, 'array')
    hkvb__cjzft = c.pyapi.unserialize(c.pyapi.serialize_object(unwrap_pd_arr))
    arr_obj = c.pyapi.call_function_objargs(hkvb__cjzft, [sldp__wku])
    zjc__ddztf = _unbox_series_data(typ.dtype, typ.data, arr_obj, c).value
    upk__njfus = c.pyapi.object_getattr_string(val, 'index')
    aszo__rrs = c.pyapi.to_native_value(typ.index, upk__njfus).value
    eulf__yek = c.pyapi.object_getattr_string(val, 'name')
    gsw__yiaa = c.pyapi.to_native_value(typ.name_typ, eulf__yek).value
    nnv__pnuz = bodo.hiframes.pd_series_ext.construct_series(c.context, c.
        builder, typ, zjc__ddztf, aszo__rrs, gsw__yiaa)
    c.pyapi.decref(hkvb__cjzft)
    c.pyapi.decref(sldp__wku)
    c.pyapi.decref(arr_obj)
    c.pyapi.decref(upk__njfus)
    c.pyapi.decref(eulf__yek)
    return NativeValue(nnv__pnuz)


def _unbox_series_data(dtype, data_typ, arr_obj, c):
    if data_typ == string_array_split_view_type:
        anv__slkj = c.context.make_helper(c.builder,
            string_array_split_view_type)
        return NativeValue(anv__slkj._getvalue())
    return c.pyapi.to_native_value(data_typ, arr_obj)


@box(HeterogeneousSeriesType)
@box(SeriesType)
def box_series(typ, val, c):
    emhal__ppyk = c.context.insert_const_string(c.builder.module, 'pandas')
    ygibt__gmnn = c.pyapi.import_module_noblock(emhal__ppyk)
    qiwtb__ucl = bodo.hiframes.pd_series_ext.get_series_payload(c.context,
        c.builder, typ, val)
    c.context.nrt.incref(c.builder, typ.data, qiwtb__ucl.data)
    c.context.nrt.incref(c.builder, typ.index, qiwtb__ucl.index)
    c.context.nrt.incref(c.builder, typ.name_typ, qiwtb__ucl.name)
    arr_obj = c.pyapi.from_native_value(typ.data, qiwtb__ucl.data, c.
        env_manager)
    upk__njfus = c.pyapi.from_native_value(typ.index, qiwtb__ucl.index, c.
        env_manager)
    eulf__yek = c.pyapi.from_native_value(typ.name_typ, qiwtb__ucl.name, c.
        env_manager)
    if isinstance(typ, HeterogeneousSeriesType) and isinstance(typ.data,
        bodo.NullableTupleType):
        dtype = c.pyapi.unserialize(c.pyapi.serialize_object(object))
    else:
        dtype = c.pyapi.make_none()
    res = c.pyapi.call_method(ygibt__gmnn, 'Series', (arr_obj, upk__njfus,
        dtype, eulf__yek))
    c.pyapi.decref(arr_obj)
    c.pyapi.decref(upk__njfus)
    c.pyapi.decref(eulf__yek)
    if isinstance(typ, HeterogeneousSeriesType) and isinstance(typ.data,
        bodo.NullableTupleType):
        c.pyapi.decref(dtype)
    _set_bodo_meta_series(res, c, typ)
    c.pyapi.decref(ygibt__gmnn)
    c.context.nrt.decref(c.builder, typ, val)
    return res


def type_enum_list_to_py_list_obj(pyapi, context, builder, env_manager,
    typ_list):
    idsh__lpplr = []
    for plcur__zouwh in typ_list:
        if isinstance(plcur__zouwh, int) and not isinstance(plcur__zouwh, bool
            ):
            tebfk__csi = pyapi.long_from_longlong(lir.Constant(lir.IntType(
                64), plcur__zouwh))
        else:
            aftia__uucex = numba.typeof(plcur__zouwh)
            eidca__nzef = context.get_constant_generic(builder,
                aftia__uucex, plcur__zouwh)
            tebfk__csi = pyapi.from_native_value(aftia__uucex, eidca__nzef,
                env_manager)
        idsh__lpplr.append(tebfk__csi)
    vfpe__rmi = pyapi.list_pack(idsh__lpplr)
    for val in idsh__lpplr:
        pyapi.decref(val)
    return vfpe__rmi


def _set_bodo_meta_dataframe(c, obj, typ):
    pyapi = c.pyapi
    context = c.context
    builder = c.builder
    ongta__rgvu = not typ.has_runtime_cols
    jmq__sdll = 2 if ongta__rgvu else 1
    nvwe__qvrcv = pyapi.dict_new(jmq__sdll)
    ielfv__yvpm = pyapi.long_from_longlong(lir.Constant(lir.IntType(64),
        typ.dist.value))
    pyapi.dict_setitem_string(nvwe__qvrcv, 'dist', ielfv__yvpm)
    pyapi.decref(ielfv__yvpm)
    if ongta__rgvu:
        frka__zzqqu = _dtype_to_type_enum_list(typ.index)
        if frka__zzqqu != None:
            cjmt__jxgt = type_enum_list_to_py_list_obj(pyapi, context,
                builder, c.env_manager, frka__zzqqu)
        else:
            cjmt__jxgt = pyapi.make_none()
        if typ.is_table_format:
            ivl__ybwc = typ.table_type
            mcmy__vwx = pyapi.list_new(lir.Constant(lir.IntType(64), len(
                typ.data)))
            for wwumq__zcv, dtype in ivl__ybwc.blk_to_type.items():
                typ_list = _dtype_to_type_enum_list(dtype)
                if typ_list != None:
                    typ_list = type_enum_list_to_py_list_obj(pyapi, context,
                        builder, c.env_manager, typ_list)
                else:
                    typ_list = pyapi.make_none()
                gqsgq__tpbv = c.context.get_constant(types.int64, len(
                    ivl__ybwc.block_to_arr_ind[wwumq__zcv]))
                dyvwr__wyyw = c.context.make_constant_array(c.builder,
                    types.Array(types.int64, 1, 'C'), np.array(ivl__ybwc.
                    block_to_arr_ind[wwumq__zcv], dtype=np.int64))
                ytpwc__iszpx = c.context.make_array(types.Array(types.int64,
                    1, 'C'))(c.context, c.builder, dyvwr__wyyw)
                with cgutils.for_range(c.builder, gqsgq__tpbv) as ler__tpuqq:
                    i = ler__tpuqq.index
                    aajum__azr = _getitem_array_single_int(c.context, c.
                        builder, types.int64, types.Array(types.int64, 1,
                        'C'), ytpwc__iszpx, i)
                    c.context.nrt.incref(builder, types.pyobject, typ_list)
                    pyapi.list_setitem(mcmy__vwx, aajum__azr, typ_list)
                c.context.nrt.decref(builder, types.pyobject, typ_list)
        else:
            qrvgd__rrfhw = []
            for dtype in typ.data:
                typ_list = _dtype_to_type_enum_list(dtype)
                if typ_list != None:
                    vfpe__rmi = type_enum_list_to_py_list_obj(pyapi,
                        context, builder, c.env_manager, typ_list)
                else:
                    vfpe__rmi = pyapi.make_none()
                qrvgd__rrfhw.append(vfpe__rmi)
            mcmy__vwx = pyapi.list_pack(qrvgd__rrfhw)
            for val in qrvgd__rrfhw:
                pyapi.decref(val)
        zrtf__fah = pyapi.list_pack([cjmt__jxgt, mcmy__vwx])
        pyapi.dict_setitem_string(nvwe__qvrcv, 'type_metadata', zrtf__fah)
    pyapi.object_setattr_string(obj, '_bodo_meta', nvwe__qvrcv)
    pyapi.decref(nvwe__qvrcv)


def get_series_dtype_handle_null_int_and_hetrogenous(series_typ):
    if isinstance(series_typ, HeterogeneousSeriesType):
        return None
    if isinstance(series_typ.dtype, types.Number) and isinstance(series_typ
        .data, IntegerArrayType):
        return IntDtype(series_typ.dtype)
    if isinstance(series_typ.dtype, types.Float) and isinstance(series_typ.
        data, FloatingArrayType):
        return FloatDtype(series_typ.dtype)
    return series_typ.dtype


def _set_bodo_meta_series(obj, c, typ):
    pyapi = c.pyapi
    context = c.context
    builder = c.builder
    nvwe__qvrcv = pyapi.dict_new(2)
    ielfv__yvpm = pyapi.long_from_longlong(lir.Constant(lir.IntType(64),
        typ.dist.value))
    frka__zzqqu = _dtype_to_type_enum_list(typ.index)
    if frka__zzqqu != None:
        cjmt__jxgt = type_enum_list_to_py_list_obj(pyapi, context, builder,
            c.env_manager, frka__zzqqu)
    else:
        cjmt__jxgt = pyapi.make_none()
    dtype = get_series_dtype_handle_null_int_and_hetrogenous(typ)
    if dtype != None:
        typ_list = _dtype_to_type_enum_list(dtype)
        if typ_list != None:
            gvzwa__fbnzg = type_enum_list_to_py_list_obj(pyapi, context,
                builder, c.env_manager, typ_list)
        else:
            gvzwa__fbnzg = pyapi.make_none()
    else:
        gvzwa__fbnzg = pyapi.make_none()
    narsz__ora = pyapi.list_pack([cjmt__jxgt, gvzwa__fbnzg])
    pyapi.dict_setitem_string(nvwe__qvrcv, 'type_metadata', narsz__ora)
    pyapi.decref(narsz__ora)
    pyapi.dict_setitem_string(nvwe__qvrcv, 'dist', ielfv__yvpm)
    pyapi.object_setattr_string(obj, '_bodo_meta', nvwe__qvrcv)
    pyapi.decref(nvwe__qvrcv)
    pyapi.decref(ielfv__yvpm)


@typeof_impl.register(np.ndarray)
def _typeof_ndarray(val, c):
    try:
        dtype = numba.np.numpy_support.from_dtype(val.dtype)
    except NotImplementedError as idzp__oli:
        dtype = types.pyobject
    if dtype == types.pyobject:
        return _infer_ndarray_obj_dtype(val)
    ysm__qhh = numba.np.numpy_support.map_layout(val)
    cdpre__zlrq = not val.flags.writeable
    return types.Array(dtype, val.ndim, ysm__qhh, readonly=cdpre__zlrq)


def _infer_ndarray_obj_dtype(val):
    if not val.dtype == np.dtype('O'):
        raise BodoError('Unsupported array dtype: {}'.format(val.dtype))
    i = 0
    while i < len(val) and (pd.api.types.is_scalar(val[i]) and pd.isna(val[
        i]) or not pd.api.types.is_scalar(val[i]) and len(val[i]) == 0):
        i += 1
    if i == len(val):
        warnings.warn(BodoWarning(
            'Empty object array passed to Bodo, which causes ambiguity in typing. This can cause errors in parallel execution.'
            ))
        return (bodo.dict_str_arr_type if _use_dict_str_type else
            string_array_type)
    hhdvq__nvo = val[i]
    bhd__kjuz = 100
    if isinstance(hhdvq__nvo, str):
        return (bodo.dict_str_arr_type if _use_dict_str_type else
            string_array_type)
    elif isinstance(hhdvq__nvo, (bytes, bytearray)):
        return binary_array_type
    elif isinstance(hhdvq__nvo, bool):
        return bodo.libs.bool_arr_ext.boolean_array
    elif isinstance(hhdvq__nvo, (int, np.int8, np.int16, np.int32, np.int64,
        np.uint8, np.uint16, np.uint32, np.uint64)):
        return bodo.libs.int_arr_ext.IntegerArrayType(numba.typeof(hhdvq__nvo))
    elif isinstance(hhdvq__nvo, (float, np.float32, np.float64)):
        return bodo.libs.float_arr_ext.FloatingArrayType(numba.typeof(
            hhdvq__nvo))
    elif isinstance(hhdvq__nvo, (dict, Dict)) and len(hhdvq__nvo.keys()
        ) <= bhd__kjuz and all(isinstance(rvmy__neg, str) for rvmy__neg in
        hhdvq__nvo.keys()):
        lex__ovql = tuple(hhdvq__nvo.keys())
        lgeb__horix = tuple(_get_struct_value_arr_type(v) for v in
            hhdvq__nvo.values())
        return StructArrayType(lgeb__horix, lex__ovql)
    elif isinstance(hhdvq__nvo, (dict, Dict)):
        bbjxy__ximn = numba.typeof(_value_to_array(list(hhdvq__nvo.keys())))
        vlvoy__cfg = numba.typeof(_value_to_array(list(hhdvq__nvo.values())))
        bbjxy__ximn = to_str_arr_if_dict_array(bbjxy__ximn)
        vlvoy__cfg = to_str_arr_if_dict_array(vlvoy__cfg)
        return MapArrayType(bbjxy__ximn, vlvoy__cfg)
    elif isinstance(hhdvq__nvo, tuple):
        lgeb__horix = tuple(_get_struct_value_arr_type(v) for v in hhdvq__nvo)
        return TupleArrayType(lgeb__horix)
    if isinstance(hhdvq__nvo, (list, np.ndarray, pd.arrays.BooleanArray, pd
        .arrays.IntegerArray, pd.arrays.FloatingArray, pd.arrays.
        StringArray, pd.arrays.ArrowStringArray)):
        if isinstance(hhdvq__nvo, list):
            hhdvq__nvo = _value_to_array(hhdvq__nvo)
        sdxek__ivtio = numba.typeof(hhdvq__nvo)
        sdxek__ivtio = to_str_arr_if_dict_array(sdxek__ivtio)
        return ArrayItemArrayType(sdxek__ivtio)
    if isinstance(hhdvq__nvo, datetime.date):
        return datetime_date_array_type
    if isinstance(hhdvq__nvo, datetime.timedelta):
        return datetime_timedelta_array_type
    if isinstance(hhdvq__nvo, bodo.Time):
        return TimeArrayType(hhdvq__nvo.precision)
    if isinstance(hhdvq__nvo, decimal.Decimal):
        return DecimalArrayType(38, 18)
    if isinstance(hhdvq__nvo, pd._libs.interval.Interval):
        return bodo.libs.interval_arr_ext.IntervalArrayType
    raise BodoError(f'Unsupported object array with first value: {hhdvq__nvo}')


def _value_to_array(val):
    assert isinstance(val, (list, dict, Dict))
    if isinstance(val, (dict, Dict)):
        val = dict(val)
        return np.array([val], np.object_)
    gfb__oscrn = val.copy()
    gfb__oscrn.append(None)
    arr = np.array(gfb__oscrn, np.object_)
    if len(val) and isinstance(val[0], float):
        arr = np.array(val, np.float64)
    return arr


def _get_struct_value_arr_type(v):
    if isinstance(v, (dict, Dict)):
        return numba.typeof(_value_to_array(v))
    if isinstance(v, list):
        return dtype_to_array_type(numba.typeof(_value_to_array(v)))
    if pd.api.types.is_scalar(v) and pd.isna(v):
        warnings.warn(BodoWarning(
            'Field value in struct array is NA, which causes ambiguity in typing. This can cause errors in parallel execution.'
            ))
        return string_array_type
    pot__qpja = dtype_to_array_type(numba.typeof(v))
    if isinstance(v, (int, bool)):
        pot__qpja = to_nullable_type(pot__qpja)
    return pot__qpja
