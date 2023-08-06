"""
S3 & Hadoop file system supports, and file system dependent calls
"""
import glob
import os
import warnings
from urllib.parse import urlparse
import llvmlite.binding as ll
import numba
import numpy as np
from fsspec.implementations.arrow import ArrowFile, ArrowFSWrapper, wrap_exceptions
from numba.core import types
from numba.extending import NativeValue, models, overload, register_model, unbox
import bodo
from bodo.io import csv_cpp
from bodo.libs.distributed_api import Reduce_Type
from bodo.libs.str_ext import unicode_to_utf8, unicode_to_utf8_and_len
from bodo.utils.typing import BodoError, BodoWarning, get_overload_constant_dict
from bodo.utils.utils import check_java_installation


def fsspec_arrowfswrapper__open(self, path, mode='rb', block_size=None, **
    kwargs):
    if mode == 'rb':
        try:
            keyck__wlh = self.fs.open_input_file(path)
        except:
            keyck__wlh = self.fs.open_input_stream(path)
    elif mode == 'wb':
        keyck__wlh = self.fs.open_output_stream(path)
    else:
        raise ValueError(f'unsupported mode for Arrow filesystem: {mode!r}')
    return ArrowFile(self, keyck__wlh, path, mode, block_size, **kwargs)


ArrowFSWrapper._open = wrap_exceptions(fsspec_arrowfswrapper__open)
_csv_write = types.ExternalFunction('csv_write', types.void(types.voidptr,
    types.voidptr, types.int64, types.int64, types.bool_, types.voidptr,
    types.voidptr))
ll.add_symbol('csv_write', csv_cpp.csv_write)
bodo_error_msg = """
    Some possible causes:
        (1) Incorrect path: Specified file/directory doesn't exist or is unreachable.
        (2) Missing credentials: You haven't provided S3 credentials, neither through 
            environment variables, nor through a local AWS setup 
            that makes the credentials available at ~/.aws/credentials.
        (3) Incorrect credentials: Your S3 credentials are incorrect or do not have
            the correct permissions.
        (4) Wrong bucket region is used. Set AWS_DEFAULT_REGION variable with correct bucket region.
    """


def get_proxy_uri_from_env_vars():
    return os.environ.get('http_proxy', None) or os.environ.get('https_proxy',
        None) or os.environ.get('HTTP_PROXY', None) or os.environ.get(
        'HTTPS_PROXY', None)


def get_s3_fs(region=None, storage_options=None):
    from pyarrow.fs import S3FileSystem
    xwgwi__fooa = os.environ.get('AWS_S3_ENDPOINT', None)
    if not region:
        region = os.environ.get('AWS_DEFAULT_REGION', None)
    yvqui__paif = False
    iacnt__scrdz = get_proxy_uri_from_env_vars()
    if storage_options:
        yvqui__paif = storage_options.get('anon', False)
    return S3FileSystem(anonymous=yvqui__paif, region=region,
        endpoint_override=xwgwi__fooa, proxy_options=iacnt__scrdz)


def get_s3_subtree_fs(bucket_name, region=None, storage_options=None):
    from pyarrow._fs import SubTreeFileSystem
    from pyarrow._s3fs import S3FileSystem
    xwgwi__fooa = os.environ.get('AWS_S3_ENDPOINT', None)
    if not region:
        region = os.environ.get('AWS_DEFAULT_REGION', None)
    yvqui__paif = False
    iacnt__scrdz = get_proxy_uri_from_env_vars()
    if storage_options:
        yvqui__paif = storage_options.get('anon', False)
    fs = S3FileSystem(region=region, endpoint_override=xwgwi__fooa,
        anonymous=yvqui__paif, proxy_options=iacnt__scrdz)
    return SubTreeFileSystem(bucket_name, fs)


def get_s3_fs_from_path(path, parallel=False, storage_options=None):
    region = get_s3_bucket_region_njit(path, parallel=parallel)
    if region == '':
        region = None
    return get_s3_fs(region, storage_options)


def get_hdfs_fs(path):
    from pyarrow.fs import HadoopFileSystem as HdFS
    zvn__uklat = urlparse(path)
    if zvn__uklat.scheme in ('abfs', 'abfss'):
        ummoi__mdc = path
        if zvn__uklat.port is None:
            ges__oko = 0
        else:
            ges__oko = zvn__uklat.port
        rbrg__gyasi = None
    else:
        ummoi__mdc = zvn__uklat.hostname
        ges__oko = zvn__uklat.port
        rbrg__gyasi = zvn__uklat.username
    try:
        fs = HdFS(host=ummoi__mdc, port=ges__oko, user=rbrg__gyasi)
    except Exception as tnv__sayv:
        raise BodoError('Hadoop file system cannot be created: {}'.format(
            tnv__sayv))
    return fs


def gcs_is_directory(path):
    import gcsfs
    fs = gcsfs.GCSFileSystem(token=None)
    try:
        dha__rqsgc = fs.isdir(path)
    except gcsfs.utils.HttpError as tnv__sayv:
        raise BodoError(
            f'{tnv__sayv}. Make sure your google cloud credentials are set!')
    return dha__rqsgc


def gcs_list_dir_fnames(path):
    import gcsfs
    fs = gcsfs.GCSFileSystem(token=None)
    return [gnj__bbhpj.split('/')[-1] for gnj__bbhpj in fs.ls(path)]


def s3_is_directory(fs, path):
    from pyarrow import fs as pa_fs
    try:
        zvn__uklat = urlparse(path)
        lklqn__fgyqe = (zvn__uklat.netloc + zvn__uklat.path).rstrip('/')
        rmsd__cok = fs.get_file_info(lklqn__fgyqe)
        if rmsd__cok.type in (pa_fs.FileType.NotFound, pa_fs.FileType.Unknown):
            raise FileNotFoundError('{} is a non-existing or unreachable file'
                .format(path))
        if not rmsd__cok.size and rmsd__cok.type == pa_fs.FileType.Directory:
            return True
        return False
    except (FileNotFoundError, OSError) as tnv__sayv:
        raise
    except BodoError as pzip__kjomh:
        raise
    except Exception as tnv__sayv:
        raise BodoError(
            f"""error from pyarrow S3FileSystem: {type(tnv__sayv).__name__}: {str(tnv__sayv)}
{bodo_error_msg}"""
            )


def s3_list_dir_fnames(fs, path):
    from pyarrow import fs as pa_fs
    sfc__nfkr = None
    try:
        if s3_is_directory(fs, path):
            zvn__uklat = urlparse(path)
            lklqn__fgyqe = (zvn__uklat.netloc + zvn__uklat.path).rstrip('/')
            voh__xxxas = pa_fs.FileSelector(lklqn__fgyqe, recursive=False)
            cjgbx__jxhg = fs.get_file_info(voh__xxxas)
            if cjgbx__jxhg and cjgbx__jxhg[0].path in [lklqn__fgyqe,
                f'{lklqn__fgyqe}/'] and int(cjgbx__jxhg[0].size or 0) == 0:
                cjgbx__jxhg = cjgbx__jxhg[1:]
            sfc__nfkr = [ekkk__zijhk.base_name for ekkk__zijhk in cjgbx__jxhg]
    except BodoError as pzip__kjomh:
        raise
    except Exception as tnv__sayv:
        raise BodoError(
            f"""error from pyarrow S3FileSystem: {type(tnv__sayv).__name__}: {str(tnv__sayv)}
{bodo_error_msg}"""
            )
    return sfc__nfkr


def hdfs_is_directory(path):
    from pyarrow.fs import FileType, HadoopFileSystem
    check_java_installation(path)
    zvn__uklat = urlparse(path)
    xfly__meql = zvn__uklat.path
    try:
        jmh__sru = HadoopFileSystem.from_uri(path)
    except Exception as tnv__sayv:
        raise BodoError(' Hadoop file system cannot be created: {}'.format(
            tnv__sayv))
    clq__flzjg = jmh__sru.get_file_info([xfly__meql])
    if clq__flzjg[0].type in (FileType.NotFound, FileType.Unknown):
        raise BodoError('{} is a non-existing or unreachable file'.format(path)
            )
    if not clq__flzjg[0].size and clq__flzjg[0].type == FileType.Directory:
        return jmh__sru, True
    return jmh__sru, False


def hdfs_list_dir_fnames(path):
    from pyarrow.fs import FileSelector
    sfc__nfkr = None
    jmh__sru, dha__rqsgc = hdfs_is_directory(path)
    if dha__rqsgc:
        zvn__uklat = urlparse(path)
        xfly__meql = zvn__uklat.path
        voh__xxxas = FileSelector(xfly__meql, recursive=True)
        try:
            cjgbx__jxhg = jmh__sru.get_file_info(voh__xxxas)
        except Exception as tnv__sayv:
            raise BodoError('Exception on getting directory info of {}: {}'
                .format(xfly__meql, tnv__sayv))
        sfc__nfkr = [ekkk__zijhk.base_name for ekkk__zijhk in cjgbx__jxhg]
    return jmh__sru, sfc__nfkr


def abfs_is_directory(path):
    jmh__sru = get_hdfs_fs(path)
    try:
        clq__flzjg = jmh__sru.info(path)
    except OSError as pzip__kjomh:
        raise BodoError('{} is a non-existing or unreachable file'.format(path)
            )
    if clq__flzjg['size'] == 0 and clq__flzjg['kind'].lower() == 'directory':
        return jmh__sru, True
    return jmh__sru, False


def abfs_list_dir_fnames(path):
    sfc__nfkr = None
    jmh__sru, dha__rqsgc = abfs_is_directory(path)
    if dha__rqsgc:
        zvn__uklat = urlparse(path)
        xfly__meql = zvn__uklat.path
        try:
            xqosr__qppgx = jmh__sru.ls(xfly__meql)
        except Exception as tnv__sayv:
            raise BodoError('Exception on getting directory info of {}: {}'
                .format(xfly__meql, tnv__sayv))
        sfc__nfkr = [fname[fname.rindex('/') + 1:] for fname in xqosr__qppgx]
    return jmh__sru, sfc__nfkr


def directory_of_files_common_filter(fname):
    return not (fname.endswith('.crc') or fname.endswith('_$folder$') or
        fname.startswith('.') or fname.startswith('_') and fname !=
        '_delta_log')


def find_file_name_or_handler(path, ftype, storage_options=None):
    from urllib.parse import urlparse
    vptej__bzn = urlparse(path)
    fname = path
    fs = None
    sqx__nubqj = 'read_json' if ftype == 'json' else 'read_csv'
    itbi__duumb = (
        f'pd.{sqx__nubqj}(): there is no {ftype} file in directory: {fname}')
    ktcb__jij = directory_of_files_common_filter
    if vptej__bzn.scheme == 's3':
        ckxd__fytt = True
        fs = get_s3_fs_from_path(path, storage_options=storage_options)
        eyxi__tlxnm = s3_list_dir_fnames(fs, path)
        lklqn__fgyqe = (vptej__bzn.netloc + vptej__bzn.path).rstrip('/')
        fname = lklqn__fgyqe
        if eyxi__tlxnm:
            eyxi__tlxnm = [(lklqn__fgyqe + '/' + gnj__bbhpj) for gnj__bbhpj in
                sorted(filter(ktcb__jij, eyxi__tlxnm))]
            foai__cvqp = [gnj__bbhpj for gnj__bbhpj in eyxi__tlxnm if int(
                fs.get_file_info(gnj__bbhpj).size or 0) > 0]
            if len(foai__cvqp) == 0:
                raise BodoError(itbi__duumb)
            fname = foai__cvqp[0]
        jhim__hhz = int(fs.get_file_info(fname).size or 0)
        fs = ArrowFSWrapper(fs)
        qxd__plt = fs._open(fname)
    elif vptej__bzn.scheme == 'hdfs':
        ckxd__fytt = True
        fs, eyxi__tlxnm = hdfs_list_dir_fnames(path)
        jhim__hhz = fs.get_file_info([vptej__bzn.path])[0].size
        if eyxi__tlxnm:
            path = path.rstrip('/')
            eyxi__tlxnm = [(path + '/' + gnj__bbhpj) for gnj__bbhpj in
                sorted(filter(ktcb__jij, eyxi__tlxnm))]
            foai__cvqp = [gnj__bbhpj for gnj__bbhpj in eyxi__tlxnm if fs.
                get_file_info([urlparse(gnj__bbhpj).path])[0].size > 0]
            if len(foai__cvqp) == 0:
                raise BodoError(itbi__duumb)
            fname = foai__cvqp[0]
            fname = urlparse(fname).path
            jhim__hhz = fs.get_file_info([fname])[0].size
        qxd__plt = fs.open_input_file(fname)
    elif vptej__bzn.scheme in ('abfs', 'abfss'):
        ckxd__fytt = True
        fs, eyxi__tlxnm = abfs_list_dir_fnames(path)
        jhim__hhz = fs.info(fname)['size']
        if eyxi__tlxnm:
            path = path.rstrip('/')
            eyxi__tlxnm = [(path + '/' + gnj__bbhpj) for gnj__bbhpj in
                sorted(filter(ktcb__jij, eyxi__tlxnm))]
            foai__cvqp = [gnj__bbhpj for gnj__bbhpj in eyxi__tlxnm if fs.
                info(gnj__bbhpj)['size'] > 0]
            if len(foai__cvqp) == 0:
                raise BodoError(itbi__duumb)
            fname = foai__cvqp[0]
            jhim__hhz = fs.info(fname)['size']
            fname = urlparse(fname).path
        qxd__plt = fs.open(fname, 'rb')
    else:
        if vptej__bzn.scheme != '':
            raise BodoError(
                f'Unrecognized scheme {vptej__bzn.scheme}. Please refer to https://docs.bodo.ai/latest/file_io/.'
                )
        ckxd__fytt = False
        if os.path.isdir(path):
            xqosr__qppgx = filter(ktcb__jij, glob.glob(os.path.join(os.path
                .abspath(path), '*')))
            foai__cvqp = [gnj__bbhpj for gnj__bbhpj in sorted(xqosr__qppgx) if
                os.path.getsize(gnj__bbhpj) > 0]
            if len(foai__cvqp) == 0:
                raise BodoError(itbi__duumb)
            fname = foai__cvqp[0]
        jhim__hhz = os.path.getsize(fname)
        qxd__plt = fname
    return ckxd__fytt, qxd__plt, jhim__hhz, fs


def get_s3_bucket_region(s3_filepath, parallel):
    try:
        from pyarrow import fs as pa_fs
    except:
        raise BodoError('Reading from s3 requires pyarrow currently.')
    from mpi4py import MPI
    puwyh__snimk = MPI.COMM_WORLD
    bucket_loc = None
    if parallel and bodo.get_rank() == 0 or not parallel:
        try:
            xwjmu__tfnml, emuj__oim = pa_fs.S3FileSystem.from_uri(s3_filepath)
            bucket_loc = xwjmu__tfnml.region
        except Exception as tnv__sayv:
            if os.environ.get('AWS_DEFAULT_REGION', '') == '':
                warnings.warn(BodoWarning(
                    f"""Unable to get S3 Bucket Region.
{tnv__sayv}.
Value not defined in the AWS_DEFAULT_REGION environment variable either. Region defaults to us-east-1 currently."""
                    ))
            bucket_loc = ''
    if parallel:
        bucket_loc = puwyh__snimk.bcast(bucket_loc)
    return bucket_loc


@numba.njit()
def get_s3_bucket_region_njit(s3_filepath, parallel):
    with numba.objmode(bucket_loc='unicode_type'):
        bucket_loc = ''
        if isinstance(s3_filepath, list):
            s3_filepath = s3_filepath[0]
        if s3_filepath.startswith('s3://'):
            bucket_loc = get_s3_bucket_region(s3_filepath, parallel)
    return bucket_loc


def csv_write(path_or_buf, D, filename_prefix, is_parallel=False):
    return None


@overload(csv_write, no_unliteral=True)
def csv_write_overload(path_or_buf, D, filename_prefix, is_parallel=False):

    def impl(path_or_buf, D, filename_prefix, is_parallel=False):
        dlmrm__lxb = get_s3_bucket_region_njit(path_or_buf, parallel=
            is_parallel)
        xzmw__tnof, ardt__bwpw = unicode_to_utf8_and_len(D)
        dhng__qmitj = 0
        if is_parallel:
            dhng__qmitj = bodo.libs.distributed_api.dist_exscan(ardt__bwpw,
                np.int32(Reduce_Type.Sum.value))
        _csv_write(unicode_to_utf8(path_or_buf), xzmw__tnof, dhng__qmitj,
            ardt__bwpw, is_parallel, unicode_to_utf8(dlmrm__lxb),
            unicode_to_utf8(filename_prefix))
        bodo.utils.utils.check_and_propagate_cpp_exception()
    return impl


class StorageOptionsDictType(types.Opaque):

    def __init__(self):
        super(StorageOptionsDictType, self).__init__(name=
            'StorageOptionsDictType')


storage_options_dict_type = StorageOptionsDictType()
types.storage_options_dict_type = storage_options_dict_type
register_model(StorageOptionsDictType)(models.OpaqueModel)


@unbox(StorageOptionsDictType)
def unbox_storage_options_dict_type(typ, val, c):
    c.pyapi.incref(val)
    return NativeValue(val)


def get_storage_options_pyobject(storage_options):
    pass


@overload(get_storage_options_pyobject, no_unliteral=True)
def overload_get_storage_options_pyobject(storage_options):
    ilrei__qhk = get_overload_constant_dict(storage_options)
    xze__xoynj = 'def impl(storage_options):\n'
    xze__xoynj += (
        "  with numba.objmode(storage_options_py='storage_options_dict_type'):\n"
        )
    xze__xoynj += f'    storage_options_py = {str(ilrei__qhk)}\n'
    xze__xoynj += '  return storage_options_py\n'
    kqv__cdoan = {}
    exec(xze__xoynj, globals(), kqv__cdoan)
    return kqv__cdoan['impl']
