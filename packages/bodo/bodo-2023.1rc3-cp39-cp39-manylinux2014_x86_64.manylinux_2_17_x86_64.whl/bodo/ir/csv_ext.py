from collections import defaultdict
import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from mpi4py import MPI
from numba.core import cgutils, ir, ir_utils, typeinfer, types
from numba.core.ir_utils import compile_to_numba_ir, replace_arg_nodes
from numba.extending import intrinsic
import bodo
import bodo.ir.connector
from bodo import objmode
from bodo.hiframes.datetime_date_ext import datetime_date_type
from bodo.hiframes.pd_categorical_ext import CategoricalArrayType, PDCategoricalDtype
from bodo.hiframes.table import Table, TableType
from bodo.io.fs_io import get_storage_options_pyobject, storage_options_dict_type
from bodo.libs.array_item_arr_ext import ArrayItemArrayType
from bodo.libs.bool_arr_ext import boolean_array
from bodo.libs.int_arr_ext import IntegerArrayType
from bodo.libs.str_arr_ext import StringArrayType, string_array_type
from bodo.libs.str_ext import string_type
from bodo.transforms import distributed_analysis, distributed_pass
from bodo.transforms.table_column_del_pass import ir_extension_table_column_use, remove_dead_column_extensions
from bodo.utils.typing import BodoError
from bodo.utils.utils import check_java_installation
from bodo.utils.utils import check_and_propagate_cpp_exception, sanitize_varname


class CsvReader(ir.Stmt):

    def __init__(self, file_name, df_out, sep, df_colnames, out_vars,
        out_types, usecols, loc, header, compression, nrows, skiprows,
        chunksize, is_skiprows_list, low_memory, escapechar,
        storage_options=None, index_column_index=None, index_column_typ=
        types.none):
        self.connector_typ = 'csv'
        self.file_name = file_name
        self.df_out = df_out
        self.sep = sep
        self.df_colnames = df_colnames
        self.out_vars = out_vars
        self.out_types = out_types
        self.usecols = usecols
        self.loc = loc
        self.skiprows = skiprows
        self.nrows = nrows
        self.header = header
        self.compression = compression
        self.chunksize = chunksize
        self.is_skiprows_list = is_skiprows_list
        self.pd_low_memory = low_memory
        self.escapechar = escapechar
        self.storage_options = storage_options
        self.index_column_index = index_column_index
        self.index_column_typ = index_column_typ
        self.out_used_cols = list(range(len(usecols)))

    def __repr__(self):
        return (
            '{} = ReadCsv(file={}, col_names={}, types={}, vars={}, nrows={}, skiprows={}, chunksize={}, is_skiprows_list={}, pd_low_memory={}, escapechar={}, storage_options={}, index_column_index={}, index_colum_typ = {}, out_used_colss={})'
            .format(self.df_out, self.file_name, self.df_colnames, self.
            out_types, self.out_vars, self.nrows, self.skiprows, self.
            chunksize, self.is_skiprows_list, self.pd_low_memory, self.
            escapechar, self.storage_options, self.index_column_index, self
            .index_column_typ, self.out_used_cols))


def check_node_typing(node, typemap):
    ulmo__pmm = typemap[node.file_name.name]
    if types.unliteral(ulmo__pmm) != types.unicode_type:
        raise BodoError(
            f"pd.read_csv(): 'filepath_or_buffer' must be a string. Found type: {ulmo__pmm}."
            , node.file_name.loc)
    if not isinstance(node.skiprows, ir.Const):
        jrm__tsy = typemap[node.skiprows.name]
        if isinstance(jrm__tsy, types.Dispatcher):
            raise BodoError(
                f"pd.read_csv(): 'skiprows' callable not supported yet.",
                node.file_name.loc)
        elif not isinstance(jrm__tsy, types.Integer) and not (isinstance(
            jrm__tsy, (types.List, types.Tuple)) and isinstance(jrm__tsy.
            dtype, types.Integer)) and not isinstance(jrm__tsy, (types.
            LiteralList, bodo.utils.typing.ListLiteral)):
            raise BodoError(
                f"pd.read_csv(): 'skiprows' must be an integer or list of integers. Found type {jrm__tsy}."
                , loc=node.skiprows.loc)
        elif isinstance(jrm__tsy, (types.List, types.Tuple)):
            node.is_skiprows_list = True
    if not isinstance(node.nrows, ir.Const):
        vbnk__dmssc = typemap[node.nrows.name]
        if not isinstance(vbnk__dmssc, types.Integer):
            raise BodoError(
                f"pd.read_csv(): 'nrows' must be an integer. Found type {vbnk__dmssc}."
                , loc=node.nrows.loc)


import llvmlite.binding as ll
from bodo.io import csv_cpp
ll.add_symbol('csv_file_chunk_reader', csv_cpp.csv_file_chunk_reader)


@intrinsic
def csv_file_chunk_reader(typingctx, fname_t, is_parallel_t, skiprows_t,
    nrows_t, header_t, compression_t, bucket_region_t, storage_options_t,
    chunksize_t, is_skiprows_list_t, skiprows_list_len_t, pd_low_memory_t):
    assert storage_options_t == storage_options_dict_type, "Storage options don't match expected type"

    def codegen(context, builder, sig, args):
        psq__sws = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(1), lir.IntType(8).
            as_pointer(), lir.IntType(64), lir.IntType(1), lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(64), lir.IntType(1), lir.IntType(64),
            lir.IntType(1)])
        xdh__paplk = cgutils.get_or_insert_function(builder.module,
            psq__sws, name='csv_file_chunk_reader')
        dnt__wwgh = builder.call(xdh__paplk, args)
        context.compile_internal(builder, lambda :
            check_and_propagate_cpp_exception(), types.none(), [])
        kqu__bmf = cgutils.create_struct_proxy(types.stream_reader_type)(
            context, builder)
        lmset__xie = context.get_python_api(builder)
        kqu__bmf.meminfo = lmset__xie.nrt_meminfo_new_from_pyobject(context
            .get_constant_null(types.voidptr), dnt__wwgh)
        kqu__bmf.pyobj = dnt__wwgh
        lmset__xie.decref(dnt__wwgh)
        return kqu__bmf._getvalue()
    return types.stream_reader_type(types.voidptr, types.bool_, types.
        voidptr, types.int64, types.bool_, types.voidptr, types.voidptr,
        storage_options_dict_type, types.int64, types.bool_, types.int64,
        types.bool_), codegen


def remove_dead_csv(csv_node, lives_no_aliases, lives, arg_aliases,
    alias_map, func_ir, typemap):
    if csv_node.chunksize is not None:
        tyqcg__xshk = csv_node.out_vars[0]
        if tyqcg__xshk.name not in lives:
            return None
    else:
        wwf__zgi = csv_node.out_vars[0]
        vneql__zid = csv_node.out_vars[1]
        if wwf__zgi.name not in lives and vneql__zid.name not in lives:
            return None
        elif vneql__zid.name not in lives:
            csv_node.index_column_index = None
            csv_node.index_column_typ = types.none
        elif wwf__zgi.name not in lives:
            csv_node.usecols = []
            csv_node.out_types = []
            csv_node.out_used_cols = []
    return csv_node


def csv_distributed_run(csv_node, array_dists, typemap, calltypes,
    typingctx, targetctx):
    jrm__tsy = types.int64 if isinstance(csv_node.skiprows, ir.Const
        ) else types.unliteral(typemap[csv_node.skiprows.name])
    if csv_node.chunksize is not None:
        parallel = False
        if bodo.user_logging.get_verbose_level() >= 1:
            halvv__plx = (
                'Finish column pruning on read_csv node:\n%s\nColumns loaded %s\n'
                )
            ddpu__uzo = csv_node.loc.strformat()
            etwvg__hsfyz = csv_node.df_colnames
            bodo.user_logging.log_message('Column Pruning', halvv__plx,
                ddpu__uzo, etwvg__hsfyz)
            fpyz__ityvv = csv_node.out_types[0].yield_type.data
            any__irw = [aqf__ukbg for vebx__fesr, aqf__ukbg in enumerate(
                csv_node.df_colnames) if isinstance(fpyz__ityvv[vebx__fesr],
                bodo.libs.dict_arr_ext.DictionaryArrayType)]
            if any__irw:
                wfw__xoerx = """Finished optimized encoding on read_csv node:
%s
Columns %s using dictionary encoding to reduce memory usage.
"""
                bodo.user_logging.log_message('Dictionary Encoding',
                    wfw__xoerx, ddpu__uzo, any__irw)
        if array_dists is not None:
            hos__pdlqq = csv_node.out_vars[0].name
            parallel = array_dists[hos__pdlqq] in (distributed_pass.
                Distribution.OneD, distributed_pass.Distribution.OneD_Var)
        ogwua__ezsc = 'def csv_iterator_impl(fname, nrows, skiprows):\n'
        ogwua__ezsc += (
            f'    reader = _csv_reader_init(fname, nrows, skiprows)\n')
        ogwua__ezsc += (
            f'    iterator = init_csv_iterator(reader, csv_iterator_type)\n')
        qcq__gdfq = {}
        from bodo.io.csv_iterator_ext import init_csv_iterator
        exec(ogwua__ezsc, {}, qcq__gdfq)
        xzty__wzqqd = qcq__gdfq['csv_iterator_impl']
        ldxh__klamn = 'def csv_reader_init(fname, nrows, skiprows):\n'
        ldxh__klamn += _gen_csv_file_reader_init(parallel, csv_node.header,
            csv_node.compression, csv_node.chunksize, csv_node.
            is_skiprows_list, csv_node.pd_low_memory, csv_node.storage_options)
        ldxh__klamn += '  return f_reader\n'
        exec(ldxh__klamn, globals(), qcq__gdfq)
        siffo__tcp = qcq__gdfq['csv_reader_init']
        kbwav__ouys = numba.njit(siffo__tcp)
        compiled_funcs.append(kbwav__ouys)
        fstm__xwhkx = compile_to_numba_ir(xzty__wzqqd, {'_csv_reader_init':
            kbwav__ouys, 'init_csv_iterator': init_csv_iterator,
            'csv_iterator_type': typemap[csv_node.out_vars[0].name]},
            typingctx=typingctx, targetctx=targetctx, arg_typs=(string_type,
            types.int64, jrm__tsy), typemap=typemap, calltypes=calltypes
            ).blocks.popitem()[1]
        replace_arg_nodes(fstm__xwhkx, [csv_node.file_name, csv_node.nrows,
            csv_node.skiprows])
        xgqrr__hszt = fstm__xwhkx.body[:-3]
        xgqrr__hszt[-1].target = csv_node.out_vars[0]
        return xgqrr__hszt
    parallel = bodo.ir.connector.is_connector_table_parallel(csv_node,
        array_dists, typemap, 'CSVReader')
    ogwua__ezsc = 'def csv_impl(fname, nrows, skiprows):\n'
    ogwua__ezsc += (
        f'    (table_val, idx_col) = _csv_reader_py(fname, nrows, skiprows)\n')
    qcq__gdfq = {}
    exec(ogwua__ezsc, {}, qcq__gdfq)
    xgfzj__awxnu = qcq__gdfq['csv_impl']
    dhhnz__upcgf = csv_node.usecols
    if dhhnz__upcgf:
        dhhnz__upcgf = [csv_node.usecols[vebx__fesr] for vebx__fesr in
            csv_node.out_used_cols]
    if bodo.user_logging.get_verbose_level() >= 1:
        halvv__plx = (
            'Finish column pruning on read_csv node:\n%s\nColumns loaded %s\n')
        ddpu__uzo = csv_node.loc.strformat()
        etwvg__hsfyz = []
        any__irw = []
        if dhhnz__upcgf:
            for vebx__fesr in csv_node.out_used_cols:
                aanfu__gpsr = csv_node.df_colnames[vebx__fesr]
                etwvg__hsfyz.append(aanfu__gpsr)
                if isinstance(csv_node.out_types[vebx__fesr], bodo.libs.
                    dict_arr_ext.DictionaryArrayType):
                    any__irw.append(aanfu__gpsr)
        bodo.user_logging.log_message('Column Pruning', halvv__plx,
            ddpu__uzo, etwvg__hsfyz)
        if any__irw:
            wfw__xoerx = """Finished optimized encoding on read_csv node:
%s
Columns %s using dictionary encoding to reduce memory usage.
"""
            bodo.user_logging.log_message('Dictionary Encoding', wfw__xoerx,
                ddpu__uzo, any__irw)
    txl__skxv = _gen_csv_reader_py(csv_node.df_colnames, csv_node.out_types,
        dhhnz__upcgf, csv_node.out_used_cols, csv_node.sep, parallel,
        csv_node.header, csv_node.compression, csv_node.is_skiprows_list,
        csv_node.pd_low_memory, csv_node.escapechar, csv_node.
        storage_options, idx_col_index=csv_node.index_column_index,
        idx_col_typ=csv_node.index_column_typ)
    fstm__xwhkx = compile_to_numba_ir(xgfzj__awxnu, {'_csv_reader_py':
        txl__skxv}, typingctx=typingctx, targetctx=targetctx, arg_typs=(
        string_type, types.int64, jrm__tsy), typemap=typemap, calltypes=
        calltypes).blocks.popitem()[1]
    replace_arg_nodes(fstm__xwhkx, [csv_node.file_name, csv_node.nrows,
        csv_node.skiprows, csv_node.is_skiprows_list])
    xgqrr__hszt = fstm__xwhkx.body[:-3]
    xgqrr__hszt[-1].target = csv_node.out_vars[1]
    xgqrr__hszt[-2].target = csv_node.out_vars[0]
    assert not (csv_node.index_column_index is None and not dhhnz__upcgf
        ), 'At most one of table and index should be dead if the CSV IR node is live'
    if csv_node.index_column_index is None:
        xgqrr__hszt.pop(-1)
    elif not dhhnz__upcgf:
        xgqrr__hszt.pop(-2)
    return xgqrr__hszt


def csv_remove_dead_column(csv_node, column_live_map, equiv_vars, typemap):
    if csv_node.chunksize is not None:
        return False
    return bodo.ir.connector.base_connector_remove_dead_columns(csv_node,
        column_live_map, equiv_vars, typemap, 'CSVReader', csv_node.usecols)


numba.parfors.array_analysis.array_analysis_extensions[CsvReader
    ] = bodo.ir.connector.connector_array_analysis
distributed_analysis.distributed_analysis_extensions[CsvReader
    ] = bodo.ir.connector.connector_distributed_analysis
typeinfer.typeinfer_extensions[CsvReader
    ] = bodo.ir.connector.connector_typeinfer
ir_utils.visit_vars_extensions[CsvReader
    ] = bodo.ir.connector.visit_vars_connector
ir_utils.remove_dead_extensions[CsvReader] = remove_dead_csv
numba.core.analysis.ir_extension_usedefs[CsvReader
    ] = bodo.ir.connector.connector_usedefs
ir_utils.copy_propagate_extensions[CsvReader
    ] = bodo.ir.connector.get_copies_connector
ir_utils.apply_copy_propagate_extensions[CsvReader
    ] = bodo.ir.connector.apply_copies_connector
ir_utils.build_defs_extensions[CsvReader
    ] = bodo.ir.connector.build_connector_definitions
distributed_pass.distributed_run_extensions[CsvReader] = csv_distributed_run
remove_dead_column_extensions[CsvReader] = csv_remove_dead_column
ir_extension_table_column_use[CsvReader
    ] = bodo.ir.connector.connector_table_column_use


def _get_dtype_str(t):
    lrqt__yuo = t.dtype
    if isinstance(lrqt__yuo, PDCategoricalDtype):
        guxxh__ujt = CategoricalArrayType(lrqt__yuo)
        rgq__ebq = 'CategoricalArrayType' + str(ir_utils.next_label())
        setattr(types, rgq__ebq, guxxh__ujt)
        return rgq__ebq
    if lrqt__yuo == types.NPDatetime('ns'):
        lrqt__yuo = 'NPDatetime("ns")'
    if t == string_array_type:
        types.string_array_type = string_array_type
        return 'string_array_type'
    if isinstance(t, IntegerArrayType):
        rlx__mqnyh = 'int_arr_{}'.format(lrqt__yuo)
        setattr(types, rlx__mqnyh, t)
        return rlx__mqnyh
    if t == boolean_array:
        types.boolean_array = boolean_array
        return 'boolean_array'
    if lrqt__yuo == types.bool_:
        lrqt__yuo = 'bool_'
    if lrqt__yuo == datetime_date_type:
        return 'datetime_date_array_type'
    if isinstance(t, ArrayItemArrayType) and isinstance(lrqt__yuo, (
        StringArrayType, ArrayItemArrayType)):
        zefk__npi = f'ArrayItemArrayType{str(ir_utils.next_label())}'
        setattr(types, zefk__npi, t)
        return zefk__npi
    return '{}[::1]'.format(lrqt__yuo)


def _get_pd_dtype_str(t):
    lrqt__yuo = t.dtype
    if isinstance(lrqt__yuo, PDCategoricalDtype):
        return 'pd.CategoricalDtype({})'.format(lrqt__yuo.categories)
    if lrqt__yuo == types.NPDatetime('ns'):
        return 'str'
    if t == string_array_type or t == bodo.dict_str_arr_type:
        return 'str'
    if isinstance(t, IntegerArrayType):
        return '"{}Int{}"'.format('' if lrqt__yuo.signed else 'U',
            lrqt__yuo.bitwidth)
    if t == boolean_array:
        return 'np.bool_'
    if isinstance(t, ArrayItemArrayType) and isinstance(lrqt__yuo, (
        StringArrayType, ArrayItemArrayType)):
        return 'object'
    return 'np.{}'.format(lrqt__yuo)


compiled_funcs = []


@numba.njit
def check_nrows_skiprows_value(nrows, skiprows):
    if nrows < -1:
        raise ValueError('pd.read_csv: nrows must be integer >= 0.')
    if skiprows[0] < 0:
        raise ValueError('pd.read_csv: skiprows must be integer >= 0.')


def astype(df, typemap, parallel):
    lkpf__kce = ''
    from collections import defaultdict
    xtpw__fdpxm = defaultdict(list)
    for hkb__byxo, vcqp__bkd in typemap.items():
        xtpw__fdpxm[vcqp__bkd].append(hkb__byxo)
    bpm__mwesd = df.columns.to_list()
    qviju__pdnpz = []
    for vcqp__bkd, flkpx__hozhx in xtpw__fdpxm.items():
        try:
            qviju__pdnpz.append(df.loc[:, flkpx__hozhx].astype(vcqp__bkd,
                copy=False))
            df = df.drop(flkpx__hozhx, axis=1)
        except (ValueError, TypeError) as jbq__btwxn:
            lkpf__kce = (
                f"Caught the runtime error '{jbq__btwxn}' on columns {flkpx__hozhx}. Consider setting the 'dtype' argument in 'read_csv' or investigate if the data is corrupted."
                )
            break
    oqmh__zkei = bool(lkpf__kce)
    if parallel:
        udd__ahpu = MPI.COMM_WORLD
        oqmh__zkei = udd__ahpu.allreduce(oqmh__zkei, op=MPI.LOR)
    if oqmh__zkei:
        kkib__cln = 'pd.read_csv(): Bodo could not infer dtypes correctly.'
        if lkpf__kce:
            raise TypeError(f'{kkib__cln}\n{lkpf__kce}')
        else:
            raise TypeError(
                f'{kkib__cln}\nPlease refer to errors on other ranks.')
    df = pd.concat(qviju__pdnpz + [df], axis=1)
    oeu__eewf = df.loc[:, bpm__mwesd]
    return oeu__eewf


def _gen_csv_file_reader_init(parallel, header, compression, chunksize,
    is_skiprows_list, pd_low_memory, storage_options):
    ojgru__reob = header == 0
    if compression is None:
        compression = 'uncompressed'
    if is_skiprows_list:
        ogwua__ezsc = '  skiprows = sorted(set(skiprows))\n'
    else:
        ogwua__ezsc = '  skiprows = [skiprows]\n'
    ogwua__ezsc += '  skiprows_list_len = len(skiprows)\n'
    ogwua__ezsc += '  check_nrows_skiprows_value(nrows, skiprows)\n'
    ogwua__ezsc += '  check_java_installation(fname)\n'
    ogwua__ezsc += f"""  bucket_region = bodo.io.fs_io.get_s3_bucket_region_njit(fname, parallel={parallel})
"""
    if storage_options is None:
        storage_options = {}
    storage_options['bodo_dummy'] = 'dummy'
    ogwua__ezsc += (
        f'  storage_options_py = get_storage_options_pyobject({str(storage_options)})\n'
        )
    ogwua__ezsc += (
        '  f_reader = bodo.ir.csv_ext.csv_file_chunk_reader(bodo.libs.str_ext.unicode_to_utf8(fname), '
        )
    ogwua__ezsc += (
        """    {}, bodo.utils.conversion.coerce_to_ndarray(skiprows, scalar_to_arr_len=1).ctypes, nrows, {}, bodo.libs.str_ext.unicode_to_utf8('{}'), bodo.libs.str_ext.unicode_to_utf8(bucket_region), storage_options_py, {}, {}, skiprows_list_len, {})
"""
        .format(parallel, ojgru__reob, compression, chunksize,
        is_skiprows_list, pd_low_memory))
    ogwua__ezsc += '  if bodo.utils.utils.is_null_pointer(f_reader._pyobj):\n'
    ogwua__ezsc += "      raise FileNotFoundError('File does not exist')\n"
    return ogwua__ezsc


def _gen_read_csv_objmode(col_names, sanitized_cnames, col_typs, usecols,
    out_used_cols, sep, escapechar, storage_options, call_id, glbs,
    parallel, check_parallel_runtime, idx_col_index, idx_col_typ):
    ysn__eyag = [str(vebx__fesr) for vebx__fesr, johx__ymu in enumerate(
        usecols) if col_typs[out_used_cols[vebx__fesr]].dtype == types.
        NPDatetime('ns')]
    if idx_col_typ == types.NPDatetime('ns'):
        assert not idx_col_index is None
        ysn__eyag.append(str(idx_col_index))
    enaj__dhnp = ', '.join(ysn__eyag)
    sln__tulnh = _gen_parallel_flag_name(sanitized_cnames)
    sfg__mbpf = f"{sln__tulnh}='bool_'" if check_parallel_runtime else ''
    awbv__zikme = [_get_pd_dtype_str(col_typs[out_used_cols[vebx__fesr]]) for
        vebx__fesr in range(len(usecols))]
    baedw__vsw = None if idx_col_index is None else _get_pd_dtype_str(
        idx_col_typ)
    wsqfb__rgmx = [johx__ymu for vebx__fesr, johx__ymu in enumerate(usecols
        ) if awbv__zikme[vebx__fesr] == 'str']
    if idx_col_index is not None and baedw__vsw == 'str':
        wsqfb__rgmx.append(idx_col_index)
    wqbao__zthi = np.array(wsqfb__rgmx, dtype=np.int64)
    glbs[f'str_col_nums_{call_id}'] = wqbao__zthi
    ogwua__ezsc = f'  str_col_nums_{call_id}_2 = str_col_nums_{call_id}\n'
    hst__cyr = np.array(usecols + ([idx_col_index] if idx_col_index is not
        None else []), dtype=np.int64)
    glbs[f'usecols_arr_{call_id}'] = hst__cyr
    ogwua__ezsc += f'  usecols_arr_{call_id}_2 = usecols_arr_{call_id}\n'
    pmcqw__itiqd = np.array(out_used_cols, dtype=np.int64)
    if usecols:
        glbs[f'type_usecols_offsets_arr_{call_id}'] = pmcqw__itiqd
        ogwua__ezsc += f"""  type_usecols_offsets_arr_{call_id}_2 = type_usecols_offsets_arr_{call_id}
"""
    xxic__ahx = defaultdict(list)
    for vebx__fesr, johx__ymu in enumerate(usecols):
        if awbv__zikme[vebx__fesr] == 'str':
            continue
        xxic__ahx[awbv__zikme[vebx__fesr]].append(johx__ymu)
    if idx_col_index is not None and baedw__vsw != 'str':
        xxic__ahx[baedw__vsw].append(idx_col_index)
    for vebx__fesr, ynpjn__hjwwi in enumerate(xxic__ahx.values()):
        glbs[f't_arr_{vebx__fesr}_{call_id}'] = np.asarray(ynpjn__hjwwi)
        ogwua__ezsc += (
            f'  t_arr_{vebx__fesr}_{call_id}_2 = t_arr_{vebx__fesr}_{call_id}\n'
            )
    if idx_col_index != None:
        ogwua__ezsc += f"""  with objmode(T=table_type_{call_id}, idx_arr=idx_array_typ, {sfg__mbpf}):
"""
    else:
        ogwua__ezsc += (
            f'  with objmode(T=table_type_{call_id}, {sfg__mbpf}):\n')
    ogwua__ezsc += f'    typemap = {{}}\n'
    for vebx__fesr, zquhm__row in enumerate(xxic__ahx.keys()):
        ogwua__ezsc += f"""    typemap.update({{i:{zquhm__row} for i in t_arr_{vebx__fesr}_{call_id}_2}})
"""
    ogwua__ezsc += '    if f_reader.get_chunk_size() == 0:\n'
    ogwua__ezsc += (
        f'      df = pd.DataFrame(columns=usecols_arr_{call_id}_2, dtype=str)\n'
        )
    ogwua__ezsc += '    else:\n'
    ogwua__ezsc += '      df = pd.read_csv(f_reader,\n'
    ogwua__ezsc += '        header=None,\n'
    ogwua__ezsc += '        parse_dates=[{}],\n'.format(enaj__dhnp)
    ogwua__ezsc += (
        f"        dtype={{i:'string[pyarrow]' for i in str_col_nums_{call_id}_2}},\n"
        )
    ogwua__ezsc += f"""        usecols=usecols_arr_{call_id}_2, sep={sep!r}, low_memory=False, escapechar={escapechar!r})
"""
    if check_parallel_runtime:
        ogwua__ezsc += f'    {sln__tulnh} = f_reader.is_parallel()\n'
    else:
        ogwua__ezsc += f'    {sln__tulnh} = {parallel}\n'
    ogwua__ezsc += f'    df = astype(df, typemap, {sln__tulnh})\n'
    if idx_col_index != None:
        dgs__kep = sorted(hst__cyr).index(idx_col_index)
        ogwua__ezsc += f'    idx_arr = df.iloc[:, {dgs__kep}].values\n'
        ogwua__ezsc += (
            f'    df.drop(columns=df.columns[{dgs__kep}], inplace=True)\n')
    if len(usecols) == 0:
        ogwua__ezsc += f'    T = None\n'
    else:
        ogwua__ezsc += f'    arrs = []\n'
        ogwua__ezsc += f'    for i in range(df.shape[1]):\n'
        ogwua__ezsc += f'      arrs.append(df.iloc[:, i].values)\n'
        ogwua__ezsc += f"""    T = Table(arrs, type_usecols_offsets_arr_{call_id}_2, {len(col_names)})
"""
    return ogwua__ezsc


def _gen_parallel_flag_name(sanitized_cnames):
    sln__tulnh = '_parallel_value'
    while sln__tulnh in sanitized_cnames:
        sln__tulnh = '_' + sln__tulnh
    return sln__tulnh


def _gen_csv_reader_py(col_names, col_typs, usecols, out_used_cols, sep,
    parallel, header, compression, is_skiprows_list, pd_low_memory,
    escapechar, storage_options, idx_col_index=None, idx_col_typ=types.none):
    sanitized_cnames = [sanitize_varname(aqf__ukbg) for aqf__ukbg in col_names]
    ogwua__ezsc = 'def csv_reader_py(fname, nrows, skiprows):\n'
    ogwua__ezsc += _gen_csv_file_reader_init(parallel, header, compression,
        -1, is_skiprows_list, pd_low_memory, storage_options)
    call_id = ir_utils.next_label()
    hvdm__ghre = globals()
    if idx_col_typ != types.none:
        hvdm__ghre[f'idx_array_typ'] = idx_col_typ
    if len(usecols) == 0:
        hvdm__ghre[f'table_type_{call_id}'] = types.none
    else:
        hvdm__ghre[f'table_type_{call_id}'] = TableType(tuple(col_typs))
    ogwua__ezsc += _gen_read_csv_objmode(col_names, sanitized_cnames,
        col_typs, usecols, out_used_cols, sep, escapechar, storage_options,
        call_id, hvdm__ghre, parallel=parallel, check_parallel_runtime=
        False, idx_col_index=idx_col_index, idx_col_typ=idx_col_typ)
    if idx_col_index != None:
        ogwua__ezsc += '  return (T, idx_arr)\n'
    else:
        ogwua__ezsc += '  return (T, None)\n'
    qcq__gdfq = {}
    hvdm__ghre['get_storage_options_pyobject'] = get_storage_options_pyobject
    exec(ogwua__ezsc, hvdm__ghre, qcq__gdfq)
    txl__skxv = qcq__gdfq['csv_reader_py']
    kbwav__ouys = numba.njit(txl__skxv)
    compiled_funcs.append(kbwav__ouys)
    return kbwav__ouys
