import gc
import inspect
import sys
import types as pytypes
import bodo
master_mode_on = False
MASTER_RANK = 0


class MasterModeDispatcher(object):

    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    def __call__(self, *args, **kwargs):
        assert bodo.get_rank() == MASTER_RANK
        return master_wrapper(self.dispatcher, *args, **kwargs)

    def __getstate__(self):
        assert bodo.get_rank() == MASTER_RANK
        return self.dispatcher.py_func

    def __setstate__(self, state):
        assert bodo.get_rank() != MASTER_RANK
        rsiid__mgs = state
        qdjth__pfx = inspect.getsourcelines(rsiid__mgs)[0][0]
        assert qdjth__pfx.startswith('@bodo.jit') or qdjth__pfx.startswith(
            '@jit')
        yzcgc__stsc = eval(qdjth__pfx[1:])
        self.dispatcher = yzcgc__stsc(rsiid__mgs)


def worker_loop():
    assert bodo.get_rank() != MASTER_RANK
    pjk__asud = MPI.COMM_WORLD
    while True:
        mbc__nkocs = pjk__asud.bcast(None, root=MASTER_RANK)
        if mbc__nkocs[0] == 'exec':
            rsiid__mgs = pickle.loads(mbc__nkocs[1])
            for jgdow__nrfb, zsm__gqxxa in list(rsiid__mgs.__globals__.items()
                ):
                if isinstance(zsm__gqxxa, MasterModeDispatcher):
                    rsiid__mgs.__globals__[jgdow__nrfb] = zsm__gqxxa.dispatcher
            if rsiid__mgs.__module__ not in sys.modules:
                sys.modules[rsiid__mgs.__module__] = pytypes.ModuleType(
                    rsiid__mgs.__module__)
            qdjth__pfx = inspect.getsourcelines(rsiid__mgs)[0][0]
            assert qdjth__pfx.startswith('@bodo.jit') or qdjth__pfx.startswith(
                '@jit')
            yzcgc__stsc = eval(qdjth__pfx[1:])
            func = yzcgc__stsc(rsiid__mgs)
            xfia__kldar = mbc__nkocs[2]
            gqncc__lvf = mbc__nkocs[3]
            lvo__okat = []
            for tipv__zay in xfia__kldar:
                if tipv__zay == 'scatter':
                    lvo__okat.append(bodo.scatterv(None))
                elif tipv__zay == 'bcast':
                    lvo__okat.append(pjk__asud.bcast(None, root=MASTER_RANK))
            yxvg__gwxm = {}
            for argname, tipv__zay in gqncc__lvf.items():
                if tipv__zay == 'scatter':
                    yxvg__gwxm[argname] = bodo.scatterv(None)
                elif tipv__zay == 'bcast':
                    yxvg__gwxm[argname] = pjk__asud.bcast(None, root=
                        MASTER_RANK)
            lkbds__rpxnn = func(*lvo__okat, **yxvg__gwxm)
            if lkbds__rpxnn is not None and func.overloads[func.signatures[0]
                ].metadata['is_return_distributed']:
                bodo.gatherv(lkbds__rpxnn)
            del (mbc__nkocs, rsiid__mgs, func, yzcgc__stsc, xfia__kldar,
                gqncc__lvf, lvo__okat, yxvg__gwxm, lkbds__rpxnn)
            gc.collect()
        elif mbc__nkocs[0] == 'exit':
            exit()
    assert False


def master_wrapper(func, *args, **kwargs):
    pjk__asud = MPI.COMM_WORLD
    if {'all_args_distributed', 'all_args_distributed_block',
        'all_args_distributed_varlength'} & set(func.targetoptions.keys()):
        xfia__kldar = ['scatter' for ppu__eyvcd in range(len(args))]
        gqncc__lvf = {argname: 'scatter' for argname in kwargs.keys()}
    else:
        aegit__jqn = func.py_func.__code__.co_varnames
        mlva__xvhds = func.targetoptions

        def get_distribution(argname):
            if argname in mlva__xvhds.get('distributed', []
                ) or argname in mlva__xvhds.get('distributed_block', []):
                return 'scatter'
            else:
                return 'bcast'
        xfia__kldar = [get_distribution(argname) for argname in aegit__jqn[
            :len(args)]]
        gqncc__lvf = {argname: get_distribution(argname) for argname in
            kwargs.keys()}
    qgruv__uhgnr = pickle.dumps(func.py_func)
    pjk__asud.bcast(['exec', qgruv__uhgnr, xfia__kldar, gqncc__lvf])
    lvo__okat = []
    for yfzd__dsi, tipv__zay in zip(args, xfia__kldar):
        if tipv__zay == 'scatter':
            lvo__okat.append(bodo.scatterv(yfzd__dsi))
        elif tipv__zay == 'bcast':
            pjk__asud.bcast(yfzd__dsi)
            lvo__okat.append(yfzd__dsi)
    yxvg__gwxm = {}
    for argname, yfzd__dsi in kwargs.items():
        tipv__zay = gqncc__lvf[argname]
        if tipv__zay == 'scatter':
            yxvg__gwxm[argname] = bodo.scatterv(yfzd__dsi)
        elif tipv__zay == 'bcast':
            pjk__asud.bcast(yfzd__dsi)
            yxvg__gwxm[argname] = yfzd__dsi
    guu__ism = []
    for jgdow__nrfb, zsm__gqxxa in list(func.py_func.__globals__.items()):
        if isinstance(zsm__gqxxa, MasterModeDispatcher):
            guu__ism.append((func.py_func.__globals__, jgdow__nrfb, func.
                py_func.__globals__[jgdow__nrfb]))
            func.py_func.__globals__[jgdow__nrfb] = zsm__gqxxa.dispatcher
    lkbds__rpxnn = func(*lvo__okat, **yxvg__gwxm)
    for wegey__nqjyo, jgdow__nrfb, zsm__gqxxa in guu__ism:
        wegey__nqjyo[jgdow__nrfb] = zsm__gqxxa
    if lkbds__rpxnn is not None and func.overloads[func.signatures[0]
        ].metadata['is_return_distributed']:
        lkbds__rpxnn = bodo.gatherv(lkbds__rpxnn)
    return lkbds__rpxnn


def init_master_mode():
    if bodo.get_size() == 1:
        return
    global master_mode_on
    assert master_mode_on is False, 'init_master_mode can only be called once on each process'
    master_mode_on = True
    assert sys.version_info[:2] >= (3, 8
        ), 'Python 3.8+ required for master mode'
    from bodo import jit
    globals()['jit'] = jit
    import cloudpickle
    from mpi4py import MPI
    globals()['pickle'] = cloudpickle
    globals()['MPI'] = MPI

    def master_exit():
        MPI.COMM_WORLD.bcast(['exit'])
    if bodo.get_rank() == MASTER_RANK:
        import atexit
        atexit.register(master_exit)
    else:
        worker_loop()
