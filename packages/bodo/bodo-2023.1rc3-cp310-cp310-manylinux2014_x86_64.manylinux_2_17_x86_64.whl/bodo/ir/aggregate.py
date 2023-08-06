"""IR node for the groupby"""
import ctypes
import operator
import types as pytypes
from collections import defaultdict, namedtuple
import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from numba.core import cgutils, compiler, ir, ir_utils, types
from numba.core.analysis import compute_use_defs
from numba.core.ir_utils import build_definitions, compile_to_numba_ir, find_callname, find_const, find_topo_order, get_definition, get_ir_of_code, get_name_var_table, guard, is_getitem, mk_unique_var, next_label, remove_dels, replace_arg_nodes, replace_var_names, replace_vars_inner, visit_vars_inner
from numba.core.typing import signature
from numba.core.typing.templates import AbstractTemplate, infer_global
from numba.extending import intrinsic
from numba.parfors.parfor import Parfor, unwrap_parfor_blocks, wrap_parfor_blocks
import bodo
from bodo.hiframes.datetime_date_ext import DatetimeDateArrayType
from bodo.hiframes.pd_series_ext import SeriesType
from bodo.libs.array import arr_info_list_to_table, array_to_info, cpp_table_to_py_data, decref_table_array, delete_info_decref_array, delete_table, delete_table_decref_arrays, groupby_and_aggregate, info_from_table, info_to_array, py_data_to_cpp_table
from bodo.libs.array_item_arr_ext import ArrayItemArrayType, pre_alloc_array_item_array
from bodo.libs.binary_arr_ext import BinaryArrayType, pre_alloc_binary_array
from bodo.libs.bool_arr_ext import BooleanArrayType
from bodo.libs.decimal_arr_ext import DecimalArrayType, alloc_decimal_array
from bodo.libs.float_arr_ext import FloatingArrayType
from bodo.libs.int_arr_ext import IntDtype, IntegerArrayType
from bodo.libs.str_arr_ext import StringArrayType, pre_alloc_string_array, string_array_type
from bodo.libs.str_ext import string_type
from bodo.transforms import distributed_analysis, distributed_pass
from bodo.transforms.distributed_analysis import Distribution
from bodo.transforms.table_column_del_pass import _compute_table_column_uses, _find_used_columns, ir_extension_table_column_use, remove_dead_column_extensions
from bodo.utils.transform import get_call_expr_arg
from bodo.utils.typing import BodoError, MetaType, decode_if_dict_array, dtype_to_array_type, get_index_data_arr_types, get_literal_value, get_overload_const_func, get_overload_const_list, get_overload_const_str, get_overload_constant_dict, is_overload_constant_dict, is_overload_constant_list, is_overload_constant_str, list_cumulative, to_str_arr_if_dict_array, type_has_unknown_cats, unwrap_typeref
from bodo.utils.utils import gen_getitem, incref, is_assign, is_call_assign, is_expr, is_null_pointer, is_var_assign
gb_agg_cfunc = {}
gb_agg_cfunc_addr = {}


@intrinsic
def add_agg_cfunc_sym(typingctx, func, sym):

    def codegen(context, builder, signature, args):
        fkjgg__snrom = func.signature
        if fkjgg__snrom == types.none(types.voidptr):
            itw__ltwb = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
                as_pointer()])
            mbllh__uzz = cgutils.get_or_insert_function(builder.module,
                itw__ltwb, sym._literal_value)
            builder.call(mbllh__uzz, [context.get_constant_null(
                fkjgg__snrom.args[0])])
        elif fkjgg__snrom == types.none(types.int64, types.voidptr, types.
            voidptr):
            itw__ltwb = lir.FunctionType(lir.VoidType(), [lir.IntType(64),
                lir.IntType(8).as_pointer(), lir.IntType(8).as_pointer()])
            mbllh__uzz = cgutils.get_or_insert_function(builder.module,
                itw__ltwb, sym._literal_value)
            builder.call(mbllh__uzz, [context.get_constant(types.int64, 0),
                context.get_constant_null(fkjgg__snrom.args[1]), context.
                get_constant_null(fkjgg__snrom.args[2])])
        else:
            itw__ltwb = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
                as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(64).
                as_pointer()])
            mbllh__uzz = cgutils.get_or_insert_function(builder.module,
                itw__ltwb, sym._literal_value)
            builder.call(mbllh__uzz, [context.get_constant_null(
                fkjgg__snrom.args[0]), context.get_constant_null(
                fkjgg__snrom.args[1]), context.get_constant_null(
                fkjgg__snrom.args[2])])
        context.add_linking_libs([gb_agg_cfunc[sym._literal_value]._library])
        return
    return types.none(func, sym), codegen


@numba.jit
def get_agg_udf_addr(name):
    with numba.objmode(addr='int64'):
        addr = gb_agg_cfunc_addr[name]
    return addr


class AggUDFStruct(object):

    def __init__(self, regular_udf_funcs=None, general_udf_funcs=None):
        assert regular_udf_funcs is not None or general_udf_funcs is not None
        self.regular_udfs = False
        self.general_udfs = False
        self.regular_udf_cfuncs = None
        self.general_udf_cfunc = None
        if regular_udf_funcs is not None:
            (self.var_typs, self.init_func, self.update_all_func, self.
                combine_all_func, self.eval_all_func) = regular_udf_funcs
            self.regular_udfs = True
        if general_udf_funcs is not None:
            self.general_udf_funcs = general_udf_funcs
            self.general_udfs = True

    def set_regular_cfuncs(self, update_cb, combine_cb, eval_cb):
        assert self.regular_udfs and self.regular_udf_cfuncs is None
        self.regular_udf_cfuncs = [update_cb, combine_cb, eval_cb]

    def set_general_cfunc(self, general_udf_cb):
        assert self.general_udfs and self.general_udf_cfunc is None
        self.general_udf_cfunc = general_udf_cb


AggFuncStruct = namedtuple('AggFuncStruct', ['func', 'ftype'])
supported_agg_funcs = ['no_op', 'ngroup', 'head', 'transform', 'size',
    'shift', 'sum', 'count', 'nunique', 'median', 'cumsum', 'cumprod',
    'cummin', 'cummax', 'mean', 'min', 'max', 'prod', 'first', 'last',
    'idxmin', 'idxmax', 'var', 'std', 'boolor_agg', 'udf', 'gen_udf']
supported_transform_funcs = ['no_op', 'sum', 'count', 'nunique', 'median',
    'mean', 'min', 'max', 'prod', 'first', 'last', 'var', 'std']


def get_agg_func(func_ir, func_name, rhs, series_type=None, typemap=None):
    if func_name == 'no_op':
        raise BodoError('Unknown aggregation function used in groupby.')
    if series_type is None:
        series_type = SeriesType(types.float64)
    if func_name in {'var', 'std'}:
        func = pytypes.SimpleNamespace()
        func.ftype = func_name
        func.fname = func_name
        func.ncols_pre_shuffle = 3
        func.ncols_post_shuffle = 4
        return func
    if func_name in {'first', 'last', 'boolor_agg'}:
        func = pytypes.SimpleNamespace()
        func.ftype = func_name
        func.fname = func_name
        func.ncols_pre_shuffle = 1
        func.ncols_post_shuffle = 1
        return func
    if func_name in {'idxmin', 'idxmax'}:
        func = pytypes.SimpleNamespace()
        func.ftype = func_name
        func.fname = func_name
        func.ncols_pre_shuffle = 2
        func.ncols_post_shuffle = 2
        return func
    if func_name in supported_agg_funcs[:-8]:
        func = pytypes.SimpleNamespace()
        func.ftype = func_name
        func.fname = func_name
        func.ncols_pre_shuffle = 1
        func.ncols_post_shuffle = 1
        hzcyn__zpgw = True
        iojpr__jsxn = 1
        byliw__bjo = -1
        if isinstance(rhs, ir.Expr):
            for mwh__dxdy in rhs.kws:
                if func_name in list_cumulative:
                    if mwh__dxdy[0] == 'skipna':
                        hzcyn__zpgw = guard(find_const, func_ir, mwh__dxdy[1])
                        if not isinstance(hzcyn__zpgw, bool):
                            raise BodoError(
                                'For {} argument of skipna should be a boolean'
                                .format(func_name))
                if func_name == 'nunique':
                    if mwh__dxdy[0] == 'dropna':
                        hzcyn__zpgw = guard(find_const, func_ir, mwh__dxdy[1])
                        if not isinstance(hzcyn__zpgw, bool):
                            raise BodoError(
                                'argument of dropna to nunique should be a boolean'
                                )
        if func_name == 'shift' and (len(rhs.args) > 0 or len(rhs.kws) > 0):
            iojpr__jsxn = get_call_expr_arg('shift', rhs.args, dict(rhs.kws
                ), 0, 'periods', iojpr__jsxn)
            iojpr__jsxn = guard(find_const, func_ir, iojpr__jsxn)
        if func_name == 'head':
            byliw__bjo = get_call_expr_arg('head', rhs.args, dict(rhs.kws),
                0, 'n', 5)
            if not isinstance(byliw__bjo, int):
                byliw__bjo = guard(find_const, func_ir, byliw__bjo)
            if byliw__bjo < 0:
                raise BodoError(
                    f'groupby.{func_name} does not work with negative values.')
        func.skipdropna = hzcyn__zpgw
        func.periods = iojpr__jsxn
        func.head_n = byliw__bjo
        if func_name == 'transform':
            kws = dict(rhs.kws)
            lpin__wgpsa = get_call_expr_arg(func_name, rhs.args, kws, 0,
                'func', '')
            igdik__lxjuh = typemap[lpin__wgpsa.name]
            ntpyj__swzs = None
            if isinstance(igdik__lxjuh, str):
                ntpyj__swzs = igdik__lxjuh
            elif is_overload_constant_str(igdik__lxjuh):
                ntpyj__swzs = get_overload_const_str(igdik__lxjuh)
            elif bodo.utils.typing.is_builtin_function(igdik__lxjuh):
                ntpyj__swzs = bodo.utils.typing.get_builtin_function_name(
                    igdik__lxjuh)
            if ntpyj__swzs not in bodo.ir.aggregate.supported_transform_funcs[:
                ]:
                raise BodoError(f'unsupported transform function {ntpyj__swzs}'
                    )
            func.transform_func = supported_agg_funcs.index(ntpyj__swzs)
        else:
            func.transform_func = supported_agg_funcs.index('no_op')
        return func
    assert func_name in ['agg', 'aggregate']
    assert typemap is not None
    kws = dict(rhs.kws)
    lpin__wgpsa = get_call_expr_arg(func_name, rhs.args, kws, 0, 'func', '')
    if lpin__wgpsa == '':
        igdik__lxjuh = types.none
    else:
        igdik__lxjuh = typemap[lpin__wgpsa.name]
    if is_overload_constant_dict(igdik__lxjuh):
        nlmby__zot = get_overload_constant_dict(igdik__lxjuh)
        gcnbi__hlky = [get_agg_func_udf(func_ir, f_val, rhs, series_type,
            typemap) for f_val in nlmby__zot.values()]
        return gcnbi__hlky
    if igdik__lxjuh == types.none:
        return [get_agg_func_udf(func_ir, get_literal_value(typemap[f_val.
            name])[1], rhs, series_type, typemap) for f_val in kws.values()]
    if isinstance(igdik__lxjuh, types.BaseTuple) or is_overload_constant_list(
        igdik__lxjuh):
        gcnbi__hlky = []
        mgn__twe = 0
        if is_overload_constant_list(igdik__lxjuh):
            byvh__qgw = get_overload_const_list(igdik__lxjuh)
        else:
            byvh__qgw = igdik__lxjuh.types
        for t in byvh__qgw:
            if is_overload_constant_str(t):
                func_name = get_overload_const_str(t)
                gcnbi__hlky.append(get_agg_func(func_ir, func_name, rhs,
                    series_type, typemap))
            else:
                assert typemap is not None, 'typemap is required for agg UDF handling'
                func = _get_const_agg_func(t, func_ir)
                func.ftype = 'udf'
                func.fname = _get_udf_name(func)
                if func.fname == '<lambda>' and len(byvh__qgw) > 1:
                    func.fname = '<lambda_' + str(mgn__twe) + '>'
                    mgn__twe += 1
                gcnbi__hlky.append(func)
        return [gcnbi__hlky]
    if is_overload_constant_str(igdik__lxjuh):
        func_name = get_overload_const_str(igdik__lxjuh)
        return get_agg_func(func_ir, func_name, rhs, series_type, typemap)
    if bodo.utils.typing.is_builtin_function(igdik__lxjuh):
        func_name = bodo.utils.typing.get_builtin_function_name(igdik__lxjuh)
        return get_agg_func(func_ir, func_name, rhs, series_type, typemap)
    assert typemap is not None, 'typemap is required for agg UDF handling'
    func = _get_const_agg_func(typemap[rhs.args[0].name], func_ir)
    func.ftype = 'udf'
    func.fname = _get_udf_name(func)
    return func


def get_agg_func_udf(func_ir, f_val, rhs, series_type, typemap):
    if isinstance(f_val, str):
        return get_agg_func(func_ir, f_val, rhs, series_type, typemap)
    if bodo.utils.typing.is_builtin_function(f_val):
        func_name = bodo.utils.typing.get_builtin_function_name(f_val)
        return get_agg_func(func_ir, func_name, rhs, series_type, typemap)
    if isinstance(f_val, (tuple, list)):
        mgn__twe = 0
        duadw__hviyy = []
        for cso__nvfu in f_val:
            func = get_agg_func_udf(func_ir, cso__nvfu, rhs, series_type,
                typemap)
            if func.fname == '<lambda>' and len(f_val) > 1:
                func.fname = f'<lambda_{mgn__twe}>'
                mgn__twe += 1
            duadw__hviyy.append(func)
        return duadw__hviyy
    else:
        assert is_expr(f_val, 'make_function') or isinstance(f_val, (numba.
            core.registry.CPUDispatcher, types.Dispatcher))
        assert typemap is not None, 'typemap is required for agg UDF handling'
        func = _get_const_agg_func(f_val, func_ir)
        func.ftype = 'udf'
        func.fname = _get_udf_name(func)
        return func


def _get_udf_name(func):
    code = func.code if hasattr(func, 'code') else func.__code__
    ntpyj__swzs = code.co_name
    return ntpyj__swzs


def _get_const_agg_func(func_typ, func_ir):
    agg_func = get_overload_const_func(func_typ, func_ir)
    if is_expr(agg_func, 'make_function'):

        def agg_func_wrapper(A):
            return A
        agg_func_wrapper.__code__ = agg_func.code
        agg_func = agg_func_wrapper
        return agg_func
    return agg_func


@infer_global(type)
class TypeDt64(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        if len(args) == 1 and isinstance(args[0], (types.NPDatetime, types.
            NPTimedelta)):
            grpk__img = types.DType(args[0])
            return signature(grpk__img, *args)


class Aggregate(ir.Stmt):

    def __init__(self, df_out, df_in, key_names, gb_info_in, gb_info_out,
        out_vars, in_vars, in_key_inds, df_in_type, out_type,
        input_has_index, same_index, return_key, loc, func_name, dropna,
        _num_shuffle_keys):
        self.df_out = df_out
        self.df_in = df_in
        self.key_names = key_names
        self.gb_info_in = gb_info_in
        self.gb_info_out = gb_info_out
        self.out_vars = out_vars
        self.in_vars = in_vars
        self.in_key_inds = in_key_inds
        self.df_in_type = df_in_type
        self.out_type = out_type
        self.input_has_index = input_has_index
        self.same_index = same_index
        self.return_key = return_key
        self.loc = loc
        self.func_name = func_name
        self.dropna = dropna
        self._num_shuffle_keys = _num_shuffle_keys
        self.dead_in_inds = set()
        self.dead_out_inds = set()

    def get_live_in_vars(self):
        return [rtc__ucla for rtc__ucla in self.in_vars if rtc__ucla is not
            None]

    def get_live_out_vars(self):
        return [rtc__ucla for rtc__ucla in self.out_vars if rtc__ucla is not
            None]

    @property
    def is_in_table_format(self):
        return self.df_in_type.is_table_format

    @property
    def n_in_table_arrays(self):
        return len(self.df_in_type.columns
            ) if self.df_in_type.is_table_format else 1

    @property
    def n_in_cols(self):
        return self.n_in_table_arrays + len(self.in_vars) - 1

    @property
    def in_col_types(self):
        return list(self.df_in_type.data) + list(get_index_data_arr_types(
            self.df_in_type.index))

    @property
    def is_output_table(self):
        return not isinstance(self.out_type, SeriesType)

    @property
    def n_out_table_arrays(self):
        return len(self.out_type.table_type.arr_types) if not isinstance(self
            .out_type, SeriesType) else 1

    @property
    def n_out_cols(self):
        return self.n_out_table_arrays + len(self.out_vars) - 1

    @property
    def out_col_types(self):
        see__mzlai = [self.out_type.data] if isinstance(self.out_type,
            SeriesType) else list(self.out_type.table_type.arr_types)
        dmqre__ddto = list(get_index_data_arr_types(self.out_type.index))
        return see__mzlai + dmqre__ddto

    def update_dead_col_info(self):
        for qvfwk__siu in self.dead_out_inds:
            self.gb_info_out.pop(qvfwk__siu, None)
        if not self.input_has_index:
            self.dead_in_inds.add(self.n_in_cols - 1)
            self.dead_out_inds.add(self.n_out_cols - 1)
        for zsiw__rap, rhq__fluy in self.gb_info_in.copy().items():
            xql__dzcj = []
            for cso__nvfu, npx__skmm in rhq__fluy:
                if npx__skmm not in self.dead_out_inds:
                    xql__dzcj.append((cso__nvfu, npx__skmm))
            if not xql__dzcj:
                if zsiw__rap is not None and zsiw__rap not in self.in_key_inds:
                    self.dead_in_inds.add(zsiw__rap)
                self.gb_info_in.pop(zsiw__rap)
            else:
                self.gb_info_in[zsiw__rap] = xql__dzcj
        if self.is_in_table_format:
            if not set(range(self.n_in_table_arrays)) - self.dead_in_inds:
                self.in_vars[0] = None
            for cueis__alw in range(1, len(self.in_vars)):
                qvfwk__siu = self.n_in_table_arrays + cueis__alw - 1
                if qvfwk__siu in self.dead_in_inds:
                    self.in_vars[cueis__alw] = None
        else:
            for cueis__alw in range(len(self.in_vars)):
                if cueis__alw in self.dead_in_inds:
                    self.in_vars[cueis__alw] = None

    def __repr__(self):
        wzmc__zxq = ', '.join(rtc__ucla.name for rtc__ucla in self.
            get_live_in_vars())
        eedla__bkylc = f'{self.df_in}{{{wzmc__zxq}}}'
        dhm__vevf = ', '.join(rtc__ucla.name for rtc__ucla in self.
            get_live_out_vars())
        uuipi__bbjh = f'{self.df_out}{{{dhm__vevf}}}'
        return (
            f'Groupby (keys: {self.key_names} {self.in_key_inds}): {eedla__bkylc} {uuipi__bbjh}'
            )


def aggregate_usedefs(aggregate_node, use_set=None, def_set=None):
    if use_set is None:
        use_set = set()
    if def_set is None:
        def_set = set()
    use_set.update({rtc__ucla.name for rtc__ucla in aggregate_node.
        get_live_in_vars()})
    def_set.update({rtc__ucla.name for rtc__ucla in aggregate_node.
        get_live_out_vars()})
    return numba.core.analysis._use_defs_result(usemap=use_set, defmap=def_set)


numba.core.analysis.ir_extension_usedefs[Aggregate] = aggregate_usedefs


def remove_dead_aggregate(agg_node, lives_no_aliases, lives, arg_aliases,
    alias_map, func_ir, typemap):
    ogin__wnj = agg_node.out_vars[0]
    if ogin__wnj is not None and ogin__wnj.name not in lives:
        agg_node.out_vars[0] = None
        if agg_node.is_output_table:
            ideit__vdv = set(range(agg_node.n_out_table_arrays))
            agg_node.dead_out_inds.update(ideit__vdv)
        else:
            agg_node.dead_out_inds.add(0)
    for cueis__alw in range(1, len(agg_node.out_vars)):
        rtc__ucla = agg_node.out_vars[cueis__alw]
        if rtc__ucla is not None and rtc__ucla.name not in lives:
            agg_node.out_vars[cueis__alw] = None
            qvfwk__siu = agg_node.n_out_table_arrays + cueis__alw - 1
            agg_node.dead_out_inds.add(qvfwk__siu)
    if all(rtc__ucla is None for rtc__ucla in agg_node.out_vars):
        return None
    agg_node.update_dead_col_info()
    return agg_node


ir_utils.remove_dead_extensions[Aggregate] = remove_dead_aggregate


def get_copies_aggregate(aggregate_node, typemap):
    oetz__iey = {rtc__ucla.name for rtc__ucla in aggregate_node.
        get_live_out_vars()}
    return set(), oetz__iey


ir_utils.copy_propagate_extensions[Aggregate] = get_copies_aggregate


def apply_copies_aggregate(aggregate_node, var_dict, name_var_table,
    typemap, calltypes, save_copies):
    for cueis__alw in range(len(aggregate_node.in_vars)):
        if aggregate_node.in_vars[cueis__alw] is not None:
            aggregate_node.in_vars[cueis__alw] = replace_vars_inner(
                aggregate_node.in_vars[cueis__alw], var_dict)
    for cueis__alw in range(len(aggregate_node.out_vars)):
        if aggregate_node.out_vars[cueis__alw] is not None:
            aggregate_node.out_vars[cueis__alw] = replace_vars_inner(
                aggregate_node.out_vars[cueis__alw], var_dict)


ir_utils.apply_copy_propagate_extensions[Aggregate] = apply_copies_aggregate


def visit_vars_aggregate(aggregate_node, callback, cbdata):
    for cueis__alw in range(len(aggregate_node.in_vars)):
        if aggregate_node.in_vars[cueis__alw] is not None:
            aggregate_node.in_vars[cueis__alw] = visit_vars_inner(
                aggregate_node.in_vars[cueis__alw], callback, cbdata)
    for cueis__alw in range(len(aggregate_node.out_vars)):
        if aggregate_node.out_vars[cueis__alw] is not None:
            aggregate_node.out_vars[cueis__alw] = visit_vars_inner(
                aggregate_node.out_vars[cueis__alw], callback, cbdata)


ir_utils.visit_vars_extensions[Aggregate] = visit_vars_aggregate


def aggregate_array_analysis(aggregate_node, equiv_set, typemap, array_analysis
    ):
    cah__hetrh = []
    for hva__zqrrp in aggregate_node.get_live_in_vars():
        afwru__qkylv = equiv_set.get_shape(hva__zqrrp)
        if afwru__qkylv is not None:
            cah__hetrh.append(afwru__qkylv[0])
    if len(cah__hetrh) > 1:
        equiv_set.insert_equiv(*cah__hetrh)
    rtvay__bkwwa = []
    cah__hetrh = []
    for hva__zqrrp in aggregate_node.get_live_out_vars():
        ucvo__wuh = typemap[hva__zqrrp.name]
        zyf__ychx = array_analysis._gen_shape_call(equiv_set, hva__zqrrp,
            ucvo__wuh.ndim, None, rtvay__bkwwa)
        equiv_set.insert_equiv(hva__zqrrp, zyf__ychx)
        cah__hetrh.append(zyf__ychx[0])
        equiv_set.define(hva__zqrrp, set())
    if len(cah__hetrh) > 1:
        equiv_set.insert_equiv(*cah__hetrh)
    return [], rtvay__bkwwa


numba.parfors.array_analysis.array_analysis_extensions[Aggregate
    ] = aggregate_array_analysis


def aggregate_distributed_analysis(aggregate_node, array_dists):
    khhdb__ajv = aggregate_node.get_live_in_vars()
    udda__btjw = aggregate_node.get_live_out_vars()
    fuzzq__cij = Distribution.OneD
    for hva__zqrrp in khhdb__ajv:
        fuzzq__cij = Distribution(min(fuzzq__cij.value, array_dists[
            hva__zqrrp.name].value))
    rcpvo__nhu = Distribution(min(fuzzq__cij.value, Distribution.OneD_Var.
        value))
    for hva__zqrrp in udda__btjw:
        if hva__zqrrp.name in array_dists:
            rcpvo__nhu = Distribution(min(rcpvo__nhu.value, array_dists[
                hva__zqrrp.name].value))
    if rcpvo__nhu != Distribution.OneD_Var:
        fuzzq__cij = rcpvo__nhu
    for hva__zqrrp in khhdb__ajv:
        array_dists[hva__zqrrp.name] = fuzzq__cij
    for hva__zqrrp in udda__btjw:
        array_dists[hva__zqrrp.name] = rcpvo__nhu


distributed_analysis.distributed_analysis_extensions[Aggregate
    ] = aggregate_distributed_analysis


def build_agg_definitions(agg_node, definitions=None):
    if definitions is None:
        definitions = defaultdict(list)
    for hva__zqrrp in agg_node.get_live_out_vars():
        definitions[hva__zqrrp.name].append(agg_node)
    return definitions


ir_utils.build_defs_extensions[Aggregate] = build_agg_definitions


def __update_redvars():
    pass


@infer_global(__update_redvars)
class UpdateDummyTyper(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        return signature(types.void, *args)


def __combine_redvars():
    pass


@infer_global(__combine_redvars)
class CombineDummyTyper(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        return signature(types.void, *args)


def __eval_res():
    pass


@infer_global(__eval_res)
class EvalDummyTyper(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        return signature(args[0].dtype, *args)


def agg_distributed_run(agg_node, array_dists, typemap, calltypes,
    typingctx, targetctx):
    parallel = False
    ikc__ezeo = agg_node.get_live_in_vars()
    yohsh__tko = agg_node.get_live_out_vars()
    if array_dists is not None:
        parallel = True
        for rtc__ucla in (ikc__ezeo + yohsh__tko):
            if array_dists[rtc__ucla.name
                ] != distributed_pass.Distribution.OneD and array_dists[
                rtc__ucla.name] != distributed_pass.Distribution.OneD_Var:
                parallel = False
    out_col_typs = agg_node.out_col_types
    in_col_typs = []
    gcnbi__hlky = []
    func_out_types = []
    for npx__skmm, (zsiw__rap, func) in agg_node.gb_info_out.items():
        if zsiw__rap is not None:
            t = agg_node.in_col_types[zsiw__rap]
            in_col_typs.append(t)
        gcnbi__hlky.append(func)
        func_out_types.append(out_col_typs[npx__skmm])
    kyrb__nxzkk = {'bodo': bodo, 'np': np, 'dt64_dtype': np.dtype(
        'datetime64[ns]'), 'td64_dtype': np.dtype('timedelta64[ns]')}
    for cueis__alw, in_col_typ in enumerate(in_col_typs):
        if isinstance(in_col_typ, bodo.CategoricalArrayType):
            kyrb__nxzkk.update({f'in_cat_dtype_{cueis__alw}': in_col_typ})
    for cueis__alw, uqx__pcnmy in enumerate(out_col_typs):
        if isinstance(uqx__pcnmy, bodo.CategoricalArrayType):
            kyrb__nxzkk.update({f'out_cat_dtype_{cueis__alw}': uqx__pcnmy})
    udf_func_struct = get_udf_func_struct(gcnbi__hlky, in_col_typs,
        typingctx, targetctx)
    out_var_types = [(typemap[rtc__ucla.name] if rtc__ucla is not None else
        types.none) for rtc__ucla in agg_node.out_vars]
    nfka__hvk, wnvd__xbcc = gen_top_level_agg_func(agg_node, in_col_typs,
        out_col_typs, func_out_types, parallel, udf_func_struct,
        out_var_types, typemap)
    kyrb__nxzkk.update(wnvd__xbcc)
    kyrb__nxzkk.update({'pd': pd, 'pre_alloc_string_array':
        pre_alloc_string_array, 'pre_alloc_binary_array':
        pre_alloc_binary_array, 'pre_alloc_array_item_array':
        pre_alloc_array_item_array, 'string_array_type': string_array_type,
        'alloc_decimal_array': alloc_decimal_array, 'array_to_info':
        array_to_info, 'arr_info_list_to_table': arr_info_list_to_table,
        'coerce_to_array': bodo.utils.conversion.coerce_to_array,
        'groupby_and_aggregate': groupby_and_aggregate, 'info_from_table':
        info_from_table, 'info_to_array': info_to_array,
        'delete_info_decref_array': delete_info_decref_array,
        'delete_table': delete_table, 'add_agg_cfunc_sym':
        add_agg_cfunc_sym, 'get_agg_udf_addr': get_agg_udf_addr,
        'delete_table_decref_arrays': delete_table_decref_arrays,
        'decref_table_array': decref_table_array, 'decode_if_dict_array':
        decode_if_dict_array, 'set_table_data': bodo.hiframes.table.
        set_table_data, 'get_table_data': bodo.hiframes.table.
        get_table_data, 'out_typs': out_col_typs})
    if udf_func_struct is not None:
        if udf_func_struct.regular_udfs:
            kyrb__nxzkk.update({'__update_redvars': udf_func_struct.
                update_all_func, '__init_func': udf_func_struct.init_func,
                '__combine_redvars': udf_func_struct.combine_all_func,
                '__eval_res': udf_func_struct.eval_all_func,
                'cpp_cb_update': udf_func_struct.regular_udf_cfuncs[0],
                'cpp_cb_combine': udf_func_struct.regular_udf_cfuncs[1],
                'cpp_cb_eval': udf_func_struct.regular_udf_cfuncs[2]})
        if udf_func_struct.general_udfs:
            kyrb__nxzkk.update({'cpp_cb_general': udf_func_struct.
                general_udf_cfunc})
    jofdc__jsibs = {}
    exec(nfka__hvk, {}, jofdc__jsibs)
    wgkr__jktog = jofdc__jsibs['agg_top']
    yapd__dihpd = compile_to_numba_ir(wgkr__jktog, kyrb__nxzkk, typingctx=
        typingctx, targetctx=targetctx, arg_typs=tuple(typemap[rtc__ucla.
        name] for rtc__ucla in ikc__ezeo), typemap=typemap, calltypes=calltypes
        ).blocks.popitem()[1]
    replace_arg_nodes(yapd__dihpd, ikc__ezeo)
    rez__hisdj = yapd__dihpd.body[-2].value.value
    iijnm__ypnog = yapd__dihpd.body[:-2]
    for cueis__alw, rtc__ucla in enumerate(yohsh__tko):
        gen_getitem(rtc__ucla, rez__hisdj, cueis__alw, calltypes, iijnm__ypnog)
    return iijnm__ypnog


distributed_pass.distributed_run_extensions[Aggregate] = agg_distributed_run


def _gen_dummy_alloc(t, colnum=0, is_input=False):
    if isinstance(t, IntegerArrayType):
        cvpum__lapwc = IntDtype(t.dtype).name
        assert cvpum__lapwc.endswith('Dtype()')
        cvpum__lapwc = cvpum__lapwc[:-7]
        return (
            f"bodo.hiframes.pd_series_ext.get_series_data(pd.Series([1], dtype='{cvpum__lapwc}'))"
            )
    elif isinstance(t, FloatingArrayType):
        return (
            f"bodo.hiframes.pd_series_ext.get_series_data(pd.Series([1.0], dtype='{t.dtype}'))"
            )
    elif isinstance(t, BooleanArrayType):
        return (
            'bodo.libs.bool_arr_ext.init_bool_array(np.empty(0, np.bool_), np.empty(0, np.uint8))'
            )
    elif isinstance(t, StringArrayType):
        return 'pre_alloc_string_array(1, 1)'
    elif t == bodo.dict_str_arr_type:
        return (
            'bodo.libs.dict_arr_ext.init_dict_arr(pre_alloc_string_array(1, 1), bodo.libs.int_arr_ext.alloc_int_array(1, np.int32), False, False)'
            )
    elif isinstance(t, BinaryArrayType):
        return 'pre_alloc_binary_array(1, 1)'
    elif t == ArrayItemArrayType(string_array_type):
        return 'pre_alloc_array_item_array(1, (1, 1), string_array_type)'
    elif isinstance(t, DecimalArrayType):
        return 'alloc_decimal_array(1, {}, {})'.format(t.precision, t.scale)
    elif isinstance(t, DatetimeDateArrayType):
        return (
            'bodo.hiframes.datetime_date_ext.init_datetime_date_array(np.empty(1, np.int64), np.empty(1, np.uint8))'
            )
    elif isinstance(t, bodo.CategoricalArrayType):
        if t.dtype.categories is None:
            raise BodoError(
                'Groupby agg operations on Categorical types require constant categories'
                )
        eyvqu__dcr = 'in' if is_input else 'out'
        return (
            f'bodo.utils.utils.alloc_type(1, {eyvqu__dcr}_cat_dtype_{colnum})')
    else:
        return 'np.empty(1, {})'.format(_get_np_dtype(t.dtype))


def _get_np_dtype(t):
    if t == types.bool_:
        return 'np.bool_'
    if t == types.NPDatetime('ns'):
        return 'dt64_dtype'
    if t == types.NPTimedelta('ns'):
        return 'td64_dtype'
    return 'np.{}'.format(t)


def gen_update_cb(udf_func_struct, allfuncs, n_keys, data_in_typs_,
    do_combine, func_idx_to_in_col, label_suffix):
    golp__ylllq = udf_func_struct.var_typs
    mwcw__lwgq = len(golp__ylllq)
    nfka__hvk = (
        'def bodo_gb_udf_update_local{}(in_table, out_table, row_to_group):\n'
        .format(label_suffix))
    nfka__hvk += '    if is_null_pointer(in_table):\n'
    nfka__hvk += '        return\n'
    nfka__hvk += '    data_redvar_dummy = ({}{})\n'.format(','.join([
        'np.empty(1, {})'.format(_get_np_dtype(t)) for t in golp__ylllq]), 
        ',' if len(golp__ylllq) == 1 else '')
    zmfur__bjyrr = n_keys
    jxgmo__xtnpc = []
    redvar_offsets = []
    jcjxw__zaz = []
    if do_combine:
        for cueis__alw, cso__nvfu in enumerate(allfuncs):
            if cso__nvfu.ftype != 'udf':
                zmfur__bjyrr += cso__nvfu.ncols_pre_shuffle
            else:
                redvar_offsets += list(range(zmfur__bjyrr, zmfur__bjyrr +
                    cso__nvfu.n_redvars))
                zmfur__bjyrr += cso__nvfu.n_redvars
                jcjxw__zaz.append(data_in_typs_[func_idx_to_in_col[cueis__alw]]
                    )
                jxgmo__xtnpc.append(func_idx_to_in_col[cueis__alw] + n_keys)
    else:
        for cueis__alw, cso__nvfu in enumerate(allfuncs):
            if cso__nvfu.ftype != 'udf':
                zmfur__bjyrr += cso__nvfu.ncols_post_shuffle
            else:
                redvar_offsets += list(range(zmfur__bjyrr + 1, zmfur__bjyrr +
                    1 + cso__nvfu.n_redvars))
                zmfur__bjyrr += cso__nvfu.n_redvars + 1
                jcjxw__zaz.append(data_in_typs_[func_idx_to_in_col[cueis__alw]]
                    )
                jxgmo__xtnpc.append(func_idx_to_in_col[cueis__alw] + n_keys)
    assert len(redvar_offsets) == mwcw__lwgq
    jrky__sgyrw = len(jcjxw__zaz)
    edzge__jvcw = []
    for cueis__alw, t in enumerate(jcjxw__zaz):
        edzge__jvcw.append(_gen_dummy_alloc(t, cueis__alw, True))
    nfka__hvk += '    data_in_dummy = ({}{})\n'.format(','.join(edzge__jvcw
        ), ',' if len(jcjxw__zaz) == 1 else '')
    nfka__hvk += """
    # initialize redvar cols
"""
    nfka__hvk += '    init_vals = __init_func()\n'
    for cueis__alw in range(mwcw__lwgq):
        nfka__hvk += (
            """    redvar_arr_{} = info_to_array(info_from_table(out_table, {}), data_redvar_dummy[{}])
"""
            .format(cueis__alw, redvar_offsets[cueis__alw], cueis__alw))
        nfka__hvk += '    incref(redvar_arr_{})\n'.format(cueis__alw)
        nfka__hvk += '    redvar_arr_{}.fill(init_vals[{}])\n'.format(
            cueis__alw, cueis__alw)
    nfka__hvk += '    redvars = ({}{})\n'.format(','.join(['redvar_arr_{}'.
        format(cueis__alw) for cueis__alw in range(mwcw__lwgq)]), ',' if 
        mwcw__lwgq == 1 else '')
    nfka__hvk += '\n'
    for cueis__alw in range(jrky__sgyrw):
        nfka__hvk += (
            """    data_in_{} = info_to_array(info_from_table(in_table, {}), data_in_dummy[{}])
"""
            .format(cueis__alw, jxgmo__xtnpc[cueis__alw], cueis__alw))
        nfka__hvk += '    incref(data_in_{})\n'.format(cueis__alw)
    nfka__hvk += '    data_in = ({}{})\n'.format(','.join(['data_in_{}'.
        format(cueis__alw) for cueis__alw in range(jrky__sgyrw)]), ',' if 
        jrky__sgyrw == 1 else '')
    nfka__hvk += '\n'
    nfka__hvk += '    for i in range(len(data_in_0)):\n'
    nfka__hvk += '        w_ind = row_to_group[i]\n'
    nfka__hvk += '        if w_ind != -1:\n'
    nfka__hvk += '            __update_redvars(redvars, data_in, w_ind, i)\n'
    jofdc__jsibs = {}
    exec(nfka__hvk, {'bodo': bodo, 'np': np, 'pd': pd, 'info_to_array':
        info_to_array, 'info_from_table': info_from_table, 'incref': incref,
        'pre_alloc_string_array': pre_alloc_string_array, '__init_func':
        udf_func_struct.init_func, '__update_redvars': udf_func_struct.
        update_all_func, 'is_null_pointer': is_null_pointer, 'dt64_dtype':
        np.dtype('datetime64[ns]'), 'td64_dtype': np.dtype(
        'timedelta64[ns]')}, jofdc__jsibs)
    return jofdc__jsibs['bodo_gb_udf_update_local{}'.format(label_suffix)]


def gen_combine_cb(udf_func_struct, allfuncs, n_keys, label_suffix):
    golp__ylllq = udf_func_struct.var_typs
    mwcw__lwgq = len(golp__ylllq)
    nfka__hvk = (
        'def bodo_gb_udf_combine{}(in_table, out_table, row_to_group):\n'.
        format(label_suffix))
    nfka__hvk += '    if is_null_pointer(in_table):\n'
    nfka__hvk += '        return\n'
    nfka__hvk += '    data_redvar_dummy = ({}{})\n'.format(','.join([
        'np.empty(1, {})'.format(_get_np_dtype(t)) for t in golp__ylllq]), 
        ',' if len(golp__ylllq) == 1 else '')
    buvkj__jmh = n_keys
    kvsr__pkkd = n_keys
    oskmw__wuk = []
    dsg__xrzrj = []
    for cso__nvfu in allfuncs:
        if cso__nvfu.ftype != 'udf':
            buvkj__jmh += cso__nvfu.ncols_pre_shuffle
            kvsr__pkkd += cso__nvfu.ncols_post_shuffle
        else:
            oskmw__wuk += list(range(buvkj__jmh, buvkj__jmh + cso__nvfu.
                n_redvars))
            dsg__xrzrj += list(range(kvsr__pkkd + 1, kvsr__pkkd + 1 +
                cso__nvfu.n_redvars))
            buvkj__jmh += cso__nvfu.n_redvars
            kvsr__pkkd += 1 + cso__nvfu.n_redvars
    assert len(oskmw__wuk) == mwcw__lwgq
    nfka__hvk += """
    # initialize redvar cols
"""
    nfka__hvk += '    init_vals = __init_func()\n'
    for cueis__alw in range(mwcw__lwgq):
        nfka__hvk += (
            """    redvar_arr_{} = info_to_array(info_from_table(out_table, {}), data_redvar_dummy[{}])
"""
            .format(cueis__alw, dsg__xrzrj[cueis__alw], cueis__alw))
        nfka__hvk += '    incref(redvar_arr_{})\n'.format(cueis__alw)
        nfka__hvk += '    redvar_arr_{}.fill(init_vals[{}])\n'.format(
            cueis__alw, cueis__alw)
    nfka__hvk += '    redvars = ({}{})\n'.format(','.join(['redvar_arr_{}'.
        format(cueis__alw) for cueis__alw in range(mwcw__lwgq)]), ',' if 
        mwcw__lwgq == 1 else '')
    nfka__hvk += '\n'
    for cueis__alw in range(mwcw__lwgq):
        nfka__hvk += (
            """    recv_redvar_arr_{} = info_to_array(info_from_table(in_table, {}), data_redvar_dummy[{}])
"""
            .format(cueis__alw, oskmw__wuk[cueis__alw], cueis__alw))
        nfka__hvk += '    incref(recv_redvar_arr_{})\n'.format(cueis__alw)
    nfka__hvk += '    recv_redvars = ({}{})\n'.format(','.join([
        'recv_redvar_arr_{}'.format(cueis__alw) for cueis__alw in range(
        mwcw__lwgq)]), ',' if mwcw__lwgq == 1 else '')
    nfka__hvk += '\n'
    if mwcw__lwgq:
        nfka__hvk += '    for i in range(len(recv_redvar_arr_0)):\n'
        nfka__hvk += '        w_ind = row_to_group[i]\n'
        nfka__hvk += (
            '        __combine_redvars(redvars, recv_redvars, w_ind, i)\n')
    jofdc__jsibs = {}
    exec(nfka__hvk, {'np': np, 'info_to_array': info_to_array,
        'info_from_table': info_from_table, 'incref': incref, '__init_func':
        udf_func_struct.init_func, '__combine_redvars': udf_func_struct.
        combine_all_func, 'is_null_pointer': is_null_pointer, 'dt64_dtype':
        np.dtype('datetime64[ns]'), 'td64_dtype': np.dtype(
        'timedelta64[ns]')}, jofdc__jsibs)
    return jofdc__jsibs['bodo_gb_udf_combine{}'.format(label_suffix)]


def gen_eval_cb(udf_func_struct, allfuncs, n_keys, out_data_typs_, label_suffix
    ):
    golp__ylllq = udf_func_struct.var_typs
    mwcw__lwgq = len(golp__ylllq)
    zmfur__bjyrr = n_keys
    redvar_offsets = []
    ntdga__keocr = []
    xlaw__vht = []
    for cueis__alw, cso__nvfu in enumerate(allfuncs):
        if cso__nvfu.ftype != 'udf':
            zmfur__bjyrr += cso__nvfu.ncols_post_shuffle
        else:
            ntdga__keocr.append(zmfur__bjyrr)
            redvar_offsets += list(range(zmfur__bjyrr + 1, zmfur__bjyrr + 1 +
                cso__nvfu.n_redvars))
            zmfur__bjyrr += 1 + cso__nvfu.n_redvars
            xlaw__vht.append(out_data_typs_[cueis__alw])
    assert len(redvar_offsets) == mwcw__lwgq
    jrky__sgyrw = len(xlaw__vht)
    nfka__hvk = 'def bodo_gb_udf_eval{}(table):\n'.format(label_suffix)
    nfka__hvk += '    if is_null_pointer(table):\n'
    nfka__hvk += '        return\n'
    nfka__hvk += '    data_redvar_dummy = ({}{})\n'.format(','.join([
        'np.empty(1, {})'.format(_get_np_dtype(t)) for t in golp__ylllq]), 
        ',' if len(golp__ylllq) == 1 else '')
    nfka__hvk += '    out_data_dummy = ({}{})\n'.format(','.join([
        'np.empty(1, {})'.format(_get_np_dtype(t.dtype)) for t in xlaw__vht
        ]), ',' if len(xlaw__vht) == 1 else '')
    for cueis__alw in range(mwcw__lwgq):
        nfka__hvk += (
            """    redvar_arr_{} = info_to_array(info_from_table(table, {}), data_redvar_dummy[{}])
"""
            .format(cueis__alw, redvar_offsets[cueis__alw], cueis__alw))
        nfka__hvk += '    incref(redvar_arr_{})\n'.format(cueis__alw)
    nfka__hvk += '    redvars = ({}{})\n'.format(','.join(['redvar_arr_{}'.
        format(cueis__alw) for cueis__alw in range(mwcw__lwgq)]), ',' if 
        mwcw__lwgq == 1 else '')
    nfka__hvk += '\n'
    for cueis__alw in range(jrky__sgyrw):
        nfka__hvk += (
            """    data_out_{} = info_to_array(info_from_table(table, {}), out_data_dummy[{}])
"""
            .format(cueis__alw, ntdga__keocr[cueis__alw], cueis__alw))
        nfka__hvk += '    incref(data_out_{})\n'.format(cueis__alw)
    nfka__hvk += '    data_out = ({}{})\n'.format(','.join(['data_out_{}'.
        format(cueis__alw) for cueis__alw in range(jrky__sgyrw)]), ',' if 
        jrky__sgyrw == 1 else '')
    nfka__hvk += '\n'
    nfka__hvk += '    for i in range(len(data_out_0)):\n'
    nfka__hvk += '        __eval_res(redvars, data_out, i)\n'
    jofdc__jsibs = {}
    exec(nfka__hvk, {'np': np, 'info_to_array': info_to_array,
        'info_from_table': info_from_table, 'incref': incref, '__eval_res':
        udf_func_struct.eval_all_func, 'is_null_pointer': is_null_pointer,
        'dt64_dtype': np.dtype('datetime64[ns]'), 'td64_dtype': np.dtype(
        'timedelta64[ns]')}, jofdc__jsibs)
    return jofdc__jsibs['bodo_gb_udf_eval{}'.format(label_suffix)]


def gen_general_udf_cb(udf_func_struct, allfuncs, n_keys, in_col_typs,
    out_col_typs, func_idx_to_in_col, label_suffix):
    zmfur__bjyrr = n_keys
    cmhhl__jpn = []
    for cueis__alw, cso__nvfu in enumerate(allfuncs):
        if cso__nvfu.ftype == 'gen_udf':
            cmhhl__jpn.append(zmfur__bjyrr)
            zmfur__bjyrr += 1
        elif cso__nvfu.ftype != 'udf':
            zmfur__bjyrr += cso__nvfu.ncols_post_shuffle
        else:
            zmfur__bjyrr += cso__nvfu.n_redvars + 1
    nfka__hvk = (
        'def bodo_gb_apply_general_udfs{}(num_groups, in_table, out_table):\n'
        .format(label_suffix))
    nfka__hvk += '    if num_groups == 0:\n'
    nfka__hvk += '        return\n'
    for cueis__alw, func in enumerate(udf_func_struct.general_udf_funcs):
        nfka__hvk += '    # col {}\n'.format(cueis__alw)
        nfka__hvk += (
            """    out_col = info_to_array(info_from_table(out_table, {}), out_col_{}_typ)
"""
            .format(cmhhl__jpn[cueis__alw], cueis__alw))
        nfka__hvk += '    incref(out_col)\n'
        nfka__hvk += '    for j in range(num_groups):\n'
        nfka__hvk += (
            """        in_col = info_to_array(info_from_table(in_table, {}*num_groups + j), in_col_{}_typ)
"""
            .format(cueis__alw, cueis__alw))
        nfka__hvk += '        incref(in_col)\n'
        nfka__hvk += (
            '        out_col[j] = func_{}(pd.Series(in_col))  # func returns scalar\n'
            .format(cueis__alw))
    kyrb__nxzkk = {'pd': pd, 'info_to_array': info_to_array,
        'info_from_table': info_from_table, 'incref': incref}
    osix__xbe = 0
    for cueis__alw, func in enumerate(allfuncs):
        if func.ftype != 'gen_udf':
            continue
        func = udf_func_struct.general_udf_funcs[osix__xbe]
        kyrb__nxzkk['func_{}'.format(osix__xbe)] = func
        kyrb__nxzkk['in_col_{}_typ'.format(osix__xbe)] = in_col_typs[
            func_idx_to_in_col[cueis__alw]]
        kyrb__nxzkk['out_col_{}_typ'.format(osix__xbe)] = out_col_typs[
            cueis__alw]
        osix__xbe += 1
    jofdc__jsibs = {}
    exec(nfka__hvk, kyrb__nxzkk, jofdc__jsibs)
    cso__nvfu = jofdc__jsibs['bodo_gb_apply_general_udfs{}'.format(
        label_suffix)]
    luta__kehfe = types.void(types.int64, types.voidptr, types.voidptr)
    return numba.cfunc(luta__kehfe, nopython=True)(cso__nvfu)


def gen_top_level_agg_func(agg_node, in_col_typs, out_col_typs,
    func_out_types, parallel, udf_func_struct, out_var_types, typemap):
    n_keys = len(agg_node.in_key_inds)
    vfs__uvkz = len(agg_node.out_vars)
    if agg_node.same_index:
        assert agg_node.input_has_index, 'agg codegen: input_has_index=True required for same_index=True'
    if agg_node.is_in_table_format:
        qncaj__znhg = []
        if agg_node.in_vars[0] is not None:
            qncaj__znhg.append('arg0')
        for cueis__alw in range(agg_node.n_in_table_arrays, agg_node.n_in_cols
            ):
            if cueis__alw not in agg_node.dead_in_inds:
                qncaj__znhg.append(f'arg{cueis__alw}')
    else:
        qncaj__znhg = [f'arg{cueis__alw}' for cueis__alw, rtc__ucla in
            enumerate(agg_node.in_vars) if rtc__ucla is not None]
    nfka__hvk = f"def agg_top({', '.join(qncaj__znhg)}):\n"
    rlv__hictl = []
    if agg_node.is_in_table_format:
        rlv__hictl = agg_node.in_key_inds + [zsiw__rap for zsiw__rap,
            txy__faa in agg_node.gb_info_out.values() if zsiw__rap is not None]
        if agg_node.input_has_index:
            rlv__hictl.append(agg_node.n_in_cols - 1)
        avfso__zikrg = ',' if len(agg_node.in_vars) - 1 == 1 else ''
        fjv__iujj = []
        for cueis__alw in range(agg_node.n_in_table_arrays, agg_node.n_in_cols
            ):
            if cueis__alw in agg_node.dead_in_inds:
                fjv__iujj.append('None')
            else:
                fjv__iujj.append(f'arg{cueis__alw}')
        vvnk__jap = 'arg0' if agg_node.in_vars[0] is not None else 'None'
        nfka__hvk += f"""    table = py_data_to_cpp_table({vvnk__jap}, ({', '.join(fjv__iujj)}{avfso__zikrg}), in_col_inds, {agg_node.n_in_table_arrays})
"""
    else:
        uxe__mxic = [f'arg{cueis__alw}' for cueis__alw in agg_node.in_key_inds]
        fsxq__vynna = [f'arg{zsiw__rap}' for zsiw__rap, txy__faa in
            agg_node.gb_info_out.values() if zsiw__rap is not None]
        hfj__vdtas = uxe__mxic + fsxq__vynna
        if agg_node.input_has_index:
            hfj__vdtas.append(f'arg{len(agg_node.in_vars) - 1}')
        nfka__hvk += '    info_list = [{}]\n'.format(', '.join(
            f'array_to_info({iqq__pzhmp})' for iqq__pzhmp in hfj__vdtas))
        nfka__hvk += '    table = arr_info_list_to_table(info_list)\n'
    do_combine = parallel
    allfuncs = []
    uqb__eem = []
    func_idx_to_in_col = []
    yxas__fif = []
    hzcyn__zpgw = False
    obeu__jggj = 1
    byliw__bjo = -1
    neor__osn = 0
    nethc__fiqcd = 0
    gcnbi__hlky = [func for txy__faa, func in agg_node.gb_info_out.values()]
    for gzd__eps, func in enumerate(gcnbi__hlky):
        uqb__eem.append(len(allfuncs))
        if func.ftype in {'median', 'nunique', 'ngroup'}:
            do_combine = False
        if func.ftype in list_cumulative:
            neor__osn += 1
        if hasattr(func, 'skipdropna'):
            hzcyn__zpgw = func.skipdropna
        if func.ftype == 'shift':
            obeu__jggj = func.periods
            do_combine = False
        if func.ftype in {'transform'}:
            nethc__fiqcd = func.transform_func
            do_combine = False
        if func.ftype == 'head':
            byliw__bjo = func.head_n
            do_combine = False
        allfuncs.append(func)
        func_idx_to_in_col.append(gzd__eps)
        if func.ftype == 'udf':
            yxas__fif.append(func.n_redvars)
        elif func.ftype == 'gen_udf':
            yxas__fif.append(0)
            do_combine = False
    uqb__eem.append(len(allfuncs))
    assert len(agg_node.gb_info_out) == len(allfuncs
        ), 'invalid number of groupby outputs'
    if neor__osn > 0:
        if neor__osn != len(allfuncs):
            raise BodoError(
                f'{agg_node.func_name}(): Cannot mix cumulative operations with other aggregation functions'
                , loc=agg_node.loc)
        do_combine = False
    sgkb__pzi = []
    if udf_func_struct is not None:
        xyzy__hhddl = next_label()
        if udf_func_struct.regular_udfs:
            luta__kehfe = types.void(types.voidptr, types.voidptr, types.
                CPointer(types.int64))
            ydst__vxrd = numba.cfunc(luta__kehfe, nopython=True)(gen_update_cb
                (udf_func_struct, allfuncs, n_keys, in_col_typs, do_combine,
                func_idx_to_in_col, xyzy__hhddl))
            lhnm__qcv = numba.cfunc(luta__kehfe, nopython=True)(gen_combine_cb
                (udf_func_struct, allfuncs, n_keys, xyzy__hhddl))
            mmu__ixik = numba.cfunc('void(voidptr)', nopython=True)(gen_eval_cb
                (udf_func_struct, allfuncs, n_keys, func_out_types,
                xyzy__hhddl))
            udf_func_struct.set_regular_cfuncs(ydst__vxrd, lhnm__qcv, mmu__ixik
                )
            for okh__axno in udf_func_struct.regular_udf_cfuncs:
                gb_agg_cfunc[okh__axno.native_name] = okh__axno
                gb_agg_cfunc_addr[okh__axno.native_name] = okh__axno.address
        if udf_func_struct.general_udfs:
            bldoq__fgm = gen_general_udf_cb(udf_func_struct, allfuncs,
                n_keys, in_col_typs, func_out_types, func_idx_to_in_col,
                xyzy__hhddl)
            udf_func_struct.set_general_cfunc(bldoq__fgm)
        golp__ylllq = (udf_func_struct.var_typs if udf_func_struct.
            regular_udfs else None)
        uguz__wddh = 0
        cueis__alw = 0
        for erza__jwwl, cso__nvfu in zip(agg_node.gb_info_out.keys(), allfuncs
            ):
            if cso__nvfu.ftype in ('udf', 'gen_udf'):
                sgkb__pzi.append(out_col_typs[erza__jwwl])
                for mwodi__tvam in range(uguz__wddh, uguz__wddh + yxas__fif
                    [cueis__alw]):
                    sgkb__pzi.append(dtype_to_array_type(golp__ylllq[
                        mwodi__tvam]))
                uguz__wddh += yxas__fif[cueis__alw]
                cueis__alw += 1
        nfka__hvk += f"""    dummy_table = create_dummy_table(({', '.join(f'udf_type{cueis__alw}' for cueis__alw in range(len(sgkb__pzi)))}{',' if len(sgkb__pzi) == 1 else ''}))
"""
        nfka__hvk += f"""    udf_table_dummy = py_data_to_cpp_table(dummy_table, (), udf_dummy_col_inds, {len(sgkb__pzi)})
"""
        if udf_func_struct.regular_udfs:
            nfka__hvk += (
                f"    add_agg_cfunc_sym(cpp_cb_update, '{ydst__vxrd.native_name}')\n"
                )
            nfka__hvk += (
                f"    add_agg_cfunc_sym(cpp_cb_combine, '{lhnm__qcv.native_name}')\n"
                )
            nfka__hvk += (
                f"    add_agg_cfunc_sym(cpp_cb_eval, '{mmu__ixik.native_name}')\n"
                )
            nfka__hvk += (
                f"    cpp_cb_update_addr = get_agg_udf_addr('{ydst__vxrd.native_name}')\n"
                )
            nfka__hvk += (
                f"    cpp_cb_combine_addr = get_agg_udf_addr('{lhnm__qcv.native_name}')\n"
                )
            nfka__hvk += (
                f"    cpp_cb_eval_addr = get_agg_udf_addr('{mmu__ixik.native_name}')\n"
                )
        else:
            nfka__hvk += '    cpp_cb_update_addr = 0\n'
            nfka__hvk += '    cpp_cb_combine_addr = 0\n'
            nfka__hvk += '    cpp_cb_eval_addr = 0\n'
        if udf_func_struct.general_udfs:
            okh__axno = udf_func_struct.general_udf_cfunc
            gb_agg_cfunc[okh__axno.native_name] = okh__axno
            gb_agg_cfunc_addr[okh__axno.native_name] = okh__axno.address
            nfka__hvk += (
                f"    add_agg_cfunc_sym(cpp_cb_general, '{okh__axno.native_name}')\n"
                )
            nfka__hvk += (
                f"    cpp_cb_general_addr = get_agg_udf_addr('{okh__axno.native_name}')\n"
                )
        else:
            nfka__hvk += '    cpp_cb_general_addr = 0\n'
    else:
        nfka__hvk += (
            '    udf_table_dummy = arr_info_list_to_table([array_to_info(np.empty(1))])\n'
            )
        nfka__hvk += '    cpp_cb_update_addr = 0\n'
        nfka__hvk += '    cpp_cb_combine_addr = 0\n'
        nfka__hvk += '    cpp_cb_eval_addr = 0\n'
        nfka__hvk += '    cpp_cb_general_addr = 0\n'
    nfka__hvk += '    ftypes = np.array([{}, 0], dtype=np.int32)\n'.format(', '
        .join([str(supported_agg_funcs.index(cso__nvfu.ftype)) for
        cso__nvfu in allfuncs] + ['0']))
    nfka__hvk += (
        f'    func_offsets = np.array({str(uqb__eem)}, dtype=np.int32)\n')
    if len(yxas__fif) > 0:
        nfka__hvk += (
            f'    udf_ncols = np.array({str(yxas__fif)}, dtype=np.int32)\n')
    else:
        nfka__hvk += '    udf_ncols = np.array([0], np.int32)\n'
    nfka__hvk += '    total_rows_np = np.array([0], dtype=np.int64)\n'
    lwt__sxk = (agg_node._num_shuffle_keys if agg_node._num_shuffle_keys !=
        -1 else n_keys)
    nfka__hvk += f"""    out_table = groupby_and_aggregate(table, {n_keys}, {agg_node.input_has_index}, ftypes.ctypes, func_offsets.ctypes, udf_ncols.ctypes, {parallel}, {hzcyn__zpgw}, {obeu__jggj}, {nethc__fiqcd}, {byliw__bjo}, {agg_node.return_key}, {agg_node.same_index}, {agg_node.dropna}, cpp_cb_update_addr, cpp_cb_combine_addr, cpp_cb_eval_addr, cpp_cb_general_addr, udf_table_dummy, total_rows_np.ctypes, {lwt__sxk})
"""
    xfk__szbm = []
    gqywz__tua = 0
    if agg_node.return_key:
        xpjys__ipe = 0 if isinstance(agg_node.out_type.index, bodo.
            RangeIndexType) else agg_node.n_out_cols - len(agg_node.in_key_inds
            ) - 1
        for cueis__alw in range(n_keys):
            qvfwk__siu = xpjys__ipe + cueis__alw
            xfk__szbm.append(qvfwk__siu if qvfwk__siu not in agg_node.
                dead_out_inds else -1)
            gqywz__tua += 1
    for erza__jwwl in agg_node.gb_info_out.keys():
        xfk__szbm.append(erza__jwwl)
        gqywz__tua += 1
    qsn__wpzj = False
    if agg_node.same_index:
        if agg_node.out_vars[-1] is not None:
            xfk__szbm.append(agg_node.n_out_cols - 1)
        else:
            qsn__wpzj = True
    avfso__zikrg = ',' if vfs__uvkz == 1 else ''
    hirse__lkock = (
        f"({', '.join(f'out_type{cueis__alw}' for cueis__alw in range(vfs__uvkz))}{avfso__zikrg})"
        )
    bgs__qncj = []
    sjdqv__yba = []
    for cueis__alw, t in enumerate(out_col_typs):
        if cueis__alw not in agg_node.dead_out_inds and type_has_unknown_cats(t
            ):
            if cueis__alw in agg_node.gb_info_out:
                zsiw__rap = agg_node.gb_info_out[cueis__alw][0]
            else:
                assert agg_node.return_key, 'Internal error: groupby key output with unknown categoricals detected, but return_key is False'
                etzs__zlhj = cueis__alw - xpjys__ipe
                zsiw__rap = agg_node.in_key_inds[etzs__zlhj]
            sjdqv__yba.append(cueis__alw)
            if (agg_node.is_in_table_format and zsiw__rap < agg_node.
                n_in_table_arrays):
                bgs__qncj.append(f'get_table_data(arg0, {zsiw__rap})')
            else:
                bgs__qncj.append(f'arg{zsiw__rap}')
    avfso__zikrg = ',' if len(bgs__qncj) == 1 else ''
    nfka__hvk += f"""    out_data = cpp_table_to_py_data(out_table, out_col_inds, {hirse__lkock}, total_rows_np[0], {agg_node.n_out_table_arrays}, ({', '.join(bgs__qncj)}{avfso__zikrg}), unknown_cat_out_inds)
"""
    nfka__hvk += (
        f"    ev_clean = bodo.utils.tracing.Event('tables_clean_up', {parallel})\n"
        )
    nfka__hvk += '    delete_table_decref_arrays(table)\n'
    nfka__hvk += '    delete_table_decref_arrays(udf_table_dummy)\n'
    if agg_node.return_key:
        for cueis__alw in range(n_keys):
            if xfk__szbm[cueis__alw] == -1:
                nfka__hvk += (
                    f'    decref_table_array(out_table, {cueis__alw})\n')
    if qsn__wpzj:
        wryb__ipgvl = len(agg_node.gb_info_out) + (n_keys if agg_node.
            return_key else 0)
        nfka__hvk += f'    decref_table_array(out_table, {wryb__ipgvl})\n'
    nfka__hvk += '    delete_table(out_table)\n'
    nfka__hvk += '    ev_clean.finalize()\n'
    nfka__hvk += '    return out_data\n'
    onsr__rati = {f'out_type{cueis__alw}': out_var_types[cueis__alw] for
        cueis__alw in range(vfs__uvkz)}
    onsr__rati['out_col_inds'] = MetaType(tuple(xfk__szbm))
    onsr__rati['in_col_inds'] = MetaType(tuple(rlv__hictl))
    onsr__rati['cpp_table_to_py_data'] = cpp_table_to_py_data
    onsr__rati['py_data_to_cpp_table'] = py_data_to_cpp_table
    onsr__rati.update({f'udf_type{cueis__alw}': t for cueis__alw, t in
        enumerate(sgkb__pzi)})
    onsr__rati['udf_dummy_col_inds'] = MetaType(tuple(range(len(sgkb__pzi))))
    onsr__rati['create_dummy_table'] = create_dummy_table
    onsr__rati['unknown_cat_out_inds'] = MetaType(tuple(sjdqv__yba))
    onsr__rati['get_table_data'] = bodo.hiframes.table.get_table_data
    return nfka__hvk, onsr__rati


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def create_dummy_table(data_types):
    oxq__sofm = tuple(unwrap_typeref(data_types.types[cueis__alw]) for
        cueis__alw in range(len(data_types.types)))
    ciw__ebhx = bodo.TableType(oxq__sofm)
    onsr__rati = {'table_type': ciw__ebhx}
    nfka__hvk = 'def impl(data_types):\n'
    nfka__hvk += '  py_table = init_table(table_type, False)\n'
    nfka__hvk += '  py_table = set_table_len(py_table, 1)\n'
    for ucvo__wuh, jrgb__gyx in ciw__ebhx.type_to_blk.items():
        onsr__rati[f'typ_list_{jrgb__gyx}'] = types.List(ucvo__wuh)
        onsr__rati[f'typ_{jrgb__gyx}'] = ucvo__wuh
        ayob__bzwhg = len(ciw__ebhx.block_to_arr_ind[jrgb__gyx])
        nfka__hvk += f"""  arr_list_{jrgb__gyx} = alloc_list_like(typ_list_{jrgb__gyx}, {ayob__bzwhg}, False)
"""
        nfka__hvk += f'  for i in range(len(arr_list_{jrgb__gyx})):\n'
        nfka__hvk += (
            f'    arr_list_{jrgb__gyx}[i] = alloc_type(1, typ_{jrgb__gyx}, (-1,))\n'
            )
        nfka__hvk += (
            f'  py_table = set_table_block(py_table, arr_list_{jrgb__gyx}, {jrgb__gyx})\n'
            )
    nfka__hvk += '  return py_table\n'
    onsr__rati.update({'init_table': bodo.hiframes.table.init_table,
        'alloc_list_like': bodo.hiframes.table.alloc_list_like,
        'set_table_block': bodo.hiframes.table.set_table_block,
        'set_table_len': bodo.hiframes.table.set_table_len, 'alloc_type':
        bodo.utils.utils.alloc_type})
    jofdc__jsibs = {}
    exec(nfka__hvk, onsr__rati, jofdc__jsibs)
    return jofdc__jsibs['impl']


def agg_table_column_use(agg_node, block_use_map, equiv_vars, typemap,
    table_col_use_map):
    if not agg_node.is_in_table_format or agg_node.in_vars[0] is None:
        return
    hgndh__uijqb = agg_node.in_vars[0].name
    ngs__berg, zih__dkvxk, nbv__lueys = block_use_map[hgndh__uijqb]
    if zih__dkvxk or nbv__lueys:
        return
    if agg_node.is_output_table and agg_node.out_vars[0] is not None:
        mpgx__gff, criqx__mrk, rsh__tjau = _compute_table_column_uses(agg_node
            .out_vars[0].name, table_col_use_map, equiv_vars)
        if criqx__mrk or rsh__tjau:
            mpgx__gff = set(range(agg_node.n_out_table_arrays))
    else:
        mpgx__gff = {}
        if agg_node.out_vars[0
            ] is not None and 0 not in agg_node.dead_out_inds:
            mpgx__gff = {0}
    nbya__ezce = set(cueis__alw for cueis__alw in agg_node.in_key_inds if 
        cueis__alw < agg_node.n_in_table_arrays)
    mpv__tffmr = set(agg_node.gb_info_out[cueis__alw][0] for cueis__alw in
        mpgx__gff if cueis__alw in agg_node.gb_info_out and agg_node.
        gb_info_out[cueis__alw][0] is not None)
    mpv__tffmr |= nbya__ezce | ngs__berg
    ryamy__lte = len(set(range(agg_node.n_in_table_arrays)) - mpv__tffmr) == 0
    block_use_map[hgndh__uijqb] = mpv__tffmr, ryamy__lte, False


ir_extension_table_column_use[Aggregate] = agg_table_column_use


def agg_remove_dead_column(agg_node, column_live_map, equiv_vars, typemap):
    if not agg_node.is_output_table or agg_node.out_vars[0] is None:
        return False
    leuw__qqyhz = agg_node.n_out_table_arrays
    qhw__mkd = agg_node.out_vars[0].name
    frfj__slf = _find_used_columns(qhw__mkd, leuw__qqyhz, column_live_map,
        equiv_vars)
    if frfj__slf is None:
        return False
    cov__dbnf = set(range(leuw__qqyhz)) - frfj__slf
    bnciv__rolux = len(cov__dbnf - agg_node.dead_out_inds) != 0
    if bnciv__rolux:
        agg_node.dead_out_inds.update(cov__dbnf)
        agg_node.update_dead_col_info()
    return bnciv__rolux


remove_dead_column_extensions[Aggregate] = agg_remove_dead_column


def compile_to_optimized_ir(func, arg_typs, typingctx, targetctx):
    code = func.code if hasattr(func, 'code') else func.__code__
    closure = func.closure if hasattr(func, 'closure') else func.__closure__
    f_ir = get_ir_of_code(func.__globals__, code)
    replace_closures(f_ir, closure, code)
    for block in f_ir.blocks.values():
        for ackrz__ckmq in block.body:
            if is_call_assign(ackrz__ckmq) and find_callname(f_ir,
                ackrz__ckmq.value) == ('len', 'builtins'
                ) and ackrz__ckmq.value.args[0].name == f_ir.arg_names[0]:
                smq__kpl = get_definition(f_ir, ackrz__ckmq.value.func)
                smq__kpl.name = 'dummy_agg_count'
                smq__kpl.value = dummy_agg_count
    jbeas__cmnf = get_name_var_table(f_ir.blocks)
    wlkkl__ybitq = {}
    for name, txy__faa in jbeas__cmnf.items():
        wlkkl__ybitq[name] = mk_unique_var(name)
    replace_var_names(f_ir.blocks, wlkkl__ybitq)
    f_ir._definitions = build_definitions(f_ir.blocks)
    assert f_ir.arg_count == 1, 'agg function should have one input'
    fny__uwry = numba.core.compiler.Flags()
    fny__uwry.nrt = True
    thejl__bus = bodo.transforms.untyped_pass.UntypedPass(f_ir, typingctx,
        arg_typs, {}, {}, fny__uwry)
    thejl__bus.run()
    f_ir._definitions = build_definitions(f_ir.blocks)
    typemap, yzpu__hpyz, calltypes, txy__faa = (numba.core.typed_passes.
        type_inference_stage(typingctx, targetctx, f_ir, arg_typs, None))
    bltvd__cczt = numba.core.cpu.ParallelOptions(True)
    targetctx = numba.core.cpu.CPUContext(typingctx)
    xwqh__epjt = namedtuple('DummyPipeline', ['typingctx', 'targetctx',
        'args', 'func_ir', 'typemap', 'return_type', 'calltypes',
        'type_annotation', 'locals', 'flags', 'pipeline'])
    yduzk__ucffr = namedtuple('TypeAnnotation', ['typemap', 'calltypes'])
    mcng__ujn = yduzk__ucffr(typemap, calltypes)
    pm = xwqh__epjt(typingctx, targetctx, None, f_ir, typemap, yzpu__hpyz,
        calltypes, mcng__ujn, {}, fny__uwry, None)
    qbh__tamtt = (numba.core.compiler.DefaultPassBuilder.
        define_untyped_pipeline(pm))
    pm = xwqh__epjt(typingctx, targetctx, None, f_ir, typemap, yzpu__hpyz,
        calltypes, mcng__ujn, {}, fny__uwry, qbh__tamtt)
    dtc__ggej = numba.core.typed_passes.InlineOverloads()
    dtc__ggej.run_pass(pm)
    himyo__odcm = bodo.transforms.series_pass.SeriesPass(f_ir, typingctx,
        targetctx, typemap, calltypes, {}, False)
    himyo__odcm.run()
    for block in f_ir.blocks.values():
        for ackrz__ckmq in block.body:
            if is_assign(ackrz__ckmq) and isinstance(ackrz__ckmq.value, (ir
                .Arg, ir.Var)) and isinstance(typemap[ackrz__ckmq.target.
                name], SeriesType):
                ucvo__wuh = typemap.pop(ackrz__ckmq.target.name)
                typemap[ackrz__ckmq.target.name] = ucvo__wuh.data
            if is_call_assign(ackrz__ckmq) and find_callname(f_ir,
                ackrz__ckmq.value) == ('get_series_data',
                'bodo.hiframes.pd_series_ext'):
                f_ir._definitions[ackrz__ckmq.target.name].remove(ackrz__ckmq
                    .value)
                ackrz__ckmq.value = ackrz__ckmq.value.args[0]
                f_ir._definitions[ackrz__ckmq.target.name].append(ackrz__ckmq
                    .value)
            if is_call_assign(ackrz__ckmq) and find_callname(f_ir,
                ackrz__ckmq.value) == ('isna', 'bodo.libs.array_kernels'):
                f_ir._definitions[ackrz__ckmq.target.name].remove(ackrz__ckmq
                    .value)
                ackrz__ckmq.value = ir.Const(False, ackrz__ckmq.loc)
                f_ir._definitions[ackrz__ckmq.target.name].append(ackrz__ckmq
                    .value)
            if is_call_assign(ackrz__ckmq) and find_callname(f_ir,
                ackrz__ckmq.value) == ('setna', 'bodo.libs.array_kernels'):
                f_ir._definitions[ackrz__ckmq.target.name].remove(ackrz__ckmq
                    .value)
                ackrz__ckmq.value = ir.Const(False, ackrz__ckmq.loc)
                f_ir._definitions[ackrz__ckmq.target.name].append(ackrz__ckmq
                    .value)
    bodo.transforms.untyped_pass.remove_dead_branches(f_ir)
    zhc__opma = numba.parfors.parfor.PreParforPass(f_ir, typemap, calltypes,
        typingctx, targetctx, bltvd__cczt)
    zhc__opma.run()
    f_ir._definitions = build_definitions(f_ir.blocks)
    iuk__zgs = numba.core.compiler.StateDict()
    iuk__zgs.func_ir = f_ir
    iuk__zgs.typemap = typemap
    iuk__zgs.calltypes = calltypes
    iuk__zgs.typingctx = typingctx
    iuk__zgs.targetctx = targetctx
    iuk__zgs.return_type = yzpu__hpyz
    numba.core.rewrites.rewrite_registry.apply('after-inference', iuk__zgs)
    diyh__mxrhm = numba.parfors.parfor.ParforPass(f_ir, typemap, calltypes,
        yzpu__hpyz, typingctx, targetctx, bltvd__cczt, fny__uwry, {})
    diyh__mxrhm.run()
    remove_dels(f_ir.blocks)
    numba.parfors.parfor.maximize_fusion(f_ir, f_ir.blocks, typemap, False)
    return f_ir, pm


def replace_closures(f_ir, closure, code):
    if closure:
        closure = f_ir.get_definition(closure)
        if isinstance(closure, tuple):
            apb__lab = ctypes.pythonapi.PyCell_Get
            apb__lab.restype = ctypes.py_object
            apb__lab.argtypes = ctypes.py_object,
            nlmby__zot = tuple(apb__lab(hmmf__zjji) for hmmf__zjji in closure)
        else:
            assert isinstance(closure, ir.Expr) and closure.op == 'build_tuple'
            nlmby__zot = closure.items
        assert len(code.co_freevars) == len(nlmby__zot)
        numba.core.inline_closurecall._replace_freevars(f_ir.blocks, nlmby__zot
            )


class RegularUDFGenerator:

    def __init__(self, in_col_types, typingctx, targetctx):
        self.in_col_types = in_col_types
        self.typingctx = typingctx
        self.targetctx = targetctx
        self.all_reduce_vars = []
        self.all_vartypes = []
        self.all_init_nodes = []
        self.all_eval_funcs = []
        self.all_update_funcs = []
        self.all_combine_funcs = []
        self.curr_offset = 0
        self.redvar_offsets = [0]

    def add_udf(self, in_col_typ, func):
        iiniz__qdjyr = SeriesType(in_col_typ.dtype,
            to_str_arr_if_dict_array(in_col_typ), None, string_type)
        f_ir, pm = compile_to_optimized_ir(func, (iiniz__qdjyr,), self.
            typingctx, self.targetctx)
        f_ir._definitions = build_definitions(f_ir.blocks)
        assert len(f_ir.blocks
            ) == 1 and 0 in f_ir.blocks, 'only simple functions with one block supported for aggregation'
        block = f_ir.blocks[0]
        tfiw__lfhkt, arr_var = _rm_arg_agg_block(block, pm.typemap)
        nkjr__lmw = -1
        for cueis__alw, ackrz__ckmq in enumerate(tfiw__lfhkt):
            if isinstance(ackrz__ckmq, numba.parfors.parfor.Parfor):
                assert nkjr__lmw == -1, 'only one parfor for aggregation function'
                nkjr__lmw = cueis__alw
        parfor = None
        if nkjr__lmw != -1:
            parfor = tfiw__lfhkt[nkjr__lmw]
            remove_dels(parfor.loop_body)
            remove_dels({(0): parfor.init_block})
        init_nodes = []
        if parfor:
            init_nodes = tfiw__lfhkt[:nkjr__lmw] + parfor.init_block.body
        eval_nodes = tfiw__lfhkt[nkjr__lmw + 1:]
        redvars = []
        var_to_redvar = {}
        if parfor:
            redvars, var_to_redvar = get_parfor_reductions(parfor, parfor.
                params, pm.calltypes)
        func.ncols_pre_shuffle = len(redvars)
        func.ncols_post_shuffle = len(redvars) + 1
        func.n_redvars = len(redvars)
        reduce_vars = [0] * len(redvars)
        for ackrz__ckmq in init_nodes:
            if is_assign(ackrz__ckmq) and ackrz__ckmq.target.name in redvars:
                ind = redvars.index(ackrz__ckmq.target.name)
                reduce_vars[ind] = ackrz__ckmq.target
        var_types = [pm.typemap[rtc__ucla] for rtc__ucla in redvars]
        frd__xnu = gen_combine_func(f_ir, parfor, redvars, var_to_redvar,
            var_types, arr_var, pm, self.typingctx, self.targetctx)
        init_nodes = _mv_read_only_init_vars(init_nodes, parfor, eval_nodes)
        vla__ako = gen_update_func(parfor, redvars, var_to_redvar,
            var_types, arr_var, in_col_typ, pm, self.typingctx, self.targetctx)
        laxc__mnrn = gen_eval_func(f_ir, eval_nodes, reduce_vars, var_types,
            pm, self.typingctx, self.targetctx)
        self.all_reduce_vars += reduce_vars
        self.all_vartypes += var_types
        self.all_init_nodes += init_nodes
        self.all_eval_funcs.append(laxc__mnrn)
        self.all_update_funcs.append(vla__ako)
        self.all_combine_funcs.append(frd__xnu)
        self.curr_offset += len(redvars)
        self.redvar_offsets.append(self.curr_offset)

    def gen_all_func(self):
        if len(self.all_update_funcs) == 0:
            return None
        ytzc__hag = gen_init_func(self.all_init_nodes, self.all_reduce_vars,
            self.all_vartypes, self.typingctx, self.targetctx)
        nma__yyv = gen_all_update_func(self.all_update_funcs, self.
            in_col_types, self.redvar_offsets)
        nuaf__ubskj = gen_all_combine_func(self.all_combine_funcs, self.
            all_vartypes, self.redvar_offsets, self.typingctx, self.targetctx)
        vpmua__unzy = gen_all_eval_func(self.all_eval_funcs, self.
            redvar_offsets)
        return self.all_vartypes, ytzc__hag, nma__yyv, nuaf__ubskj, vpmua__unzy


class GeneralUDFGenerator(object):

    def __init__(self):
        self.funcs = []

    def add_udf(self, func):
        self.funcs.append(bodo.jit(distributed=False)(func))
        func.ncols_pre_shuffle = 1
        func.ncols_post_shuffle = 1
        func.n_redvars = 0

    def gen_all_func(self):
        if len(self.funcs) > 0:
            return self.funcs
        else:
            return None


def get_udf_func_struct(agg_func, in_col_types, typingctx, targetctx):
    tzgh__dlul = []
    for t, cso__nvfu in zip(in_col_types, agg_func):
        tzgh__dlul.append((t, cso__nvfu))
    yeolm__wzwm = RegularUDFGenerator(in_col_types, typingctx, targetctx)
    fxa__dvyyy = GeneralUDFGenerator()
    for in_col_typ, func in tzgh__dlul:
        if func.ftype not in ('udf', 'gen_udf'):
            continue
        try:
            yeolm__wzwm.add_udf(in_col_typ, func)
        except:
            fxa__dvyyy.add_udf(func)
            func.ftype = 'gen_udf'
    regular_udf_funcs = yeolm__wzwm.gen_all_func()
    general_udf_funcs = fxa__dvyyy.gen_all_func()
    if regular_udf_funcs is not None or general_udf_funcs is not None:
        return AggUDFStruct(regular_udf_funcs, general_udf_funcs)
    else:
        return None


def _mv_read_only_init_vars(init_nodes, parfor, eval_nodes):
    if not parfor:
        return init_nodes
    fzq__uvg = compute_use_defs(parfor.loop_body)
    kcbdq__hri = set()
    for twcrz__ekoc in fzq__uvg.usemap.values():
        kcbdq__hri |= twcrz__ekoc
    wkc__akbo = set()
    for twcrz__ekoc in fzq__uvg.defmap.values():
        wkc__akbo |= twcrz__ekoc
    cgavp__wwd = ir.Block(ir.Scope(None, parfor.loc), parfor.loc)
    cgavp__wwd.body = eval_nodes
    pfwx__adjo = compute_use_defs({(0): cgavp__wwd})
    ibtp__xpjpt = pfwx__adjo.usemap[0]
    ltkm__jawi = set()
    rhw__wfpn = []
    wjdv__wvwj = []
    for ackrz__ckmq in reversed(init_nodes):
        jqq__smm = {rtc__ucla.name for rtc__ucla in ackrz__ckmq.list_vars()}
        if is_assign(ackrz__ckmq):
            rtc__ucla = ackrz__ckmq.target.name
            jqq__smm.remove(rtc__ucla)
            if (rtc__ucla in kcbdq__hri and rtc__ucla not in ltkm__jawi and
                rtc__ucla not in ibtp__xpjpt and rtc__ucla not in wkc__akbo):
                wjdv__wvwj.append(ackrz__ckmq)
                kcbdq__hri |= jqq__smm
                wkc__akbo.add(rtc__ucla)
                continue
        ltkm__jawi |= jqq__smm
        rhw__wfpn.append(ackrz__ckmq)
    wjdv__wvwj.reverse()
    rhw__wfpn.reverse()
    dfh__yya = min(parfor.loop_body.keys())
    ijq__xzxc = parfor.loop_body[dfh__yya]
    ijq__xzxc.body = wjdv__wvwj + ijq__xzxc.body
    return rhw__wfpn


def gen_init_func(init_nodes, reduce_vars, var_types, typingctx, targetctx):
    haeky__zlds = (numba.parfors.parfor.max_checker, numba.parfors.parfor.
        min_checker, numba.parfors.parfor.argmax_checker, numba.parfors.
        parfor.argmin_checker)
    twxa__poi = set()
    vcs__zmbe = []
    for ackrz__ckmq in init_nodes:
        if is_assign(ackrz__ckmq) and isinstance(ackrz__ckmq.value, ir.Global
            ) and isinstance(ackrz__ckmq.value.value, pytypes.FunctionType
            ) and ackrz__ckmq.value.value in haeky__zlds:
            twxa__poi.add(ackrz__ckmq.target.name)
        elif is_call_assign(ackrz__ckmq
            ) and ackrz__ckmq.value.func.name in twxa__poi:
            pass
        else:
            vcs__zmbe.append(ackrz__ckmq)
    init_nodes = vcs__zmbe
    zgx__grzk = types.Tuple(var_types)
    awbb__crbff = lambda : None
    f_ir = compile_to_numba_ir(awbb__crbff, {})
    block = list(f_ir.blocks.values())[0]
    loc = block.loc
    azng__ezsp = ir.Var(block.scope, mk_unique_var('init_tup'), loc)
    pigxi__zkrn = ir.Assign(ir.Expr.build_tuple(reduce_vars, loc),
        azng__ezsp, loc)
    block.body = block.body[-2:]
    block.body = init_nodes + [pigxi__zkrn] + block.body
    block.body[-2].value.value = azng__ezsp
    fods__msslk = compiler.compile_ir(typingctx, targetctx, f_ir, (),
        zgx__grzk, compiler.DEFAULT_FLAGS, {})
    from numba.core.target_extension import cpu_target
    yqka__taykv = numba.core.target_extension.dispatcher_registry[cpu_target](
        awbb__crbff)
    yqka__taykv.add_overload(fods__msslk)
    return yqka__taykv


def gen_all_update_func(update_funcs, in_col_types, redvar_offsets):
    auyv__vfk = len(update_funcs)
    rxzyp__cfe = len(in_col_types)
    nfka__hvk = 'def update_all_f(redvar_arrs, data_in, w_ind, i):\n'
    for mwodi__tvam in range(auyv__vfk):
        umc__oputp = ', '.join(['redvar_arrs[{}][w_ind]'.format(cueis__alw) for
            cueis__alw in range(redvar_offsets[mwodi__tvam], redvar_offsets
            [mwodi__tvam + 1])])
        if umc__oputp:
            nfka__hvk += '  {} = update_vars_{}({},  data_in[{}][i])\n'.format(
                umc__oputp, mwodi__tvam, umc__oputp, 0 if rxzyp__cfe == 1 else
                mwodi__tvam)
    nfka__hvk += '  return\n'
    kyrb__nxzkk = {}
    for cueis__alw, cso__nvfu in enumerate(update_funcs):
        kyrb__nxzkk['update_vars_{}'.format(cueis__alw)] = cso__nvfu
    jofdc__jsibs = {}
    exec(nfka__hvk, kyrb__nxzkk, jofdc__jsibs)
    tnbk__tmm = jofdc__jsibs['update_all_f']
    return numba.njit(no_cpython_wrapper=True)(tnbk__tmm)


def gen_all_combine_func(combine_funcs, reduce_var_types, redvar_offsets,
    typingctx, targetctx):
    bwr__cjd = types.Tuple([types.Array(t, 1, 'C') for t in reduce_var_types])
    arg_typs = bwr__cjd, bwr__cjd, types.intp, types.intp
    hlfho__sek = len(redvar_offsets) - 1
    nfka__hvk = 'def combine_all_f(redvar_arrs, recv_arrs, w_ind, i):\n'
    for mwodi__tvam in range(hlfho__sek):
        umc__oputp = ', '.join(['redvar_arrs[{}][w_ind]'.format(cueis__alw) for
            cueis__alw in range(redvar_offsets[mwodi__tvam], redvar_offsets
            [mwodi__tvam + 1])])
        yegde__teqt = ', '.join(['recv_arrs[{}][i]'.format(cueis__alw) for
            cueis__alw in range(redvar_offsets[mwodi__tvam], redvar_offsets
            [mwodi__tvam + 1])])
        if yegde__teqt:
            nfka__hvk += '  {} = combine_vars_{}({}, {})\n'.format(umc__oputp,
                mwodi__tvam, umc__oputp, yegde__teqt)
    nfka__hvk += '  return\n'
    kyrb__nxzkk = {}
    for cueis__alw, cso__nvfu in enumerate(combine_funcs):
        kyrb__nxzkk['combine_vars_{}'.format(cueis__alw)] = cso__nvfu
    jofdc__jsibs = {}
    exec(nfka__hvk, kyrb__nxzkk, jofdc__jsibs)
    feej__vaz = jofdc__jsibs['combine_all_f']
    f_ir = compile_to_numba_ir(feej__vaz, kyrb__nxzkk)
    nuaf__ubskj = compiler.compile_ir(typingctx, targetctx, f_ir, arg_typs,
        types.none, compiler.DEFAULT_FLAGS, {})
    from numba.core.target_extension import cpu_target
    yqka__taykv = numba.core.target_extension.dispatcher_registry[cpu_target](
        feej__vaz)
    yqka__taykv.add_overload(nuaf__ubskj)
    return yqka__taykv


def gen_all_eval_func(eval_funcs, redvar_offsets):
    hlfho__sek = len(redvar_offsets) - 1
    nfka__hvk = 'def eval_all_f(redvar_arrs, out_arrs, j):\n'
    for mwodi__tvam in range(hlfho__sek):
        umc__oputp = ', '.join(['redvar_arrs[{}][j]'.format(cueis__alw) for
            cueis__alw in range(redvar_offsets[mwodi__tvam], redvar_offsets
            [mwodi__tvam + 1])])
        nfka__hvk += '  out_arrs[{}][j] = eval_vars_{}({})\n'.format(
            mwodi__tvam, mwodi__tvam, umc__oputp)
    nfka__hvk += '  return\n'
    kyrb__nxzkk = {}
    for cueis__alw, cso__nvfu in enumerate(eval_funcs):
        kyrb__nxzkk['eval_vars_{}'.format(cueis__alw)] = cso__nvfu
    jofdc__jsibs = {}
    exec(nfka__hvk, kyrb__nxzkk, jofdc__jsibs)
    ozekf__zizig = jofdc__jsibs['eval_all_f']
    return numba.njit(no_cpython_wrapper=True)(ozekf__zizig)


def gen_eval_func(f_ir, eval_nodes, reduce_vars, var_types, pm, typingctx,
    targetctx):
    zylwk__wfd = len(var_types)
    jhn__ufptt = [f'in{cueis__alw}' for cueis__alw in range(zylwk__wfd)]
    zgx__grzk = types.unliteral(pm.typemap[eval_nodes[-1].value.name])
    hbiyv__yxp = zgx__grzk(0)
    nfka__hvk = 'def agg_eval({}):\n return _zero\n'.format(', '.join(
        jhn__ufptt))
    jofdc__jsibs = {}
    exec(nfka__hvk, {'_zero': hbiyv__yxp}, jofdc__jsibs)
    hqalo__tfh = jofdc__jsibs['agg_eval']
    arg_typs = tuple(var_types)
    f_ir = compile_to_numba_ir(hqalo__tfh, {'numba': numba, 'bodo': bodo,
        'np': np, '_zero': hbiyv__yxp}, typingctx=typingctx, targetctx=
        targetctx, arg_typs=arg_typs, typemap=pm.typemap, calltypes=pm.
        calltypes)
    block = list(f_ir.blocks.values())[0]
    sehbx__rpgs = []
    for cueis__alw, rtc__ucla in enumerate(reduce_vars):
        sehbx__rpgs.append(ir.Assign(block.body[cueis__alw].target,
            rtc__ucla, rtc__ucla.loc))
        for zpe__rgez in rtc__ucla.versioned_names:
            sehbx__rpgs.append(ir.Assign(rtc__ucla, ir.Var(rtc__ucla.scope,
                zpe__rgez, rtc__ucla.loc), rtc__ucla.loc))
    block.body = block.body[:zylwk__wfd] + sehbx__rpgs + eval_nodes
    laxc__mnrn = compiler.compile_ir(typingctx, targetctx, f_ir, arg_typs,
        zgx__grzk, compiler.DEFAULT_FLAGS, {})
    from numba.core.target_extension import cpu_target
    yqka__taykv = numba.core.target_extension.dispatcher_registry[cpu_target](
        hqalo__tfh)
    yqka__taykv.add_overload(laxc__mnrn)
    return yqka__taykv


def gen_combine_func(f_ir, parfor, redvars, var_to_redvar, var_types,
    arr_var, pm, typingctx, targetctx):
    if not parfor:
        return numba.njit(lambda : ())
    zylwk__wfd = len(redvars)
    cxxm__qxll = [f'v{cueis__alw}' for cueis__alw in range(zylwk__wfd)]
    jhn__ufptt = [f'in{cueis__alw}' for cueis__alw in range(zylwk__wfd)]
    nfka__hvk = 'def agg_combine({}):\n'.format(', '.join(cxxm__qxll +
        jhn__ufptt))
    lzg__nrfnd = wrap_parfor_blocks(parfor)
    xpemn__ninyq = find_topo_order(lzg__nrfnd)
    xpemn__ninyq = xpemn__ninyq[1:]
    unwrap_parfor_blocks(parfor)
    icxd__lnqr = {}
    mbk__gbqgx = []
    for ynicb__lrnn in xpemn__ninyq:
        ickf__scq = parfor.loop_body[ynicb__lrnn]
        for ackrz__ckmq in ickf__scq.body:
            if is_assign(ackrz__ckmq) and ackrz__ckmq.target.name in redvars:
                cslcj__yzkf = ackrz__ckmq.target.name
                ind = redvars.index(cslcj__yzkf)
                if ind in mbk__gbqgx:
                    continue
                if len(f_ir._definitions[cslcj__yzkf]) == 2:
                    var_def = f_ir._definitions[cslcj__yzkf][0]
                    nfka__hvk += _match_reduce_def(var_def, f_ir, ind)
                    var_def = f_ir._definitions[cslcj__yzkf][1]
                    nfka__hvk += _match_reduce_def(var_def, f_ir, ind)
    nfka__hvk += '    return {}'.format(', '.join(['v{}'.format(cueis__alw) for
        cueis__alw in range(zylwk__wfd)]))
    jofdc__jsibs = {}
    exec(nfka__hvk, {}, jofdc__jsibs)
    unbgw__imyog = jofdc__jsibs['agg_combine']
    arg_typs = tuple(2 * var_types)
    kyrb__nxzkk = {'numba': numba, 'bodo': bodo, 'np': np}
    kyrb__nxzkk.update(icxd__lnqr)
    f_ir = compile_to_numba_ir(unbgw__imyog, kyrb__nxzkk, typingctx=
        typingctx, targetctx=targetctx, arg_typs=arg_typs, typemap=pm.
        typemap, calltypes=pm.calltypes)
    block = list(f_ir.blocks.values())[0]
    zgx__grzk = pm.typemap[block.body[-1].value.name]
    frd__xnu = compiler.compile_ir(typingctx, targetctx, f_ir, arg_typs,
        zgx__grzk, compiler.DEFAULT_FLAGS, {})
    from numba.core.target_extension import cpu_target
    yqka__taykv = numba.core.target_extension.dispatcher_registry[cpu_target](
        unbgw__imyog)
    yqka__taykv.add_overload(frd__xnu)
    return yqka__taykv


def _match_reduce_def(var_def, f_ir, ind):
    nfka__hvk = ''
    while isinstance(var_def, ir.Var):
        var_def = guard(get_definition, f_ir, var_def)
    if isinstance(var_def, ir.Expr
        ) and var_def.op == 'inplace_binop' and var_def.fn in ('+=',
        operator.iadd):
        nfka__hvk = '    v{} += in{}\n'.format(ind, ind)
    if isinstance(var_def, ir.Expr) and var_def.op == 'call':
        ruag__ctdmp = guard(find_callname, f_ir, var_def)
        if ruag__ctdmp == ('min', 'builtins'):
            nfka__hvk = '    v{} = min(v{}, in{})\n'.format(ind, ind, ind)
        if ruag__ctdmp == ('max', 'builtins'):
            nfka__hvk = '    v{} = max(v{}, in{})\n'.format(ind, ind, ind)
    return nfka__hvk


def gen_update_func(parfor, redvars, var_to_redvar, var_types, arr_var,
    in_col_typ, pm, typingctx, targetctx):
    if not parfor:
        return numba.njit(lambda A: ())
    zylwk__wfd = len(redvars)
    gfi__tsrzj = 1
    in_vars = []
    for cueis__alw in range(gfi__tsrzj):
        szi__yfjwh = ir.Var(arr_var.scope, f'$input{cueis__alw}', arr_var.loc)
        in_vars.append(szi__yfjwh)
    rdc__dciz = parfor.loop_nests[0].index_variable
    aixy__tjq = [0] * zylwk__wfd
    for ickf__scq in parfor.loop_body.values():
        wcsj__zmqk = []
        for ackrz__ckmq in ickf__scq.body:
            if is_var_assign(ackrz__ckmq
                ) and ackrz__ckmq.value.name == rdc__dciz.name:
                continue
            if is_getitem(ackrz__ckmq
                ) and ackrz__ckmq.value.value.name == arr_var.name:
                ackrz__ckmq.value = in_vars[0]
            if is_call_assign(ackrz__ckmq) and guard(find_callname, pm.
                func_ir, ackrz__ckmq.value) == ('isna',
                'bodo.libs.array_kernels') and ackrz__ckmq.value.args[0
                ].name == arr_var.name:
                ackrz__ckmq.value = ir.Const(False, ackrz__ckmq.target.loc)
            if is_assign(ackrz__ckmq) and ackrz__ckmq.target.name in redvars:
                ind = redvars.index(ackrz__ckmq.target.name)
                aixy__tjq[ind] = ackrz__ckmq.target
            wcsj__zmqk.append(ackrz__ckmq)
        ickf__scq.body = wcsj__zmqk
    cxxm__qxll = ['v{}'.format(cueis__alw) for cueis__alw in range(zylwk__wfd)]
    jhn__ufptt = ['in{}'.format(cueis__alw) for cueis__alw in range(gfi__tsrzj)
        ]
    nfka__hvk = 'def agg_update({}):\n'.format(', '.join(cxxm__qxll +
        jhn__ufptt))
    nfka__hvk += '    __update_redvars()\n'
    nfka__hvk += '    return {}'.format(', '.join(['v{}'.format(cueis__alw) for
        cueis__alw in range(zylwk__wfd)]))
    jofdc__jsibs = {}
    exec(nfka__hvk, {}, jofdc__jsibs)
    qiq__ynu = jofdc__jsibs['agg_update']
    arg_typs = tuple(var_types + [in_col_typ.dtype] * gfi__tsrzj)
    f_ir = compile_to_numba_ir(qiq__ynu, {'__update_redvars':
        __update_redvars}, typingctx=typingctx, targetctx=targetctx,
        arg_typs=arg_typs, typemap=pm.typemap, calltypes=pm.calltypes)
    f_ir._definitions = build_definitions(f_ir.blocks)
    yucq__cyv = f_ir.blocks.popitem()[1].body
    zgx__grzk = pm.typemap[yucq__cyv[-1].value.name]
    lzg__nrfnd = wrap_parfor_blocks(parfor)
    xpemn__ninyq = find_topo_order(lzg__nrfnd)
    xpemn__ninyq = xpemn__ninyq[1:]
    unwrap_parfor_blocks(parfor)
    f_ir.blocks = parfor.loop_body
    ijq__xzxc = f_ir.blocks[xpemn__ninyq[0]]
    fdnt__aib = f_ir.blocks[xpemn__ninyq[-1]]
    geczt__qwbgy = yucq__cyv[:zylwk__wfd + gfi__tsrzj]
    if zylwk__wfd > 1:
        unl__moxbi = yucq__cyv[-3:]
        assert is_assign(unl__moxbi[0]) and isinstance(unl__moxbi[0].value,
            ir.Expr) and unl__moxbi[0].value.op == 'build_tuple'
    else:
        unl__moxbi = yucq__cyv[-2:]
    for cueis__alw in range(zylwk__wfd):
        xwkt__tcb = yucq__cyv[cueis__alw].target
        yuf__hstt = ir.Assign(xwkt__tcb, aixy__tjq[cueis__alw], xwkt__tcb.loc)
        geczt__qwbgy.append(yuf__hstt)
    for cueis__alw in range(zylwk__wfd, zylwk__wfd + gfi__tsrzj):
        xwkt__tcb = yucq__cyv[cueis__alw].target
        yuf__hstt = ir.Assign(xwkt__tcb, in_vars[cueis__alw - zylwk__wfd],
            xwkt__tcb.loc)
        geczt__qwbgy.append(yuf__hstt)
    ijq__xzxc.body = geczt__qwbgy + ijq__xzxc.body
    abr__swwa = []
    for cueis__alw in range(zylwk__wfd):
        xwkt__tcb = yucq__cyv[cueis__alw].target
        yuf__hstt = ir.Assign(aixy__tjq[cueis__alw], xwkt__tcb, xwkt__tcb.loc)
        abr__swwa.append(yuf__hstt)
    fdnt__aib.body += abr__swwa + unl__moxbi
    lwbjc__jrp = compiler.compile_ir(typingctx, targetctx, f_ir, arg_typs,
        zgx__grzk, compiler.DEFAULT_FLAGS, {})
    from numba.core.target_extension import cpu_target
    yqka__taykv = numba.core.target_extension.dispatcher_registry[cpu_target](
        qiq__ynu)
    yqka__taykv.add_overload(lwbjc__jrp)
    return yqka__taykv


def _rm_arg_agg_block(block, typemap):
    tfiw__lfhkt = []
    arr_var = None
    for cueis__alw, ackrz__ckmq in enumerate(block.body):
        if is_assign(ackrz__ckmq) and isinstance(ackrz__ckmq.value, ir.Arg):
            arr_var = ackrz__ckmq.target
            ofjgj__vgg = typemap[arr_var.name]
            if not isinstance(ofjgj__vgg, types.ArrayCompatible):
                tfiw__lfhkt += block.body[cueis__alw + 1:]
                break
            atldz__ett = block.body[cueis__alw + 1]
            assert is_assign(atldz__ett) and isinstance(atldz__ett.value,
                ir.Expr
                ) and atldz__ett.value.op == 'getattr' and atldz__ett.value.attr == 'shape' and atldz__ett.value.value.name == arr_var.name
            ewdu__rvdj = atldz__ett.target
            uxt__cpx = block.body[cueis__alw + 2]
            assert is_assign(uxt__cpx) and isinstance(uxt__cpx.value, ir.Expr
                ) and uxt__cpx.value.op == 'static_getitem' and uxt__cpx.value.value.name == ewdu__rvdj.name
            tfiw__lfhkt += block.body[cueis__alw + 3:]
            break
        tfiw__lfhkt.append(ackrz__ckmq)
    return tfiw__lfhkt, arr_var


def get_parfor_reductions(parfor, parfor_params, calltypes, reduce_varnames
    =None, param_uses=None, var_to_param=None):
    if reduce_varnames is None:
        reduce_varnames = []
    if param_uses is None:
        param_uses = defaultdict(list)
    if var_to_param is None:
        var_to_param = {}
    lzg__nrfnd = wrap_parfor_blocks(parfor)
    xpemn__ninyq = find_topo_order(lzg__nrfnd)
    xpemn__ninyq = xpemn__ninyq[1:]
    unwrap_parfor_blocks(parfor)
    for ynicb__lrnn in reversed(xpemn__ninyq):
        for ackrz__ckmq in reversed(parfor.loop_body[ynicb__lrnn].body):
            if isinstance(ackrz__ckmq, ir.Assign) and (ackrz__ckmq.target.
                name in parfor_params or ackrz__ckmq.target.name in
                var_to_param):
                ahd__nohb = ackrz__ckmq.target.name
                rhs = ackrz__ckmq.value
                aemru__okam = (ahd__nohb if ahd__nohb in parfor_params else
                    var_to_param[ahd__nohb])
                zzpg__xtu = []
                if isinstance(rhs, ir.Var):
                    zzpg__xtu = [rhs.name]
                elif isinstance(rhs, ir.Expr):
                    zzpg__xtu = [rtc__ucla.name for rtc__ucla in
                        ackrz__ckmq.value.list_vars()]
                param_uses[aemru__okam].extend(zzpg__xtu)
                for rtc__ucla in zzpg__xtu:
                    var_to_param[rtc__ucla] = aemru__okam
            if isinstance(ackrz__ckmq, Parfor):
                get_parfor_reductions(ackrz__ckmq, parfor_params, calltypes,
                    reduce_varnames, param_uses, var_to_param)
    for ysie__nftk, zzpg__xtu in param_uses.items():
        if ysie__nftk in zzpg__xtu and ysie__nftk not in reduce_varnames:
            reduce_varnames.append(ysie__nftk)
    return reduce_varnames, var_to_param


@numba.extending.register_jitable
def dummy_agg_count(A):
    return len(A)
