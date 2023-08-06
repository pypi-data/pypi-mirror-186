"""Support distributed deep learning with Horovod
"""
import time
import numba
import numpy as np
from mpi4py import MPI
import bodo
from bodo.libs.distributed_api import create_subcomm_mpi4py, get_host_ranks, get_nodes_first_ranks
dl_status = None


def assert_dl_initialized():
    assert dl_status is not None, 'Horovod has not been initialized. Call bodo.dl.start() first'


class DLStatus(object):

    def __init__(self, framework, gpu_ranks):
        self.framework = framework
        self.gpu_ranks = gpu_ranks


def get_num_gpus(framework):
    if framework == 'torch':
        import torch
        return torch.cuda.device_count()
    elif framework == 'tensorflow':
        import tensorflow as tf
        return len(tf.config.experimental.list_physical_devices('GPU'))
    else:
        raise RuntimeError('Framework {} not recognized'.format(framework))


def get_gpu_ranks(framework):
    mtw__msesx = MPI.COMM_WORLD
    curn__mrt = mtw__msesx.Get_rank()
    nppa__twqfq = get_host_ranks()
    ccvnx__trceq = get_nodes_first_ranks()
    if curn__mrt in ccvnx__trceq:
        try:
            udbjb__ulglu = get_num_gpus(framework)
        except Exception as uny__xlkxj:
            udbjb__ulglu = uny__xlkxj
        ofbv__vkh = create_subcomm_mpi4py(ccvnx__trceq)
        qcrcv__eaeu = ofbv__vkh.gather(udbjb__ulglu)
        if curn__mrt == 0:
            gpu_ranks = []
            syw__cwp = None
            for ttv__jzra, cvc__mfzs in enumerate(nppa__twqfq.values()):
                djrxg__qbp = qcrcv__eaeu[ttv__jzra]
                if isinstance(djrxg__qbp, Exception):
                    syw__cwp = djrxg__qbp
                    break
                if djrxg__qbp == 0:
                    continue
                vqkf__ljwd = len(cvc__mfzs) // djrxg__qbp
                for wcsrb__nbztp, ihswz__bphd in enumerate(cvc__mfzs):
                    if wcsrb__nbztp % vqkf__ljwd == 0:
                        oaohm__ltd = wcsrb__nbztp / vqkf__ljwd
                        if oaohm__ltd < djrxg__qbp:
                            gpu_ranks.append(ihswz__bphd)
            if syw__cwp:
                mtw__msesx.bcast(syw__cwp)
                raise syw__cwp
            else:
                mtw__msesx.bcast(gpu_ranks)
    if curn__mrt != 0:
        gpu_ranks = mtw__msesx.bcast(None)
        if isinstance(gpu_ranks, Exception):
            uny__xlkxj = gpu_ranks
            raise uny__xlkxj
    return gpu_ranks


def is_cuda_available():
    assert_dl_initialized()
    return len(dl_status.gpu_ranks) > 0


def initialize_horovod(framework):
    global dl_status
    if dl_status is not None:
        assert dl_status.framework == framework, 'Attempted to initialize Horovod with different DL frameworks'
        return np.array(dl_status.gpu_ranks, dtype=np.int32)
    gpu_ranks = get_gpu_ranks(framework)
    if framework == 'torch':
        import horovod.torch as hvd
        import torch
        torch.set_num_threads(1)
    elif framework == 'tensorflow':
        import horovod.tensorflow as hvd
        import tensorflow as tf
    else:
        raise RuntimeError('Framework {} not recognized'.format(framework))
    xlfi__imsb = MPI.COMM_WORLD.rank
    if len(gpu_ranks) > 0:
        ofbv__vkh = MPI.COMM_WORLD.Split(color=0 if xlfi__imsb in gpu_ranks
             else MPI.UNDEFINED, key=xlfi__imsb)
        if ofbv__vkh != MPI.COMM_NULL:
            hvd.init(comm=ofbv__vkh)
            if framework == 'torch':
                torch.cuda.set_device(hvd.local_rank())
            elif framework == 'tensorflow':
                qia__mklxk = tf.config.experimental.list_physical_devices('GPU'
                    )
                for mdgns__mzgso in qia__mklxk:
                    tf.config.experimental.set_memory_growth(mdgns__mzgso, True
                        )
                tf.config.experimental.set_visible_devices(qia__mklxk[hvd.
                    local_rank()], 'GPU')
    else:
        if xlfi__imsb == 0:
            print('[BODO-DL]: No GPUs found in cluster. Using CPUs')
        hvd.init()
    dl_status = DLStatus(framework, np.array(gpu_ranks, dtype=np.int32))


@numba.njit
def start(framework):
    with numba.objmode:
        initialize_horovod(framework)


@numba.njit
def end():
    with numba.objmode:
        end_py()


def end_py():
    if is_cuda_available():
        lcr__zaxx = 17
        mtw__msesx = MPI.COMM_WORLD
        znz__kvnx = MPI.Get_processor_name()
        urscq__hsymm = get_host_ranks()[znz__kvnx]
        assert_dl_initialized()
        if bodo.get_rank() == urscq__hsymm[0]:
            assert bodo.get_rank() in dl_status.gpu_ranks
            for curn__mrt in urscq__hsymm[1:]:
                mtw__msesx.isend(1, dest=curn__mrt, tag=lcr__zaxx)
        else:
            while True:
                chzda__yhvgs = MPI.Status()
                tap__qxlu = mtw__msesx.Iprobe(MPI.ANY_SOURCE, MPI.ANY_TAG,
                    chzda__yhvgs)
                if tap__qxlu:
                    assert chzda__yhvgs.source == urscq__hsymm[0]
                    assert chzda__yhvgs.tag == lcr__zaxx
                    mtw__msesx.recv(source=0, tag=lcr__zaxx)
                    break
                time.sleep(1.0)
    else:
        bodo.barrier()


def _prepare_data_get_gpu_ranks():
    assert_dl_initialized()
    return dl_status.gpu_ranks


@numba.njit
def prepare_data(data):
    with numba.objmode(gpu_ranks='int32[:]'):
        gpu_ranks = _prepare_data_get_gpu_ranks()
    if len(gpu_ranks) > 0:
        data = bodo.rebalance(data, dests=list(gpu_ranks), parallel=True)
    else:
        data = bodo.rebalance(data, parallel=True)
    return data
