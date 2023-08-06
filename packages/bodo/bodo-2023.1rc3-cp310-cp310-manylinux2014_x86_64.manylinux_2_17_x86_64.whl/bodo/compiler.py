"""
Defines Bodo's compiler pipeline.
"""
import os
import warnings
from collections import namedtuple
import numba
from numba.core import ir, ir_utils, types
from numba.core.compiler import DefaultPassBuilder
from numba.core.compiler_machinery import AnalysisPass, FunctionPass, register_pass
from numba.core.errors import NumbaExperimentalFeatureWarning, NumbaPendingDeprecationWarning
from numba.core.inline_closurecall import inline_closure_call
from numba.core.ir_utils import build_definitions, find_callname, get_definition, guard
from numba.core.registry import CPUDispatcher
from numba.core.typed_passes import DumpParforDiagnostics, InlineOverloads, IRLegalization, NopythonTypeInference, ParforPass, PreParforPass
from numba.core.untyped_passes import MakeFunctionToJitFunction, ReconstructSSA, WithLifting
import bodo
import bodo.hiframes.dataframe_indexing
import bodo.hiframes.datetime_datetime_ext
import bodo.hiframes.datetime_timedelta_ext
import bodo.io
import bodo.libs
import bodo.libs.array_kernels
import bodo.libs.int_arr_ext
import bodo.libs.re_ext
import bodo.libs.spark_extra
import bodo.transforms
import bodo.transforms.series_pass
import bodo.transforms.untyped_pass
import bodo.utils
import bodo.utils.table_utils
import bodo.utils.typing
from bodo.transforms.series_pass import SeriesPass
from bodo.transforms.table_column_del_pass import TableColumnDelPass
from bodo.transforms.typing_pass import BodoTypeInference
from bodo.transforms.untyped_pass import UntypedPass
from bodo.utils.utils import is_assign, is_call_assign, is_expr
warnings.simplefilter('ignore', category=NumbaExperimentalFeatureWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)
inline_all_calls = False


class BodoCompiler(numba.core.compiler.CompilerBase):

    def define_pipelines(self):
        return self._create_bodo_pipeline(distributed=True,
            inline_calls_pass=inline_all_calls)

    def _create_bodo_pipeline(self, distributed=True, inline_calls_pass=
        False, udf_pipeline=False):
        rmwez__kfc = 'bodo' if distributed else 'bodo_seq'
        rmwez__kfc = (rmwez__kfc + '_inline' if inline_calls_pass else
            rmwez__kfc)
        pm = DefaultPassBuilder.define_nopython_pipeline(self.state, rmwez__kfc
            )
        if inline_calls_pass:
            pm.add_pass_after(InlinePass, WithLifting)
        if udf_pipeline:
            pm.add_pass_after(ConvertCallsUDFPass, WithLifting)
        add_pass_before(pm, BodoUntypedPass, ReconstructSSA)
        replace_pass(pm, BodoTypeInference, NopythonTypeInference)
        remove_pass(pm, MakeFunctionToJitFunction)
        add_pass_before(pm, BodoSeriesPass, PreParforPass)
        if distributed:
            pm.add_pass_after(BodoDistributedPass, ParforPass)
        else:
            pm.add_pass_after(LowerParforSeq, ParforPass)
            pm.add_pass_after(LowerBodoIRExtSeq, LowerParforSeq)
        add_pass_before(pm, BodoTableColumnDelPass, IRLegalization)
        pm.add_pass_after(BodoDumpDistDiagnosticsPass, DumpParforDiagnostics)
        pm.finalize()
        return [pm]


def add_pass_before(pm, pass_cls, location):
    assert pm.passes
    pm._validate_pass(pass_cls)
    pm._validate_pass(location)
    for mnaso__puqgi, (plfbj__vgex, oux__bilgt) in enumerate(pm.passes):
        if plfbj__vgex == location:
            break
    else:
        raise bodo.utils.typing.BodoError('Could not find pass %s' % location)
    pm.passes.insert(mnaso__puqgi, (pass_cls, str(pass_cls)))
    pm._finalized = False


def replace_pass(pm, pass_cls, location):
    assert pm.passes
    pm._validate_pass(pass_cls)
    pm._validate_pass(location)
    for mnaso__puqgi, (plfbj__vgex, oux__bilgt) in enumerate(pm.passes):
        if plfbj__vgex == location:
            break
    else:
        raise bodo.utils.typing.BodoError('Could not find pass %s' % location)
    pm.passes[mnaso__puqgi] = pass_cls, str(pass_cls)
    pm._finalized = False


def remove_pass(pm, location):
    assert pm.passes
    pm._validate_pass(location)
    for mnaso__puqgi, (plfbj__vgex, oux__bilgt) in enumerate(pm.passes):
        if plfbj__vgex == location:
            break
    else:
        raise bodo.utils.typing.BodoError('Could not find pass %s' % location)
    pm.passes.pop(mnaso__puqgi)
    pm._finalized = False


@register_pass(mutates_CFG=True, analysis_only=False)
class InlinePass(FunctionPass):
    _name = 'inline_pass'

    def __init__(self):
        FunctionPass.__init__(self)

    def run_pass(self, state):
        assert state.func_ir
        inline_calls(state.func_ir, state.locals)
        state.func_ir.blocks = ir_utils.simplify_CFG(state.func_ir.blocks)
        return True


def _convert_bodo_dispatcher_to_udf(rhs, func_ir):
    lldpb__wqt = guard(get_definition, func_ir, rhs.func)
    if isinstance(lldpb__wqt, (ir.Global, ir.FreeVar, ir.Const)):
        pzi__mnpo = lldpb__wqt.value
    else:
        qvgvp__cfk = guard(find_callname, func_ir, rhs)
        if not (qvgvp__cfk and isinstance(qvgvp__cfk[0], str) and
            isinstance(qvgvp__cfk[1], str)):
            return
        func_name, func_mod = qvgvp__cfk
        try:
            import importlib
            lqp__qwpsg = importlib.import_module(func_mod)
            pzi__mnpo = getattr(lqp__qwpsg, func_name)
        except:
            return
    if isinstance(pzi__mnpo, CPUDispatcher) and issubclass(pzi__mnpo.
        _compiler.pipeline_class, BodoCompiler
        ) and pzi__mnpo._compiler.pipeline_class != BodoCompilerUDF:
        pzi__mnpo._compiler.pipeline_class = BodoCompilerUDF
        pzi__mnpo.recompile()


@register_pass(mutates_CFG=True, analysis_only=False)
class ConvertCallsUDFPass(FunctionPass):
    _name = 'inline_pass'

    def __init__(self):
        FunctionPass.__init__(self)

    def run_pass(self, state):
        assert state.func_ir
        for block in state.func_ir.blocks.values():
            for kcmph__ojfe in block.body:
                if is_call_assign(kcmph__ojfe):
                    _convert_bodo_dispatcher_to_udf(kcmph__ojfe.value,
                        state.func_ir)
        return True


@register_pass(mutates_CFG=True, analysis_only=False)
class BodoUntypedPass(FunctionPass):
    _name = 'bodo_untyped_pass'

    def __init__(self):
        FunctionPass.__init__(self)

    def run_pass(self, state):
        assert state.func_ir
        tuxvu__tmjvr = UntypedPass(state.func_ir, state.typingctx, state.
            args, state.locals, state.metadata, state.flags, isinstance(
            state.pipeline, BodoCompilerSeq))
        tuxvu__tmjvr.run()
        return True


def _update_definitions(func_ir, node_list):
    wmgkc__umpe = ir.Loc('', 0)
    gqz__cmo = ir.Block(ir.Scope(None, wmgkc__umpe), wmgkc__umpe)
    gqz__cmo.body = node_list
    build_definitions({(0): gqz__cmo}, func_ir._definitions)


_series_inline_attrs = {'values', 'shape', 'size', 'empty', 'name', 'index',
    'dtype'}
_series_no_inline_methods = {'to_list', 'tolist', 'rolling', 'to_csv',
    'count', 'fillna', 'to_dict', 'map', 'apply', 'pipe', 'combine',
    'bfill', 'ffill', 'pad', 'backfill', 'mask', 'where'}
_series_method_alias = {'isnull': 'isna', 'product': 'prod', 'kurtosis':
    'kurt', 'is_monotonic': 'is_monotonic_increasing', 'notnull': 'notna'}
_dataframe_no_inline_methods = {'apply', 'itertuples', 'pipe', 'to_parquet',
    'to_sql', 'to_csv', 'to_json', 'assign', 'to_string', 'query',
    'rolling', 'mask', 'where'}
TypingInfo = namedtuple('TypingInfo', ['typingctx', 'targetctx', 'typemap',
    'calltypes', 'curr_loc'])


def _inline_bodo_getattr(stmt, rhs, rhs_type, new_body, func_ir, typingctx,
    targetctx, typemap, calltypes):
    from bodo.hiframes.pd_dataframe_ext import DataFrameType
    from bodo.hiframes.pd_series_ext import SeriesType
    from bodo.utils.transform import compile_func_single_block
    if isinstance(rhs_type, SeriesType) and rhs.attr in _series_inline_attrs:
        tbrry__tzqx = 'overload_series_' + rhs.attr
        axy__jzpp = getattr(bodo.hiframes.series_impl, tbrry__tzqx)
    if isinstance(rhs_type, DataFrameType) and rhs.attr in ('index', 'columns'
        ):
        tbrry__tzqx = 'overload_dataframe_' + rhs.attr
        axy__jzpp = getattr(bodo.hiframes.dataframe_impl, tbrry__tzqx)
    else:
        return False
    func_ir._definitions[stmt.target.name].remove(rhs)
    iejs__yhg = axy__jzpp(rhs_type)
    aztf__effxw = TypingInfo(typingctx, targetctx, typemap, calltypes, stmt.loc
        )
    luvg__wnc = compile_func_single_block(iejs__yhg, (rhs.value,), stmt.
        target, aztf__effxw)
    _update_definitions(func_ir, luvg__wnc)
    new_body += luvg__wnc
    return True


def _inline_bodo_call(rhs, i, func_mod, func_name, pass_info, new_body,
    block, typingctx, targetctx, calltypes, work_list):
    from bodo.hiframes.pd_dataframe_ext import DataFrameType
    from bodo.hiframes.pd_series_ext import SeriesType
    from bodo.utils.transform import replace_func, update_locs
    func_ir = pass_info.func_ir
    typemap = pass_info.typemap
    if isinstance(func_mod, ir.Var) and isinstance(typemap[func_mod.name],
        SeriesType) and func_name not in _series_no_inline_methods:
        if func_name in _series_method_alias:
            func_name = _series_method_alias[func_name]
        if (func_name in bodo.hiframes.series_impl.explicit_binop_funcs or 
            func_name.startswith('r') and func_name[1:] in bodo.hiframes.
            series_impl.explicit_binop_funcs):
            return False
        rhs.args.insert(0, func_mod)
        gjnso__nppsy = tuple(typemap[iad__fwign.name] for iad__fwign in rhs
            .args)
        lbw__fuaze = {rmwez__kfc: typemap[iad__fwign.name] for rmwez__kfc,
            iad__fwign in dict(rhs.kws).items()}
        iejs__yhg = getattr(bodo.hiframes.series_impl, 'overload_series_' +
            func_name)(*gjnso__nppsy, **lbw__fuaze)
    elif isinstance(func_mod, ir.Var) and isinstance(typemap[func_mod.name],
        DataFrameType) and func_name not in _dataframe_no_inline_methods:
        if func_name in _series_method_alias:
            func_name = _series_method_alias[func_name]
        rhs.args.insert(0, func_mod)
        gjnso__nppsy = tuple(typemap[iad__fwign.name] for iad__fwign in rhs
            .args)
        lbw__fuaze = {rmwez__kfc: typemap[iad__fwign.name] for rmwez__kfc,
            iad__fwign in dict(rhs.kws).items()}
        iejs__yhg = getattr(bodo.hiframes.dataframe_impl, 
            'overload_dataframe_' + func_name)(*gjnso__nppsy, **lbw__fuaze)
    else:
        return False
    riyz__uunk = replace_func(pass_info, iejs__yhg, rhs.args, pysig=numba.
        core.utils.pysignature(iejs__yhg), kws=dict(rhs.kws))
    block.body = new_body + block.body[i:]
    zvw__sdcgg, oux__bilgt = inline_closure_call(func_ir, riyz__uunk.glbls,
        block, len(new_body), riyz__uunk.func, typingctx=typingctx,
        targetctx=targetctx, arg_typs=riyz__uunk.arg_types, typemap=typemap,
        calltypes=calltypes, work_list=work_list)
    for eefk__giyr in zvw__sdcgg.values():
        eefk__giyr.loc = rhs.loc
        update_locs(eefk__giyr.body, rhs.loc)
    return True


def bodo_overload_inline_pass(func_ir, typingctx, targetctx, typemap, calltypes
    ):
    nwcj__gqypk = namedtuple('PassInfo', ['func_ir', 'typemap'])
    pass_info = nwcj__gqypk(func_ir, typemap)
    dnog__sjm = func_ir.blocks
    work_list = list((tahe__paaxm, dnog__sjm[tahe__paaxm]) for tahe__paaxm in
        reversed(dnog__sjm.keys()))
    while work_list:
        hsrj__hveg, block = work_list.pop()
        new_body = []
        eijtn__exfk = False
        for i, stmt in enumerate(block.body):
            if is_assign(stmt) and is_expr(stmt.value, 'getattr'):
                rhs = stmt.value
                rhs_type = typemap[rhs.value.name]
                if _inline_bodo_getattr(stmt, rhs, rhs_type, new_body,
                    func_ir, typingctx, targetctx, typemap, calltypes):
                    continue
            if is_call_assign(stmt):
                rhs = stmt.value
                qvgvp__cfk = guard(find_callname, func_ir, rhs, typemap)
                if qvgvp__cfk is None:
                    new_body.append(stmt)
                    continue
                func_name, func_mod = qvgvp__cfk
                if _inline_bodo_call(rhs, i, func_mod, func_name, pass_info,
                    new_body, block, typingctx, targetctx, calltypes, work_list
                    ):
                    eijtn__exfk = True
                    break
            new_body.append(stmt)
        if not eijtn__exfk:
            dnog__sjm[hsrj__hveg].body = new_body
    func_ir.blocks = ir_utils.simplify_CFG(func_ir.blocks)


@register_pass(mutates_CFG=True, analysis_only=False)
class BodoDistributedPass(FunctionPass):
    _name = 'bodo_distributed_pass'

    def __init__(self):
        FunctionPass.__init__(self)

    def run_pass(self, state):
        assert state.func_ir
        from bodo.transforms.distributed_pass import DistributedPass
        how__cryh = DistributedPass(state.func_ir, state.typingctx, state.
            targetctx, state.typemap, state.calltypes, state.return_type,
            state.metadata, state.flags)
        state.return_type = how__cryh.run()
        return True


@register_pass(mutates_CFG=True, analysis_only=False)
class BodoSeriesPass(FunctionPass):
    _name = 'bodo_series_pass'

    def __init__(self):
        FunctionPass.__init__(self)

    def run_pass(self, state):
        assert state.func_ir
        wxn__vzd = SeriesPass(state.func_ir, state.typingctx, state.
            targetctx, state.typemap, state.calltypes, state.locals)
        ryybt__auhk = wxn__vzd.run()
        fzsn__zuov = ryybt__auhk
        if fzsn__zuov:
            fzsn__zuov = wxn__vzd.run()
        if fzsn__zuov:
            wxn__vzd.run()
        return ryybt__auhk


@register_pass(mutates_CFG=False, analysis_only=True)
class BodoDumpDistDiagnosticsPass(AnalysisPass):
    _name = 'bodo_dump_diagnostics_pass'

    def __init__(self):
        AnalysisPass.__init__(self)

    def run_pass(self, state):
        kyuv__xjh = 0
        okl__jyk = 'BODO_DISTRIBUTED_DIAGNOSTICS'
        try:
            kyuv__xjh = int(os.environ[okl__jyk])
        except:
            pass
        if kyuv__xjh > 0 and 'distributed_diagnostics' in state.metadata:
            state.metadata['distributed_diagnostics'].dump(kyuv__xjh, state
                .metadata)
        return True


class BodoCompilerSeq(BodoCompiler):

    def define_pipelines(self):
        return self._create_bodo_pipeline(distributed=False,
            inline_calls_pass=inline_all_calls)


class BodoCompilerUDF(BodoCompiler):

    def define_pipelines(self):
        return self._create_bodo_pipeline(distributed=False, udf_pipeline=True)


@register_pass(mutates_CFG=False, analysis_only=True)
class LowerParforSeq(FunctionPass):
    _name = 'bodo_lower_parfor_seq_pass'

    def __init__(self):
        FunctionPass.__init__(self)

    def run_pass(self, state):
        bodo.transforms.distributed_pass.lower_parfor_sequential(state.
            typingctx, state.func_ir, state.typemap, state.calltypes, state
            .metadata)
        return True


@register_pass(mutates_CFG=False, analysis_only=True)
class LowerBodoIRExtSeq(FunctionPass):
    _name = 'bodo_lower_ir_ext_pass'

    def __init__(self):
        FunctionPass.__init__(self)

    def run_pass(self, state):
        from bodo.transforms.distributed_pass import distributed_run_extensions
        from bodo.transforms.table_column_del_pass import remove_dead_table_columns
        from bodo.utils.transform import compile_func_single_block
        from bodo.utils.typing import decode_if_dict_array, to_str_arr_if_dict_array
        state.func_ir._definitions = build_definitions(state.func_ir.blocks)
        aztf__effxw = TypingInfo(state.typingctx, state.targetctx, state.
            typemap, state.calltypes, state.func_ir.loc)
        remove_dead_table_columns(state.func_ir, state.typemap, aztf__effxw)
        for block in state.func_ir.blocks.values():
            new_body = []
            for kcmph__ojfe in block.body:
                if type(kcmph__ojfe) in distributed_run_extensions:
                    asq__tagsl = distributed_run_extensions[type(kcmph__ojfe)]
                    if isinstance(kcmph__ojfe, bodo.ir.parquet_ext.
                        ParquetReader) or isinstance(kcmph__ojfe, bodo.ir.
                        sql_ext.SqlReader) and kcmph__ojfe.db_type in (
                        'iceberg', 'snowflake'):
                        erwg__ohk = asq__tagsl(kcmph__ojfe, None, state.
                            typemap, state.calltypes, state.typingctx,
                            state.targetctx, is_independent=True,
                            meta_head_only_info=None)
                    else:
                        erwg__ohk = asq__tagsl(kcmph__ojfe, None, state.
                            typemap, state.calltypes, state.typingctx,
                            state.targetctx)
                    new_body += erwg__ohk
                elif is_call_assign(kcmph__ojfe):
                    rhs = kcmph__ojfe.value
                    qvgvp__cfk = guard(find_callname, state.func_ir, rhs)
                    if qvgvp__cfk == ('gatherv', 'bodo') or qvgvp__cfk == (
                        'allgatherv', 'bodo'):
                        akkzw__wpw = state.typemap[kcmph__ojfe.target.name]
                        bgs__jixt = state.typemap[rhs.args[0].name]
                        if isinstance(bgs__jixt, types.Array) and isinstance(
                            akkzw__wpw, types.Array):
                            gxkld__cbw = bgs__jixt.copy(readonly=False)
                            hzee__maax = akkzw__wpw.copy(readonly=False)
                            if gxkld__cbw == hzee__maax:
                                new_body += compile_func_single_block(eval(
                                    'lambda data: data.copy()'), (rhs.args[
                                    0],), kcmph__ojfe.target, aztf__effxw)
                                continue
                        if (akkzw__wpw != bgs__jixt and 
                            to_str_arr_if_dict_array(akkzw__wpw) ==
                            to_str_arr_if_dict_array(bgs__jixt)):
                            new_body += compile_func_single_block(eval(
                                'lambda data: decode_if_dict_array(data)'),
                                (rhs.args[0],), kcmph__ojfe.target,
                                aztf__effxw, extra_globals={
                                'decode_if_dict_array': decode_if_dict_array})
                            continue
                        else:
                            kcmph__ojfe.value = rhs.args[0]
                    new_body.append(kcmph__ojfe)
                else:
                    new_body.append(kcmph__ojfe)
            block.body = new_body
        return True


@register_pass(mutates_CFG=False, analysis_only=True)
class BodoTableColumnDelPass(AnalysisPass):
    _name = 'bodo_table_column_del_pass'

    def __init__(self):
        FunctionPass.__init__(self)

    def run_pass(self, state):
        xtanb__ymaix = TableColumnDelPass(state.func_ir, state.typingctx,
            state.targetctx, state.typemap, state.calltypes)
        return xtanb__ymaix.run()


def inline_calls(func_ir, _locals, work_list=None, typingctx=None,
    targetctx=None, typemap=None, calltypes=None):
    if work_list is None:
        work_list = list(func_ir.blocks.items())
    oer__ijiv = set()
    while work_list:
        hsrj__hveg, block = work_list.pop()
        oer__ijiv.add(hsrj__hveg)
        for i, aeftx__teixr in enumerate(block.body):
            if isinstance(aeftx__teixr, ir.Assign):
                sfom__esqhw = aeftx__teixr.value
                if isinstance(sfom__esqhw, ir.Expr
                    ) and sfom__esqhw.op == 'call':
                    lldpb__wqt = guard(get_definition, func_ir, sfom__esqhw
                        .func)
                    if isinstance(lldpb__wqt, (ir.Global, ir.FreeVar)
                        ) and isinstance(lldpb__wqt.value, CPUDispatcher
                        ) and issubclass(lldpb__wqt.value._compiler.
                        pipeline_class, BodoCompiler):
                        ehdc__vbe = lldpb__wqt.value.py_func
                        arg_types = None
                        if typingctx:
                            qon__vspfw = dict(sfom__esqhw.kws)
                            mmehl__ccq = tuple(typemap[iad__fwign.name] for
                                iad__fwign in sfom__esqhw.args)
                            vzfr__dsup = {wln__pptkm: typemap[iad__fwign.
                                name] for wln__pptkm, iad__fwign in
                                qon__vspfw.items()}
                            oux__bilgt, arg_types = (lldpb__wqt.value.
                                fold_argument_types(mmehl__ccq, vzfr__dsup))
                        oux__bilgt, nglrd__pwc = inline_closure_call(func_ir,
                            ehdc__vbe.__globals__, block, i, ehdc__vbe,
                            typingctx=typingctx, targetctx=targetctx,
                            arg_typs=arg_types, typemap=typemap, calltypes=
                            calltypes, work_list=work_list)
                        _locals.update((nglrd__pwc[wln__pptkm].name,
                            iad__fwign) for wln__pptkm, iad__fwign in
                            lldpb__wqt.value.locals.items() if wln__pptkm in
                            nglrd__pwc)
                        break
    return oer__ijiv


def udf_jit(signature_or_function=None, **options):
    rai__gkzb = {'comprehension': True, 'setitem': False, 'inplace_binop': 
        False, 'reduction': True, 'numpy': True, 'stencil': False, 'fusion':
        True}
    return numba.njit(signature_or_function, parallel=rai__gkzb,
        pipeline_class=bodo.compiler.BodoCompilerUDF, **options)


def is_udf_call(func_type):
    return isinstance(func_type, numba.core.types.Dispatcher
        ) and func_type.dispatcher._compiler.pipeline_class == BodoCompilerUDF


def is_user_dispatcher(func_type):
    return isinstance(func_type, numba.core.types.functions.ObjModeDispatcher
        ) or isinstance(func_type, numba.core.types.Dispatcher) and issubclass(
        func_type.dispatcher._compiler.pipeline_class, BodoCompiler)


@register_pass(mutates_CFG=False, analysis_only=True)
class DummyCR(FunctionPass):
    _name = 'bodo_dummy_cr'

    def __init__(self):
        FunctionPass.__init__(self)

    def run_pass(self, state):
        state.cr = (state.func_ir, state.typemap, state.calltypes, state.
            return_type)
        return True


def remove_passes_after(pm, location):
    assert pm.passes
    pm._validate_pass(location)
    for mnaso__puqgi, (plfbj__vgex, oux__bilgt) in enumerate(pm.passes):
        if plfbj__vgex == location:
            break
    else:
        raise bodo.utils.typing.BodoError('Could not find pass %s' % location)
    pm.passes = pm.passes[:mnaso__puqgi + 1]
    pm._finalized = False


class TyperCompiler(BodoCompiler):

    def define_pipelines(self):
        [pm] = self._create_bodo_pipeline()
        remove_passes_after(pm, InlineOverloads)
        pm.add_pass_after(DummyCR, InlineOverloads)
        pm.finalize()
        return [pm]


def get_func_type_info(func, arg_types, kw_types):
    typingctx = numba.core.registry.cpu_target.typing_context
    targetctx = numba.core.registry.cpu_target.target_context
    veg__zxqmu = None
    uhq__qlfo = None
    _locals = {}
    xsotx__uka = numba.core.utils.pysignature(func)
    args = bodo.utils.transform.fold_argument_types(xsotx__uka, arg_types,
        kw_types)
    xiby__yxcbb = numba.core.compiler.Flags()
    sujsg__raxgp = {'comprehension': True, 'setitem': False,
        'inplace_binop': False, 'reduction': True, 'numpy': True, 'stencil':
        False, 'fusion': True}
    lou__jghrb = {'nopython': True, 'boundscheck': False, 'parallel':
        sujsg__raxgp}
    numba.core.registry.cpu_target.options.parse_as_flags(xiby__yxcbb,
        lou__jghrb)
    helzb__jqja = TyperCompiler(typingctx, targetctx, veg__zxqmu, args,
        uhq__qlfo, xiby__yxcbb, _locals)
    return helzb__jqja.compile_extra(func)
