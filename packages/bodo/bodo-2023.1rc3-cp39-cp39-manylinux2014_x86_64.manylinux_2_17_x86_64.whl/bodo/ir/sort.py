"""IR node for the data sorting"""
from collections import defaultdict
from typing import List, Set, Tuple, Union
import numba
import numpy as np
from numba.core import ir, ir_utils, typeinfer, types
from numba.core.ir_utils import compile_to_numba_ir, mk_unique_var, replace_arg_nodes, replace_vars_inner, visit_vars_inner
import bodo
from bodo.libs.array import arr_info_list_to_table, array_to_info, cpp_table_to_py_data, delete_table, delete_table_decref_arrays, info_from_table, info_to_array, py_data_to_cpp_table, sort_values_table
from bodo.transforms import distributed_analysis, distributed_pass
from bodo.transforms.distributed_analysis import Distribution
from bodo.transforms.table_column_del_pass import _compute_table_column_uses, _find_used_columns, ir_extension_table_column_use, remove_dead_column_extensions
from bodo.utils.typing import MetaType, is_overload_none, type_has_unknown_cats
from bodo.utils.utils import gen_getitem


class Sort(ir.Stmt):

    def __init__(self, df_in: str, df_out: str, in_vars: List[ir.Var],
        out_vars: List[ir.Var], key_inds: Tuple[int], inplace: bool, loc:
        ir.Loc, ascending_list: Union[List[bool], bool]=True, na_position:
        Union[List[str], str]='last', _bodo_chunk_bounds: Union[ir.Var,
        None]=None, is_table_format: bool=False, num_table_arrays: int=0):
        self.df_in = df_in
        self.df_out = df_out
        self.in_vars = in_vars
        self.out_vars = out_vars
        self.key_inds = key_inds
        self.inplace = inplace
        self._bodo_chunk_bounds = _bodo_chunk_bounds
        self.is_table_format = is_table_format
        self.num_table_arrays = num_table_arrays
        self.dead_var_inds: Set[int] = set()
        self.dead_key_var_inds: Set[int] = set()
        if isinstance(na_position, str):
            if na_position == 'last':
                self.na_position_b = (True,) * len(key_inds)
            else:
                self.na_position_b = (False,) * len(key_inds)
        else:
            self.na_position_b = tuple([(True if izro__oiaop == 'last' else
                False) for izro__oiaop in na_position])
        if isinstance(ascending_list, bool):
            ascending_list = (ascending_list,) * len(key_inds)
        self.ascending_list = ascending_list
        self.loc = loc

    def get_live_in_vars(self):
        return [upu__zrv for upu__zrv in self.in_vars if upu__zrv is not None]

    def get_live_out_vars(self):
        return [upu__zrv for upu__zrv in self.out_vars if upu__zrv is not None]

    def __repr__(self):
        ccsku__rcab = ', '.join(upu__zrv.name for upu__zrv in self.
            get_live_in_vars())
        bwsqu__sxmbm = f'{self.df_in}{{{ccsku__rcab}}}'
        rral__njsi = ', '.join(upu__zrv.name for upu__zrv in self.
            get_live_out_vars())
        cylpb__utihs = f'{self.df_out}{{{rral__njsi}}}'
        return f'Sort (keys: {self.key_inds}): {bwsqu__sxmbm} {cylpb__utihs}'


def sort_array_analysis(sort_node, equiv_set, typemap, array_analysis):
    zjwgx__irm = []
    for ngrf__ncp in sort_node.get_live_in_vars():
        nkk__mqbs = equiv_set.get_shape(ngrf__ncp)
        if nkk__mqbs is not None:
            zjwgx__irm.append(nkk__mqbs[0])
    if len(zjwgx__irm) > 1:
        equiv_set.insert_equiv(*zjwgx__irm)
    eyf__nxfd = []
    zjwgx__irm = []
    for ngrf__ncp in sort_node.get_live_out_vars():
        kat__nje = typemap[ngrf__ncp.name]
        kmjel__kosrz = array_analysis._gen_shape_call(equiv_set, ngrf__ncp,
            kat__nje.ndim, None, eyf__nxfd)
        equiv_set.insert_equiv(ngrf__ncp, kmjel__kosrz)
        zjwgx__irm.append(kmjel__kosrz[0])
        equiv_set.define(ngrf__ncp, set())
    if len(zjwgx__irm) > 1:
        equiv_set.insert_equiv(*zjwgx__irm)
    return [], eyf__nxfd


numba.parfors.array_analysis.array_analysis_extensions[Sort
    ] = sort_array_analysis


def sort_distributed_analysis(sort_node, array_dists):
    aova__lfx = sort_node.get_live_in_vars()
    ttbw__jntj = sort_node.get_live_out_vars()
    exjw__ehco = Distribution.OneD
    for ngrf__ncp in aova__lfx:
        exjw__ehco = Distribution(min(exjw__ehco.value, array_dists[
            ngrf__ncp.name].value))
    qqok__stf = Distribution(min(exjw__ehco.value, Distribution.OneD_Var.value)
        )
    for ngrf__ncp in ttbw__jntj:
        if ngrf__ncp.name in array_dists:
            qqok__stf = Distribution(min(qqok__stf.value, array_dists[
                ngrf__ncp.name].value))
    if qqok__stf != Distribution.OneD_Var:
        exjw__ehco = qqok__stf
    for ngrf__ncp in aova__lfx:
        array_dists[ngrf__ncp.name] = exjw__ehco
    for ngrf__ncp in ttbw__jntj:
        array_dists[ngrf__ncp.name] = qqok__stf


distributed_analysis.distributed_analysis_extensions[Sort
    ] = sort_distributed_analysis


def sort_typeinfer(sort_node, typeinferer):
    for efec__lsh, jcrb__gudtx in enumerate(sort_node.out_vars):
        vysyo__suhgh = sort_node.in_vars[efec__lsh]
        if vysyo__suhgh is not None and jcrb__gudtx is not None:
            typeinferer.constraints.append(typeinfer.Propagate(dst=
                jcrb__gudtx.name, src=vysyo__suhgh.name, loc=sort_node.loc))


typeinfer.typeinfer_extensions[Sort] = sort_typeinfer


def build_sort_definitions(sort_node, definitions=None):
    if definitions is None:
        definitions = defaultdict(list)
    if not sort_node.inplace:
        for ngrf__ncp in sort_node.get_live_out_vars():
            definitions[ngrf__ncp.name].append(sort_node)
    return definitions


ir_utils.build_defs_extensions[Sort] = build_sort_definitions


def visit_vars_sort(sort_node, callback, cbdata):
    for efec__lsh in range(len(sort_node.in_vars)):
        if sort_node.in_vars[efec__lsh] is not None:
            sort_node.in_vars[efec__lsh] = visit_vars_inner(sort_node.
                in_vars[efec__lsh], callback, cbdata)
        if sort_node.out_vars[efec__lsh] is not None:
            sort_node.out_vars[efec__lsh] = visit_vars_inner(sort_node.
                out_vars[efec__lsh], callback, cbdata)
    if sort_node._bodo_chunk_bounds is not None:
        sort_node._bodo_chunk_bounds = visit_vars_inner(sort_node.
            _bodo_chunk_bounds, callback, cbdata)


ir_utils.visit_vars_extensions[Sort] = visit_vars_sort


def remove_dead_sort(sort_node, lives_no_aliases, lives, arg_aliases,
    alias_map, func_ir, typemap):
    if sort_node.is_table_format:
        mnx__ycvcl = sort_node.out_vars[0]
        if mnx__ycvcl is not None and mnx__ycvcl.name not in lives:
            sort_node.out_vars[0] = None
            dead_cols = set(range(sort_node.num_table_arrays))
            udzvl__rcblk = set(sort_node.key_inds)
            sort_node.dead_key_var_inds.update(dead_cols & udzvl__rcblk)
            sort_node.dead_var_inds.update(dead_cols - udzvl__rcblk)
            if len(udzvl__rcblk & dead_cols) == 0:
                sort_node.in_vars[0] = None
        for efec__lsh in range(1, len(sort_node.out_vars)):
            upu__zrv = sort_node.out_vars[efec__lsh]
            if upu__zrv is not None and upu__zrv.name not in lives:
                sort_node.out_vars[efec__lsh] = None
                hlk__onck = sort_node.num_table_arrays + efec__lsh - 1
                if hlk__onck in sort_node.key_inds:
                    sort_node.dead_key_var_inds.add(hlk__onck)
                else:
                    sort_node.dead_var_inds.add(hlk__onck)
                    sort_node.in_vars[efec__lsh] = None
    else:
        for efec__lsh in range(len(sort_node.out_vars)):
            upu__zrv = sort_node.out_vars[efec__lsh]
            if upu__zrv is not None and upu__zrv.name not in lives:
                sort_node.out_vars[efec__lsh] = None
                if efec__lsh in sort_node.key_inds:
                    sort_node.dead_key_var_inds.add(efec__lsh)
                else:
                    sort_node.dead_var_inds.add(efec__lsh)
                    sort_node.in_vars[efec__lsh] = None
    if all(upu__zrv is None for upu__zrv in sort_node.out_vars):
        return None
    return sort_node


ir_utils.remove_dead_extensions[Sort] = remove_dead_sort


def sort_usedefs(sort_node, use_set=None, def_set=None):
    if use_set is None:
        use_set = set()
    if def_set is None:
        def_set = set()
    use_set.update({upu__zrv.name for upu__zrv in sort_node.get_live_in_vars()}
        )
    if not sort_node.inplace:
        def_set.update({upu__zrv.name for upu__zrv in sort_node.
            get_live_out_vars()})
    if sort_node._bodo_chunk_bounds is not None:
        use_set.add(sort_node._bodo_chunk_bounds.name)
    return numba.core.analysis._use_defs_result(usemap=use_set, defmap=def_set)


numba.core.analysis.ir_extension_usedefs[Sort] = sort_usedefs


def get_copies_sort(sort_node, typemap):
    lugu__pfx = set()
    if not sort_node.inplace:
        lugu__pfx.update({upu__zrv.name for upu__zrv in sort_node.
            get_live_out_vars()})
    return set(), lugu__pfx


ir_utils.copy_propagate_extensions[Sort] = get_copies_sort


def apply_copies_sort(sort_node, var_dict, name_var_table, typemap,
    calltypes, save_copies):
    for efec__lsh in range(len(sort_node.in_vars)):
        if sort_node.in_vars[efec__lsh] is not None:
            sort_node.in_vars[efec__lsh] = replace_vars_inner(sort_node.
                in_vars[efec__lsh], var_dict)
        if sort_node.out_vars[efec__lsh] is not None:
            sort_node.out_vars[efec__lsh] = replace_vars_inner(sort_node.
                out_vars[efec__lsh], var_dict)
    if sort_node._bodo_chunk_bounds is not None:
        sort_node._bodo_chunk_bounds = replace_vars_inner(sort_node.
            _bodo_chunk_bounds, var_dict)


ir_utils.apply_copy_propagate_extensions[Sort] = apply_copies_sort


def sort_distributed_run(sort_node, array_dists, typemap, calltypes,
    typingctx, targetctx):
    parallel = False
    in_vars = sort_node.get_live_in_vars()
    out_vars = sort_node.get_live_out_vars()
    if array_dists is not None:
        parallel = True
        for upu__zrv in (in_vars + out_vars):
            if array_dists[upu__zrv.name
                ] != distributed_pass.Distribution.OneD and array_dists[
                upu__zrv.name] != distributed_pass.Distribution.OneD_Var:
                parallel = False
    nodes = []
    if not sort_node.inplace:
        ixqdd__czmdx = []
        for upu__zrv in in_vars:
            ila__uddxa = _copy_array_nodes(upu__zrv, nodes, typingctx,
                targetctx, typemap, calltypes, sort_node.dead_var_inds)
            ixqdd__czmdx.append(ila__uddxa)
        in_vars = ixqdd__czmdx
    out_types = [(typemap[upu__zrv.name] if upu__zrv is not None else types
        .none) for upu__zrv in sort_node.out_vars]
    bvfa__stw, vjhof__apral = get_sort_cpp_section(sort_node, out_types,
        typemap, parallel)
    ctnjg__xdcyg = {}
    exec(bvfa__stw, {}, ctnjg__xdcyg)
    ytvox__jehr = ctnjg__xdcyg['f']
    vjhof__apral.update({'bodo': bodo, 'np': np, 'delete_table':
        delete_table, 'delete_table_decref_arrays':
        delete_table_decref_arrays, 'info_to_array': info_to_array,
        'info_from_table': info_from_table, 'sort_values_table':
        sort_values_table, 'arr_info_list_to_table': arr_info_list_to_table,
        'array_to_info': array_to_info, 'py_data_to_cpp_table':
        py_data_to_cpp_table, 'cpp_table_to_py_data': cpp_table_to_py_data})
    vjhof__apral.update({f'out_type{efec__lsh}': out_types[efec__lsh] for
        efec__lsh in range(len(out_types))})
    qbmu__pebq = sort_node._bodo_chunk_bounds
    abm__uwgbp = qbmu__pebq
    if qbmu__pebq is None:
        loc = sort_node.loc
        abm__uwgbp = ir.Var(ir.Scope(None, loc), mk_unique_var(
            '$bounds_none'), loc)
        typemap[abm__uwgbp.name] = types.none
        nodes.append(ir.Assign(ir.Const(None, loc), abm__uwgbp, loc))
    ymbqy__egqp = compile_to_numba_ir(ytvox__jehr, vjhof__apral, typingctx=
        typingctx, targetctx=targetctx, arg_typs=tuple(typemap[upu__zrv.
        name] for upu__zrv in in_vars) + (typemap[abm__uwgbp.name],),
        typemap=typemap, calltypes=calltypes).blocks.popitem()[1]
    replace_arg_nodes(ymbqy__egqp, in_vars + [abm__uwgbp])
    haw__fauy = ymbqy__egqp.body[-2].value.value
    nodes += ymbqy__egqp.body[:-2]
    for efec__lsh, upu__zrv in enumerate(out_vars):
        gen_getitem(upu__zrv, haw__fauy, efec__lsh, calltypes, nodes)
    return nodes


distributed_pass.distributed_run_extensions[Sort] = sort_distributed_run


def _copy_array_nodes(var, nodes, typingctx, targetctx, typemap, calltypes,
    dead_cols):
    from bodo.hiframes.table import TableType
    gcgjo__vurn = lambda arr: arr.copy()
    dqtuc__gknuu = None
    if isinstance(typemap[var.name], TableType):
        okgt__sujlr = len(typemap[var.name].arr_types)
        dqtuc__gknuu = set(range(okgt__sujlr)) - dead_cols
        dqtuc__gknuu = MetaType(tuple(sorted(dqtuc__gknuu)))
        gcgjo__vurn = (lambda T: bodo.utils.table_utils.
            generate_mappable_table_func(T, 'copy', types.none, True,
            used_cols=_used_columns))
    ymbqy__egqp = compile_to_numba_ir(gcgjo__vurn, {'bodo': bodo, 'types':
        types, '_used_columns': dqtuc__gknuu}, typingctx=typingctx,
        targetctx=targetctx, arg_typs=(typemap[var.name],), typemap=typemap,
        calltypes=calltypes).blocks.popitem()[1]
    replace_arg_nodes(ymbqy__egqp, [var])
    nodes += ymbqy__egqp.body[:-2]
    return nodes[-1].target


def get_sort_cpp_section(sort_node, out_types, typemap, parallel):
    nbe__ulody = len(sort_node.key_inds)
    lpb__evgv = len(sort_node.in_vars)
    end__wolb = len(sort_node.out_vars)
    n_cols = (sort_node.num_table_arrays + lpb__evgv - 1 if sort_node.
        is_table_format else lpb__evgv)
    fparq__ftmx, vwe__grdm, peuei__sek = _get_cpp_col_ind_mappings(sort_node
        .key_inds, sort_node.dead_var_inds, sort_node.dead_key_var_inds, n_cols
        )
    lsgvf__sxds = []
    if sort_node.is_table_format:
        lsgvf__sxds.append('arg0')
        for efec__lsh in range(1, lpb__evgv):
            hlk__onck = sort_node.num_table_arrays + efec__lsh - 1
            if hlk__onck not in sort_node.dead_var_inds:
                lsgvf__sxds.append(f'arg{hlk__onck}')
    else:
        for efec__lsh in range(n_cols):
            if efec__lsh not in sort_node.dead_var_inds:
                lsgvf__sxds.append(f'arg{efec__lsh}')
    bvfa__stw = f"def f({', '.join(lsgvf__sxds)}, bounds_in):\n"
    if sort_node.is_table_format:
        dyi__udm = ',' if lpb__evgv - 1 == 1 else ''
        zzf__uuooc = []
        for efec__lsh in range(sort_node.num_table_arrays, n_cols):
            if efec__lsh in sort_node.dead_var_inds:
                zzf__uuooc.append('None')
            else:
                zzf__uuooc.append(f'arg{efec__lsh}')
        bvfa__stw += f"""  in_cpp_table = py_data_to_cpp_table(arg0, ({', '.join(zzf__uuooc)}{dyi__udm}), in_col_inds, {sort_node.num_table_arrays})
"""
    else:
        woqy__ked = {seewr__yiylt: efec__lsh for efec__lsh, seewr__yiylt in
            enumerate(fparq__ftmx)}
        ghu__ztp = [None] * len(fparq__ftmx)
        for efec__lsh in range(n_cols):
            ruok__uezkp = woqy__ked.get(efec__lsh, -1)
            if ruok__uezkp != -1:
                ghu__ztp[ruok__uezkp] = f'array_to_info(arg{efec__lsh})'
        bvfa__stw += '  info_list_total = [{}]\n'.format(','.join(ghu__ztp))
        bvfa__stw += (
            '  in_cpp_table = arr_info_list_to_table(info_list_total)\n')
    bvfa__stw += '  vect_ascending = np.array([{}], np.int64)\n'.format(','
        .join('1' if udhg__prqcj else '0' for udhg__prqcj in sort_node.
        ascending_list))
    bvfa__stw += '  na_position = np.array([{}], np.int64)\n'.format(','.
        join('1' if udhg__prqcj else '0' for udhg__prqcj in sort_node.
        na_position_b))
    bvfa__stw += '  dead_keys = np.array([{}], np.int64)\n'.format(','.join
        ('1' if efec__lsh in peuei__sek else '0' for efec__lsh in range(
        nbe__ulody)))
    bvfa__stw += f'  total_rows_np = np.array([0], dtype=np.int64)\n'
    nyuyh__qmigv = sort_node._bodo_chunk_bounds
    qzql__yagoy = '0' if nyuyh__qmigv is None or is_overload_none(typemap[
        nyuyh__qmigv.name]
        ) else 'arr_info_list_to_table([array_to_info(bounds_in)])'
    bvfa__stw += f"""  out_cpp_table = sort_values_table(in_cpp_table, {nbe__ulody}, vect_ascending.ctypes, na_position.ctypes, dead_keys.ctypes, total_rows_np.ctypes, {qzql__yagoy}, {parallel})
"""
    if sort_node.is_table_format:
        dyi__udm = ',' if end__wolb == 1 else ''
        yhea__own = (
            f"({', '.join(f'out_type{efec__lsh}' if not type_has_unknown_cats(out_types[efec__lsh]) else f'arg{efec__lsh}' for efec__lsh in range(end__wolb))}{dyi__udm})"
            )
        bvfa__stw += f"""  out_data = cpp_table_to_py_data(out_cpp_table, out_col_inds, {yhea__own}, total_rows_np[0], {sort_node.num_table_arrays})
"""
    else:
        woqy__ked = {seewr__yiylt: efec__lsh for efec__lsh, seewr__yiylt in
            enumerate(vwe__grdm)}
        ghu__ztp = []
        for efec__lsh in range(n_cols):
            ruok__uezkp = woqy__ked.get(efec__lsh, -1)
            if ruok__uezkp != -1:
                auev__tciw = (f'out_type{efec__lsh}' if not
                    type_has_unknown_cats(out_types[efec__lsh]) else
                    f'arg{efec__lsh}')
                bvfa__stw += f"""  out{efec__lsh} = info_to_array(info_from_table(out_cpp_table, {ruok__uezkp}), {auev__tciw})
"""
                ghu__ztp.append(f'out{efec__lsh}')
        dyi__udm = ',' if len(ghu__ztp) == 1 else ''
        gqcih__ysqb = f"({', '.join(ghu__ztp)}{dyi__udm})"
        bvfa__stw += f'  out_data = {gqcih__ysqb}\n'
    bvfa__stw += '  delete_table(out_cpp_table)\n'
    bvfa__stw += '  delete_table(in_cpp_table)\n'
    bvfa__stw += f'  return out_data\n'
    return bvfa__stw, {'in_col_inds': MetaType(tuple(fparq__ftmx)),
        'out_col_inds': MetaType(tuple(vwe__grdm))}


def _get_cpp_col_ind_mappings(key_inds, dead_var_inds, dead_key_var_inds,
    n_cols):
    fparq__ftmx = []
    vwe__grdm = []
    peuei__sek = []
    for seewr__yiylt, efec__lsh in enumerate(key_inds):
        fparq__ftmx.append(efec__lsh)
        if efec__lsh in dead_key_var_inds:
            peuei__sek.append(seewr__yiylt)
        else:
            vwe__grdm.append(efec__lsh)
    for efec__lsh in range(n_cols):
        if efec__lsh in dead_var_inds or efec__lsh in key_inds:
            continue
        fparq__ftmx.append(efec__lsh)
        vwe__grdm.append(efec__lsh)
    return fparq__ftmx, vwe__grdm, peuei__sek


def sort_table_column_use(sort_node, block_use_map, equiv_vars, typemap,
    table_col_use_map):
    if not sort_node.is_table_format or sort_node.in_vars[0
        ] is None or sort_node.out_vars[0] is None:
        return
    ykx__sqm = sort_node.in_vars[0].name
    dbrsa__bmue = sort_node.out_vars[0].name
    ljbq__edpuh, ukhk__fvys, sipw__ksmnn = block_use_map[ykx__sqm]
    if ukhk__fvys or sipw__ksmnn:
        return
    jhun__mcze, ote__lksb, ylr__zbdmc = _compute_table_column_uses(dbrsa__bmue,
        table_col_use_map, equiv_vars)
    xoal__uga = set(efec__lsh for efec__lsh in sort_node.key_inds if 
        efec__lsh < sort_node.num_table_arrays)
    block_use_map[ykx__sqm
        ] = ljbq__edpuh | jhun__mcze | xoal__uga, ote__lksb or ylr__zbdmc, False


ir_extension_table_column_use[Sort] = sort_table_column_use


def sort_remove_dead_column(sort_node, column_live_map, equiv_vars, typemap):
    if not sort_node.is_table_format or sort_node.out_vars[0] is None:
        return False
    okgt__sujlr = sort_node.num_table_arrays
    dbrsa__bmue = sort_node.out_vars[0].name
    dqtuc__gknuu = _find_used_columns(dbrsa__bmue, okgt__sujlr,
        column_live_map, equiv_vars)
    if dqtuc__gknuu is None:
        return False
    jbdeq__plo = set(range(okgt__sujlr)) - dqtuc__gknuu
    xoal__uga = set(efec__lsh for efec__lsh in sort_node.key_inds if 
        efec__lsh < okgt__sujlr)
    dffpi__ludcp = sort_node.dead_key_var_inds | jbdeq__plo & xoal__uga
    cvrc__cgea = sort_node.dead_var_inds | jbdeq__plo - xoal__uga
    myogd__wec = (dffpi__ludcp != sort_node.dead_key_var_inds) | (cvrc__cgea !=
        sort_node.dead_var_inds)
    sort_node.dead_key_var_inds = dffpi__ludcp
    sort_node.dead_var_inds = cvrc__cgea
    return myogd__wec


remove_dead_column_extensions[Sort] = sort_remove_dead_column
