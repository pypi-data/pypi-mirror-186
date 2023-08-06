"""
Implementation of pd.read_sql in Bodo.
We piggyback on the pandas implementation. Future plan is to have a faster
version for this task.
"""
from typing import Any, List, Optional
from urllib.parse import urlparse
import numba
import numpy as np
import pandas as pd
import pyarrow as pa
from llvmlite import ir as lir
from numba.core import cgutils, ir, ir_utils, typeinfer, types
from numba.core.ir_utils import compile_to_numba_ir, next_label, replace_arg_nodes
from numba.extending import intrinsic
import bodo
import bodo.ir.connector
from bodo import objmode
from bodo.hiframes.table import Table, TableType
from bodo.io.helpers import PyArrowTableSchemaType, is_nullable
from bodo.io.parquet_pio import ParquetPredicateType
from bodo.libs.array import cpp_table_to_py_table, delete_table, info_from_table, info_to_array, table_type
from bodo.libs.dict_arr_ext import dict_str_arr_type
from bodo.libs.distributed_api import bcast, bcast_scalar
from bodo.libs.str_ext import string_type, unicode_to_utf8
from bodo.transforms import distributed_analysis, distributed_pass
from bodo.transforms.table_column_del_pass import ir_extension_table_column_use, remove_dead_column_extensions
from bodo.utils.typing import BodoError
from bodo.utils.utils import check_and_propagate_cpp_exception
if bodo.utils.utils.has_pyarrow():
    import llvmlite.binding as ll
    from bodo.io import arrow_cpp
    ll.add_symbol('snowflake_read', arrow_cpp.snowflake_read)
    ll.add_symbol('iceberg_pq_read', arrow_cpp.iceberg_pq_read)
MPI_ROOT = 0


class SqlReader(ir.Stmt):

    def __init__(self, sql_request: str, connection: str, df_out,
        df_colnames, out_vars, out_types, converted_colnames: List[str],
        db_type: str, loc, unsupported_columns: List[str],
        unsupported_arrow_types: List[pa.DataType], is_select_query: bool,
        has_side_effects: bool, index_column_name: str, index_column_type,
        database_schema: Optional[str], pyarrow_schema: Optional[pa.Schema],
        is_merge_into: bool, file_list_type, snapshot_id_type):
        self.connector_typ = 'sql'
        self.sql_request = sql_request
        self.connection = connection
        self.df_out = df_out
        self.df_colnames = df_colnames
        self.out_vars = out_vars
        self.out_types = out_types
        self.converted_colnames = converted_colnames
        self.loc = loc
        self.limit = req_limit(sql_request)
        self.db_type = db_type
        self.filters = None
        self.unsupported_columns = unsupported_columns
        self.unsupported_arrow_types = unsupported_arrow_types
        self.is_select_query = is_select_query
        self.has_side_effects = has_side_effects
        self.index_column_name = index_column_name
        self.index_column_type = index_column_type
        self.out_used_cols = list(range(len(df_colnames)))
        self.database_schema = database_schema
        self.pyarrow_schema = pyarrow_schema
        self.is_merge_into = is_merge_into
        self.is_live_table = True
        self.file_list_live = is_merge_into
        self.snapshot_id_live = is_merge_into
        if is_merge_into:
            self.file_list_type = file_list_type
            self.snapshot_id_type = snapshot_id_type
        else:
            self.file_list_type = types.none
            self.snapshot_id_type = types.none

    def __repr__(self):
        zsmm__phsyx = tuple(xqh__gqas.name for xqh__gqas in self.out_vars)
        return (
            f'{zsmm__phsyx} = SQLReader(sql_request={self.sql_request}, connection={self.connection}, col_names={self.df_colnames}, types={self.out_types}, df_out={self.df_out}, limit={self.limit}, unsupported_columns={self.unsupported_columns}, unsupported_arrow_types={self.unsupported_arrow_types}, is_select_query={self.is_select_query}, index_column_name={self.index_column_name}, index_column_type={self.index_column_type}, out_used_cols={self.out_used_cols}, database_schema={self.database_schema}, pyarrow_schema={self.pyarrow_schema}, is_merge_into={self.is_merge_into})'
            )


def parse_dbtype(con_str):
    gjak__ldmq = urlparse(con_str)
    db_type = gjak__ldmq.scheme
    uidbs__lnv = gjak__ldmq.password
    if con_str.startswith('oracle+cx_oracle://'):
        return 'oracle', uidbs__lnv
    if db_type == 'mysql+pymysql':
        return 'mysql', uidbs__lnv
    if con_str.startswith('iceberg+glue') or gjak__ldmq.scheme in ('iceberg',
        'iceberg+file', 'iceberg+s3', 'iceberg+thrift', 'iceberg+http',
        'iceberg+https'):
        return 'iceberg', uidbs__lnv
    return db_type, uidbs__lnv


def remove_iceberg_prefix(con):
    import sys
    if sys.version_info.minor < 9:
        if con.startswith('iceberg+'):
            con = con[len('iceberg+'):]
        if con.startswith('iceberg://'):
            con = con[len('iceberg://'):]
    else:
        con = con.removeprefix('iceberg+').removeprefix('iceberg://')
    return con


def remove_dead_sql(sql_node, lives_no_aliases, lives, arg_aliases,
    alias_map, func_ir, typemap):
    keod__gjer = sql_node.out_vars[0].name
    wrlox__hxs = sql_node.out_vars[1].name
    ltzl__bnjr = sql_node.out_vars[2].name if len(sql_node.out_vars
        ) > 2 else None
    bfh__zxvht = sql_node.out_vars[3].name if len(sql_node.out_vars
        ) > 3 else None
    if (not sql_node.has_side_effects and keod__gjer not in lives and 
        wrlox__hxs not in lives and ltzl__bnjr not in lives and bfh__zxvht
         not in lives):
        return None
    if keod__gjer not in lives:
        sql_node.out_types = []
        sql_node.df_colnames = []
        sql_node.out_used_cols = []
        sql_node.is_live_table = False
    if wrlox__hxs not in lives:
        sql_node.index_column_name = None
        sql_node.index_arr_typ = types.none
    if ltzl__bnjr not in lives:
        sql_node.file_list_live = False
        sql_node.file_list_type = types.none
    if bfh__zxvht not in lives:
        sql_node.snapshot_id_live = False
        sql_node.snapshot_id_type = types.none
    return sql_node


def sql_distributed_run(sql_node: SqlReader, array_dists, typemap,
    calltypes, typingctx, targetctx, is_independent=False,
    meta_head_only_info=None):
    if bodo.user_logging.get_verbose_level() >= 1:
        soa__odo = (
            'Finish column pruning on read_sql node:\n%s\nColumns loaded %s\n')
        ryrf__rcap = []
        dict_encoded_cols = []
        for zngd__vpmz in sql_node.out_used_cols:
            cdx__khfxi = sql_node.df_colnames[zngd__vpmz]
            ryrf__rcap.append(cdx__khfxi)
            if isinstance(sql_node.out_types[zngd__vpmz], bodo.libs.
                dict_arr_ext.DictionaryArrayType):
                dict_encoded_cols.append(cdx__khfxi)
        if sql_node.index_column_name:
            ryrf__rcap.append(sql_node.index_column_name)
            if isinstance(sql_node.index_column_type, bodo.libs.
                dict_arr_ext.DictionaryArrayType):
                dict_encoded_cols.append(sql_node.index_column_name)
        qhvi__hpwlk = sql_node.loc.strformat()
        bodo.user_logging.log_message('Column Pruning', soa__odo,
            qhvi__hpwlk, ryrf__rcap)
        if dict_encoded_cols:
            ryb__dbol = """Finished optimized encoding on read_sql node:
%s
Columns %s using dictionary encoding to reduce memory usage.
"""
            bodo.user_logging.log_message('Dictionary Encoding', ryb__dbol,
                qhvi__hpwlk, dict_encoded_cols)
    parallel = bodo.ir.connector.is_connector_table_parallel(sql_node,
        array_dists, typemap, 'SQLReader')
    if sql_node.unsupported_columns:
        mad__bagq = set(sql_node.unsupported_columns)
        dbyd__xkud = set(sql_node.out_used_cols)
        nsi__jkch = dbyd__xkud & mad__bagq
        if nsi__jkch:
            gwa__ppnd = sorted(nsi__jkch)
            fha__evtux = [
                f'pandas.read_sql(): 1 or more columns found with Arrow types that are not supported in Bodo and could not be eliminated. '
                 +
                'Please manually remove these columns from your sql query by specifying the columns you need in your SELECT statement. If these '
                 +
                'columns are needed, you will need to modify your dataset to use a supported type.'
                , 'Unsupported Columns:']
            axj__vimb = 0
            for xjuj__ehgnb in gwa__ppnd:
                while sql_node.unsupported_columns[axj__vimb] != xjuj__ehgnb:
                    axj__vimb += 1
                fha__evtux.append(
                    f"Column '{sql_node.original_df_colnames[xjuj__ehgnb]}' with unsupported arrow type {sql_node.unsupported_arrow_types[axj__vimb]}"
                    )
                axj__vimb += 1
            ndwmo__lab = '\n'.join(fha__evtux)
            raise BodoError(ndwmo__lab, loc=sql_node.loc)
    if sql_node.limit is None and (not meta_head_only_info or 
        meta_head_only_info[0] is None):
        limit = None
    elif sql_node.limit is None:
        limit = meta_head_only_info[0]
    elif not meta_head_only_info or meta_head_only_info[0] is None:
        limit = sql_node.limit
    else:
        limit = min(limit, meta_head_only_info[0])
    iblut__knqz, recet__ltded = bodo.ir.connector.generate_filter_map(sql_node
        .filters)
    zuy__psbhl = ', '.join(iblut__knqz.values())
    ffep__blny = (
        f'def sql_impl(sql_request, conn, database_schema, {zuy__psbhl}):\n')
    if sql_node.is_select_query and sql_node.db_type != 'iceberg':
        if sql_node.filters:
            ffl__vcgx = []
            for cpfw__qtlq in sql_node.filters:
                nqn__hbc = []
                for btb__nanl in cpfw__qtlq:
                    fbhjp__amnpq, ura__elgd = btb__nanl[0], btb__nanl[2]
                    fbhjp__amnpq = convert_col_name(fbhjp__amnpq, sql_node.
                        converted_colnames)
                    fbhjp__amnpq = '\\"' + fbhjp__amnpq + '\\"'
                    macpd__dyxur = '{' + iblut__knqz[btb__nanl[2].name
                        ] + '}' if isinstance(btb__nanl[2], ir.Var
                        ) else ura__elgd
                    if btb__nanl[1] in ('startswith', 'endswith'):
                        jyb__ftb = ['(', btb__nanl[1], '(', fbhjp__amnpq,
                            ',', macpd__dyxur, ')', ')']
                    else:
                        jyb__ftb = ['(', fbhjp__amnpq, btb__nanl[1],
                            macpd__dyxur, ')']
                    nqn__hbc.append(' '.join(jyb__ftb))
                ffl__vcgx.append(' ( ' + ' AND '.join(nqn__hbc) + ' ) ')
            brui__mvlon = ' WHERE ' + ' OR '.join(ffl__vcgx)
            for zngd__vpmz, tilxz__ziwc in enumerate(iblut__knqz.values()):
                ffep__blny += (
                    f'    {tilxz__ziwc} = get_sql_literal({tilxz__ziwc})\n')
            ffep__blny += (
                f'    sql_request = f"{{sql_request}} {brui__mvlon}"\n')
        if sql_node.limit != limit:
            ffep__blny += (
                f'    sql_request = f"{{sql_request}} LIMIT {limit}"\n')
    gld__psn = ''
    if sql_node.db_type == 'iceberg':
        gld__psn = zuy__psbhl
    ffep__blny += f"""    (total_rows, table_var, index_var, file_list, snapshot_id) = _sql_reader_py(sql_request, conn, database_schema, {gld__psn})
"""
    yjgno__pvtq = {}
    exec(ffep__blny, {}, yjgno__pvtq)
    vbqc__mkljc = yjgno__pvtq['sql_impl']
    xhyj__uunpp = _gen_sql_reader_py(sql_node.df_colnames, sql_node.
        out_types, sql_node.index_column_name, sql_node.index_column_type,
        sql_node.out_used_cols, sql_node.converted_colnames, typingctx,
        targetctx, sql_node.db_type, limit, parallel, typemap, sql_node.
        filters, sql_node.pyarrow_schema, not sql_node.is_live_table,
        sql_node.is_select_query, sql_node.is_merge_into, is_independent)
    ayomx__crn = (types.none if sql_node.database_schema is None else
        string_type)
    obvup__tnlj = compile_to_numba_ir(vbqc__mkljc, {'_sql_reader_py':
        xhyj__uunpp, 'bcast_scalar': bcast_scalar, 'bcast': bcast,
        'get_sql_literal': _get_snowflake_sql_literal}, typingctx=typingctx,
        targetctx=targetctx, arg_typs=(string_type, string_type, ayomx__crn
        ) + tuple(typemap[xqh__gqas.name] for xqh__gqas in recet__ltded),
        typemap=typemap, calltypes=calltypes).blocks.popitem()[1]
    if sql_node.is_select_query and sql_node.db_type != 'iceberg':
        vdt__atmc = [sql_node.df_colnames[zngd__vpmz] for zngd__vpmz in
            sql_node.out_used_cols]
        if sql_node.index_column_name:
            vdt__atmc.append(sql_node.index_column_name)
        if len(vdt__atmc) == 0:
            cwds__uif = 'COUNT(*)'
        else:
            cwds__uif = escape_column_names(vdt__atmc, sql_node.db_type,
                sql_node.converted_colnames)
        if sql_node.db_type == 'oracle':
            cmi__djorc = ('SELECT ' + cwds__uif + ' FROM (' + sql_node.
                sql_request + ') TEMP')
        else:
            cmi__djorc = ('SELECT ' + cwds__uif + ' FROM (' + sql_node.
                sql_request + ') as TEMP')
    else:
        cmi__djorc = sql_node.sql_request
    replace_arg_nodes(obvup__tnlj, [ir.Const(cmi__djorc, sql_node.loc), ir.
        Const(sql_node.connection, sql_node.loc), ir.Const(sql_node.
        database_schema, sql_node.loc)] + recet__ltded)
    lcfps__jyk = obvup__tnlj.body[:-3]
    if meta_head_only_info:
        lcfps__jyk[-5].target = meta_head_only_info[1]
    lcfps__jyk[-4].target = sql_node.out_vars[0]
    lcfps__jyk[-3].target = sql_node.out_vars[1]
    assert sql_node.has_side_effects or not (sql_node.index_column_name is
        None and not sql_node.is_live_table
        ), 'At most one of table and index should be dead if the SQL IR node is live and has no side effects'
    if sql_node.index_column_name is None:
        lcfps__jyk.pop(-3)
    elif not sql_node.is_live_table:
        lcfps__jyk.pop(-4)
    if sql_node.file_list_live:
        lcfps__jyk[-2].target = sql_node.out_vars[2]
    else:
        lcfps__jyk.pop(-2)
    if sql_node.snapshot_id_live:
        lcfps__jyk[-1].target = sql_node.out_vars[3]
    else:
        lcfps__jyk.pop(-1)
    return lcfps__jyk


def convert_col_name(col_name: str, converted_colnames: List[str]) ->str:
    if col_name in converted_colnames:
        return col_name.upper()
    return col_name


def escape_column_names(col_names, db_type, converted_colnames):
    if db_type == 'snowflake':
        from bodo.io.snowflake import escape_col_name
        cwds__uif = ', '.join(escape_col_name(convert_col_name(eojp__upt,
            converted_colnames)) for eojp__upt in col_names)
    elif db_type == 'oracle':
        vdt__atmc = []
        for eojp__upt in col_names:
            vdt__atmc.append(convert_col_name(eojp__upt, converted_colnames))
        cwds__uif = ', '.join([f'"{eojp__upt}"' for eojp__upt in vdt__atmc])
    elif db_type == 'mysql':
        cwds__uif = ', '.join([f'`{eojp__upt}`' for eojp__upt in col_names])
    else:
        cwds__uif = ', '.join([f'"{eojp__upt}"' for eojp__upt in col_names])
    return cwds__uif


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def _get_snowflake_sql_literal_scalar(filter_value):
    dxj__okaj = types.unliteral(filter_value)
    if dxj__okaj == types.unicode_type:
        return lambda filter_value: f'$${filter_value}$$'
    elif isinstance(dxj__okaj, (types.Integer, types.Float)
        ) or filter_value == types.bool_:
        return lambda filter_value: str(filter_value)
    elif isinstance(dxj__okaj, bodo.PandasTimestampType):
        if dxj__okaj.tz is None:
            xlnv__bohn = 'TIMESTAMP_NTZ'
        else:
            xlnv__bohn = 'TIMESTAMP_TZ'

        def impl(filter_value):
            enjy__sulmy = filter_value.nanosecond
            kbk__cqenc = ''
            if enjy__sulmy < 10:
                kbk__cqenc = '00'
            elif enjy__sulmy < 100:
                kbk__cqenc = '0'
            return (
                f"timestamp '{filter_value.strftime('%Y-%m-%d %H:%M:%S.%f')}{kbk__cqenc}{enjy__sulmy}'::{xlnv__bohn}"
                )
        return impl
    elif dxj__okaj == bodo.datetime_date_type:
        return (lambda filter_value:
            f"date '{filter_value.strftime('%Y-%m-%d')}'")
    else:
        raise BodoError(
            f'pd.read_sql(): Internal error, unsupported scalar type {dxj__okaj} used in filter pushdown.'
            )


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def _get_snowflake_sql_literal(filter_value):
    scalar_isinstance = types.Integer, types.Float, bodo.PandasTimestampType
    onuwk__mbf = bodo.datetime_date_type, types.unicode_type, types.bool_
    dxj__okaj = types.unliteral(filter_value)
    if (isinstance(dxj__okaj, (types.List, types.Array, bodo.
        IntegerArrayType, bodo.FloatingArrayType, bodo.DatetimeArrayType)) or
        dxj__okaj in (bodo.string_array_type, bodo.dict_str_arr_type, bodo.
        boolean_array, bodo.datetime_date_array_type)) and (isinstance(
        dxj__okaj.dtype, scalar_isinstance) or dxj__okaj.dtype in onuwk__mbf):

        def impl(filter_value):
            ifctq__jqk = ', '.join([_get_snowflake_sql_literal_scalar(
                eojp__upt) for eojp__upt in filter_value])
            return f'({ifctq__jqk})'
        return impl
    elif isinstance(dxj__okaj, scalar_isinstance) or dxj__okaj in onuwk__mbf:
        return lambda filter_value: _get_snowflake_sql_literal_scalar(
            filter_value)
    else:
        raise BodoError(
            f'pd.read_sql(): Internal error, unsupported type {dxj__okaj} used in filter pushdown.'
            )


def sql_remove_dead_column(sql_node, column_live_map, equiv_vars, typemap):
    return bodo.ir.connector.base_connector_remove_dead_columns(sql_node,
        column_live_map, equiv_vars, typemap, 'SQLReader', sql_node.
        df_colnames, require_one_column=sql_node.db_type not in ('iceberg',
        'snowflake'))


numba.parfors.array_analysis.array_analysis_extensions[SqlReader
    ] = bodo.ir.connector.connector_array_analysis
distributed_analysis.distributed_analysis_extensions[SqlReader
    ] = bodo.ir.connector.connector_distributed_analysis
typeinfer.typeinfer_extensions[SqlReader
    ] = bodo.ir.connector.connector_typeinfer
ir_utils.visit_vars_extensions[SqlReader
    ] = bodo.ir.connector.visit_vars_connector
ir_utils.remove_dead_extensions[SqlReader] = remove_dead_sql
numba.core.analysis.ir_extension_usedefs[SqlReader
    ] = bodo.ir.connector.connector_usedefs
ir_utils.copy_propagate_extensions[SqlReader
    ] = bodo.ir.connector.get_copies_connector
ir_utils.apply_copy_propagate_extensions[SqlReader
    ] = bodo.ir.connector.apply_copies_connector
ir_utils.build_defs_extensions[SqlReader
    ] = bodo.ir.connector.build_connector_definitions
distributed_pass.distributed_run_extensions[SqlReader] = sql_distributed_run
remove_dead_column_extensions[SqlReader] = sql_remove_dead_column
ir_extension_table_column_use[SqlReader
    ] = bodo.ir.connector.connector_table_column_use
compiled_funcs = []


@numba.njit
def sqlalchemy_check():
    with numba.objmode():
        sqlalchemy_check_()


def sqlalchemy_check_():
    try:
        import sqlalchemy
    except ImportError as zoxtu__gjwp:
        jmzjv__qurnt = (
            "Using URI string without sqlalchemy installed. sqlalchemy can be installed by calling 'conda install -c conda-forge sqlalchemy'."
            )
        raise BodoError(jmzjv__qurnt)


@numba.njit
def pymysql_check():
    with numba.objmode():
        pymysql_check_()


def pymysql_check_():
    try:
        import pymysql
    except ImportError as zoxtu__gjwp:
        jmzjv__qurnt = (
            "Using MySQL URI string requires pymsql to be installed. It can be installed by calling 'conda install -c conda-forge pymysql' or 'pip install PyMySQL'."
            )
        raise BodoError(jmzjv__qurnt)


@numba.njit
def cx_oracle_check():
    with numba.objmode():
        cx_oracle_check_()


def cx_oracle_check_():
    try:
        import cx_Oracle
    except ImportError as zoxtu__gjwp:
        jmzjv__qurnt = (
            "Using Oracle URI string requires cx_oracle to be installed. It can be installed by calling 'conda install -c conda-forge cx_oracle' or 'pip install cx-Oracle'."
            )
        raise BodoError(jmzjv__qurnt)


@numba.njit
def psycopg2_check():
    with numba.objmode():
        psycopg2_check_()


def psycopg2_check_():
    try:
        import psycopg2
    except ImportError as zoxtu__gjwp:
        jmzjv__qurnt = (
            "Using PostgreSQL URI string requires psycopg2 to be installed. It can be installed by calling 'conda install -c conda-forge psycopg2' or 'pip install psycopg2'."
            )
        raise BodoError(jmzjv__qurnt)


def req_limit(sql_request):
    import re
    fnlm__drs = re.compile('LIMIT\\s+(\\d+)\\s*$', re.IGNORECASE)
    qwjd__wmj = fnlm__drs.search(sql_request)
    if qwjd__wmj:
        return int(qwjd__wmj.group(1))
    else:
        return None


def _gen_sql_reader_py(col_names: List[str], col_typs: List[Any],
    index_column_name: Optional[str], index_column_type, out_used_cols:
    List[int], converted_colnames: List[str], typingctx, targetctx, db_type:
    str, limit: Optional[int], parallel: bool, typemap, filters: Optional[
    Any], pyarrow_schema: Optional[pa.Schema], is_dead_table: bool,
    is_select_query: bool, is_merge_into: bool, is_independent: bool):
    kelj__yqr = next_label()
    vdt__atmc = [col_names[zngd__vpmz] for zngd__vpmz in out_used_cols]
    jtdzs__znlz = [col_typs[zngd__vpmz] for zngd__vpmz in out_used_cols]
    if index_column_name:
        vdt__atmc.append(index_column_name)
        jtdzs__znlz.append(index_column_type)
    uylf__apk = None
    gxnv__vjbdt = None
    plkdy__rcocf = types.none if is_dead_table else TableType(tuple(col_typs))
    gld__psn = ''
    iblut__knqz = {}
    recet__ltded = []
    if filters and db_type == 'iceberg':
        iblut__knqz, recet__ltded = bodo.ir.connector.generate_filter_map(
            filters)
        gld__psn = ', '.join(iblut__knqz.values())
    ffep__blny = (
        f'def sql_reader_py(sql_request, conn, database_schema, {gld__psn}):\n'
        )
    if db_type == 'iceberg':
        assert pyarrow_schema is not None, 'SQLNode must contain a pyarrow_schema if reading from an Iceberg database'
        vvheq__jxn, pbnx__wqi = bodo.ir.connector.generate_arrow_filters(
            filters, iblut__knqz, recet__ltded, col_names, col_names,
            col_typs, typemap, 'iceberg')
        rkddv__gvq = -1
        if is_merge_into and col_names.index('_bodo_row_id') in out_used_cols:
            rkddv__gvq = col_names.index('_bodo_row_id')
        selected_cols: List[int] = [pyarrow_schema.get_field_index(
            col_names[zngd__vpmz]) for zngd__vpmz in out_used_cols if 
            zngd__vpmz != rkddv__gvq]
        ojeo__hgqtn = {oon__rvua: zngd__vpmz for zngd__vpmz, oon__rvua in
            enumerate(selected_cols)}
        nullable_cols = [int(is_nullable(col_typs[zngd__vpmz])) for
            zngd__vpmz in selected_cols]
        uxfu__mpycs = [zngd__vpmz for zngd__vpmz in selected_cols if 
            col_typs[zngd__vpmz] == bodo.dict_str_arr_type]
        eeurn__wvofa = (
            f'dict_str_cols_arr_{kelj__yqr}.ctypes, np.int32({len(uxfu__mpycs)})'
             if uxfu__mpycs else '0, 0')
        lpe__bicd = ',' if gld__psn else ''
        ffep__blny += f"""  ev = bodo.utils.tracing.Event('read_iceberg', {parallel})
  dnf_filters, expr_filters = get_filters_pyobject("{vvheq__jxn}", "{pbnx__wqi}", ({gld__psn}{lpe__bicd}))
  out_table, total_rows, file_list, snapshot_id = iceberg_read(
    unicode_to_utf8(conn),
    unicode_to_utf8(database_schema),
    unicode_to_utf8(sql_request),
    {parallel},
    {-1 if limit is None else limit},
    dnf_filters,
    expr_filters,
    selected_cols_arr_{kelj__yqr}.ctypes,
    {len(selected_cols)},
    nullable_cols_arr_{kelj__yqr}.ctypes,
    pyarrow_schema_{kelj__yqr},
    {eeurn__wvofa},
    {is_merge_into},
  )
"""
        if parallel:
            ffep__blny += f"""  local_rows = get_node_portion(total_rows, bodo.get_size(), bodo.get_rank())
"""
        else:
            ffep__blny += f'  local_rows = total_rows\n'
        uylf__apk = None
        if not is_dead_table:
            uylf__apk = []
            zuvf__rfb = 0
            for zngd__vpmz in range(len(col_names)):
                if zuvf__rfb < len(out_used_cols
                    ) and zngd__vpmz == out_used_cols[zuvf__rfb]:
                    if zngd__vpmz == rkddv__gvq:
                        uylf__apk.append(len(selected_cols))
                    else:
                        uylf__apk.append(ojeo__hgqtn[zngd__vpmz])
                    zuvf__rfb += 1
                else:
                    uylf__apk.append(-1)
            uylf__apk = np.array(uylf__apk, dtype=np.int64)
        if is_dead_table:
            ffep__blny += '  table_var = None\n'
        else:
            ffep__blny += f"""  table_var = cpp_table_to_py_table(out_table, table_idx_{kelj__yqr}, py_table_type_{kelj__yqr})
"""
            if len(out_used_cols) == 0:
                ffep__blny += (
                    f'  table_var = set_table_len(table_var, local_rows)\n')
        wrlox__hxs = 'None'
        if index_column_name is not None:
            cyxxr__ybx = len(out_used_cols) + 1 if not is_dead_table else 0
            wrlox__hxs = (
                f'info_to_array(info_from_table(out_table, {cyxxr__ybx}), index_col_typ)'
                )
        ffep__blny += f'  index_var = {wrlox__hxs}\n'
        ffep__blny += f'  delete_table(out_table)\n'
        ffep__blny += f'  ev.finalize()\n'
        ffep__blny += (
            '  return (total_rows, table_var, index_var, file_list, snapshot_id)\n'
            )
    elif db_type == 'snowflake':
        assert pyarrow_schema is not None, 'SQLNode must contain a pyarrow_schema if reading from Snowflake'
        if is_select_query:
            wrjb__hprgy = []
            for col_name in vdt__atmc:
                porv__mifop = convert_col_name(col_name, converted_colnames)
                axj__vimb = pyarrow_schema.get_field_index(porv__mifop)
                if axj__vimb < 0:
                    raise BodoError(
                        f'SQLReader Snowflake: Column {porv__mifop} is not in source schema'
                        )
                wrjb__hprgy.append(pyarrow_schema.field(axj__vimb))
            pyarrow_schema = pa.schema(wrjb__hprgy)
        kygav__ckwx = {oon__rvua: zngd__vpmz for zngd__vpmz, oon__rvua in
            enumerate(out_used_cols)}
        hrltu__uciu = [kygav__ckwx[zngd__vpmz] for zngd__vpmz in
            out_used_cols if col_typs[zngd__vpmz] == dict_str_arr_type]
        nullable_cols = [int(is_nullable(col_typs[zngd__vpmz])) for
            zngd__vpmz in out_used_cols]
        if index_column_name:
            nullable_cols.append(int(is_nullable(index_column_type)))
        dtyt__mla = np.array(hrltu__uciu, dtype=np.int32)
        wti__ypav = np.array(nullable_cols, dtype=np.int32)
        ffep__blny += f"""  ev = bodo.utils.tracing.Event('read_snowflake', {parallel})
  total_rows_np = np.array([0], dtype=np.int64)
  out_table = snowflake_read(
    unicode_to_utf8(sql_request),
    unicode_to_utf8(conn),
    {parallel},
    {is_independent},
    pyarrow_schema_{kelj__yqr},
    {len(wti__ypav)},
    nullable_cols_array.ctypes,
    snowflake_dict_cols_array.ctypes,
    {len(dtyt__mla)},
    total_rows_np.ctypes,
    {is_select_query and len(vdt__atmc) == 0},
    {is_select_query},
  )
  check_and_propagate_cpp_exception()
"""
        ffep__blny += f'  total_rows = total_rows_np[0]\n'
        if parallel:
            ffep__blny += f"""  local_rows = get_node_portion(total_rows, bodo.get_size(), bodo.get_rank())
"""
        else:
            ffep__blny += f'  local_rows = total_rows\n'
        if index_column_name:
            ffep__blny += f"""  index_var = info_to_array(info_from_table(out_table, {len(out_used_cols)}), index_col_typ)
"""
        else:
            ffep__blny += '  index_var = None\n'
        if not is_dead_table:
            axj__vimb = []
            zuvf__rfb = 0
            for zngd__vpmz in range(len(col_names)):
                if zuvf__rfb < len(out_used_cols
                    ) and zngd__vpmz == out_used_cols[zuvf__rfb]:
                    axj__vimb.append(zuvf__rfb)
                    zuvf__rfb += 1
                else:
                    axj__vimb.append(-1)
            uylf__apk = np.array(axj__vimb, dtype=np.int64)
            ffep__blny += f"""  table_var = cpp_table_to_py_table(out_table, table_idx_{kelj__yqr}, py_table_type_{kelj__yqr})
"""
            if len(out_used_cols) == 0:
                if index_column_name:
                    ffep__blny += (
                        f'  table_var = set_table_len(table_var, len(index_var))\n'
                        )
                else:
                    ffep__blny += (
                        f'  table_var = set_table_len(table_var, local_rows)\n'
                        )
        else:
            ffep__blny += '  table_var = None\n'
        ffep__blny += '  delete_table(out_table)\n'
        ffep__blny += '  ev.finalize()\n'
        ffep__blny += (
            '  return (total_rows, table_var, index_var, None, None)\n')
    else:
        if not is_dead_table:
            ffep__blny += f"""  type_usecols_offsets_arr_{kelj__yqr}_2 = type_usecols_offsets_arr_{kelj__yqr}
"""
            gxnv__vjbdt = np.array(out_used_cols, dtype=np.int64)
        ffep__blny += '  df_typeref_2 = df_typeref\n'
        ffep__blny += '  sqlalchemy_check()\n'
        if db_type == 'mysql':
            ffep__blny += '  pymysql_check()\n'
        elif db_type == 'oracle':
            ffep__blny += '  cx_oracle_check()\n'
        elif db_type == 'postgresql' or db_type == 'postgresql+psycopg2':
            ffep__blny += '  psycopg2_check()\n'
        if parallel:
            ffep__blny += '  rank = bodo.libs.distributed_api.get_rank()\n'
            if limit is not None:
                ffep__blny += f'  nb_row = {limit}\n'
            else:
                ffep__blny += '  with objmode(nb_row="int64"):\n'
                ffep__blny += f'     if rank == {MPI_ROOT}:\n'
                ffep__blny += """         sql_cons = 'select count(*) from (' + sql_request + ') x'
"""
                ffep__blny += '         frame = pd.read_sql(sql_cons, conn)\n'
                ffep__blny += '         nb_row = frame.iat[0,0]\n'
                ffep__blny += '     else:\n'
                ffep__blny += '         nb_row = 0\n'
                ffep__blny += '  nb_row = bcast_scalar(nb_row)\n'
            ffep__blny += f"""  with objmode(table_var=py_table_type_{kelj__yqr}, index_var=index_col_typ):
"""
            ffep__blny += (
                '    offset, limit = bodo.libs.distributed_api.get_start_count(nb_row)\n'
                )
            if db_type == 'oracle':
                ffep__blny += f"""    sql_cons = 'select * from (' + sql_request + ') OFFSET ' + str(offset) + ' ROWS FETCH NEXT ' + str(limit) + ' ROWS ONLY'
"""
            else:
                ffep__blny += f"""    sql_cons = 'select * from (' + sql_request + ') x LIMIT ' + str(limit) + ' OFFSET ' + str(offset)
"""
            ffep__blny += '    df_ret = pd.read_sql(sql_cons, conn)\n'
            ffep__blny += (
                '    bodo.ir.connector.cast_float_to_nullable(df_ret, df_typeref_2)\n'
                )
        else:
            ffep__blny += f"""  with objmode(table_var=py_table_type_{kelj__yqr}, index_var=index_col_typ):
"""
            ffep__blny += '    df_ret = pd.read_sql(sql_request, conn)\n'
            ffep__blny += (
                '    bodo.ir.connector.cast_float_to_nullable(df_ret, df_typeref_2)\n'
                )
        if index_column_name:
            ffep__blny += (
                f'    index_var = df_ret.iloc[:, {len(out_used_cols)}].values\n'
                )
            ffep__blny += f"""    df_ret.drop(columns=df_ret.columns[{len(out_used_cols)}], inplace=True)
"""
        else:
            ffep__blny += '    index_var = None\n'
        if not is_dead_table:
            ffep__blny += f'    arrs = []\n'
            ffep__blny += f'    for i in range(df_ret.shape[1]):\n'
            ffep__blny += f'      arrs.append(df_ret.iloc[:, i].values)\n'
            ffep__blny += f"""    table_var = Table(arrs, type_usecols_offsets_arr_{kelj__yqr}_2, {len(col_names)})
"""
        else:
            ffep__blny += '    table_var = None\n'
        ffep__blny += '  return (-1, table_var, index_var, None, None)\n'
    rmqtm__pxfhg = globals()
    rmqtm__pxfhg.update({'bodo': bodo, f'py_table_type_{kelj__yqr}':
        plkdy__rcocf, 'index_col_typ': index_column_type})
    if db_type in ('iceberg', 'snowflake'):
        rmqtm__pxfhg.update({f'table_idx_{kelj__yqr}': uylf__apk,
            f'pyarrow_schema_{kelj__yqr}': pyarrow_schema,
            'unicode_to_utf8': unicode_to_utf8,
            'check_and_propagate_cpp_exception':
            check_and_propagate_cpp_exception, 'info_to_array':
            info_to_array, 'info_from_table': info_from_table,
            'delete_table': delete_table, 'cpp_table_to_py_table':
            cpp_table_to_py_table, 'set_table_len': bodo.hiframes.table.
            set_table_len, 'get_node_portion': bodo.libs.distributed_api.
            get_node_portion})
    if db_type == 'iceberg':
        rmqtm__pxfhg.update({f'selected_cols_arr_{kelj__yqr}': np.array(
            selected_cols, np.int32), f'nullable_cols_arr_{kelj__yqr}': np.
            array(nullable_cols, np.int32),
            f'dict_str_cols_arr_{kelj__yqr}': np.array(uxfu__mpycs, np.
            int32), f'py_table_type_{kelj__yqr}': plkdy__rcocf,
            'get_filters_pyobject': bodo.io.parquet_pio.
            get_filters_pyobject, 'iceberg_read': _iceberg_pq_read})
    elif db_type == 'snowflake':
        rmqtm__pxfhg.update({'np': np, 'snowflake_read': _snowflake_read,
            'nullable_cols_array': wti__ypav, 'snowflake_dict_cols_array':
            dtyt__mla})
    else:
        rmqtm__pxfhg.update({'sqlalchemy_check': sqlalchemy_check, 'pd': pd,
            'objmode': objmode, 'bcast_scalar': bcast_scalar,
            'pymysql_check': pymysql_check, 'cx_oracle_check':
            cx_oracle_check, 'psycopg2_check': psycopg2_check, 'df_typeref':
            bodo.DataFrameType(tuple(jtdzs__znlz), bodo.RangeIndexType(None
            ), tuple(vdt__atmc)), 'Table': Table,
            f'type_usecols_offsets_arr_{kelj__yqr}': gxnv__vjbdt})
    yjgno__pvtq = {}
    exec(ffep__blny, rmqtm__pxfhg, yjgno__pvtq)
    xhyj__uunpp = yjgno__pvtq['sql_reader_py']
    suo__vhdgg = numba.njit(xhyj__uunpp)
    compiled_funcs.append(suo__vhdgg)
    return suo__vhdgg


parquet_predicate_type = ParquetPredicateType()
pyarrow_schema_type = PyArrowTableSchemaType()


@intrinsic
def _iceberg_pq_read(typingctx, conn_str, db_schema, sql_request_str,
    parallel, limit, dnf_filters, expr_filters, selected_cols,
    num_selected_cols, nullable_cols, pyarrow_schema, dict_encoded_cols,
    num_dict_encoded_cols, is_merge_into_cow):

    def codegen(context, builder, signature, args):
        gwp__myn = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(8).as_pointer(), lir.
            IntType(8).as_pointer(), lir.IntType(1), lir.IntType(64), lir.
            IntType(8).as_pointer(), lir.IntType(8).as_pointer(), lir.
            IntType(8).as_pointer(), lir.IntType(32), lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(32), lir.IntType(1), lir.IntType(64).
            as_pointer(), lir.IntType(8).as_pointer().as_pointer(), lir.
            IntType(64).as_pointer()])
        kyo__fsaj = cgutils.get_or_insert_function(builder.module, gwp__myn,
            name='iceberg_pq_read')
        jhf__cxxe = cgutils.alloca_once(builder, lir.IntType(64))
        hdbf__zcvpd = cgutils.alloca_once(builder, lir.IntType(8).as_pointer())
        rld__hcv = cgutils.alloca_once(builder, lir.IntType(64))
        hlh__xxoz = args + (jhf__cxxe, hdbf__zcvpd, rld__hcv)
        xyuq__hkk = builder.call(kyo__fsaj, hlh__xxoz)
        bodo.utils.utils.inlined_check_and_propagate_cpp_exception(context,
            builder)
        lxy__tzek = builder.load(hdbf__zcvpd)
        dofbl__gvye = cgutils.create_struct_proxy(types.pyobject_of_list_type)(
            context, builder)
        szyc__aidyi = context.get_python_api(builder)
        dofbl__gvye.meminfo = szyc__aidyi.nrt_meminfo_new_from_pyobject(context
            .get_constant_null(types.voidptr), lxy__tzek)
        dofbl__gvye.pyobj = lxy__tzek
        szyc__aidyi.decref(lxy__tzek)
        hxq__ghyq = [xyuq__hkk, builder.load(jhf__cxxe), dofbl__gvye.
            _getvalue(), builder.load(rld__hcv)]
        return context.make_tuple(builder, wack__wvq, hxq__ghyq)
    wack__wvq = types.Tuple([table_type, types.int64, types.
        pyobject_of_list_type, types.int64])
    mgo__ycdp = wack__wvq(types.voidptr, types.voidptr, types.voidptr,
        types.boolean, types.int64, parquet_predicate_type,
        parquet_predicate_type, types.voidptr, types.int32, types.voidptr,
        pyarrow_schema_type, types.voidptr, types.int32, types.boolean)
    return mgo__ycdp, codegen


_snowflake_read = types.ExternalFunction('snowflake_read', table_type(types
    .voidptr, types.voidptr, types.boolean, types.boolean,
    pyarrow_schema_type, types.int64, types.voidptr, types.voidptr, types.
    int32, types.voidptr, types.boolean, types.boolean))
