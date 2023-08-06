"""IR node for the join and merge"""
from collections import defaultdict
from typing import Dict, List, Literal, Optional, Set, Tuple, Union
import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from numba.core import cgutils, ir, ir_utils, types
from numba.core.ir_utils import compile_to_numba_ir, next_label, replace_arg_nodes, replace_vars_inner, visit_vars_inner
from numba.extending import intrinsic
import bodo
from bodo.hiframes.table import TableType
from bodo.ir.connector import trim_extra_used_columns
from bodo.libs.array import arr_info_list_to_table, array_to_info, cpp_table_to_py_data, cross_join_table, delete_table, hash_join_table, py_data_to_cpp_table
from bodo.libs.timsort import getitem_arr_tup, setitem_arr_tup
from bodo.transforms import distributed_analysis, distributed_pass
from bodo.transforms.distributed_analysis import Distribution
from bodo.transforms.table_column_del_pass import _compute_table_column_uses, get_live_column_nums_block, ir_extension_table_column_use, remove_dead_column_extensions
from bodo.utils.typing import INDEX_SENTINEL, BodoError, MetaType, dtype_to_array_type, find_common_np_dtype, is_dtype_nullable, is_nullable_type, is_str_arr_type, to_nullable_type
from bodo.utils.utils import alloc_arr_tup, is_null_pointer
join_gen_cond_cfunc = {}
join_gen_cond_cfunc_addr = {}


@intrinsic
def add_join_gen_cond_cfunc_sym(typingctx, func, sym):

    def codegen(context, builder, signature, args):
        ajdh__lrvyq = func.signature
        qtpc__fsv = lir.FunctionType(lir.IntType(1), [lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(64), lir
            .IntType(64)])
        skat__jwqw = cgutils.get_or_insert_function(builder.module,
            qtpc__fsv, sym._literal_value)
        builder.call(skat__jwqw, [context.get_constant_null(ajdh__lrvyq.
            args[0]), context.get_constant_null(ajdh__lrvyq.args[1]),
            context.get_constant_null(ajdh__lrvyq.args[2]), context.
            get_constant_null(ajdh__lrvyq.args[3]), context.
            get_constant_null(ajdh__lrvyq.args[4]), context.
            get_constant_null(ajdh__lrvyq.args[5]), context.get_constant(
            types.int64, 0), context.get_constant(types.int64, 0)])
        context.add_linking_libs([join_gen_cond_cfunc[sym._literal_value].
            _library])
        return
    return types.none(func, sym), codegen


@numba.jit
def get_join_cond_addr(name):
    with numba.objmode(addr='int64'):
        addr = join_gen_cond_cfunc_addr[name]
    return addr


HOW_OPTIONS = Literal['inner', 'left', 'right', 'outer', 'asof', 'cross']


class Join(ir.Stmt):

    def __init__(self, left_keys: Union[List[str], str], right_keys: Union[
        List[str], str], out_data_vars: List[ir.Var], out_df_type: bodo.
        DataFrameType, left_vars: List[ir.Var], left_df_type: bodo.
        DataFrameType, right_vars: List[ir.Var], right_df_type: bodo.
        DataFrameType, how: HOW_OPTIONS, suffix_left: str, suffix_right:
        str, loc: ir.Loc, is_left: bool, is_right: bool, is_join: bool,
        left_index: bool, right_index: bool, indicator_col_num: int,
        is_na_equal: bool, gen_cond_expr: str, left_len_var: ir.Var,
        right_len_var: ir.Var):
        self.left_keys = left_keys
        self.right_keys = right_keys
        self.out_data_vars = out_data_vars
        self.out_col_names = out_df_type.columns
        self.left_vars = left_vars
        self.right_vars = right_vars
        self.how = how
        self.loc = loc
        self.is_left = is_left
        self.is_right = is_right
        self.is_join = is_join
        self.left_index = left_index
        self.right_index = right_index
        self.indicator_col_num = indicator_col_num
        self.is_na_equal = is_na_equal
        self.gen_cond_expr = gen_cond_expr
        self.left_len_var = left_len_var
        self.right_len_var = right_len_var
        self.n_out_table_cols = len(self.out_col_names)
        self.out_used_cols = set(range(self.n_out_table_cols))
        if self.out_data_vars[1] is not None:
            self.out_used_cols.add(self.n_out_table_cols)
        ysb__pxn = left_df_type.columns
        tuox__qlg = right_df_type.columns
        self.left_col_names = ysb__pxn
        self.right_col_names = tuox__qlg
        self.is_left_table = left_df_type.is_table_format
        self.is_right_table = right_df_type.is_table_format
        self.n_left_table_cols = len(ysb__pxn) if self.is_left_table else 0
        self.n_right_table_cols = len(tuox__qlg) if self.is_right_table else 0
        olooy__kobls = self.n_left_table_cols if self.is_left_table else len(
            left_vars) - 1
        lva__chsy = self.n_right_table_cols if self.is_right_table else len(
            right_vars) - 1
        self.left_dead_var_inds = set()
        self.right_dead_var_inds = set()
        if self.left_vars[-1] is None:
            self.left_dead_var_inds.add(olooy__kobls)
        if self.right_vars[-1] is None:
            self.right_dead_var_inds.add(lva__chsy)
        self.left_var_map = {upfi__vxqr: nqs__wnvyf for nqs__wnvyf,
            upfi__vxqr in enumerate(ysb__pxn)}
        self.right_var_map = {upfi__vxqr: nqs__wnvyf for nqs__wnvyf,
            upfi__vxqr in enumerate(tuox__qlg)}
        if self.left_vars[-1] is not None:
            self.left_var_map[INDEX_SENTINEL] = olooy__kobls
        if self.right_vars[-1] is not None:
            self.right_var_map[INDEX_SENTINEL] = lva__chsy
        self.left_key_set = set(self.left_var_map[upfi__vxqr] for
            upfi__vxqr in left_keys)
        self.right_key_set = set(self.right_var_map[upfi__vxqr] for
            upfi__vxqr in right_keys)
        if gen_cond_expr:
            self.left_cond_cols = set(self.left_var_map[upfi__vxqr] for
                upfi__vxqr in ysb__pxn if f'(left.{upfi__vxqr})' in
                gen_cond_expr)
            self.right_cond_cols = set(self.right_var_map[upfi__vxqr] for
                upfi__vxqr in tuox__qlg if f'(right.{upfi__vxqr})' in
                gen_cond_expr)
        else:
            self.left_cond_cols = set()
            self.right_cond_cols = set()
        ezo__vys: int = -1
        djz__cyrsh = set(left_keys) & set(right_keys)
        lvy__wad = set(ysb__pxn) & set(tuox__qlg)
        dgwo__zkmgv = lvy__wad - djz__cyrsh
        npcpr__cevzx: Dict[int, (Literal['left', 'right'], int)] = {}
        xhhkr__wqed: Dict[int, int] = {}
        qxcl__yutqy: Dict[int, int] = {}
        for nqs__wnvyf, upfi__vxqr in enumerate(ysb__pxn):
            if upfi__vxqr in dgwo__zkmgv:
                wspfj__mswbq = str(upfi__vxqr) + suffix_left
                fuy__dzyls = out_df_type.column_index[wspfj__mswbq]
                if (right_index and not left_index and nqs__wnvyf in self.
                    left_key_set):
                    ezo__vys = out_df_type.column_index[upfi__vxqr]
                    npcpr__cevzx[ezo__vys] = 'left', nqs__wnvyf
            else:
                fuy__dzyls = out_df_type.column_index[upfi__vxqr]
            npcpr__cevzx[fuy__dzyls] = 'left', nqs__wnvyf
            xhhkr__wqed[nqs__wnvyf] = fuy__dzyls
        for nqs__wnvyf, upfi__vxqr in enumerate(tuox__qlg):
            if upfi__vxqr not in djz__cyrsh:
                if upfi__vxqr in dgwo__zkmgv:
                    lox__ilv = str(upfi__vxqr) + suffix_right
                    fuy__dzyls = out_df_type.column_index[lox__ilv]
                    if (left_index and not right_index and nqs__wnvyf in
                        self.right_key_set):
                        ezo__vys = out_df_type.column_index[upfi__vxqr]
                        npcpr__cevzx[ezo__vys] = 'right', nqs__wnvyf
                else:
                    fuy__dzyls = out_df_type.column_index[upfi__vxqr]
                npcpr__cevzx[fuy__dzyls] = 'right', nqs__wnvyf
                qxcl__yutqy[nqs__wnvyf] = fuy__dzyls
        if self.left_vars[-1] is not None:
            xhhkr__wqed[olooy__kobls] = self.n_out_table_cols
        if self.right_vars[-1] is not None:
            qxcl__yutqy[lva__chsy] = self.n_out_table_cols
        self.out_to_input_col_map = npcpr__cevzx
        self.left_to_output_map = xhhkr__wqed
        self.right_to_output_map = qxcl__yutqy
        self.extra_data_col_num = ezo__vys
        if self.out_data_vars[1] is not None:
            lorqe__fztjn = 'left' if right_index else 'right'
            if lorqe__fztjn == 'left':
                vdl__htc = olooy__kobls
            elif lorqe__fztjn == 'right':
                vdl__htc = lva__chsy
        else:
            lorqe__fztjn = None
            vdl__htc = -1
        self.index_source = lorqe__fztjn
        self.index_col_num = vdl__htc
        ehz__mazj = []
        jxzl__afeal = len(left_keys)
        for tlbam__qepl in range(jxzl__afeal):
            fesqf__dlllf = left_keys[tlbam__qepl]
            gfw__wjow = right_keys[tlbam__qepl]
            ehz__mazj.append(fesqf__dlllf == gfw__wjow)
        self.vect_same_key = ehz__mazj

    @property
    def has_live_left_table_var(self):
        return self.is_left_table and self.left_vars[0] is not None

    @property
    def has_live_right_table_var(self):
        return self.is_right_table and self.right_vars[0] is not None

    @property
    def has_live_out_table_var(self):
        return self.out_data_vars[0] is not None

    @property
    def has_live_out_index_var(self):
        return self.out_data_vars[1] is not None

    def get_out_table_var(self):
        return self.out_data_vars[0]

    def get_out_index_var(self):
        return self.out_data_vars[1]

    def get_live_left_vars(self):
        vars = []
        for mqg__sii in self.left_vars:
            if mqg__sii is not None:
                vars.append(mqg__sii)
        return vars

    def get_live_right_vars(self):
        vars = []
        for mqg__sii in self.right_vars:
            if mqg__sii is not None:
                vars.append(mqg__sii)
        return vars

    def get_live_out_vars(self):
        vars = []
        for mqg__sii in self.out_data_vars:
            if mqg__sii is not None:
                vars.append(mqg__sii)
        return vars

    def set_live_left_vars(self, live_data_vars):
        left_vars = []
        xzjl__vhfgh = 0
        start = 0
        if self.is_left_table:
            if self.has_live_left_table_var:
                left_vars.append(live_data_vars[xzjl__vhfgh])
                xzjl__vhfgh += 1
            else:
                left_vars.append(None)
            start = 1
        jmlgx__eoe = max(self.n_left_table_cols - 1, 0)
        for nqs__wnvyf in range(start, len(self.left_vars)):
            if nqs__wnvyf + jmlgx__eoe in self.left_dead_var_inds:
                left_vars.append(None)
            else:
                left_vars.append(live_data_vars[xzjl__vhfgh])
                xzjl__vhfgh += 1
        self.left_vars = left_vars

    def set_live_right_vars(self, live_data_vars):
        right_vars = []
        xzjl__vhfgh = 0
        start = 0
        if self.is_right_table:
            if self.has_live_right_table_var:
                right_vars.append(live_data_vars[xzjl__vhfgh])
                xzjl__vhfgh += 1
            else:
                right_vars.append(None)
            start = 1
        jmlgx__eoe = max(self.n_right_table_cols - 1, 0)
        for nqs__wnvyf in range(start, len(self.right_vars)):
            if nqs__wnvyf + jmlgx__eoe in self.right_dead_var_inds:
                right_vars.append(None)
            else:
                right_vars.append(live_data_vars[xzjl__vhfgh])
                xzjl__vhfgh += 1
        self.right_vars = right_vars

    def set_live_out_data_vars(self, live_data_vars):
        out_data_vars = []
        nhwf__yuzg = [self.has_live_out_table_var, self.has_live_out_index_var]
        xzjl__vhfgh = 0
        for nqs__wnvyf in range(len(self.out_data_vars)):
            if not nhwf__yuzg[nqs__wnvyf]:
                out_data_vars.append(None)
            else:
                out_data_vars.append(live_data_vars[xzjl__vhfgh])
                xzjl__vhfgh += 1
        self.out_data_vars = out_data_vars

    def get_out_table_used_cols(self):
        return {nqs__wnvyf for nqs__wnvyf in self.out_used_cols if 
            nqs__wnvyf < self.n_out_table_cols}

    def __repr__(self):
        qdwz__lart = ', '.join([f'{upfi__vxqr}' for upfi__vxqr in self.
            left_col_names])
        auki__fei = f'left={{{qdwz__lart}}}'
        qdwz__lart = ', '.join([f'{upfi__vxqr}' for upfi__vxqr in self.
            right_col_names])
        qnjao__hcl = f'right={{{qdwz__lart}}}'
        return 'join [{}={}]: {}, {}'.format(self.left_keys, self.
            right_keys, auki__fei, qnjao__hcl)


def join_array_analysis(join_node, equiv_set, typemap, array_analysis):
    pzsbn__yzl = []
    assert len(join_node.get_live_out_vars()
        ) > 0, 'empty join in array analysis'
    egxyd__ohz = []
    wzpdo__owlbh = join_node.get_live_left_vars()
    for clirp__cyzt in wzpdo__owlbh:
        hcdgw__kvtt = typemap[clirp__cyzt.name]
        rpmw__xdxk = equiv_set.get_shape(clirp__cyzt)
        if rpmw__xdxk:
            egxyd__ohz.append(rpmw__xdxk[0])
    if len(egxyd__ohz) > 1:
        equiv_set.insert_equiv(*egxyd__ohz)
    egxyd__ohz = []
    wzpdo__owlbh = list(join_node.get_live_right_vars())
    for clirp__cyzt in wzpdo__owlbh:
        hcdgw__kvtt = typemap[clirp__cyzt.name]
        rpmw__xdxk = equiv_set.get_shape(clirp__cyzt)
        if rpmw__xdxk:
            egxyd__ohz.append(rpmw__xdxk[0])
    if len(egxyd__ohz) > 1:
        equiv_set.insert_equiv(*egxyd__ohz)
    egxyd__ohz = []
    for lmzzm__ymt in join_node.get_live_out_vars():
        hcdgw__kvtt = typemap[lmzzm__ymt.name]
        mwysq__oemfb = array_analysis._gen_shape_call(equiv_set, lmzzm__ymt,
            hcdgw__kvtt.ndim, None, pzsbn__yzl)
        equiv_set.insert_equiv(lmzzm__ymt, mwysq__oemfb)
        egxyd__ohz.append(mwysq__oemfb[0])
        equiv_set.define(lmzzm__ymt, set())
    if len(egxyd__ohz) > 1:
        equiv_set.insert_equiv(*egxyd__ohz)
    return [], pzsbn__yzl


numba.parfors.array_analysis.array_analysis_extensions[Join
    ] = join_array_analysis


def join_distributed_analysis(join_node, array_dists):
    omrxw__fyzk = Distribution.OneD
    nuto__nhk = Distribution.OneD
    for clirp__cyzt in join_node.get_live_left_vars():
        omrxw__fyzk = Distribution(min(omrxw__fyzk.value, array_dists[
            clirp__cyzt.name].value))
    for clirp__cyzt in join_node.get_live_right_vars():
        nuto__nhk = Distribution(min(nuto__nhk.value, array_dists[
            clirp__cyzt.name].value))
    ginpa__lyam = Distribution.OneD_Var
    for lmzzm__ymt in join_node.get_live_out_vars():
        if lmzzm__ymt.name in array_dists:
            ginpa__lyam = Distribution(min(ginpa__lyam.value, array_dists[
                lmzzm__ymt.name].value))
    wxmpl__ixffl = Distribution(min(ginpa__lyam.value, omrxw__fyzk.value))
    mxet__ltvet = Distribution(min(ginpa__lyam.value, nuto__nhk.value))
    ginpa__lyam = Distribution(max(wxmpl__ixffl.value, mxet__ltvet.value))
    for lmzzm__ymt in join_node.get_live_out_vars():
        array_dists[lmzzm__ymt.name] = ginpa__lyam
    if ginpa__lyam != Distribution.OneD_Var:
        omrxw__fyzk = ginpa__lyam
        nuto__nhk = ginpa__lyam
    for clirp__cyzt in join_node.get_live_left_vars():
        array_dists[clirp__cyzt.name] = omrxw__fyzk
    for clirp__cyzt in join_node.get_live_right_vars():
        array_dists[clirp__cyzt.name] = nuto__nhk
    join_node.left_dist = omrxw__fyzk
    join_node.right_dist = nuto__nhk


distributed_analysis.distributed_analysis_extensions[Join
    ] = join_distributed_analysis


def visit_vars_join(join_node, callback, cbdata):
    join_node.set_live_left_vars([visit_vars_inner(mqg__sii, callback,
        cbdata) for mqg__sii in join_node.get_live_left_vars()])
    join_node.set_live_right_vars([visit_vars_inner(mqg__sii, callback,
        cbdata) for mqg__sii in join_node.get_live_right_vars()])
    join_node.set_live_out_data_vars([visit_vars_inner(mqg__sii, callback,
        cbdata) for mqg__sii in join_node.get_live_out_vars()])
    if join_node.how == 'cross':
        join_node.left_len_var = visit_vars_inner(join_node.left_len_var,
            callback, cbdata)
        join_node.right_len_var = visit_vars_inner(join_node.right_len_var,
            callback, cbdata)


ir_utils.visit_vars_extensions[Join] = visit_vars_join


def _is_cross_join_len(join_node):
    return (join_node.how == 'cross' and not join_node.out_used_cols and
        join_node.has_live_out_table_var and not join_node.
        has_live_out_index_var)


def remove_dead_join(join_node, lives_no_aliases, lives, arg_aliases,
    alias_map, func_ir, typemap):
    if join_node.has_live_out_table_var:
        acfo__oswc = []
        glwg__idztn = join_node.get_out_table_var()
        if glwg__idztn.name not in lives:
            join_node.out_data_vars[0] = None
            join_node.out_used_cols.difference_update(join_node.
                get_out_table_used_cols())
        for mnjxt__mqf in join_node.out_to_input_col_map.keys():
            if mnjxt__mqf in join_node.out_used_cols:
                continue
            acfo__oswc.append(mnjxt__mqf)
            if join_node.indicator_col_num == mnjxt__mqf:
                join_node.indicator_col_num = -1
                continue
            if mnjxt__mqf == join_node.extra_data_col_num:
                join_node.extra_data_col_num = -1
                continue
            bzdbw__xvmx, mnjxt__mqf = join_node.out_to_input_col_map[mnjxt__mqf
                ]
            if bzdbw__xvmx == 'left':
                if (mnjxt__mqf not in join_node.left_key_set and mnjxt__mqf
                     not in join_node.left_cond_cols):
                    join_node.left_dead_var_inds.add(mnjxt__mqf)
                    if not join_node.is_left_table:
                        join_node.left_vars[mnjxt__mqf] = None
            elif bzdbw__xvmx == 'right':
                if (mnjxt__mqf not in join_node.right_key_set and 
                    mnjxt__mqf not in join_node.right_cond_cols):
                    join_node.right_dead_var_inds.add(mnjxt__mqf)
                    if not join_node.is_right_table:
                        join_node.right_vars[mnjxt__mqf] = None
        for nqs__wnvyf in acfo__oswc:
            del join_node.out_to_input_col_map[nqs__wnvyf]
        if join_node.is_left_table:
            rnday__mtlb = set(range(join_node.n_left_table_cols))
            koqn__ntfo = not bool(rnday__mtlb - join_node.left_dead_var_inds)
            if koqn__ntfo:
                join_node.left_vars[0] = None
        if join_node.is_right_table:
            rnday__mtlb = set(range(join_node.n_right_table_cols))
            koqn__ntfo = not bool(rnday__mtlb - join_node.right_dead_var_inds)
            if koqn__ntfo:
                join_node.right_vars[0] = None
    if join_node.has_live_out_index_var:
        qdq__ergj = join_node.get_out_index_var()
        if qdq__ergj.name not in lives:
            join_node.out_data_vars[1] = None
            join_node.out_used_cols.remove(join_node.n_out_table_cols)
            if join_node.index_source == 'left':
                if (join_node.index_col_num not in join_node.left_key_set and
                    join_node.index_col_num not in join_node.left_cond_cols):
                    join_node.left_dead_var_inds.add(join_node.index_col_num)
                    join_node.left_vars[-1] = None
            elif join_node.index_col_num not in join_node.right_key_set and join_node.index_col_num not in join_node.right_cond_cols:
                join_node.right_dead_var_inds.add(join_node.index_col_num)
                join_node.right_vars[-1] = None
    if not (join_node.has_live_out_table_var or join_node.
        has_live_out_index_var):
        return None
    return join_node


ir_utils.remove_dead_extensions[Join] = remove_dead_join


def join_remove_dead_column(join_node, column_live_map, equiv_vars, typemap):
    ekhv__zobo = False
    if join_node.has_live_out_table_var:
        hlc__yepdl = join_node.get_out_table_var().name
        goy__zkcfv, ijzt__ftntl, yrmq__gdify = get_live_column_nums_block(
            column_live_map, equiv_vars, hlc__yepdl)
        if not (ijzt__ftntl or yrmq__gdify):
            goy__zkcfv = trim_extra_used_columns(goy__zkcfv, join_node.
                n_out_table_cols)
            sbmeo__yogyx = join_node.get_out_table_used_cols()
            if len(goy__zkcfv) != len(sbmeo__yogyx):
                ekhv__zobo = not (join_node.is_left_table and join_node.
                    is_right_table)
                qlpsn__bweu = sbmeo__yogyx - goy__zkcfv
                join_node.out_used_cols = join_node.out_used_cols - qlpsn__bweu
    return ekhv__zobo


remove_dead_column_extensions[Join] = join_remove_dead_column


def join_table_column_use(join_node: Join, block_use_map: Dict[str, Tuple[
    Set[int], bool, bool]], equiv_vars: Dict[str, Set[str]], typemap: Dict[
    str, types.Type], table_col_use_map: Dict[int, Dict[str, Tuple[Set[int],
    bool, bool]]]):
    if not (join_node.is_left_table or join_node.is_right_table):
        return
    if join_node.has_live_out_table_var:
        leng__cxamz = join_node.get_out_table_var()
        umala__vrbq, ijzt__ftntl, yrmq__gdify = _compute_table_column_uses(
            leng__cxamz.name, table_col_use_map, equiv_vars)
    else:
        umala__vrbq, ijzt__ftntl, yrmq__gdify = set(), False, False
    if join_node.has_live_left_table_var:
        nrvjb__mmhph = join_node.left_vars[0].name
        hcgd__yemiw, fix__bdhj, cuw__minj = block_use_map[nrvjb__mmhph]
        if not (fix__bdhj or cuw__minj):
            pnw__wuuv = set([join_node.out_to_input_col_map[nqs__wnvyf][1] for
                nqs__wnvyf in umala__vrbq if join_node.out_to_input_col_map
                [nqs__wnvyf][0] == 'left'])
            zkl__pxfe = set(nqs__wnvyf for nqs__wnvyf in join_node.
                left_key_set | join_node.left_cond_cols if nqs__wnvyf <
                join_node.n_left_table_cols)
            if not (ijzt__ftntl or yrmq__gdify):
                join_node.left_dead_var_inds |= set(range(join_node.
                    n_left_table_cols)) - (pnw__wuuv | zkl__pxfe)
            block_use_map[nrvjb__mmhph] = (hcgd__yemiw | pnw__wuuv |
                zkl__pxfe, ijzt__ftntl or yrmq__gdify, False)
    if join_node.has_live_right_table_var:
        tbyg__krbti = join_node.right_vars[0].name
        hcgd__yemiw, fix__bdhj, cuw__minj = block_use_map[tbyg__krbti]
        if not (fix__bdhj or cuw__minj):
            umht__kax = set([join_node.out_to_input_col_map[nqs__wnvyf][1] for
                nqs__wnvyf in umala__vrbq if join_node.out_to_input_col_map
                [nqs__wnvyf][0] == 'right'])
            cvdx__tlxzi = set(nqs__wnvyf for nqs__wnvyf in join_node.
                right_key_set | join_node.right_cond_cols if nqs__wnvyf <
                join_node.n_right_table_cols)
            if not (ijzt__ftntl or yrmq__gdify):
                join_node.right_dead_var_inds |= set(range(join_node.
                    n_right_table_cols)) - (umht__kax | cvdx__tlxzi)
            block_use_map[tbyg__krbti] = (hcgd__yemiw | umht__kax |
                cvdx__tlxzi, ijzt__ftntl or yrmq__gdify, False)


ir_extension_table_column_use[Join] = join_table_column_use


def join_usedefs(join_node, use_set=None, def_set=None):
    if use_set is None:
        use_set = set()
    if def_set is None:
        def_set = set()
    use_set.update({onai__qwj.name for onai__qwj in join_node.
        get_live_left_vars()})
    use_set.update({onai__qwj.name for onai__qwj in join_node.
        get_live_right_vars()})
    def_set.update({onai__qwj.name for onai__qwj in join_node.
        get_live_out_vars()})
    if join_node.how == 'cross':
        use_set.add(join_node.left_len_var.name)
        use_set.add(join_node.right_len_var.name)
    return numba.core.analysis._use_defs_result(usemap=use_set, defmap=def_set)


numba.core.analysis.ir_extension_usedefs[Join] = join_usedefs


def get_copies_join(join_node, typemap):
    gimoe__qgy = set(onai__qwj.name for onai__qwj in join_node.
        get_live_out_vars())
    return set(), gimoe__qgy


ir_utils.copy_propagate_extensions[Join] = get_copies_join


def apply_copies_join(join_node, var_dict, name_var_table, typemap,
    calltypes, save_copies):
    join_node.set_live_left_vars([replace_vars_inner(mqg__sii, var_dict) for
        mqg__sii in join_node.get_live_left_vars()])
    join_node.set_live_right_vars([replace_vars_inner(mqg__sii, var_dict) for
        mqg__sii in join_node.get_live_right_vars()])
    join_node.set_live_out_data_vars([replace_vars_inner(mqg__sii, var_dict
        ) for mqg__sii in join_node.get_live_out_vars()])
    if join_node.how == 'cross':
        join_node.left_len_var = replace_vars_inner(join_node.left_len_var,
            var_dict)
        join_node.right_len_var = replace_vars_inner(join_node.
            right_len_var, var_dict)


ir_utils.apply_copy_propagate_extensions[Join] = apply_copies_join


def build_join_definitions(join_node, definitions=None):
    if definitions is None:
        definitions = defaultdict(list)
    for clirp__cyzt in join_node.get_live_out_vars():
        definitions[clirp__cyzt.name].append(join_node)
    return definitions


ir_utils.build_defs_extensions[Join] = build_join_definitions


def _gen_cross_join_len(join_node, out_table_type, typemap, calltypes,
    typingctx, targetctx, left_parallel, right_parallel):
    func_text = 'def f(left_len, right_len):\n'
    gii__uqeny = 'bodo.libs.distributed_api.get_size()'
    otfy__kgq = 'bodo.libs.distributed_api.get_rank()'
    if left_parallel:
        func_text += f"""  left_len = bodo.libs.distributed_api.get_node_portion(left_len, {gii__uqeny}, {otfy__kgq})
"""
    if right_parallel and not left_parallel:
        func_text += f"""  right_len = bodo.libs.distributed_api.get_node_portion(right_len, {gii__uqeny}, {otfy__kgq})
"""
    func_text += '  n_rows = left_len * right_len\n'
    func_text += '  py_table = init_table(py_table_type, False)\n'
    func_text += '  py_table = set_table_len(py_table, n_rows)\n'
    gybh__bhhv = {}
    exec(func_text, {}, gybh__bhhv)
    hlvna__vxpbl = gybh__bhhv['f']
    glbs = {'py_table_type': out_table_type, 'init_table': bodo.hiframes.
        table.init_table, 'set_table_len': bodo.hiframes.table.
        set_table_len, 'sum_op': np.int32(bodo.libs.distributed_api.
        Reduce_Type.Sum.value), 'bodo': bodo}
    rkktd__akr = [join_node.left_len_var, join_node.right_len_var]
    bkm__xlydw = tuple(typemap[onai__qwj.name] for onai__qwj in rkktd__akr)
    urrap__shgxz = compile_to_numba_ir(hlvna__vxpbl, glbs, typingctx=
        typingctx, targetctx=targetctx, arg_typs=bkm__xlydw, typemap=
        typemap, calltypes=calltypes).blocks.popitem()[1]
    replace_arg_nodes(urrap__shgxz, rkktd__akr)
    nqiz__csj = urrap__shgxz.body[:-3]
    nqiz__csj[-1].target = join_node.out_data_vars[0]
    return nqiz__csj


def _gen_cross_join_repeat(join_node, out_table_type, typemap, calltypes,
    typingctx, targetctx, left_parallel, right_parallel, left_is_dead):
    wzpdo__owlbh = (join_node.right_vars if left_is_dead else join_node.
        left_vars)
    mgcku__cyr = ', '.join(f't{nqs__wnvyf}' for nqs__wnvyf in range(len(
        wzpdo__owlbh)) if wzpdo__owlbh[nqs__wnvyf] is not None)
    xcnjg__yww = len(join_node.right_col_names) if left_is_dead else len(
        join_node.left_col_names)
    ygn__vbv = (join_node.is_right_table if left_is_dead else join_node.
        is_left_table)
    rdhdf__eky = (join_node.right_dead_var_inds if left_is_dead else
        join_node.left_dead_var_inds)
    zvr__fhzaq = [(f'get_table_data(t0, {nqs__wnvyf})' if ygn__vbv else
        f't{nqs__wnvyf}') for nqs__wnvyf in range(xcnjg__yww)]
    zbg__qirln = ', '.join(
        f'bodo.libs.array_kernels.repeat_kernel({zvr__fhzaq[nqs__wnvyf]}, repeats)'
         if nqs__wnvyf not in rdhdf__eky else 'None' for nqs__wnvyf in
        range(xcnjg__yww))
    kmve__shmbj = len(out_table_type.arr_types)
    xyqmh__yjihg = [join_node.out_to_input_col_map.get(nqs__wnvyf, (-1, -1)
        )[1] for nqs__wnvyf in range(kmve__shmbj)]
    gii__uqeny = 'bodo.libs.distributed_api.get_size()'
    otfy__kgq = 'bodo.libs.distributed_api.get_rank()'
    pljx__gfig = 'left_len' if left_is_dead else 'right_len'
    vbdbo__flcae = right_parallel if left_is_dead else left_parallel
    flvhp__ebnqz = left_parallel if left_is_dead else right_parallel
    zxpbx__rrgg = not vbdbo__flcae and flvhp__ebnqz
    qzx__cvgx = (
        f'bodo.libs.distributed_api.get_node_portion({pljx__gfig}, {gii__uqeny}, {otfy__kgq})'
         if zxpbx__rrgg else pljx__gfig)
    func_text = f'def f({mgcku__cyr}, left_len, right_len):\n'
    func_text += f'  repeats = {qzx__cvgx}\n'
    func_text += f'  out_data = ({zbg__qirln},)\n'
    func_text += f"""  py_table = logical_table_to_table(out_data, (), col_inds, {xcnjg__yww}, out_table_type, used_cols)
"""
    gybh__bhhv = {}
    exec(func_text, {}, gybh__bhhv)
    hlvna__vxpbl = gybh__bhhv['f']
    glbs = {'out_table_type': out_table_type, 'sum_op': np.int32(bodo.libs.
        distributed_api.Reduce_Type.Sum.value), 'bodo': bodo, 'used_cols':
        bodo.utils.typing.MetaType(tuple(join_node.out_used_cols)),
        'col_inds': bodo.utils.typing.MetaType(tuple(xyqmh__yjihg)),
        'logical_table_to_table': bodo.hiframes.table.
        logical_table_to_table, 'get_table_data': bodo.hiframes.table.
        get_table_data}
    rkktd__akr = [onai__qwj for onai__qwj in wzpdo__owlbh if onai__qwj is not
        None] + [join_node.left_len_var, join_node.right_len_var]
    bkm__xlydw = tuple(typemap[onai__qwj.name] for onai__qwj in rkktd__akr)
    urrap__shgxz = compile_to_numba_ir(hlvna__vxpbl, glbs, typingctx=
        typingctx, targetctx=targetctx, arg_typs=bkm__xlydw, typemap=
        typemap, calltypes=calltypes).blocks.popitem()[1]
    replace_arg_nodes(urrap__shgxz, rkktd__akr)
    nqiz__csj = urrap__shgxz.body[:-3]
    nqiz__csj[-1].target = join_node.out_data_vars[0]
    return nqiz__csj


def join_distributed_run(join_node, array_dists, typemap, calltypes,
    typingctx, targetctx):
    if bodo.user_logging.get_verbose_level() >= 2:
        kvi__ykw = join_node.loc.strformat()
        fgjn__grgtz = [join_node.left_col_names[nqs__wnvyf] for nqs__wnvyf in
            sorted(set(range(len(join_node.left_col_names))) - join_node.
            left_dead_var_inds)]
        qfsow__hxyj = """Finished column elimination on join's left input:
%s
Left input columns: %s
"""
        bodo.user_logging.log_message('Column Pruning', qfsow__hxyj,
            kvi__ykw, fgjn__grgtz)
        pucyt__jmrsq = [join_node.right_col_names[nqs__wnvyf] for
            nqs__wnvyf in sorted(set(range(len(join_node.right_col_names))) -
            join_node.right_dead_var_inds)]
        qfsow__hxyj = """Finished column elimination on join's right input:
%s
Right input columns: %s
"""
        bodo.user_logging.log_message('Column Pruning', qfsow__hxyj,
            kvi__ykw, pucyt__jmrsq)
        lhds__ilw = [join_node.out_col_names[nqs__wnvyf] for nqs__wnvyf in
            sorted(join_node.get_out_table_used_cols())]
        qfsow__hxyj = (
            'Finished column pruning on join node:\n%s\nOutput columns: %s\n')
        bodo.user_logging.log_message('Column Pruning', qfsow__hxyj,
            kvi__ykw, lhds__ilw)
    left_parallel, right_parallel = False, False
    if array_dists is not None:
        left_parallel, right_parallel = _get_table_parallel_flags(join_node,
            array_dists)
    jxzl__afeal = len(join_node.left_keys)
    out_physical_to_logical_list = []
    if join_node.has_live_out_table_var:
        out_table_type = typemap[join_node.get_out_table_var().name]
    else:
        out_table_type = types.none
    if join_node.has_live_out_index_var:
        index_col_type = typemap[join_node.get_out_index_var().name]
    else:
        index_col_type = types.none
    if _is_cross_join_len(join_node):
        return _gen_cross_join_len(join_node, out_table_type, typemap,
            calltypes, typingctx, targetctx, left_parallel, right_parallel)
    elif join_node.how == 'cross' and all(nqs__wnvyf in join_node.
        left_dead_var_inds for nqs__wnvyf in range(len(join_node.
        left_col_names))):
        return _gen_cross_join_repeat(join_node, out_table_type, typemap,
            calltypes, typingctx, targetctx, left_parallel, right_parallel,
            True)
    elif join_node.how == 'cross' and all(nqs__wnvyf in join_node.
        right_dead_var_inds for nqs__wnvyf in range(len(join_node.
        right_col_names))):
        return _gen_cross_join_repeat(join_node, out_table_type, typemap,
            calltypes, typingctx, targetctx, left_parallel, right_parallel,
            False)
    if join_node.extra_data_col_num != -1:
        out_physical_to_logical_list.append(join_node.extra_data_col_num)
    left_key_in_output = []
    right_key_in_output = []
    left_used_key_nums = set()
    right_used_key_nums = set()
    fgd__olbjy = set()
    nsmfz__bsx = set()
    left_logical_physical_map = {}
    right_logical_physical_map = {}
    left_physical_to_logical_list = []
    right_physical_to_logical_list = []
    jtbof__twjf = 0
    ezvnk__ryjv = 0
    gtnxq__elugy = []
    for seyd__vry, upfi__vxqr in enumerate(join_node.left_keys):
        qyi__jslt = join_node.left_var_map[upfi__vxqr]
        if not join_node.is_left_table:
            gtnxq__elugy.append(join_node.left_vars[qyi__jslt])
        nhwf__yuzg = 1
        fuy__dzyls = join_node.left_to_output_map[qyi__jslt]
        if upfi__vxqr == INDEX_SENTINEL:
            if (join_node.has_live_out_index_var and join_node.index_source ==
                'left' and join_node.index_col_num == qyi__jslt):
                out_physical_to_logical_list.append(fuy__dzyls)
                left_used_key_nums.add(seyd__vry)
                fgd__olbjy.add(qyi__jslt)
            else:
                nhwf__yuzg = 0
        elif fuy__dzyls not in join_node.out_used_cols:
            nhwf__yuzg = 0
        elif qyi__jslt in fgd__olbjy:
            nhwf__yuzg = 0
        else:
            left_used_key_nums.add(seyd__vry)
            fgd__olbjy.add(qyi__jslt)
            out_physical_to_logical_list.append(fuy__dzyls)
        left_physical_to_logical_list.append(qyi__jslt)
        left_logical_physical_map[qyi__jslt] = jtbof__twjf
        jtbof__twjf += 1
        left_key_in_output.append(nhwf__yuzg)
    gtnxq__elugy = tuple(gtnxq__elugy)
    wpcsv__swvlv = []
    for nqs__wnvyf in range(len(join_node.left_col_names)):
        if (nqs__wnvyf not in join_node.left_dead_var_inds and nqs__wnvyf
             not in join_node.left_key_set):
            if not join_node.is_left_table:
                onai__qwj = join_node.left_vars[nqs__wnvyf]
                wpcsv__swvlv.append(onai__qwj)
            eltyy__nhqzb = 1
            eylkk__spg = 1
            fuy__dzyls = join_node.left_to_output_map[nqs__wnvyf]
            if nqs__wnvyf in join_node.left_cond_cols:
                if fuy__dzyls not in join_node.out_used_cols:
                    eltyy__nhqzb = 0
                left_key_in_output.append(eltyy__nhqzb)
            elif nqs__wnvyf in join_node.left_dead_var_inds:
                eltyy__nhqzb = 0
                eylkk__spg = 0
            if eltyy__nhqzb:
                out_physical_to_logical_list.append(fuy__dzyls)
            if eylkk__spg:
                left_physical_to_logical_list.append(nqs__wnvyf)
                left_logical_physical_map[nqs__wnvyf] = jtbof__twjf
                jtbof__twjf += 1
    if (join_node.has_live_out_index_var and join_node.index_source ==
        'left' and join_node.index_col_num not in join_node.left_key_set):
        if not join_node.is_left_table:
            wpcsv__swvlv.append(join_node.left_vars[join_node.index_col_num])
        fuy__dzyls = join_node.left_to_output_map[join_node.index_col_num]
        out_physical_to_logical_list.append(fuy__dzyls)
        left_physical_to_logical_list.append(join_node.index_col_num)
    wpcsv__swvlv = tuple(wpcsv__swvlv)
    if join_node.is_left_table:
        wpcsv__swvlv = tuple(join_node.get_live_left_vars())
    biptt__aju = []
    for seyd__vry, upfi__vxqr in enumerate(join_node.right_keys):
        qyi__jslt = join_node.right_var_map[upfi__vxqr]
        if not join_node.is_right_table:
            biptt__aju.append(join_node.right_vars[qyi__jslt])
        if not join_node.vect_same_key[seyd__vry] and not join_node.is_join:
            nhwf__yuzg = 1
            if qyi__jslt not in join_node.right_to_output_map:
                nhwf__yuzg = 0
            else:
                fuy__dzyls = join_node.right_to_output_map[qyi__jslt]
                if upfi__vxqr == INDEX_SENTINEL:
                    if (join_node.has_live_out_index_var and join_node.
                        index_source == 'right' and join_node.index_col_num ==
                        qyi__jslt):
                        out_physical_to_logical_list.append(fuy__dzyls)
                        right_used_key_nums.add(seyd__vry)
                        nsmfz__bsx.add(qyi__jslt)
                    else:
                        nhwf__yuzg = 0
                elif fuy__dzyls not in join_node.out_used_cols:
                    nhwf__yuzg = 0
                elif qyi__jslt in nsmfz__bsx:
                    nhwf__yuzg = 0
                else:
                    right_used_key_nums.add(seyd__vry)
                    nsmfz__bsx.add(qyi__jslt)
                    out_physical_to_logical_list.append(fuy__dzyls)
            right_key_in_output.append(nhwf__yuzg)
        right_physical_to_logical_list.append(qyi__jslt)
        right_logical_physical_map[qyi__jslt] = ezvnk__ryjv
        ezvnk__ryjv += 1
    biptt__aju = tuple(biptt__aju)
    vsbtz__jwwba = []
    for nqs__wnvyf in range(len(join_node.right_col_names)):
        if (nqs__wnvyf not in join_node.right_dead_var_inds and nqs__wnvyf
             not in join_node.right_key_set):
            if not join_node.is_right_table:
                vsbtz__jwwba.append(join_node.right_vars[nqs__wnvyf])
            eltyy__nhqzb = 1
            eylkk__spg = 1
            fuy__dzyls = join_node.right_to_output_map[nqs__wnvyf]
            if nqs__wnvyf in join_node.right_cond_cols:
                if fuy__dzyls not in join_node.out_used_cols:
                    eltyy__nhqzb = 0
                right_key_in_output.append(eltyy__nhqzb)
            elif nqs__wnvyf in join_node.right_dead_var_inds:
                eltyy__nhqzb = 0
                eylkk__spg = 0
            if eltyy__nhqzb:
                out_physical_to_logical_list.append(fuy__dzyls)
            if eylkk__spg:
                right_physical_to_logical_list.append(nqs__wnvyf)
                right_logical_physical_map[nqs__wnvyf] = ezvnk__ryjv
                ezvnk__ryjv += 1
    if (join_node.has_live_out_index_var and join_node.index_source ==
        'right' and join_node.index_col_num not in join_node.right_key_set):
        if not join_node.is_right_table:
            vsbtz__jwwba.append(join_node.right_vars[join_node.index_col_num])
        fuy__dzyls = join_node.right_to_output_map[join_node.index_col_num]
        out_physical_to_logical_list.append(fuy__dzyls)
        right_physical_to_logical_list.append(join_node.index_col_num)
    vsbtz__jwwba = tuple(vsbtz__jwwba)
    if join_node.is_right_table:
        vsbtz__jwwba = tuple(join_node.get_live_right_vars())
    if join_node.indicator_col_num != -1:
        out_physical_to_logical_list.append(join_node.indicator_col_num)
    rkktd__akr = gtnxq__elugy + biptt__aju + wpcsv__swvlv + vsbtz__jwwba
    bkm__xlydw = tuple(typemap[onai__qwj.name] for onai__qwj in rkktd__akr)
    left_other_names = tuple('t1_c' + str(nqs__wnvyf) for nqs__wnvyf in
        range(len(wpcsv__swvlv)))
    right_other_names = tuple('t2_c' + str(nqs__wnvyf) for nqs__wnvyf in
        range(len(vsbtz__jwwba)))
    if join_node.is_left_table:
        lnuts__wqrf = ()
    else:
        lnuts__wqrf = tuple('t1_key' + str(nqs__wnvyf) for nqs__wnvyf in
            range(jxzl__afeal))
    if join_node.is_right_table:
        qkog__siypk = ()
    else:
        qkog__siypk = tuple('t2_key' + str(nqs__wnvyf) for nqs__wnvyf in
            range(jxzl__afeal))
    glbs = {}
    loc = join_node.loc
    func_text = 'def f({}):\n'.format(','.join(lnuts__wqrf + qkog__siypk +
        left_other_names + right_other_names))
    if join_node.is_left_table:
        left_key_types = []
        left_other_types = []
        if join_node.has_live_left_table_var:
            rbmev__fuy = typemap[join_node.left_vars[0].name]
        else:
            rbmev__fuy = types.none
        for whfu__drnhs in left_physical_to_logical_list:
            if whfu__drnhs < join_node.n_left_table_cols:
                assert join_node.has_live_left_table_var, 'No logical columns should refer to a dead table'
                hcdgw__kvtt = rbmev__fuy.arr_types[whfu__drnhs]
            else:
                hcdgw__kvtt = typemap[join_node.left_vars[-1].name]
            if whfu__drnhs in join_node.left_key_set:
                left_key_types.append(hcdgw__kvtt)
            else:
                left_other_types.append(hcdgw__kvtt)
        left_key_types = tuple(left_key_types)
        left_other_types = tuple(left_other_types)
    else:
        left_key_types = tuple(typemap[onai__qwj.name] for onai__qwj in
            gtnxq__elugy)
        left_other_types = tuple([typemap[upfi__vxqr.name] for upfi__vxqr in
            wpcsv__swvlv])
    if join_node.is_right_table:
        right_key_types = []
        right_other_types = []
        if join_node.has_live_right_table_var:
            rbmev__fuy = typemap[join_node.right_vars[0].name]
        else:
            rbmev__fuy = types.none
        for whfu__drnhs in right_physical_to_logical_list:
            if whfu__drnhs < join_node.n_right_table_cols:
                assert join_node.has_live_right_table_var, 'No logical columns should refer to a dead table'
                hcdgw__kvtt = rbmev__fuy.arr_types[whfu__drnhs]
            else:
                hcdgw__kvtt = typemap[join_node.right_vars[-1].name]
            if whfu__drnhs in join_node.right_key_set:
                right_key_types.append(hcdgw__kvtt)
            else:
                right_other_types.append(hcdgw__kvtt)
        right_key_types = tuple(right_key_types)
        right_other_types = tuple(right_other_types)
    else:
        right_key_types = tuple(typemap[onai__qwj.name] for onai__qwj in
            biptt__aju)
        right_other_types = tuple([typemap[upfi__vxqr.name] for upfi__vxqr in
            vsbtz__jwwba])
    matched_key_types = []
    for nqs__wnvyf in range(jxzl__afeal):
        yfqgo__mqae = _match_join_key_types(left_key_types[nqs__wnvyf],
            right_key_types[nqs__wnvyf], loc)
        glbs[f'key_type_{nqs__wnvyf}'] = yfqgo__mqae
        matched_key_types.append(yfqgo__mqae)
    if join_node.is_left_table:
        oqtm__mlwi = determine_table_cast_map(matched_key_types,
            left_key_types, None, {nqs__wnvyf: join_node.left_var_map[
            mhdxl__hhx] for nqs__wnvyf, mhdxl__hhx in enumerate(join_node.
            left_keys)}, True)
        if oqtm__mlwi:
            fer__yeee = False
            szls__ipmxt = False
            kksb__ults = None
            if join_node.has_live_left_table_var:
                udjn__hfbse = list(typemap[join_node.left_vars[0].name].
                    arr_types)
            else:
                udjn__hfbse = None
            for mnjxt__mqf, hcdgw__kvtt in oqtm__mlwi.items():
                if mnjxt__mqf < join_node.n_left_table_cols:
                    assert join_node.has_live_left_table_var, 'Casting columns for a dead table should not occur'
                    udjn__hfbse[mnjxt__mqf] = hcdgw__kvtt
                    fer__yeee = True
                else:
                    kksb__ults = hcdgw__kvtt
                    szls__ipmxt = True
            if fer__yeee:
                func_text += f"""    {left_other_names[0]} = bodo.utils.table_utils.table_astype({left_other_names[0]}, left_cast_table_type, False, _bodo_nan_to_str=False, used_cols=left_used_cols)
"""
                glbs['left_cast_table_type'] = TableType(tuple(udjn__hfbse))
                glbs['left_used_cols'] = MetaType(tuple(sorted(set(range(
                    join_node.n_left_table_cols)) - join_node.
                    left_dead_var_inds)))
            if szls__ipmxt:
                func_text += f"""    {left_other_names[1]} = bodo.utils.utils.astype({left_other_names[1]}, left_cast_index_type)
"""
                glbs['left_cast_index_type'] = kksb__ults
    else:
        func_text += '    t1_keys = ({}{})\n'.format(', '.join(
            f'bodo.utils.utils.astype({lnuts__wqrf[nqs__wnvyf]}, key_type_{nqs__wnvyf})'
             if left_key_types[nqs__wnvyf] != matched_key_types[nqs__wnvyf]
             else f'{lnuts__wqrf[nqs__wnvyf]}' for nqs__wnvyf in range(
            jxzl__afeal)), ',' if jxzl__afeal != 0 else '')
        func_text += '    data_left = ({}{})\n'.format(','.join(
            left_other_names), ',' if len(left_other_names) != 0 else '')
    if join_node.is_right_table:
        oqtm__mlwi = determine_table_cast_map(matched_key_types,
            right_key_types, None, {nqs__wnvyf: join_node.right_var_map[
            mhdxl__hhx] for nqs__wnvyf, mhdxl__hhx in enumerate(join_node.
            right_keys)}, True)
        if oqtm__mlwi:
            fer__yeee = False
            szls__ipmxt = False
            kksb__ults = None
            if join_node.has_live_right_table_var:
                udjn__hfbse = list(typemap[join_node.right_vars[0].name].
                    arr_types)
            else:
                udjn__hfbse = None
            for mnjxt__mqf, hcdgw__kvtt in oqtm__mlwi.items():
                if mnjxt__mqf < join_node.n_right_table_cols:
                    assert join_node.has_live_right_table_var, 'Casting columns for a dead table should not occur'
                    udjn__hfbse[mnjxt__mqf] = hcdgw__kvtt
                    fer__yeee = True
                else:
                    kksb__ults = hcdgw__kvtt
                    szls__ipmxt = True
            if fer__yeee:
                func_text += f"""    {right_other_names[0]} = bodo.utils.table_utils.table_astype({right_other_names[0]}, right_cast_table_type, False, _bodo_nan_to_str=False, used_cols=right_used_cols)
"""
                glbs['right_cast_table_type'] = TableType(tuple(udjn__hfbse))
                glbs['right_used_cols'] = MetaType(tuple(sorted(set(range(
                    join_node.n_right_table_cols)) - join_node.
                    right_dead_var_inds)))
            if szls__ipmxt:
                func_text += f"""    {right_other_names[1]} = bodo.utils.utils.astype({right_other_names[1]}, left_cast_index_type)
"""
                glbs['right_cast_index_type'] = kksb__ults
    else:
        func_text += '    t2_keys = ({}{})\n'.format(', '.join(
            f'bodo.utils.utils.astype({qkog__siypk[nqs__wnvyf]}, key_type_{nqs__wnvyf})'
             if right_key_types[nqs__wnvyf] != matched_key_types[nqs__wnvyf
            ] else f'{qkog__siypk[nqs__wnvyf]}' for nqs__wnvyf in range(
            jxzl__afeal)), ',' if jxzl__afeal != 0 else '')
        func_text += '    data_right = ({}{})\n'.format(','.join(
            right_other_names), ',' if len(right_other_names) != 0 else '')
    general_cond_cfunc, left_col_nums, right_col_nums = (
        _gen_general_cond_cfunc(join_node, typemap,
        left_logical_physical_map, right_logical_physical_map))
    if join_node.how == 'asof':
        if left_parallel or right_parallel:
            assert left_parallel and right_parallel, 'pd.merge_asof requires both left and right to be replicated or distributed'
            func_text += """    t2_keys, data_right = parallel_asof_comm(t1_keys, t2_keys, data_right)
"""
        func_text += """    out_t1_keys, out_t2_keys, out_data_left, out_data_right = bodo.ir.join.local_merge_asof(t1_keys, t2_keys, data_left, data_right)
"""
    else:
        func_text += _gen_join_cpp_call(join_node, left_key_types,
            right_key_types, matched_key_types, left_other_names,
            right_other_names, left_other_types, right_other_types,
            left_key_in_output, right_key_in_output, left_parallel,
            right_parallel, glbs, out_physical_to_logical_list,
            out_table_type, index_col_type, join_node.
            get_out_table_used_cols(), left_used_key_nums,
            right_used_key_nums, general_cond_cfunc, left_col_nums,
            right_col_nums, left_physical_to_logical_list,
            right_physical_to_logical_list)
    if join_node.how == 'asof':
        for nqs__wnvyf in range(len(left_other_names)):
            func_text += '    left_{} = out_data_left[{}]\n'.format(nqs__wnvyf,
                nqs__wnvyf)
        for nqs__wnvyf in range(len(right_other_names)):
            func_text += '    right_{} = out_data_right[{}]\n'.format(
                nqs__wnvyf, nqs__wnvyf)
        for nqs__wnvyf in range(jxzl__afeal):
            func_text += (
                f'    t1_keys_{nqs__wnvyf} = out_t1_keys[{nqs__wnvyf}]\n')
        for nqs__wnvyf in range(jxzl__afeal):
            func_text += (
                f'    t2_keys_{nqs__wnvyf} = out_t2_keys[{nqs__wnvyf}]\n')
    gybh__bhhv = {}
    exec(func_text, {}, gybh__bhhv)
    hlvna__vxpbl = gybh__bhhv['f']
    glbs.update({'bodo': bodo, 'np': np, 'pd': pd, 'parallel_asof_comm':
        parallel_asof_comm, 'array_to_info': array_to_info,
        'arr_info_list_to_table': arr_info_list_to_table,
        'cross_join_table': cross_join_table, 'hash_join_table':
        hash_join_table, 'delete_table': delete_table,
        'add_join_gen_cond_cfunc_sym': add_join_gen_cond_cfunc_sym,
        'get_join_cond_addr': get_join_cond_addr, 'key_in_output': np.array
        (left_key_in_output + right_key_in_output, dtype=np.bool_),
        'py_data_to_cpp_table': py_data_to_cpp_table,
        'cpp_table_to_py_data': cpp_table_to_py_data})
    if general_cond_cfunc:
        glbs.update({'general_cond_cfunc': general_cond_cfunc})
    urrap__shgxz = compile_to_numba_ir(hlvna__vxpbl, glbs, typingctx=
        typingctx, targetctx=targetctx, arg_typs=bkm__xlydw, typemap=
        typemap, calltypes=calltypes).blocks.popitem()[1]
    replace_arg_nodes(urrap__shgxz, rkktd__akr)
    nqiz__csj = urrap__shgxz.body[:-3]
    if join_node.has_live_out_index_var:
        nqiz__csj[-1].target = join_node.out_data_vars[1]
    if join_node.has_live_out_table_var:
        nqiz__csj[-2].target = join_node.out_data_vars[0]
    assert join_node.has_live_out_index_var or join_node.has_live_out_table_var, 'At most one of table and index should be dead if the Join IR node is live'
    if not join_node.has_live_out_index_var:
        nqiz__csj.pop(-1)
    elif not join_node.has_live_out_table_var:
        nqiz__csj.pop(-2)
    return nqiz__csj


distributed_pass.distributed_run_extensions[Join] = join_distributed_run


def _gen_general_cond_cfunc(join_node, typemap, left_logical_physical_map,
    right_logical_physical_map):
    expr = join_node.gen_cond_expr
    if not expr:
        return None, [], []
    mtfdz__apg = next_label()
    table_getitem_funcs = {'bodo': bodo, 'numba': numba, 'is_null_pointer':
        is_null_pointer}
    na_check_name = 'NOT_NA'
    func_text = f"""def bodo_join_gen_cond{mtfdz__apg}(left_table, right_table, left_data1, right_data1, left_null_bitmap, right_null_bitmap, left_ind, right_ind):
"""
    func_text += '  if is_null_pointer(left_table):\n'
    func_text += '    return False\n'
    expr, func_text, left_col_nums = _replace_column_accesses(expr,
        left_logical_physical_map, join_node.left_var_map, typemap,
        join_node.left_vars, table_getitem_funcs, func_text, 'left',
        join_node.left_key_set, na_check_name, join_node.is_left_table)
    expr, func_text, right_col_nums = _replace_column_accesses(expr,
        right_logical_physical_map, join_node.right_var_map, typemap,
        join_node.right_vars, table_getitem_funcs, func_text, 'right',
        join_node.right_key_set, na_check_name, join_node.is_right_table)
    expr = expr.replace(' & ', ' and ').replace(' | ', ' or ')
    func_text += f'  return {expr}'
    gybh__bhhv = {}
    exec(func_text, table_getitem_funcs, gybh__bhhv)
    itsbg__eynj = gybh__bhhv[f'bodo_join_gen_cond{mtfdz__apg}']
    esyc__kjgp = types.bool_(types.voidptr, types.voidptr, types.voidptr,
        types.voidptr, types.voidptr, types.voidptr, types.int64, types.int64)
    eltir__hrz = numba.cfunc(esyc__kjgp, nopython=True)(itsbg__eynj)
    join_gen_cond_cfunc[eltir__hrz.native_name] = eltir__hrz
    join_gen_cond_cfunc_addr[eltir__hrz.native_name] = eltir__hrz.address
    return eltir__hrz, left_col_nums, right_col_nums


def _replace_column_accesses(expr, logical_to_physical_ind, name_to_var_map,
    typemap, col_vars, table_getitem_funcs, func_text, table_name, key_set,
    na_check_name, is_table_var):
    kqn__klo = []
    for upfi__vxqr, dfuzx__yng in name_to_var_map.items():
        zrju__jjcky = f'({table_name}.{upfi__vxqr})'
        if zrju__jjcky not in expr:
            continue
        sykq__btuw = f'getitem_{table_name}_val_{dfuzx__yng}'
        if is_table_var:
            pxicm__vapum = typemap[col_vars[0].name].arr_types[dfuzx__yng]
        else:
            pxicm__vapum = typemap[col_vars[dfuzx__yng].name]
        if is_str_arr_type(pxicm__vapum
            ) or pxicm__vapum == bodo.binary_array_type:
            qffql__xvnk = (
                f'{sykq__btuw}({table_name}_table, {table_name}_ind)\n')
        else:
            qffql__xvnk = (
                f'{sykq__btuw}({table_name}_data1, {table_name}_ind)\n')
        azr__ombl = logical_to_physical_ind[dfuzx__yng]
        table_getitem_funcs[sykq__btuw
            ] = bodo.libs.array._gen_row_access_intrinsic(pxicm__vapum,
            azr__ombl)
        expr = expr.replace(zrju__jjcky, qffql__xvnk)
        pvykr__gyu = f'({na_check_name}.{table_name}.{upfi__vxqr})'
        if pvykr__gyu in expr:
            ykmk__bwdey = f'nacheck_{table_name}_val_{dfuzx__yng}'
            kjm__rnhl = f'_bodo_isna_{table_name}_val_{dfuzx__yng}'
            if isinstance(pxicm__vapum, (bodo.libs.int_arr_ext.
                IntegerArrayType, bodo.FloatingArrayType, bodo.TimeArrayType)
                ) or pxicm__vapum in (bodo.libs.bool_arr_ext.boolean_array,
                bodo.binary_array_type, bodo.datetime_date_array_type
                ) or is_str_arr_type(pxicm__vapum):
                func_text += f"""  {kjm__rnhl} = {ykmk__bwdey}({table_name}_null_bitmap, {table_name}_ind)
"""
            else:
                func_text += f"""  {kjm__rnhl} = {ykmk__bwdey}({table_name}_data1, {table_name}_ind)
"""
            table_getitem_funcs[ykmk__bwdey
                ] = bodo.libs.array._gen_row_na_check_intrinsic(pxicm__vapum,
                azr__ombl)
            expr = expr.replace(pvykr__gyu, kjm__rnhl)
        if dfuzx__yng not in key_set:
            kqn__klo.append(azr__ombl)
    return expr, func_text, kqn__klo


def _match_join_key_types(t1, t2, loc):
    if t1 == t2:
        return t1
    if is_str_arr_type(t1) and is_str_arr_type(t2):
        return bodo.string_array_type
    try:
        arr = dtype_to_array_type(find_common_np_dtype([t1, t2]))
        return to_nullable_type(arr) if is_nullable_type(t1
            ) or is_nullable_type(t2) else arr
    except Exception as fva__bejb:
        raise BodoError(f'Join key types {t1} and {t2} do not match', loc=loc)


def _get_table_parallel_flags(join_node, array_dists):
    yab__lqv = (distributed_pass.Distribution.OneD, distributed_pass.
        Distribution.OneD_Var)
    left_parallel = all(array_dists[onai__qwj.name] in yab__lqv for
        onai__qwj in join_node.get_live_left_vars())
    if not join_node.get_live_left_vars():
        assert join_node.how == 'cross', 'cross join expected if left data is dead'
        left_parallel = join_node.left_dist in yab__lqv
    right_parallel = all(array_dists[onai__qwj.name] in yab__lqv for
        onai__qwj in join_node.get_live_right_vars())
    if not join_node.get_live_right_vars():
        assert join_node.how == 'cross', 'cross join expected if right data is dead'
        right_parallel = join_node.right_dist in yab__lqv
    if not left_parallel:
        assert not any(array_dists[onai__qwj.name] in yab__lqv for
            onai__qwj in join_node.get_live_left_vars())
    if not right_parallel:
        assert not any(array_dists[onai__qwj.name] in yab__lqv for
            onai__qwj in join_node.get_live_right_vars())
    if left_parallel or right_parallel:
        assert all(array_dists[onai__qwj.name] in yab__lqv for onai__qwj in
            join_node.get_live_out_vars())
    return left_parallel, right_parallel


def _gen_join_cpp_call(join_node, left_key_types, right_key_types,
    matched_key_types, left_other_names, right_other_names,
    left_other_types, right_other_types, left_key_in_output,
    right_key_in_output, left_parallel, right_parallel, glbs,
    out_physical_to_logical_list, out_table_type, index_col_type,
    out_table_used_cols, left_used_key_nums, right_used_key_nums,
    general_cond_cfunc, left_col_nums, right_col_nums,
    left_physical_to_logical_list, right_physical_to_logical_list):

    def needs_typechange(in_type, need_nullable, is_same_key):
        return isinstance(in_type, types.Array) and not is_dtype_nullable(
            in_type.dtype) and need_nullable and not is_same_key
    zcmmf__lrfu = set(left_col_nums)
    ojjej__srpuy = set(right_col_nums)
    ehz__mazj = join_node.vect_same_key
    jfgrl__rasw = []
    for nqs__wnvyf in range(len(left_key_types)):
        if left_key_in_output[nqs__wnvyf]:
            jfgrl__rasw.append(needs_typechange(matched_key_types[
                nqs__wnvyf], join_node.is_right, ehz__mazj[nqs__wnvyf]))
    vglzs__afm = len(left_key_types)
    jskq__zklru = 0
    ngco__dxo = left_physical_to_logical_list[len(left_key_types):]
    for nqs__wnvyf, whfu__drnhs in enumerate(ngco__dxo):
        see__kid = True
        if whfu__drnhs in zcmmf__lrfu:
            see__kid = left_key_in_output[vglzs__afm]
            vglzs__afm += 1
        if see__kid:
            jfgrl__rasw.append(needs_typechange(left_other_types[nqs__wnvyf
                ], join_node.is_right, False))
    for nqs__wnvyf in range(len(right_key_types)):
        if not ehz__mazj[nqs__wnvyf] and not join_node.is_join:
            if right_key_in_output[jskq__zklru]:
                jfgrl__rasw.append(needs_typechange(matched_key_types[
                    nqs__wnvyf], join_node.is_left, False))
            jskq__zklru += 1
    jau__qvgyr = right_physical_to_logical_list[len(right_key_types):]
    for nqs__wnvyf, whfu__drnhs in enumerate(jau__qvgyr):
        see__kid = True
        if whfu__drnhs in ojjej__srpuy:
            see__kid = right_key_in_output[jskq__zklru]
            jskq__zklru += 1
        if see__kid:
            jfgrl__rasw.append(needs_typechange(right_other_types[
                nqs__wnvyf], join_node.is_left, False))
    jxzl__afeal = len(left_key_types)
    func_text = '    # beginning of _gen_join_cpp_call\n'
    if join_node.is_left_table:
        if join_node.has_live_left_table_var:
            pnm__oignx = left_other_names[1:]
            glwg__idztn = left_other_names[0]
        else:
            pnm__oignx = left_other_names
            glwg__idztn = None
        ieijn__zhi = '()' if len(pnm__oignx) == 0 else f'({pnm__oignx[0]},)'
        func_text += f"""    table_left = py_data_to_cpp_table({glwg__idztn}, {ieijn__zhi}, left_in_cols, {join_node.n_left_table_cols})
"""
        glbs['left_in_cols'] = MetaType(tuple(left_physical_to_logical_list))
    else:
        xapg__qoo = []
        for nqs__wnvyf in range(jxzl__afeal):
            xapg__qoo.append('t1_keys[{}]'.format(nqs__wnvyf))
        for nqs__wnvyf in range(len(left_other_names)):
            xapg__qoo.append('data_left[{}]'.format(nqs__wnvyf))
        func_text += '    info_list_total_l = [{}]\n'.format(','.join(
            'array_to_info({})'.format(pjz__sojgm) for pjz__sojgm in xapg__qoo)
            )
        func_text += (
            '    table_left = arr_info_list_to_table(info_list_total_l)\n')
    if join_node.is_right_table:
        if join_node.has_live_right_table_var:
            rneco__oekz = right_other_names[1:]
            glwg__idztn = right_other_names[0]
        else:
            rneco__oekz = right_other_names
            glwg__idztn = None
        ieijn__zhi = '()' if len(rneco__oekz) == 0 else f'({rneco__oekz[0]},)'
        func_text += f"""    table_right = py_data_to_cpp_table({glwg__idztn}, {ieijn__zhi}, right_in_cols, {join_node.n_right_table_cols})
"""
        glbs['right_in_cols'] = MetaType(tuple(right_physical_to_logical_list))
    else:
        ehpdw__ylw = []
        for nqs__wnvyf in range(jxzl__afeal):
            ehpdw__ylw.append('t2_keys[{}]'.format(nqs__wnvyf))
        for nqs__wnvyf in range(len(right_other_names)):
            ehpdw__ylw.append('data_right[{}]'.format(nqs__wnvyf))
        func_text += '    info_list_total_r = [{}]\n'.format(','.join(
            'array_to_info({})'.format(pjz__sojgm) for pjz__sojgm in
            ehpdw__ylw))
        func_text += (
            '    table_right = arr_info_list_to_table(info_list_total_r)\n')
    glbs['vect_same_key'] = np.array(ehz__mazj, dtype=np.int64)
    glbs['use_nullable_arr_type'] = np.array(jfgrl__rasw, dtype=np.int64)
    glbs['left_table_cond_columns'] = np.array(left_col_nums if len(
        left_col_nums) > 0 else [-1], dtype=np.int64)
    glbs['right_table_cond_columns'] = np.array(right_col_nums if len(
        right_col_nums) > 0 else [-1], dtype=np.int64)
    if general_cond_cfunc:
        func_text += f"""    cfunc_cond = add_join_gen_cond_cfunc_sym(general_cond_cfunc, '{general_cond_cfunc.native_name}')
"""
        func_text += (
            f"    cfunc_cond = get_join_cond_addr('{general_cond_cfunc.native_name}')\n"
            )
    else:
        func_text += '    cfunc_cond = 0\n'
    func_text += f'    total_rows_np = np.array([0], dtype=np.int64)\n'
    if join_node.how == 'cross' or not join_node.left_keys:
        func_text += f"""    out_table = cross_join_table(table_left, table_right, {left_parallel}, {right_parallel}, {join_node.is_left}, {join_node.is_right}, key_in_output.ctypes, use_nullable_arr_type.ctypes, cfunc_cond, left_table_cond_columns.ctypes, {len(left_col_nums)}, right_table_cond_columns.ctypes, {len(right_col_nums)}, total_rows_np.ctypes)
"""
    else:
        func_text += f"""    out_table = hash_join_table(table_left, table_right, {left_parallel}, {right_parallel}, {jxzl__afeal}, {len(ngco__dxo)}, {len(jau__qvgyr)}, vect_same_key.ctypes, key_in_output.ctypes, use_nullable_arr_type.ctypes, {join_node.is_left}, {join_node.is_right}, {join_node.is_join}, {join_node.extra_data_col_num != -1}, {join_node.indicator_col_num != -1}, {join_node.is_na_equal}, cfunc_cond, left_table_cond_columns.ctypes, {len(left_col_nums)}, right_table_cond_columns.ctypes, {len(right_col_nums)}, total_rows_np.ctypes)
"""
    func_text += '    delete_table(table_left)\n'
    func_text += '    delete_table(table_right)\n'
    hajq__jbik = '(py_table_type, index_col_type)'
    func_text += f"""    out_data = cpp_table_to_py_data(out_table, out_col_inds, {hajq__jbik}, total_rows_np[0], {join_node.n_out_table_cols})
"""
    if join_node.has_live_out_table_var:
        func_text += f'    T = out_data[0]\n'
    else:
        func_text += f'    T = None\n'
    if join_node.has_live_out_index_var:
        xzjl__vhfgh = 1 if join_node.has_live_out_table_var else 0
        func_text += f'    index_var = out_data[{xzjl__vhfgh}]\n'
    else:
        func_text += f'    index_var = None\n'
    glbs['py_table_type'] = out_table_type
    glbs['index_col_type'] = index_col_type
    glbs['out_col_inds'] = MetaType(tuple(out_physical_to_logical_list))
    if bool(join_node.out_used_cols) or index_col_type != types.none:
        func_text += '    delete_table(out_table)\n'
    if out_table_type != types.none:
        iihcm__argr = {}
        for nqs__wnvyf, mhdxl__hhx in enumerate(join_node.left_keys):
            if nqs__wnvyf in left_used_key_nums:
                pysln__moq = join_node.left_var_map[mhdxl__hhx]
                iihcm__argr[nqs__wnvyf] = join_node.left_to_output_map[
                    pysln__moq]
        oqtm__mlwi = determine_table_cast_map(matched_key_types,
            left_key_types, left_used_key_nums, iihcm__argr, False)
        jdqoi__nnj = {}
        for nqs__wnvyf, mhdxl__hhx in enumerate(join_node.right_keys):
            if nqs__wnvyf in right_used_key_nums:
                pysln__moq = join_node.right_var_map[mhdxl__hhx]
                jdqoi__nnj[nqs__wnvyf] = join_node.right_to_output_map[
                    pysln__moq]
        oqtm__mlwi.update(determine_table_cast_map(matched_key_types,
            right_key_types, right_used_key_nums, jdqoi__nnj, False))
        fer__yeee = False
        szls__ipmxt = False
        if join_node.has_live_out_table_var:
            udjn__hfbse = list(out_table_type.arr_types)
        else:
            udjn__hfbse = None
        for mnjxt__mqf, hcdgw__kvtt in oqtm__mlwi.items():
            if mnjxt__mqf < join_node.n_out_table_cols:
                assert join_node.has_live_out_table_var, 'Casting columns for a dead table should not occur'
                udjn__hfbse[mnjxt__mqf] = hcdgw__kvtt
                fer__yeee = True
            else:
                kksb__ults = hcdgw__kvtt
                szls__ipmxt = True
        if fer__yeee:
            func_text += f"""    T = bodo.utils.table_utils.table_astype(T, cast_table_type, False, _bodo_nan_to_str=False, used_cols=used_cols)
"""
            hnlre__sldu = bodo.TableType(tuple(udjn__hfbse))
            glbs['py_table_type'] = hnlre__sldu
            glbs['cast_table_type'] = out_table_type
            glbs['used_cols'] = MetaType(tuple(out_table_used_cols))
        if szls__ipmxt:
            glbs['index_col_type'] = kksb__ults
            glbs['index_cast_type'] = index_col_type
            func_text += (
                f'    index_var = bodo.utils.utils.astype(index_var, index_cast_type)\n'
                )
    func_text += f'    out_table = T\n'
    func_text += f'    out_index = index_var\n'
    return func_text


def determine_table_cast_map(matched_key_types: List[types.Type], key_types:
    List[types.Type], used_key_nums: Optional[Set[int]], output_map: Dict[
    int, int], convert_dict_col: bool):
    oqtm__mlwi: Dict[int, types.Type] = {}
    jxzl__afeal = len(matched_key_types)
    for nqs__wnvyf in range(jxzl__afeal):
        if used_key_nums is None or nqs__wnvyf in used_key_nums:
            if matched_key_types[nqs__wnvyf] != key_types[nqs__wnvyf] and (
                convert_dict_col or key_types[nqs__wnvyf] != bodo.
                dict_str_arr_type):
                xzjl__vhfgh = output_map[nqs__wnvyf]
                oqtm__mlwi[xzjl__vhfgh] = matched_key_types[nqs__wnvyf]
    return oqtm__mlwi


@numba.njit
def parallel_asof_comm(left_key_arrs, right_key_arrs, right_data):
    gii__uqeny = bodo.libs.distributed_api.get_size()
    quidw__haft = np.empty(gii__uqeny, left_key_arrs[0].dtype)
    dbfsk__njn = np.empty(gii__uqeny, left_key_arrs[0].dtype)
    bodo.libs.distributed_api.allgather(quidw__haft, left_key_arrs[0][0])
    bodo.libs.distributed_api.allgather(dbfsk__njn, left_key_arrs[0][-1])
    qqajp__hgcp = np.zeros(gii__uqeny, np.int32)
    fhbd__mpm = np.zeros(gii__uqeny, np.int32)
    kplu__szc = np.zeros(gii__uqeny, np.int32)
    tqow__xclo = right_key_arrs[0][0]
    wkv__sij = right_key_arrs[0][-1]
    jmlgx__eoe = -1
    nqs__wnvyf = 0
    while nqs__wnvyf < gii__uqeny - 1 and dbfsk__njn[nqs__wnvyf] < tqow__xclo:
        nqs__wnvyf += 1
    while nqs__wnvyf < gii__uqeny and quidw__haft[nqs__wnvyf] <= wkv__sij:
        jmlgx__eoe, cixgp__cgzz = _count_overlap(right_key_arrs[0],
            quidw__haft[nqs__wnvyf], dbfsk__njn[nqs__wnvyf])
        if jmlgx__eoe != 0:
            jmlgx__eoe -= 1
            cixgp__cgzz += 1
        qqajp__hgcp[nqs__wnvyf] = cixgp__cgzz
        fhbd__mpm[nqs__wnvyf] = jmlgx__eoe
        nqs__wnvyf += 1
    while nqs__wnvyf < gii__uqeny:
        qqajp__hgcp[nqs__wnvyf] = 1
        fhbd__mpm[nqs__wnvyf] = len(right_key_arrs[0]) - 1
        nqs__wnvyf += 1
    bodo.libs.distributed_api.alltoall(qqajp__hgcp, kplu__szc, 1)
    ign__rclgo = kplu__szc.sum()
    affh__cmc = np.empty(ign__rclgo, right_key_arrs[0].dtype)
    yikj__nzcr = alloc_arr_tup(ign__rclgo, right_data)
    ucwaz__raceg = bodo.ir.join.calc_disp(kplu__szc)
    bodo.libs.distributed_api.alltoallv(right_key_arrs[0], affh__cmc,
        qqajp__hgcp, kplu__szc, fhbd__mpm, ucwaz__raceg)
    bodo.libs.distributed_api.alltoallv_tup(right_data, yikj__nzcr,
        qqajp__hgcp, kplu__szc, fhbd__mpm, ucwaz__raceg)
    return (affh__cmc,), yikj__nzcr


@numba.njit
def _count_overlap(r_key_arr, start, end):
    cixgp__cgzz = 0
    jmlgx__eoe = 0
    qgg__qyfph = 0
    while qgg__qyfph < len(r_key_arr) and r_key_arr[qgg__qyfph] < start:
        jmlgx__eoe += 1
        qgg__qyfph += 1
    while qgg__qyfph < len(r_key_arr) and start <= r_key_arr[qgg__qyfph
        ] <= end:
        qgg__qyfph += 1
        cixgp__cgzz += 1
    return jmlgx__eoe, cixgp__cgzz


import llvmlite.binding as ll
from bodo.libs import hdist
ll.add_symbol('c_alltoallv', hdist.c_alltoallv)


@numba.njit
def calc_disp(arr):
    pgj__eafn = np.empty_like(arr)
    pgj__eafn[0] = 0
    for nqs__wnvyf in range(1, len(arr)):
        pgj__eafn[nqs__wnvyf] = pgj__eafn[nqs__wnvyf - 1] + arr[nqs__wnvyf - 1]
    return pgj__eafn


@numba.njit
def local_merge_asof(left_keys, right_keys, data_left, data_right):
    catz__csus = len(left_keys[0])
    irqtc__cwzsb = len(right_keys[0])
    byehf__jdxwp = alloc_arr_tup(catz__csus, left_keys)
    lwinh__pqhsv = alloc_arr_tup(catz__csus, right_keys)
    qmzkt__ysed = alloc_arr_tup(catz__csus, data_left)
    fhluq__adqxw = alloc_arr_tup(catz__csus, data_right)
    tnpxe__njly = 0
    ktd__lgoe = 0
    for tnpxe__njly in range(catz__csus):
        if ktd__lgoe < 0:
            ktd__lgoe = 0
        while ktd__lgoe < irqtc__cwzsb and getitem_arr_tup(right_keys,
            ktd__lgoe) <= getitem_arr_tup(left_keys, tnpxe__njly):
            ktd__lgoe += 1
        ktd__lgoe -= 1
        setitem_arr_tup(byehf__jdxwp, tnpxe__njly, getitem_arr_tup(
            left_keys, tnpxe__njly))
        setitem_arr_tup(qmzkt__ysed, tnpxe__njly, getitem_arr_tup(data_left,
            tnpxe__njly))
        if ktd__lgoe >= 0:
            setitem_arr_tup(lwinh__pqhsv, tnpxe__njly, getitem_arr_tup(
                right_keys, ktd__lgoe))
            setitem_arr_tup(fhluq__adqxw, tnpxe__njly, getitem_arr_tup(
                data_right, ktd__lgoe))
        else:
            bodo.libs.array_kernels.setna_tup(lwinh__pqhsv, tnpxe__njly)
            bodo.libs.array_kernels.setna_tup(fhluq__adqxw, tnpxe__njly)
    return byehf__jdxwp, lwinh__pqhsv, qmzkt__ysed, fhluq__adqxw
