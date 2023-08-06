"""Numba extension support for time objects and their arrays.
"""
import operator
import llvmlite.binding as ll
import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.imputils import lower_builtin, lower_constant
from numba.extending import NativeValue, box, intrinsic, lower_builtin, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_model, typeof_impl, unbox
from numba.parfors.array_analysis import ArrayAnalysis
import bodo
from bodo.libs import hdatetime_ext
from bodo.utils.indexing import array_getitem_bool_index, array_getitem_int_index, array_getitem_slice_index, array_setitem_bool_index, array_setitem_int_index, array_setitem_slice_index
from bodo.utils.typing import BodoError, is_iterable_type, is_list_like_index_type
_nanos_per_micro = 1000
_nanos_per_milli = 1000 * _nanos_per_micro
_nanos_per_second = 1000 * _nanos_per_milli
_nanos_per_minute = 60 * _nanos_per_second
_nanos_per_hour = 60 * _nanos_per_minute


class Time:

    def __init__(self, hour=0, minute=0, second=0, millisecond=0,
        microsecond=0, nanosecond=0, precision=9):
        self.precision = precision
        assert all(np.issubdtype(type(val), np.integer) or pd.api.types.
            is_int64_dtype(val) for val in (hour, minute, second,
            millisecond, microsecond, nanosecond)
            ), 'All time components must be integers'
        self.value = np.int64(hour * _nanos_per_hour + minute *
            _nanos_per_minute + second * _nanos_per_second + millisecond *
            _nanos_per_milli + microsecond * _nanos_per_micro + nanosecond)

    def __repr__(self):
        return (
            f'Time(hour={self.hour}, minute={self.minute}, second={self.second}, millisecond={self.millisecond}, microsecond={self.microsecond}, nanosecond={self.nanosecond}, precision={self.precision})'
            )

    def __str__(self):
        return (
            f'{self.hour}:{self.minute}:{self.second}.{self.microsecond}{self.nanosecond}'
            )

    def __eq__(self, other):
        if not isinstance(other, Time):
            return False
        return self.value == other.value and self.precision == other.precision

    def _check_can_compare(self, other):
        if isinstance(other, Time):
            if self.precision != other.precision:
                raise TypeError(
                    f'Cannot compare times with different precisions: {self} and {other}'
                    )
        else:
            raise TypeError('Cannot compare Time with non-Time type')

    def __lt__(self, other):
        self._check_can_compare(other)
        return self.value < other.value

    def __le__(self, other):
        self._check_can_compare(other)
        return self.value <= other.value

    def __int__(self):
        if self.precision == 9:
            return self.value
        if self.precision == 6:
            return self.value // _nanos_per_micro
        if self.precision == 3:
            return self.value // _nanos_per_milli
        if self.precision == 0:
            return self.value // _nanos_per_second
        raise BodoError(f'Unsupported precision: {self.precision}')

    def __hash__(self):
        return hash((self.value, self.precision))

    @property
    def hour(self):
        return self.value // _nanos_per_hour

    @property
    def minute(self):
        return self.value % _nanos_per_hour // _nanos_per_minute

    @property
    def second(self):
        return self.value % _nanos_per_minute // _nanos_per_second

    @property
    def millisecond(self):
        return self.value % _nanos_per_second // _nanos_per_milli

    @property
    def microsecond(self):
        return self.value % _nanos_per_milli // _nanos_per_micro

    @property
    def nanosecond(self):
        return self.value % _nanos_per_micro


def time_from_str(time_str, precision=9):
    hour = 0
    minute = 0
    second = 0
    millisecond = 0
    microsecond = 0
    nanosecond = 0
    hour = int(time_str[:2])
    assert time_str[2] == ':', 'Invalid time string'
    minute = int(time_str[3:5])
    assert time_str[5] == ':', 'Invalid time string'
    second = int(time_str[6:8])
    if len(time_str) > 8:
        assert time_str[8] == '.', 'Invalid time string'
        millisecond = int(time_str[9:12])
        if len(time_str) > 12:
            microsecond = int(time_str[12:15])
            if len(time_str) > 15:
                nanosecond = int(time_str[15:18])
    return Time(hour, minute, second, millisecond, microsecond, nanosecond,
        precision=precision)


@overload(time_from_str)
def overload_time_from_str(time_str, precision=9):
    return time_from_str


ll.add_symbol('box_time_array', hdatetime_ext.box_time_array)
ll.add_symbol('unbox_time_array', hdatetime_ext.unbox_time_array)


class TimeType(types.Type):

    def __init__(self, precision):
        assert isinstance(precision, int
            ) and precision >= 0 and precision <= 9, 'precision must be an integer between 0 and 9'
        self.precision = precision
        super(TimeType, self).__init__(name=f'TimeType({precision})')
        self.bitwidth = 64


@typeof_impl.register(Time)
def typeof_time(val, c):
    return TimeType(val.precision)


@overload(Time)
def overload_time(hour=0, min=0, second=0, millisecond=0, microsecond=0,
    nanosecond=0, precision=9):
    if isinstance(hour, types.Integer) or isinstance(hour, types.IntegerLiteral
        ) or hour == 0:

        def impl(hour=0, min=0, second=0, millisecond=0, microsecond=0,
            nanosecond=0, precision=9):
            return cast_int_to_time(_nanos_per_hour * hour + 
                _nanos_per_minute * min + _nanos_per_second * second + 
                _nanos_per_milli * millisecond + _nanos_per_micro *
                microsecond + nanosecond, precision)
    else:
        raise TypeError(f'Invalid type for Time: {type(hour)}')
    return impl


register_model(TimeType)(models.IntegerModel)


@overload_attribute(TimeType, 'hour')
def time_hour_attribute(val):
    return lambda val: cast_time_to_int(val) // _nanos_per_hour


@overload_attribute(TimeType, 'minute')
def time_minute_attribute(val):
    return lambda val: cast_time_to_int(val
        ) % _nanos_per_hour // _nanos_per_minute


@overload_attribute(TimeType, 'second')
def time_second_attribute(val):
    return lambda val: cast_time_to_int(val
        ) % _nanos_per_minute // _nanos_per_second


@overload_attribute(TimeType, 'millisecond')
def time_millisecond_attribute(val):
    return lambda val: cast_time_to_int(val
        ) % _nanos_per_second // _nanos_per_milli


@overload_attribute(TimeType, 'microsecond')
def time_microsecond_attribute(val):
    return lambda val: cast_time_to_int(val
        ) % _nanos_per_milli // _nanos_per_micro


@overload_attribute(TimeType, 'nanosecond')
def time_nanosecond_attribute(val):
    return lambda val: cast_time_to_int(val) % _nanos_per_micro


def _to_nanos_codegen(c, hour_ll, minute_ll, second_ll, millisecond_ll,
    microsecond_ll, nanosecond_ll):
    return c.builder.add(nanosecond_ll, c.builder.add(c.builder.mul(
        microsecond_ll, lir.Constant(lir.IntType(64), _nanos_per_micro)), c
        .builder.add(c.builder.mul(millisecond_ll, lir.Constant(lir.IntType
        (64), _nanos_per_milli)), c.builder.add(c.builder.mul(second_ll,
        lir.Constant(lir.IntType(64), _nanos_per_second)), c.builder.add(c.
        builder.mul(minute_ll, lir.Constant(lir.IntType(64),
        _nanos_per_minute)), c.builder.mul(hour_ll, lir.Constant(lir.
        IntType(64), _nanos_per_hour)))))))


def _from_nanos_codegen(c, val):
    nnxl__boa = c.pyapi.long_from_longlong(c.builder.udiv(val, lir.Constant
        (lir.IntType(64), _nanos_per_hour)))
    fce__qmfu = c.pyapi.long_from_longlong(c.builder.udiv(c.builder.urem(
        val, lir.Constant(lir.IntType(64), _nanos_per_hour)), lir.Constant(
        lir.IntType(64), _nanos_per_minute)))
    unhrw__aziy = c.pyapi.long_from_longlong(c.builder.udiv(c.builder.urem(
        val, lir.Constant(lir.IntType(64), _nanos_per_minute)), lir.
        Constant(lir.IntType(64), _nanos_per_second)))
    afh__mwu = c.pyapi.long_from_longlong(c.builder.udiv(c.builder.urem(val,
        lir.Constant(lir.IntType(64), _nanos_per_second)), lir.Constant(lir
        .IntType(64), _nanos_per_milli)))
    eienl__zwel = c.pyapi.long_from_longlong(c.builder.udiv(c.builder.urem(
        val, lir.Constant(lir.IntType(64), _nanos_per_milli)), lir.Constant
        (lir.IntType(64), _nanos_per_micro)))
    vifp__uhcl = c.pyapi.long_from_longlong(c.builder.urem(val, lir.
        Constant(lir.IntType(64), _nanos_per_micro)))
    return nnxl__boa, fce__qmfu, unhrw__aziy, afh__mwu, eienl__zwel, vifp__uhcl


@unbox(TimeType)
def unbox_time(typ, val, c):
    nnxl__boa = c.pyapi.object_getattr_string(val, 'hour')
    fce__qmfu = c.pyapi.object_getattr_string(val, 'minute')
    unhrw__aziy = c.pyapi.object_getattr_string(val, 'second')
    afh__mwu = c.pyapi.object_getattr_string(val, 'millisecond')
    eienl__zwel = c.pyapi.object_getattr_string(val, 'microsecond')
    vifp__uhcl = c.pyapi.object_getattr_string(val, 'nanosecond')
    hour_ll = c.pyapi.long_as_longlong(nnxl__boa)
    minute_ll = c.pyapi.long_as_longlong(fce__qmfu)
    second_ll = c.pyapi.long_as_longlong(unhrw__aziy)
    millisecond_ll = c.pyapi.long_as_longlong(afh__mwu)
    microsecond_ll = c.pyapi.long_as_longlong(eienl__zwel)
    nanosecond_ll = c.pyapi.long_as_longlong(vifp__uhcl)
    btpf__eiq = _to_nanos_codegen(c, hour_ll, minute_ll, second_ll,
        millisecond_ll, microsecond_ll, nanosecond_ll)
    c.pyapi.decref(nnxl__boa)
    c.pyapi.decref(fce__qmfu)
    c.pyapi.decref(unhrw__aziy)
    c.pyapi.decref(afh__mwu)
    c.pyapi.decref(eienl__zwel)
    c.pyapi.decref(vifp__uhcl)
    orls__wbc = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(btpf__eiq, is_error=orls__wbc)


@lower_constant(TimeType)
def lower_constant_time(context, builder, ty, pyval):
    hour_ll = context.get_constant(types.int64, pyval.hour)
    minute_ll = context.get_constant(types.int64, pyval.minute)
    second_ll = context.get_constant(types.int64, pyval.second)
    millisecond_ll = context.get_constant(types.int64, pyval.millisecond)
    microsecond_ll = context.get_constant(types.int64, pyval.microsecond)
    nanosecond_ll = context.get_constant(types.int64, pyval.nanosecond)
    btpf__eiq = _to_nanos_codegen(context, hour_ll, minute_ll, second_ll,
        millisecond_ll, microsecond_ll, nanosecond_ll)
    return btpf__eiq


@box(TimeType)
def box_time(typ, val, c):
    (nnxl__boa, fce__qmfu, unhrw__aziy, afh__mwu, eienl__zwel, vifp__uhcl
        ) = _from_nanos_codegen(c, val)
    jbr__jlkc = c.pyapi.unserialize(c.pyapi.serialize_object(Time))
    uwtv__cqbzm = c.pyapi.call_function_objargs(jbr__jlkc, (nnxl__boa,
        fce__qmfu, unhrw__aziy, afh__mwu, eienl__zwel, vifp__uhcl, c.pyapi.
        long_from_longlong(lir.Constant(lir.IntType(64), typ.precision))))
    c.pyapi.decref(nnxl__boa)
    c.pyapi.decref(fce__qmfu)
    c.pyapi.decref(unhrw__aziy)
    c.pyapi.decref(afh__mwu)
    c.pyapi.decref(eienl__zwel)
    c.pyapi.decref(vifp__uhcl)
    c.pyapi.decref(jbr__jlkc)
    return uwtv__cqbzm


@lower_builtin(Time, types.int64, types.int64, types.int64, types.int64,
    types.int64, types.int64)
def impl_ctor_time(context, builder, sig, args):
    (hour_ll, minute_ll, second_ll, millisecond_ll, microsecond_ll,
        nanosecond_ll) = args
    btpf__eiq = _to_nanos_codegen(context, hour_ll, minute_ll, second_ll,
        millisecond_ll, microsecond_ll, nanosecond_ll)
    return btpf__eiq


@intrinsic
def cast_int_to_time(typingctx, val, precision):
    assert types.unliteral(val) == types.int64, 'val must be int64'
    assert isinstance(precision, types.IntegerLiteral
        ), 'precision must be an integer literal'

    def codegen(context, builder, signature, args):
        return args[0]
    return TimeType(precision.literal_value)(types.int64, types.int64), codegen


@intrinsic
def cast_time_to_int(typingctx, val):
    assert isinstance(val, TimeType), 'val must be Time'

    def codegen(context, builder, signature, args):
        return args[0]
    return types.int64(val), codegen


class TimeArrayType(types.ArrayCompatible):

    def __init__(self, precision):
        assert isinstance(precision, int
            ) and precision >= 0 and precision <= 9, 'precision must be an integer between 0 and 9'
        self.precision = precision
        super(TimeArrayType, self).__init__(name=f'TimeArrayType({precision})')

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    @property
    def dtype(self):
        return TimeType(self.precision)

    def copy(self):
        return TimeArrayType(self.precision)


data_type = types.Array(types.int64, 1, 'C')
nulls_type = types.Array(types.uint8, 1, 'C')


@register_model(TimeArrayType)
class TimeArrayModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        fvrq__hsjs = [('data', data_type), ('null_bitmap', nulls_type)]
        models.StructModel.__init__(self, dmm, fe_type, fvrq__hsjs)


make_attribute_wrapper(TimeArrayType, 'data', '_data')
make_attribute_wrapper(TimeArrayType, 'null_bitmap', '_null_bitmap')


@overload_method(TimeArrayType, 'copy', no_unliteral=True)
def overload_time_arr_copy(A):
    precision = A.precision
    """Copy a TimeArrayType by copying the underlying data and null bitmap"""
    return lambda A: bodo.hiframes.time_ext.init_time_array(A._data.copy(),
        A._null_bitmap.copy(), precision)


@overload_attribute(TimeArrayType, 'dtype')
def overload_time_arr_dtype(A):
    return lambda A: np.object_


@unbox(TimeArrayType)
def unbox_time_array(typ, val, c):
    n = bodo.utils.utils.object_length(c, val)
    tktwf__owf = types.Array(types.intp, 1, 'C')
    cxx__fcwbz = bodo.utils.utils._empty_nd_impl(c.context, c.builder,
        tktwf__owf, [n])
    hsw__mjh = c.builder.udiv(c.builder.add(n, lir.Constant(lir.IntType(64),
        7)), lir.Constant(lir.IntType(64), 8))
    iewmt__porj = bodo.utils.utils._empty_nd_impl(c.context, c.builder,
        types.Array(types.uint8, 1, 'C'), [hsw__mjh])
    ojd__ltg = lir.FunctionType(lir.VoidType(), [lir.IntType(8).as_pointer(
        ), lir.IntType(64), lir.IntType(64).as_pointer(), lir.IntType(8).
        as_pointer()])
    ifl__niof = cgutils.get_or_insert_function(c.builder.module, ojd__ltg,
        name='unbox_time_array')
    c.builder.call(ifl__niof, [val, n, cxx__fcwbz.data, iewmt__porj.data])
    tgov__hqvsx = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    tgov__hqvsx.data = cxx__fcwbz._getvalue()
    tgov__hqvsx.null_bitmap = iewmt__porj._getvalue()
    orls__wbc = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(tgov__hqvsx._getvalue(), is_error=orls__wbc)


@box(TimeArrayType)
def box_time_array(typ, val, c):
    qecr__oohry = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    cxx__fcwbz = c.context.make_array(types.Array(types.int64, 1, 'C'))(c.
        context, c.builder, qecr__oohry.data)
    fdngi__kxobq = c.context.make_array(types.Array(types.uint8, 1, 'C'))(c
        .context, c.builder, qecr__oohry.null_bitmap).data
    n = c.builder.extract_value(cxx__fcwbz.shape, 0)
    ojd__ltg = lir.FunctionType(c.pyapi.pyobj, [lir.IntType(64), lir.
        IntType(64).as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(8)])
    zuhro__qyt = cgutils.get_or_insert_function(c.builder.module, ojd__ltg,
        name='box_time_array')
    toci__pzzby = c.builder.call(zuhro__qyt, [n, cxx__fcwbz.data,
        fdngi__kxobq, lir.Constant(lir.IntType(8), typ.precision)])
    c.context.nrt.decref(c.builder, typ, val)
    return toci__pzzby


@intrinsic
def init_time_array(typingctx, data, nulls, precision):
    assert data == types.Array(types.int64, 1, 'C'
        ), 'data must be an array of int64'
    assert nulls == types.Array(types.uint8, 1, 'C'
        ), 'nulls must be an array of uint8'
    assert isinstance(precision, types.IntegerLiteral
        ), 'precision must be an integer literal'

    def codegen(context, builder, signature, args):
        hnnu__ddds, pft__omm, cbts__fgvla = args
        std__thdx = cgutils.create_struct_proxy(signature.return_type)(context,
            builder)
        std__thdx.data = hnnu__ddds
        std__thdx.null_bitmap = pft__omm
        context.nrt.incref(builder, signature.args[0], hnnu__ddds)
        context.nrt.incref(builder, signature.args[1], pft__omm)
        return std__thdx._getvalue()
    sig = TimeArrayType(precision.literal_value)(data, nulls, precision)
    return sig, codegen


@lower_constant(TimeArrayType)
def lower_constant_time_arr(context, builder, typ, pyval):
    n = len(pyval)
    cxx__fcwbz = np.full(n, 0, np.int64)
    rhdj__qexn = np.empty(n + 7 >> 3, np.uint8)
    for dkz__dnwj, yyg__zxu in enumerate(pyval):
        vzra__mbufe = pd.isna(yyg__zxu)
        bodo.libs.int_arr_ext.set_bit_to_arr(rhdj__qexn, dkz__dnwj, int(not
            vzra__mbufe))
        if not vzra__mbufe:
            cxx__fcwbz[dkz__dnwj] = (yyg__zxu.hour * _nanos_per_hour + 
                yyg__zxu.minute * _nanos_per_minute + yyg__zxu.second *
                _nanos_per_second + yyg__zxu.millisecond * _nanos_per_milli +
                yyg__zxu.microsecond * _nanos_per_micro + yyg__zxu.nanosecond)
    ici__msyhg = context.get_constant_generic(builder, data_type, cxx__fcwbz)
    bjvwg__spl = context.get_constant_generic(builder, nulls_type, rhdj__qexn)
    return lir.Constant.literal_struct([ici__msyhg, bjvwg__spl])


@numba.njit(no_cpython_wrapper=True)
def alloc_time_array(n, precision):
    cxx__fcwbz = np.empty(n, dtype=np.int64)
    nulls = np.empty(n + 7 >> 3, dtype=np.uint8)
    return init_time_array(cxx__fcwbz, nulls, precision)


def alloc_time_array_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 2 and not kws, 'alloc_time_array() takes two arguments'
    return ArrayAnalysis.AnalyzeResult(shape=args[0], pre=[])


ArrayAnalysis._analyze_op_call_bodo_hiframes_time_ext_alloc_time_array = (
    alloc_time_array_equiv)


@overload(operator.getitem, no_unliteral=True)
def time_arr_getitem(A, ind):
    if not isinstance(A, TimeArrayType):
        return
    precision = A.precision
    if isinstance(types.unliteral(ind), types.Integer):
        return lambda A, ind: cast_int_to_time(A._data[ind], precision)
    if ind != bodo.boolean_array and is_list_like_index_type(ind
        ) and ind.dtype == types.bool_:

        def impl_bool(A, ind):
            whouv__aifh, owmn__iuk = array_getitem_bool_index(A, ind)
            return init_time_array(whouv__aifh, owmn__iuk, precision)
        return impl_bool
    if is_list_like_index_type(ind) and isinstance(ind.dtype, types.Integer):

        def impl(A, ind):
            whouv__aifh, owmn__iuk = array_getitem_int_index(A, ind)
            return init_time_array(whouv__aifh, owmn__iuk, precision)
        return impl
    if isinstance(ind, types.SliceType):

        def impl_slice(A, ind):
            whouv__aifh, owmn__iuk = array_getitem_slice_index(A, ind)
            return init_time_array(whouv__aifh, owmn__iuk, precision)
        return impl_slice
    if ind != bodo.boolean_array:
        raise BodoError(
            f'getitem for TimeArray with indexing type {ind} not supported.')


@overload(operator.setitem, no_unliteral=True)
def time_arr_setitem(A, idx, val):
    if not isinstance(A, TimeArrayType):
        return
    if val == types.none or isinstance(val, types.optional):
        return
    kqk__fgh = (
        f"setitem for TimeArray with indexing type {idx} received an incorrect 'value' type {val}."
        )
    if isinstance(idx, types.Integer):
        if isinstance(types.unliteral(val), TimeType):

            def impl(A, idx, val):
                A._data[idx] = cast_time_to_int(val)
                bodo.libs.int_arr_ext.set_bit_to_arr(A._null_bitmap, idx, 1)
            return impl
        else:
            raise BodoError(kqk__fgh)
    if not (is_iterable_type(val) and isinstance(val.dtype, TimeType) or
        isinstance(types.unliteral(val), TimeType)):
        raise BodoError(kqk__fgh)
    if is_list_like_index_type(idx) and isinstance(idx.dtype, types.Integer):
        if isinstance(types.unliteral(val), TimeType):
            return lambda A, idx, val: array_setitem_int_index(A, idx,
                cast_time_to_int(val))

        def impl_arr_ind(A, idx, val):
            array_setitem_int_index(A, idx, val)
        return impl_arr_ind
    if is_list_like_index_type(idx) and idx.dtype == types.bool_:
        if isinstance(types.unliteral(val), TimeType):
            return lambda A, idx, val: array_setitem_bool_index(A, idx,
                cast_time_to_int(val))

        def impl_bool_ind_mask(A, idx, val):
            array_setitem_bool_index(A, idx, val)
        return impl_bool_ind_mask
    if isinstance(idx, types.SliceType):
        if isinstance(types.unliteral(val), TimeType):
            return lambda A, idx, val: array_setitem_slice_index(A, idx,
                cast_time_to_int(val))

        def impl_slice_mask(A, idx, val):
            array_setitem_slice_index(A, idx, val)
        return impl_slice_mask
    raise BodoError(
        f'setitem for TimeArray with indexing type {idx} not supported.')


@overload(len, no_unliteral=True)
def overload_len_time_arr(A):
    if isinstance(A, TimeArrayType):
        return lambda A: len(A._data)


@overload_attribute(TimeArrayType, 'shape')
def overload_time_arr_shape(A):
    return lambda A: (len(A._data),)


@overload_attribute(TimeArrayType, 'nbytes')
def time_arr_nbytes_overload(A):
    return lambda A: A._data.nbytes + A._null_bitmap.nbytes


def create_cmp_op_overload(op):

    def overload_time_cmp(lhs, rhs):
        if isinstance(lhs, TimeType) and isinstance(rhs, TimeType):

            def impl(lhs, rhs):
                gsgiz__qmq = cast_time_to_int(lhs)
                ymbj__bqe = cast_time_to_int(rhs)
                return op(0 if gsgiz__qmq == ymbj__bqe else 1 if gsgiz__qmq >
                    ymbj__bqe else -1, 0)
            return impl
    return overload_time_cmp
