import os
import sys
import traceback
import warnings
from tempfile import TemporaryDirectory
from typing import TYPE_CHECKING, Callable, Dict, List, Literal, Optional, Tuple
from urllib.parse import parse_qsl, urlparse
from uuid import uuid4
import pyarrow as pa
from mpi4py import MPI
from numba.core import types
import bodo
from bodo.hiframes.pd_dataframe_ext import DataFrameType
from bodo.io.helpers import ExceptionPropagatingThread, _get_numba_typ_from_pa_typ, update_env_vars, update_file_contents
from bodo.libs.array_item_arr_ext import ArrayItemArrayType
from bodo.libs.dict_arr_ext import dict_str_arr_type
from bodo.libs.str_arr_ext import string_array_type
from bodo.libs.struct_arr_ext import StructArrayType
from bodo.utils import tracing
from bodo.utils.py_objs import install_py_obj_class
from bodo.utils.typing import BodoError, BodoWarning, is_str_arr_type
if TYPE_CHECKING:
    from snowflake.connector import SnowflakeConnection
    from snowflake.connector.cursor import ResultMetadata, SnowflakeCursor
    from snowflake.connector.result_batch import JSONResultBatch, ResultBatch
SF_READ_SCHEMA_PROBE_TIMEOUT = 5
SF_READ_AUTO_DICT_ENCODE_ENABLED = True
SF_READ_DICT_ENCODE_CRITERION = 0.5
SF_READ_DICT_ENCODING_PROBE_TIMEOUT = 5
SF_READ_DICT_ENCODING_IF_TIMEOUT = False
SF_READ_DICT_ENCODING_PROBE_ROW_LIMIT = 100000000
SCALE_TO_UNIT_PRECISION: Dict[int, Literal['s', 'ms', 'us', 'ns']] = {(0):
    's', (3): 'ms', (6): 'us', (9): 'ns'}
TYPE_CODE_TO_ARROW_TYPE: List[Callable[['ResultMetadata', str], pa.DataType]
    ] = [lambda m, _: pa.int64() if m.scale == 0 else pa.float64() if m.
    scale < 18 else pa.decimal128(m.precision, m.scale), lambda _, __: pa.
    float64(), lambda _, __: pa.string(), lambda _, __: pa.date32(), lambda
    _, __: pa.time64('ns'), lambda _, __: pa.string(), lambda m, tz: pa.
    timestamp(SCALE_TO_UNIT_PRECISION[m.scale], tz=tz), lambda m, tz: pa.
    timestamp(SCALE_TO_UNIT_PRECISION[m.scale], tz=tz), lambda m, _: pa.
    timestamp(SCALE_TO_UNIT_PRECISION[m.scale]), lambda _, __: pa.string(),
    lambda _, __: pa.string(), lambda _, __: pa.binary(), lambda m, _: {(0):
    pa.time32('s'), (3): pa.time32('ms'), (6): pa.time64('us'), (9): pa.
    time64('ns')}[m.scale], lambda _, __: pa.bool_(), lambda _, __: pa.string()
    ]
INT_BITSIZE_TO_ARROW_DATATYPE = {(1): pa.int8(), (2): pa.int16(), (4): pa.
    int32(), (8): pa.int64()}


def gen_snowflake_schema(column_names, column_datatypes):
    sf_schema = {}
    for col_name, ovygg__ygrap in zip(column_names, column_datatypes):
        if isinstance(ovygg__ygrap, bodo.DatetimeArrayType
            ) or ovygg__ygrap == bodo.datetime_datetime_type:
            sf_schema[col_name] = 'TIMESTAMP_NTZ'
        elif ovygg__ygrap == bodo.datetime_date_array_type:
            sf_schema[col_name] = 'DATE'
        elif isinstance(ovygg__ygrap, bodo.TimeArrayType):
            if ovygg__ygrap.precision in [0, 3, 6]:
                koy__ekqv = ovygg__ygrap.precision
            elif ovygg__ygrap.precision == 9:
                if bodo.get_rank() == 0:
                    warnings.warn(BodoWarning(
                        f"""to_sql(): {col_name} time precision will be lost.
Snowflake loses nano second precision when exporting parquet file using COPY INTO.
 This is due to a limitation on Parquet V1 that is currently being used in Snowflake"""
                        ))
                koy__ekqv = 6
            else:
                raise ValueError(
                    'Unsupported Precision Found in Bodo Time Array')
            sf_schema[col_name] = f'TIME({koy__ekqv})'
        elif isinstance(ovygg__ygrap, types.Array):
            uthua__xan = ovygg__ygrap.dtype.name
            if uthua__xan.startswith('datetime'):
                sf_schema[col_name] = 'DATETIME'
            if uthua__xan.startswith('timedelta'):
                sf_schema[col_name] = 'NUMBER(38, 0)'
                if bodo.get_rank() == 0:
                    warnings.warn(BodoWarning(
                        f"to_sql(): {col_name} with type 'timedelta' will be written as integer values (ns frequency) to the database."
                        ))
            elif uthua__xan.startswith(('int', 'uint')):
                sf_schema[col_name] = 'NUMBER(38, 0)'
            elif uthua__xan.startswith('float'):
                sf_schema[col_name] = 'REAL'
        elif is_str_arr_type(ovygg__ygrap):
            sf_schema[col_name] = 'TEXT'
        elif ovygg__ygrap == bodo.binary_array_type:
            sf_schema[col_name] = 'BINARY'
        elif ovygg__ygrap == bodo.boolean_array:
            sf_schema[col_name] = 'BOOLEAN'
        elif isinstance(ovygg__ygrap, bodo.IntegerArrayType):
            sf_schema[col_name] = 'NUMBER(38, 0)'
        elif isinstance(ovygg__ygrap, bodo.FloatingArrayType):
            sf_schema[col_name] = 'REAL'
        elif isinstance(ovygg__ygrap, bodo.DecimalArrayType):
            sf_schema[col_name] = 'NUMBER(38, 18)'
        elif isinstance(ovygg__ygrap, (ArrayItemArrayType, StructArrayType)):
            sf_schema[col_name] = 'VARIANT'
        else:
            raise BodoError(
                f'Conversion from Bodo array type {ovygg__ygrap} to snowflake type for {col_name} not supported yet.'
                )
    return sf_schema


SF_WRITE_COPY_INTO_ON_ERROR = 'abort_statement'
SF_WRITE_OVERLAP_UPLOAD = True
SF_WRITE_PARQUET_CHUNK_SIZE = int(256000000.0)
SF_WRITE_PARQUET_COMPRESSION = 'snappy'
SF_WRITE_UPLOAD_USING_PUT = False
SF_AZURE_WRITE_HDFS_CORE_SITE = """<configuration>
  <property>
    <name>fs.azure.account.auth.type</name>
    <value>SAS</value>
  </property>
  <property>
    <name>fs.azure.sas.token.provider.type</name>
    <value>org.bodo.azurefs.sas.BodoSASTokenProvider</value>
  </property>
  <property>
    <name>fs.abfs.impl</name>
    <value>org.apache.hadoop.fs.azurebfs.AzureBlobFileSystem</value>
  </property>
</configuration>
"""
SF_AZURE_WRITE_SAS_TOKEN_FILE_LOCATION = os.path.join(bodo.
    HDFS_CORE_SITE_LOC_DIR.name, 'sas_token.txt')


def execute_query(cursor: 'SnowflakeCursor', query: str, timeout: Optional[int]
    ) ->Optional['SnowflakeCursor']:
    try:
        return cursor.execute(query, timeout=timeout)
    except snowflake.connector.errors.ProgrammingError as lnf__koad:
        if 'SQL execution canceled' in str(lnf__koad):
            return None
        else:
            raise


def escape_col_name(col_name: str) ->str:
    return '"{}"'.format(col_name.replace('"', '""'))


def snowflake_connect(conn_str: str, is_parallel: bool=False
    ) ->'SnowflakeConnection':
    igegh__hgqsf = tracing.Event('snowflake_connect', is_parallel=is_parallel)
    toyo__paul = urlparse(conn_str)
    moct__rhg = {}
    if toyo__paul.username:
        moct__rhg['user'] = toyo__paul.username
    if toyo__paul.password:
        moct__rhg['password'] = toyo__paul.password
    if toyo__paul.hostname:
        moct__rhg['account'] = toyo__paul.hostname
    if toyo__paul.port:
        moct__rhg['port'] = toyo__paul.port
    if toyo__paul.path:
        qbj__dmzt = toyo__paul.path
        if qbj__dmzt.startswith('/'):
            qbj__dmzt = qbj__dmzt[1:]
        virhc__ijj = qbj__dmzt.split('/')
        if len(virhc__ijj) == 2:
            qxt__eui, schema = virhc__ijj
        elif len(virhc__ijj) == 1:
            qxt__eui = virhc__ijj[0]
            schema = None
        else:
            raise BodoError(
                f'Unexpected Snowflake connection string {conn_str}. Path is expected to contain database name and possibly schema'
                )
        moct__rhg['database'] = qxt__eui
        if schema:
            moct__rhg['schema'] = schema
    if toyo__paul.query:
        for xif__npi, jbfpz__twa in parse_qsl(toyo__paul.query):
            moct__rhg[xif__npi] = jbfpz__twa
            if xif__npi == 'session_parameters':
                import json
                moct__rhg[xif__npi] = json.loads(jbfpz__twa)
    moct__rhg['application'] = 'bodo'
    moct__rhg['login_timeout'] = 5
    try:
        import snowflake.connector
    except ImportError as ywfwy__yqkj:
        raise BodoError(
            "Snowflake Python connector packages not found. Using 'to_sql' with Snowflake requires snowflake-connector-python. This can be installed by calling 'conda install -c conda-forge snowflake-connector-python' or 'pip install snowflake-connector-python'."
            )
    conn = snowflake.connector.connect(**moct__rhg)
    dyfi__jgsq = os.environ.get('BODO_PLATFORM_WORKSPACE_REGION', None)
    if dyfi__jgsq and bodo.get_rank() == 0:
        dyfi__jgsq = dyfi__jgsq.lower()
        ejezn__oabet = os.environ.get('BODO_PLATFORM_CLOUD_PROVIDER', None)
        if ejezn__oabet is not None:
            ejezn__oabet = ejezn__oabet.lower()
        edbj__nsc = conn.cursor()
        edbj__nsc.execute('select current_region()')
        yijv__mlk: pa.Table = edbj__nsc.fetch_arrow_all()
        rosn__zabk = yijv__mlk[0][0].as_py()
        edbj__nsc.close()
        rzlxh__qhk = rosn__zabk.split('_')
        ywjq__qxoa = rzlxh__qhk[0].lower()
        evqf__mdi = '-'.join(rzlxh__qhk[1:]).lower()
        if ejezn__oabet and ejezn__oabet != ywjq__qxoa:
            gka__xsjqs = BodoWarning(
                f'Performance Warning: The Snowflake warehouse and Bodo platform are on different cloud providers. '
                 +
                f'The Snowflake warehouse is located on {ywjq__qxoa}, but the Bodo cluster is located on {ejezn__oabet}. '
                 +
                'For best performance we recommend using your cluster and Snowflake account in the same region with the same cloud provider.'
                )
            warnings.warn(gka__xsjqs)
        elif dyfi__jgsq != evqf__mdi:
            gka__xsjqs = BodoWarning(
                f'Performance Warning: The Snowflake warehouse and Bodo platform are in different cloud regions. '
                 +
                f'The Snowflake warehouse is located in {evqf__mdi}, but the Bodo cluster is located in {dyfi__jgsq}. '
                 +
                'For best performance we recommend using your cluster and Snowflake account in the same region with the same cloud provider.'
                )
            warnings.warn(gka__xsjqs)
    igegh__hgqsf.finalize()
    return conn


def get_schema_from_metadata(cursor: 'SnowflakeCursor', sql_query: str,
    is_select_query: bool) ->Tuple[List[pa.Field], List, List[int], List[pa
    .DataType]]:
    sfv__bxga = cursor.describe(sql_query)
    tz: str = cursor._timezone
    zfytn__jlzq: List[pa.Field] = []
    dhn__avq: List[str] = []
    etwe__mmjf: List[int] = []
    for ekeov__nnh, zsod__dsqe in enumerate(sfv__bxga):
        egf__tmuht = TYPE_CODE_TO_ARROW_TYPE[zsod__dsqe.type_code](zsod__dsqe,
            tz)
        zfytn__jlzq.append(pa.field(zsod__dsqe.name, egf__tmuht, zsod__dsqe
            .is_nullable))
        if pa.types.is_int64(egf__tmuht):
            dhn__avq.append(zsod__dsqe.name)
            etwe__mmjf.append(ekeov__nnh)
    if is_select_query and len(dhn__avq) != 0:
        eqsp__doabz = 'SELECT ' + ', '.join(
            f'SYSTEM$TYPEOF({escape_col_name(x)})' for x in dhn__avq
            ) + f' FROM ({sql_query}) LIMIT 1'
        mwxf__grgnp = execute_query(cursor, eqsp__doabz, timeout=
            SF_READ_SCHEMA_PROBE_TIMEOUT)
        if mwxf__grgnp is not None and (ckuj__vuubv := mwxf__grgnp.
            fetch_arrow_all()) is not None:
            for ekeov__nnh, (cip__myznz, fmiku__iim) in enumerate(ckuj__vuubv
                .to_pylist()[0].items()):
                uamu__jlje = dhn__avq[ekeov__nnh]
                ziwo__dwo = (
                    f'SYSTEM$TYPEOF({escape_col_name(uamu__jlje)})',
                    f'SYSTEM$TYPEOF({escape_col_name(uamu__jlje.upper())})')
                assert cip__myznz in ziwo__dwo, 'Output of Snowflake Schema Probe Query Uses Unexpected Column Names'
                vzl__fll = etwe__mmjf[ekeov__nnh]
                ppsd__dlc = int(fmiku__iim[-2])
                isj__cgebe = INT_BITSIZE_TO_ARROW_DATATYPE[ppsd__dlc]
                zfytn__jlzq[vzl__fll] = zfytn__jlzq[vzl__fll].with_type(
                    isj__cgebe)
    bna__tjn = []
    ccdo__xsmu = []
    zeawm__dohb = []
    for ekeov__nnh, adue__gzz in enumerate(zfytn__jlzq):
        egf__tmuht, whzb__rnqp = _get_numba_typ_from_pa_typ(adue__gzz, 
            False, adue__gzz.nullable, None)
        bna__tjn.append(egf__tmuht)
        if not whzb__rnqp:
            ccdo__xsmu.append(ekeov__nnh)
            zeawm__dohb.append(adue__gzz.type)
    return zfytn__jlzq, bna__tjn, ccdo__xsmu, zeawm__dohb


def get_schema(conn_str: str, sql_query: str, is_select_query: bool,
    _bodo_read_as_dict: Optional[List[str]]):
    conn = snowflake_connect(conn_str)
    cursor = conn.cursor()
    bfpv__pju, bna__tjn, ccdo__xsmu, zeawm__dohb = get_schema_from_metadata(
        cursor, sql_query, is_select_query)
    embp__ntym = _bodo_read_as_dict if _bodo_read_as_dict else []
    uvgy__ffiuj = {}
    for ekeov__nnh, wzj__vsxho in enumerate(bna__tjn):
        if wzj__vsxho == string_array_type:
            uvgy__ffiuj[bfpv__pju[ekeov__nnh].name] = ekeov__nnh
    uwlxn__cxxcg = {(stzyl__bflpg.lower() if stzyl__bflpg.isupper() else
        stzyl__bflpg): stzyl__bflpg for stzyl__bflpg in uvgy__ffiuj.keys()}
    lump__juxec = embp__ntym - uwlxn__cxxcg.keys()
    if len(lump__juxec) > 0:
        if bodo.get_rank() == 0:
            warnings.warn(BodoWarning(
                f'The following columns are not of datatype string and hence cannot be read with dictionary encoding: {lump__juxec}'
                ))
    erf__kvvm = uwlxn__cxxcg.keys() & embp__ntym
    for stzyl__bflpg in erf__kvvm:
        bna__tjn[uvgy__ffiuj[uwlxn__cxxcg[stzyl__bflpg]]] = dict_str_arr_type
    mubyv__nysn, fbd__fxou = [], []
    twhc__rccz = uwlxn__cxxcg.keys() - embp__ntym
    for stzyl__bflpg in twhc__rccz:
        mubyv__nysn.append(f'count (distinct "{uwlxn__cxxcg[stzyl__bflpg]}")')
        fbd__fxou.append(uvgy__ffiuj[uwlxn__cxxcg[stzyl__bflpg]])
    jes__cckw: Optional[Tuple[int, List[str]]] = None
    if len(mubyv__nysn) != 0 and SF_READ_AUTO_DICT_ENCODE_ENABLED:
        eyw__qysr = max(SF_READ_DICT_ENCODING_PROBE_ROW_LIMIT // len(
            mubyv__nysn), 1)
        iorsz__qga = (
            f"select count(*),{', '.join(mubyv__nysn)}from ( select * from ({sql_query}) limit {eyw__qysr} ) SAMPLE (1)"
            )
        mfrt__pkky = execute_query(cursor, iorsz__qga, timeout=
            SF_READ_DICT_ENCODING_PROBE_TIMEOUT)
        if mfrt__pkky is None:
            jes__cckw = eyw__qysr, mubyv__nysn
            if SF_READ_DICT_ENCODING_IF_TIMEOUT:
                for ekeov__nnh in fbd__fxou:
                    bna__tjn[ekeov__nnh] = dict_str_arr_type
        else:
            ncw__yhg: pa.Table = mfrt__pkky.fetch_arrow_all()
            fzzd__pcec = ncw__yhg[0][0].as_py()
            hzk__yspx = [(ncw__yhg[ekeov__nnh][0].as_py() / max(fzzd__pcec,
                1)) for ekeov__nnh in range(1, len(mubyv__nysn) + 1)]
            qud__jcd = filter(lambda x: x[0] <=
                SF_READ_DICT_ENCODE_CRITERION, zip(hzk__yspx, fbd__fxou))
            for _, gkvti__nlun in qud__jcd:
                bna__tjn[gkvti__nlun] = dict_str_arr_type
    yriw__ytp: List[str] = []
    pqtc__kff = set()
    for x in bfpv__pju:
        if x.name.isupper():
            pqtc__kff.add(x.name.lower())
            yriw__ytp.append(x.name.lower())
        else:
            yriw__ytp.append(x.name)
    txn__pur = DataFrameType(data=tuple(bna__tjn), columns=tuple(yriw__ytp))
    return txn__pur, pqtc__kff, ccdo__xsmu, zeawm__dohb, pa.schema(bfpv__pju
        ), jes__cckw


class SnowflakeDataset(object):

    def __init__(self, batches: List['ResultBatch'], schema, conn:
        'SnowflakeConnection'):
        self.pieces = batches
        self._bodo_total_rows = 0
        for eif__ebeya in batches:
            eif__ebeya._bodo_num_rows = eif__ebeya.rowcount
            self._bodo_total_rows += eif__ebeya._bodo_num_rows
        self.schema = schema
        self.conn = conn


class FakeArrowJSONResultBatch:

    def __init__(self, json_batch: 'JSONResultBatch', schema: pa.Schema
        ) ->None:
        self._json_batch = json_batch
        self._schema = schema

    @property
    def rowcount(self):
        return self._json_batch.rowcount

    def to_arrow(self, _: Optional['SnowflakeConnection']=None) ->pa.Table:
        rpy__jttvu = []
        for gairl__jxe in self._json_batch.create_iter():
            rpy__jttvu.append({self._schema.names[ekeov__nnh]: yxssr__evctv for
                ekeov__nnh, yxssr__evctv in enumerate(gairl__jxe)})
        boe__fby = pa.Table.from_pylist(rpy__jttvu, schema=self._schema)
        return boe__fby


def get_dataset(query: str, conn_str: str, schema: pa.Schema,
    only_fetch_length: bool=False, is_select_query: bool=True, is_parallel:
    bool=True, is_independent: bool=False) ->Tuple[SnowflakeDataset, int]:
    assert not (only_fetch_length and not is_select_query
        ), 'The only length optimization can only be run with select queries'
    assert not (is_parallel and is_independent
        ), 'Snowflake get_dataset: is_parallel and is_independent cannot be True at the same time'
    try:
        import snowflake.connector
        from snowflake.connector.result_batch import ArrowResultBatch, JSONResultBatch
    except ImportError as ywfwy__yqkj:
        raise BodoError(
            "Snowflake Python connector packages not found. Fetching data from Snowflake requires snowflake-connector-python. This can be installed by calling 'conda install -c conda-forge snowflake-connector-python' or 'pip install snowflake-connector-python'."
            )
    igegh__hgqsf = tracing.Event('get_snowflake_dataset', is_parallel=
        is_parallel)
    jrqw__pyoq = MPI.COMM_WORLD
    conn = snowflake_connect(conn_str)
    cvj__xse = -1
    batches = []
    if only_fetch_length and is_select_query:
        if bodo.get_rank() == 0 or is_independent:
            edbj__nsc = conn.cursor()
            kwgdf__ypit = tracing.Event('execute_length_query', is_parallel
                =False)
            edbj__nsc.execute(query)
            yijv__mlk = edbj__nsc.fetch_arrow_all()
            cvj__xse = yijv__mlk[0][0].as_py()
            edbj__nsc.close()
            kwgdf__ypit.finalize()
        if not is_independent:
            cvj__xse = jrqw__pyoq.bcast(cvj__xse)
    else:
        if bodo.get_rank() == 0 or is_independent:
            edbj__nsc = conn.cursor()
            kwgdf__ypit = tracing.Event('execute_query', is_parallel=False)
            edbj__nsc = conn.cursor()
            edbj__nsc.execute(query)
            kwgdf__ypit.finalize()
            cvj__xse: int = edbj__nsc.rowcount
            batches: 'List[ResultBatch]' = edbj__nsc.get_result_batches()
            if len(batches) > 0 and not isinstance(batches[0], ArrowResultBatch
                ):
                if not is_select_query and len(batches) == 1 and isinstance(
                    batches[0], JSONResultBatch):
                    batches = [FakeArrowJSONResultBatch(x, schema) for x in
                        batches]
                else:
                    raise BodoError(
                        f"Batches returns from Snowflake don't match the expected format. Expected Arrow batches but got {type(batches[0])}"
                        )
            edbj__nsc.close()
        if not is_independent:
            cvj__xse, batches, schema = jrqw__pyoq.bcast((cvj__xse, batches,
                schema))
    tivq__xun = SnowflakeDataset(batches, schema, conn)
    igegh__hgqsf.finalize()
    return tivq__xun, cvj__xse


def create_internal_stage(cursor: 'SnowflakeCursor', is_temporary: bool=False
    ) ->str:
    igegh__hgqsf = tracing.Event('create_internal_stage', is_parallel=False)
    try:
        import snowflake.connector
    except ImportError as ywfwy__yqkj:
        raise BodoError(
            "Snowflake Python connector packages not found. Using 'to_sql' with Snowflake requires snowflake-connector-python. This can be installed by calling 'conda install -c conda-forge snowflake-connector-python' or 'pip install snowflake-connector-python'."
            )
    stage_name = ''
    tue__pmu = None
    while True:
        try:
            stage_name = f'bodo_io_snowflake_{uuid4()}'
            if is_temporary:
                pslwv__xmlgm = 'CREATE TEMPORARY STAGE'
            else:
                pslwv__xmlgm = 'CREATE STAGE'
            fotdq__hmvyv = (
                f'{pslwv__xmlgm} "{stage_name}" /* Python:bodo.io.snowflake.create_internal_stage() */ '
                )
            cursor.execute(fotdq__hmvyv, _is_internal=True).fetchall()
            break
        except snowflake.connector.ProgrammingError as rpa__trpr:
            if rpa__trpr.msg is not None and rpa__trpr.msg.endswith(
                'already exists.'):
                continue
            tue__pmu = rpa__trpr.msg
            break
    igegh__hgqsf.finalize()
    if tue__pmu is not None:
        raise snowflake.connector.ProgrammingError(tue__pmu)
    return stage_name


def drop_internal_stage(cursor: 'SnowflakeCursor', stage_name: str):
    igegh__hgqsf = tracing.Event('drop_internal_stage', is_parallel=False)
    apanq__eczyl = (
        f'DROP STAGE "{stage_name}" /* Python:bodo.io.snowflake.drop_internal_stage() */ '
        )
    cursor.execute(apanq__eczyl, _is_internal=True)
    igegh__hgqsf.finalize()


def do_upload_and_cleanup(cursor: 'SnowflakeCursor', chunk_idx: int,
    chunk_path: str, stage_name: str):

    def upload_cleanup_thread_func(chunk_idx, chunk_path, stage_name):
        azyw__ndd = tracing.Event(f'upload_parquet_file{chunk_idx}',
            is_parallel=False)
        jvqu__rfc = (
            f'PUT \'file://{chunk_path}\' @"{stage_name}" AUTO_COMPRESS=FALSE /* Python:bodo.io.snowflake.do_upload_and_cleanup() */'
            )
        cursor.execute(jvqu__rfc, _is_internal=True).fetchall()
        azyw__ndd.finalize()
        os.remove(chunk_path)
    if SF_WRITE_OVERLAP_UPLOAD:
        iuako__lwobg = ExceptionPropagatingThread(target=
            upload_cleanup_thread_func, args=(chunk_idx, chunk_path,
            stage_name))
        iuako__lwobg.start()
    else:
        upload_cleanup_thread_func(chunk_idx, chunk_path, stage_name)
        iuako__lwobg = None
    return iuako__lwobg


def create_table_handle_exists(cursor: 'SnowflakeCursor', stage_name: str,
    location: str, sf_schema, if_exists: str):
    igegh__hgqsf = tracing.Event('create_table_if_not_exists', is_parallel=
        False)
    try:
        import snowflake.connector
    except ImportError as ywfwy__yqkj:
        raise BodoError(
            "Snowflake Python connector packages not found. Using 'to_sql' with Snowflake requires snowflake-connector-python. This can be installed by calling 'conda install -c conda-forge snowflake-connector-python' or 'pip install snowflake-connector-python'."
            )
    if if_exists == 'fail':
        huqo__ezu = 'CREATE TABLE'
    elif if_exists == 'replace':
        huqo__ezu = 'CREATE OR REPLACE TABLE'
    elif if_exists == 'append':
        huqo__ezu = 'CREATE TABLE IF NOT EXISTS'
    else:
        raise ValueError(f"'{if_exists}' is not valid for if_exists")
    suom__tzwsf = tracing.Event('create_table', is_parallel=False)
    zpu__ltbv = ', '.join([f'"{dzlgq__ithb}" {sf_schema[dzlgq__ithb]}' for
        dzlgq__ithb in sf_schema.keys()])
    jyqxf__joaap = (
        f'{huqo__ezu} {location} ({zpu__ltbv}) /* Python:bodo.io.snowflake.create_table_if_not_exists() */'
        )
    cursor.execute(jyqxf__joaap, _is_internal=True)
    suom__tzwsf.finalize()
    igegh__hgqsf.finalize()


def execute_copy_into(cursor: 'SnowflakeCursor', stage_name: str, location:
    str, sf_schema):
    igegh__hgqsf = tracing.Event('execute_copy_into', is_parallel=False)
    kxdde__cpb = ','.join([f'"{dzlgq__ithb}"' for dzlgq__ithb in sf_schema.
        keys()])
    ojlu__ltr = {dzlgq__ithb: ('::binary' if sf_schema[dzlgq__ithb] ==
        'BINARY' else '::string' if sf_schema[dzlgq__ithb].startswith(
        'TIME') else '') for dzlgq__ithb in sf_schema.keys()}
    eldj__muy = ','.join([f'$1:"{dzlgq__ithb}"{ojlu__ltr[dzlgq__ithb]}' for
        dzlgq__ithb in sf_schema.keys()])
    laqke__ghq = (
        f'COPY INTO {location} ({kxdde__cpb}) FROM (SELECT {eldj__muy} FROM @"{stage_name}") FILE_FORMAT=(TYPE=PARQUET COMPRESSION=AUTO BINARY_AS_TEXT=False) PURGE=TRUE ON_ERROR={SF_WRITE_COPY_INTO_ON_ERROR} /* Python:bodo.io.snowflake.execute_copy_into() */'
        )
    gij__ksi = cursor.execute(laqke__ghq, _is_internal=True).fetchall()
    ecr__kwse = sum(1 if lnf__koad[1] == 'LOADED' else 0 for lnf__koad in
        gij__ksi)
    worhq__mmov = len(gij__ksi)
    scovx__vcnjn = sum(int(lnf__koad[3]) for lnf__koad in gij__ksi)
    bwlr__diux = ecr__kwse, worhq__mmov, scovx__vcnjn, gij__ksi
    igegh__hgqsf.add_attribute('copy_into_nsuccess', ecr__kwse)
    igegh__hgqsf.add_attribute('copy_into_nchunks', worhq__mmov)
    igegh__hgqsf.add_attribute('copy_into_nrows', scovx__vcnjn)
    if os.environ.get('BODO_SF_WRITE_DEBUG') is not None:
        print(f'[Snowflake Write] copy_into results: {repr(gij__ksi)}')
    igegh__hgqsf.finalize()
    return bwlr__diux


try:
    import snowflake.connector
    snowflake_connector_cursor_python_type = (snowflake.connector.cursor.
        SnowflakeCursor)
except (ImportError, AttributeError) as ywfwy__yqkj:
    snowflake_connector_cursor_python_type = None
SnowflakeConnectorCursorType = install_py_obj_class(types_name=
    'snowflake_connector_cursor_type', python_type=
    snowflake_connector_cursor_python_type, module=sys.modules[__name__],
    class_name='SnowflakeConnectorCursorType', model_name=
    'SnowflakeConnectorCursorModel')
TemporaryDirectoryType = install_py_obj_class(types_name=
    'temporary_directory_type', python_type=TemporaryDirectory, module=sys.
    modules[__name__], class_name='TemporaryDirectoryType', model_name=
    'TemporaryDirectoryModel')


def get_snowflake_stage_info(cursor: 'SnowflakeCursor', stage_name: str,
    tmp_folder: TemporaryDirectory) ->Dict:
    igegh__hgqsf = tracing.Event('get_snowflake_stage_info', is_parallel=False)
    lniib__zfrec = os.path.join(tmp_folder.name,
        f'get_credentials_{uuid4()}.parquet')
    lniib__zfrec = lniib__zfrec.replace('\\', '\\\\').replace("'", "\\'")
    jvqu__rfc = (
        f'PUT \'file://{lniib__zfrec}\' @"{stage_name}" AUTO_COMPRESS=FALSE /* Python:bodo.io.snowflake.get_snowflake_stage_info() */'
        )
    weyz__bkcbn = cursor._execute_helper(jvqu__rfc, is_internal=True)
    igegh__hgqsf.finalize()
    return weyz__bkcbn


def connect_and_get_upload_info(conn_str: str):
    igegh__hgqsf = tracing.Event('connect_and_get_upload_info')
    jrqw__pyoq = MPI.COMM_WORLD
    cdfa__kaeow = jrqw__pyoq.Get_rank()
    tmp_folder = TemporaryDirectory()
    cursor = None
    stage_name = ''
    zzchj__vdfp = ''
    lydt__zyv = {}
    old_creds = {}
    old_core_site = ''
    ghu__lgbn = ''
    old_sas_token = ''
    nptm__uxetr = None
    if cdfa__kaeow == 0:
        try:
            conn = snowflake_connect(conn_str)
            cursor = conn.cursor()
            is_temporary = not SF_WRITE_UPLOAD_USING_PUT
            stage_name = create_internal_stage(cursor, is_temporary=
                is_temporary)
            if SF_WRITE_UPLOAD_USING_PUT:
                zzchj__vdfp = ''
            else:
                weyz__bkcbn = get_snowflake_stage_info(cursor, stage_name,
                    tmp_folder)
                wfno__nap = weyz__bkcbn['data']['uploadInfo']
                jkzhm__ern = wfno__nap.get('locationType', 'UNKNOWN')
                nbl__hplb = False
                if jkzhm__ern == 'S3':
                    aovf__fttb, _, qbj__dmzt = wfno__nap['location'].partition(
                        '/')
                    qbj__dmzt = qbj__dmzt.rstrip('/')
                    zzchj__vdfp = f's3://{aovf__fttb}/{qbj__dmzt}/'
                    lydt__zyv = {'AWS_ACCESS_KEY_ID': wfno__nap['creds'][
                        'AWS_KEY_ID'], 'AWS_SECRET_ACCESS_KEY': wfno__nap[
                        'creds']['AWS_SECRET_KEY'], 'AWS_SESSION_TOKEN':
                        wfno__nap['creds']['AWS_TOKEN'],
                        'AWS_DEFAULT_REGION': wfno__nap['region']}
                elif jkzhm__ern == 'AZURE':
                    oavvp__gtvuw = False
                    try:
                        import bodo_azurefs_sas_token_provider
                        oavvp__gtvuw = True
                    except ImportError as ywfwy__yqkj:
                        pass
                    mbf__ztht = len(os.environ.get('HADOOP_HOME', '')
                        ) > 0 and len(os.environ.get('ARROW_LIBHDFS_DIR', '')
                        ) > 0 and len(os.environ.get('CLASSPATH', '')) > 0
                    if oavvp__gtvuw and mbf__ztht:
                        amxh__pan, _, qbj__dmzt = wfno__nap['location'
                            ].partition('/')
                        qbj__dmzt = qbj__dmzt.rstrip('/')
                        fwl__dvhf = wfno__nap['storageAccount']
                        ghu__lgbn = wfno__nap['creds']['AZURE_SAS_TOKEN'
                            ].lstrip('?')
                        if len(qbj__dmzt) == 0:
                            zzchj__vdfp = (
                                f'abfs://{amxh__pan}@{fwl__dvhf}.dfs.core.windows.net/'
                                )
                        else:
                            zzchj__vdfp = (
                                f'abfs://{amxh__pan}@{fwl__dvhf}.dfs.core.windows.net/{qbj__dmzt}/'
                                )
                        if not 'BODO_PLATFORM_WORKSPACE_UUID' in os.environ:
                            warnings.warn(BodoWarning(
                                """Detected Azure Stage. Bodo will try to upload to the stage directly. If this fails, there might be issues with your Hadoop configuration and you may need to use the PUT method instead by setting
import bodo
bodo.io.snowflake.SF_WRITE_UPLOAD_USING_PUT = True
before calling this function."""
                                ))
                    else:
                        nbl__hplb = True
                        eop__tishw = 'Detected Azure Stage. '
                        if not oavvp__gtvuw:
                            eop__tishw += """Required package bodo_azurefs_sas_token_provider is not installed. To use direct upload to stage in the future, install the package using: 'conda install bodo-azurefs-sas-token-provider -c bodo.ai -c conda-forge'.
"""
                        if not mbf__ztht:
                            eop__tishw += """You need to download and set up Hadoop. For more information, refer to our documentation: https://docs.bodo.ai/latest/file_io/?h=hdfs#HDFS.
"""
                        eop__tishw += (
                            'Falling back to PUT command for upload for now.')
                        warnings.warn(BodoWarning(eop__tishw))
                else:
                    nbl__hplb = True
                    warnings.warn(BodoWarning(
                        f"Direct upload to stage is not supported for internal stage type '{jkzhm__ern}'. Falling back to PUT command for upload."
                        ))
                if nbl__hplb:
                    drop_internal_stage(cursor, stage_name)
                    stage_name = create_internal_stage(cursor, is_temporary
                        =False)
        except Exception as lnf__koad:
            nptm__uxetr = RuntimeError(str(lnf__koad))
            if os.environ.get('BODO_SF_WRITE_DEBUG') is not None:
                print(''.join(traceback.format_exception(None, lnf__koad,
                    lnf__koad.__traceback__)))
    nptm__uxetr = jrqw__pyoq.bcast(nptm__uxetr)
    if isinstance(nptm__uxetr, Exception):
        raise nptm__uxetr
    zzchj__vdfp = jrqw__pyoq.bcast(zzchj__vdfp)
    azure_stage_direct_upload = zzchj__vdfp.startswith('abfs://')
    if zzchj__vdfp == '':
        hnn__lhsfk = True
        zzchj__vdfp = tmp_folder.name + '/'
        if cdfa__kaeow != 0:
            conn = snowflake_connect(conn_str)
            cursor = conn.cursor()
    else:
        hnn__lhsfk = False
        lydt__zyv = jrqw__pyoq.bcast(lydt__zyv)
        old_creds = update_env_vars(lydt__zyv)
        if azure_stage_direct_upload:
            import bodo_azurefs_sas_token_provider
            bodo.HDFS_CORE_SITE_LOC_DIR.initialize()
            old_core_site = update_file_contents(bodo.HDFS_CORE_SITE_LOC,
                SF_AZURE_WRITE_HDFS_CORE_SITE)
            ghu__lgbn = jrqw__pyoq.bcast(ghu__lgbn)
            old_sas_token = update_file_contents(
                SF_AZURE_WRITE_SAS_TOKEN_FILE_LOCATION, ghu__lgbn)
    stage_name = jrqw__pyoq.bcast(stage_name)
    igegh__hgqsf.finalize()
    return (cursor, tmp_folder, stage_name, zzchj__vdfp, hnn__lhsfk,
        old_creds, azure_stage_direct_upload, old_core_site, old_sas_token)


def create_table_copy_into(cursor: 'SnowflakeCursor', stage_name: str,
    location: str, sf_schema, if_exists: str, old_creds, tmp_folder:
    TemporaryDirectory, azure_stage_direct_upload: bool, old_core_site: str,
    old_sas_token: str):
    igegh__hgqsf = tracing.Event('create_table_copy_into', is_parallel=False)
    jrqw__pyoq = MPI.COMM_WORLD
    cdfa__kaeow = jrqw__pyoq.Get_rank()
    nptm__uxetr = None
    if cdfa__kaeow == 0:
        try:
            ubbhk__aksvo = (
                'BEGIN /* Python:bodo.io.snowflake.create_table_copy_into() */'
                )
            cursor.execute(ubbhk__aksvo)
            create_table_handle_exists(cursor, stage_name, location,
                sf_schema, if_exists)
            ecr__kwse, worhq__mmov, scovx__vcnjn, qhb__qsnzr = (
                execute_copy_into(cursor, stage_name, location, sf_schema))
            if ecr__kwse != worhq__mmov:
                raise BodoError(
                    f'Snowflake write copy_into failed: {qhb__qsnzr}')
            pcms__gxesh = (
                'COMMIT /* Python:bodo.io.snowflake.create_table_copy_into() */'
                )
            cursor.execute(pcms__gxesh)
            drop_internal_stage(cursor, stage_name)
            cursor.close()
        except Exception as lnf__koad:
            nptm__uxetr = RuntimeError(str(lnf__koad))
            if os.environ.get('BODO_SF_WRITE_DEBUG') is not None:
                print(''.join(traceback.format_exception(None, lnf__koad,
                    lnf__koad.__traceback__)))
    nptm__uxetr = jrqw__pyoq.bcast(nptm__uxetr)
    if isinstance(nptm__uxetr, Exception):
        raise nptm__uxetr
    update_env_vars(old_creds)
    tmp_folder.cleanup()
    if azure_stage_direct_upload:
        update_file_contents(bodo.HDFS_CORE_SITE_LOC, old_core_site)
        update_file_contents(SF_AZURE_WRITE_SAS_TOKEN_FILE_LOCATION,
            old_sas_token)
    igegh__hgqsf.finalize()
