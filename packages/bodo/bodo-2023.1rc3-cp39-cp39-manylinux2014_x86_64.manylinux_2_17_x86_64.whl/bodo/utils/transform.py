"""
Helper functions for transformations.
"""
import itertools
import math
import operator
import types as pytypes
from collections import namedtuple
import numba
import numpy as np
import pandas as pd
from numba.core import ir, ir_utils, types
from numba.core.ir_utils import GuardException, build_definitions, compile_to_numba_ir, compute_cfg_from_blocks, find_callname, find_const, get_definition, guard, is_setitem, mk_unique_var, replace_arg_nodes, require
from numba.core.registry import CPUDispatcher
from numba.core.typing.templates import fold_arguments
import bodo
from bodo.libs.array_item_arr_ext import ArrayItemArrayType
from bodo.libs.map_arr_ext import MapArrayType
from bodo.libs.str_arr_ext import string_array_type
from bodo.libs.struct_arr_ext import StructArrayType, StructType
from bodo.libs.tuple_arr_ext import TupleArrayType
from bodo.utils.typing import BodoConstUpdatedError, BodoError, can_literalize_type, get_literal_value, get_overload_const_bool, get_overload_const_list, is_literal_type, is_overload_constant_bool
from bodo.utils.utils import is_array_typ, is_assign, is_call, is_expr
ReplaceFunc = namedtuple('ReplaceFunc', ['func', 'arg_types', 'args',
    'glbls', 'inline_bodo_calls', 'run_full_pipeline', 'pre_nodes'])
bodo_types_with_params = {'ArrayItemArrayType', 'CSRMatrixType',
    'CategoricalArrayType', 'CategoricalIndexType', 'DataFrameType',
    'DatetimeIndexType', 'Decimal128Type', 'DecimalArrayType',
    'IntegerArrayType', 'FloatingArrayType', 'IntervalArrayType',
    'IntervalIndexType', 'List', 'MapArrayType', 'NumericIndexType',
    'PDCategoricalDtype', 'PeriodIndexType', 'RangeIndexType', 'SeriesType',
    'StringIndexType', 'BinaryIndexType', 'StructArrayType',
    'TimedeltaIndexType', 'TupleArrayType'}
container_update_method_names = ('clear', 'pop', 'popitem', 'update', 'add',
    'difference_update', 'discard', 'intersection_update', 'remove',
    'symmetric_difference_update', 'append', 'extend', 'insert', 'reverse',
    'sort')
no_side_effect_call_tuples = {(int,), (list,), (set,), (dict,), (min,), (
    max,), (abs,), (len,), (bool,), (str,), ('ceil', math), ('Int32Dtype',
    pd), ('Int64Dtype', pd), ('Timestamp', pd), ('Week', 'offsets',
    'tseries', pd), ('init_series', 'pd_series_ext', 'hiframes', bodo), (
    'get_series_data', 'pd_series_ext', 'hiframes', bodo), (
    'get_series_index', 'pd_series_ext', 'hiframes', bodo), (
    'get_series_name', 'pd_series_ext', 'hiframes', bodo), (
    'get_index_data', 'pd_index_ext', 'hiframes', bodo), ('get_index_name',
    'pd_index_ext', 'hiframes', bodo), ('init_binary_str_index',
    'pd_index_ext', 'hiframes', bodo), ('init_numeric_index',
    'pd_index_ext', 'hiframes', bodo), ('init_categorical_index',
    'pd_index_ext', 'hiframes', bodo), ('_dti_val_finalize', 'pd_index_ext',
    'hiframes', bodo), ('init_datetime_index', 'pd_index_ext', 'hiframes',
    bodo), ('init_timedelta_index', 'pd_index_ext', 'hiframes', bodo), (
    'init_range_index', 'pd_index_ext', 'hiframes', bodo), (
    'init_heter_index', 'pd_index_ext', 'hiframes', bodo), (
    'get_int_arr_data', 'int_arr_ext', 'libs', bodo), ('get_int_arr_bitmap',
    'int_arr_ext', 'libs', bodo), ('init_integer_array', 'int_arr_ext',
    'libs', bodo), ('alloc_int_array', 'int_arr_ext', 'libs', bodo), (
    'init_float_array', 'float_arr_ext', 'libs', bodo), (
    'alloc_float_array', 'float_arr_ext', 'libs', bodo), ('inplace_eq',
    'str_arr_ext', 'libs', bodo), ('get_bool_arr_data', 'bool_arr_ext',
    'libs', bodo), ('get_bool_arr_bitmap', 'bool_arr_ext', 'libs', bodo), (
    'init_bool_array', 'bool_arr_ext', 'libs', bodo), ('alloc_bool_array',
    'bool_arr_ext', 'libs', bodo), ('datetime_date_arr_to_dt64_arr',
    'pd_timestamp_ext', 'hiframes', bodo), ('alloc_pd_datetime_array',
    'pd_datetime_arr_ext', 'libs', bodo), (bodo.libs.bool_arr_ext.
    compute_or_body,), (bodo.libs.bool_arr_ext.compute_and_body,), (
    'alloc_datetime_date_array', 'datetime_date_ext', 'hiframes', bodo), (
    'alloc_datetime_timedelta_array', 'datetime_timedelta_ext', 'hiframes',
    bodo), ('cat_replace', 'pd_categorical_ext', 'hiframes', bodo), (
    'init_categorical_array', 'pd_categorical_ext', 'hiframes', bodo), (
    'alloc_categorical_array', 'pd_categorical_ext', 'hiframes', bodo), (
    'get_categorical_arr_codes', 'pd_categorical_ext', 'hiframes', bodo), (
    '_sum_handle_nan', 'series_kernels', 'hiframes', bodo), ('_box_cat_val',
    'series_kernels', 'hiframes', bodo), ('_mean_handle_nan',
    'series_kernels', 'hiframes', bodo), ('_var_handle_mincount',
    'series_kernels', 'hiframes', bodo), ('_compute_var_nan_count_ddof',
    'series_kernels', 'hiframes', bodo), ('_sem_handle_nan',
    'series_kernels', 'hiframes', bodo), ('dist_return', 'distributed_api',
    'libs', bodo), ('rep_return', 'distributed_api', 'libs', bodo), (
    'init_dataframe', 'pd_dataframe_ext', 'hiframes', bodo), (
    'get_dataframe_data', 'pd_dataframe_ext', 'hiframes', bodo), (
    'get_dataframe_all_data', 'pd_dataframe_ext', 'hiframes', bodo), (
    'get_dataframe_table', 'pd_dataframe_ext', 'hiframes', bodo), (
    'get_dataframe_column_names', 'pd_dataframe_ext', 'hiframes', bodo), (
    'get_table_data', 'table', 'hiframes', bodo), ('get_dataframe_index',
    'pd_dataframe_ext', 'hiframes', bodo), ('init_rolling',
    'pd_rolling_ext', 'hiframes', bodo), ('init_groupby', 'pd_groupby_ext',
    'hiframes', bodo), ('calc_nitems', 'array_kernels', 'libs', bodo), (
    'concat', 'array_kernels', 'libs', bodo), ('unique', 'array_kernels',
    'libs', bodo), ('nunique', 'array_kernels', 'libs', bodo), ('quantile',
    'array_kernels', 'libs', bodo), ('explode', 'array_kernels', 'libs',
    bodo), ('explode_no_index', 'array_kernels', 'libs', bodo), (
    'get_arr_lens', 'array_kernels', 'libs', bodo), (
    'str_arr_from_sequence', 'str_arr_ext', 'libs', bodo), (
    'get_str_arr_str_length', 'str_arr_ext', 'libs', bodo), (
    'parse_datetime_str', 'pd_timestamp_ext', 'hiframes', bodo), (
    'integer_to_dt64', 'pd_timestamp_ext', 'hiframes', bodo), (
    'dt64_to_integer', 'pd_timestamp_ext', 'hiframes', bodo), (
    'timedelta64_to_integer', 'pd_timestamp_ext', 'hiframes', bodo), (
    'integer_to_timedelta64', 'pd_timestamp_ext', 'hiframes', bodo), (
    'npy_datetimestruct_to_datetime', 'pd_timestamp_ext', 'hiframes', bodo),
    ('isna', 'array_kernels', 'libs', bodo), (bodo.libs.str_arr_ext.
    num_total_chars,), ('num_total_chars', 'str_arr_ext', 'libs', bodo), (
    'copy',), ('from_iterable_impl', 'typing', 'utils', bodo), ('chain',
    itertools), ('groupby',), ('rolling',), (pd.CategoricalDtype,), (bodo.
    hiframes.pd_categorical_ext.get_code_for_value,), ('asarray', np), (
    'int32', np), ('int64', np), ('float64', np), ('float32', np), ('bool_',
    np), ('full', np), ('round', np), ('isnan', np), ('isnat', np), (
    'arange', np), ('internal_prange', 'parfor', numba), ('internal_prange',
    'parfor', 'parfors', numba), ('empty_inferred', 'ndarray', 'unsafe',
    numba), ('_slice_span', 'unicode', numba), ('_normalize_slice',
    'unicode', numba), ('init_session_builder', 'pyspark_ext', 'libs', bodo
    ), ('init_session', 'pyspark_ext', 'libs', bodo), ('init_spark_df',
    'pyspark_ext', 'libs', bodo), ('h5size', 'h5_api', 'io', bodo), (
    'pre_alloc_struct_array', 'struct_arr_ext', 'libs', bodo), (bodo.libs.
    struct_arr_ext.pre_alloc_struct_array,), ('pre_alloc_tuple_array',
    'tuple_arr_ext', 'libs', bodo), (bodo.libs.tuple_arr_ext.
    pre_alloc_tuple_array,), ('pre_alloc_array_item_array',
    'array_item_arr_ext', 'libs', bodo), (bodo.libs.array_item_arr_ext.
    pre_alloc_array_item_array,), ('dist_reduce', 'distributed_api', 'libs',
    bodo), (bodo.libs.distributed_api.dist_reduce,), (
    'pre_alloc_string_array', 'str_arr_ext', 'libs', bodo), (bodo.libs.
    str_arr_ext.pre_alloc_string_array,), ('pre_alloc_binary_array',
    'binary_arr_ext', 'libs', bodo), (bodo.libs.binary_arr_ext.
    pre_alloc_binary_array,), ('pre_alloc_map_array', 'map_arr_ext', 'libs',
    bodo), (bodo.libs.map_arr_ext.pre_alloc_map_array,), (
    'convert_dict_arr_to_int', 'dict_arr_ext', 'libs', bodo), (
    'cat_dict_str', 'dict_arr_ext', 'libs', bodo), ('str_replace',
    'dict_arr_ext', 'libs', bodo), ('dict_arr_to_numeric', 'dict_arr_ext',
    'libs', bodo), ('dict_arr_eq', 'dict_arr_ext', 'libs', bodo), (
    'dict_arr_ne', 'dict_arr_ext', 'libs', bodo), ('str_startswith',
    'dict_arr_ext', 'libs', bodo), ('str_endswith', 'dict_arr_ext', 'libs',
    bodo), ('str_contains_non_regex', 'dict_arr_ext', 'libs', bodo), (
    'str_series_contains_regex', 'dict_arr_ext', 'libs', bodo), (
    'str_capitalize', 'dict_arr_ext', 'libs', bodo), ('str_lower',
    'dict_arr_ext', 'libs', bodo), ('str_swapcase', 'dict_arr_ext', 'libs',
    bodo), ('str_title', 'dict_arr_ext', 'libs', bodo), ('str_upper',
    'dict_arr_ext', 'libs', bodo), ('str_center', 'dict_arr_ext', 'libs',
    bodo), ('str_get', 'dict_arr_ext', 'libs', bodo), ('str_repeat_int',
    'dict_arr_ext', 'libs', bodo), ('str_lstrip', 'dict_arr_ext', 'libs',
    bodo), ('str_rstrip', 'dict_arr_ext', 'libs', bodo), ('str_strip',
    'dict_arr_ext', 'libs', bodo), ('str_zfill', 'dict_arr_ext', 'libs',
    bodo), ('str_ljust', 'dict_arr_ext', 'libs', bodo), ('str_rjust',
    'dict_arr_ext', 'libs', bodo), ('str_find', 'dict_arr_ext', 'libs',
    bodo), ('str_rfind', 'dict_arr_ext', 'libs', bodo), ('str_index',
    'dict_arr_ext', 'libs', bodo), ('str_rindex', 'dict_arr_ext', 'libs',
    bodo), ('str_slice', 'dict_arr_ext', 'libs', bodo), ('str_extract',
    'dict_arr_ext', 'libs', bodo), ('str_extractall', 'dict_arr_ext',
    'libs', bodo), ('str_extractall_multi', 'dict_arr_ext', 'libs', bodo),
    ('str_len', 'dict_arr_ext', 'libs', bodo), ('str_count', 'dict_arr_ext',
    'libs', bodo), ('str_isalnum', 'dict_arr_ext', 'libs', bodo), (
    'str_isalpha', 'dict_arr_ext', 'libs', bodo), ('str_isdigit',
    'dict_arr_ext', 'libs', bodo), ('str_isspace', 'dict_arr_ext', 'libs',
    bodo), ('str_islower', 'dict_arr_ext', 'libs', bodo), ('str_isupper',
    'dict_arr_ext', 'libs', bodo), ('str_istitle', 'dict_arr_ext', 'libs',
    bodo), ('str_isnumeric', 'dict_arr_ext', 'libs', bodo), (
    'str_isdecimal', 'dict_arr_ext', 'libs', bodo), ('str_match',
    'dict_arr_ext', 'libs', bodo), ('prange', bodo), (bodo.prange,), (
    'objmode', bodo), (bodo.objmode,), ('get_label_dict_from_categories',
    'pd_categorial_ext', 'hiframes', bodo), (
    'get_label_dict_from_categories_no_duplicates', 'pd_categorial_ext',
    'hiframes', bodo), ('build_nullable_tuple', 'nullable_tuple_ext',
    'libs', bodo), ('generate_mappable_table_func', 'table_utils', 'utils',
    bodo), ('table_astype', 'table_utils', 'utils', bodo), ('table_concat',
    'table_utils', 'utils', bodo), ('table_filter', 'table', 'hiframes',
    bodo), ('table_subset', 'table', 'hiframes', bodo), (
    'logical_table_to_table', 'table', 'hiframes', bodo), ('set_table_data',
    'table', 'hiframes', bodo), ('set_table_null', 'table', 'hiframes',
    bodo), ('startswith',), ('endswith',), ('upper',), ('lower',), (
    '__bodosql_replace_columns_dummy', 'dataframe_impl', 'hiframes', bodo)}
_np_type_names = {'int8', 'int16', 'int32', 'int64', 'uint8', 'uint16',
    'uint32', 'uint64', 'float32', 'float64', 'bool_'}


def remove_hiframes(rhs, lives, call_list):
    fhsgk__dkh = tuple(call_list)
    if fhsgk__dkh in no_side_effect_call_tuples:
        return True
    if fhsgk__dkh == (bodo.hiframes.pd_index_ext.init_range_index,):
        return True
    if len(call_list) == 4 and call_list[1:] == ['conversion', 'utils', bodo]:
        return True
    if isinstance(call_list[-1], pytypes.ModuleType) and call_list[-1
        ].__name__ == 'bodosql':
        return True
    if call_list[1:] == ['bodosql_array_kernels', 'libs', bodo]:
        return True
    if len(call_list) == 2 and call_list[0] == 'copy':
        return True
    if call_list == ['h5read', 'h5_api', 'io', bodo] and rhs.args[5
        ].name not in lives:
        return True
    if call_list == ['move_str_binary_arr_payload', 'str_arr_ext', 'libs', bodo
        ] and rhs.args[0].name not in lives:
        return True
    if call_list in (['setna', 'array_kernels', 'libs', bodo], [
        'copy_array_element', 'array_kernels', 'libs', bodo], [
        'get_str_arr_item_copy', 'str_arr_ext', 'libs', bodo]) and rhs.args[0
        ].name not in lives:
        return True
    if call_list == ['ensure_column_unboxed', 'table', 'hiframes', bodo
        ] and rhs.args[0].name not in lives and rhs.args[1].name not in lives:
        return True
    if call_list == ['generate_table_nbytes', 'table_utils', 'utils', bodo
        ] and rhs.args[1].name not in lives:
        return True
    if len(fhsgk__dkh) == 1 and tuple in getattr(fhsgk__dkh[0], '__mro__', ()):
        return True
    return False


numba.core.ir_utils.remove_call_handlers.append(remove_hiframes)


def compile_func_single_block(func, args, ret_var, typing_info=None,
    extra_globals=None, infer_types=True, run_untyped_pass=False, flags=
    None, replace_globals=False, add_default_globals=True):
    if replace_globals:
        ayk__pftyq = {'numba': numba, 'np': np, 'bodo': bodo, 'pd': pd,
            'math': math}
    else:
        ayk__pftyq = func.__globals__
    if extra_globals is not None:
        ayk__pftyq.update(extra_globals)
    if add_default_globals:
        ayk__pftyq.update({'numba': numba, 'np': np, 'bodo': bodo, 'pd': pd,
            'math': math})
    loc = ir.Loc('', 0)
    if ret_var:
        loc = ret_var.loc
    if typing_info and infer_types:
        loc = typing_info.curr_loc
        f_ir = compile_to_numba_ir(func, ayk__pftyq, typingctx=typing_info.
            typingctx, targetctx=typing_info.targetctx, arg_typs=tuple(
            typing_info.typemap[uifbl__ykmhe.name] for uifbl__ykmhe in args
            ), typemap=typing_info.typemap, calltypes=typing_info.calltypes)
    else:
        f_ir = compile_to_numba_ir(func, ayk__pftyq)
    assert len(f_ir.blocks
        ) == 1, 'only single block functions supported in compile_func_single_block()'
    if run_untyped_pass:
        tdyn__qpka = tuple(typing_info.typemap[uifbl__ykmhe.name] for
            uifbl__ykmhe in args)
        lwdh__sws = bodo.transforms.untyped_pass.UntypedPass(f_ir,
            typing_info.typingctx, tdyn__qpka, {}, {}, flags)
        lwdh__sws.run()
    yfbz__nyor = f_ir.blocks.popitem()[1]
    replace_arg_nodes(yfbz__nyor, args)
    qto__nld = yfbz__nyor.body[:-2]
    update_locs(qto__nld[len(args):], loc)
    for stmt in qto__nld[:len(args)]:
        stmt.target.loc = loc
    if ret_var is not None:
        wcip__jwj = yfbz__nyor.body[-2]
        assert is_assign(wcip__jwj) and is_expr(wcip__jwj.value, 'cast')
        ckne__wnjg = wcip__jwj.value.value
        qto__nld.append(ir.Assign(ckne__wnjg, ret_var, loc))
    return qto__nld


def update_locs(node_list, loc):
    for stmt in node_list:
        stmt.loc = loc
        for uofbk__qyb in stmt.list_vars():
            uofbk__qyb.loc = loc
        if is_assign(stmt):
            stmt.value.loc = loc


def get_stmt_defs(stmt):
    if is_assign(stmt):
        return set([stmt.target.name])
    if type(stmt) in numba.core.analysis.ir_extension_usedefs:
        fokwv__velgy = numba.core.analysis.ir_extension_usedefs[type(stmt)]
        muuu__igy, olsw__qolv = fokwv__velgy(stmt)
        return olsw__qolv
    return set()


def get_const_value(var, func_ir, err_msg, typemap=None, arg_types=None,
    file_info=None):
    if hasattr(var, 'loc'):
        loc = var.loc
    else:
        loc = None
    try:
        xxe__dkbpg = get_const_value_inner(func_ir, var, arg_types, typemap,
            file_info=file_info)
        if isinstance(xxe__dkbpg, ir.UndefinedType):
            fgt__smxk = func_ir.get_definition(var.name).name
            raise BodoError(f"name '{fgt__smxk}' is not defined", loc=loc)
    except GuardException as vyp__apm:
        raise BodoError(err_msg, loc=loc)
    return xxe__dkbpg


def get_const_value_inner(func_ir, var, arg_types=None, typemap=None,
    updated_containers=None, file_info=None, pyobject_to_literal=False,
    literalize_args=True):
    require(isinstance(var, ir.Var))
    qeag__rxbku = get_definition(func_ir, var)
    pnj__gsmn = None
    if typemap is not None:
        pnj__gsmn = typemap.get(var.name, None)
    if isinstance(qeag__rxbku, ir.Arg) and arg_types is not None:
        pnj__gsmn = arg_types[qeag__rxbku.index]
    if updated_containers and var.name in updated_containers:
        raise BodoConstUpdatedError(
            f"variable '{var.name}' is updated inplace using '{updated_containers[var.name]}'"
            )
    if is_literal_type(pnj__gsmn):
        return get_literal_value(pnj__gsmn)
    if isinstance(qeag__rxbku, (ir.Const, ir.Global, ir.FreeVar)):
        xxe__dkbpg = qeag__rxbku.value
        return xxe__dkbpg
    if literalize_args and isinstance(qeag__rxbku, ir.Arg
        ) and can_literalize_type(pnj__gsmn, pyobject_to_literal):
        raise numba.core.errors.ForceLiteralArg({qeag__rxbku.index}, loc=
            var.loc, file_infos={qeag__rxbku.index: file_info} if file_info
             is not None else None)
    if is_expr(qeag__rxbku, 'binop'):
        if file_info and qeag__rxbku.fn == operator.add:
            try:
                mzv__wqk = get_const_value_inner(func_ir, qeag__rxbku.lhs,
                    arg_types, typemap, updated_containers, literalize_args
                    =False)
                file_info.set_concat(mzv__wqk, True)
                eljba__xyoeb = get_const_value_inner(func_ir, qeag__rxbku.
                    rhs, arg_types, typemap, updated_containers, file_info)
                return qeag__rxbku.fn(mzv__wqk, eljba__xyoeb)
            except (GuardException, BodoConstUpdatedError) as vyp__apm:
                pass
            try:
                eljba__xyoeb = get_const_value_inner(func_ir, qeag__rxbku.
                    rhs, arg_types, typemap, updated_containers,
                    literalize_args=False)
                file_info.set_concat(eljba__xyoeb, False)
                mzv__wqk = get_const_value_inner(func_ir, qeag__rxbku.lhs,
                    arg_types, typemap, updated_containers, file_info)
                return qeag__rxbku.fn(mzv__wqk, eljba__xyoeb)
            except (GuardException, BodoConstUpdatedError) as vyp__apm:
                pass
        mzv__wqk = get_const_value_inner(func_ir, qeag__rxbku.lhs,
            arg_types, typemap, updated_containers)
        eljba__xyoeb = get_const_value_inner(func_ir, qeag__rxbku.rhs,
            arg_types, typemap, updated_containers)
        return qeag__rxbku.fn(mzv__wqk, eljba__xyoeb)
    if is_expr(qeag__rxbku, 'unary'):
        xxe__dkbpg = get_const_value_inner(func_ir, qeag__rxbku.value,
            arg_types, typemap, updated_containers)
        return qeag__rxbku.fn(xxe__dkbpg)
    if is_expr(qeag__rxbku, 'getattr') and typemap:
        baeom__ckndd = typemap.get(qeag__rxbku.value.name, None)
        if isinstance(baeom__ckndd, bodo.hiframes.pd_dataframe_ext.
            DataFrameType) and qeag__rxbku.attr == 'columns':
            return pd.Index(baeom__ckndd.columns)
        if isinstance(baeom__ckndd, types.SliceType):
            arcy__vxu = get_definition(func_ir, qeag__rxbku.value)
            require(is_call(arcy__vxu))
            tri__ikydw = find_callname(func_ir, arcy__vxu)
            eho__rkwy = False
            if tri__ikydw == ('_normalize_slice', 'numba.cpython.unicode'):
                require(qeag__rxbku.attr in ('start', 'step'))
                arcy__vxu = get_definition(func_ir, arcy__vxu.args[0])
                eho__rkwy = True
            require(find_callname(func_ir, arcy__vxu) == ('slice', 'builtins'))
            if len(arcy__vxu.args) == 1:
                if qeag__rxbku.attr == 'start':
                    return 0
                if qeag__rxbku.attr == 'step':
                    return 1
                require(qeag__rxbku.attr == 'stop')
                return get_const_value_inner(func_ir, arcy__vxu.args[0],
                    arg_types, typemap, updated_containers)
            if qeag__rxbku.attr == 'start':
                xxe__dkbpg = get_const_value_inner(func_ir, arcy__vxu.args[
                    0], arg_types, typemap, updated_containers)
                if xxe__dkbpg is None:
                    xxe__dkbpg = 0
                if eho__rkwy:
                    require(xxe__dkbpg == 0)
                return xxe__dkbpg
            if qeag__rxbku.attr == 'stop':
                assert not eho__rkwy
                return get_const_value_inner(func_ir, arcy__vxu.args[1],
                    arg_types, typemap, updated_containers)
            require(qeag__rxbku.attr == 'step')
            if len(arcy__vxu.args) == 2:
                return 1
            else:
                xxe__dkbpg = get_const_value_inner(func_ir, arcy__vxu.args[
                    2], arg_types, typemap, updated_containers)
                if xxe__dkbpg is None:
                    xxe__dkbpg = 1
                if eho__rkwy:
                    require(xxe__dkbpg == 1)
                return xxe__dkbpg
    if is_expr(qeag__rxbku, 'getattr'):
        return getattr(get_const_value_inner(func_ir, qeag__rxbku.value,
            arg_types, typemap, updated_containers), qeag__rxbku.attr)
    if is_expr(qeag__rxbku, 'getitem'):
        value = get_const_value_inner(func_ir, qeag__rxbku.value, arg_types,
            typemap, updated_containers)
        index = get_const_value_inner(func_ir, qeag__rxbku.index, arg_types,
            typemap, updated_containers)
        return value[index]
    mlvkh__yxlr = guard(find_callname, func_ir, qeag__rxbku, typemap)
    if mlvkh__yxlr is not None and len(mlvkh__yxlr) == 2 and mlvkh__yxlr[0
        ] == 'keys' and isinstance(mlvkh__yxlr[1], ir.Var):
        nsp__vor = qeag__rxbku.func
        qeag__rxbku = get_definition(func_ir, mlvkh__yxlr[1])
        eqqm__jygoo = mlvkh__yxlr[1].name
        if updated_containers and eqqm__jygoo in updated_containers:
            raise BodoConstUpdatedError(
                "variable '{}' is updated inplace using '{}'".format(
                eqqm__jygoo, updated_containers[eqqm__jygoo]))
        require(is_expr(qeag__rxbku, 'build_map'))
        vals = [uofbk__qyb[0] for uofbk__qyb in qeag__rxbku.items]
        nuuu__uzp = guard(get_definition, func_ir, nsp__vor)
        assert isinstance(nuuu__uzp, ir.Expr) and nuuu__uzp.attr == 'keys'
        nuuu__uzp.attr = 'copy'
        return [get_const_value_inner(func_ir, uofbk__qyb, arg_types,
            typemap, updated_containers) for uofbk__qyb in vals]
    if is_expr(qeag__rxbku, 'build_map'):
        return {get_const_value_inner(func_ir, uofbk__qyb[0], arg_types,
            typemap, updated_containers): get_const_value_inner(func_ir,
            uofbk__qyb[1], arg_types, typemap, updated_containers) for
            uofbk__qyb in qeag__rxbku.items}
    if is_expr(qeag__rxbku, 'build_tuple'):
        return tuple(get_const_value_inner(func_ir, uofbk__qyb, arg_types,
            typemap, updated_containers) for uofbk__qyb in qeag__rxbku.items)
    if is_expr(qeag__rxbku, 'build_list'):
        return [get_const_value_inner(func_ir, uofbk__qyb, arg_types,
            typemap, updated_containers) for uofbk__qyb in qeag__rxbku.items]
    if is_expr(qeag__rxbku, 'build_set'):
        return {get_const_value_inner(func_ir, uofbk__qyb, arg_types,
            typemap, updated_containers) for uofbk__qyb in qeag__rxbku.items}
    if mlvkh__yxlr == ('list', 'builtins'):
        values = get_const_value_inner(func_ir, qeag__rxbku.args[0],
            arg_types, typemap, updated_containers)
        if isinstance(values, set):
            values = sorted(values)
        return list(values)
    if mlvkh__yxlr == ('set', 'builtins'):
        return set(get_const_value_inner(func_ir, qeag__rxbku.args[0],
            arg_types, typemap, updated_containers))
    if mlvkh__yxlr == ('range', 'builtins') and len(qeag__rxbku.args) == 1:
        return range(get_const_value_inner(func_ir, qeag__rxbku.args[0],
            arg_types, typemap, updated_containers))
    if mlvkh__yxlr == ('slice', 'builtins'):
        return slice(*tuple(get_const_value_inner(func_ir, uofbk__qyb,
            arg_types, typemap, updated_containers) for uofbk__qyb in
            qeag__rxbku.args))
    if mlvkh__yxlr == ('str', 'builtins'):
        return str(get_const_value_inner(func_ir, qeag__rxbku.args[0],
            arg_types, typemap, updated_containers))
    if mlvkh__yxlr == ('bool', 'builtins'):
        return bool(get_const_value_inner(func_ir, qeag__rxbku.args[0],
            arg_types, typemap, updated_containers))
    if mlvkh__yxlr == ('format', 'builtins'):
        uifbl__ykmhe = get_const_value_inner(func_ir, qeag__rxbku.args[0],
            arg_types, typemap, updated_containers)
        ttc__muxpc = get_const_value_inner(func_ir, qeag__rxbku.args[1],
            arg_types, typemap, updated_containers) if len(qeag__rxbku.args
            ) > 1 else ''
        return format(uifbl__ykmhe, ttc__muxpc)
    if mlvkh__yxlr in (('init_binary_str_index',
        'bodo.hiframes.pd_index_ext'), ('init_numeric_index',
        'bodo.hiframes.pd_index_ext'), ('init_categorical_index',
        'bodo.hiframes.pd_index_ext'), ('init_datetime_index',
        'bodo.hiframes.pd_index_ext'), ('init_timedelta_index',
        'bodo.hiframes.pd_index_ext'), ('init_heter_index',
        'bodo.hiframes.pd_index_ext')):
        return pd.Index(get_const_value_inner(func_ir, qeag__rxbku.args[0],
            arg_types, typemap, updated_containers))
    if mlvkh__yxlr == ('str_arr_from_sequence', 'bodo.libs.str_arr_ext'):
        return np.array(get_const_value_inner(func_ir, qeag__rxbku.args[0],
            arg_types, typemap, updated_containers))
    if mlvkh__yxlr == ('init_range_index', 'bodo.hiframes.pd_index_ext'):
        return pd.RangeIndex(get_const_value_inner(func_ir, qeag__rxbku.
            args[0], arg_types, typemap, updated_containers),
            get_const_value_inner(func_ir, qeag__rxbku.args[1], arg_types,
            typemap, updated_containers), get_const_value_inner(func_ir,
            qeag__rxbku.args[2], arg_types, typemap, updated_containers))
    if mlvkh__yxlr == ('len', 'builtins') and typemap and isinstance(typemap
        .get(qeag__rxbku.args[0].name, None), types.BaseTuple):
        return len(typemap[qeag__rxbku.args[0].name])
    if mlvkh__yxlr == ('len', 'builtins'):
        xprui__yhsmr = guard(get_definition, func_ir, qeag__rxbku.args[0])
        if isinstance(xprui__yhsmr, ir.Expr) and xprui__yhsmr.op in (
            'build_tuple', 'build_list', 'build_set', 'build_map'):
            return len(xprui__yhsmr.items)
        return len(get_const_value_inner(func_ir, qeag__rxbku.args[0],
            arg_types, typemap, updated_containers))
    if mlvkh__yxlr == ('CategoricalDtype', 'pandas'):
        kws = dict(qeag__rxbku.kws)
        vkj__gmf = get_call_expr_arg('CategoricalDtype', qeag__rxbku.args,
            kws, 0, 'categories', '')
        oklt__qegec = get_call_expr_arg('CategoricalDtype', qeag__rxbku.
            args, kws, 1, 'ordered', False)
        if oklt__qegec is not False:
            oklt__qegec = get_const_value_inner(func_ir, oklt__qegec,
                arg_types, typemap, updated_containers)
        if vkj__gmf == '':
            vkj__gmf = None
        else:
            vkj__gmf = get_const_value_inner(func_ir, vkj__gmf, arg_types,
                typemap, updated_containers)
        return pd.CategoricalDtype(vkj__gmf, oklt__qegec)
    if mlvkh__yxlr == ('dtype', 'numpy'):
        return np.dtype(get_const_value_inner(func_ir, qeag__rxbku.args[0],
            arg_types, typemap, updated_containers))
    if mlvkh__yxlr is not None and mlvkh__yxlr[1] == 'numpy' and mlvkh__yxlr[0
        ] in _np_type_names:
        return getattr(np, mlvkh__yxlr[0])(get_const_value_inner(func_ir,
            qeag__rxbku.args[0], arg_types, typemap, updated_containers))
    if mlvkh__yxlr is not None and len(mlvkh__yxlr) == 2 and mlvkh__yxlr[1
        ] == 'pandas' and mlvkh__yxlr[0] in ('Int8Dtype', 'Int16Dtype',
        'Int32Dtype', 'Int64Dtype', 'UInt8Dtype', 'UInt16Dtype',
        'UInt32Dtype', 'UInt64Dtype'):
        return getattr(pd, mlvkh__yxlr[0])()
    if mlvkh__yxlr is not None and len(mlvkh__yxlr) == 2 and isinstance(
        mlvkh__yxlr[1], ir.Var):
        xxe__dkbpg = get_const_value_inner(func_ir, mlvkh__yxlr[1],
            arg_types, typemap, updated_containers)
        args = [get_const_value_inner(func_ir, uofbk__qyb, arg_types,
            typemap, updated_containers) for uofbk__qyb in qeag__rxbku.args]
        kws = {dhrap__vus[0]: get_const_value_inner(func_ir, dhrap__vus[1],
            arg_types, typemap, updated_containers) for dhrap__vus in
            qeag__rxbku.kws}
        return getattr(xxe__dkbpg, mlvkh__yxlr[0])(*args, **kws)
    if mlvkh__yxlr is not None and len(mlvkh__yxlr) == 2 and mlvkh__yxlr[1
        ] == 'bodo' and mlvkh__yxlr[0] in bodo_types_with_params:
        args = tuple(get_const_value_inner(func_ir, uofbk__qyb, arg_types,
            typemap, updated_containers) for uofbk__qyb in qeag__rxbku.args)
        kwargs = {fgt__smxk: get_const_value_inner(func_ir, uofbk__qyb,
            arg_types, typemap, updated_containers) for fgt__smxk,
            uofbk__qyb in dict(qeag__rxbku.kws).items()}
        return getattr(bodo, mlvkh__yxlr[0])(*args, **kwargs)
    if is_call(qeag__rxbku) and typemap and isinstance(typemap.get(
        qeag__rxbku.func.name, None), types.Dispatcher):
        py_func = typemap[qeag__rxbku.func.name].dispatcher.py_func
        require(qeag__rxbku.vararg is None)
        args = tuple(get_const_value_inner(func_ir, uofbk__qyb, arg_types,
            typemap, updated_containers) for uofbk__qyb in qeag__rxbku.args)
        kwargs = {fgt__smxk: get_const_value_inner(func_ir, uofbk__qyb,
            arg_types, typemap, updated_containers) for fgt__smxk,
            uofbk__qyb in dict(qeag__rxbku.kws).items()}
        arg_types = tuple(bodo.typeof(uofbk__qyb) for uofbk__qyb in args)
        kw_types = {dxknr__jdi: bodo.typeof(uofbk__qyb) for dxknr__jdi,
            uofbk__qyb in kwargs.items()}
        require(_func_is_pure(py_func, arg_types, kw_types))
        return py_func(*args, **kwargs)
    raise GuardException('Constant value not found')


def _func_is_pure(py_func, arg_types, kw_types):
    from bodo.hiframes.pd_dataframe_ext import DataFrameType
    from bodo.hiframes.pd_series_ext import SeriesType
    from bodo.ir.csv_ext import CsvReader
    from bodo.ir.json_ext import JsonReader
    from bodo.ir.parquet_ext import ParquetReader
    from bodo.ir.sql_ext import SqlReader
    f_ir, typemap, tpsqe__folq, tpsqe__folq = bodo.compiler.get_func_type_info(
        py_func, arg_types, kw_types)
    for block in f_ir.blocks.values():
        for stmt in block.body:
            if isinstance(stmt, ir.Print):
                return False
            if isinstance(stmt, (CsvReader, JsonReader, ParquetReader,
                SqlReader)):
                return False
            if is_setitem(stmt) and isinstance(guard(get_definition, f_ir,
                stmt.target), ir.Arg):
                return False
            if is_assign(stmt):
                rhs = stmt.value
                if isinstance(rhs, ir.Yield):
                    return False
                if is_call(rhs):
                    rnpj__bhi = guard(get_definition, f_ir, rhs.func)
                    if isinstance(rnpj__bhi, ir.Const) and isinstance(rnpj__bhi
                        .value, numba.core.dispatcher.ObjModeLiftedWith):
                        return False
                    ilv__mwhop = guard(find_callname, f_ir, rhs)
                    if ilv__mwhop is None:
                        return False
                    func_name, enie__dyqfv = ilv__mwhop
                    if enie__dyqfv == 'pandas' and func_name.startswith('read_'
                        ):
                        return False
                    if ilv__mwhop in (('fromfile', 'numpy'), ('file_read',
                        'bodo.io.np_io')):
                        return False
                    if ilv__mwhop == ('File', 'h5py'):
                        return False
                    if isinstance(enie__dyqfv, ir.Var):
                        pnj__gsmn = typemap[enie__dyqfv.name]
                        if isinstance(pnj__gsmn, (DataFrameType, SeriesType)
                            ) and func_name in ('to_csv', 'to_excel',
                            'to_json', 'to_sql', 'to_pickle', 'to_parquet',
                            'info'):
                            return False
                        if isinstance(pnj__gsmn, types.Array
                            ) and func_name == 'tofile':
                            return False
                        if isinstance(pnj__gsmn, bodo.LoggingLoggerType):
                            return False
                        if str(pnj__gsmn).startswith('Mpl'):
                            return False
                        if (func_name in container_update_method_names and
                            isinstance(guard(get_definition, f_ir,
                            enie__dyqfv), ir.Arg)):
                            return False
                    if enie__dyqfv in ('numpy.random', 'time', 'logging',
                        'matplotlib.pyplot'):
                        return False
    return True


def fold_argument_types(pysig, args, kws):

    def normal_handler(index, param, value):
        return value

    def default_handler(index, param, default):
        return types.Omitted(default)

    def stararg_handler(index, param, values):
        return types.StarArgTuple(values)
    args = fold_arguments(pysig, args, kws, normal_handler, default_handler,
        stararg_handler)
    return args


def get_const_func_output_type(func, arg_types, kw_types, typing_context,
    target_context, is_udf=True):
    from bodo.hiframes.pd_series_ext import HeterogeneousSeriesType, SeriesType
    py_func = None
    if isinstance(func, types.MakeFunctionLiteral):
        own__jfoio = func.literal_value.code
        dddr__tasir = {'np': np, 'pd': pd, 'numba': numba, 'bodo': bodo}
        if hasattr(func.literal_value, 'globals'):
            dddr__tasir = func.literal_value.globals
        f_ir = numba.core.ir_utils.get_ir_of_code(dddr__tasir, own__jfoio)
        fix_struct_return(f_ir)
        typemap, ori__ksw, cvb__cbka, tpsqe__folq = (numba.core.
            typed_passes.type_inference_stage(typing_context,
            target_context, f_ir, arg_types, None))
    elif isinstance(func, bodo.utils.typing.FunctionLiteral):
        py_func = func.literal_value
        f_ir, typemap, cvb__cbka, ori__ksw = bodo.compiler.get_func_type_info(
            py_func, arg_types, kw_types)
    elif isinstance(func, CPUDispatcher):
        py_func = func.py_func
        f_ir, typemap, cvb__cbka, ori__ksw = bodo.compiler.get_func_type_info(
            py_func, arg_types, kw_types)
    else:
        if not isinstance(func, types.Dispatcher):
            if isinstance(func, types.Function):
                raise BodoError(
                    f'Bodo does not support built-in functions yet, {func}')
            else:
                raise BodoError(f'Function type expected, not {func}')
        py_func = func.dispatcher.py_func
        f_ir, typemap, cvb__cbka, ori__ksw = bodo.compiler.get_func_type_info(
            py_func, arg_types, kw_types)
    if is_udf and isinstance(ori__ksw, types.DictType):
        tupf__aso = guard(get_struct_keynames, f_ir, typemap)
        if tupf__aso is not None:
            ori__ksw = StructType((ori__ksw.value_type,) * len(tupf__aso),
                tupf__aso)
    if is_udf and isinstance(ori__ksw, (SeriesType, HeterogeneousSeriesType)):
        bqo__dxc = numba.core.registry.cpu_target.typing_context
        btw__czh = numba.core.registry.cpu_target.target_context
        duwc__gipuv = bodo.transforms.series_pass.SeriesPass(f_ir, bqo__dxc,
            btw__czh, typemap, cvb__cbka, {})
        sgrok__xmrbz = duwc__gipuv.run()
        if sgrok__xmrbz:
            sgrok__xmrbz = duwc__gipuv.run()
            if sgrok__xmrbz:
                duwc__gipuv.run()
        trm__bpbkx = compute_cfg_from_blocks(f_ir.blocks)
        naf__frp = [guard(_get_const_series_info, f_ir.blocks[uebly__lvhre],
            f_ir, typemap) for uebly__lvhre in trm__bpbkx.exit_points() if
            isinstance(f_ir.blocks[uebly__lvhre].body[-1], ir.Return)]
        if None in naf__frp or len(pd.Series(naf__frp).unique()) != 1:
            ori__ksw.const_info = None
        else:
            ori__ksw.const_info = naf__frp[0]
    return ori__ksw


def _get_const_series_info(block, f_ir, typemap):
    from bodo.hiframes.pd_series_ext import HeterogeneousSeriesType
    assert isinstance(block.body[-1], ir.Return)
    qzucz__pishy = block.body[-1].value
    ahvu__xfap = get_definition(f_ir, qzucz__pishy)
    require(is_expr(ahvu__xfap, 'cast'))
    ahvu__xfap = get_definition(f_ir, ahvu__xfap.value)
    require(is_call(ahvu__xfap) and find_callname(f_ir, ahvu__xfap) == (
        'init_series', 'bodo.hiframes.pd_series_ext'))
    eno__hngk = ahvu__xfap.args[1]
    yzpqq__trd = tuple(get_const_value_inner(f_ir, eno__hngk, typemap=typemap))
    if isinstance(typemap[qzucz__pishy.name], HeterogeneousSeriesType):
        return len(typemap[qzucz__pishy.name].data), yzpqq__trd
    erykp__byu = ahvu__xfap.args[0]
    vzu__ncxl = get_definition(f_ir, erykp__byu)
    func_name, sfvi__tfybg = find_callname(f_ir, vzu__ncxl)
    if is_call(vzu__ncxl) and bodo.utils.utils.is_alloc_callname(func_name,
        sfvi__tfybg):
        xhczu__zwj = vzu__ncxl.args[0]
        dnplj__ywfov = get_const_value_inner(f_ir, xhczu__zwj, typemap=typemap)
        return dnplj__ywfov, yzpqq__trd
    if is_call(vzu__ncxl) and find_callname(f_ir, vzu__ncxl) in [('asarray',
        'numpy'), ('str_arr_from_sequence', 'bodo.libs.str_arr_ext'), (
        'build_nullable_tuple', 'bodo.libs.nullable_tuple_ext')]:
        erykp__byu = vzu__ncxl.args[0]
        vzu__ncxl = get_definition(f_ir, erykp__byu)
    require(is_expr(vzu__ncxl, 'build_tuple') or is_expr(vzu__ncxl,
        'build_list'))
    return len(vzu__ncxl.items), yzpqq__trd


def extract_keyvals_from_struct_map(f_ir, build_map, loc, scope, typemap=None):
    cup__pkj = []
    wxs__ppby = []
    values = []
    for dxknr__jdi, uofbk__qyb in build_map.items:
        vfr__qnwz = find_const(f_ir, dxknr__jdi)
        require(isinstance(vfr__qnwz, str))
        wxs__ppby.append(vfr__qnwz)
        cup__pkj.append(dxknr__jdi)
        values.append(uofbk__qyb)
    apng__uwt = ir.Var(scope, mk_unique_var('val_tup'), loc)
    kcuq__xwgi = ir.Assign(ir.Expr.build_tuple(values, loc), apng__uwt, loc)
    f_ir._definitions[apng__uwt.name] = [kcuq__xwgi.value]
    yrq__sgior = ir.Var(scope, mk_unique_var('key_tup'), loc)
    ezq__vcir = ir.Assign(ir.Expr.build_tuple(cup__pkj, loc), yrq__sgior, loc)
    f_ir._definitions[yrq__sgior.name] = [ezq__vcir.value]
    if typemap is not None:
        typemap[apng__uwt.name] = types.Tuple([typemap[uofbk__qyb.name] for
            uofbk__qyb in values])
        typemap[yrq__sgior.name] = types.Tuple([typemap[uofbk__qyb.name] for
            uofbk__qyb in cup__pkj])
    return wxs__ppby, apng__uwt, kcuq__xwgi, yrq__sgior, ezq__vcir


def _replace_const_map_return(f_ir, block, label):
    require(isinstance(block.body[-1], ir.Return))
    ezqec__gaa = block.body[-1].value
    sqxy__dfxy = guard(get_definition, f_ir, ezqec__gaa)
    require(is_expr(sqxy__dfxy, 'cast'))
    ahvu__xfap = guard(get_definition, f_ir, sqxy__dfxy.value)
    require(is_expr(ahvu__xfap, 'build_map'))
    require(len(ahvu__xfap.items) > 0)
    loc = block.loc
    scope = block.scope
    wxs__ppby, apng__uwt, kcuq__xwgi, yrq__sgior, ezq__vcir = (
        extract_keyvals_from_struct_map(f_ir, ahvu__xfap, loc, scope))
    mxq__kgxxw = ir.Var(scope, mk_unique_var('conv_call'), loc)
    qbqus__xqfx = ir.Assign(ir.Global('struct_if_heter_dict', bodo.utils.
        conversion.struct_if_heter_dict, loc), mxq__kgxxw, loc)
    f_ir._definitions[mxq__kgxxw.name] = [qbqus__xqfx.value]
    kofyl__lvyhb = ir.Var(scope, mk_unique_var('struct_val'), loc)
    teqq__aunoc = ir.Assign(ir.Expr.call(mxq__kgxxw, [apng__uwt, yrq__sgior
        ], {}, loc), kofyl__lvyhb, loc)
    f_ir._definitions[kofyl__lvyhb.name] = [teqq__aunoc.value]
    sqxy__dfxy.value = kofyl__lvyhb
    ahvu__xfap.items = [(dxknr__jdi, dxknr__jdi) for dxknr__jdi,
        tpsqe__folq in ahvu__xfap.items]
    block.body = block.body[:-2] + [kcuq__xwgi, ezq__vcir, qbqus__xqfx,
        teqq__aunoc] + block.body[-2:]
    return tuple(wxs__ppby)


def get_struct_keynames(f_ir, typemap):
    trm__bpbkx = compute_cfg_from_blocks(f_ir.blocks)
    ognir__aix = list(trm__bpbkx.exit_points())[0]
    block = f_ir.blocks[ognir__aix]
    require(isinstance(block.body[-1], ir.Return))
    ezqec__gaa = block.body[-1].value
    sqxy__dfxy = guard(get_definition, f_ir, ezqec__gaa)
    require(is_expr(sqxy__dfxy, 'cast'))
    ahvu__xfap = guard(get_definition, f_ir, sqxy__dfxy.value)
    require(is_call(ahvu__xfap) and find_callname(f_ir, ahvu__xfap) == (
        'struct_if_heter_dict', 'bodo.utils.conversion'))
    return get_overload_const_list(typemap[ahvu__xfap.args[1].name])


def fix_struct_return(f_ir):
    hhe__ecwe = None
    trm__bpbkx = compute_cfg_from_blocks(f_ir.blocks)
    for ognir__aix in trm__bpbkx.exit_points():
        hhe__ecwe = guard(_replace_const_map_return, f_ir, f_ir.blocks[
            ognir__aix], ognir__aix)
    return hhe__ecwe


def update_node_list_definitions(node_list, func_ir):
    loc = ir.Loc('', 0)
    jfakh__gwlik = ir.Block(ir.Scope(None, loc), loc)
    jfakh__gwlik.body = node_list
    build_definitions({(0): jfakh__gwlik}, func_ir._definitions)
    return


NESTED_TUP_SENTINEL = '$BODO_NESTED_TUP'


def gen_const_val_str(c):
    if isinstance(c, tuple):
        return "'{}{}', ".format(NESTED_TUP_SENTINEL, len(c)) + ', '.join(
            gen_const_val_str(uofbk__qyb) for uofbk__qyb in c)
    if isinstance(c, str):
        return "'{}'".format(c)
    if isinstance(c, (pd.Timestamp, pd.Timedelta, float)):
        return "'{}'".format(c)
    return str(c)


def gen_const_tup(vals):
    futii__qle = ', '.join(gen_const_val_str(c) for c in vals)
    return '({}{})'.format(futii__qle, ',' if len(vals) == 1 else '')


def get_const_tup_vals(c_typ):
    vals = get_overload_const_list(c_typ)
    return _get_original_nested_tups(vals)


def _get_original_nested_tups(vals):
    for tioty__yqhj in range(len(vals) - 1, -1, -1):
        uofbk__qyb = vals[tioty__yqhj]
        if isinstance(uofbk__qyb, str) and uofbk__qyb.startswith(
            NESTED_TUP_SENTINEL):
            cmy__oqc = int(uofbk__qyb[len(NESTED_TUP_SENTINEL):])
            return _get_original_nested_tups(tuple(vals[:tioty__yqhj]) + (
                tuple(vals[tioty__yqhj + 1:tioty__yqhj + cmy__oqc + 1]),) +
                tuple(vals[tioty__yqhj + cmy__oqc + 1:]))
    return tuple(vals)


def get_call_expr_arg(f_name, args, kws, arg_no, arg_name, default=None,
    err_msg=None, use_default=False):
    uifbl__ykmhe = None
    if len(args) > arg_no and arg_no >= 0:
        uifbl__ykmhe = args[arg_no]
        if arg_name in kws:
            err_msg = (
                f"{f_name}() got multiple values for argument '{arg_name}'")
            raise BodoError(err_msg)
    elif arg_name in kws:
        uifbl__ykmhe = kws[arg_name]
    if uifbl__ykmhe is None:
        if use_default or default is not None:
            return default
        if err_msg is None:
            err_msg = "{} requires '{}' argument".format(f_name, arg_name)
        raise BodoError(err_msg)
    return uifbl__ykmhe


def set_call_expr_arg(var, args, kws, arg_no, arg_name, add_if_missing=False):
    if len(args) > arg_no:
        args[arg_no] = var
    elif add_if_missing or arg_name in kws:
        kws[arg_name] = var
    else:
        raise BodoError('cannot set call argument since does not exist')


def avoid_udf_inline(py_func, arg_types, kw_types):
    from bodo.hiframes.pd_dataframe_ext import DataFrameType
    f_ir = numba.core.compiler.run_frontend(py_func, inline_closures=True)
    if '_bodo_inline' in kw_types and is_overload_constant_bool(kw_types[
        '_bodo_inline']):
        return not get_overload_const_bool(kw_types['_bodo_inline'])
    if any(isinstance(t, DataFrameType) for t in arg_types + tuple(kw_types
        .values())):
        return True
    for block in f_ir.blocks.values():
        if isinstance(block.body[-1], (ir.Raise, ir.StaticRaise)):
            return True
        for stmt in block.body:
            if isinstance(stmt, ir.EnterWith):
                return True
    return False


def replace_func(pass_info, func, args, const=False, pre_nodes=None,
    extra_globals=None, pysig=None, kws=None, inline_bodo_calls=False,
    run_full_pipeline=False):
    ayk__pftyq = {'numba': numba, 'np': np, 'bodo': bodo, 'pd': pd}
    if extra_globals is not None:
        ayk__pftyq.update(extra_globals)
    func.__globals__.update(ayk__pftyq)
    if pysig is not None:
        pre_nodes = [] if pre_nodes is None else pre_nodes
        scope = next(iter(pass_info.func_ir.blocks.values())).scope
        loc = scope.loc

        def normal_handler(index, param, default):
            return default

        def default_handler(index, param, default):
            cnfls__smmeu = ir.Var(scope, mk_unique_var('defaults'), loc)
            try:
                pass_info.typemap[cnfls__smmeu.name] = types.literal(default)
            except:
                pass_info.typemap[cnfls__smmeu.name] = numba.typeof(default)
            alwzo__emgek = ir.Assign(ir.Const(default, loc), cnfls__smmeu, loc)
            pre_nodes.append(alwzo__emgek)
            return cnfls__smmeu
        args = numba.core.typing.fold_arguments(pysig, args, kws,
            normal_handler, default_handler, normal_handler)
    tdyn__qpka = tuple(pass_info.typemap[uofbk__qyb.name] for uofbk__qyb in
        args)
    if const:
        nse__gouta = []
        for tioty__yqhj, uifbl__ykmhe in enumerate(args):
            xxe__dkbpg = guard(find_const, pass_info.func_ir, uifbl__ykmhe)
            if xxe__dkbpg:
                nse__gouta.append(types.literal(xxe__dkbpg))
            else:
                nse__gouta.append(tdyn__qpka[tioty__yqhj])
        tdyn__qpka = tuple(nse__gouta)
    return ReplaceFunc(func, tdyn__qpka, args, ayk__pftyq,
        inline_bodo_calls, run_full_pipeline, pre_nodes)


def is_var_size_item_array_type(t):
    assert is_array_typ(t, False)
    return t == string_array_type or isinstance(t, ArrayItemArrayType
        ) or isinstance(t, StructArrayType) and any(
        is_var_size_item_array_type(djj__fphdq) for djj__fphdq in t.data)


def gen_init_varsize_alloc_sizes(t):
    if t == string_array_type:
        itzbz__aqwrr = 'num_chars_{}'.format(ir_utils.next_label())
        return f'  {itzbz__aqwrr} = 0\n', (itzbz__aqwrr,)
    if isinstance(t, ArrayItemArrayType):
        uvhv__haf, tds__xpbe = gen_init_varsize_alloc_sizes(t.dtype)
        itzbz__aqwrr = 'num_items_{}'.format(ir_utils.next_label())
        return f'  {itzbz__aqwrr} = 0\n' + uvhv__haf, (itzbz__aqwrr,
            ) + tds__xpbe
    return '', ()


def gen_varsize_item_sizes(t, item, var_names):
    if t == string_array_type:
        return '    {} += bodo.libs.str_arr_ext.get_utf8_size({})\n'.format(
            var_names[0], item)
    if isinstance(t, ArrayItemArrayType):
        return '    {} += len({})\n'.format(var_names[0], item
            ) + gen_varsize_array_counts(t.dtype, item, var_names[1:])
    return ''


def gen_varsize_array_counts(t, item, var_names):
    if t == string_array_type:
        return ('    {} += bodo.libs.str_arr_ext.get_num_total_chars({})\n'
            .format(var_names[0], item))
    return ''


def get_type_alloc_counts(t):
    if isinstance(t, (StructArrayType, TupleArrayType)):
        return 1 + sum(get_type_alloc_counts(djj__fphdq.dtype) for
            djj__fphdq in t.data)
    if isinstance(t, ArrayItemArrayType) or t == string_array_type:
        return 1 + get_type_alloc_counts(t.dtype)
    if isinstance(t, MapArrayType):
        return get_type_alloc_counts(t.key_arr_type) + get_type_alloc_counts(t
            .value_arr_type)
    if bodo.utils.utils.is_array_typ(t, False) or t == bodo.string_type:
        return 1
    if isinstance(t, StructType):
        return sum(get_type_alloc_counts(djj__fphdq) for djj__fphdq in t.data)
    if isinstance(t, types.BaseTuple):
        return sum(get_type_alloc_counts(djj__fphdq) for djj__fphdq in t.types)
    return 0


def find_udf_str_name(obj_dtype, func_name, typing_context, caller_name):
    mjew__ifkox = typing_context.resolve_getattr(obj_dtype, func_name)
    if mjew__ifkox is None:
        ckdp__gnqj = types.misc.Module(np)
        try:
            mjew__ifkox = typing_context.resolve_getattr(ckdp__gnqj, func_name)
        except AttributeError as vyp__apm:
            mjew__ifkox = None
        if mjew__ifkox is None:
            raise BodoError(
                f"{caller_name}(): No Pandas method or Numpy function found with the name '{func_name}'."
                )
    return mjew__ifkox


def get_udf_str_return_type(obj_dtype, func_name, typing_context,
    caller_name, axis=None):
    mjew__ifkox = find_udf_str_name(obj_dtype, func_name, typing_context,
        caller_name)
    if isinstance(mjew__ifkox, types.BoundFunction):
        if axis is not None:
            zkeas__bma = mjew__ifkox.get_call_type(typing_context, (), {
                'axis': axis})
        else:
            zkeas__bma = mjew__ifkox.get_call_type(typing_context, (), {})
        return zkeas__bma.return_type
    else:
        if bodo.utils.typing.is_numpy_ufunc(mjew__ifkox):
            zkeas__bma = mjew__ifkox.get_call_type(typing_context, (
                obj_dtype,), {})
            return zkeas__bma.return_type
        raise BodoError(
            f"{caller_name}(): Only Pandas methods and np.ufunc are supported as string literals. '{func_name}' not supported."
            )


def get_pandas_method_str_impl(obj_dtype, func_name, typing_context,
    caller_name, axis=None):
    mjew__ifkox = find_udf_str_name(obj_dtype, func_name, typing_context,
        caller_name)
    if isinstance(mjew__ifkox, types.BoundFunction):
        xvtjd__luvbh = mjew__ifkox.template
        if axis is not None:
            return xvtjd__luvbh._overload_func(obj_dtype, axis=axis)
        else:
            return xvtjd__luvbh._overload_func(obj_dtype)
    return None


def dict_to_const_keys_var_values_lists(dict_var, func_ir, arg_types,
    typemap, updated_containers, require_const_map, label):
    require(isinstance(dict_var, ir.Var))
    gykp__xcdaw = get_definition(func_ir, dict_var)
    require(isinstance(gykp__xcdaw, ir.Expr))
    require(gykp__xcdaw.op == 'build_map')
    nyukg__qmzy = gykp__xcdaw.items
    cup__pkj = []
    values = []
    vzv__besdm = False
    for tioty__yqhj in range(len(nyukg__qmzy)):
        jvls__utpv, value = nyukg__qmzy[tioty__yqhj]
        try:
            svs__aintw = get_const_value_inner(func_ir, jvls__utpv,
                arg_types, typemap, updated_containers)
            cup__pkj.append(svs__aintw)
            values.append(value)
        except GuardException as vyp__apm:
            require_const_map[jvls__utpv] = label
            vzv__besdm = True
    if vzv__besdm:
        raise GuardException
    return cup__pkj, values


def _get_const_keys_from_dict(args, func_ir, build_map, err_msg, loc):
    try:
        cup__pkj = tuple(get_const_value_inner(func_ir, t[0], args) for t in
            build_map.items)
    except GuardException as vyp__apm:
        raise BodoError(err_msg, loc)
    if not all(isinstance(c, (str, int)) for c in cup__pkj):
        raise BodoError(err_msg, loc)
    return cup__pkj


def _convert_const_key_dict(args, func_ir, build_map, err_msg, scope, loc,
    output_sentinel_tuple=False):
    cup__pkj = _get_const_keys_from_dict(args, func_ir, build_map, err_msg, loc
        )
    zov__jhcs = []
    gpw__xvmt = [bodo.transforms.typing_pass._create_const_var(dxknr__jdi,
        'dict_key', scope, loc, zov__jhcs) for dxknr__jdi in cup__pkj]
    gaxv__anbo = [t[1] for t in build_map.items]
    if output_sentinel_tuple:
        zljyh__zcuco = ir.Var(scope, mk_unique_var('sentinel'), loc)
        gqpw__jhcr = ir.Var(scope, mk_unique_var('dict_tup'), loc)
        zov__jhcs.append(ir.Assign(ir.Const('__bodo_tup', loc),
            zljyh__zcuco, loc))
        fgyos__ljsi = [zljyh__zcuco] + gpw__xvmt + gaxv__anbo
        zov__jhcs.append(ir.Assign(ir.Expr.build_tuple(fgyos__ljsi, loc),
            gqpw__jhcr, loc))
        return (gqpw__jhcr,), zov__jhcs
    else:
        lpg__nwg = ir.Var(scope, mk_unique_var('values_tup'), loc)
        hfawa__pejj = ir.Var(scope, mk_unique_var('idx_tup'), loc)
        zov__jhcs.append(ir.Assign(ir.Expr.build_tuple(gaxv__anbo, loc),
            lpg__nwg, loc))
        zov__jhcs.append(ir.Assign(ir.Expr.build_tuple(gpw__xvmt, loc),
            hfawa__pejj, loc))
        return (lpg__nwg, hfawa__pejj), zov__jhcs
