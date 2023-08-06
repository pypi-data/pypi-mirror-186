"""
Helper functions to enable typing.
"""
import copy
import itertools
import operator
import types as pytypes
import warnings
from inspect import getfullargspec
from typing import Any, Dict, List, Optional, Tuple, Union
import numba
import numba.cpython.unicode
import numpy as np
import pandas as pd
import pyarrow as pa
from numba.core import cgutils, ir, ir_utils, types
from numba.core.errors import NumbaError
from numba.core.imputils import RefType, iternext_impl
from numba.core.registry import CPUDispatcher
from numba.core.typing.templates import AbstractTemplate, infer_global, signature
from numba.extending import NativeValue, box, infer, intrinsic, lower_builtin, lower_cast, models, overload, overload_attribute, overload_method, register_jitable, register_model, unbox
import bodo
CONST_DICT_SENTINEL = '$_bodo_const_dict_$'
INDEX_SENTINEL = '$_bodo_index_'
list_cumulative = {'cumsum', 'cumprod', 'cummin', 'cummax'}
Index = Union[str, Dict, None]
FileSchema = Tuple[List[str], List, Index, List[int], List, List, List, pa.
    Schema]


def is_timedelta_type(in_type):
    return in_type in [bodo.hiframes.datetime_timedelta_ext.
        pd_timedelta_type, bodo.hiframes.datetime_date_ext.
        datetime_timedelta_type]


def is_dtype_nullable(in_dtype):
    return isinstance(in_dtype, (types.Float, types.NPDatetime, types.
        NPTimedelta))


def is_nullable(typ):
    return bodo.utils.utils.is_array_typ(typ, False) and (not isinstance(
        typ, types.Array) or is_dtype_nullable(typ.dtype))


def is_str_arr_type(t):
    return t == bodo.string_array_type or t == bodo.dict_str_arr_type


def is_bin_arr_type(t):
    return t == bodo.binary_array_type


def type_has_unknown_cats(typ):
    return isinstance(typ, bodo.CategoricalArrayType
        ) and typ.dtype.categories is None or isinstance(typ, bodo.TableType
        ) and any(type_has_unknown_cats(t) for t in typ.type_to_blk.keys())


def unwrap_typeref(typ):
    return typ.instance_type if isinstance(typ, types.TypeRef) else typ


def decode_if_dict_array(A):
    return A


@overload(decode_if_dict_array)
def decode_if_dict_array_overload(A):
    if isinstance(A, types.BaseTuple):
        yttk__cjoml = len(A.types)
        uma__aqdl = 'def f(A):\n'
        qcj__mgqrm = ','.join(f'decode_if_dict_array(A[{i}])' for i in
            range(yttk__cjoml))
        uma__aqdl += '  return ({}{})\n'.format(qcj__mgqrm, ',' if 
            yttk__cjoml == 1 else '')
        uiq__nueri = {}
        exec(uma__aqdl, {'decode_if_dict_array': decode_if_dict_array},
            uiq__nueri)
        impl = uiq__nueri['f']
        return impl
    if isinstance(A, types.List):

        def impl(A):
            yttk__cjoml = 0
            for a in A:
                yttk__cjoml += 1
            ukd__ikzpi = []
            for i in range(yttk__cjoml):
                ukd__ikzpi.append(decode_if_dict_array(A[i]))
            return ukd__ikzpi
        return impl
    if A == bodo.dict_str_arr_type:
        return lambda A: A._decode()
    if isinstance(A, bodo.SeriesType):

        def impl(A):
            zpzyk__inb = bodo.hiframes.pd_series_ext.get_series_data(A)
            hkiug__gbinj = bodo.hiframes.pd_series_ext.get_series_index(A)
            name = bodo.hiframes.pd_series_ext.get_series_name(A)
            jshel__sjihw = decode_if_dict_array(zpzyk__inb)
            return bodo.hiframes.pd_series_ext.init_series(jshel__sjihw,
                hkiug__gbinj, name)
        return impl
    if isinstance(A, bodo.DataFrameType):
        if A.is_table_format:
            cjt__sxwb = (
                'bodo.hiframes.table.decode_if_dict_table(bodo.hiframes.pd_dataframe_ext.get_dataframe_table(A))'
                )
        else:
            cjt__sxwb = ', '.join(
                f'decode_if_dict_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(A, {i}))'
                 for i in range(len(A.columns)))
        impl = bodo.hiframes.dataframe_impl._gen_init_df('def impl(A):\n',
            A.columns, cjt__sxwb,
            'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(A)',
            extra_globals={'decode_if_dict_array': decode_if_dict_array,
            'bodo': bodo})
        return impl
    return lambda A: A


def to_str_arr_if_dict_array(t):
    if t == bodo.dict_str_arr_type:
        return bodo.string_array_type
    if isinstance(t, types.BaseTuple):
        return types.BaseTuple.from_types([to_str_arr_if_dict_array(a) for
            a in t.types])
    if isinstance(t, bodo.TableType):
        amu__jqx = tuple(to_str_arr_if_dict_array(t) for t in t.arr_types)
        return bodo.TableType(amu__jqx, t.has_runtime_cols)
    if isinstance(t, bodo.DataFrameType):
        return t.copy(data=tuple(to_str_arr_if_dict_array(t) for t in t.data))
    return t


class BodoError(NumbaError):

    def __init__(self, msg, loc=None, locs_in_msg=None):
        if locs_in_msg is None:
            self.locs_in_msg = []
        else:
            self.locs_in_msg = locs_in_msg
        ddwld__aji = numba.core.errors.termcolor().errmsg
        super(BodoError, self).__init__(ddwld__aji(msg), loc)


class BodoException(numba.core.errors.TypingError):
    pass


class BodoConstUpdatedError(Exception):
    pass


def raise_bodo_error(msg, loc=None):
    if bodo.transforms.typing_pass.in_partial_typing:
        bodo.transforms.typing_pass.typing_transform_required = True
        raise BodoException(msg)
    else:
        acukv__ubzu = [] if loc is None else [loc]
        raise BodoError(msg, locs_in_msg=acukv__ubzu)


class BodoWarning(Warning):
    pass


def get_udf_error_msg(context_str, error):
    msg = ''
    if hasattr(error, 'msg'):
        msg = str(error.msg)
    if hasattr(error, 'args') and error.args:
        msg = str(error.args[0])
    loc = ''
    if hasattr(error, 'loc') and error.loc is not None:
        loc = error.loc.strformat()
    return f'{context_str}: user-defined function not supported: {msg}\n{loc}'


class FileInfo:

    def __init__(self):
        self._concat_str: Optional[str] = None
        self._concat_left: Optional[str] = None

    def get_schema(self, fname: str):
        fwr__vkaca = self.get_full_filename(fname)
        return self._get_schema(fwr__vkaca)

    def set_concat(self, concat_str, is_left):
        self._concat_str = concat_str
        self._concat_left = is_left

    def _get_schema(self, fname: str) ->FileSchema:
        raise NotImplementedError

    def get_full_filename(self, fname: str):
        if self._concat_str is None:
            return fname
        if self._concat_left:
            return self._concat_str + fname
        return fname + self._concat_str


class FilenameType(types.Literal):

    def __init__(self, fname, finfo: FileInfo):
        self.fname = fname
        self._schema = finfo.get_schema(fname)
        super(FilenameType, self).__init__(self.fname)

    def __hash__(self):
        return 37

    def __eq__(self, other):
        if isinstance(other, types.FilenameType):
            assert self._schema is not None
            assert other._schema is not None
            return bodo.typeof(self.fname) == bodo.typeof(other.fname
                ) and self._schema == other._schema
        else:
            return False

    @property
    def schema(self):
        return copy.deepcopy(self._schema)


types.FilenameType = FilenameType


@register_model(types.FilenameType)
class FilenameModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        epmi__tlsci = dmm.lookup(bodo.typeof(fe_type.fname))
        zol__sus = [(a, aonnv__mpubn) for a, aonnv__mpubn in zip(
            epmi__tlsci._fields, epmi__tlsci._members)]
        super().__init__(dmm, fe_type, zol__sus)


@unbox(FilenameType)
def unbox_file_name_type(typ, obj, c):
    return c.unbox(bodo.typeof(typ.fname), obj)


@lower_cast(types.FilenameType, types.unicode_type)
@lower_cast(types.FilenameType, types.List)
def cast_filename_to_unicode(context, builder, fromty, toty, val):
    return val


@box(FilenameType)
def box_filename_type(typ, val, c):
    return c.box(bodo.typeof(typ.fname), val)


class NotConstant:
    pass


NOT_CONSTANT = NotConstant()


def is_overload_none(val):
    return val is None or val == types.none or getattr(val, 'value', False
        ) is None


def is_overload_constant_bool(val):
    return isinstance(val, bool) or isinstance(val, types.BooleanLiteral
        ) or isinstance(val, types.Omitted) and isinstance(val.value, bool)


def is_overload_bool(val):
    return isinstance(val, types.Boolean) or is_overload_constant_bool(val)


def is_overload_constant_str(val):
    return isinstance(val, str) or isinstance(val, types.StringLiteral
        ) and isinstance(val.literal_value, str) or isinstance(val, types.
        Omitted) and isinstance(val.value, str)


def is_overload_constant_bytes(val):
    return isinstance(val, bytes) or isinstance(val, types.Omitted
        ) and isinstance(val.value, bytes)


def is_overload_constant_list(val):
    return isinstance(val, (list, tuple)) or isinstance(val, types.Omitted
        ) and isinstance(val.value, tuple) or is_initial_value_list_type(val
        ) or isinstance(val, types.LiteralList) or isinstance(val, bodo.
        utils.typing.ListLiteral) or isinstance(val, types.BaseTuple) and all(
        is_literal_type(t) for t in val.types) and (not val.types or val.
        types[0] != types.StringLiteral(CONST_DICT_SENTINEL))


def is_overload_constant_tuple(val):
    return isinstance(val, tuple) or isinstance(val, types.Omitted
        ) and isinstance(val.value, tuple) or isinstance(val, types.BaseTuple
        ) and all(get_overload_const(t) is not NOT_CONSTANT for t in val.types)


def is_initial_value_type(t):
    if not isinstance(t, types.InitialValue) or t.initial_value is None:
        return False
    ncv__uis = t.initial_value
    if isinstance(ncv__uis, dict):
        ncv__uis = ncv__uis.values()
    return not any(isinstance(ueh__erhg, (types.Poison, numba.core.
        interpreter._UNKNOWN_VALUE)) for ueh__erhg in ncv__uis)


def is_initial_value_list_type(t):
    return isinstance(t, types.List) and is_initial_value_type(t)


def is_initial_value_dict_type(t):
    return isinstance(t, types.DictType) and is_initial_value_type(t)


def is_overload_constant_dict(val):
    return isinstance(val, types.LiteralStrKeyDict) and all(is_literal_type
        (ueh__erhg) for ueh__erhg in val.types) or is_initial_value_dict_type(
        val) or isinstance(val, DictLiteral) or isinstance(val, types.BaseTuple
        ) and val.types and val.types[0] == types.StringLiteral(
        CONST_DICT_SENTINEL) or isinstance(val, dict)


def is_overload_constant_number(val):
    return is_overload_constant_int(val) or is_overload_constant_float(val)


def is_overload_constant_nan(val):
    return is_overload_constant_float(val) and np.isnan(
        get_overload_const_float(val))


def is_overload_constant_float(val):
    return isinstance(val, float) or isinstance(val, types.Omitted
        ) and isinstance(val.value, float)


def is_overload_int(val):
    return is_overload_constant_int(val) or isinstance(val, types.Integer)


def is_overload_float(val):
    return is_overload_constant_float(val) or isinstance(val, types.Float)


def is_overload_constant_int(val):
    return isinstance(val, int) or isinstance(val, types.IntegerLiteral
        ) and isinstance(val.literal_value, int) or isinstance(val, types.
        Omitted) and isinstance(val.value, int)


def is_overload_bool_list(val):
    return is_overload_constant_list(val) and all(is_overload_constant_bool
        (ueh__erhg) for ueh__erhg in get_overload_const_list(val))


def is_overload_true(val):
    return val == True or val == types.BooleanLiteral(True) or getattr(val,
        'value', False) is True


def is_overload_false(val):
    return val == False or val == types.BooleanLiteral(False) or getattr(val,
        'value', True) is False


def is_overload_zero(val):
    return val == 0 or val == types.IntegerLiteral(0) or getattr(val,
        'value', -1) == 0


def is_overload_str(val, const):
    return val == const or val == types.StringLiteral(const) or getattr(val,
        'value', -1) == const


def get_overload_const(val):
    from bodo.hiframes.datetime_timedelta_ext import _no_input
    if isinstance(val, types.TypeRef):
        val = val.instance_type
    if val == types.none:
        return None
    if val is _no_input:
        return _no_input
    if val is None or isinstance(val, (bool, int, float, str, tuple, types.
        Dispatcher)):
        return val
    if isinstance(val, types.Omitted):
        return val.value
    if isinstance(val, types.LiteralList):
        lizrg__sdnkq = []
        for ueh__erhg in val.literal_value:
            zajqy__acm = get_overload_const(ueh__erhg)
            if zajqy__acm == NOT_CONSTANT:
                return NOT_CONSTANT
            else:
                lizrg__sdnkq.append(zajqy__acm)
        return lizrg__sdnkq
    if isinstance(val, types.Literal):
        return val.literal_value
    if isinstance(val, types.Dispatcher):
        return val
    if isinstance(val, types.BaseTuple):
        lizrg__sdnkq = []
        for ueh__erhg in val.types:
            zajqy__acm = get_overload_const(ueh__erhg)
            if zajqy__acm == NOT_CONSTANT:
                return NOT_CONSTANT
            else:
                lizrg__sdnkq.append(zajqy__acm)
        return tuple(lizrg__sdnkq)
    if is_initial_value_list_type(val):
        return val.initial_value
    if is_literal_type(val):
        return get_literal_value(val)
    return NOT_CONSTANT


def element_type(val):
    if isinstance(val, (types.List, types.ArrayCompatible)):
        if isinstance(val.dtype, bodo.hiframes.pd_categorical_ext.
            PDCategoricalDtype):
            return val.dtype.elem_type
        if val == bodo.bytes_type:
            return bodo.bytes_type
        return val.dtype
    return types.unliteral(val)


def can_replace(to_replace, value):
    return is_common_scalar_dtype([to_replace, value]) and not (isinstance(
        to_replace, types.Integer) and isinstance(value, types.Float)
        ) and not (isinstance(to_replace, types.Boolean) and isinstance(
        value, (types.Integer, types.Float)))


_const_type_repr = {str: 'string', bool: 'boolean', int: 'integer'}


def ensure_constant_arg(fname, arg_name, val, const_type):
    zajqy__acm = get_overload_const(val)
    nohe__gni = _const_type_repr.get(const_type, str(const_type))
    if not isinstance(zajqy__acm, const_type):
        raise BodoError(
            f"{fname}(): argument '{arg_name}' should be a constant {nohe__gni} not {val}"
            )


def ensure_constant_values(fname, arg_name, val, const_values):
    zajqy__acm = get_overload_const(val)
    if zajqy__acm not in const_values:
        raise BodoError(
            f"{fname}(): argument '{arg_name}' should be a constant value in {const_values} not '{zajqy__acm}'"
            )


def check_unsupported_args(fname, args_dict, arg_defaults_dict,
    package_name='pandas', fn_str=None, module_name=''):
    from bodo.hiframes.datetime_timedelta_ext import _no_input
    assert len(args_dict) == len(arg_defaults_dict)
    if fn_str == None:
        fn_str = f'{fname}()'
    nirq__fdq = ''
    mvth__xmvrc = False
    for a in args_dict:
        whw__aqe = get_overload_const(args_dict[a])
        srqee__prndd = arg_defaults_dict[a]
        if (whw__aqe is NOT_CONSTANT or whw__aqe is not None and 
            srqee__prndd is None or whw__aqe is None and srqee__prndd is not
            None or whw__aqe != srqee__prndd or whw__aqe is not _no_input and
            srqee__prndd is _no_input or whw__aqe is _no_input and 
            srqee__prndd is not _no_input):
            nirq__fdq = (
                f'{fn_str}: {a} parameter only supports default value {srqee__prndd}'
                )
            mvth__xmvrc = True
            break
    if mvth__xmvrc and package_name == 'pandas':
        if module_name == 'IO':
            nirq__fdq += """
Please check supported Pandas operations here (https://docs.bodo.ai/latest/api_docs/pandas/io/).
"""
        elif module_name == 'General':
            nirq__fdq += """
Please check supported Pandas operations here (https://docs.bodo.ai/latest/api_docs/pandas/general/).
"""
        elif module_name == 'DataFrame':
            nirq__fdq += """
Please check supported Pandas operations here (https://docs.bodo.ai/latest/api_docs/pandas/dataframe/).
"""
        elif module_name == 'Window':
            nirq__fdq += """
Please check supported Pandas operations here (https://docs.bodo.ai/latest/api_docs/pandas/window/).
"""
        elif module_name == 'GroupBy':
            nirq__fdq += """
Please check supported Pandas operations here (https://docs.bodo.ai/latest/api_docs/pandas/groupby/).
"""
        elif module_name == 'Series':
            nirq__fdq += """
Please check supported Pandas operations here (https://docs.bodo.ai/latest/api_docs/pandas/series/).
"""
        elif module_name == 'HeterogeneousSeries':
            nirq__fdq += """
Please check supported Pandas operations here (https://docs.bodo.ai/latest/api_docs/pandas/series/#heterogeneous_series).
"""
        elif module_name == 'Index':
            nirq__fdq += """
Please check supported Pandas operations here (https://docs.bodo.ai/latest/api_docs/pandas/indexapi/).
"""
        elif module_name == 'Timestamp':
            nirq__fdq += """
Please check supported Pandas operations here (https://docs.bodo.ai/latest/api_docs/pandas/timestamp/).
"""
        elif module_name == 'Timedelta':
            nirq__fdq += """
Please check supported Pandas operations here (https://docs.bodo.ai/latest/api_docs/pandas/timedelta/).
"""
        elif module_name == 'DateOffsets':
            nirq__fdq += """
Please check supported Pandas operations here (https://docs.bodo.ai/latest/api_docs/pandas/dateoffsets/).
"""
    elif mvth__xmvrc and package_name == 'ml':
        nirq__fdq += """
Please check supported ML operations here (https://docs.bodo.ai/latest/api_docs/ml/).
"""
    elif mvth__xmvrc and package_name == 'numpy':
        nirq__fdq += """
Please check supported Numpy operations here (https://docs.bodo.ai/latest/api_docs/numpy/).
"""
    if mvth__xmvrc:
        raise BodoError(nirq__fdq)


def get_overload_const_tuple(val) ->Optional[Tuple]:
    if isinstance(val, tuple):
        return val
    if isinstance(val, types.Omitted):
        assert isinstance(val.value, tuple)
        return val.value
    if isinstance(val, types.BaseTuple):
        return tuple(get_overload_const(t) for t in val.types)


def get_overload_constant_dict(val) ->Dict:
    if isinstance(val, types.LiteralStrKeyDict):
        return {get_literal_value(xoyo__gca): get_literal_value(ueh__erhg) for
            xoyo__gca, ueh__erhg in val.literal_value.items()}
    if isinstance(val, DictLiteral):
        return val.literal_value
    if isinstance(val, dict):
        return val
    assert is_initial_value_dict_type(val) or isinstance(val, types.BaseTuple
        ) and val.types and val.types[0] == types.StringLiteral(
        CONST_DICT_SENTINEL), 'invalid const dict'
    if isinstance(val, types.DictType):
        assert val.initial_value is not None, 'invalid dict initial value'
        return val.initial_value
    thvu__twsbl = [get_overload_const(ueh__erhg) for ueh__erhg in val.types[1:]
        ]
    return {thvu__twsbl[2 * i]: thvu__twsbl[2 * i + 1] for i in range(len(
        thvu__twsbl) // 2)}


def get_overload_const_str_len(val):
    if isinstance(val, str):
        return len(val)
    if isinstance(val, types.StringLiteral) and isinstance(val.
        literal_value, str):
        return len(val.literal_value)
    if isinstance(val, types.Omitted) and isinstance(val.value, str):
        return len(val.value)


def get_overload_const_list(val) ->Union[List[Any], Tuple[Any, ...], None]:
    if isinstance(val, (list, tuple)):
        return val
    if isinstance(val, types.Omitted) and isinstance(val.value, tuple):
        return val.value
    if is_initial_value_list_type(val):
        return val.initial_value
    if isinstance(val, types.LiteralList):
        return [get_literal_value(ueh__erhg) for ueh__erhg in val.literal_value
            ]
    if isinstance(val, bodo.utils.typing.ListLiteral):
        return val.literal_value
    if isinstance(val, types.Omitted):
        return [val.value]
    if isinstance(val, types.Literal):
        return [val.literal_value]
    if isinstance(val, types.BaseTuple) and all(is_literal_type(t) for t in
        val.types):
        return tuple(get_literal_value(t) for t in val.types)


def get_overload_const_str(val) ->str:
    if isinstance(val, str):
        return val
    if isinstance(val, types.Omitted):
        assert isinstance(val.value, str)
        return val.value
    if isinstance(val, types.StringLiteral):
        assert isinstance(val.literal_value, str)
        return val.literal_value
    raise BodoError('{} not constant string'.format(val))


def get_overload_const_bytes(val) ->bytes:
    if isinstance(val, bytes):
        return val
    if isinstance(val, types.Omitted):
        assert isinstance(val.value, bytes)
        return val.value
    raise BodoError('{} not constant binary'.format(val))


def get_overload_const_int(val) ->int:
    if isinstance(val, int):
        return val
    if isinstance(val, types.Omitted):
        assert isinstance(val.value, int)
        return val.value
    if isinstance(val, types.IntegerLiteral):
        assert isinstance(val.literal_value, int)
        return val.literal_value
    raise BodoError('{} not constant integer'.format(val))


def get_overload_const_float(val) ->float:
    if isinstance(val, float):
        return val
    if isinstance(val, types.Omitted):
        assert isinstance(val.value, float)
        return val.value
    raise BodoError('{} not constant float'.format(val))


def get_overload_const_bool(val) ->bool:
    if isinstance(val, bool):
        return val
    if isinstance(val, types.Omitted):
        assert isinstance(val.value, bool)
        return val.value
    if isinstance(val, types.BooleanLiteral):
        assert isinstance(val.literal_value, bool)
        return val.literal_value
    raise BodoError('{} not constant boolean'.format(val))


def is_const_func_type(t) ->bool:
    return isinstance(t, (types.MakeFunctionLiteral, bodo.utils.typing.
        FunctionLiteral, types.Dispatcher))


def get_overload_const_func(val, func_ir):
    if isinstance(val, (types.MakeFunctionLiteral, bodo.utils.typing.
        FunctionLiteral)):
        func = val.literal_value
        if isinstance(func, ir.Expr) and func.op == 'make_function':
            assert func_ir is not None, 'Function expression is make_function but there is no existing IR'
            func = numba.core.ir_utils.convert_code_obj_to_function(func,
                func_ir)
        return func
    if isinstance(val, types.Dispatcher):
        return val.dispatcher.py_func
    if isinstance(val, CPUDispatcher):
        return val.py_func
    raise BodoError("'{}' not a constant function type".format(val))


def is_heterogeneous_tuple_type(t):
    if is_overload_constant_list(t):
        if isinstance(t, types.LiteralList):
            t = types.BaseTuple.from_types(t.types)
        else:
            t = bodo.typeof(tuple(get_overload_const_list(t)))
    if isinstance(t, bodo.NullableTupleType):
        t = t.tuple_typ
    return isinstance(t, types.BaseTuple) and not isinstance(t, types.UniTuple)


def parse_dtype(dtype, func_name=None):
    if isinstance(dtype, types.TypeRef):
        return dtype.instance_type
    if isinstance(dtype, types.Function):
        if dtype.key[0] == float:
            dtype = types.StringLiteral('float')
        elif dtype.key[0] == int:
            dtype = types.StringLiteral('int')
        elif dtype.key[0] == bool:
            dtype = types.StringLiteral('bool')
        elif dtype.key[0] == str:
            dtype = bodo.string_type
    if type(dtype) in bodo.libs.int_arr_ext.pd_int_dtype_classes:
        dtype = types.StringLiteral(dtype.name)
    if isinstance(dtype, types.DTypeSpec):
        return dtype.dtype
    if isinstance(dtype, types.Number) or dtype == bodo.string_type:
        return dtype
    try:
        qlto__szzx = get_overload_const_str(dtype)
        if qlto__szzx.startswith('Int') or qlto__szzx.startswith('UInt'):
            return bodo.libs.int_arr_ext.typeof_pd_int_dtype(pd.api.types.
                pandas_dtype(qlto__szzx), None)
        if qlto__szzx.startswith('Float'):
            return bodo.libs.float_arr_ext.typeof_pd_float_dtype(pd.api.
                types.pandas_dtype(qlto__szzx), None)
        if qlto__szzx == 'boolean':
            return bodo.libs.bool_arr_ext.boolean_dtype
        if qlto__szzx == 'str':
            return bodo.string_type
        return numba.np.numpy_support.from_dtype(np.dtype(qlto__szzx))
    except:
        pass
    if func_name is not None:
        raise BodoError(f'{func_name}(): invalid dtype {dtype}')
    else:
        raise BodoError(f'invalid dtype {dtype}')


def is_list_like_index_type(t) ->bool:
    from bodo.hiframes.pd_index_ext import NumericIndexType, RangeIndexType
    from bodo.hiframes.pd_series_ext import SeriesType
    from bodo.libs.bool_arr_ext import boolean_array
    return isinstance(t, types.List) or isinstance(t, types.Array
        ) and t.ndim == 1 or isinstance(t, (NumericIndexType, RangeIndexType)
        ) or isinstance(t, SeriesType) or isinstance(t, bodo.IntegerArrayType
        ) or t == boolean_array


def is_tuple_like_type(t):
    return isinstance(t, types.BaseTuple) or is_heterogeneous_tuple_type(t
        ) or isinstance(t, bodo.hiframes.pd_index_ext.HeterogeneousIndexType)


def get_index_names(t, func_name, default_name):
    from bodo.hiframes.pd_multi_index_ext import MultiIndexType
    qcc__zoxy = '{}: index name should be a constant string'.format(func_name)
    if isinstance(t, MultiIndexType):
        apne__muy = []
        for i, nvfs__bqaef in enumerate(t.names_typ):
            if nvfs__bqaef == types.none:
                apne__muy.append('level_{}'.format(i))
                continue
            if not is_overload_constant_str(nvfs__bqaef):
                raise BodoError(qcc__zoxy)
            apne__muy.append(get_overload_const_str(nvfs__bqaef))
        return tuple(apne__muy)
    if t.name_typ == types.none:
        return default_name,
    if not is_overload_constant_str(t.name_typ):
        raise BodoError(qcc__zoxy)
    return get_overload_const_str(t.name_typ),


def get_index_data_arr_types(t):
    from bodo.hiframes.pd_index_ext import BinaryIndexType, CategoricalIndexType, DatetimeIndexType, IntervalIndexType, NumericIndexType, PeriodIndexType, RangeIndexType, StringIndexType, TimedeltaIndexType
    from bodo.hiframes.pd_multi_index_ext import MultiIndexType
    if isinstance(t, MultiIndexType):
        return tuple(t.array_types)
    if isinstance(t, (RangeIndexType, PeriodIndexType)):
        return types.Array(types.int64, 1, 'C'),
    if isinstance(t, (NumericIndexType, StringIndexType, BinaryIndexType,
        DatetimeIndexType, TimedeltaIndexType, CategoricalIndexType,
        IntervalIndexType)):
        return t.data,
    raise BodoError(f'Invalid index type {t}')


def to_numeric_index_if_range_index(t):
    from bodo.hiframes.pd_index_ext import NumericIndexType, RangeIndexType
    return NumericIndexType(types.int64, t.name_typ) if isinstance(t,
        RangeIndexType) else t


def get_index_type_from_dtype(t):
    from bodo.hiframes.pd_index_ext import BinaryIndexType, CategoricalIndexType, DatetimeIndexType, NumericIndexType, StringIndexType, TimedeltaIndexType
    if t in [bodo.hiframes.pd_timestamp_ext.pd_timestamp_tz_naive_type,
        bodo.datetime64ns, bodo.datetime_date_type]:
        return DatetimeIndexType(types.none)
    if isinstance(t, bodo.hiframes.pd_timestamp_ext.PandasTimestampType
        ) and t.tz is not None:
        return DatetimeIndexType(types.none, bodo.libs.pd_datetime_arr_ext.
            DatetimeArrayType(t.tz))
    if t in [bodo.hiframes.datetime_timedelta_ext.pd_timedelta_type, bodo.
        timedelta64ns]:
        return TimedeltaIndexType(types.none)
    if t == bodo.string_type:
        return StringIndexType(types.none)
    if t == bodo.bytes_type:
        return BinaryIndexType(types.none)
    if isinstance(t, (types.Integer, types.Float, types.Boolean)):
        return NumericIndexType(t, types.none)
    if isinstance(t, bodo.hiframes.pd_categorical_ext.PDCategoricalDtype):
        return CategoricalIndexType(bodo.CategoricalArrayType(t))
    raise BodoError(f'Cannot convert dtype {t} to index type')


def get_val_type_maybe_str_literal(value):
    t = numba.typeof(value)
    if isinstance(value, str):
        t = types.StringLiteral(value)
    return t


def get_index_name_types(t):
    from bodo.hiframes.pd_multi_index_ext import MultiIndexType
    if isinstance(t, MultiIndexType):
        return t.names_typ
    return t.name_typ,


if types.SliceLiteral in numba.core.pythonapi._boxers.functions:
    warnings.warn('SliceLiteral boxing has been implemented in Numba')
else:

    @box(types.SliceLiteral)
    def box_slice_literal(typ, val, c):
        irt__jrbh = typ.literal_value
        aujmg__piid = []
        for zue__oml in ('start', 'stop', 'step'):
            mnqmy__jisn = getattr(typ.literal_value, zue__oml)
            jjsvu__fwgd = c.pyapi.make_none(
                ) if mnqmy__jisn is None else c.pyapi.from_native_value(types
                .literal(mnqmy__jisn), mnqmy__jisn, c.env_manager)
            aujmg__piid.append(jjsvu__fwgd)
        oohe__tshdf = c.pyapi.unserialize(c.pyapi.serialize_object(slice))
        afq__ysb = c.pyapi.call_function_objargs(oohe__tshdf, aujmg__piid)
        for a in aujmg__piid:
            c.pyapi.decref(a)
        c.pyapi.decref(oohe__tshdf)
        return afq__ysb


class ListLiteral(types.Literal):
    pass


types.Literal.ctor_map[list] = ListLiteral
register_model(ListLiteral)(models.OpaqueModel)


@unbox(ListLiteral)
def unbox_list_literal(typ, obj, c):
    return NativeValue(c.context.get_dummy_value())


@box(ListLiteral)
def box_list_literal(typ, val, c):
    wiqqv__mdzc = typ.literal_value
    qsz__yoy = [c.pyapi.from_native_value(types.literal(ueh__erhg),
        ueh__erhg, c.env_manager) for ueh__erhg in wiqqv__mdzc]
    hodap__fdui = c.pyapi.list_pack(qsz__yoy)
    for a in qsz__yoy:
        c.pyapi.decref(a)
    return hodap__fdui


@lower_cast(ListLiteral, types.List)
def list_literal_to_list(context, builder, fromty, toty, val):
    list_vals = tuple(fromty.literal_value)
    gzsr__cblof = types.List(toty.dtype)
    return context.compile_internal(builder, lambda : list(list_vals),
        gzsr__cblof(), [])


class DictLiteral(types.Literal):
    pass


types.Literal.ctor_map[dict] = DictLiteral
register_model(DictLiteral)(models.OpaqueModel)


@unbox(DictLiteral)
def unbox_dict_literal(typ, obj, c):
    return NativeValue(c.context.get_dummy_value())


class FunctionLiteral(types.Literal, types.Opaque):
    pass


types.Literal.ctor_map[pytypes.FunctionType] = FunctionLiteral
register_model(FunctionLiteral)(models.OpaqueModel)


@unbox(FunctionLiteral)
def unbox_func_literal(typ, obj, c):
    return NativeValue(obj)


types.MakeFunctionLiteral._literal_type_cache = types.MakeFunctionLiteral(
    lambda : 0)


class MetaType(types.Type):

    def __init__(self, meta):
        self.meta = meta
        super(MetaType, self).__init__('MetaType({})'.format(meta))

    def can_convert_from(self, typingctx, other):
        return True

    @property
    def key(self):
        return tuple(self.meta)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)

    def __len__(self):
        return len(self.meta)


register_model(MetaType)(models.OpaqueModel)


class ColNamesMetaType(MetaType):

    def __init__(self, meta):
        self.meta = meta
        types.Type.__init__(self, f'ColNamesMetaType({meta})')


register_model(ColNamesMetaType)(models.OpaqueModel)


def is_literal_type(t):
    return isinstance(t, types.TypeRef) or isinstance(t, (types.Literal,
        types.Omitted)) and not isinstance(t, types.LiteralStrKeyDict
        ) or t == types.none or isinstance(t, types.Dispatcher) or isinstance(t
        , types.BaseTuple) and all(is_literal_type(ueh__erhg) for ueh__erhg in
        t.types) or is_initial_value_type(t) or isinstance(t, (types.
        DTypeSpec, types.Function)) or isinstance(t, bodo.libs.int_arr_ext.
        IntDtype) or isinstance(t, bodo.libs.float_arr_ext.FloatDtype
        ) or t in (bodo.libs.bool_arr_ext.boolean_dtype, bodo.libs.
        str_arr_ext.string_dtype) or isinstance(t, types.Function
        ) or is_overload_constant_index(t) or is_overload_constant_series(t
        ) or is_overload_constant_dict(t)


def is_overload_constant_index(t):
    from bodo.hiframes.pd_index_ext import HeterogeneousIndexType
    return isinstance(t, HeterogeneousIndexType) and is_literal_type(t.data
        ) and is_literal_type(t.name_typ)


def get_overload_constant_index(t):
    assert is_overload_constant_index(t)
    return pd.Index(get_literal_value(t.data), name=get_literal_value(t.
        name_typ))


def is_overload_constant_series(t):
    from bodo.hiframes.pd_series_ext import HeterogeneousSeriesType, SeriesType
    return isinstance(t, (SeriesType, HeterogeneousSeriesType)
        ) and is_literal_type(t.data) and is_literal_type(t.index
        ) and is_literal_type(t.name_typ)


def get_overload_constant_series(t):
    assert is_overload_constant_series(t)
    return pd.Series(get_literal_value(t.data), get_literal_value(t.index),
        name=get_literal_value(t.name_typ))


def get_literal_value(t):
    if isinstance(t, types.TypeRef):
        t = t.instance_type
    assert is_literal_type(t)
    if t == types.none:
        return None
    if isinstance(t, types.Literal):
        if isinstance(t, types.LiteralStrKeyDict):
            return {get_literal_value(xoyo__gca): get_literal_value(
                ueh__erhg) for xoyo__gca, ueh__erhg in t.literal_value.items()}
        if isinstance(t, types.LiteralList):
            return [get_literal_value(ueh__erhg) for ueh__erhg in t.
                literal_value]
        return t.literal_value
    if isinstance(t, types.Omitted):
        return t.value
    if isinstance(t, types.BaseTuple):
        return tuple(get_literal_value(ueh__erhg) for ueh__erhg in t.types)
    if isinstance(t, types.Dispatcher):
        return t
    if is_initial_value_type(t):
        return t.initial_value
    if isinstance(t, (types.DTypeSpec, types.Function)):
        return t
    if isinstance(t, bodo.libs.int_arr_ext.IntDtype):
        return getattr(pd, str(t)[:-2])()
    if isinstance(t, bodo.libs.float_arr_ext.FloatDtype):
        return getattr(pd, str(t)[:-2])()
    if t == bodo.libs.bool_arr_ext.boolean_dtype:
        return pd.BooleanDtype()
    if t == bodo.libs.str_arr_ext.string_dtype:
        return pd.StringDtype()
    if is_overload_constant_index(t):
        return get_overload_constant_index(t)
    if is_overload_constant_series(t):
        return get_overload_constant_series(t)
    if is_overload_constant_dict(t):
        return get_overload_constant_dict(t)


def can_literalize_type(t, pyobject_to_literal=False):
    return t in (bodo.string_type, types.bool_) or isinstance(t, (types.
        Integer, types.List, types.SliceType, types.DictType)
        ) or pyobject_to_literal and t == types.pyobject


def dtype_to_array_type(dtype, convert_nullable=False):
    dtype = types.unliteral(dtype)
    if isinstance(dtype, types.List):
        dtype = dtype_to_array_type(dtype.dtype)
    if isinstance(dtype, types.Optional):
        dtype = dtype.type
        convert_nullable = True
    if dtype == bodo.string_type:
        return bodo.string_array_type
    if dtype == bodo.bytes_type:
        return bodo.binary_array_type
    if bodo.utils.utils.is_array_typ(dtype, False):
        return bodo.ArrayItemArrayType(dtype)
    if isinstance(dtype, bodo.hiframes.pd_categorical_ext.PDCategoricalDtype):
        return bodo.CategoricalArrayType(dtype)
    if isinstance(dtype, bodo.libs.int_arr_ext.IntDtype):
        return bodo.IntegerArrayType(dtype.dtype)
    if isinstance(dtype, bodo.libs.float_arr_ext.FloatDtype):
        return bodo.FloatingArrayType(dtype.dtype)
    if dtype == types.bool_:
        return bodo.boolean_array
    if dtype == bodo.datetime_date_type:
        return bodo.hiframes.datetime_date_ext.datetime_date_array_type
    if isinstance(dtype, bodo.TimeType):
        return bodo.hiframes.time_ext.TimeArrayType(dtype.precision)
    if isinstance(dtype, bodo.Decimal128Type):
        return bodo.DecimalArrayType(dtype.precision, dtype.scale)
    if isinstance(dtype, bodo.libs.struct_arr_ext.StructType):
        return bodo.StructArrayType(tuple(dtype_to_array_type(t, True) for
            t in dtype.data), dtype.names)
    if isinstance(dtype, types.BaseTuple):
        return bodo.TupleArrayType(tuple(dtype_to_array_type(t) for t in
            dtype.types))
    if isinstance(dtype, types.DictType):
        return bodo.MapArrayType(dtype_to_array_type(dtype.key_type),
            dtype_to_array_type(dtype.value_type))
    if isinstance(dtype, bodo.libs.pd_datetime_arr_ext.PandasDatetimeTZDtype):
        return bodo.DatetimeArrayType(dtype.tz)
    if dtype in (bodo.pd_timestamp_tz_naive_type, bodo.hiframes.
        datetime_datetime_ext.datetime_datetime_type):
        return types.Array(bodo.datetime64ns, 1, 'C')
    if dtype in (bodo.pd_timedelta_type, bodo.hiframes.
        datetime_timedelta_ext.datetime_timedelta_type):
        return types.Array(bodo.timedelta64ns, 1, 'C')
    if isinstance(dtype, (types.Number, types.Boolean, types.NPDatetime,
        types.NPTimedelta)):
        zpzyk__inb = types.Array(dtype, 1, 'C')
        if convert_nullable:
            return to_nullable_type(zpzyk__inb)
        return zpzyk__inb
    raise BodoError(f'dtype {dtype} cannot be stored in arrays')


def get_udf_out_arr_type(f_return_type, return_nullable=False):
    if isinstance(f_return_type, types.Optional):
        f_return_type = f_return_type.type
        return_nullable = True
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(f_return_type,
        'Series.apply')
    if (f_return_type == bodo.hiframes.pd_timestamp_ext.
        pd_timestamp_tz_naive_type):
        f_return_type = types.NPDatetime('ns')
    if f_return_type == bodo.hiframes.datetime_timedelta_ext.pd_timedelta_type:
        f_return_type = types.NPTimedelta('ns')
    out_arr_type = dtype_to_array_type(f_return_type)
    out_arr_type = to_nullable_type(out_arr_type
        ) if return_nullable else out_arr_type
    return out_arr_type


def equality_always_false(t1, t2):
    string_types = types.UnicodeType, types.StringLiteral, types.UnicodeCharSeq
    return isinstance(t1, string_types) and not isinstance(t2, string_types
        ) or isinstance(t2, string_types) and not isinstance(t1, string_types)


def types_equality_exists(t1, t2):
    wpzy__yqr = numba.core.registry.cpu_target.typing_context
    try:
        wpzy__yqr.resolve_function_type(operator.eq, (t1, t2), {})
        return True
    except:
        return False


def is_hashable_type(t):
    whitelist_types = (types.UnicodeType, types.StringLiteral, types.
        UnicodeCharSeq, types.Number, bodo.hiframes.pd_timestamp_ext.
        PandasTimestampType)
    fnaxr__chf = (types.bool_, bodo.datetime64ns, bodo.timedelta64ns, bodo.
        pd_timedelta_type)
    if isinstance(t, whitelist_types) or t in fnaxr__chf:
        return True
    wpzy__yqr = numba.core.registry.cpu_target.typing_context
    try:
        wpzy__yqr.resolve_function_type(hash, (t,), {})
        return True
    except:
        return False


def to_nullable_type(t):
    from bodo.hiframes.pd_dataframe_ext import DataFrameType
    from bodo.hiframes.pd_series_ext import SeriesType
    if isinstance(t, DataFrameType):
        xcx__ftm = tuple(to_nullable_type(t) for t in t.data)
        return DataFrameType(xcx__ftm, t.index, t.columns, t.dist, t.
            is_table_format)
    if isinstance(t, SeriesType):
        return SeriesType(t.dtype, to_nullable_type(t.data), t.index, t.
            name_typ)
    if isinstance(t, types.Array):
        if t.dtype == types.bool_:
            return bodo.libs.bool_arr_ext.boolean_array
        if isinstance(t.dtype, types.Integer):
            return bodo.libs.int_arr_ext.IntegerArrayType(t.dtype)
        if isinstance(t.dtype, types.Float
            ) and bodo.libs.float_arr_ext._use_nullable_float:
            return bodo.libs.float_arr_ext.FloatingArrayType(t.dtype)
    return t


def is_nullable_type(t):
    return t == to_nullable_type(t)


def is_iterable_type(t):
    from bodo.hiframes.pd_dataframe_ext import DataFrameType
    from bodo.hiframes.pd_series_ext import SeriesType
    return bodo.utils.utils.is_array_typ(t, False) or isinstance(t, (
        SeriesType, DataFrameType, types.List, types.BaseTuple, types.
        LiteralList, types.RangeType)
        ) or bodo.hiframes.pd_index_ext.is_pd_index_type(t)


def is_scalar_type(t):
    return isinstance(t, (types.Boolean, types.Number, types.StringLiteral,
        bodo.hiframes.pd_timestamp_ext.PandasTimestampType, bodo.TimeType)
        ) or t in (bodo.datetime64ns, bodo.timedelta64ns, bodo.string_type,
        bodo.bytes_type, bodo.datetime_date_type, bodo.
        datetime_datetime_type, bodo.datetime_timedelta_type, bodo.
        pd_timedelta_type, bodo.month_end_type, bodo.week_type, bodo.
        date_offset_type, types.none)


def is_common_scalar_dtype(scalar_types):
    dzc__lfbo, yljj__xhtxc = get_common_scalar_dtype(scalar_types)
    return yljj__xhtxc


def get_common_scalar_dtype(scalar_types):
    scalar_types = [types.unliteral(a) for a in scalar_types]
    if len(scalar_types) == 0:
        raise_bodo_error(
            'Internal error, length of argument passed to get_common_scalar_dtype scalar_types is 0'
            )
    try:
        usnq__ivp = np.find_common_type([numba.np.numpy_support.as_dtype(t) for
            t in scalar_types], [])
        if usnq__ivp != object:
            return numba.np.numpy_support.from_dtype(usnq__ivp), True
    except numba.core.errors.NumbaNotImplementedError as sba__upa:
        pass
    if scalar_types[0] in (bodo.datetime64ns, bodo.pd_timestamp_tz_naive_type):
        for typ in scalar_types[1:]:
            if typ not in (bodo.datetime64ns, bodo.pd_timestamp_tz_naive_type):
                return None, False
        return bodo.datetime64ns, True
    if scalar_types[0] in (bodo.timedelta64ns, bodo.pd_timedelta_type):
        for typ in scalar_types[1:]:
            if scalar_types[0] not in (bodo.timedelta64ns, bodo.
                pd_timedelta_type):
                return None, False
        return bodo.timedelta64ns, True
    saoy__szqn = itertools.groupby(scalar_types)
    if next(saoy__szqn, True) and not next(saoy__szqn, False):
        return scalar_types[0], True
    return None, False


def find_common_np_dtype(arr_types):
    return numba.np.numpy_support.from_dtype(np.find_common_type([numba.np.
        numpy_support.as_dtype(t.dtype) for t in arr_types], []))


def is_immutable_array(typ):
    return isinstance(typ, (bodo.ArrayItemArrayType, bodo.MapArrayType))


def get_nullable_and_non_nullable_types(array_of_types):
    ehra__iyzcq = []
    for typ in array_of_types:
        if typ == bodo.libs.bool_arr_ext.boolean_array:
            ehra__iyzcq.append(types.Array(types.bool_, 1, 'C'))
        elif isinstance(typ, (bodo.libs.int_arr_ext.IntegerArrayType, bodo.
            libs.float_arr_ext.FloatingArrayType)):
            ehra__iyzcq.append(types.Array(typ.dtype, 1, 'C'))
        elif isinstance(typ, types.Array):
            if typ.dtype == types.bool_:
                ehra__iyzcq.append(bodo.libs.bool_arr_ext.boolean_array)
            if isinstance(typ.dtype, types.Integer):
                ehra__iyzcq.append(bodo.libs.int_arr_ext.IntegerArrayType(
                    typ.dtype))
            if isinstance(typ.dtype, types.Float):
                ehra__iyzcq.append(bodo.libs.float_arr_ext.
                    FloatingArrayType(typ.dtype))
        ehra__iyzcq.append(typ)
    return ehra__iyzcq


def is_np_arr_typ(t, dtype, ndim=1):
    return isinstance(t, types.Array) and t.dtype == dtype and t.ndim == ndim


def _gen_objmode_overload(func, output_type, attr_name=None, is_function=
    True, single_rank=False):
    if is_function:
        eaimv__iljw = getfullargspec(func)
        assert eaimv__iljw.varargs is None, 'varargs not supported'
        assert eaimv__iljw.varkw is None, 'varkw not supported'
        defaults = [] if eaimv__iljw.defaults is None else eaimv__iljw.defaults
        ahez__yzmeu = len(eaimv__iljw.args) - len(defaults)
        args = eaimv__iljw.args[1:] if attr_name else eaimv__iljw.args[:]
        tty__sat = []
        for i, bxkvd__fkyu in enumerate(eaimv__iljw.args):
            if i < ahez__yzmeu:
                tty__sat.append(bxkvd__fkyu)
            elif str(defaults[i - ahez__yzmeu]) != '<deprecated parameter>':
                tty__sat.append(bxkvd__fkyu + '=' + str(defaults[i -
                    ahez__yzmeu]))
            else:
                args.remove(bxkvd__fkyu)
        if eaimv__iljw.kwonlyargs is not None:
            for bxkvd__fkyu in eaimv__iljw.kwonlyargs:
                args.append(f'{bxkvd__fkyu}={bxkvd__fkyu}')
                tty__sat.append(
                    f'{bxkvd__fkyu}={str(eaimv__iljw.kwonlydefaults[bxkvd__fkyu])}'
                    )
        sig = ', '.join(tty__sat)
        args = ', '.join(args)
    else:
        sig = 'self'
    type_name = str(output_type)
    if not hasattr(types, type_name):
        type_name = f'objmode_type{ir_utils.next_label()}'
        setattr(types, type_name, output_type)
    if not attr_name:
        func_name = func.__module__.replace('.', '_'
            ) + '_' + func.__name__ + '_func'
    tfuel__mcwu = f'self.{attr_name}' if attr_name else f'{func_name}'
    uma__aqdl = f'def overload_impl({sig}):\n'
    uma__aqdl += f'    def impl({sig}):\n'
    if single_rank:
        uma__aqdl += f'        if bodo.get_rank() == 0:\n'
        mhd__fgfqc = '    '
    else:
        mhd__fgfqc = ''
    uma__aqdl += (
        f"        {mhd__fgfqc}with numba.objmode(res='{type_name}'):\n")
    if is_function:
        uma__aqdl += f'            {mhd__fgfqc}res = {tfuel__mcwu}({args})\n'
    else:
        uma__aqdl += f'            {mhd__fgfqc}res = {tfuel__mcwu}\n'
    uma__aqdl += f'        return res\n'
    uma__aqdl += f'    return impl\n'
    uiq__nueri = {}
    hkvmd__zadc = globals()
    if not attr_name:
        hkvmd__zadc[func_name] = func
    exec(uma__aqdl, hkvmd__zadc, uiq__nueri)
    ftkzp__sgax = uiq__nueri['overload_impl']
    return ftkzp__sgax


def gen_objmode_func_overload(func, output_type=None, single_rank=False):
    try:
        ftkzp__sgax = _gen_objmode_overload(func, output_type, is_function=
            True, single_rank=single_rank)
        overload(func, no_unliteral=True)(ftkzp__sgax)
    except Exception as sba__upa:
        pass


def gen_objmode_method_overload(obj_type, method_name, method, output_type=
    None, single_rank=False):
    try:
        ftkzp__sgax = _gen_objmode_overload(method, output_type,
            method_name, True, single_rank)
        overload_method(obj_type, method_name, no_unliteral=True)(ftkzp__sgax)
    except Exception as sba__upa:
        pass


def gen_objmode_attr_overload(obj_type, attr_name, attr, output_type=None,
    single_rank=False):
    try:
        ftkzp__sgax = _gen_objmode_overload(attr, output_type, attr_name, 
            False, single_rank)
        overload_attribute(obj_type, attr_name, no_unliteral=True)(ftkzp__sgax)
    except Exception as sba__upa:
        pass


@infer
class NumTypeStaticGetItem(AbstractTemplate):
    key = 'static_getitem'

    def generic(self, args, kws):
        val, rzui__kyqcv = args
        if isinstance(rzui__kyqcv, slice) and (isinstance(val, types.
            NumberClass) or isinstance(val, types.TypeRef) and isinstance(
            val.instance_type, (types.NPDatetime, types.NPTimedelta))):
            return signature(types.TypeRef(val.instance_type[rzui__kyqcv]),
                *args)


@lower_builtin('static_getitem', types.NumberClass, types.SliceLiteral)
def num_class_type_static_getitem(context, builder, sig, args):
    return context.get_dummy_value()


@overload(itertools.chain, no_unliteral=True)
def chain_overload():
    return lambda : [0]


@register_jitable
def from_iterable_impl(A):
    return bodo.utils.conversion.flatten_array(bodo.utils.conversion.
        coerce_to_array(A))


@intrinsic
def unliteral_val(typingctx, val=None):

    def codegen(context, builder, signature, args):
        return args[0]
    return types.unliteral(val)(val), codegen


def create_unsupported_overload(fname):

    def overload_f(*a, **kws):
        raise BodoError('{} not supported yet'.format(fname))
    return overload_f


def is_numpy_ufunc(func):
    return isinstance(func, types.Function) and isinstance(func.typing_key,
        np.ufunc)


def is_builtin_function(func):
    return isinstance(func, types.Function) and isinstance(func.typing_key,
        pytypes.BuiltinFunctionType)


def get_builtin_function_name(func):
    return func.typing_key.__name__


def construct_pysig(arg_names, defaults):
    uma__aqdl = f'def stub('
    for bxkvd__fkyu in arg_names:
        uma__aqdl += bxkvd__fkyu
        if bxkvd__fkyu in defaults:
            if isinstance(defaults[bxkvd__fkyu], str):
                uma__aqdl += f"='{defaults[bxkvd__fkyu]}'"
            else:
                uma__aqdl += f'={defaults[bxkvd__fkyu]}'
        uma__aqdl += ', '
    uma__aqdl += '):\n'
    uma__aqdl += '    pass\n'
    uiq__nueri = {}
    exec(uma__aqdl, {}, uiq__nueri)
    lqfty__asrzu = uiq__nueri['stub']
    return numba.core.utils.pysignature(lqfty__asrzu)


def fold_typing_args(func_name, args, kws, arg_names, defaults,
    unsupported_arg_names=()):
    kws = dict(kws)
    ulpe__wtmr = len(arg_names)
    rmkan__rrdqa = len(args) + len(kws)
    if rmkan__rrdqa > ulpe__wtmr:
        ijg__lewl = 'argument' if ulpe__wtmr == 1 else 'arguments'
        vtly__dafjz = 'was' if rmkan__rrdqa == 1 else 'were'
        raise BodoError(
            f'{func_name}(): Too many arguments specified. Function takes {ulpe__wtmr} {ijg__lewl}, but {rmkan__rrdqa} {vtly__dafjz} provided.'
            )
    qqi__pih = bodo.utils.typing.construct_pysig(arg_names, defaults)
    try:
        dtx__zdj = bodo.utils.transform.fold_argument_types(qqi__pih, args, kws
            )
    except Exception as fjwu__qvo:
        raise_bodo_error(f'{func_name}(): {fjwu__qvo}')
    if unsupported_arg_names:
        mvkwp__hhra = {}
        ndn__fxfe = {}
        for i, arg_name in enumerate(arg_names):
            if arg_name in unsupported_arg_names:
                assert arg_name in defaults, f"{func_name}(): '{arg_name}' is unsupported but no default is provided"
                mvkwp__hhra[arg_name] = dtx__zdj[i]
                ndn__fxfe[arg_name] = defaults[arg_name]
        check_unsupported_args(func_name, mvkwp__hhra, ndn__fxfe)
    return qqi__pih, dtx__zdj


def _is_pandas_numeric_dtype(dtype):
    return isinstance(dtype, types.Number) or dtype == types.bool_


def type_col_to_index(col_names):
    if all(isinstance(a, str) for a in col_names):
        return bodo.StringIndexType(None)
    elif all(isinstance(a, bytes) for a in col_names):
        return bodo.BinaryIndexType(None)
    elif all(isinstance(a, (int, float)) for a in col_names):
        if any(isinstance(a, float) for a in col_names):
            return bodo.NumericIndexType(types.float64)
        else:
            return bodo.NumericIndexType(types.int64)
    else:
        return bodo.hiframes.pd_index_ext.HeterogeneousIndexType(col_names)


class BodoArrayIterator(types.SimpleIteratorType):

    def __init__(self, arr_type, yield_type=None):
        self.arr_type = arr_type
        name = f'iter({arr_type})'
        if yield_type == None:
            yield_type = arr_type.dtype
        super(BodoArrayIterator, self).__init__(name, yield_type)


@register_model(BodoArrayIterator)
class BodoArrayIteratorModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        zol__sus = [('index', types.EphemeralPointer(types.uintp)), (
            'array', fe_type.arr_type)]
        super(BodoArrayIteratorModel, self).__init__(dmm, fe_type, zol__sus)


@lower_builtin('iternext', BodoArrayIterator)
@iternext_impl(RefType.NEW)
def iternext_bodo_array(context, builder, sig, args, result):
    [kunt__baw] = sig.args
    [wen__efi] = args
    twzsz__pwo = context.make_helper(builder, kunt__baw, value=wen__efi)
    gld__ghbm = signature(types.intp, kunt__baw.arr_type)
    vwkg__mbz = context.compile_internal(builder, lambda a: len(a),
        gld__ghbm, [twzsz__pwo.array])
    hkiug__gbinj = builder.load(twzsz__pwo.index)
    let__gmp = builder.icmp_signed('<', hkiug__gbinj, vwkg__mbz)
    result.set_valid(let__gmp)
    with builder.if_then(let__gmp):
        emkv__zhy = signature(kunt__baw.yield_type, kunt__baw.arr_type,
            types.intp)
        value = context.compile_internal(builder, lambda a, i: a[i],
            emkv__zhy, [twzsz__pwo.array, hkiug__gbinj])
        result.yield_(value)
        oeqox__lduk = cgutils.increment_index(builder, hkiug__gbinj)
        builder.store(oeqox__lduk, twzsz__pwo.index)


def index_typ_from_dtype_name_arr(elem_dtype, name, arr_typ):
    ivynm__dkiyq = type(get_index_type_from_dtype(elem_dtype))
    if name is None:
        ryk__yfjnf = None
    else:
        ryk__yfjnf = types.StringLiteral(name)
    if ivynm__dkiyq == bodo.hiframes.pd_index_ext.NumericIndexType:
        vgti__cmas = ivynm__dkiyq(elem_dtype, ryk__yfjnf, arr_typ)
    elif ivynm__dkiyq == bodo.hiframes.pd_index_ext.CategoricalIndexType:
        vgti__cmas = ivynm__dkiyq(bodo.CategoricalArrayType(elem_dtype),
            ryk__yfjnf, arr_typ)
    else:
        vgti__cmas = ivynm__dkiyq(ryk__yfjnf, arr_typ)
    return vgti__cmas


def is_safe_arrow_cast(lhs_scalar_typ, rhs_scalar_typ):
    if lhs_scalar_typ == types.unicode_type:
        return rhs_scalar_typ in (bodo.datetime64ns, bodo.
            pd_timestamp_tz_naive_type)
    elif rhs_scalar_typ == types.unicode_type:
        return lhs_scalar_typ in (bodo.datetime64ns, bodo.
            pd_timestamp_tz_naive_type)
    elif lhs_scalar_typ == bodo.datetime_date_type:
        return rhs_scalar_typ in (bodo.datetime64ns, bodo.
            pd_timestamp_tz_naive_type)
    elif rhs_scalar_typ == bodo.datetime_date_type:
        return lhs_scalar_typ in (bodo.datetime64ns, bodo.
            pd_timestamp_tz_naive_type)
    return False


def register_type(type_name, type_value):
    if not isinstance(type_name, str):
        raise BodoError(
            f'register_type(): type name should be a string, not {type(type_name)}'
            )
    if not isinstance(type_value, types.Type):
        raise BodoError(
            f'register_type(): type value should be a valid data type, not {type(type_value)}'
            )
    if hasattr(types, type_name):
        raise BodoError(
            f"register_type(): type name '{type_name}' already exists")
    setattr(types, type_name, type_value)


@box(types.TypeRef)
def box_typeref(typ, val, c):
    return c.pyapi.unserialize(c.pyapi.serialize_object(typ.instance_type))


def check_objmode_output_type(ret_tup, ret_type):
    return tuple(_check_objmode_type(ueh__erhg, t) for ueh__erhg, t in zip(
        ret_tup, ret_type.types))


def _is_equiv_array_type(A, B):
    from bodo.libs.map_arr_ext import MapArrayType
    from bodo.libs.struct_arr_ext import StructArrayType
    return isinstance(A, StructArrayType) and isinstance(B, MapArrayType
        ) and set(A.data) == {B.value_arr_type
        } and B.key_arr_type.dtype == bodo.string_type or isinstance(A,
        types.Array) and isinstance(B, types.Array
        ) and A.ndim == B.ndim and A.dtype == B.dtype and B.layout in ('A',
        A.layout) and (A.mutable or not B.mutable) and (A.aligned or not B.
        aligned)


def _fix_objmode_df_type(val, val_typ, typ):
    from bodo.hiframes.pd_index_ext import RangeIndexType
    if val_typ.dist != typ.dist:
        val_typ = val_typ.copy(dist=typ.dist)
    if isinstance(typ.index, RangeIndexType) and not isinstance(val_typ.
        index, RangeIndexType):
        warnings.warn(BodoWarning(
            f'Dropping Index of objmode output dataframe since RangeIndexType specified in type annotation ({val_typ.index} to {typ.index})'
            ))
        val.reset_index(drop=True, inplace=True)
        val_typ = val_typ.copy(index=typ.index)
    if (val_typ.index.name_typ != types.none and typ.index.name_typ ==
        types.none):
        warnings.warn(BodoWarning(
            f'Dropping name field in Index of objmode output dataframe since none specified in type annotation ({val_typ.index} to {typ.index})'
            ))
        val_typ = val_typ.copy(index=typ.index)
        val.index.name = None
    for i, (A, B) in enumerate(zip(val_typ.data, typ.data)):
        if _is_equiv_array_type(A, B):
            val_typ = val_typ.replace_col_type(val_typ.columns[i], B)
    if val_typ.is_table_format and not typ.is_table_format:
        val_typ = val_typ.copy(is_table_format=False)
    if val_typ != typ:
        bstwr__ygx = pd.Index(val_typ.columns)
        abu__gunxy = pd.Index(typ.columns)
        uetvu__rpln = bstwr__ygx.argsort()
        zckoz__bgzjr = abu__gunxy.argsort()
        xlkp__myw = val_typ.copy(data=tuple(np.array(val_typ.data)[
            uetvu__rpln]), columns=tuple(bstwr__ygx[uetvu__rpln]))
        rvby__rrhvk = typ.copy(data=tuple(np.array(typ.data)[zckoz__bgzjr]),
            columns=tuple(abu__gunxy[zckoz__bgzjr]))
        if xlkp__myw == rvby__rrhvk:
            val_typ = typ
            val = val.reindex(columns=typ.columns)
    return val, val_typ


def _check_objmode_type(val, typ):
    from bodo.hiframes.pd_dataframe_ext import DataFrameType
    val_typ = bodo.typeof(val)
    if isinstance(typ, DataFrameType) and isinstance(val_typ, DataFrameType):
        val, val_typ = _fix_objmode_df_type(val, val_typ, typ)
    if _is_equiv_array_type(val_typ, typ):
        val_typ = typ
    if isinstance(val_typ, (types.List, types.Set)):
        val_typ = val_typ.copy(reflected=False)
    if isinstance(val_typ, (types.Integer, types.Float)) and isinstance(typ,
        (types.Integer, types.Float)):
        return val
    if val_typ != typ:
        raise BodoError(
            f"""Invalid objmode data type specified.
User specified:	{typ}
Value type:	{val_typ}"""
            )
    return val


def bodosql_case_placeholder(arrs, case_code, out_arr_type):
    pass


@infer_global(bodosql_case_placeholder)
class CasePlaceholderTyper(AbstractTemplate):

    def generic(self, args, kws):
        return signature(unwrap_typeref(args[-1]), *args)


CasePlaceholderTyper.prefer_literal = True
gen_objmode_func_overload(warnings.warn, 'none')


def get_castable_arr_dtype(arr_type: types.Type):
    if isinstance(arr_type, (bodo.IntegerArrayType, bodo.FloatingArrayType)):
        fdgd__bnar = arr_type.get_pandas_scalar_type_instance.name
    elif arr_type in (bodo.boolean_array, bodo.dict_str_arr_type
        ) or isinstance(arr_type, bodo.DatetimeArrayType):
        fdgd__bnar = arr_type
    else:
        fdgd__bnar = arr_type.dtype
    return fdgd__bnar
