import os
import warnings
from collections import defaultdict
from glob import has_magic
from typing import Optional
from urllib.parse import urlparse
import llvmlite.binding as ll
import numba
import numpy as np
import pyarrow
import pyarrow as pa
import pyarrow.dataset as ds
from numba.core import types
from numba.extending import NativeValue, box, intrinsic, models, overload, register_model, unbox
from pyarrow._fs import PyFileSystem
from pyarrow.fs import FSSpecHandler
import bodo
import bodo.utils.tracing as tracing
from bodo.hiframes.pd_categorical_ext import CategoricalArrayType, PDCategoricalDtype
from bodo.io.fs_io import get_hdfs_fs, get_s3_fs_from_path
from bodo.io.helpers import _get_numba_typ_from_pa_typ
from bodo.libs.dict_arr_ext import dict_str_arr_type
from bodo.libs.distributed_api import get_end, get_start
from bodo.utils.typing import BodoError, BodoWarning, FileInfo, FileSchema, get_overload_const_str
REMOTE_FILESYSTEMS = {'s3', 'gcs', 'gs', 'http', 'hdfs', 'abfs', 'abfss'}
READ_STR_AS_DICT_THRESHOLD = 1.0
list_of_files_error_msg = (
    '. Make sure the list/glob passed to read_parquet() only contains paths to files (no directories)'
    )


class ParquetPredicateType(types.Type):

    def __init__(self):
        super(ParquetPredicateType, self).__init__(name=
            'ParquetPredicateType()')


parquet_predicate_type = ParquetPredicateType()
types.parquet_predicate_type = parquet_predicate_type
register_model(ParquetPredicateType)(models.OpaqueModel)


@unbox(ParquetPredicateType)
def unbox_parquet_predicate_type(typ, val, c):
    c.pyapi.incref(val)
    return NativeValue(val)


@box(ParquetPredicateType)
def box_parquet_predicate_type(typ, val, c):
    c.pyapi.incref(val)
    return val


class ParquetFileInfo(FileInfo):

    def __init__(self, columns, storage_options=None, input_file_name_col=
        None, read_as_dict_cols=None, use_hive=True):
        self.columns = columns
        self.storage_options = storage_options
        self.input_file_name_col = input_file_name_col
        self.read_as_dict_cols = read_as_dict_cols
        self.use_hive = use_hive
        super().__init__()

    def _get_schema(self, fname):
        try:
            return parquet_file_schema(fname, selected_columns=self.columns,
                storage_options=self.storage_options, input_file_name_col=
                self.input_file_name_col, read_as_dict_cols=self.
                read_as_dict_cols, use_hive=self.use_hive)
        except OSError as nlqc__hdua:
            if 'non-file path' in str(nlqc__hdua):
                raise FileNotFoundError(str(nlqc__hdua))
            raise


def get_filters_pyobject(dnf_filter_str, expr_filter_str, vars):
    pass


@overload(get_filters_pyobject, no_unliteral=True)
def overload_get_filters_pyobject(dnf_filter_str, expr_filter_str, var_tup):
    ypvz__qxaho = get_overload_const_str(dnf_filter_str)
    vob__xhj = get_overload_const_str(expr_filter_str)
    jkb__zkzv = ', '.join(f'f{pdxu__lwodc}' for pdxu__lwodc in range(len(
        var_tup)))
    hdxzs__dncy = 'def impl(dnf_filter_str, expr_filter_str, var_tup):\n'
    if len(var_tup):
        hdxzs__dncy += f'  {jkb__zkzv}, = var_tup\n'
    hdxzs__dncy += """  with numba.objmode(dnf_filters_py='parquet_predicate_type', expr_filters_py='parquet_predicate_type'):
"""
    hdxzs__dncy += f'    dnf_filters_py = {ypvz__qxaho}\n'
    hdxzs__dncy += f'    expr_filters_py = {vob__xhj}\n'
    hdxzs__dncy += '  return (dnf_filters_py, expr_filters_py)\n'
    usfop__wrg = {}
    grmgc__vrvc = globals()
    grmgc__vrvc['numba'] = numba
    exec(hdxzs__dncy, grmgc__vrvc, usfop__wrg)
    return usfop__wrg['impl']


def unify_schemas(schemas):
    lqa__gym = []
    for schema in schemas:
        for pdxu__lwodc in range(len(schema)):
            xjvk__pnd = schema.field(pdxu__lwodc)
            if xjvk__pnd.type == pa.large_string():
                schema = schema.set(pdxu__lwodc, xjvk__pnd.with_type(pa.
                    string()))
            elif xjvk__pnd.type == pa.large_binary():
                schema = schema.set(pdxu__lwodc, xjvk__pnd.with_type(pa.
                    binary()))
            elif isinstance(xjvk__pnd.type, (pa.ListType, pa.LargeListType)
                ) and xjvk__pnd.type.value_type in (pa.string(), pa.
                large_string()):
                schema = schema.set(pdxu__lwodc, xjvk__pnd.with_type(pa.
                    list_(pa.field(xjvk__pnd.type.value_field.name, pa.
                    string()))))
            elif isinstance(xjvk__pnd.type, pa.LargeListType):
                schema = schema.set(pdxu__lwodc, xjvk__pnd.with_type(pa.
                    list_(pa.field(xjvk__pnd.type.value_field.name,
                    xjvk__pnd.type.value_type))))
        lqa__gym.append(schema)
    return pa.unify_schemas(lqa__gym)


class ParquetDataset:

    def __init__(self, pa_pq_dataset, prefix=''):
        self.schema: pa.Schema = pa_pq_dataset.schema
        self.filesystem = None
        self._bodo_total_rows = 0
        self._prefix = prefix
        self.partitioning = None
        partitioning = pa_pq_dataset.partitioning
        self.partition_names = ([] if partitioning is None or partitioning.
            schema == pa_pq_dataset.schema else list(partitioning.schema.names)
            )
        if self.partition_names:
            self.partitioning_dictionaries = partitioning.dictionaries
            self.partitioning_cls = partitioning.__class__
            self.partitioning_schema = partitioning.schema
        else:
            self.partitioning_dictionaries = {}
        for pdxu__lwodc in range(len(self.schema)):
            xjvk__pnd = self.schema.field(pdxu__lwodc)
            if xjvk__pnd.type == pa.large_string():
                self.schema = self.schema.set(pdxu__lwodc, xjvk__pnd.
                    with_type(pa.string()))
        self.pieces = [ParquetPiece(frag, partitioning, self.
            partition_names) for frag in pa_pq_dataset._dataset.
            get_fragments(filter=pa_pq_dataset._filter_expression)]

    def set_fs(self, fs):
        self.filesystem = fs
        for ksfl__hhi in self.pieces:
            ksfl__hhi.filesystem = fs

    def __setstate__(self, state):
        self.__dict__ = state
        if self.partition_names:
            apre__dur = {ksfl__hhi: self.partitioning_dictionaries[
                pdxu__lwodc] for pdxu__lwodc, ksfl__hhi in enumerate(self.
                partition_names)}
            self.partitioning = self.partitioning_cls(self.
                partitioning_schema, apre__dur)


class ParquetPiece(object):

    def __init__(self, frag, partitioning, partition_names):
        self._frag = None
        self.format = frag.format
        self.path = frag.path
        self._bodo_num_rows = 0
        self.partition_keys = []
        if partitioning is not None:
            self.partition_keys = ds._get_partition_keys(frag.
                partition_expression)
            self.partition_keys = [(feeao__bur, partitioning.dictionaries[
                pdxu__lwodc].index(self.partition_keys[feeao__bur]).as_py()
                ) for pdxu__lwodc, feeao__bur in enumerate(partition_names)]

    @property
    def frag(self):
        if self._frag is None:
            self._frag = self.format.make_fragment(self.path, self.filesystem)
            del self.format
        return self._frag

    @property
    def metadata(self):
        return self.frag.metadata

    @property
    def num_row_groups(self):
        return self.frag.num_row_groups


def get_parquet_dataset(fpath, get_row_counts: bool=True, dnf_filters=None,
    expr_filters=None, storage_options=None, read_categories: bool=False,
    is_parallel=False, tot_rows_to_read: Optional[int]=None,
    typing_pa_schema: Optional[pa.Schema]=None, use_hive: bool=True,
    partitioning='hive') ->ParquetDataset:
    if not use_hive:
        partitioning = None
    if get_row_counts:
        wjnfb__esevc = tracing.Event('get_parquet_dataset')
    import time
    import pyarrow as pa
    import pyarrow.parquet as pq
    from mpi4py import MPI
    rutgh__tlms = MPI.COMM_WORLD
    if isinstance(fpath, list):
        idhng__evdjk = urlparse(fpath[0])
        protocol = idhng__evdjk.scheme
        yvpw__jsao = idhng__evdjk.netloc
        for pdxu__lwodc in range(len(fpath)):
            xjvk__pnd = fpath[pdxu__lwodc]
            emp__axxm = urlparse(xjvk__pnd)
            if emp__axxm.scheme != protocol:
                raise BodoError(
                    'All parquet files must use the same filesystem protocol')
            if emp__axxm.netloc != yvpw__jsao:
                raise BodoError(
                    'All parquet files must be in the same S3 bucket')
            fpath[pdxu__lwodc] = xjvk__pnd.rstrip('/')
    else:
        idhng__evdjk = urlparse(fpath)
        protocol = idhng__evdjk.scheme
        fpath = fpath.rstrip('/')
    if protocol in {'gcs', 'gs'}:
        try:
            import gcsfs
        except ImportError as cxqe__qhvd:
            anhk__vzwwq = """Couldn't import gcsfs, which is required for Google cloud access. gcsfs can be installed by calling 'conda install -c conda-forge gcsfs'.
"""
            raise BodoError(anhk__vzwwq)
    if protocol == 'http':
        try:
            import fsspec
        except ImportError as cxqe__qhvd:
            anhk__vzwwq = """Couldn't import fsspec, which is required for http access. fsspec can be installed by calling 'conda install -c conda-forge fsspec'.
"""
    fs = []

    def getfs(parallel=False):
        if len(fs) == 1:
            return fs[0]
        if protocol == 's3':
            fs.append(get_s3_fs_from_path(fpath, parallel=parallel,
                storage_options=storage_options) if not isinstance(fpath,
                list) else get_s3_fs_from_path(fpath[0], parallel=parallel,
                storage_options=storage_options))
        elif protocol in {'gcs', 'gs'}:
            palzj__tcgve = gcsfs.GCSFileSystem(token=None)
            fs.append(PyFileSystem(FSSpecHandler(palzj__tcgve)))
        elif protocol == 'http':
            fs.append(PyFileSystem(FSSpecHandler(fsspec.filesystem('http'))))
        elif protocol in {'hdfs', 'abfs', 'abfss'}:
            fs.append(get_hdfs_fs(fpath) if not isinstance(fpath, list) else
                get_hdfs_fs(fpath[0]))
        else:
            fs.append(pa.fs.LocalFileSystem())
        return fs[0]

    def glob(protocol, fs, path):
        if not protocol and fs is None:
            from fsspec.implementations.local import LocalFileSystem
            fs = LocalFileSystem()
        if isinstance(fs, pa.fs.FileSystem):
            from fsspec.implementations.arrow import ArrowFSWrapper
            fs = ArrowFSWrapper(fs)
        try:
            hzus__vez = fs.glob(path)
        except:
            raise BodoError(
                f'glob pattern expansion not supported for {protocol}')
        if len(hzus__vez) == 0:
            raise BodoError('No files found matching glob pattern')
        return hzus__vez
    fdqx__gsbo = False
    if get_row_counts:
        yxvn__hdhk = getfs(parallel=True)
        fdqx__gsbo = bodo.parquet_validate_schema
    if bodo.get_rank() == 0:
        vsbd__zoxu = 1
        tjxdf__bwmfv = os.cpu_count()
        if tjxdf__bwmfv is not None and tjxdf__bwmfv > 1:
            vsbd__zoxu = tjxdf__bwmfv // 2
        try:
            if get_row_counts:
                jleqk__elrey = tracing.Event('pq.ParquetDataset',
                    is_parallel=False)
                if tracing.is_tracing():
                    jleqk__elrey.add_attribute('g_dnf_filter', str(dnf_filters)
                        )
            mtdbx__ibw = pa.io_thread_count()
            pa.set_io_thread_count(vsbd__zoxu)
            prefix = ''
            if protocol == 's3':
                prefix = 's3://'
            elif protocol in {'hdfs', 'abfs', 'abfss'}:
                prefix = f'{protocol}://{idhng__evdjk.netloc}'
            if prefix:
                if isinstance(fpath, list):
                    yym__brzmp = [xjvk__pnd[len(prefix):] for xjvk__pnd in
                        fpath]
                else:
                    yym__brzmp = fpath[len(prefix):]
            else:
                yym__brzmp = fpath
            if isinstance(yym__brzmp, list):
                zuh__pjjv = []
                for ksfl__hhi in yym__brzmp:
                    if has_magic(ksfl__hhi):
                        zuh__pjjv += glob(protocol, getfs(), ksfl__hhi)
                    else:
                        zuh__pjjv.append(ksfl__hhi)
                yym__brzmp = zuh__pjjv
            elif has_magic(yym__brzmp):
                yym__brzmp = glob(protocol, getfs(), yym__brzmp)
            rwui__tkilt = pq.ParquetDataset(yym__brzmp, filesystem=getfs(),
                filters=None, use_legacy_dataset=False, partitioning=
                partitioning)
            if dnf_filters is not None:
                rwui__tkilt._filters = dnf_filters
                rwui__tkilt._filter_expression = pq._filters_to_expression(
                    dnf_filters)
            ech__gjqif = len(rwui__tkilt.files)
            rwui__tkilt = ParquetDataset(rwui__tkilt, prefix)
            pa.set_io_thread_count(mtdbx__ibw)
            if typing_pa_schema:
                rwui__tkilt.schema = typing_pa_schema
            if get_row_counts:
                if dnf_filters is not None:
                    jleqk__elrey.add_attribute('num_pieces_before_filter',
                        ech__gjqif)
                    jleqk__elrey.add_attribute('num_pieces_after_filter',
                        len(rwui__tkilt.pieces))
                jleqk__elrey.finalize()
        except Exception as nlqc__hdua:
            if isinstance(nlqc__hdua, IsADirectoryError):
                nlqc__hdua = BodoError(list_of_files_error_msg)
            elif isinstance(fpath, list) and isinstance(nlqc__hdua, (
                OSError, FileNotFoundError)):
                nlqc__hdua = BodoError(str(nlqc__hdua) +
                    list_of_files_error_msg)
            else:
                nlqc__hdua = BodoError(
                    f"""error from pyarrow: {type(nlqc__hdua).__name__}: {str(nlqc__hdua)}
"""
                    )
            rutgh__tlms.bcast(nlqc__hdua)
            raise nlqc__hdua
        if get_row_counts:
            bzlpk__pmg = tracing.Event('bcast dataset')
        rwui__tkilt = rutgh__tlms.bcast(rwui__tkilt)
    else:
        if get_row_counts:
            bzlpk__pmg = tracing.Event('bcast dataset')
        rwui__tkilt = rutgh__tlms.bcast(None)
        if isinstance(rwui__tkilt, Exception):
            snqk__dfv = rwui__tkilt
            raise snqk__dfv
    rwui__tkilt.set_fs(getfs())
    if get_row_counts:
        bzlpk__pmg.finalize()
    if get_row_counts and tot_rows_to_read == 0:
        get_row_counts = fdqx__gsbo = False
    if get_row_counts or fdqx__gsbo:
        if get_row_counts and tracing.is_tracing():
            sgw__jct = tracing.Event('get_row_counts')
            sgw__jct.add_attribute('g_num_pieces', len(rwui__tkilt.pieces))
            sgw__jct.add_attribute('g_expr_filters', str(expr_filters))
        ndx__xovs = 0.0
        num_pieces = len(rwui__tkilt.pieces)
        start = get_start(num_pieces, bodo.get_size(), bodo.get_rank())
        jsdog__uotm = get_end(num_pieces, bodo.get_size(), bodo.get_rank())
        xqjx__vdwuj = 0
        dge__irs = 0
        vzgil__oyg = 0
        uky__iylj = True
        if expr_filters is not None:
            import random
            random.seed(37)
            xuuai__lvd = random.sample(rwui__tkilt.pieces, k=len(
                rwui__tkilt.pieces))
        else:
            xuuai__lvd = rwui__tkilt.pieces
        fpaths = [ksfl__hhi.path for ksfl__hhi in xuuai__lvd[start:jsdog__uotm]
            ]
        vsbd__zoxu = min(int(os.environ.get('BODO_MIN_IO_THREADS', 4)), 4)
        pa.set_io_thread_count(vsbd__zoxu)
        pa.set_cpu_count(vsbd__zoxu)
        snqk__dfv = None
        try:
            mucy__xgfl = ds.dataset(fpaths, filesystem=rwui__tkilt.
                filesystem, partitioning=rwui__tkilt.partitioning)
            for vhs__edsom, frag in zip(xuuai__lvd[start:jsdog__uotm],
                mucy__xgfl.get_fragments()):
                if fdqx__gsbo:
                    tsn__onj = frag.metadata.schema.to_arrow_schema()
                    hih__kpow = set(tsn__onj.names)
                    cvns__hoz = set(rwui__tkilt.schema.names) - set(rwui__tkilt
                        .partition_names)
                    if cvns__hoz != hih__kpow:
                        utjpl__hndqk = hih__kpow - cvns__hoz
                        ykpy__gar = cvns__hoz - hih__kpow
                        dhq__pod = f'Schema in {vhs__edsom} was different.\n'
                        if typing_pa_schema is not None:
                            if utjpl__hndqk:
                                dhq__pod += f"""File contains column(s) {utjpl__hndqk} not found in other files in the dataset.
"""
                                raise BodoError(dhq__pod)
                        else:
                            if utjpl__hndqk:
                                dhq__pod += f"""File contains column(s) {utjpl__hndqk} not found in other files in the dataset.
"""
                            if ykpy__gar:
                                dhq__pod += f"""File missing column(s) {ykpy__gar} found in other files in the dataset.
"""
                            raise BodoError(dhq__pod)
                    try:
                        rwui__tkilt.schema = unify_schemas([rwui__tkilt.
                            schema, tsn__onj])
                    except Exception as nlqc__hdua:
                        dhq__pod = (
                            f'Schema in {vhs__edsom} was different.\n' +
                            str(nlqc__hdua))
                        raise BodoError(dhq__pod)
                kkbf__bvhsk = time.time()
                fryxd__bjp = frag.scanner(schema=mucy__xgfl.schema, filter=
                    expr_filters, use_threads=True).count_rows()
                ndx__xovs += time.time() - kkbf__bvhsk
                vhs__edsom._bodo_num_rows = fryxd__bjp
                xqjx__vdwuj += fryxd__bjp
                dge__irs += frag.num_row_groups
                vzgil__oyg += sum(tib__ubk.total_byte_size for tib__ubk in
                    frag.row_groups)
        except Exception as nlqc__hdua:
            snqk__dfv = nlqc__hdua
        if rutgh__tlms.allreduce(snqk__dfv is not None, op=MPI.LOR):
            for snqk__dfv in rutgh__tlms.allgather(snqk__dfv):
                if snqk__dfv:
                    if isinstance(fpath, list) and isinstance(snqk__dfv, (
                        OSError, FileNotFoundError)):
                        raise BodoError(str(snqk__dfv) +
                            list_of_files_error_msg)
                    raise snqk__dfv
        if fdqx__gsbo:
            uky__iylj = rutgh__tlms.allreduce(uky__iylj, op=MPI.LAND)
            if not uky__iylj:
                raise BodoError("Schema in parquet files don't match")
        if get_row_counts:
            rwui__tkilt._bodo_total_rows = rutgh__tlms.allreduce(xqjx__vdwuj,
                op=MPI.SUM)
            pzjzj__zmq = rutgh__tlms.allreduce(dge__irs, op=MPI.SUM)
            ugcgg__yrut = rutgh__tlms.allreduce(vzgil__oyg, op=MPI.SUM)
            rfwd__lscke = np.array([ksfl__hhi._bodo_num_rows for ksfl__hhi in
                rwui__tkilt.pieces])
            rfwd__lscke = rutgh__tlms.allreduce(rfwd__lscke, op=MPI.SUM)
            for ksfl__hhi, xkeqz__terij in zip(rwui__tkilt.pieces, rfwd__lscke
                ):
                ksfl__hhi._bodo_num_rows = xkeqz__terij
            if is_parallel and bodo.get_rank(
                ) == 0 and pzjzj__zmq < bodo.get_size() and pzjzj__zmq != 0:
                warnings.warn(BodoWarning(
                    f"""Total number of row groups in parquet dataset {fpath} ({pzjzj__zmq}) is too small for effective IO parallelization.
For best performance the number of row groups should be greater than the number of workers ({bodo.get_size()}). For more details, refer to
https://docs.bodo.ai/latest/file_io/#parquet-section.
"""
                    ))
            if pzjzj__zmq == 0:
                uutg__imns = 0
            else:
                uutg__imns = ugcgg__yrut // pzjzj__zmq
            if (bodo.get_rank() == 0 and ugcgg__yrut >= 20 * 1048576 and 
                uutg__imns < 1048576 and protocol in REMOTE_FILESYSTEMS):
                warnings.warn(BodoWarning(
                    f'Parquet average row group size is small ({uutg__imns} bytes) and can have negative impact on performance when reading from remote sources'
                    ))
            if tracing.is_tracing():
                sgw__jct.add_attribute('g_total_num_row_groups', pzjzj__zmq)
                sgw__jct.add_attribute('total_scan_time', ndx__xovs)
                jjz__rhjp = np.array([ksfl__hhi._bodo_num_rows for
                    ksfl__hhi in rwui__tkilt.pieces])
                mqh__bra = np.percentile(jjz__rhjp, [25, 50, 75])
                sgw__jct.add_attribute('g_row_counts_min', jjz__rhjp.min())
                sgw__jct.add_attribute('g_row_counts_Q1', mqh__bra[0])
                sgw__jct.add_attribute('g_row_counts_median', mqh__bra[1])
                sgw__jct.add_attribute('g_row_counts_Q3', mqh__bra[2])
                sgw__jct.add_attribute('g_row_counts_max', jjz__rhjp.max())
                sgw__jct.add_attribute('g_row_counts_mean', jjz__rhjp.mean())
                sgw__jct.add_attribute('g_row_counts_std', jjz__rhjp.std())
                sgw__jct.add_attribute('g_row_counts_sum', jjz__rhjp.sum())
                sgw__jct.finalize()
    if read_categories:
        _add_categories_to_pq_dataset(rwui__tkilt)
    if get_row_counts:
        wjnfb__esevc.finalize()
    if fdqx__gsbo:
        if tracing.is_tracing():
            lpw__qvgx = tracing.Event('unify_schemas_across_ranks')
        snqk__dfv = None
        try:
            rwui__tkilt.schema = rutgh__tlms.allreduce(rwui__tkilt.schema,
                bodo.io.helpers.pa_schema_unify_mpi_op)
        except Exception as nlqc__hdua:
            snqk__dfv = nlqc__hdua
        if tracing.is_tracing():
            lpw__qvgx.finalize()
        if rutgh__tlms.allreduce(snqk__dfv is not None, op=MPI.LOR):
            for snqk__dfv in rutgh__tlms.allgather(snqk__dfv):
                if snqk__dfv:
                    dhq__pod = f'Schema in some files were different.\n' + str(
                        snqk__dfv)
                    raise BodoError(dhq__pod)
    return rwui__tkilt


def get_scanner_batches(fpaths, expr_filters, selected_fields,
    avg_num_pieces, is_parallel, filesystem, str_as_dict_cols, start_offset,
    rows_to_read, partitioning, schema):
    import pyarrow as pa
    tjxdf__bwmfv = os.cpu_count()
    if tjxdf__bwmfv is None or tjxdf__bwmfv == 0:
        tjxdf__bwmfv = 2
    igce__clsb = min(int(os.environ.get('BODO_MIN_IO_THREADS', 4)),
        tjxdf__bwmfv)
    wdh__nfr = min(int(os.environ.get('BODO_MAX_IO_THREADS', 16)), tjxdf__bwmfv
        )
    if is_parallel and len(fpaths) > wdh__nfr and len(fpaths
        ) / avg_num_pieces >= 2.0:
        pa.set_io_thread_count(wdh__nfr)
        pa.set_cpu_count(wdh__nfr)
    else:
        pa.set_io_thread_count(igce__clsb)
        pa.set_cpu_count(igce__clsb)
    lgax__bvg = ds.ParquetFileFormat(dictionary_columns=str_as_dict_cols)
    dcd__zgyqu = set(str_as_dict_cols)
    for pdxu__lwodc, name in enumerate(schema.names):
        if name in dcd__zgyqu:
            rhhin__myio = schema.field(pdxu__lwodc)
            atw__nqm = pa.field(name, pa.dictionary(pa.int32(), rhhin__myio
                .type), rhhin__myio.nullable)
            schema = schema.remove(pdxu__lwodc).insert(pdxu__lwodc, atw__nqm)
    rwui__tkilt = ds.dataset(fpaths, filesystem=filesystem, partitioning=
        partitioning, schema=schema, format=lgax__bvg)
    yzs__byuz = rwui__tkilt.schema.names
    ygdxi__aus = [yzs__byuz[iud__jzea] for iud__jzea in selected_fields]
    henu__czx = len(fpaths) <= 3 or start_offset > 0 and len(fpaths) <= 10
    if henu__czx and expr_filters is None:
        wycps__flo = []
        prpe__jxczg = 0
        eigws__zvlt = 0
        for frag in rwui__tkilt.get_fragments():
            gzrn__yrmv = []
            for tib__ubk in frag.row_groups:
                hgmo__how = tib__ubk.num_rows
                if start_offset < prpe__jxczg + hgmo__how:
                    if eigws__zvlt == 0:
                        whlp__dzsu = start_offset - prpe__jxczg
                        duud__flje = min(hgmo__how - whlp__dzsu, rows_to_read)
                    else:
                        duud__flje = min(hgmo__how, rows_to_read - eigws__zvlt)
                    eigws__zvlt += duud__flje
                    gzrn__yrmv.append(tib__ubk.id)
                prpe__jxczg += hgmo__how
                if eigws__zvlt == rows_to_read:
                    break
            wycps__flo.append(frag.subset(row_group_ids=gzrn__yrmv))
            if eigws__zvlt == rows_to_read:
                break
        rwui__tkilt = ds.FileSystemDataset(wycps__flo, rwui__tkilt.schema,
            lgax__bvg, filesystem=rwui__tkilt.filesystem)
        start_offset = whlp__dzsu
    bnak__apkg = rwui__tkilt.scanner(columns=ygdxi__aus, filter=
        expr_filters, use_threads=True).to_reader()
    return rwui__tkilt, bnak__apkg, start_offset


def _add_categories_to_pq_dataset(pq_dataset):
    import pyarrow as pa
    from mpi4py import MPI
    if len(pq_dataset.pieces) < 1:
        raise BodoError(
            'No pieces found in Parquet dataset. Cannot get read categorical values'
            )
    pa_schema = pq_dataset.schema
    ctdcv__jvp = [c for c in pa_schema.names if isinstance(pa_schema.field(
        c).type, pa.DictionaryType) and c not in pq_dataset.partition_names]
    if len(ctdcv__jvp) == 0:
        pq_dataset._category_info = {}
        return
    rutgh__tlms = MPI.COMM_WORLD
    if bodo.get_rank() == 0:
        try:
            teq__xmsv = pq_dataset.pieces[0].frag.head(100, columns=ctdcv__jvp)
            zrxu__aquxy = {c: tuple(teq__xmsv.column(c).chunk(0).dictionary
                .to_pylist()) for c in ctdcv__jvp}
            del teq__xmsv
        except Exception as nlqc__hdua:
            rutgh__tlms.bcast(nlqc__hdua)
            raise nlqc__hdua
        rutgh__tlms.bcast(zrxu__aquxy)
    else:
        zrxu__aquxy = rutgh__tlms.bcast(None)
        if isinstance(zrxu__aquxy, Exception):
            snqk__dfv = zrxu__aquxy
            raise snqk__dfv
    pq_dataset._category_info = zrxu__aquxy


def get_pandas_metadata(schema, num_pieces):
    qbrg__mgiv = None
    denoj__frmww = defaultdict(lambda : None)
    jcmja__zdvt = b'pandas'
    if schema.metadata is not None and jcmja__zdvt in schema.metadata:
        import json
        ohtu__zqk = json.loads(schema.metadata[jcmja__zdvt].decode('utf8'))
        bwvlc__ztull = len(ohtu__zqk['index_columns'])
        if bwvlc__ztull > 1:
            raise BodoError('read_parquet: MultiIndex not supported yet')
        qbrg__mgiv = ohtu__zqk['index_columns'][0] if bwvlc__ztull else None
        if not isinstance(qbrg__mgiv, str) and not isinstance(qbrg__mgiv, dict
            ):
            qbrg__mgiv = None
        for ytqr__roqmo in ohtu__zqk['columns']:
            pjpdf__htdo = ytqr__roqmo['name']
            cxjis__fkx = ytqr__roqmo['pandas_type']
            if (cxjis__fkx.startswith('int') or cxjis__fkx.startswith('float')
                ) and pjpdf__htdo is not None:
                bvia__pofy = ytqr__roqmo['numpy_type']
                if bvia__pofy.startswith('Int') or bvia__pofy.startswith(
                    'Float'):
                    denoj__frmww[pjpdf__htdo] = True
                else:
                    denoj__frmww[pjpdf__htdo] = False
    return qbrg__mgiv, denoj__frmww


def get_str_columns_from_pa_schema(pa_schema):
    str_columns = []
    for pjpdf__htdo in pa_schema.names:
        yhr__hqxh = pa_schema.field(pjpdf__htdo)
        if yhr__hqxh.type in (pa.string(), pa.large_string()):
            str_columns.append(pjpdf__htdo)
    return str_columns


def _pa_schemas_match(pa_schema1, pa_schema2):
    if pa_schema1.names != pa_schema2.names:
        return False
    try:
        unify_schemas([pa_schema1, pa_schema2])
    except:
        return False
    return True


def _get_sample_pq_pieces(pq_dataset, pa_schema, is_iceberg):
    xuuai__lvd = pq_dataset.pieces
    if len(xuuai__lvd) > bodo.get_size():
        import random
        random.seed(37)
        xuuai__lvd = random.sample(xuuai__lvd, bodo.get_size())
    else:
        xuuai__lvd = xuuai__lvd
    if is_iceberg:
        xuuai__lvd = [ksfl__hhi for ksfl__hhi in xuuai__lvd if
            _pa_schemas_match(ksfl__hhi.metadata.schema.to_arrow_schema(),
            pa_schema)]
    return xuuai__lvd


def determine_str_as_dict_columns(pq_dataset, pa_schema, str_columns: list,
    is_iceberg: bool=False) ->set:
    from mpi4py import MPI
    rutgh__tlms = MPI.COMM_WORLD
    if len(str_columns) == 0:
        return set()
    xuuai__lvd = _get_sample_pq_pieces(pq_dataset, pa_schema, is_iceberg)
    str_columns = sorted(str_columns)
    djvnq__drqy = np.zeros(len(str_columns), dtype=np.int64)
    qryhb__actd = np.zeros(len(str_columns), dtype=np.int64)
    if bodo.get_rank() < len(xuuai__lvd):
        vhs__edsom = xuuai__lvd[bodo.get_rank()]
        try:
            metadata = vhs__edsom.metadata
            for pdxu__lwodc in range(vhs__edsom.num_row_groups):
                for adpxs__yar, pjpdf__htdo in enumerate(str_columns):
                    ron__xkdf = pa_schema.get_field_index(pjpdf__htdo)
                    djvnq__drqy[adpxs__yar] += metadata.row_group(pdxu__lwodc
                        ).column(ron__xkdf).total_uncompressed_size
            pme__xumjn = metadata.num_rows
        except Exception as nlqc__hdua:
            if isinstance(nlqc__hdua, (OSError, FileNotFoundError)):
                pme__xumjn = 0
            else:
                raise
    else:
        pme__xumjn = 0
    bgbrz__lurfw = rutgh__tlms.allreduce(pme__xumjn, op=MPI.SUM)
    if bgbrz__lurfw == 0:
        return set()
    rutgh__tlms.Allreduce(djvnq__drqy, qryhb__actd, op=MPI.SUM)
    uos__dcqu = qryhb__actd / bgbrz__lurfw
    avw__vtdzb = set()
    for pdxu__lwodc, qgz__lcfiu in enumerate(uos__dcqu):
        if qgz__lcfiu < READ_STR_AS_DICT_THRESHOLD:
            pjpdf__htdo = str_columns[pdxu__lwodc]
            avw__vtdzb.add(pjpdf__htdo)
    return avw__vtdzb


def parquet_file_schema(file_name, selected_columns, storage_options=None,
    input_file_name_col=None, read_as_dict_cols=None, use_hive=True
    ) ->FileSchema:
    yzs__byuz = []
    bkk__dpz = []
    pq_dataset = get_parquet_dataset(file_name, get_row_counts=False,
        storage_options=storage_options, read_categories=True, use_hive=
        use_hive)
    partition_names = pq_dataset.partition_names
    pa_schema = pq_dataset.schema
    num_pieces = len(pq_dataset.pieces)
    str_columns = get_str_columns_from_pa_schema(pa_schema)
    pjuzl__itoym = set(str_columns)
    if read_as_dict_cols is None:
        read_as_dict_cols = []
    read_as_dict_cols = set(read_as_dict_cols)
    frazx__wqkld = read_as_dict_cols - pjuzl__itoym
    if len(frazx__wqkld) > 0:
        if bodo.get_rank() == 0:
            warnings.warn(
                f'The following columns are not of datatype string and hence cannot be read with dictionary encoding: {frazx__wqkld}'
                , bodo.utils.typing.BodoWarning)
    read_as_dict_cols.intersection_update(pjuzl__itoym)
    pjuzl__itoym = pjuzl__itoym - read_as_dict_cols
    str_columns = [hqck__skv for hqck__skv in str_columns if hqck__skv in
        pjuzl__itoym]
    avw__vtdzb = determine_str_as_dict_columns(pq_dataset, pa_schema,
        str_columns)
    avw__vtdzb.update(read_as_dict_cols)
    yzs__byuz = pa_schema.names
    qbrg__mgiv, denoj__frmww = get_pandas_metadata(pa_schema, num_pieces)
    iigsy__zxuo = []
    uqde__scam = []
    oca__srgaq = []
    for pdxu__lwodc, c in enumerate(yzs__byuz):
        if c in partition_names:
            continue
        yhr__hqxh = pa_schema.field(c)
        drk__snh, ewg__oqkg = _get_numba_typ_from_pa_typ(yhr__hqxh, c ==
            qbrg__mgiv, denoj__frmww[c], pq_dataset._category_info,
            str_as_dict=c in avw__vtdzb)
        iigsy__zxuo.append(drk__snh)
        uqde__scam.append(ewg__oqkg)
        oca__srgaq.append(yhr__hqxh.type)
    if partition_names:
        iigsy__zxuo += [_get_partition_cat_dtype(pq_dataset.
            partitioning_dictionaries[pdxu__lwodc]) for pdxu__lwodc in
            range(len(partition_names))]
        uqde__scam.extend([True] * len(partition_names))
        oca__srgaq.extend([None] * len(partition_names))
    if input_file_name_col is not None:
        yzs__byuz += [input_file_name_col]
        iigsy__zxuo += [dict_str_arr_type]
        uqde__scam.append(True)
        oca__srgaq.append(None)
    vnzu__lyqg = {c: pdxu__lwodc for pdxu__lwodc, c in enumerate(yzs__byuz)}
    if selected_columns is None:
        selected_columns = yzs__byuz
    for c in selected_columns:
        if c not in vnzu__lyqg:
            raise BodoError(f'Selected column {c} not in Parquet file schema')
    if qbrg__mgiv and not isinstance(qbrg__mgiv, dict
        ) and qbrg__mgiv not in selected_columns:
        selected_columns.append(qbrg__mgiv)
    yzs__byuz = selected_columns
    ovdsv__bgnk = []
    bkk__dpz = []
    ffwi__pgo = []
    mki__rst = []
    for pdxu__lwodc, c in enumerate(yzs__byuz):
        fhz__smnu = vnzu__lyqg[c]
        ovdsv__bgnk.append(fhz__smnu)
        bkk__dpz.append(iigsy__zxuo[fhz__smnu])
        if not uqde__scam[fhz__smnu]:
            ffwi__pgo.append(pdxu__lwodc)
            mki__rst.append(oca__srgaq[fhz__smnu])
    return (yzs__byuz, bkk__dpz, qbrg__mgiv, ovdsv__bgnk, partition_names,
        ffwi__pgo, mki__rst, pa_schema)


def _get_partition_cat_dtype(dictionary):
    assert dictionary is not None
    esomn__npko = dictionary.to_pandas()
    ekamg__pqb = bodo.typeof(esomn__npko).dtype
    if isinstance(ekamg__pqb, types.Integer):
        besh__pwfyy = PDCategoricalDtype(tuple(esomn__npko), ekamg__pqb, 
            False, int_type=ekamg__pqb)
    else:
        besh__pwfyy = PDCategoricalDtype(tuple(esomn__npko), ekamg__pqb, False)
    return CategoricalArrayType(besh__pwfyy)


from llvmlite import ir as lir
from numba.core import cgutils
if bodo.utils.utils.has_pyarrow():
    from bodo.io import arrow_cpp
    ll.add_symbol('pq_write', arrow_cpp.pq_write)
    ll.add_symbol('pq_write_partitioned', arrow_cpp.pq_write_partitioned)


@intrinsic
def parquet_write_table_cpp(typingctx, filename_t, table_t, col_names_t,
    index_t, write_index, metadata_t, compression_t, is_parallel_t,
    write_range_index, start, stop, step, name, bucket_region,
    row_group_size, file_prefix, convert_timedelta_to_int64, timestamp_tz,
    downcast_time_ns_to_us):

    def codegen(context, builder, sig, args):
        bmfwq__zbzjw = lir.FunctionType(lir.IntType(64), [lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(1), lir.
            IntType(8).as_pointer(), lir.IntType(8).as_pointer(), lir.
            IntType(1), lir.IntType(1), lir.IntType(32), lir.IntType(32),
            lir.IntType(32), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(64), lir.IntType(8).as_pointer(), lir
            .IntType(1), lir.IntType(8).as_pointer(), lir.IntType(1)])
        bsd__nbv = cgutils.get_or_insert_function(builder.module,
            bmfwq__zbzjw, name='pq_write')
        ogjlp__zqp = builder.call(bsd__nbv, args)
        bodo.utils.utils.inlined_check_and_propagate_cpp_exception(context,
            builder)
        return ogjlp__zqp
    return types.int64(types.voidptr, table_t, col_names_t, index_t, types.
        boolean, types.voidptr, types.voidptr, types.boolean, types.boolean,
        types.int32, types.int32, types.int32, types.voidptr, types.voidptr,
        types.int64, types.voidptr, types.boolean, types.voidptr, types.boolean
        ), codegen


@intrinsic
def parquet_write_table_partitioned_cpp(typingctx, filename_t, data_table_t,
    col_names_t, col_names_no_partitions_t, cat_table_t, part_col_idxs_t,
    num_part_col_t, compression_t, is_parallel_t, bucket_region,
    row_group_size, file_prefix, timestamp_tz):

    def codegen(context, builder, sig, args):
        bmfwq__zbzjw = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(32), lir
            .IntType(8).as_pointer(), lir.IntType(1), lir.IntType(8).
            as_pointer(), lir.IntType(64), lir.IntType(8).as_pointer(), lir
            .IntType(8).as_pointer()])
        bsd__nbv = cgutils.get_or_insert_function(builder.module,
            bmfwq__zbzjw, name='pq_write_partitioned')
        builder.call(bsd__nbv, args)
        bodo.utils.utils.inlined_check_and_propagate_cpp_exception(context,
            builder)
    return types.void(types.voidptr, data_table_t, col_names_t,
        col_names_no_partitions_t, cat_table_t, types.voidptr, types.int32,
        types.voidptr, types.boolean, types.voidptr, types.int64, types.
        voidptr, types.voidptr), codegen
