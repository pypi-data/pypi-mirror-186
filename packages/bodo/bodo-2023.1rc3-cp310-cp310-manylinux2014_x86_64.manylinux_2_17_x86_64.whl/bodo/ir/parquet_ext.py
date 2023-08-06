"""IR node for the parquet data access"""
from typing import List
import llvmlite.binding as ll
import numba
import numpy as np
import pandas as pd
import pyarrow as pa
from numba.core import ir, ir_utils, typeinfer, types
from numba.core.ir_utils import compile_to_numba_ir, get_definition, guard, mk_unique_var, next_label, replace_arg_nodes
from numba.extending import NativeValue, models, register_model, unbox
import bodo
import bodo.ir.connector
from bodo.hiframes.pd_dataframe_ext import DataFrameType
from bodo.hiframes.table import Table, TableType
from bodo.io.fs_io import get_storage_options_pyobject, storage_options_dict_type
from bodo.io.helpers import is_nullable, numba_to_pyarrow_schema, pyarrow_table_schema_type
from bodo.io.parquet_pio import ParquetFileInfo, get_filters_pyobject, parquet_file_schema, parquet_predicate_type
from bodo.libs.array import cpp_table_to_py_table, delete_table, info_from_table, info_to_array, table_type
from bodo.libs.dict_arr_ext import dict_str_arr_type
from bodo.libs.str_ext import unicode_to_utf8
from bodo.transforms import distributed_analysis, distributed_pass
from bodo.transforms.table_column_del_pass import ir_extension_table_column_use, remove_dead_column_extensions
from bodo.utils.transform import get_const_value
from bodo.utils.typing import BodoError, FilenameType
from bodo.utils.utils import check_and_propagate_cpp_exception, numba_to_c_type, sanitize_varname


class ReadParquetFilepathType(types.Opaque):

    def __init__(self):
        super(ReadParquetFilepathType, self).__init__(name=
            'ReadParquetFilepathType')


read_parquet_fpath_type = ReadParquetFilepathType()
types.read_parquet_fpath_type = read_parquet_fpath_type
register_model(ReadParquetFilepathType)(models.OpaqueModel)


@unbox(ReadParquetFilepathType)
def unbox_read_parquet_fpath_type(typ, val, c):
    c.pyapi.incref(val)
    return NativeValue(val)


class ParquetHandler:

    def __init__(self, func_ir, typingctx, args, _locals):
        self.func_ir = func_ir
        self.typingctx = typingctx
        self.args = args
        self.locals = _locals

    def gen_parquet_read(self, file_name, lhs, columns, storage_options=
        None, input_file_name_col=None, read_as_dict_cols=None, use_hive=True):
        wcgtc__fat = lhs.scope
        loc = lhs.loc
        kwyom__mrsv = None
        if lhs.name in self.locals:
            kwyom__mrsv = self.locals[lhs.name]
            self.locals.pop(lhs.name)
        zza__vmiro = {}
        if lhs.name + ':convert' in self.locals:
            zza__vmiro = self.locals[lhs.name + ':convert']
            self.locals.pop(lhs.name + ':convert')
        if kwyom__mrsv is None:
            wvxe__lcauj = (
                'Parquet schema not available. Either path argument should be constant for Bodo to look at the file at compile time or schema should be provided. For more information, see: https://docs.bodo.ai/latest/file_io/#parquet-section.'
                )
            utyt__rlq = get_const_value(file_name, self.func_ir,
                wvxe__lcauj, arg_types=self.args, file_info=ParquetFileInfo
                (columns, storage_options=storage_options,
                input_file_name_col=input_file_name_col, read_as_dict_cols=
                read_as_dict_cols, use_hive=use_hive))
            bwri__pkr = guard(get_definition, self.func_ir, file_name)
            if isinstance(bwri__pkr, ir.Arg) and isinstance(self.args[
                bwri__pkr.index], FilenameType):
                typ: FilenameType = self.args[bwri__pkr.index]
                (col_names, ntd__uyzr, rahj__era, col_indices,
                    partition_names, unsupported_columns,
                    unsupported_arrow_types, arrow_schema) = typ.schema
            else:
                (col_names, ntd__uyzr, rahj__era, col_indices,
                    partition_names, unsupported_columns,
                    unsupported_arrow_types, arrow_schema) = (
                    parquet_file_schema(utyt__rlq, columns, storage_options,
                    input_file_name_col, read_as_dict_cols, use_hive))
        else:
            vszpp__esny: List[str] = list(kwyom__mrsv.keys())
            ddtrq__decx = {c: uelw__mpk for uelw__mpk, c in enumerate(
                vszpp__esny)}
            oug__cdffj = [bbkl__jah for bbkl__jah in kwyom__mrsv.values()]
            col_names: List[str] = vszpp__esny if columns is None else columns
            col_indices = [ddtrq__decx[c] for c in col_names]
            ntd__uyzr = [oug__cdffj[ddtrq__decx[c]] for c in col_names]
            rahj__era = next((fel__uilyw for fel__uilyw in col_names if
                fel__uilyw.startswith('__index_level_')), None)
            partition_names = []
            unsupported_columns = []
            unsupported_arrow_types = []
            arrow_schema = numba_to_pyarrow_schema(DataFrameType(data=tuple
                (ntd__uyzr), columns=tuple(col_names)))
        tdeo__rgn = None if isinstance(rahj__era, dict
            ) or rahj__era is None else rahj__era
        index_column_index = None
        index_column_type = types.none
        if tdeo__rgn:
            ojixv__nkeup = col_names.index(tdeo__rgn)
            index_column_index = col_indices.pop(ojixv__nkeup)
            index_column_type = ntd__uyzr.pop(ojixv__nkeup)
            col_names.pop(ojixv__nkeup)
        for uelw__mpk, c in enumerate(col_names):
            if c in zza__vmiro:
                ntd__uyzr[uelw__mpk] = zza__vmiro[c]
        rwzg__bgjxd = [ir.Var(wcgtc__fat, mk_unique_var('pq_table'), loc),
            ir.Var(wcgtc__fat, mk_unique_var('pq_index'), loc)]
        qdt__qhkzy = [ParquetReader(file_name, lhs.name, col_names,
            col_indices, ntd__uyzr, rwzg__bgjxd, loc, partition_names,
            storage_options, index_column_index, index_column_type,
            input_file_name_col, unsupported_columns,
            unsupported_arrow_types, arrow_schema, use_hive)]
        return (col_names, rwzg__bgjxd, rahj__era, qdt__qhkzy, ntd__uyzr,
            index_column_type)


class ParquetReader(ir.Stmt):

    def __init__(self, file_name, df_out, col_names, col_indices, out_types,
        out_vars, loc, partition_names, storage_options, index_column_index,
        index_column_type, input_file_name_col, unsupported_columns,
        unsupported_arrow_types, arrow_schema, use_hive):
        self.connector_typ = 'parquet'
        self.file_name = file_name
        self.df_out = df_out
        self.df_colnames = col_names
        self.col_indices = col_indices
        self.out_types = out_types
        self.original_out_types = out_types
        self.original_df_colnames = col_names
        self.out_vars = out_vars
        self.loc = loc
        self.partition_names = partition_names
        self.filters = None
        self.storage_options = storage_options
        self.index_column_index = index_column_index
        self.index_column_type = index_column_type
        self.out_used_cols = list(range(len(col_indices)))
        self.input_file_name_col = input_file_name_col
        self.unsupported_columns = unsupported_columns
        self.unsupported_arrow_types = unsupported_arrow_types
        self.arrow_schema = arrow_schema
        self.is_live_table = True
        self.use_hive = use_hive

    def __repr__(self):
        return (
            '({}) = ReadParquet({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})'
            .format(self.df_out, self.file_name.name, self.df_colnames,
            self.col_indices, self.out_types, self.original_out_types, self
            .original_df_colnames, self.out_vars, self.partition_names,
            self.filters, self.storage_options, self.index_column_index,
            self.index_column_type, self.out_used_cols, self.
            input_file_name_col, self.unsupported_columns, self.
            unsupported_arrow_types, self.arrow_schema))


def remove_dead_pq(pq_node, lives_no_aliases, lives, arg_aliases, alias_map,
    func_ir, typemap):
    iivi__rwjau = pq_node.out_vars[0].name
    lhr__isrpr = pq_node.out_vars[1].name
    if iivi__rwjau not in lives and lhr__isrpr not in lives:
        return None
    elif iivi__rwjau not in lives:
        pq_node.col_indices = []
        pq_node.df_colnames = []
        pq_node.out_used_cols = []
        pq_node.is_live_table = False
    elif lhr__isrpr not in lives:
        pq_node.index_column_index = None
        pq_node.index_column_type = types.none
    return pq_node


def pq_remove_dead_column(pq_node, column_live_map, equiv_vars, typemap):
    return bodo.ir.connector.base_connector_remove_dead_columns(pq_node,
        column_live_map, equiv_vars, typemap, 'ParquetReader', pq_node.
        col_indices, require_one_column=False)


def pq_distributed_run(pq_node, array_dists, typemap, calltypes, typingctx,
    targetctx, is_independent=False, meta_head_only_info=None):
    qmhf__clrdw = len(pq_node.out_vars)
    dnf_filter_str = 'None'
    expr_filter_str = 'None'
    ado__xod, hsnem__wbn = bodo.ir.connector.generate_filter_map(pq_node.
        filters)
    extra_args = ', '.join(ado__xod.values())
    dnf_filter_str, expr_filter_str = bodo.ir.connector.generate_arrow_filters(
        pq_node.filters, ado__xod, hsnem__wbn, pq_node.original_df_colnames,
        pq_node.partition_names, pq_node.original_out_types, typemap,
        'parquet', output_dnf=False)
    rkgg__yqlw = ', '.join(f'out{uelw__mpk}' for uelw__mpk in range(
        qmhf__clrdw))
    qqr__fnta = f'def pq_impl(fname, {extra_args}):\n'
    qqr__fnta += (
        f'    (total_rows, {rkgg__yqlw},) = _pq_reader_py(fname, {extra_args})\n'
        )
    qolp__xnos = {}
    exec(qqr__fnta, {}, qolp__xnos)
    zqo__doar = qolp__xnos['pq_impl']
    if bodo.user_logging.get_verbose_level() >= 1:
        mhyii__hlb = pq_node.loc.strformat()
        nsesj__lhegv = []
        vqs__thv = []
        for uelw__mpk in pq_node.out_used_cols:
            dwany__ztvs = pq_node.df_colnames[uelw__mpk]
            nsesj__lhegv.append(dwany__ztvs)
            if isinstance(pq_node.out_types[uelw__mpk], bodo.libs.
                dict_arr_ext.DictionaryArrayType):
                vqs__thv.append(dwany__ztvs)
        sgvng__pcwd = (
            'Finish column pruning on read_parquet node:\n%s\nColumns loaded %s\n'
            )
        bodo.user_logging.log_message('Column Pruning', sgvng__pcwd,
            mhyii__hlb, nsesj__lhegv)
        if vqs__thv:
            quqo__cyll = """Finished optimized encoding on read_parquet node:
%s
Columns %s using dictionary encoding to reduce memory usage.
"""
            bodo.user_logging.log_message('Dictionary Encoding', quqo__cyll,
                mhyii__hlb, vqs__thv)
    glf__dip = bodo.ir.connector.is_connector_table_parallel(pq_node,
        array_dists, typemap, 'ParquetReader')
    if pq_node.unsupported_columns:
        yyltp__lmaj = set(pq_node.out_used_cols)
        yuxzn__fml = set(pq_node.unsupported_columns)
        xiji__mjy = yyltp__lmaj & yuxzn__fml
        if xiji__mjy:
            bzc__senol = sorted(xiji__mjy)
            ykiln__mrnh = [
                f'pandas.read_parquet(): 1 or more columns found with Arrow types that are not supported in Bodo and could not be eliminated. '
                 +
                "Please manually remove these columns from your read_parquet with the 'columns' argument. If these "
                 +
                'columns are needed, you will need to modify your dataset to use a supported type.'
                , 'Unsupported Columns:']
            zxd__inihe = 0
            for lwsch__gjkt in bzc__senol:
                while pq_node.unsupported_columns[zxd__inihe] != lwsch__gjkt:
                    zxd__inihe += 1
                ykiln__mrnh.append(
                    f"Column '{pq_node.df_colnames[lwsch__gjkt]}' with unsupported arrow type {pq_node.unsupported_arrow_types[zxd__inihe]}"
                    )
                zxd__inihe += 1
            onu__jin = '\n'.join(ykiln__mrnh)
            raise BodoError(onu__jin, loc=pq_node.loc)
    dme__zkwb = _gen_pq_reader_py(pq_node.df_colnames, pq_node.col_indices,
        pq_node.out_used_cols, pq_node.out_types, pq_node.storage_options,
        pq_node.partition_names, dnf_filter_str, expr_filter_str,
        extra_args, glf__dip, meta_head_only_info, pq_node.
        index_column_index, pq_node.index_column_type, pq_node.
        input_file_name_col, not pq_node.is_live_table, pq_node.
        arrow_schema, pq_node.use_hive)
    lfjq__zhx = typemap[pq_node.file_name.name]
    ygyed__ofu = (lfjq__zhx,) + tuple(typemap[nvno__olu.name] for nvno__olu in
        hsnem__wbn)
    jhr__cnt = compile_to_numba_ir(zqo__doar, {'_pq_reader_py': dme__zkwb},
        typingctx=typingctx, targetctx=targetctx, arg_typs=ygyed__ofu,
        typemap=typemap, calltypes=calltypes).blocks.popitem()[1]
    replace_arg_nodes(jhr__cnt, [pq_node.file_name] + hsnem__wbn)
    qdt__qhkzy = jhr__cnt.body[:-3]
    if meta_head_only_info:
        qdt__qhkzy[-3].target = meta_head_only_info[1]
    qdt__qhkzy[-2].target = pq_node.out_vars[0]
    qdt__qhkzy[-1].target = pq_node.out_vars[1]
    assert not (pq_node.index_column_index is None and not pq_node.
        is_live_table
        ), 'At most one of table and index should be dead if the Parquet IR node is live'
    if pq_node.index_column_index is None:
        qdt__qhkzy.pop(-1)
    elif not pq_node.is_live_table:
        qdt__qhkzy.pop(-2)
    return qdt__qhkzy


def _gen_pq_reader_py(col_names, col_indices, out_used_cols, out_types,
    storage_options, partition_names, dnf_filter_str, expr_filter_str,
    extra_args, is_parallel, meta_head_only_info, index_column_index,
    index_column_type, input_file_name_col, is_dead_table, pyarrow_schema:
    pa.Schema, use_hive: bool):
    chtf__ony = next_label()
    iuk__haht = ',' if extra_args else ''
    qqr__fnta = f'def pq_reader_py(fname,{extra_args}):\n'
    qqr__fnta += (
        f"    ev = bodo.utils.tracing.Event('read_parquet', {is_parallel})\n")
    qqr__fnta += f"    ev.add_attribute('g_fname', fname)\n"
    qqr__fnta += f"""    dnf_filters, expr_filters = get_filters_pyobject("{dnf_filter_str}", "{expr_filter_str}", ({extra_args}{iuk__haht}))
"""
    qqr__fnta += '    fname_py = get_fname_pyobject(fname)\n'
    storage_options['bodo_dummy'] = 'dummy'
    qqr__fnta += (
        f'    storage_options_py = get_storage_options_pyobject({str(storage_options)})\n'
        )
    qpqfv__ygz = -1
    if meta_head_only_info and meta_head_only_info[0] is not None:
        qpqfv__ygz = meta_head_only_info[0]
    pmsl__srgeq = [sanitize_varname(c) for c in col_names]
    partition_names = [sanitize_varname(c) for c in partition_names]
    input_file_name_col = sanitize_varname(input_file_name_col
        ) if input_file_name_col is not None and col_names.index(
        input_file_name_col) in out_used_cols else None
    ttw__ugz = {c: uelw__mpk for uelw__mpk, c in enumerate(col_indices)}
    djly__zfi = {c: uelw__mpk for uelw__mpk, c in enumerate(pmsl__srgeq)}
    nwun__opoan = []
    lryux__wbf = set()
    jvdjg__ggbu = partition_names + [input_file_name_col]
    for uelw__mpk in out_used_cols:
        if pmsl__srgeq[uelw__mpk] not in jvdjg__ggbu:
            nwun__opoan.append(col_indices[uelw__mpk])
        elif not input_file_name_col or pmsl__srgeq[uelw__mpk
            ] != input_file_name_col:
            lryux__wbf.add(col_indices[uelw__mpk])
    if index_column_index is not None:
        nwun__opoan.append(index_column_index)
    nwun__opoan = sorted(nwun__opoan)
    piktx__sadu = {c: uelw__mpk for uelw__mpk, c in enumerate(nwun__opoan)}
    rudjp__azzh = [(int(is_nullable(out_types[ttw__ugz[ixuah__zfmh]])) if 
        ixuah__zfmh != index_column_index else int(is_nullable(
        index_column_type))) for ixuah__zfmh in nwun__opoan]
    zlv__etea = []
    for ixuah__zfmh in nwun__opoan:
        if ixuah__zfmh == index_column_index:
            bbkl__jah = index_column_type
        else:
            bbkl__jah = out_types[ttw__ugz[ixuah__zfmh]]
        if bbkl__jah == dict_str_arr_type:
            zlv__etea.append(ixuah__zfmh)
    rwbzr__avdq = []
    lmnjn__qny = {}
    inlq__qup = []
    zlue__vgwlt = []
    for uelw__mpk, lwrbo__nlk in enumerate(partition_names):
        try:
            fffi__nunq = djly__zfi[lwrbo__nlk]
            if col_indices[fffi__nunq] not in lryux__wbf:
                continue
        except (KeyError, ValueError) as lplvh__xnco:
            continue
        lmnjn__qny[lwrbo__nlk] = len(rwbzr__avdq)
        rwbzr__avdq.append(lwrbo__nlk)
        inlq__qup.append(uelw__mpk)
        tvwkv__joq = out_types[fffi__nunq].dtype
        ezvz__egzo = bodo.hiframes.pd_categorical_ext.get_categories_int_type(
            tvwkv__joq)
        zlue__vgwlt.append(numba_to_c_type(ezvz__egzo))
    qqr__fnta += f"""    total_rows_np = np.array([0], dtype=np.int64)
    out_table = pq_read(
        fname_py,
        {is_parallel},
        dnf_filters,
        expr_filters,
        storage_options_py,
        pyarrow_schema_{chtf__ony},
        {qpqfv__ygz},
        selected_cols_arr_{chtf__ony}.ctypes,
        {len(nwun__opoan)},
        nullable_cols_arr_{chtf__ony}.ctypes,
"""
    if len(inlq__qup) > 0:
        qqr__fnta += f"""        np.array({inlq__qup}, dtype=np.int32).ctypes,
        np.array({zlue__vgwlt}, dtype=np.int32).ctypes,
        {len(inlq__qup)},
"""
    else:
        qqr__fnta += f'        0, 0, 0,\n'
    if len(zlv__etea) > 0:
        qqr__fnta += (
            f'        np.array({zlv__etea}, dtype=np.int32).ctypes, {len(zlv__etea)},\n'
            )
    else:
        qqr__fnta += f'        0, 0,\n'
    qqr__fnta += f'        total_rows_np.ctypes,\n'
    qqr__fnta += f'        {input_file_name_col is not None},\n'
    qqr__fnta += f'        {use_hive},\n'
    qqr__fnta += f'    )\n'
    qqr__fnta += f'    check_and_propagate_cpp_exception()\n'
    qqr__fnta += f'    total_rows = total_rows_np[0]\n'
    if is_parallel:
        qqr__fnta += f"""    local_rows = get_node_portion(total_rows, bodo.get_size(), bodo.get_rank())
"""
    else:
        qqr__fnta += f'    local_rows = total_rows\n'
    yqf__eugm = index_column_type
    krkk__vdpa = TableType(tuple(out_types))
    if is_dead_table:
        krkk__vdpa = types.none
    if is_dead_table:
        fvrhx__xumyy = None
    else:
        fvrhx__xumyy = []
        icjx__cqwc = 0
        fwz__ygcv = col_indices[col_names.index(input_file_name_col)
            ] if input_file_name_col is not None else None
        for uelw__mpk, lwsch__gjkt in enumerate(col_indices):
            if icjx__cqwc < len(out_used_cols) and uelw__mpk == out_used_cols[
                icjx__cqwc]:
                ema__nqidi = col_indices[uelw__mpk]
                if fwz__ygcv and ema__nqidi == fwz__ygcv:
                    fvrhx__xumyy.append(len(nwun__opoan) + len(rwbzr__avdq))
                elif ema__nqidi in lryux__wbf:
                    xvjl__lajl = pmsl__srgeq[uelw__mpk]
                    fvrhx__xumyy.append(len(nwun__opoan) + lmnjn__qny[
                        xvjl__lajl])
                else:
                    fvrhx__xumyy.append(piktx__sadu[lwsch__gjkt])
                icjx__cqwc += 1
            else:
                fvrhx__xumyy.append(-1)
        fvrhx__xumyy = np.array(fvrhx__xumyy, dtype=np.int64)
    if is_dead_table:
        qqr__fnta += '    T = None\n'
    else:
        qqr__fnta += f"""    T = cpp_table_to_py_table(out_table, table_idx_{chtf__ony}, py_table_type_{chtf__ony})
"""
        if len(out_used_cols) == 0:
            qqr__fnta += f'    T = set_table_len(T, local_rows)\n'
    if index_column_index is None:
        qqr__fnta += '    index_arr = None\n'
    else:
        sapj__sbpi = piktx__sadu[index_column_index]
        qqr__fnta += f"""    index_arr = info_to_array(info_from_table(out_table, {sapj__sbpi}), index_arr_type)
"""
    qqr__fnta += f'    delete_table(out_table)\n'
    qqr__fnta += f'    ev.finalize()\n'
    qqr__fnta += f'    return (total_rows, T, index_arr)\n'
    qolp__xnos = {}
    ldvab__klfdt = {f'py_table_type_{chtf__ony}': krkk__vdpa,
        f'table_idx_{chtf__ony}': fvrhx__xumyy,
        f'selected_cols_arr_{chtf__ony}': np.array(nwun__opoan, np.int32),
        f'nullable_cols_arr_{chtf__ony}': np.array(rudjp__azzh, np.int32),
        f'pyarrow_schema_{chtf__ony}': pyarrow_schema.remove_metadata(),
        'index_arr_type': yqf__eugm, 'cpp_table_to_py_table':
        cpp_table_to_py_table, 'info_to_array': info_to_array,
        'info_from_table': info_from_table, 'delete_table': delete_table,
        'check_and_propagate_cpp_exception':
        check_and_propagate_cpp_exception, 'pq_read': _pq_read,
        'unicode_to_utf8': unicode_to_utf8, 'get_filters_pyobject':
        get_filters_pyobject, 'get_storage_options_pyobject':
        get_storage_options_pyobject, 'get_fname_pyobject':
        get_fname_pyobject, 'np': np, 'pd': pd, 'bodo': bodo,
        'get_node_portion': bodo.libs.distributed_api.get_node_portion,
        'set_table_len': bodo.hiframes.table.set_table_len}
    exec(qqr__fnta, ldvab__klfdt, qolp__xnos)
    dme__zkwb = qolp__xnos['pq_reader_py']
    btqj__zzi = numba.njit(dme__zkwb, no_cpython_wrapper=True)
    return btqj__zzi


@numba.njit
def get_fname_pyobject(fname):
    with numba.objmode(fname_py='read_parquet_fpath_type'):
        fname_py = fname
    return fname_py


numba.parfors.array_analysis.array_analysis_extensions[ParquetReader
    ] = bodo.ir.connector.connector_array_analysis
distributed_analysis.distributed_analysis_extensions[ParquetReader
    ] = bodo.ir.connector.connector_distributed_analysis
typeinfer.typeinfer_extensions[ParquetReader
    ] = bodo.ir.connector.connector_typeinfer
ir_utils.visit_vars_extensions[ParquetReader
    ] = bodo.ir.connector.visit_vars_connector
ir_utils.remove_dead_extensions[ParquetReader] = remove_dead_pq
numba.core.analysis.ir_extension_usedefs[ParquetReader
    ] = bodo.ir.connector.connector_usedefs
ir_utils.copy_propagate_extensions[ParquetReader
    ] = bodo.ir.connector.get_copies_connector
ir_utils.apply_copy_propagate_extensions[ParquetReader
    ] = bodo.ir.connector.apply_copies_connector
ir_utils.build_defs_extensions[ParquetReader
    ] = bodo.ir.connector.build_connector_definitions
remove_dead_column_extensions[ParquetReader] = pq_remove_dead_column
ir_extension_table_column_use[ParquetReader
    ] = bodo.ir.connector.connector_table_column_use
distributed_pass.distributed_run_extensions[ParquetReader] = pq_distributed_run
if bodo.utils.utils.has_pyarrow():
    from bodo.io import arrow_cpp
    ll.add_symbol('pq_read', arrow_cpp.pq_read)
_pq_read = types.ExternalFunction('pq_read', table_type(
    read_parquet_fpath_type, types.boolean, parquet_predicate_type,
    parquet_predicate_type, storage_options_dict_type,
    pyarrow_table_schema_type, types.int64, types.voidptr, types.int32,
    types.voidptr, types.voidptr, types.voidptr, types.int32, types.voidptr,
    types.int32, types.voidptr, types.boolean, types.boolean))
