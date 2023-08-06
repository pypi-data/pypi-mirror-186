"""
File that contains some IO related helpers.
"""
import os
import threading
import uuid
import numba
import pyarrow as pa
from mpi4py import MPI
from numba.core import types
from numba.core.imputils import lower_constant
from numba.extending import NativeValue, box, models, register_model, typeof_impl, unbox
import bodo
from bodo.hiframes.datetime_date_ext import datetime_date_array_type, datetime_date_type
from bodo.hiframes.pd_categorical_ext import CategoricalArrayType, PDCategoricalDtype
from bodo.hiframes.pd_dataframe_ext import DataFrameType
from bodo.hiframes.time_ext import TimeArrayType, TimeType
from bodo.libs.array_item_arr_ext import ArrayItemArrayType
from bodo.libs.binary_arr_ext import binary_array_type, bytes_type
from bodo.libs.bool_arr_ext import boolean_array
from bodo.libs.decimal_arr_ext import DecimalArrayType
from bodo.libs.dict_arr_ext import dict_str_arr_type
from bodo.libs.float_arr_ext import FloatingArrayType
from bodo.libs.int_arr_ext import IntegerArrayType
from bodo.libs.str_arr_ext import string_array_type
from bodo.libs.str_ext import string_type
from bodo.libs.struct_arr_ext import StructArrayType
from bodo.utils import tracing
from bodo.utils.typing import BodoError, raise_bodo_error


class PyArrowTableSchemaType(types.Opaque):

    def __init__(self):
        super(PyArrowTableSchemaType, self).__init__(name=
            'PyArrowTableSchemaType')


pyarrow_table_schema_type = PyArrowTableSchemaType()
types.pyarrow_table_schema_type = pyarrow_table_schema_type
register_model(PyArrowTableSchemaType)(models.OpaqueModel)


@unbox(PyArrowTableSchemaType)
def unbox_pyarrow_table_schema_type(typ, val, c):
    c.pyapi.incref(val)
    return NativeValue(val)


@box(PyArrowTableSchemaType)
def box_pyarrow_table_schema_type(typ, val, c):
    c.pyapi.incref(val)
    return val


@typeof_impl.register(pa.lib.Schema)
def typeof_pyarrow_table_schema(val, c):
    return pyarrow_table_schema_type


@lower_constant(PyArrowTableSchemaType)
def lower_pyarrow_table_schema(context, builder, ty, pyval):
    qbnqn__zwnvz = context.get_python_api(builder)
    return qbnqn__zwnvz.unserialize(qbnqn__zwnvz.serialize_object(pyval))


def is_nullable(typ):
    return bodo.utils.utils.is_array_typ(typ, False) and (not isinstance(
        typ, types.Array) and not isinstance(typ, bodo.DatetimeArrayType))


def pa_schema_unify_reduction(schema_a, schema_b, unused):
    return pa.unify_schemas([schema_a, schema_b])


pa_schema_unify_mpi_op = MPI.Op.Create(pa_schema_unify_reduction, commute=True)
use_nullable_pd_arr = True
_pyarrow_numba_type_map = {pa.bool_(): types.bool_, pa.int8(): types.int8,
    pa.int16(): types.int16, pa.int32(): types.int32, pa.int64(): types.
    int64, pa.uint8(): types.uint8, pa.uint16(): types.uint16, pa.uint32():
    types.uint32, pa.uint64(): types.uint64, pa.float32(): types.float32,
    pa.float64(): types.float64, pa.string(): string_type, pa.large_string(
    ): string_type, pa.binary(): bytes_type, pa.date32():
    datetime_date_type, pa.date64(): types.NPDatetime('ns'), pa.time32('s'):
    TimeType(0), pa.time32('ms'): TimeType(3), pa.time64('us'): TimeType(6),
    pa.time64('ns'): TimeType(9), pa.null(): string_type}


def get_arrow_timestamp_type(pa_ts_typ):
    ema__ajo = ['ns', 'us', 'ms', 's']
    if pa_ts_typ.unit not in ema__ajo:
        return types.Array(bodo.datetime64ns, 1, 'C'), False
    elif pa_ts_typ.tz is not None:
        dmik__fou = pa_ts_typ.to_pandas_dtype().tz
        hfqk__bxg = bodo.libs.pd_datetime_arr_ext.get_pytz_type_info(dmik__fou)
        return bodo.DatetimeArrayType(hfqk__bxg), True
    else:
        return types.Array(bodo.datetime64ns, 1, 'C'), True


def _get_numba_typ_from_pa_typ(pa_typ: pa.Field, is_index,
    nullable_from_metadata, category_info, str_as_dict=False):
    if isinstance(pa_typ.type, pa.ListType):
        maz__ormp, msmp__eceb = _get_numba_typ_from_pa_typ(pa_typ.type.
            value_field, is_index, nullable_from_metadata, category_info)
        return ArrayItemArrayType(maz__ormp), msmp__eceb
    if isinstance(pa_typ.type, pa.StructType):
        zad__atzfq = []
        mrgzw__pruu = []
        msmp__eceb = True
        for vlms__ocai in pa_typ.flatten():
            mrgzw__pruu.append(vlms__ocai.name.split('.')[-1])
            nap__bmkrr, uqax__vjjk = _get_numba_typ_from_pa_typ(vlms__ocai,
                is_index, nullable_from_metadata, category_info)
            zad__atzfq.append(nap__bmkrr)
            msmp__eceb = msmp__eceb and uqax__vjjk
        return StructArrayType(tuple(zad__atzfq), tuple(mrgzw__pruu)
            ), msmp__eceb
    if isinstance(pa_typ.type, pa.Decimal128Type):
        return DecimalArrayType(pa_typ.type.precision, pa_typ.type.scale), True
    if str_as_dict:
        if pa_typ.type != pa.string():
            raise BodoError(
                f'Read as dictionary used for non-string column {pa_typ}')
        return dict_str_arr_type, True
    if isinstance(pa_typ.type, pa.DictionaryType):
        if pa_typ.type.value_type != pa.string():
            raise BodoError(
                f'Parquet Categorical data type should be string, not {pa_typ.type.value_type}'
                )
        buynj__upmft = _pyarrow_numba_type_map[pa_typ.type.index_type]
        imixv__kfbb = PDCategoricalDtype(category_info[pa_typ.name], bodo.
            string_type, pa_typ.type.ordered, int_type=buynj__upmft)
        return CategoricalArrayType(imixv__kfbb), True
    if isinstance(pa_typ.type, pa.lib.TimestampType):
        return get_arrow_timestamp_type(pa_typ.type)
    elif pa_typ.type in _pyarrow_numba_type_map:
        xlkm__pnd = _pyarrow_numba_type_map[pa_typ.type]
        msmp__eceb = True
    else:
        raise BodoError('Arrow data type {} not supported yet'.format(
            pa_typ.type))
    if xlkm__pnd == datetime_date_type:
        return datetime_date_array_type, msmp__eceb
    if isinstance(xlkm__pnd, TimeType):
        return TimeArrayType(xlkm__pnd.precision), msmp__eceb
    if xlkm__pnd == bytes_type:
        return binary_array_type, msmp__eceb
    maz__ormp = string_array_type if xlkm__pnd == string_type else types.Array(
        xlkm__pnd, 1, 'C')
    if xlkm__pnd == types.bool_:
        maz__ormp = boolean_array
    zzjyi__ydvu = (use_nullable_pd_arr if nullable_from_metadata is None else
        nullable_from_metadata)
    if zzjyi__ydvu and not is_index and isinstance(xlkm__pnd, types.Integer
        ) and pa_typ.nullable:
        maz__ormp = IntegerArrayType(xlkm__pnd)
    if (zzjyi__ydvu and bodo.libs.float_arr_ext._use_nullable_float and not
        is_index and isinstance(xlkm__pnd, types.Float) and pa_typ.nullable):
        maz__ormp = FloatingArrayType(xlkm__pnd)
    return maz__ormp, msmp__eceb


_numba_pyarrow_type_map = {types.bool_: pa.bool_(), types.int8: pa.int8(),
    types.int16: pa.int16(), types.int32: pa.int32(), types.int64: pa.int64
    (), types.uint8: pa.uint8(), types.uint16: pa.uint16(), types.uint32:
    pa.uint32(), types.uint64: pa.uint64(), types.float32: pa.float32(),
    types.float64: pa.float64(), types.NPDatetime('ns'): pa.date64()}


def is_nullable_arrow_out(numba_type: types.ArrayCompatible) ->bool:
    return is_nullable(numba_type) or isinstance(numba_type, bodo.
        DatetimeArrayType) or isinstance(numba_type, types.Array
        ) and numba_type.dtype == bodo.datetime64ns


def _numba_to_pyarrow_type(numba_type: types.ArrayCompatible, is_iceberg:
    bool=False):
    if isinstance(numba_type, ArrayItemArrayType):
        qumm__onqw = pa.field('element', _numba_to_pyarrow_type(numba_type.
            dtype, is_iceberg)[0])
        xlkm__pnd = pa.list_(qumm__onqw)
    elif isinstance(numba_type, StructArrayType):
        bse__yox = []
        for uuj__cxc, tisl__epv in zip(numba_type.names, numba_type.data):
            ysp__kzbdo, rpi__mvkv = _numba_to_pyarrow_type(tisl__epv,
                is_iceberg)
            bse__yox.append(pa.field(uuj__cxc, ysp__kzbdo, True))
        xlkm__pnd = pa.struct(bse__yox)
    elif isinstance(numba_type, DecimalArrayType):
        xlkm__pnd = pa.decimal128(numba_type.precision, numba_type.scale)
    elif isinstance(numba_type, CategoricalArrayType):
        imixv__kfbb: PDCategoricalDtype = numba_type.dtype
        xlkm__pnd = pa.dictionary(_numba_to_pyarrow_type(imixv__kfbb.
            int_type, is_iceberg)[0], _numba_to_pyarrow_type(imixv__kfbb.
            elem_type, is_iceberg)[0], ordered=False if imixv__kfbb.ordered is
            None else imixv__kfbb.ordered)
    elif numba_type == boolean_array:
        xlkm__pnd = pa.bool_()
    elif numba_type in (string_array_type, bodo.dict_str_arr_type):
        xlkm__pnd = pa.string()
    elif numba_type == binary_array_type:
        xlkm__pnd = pa.binary()
    elif numba_type == datetime_date_array_type:
        xlkm__pnd = pa.date32()
    elif isinstance(numba_type, bodo.DatetimeArrayType) or isinstance(
        numba_type, types.Array) and numba_type.dtype == bodo.datetime64ns:
        xlkm__pnd = pa.timestamp('us', 'UTC') if is_iceberg else pa.timestamp(
            'ns', 'UTC')
    elif isinstance(numba_type, types.Array
        ) and numba_type.dtype == bodo.timedelta64ns:
        xlkm__pnd = pa.duration('ns')
    elif isinstance(numba_type, (types.Array, IntegerArrayType,
        FloatingArrayType)) and numba_type.dtype in _numba_pyarrow_type_map:
        xlkm__pnd = _numba_pyarrow_type_map[numba_type.dtype]
    elif isinstance(numba_type, bodo.TimeArrayType):
        if numba_type.precision == 0:
            xlkm__pnd = pa.time32('s')
        elif numba_type.precision == 3:
            xlkm__pnd = pa.time32('ms')
        elif numba_type.precision == 6:
            xlkm__pnd = pa.time64('us')
        elif numba_type.precision == 9:
            xlkm__pnd = pa.time64('ns')
    else:
        raise BodoError(
            f'Conversion from Bodo array type {numba_type} to PyArrow type not supported yet'
            )
    return xlkm__pnd, is_nullable_arrow_out(numba_type)


def numba_to_pyarrow_schema(df: DataFrameType, is_iceberg: bool=False
    ) ->pa.Schema:
    bse__yox = []
    for uuj__cxc, dsc__rmrz in zip(df.columns, df.data):
        try:
            fcm__lja, xtzgu__opcdy = _numba_to_pyarrow_type(dsc__rmrz,
                is_iceberg)
        except BodoError as mqk__pqhr:
            raise_bodo_error(mqk__pqhr.msg, mqk__pqhr.loc)
        bse__yox.append(pa.field(uuj__cxc, fcm__lja, xtzgu__opcdy))
    return pa.schema(bse__yox)


def update_env_vars(env_vars):
    kwiev__eml = {}
    for iuf__spyn, fey__gkzo in env_vars.items():
        if iuf__spyn in os.environ:
            kwiev__eml[iuf__spyn] = os.environ[iuf__spyn]
        else:
            kwiev__eml[iuf__spyn] = '__none__'
        if fey__gkzo == '__none__':
            del os.environ[iuf__spyn]
        else:
            os.environ[iuf__spyn] = fey__gkzo
    return kwiev__eml


def update_file_contents(fname: str, contents: str, is_parallel=True) ->str:
    rwp__tjoqn = MPI.COMM_WORLD
    ylwsi__shri = None
    if not is_parallel or rwp__tjoqn.Get_rank() == 0:
        if os.path.exists(fname):
            with open(fname, 'r') as pux__wpw:
                ylwsi__shri = pux__wpw.read()
    if is_parallel:
        ylwsi__shri = rwp__tjoqn.bcast(ylwsi__shri)
    if ylwsi__shri is None:
        ylwsi__shri = '__none__'
    qwyxn__dgk = bodo.get_rank() in bodo.get_nodes_first_ranks(
        ) if is_parallel else True
    if contents == '__none__':
        if qwyxn__dgk and os.path.exists(fname):
            os.remove(fname)
    elif qwyxn__dgk:
        with open(fname, 'w') as pux__wpw:
            pux__wpw.write(contents)
    if is_parallel:
        rwp__tjoqn.Barrier()
    return ylwsi__shri


@numba.njit
def uuid4_helper():
    with numba.objmode(out='unicode_type'):
        out = str(uuid.uuid4())
    return out


class ExceptionPropagatingThread(threading.Thread):

    def run(self):
        self.exc = None
        try:
            self.ret = self._target(*self._args, **self._kwargs)
        except BaseException as mqk__pqhr:
            self.exc = mqk__pqhr

    def join(self, timeout=None):
        super().join(timeout)
        if self.exc:
            raise self.exc
        return self.ret


class ExceptionPropagatingThreadType(types.Opaque):

    def __init__(self):
        super(ExceptionPropagatingThreadType, self).__init__(name=
            'ExceptionPropagatingThreadType')


exception_propagating_thread_type = ExceptionPropagatingThreadType()
types.exception_propagating_thread_type = exception_propagating_thread_type
register_model(ExceptionPropagatingThreadType)(models.OpaqueModel)


@unbox(ExceptionPropagatingThreadType)
def unbox_exception_propagating_thread_type(typ, val, c):
    c.pyapi.incref(val)
    return NativeValue(val)


@box(ExceptionPropagatingThreadType)
def box_exception_propagating_thread_type(typ, val, c):
    c.pyapi.incref(val)
    return val


@typeof_impl.register(ExceptionPropagatingThread)
def typeof_exception_propagating_thread(val, c):
    return exception_propagating_thread_type


def join_all_threads(thread_list):
    xxrhw__wcq = tracing.Event('join_all_threads', is_parallel=True)
    rwp__tjoqn = MPI.COMM_WORLD
    wsnf__sdjlw = None
    try:
        for pkylw__ejnp in thread_list:
            if isinstance(pkylw__ejnp, threading.Thread):
                pkylw__ejnp.join()
    except Exception as mqk__pqhr:
        wsnf__sdjlw = mqk__pqhr
    bnpr__kygmy = int(wsnf__sdjlw is not None)
    ehqk__mcji, zhx__nqo = rwp__tjoqn.allreduce((bnpr__kygmy, rwp__tjoqn.
        Get_rank()), op=MPI.MAXLOC)
    if ehqk__mcji:
        if rwp__tjoqn.Get_rank() == zhx__nqo:
            ezgv__rckn = wsnf__sdjlw
        else:
            ezgv__rckn = None
        ezgv__rckn = rwp__tjoqn.bcast(ezgv__rckn, root=zhx__nqo)
        if bnpr__kygmy:
            raise wsnf__sdjlw
        else:
            raise ezgv__rckn
    xxrhw__wcq.finalize()
