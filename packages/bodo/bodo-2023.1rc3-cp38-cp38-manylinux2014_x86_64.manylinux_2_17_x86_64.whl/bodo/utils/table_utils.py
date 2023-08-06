"""File containing utility functions for supporting DataFrame operations with Table Format."""
from collections import defaultdict
from typing import Any, Dict, Set
import numba
import numpy as np
from numba.core import types
from numba.parfors.array_analysis import ArrayAnalysis
import bodo
from bodo.hiframes.table import TableType
from bodo.utils.typing import get_castable_arr_dtype, get_overload_const_bool, get_overload_const_str, is_overload_constant_bool, is_overload_constant_str, is_overload_false, is_overload_none, is_overload_true, raise_bodo_error


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def generate_mappable_table_func(table, func_name, out_arr_typ, is_method,
    used_cols=None):
    if not is_overload_constant_str(func_name) and not is_overload_none(
        func_name):
        raise_bodo_error(
            'generate_mappable_table_func(): func_name must be a constant string'
            )
    if not is_overload_constant_bool(is_method):
        raise_bodo_error(
            'generate_mappable_table_func(): is_method must be a constant boolean'
            )
    epwp__ylq = not is_overload_none(func_name)
    if epwp__ylq:
        func_name = get_overload_const_str(func_name)
        bkdov__afgt = get_overload_const_bool(is_method)
    luk__nrwgq = out_arr_typ.instance_type if isinstance(out_arr_typ, types
        .TypeRef) else out_arr_typ
    jaxki__djwe = luk__nrwgq == types.none
    vwu__dns = len(table.arr_types)
    if jaxki__djwe:
        bvgut__jhmdh = table
    else:
        rxek__pkv = tuple([luk__nrwgq] * vwu__dns)
        bvgut__jhmdh = TableType(rxek__pkv)
    vpl__wror = {'bodo': bodo, 'lst_dtype': luk__nrwgq, 'table_typ':
        bvgut__jhmdh}
    cuua__kytxp = (
        'def impl(table, func_name, out_arr_typ, is_method, used_cols=None):\n'
        )
    if jaxki__djwe:
        cuua__kytxp += (
            f'  out_table = bodo.hiframes.table.init_table(table, False)\n')
        cuua__kytxp += f'  l = len(table)\n'
    else:
        cuua__kytxp += f"""  out_list = bodo.hiframes.table.alloc_empty_list_type({vwu__dns}, lst_dtype)
"""
    if not is_overload_none(used_cols):
        ormf__mcg = used_cols.instance_type
        ejzdm__sib = np.array(ormf__mcg.meta, dtype=np.int64)
        vpl__wror['used_cols_glbl'] = ejzdm__sib
        uok__ufwa = set([table.block_nums[btq__xtpc] for btq__xtpc in
            ejzdm__sib])
        cuua__kytxp += f'  used_cols_set = set(used_cols_glbl)\n'
    else:
        cuua__kytxp += f'  used_cols_set = None\n'
        ejzdm__sib = None
    cuua__kytxp += (
        f'  bodo.hiframes.table.ensure_table_unboxed(table, used_cols_set)\n')
    for zigxa__byx in table.type_to_blk.values():
        cuua__kytxp += f"""  blk_{zigxa__byx} = bodo.hiframes.table.get_table_block(table, {zigxa__byx})
"""
        if jaxki__djwe:
            cuua__kytxp += f"""  out_list_{zigxa__byx} = bodo.hiframes.table.alloc_list_like(blk_{zigxa__byx}, len(blk_{zigxa__byx}), False)
"""
            dzyuo__wahm = f'out_list_{zigxa__byx}'
        else:
            dzyuo__wahm = 'out_list'
        if ejzdm__sib is None or zigxa__byx in uok__ufwa:
            cuua__kytxp += f'  for i in range(len(blk_{zigxa__byx})):\n'
            vpl__wror[f'col_indices_{zigxa__byx}'] = np.array(table.
                block_to_arr_ind[zigxa__byx], dtype=np.int64)
            cuua__kytxp += f'    col_loc = col_indices_{zigxa__byx}[i]\n'
            if ejzdm__sib is not None:
                cuua__kytxp += f'    if col_loc not in used_cols_set:\n'
                cuua__kytxp += f'        continue\n'
            if jaxki__djwe:
                pmes__imh = 'i'
            else:
                pmes__imh = 'col_loc'
            if not epwp__ylq:
                cuua__kytxp += (
                    f'    {dzyuo__wahm}[{pmes__imh}] = blk_{zigxa__byx}[i]\n')
            elif bkdov__afgt:
                cuua__kytxp += f"""    {dzyuo__wahm}[{pmes__imh}] = blk_{zigxa__byx}[i].{func_name}()
"""
            else:
                cuua__kytxp += f"""    {dzyuo__wahm}[{pmes__imh}] = {func_name}(blk_{zigxa__byx}[i])
"""
        if jaxki__djwe:
            cuua__kytxp += f"""  out_table = bodo.hiframes.table.set_table_block(out_table, {dzyuo__wahm}, {zigxa__byx})
"""
    if jaxki__djwe:
        cuua__kytxp += (
            f'  out_table = bodo.hiframes.table.set_table_len(out_table, l)\n')
        cuua__kytxp += '  return out_table\n'
    else:
        cuua__kytxp += """  return bodo.hiframes.table.init_table_from_lists((out_list,), table_typ)
"""
    bjq__xvzl = {}
    exec(cuua__kytxp, vpl__wror, bjq__xvzl)
    return bjq__xvzl['impl']


def generate_mappable_table_func_equiv(self, scope, equiv_set, loc, args, kws):
    jbvd__ymubw = args[0]
    if equiv_set.has_shape(jbvd__ymubw):
        return ArrayAnalysis.AnalyzeResult(shape=jbvd__ymubw, pre=[])
    return None


(ArrayAnalysis.
    _analyze_op_call_bodo_utils_table_utils_generate_mappable_table_func
    ) = generate_mappable_table_func_equiv


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def generate_table_nbytes(table, out_arr, start_offset, parallel=False):
    vpl__wror = {'bodo': bodo, 'sum_op': np.int32(bodo.libs.distributed_api
        .Reduce_Type.Sum.value)}
    cuua__kytxp = 'def impl(table, out_arr, start_offset, parallel=False):\n'
    cuua__kytxp += '  bodo.hiframes.table.ensure_table_unboxed(table, None)\n'
    for zigxa__byx in table.type_to_blk.values():
        cuua__kytxp += (
            f'  blk = bodo.hiframes.table.get_table_block(table, {zigxa__byx})\n'
            )
        vpl__wror[f'col_indices_{zigxa__byx}'] = np.array(table.
            block_to_arr_ind[zigxa__byx], dtype=np.int64)
        cuua__kytxp += '  for i in range(len(blk)):\n'
        cuua__kytxp += f'    col_loc = col_indices_{zigxa__byx}[i]\n'
        cuua__kytxp += '    out_arr[col_loc + start_offset] = blk[i].nbytes\n'
    cuua__kytxp += '  if parallel:\n'
    cuua__kytxp += '    for i in range(start_offset, len(out_arr)):\n'
    cuua__kytxp += (
        '      out_arr[i] = bodo.libs.distributed_api.dist_reduce(out_arr[i], sum_op)\n'
        )
    bjq__xvzl = {}
    exec(cuua__kytxp, vpl__wror, bjq__xvzl)
    return bjq__xvzl['impl']


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def table_concat(table, col_nums_meta, arr_type):
    arr_type = arr_type.instance_type if isinstance(arr_type, types.TypeRef
        ) else arr_type
    ttw__fgxx = table.type_to_blk[arr_type]
    vpl__wror: Dict[str, Any] = {'bodo': bodo}
    vpl__wror['col_indices'] = np.array(table.block_to_arr_ind[ttw__fgxx],
        dtype=np.int64)
    dhp__qlyl = col_nums_meta.instance_type
    vpl__wror['col_nums'] = np.array(dhp__qlyl.meta, np.int64)
    cuua__kytxp = 'def impl(table, col_nums_meta, arr_type):\n'
    cuua__kytxp += (
        f'  blk = bodo.hiframes.table.get_table_block(table, {ttw__fgxx})\n')
    cuua__kytxp += (
        '  col_num_to_ind_in_blk = {c : i for i, c in enumerate(col_indices)}\n'
        )
    cuua__kytxp += '  n = len(table)\n'
    oan__wdxe = arr_type == bodo.string_array_type
    if oan__wdxe:
        cuua__kytxp += '  total_chars = 0\n'
        cuua__kytxp += '  for c in col_nums:\n'
        cuua__kytxp += """    bodo.hiframes.table.ensure_column_unboxed(table, blk, col_num_to_ind_in_blk[c], c)
"""
        cuua__kytxp += '    arr = blk[col_num_to_ind_in_blk[c]]\n'
        cuua__kytxp += (
            '    total_chars += bodo.libs.str_arr_ext.num_total_chars(arr)\n')
        cuua__kytxp += """  out_arr = bodo.libs.str_arr_ext.pre_alloc_string_array(n * len(col_nums), total_chars)
"""
    else:
        cuua__kytxp += """  out_arr = bodo.utils.utils.alloc_type(n * len(col_nums), arr_type, (-1,))
"""
    cuua__kytxp += '  for i in range(len(col_nums)):\n'
    cuua__kytxp += '    c = col_nums[i]\n'
    if not oan__wdxe:
        cuua__kytxp += """    bodo.hiframes.table.ensure_column_unboxed(table, blk, col_num_to_ind_in_blk[c], c)
"""
    cuua__kytxp += '    arr = blk[col_num_to_ind_in_blk[c]]\n'
    cuua__kytxp += '    off = i * n\n'
    cuua__kytxp += '    for j in range(len(arr)):\n'
    cuua__kytxp += '      if bodo.libs.array_kernels.isna(arr, j):\n'
    cuua__kytxp += '        bodo.libs.array_kernels.setna(out_arr, off+j)\n'
    cuua__kytxp += '      else:\n'
    cuua__kytxp += '        out_arr[off+j] = arr[j]\n'
    cuua__kytxp += '  return out_arr\n'
    nnkoc__yxjwz = {}
    exec(cuua__kytxp, vpl__wror, nnkoc__yxjwz)
    yuaq__avq = nnkoc__yxjwz['impl']
    return yuaq__avq


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def table_astype(table, new_table_typ, copy, _bodo_nan_to_str, used_cols=None):
    new_table_typ = new_table_typ.instance_type
    ixccy__kwttn = not is_overload_false(copy)
    ukxhh__lcy = is_overload_true(copy)
    vpl__wror: Dict[str, Any] = {'bodo': bodo}
    fgone__ypcm = table.arr_types
    zxh__iwkgb = new_table_typ.arr_types
    czf__agp: Set[int] = set()
    lryx__yur: Dict[types.Type, Set[types.Type]] = defaultdict(set)
    ocsmv__czzv: Set[types.Type] = set()
    for btq__xtpc, jkpes__moxa in enumerate(fgone__ypcm):
        ydcg__vcb = zxh__iwkgb[btq__xtpc]
        if jkpes__moxa == ydcg__vcb:
            ocsmv__czzv.add(jkpes__moxa)
        else:
            czf__agp.add(btq__xtpc)
            lryx__yur[ydcg__vcb].add(jkpes__moxa)
    cuua__kytxp = (
        'def impl(table, new_table_typ, copy, _bodo_nan_to_str, used_cols=None):\n'
        )
    cuua__kytxp += (
        f'  out_table = bodo.hiframes.table.init_table(new_table_typ, False)\n'
        )
    cuua__kytxp += (
        f'  out_table = bodo.hiframes.table.set_table_len(out_table, len(table))\n'
        )
    ulrsx__tmnmn = set(range(len(fgone__ypcm)))
    mtj__hlq = ulrsx__tmnmn - czf__agp
    if not is_overload_none(used_cols):
        ormf__mcg = used_cols.instance_type
        puure__yeag = set(ormf__mcg.meta)
        czf__agp = czf__agp & puure__yeag
        mtj__hlq = mtj__hlq & puure__yeag
        uok__ufwa = set([table.block_nums[btq__xtpc] for btq__xtpc in
            puure__yeag])
    else:
        puure__yeag = None
    yjc__eghc = dict()
    for uarg__vckc in czf__agp:
        hdbv__wmie = table.block_nums[uarg__vckc]
        ujw__mghkq = new_table_typ.block_nums[uarg__vckc]
        if f'cast_cols_{hdbv__wmie}_{ujw__mghkq}' in yjc__eghc:
            yjc__eghc[f'cast_cols_{hdbv__wmie}_{ujw__mghkq}'].append(uarg__vckc
                )
        else:
            yjc__eghc[f'cast_cols_{hdbv__wmie}_{ujw__mghkq}'] = [uarg__vckc]
    for xue__colt in table.blk_to_type:
        for ujw__mghkq in new_table_typ.blk_to_type:
            ilu__ipnj = yjc__eghc.get(f'cast_cols_{xue__colt}_{ujw__mghkq}', []
                )
            vpl__wror[f'cast_cols_{xue__colt}_{ujw__mghkq}'] = np.array(list
                (ilu__ipnj), dtype=np.int64)
            cuua__kytxp += f"""  cast_cols_{xue__colt}_{ujw__mghkq}_set = set(cast_cols_{xue__colt}_{ujw__mghkq})
"""
    vpl__wror['copied_cols'] = np.array(list(mtj__hlq), dtype=np.int64)
    cuua__kytxp += f'  copied_cols_set = set(copied_cols)\n'
    for sik__nfvmk, wcet__pmsk in new_table_typ.type_to_blk.items():
        vpl__wror[f'typ_list_{wcet__pmsk}'] = types.List(sik__nfvmk)
        cuua__kytxp += f"""  out_arr_list_{wcet__pmsk} = bodo.hiframes.table.alloc_list_like(typ_list_{wcet__pmsk}, {len(new_table_typ.block_to_arr_ind[wcet__pmsk])}, False)
"""
        if sik__nfvmk in ocsmv__czzv:
            nkvne__bjo = table.type_to_blk[sik__nfvmk]
            if puure__yeag is None or nkvne__bjo in uok__ufwa:
                hroxu__owo = table.block_to_arr_ind[nkvne__bjo]
                lpzi__bxtl = [new_table_typ.block_offsets[tsuk__lsgy] for
                    tsuk__lsgy in hroxu__owo]
                vpl__wror[f'new_idx_{nkvne__bjo}'] = np.array(lpzi__bxtl,
                    np.int64)
                vpl__wror[f'orig_arr_inds_{nkvne__bjo}'] = np.array(hroxu__owo,
                    np.int64)
                cuua__kytxp += f"""  arr_list_{nkvne__bjo} = bodo.hiframes.table.get_table_block(table, {nkvne__bjo})
"""
                cuua__kytxp += (
                    f'  for i in range(len(arr_list_{nkvne__bjo})):\n')
                cuua__kytxp += (
                    f'    arr_ind_{nkvne__bjo} = orig_arr_inds_{nkvne__bjo}[i]\n'
                    )
                cuua__kytxp += (
                    f'    if arr_ind_{nkvne__bjo} not in copied_cols_set:\n')
                cuua__kytxp += f'      continue\n'
                cuua__kytxp += f"""    bodo.hiframes.table.ensure_column_unboxed(table, arr_list_{nkvne__bjo}, i, arr_ind_{nkvne__bjo})
"""
                cuua__kytxp += (
                    f'    out_idx_{wcet__pmsk}_{nkvne__bjo} = new_idx_{nkvne__bjo}[i]\n'
                    )
                cuua__kytxp += (
                    f'    arr_val_{nkvne__bjo} = arr_list_{nkvne__bjo}[i]\n')
                if ukxhh__lcy:
                    cuua__kytxp += (
                        f'    arr_val_{nkvne__bjo} = arr_val_{nkvne__bjo}.copy()\n'
                        )
                elif ixccy__kwttn:
                    cuua__kytxp += f"""    arr_val_{nkvne__bjo} = arr_val_{nkvne__bjo}.copy() if copy else arr_val_{wcet__pmsk}
"""
                cuua__kytxp += f"""    out_arr_list_{wcet__pmsk}[out_idx_{wcet__pmsk}_{nkvne__bjo}] = arr_val_{nkvne__bjo}
"""
    xrgbq__net = set()
    for sik__nfvmk, wcet__pmsk in new_table_typ.type_to_blk.items():
        if sik__nfvmk in lryx__yur:
            vpl__wror[f'typ_{wcet__pmsk}'] = get_castable_arr_dtype(sik__nfvmk)
            vke__aqn = lryx__yur[sik__nfvmk]
            for zgc__ajnrg in vke__aqn:
                nkvne__bjo = table.type_to_blk[zgc__ajnrg]
                if puure__yeag is None or nkvne__bjo in uok__ufwa:
                    if (zgc__ajnrg not in ocsmv__czzv and zgc__ajnrg not in
                        xrgbq__net):
                        hroxu__owo = table.block_to_arr_ind[nkvne__bjo]
                        lpzi__bxtl = [new_table_typ.block_offsets[
                            tsuk__lsgy] for tsuk__lsgy in hroxu__owo]
                        vpl__wror[f'new_idx_{nkvne__bjo}'] = np.array(
                            lpzi__bxtl, np.int64)
                        vpl__wror[f'orig_arr_inds_{nkvne__bjo}'] = np.array(
                            hroxu__owo, np.int64)
                        cuua__kytxp += f"""  arr_list_{nkvne__bjo} = bodo.hiframes.table.get_table_block(table, {nkvne__bjo})
"""
                    xrgbq__net.add(zgc__ajnrg)
                    cuua__kytxp += (
                        f'  for i in range(len(arr_list_{nkvne__bjo})):\n')
                    cuua__kytxp += (
                        f'    arr_ind_{nkvne__bjo} = orig_arr_inds_{nkvne__bjo}[i]\n'
                        )
                    cuua__kytxp += f"""    if arr_ind_{nkvne__bjo} not in cast_cols_{nkvne__bjo}_{wcet__pmsk}_set:
"""
                    cuua__kytxp += f'      continue\n'
                    cuua__kytxp += f"""    bodo.hiframes.table.ensure_column_unboxed(table, arr_list_{nkvne__bjo}, i, arr_ind_{nkvne__bjo})
"""
                    cuua__kytxp += f"""    out_idx_{wcet__pmsk}_{nkvne__bjo} = new_idx_{nkvne__bjo}[i]
"""
                    cuua__kytxp += f"""    arr_val_{wcet__pmsk} =  bodo.utils.conversion.fix_arr_dtype(arr_list_{nkvne__bjo}[i], typ_{wcet__pmsk}, copy, nan_to_str=_bodo_nan_to_str, from_series=True)
"""
                    cuua__kytxp += f"""    out_arr_list_{wcet__pmsk}[out_idx_{wcet__pmsk}_{nkvne__bjo}] = arr_val_{wcet__pmsk}
"""
        cuua__kytxp += f"""  out_table = bodo.hiframes.table.set_table_block(out_table, out_arr_list_{wcet__pmsk}, {wcet__pmsk})
"""
    cuua__kytxp += '  return out_table\n'
    bjq__xvzl = {}
    exec(cuua__kytxp, vpl__wror, bjq__xvzl)
    return bjq__xvzl['impl']


def table_astype_equiv(self, scope, equiv_set, loc, args, kws):
    jbvd__ymubw = args[0]
    if equiv_set.has_shape(jbvd__ymubw):
        return ArrayAnalysis.AnalyzeResult(shape=jbvd__ymubw, pre=[])
    return None


ArrayAnalysis._analyze_op_call_bodo_utils_table_utils_table_astype = (
    table_astype_equiv)
