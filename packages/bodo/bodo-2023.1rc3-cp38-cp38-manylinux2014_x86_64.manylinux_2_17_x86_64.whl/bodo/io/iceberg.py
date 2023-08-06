"""
File that contains the main functionality for the Iceberg
integration within the Bodo repo. This does not contain the
main IR transformation.
"""
import os
import re
import sys
from typing import Any, Dict, List, Tuple
from urllib.parse import urlparse
import numba
import numpy as np
import pandas as pd
import pyarrow as pa
from mpi4py import MPI
from numba.core import types
from numba.extending import intrinsic
import bodo
from bodo.io.fs_io import get_s3_bucket_region_njit
from bodo.io.helpers import _get_numba_typ_from_pa_typ, pyarrow_table_schema_type
from bodo.libs.array import arr_info_list_to_table, array_to_info, py_table_to_cpp_table
from bodo.libs.str_ext import unicode_to_utf8
from bodo.utils import tracing
from bodo.utils.py_objs import install_py_obj_class
from bodo.utils.typing import BodoError


def format_iceberg_conn(conn_str: str) ->str:
    durk__grp = urlparse(conn_str)
    if not conn_str.startswith('iceberg+glue') and durk__grp.scheme not in (
        'iceberg', 'iceberg+file', 'iceberg+s3', 'iceberg+thrift',
        'iceberg+http', 'iceberg+https'):
        raise BodoError(
            "'con' must start with one of the following: 'iceberg://', 'iceberg+file://', 'iceberg+s3://', 'iceberg+thrift://', 'iceberg+http://', 'iceberg+https://', 'iceberg+glue'"
            )
    if sys.version_info.minor < 9:
        if conn_str.startswith('iceberg+'):
            conn_str = conn_str[len('iceberg+'):]
        if conn_str.startswith('iceberg://'):
            conn_str = conn_str[len('iceberg://'):]
    else:
        conn_str = conn_str.removeprefix('iceberg+').removeprefix('iceberg://')
    return conn_str


@numba.njit
def format_iceberg_conn_njit(conn_str):
    with numba.objmode(conn_str='unicode_type'):
        conn_str = format_iceberg_conn(conn_str)
    return conn_str


def get_iceberg_type_info(table_name: str, con: str, database_schema: str,
    is_merge_into_cow: bool=False):
    import bodo_iceberg_connector
    import numba.core
    lio__ouzb = None
    gbyg__dkoo = None
    tqzp__ehzmq = None
    if bodo.get_rank() == 0:
        try:
            lio__ouzb, gbyg__dkoo, tqzp__ehzmq = (bodo_iceberg_connector.
                get_iceberg_typing_schema(con, database_schema, table_name))
            if tqzp__ehzmq is None:
                raise BodoError('No such Iceberg table found')
        except bodo_iceberg_connector.IcebergError as aymv__qkv:
            if isinstance(aymv__qkv, bodo_iceberg_connector.IcebergJavaError
                ) and numba.core.config.DEVELOPER_MODE:
                lio__ouzb = BodoError(
                    f'{aymv__qkv.message}: {aymv__qkv.java_error}')
            else:
                lio__ouzb = BodoError(aymv__qkv.message)
    nkkb__yac = MPI.COMM_WORLD
    lio__ouzb = nkkb__yac.bcast(lio__ouzb)
    if isinstance(lio__ouzb, Exception):
        raise lio__ouzb
    col_names = lio__ouzb
    gbyg__dkoo = nkkb__yac.bcast(gbyg__dkoo)
    tqzp__ehzmq = nkkb__yac.bcast(tqzp__ehzmq)
    trz__xpd = [_get_numba_typ_from_pa_typ(typ, False, True, None)[0] for
        typ in gbyg__dkoo]
    if is_merge_into_cow:
        col_names.append('_bodo_row_id')
        trz__xpd.append(types.Array(types.int64, 1, 'C'))
    return col_names, trz__xpd, tqzp__ehzmq


def get_iceberg_file_list(table_name: str, conn: str, database_schema: str,
    filters) ->Tuple[List[str], List[str]]:
    import bodo_iceberg_connector
    import numba.core
    assert bodo.get_rank(
        ) == 0, 'get_iceberg_file_list should only ever be called on rank 0, as the operation requires access to the py4j server, which is only available on rank 0'
    try:
        cffyz__dmjha = (bodo_iceberg_connector.
            bodo_connector_get_parquet_file_list(conn, database_schema,
            table_name, filters))
    except bodo_iceberg_connector.IcebergError as aymv__qkv:
        if isinstance(aymv__qkv, bodo_iceberg_connector.IcebergJavaError
            ) and numba.core.config.DEVELOPER_MODE:
            raise BodoError(f'{aymv__qkv.message}:\n{aymv__qkv.java_error}')
        else:
            raise BodoError(aymv__qkv.message)
    return cffyz__dmjha


def get_iceberg_snapshot_id(table_name: str, conn: str, database_schema: str):
    import bodo_iceberg_connector
    import numba.core
    assert bodo.get_rank(
        ) == 0, 'get_iceberg_snapshot_id should only ever be called on rank 0, as the operation requires access to the py4j server, which is only available on rank 0'
    try:
        snapshot_id = (bodo_iceberg_connector.
            bodo_connector_get_current_snapshot_id(conn, database_schema,
            table_name))
    except bodo_iceberg_connector.IcebergError as aymv__qkv:
        if isinstance(aymv__qkv, bodo_iceberg_connector.IcebergJavaError
            ) and numba.core.config.DEVELOPER_MODE:
            raise BodoError(f'{aymv__qkv.message}:\n{aymv__qkv.java_error}')
        else:
            raise BodoError(aymv__qkv.message)
    return snapshot_id


class IcebergParquetDataset:

    def __init__(self, conn, database_schema, table_name, pa_table_schema,
        pq_file_list, snapshot_id, pq_dataset=None):
        self.pq_dataset = pq_dataset
        self.conn = conn
        self.database_schema = database_schema
        self.table_name = table_name
        self.schema = pa_table_schema
        self.file_list = pq_file_list
        self.snapshot_id = snapshot_id
        self.pieces = []
        self._bodo_total_rows = 0
        self._prefix = ''
        self.filesystem = None
        if pq_dataset is not None:
            self.pieces = pq_dataset.pieces
            self._bodo_total_rows = pq_dataset._bodo_total_rows
            self._prefix = pq_dataset._prefix
            self.filesystem = pq_dataset.filesystem


def get_iceberg_pq_dataset(conn: str, database_schema: str, table_name: str,
    typing_pa_table_schema: pa.Schema, dnf_filters=None, expr_filters=None,
    tot_rows_to_read=None, is_parallel=False, get_row_counts=True):
    cfu__yclk = get_row_counts and tracing.is_tracing()
    if cfu__yclk:
        cqusz__scl = tracing.Event('get_iceberg_pq_dataset')
    nkkb__yac = MPI.COMM_WORLD
    nkjx__qjaj = None
    jfzc__izt = None
    xcf__liu = None
    if bodo.get_rank() == 0:
        if cfu__yclk:
            ksoe__ext = tracing.Event('get_iceberg_file_list', is_parallel=
                False)
            ksoe__ext.add_attribute('g_dnf_filter', str(dnf_filters))
        try:
            nkjx__qjaj, xcf__liu = get_iceberg_file_list(table_name, conn,
                database_schema, dnf_filters)
            if cfu__yclk:
                hpc__yhhp = int(os.environ.get(
                    'BODO_ICEBERG_TRACING_NUM_FILES_TO_LOG', '50'))
                ksoe__ext.add_attribute('num_files', len(nkjx__qjaj))
                ksoe__ext.add_attribute(f'first_{hpc__yhhp}_files', ', '.
                    join(nkjx__qjaj[:hpc__yhhp]))
        except Exception as aymv__qkv:
            nkjx__qjaj = aymv__qkv
        if cfu__yclk:
            ksoe__ext.finalize()
            zahf__atcgm = tracing.Event('get_snapshot_id', is_parallel=False)
        try:
            jfzc__izt = get_iceberg_snapshot_id(table_name, conn,
                database_schema)
        except Exception as aymv__qkv:
            jfzc__izt = aymv__qkv
        if cfu__yclk:
            zahf__atcgm.finalize()
    nkjx__qjaj, jfzc__izt, xcf__liu = nkkb__yac.bcast((nkjx__qjaj,
        jfzc__izt, xcf__liu))
    if isinstance(nkjx__qjaj, Exception):
        utwjr__nejl = nkjx__qjaj
        raise BodoError(
            f"""Error reading Iceberg Table: {type(utwjr__nejl).__name__}: {str(utwjr__nejl)}
"""
            )
    if isinstance(jfzc__izt, Exception):
        utwjr__nejl = jfzc__izt
        raise BodoError(
            f"""Error reading Iceberg Table: {type(utwjr__nejl).__name__}: {str(utwjr__nejl)}
"""
            )
    lohtm__fgfvd: List[str] = nkjx__qjaj
    snapshot_id: int = jfzc__izt
    if len(lohtm__fgfvd) == 0:
        pq_dataset = None
    else:
        try:
            pq_dataset = bodo.io.parquet_pio.get_parquet_dataset(lohtm__fgfvd,
                get_row_counts=get_row_counts, expr_filters=expr_filters,
                is_parallel=is_parallel, typing_pa_schema=
                typing_pa_table_schema, partitioning=None, tot_rows_to_read
                =tot_rows_to_read)
        except BodoError as aymv__qkv:
            if re.search('Schema .* was different', str(aymv__qkv), re.
                IGNORECASE):
                raise BodoError(
                    f"""Bodo currently doesn't support reading Iceberg tables with schema evolution.
{aymv__qkv}"""
                    )
            else:
                raise
    zbm__kqt = IcebergParquetDataset(conn, database_schema, table_name,
        typing_pa_table_schema, xcf__liu, snapshot_id, pq_dataset)
    if cfu__yclk:
        cqusz__scl.finalize()
    return zbm__kqt


def are_schemas_compatible(pa_schema: pa.Schema, df_schema: pa.Schema,
    allow_downcasting: bool=False) ->bool:
    if pa_schema.equals(df_schema):
        return True
    if len(df_schema) < len(pa_schema):
        hqo__gdrlj = []
        for vjcf__juboh in pa_schema:
            lfxm__roon = df_schema.field_by_name(vjcf__juboh.name)
            if not (lfxm__roon is None and vjcf__juboh.nullable):
                hqo__gdrlj.append(vjcf__juboh)
        pa_schema = pa.schema(hqo__gdrlj)
    if len(pa_schema) != len(df_schema):
        return False
    for uof__sgjm in range(len(df_schema)):
        lfxm__roon = df_schema.field(uof__sgjm)
        vjcf__juboh = pa_schema.field(uof__sgjm)
        if lfxm__roon.equals(vjcf__juboh):
            continue
        mjrq__eiv = lfxm__roon.type
        hjmjm__hphj = vjcf__juboh.type
        if not mjrq__eiv.equals(hjmjm__hphj) and allow_downcasting and (pa.
            types.is_signed_integer(mjrq__eiv) and pa.types.
            is_signed_integer(hjmjm__hphj) or pa.types.is_floating(
            mjrq__eiv) and pa.types.is_floating(hjmjm__hphj)
            ) and mjrq__eiv.bit_width > hjmjm__hphj.bit_width:
            lfxm__roon = lfxm__roon.with_type(hjmjm__hphj)
        if not lfxm__roon.nullable and vjcf__juboh.nullable:
            lfxm__roon = lfxm__roon.with_nullable(True)
        elif allow_downcasting and lfxm__roon.nullable and not vjcf__juboh.nullable:
            lfxm__roon = lfxm__roon.with_nullable(False)
        df_schema = df_schema.set(uof__sgjm, lfxm__roon)
    return df_schema.equals(pa_schema)


def get_table_details_before_write(table_name: str, conn: str,
    database_schema: str, df_schema: pa.Schema, if_exists: str,
    allow_downcasting: bool=False):
    cqusz__scl = tracing.Event('iceberg_get_table_details_before_write')
    import bodo_iceberg_connector as connector
    nkkb__yac = MPI.COMM_WORLD
    nqzty__kzp = None
    iceberg_schema_id = None
    table_loc = ''
    partition_spec = []
    sort_order = []
    iceberg_schema_str = ''
    pa_schema = None
    rjklf__guse = {zcr__ewsx: qxjc__jkxx for qxjc__jkxx, zcr__ewsx in
        enumerate(df_schema.names)}
    if nkkb__yac.Get_rank() == 0:
        try:
            (table_loc, iceberg_schema_id, pa_schema, iceberg_schema_str,
                partition_spec, sort_order) = (connector.get_typing_info(
                conn, database_schema, table_name))
            for hrqg__owwr, *klmew__oxlp in partition_spec:
                assert hrqg__owwr in rjklf__guse, f'Iceberg Partition column {hrqg__owwr} not found in dataframe'
            for hrqg__owwr, *klmew__oxlp in sort_order:
                assert hrqg__owwr in rjklf__guse, f'Iceberg Sort column {hrqg__owwr} not found in dataframe'
            partition_spec = [(rjklf__guse[hrqg__owwr], *zkoo__jdcd) for 
                hrqg__owwr, *zkoo__jdcd in partition_spec]
            sort_order = [(rjklf__guse[hrqg__owwr], *zkoo__jdcd) for 
                hrqg__owwr, *zkoo__jdcd in sort_order]
            if if_exists == 'append' and pa_schema is not None:
                if not are_schemas_compatible(pa_schema, df_schema,
                    allow_downcasting):
                    if numba.core.config.DEVELOPER_MODE:
                        raise BodoError(
                            f"""DataFrame schema needs to be an ordered subset of Iceberg table for append

Iceberg:
{pa_schema}

DataFrame:
{df_schema}
"""
                            )
                    else:
                        raise BodoError(
                            'DataFrame schema needs to be an ordered subset of Iceberg table for append'
                            )
            if iceberg_schema_id is None:
                iceberg_schema_str = connector.pyarrow_to_iceberg_schema_str(
                    df_schema)
        except connector.IcebergError as aymv__qkv:
            if isinstance(aymv__qkv, connector.IcebergJavaError
                ) and numba.core.config.DEVELOPER_MODE:
                nqzty__kzp = BodoError(
                    f'{aymv__qkv.message}: {aymv__qkv.java_error}')
            else:
                nqzty__kzp = BodoError(aymv__qkv.message)
        except Exception as aymv__qkv:
            nqzty__kzp = aymv__qkv
    nqzty__kzp = nkkb__yac.bcast(nqzty__kzp)
    if isinstance(nqzty__kzp, Exception):
        raise nqzty__kzp
    table_loc = nkkb__yac.bcast(table_loc)
    iceberg_schema_id = nkkb__yac.bcast(iceberg_schema_id)
    partition_spec = nkkb__yac.bcast(partition_spec)
    sort_order = nkkb__yac.bcast(sort_order)
    iceberg_schema_str = nkkb__yac.bcast(iceberg_schema_str)
    pa_schema = nkkb__yac.bcast(pa_schema)
    if iceberg_schema_id is None:
        already_exists = False
        iceberg_schema_id = -1
    else:
        already_exists = True
    cqusz__scl.finalize()
    return (already_exists, table_loc, iceberg_schema_id, partition_spec,
        sort_order, iceberg_schema_str, pa_schema if if_exists == 'append' and
        pa_schema is not None else df_schema)


def collect_file_info(iceberg_files_info) ->Tuple[List[str], List[int],
    List[int]]:
    from mpi4py import MPI
    nkkb__yac = MPI.COMM_WORLD
    ksnf__tpl = [dlxax__qyy[0] for dlxax__qyy in iceberg_files_info]
    heta__kufyb = nkkb__yac.gather(ksnf__tpl)
    fnames = [hlz__qdpdo for bmw__bovmb in heta__kufyb for hlz__qdpdo in
        bmw__bovmb] if nkkb__yac.Get_rank() == 0 else None
    uni__vyocr = np.array([dlxax__qyy[1] for dlxax__qyy in
        iceberg_files_info], dtype=np.int64)
    plsec__kwapl = np.array([dlxax__qyy[2] for dlxax__qyy in
        iceberg_files_info], dtype=np.int64)
    zbjb__koio = bodo.gatherv(uni__vyocr).tolist()
    xqnl__idu = bodo.gatherv(plsec__kwapl).tolist()
    return fnames, zbjb__koio, xqnl__idu


def register_table_write(conn_str: str, db_name: str, table_name: str,
    table_loc: str, fnames: List[str], all_metrics: Dict[str, List[Any]],
    iceberg_schema_id: int, pa_schema, partition_spec, sort_order, mode: str):
    cqusz__scl = tracing.Event('iceberg_register_table_write')
    import bodo_iceberg_connector
    nkkb__yac = MPI.COMM_WORLD
    success = False
    if nkkb__yac.Get_rank() == 0:
        vezv__eemdv = None if iceberg_schema_id < 0 else iceberg_schema_id
        success = bodo_iceberg_connector.commit_write(conn_str, db_name,
            table_name, table_loc, fnames, all_metrics, vezv__eemdv,
            pa_schema, partition_spec, sort_order, mode)
    success = nkkb__yac.bcast(success)
    cqusz__scl.finalize()
    return success


def register_table_merge_cow(conn_str: str, db_name: str, table_name: str,
    table_loc: str, old_fnames: List[str], new_fnames: List[str],
    all_metrics: Dict[str, List[Any]], snapshot_id: int):
    cqusz__scl = tracing.Event('iceberg_register_table_merge_cow')
    import bodo_iceberg_connector
    nkkb__yac = MPI.COMM_WORLD
    success = False
    if nkkb__yac.Get_rank() == 0:
        success = bodo_iceberg_connector.commit_merge_cow(conn_str, db_name,
            table_name, table_loc, old_fnames, new_fnames, all_metrics,
            snapshot_id)
    success: bool = nkkb__yac.bcast(success)
    cqusz__scl.finalize()
    return success


from numba.extending import NativeValue, box, models, register_model, unbox


class PythonListOfHeterogeneousTuples(types.Opaque):

    def __init__(self):
        super(PythonListOfHeterogeneousTuples, self).__init__(name=
            'PythonListOfHeterogeneousTuples')


python_list_of_heterogeneous_tuples_type = PythonListOfHeterogeneousTuples()
types.python_list_of_heterogeneous_tuples_type = (
    python_list_of_heterogeneous_tuples_type)
register_model(PythonListOfHeterogeneousTuples)(models.OpaqueModel)


@unbox(PythonListOfHeterogeneousTuples)
def unbox_python_list_of_heterogeneous_tuples_type(typ, val, c):
    c.pyapi.incref(val)
    return NativeValue(val)


@box(PythonListOfHeterogeneousTuples)
def box_python_list_of_heterogeneous_tuples_type(typ, val, c):
    c.pyapi.incref(val)
    return val


this_module = sys.modules[__name__]
PyObjectOfList = install_py_obj_class(types_name='pyobject_of_list_type',
    python_type=None, module=this_module, class_name='PyObjectOfListType',
    model_name='PyObjectOfListModel')


@numba.njit()
def iceberg_pq_write(table_loc, bodo_table, col_names, partition_spec,
    sort_order, iceberg_schema_str, is_parallel, expected_schema):
    bucket_region = get_s3_bucket_region_njit(table_loc, is_parallel)
    kofd__owc = 'snappy'
    drti__owy = -1
    iceberg_files_info = iceberg_pq_write_table_cpp(unicode_to_utf8(
        table_loc), bodo_table, col_names, partition_spec, sort_order,
        unicode_to_utf8(kofd__owc), is_parallel, unicode_to_utf8(
        bucket_region), drti__owy, unicode_to_utf8(iceberg_schema_str),
        expected_schema)
    return iceberg_files_info


@numba.njit()
def iceberg_write(table_name, conn, database_schema, bodo_table, col_names,
    if_exists, is_parallel, df_pyarrow_schema, allow_downcasting=False):
    cqusz__scl = tracing.Event('iceberg_write_py', is_parallel)
    assert is_parallel, 'Iceberg Write only supported for distributed dataframes'
    with numba.objmode(already_exists='bool_', table_loc='unicode_type',
        iceberg_schema_id='i8', partition_spec=
        'python_list_of_heterogeneous_tuples_type', sort_order=
        'python_list_of_heterogeneous_tuples_type', iceberg_schema_str=
        'unicode_type', expected_schema='pyarrow_table_schema_type'):
        (already_exists, table_loc, iceberg_schema_id, partition_spec,
            sort_order, iceberg_schema_str, expected_schema) = (
            get_table_details_before_write(table_name, conn,
            database_schema, df_pyarrow_schema, if_exists, allow_downcasting))
    if already_exists and if_exists == 'fail':
        raise ValueError(f'Table already exists.')
    if already_exists:
        mode = if_exists
    else:
        mode = 'create'
    iceberg_files_info = iceberg_pq_write(table_loc, bodo_table, col_names,
        partition_spec, sort_order, iceberg_schema_str, is_parallel,
        expected_schema)
    with numba.objmode(success='bool_'):
        fnames, zbjb__koio, xqnl__idu = collect_file_info(iceberg_files_info)
        success = register_table_write(conn, database_schema, table_name,
            table_loc, fnames, {'size': xqnl__idu, 'record_count':
            zbjb__koio}, iceberg_schema_id, df_pyarrow_schema,
            partition_spec, sort_order, mode)
    if not success:
        raise BodoError('Iceberg write failed.')
    cqusz__scl.finalize()


@numba.generated_jit(nopython=True)
def iceberg_merge_cow_py(table_name, conn, database_schema, bodo_df,
    snapshot_id, old_fnames, is_parallel=False):
    if not is_parallel:
        raise BodoError(
            'Merge Into with Iceberg Tables are only supported on distributed DataFrames'
            )
    df_pyarrow_schema = bodo.io.helpers.numba_to_pyarrow_schema(bodo_df,
        is_iceberg=True)
    cev__vtpe = pd.array(bodo_df.columns)
    if bodo_df.is_table_format:
        yfk__wuqmj = bodo_df.table_type

        def impl(table_name, conn, database_schema, bodo_df, snapshot_id,
            old_fnames, is_parallel=False):
            iceberg_merge_cow(table_name, format_iceberg_conn_njit(conn),
                database_schema, py_table_to_cpp_table(bodo.hiframes.
                pd_dataframe_ext.get_dataframe_table(bodo_df), yfk__wuqmj),
                snapshot_id, old_fnames, array_to_info(cev__vtpe),
                df_pyarrow_schema, is_parallel)
    else:
        kbn__dyx = ', '.join(
            'array_to_info(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(bodo_df, {}))'
            .format(qxjc__jkxx) for qxjc__jkxx in range(len(bodo_df.columns)))
        etg__zmna = 'def impl(\n'
        etg__zmna += '    table_name,\n'
        etg__zmna += '    conn,\n'
        etg__zmna += '    database_schema,\n'
        etg__zmna += '    bodo_df,\n'
        etg__zmna += '    snapshot_id,\n'
        etg__zmna += '    old_fnames,\n'
        etg__zmna += '    is_parallel=False,\n'
        etg__zmna += '):\n'
        etg__zmna += '    info_list = [{}]\n'.format(kbn__dyx)
        etg__zmna += '    table = arr_info_list_to_table(info_list)\n'
        etg__zmna += '    iceberg_merge_cow(\n'
        etg__zmna += '        table_name,\n'
        etg__zmna += '        format_iceberg_conn_njit(conn),\n'
        etg__zmna += '        database_schema,\n'
        etg__zmna += '        table,\n'
        etg__zmna += '        snapshot_id,\n'
        etg__zmna += '        old_fnames,\n'
        etg__zmna += '        array_to_info(col_names_py),\n'
        etg__zmna += '        df_pyarrow_schema,\n'
        etg__zmna += '        is_parallel,\n'
        etg__zmna += '    )\n'
        locals = dict()
        globals = {'bodo': bodo, 'array_to_info': array_to_info,
            'arr_info_list_to_table': arr_info_list_to_table,
            'iceberg_merge_cow': iceberg_merge_cow,
            'format_iceberg_conn_njit': format_iceberg_conn_njit,
            'col_names_py': cev__vtpe, 'df_pyarrow_schema': df_pyarrow_schema}
        exec(etg__zmna, globals, locals)
        impl = locals['impl']
    return impl


@numba.njit()
def iceberg_merge_cow(table_name, conn, database_schema, bodo_table,
    snapshot_id, old_fnames, col_names, df_pyarrow_schema, is_parallel):
    cqusz__scl = tracing.Event('iceberg_merge_cow_py', is_parallel)
    assert is_parallel, 'Iceberg Write only supported for distributed dataframes'
    with numba.objmode(already_exists='bool_', table_loc='unicode_type',
        partition_spec='python_list_of_heterogeneous_tuples_type',
        sort_order='python_list_of_heterogeneous_tuples_type',
        iceberg_schema_str='unicode_type', expected_schema=
        'pyarrow_table_schema_type'):
        (already_exists, table_loc, klmew__oxlp, partition_spec, sort_order,
            iceberg_schema_str, expected_schema) = (
            get_table_details_before_write(table_name, conn,
            database_schema, df_pyarrow_schema, 'append', allow_downcasting
            =True))
    if not already_exists:
        raise ValueError(f'Iceberg MERGE INTO: Table does not exist at write')
    iceberg_files_info = iceberg_pq_write(table_loc, bodo_table, col_names,
        partition_spec, sort_order, iceberg_schema_str, is_parallel,
        expected_schema)
    with numba.objmode(success='bool_'):
        fnames, zbjb__koio, xqnl__idu = collect_file_info(iceberg_files_info)
        success = register_table_merge_cow(conn, database_schema,
            table_name, table_loc, old_fnames, fnames, {'size': xqnl__idu,
            'record_count': zbjb__koio}, snapshot_id)
    if not success:
        raise BodoError('Iceberg MERGE INTO: write failed')
    cqusz__scl.finalize()


import llvmlite.binding as ll
from llvmlite import ir as lir
from numba.core import cgutils, types
if bodo.utils.utils.has_pyarrow():
    from bodo.io import arrow_cpp
    ll.add_symbol('iceberg_pq_write', arrow_cpp.iceberg_pq_write)


@intrinsic
def iceberg_pq_write_table_cpp(typingctx, table_data_loc_t, table_t,
    col_names_t, partition_spec_t, sort_order_t, compression_t,
    is_parallel_t, bucket_region, row_group_size, iceberg_metadata_t,
    iceberg_schema_t):

    def codegen(context, builder, sig, args):
        wzrt__skp = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(8).as_pointer(), lir.
            IntType(8).as_pointer(), lir.IntType(8).as_pointer(), lir.
            IntType(8).as_pointer(), lir.IntType(8).as_pointer(), lir.
            IntType(1), lir.IntType(8).as_pointer(), lir.IntType(64), lir.
            IntType(8).as_pointer(), lir.IntType(8).as_pointer()])
        dte__mtsde = cgutils.get_or_insert_function(builder.module,
            wzrt__skp, name='iceberg_pq_write')
        knl__cupq = builder.call(dte__mtsde, args)
        bodo.utils.utils.inlined_check_and_propagate_cpp_exception(context,
            builder)
        return knl__cupq
    return types.python_list_of_heterogeneous_tuples_type(types.voidptr,
        table_t, col_names_t, python_list_of_heterogeneous_tuples_type,
        python_list_of_heterogeneous_tuples_type, types.voidptr, types.
        boolean, types.voidptr, types.int64, types.voidptr,
        pyarrow_table_schema_type), codegen
