"""
Numba monkey patches to fix issues related to Bodo. Should be imported before any
other module in bodo package.
"""
import copy
import functools
import hashlib
import inspect
import itertools
import operator
import os
import re
import sys
import textwrap
import traceback
import types as pytypes
import warnings
from collections import OrderedDict
from collections.abc import Sequence
from contextlib import ExitStack
import numba
import numba.core.boxing
import numba.core.inline_closurecall
import numba.core.typing.listdecl
import numba.np.linalg
from numba.core import analysis, cgutils, errors, ir, ir_utils, types
from numba.core.compiler import Compiler
from numba.core.errors import ForceLiteralArg, LiteralTypingError, TypingError
from numba.core.ir_utils import GuardException, _create_function_from_code_obj, analysis, build_definitions, find_callname, get_definition, guard, has_no_side_effect, mk_unique_var, remove_dead_extensions, replace_vars_inner, require, visit_vars_extensions, visit_vars_inner
from numba.core.types import literal
from numba.core.types.functions import _bt_as_lines, _ResolutionFailures, _termcolor, _unlit_non_poison
from numba.core.typing.templates import AbstractTemplate, Signature, _EmptyImplementationEntry, _inline_info, _OverloadAttributeTemplate, infer_global, signature
from numba.core.typing.typeof import Purpose, typeof
from numba.experimental.jitclass import base as jitclass_base
from numba.experimental.jitclass import decorators as jitclass_decorators
from numba.extending import NativeValue, lower_builtin, typeof_impl
from numba.parfors.parfor import get_expr_args
from bodo.utils.python_310_bytecode_pass import Bodo310ByteCodePass, peep_hole_call_function_ex_to_call_function_kw, peep_hole_fuse_dict_add_updates, peep_hole_fuse_tuple_adds
from bodo.utils.typing import BodoError, get_overload_const_str, is_overload_constant_str, raise_bodo_error
_check_numba_change = False
numba.core.typing.templates._IntrinsicTemplate.prefer_literal = True


def run_frontend(func, inline_closures=False, emit_dels=False):
    from numba.core.utils import PYVERSION
    tizj__vjdju = numba.core.bytecode.FunctionIdentity.from_function(func)
    twji__kntd = numba.core.interpreter.Interpreter(tizj__vjdju)
    jft__oxz = numba.core.bytecode.ByteCode(func_id=tizj__vjdju)
    func_ir = twji__kntd.interpret(jft__oxz)
    if PYVERSION == (3, 10):
        func_ir = peep_hole_call_function_ex_to_call_function_kw(func_ir)
        func_ir = peep_hole_fuse_dict_add_updates(func_ir)
        func_ir = peep_hole_fuse_tuple_adds(func_ir)
    if inline_closures:
        from numba.core.inline_closurecall import InlineClosureCallPass


        class DummyPipeline:

            def __init__(self, f_ir):
                self.state = numba.core.compiler.StateDict()
                self.state.typingctx = None
                self.state.targetctx = None
                self.state.args = None
                self.state.func_ir = f_ir
                self.state.typemap = None
                self.state.return_type = None
                self.state.calltypes = None
        numba.core.rewrites.rewrite_registry.apply('before-inference',
            DummyPipeline(func_ir).state)
        tckp__umuun = InlineClosureCallPass(func_ir, numba.core.cpu.
            ParallelOptions(False), {}, False)
        tckp__umuun.run()
    lkw__jvixb = numba.core.postproc.PostProcessor(func_ir)
    lkw__jvixb.run(emit_dels)
    return func_ir


if _check_numba_change:
    lines = inspect.getsource(numba.core.compiler.run_frontend)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '8c2477a793b2c08d56430997880974ac12c5570e69c9e54d37d694b322ea18b6':
        warnings.warn('numba.core.compiler.run_frontend has changed')
numba.core.compiler.run_frontend = run_frontend


def visit_vars_stmt(stmt, callback, cbdata):
    for t, wztfa__vcc in visit_vars_extensions.items():
        if isinstance(stmt, t):
            wztfa__vcc(stmt, callback, cbdata)
            return
    if isinstance(stmt, ir.Assign):
        stmt.target = visit_vars_inner(stmt.target, callback, cbdata)
        stmt.value = visit_vars_inner(stmt.value, callback, cbdata)
    elif isinstance(stmt, ir.Arg):
        stmt.name = visit_vars_inner(stmt.name, callback, cbdata)
    elif isinstance(stmt, ir.Return):
        stmt.value = visit_vars_inner(stmt.value, callback, cbdata)
    elif isinstance(stmt, ir.Raise):
        stmt.exception = visit_vars_inner(stmt.exception, callback, cbdata)
    elif isinstance(stmt, ir.Branch):
        stmt.cond = visit_vars_inner(stmt.cond, callback, cbdata)
    elif isinstance(stmt, ir.Jump):
        stmt.target = visit_vars_inner(stmt.target, callback, cbdata)
    elif isinstance(stmt, ir.Del):
        var = ir.Var(None, stmt.value, stmt.loc)
        var = visit_vars_inner(var, callback, cbdata)
        stmt.value = var.name
    elif isinstance(stmt, ir.DelAttr):
        stmt.target = visit_vars_inner(stmt.target, callback, cbdata)
        stmt.attr = visit_vars_inner(stmt.attr, callback, cbdata)
    elif isinstance(stmt, ir.SetAttr):
        stmt.target = visit_vars_inner(stmt.target, callback, cbdata)
        stmt.attr = visit_vars_inner(stmt.attr, callback, cbdata)
        stmt.value = visit_vars_inner(stmt.value, callback, cbdata)
    elif isinstance(stmt, ir.DelItem):
        stmt.target = visit_vars_inner(stmt.target, callback, cbdata)
        stmt.index = visit_vars_inner(stmt.index, callback, cbdata)
    elif isinstance(stmt, ir.StaticSetItem):
        stmt.target = visit_vars_inner(stmt.target, callback, cbdata)
        stmt.index_var = visit_vars_inner(stmt.index_var, callback, cbdata)
        stmt.value = visit_vars_inner(stmt.value, callback, cbdata)
    elif isinstance(stmt, ir.SetItem):
        stmt.target = visit_vars_inner(stmt.target, callback, cbdata)
        stmt.index = visit_vars_inner(stmt.index, callback, cbdata)
        stmt.value = visit_vars_inner(stmt.value, callback, cbdata)
    elif isinstance(stmt, ir.Print):
        stmt.args = [visit_vars_inner(x, callback, cbdata) for x in stmt.args]
        stmt.vararg = visit_vars_inner(stmt.vararg, callback, cbdata)
    else:
        pass
    return


if _check_numba_change:
    lines = inspect.getsource(numba.core.ir_utils.visit_vars_stmt)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '52b7b645ba65c35f3cf564f936e113261db16a2dff1e80fbee2459af58844117':
        warnings.warn('numba.core.ir_utils.visit_vars_stmt has changed')
numba.core.ir_utils.visit_vars_stmt = visit_vars_stmt
old_run_pass = numba.core.typed_passes.InlineOverloads.run_pass


def InlineOverloads_run_pass(self, state):
    import bodo
    bodo.compiler.bodo_overload_inline_pass(state.func_ir, state.typingctx,
        state.targetctx, state.typemap, state.calltypes)
    return old_run_pass(self, state)


numba.core.typed_passes.InlineOverloads.run_pass = InlineOverloads_run_pass
from numba.core.ir_utils import _add_alias, alias_analysis_extensions, alias_func_extensions
_immutable_type_class = (types.Number, types.scalars._NPDatetimeBase, types
    .iterators.RangeType, types.UnicodeType)


def is_immutable_type(var, typemap):
    if typemap is None or var not in typemap:
        return False
    typ = typemap[var]
    if isinstance(typ, _immutable_type_class):
        return True
    if isinstance(typ, types.BaseTuple) and all(isinstance(t,
        _immutable_type_class) for t in typ.types):
        return True
    return False


def find_potential_aliases(blocks, args, typemap, func_ir, alias_map=None,
    arg_aliases=None):
    if alias_map is None:
        alias_map = {}
    if arg_aliases is None:
        arg_aliases = set(a for a in args if not is_immutable_type(a, typemap))
    func_ir._definitions = build_definitions(func_ir.blocks)
    hior__qyfjg = ['ravel', 'transpose', 'reshape']
    for yexl__xcdtw in blocks.values():
        for seiz__nfvy in yexl__xcdtw.body:
            if type(seiz__nfvy) in alias_analysis_extensions:
                wztfa__vcc = alias_analysis_extensions[type(seiz__nfvy)]
                wztfa__vcc(seiz__nfvy, args, typemap, func_ir, alias_map,
                    arg_aliases)
            if isinstance(seiz__nfvy, ir.Assign):
                idea__ggdyg = seiz__nfvy.value
                sil__lrqd = seiz__nfvy.target.name
                if is_immutable_type(sil__lrqd, typemap):
                    continue
                if isinstance(idea__ggdyg, ir.Var
                    ) and sil__lrqd != idea__ggdyg.name:
                    _add_alias(sil__lrqd, idea__ggdyg.name, alias_map,
                        arg_aliases)
                if isinstance(idea__ggdyg, ir.Expr) and (idea__ggdyg.op ==
                    'cast' or idea__ggdyg.op in ['getitem', 'static_getitem']):
                    _add_alias(sil__lrqd, idea__ggdyg.value.name, alias_map,
                        arg_aliases)
                if isinstance(idea__ggdyg, ir.Expr
                    ) and idea__ggdyg.op == 'inplace_binop':
                    _add_alias(sil__lrqd, idea__ggdyg.lhs.name, alias_map,
                        arg_aliases)
                if isinstance(idea__ggdyg, ir.Expr
                    ) and idea__ggdyg.op == 'getattr' and idea__ggdyg.attr in [
                    'T', 'ctypes', 'flat']:
                    _add_alias(sil__lrqd, idea__ggdyg.value.name, alias_map,
                        arg_aliases)
                if isinstance(idea__ggdyg, ir.Expr
                    ) and idea__ggdyg.op == 'getattr' and idea__ggdyg.attr not in [
                    'shape'] and idea__ggdyg.value.name in arg_aliases:
                    _add_alias(sil__lrqd, idea__ggdyg.value.name, alias_map,
                        arg_aliases)
                if isinstance(idea__ggdyg, ir.Expr
                    ) and idea__ggdyg.op == 'getattr' and idea__ggdyg.attr in (
                    'loc', 'iloc', 'iat', '_obj', 'obj', 'codes', '_df'):
                    _add_alias(sil__lrqd, idea__ggdyg.value.name, alias_map,
                        arg_aliases)
                if isinstance(idea__ggdyg, ir.Expr) and idea__ggdyg.op in (
                    'build_tuple', 'build_list', 'build_set'
                    ) and not is_immutable_type(sil__lrqd, typemap):
                    for udil__tquzm in idea__ggdyg.items:
                        _add_alias(sil__lrqd, udil__tquzm.name, alias_map,
                            arg_aliases)
                if isinstance(idea__ggdyg, ir.Expr
                    ) and idea__ggdyg.op == 'call':
                    pez__wvvw = guard(find_callname, func_ir, idea__ggdyg,
                        typemap)
                    if pez__wvvw is None:
                        continue
                    dzjv__yohb, ofg__rrfqx = pez__wvvw
                    if pez__wvvw in alias_func_extensions:
                        afth__ilqaq = alias_func_extensions[pez__wvvw]
                        afth__ilqaq(sil__lrqd, idea__ggdyg.args, alias_map,
                            arg_aliases)
                    if ofg__rrfqx == 'numpy' and dzjv__yohb in hior__qyfjg:
                        _add_alias(sil__lrqd, idea__ggdyg.args[0].name,
                            alias_map, arg_aliases)
                    if isinstance(ofg__rrfqx, ir.Var
                        ) and dzjv__yohb in hior__qyfjg:
                        _add_alias(sil__lrqd, ofg__rrfqx.name, alias_map,
                            arg_aliases)
    lzrb__qody = copy.deepcopy(alias_map)
    for udil__tquzm in lzrb__qody:
        for kvt__bazz in lzrb__qody[udil__tquzm]:
            alias_map[udil__tquzm] |= alias_map[kvt__bazz]
        for kvt__bazz in lzrb__qody[udil__tquzm]:
            alias_map[kvt__bazz] = alias_map[udil__tquzm]
    return alias_map, arg_aliases


if _check_numba_change:
    lines = inspect.getsource(ir_utils.find_potential_aliases)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'e6cf3e0f502f903453eb98346fc6854f87dc4ea1ac62f65c2d6aef3bf690b6c5':
        warnings.warn('ir_utils.find_potential_aliases has changed')
ir_utils.find_potential_aliases = find_potential_aliases
numba.parfors.array_analysis.find_potential_aliases = find_potential_aliases
if _check_numba_change:
    lines = inspect.getsource(ir_utils.dead_code_elimination)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '40a8626300a1a17523944ec7842b093c91258bbc60844bbd72191a35a4c366bf':
        warnings.warn('ir_utils.dead_code_elimination has changed')


def mini_dce(func_ir, typemap=None, alias_map=None, arg_aliases=None):
    from numba.core.analysis import compute_cfg_from_blocks, compute_live_map, compute_use_defs
    jbs__mqwyq = compute_cfg_from_blocks(func_ir.blocks)
    wzb__lbtx = compute_use_defs(func_ir.blocks)
    yhe__nqs = compute_live_map(jbs__mqwyq, func_ir.blocks, wzb__lbtx.
        usemap, wzb__lbtx.defmap)
    enzy__igus = True
    while enzy__igus:
        enzy__igus = False
        for label, block in func_ir.blocks.items():
            lives = {udil__tquzm.name for udil__tquzm in block.terminator.
                list_vars()}
            for tzj__rlifd, itinr__pmb in jbs__mqwyq.successors(label):
                lives |= yhe__nqs[tzj__rlifd]
            vpvw__ppwm = [block.terminator]
            for stmt in reversed(block.body[:-1]):
                if isinstance(stmt, ir.Assign):
                    sil__lrqd = stmt.target
                    rabz__hyk = stmt.value
                    if sil__lrqd.name not in lives:
                        if isinstance(rabz__hyk, ir.Expr
                            ) and rabz__hyk.op == 'make_function':
                            continue
                        if isinstance(rabz__hyk, ir.Expr
                            ) and rabz__hyk.op == 'getattr':
                            continue
                        if isinstance(rabz__hyk, ir.Const):
                            continue
                        if typemap and isinstance(typemap.get(sil__lrqd,
                            None), types.Function):
                            continue
                        if isinstance(rabz__hyk, ir.Expr
                            ) and rabz__hyk.op == 'build_map':
                            continue
                        if isinstance(rabz__hyk, ir.Expr
                            ) and rabz__hyk.op == 'build_tuple':
                            continue
                        if isinstance(rabz__hyk, ir.Expr
                            ) and rabz__hyk.op == 'binop':
                            continue
                        if isinstance(rabz__hyk, ir.Expr
                            ) and rabz__hyk.op == 'unary':
                            continue
                        if isinstance(rabz__hyk, ir.Expr) and rabz__hyk.op in (
                            'static_getitem', 'getitem'):
                            continue
                    if isinstance(rabz__hyk, ir.Var
                        ) and sil__lrqd.name == rabz__hyk.name:
                        continue
                if isinstance(stmt, ir.Del):
                    if stmt.value not in lives:
                        continue
                if type(stmt) in analysis.ir_extension_usedefs:
                    nog__tabp = analysis.ir_extension_usedefs[type(stmt)]
                    vqu__kayf, hectu__arcgb = nog__tabp(stmt)
                    lives -= hectu__arcgb
                    lives |= vqu__kayf
                else:
                    lives |= {udil__tquzm.name for udil__tquzm in stmt.
                        list_vars()}
                    if isinstance(stmt, ir.Assign):
                        dyl__ngjr = set()
                        if isinstance(rabz__hyk, ir.Expr):
                            dyl__ngjr = {udil__tquzm.name for udil__tquzm in
                                rabz__hyk.list_vars()}
                        if sil__lrqd.name not in dyl__ngjr:
                            lives.remove(sil__lrqd.name)
                vpvw__ppwm.append(stmt)
            vpvw__ppwm.reverse()
            if len(block.body) != len(vpvw__ppwm):
                enzy__igus = True
            block.body = vpvw__ppwm


ir_utils.dead_code_elimination = mini_dce
numba.core.typed_passes.dead_code_elimination = mini_dce
numba.core.inline_closurecall.dead_code_elimination = mini_dce
from numba.core.cpu_options import InlineOptions


def make_overload_template(func, overload_func, jit_options, strict, inline,
    prefer_literal=False, **kwargs):
    xysx__mqxqt = getattr(func, '__name__', str(func))
    name = 'OverloadTemplate_%s' % (xysx__mqxqt,)
    no_unliteral = kwargs.pop('no_unliteral', False)
    base = numba.core.typing.templates._OverloadFunctionTemplate
    ajw__kxrqe = dict(key=func, _overload_func=staticmethod(overload_func),
        _impl_cache={}, _compiled_overloads={}, _jit_options=jit_options,
        _strict=strict, _inline=staticmethod(InlineOptions(inline)),
        _inline_overloads={}, prefer_literal=prefer_literal, _no_unliteral=
        no_unliteral, metadata=kwargs)
    return type(base)(name, (base,), ajw__kxrqe)


if _check_numba_change:
    lines = inspect.getsource(numba.core.typing.templates.
        make_overload_template)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '7f6974584cb10e49995b652827540cc6732e497c0b9f8231b44fd83fcc1c0a83':
        warnings.warn(
            'numba.core.typing.templates.make_overload_template has changed')
numba.core.typing.templates.make_overload_template = make_overload_template


def _resolve(self, typ, attr):
    if self._attr != attr:
        return None
    if isinstance(typ, types.TypeRef):
        assert typ == self.key
    else:
        assert isinstance(typ, self.key)


    class MethodTemplate(AbstractTemplate):
        key = self.key, attr
        _inline = self._inline
        _no_unliteral = getattr(self, '_no_unliteral', False)
        _overload_func = staticmethod(self._overload_func)
        _inline_overloads = self._inline_overloads
        prefer_literal = self.prefer_literal

        def generic(_, args, kws):
            args = (typ,) + tuple(args)
            fnty = self._get_function_type(self.context, typ)
            sig = self._get_signature(self.context, fnty, args, kws)
            sig = sig.replace(pysig=numba.core.utils.pysignature(self.
                _overload_func))
            for mjw__kqa in fnty.templates:
                self._inline_overloads.update(mjw__kqa._inline_overloads)
            if sig is not None:
                return sig.as_method()
    return types.BoundFunction(MethodTemplate, typ)


if _check_numba_change:
    lines = inspect.getsource(numba.core.typing.templates.
        _OverloadMethodTemplate._resolve)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'ce8e0935dc939d0867ef969e1ed2975adb3533a58a4133fcc90ae13c4418e4d6':
        warnings.warn(
            'numba.core.typing.templates._OverloadMethodTemplate._resolve has changed'
            )
numba.core.typing.templates._OverloadMethodTemplate._resolve = _resolve


def make_overload_attribute_template(typ, attr, overload_func, inline,
    prefer_literal=False, base=_OverloadAttributeTemplate, **kwargs):
    assert isinstance(typ, types.Type) or issubclass(typ, types.Type)
    name = 'OverloadAttributeTemplate_%s_%s' % (typ, attr)
    no_unliteral = kwargs.pop('no_unliteral', False)
    ajw__kxrqe = dict(key=typ, _attr=attr, _impl_cache={}, _inline=
        staticmethod(InlineOptions(inline)), _inline_overloads={},
        _no_unliteral=no_unliteral, _overload_func=staticmethod(
        overload_func), prefer_literal=prefer_literal, metadata=kwargs)
    obj = type(base)(name, (base,), ajw__kxrqe)
    return obj


if _check_numba_change:
    lines = inspect.getsource(numba.core.typing.templates.
        make_overload_attribute_template)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'f066c38c482d6cf8bf5735a529c3264118ba9b52264b24e58aad12a6b1960f5d':
        warnings.warn(
            'numba.core.typing.templates.make_overload_attribute_template has changed'
            )
numba.core.typing.templates.make_overload_attribute_template = (
    make_overload_attribute_template)


def generic(self, args, kws):
    from numba.core.typed_passes import PreLowerStripPhis
    lah__klgv, wuj__uyoa = self._get_impl(args, kws)
    if lah__klgv is None:
        return
    jkho__kdqkd = types.Dispatcher(lah__klgv)
    if not self._inline.is_never_inline:
        from numba.core import compiler, typed_passes
        from numba.core.inline_closurecall import InlineWorker
        hdb__vkgku = lah__klgv._compiler
        flags = compiler.Flags()
        zkldj__pcuu = hdb__vkgku.targetdescr.typing_context
        klk__bwxlk = hdb__vkgku.targetdescr.target_context
        xznt__zcmgx = hdb__vkgku.pipeline_class(zkldj__pcuu, klk__bwxlk,
            None, None, None, flags, None)
        vckd__wwsx = InlineWorker(zkldj__pcuu, klk__bwxlk, hdb__vkgku.
            locals, xznt__zcmgx, flags, None)
        ryw__mya = jkho__kdqkd.dispatcher.get_call_template
        mjw__kqa, huxst__gaq, plbt__saf, kws = ryw__mya(wuj__uyoa, kws)
        if plbt__saf in self._inline_overloads:
            return self._inline_overloads[plbt__saf]['iinfo'].signature
        ir = vckd__wwsx.run_untyped_passes(jkho__kdqkd.dispatcher.py_func,
            enable_ssa=True)
        typemap, return_type, calltypes, _ = typed_passes.type_inference_stage(
            self.context, klk__bwxlk, ir, plbt__saf, None)
        ir = PreLowerStripPhis()._strip_phi_nodes(ir)
        ir._definitions = numba.core.ir_utils.build_definitions(ir.blocks)
        sig = Signature(return_type, plbt__saf, None)
        self._inline_overloads[sig.args] = {'folded_args': plbt__saf}
        rskn__rvdb = _EmptyImplementationEntry('always inlined')
        self._compiled_overloads[sig.args] = rskn__rvdb
        if not self._inline.is_always_inline:
            sig = jkho__kdqkd.get_call_type(self.context, wuj__uyoa, kws)
            self._compiled_overloads[sig.args] = jkho__kdqkd.get_overload(sig)
        bhka__ewjdm = _inline_info(ir, typemap, calltypes, sig)
        self._inline_overloads[sig.args] = {'folded_args': plbt__saf,
            'iinfo': bhka__ewjdm}
    else:
        sig = jkho__kdqkd.get_call_type(self.context, wuj__uyoa, kws)
        if sig is None:
            return None
        self._compiled_overloads[sig.args] = jkho__kdqkd.get_overload(sig)
    return sig


if _check_numba_change:
    lines = inspect.getsource(numba.core.typing.templates.
        _OverloadFunctionTemplate.generic)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '5d453a6d0215ebf0bab1279ff59eb0040b34938623be99142ce20acc09cdeb64':
        warnings.warn(
            'numba.core.typing.templates._OverloadFunctionTemplate.generic has changed'
            )
numba.core.typing.templates._OverloadFunctionTemplate.generic = generic


def bound_function(template_key, no_unliteral=False):

    def wrapper(method_resolver):

        @functools.wraps(method_resolver)
        def attribute_resolver(self, ty):


            class MethodTemplate(AbstractTemplate):
                key = template_key

                def generic(_, args, kws):
                    sig = method_resolver(self, ty, args, kws)
                    if sig is not None and sig.recvr is None:
                        sig = sig.replace(recvr=ty)
                    return sig
            MethodTemplate._no_unliteral = no_unliteral
            return types.BoundFunction(MethodTemplate, ty)
        return attribute_resolver
    return wrapper


if _check_numba_change:
    lines = inspect.getsource(numba.core.typing.templates.bound_function)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'a2feefe64eae6a15c56affc47bf0c1d04461f9566913442d539452b397103322':
        warnings.warn('numba.core.typing.templates.bound_function has changed')
numba.core.typing.templates.bound_function = bound_function


def get_call_type(self, context, args, kws):
    from numba.core import utils
    irft__mxzk = [True, False]
    zzykc__ryy = [False, True]
    hvuzn__bro = _ResolutionFailures(context, self, args, kws, depth=self.
        _depth)
    from numba.core.target_extension import get_local_target
    qbj__rsv = get_local_target(context)
    hkr__kgxe = utils.order_by_target_specificity(qbj__rsv, self.templates,
        fnkey=self.key[0])
    self._depth += 1
    for reu__rear in hkr__kgxe:
        auq__pzkt = reu__rear(context)
        xvsiq__vilv = irft__mxzk if auq__pzkt.prefer_literal else zzykc__ryy
        xvsiq__vilv = [True] if getattr(auq__pzkt, '_no_unliteral', False
            ) else xvsiq__vilv
        for xmdw__yfz in xvsiq__vilv:
            try:
                if xmdw__yfz:
                    sig = auq__pzkt.apply(args, kws)
                else:
                    aogck__gfhr = tuple([_unlit_non_poison(a) for a in args])
                    couhn__ffhr = {qolux__rpok: _unlit_non_poison(
                        udil__tquzm) for qolux__rpok, udil__tquzm in kws.
                        items()}
                    sig = auq__pzkt.apply(aogck__gfhr, couhn__ffhr)
            except Exception as e:
                from numba.core import utils
                if utils.use_new_style_errors() and not isinstance(e,
                    errors.NumbaError):
                    raise e
                else:
                    sig = None
                    hvuzn__bro.add_error(auq__pzkt, False, e, xmdw__yfz)
            else:
                if sig is not None:
                    self._impl_keys[sig.args] = auq__pzkt.get_impl_key(sig)
                    self._depth -= 1
                    return sig
                else:
                    gcon__mnrmy = getattr(auq__pzkt, 'cases', None)
                    if gcon__mnrmy is not None:
                        msg = 'No match for registered cases:\n%s'
                        msg = msg % '\n'.join(' * {}'.format(x) for x in
                            gcon__mnrmy)
                    else:
                        msg = 'No match.'
                    hvuzn__bro.add_error(auq__pzkt, True, msg, xmdw__yfz)
    hvuzn__bro.raise_error()


if _check_numba_change:
    lines = inspect.getsource(numba.core.types.functions.BaseFunction.
        get_call_type)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '25f038a7216f8e6f40068ea81e11fd9af8ad25d19888f7304a549941b01b7015':
        warnings.warn(
            'numba.core.types.functions.BaseFunction.get_call_type has changed'
            )
numba.core.types.functions.BaseFunction.get_call_type = get_call_type
bodo_typing_error_info = """
This is often caused by the use of unsupported features or typing issues.
See https://docs.bodo.ai/
"""


def get_call_type2(self, context, args, kws):
    mjw__kqa = self.template(context)
    obq__lant = None
    vhw__wagq = None
    ardz__sjlbc = None
    xvsiq__vilv = [True, False] if mjw__kqa.prefer_literal else [False, True]
    xvsiq__vilv = [True] if getattr(mjw__kqa, '_no_unliteral', False
        ) else xvsiq__vilv
    for xmdw__yfz in xvsiq__vilv:
        if xmdw__yfz:
            try:
                ardz__sjlbc = mjw__kqa.apply(args, kws)
            except Exception as cmjwn__zxh:
                if isinstance(cmjwn__zxh, errors.ForceLiteralArg):
                    raise cmjwn__zxh
                obq__lant = cmjwn__zxh
                ardz__sjlbc = None
            else:
                break
        else:
            ksr__yjqqh = tuple([_unlit_non_poison(a) for a in args])
            jkuq__fkctb = {qolux__rpok: _unlit_non_poison(udil__tquzm) for 
                qolux__rpok, udil__tquzm in kws.items()}
            cme__qgsyx = ksr__yjqqh == args and kws == jkuq__fkctb
            if not cme__qgsyx and ardz__sjlbc is None:
                try:
                    ardz__sjlbc = mjw__kqa.apply(ksr__yjqqh, jkuq__fkctb)
                except Exception as cmjwn__zxh:
                    from numba.core import utils
                    if utils.use_new_style_errors() and not isinstance(
                        cmjwn__zxh, errors.NumbaError):
                        raise cmjwn__zxh
                    if isinstance(cmjwn__zxh, errors.ForceLiteralArg):
                        if mjw__kqa.prefer_literal:
                            raise cmjwn__zxh
                    vhw__wagq = cmjwn__zxh
                else:
                    break
    if ardz__sjlbc is None and (vhw__wagq is not None or obq__lant is not None
        ):
        nzgcx__tzsu = '- Resolution failure for {} arguments:\n{}\n'
        bhy__vluk = _termcolor.highlight(nzgcx__tzsu)
        if numba.core.config.DEVELOPER_MODE:
            xnwc__fom = ' ' * 4

            def add_bt(error):
                if isinstance(error, BaseException):
                    irkex__mrn = traceback.format_exception(type(error),
                        error, error.__traceback__)
                else:
                    irkex__mrn = ['']
                xvvcr__xdi = '\n{}'.format(2 * xnwc__fom)
                iax__hsw = _termcolor.reset(xvvcr__xdi + xvvcr__xdi.join(
                    _bt_as_lines(irkex__mrn)))
                return _termcolor.reset(iax__hsw)
        else:
            add_bt = lambda X: ''

        def nested_msg(literalness, e):
            qejaz__fmzp = str(e)
            qejaz__fmzp = qejaz__fmzp if qejaz__fmzp else str(repr(e)
                ) + add_bt(e)
            bhgnc__kuw = errors.TypingError(textwrap.dedent(qejaz__fmzp))
            return bhy__vluk.format(literalness, str(bhgnc__kuw))
        import bodo
        if isinstance(obq__lant, bodo.utils.typing.BodoError):
            raise obq__lant
        if numba.core.config.DEVELOPER_MODE:
            raise errors.TypingError(nested_msg('literal', obq__lant) +
                nested_msg('non-literal', vhw__wagq))
        else:
            if 'missing a required argument' in obq__lant.msg:
                msg = 'missing a required argument'
            else:
                msg = 'Compilation error for '
                if isinstance(self.this, bodo.hiframes.pd_dataframe_ext.
                    DataFrameType):
                    msg += 'DataFrame.'
                elif isinstance(self.this, bodo.hiframes.pd_series_ext.
                    SeriesType):
                    msg += 'Series.'
                msg += f'{self.typing_key[1]}().{bodo_typing_error_info}'
            raise errors.TypingError(msg, loc=obq__lant.loc)
    return ardz__sjlbc


if _check_numba_change:
    lines = inspect.getsource(numba.core.types.functions.BoundFunction.
        get_call_type)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '502cd77c0084452e903a45a0f1f8107550bfbde7179363b57dabd617ce135f4a':
        warnings.warn(
            'numba.core.types.functions.BoundFunction.get_call_type has changed'
            )
numba.core.types.functions.BoundFunction.get_call_type = get_call_type2


def string_from_string_and_size(self, string, size):
    from llvmlite import ir as lir
    fnty = lir.FunctionType(self.pyobj, [self.cstring, self.py_ssize_t])
    dzjv__yohb = 'PyUnicode_FromStringAndSize'
    fn = self._get_function(fnty, name=dzjv__yohb)
    return self.builder.call(fn, [string, size])


numba.core.pythonapi.PythonAPI.string_from_string_and_size = (
    string_from_string_and_size)


def _compile_for_args(self, *args, **kws):
    assert not kws
    self._compilation_chain_init_hook()
    import bodo

    def error_rewrite(e, issue_type):
        if numba.core.config.SHOW_HELP:
            gjfvt__veksn = errors.error_extras[issue_type]
            e.patch_message('\n'.join((str(e).rstrip(), gjfvt__veksn)))
        if numba.core.config.FULL_TRACEBACKS:
            raise e
        else:
            raise e.with_traceback(None)
    pxxqe__alfly = []
    for a in args:
        if isinstance(a, numba.core.dispatcher.OmittedArg):
            pxxqe__alfly.append(types.Omitted(a.value))
        else:
            pxxqe__alfly.append(self.typeof_pyval(a))
    lonpb__fqc = None
    try:
        error = None
        lonpb__fqc = self.compile(tuple(pxxqe__alfly))
    except errors.ForceLiteralArg as e:
        nzc__abfh = [i for i in e.requested_args if isinstance(args[i],
            types.Literal) and not isinstance(args[i], types.LiteralStrKeyDict)
            ]
        if nzc__abfh:
            ntrth__wocw = """Repeated literal typing request.
{}.
This is likely caused by an error in typing. Please see nested and suppressed exceptions."""
            cmu__aec = ', '.join('Arg #{} is {}'.format(i, args[i]) for i in
                sorted(nzc__abfh))
            raise errors.CompilerError(ntrth__wocw.format(cmu__aec))
        wuj__uyoa = []
        try:
            for i, udil__tquzm in enumerate(args):
                if i in e.requested_args:
                    if i in e.file_infos:
                        wuj__uyoa.append(types.FilenameType(args[i], e.
                            file_infos[i]))
                    else:
                        wuj__uyoa.append(types.literal(args[i]))
                else:
                    wuj__uyoa.append(args[i])
            args = wuj__uyoa
        except (OSError, FileNotFoundError) as jvu__mmtz:
            error = FileNotFoundError(str(jvu__mmtz) + '\n' + e.loc.
                strformat() + '\n')
        except bodo.utils.typing.BodoError as e:
            error = bodo.utils.typing.BodoError(str(e))
        if error is None:
            try:
                lonpb__fqc = self._compile_for_args(*args)
            except TypingError as e:
                error = errors.TypingError(str(e))
            except bodo.utils.typing.BodoError as e:
                error = bodo.utils.typing.BodoError(str(e))
    except errors.TypingError as e:
        snt__zxyk = []
        for i, avti__xgj in enumerate(args):
            val = avti__xgj.value if isinstance(avti__xgj, numba.core.
                dispatcher.OmittedArg) else avti__xgj
            try:
                bhb__gmnwl = typeof(val, Purpose.argument)
            except ValueError as vab__ufx:
                snt__zxyk.append((i, str(vab__ufx)))
            else:
                if bhb__gmnwl is None:
                    snt__zxyk.append((i,
                        f'cannot determine Numba type of value {val}'))
        if snt__zxyk:
            moj__yrz = '\n'.join(f'- argument {i}: {ces__vaik}' for i,
                ces__vaik in snt__zxyk)
            msg = f"""{str(e).rstrip()} 

This error may have been caused by the following argument(s):
{moj__yrz}
"""
            e.patch_message(msg)
        if "Cannot determine Numba type of <class 'numpy.ufunc'>" in e.msg:
            msg = 'Unsupported Numpy ufunc encountered in JIT code'
            error = bodo.utils.typing.BodoError(msg, loc=e.loc)
        elif not numba.core.config.DEVELOPER_MODE:
            if bodo_typing_error_info not in e.msg:
                iqg__ndki = ['Failed in nopython mode pipeline',
                    'Failed in bodo mode pipeline', 'Failed at nopython',
                    'Overload', 'lowering']
                icb__dcv = False
                for pqphh__nfvj in iqg__ndki:
                    if pqphh__nfvj in e.msg:
                        msg = 'Compilation error. '
                        msg += f'{bodo_typing_error_info}'
                        icb__dcv = True
                        break
                if not icb__dcv:
                    msg = f'{str(e)}'
                msg += '\n' + e.loc.strformat() + '\n'
                e.patch_message(msg)
        error_rewrite(e, 'typing')
    except errors.UnsupportedError as e:
        error_rewrite(e, 'unsupported_error')
    except (errors.NotDefinedError, errors.RedefinedError, errors.
        VerificationError) as e:
        error_rewrite(e, 'interpreter')
    except errors.ConstantInferenceError as e:
        error_rewrite(e, 'constant_inference')
    except bodo.utils.typing.BodoError as e:
        error = bodo.utils.typing.BodoError(str(e))
    except Exception as e:
        if numba.core.config.SHOW_HELP:
            if hasattr(e, 'patch_message'):
                gjfvt__veksn = errors.error_extras['reportable']
                e.patch_message('\n'.join((str(e).rstrip(), gjfvt__veksn)))
        raise e
    finally:
        self._types_active_call = []
        del args
        if error:
            raise error
    return lonpb__fqc


if _check_numba_change:
    lines = inspect.getsource(numba.core.dispatcher._DispatcherBase.
        _compile_for_args)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '5cdfbf0b13a528abf9f0408e70f67207a03e81d610c26b1acab5b2dc1f79bf06':
        warnings.warn(
            'numba.core.dispatcher._DispatcherBase._compile_for_args has changed'
            )
numba.core.dispatcher._DispatcherBase._compile_for_args = _compile_for_args


def resolve_gb_agg_funcs(cres):
    from bodo.ir.aggregate import gb_agg_cfunc_addr
    for bhfg__nwv in cres.library._codegen._engine._defined_symbols:
        if bhfg__nwv.startswith('cfunc'
            ) and 'get_agg_udf_addr' not in bhfg__nwv and (
            'bodo_gb_udf_update_local' in bhfg__nwv or 
            'bodo_gb_udf_combine' in bhfg__nwv or 'bodo_gb_udf_eval' in
            bhfg__nwv or 'bodo_gb_apply_general_udfs' in bhfg__nwv):
            gb_agg_cfunc_addr[bhfg__nwv
                ] = cres.library.get_pointer_to_function(bhfg__nwv)


def resolve_join_general_cond_funcs(cres):
    from bodo.ir.join import join_gen_cond_cfunc_addr
    for bhfg__nwv in cres.library._codegen._engine._defined_symbols:
        if bhfg__nwv.startswith('cfunc') and ('get_join_cond_addr' not in
            bhfg__nwv or 'bodo_join_gen_cond' in bhfg__nwv):
            join_gen_cond_cfunc_addr[bhfg__nwv
                ] = cres.library.get_pointer_to_function(bhfg__nwv)


def compile(self, sig):
    import numba.core.event as ev
    from numba.core import sigutils
    from numba.core.compiler_lock import global_compiler_lock
    import bodo
    lah__klgv = self._get_dispatcher_for_current_target()
    if lah__klgv is not self:
        return lah__klgv.compile(sig)
    with ExitStack() as scope:
        cres = None

        def cb_compiler(dur):
            if cres is not None:
                self._callback_add_compiler_timer(dur, cres)

        def cb_llvm(dur):
            if cres is not None:
                self._callback_add_llvm_timer(dur, cres)
        scope.enter_context(ev.install_timer('numba:compiler_lock',
            cb_compiler))
        scope.enter_context(ev.install_timer('numba:llvm_lock', cb_llvm))
        scope.enter_context(global_compiler_lock)
        if not self._can_compile:
            raise RuntimeError('compilation disabled')
        with self._compiling_counter:
            args, return_type = sigutils.normalize_signature(sig)
            lbn__nnlgn = self.overloads.get(tuple(args))
            if lbn__nnlgn is not None:
                return lbn__nnlgn.entry_point
            cres = self._cache.load_overload(sig, self.targetctx)
            if cres is not None:
                resolve_gb_agg_funcs(cres)
                resolve_join_general_cond_funcs(cres)
                self._cache_hits[sig] += 1
                if not cres.objectmode:
                    self.targetctx.insert_user_function(cres.entry_point,
                        cres.fndesc, [cres.library])
                self.add_overload(cres)
                return cres.entry_point
            self._cache_misses[sig] += 1
            fcyze__nss = dict(dispatcher=self, args=args, return_type=
                return_type)
            with ev.trigger_event('numba:compile', data=fcyze__nss):
                try:
                    cres = self._compiler.compile(args, return_type)
                except errors.ForceLiteralArg as e:

                    def folded(args, kws):
                        return self._compiler.fold_argument_types(args, kws)[1]
                    raise e.bind_fold_arguments(folded)
                self.add_overload(cres)
            if os.environ.get('BODO_PLATFORM_CACHE_LOCATION') is not None:
                if bodo.get_rank() == 0:
                    self._cache.save_overload(sig, cres)
            else:
                epck__hagsn = bodo.get_nodes_first_ranks()
                if bodo.get_rank() in epck__hagsn:
                    self._cache.save_overload(sig, cres)
            return cres.entry_point


if _check_numba_change:
    lines = inspect.getsource(numba.core.dispatcher.Dispatcher.compile)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '934ec993577ea3b1c7dd2181ac02728abf8559fd42c17062cc821541b092ff8f':
        warnings.warn('numba.core.dispatcher.Dispatcher.compile has changed')
numba.core.dispatcher.Dispatcher.compile = compile


def _get_module_for_linking(self):
    import llvmlite.binding as ll
    self._ensure_finalized()
    if self._shared_module is not None:
        return self._shared_module
    pukq__olxkc = self._final_module
    bdfqh__mzzm = []
    qug__vxi = 0
    for fn in pukq__olxkc.functions:
        qug__vxi += 1
        if not fn.is_declaration and fn.linkage == ll.Linkage.external:
            if 'get_agg_udf_addr' not in fn.name:
                if 'bodo_gb_udf_update_local' in fn.name:
                    continue
                if 'bodo_gb_udf_combine' in fn.name:
                    continue
                if 'bodo_gb_udf_eval' in fn.name:
                    continue
                if 'bodo_gb_apply_general_udfs' in fn.name:
                    continue
            if 'get_join_cond_addr' not in fn.name:
                if 'bodo_join_gen_cond' in fn.name:
                    continue
            bdfqh__mzzm.append(fn.name)
    if qug__vxi == 0:
        raise RuntimeError(
            'library unfit for linking: no available functions in %s' % (self,)
            )
    if bdfqh__mzzm:
        pukq__olxkc = pukq__olxkc.clone()
        for name in bdfqh__mzzm:
            pukq__olxkc.get_function(name).linkage = 'linkonce_odr'
    self._shared_module = pukq__olxkc
    return pukq__olxkc


if _check_numba_change:
    lines = inspect.getsource(numba.core.codegen.CPUCodeLibrary.
        _get_module_for_linking)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '56dde0e0555b5ec85b93b97c81821bce60784515a1fbf99e4542e92d02ff0a73':
        warnings.warn(
            'numba.core.codegen.CPUCodeLibrary._get_module_for_linking has changed'
            )
numba.core.codegen.CPUCodeLibrary._get_module_for_linking = (
    _get_module_for_linking)


def propagate(self, typeinfer):
    import bodo
    errors = []
    for ghjrb__qctfn in self.constraints:
        loc = ghjrb__qctfn.loc
        with typeinfer.warnings.catch_warnings(filename=loc.filename,
            lineno=loc.line):
            try:
                ghjrb__qctfn(typeinfer)
            except numba.core.errors.ForceLiteralArg as e:
                errors.append(e)
            except numba.core.errors.TypingError as e:
                numba.core.typeinfer._logger.debug('captured error', exc_info=e
                    )
                dpkz__oug = numba.core.errors.TypingError(str(e), loc=
                    ghjrb__qctfn.loc, highlighting=False)
                errors.append(numba.core.utils.chain_exception(dpkz__oug, e))
            except bodo.utils.typing.BodoError as e:
                if loc not in e.locs_in_msg:
                    errors.append(bodo.utils.typing.BodoError(str(e.msg) +
                        '\n' + loc.strformat() + '\n', locs_in_msg=e.
                        locs_in_msg + [loc]))
                else:
                    errors.append(bodo.utils.typing.BodoError(e.msg,
                        locs_in_msg=e.locs_in_msg))
            except Exception as e:
                from numba.core import utils
                if utils.use_old_style_errors():
                    numba.core.typeinfer._logger.debug('captured error',
                        exc_info=e)
                    msg = """Internal error at {con}.
{err}
Enable logging at debug level for details."""
                    dpkz__oug = numba.core.errors.TypingError(msg.format(
                        con=ghjrb__qctfn, err=str(e)), loc=ghjrb__qctfn.loc,
                        highlighting=False)
                    errors.append(utils.chain_exception(dpkz__oug, e))
                elif utils.use_new_style_errors():
                    raise e
                else:
                    msg = (
                        f"Unknown CAPTURED_ERRORS style: '{numba.core.config.CAPTURED_ERRORS}'."
                        )
                    assert 0, msg
    return errors


if _check_numba_change:
    lines = inspect.getsource(numba.core.typeinfer.ConstraintNetwork.propagate)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '1e73635eeba9ba43cb3372f395b747ae214ce73b729fb0adba0a55237a1cb063':
        warnings.warn(
            'numba.core.typeinfer.ConstraintNetwork.propagate has changed')
numba.core.typeinfer.ConstraintNetwork.propagate = propagate


def raise_error(self):
    import bodo
    for mbb__mcice in self._failures.values():
        for nqutk__kwck in mbb__mcice:
            if isinstance(nqutk__kwck.error, ForceLiteralArg):
                raise nqutk__kwck.error
            if isinstance(nqutk__kwck.error, bodo.utils.typing.BodoError):
                raise nqutk__kwck.error
    raise TypingError(self.format())


if _check_numba_change:
    lines = inspect.getsource(numba.core.types.functions.
        _ResolutionFailures.raise_error)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '84b89430f5c8b46cfc684804e6037f00a0f170005cd128ad245551787b2568ea':
        warnings.warn(
            'numba.core.types.functions._ResolutionFailures.raise_error has changed'
            )
numba.core.types.functions._ResolutionFailures.raise_error = raise_error


def bodo_remove_dead_block(block, lives, call_table, arg_aliases, alias_map,
    alias_set, func_ir, typemap):
    from bodo.transforms.distributed_pass import saved_array_analysis
    from bodo.utils.utils import is_array_typ, is_expr
    yxhr__bxs = False
    vpvw__ppwm = [block.terminator]
    for stmt in reversed(block.body[:-1]):
        vsqs__lznk = set()
        rueu__gvmme = lives & alias_set
        for udil__tquzm in rueu__gvmme:
            vsqs__lznk |= alias_map[udil__tquzm]
        lives_n_aliases = lives | vsqs__lznk | arg_aliases
        if type(stmt) in remove_dead_extensions:
            wztfa__vcc = remove_dead_extensions[type(stmt)]
            stmt = wztfa__vcc(stmt, lives, lives_n_aliases, arg_aliases,
                alias_map, func_ir, typemap)
            if stmt is None:
                yxhr__bxs = True
                continue
        if isinstance(stmt, ir.Assign):
            sil__lrqd = stmt.target
            rabz__hyk = stmt.value
            if sil__lrqd.name not in lives:
                if has_no_side_effect(rabz__hyk, lives_n_aliases, call_table):
                    yxhr__bxs = True
                    continue
                if isinstance(rabz__hyk, ir.Expr
                    ) and rabz__hyk.op == 'call' and call_table[rabz__hyk.
                    func.name] == ['astype']:
                    bboa__fcf = guard(get_definition, func_ir, rabz__hyk.func)
                    if (bboa__fcf is not None and bboa__fcf.op == 'getattr' and
                        isinstance(typemap[bboa__fcf.value.name], types.
                        Array) and bboa__fcf.attr == 'astype'):
                        yxhr__bxs = True
                        continue
            if saved_array_analysis and sil__lrqd.name in lives and is_expr(
                rabz__hyk, 'getattr'
                ) and rabz__hyk.attr == 'shape' and is_array_typ(typemap[
                rabz__hyk.value.name]) and rabz__hyk.value.name not in lives:
                relcm__hkq = {udil__tquzm: qolux__rpok for qolux__rpok,
                    udil__tquzm in func_ir.blocks.items()}
                if block in relcm__hkq:
                    label = relcm__hkq[block]
                    jur__vkk = saved_array_analysis.get_equiv_set(label)
                    crws__cgh = jur__vkk.get_equiv_set(rabz__hyk.value)
                    if crws__cgh is not None:
                        for udil__tquzm in crws__cgh:
                            if udil__tquzm.endswith('#0'):
                                udil__tquzm = udil__tquzm[:-2]
                            if udil__tquzm in typemap and is_array_typ(typemap
                                [udil__tquzm]) and udil__tquzm in lives:
                                rabz__hyk.value = ir.Var(rabz__hyk.value.
                                    scope, udil__tquzm, rabz__hyk.value.loc)
                                yxhr__bxs = True
                                break
            if isinstance(rabz__hyk, ir.Var
                ) and sil__lrqd.name == rabz__hyk.name:
                yxhr__bxs = True
                continue
        if isinstance(stmt, ir.Del):
            if stmt.value not in lives:
                yxhr__bxs = True
                continue
        if isinstance(stmt, ir.SetItem):
            name = stmt.target.name
            if name not in lives_n_aliases:
                continue
        if type(stmt) in analysis.ir_extension_usedefs:
            nog__tabp = analysis.ir_extension_usedefs[type(stmt)]
            vqu__kayf, hectu__arcgb = nog__tabp(stmt)
            lives -= hectu__arcgb
            lives |= vqu__kayf
        else:
            lives |= {udil__tquzm.name for udil__tquzm in stmt.list_vars()}
            if isinstance(stmt, ir.Assign):
                dyl__ngjr = set()
                if isinstance(rabz__hyk, ir.Expr):
                    dyl__ngjr = {udil__tquzm.name for udil__tquzm in
                        rabz__hyk.list_vars()}
                if sil__lrqd.name not in dyl__ngjr:
                    lives.remove(sil__lrqd.name)
        vpvw__ppwm.append(stmt)
    vpvw__ppwm.reverse()
    block.body = vpvw__ppwm
    return yxhr__bxs


ir_utils.remove_dead_block = bodo_remove_dead_block


@infer_global(set)
class SetBuiltin(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        if args:
            layg__zmg, = args
            if isinstance(layg__zmg, types.IterableType):
                dtype = layg__zmg.iterator_type.yield_type
                if isinstance(dtype, types.Hashable
                    ) or dtype == numba.core.types.unicode_type:
                    return signature(types.Set(dtype), layg__zmg)
        else:
            return signature(types.Set(types.undefined))


def Set__init__(self, dtype, reflected=False):
    assert isinstance(dtype, (types.Hashable, types.Undefined)
        ) or dtype == numba.core.types.unicode_type
    self.dtype = dtype
    self.reflected = reflected
    joex__wccvy = 'reflected set' if reflected else 'set'
    name = '%s(%s)' % (joex__wccvy, self.dtype)
    super(types.Set, self).__init__(name=name)


types.Set.__init__ = Set__init__


@lower_builtin(operator.eq, types.UnicodeType, types.UnicodeType)
def eq_str(context, builder, sig, args):
    func = numba.cpython.unicode.unicode_eq(*sig.args)
    return context.compile_internal(builder, func, sig, args)


numba.parfors.parfor.push_call_vars = (lambda blocks, saved_globals,
    saved_getattrs, typemap, nested=False: None)


def maybe_literal(value):
    if isinstance(value, (list, dict, pytypes.FunctionType)):
        return
    if isinstance(value, tuple):
        try:
            return types.Tuple([literal(x) for x in value])
        except LiteralTypingError as iezc__rwqn:
            return
    try:
        return literal(value)
    except LiteralTypingError as iezc__rwqn:
        return


if _check_numba_change:
    lines = inspect.getsource(types.maybe_literal)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '8fb2fd93acf214b28e33e37d19dc2f7290a42792ec59b650553ac278854b5081':
        warnings.warn('types.maybe_literal has changed')
types.maybe_literal = maybe_literal
types.misc.maybe_literal = maybe_literal


def CacheImpl__init__(self, py_func):
    self._lineno = py_func.__code__.co_firstlineno
    try:
        rgyfi__okt = py_func.__qualname__
    except AttributeError as iezc__rwqn:
        rgyfi__okt = py_func.__name__
    vrn__erugx = inspect.getfile(py_func)
    for cls in self._locator_classes:
        qln__rby = cls.from_function(py_func, vrn__erugx)
        if qln__rby is not None:
            break
    else:
        raise RuntimeError(
            'cannot cache function %r: no locator available for file %r' %
            (rgyfi__okt, vrn__erugx))
    self._locator = qln__rby
    emnh__dgdes = inspect.getfile(py_func)
    hviji__tvgj = os.path.splitext(os.path.basename(emnh__dgdes))[0]
    if vrn__erugx.startswith('<ipython-'):
        moh__jqwlj = re.sub('(ipython-input)(-\\d+)(-[0-9a-fA-F]+)',
            '\\1\\3', hviji__tvgj, count=1)
        if moh__jqwlj == hviji__tvgj:
            warnings.warn(
                'Did not recognize ipython module name syntax. Caching might not work'
                )
        hviji__tvgj = moh__jqwlj
    bxyae__tjdtp = '%s.%s' % (hviji__tvgj, rgyfi__okt)
    tcu__tny = getattr(sys, 'abiflags', '')
    from bodo import __version__ as bodo_version
    self._filename_base = self.get_filename_base(bxyae__tjdtp, tcu__tny
        ) + 'bodo' + bodo_version


if _check_numba_change:
    lines = inspect.getsource(numba.core.caching._CacheImpl.__init__)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'b46d298146e3844e9eaeef29d36f5165ba4796c270ca50d2b35f9fcdc0fa032a':
        warnings.warn('numba.core.caching._CacheImpl.__init__ has changed')
numba.core.caching._CacheImpl.__init__ = CacheImpl__init__


def _analyze_broadcast(self, scope, equiv_set, loc, args, fn):
    from numba.parfors.array_analysis import ArrayAnalysis
    ewms__ryn = list(filter(lambda a: self._istuple(a.name), args))
    if len(ewms__ryn) == 2 and fn.__name__ == 'add':
        qjuff__nhmxk = self.typemap[ewms__ryn[0].name]
        sjtpf__fxw = self.typemap[ewms__ryn[1].name]
        if qjuff__nhmxk.count == 0:
            return ArrayAnalysis.AnalyzeResult(shape=equiv_set.get_shape(
                ewms__ryn[1]))
        if sjtpf__fxw.count == 0:
            return ArrayAnalysis.AnalyzeResult(shape=equiv_set.get_shape(
                ewms__ryn[0]))
        try:
            uobe__bcmw = [equiv_set.get_shape(x) for x in ewms__ryn]
            if None in uobe__bcmw:
                return None
            puzl__dqt = sum(uobe__bcmw, ())
            return ArrayAnalysis.AnalyzeResult(shape=puzl__dqt)
        except GuardException as iezc__rwqn:
            return None
    aow__ryv = list(filter(lambda a: self._isarray(a.name), args))
    require(len(aow__ryv) > 0)
    gfjca__spe = [x.name for x in aow__ryv]
    dazvg__btwn = [self.typemap[x.name].ndim for x in aow__ryv]
    lrdi__szka = max(dazvg__btwn)
    require(lrdi__szka > 0)
    uobe__bcmw = [equiv_set.get_shape(x) for x in aow__ryv]
    if any(a is None for a in uobe__bcmw):
        return ArrayAnalysis.AnalyzeResult(shape=aow__ryv[0], pre=self.
            _call_assert_equiv(scope, loc, equiv_set, aow__ryv))
    return self._broadcast_assert_shapes(scope, equiv_set, loc, uobe__bcmw,
        gfjca__spe)


if _check_numba_change:
    lines = inspect.getsource(numba.parfors.array_analysis.ArrayAnalysis.
        _analyze_broadcast)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '6c91fec038f56111338ea2b08f5f0e7f61ebdab1c81fb811fe26658cc354e40f':
        warnings.warn(
            'numba.parfors.array_analysis.ArrayAnalysis._analyze_broadcast has changed'
            )
numba.parfors.array_analysis.ArrayAnalysis._analyze_broadcast = (
    _analyze_broadcast)


def slice_size(self, index, dsize, equiv_set, scope, stmts):
    return None, None


numba.parfors.array_analysis.ArrayAnalysis.slice_size = slice_size


def convert_code_obj_to_function(code_obj, caller_ir):
    import bodo
    wcfpk__ajxtc = code_obj.code
    yslhb__ahgbq = len(wcfpk__ajxtc.co_freevars)
    qhyn__ibcml = wcfpk__ajxtc.co_freevars
    if code_obj.closure is not None:
        assert isinstance(code_obj.closure, ir.Var)
        jakc__aocxx, op = ir_utils.find_build_sequence(caller_ir, code_obj.
            closure)
        assert op == 'build_tuple'
        qhyn__ibcml = [udil__tquzm.name for udil__tquzm in jakc__aocxx]
    tla__oye = caller_ir.func_id.func.__globals__
    try:
        tla__oye = getattr(code_obj, 'globals', tla__oye)
    except KeyError as iezc__rwqn:
        pass
    msg = (
        "Inner function is using non-constant variable '{}' from outer function. Please pass as argument if possible. See https://docs.bodo.ai/latest/api_docs/udfs/."
        )
    hsslb__cit = []
    for x in qhyn__ibcml:
        try:
            zlhsy__pwond = caller_ir.get_definition(x)
        except KeyError as iezc__rwqn:
            raise bodo.utils.typing.BodoError(msg.format(x), loc=code_obj.loc)
        from numba.core.registry import CPUDispatcher
        if isinstance(zlhsy__pwond, (ir.Const, ir.Global, ir.FreeVar)):
            val = zlhsy__pwond.value
            if isinstance(val, str):
                val = "'{}'".format(val)
            if isinstance(val, pytypes.FunctionType):
                xysx__mqxqt = ir_utils.mk_unique_var('nested_func').replace('.'
                    , '_')
                tla__oye[xysx__mqxqt] = bodo.jit(distributed=False)(val)
                tla__oye[xysx__mqxqt].is_nested_func = True
                val = xysx__mqxqt
            if isinstance(val, CPUDispatcher):
                xysx__mqxqt = ir_utils.mk_unique_var('nested_func').replace('.'
                    , '_')
                tla__oye[xysx__mqxqt] = val
                val = xysx__mqxqt
            hsslb__cit.append(val)
        elif isinstance(zlhsy__pwond, ir.Expr
            ) and zlhsy__pwond.op == 'make_function':
            iqfzr__axw = convert_code_obj_to_function(zlhsy__pwond, caller_ir)
            xysx__mqxqt = ir_utils.mk_unique_var('nested_func').replace('.',
                '_')
            tla__oye[xysx__mqxqt] = bodo.jit(distributed=False)(iqfzr__axw)
            tla__oye[xysx__mqxqt].is_nested_func = True
            hsslb__cit.append(xysx__mqxqt)
        else:
            raise bodo.utils.typing.BodoError(msg.format(x), loc=code_obj.loc)
    mrj__qwqf = '\n'.join([('\tc_%d = %s' % (i, x)) for i, x in enumerate(
        hsslb__cit)])
    ean__npvqs = ','.join([('c_%d' % i) for i in range(yslhb__ahgbq)])
    hrefr__tkc = list(wcfpk__ajxtc.co_varnames)
    svnxq__fia = 0
    rmg__eovdu = wcfpk__ajxtc.co_argcount
    gcpns__tpfpv = caller_ir.get_definition(code_obj.defaults)
    if gcpns__tpfpv is not None:
        if isinstance(gcpns__tpfpv, tuple):
            d = [caller_ir.get_definition(x).value for x in gcpns__tpfpv]
            fklr__khuwi = tuple(d)
        else:
            d = [caller_ir.get_definition(x).value for x in gcpns__tpfpv.items]
            fklr__khuwi = tuple(d)
        svnxq__fia = len(fklr__khuwi)
    bttzq__nxzvt = rmg__eovdu - svnxq__fia
    kdk__vfuyw = ','.join([('%s' % hrefr__tkc[i]) for i in range(bttzq__nxzvt)]
        )
    if svnxq__fia:
        iihu__shs = [('%s = %s' % (hrefr__tkc[i + bttzq__nxzvt],
            fklr__khuwi[i])) for i in range(svnxq__fia)]
        kdk__vfuyw += ', '
        kdk__vfuyw += ', '.join(iihu__shs)
    return _create_function_from_code_obj(wcfpk__ajxtc, mrj__qwqf,
        kdk__vfuyw, ean__npvqs, tla__oye)


if _check_numba_change:
    lines = inspect.getsource(numba.core.ir_utils.convert_code_obj_to_function)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'b840769812418d589460e924a15477e83e7919aac8a3dcb0188ff447344aa8ac':
        warnings.warn(
            'numba.core.ir_utils.convert_code_obj_to_function has changed')
numba.core.ir_utils.convert_code_obj_to_function = convert_code_obj_to_function
numba.core.untyped_passes.convert_code_obj_to_function = (
    convert_code_obj_to_function)


def passmanager_run(self, state):
    from numba.core.compiler import _EarlyPipelineCompletion
    if not self.finalized:
        raise RuntimeError('Cannot run non-finalised pipeline')
    from numba.core.compiler_machinery import CompilerPass, _pass_registry
    import bodo
    for mkr__wyq, (kkbam__zabae, etdk__xms) in enumerate(self.passes):
        try:
            numba.core.tracing.event('-- %s' % etdk__xms)
            pyhyy__ywj = _pass_registry.get(kkbam__zabae).pass_inst
            if isinstance(pyhyy__ywj, CompilerPass):
                self._runPass(mkr__wyq, pyhyy__ywj, state)
            else:
                raise BaseException('Legacy pass in use')
        except _EarlyPipelineCompletion as e:
            raise e
        except bodo.utils.typing.BodoError as e:
            raise
        except Exception as e:
            if numba.core.config.DEVELOPER_MODE:
                from numba.core import utils
                if utils.use_new_style_errors() and not isinstance(e,
                    errors.NumbaError):
                    raise e
                msg = 'Failed in %s mode pipeline (step: %s)' % (self.
                    pipeline_name, etdk__xms)
                zzh__wawzx = self._patch_error(msg, e)
                raise zzh__wawzx
            else:
                raise e


if _check_numba_change:
    lines = inspect.getsource(numba.core.compiler_machinery.PassManager.run)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '43505782e15e690fd2d7e53ea716543bec37aa0633502956864edf649e790cdb':
        warnings.warn(
            'numba.core.compiler_machinery.PassManager.run has changed')
numba.core.compiler_machinery.PassManager.run = passmanager_run
if _check_numba_change:
    lines = inspect.getsource(numba.np.ufunc.parallel._launch_threads)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'a57ef28c4168fdd436a5513bba4351ebc6d9fba76c5819f44046431a79b9030f':
        warnings.warn('numba.np.ufunc.parallel._launch_threads has changed')
numba.np.ufunc.parallel._launch_threads = lambda : None


def get_reduce_nodes(reduction_node, nodes, func_ir):
    vzorp__ovf = None
    hectu__arcgb = {}

    def lookup(var, already_seen, varonly=True):
        val = hectu__arcgb.get(var.name, None)
        if isinstance(val, ir.Var):
            if val.name in already_seen:
                return var
            already_seen.add(val.name)
            return lookup(val, already_seen, varonly)
        else:
            return var if varonly or val is None else val
    name = reduction_node.name
    tezb__flas = reduction_node.unversioned_name
    for i, stmt in enumerate(nodes):
        sil__lrqd = stmt.target
        rabz__hyk = stmt.value
        hectu__arcgb[sil__lrqd.name] = rabz__hyk
        if isinstance(rabz__hyk, ir.Var) and rabz__hyk.name in hectu__arcgb:
            rabz__hyk = lookup(rabz__hyk, set())
        if isinstance(rabz__hyk, ir.Expr):
            nqewl__ttlb = set(lookup(udil__tquzm, set(), True).name for
                udil__tquzm in rabz__hyk.list_vars())
            if name in nqewl__ttlb:
                args = [(x.name, lookup(x, set(), True)) for x in
                    get_expr_args(rabz__hyk)]
                jrawv__bqnhx = [x for x, davuq__unns in args if davuq__unns
                    .name != name]
                args = [(x, davuq__unns) for x, davuq__unns in args if x !=
                    davuq__unns.name]
                rdreb__vket = dict(args)
                if len(jrawv__bqnhx) == 1:
                    rdreb__vket[jrawv__bqnhx[0]] = ir.Var(sil__lrqd.scope, 
                        name + '#init', sil__lrqd.loc)
                replace_vars_inner(rabz__hyk, rdreb__vket)
                vzorp__ovf = nodes[i:]
                break
    return vzorp__ovf


if _check_numba_change:
    lines = inspect.getsource(numba.parfors.parfor.get_reduce_nodes)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'a05b52aff9cb02e595a510cd34e973857303a71097fc5530567cb70ca183ef3b':
        warnings.warn('numba.parfors.parfor.get_reduce_nodes has changed')
numba.parfors.parfor.get_reduce_nodes = get_reduce_nodes


def _can_reorder_stmts(stmt, next_stmt, func_ir, call_table, alias_map,
    arg_aliases):
    from numba.parfors.parfor import Parfor, expand_aliases, is_assert_equiv
    if isinstance(stmt, Parfor) and not isinstance(next_stmt, Parfor
        ) and not isinstance(next_stmt, ir.Print) and (not isinstance(
        next_stmt, ir.Assign) or has_no_side_effect(next_stmt.value, set(),
        call_table) or guard(is_assert_equiv, func_ir, next_stmt.value)):
        jhsbh__gqdx = expand_aliases({udil__tquzm.name for udil__tquzm in
            stmt.list_vars()}, alias_map, arg_aliases)
        vvp__rjna = expand_aliases(get_parfor_writes(stmt, func_ir),
            alias_map, arg_aliases)
        nohk__wepxi = expand_aliases({udil__tquzm.name for udil__tquzm in
            next_stmt.list_vars()}, alias_map, arg_aliases)
        efnng__jfg = expand_aliases(get_stmt_writes(next_stmt, func_ir),
            alias_map, arg_aliases)
        if len(vvp__rjna & nohk__wepxi | efnng__jfg & jhsbh__gqdx) == 0:
            return True
    return False


if _check_numba_change:
    lines = inspect.getsource(numba.parfors.parfor._can_reorder_stmts)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '18caa9a01b21ab92b4f79f164cfdbc8574f15ea29deedf7bafdf9b0e755d777c':
        warnings.warn('numba.parfors.parfor._can_reorder_stmts has changed')
numba.parfors.parfor._can_reorder_stmts = _can_reorder_stmts


def get_parfor_writes(parfor, func_ir):
    from numba.parfors.parfor import Parfor
    assert isinstance(parfor, Parfor)
    qbfy__eaoqt = set()
    blocks = parfor.loop_body.copy()
    blocks[-1] = parfor.init_block
    for block in blocks.values():
        for stmt in block.body:
            qbfy__eaoqt.update(get_stmt_writes(stmt, func_ir))
            if isinstance(stmt, Parfor):
                qbfy__eaoqt.update(get_parfor_writes(stmt, func_ir))
    return qbfy__eaoqt


if _check_numba_change:
    lines = inspect.getsource(numba.parfors.parfor.get_parfor_writes)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'a7b29cd76832b6f6f1f2d2397ec0678c1409b57a6eab588bffd344b775b1546f':
        warnings.warn('numba.parfors.parfor.get_parfor_writes has changed')


def get_stmt_writes(stmt, func_ir):
    import bodo
    from bodo.utils.utils import is_call_assign
    qbfy__eaoqt = set()
    if isinstance(stmt, (ir.Assign, ir.SetItem, ir.StaticSetItem)):
        qbfy__eaoqt.add(stmt.target.name)
    if isinstance(stmt, (bodo.ir.csv_ext.CsvReader, bodo.ir.parquet_ext.
        ParquetReader)):
        qbfy__eaoqt = {udil__tquzm.name for udil__tquzm in stmt.out_vars}
    if isinstance(stmt, (bodo.ir.join.Join, bodo.ir.aggregate.Aggregate)):
        qbfy__eaoqt = {udil__tquzm.name for udil__tquzm in stmt.
            get_live_out_vars()}
    if isinstance(stmt, bodo.ir.sort.Sort):
        if not stmt.inplace:
            qbfy__eaoqt.update({udil__tquzm.name for udil__tquzm in stmt.
                get_live_out_vars()})
    if is_call_assign(stmt):
        pez__wvvw = guard(find_callname, func_ir, stmt.value)
        if pez__wvvw in (('setitem_str_arr_ptr', 'bodo.libs.str_arr_ext'),
            ('setna', 'bodo.libs.array_kernels'), (
            'str_arr_item_to_numeric', 'bodo.libs.str_arr_ext'), (
            'str_arr_setitem_int_to_str', 'bodo.libs.str_arr_ext'), (
            'str_arr_setitem_NA_str', 'bodo.libs.str_arr_ext'), (
            'str_arr_set_not_na', 'bodo.libs.str_arr_ext'), (
            'get_str_arr_item_copy', 'bodo.libs.str_arr_ext'), (
            'copy_array_element', 'bodo.libs.array_kernels'), (
            'set_bit_to_arr', 'bodo.libs.int_arr_ext'), (
            'tuple_list_to_array', 'bodo.utils.utils')):
            qbfy__eaoqt.add(stmt.value.args[0].name)
        if pez__wvvw == ('generate_table_nbytes', 'bodo.utils.table_utils'):
            qbfy__eaoqt.add(stmt.value.args[1].name)
    return qbfy__eaoqt


if _check_numba_change:
    lines = inspect.getsource(numba.core.ir_utils.get_stmt_writes)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '1a7a80b64c9a0eb27e99dc8eaae187bde379d4da0b74c84fbf87296d87939974':
        warnings.warn('numba.core.ir_utils.get_stmt_writes has changed')


def patch_message(self, new_message):
    self.msg = new_message
    self.args = (new_message,) + self.args[1:]


if _check_numba_change:
    lines = inspect.getsource(numba.core.errors.NumbaError.patch_message)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'ed189a428a7305837e76573596d767b6e840e99f75c05af6941192e0214fa899':
        warnings.warn('numba.core.errors.NumbaError.patch_message has changed')
numba.core.errors.NumbaError.patch_message = patch_message


def add_context(self, msg):
    if numba.core.config.DEVELOPER_MODE:
        self.contexts.append(msg)
        wztfa__vcc = _termcolor.errmsg('{0}') + _termcolor.filename(
            'During: {1}')
        uqyo__uynab = wztfa__vcc.format(self, msg)
        self.args = uqyo__uynab,
    else:
        wztfa__vcc = _termcolor.errmsg('{0}')
        uqyo__uynab = wztfa__vcc.format(self)
        self.args = uqyo__uynab,
    return self


if _check_numba_change:
    lines = inspect.getsource(numba.core.errors.NumbaError.add_context)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '6a388d87788f8432c2152ac55ca9acaa94dbc3b55be973b2cf22dd4ee7179ab8':
        warnings.warn('numba.core.errors.NumbaError.add_context has changed')
numba.core.errors.NumbaError.add_context = add_context


def _get_dist_spec_from_options(spec, **options):
    from bodo.transforms.distributed_analysis import Distribution
    dist_spec = {}
    if 'distributed' in options:
        for nbdnb__rlukl in options['distributed']:
            dist_spec[nbdnb__rlukl] = Distribution.OneD_Var
    if 'distributed_block' in options:
        for nbdnb__rlukl in options['distributed_block']:
            dist_spec[nbdnb__rlukl] = Distribution.OneD
    return dist_spec


def register_class_type(cls, spec, class_ctor, builder, **options):
    import typing as pt
    from numba.core.typing.asnumbatype import as_numba_type
    import bodo
    dist_spec = _get_dist_spec_from_options(spec, **options)
    rdcu__usjzy = options.get('returns_maybe_distributed', True)
    if spec is None:
        spec = OrderedDict()
    elif isinstance(spec, Sequence):
        spec = OrderedDict(spec)
    for attr, ppio__pxwje in pt.get_type_hints(cls).items():
        if attr not in spec:
            spec[attr] = as_numba_type(ppio__pxwje)
    jitclass_base._validate_spec(spec)
    spec = jitclass_base._fix_up_private_attr(cls.__name__, spec)
    azh__gpjh = {}
    for fug__qxqvh in reversed(inspect.getmro(cls)):
        azh__gpjh.update(fug__qxqvh.__dict__)
    xzcme__vter, shjds__pcq, pbcah__vqghq, cic__jdor = {}, {}, {}, {}
    for qolux__rpok, udil__tquzm in azh__gpjh.items():
        if isinstance(udil__tquzm, pytypes.FunctionType):
            xzcme__vter[qolux__rpok] = udil__tquzm
        elif isinstance(udil__tquzm, property):
            shjds__pcq[qolux__rpok] = udil__tquzm
        elif isinstance(udil__tquzm, staticmethod):
            pbcah__vqghq[qolux__rpok] = udil__tquzm
        else:
            cic__jdor[qolux__rpok] = udil__tquzm
    hengo__ngiyl = (set(xzcme__vter) | set(shjds__pcq) | set(pbcah__vqghq)
        ) & set(spec)
    if hengo__ngiyl:
        raise NameError('name shadowing: {0}'.format(', '.join(hengo__ngiyl)))
    xvd__oemlf = cic__jdor.pop('__doc__', '')
    jitclass_base._drop_ignored_attrs(cic__jdor)
    if cic__jdor:
        msg = 'class members are not yet supported: {0}'
        mwfht__avglb = ', '.join(cic__jdor.keys())
        raise TypeError(msg.format(mwfht__avglb))
    for qolux__rpok, udil__tquzm in shjds__pcq.items():
        if udil__tquzm.fdel is not None:
            raise TypeError('deleter is not supported: {0}'.format(qolux__rpok)
                )
    jit_methods = {qolux__rpok: bodo.jit(returns_maybe_distributed=
        rdcu__usjzy)(udil__tquzm) for qolux__rpok, udil__tquzm in
        xzcme__vter.items()}
    jit_props = {}
    for qolux__rpok, udil__tquzm in shjds__pcq.items():
        ajw__kxrqe = {}
        if udil__tquzm.fget:
            ajw__kxrqe['get'] = bodo.jit(udil__tquzm.fget)
        if udil__tquzm.fset:
            ajw__kxrqe['set'] = bodo.jit(udil__tquzm.fset)
        jit_props[qolux__rpok] = ajw__kxrqe
    jit_static_methods = {qolux__rpok: bodo.jit(udil__tquzm.__func__) for 
        qolux__rpok, udil__tquzm in pbcah__vqghq.items()}
    hcn__jydpc = class_ctor(cls, jitclass_base.ConstructorTemplate, spec,
        jit_methods, jit_props, jit_static_methods, dist_spec)
    roy__khtt = dict(class_type=hcn__jydpc, __doc__=xvd__oemlf)
    roy__khtt.update(jit_static_methods)
    cls = jitclass_base.JitClassType(cls.__name__, (cls,), roy__khtt)
    typingctx = numba.core.registry.cpu_target.typing_context
    typingctx.insert_global(cls, hcn__jydpc)
    targetctx = numba.core.registry.cpu_target.target_context
    builder(hcn__jydpc, typingctx, targetctx).register()
    as_numba_type.register(cls, hcn__jydpc.instance_type)
    return cls


if _check_numba_change:
    lines = inspect.getsource(jitclass_base.register_class_type)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '005e6e2e89a47f77a19ba86305565050d4dbc2412fc4717395adf2da348671a9':
        warnings.warn('jitclass_base.register_class_type has changed')
jitclass_base.register_class_type = register_class_type


def ClassType__init__(self, class_def, ctor_template_cls, struct,
    jit_methods, jit_props, jit_static_methods, dist_spec=None):
    if dist_spec is None:
        dist_spec = {}
    self.class_name = class_def.__name__
    self.class_doc = class_def.__doc__
    self._ctor_template_class = ctor_template_cls
    self.jit_methods = jit_methods
    self.jit_props = jit_props
    self.jit_static_methods = jit_static_methods
    self.struct = struct
    self.dist_spec = dist_spec
    jctha__xsoiw = ','.join('{0}:{1}'.format(qolux__rpok, udil__tquzm) for 
        qolux__rpok, udil__tquzm in struct.items())
    dtk__cpc = ','.join('{0}:{1}'.format(qolux__rpok, udil__tquzm) for 
        qolux__rpok, udil__tquzm in dist_spec.items())
    name = '{0}.{1}#{2:x}<{3}><{4}>'.format(self.name_prefix, self.
        class_name, id(self), jctha__xsoiw, dtk__cpc)
    super(types.misc.ClassType, self).__init__(name)


if _check_numba_change:
    lines = inspect.getsource(types.misc.ClassType.__init__)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '2b848ea82946c88f540e81f93ba95dfa7cd66045d944152a337fe2fc43451c30':
        warnings.warn('types.misc.ClassType.__init__ has changed')
types.misc.ClassType.__init__ = ClassType__init__


def jitclass(cls_or_spec=None, spec=None, **options):
    if cls_or_spec is not None and spec is None and not isinstance(cls_or_spec,
        type):
        spec = cls_or_spec
        cls_or_spec = None

    def wrap(cls):
        if numba.core.config.DISABLE_JIT:
            return cls
        else:
            from numba.experimental.jitclass.base import ClassBuilder
            return register_class_type(cls, spec, types.ClassType,
                ClassBuilder, **options)
    if cls_or_spec is None:
        return wrap
    else:
        return wrap(cls_or_spec)


if _check_numba_change:
    lines = inspect.getsource(jitclass_decorators.jitclass)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '265f1953ee5881d1a5d90238d3c932cd300732e41495657e65bf51e59f7f4af5':
        warnings.warn('jitclass_decorators.jitclass has changed')


def CallConstraint_resolve(self, typeinfer, typevars, fnty):
    assert fnty
    context = typeinfer.context
    icwvu__nrkys = numba.core.typeinfer.fold_arg_vars(typevars, self.args,
        self.vararg, self.kws)
    if icwvu__nrkys is None:
        return
    uram__tqfot, tajn__sddu = icwvu__nrkys
    for a in itertools.chain(uram__tqfot, tajn__sddu.values()):
        if not a.is_precise() and not isinstance(a, types.Array):
            return
    if isinstance(fnty, types.TypeRef):
        fnty = fnty.instance_type
    try:
        sig = typeinfer.resolve_call(fnty, uram__tqfot, tajn__sddu)
    except ForceLiteralArg as e:
        qxjno__vhlt = (fnty.this,) + tuple(self.args) if isinstance(fnty,
            types.BoundFunction) else self.args
        folded = e.fold_arguments(qxjno__vhlt, self.kws)
        yvox__cqes = set()
        zpbl__hwt = set()
        wbk__ktgk = {}
        for mkr__wyq in e.requested_args:
            xgp__orirn = typeinfer.func_ir.get_definition(folded[mkr__wyq])
            if isinstance(xgp__orirn, ir.Arg):
                yvox__cqes.add(xgp__orirn.index)
                if xgp__orirn.index in e.file_infos:
                    wbk__ktgk[xgp__orirn.index] = e.file_infos[xgp__orirn.index
                        ]
            else:
                zpbl__hwt.add(mkr__wyq)
        if zpbl__hwt:
            raise TypingError('Cannot request literal type.', loc=self.loc)
        elif yvox__cqes:
            raise ForceLiteralArg(yvox__cqes, loc=self.loc, file_infos=
                wbk__ktgk)
    if sig is None:
        hvk__gvkp = 'Invalid use of {0} with parameters ({1})'
        args = [str(a) for a in uram__tqfot]
        args += [('%s=%s' % (qolux__rpok, udil__tquzm)) for qolux__rpok,
            udil__tquzm in sorted(tajn__sddu.items())]
        njbpe__buj = hvk__gvkp.format(fnty, ', '.join(map(str, args)))
        neee__oakrl = context.explain_function_type(fnty)
        msg = '\n'.join([njbpe__buj, neee__oakrl])
        raise TypingError(msg)
    typeinfer.add_type(self.target, sig.return_type, loc=self.loc)
    if isinstance(fnty, types.BoundFunction
        ) and sig.recvr is not None and sig.recvr != fnty.this:
        goaz__iniay = context.unify_pairs(sig.recvr, fnty.this)
        if goaz__iniay is None and fnty.this.is_precise(
            ) and sig.recvr.is_precise():
            msg = 'Cannot refine type {} to {}'.format(sig.recvr, fnty.this)
            raise TypingError(msg, loc=self.loc)
        if goaz__iniay is not None and goaz__iniay.is_precise():
            zcz__wer = fnty.copy(this=goaz__iniay)
            typeinfer.propagate_refined_type(self.func, zcz__wer)
    if not sig.return_type.is_precise():
        target = typevars[self.target]
        if target.defined:
            zwh__bklxf = target.getone()
            if context.unify_pairs(zwh__bklxf, sig.return_type) == zwh__bklxf:
                sig = sig.replace(return_type=zwh__bklxf)
    self.signature = sig
    self._add_refine_map(typeinfer, typevars, sig)


if _check_numba_change:
    lines = inspect.getsource(numba.core.typeinfer.CallConstraint.resolve)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'c78cd8ffc64b836a6a2ddf0362d481b52b9d380c5249920a87ff4da052ce081f':
        warnings.warn('numba.core.typeinfer.CallConstraint.resolve has changed'
            )
numba.core.typeinfer.CallConstraint.resolve = CallConstraint_resolve


def ForceLiteralArg__init__(self, arg_indices, fold_arguments=None, loc=
    None, file_infos=None):
    super(ForceLiteralArg, self).__init__(
        'Pseudo-exception to force literal arguments in the dispatcher',
        loc=loc)
    self.requested_args = frozenset(arg_indices)
    self.fold_arguments = fold_arguments
    if file_infos is None:
        self.file_infos = {}
    else:
        self.file_infos = file_infos


if _check_numba_change:
    lines = inspect.getsource(numba.core.errors.ForceLiteralArg.__init__)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'b241d5e36a4cf7f4c73a7ad3238693612926606c7a278cad1978070b82fb55ef':
        warnings.warn('numba.core.errors.ForceLiteralArg.__init__ has changed')
numba.core.errors.ForceLiteralArg.__init__ = ForceLiteralArg__init__


def ForceLiteralArg_bind_fold_arguments(self, fold_arguments):
    e = ForceLiteralArg(self.requested_args, fold_arguments, loc=self.loc,
        file_infos=self.file_infos)
    return numba.core.utils.chain_exception(e, self)


if _check_numba_change:
    lines = inspect.getsource(numba.core.errors.ForceLiteralArg.
        bind_fold_arguments)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '1e93cca558f7c604a47214a8f2ec33ee994104cb3e5051166f16d7cc9315141d':
        warnings.warn(
            'numba.core.errors.ForceLiteralArg.bind_fold_arguments has changed'
            )
numba.core.errors.ForceLiteralArg.bind_fold_arguments = (
    ForceLiteralArg_bind_fold_arguments)


def ForceLiteralArg_combine(self, other):
    if not isinstance(other, ForceLiteralArg):
        ntrth__wocw = '*other* must be a {} but got a {} instead'
        raise TypeError(ntrth__wocw.format(ForceLiteralArg, type(other)))
    return ForceLiteralArg(self.requested_args | other.requested_args,
        file_infos={**self.file_infos, **other.file_infos})


if _check_numba_change:
    lines = inspect.getsource(numba.core.errors.ForceLiteralArg.combine)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '49bf06612776f5d755c1c7d1c5eb91831a57665a8fed88b5651935f3bf33e899':
        warnings.warn('numba.core.errors.ForceLiteralArg.combine has changed')
numba.core.errors.ForceLiteralArg.combine = ForceLiteralArg_combine


def _get_global_type(self, gv):
    from bodo.utils.typing import FunctionLiteral
    ty = self._lookup_global(gv)
    if ty is not None:
        return ty
    if isinstance(gv, pytypes.ModuleType):
        return types.Module(gv)
    if isinstance(gv, pytypes.FunctionType):
        return FunctionLiteral(gv)


if _check_numba_change:
    lines = inspect.getsource(numba.core.typing.context.BaseContext.
        _get_global_type)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '8ffe6b81175d1eecd62a37639b5005514b4477d88f35f5b5395041ac8c945a4a':
        warnings.warn(
            'numba.core.typing.context.BaseContext._get_global_type has changed'
            )
numba.core.typing.context.BaseContext._get_global_type = _get_global_type


def _legalize_args(self, func_ir, args, kwargs, loc, func_globals,
    func_closures):
    from numba.core import sigutils
    from bodo.utils.transform import get_const_value_inner
    if args:
        raise errors.CompilerError(
            "objectmode context doesn't take any positional arguments")
    yzyi__hmq = {}

    def report_error(varname, msg, loc):
        raise errors.CompilerError(
            f'Error handling objmode argument {varname!r}. {msg}', loc=loc)
    for qolux__rpok, udil__tquzm in kwargs.items():
        hboj__mxdz = None
        try:
            pkia__fvjy = ir.Var(ir.Scope(None, loc), ir_utils.mk_unique_var
                ('dummy'), loc)
            func_ir._definitions[pkia__fvjy.name] = [udil__tquzm]
            hboj__mxdz = get_const_value_inner(func_ir, pkia__fvjy)
            func_ir._definitions.pop(pkia__fvjy.name)
            if isinstance(hboj__mxdz, str):
                hboj__mxdz = sigutils._parse_signature_string(hboj__mxdz)
            if isinstance(hboj__mxdz, types.abstract._TypeMetaclass):
                raise BodoError(
                    f"""objmode type annotations require full data types, not just data type classes. For example, 'bodo.DataFrameType((bodo.float64[::1],), bodo.RangeIndexType(), ('A',))' is a valid data type but 'bodo.DataFrameType' is not.
Variable {qolux__rpok} is annotated as type class {hboj__mxdz}."""
                    )
            assert isinstance(hboj__mxdz, types.Type)
            if isinstance(hboj__mxdz, (types.List, types.Set)):
                hboj__mxdz = hboj__mxdz.copy(reflected=False)
            yzyi__hmq[qolux__rpok] = hboj__mxdz
        except BodoError as iezc__rwqn:
            raise
        except:
            msg = (
                'The value must be a compile-time constant either as a non-local variable or an expression that refers to a Bodo type.'
                )
            if isinstance(hboj__mxdz, ir.UndefinedType):
                msg = f'not defined.'
                if isinstance(udil__tquzm, ir.Global):
                    msg = f'Global {udil__tquzm.name!r} is not defined.'
                if isinstance(udil__tquzm, ir.FreeVar):
                    msg = f'Freevar {udil__tquzm.name!r} is not defined.'
            if isinstance(udil__tquzm, ir.Expr
                ) and udil__tquzm.op == 'getattr':
                msg = 'Getattr cannot be resolved at compile-time.'
            report_error(varname=qolux__rpok, msg=msg, loc=loc)
    for name, typ in yzyi__hmq.items():
        self._legalize_arg_type(name, typ, loc)
    return yzyi__hmq


if _check_numba_change:
    lines = inspect.getsource(numba.core.withcontexts._ObjModeContextType.
        _legalize_args)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '867c9ba7f1bcf438be56c38e26906bb551f59a99f853a9f68b71208b107c880e':
        warnings.warn(
            'numba.core.withcontexts._ObjModeContextType._legalize_args has changed'
            )
numba.core.withcontexts._ObjModeContextType._legalize_args = _legalize_args


def op_FORMAT_VALUE_byteflow(self, state, inst):
    flags = inst.arg
    if flags & 3 != 0:
        msg = 'str/repr/ascii conversion in f-strings not supported yet'
        raise errors.UnsupportedError(msg, loc=self.get_debug_loc(inst.lineno))
    format_spec = None
    if flags & 4 == 4:
        format_spec = state.pop()
    value = state.pop()
    fmtvar = state.make_temp()
    res = state.make_temp()
    state.append(inst, value=value, res=res, fmtvar=fmtvar, format_spec=
        format_spec)
    state.push(res)


def op_BUILD_STRING_byteflow(self, state, inst):
    ftyf__luvsa = inst.arg
    assert ftyf__luvsa > 0, 'invalid BUILD_STRING count'
    strings = list(reversed([state.pop() for _ in range(ftyf__luvsa)]))
    tmps = [state.make_temp() for _ in range(ftyf__luvsa - 1)]
    state.append(inst, strings=strings, tmps=tmps)
    state.push(tmps[-1])


numba.core.byteflow.TraceRunner.op_FORMAT_VALUE = op_FORMAT_VALUE_byteflow
numba.core.byteflow.TraceRunner.op_BUILD_STRING = op_BUILD_STRING_byteflow


def op_FORMAT_VALUE_interpreter(self, inst, value, res, fmtvar, format_spec):
    value = self.get(value)
    hdt__bfon = ir.Global('format', format, loc=self.loc)
    self.store(value=hdt__bfon, name=fmtvar)
    args = (value, self.get(format_spec)) if format_spec else (value,)
    fjnt__yxouo = ir.Expr.call(self.get(fmtvar), args, (), loc=self.loc)
    self.store(value=fjnt__yxouo, name=res)


def op_BUILD_STRING_interpreter(self, inst, strings, tmps):
    ftyf__luvsa = inst.arg
    assert ftyf__luvsa > 0, 'invalid BUILD_STRING count'
    tos__byrlm = self.get(strings[0])
    for other, zgd__wnxiz in zip(strings[1:], tmps):
        other = self.get(other)
        idea__ggdyg = ir.Expr.binop(operator.add, lhs=tos__byrlm, rhs=other,
            loc=self.loc)
        self.store(idea__ggdyg, zgd__wnxiz)
        tos__byrlm = self.get(zgd__wnxiz)


numba.core.interpreter.Interpreter.op_FORMAT_VALUE = (
    op_FORMAT_VALUE_interpreter)
numba.core.interpreter.Interpreter.op_BUILD_STRING = (
    op_BUILD_STRING_interpreter)


def object_hasattr_string(self, obj, attr):
    from llvmlite import ir as lir
    qkpc__dpbuj = self.context.insert_const_string(self.module, attr)
    fnty = lir.FunctionType(lir.IntType(32), [self.pyobj, self.cstring])
    fn = self._get_function(fnty, name='PyObject_HasAttrString')
    return self.builder.call(fn, [obj, qkpc__dpbuj])


numba.core.pythonapi.PythonAPI.object_hasattr_string = object_hasattr_string


def _created_inlined_var_name(function_name, var_name):
    muymh__mpl = mk_unique_var(f'{var_name}')
    elfu__xnlvq = muymh__mpl.replace('<', '_').replace('>', '_')
    elfu__xnlvq = elfu__xnlvq.replace('.', '_').replace('$', '_v')
    return elfu__xnlvq


if _check_numba_change:
    lines = inspect.getsource(numba.core.inline_closurecall.
        _created_inlined_var_name)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '0d91aac55cd0243e58809afe9d252562f9ae2899cde1112cc01a46804e01821e':
        warnings.warn(
            'numba.core.inline_closurecall._created_inlined_var_name has changed'
            )
numba.core.inline_closurecall._created_inlined_var_name = (
    _created_inlined_var_name)


def resolve_number___call__(self, classty):
    import numpy as np
    from numba.core.typing.templates import make_callable_template
    import bodo
    ty = classty.instance_type
    if isinstance(ty, types.NPDatetime):

        def typer(val1, val2):
            bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(val1,
                'numpy.datetime64')
            if (val1 == bodo.hiframes.pd_timestamp_ext.
                pd_timestamp_tz_naive_type):
                if not is_overload_constant_str(val2):
                    raise_bodo_error(
                        "datetime64(): 'units' must be a 'str' specifying 'ns'"
                        )
                ldqpm__snepl = get_overload_const_str(val2)
                if ldqpm__snepl != 'ns':
                    raise BodoError("datetime64(): 'units' must be 'ns'")
                return types.NPDatetime('ns')
    else:

        def typer(val):
            if isinstance(val, (types.BaseTuple, types.Sequence)):
                fnty = self.context.resolve_value_type(np.array)
                sig = fnty.get_call_type(self.context, (val, types.DType(ty
                    )), {})
                return sig.return_type
            elif isinstance(val, (types.Number, types.Boolean, types.
                IntEnumMember)):
                return ty
            elif val == types.unicode_type:
                return ty
            elif isinstance(val, (types.NPDatetime, types.NPTimedelta)):
                if ty.bitwidth == 64:
                    return ty
                else:
                    msg = (
                        f'Cannot cast {val} to {ty} as {ty} is not 64 bits wide.'
                        )
                    raise errors.TypingError(msg)
            elif isinstance(val, types.Array
                ) and val.ndim == 0 and val.dtype == ty:
                return ty
            else:
                msg = f'Casting {val} to {ty} directly is unsupported.'
                if isinstance(val, types.Array):
                    msg += f" Try doing '<array>.astype(np.{ty})' instead"
                raise errors.TypingError(msg)
    return types.Function(make_callable_template(key=ty, typer=typer))


if _check_numba_change:
    lines = inspect.getsource(numba.core.typing.builtins.
        NumberClassAttribute.resolve___call__)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'fdaf0c7d0820130481bb2bd922985257b9281b670f0bafffe10e51cabf0d5081':
        warnings.warn(
            'numba.core.typing.builtins.NumberClassAttribute.resolve___call__ has changed'
            )
numba.core.typing.builtins.NumberClassAttribute.resolve___call__ = (
    resolve_number___call__)


def on_assign(self, states, assign):
    if assign.target.name == states['varname']:
        scope = states['scope']
        dija__vrurf = states['defmap']
        if len(dija__vrurf) == 0:
            dnpbw__coidf = assign.target
            numba.core.ssa._logger.debug('first assign: %s', dnpbw__coidf)
            if dnpbw__coidf.name not in scope.localvars:
                dnpbw__coidf = scope.define(assign.target.name, loc=assign.loc)
        else:
            dnpbw__coidf = scope.redefine(assign.target.name, loc=assign.loc)
        assign = ir.Assign(target=dnpbw__coidf, value=assign.value, loc=
            assign.loc)
        dija__vrurf[states['label']].append(assign)
    return assign


if _check_numba_change:
    lines = inspect.getsource(numba.core.ssa._FreshVarHandler.on_assign)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '922c4f9807455f81600b794bbab36f9c6edfecfa83fda877bf85f465db7865e8':
        warnings.warn('_FreshVarHandler on_assign has changed')
numba.core.ssa._FreshVarHandler.on_assign = on_assign


def get_np_ufunc_typ_lst(func):
    from numba.core import typing
    rgre__uqzpb = []
    for qolux__rpok, udil__tquzm in typing.npydecl.registry.globals:
        if qolux__rpok == func:
            rgre__uqzpb.append(udil__tquzm)
    for qolux__rpok, udil__tquzm in typing.templates.builtin_registry.globals:
        if qolux__rpok == func:
            rgre__uqzpb.append(udil__tquzm)
    if len(rgre__uqzpb) == 0:
        raise RuntimeError('type for func ', func, ' not found')
    return rgre__uqzpb


def canonicalize_array_math(func_ir, typemap, calltypes, typingctx):
    import numpy
    from numba.core.ir_utils import arr_math, find_topo_order, mk_unique_var
    blocks = func_ir.blocks
    bbzkj__upgfx = {}
    ntdrx__udt = find_topo_order(blocks)
    qyil__jwkm = {}
    for label in ntdrx__udt:
        block = blocks[label]
        vpvw__ppwm = []
        for stmt in block.body:
            if isinstance(stmt, ir.Assign) and isinstance(stmt.value, ir.Expr):
                sil__lrqd = stmt.target.name
                rabz__hyk = stmt.value
                if (rabz__hyk.op == 'getattr' and rabz__hyk.attr in
                    arr_math and isinstance(typemap[rabz__hyk.value.name],
                    types.npytypes.Array)):
                    rabz__hyk = stmt.value
                    lcpqf__gtow = rabz__hyk.value
                    bbzkj__upgfx[sil__lrqd] = lcpqf__gtow
                    scope = lcpqf__gtow.scope
                    loc = lcpqf__gtow.loc
                    ujd__glvl = ir.Var(scope, mk_unique_var('$np_g_var'), loc)
                    typemap[ujd__glvl.name] = types.misc.Module(numpy)
                    ypmee__ofsz = ir.Global('np', numpy, loc)
                    gdos__spbwg = ir.Assign(ypmee__ofsz, ujd__glvl, loc)
                    rabz__hyk.value = ujd__glvl
                    vpvw__ppwm.append(gdos__spbwg)
                    func_ir._definitions[ujd__glvl.name] = [ypmee__ofsz]
                    func = getattr(numpy, rabz__hyk.attr)
                    abkis__gree = get_np_ufunc_typ_lst(func)
                    qyil__jwkm[sil__lrqd] = abkis__gree
                if (rabz__hyk.op == 'call' and rabz__hyk.func.name in
                    bbzkj__upgfx):
                    lcpqf__gtow = bbzkj__upgfx[rabz__hyk.func.name]
                    npkl__gqukr = calltypes.pop(rabz__hyk)
                    voplx__jxa = npkl__gqukr.args[:len(rabz__hyk.args)]
                    orlt__qpabu = {name: typemap[udil__tquzm.name] for name,
                        udil__tquzm in rabz__hyk.kws}
                    dfy__bhqat = qyil__jwkm[rabz__hyk.func.name]
                    utr__uche = None
                    for snk__cww in dfy__bhqat:
                        try:
                            utr__uche = snk__cww.get_call_type(typingctx, [
                                typemap[lcpqf__gtow.name]] + list(
                                voplx__jxa), orlt__qpabu)
                            typemap.pop(rabz__hyk.func.name)
                            typemap[rabz__hyk.func.name] = snk__cww
                            calltypes[rabz__hyk] = utr__uche
                            break
                        except Exception as iezc__rwqn:
                            pass
                    if utr__uche is None:
                        raise TypeError(
                            f'No valid template found for {rabz__hyk.func.name}'
                            )
                    rabz__hyk.args = [lcpqf__gtow] + rabz__hyk.args
            vpvw__ppwm.append(stmt)
        block.body = vpvw__ppwm


if _check_numba_change:
    lines = inspect.getsource(numba.core.ir_utils.canonicalize_array_math)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'b2200e9100613631cc554f4b640bc1181ba7cea0ece83630122d15b86941be2e':
        warnings.warn('canonicalize_array_math has changed')
numba.core.ir_utils.canonicalize_array_math = canonicalize_array_math
numba.parfors.parfor.canonicalize_array_math = canonicalize_array_math
numba.core.inline_closurecall.canonicalize_array_math = canonicalize_array_math


def _Numpy_Rules_ufunc_handle_inputs(cls, ufunc, args, kws):
    gcj__cfkuc = ufunc.nin
    hqs__oloo = ufunc.nout
    bttzq__nxzvt = ufunc.nargs
    assert bttzq__nxzvt == gcj__cfkuc + hqs__oloo
    if len(args) < gcj__cfkuc:
        msg = "ufunc '{0}': not enough arguments ({1} found, {2} required)"
        raise TypingError(msg=msg.format(ufunc.__name__, len(args), gcj__cfkuc)
            )
    if len(args) > bttzq__nxzvt:
        msg = "ufunc '{0}': too many arguments ({1} found, {2} maximum)"
        raise TypingError(msg=msg.format(ufunc.__name__, len(args),
            bttzq__nxzvt))
    args = [(a.as_array if isinstance(a, types.ArrayCompatible) and not
        isinstance(a, types.Bytes) else a) for a in args]
    voq__vzuzv = [(a.ndim if isinstance(a, types.ArrayCompatible) and not
        isinstance(a, types.Bytes) else 0) for a in args]
    esqu__eln = max(voq__vzuzv)
    tnm__bhusg = args[gcj__cfkuc:]
    if not all(d == esqu__eln for d in voq__vzuzv[gcj__cfkuc:]):
        msg = "ufunc '{0}' called with unsuitable explicit output arrays."
        raise TypingError(msg=msg.format(ufunc.__name__))
    if not all(isinstance(nok__wuvkk, types.ArrayCompatible) and not
        isinstance(nok__wuvkk, types.Bytes) for nok__wuvkk in tnm__bhusg):
        msg = "ufunc '{0}' called with an explicit output that is not an array"
        raise TypingError(msg=msg.format(ufunc.__name__))
    if not all(nok__wuvkk.mutable for nok__wuvkk in tnm__bhusg):
        msg = "ufunc '{0}' called with an explicit output that is read-only"
        raise TypingError(msg=msg.format(ufunc.__name__))
    yijas__faj = [(x.dtype if isinstance(x, types.ArrayCompatible) and not
        isinstance(x, types.Bytes) else x) for x in args]
    ccwb__nmmsz = None
    if esqu__eln > 0 and len(tnm__bhusg) < ufunc.nout:
        ccwb__nmmsz = 'C'
        plq__jwu = [(x.layout if isinstance(x, types.ArrayCompatible) and 
            not isinstance(x, types.Bytes) else '') for x in args]
        if 'C' not in plq__jwu and 'F' in plq__jwu:
            ccwb__nmmsz = 'F'
    return yijas__faj, tnm__bhusg, esqu__eln, ccwb__nmmsz


if _check_numba_change:
    lines = inspect.getsource(numba.core.typing.npydecl.Numpy_rules_ufunc.
        _handle_inputs)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '4b97c64ad9c3d50e082538795054f35cf6d2fe962c3ca40e8377a4601b344d5c':
        warnings.warn('Numpy_rules_ufunc._handle_inputs has changed')
numba.core.typing.npydecl.Numpy_rules_ufunc._handle_inputs = (
    _Numpy_Rules_ufunc_handle_inputs)
numba.np.ufunc.dufunc.npydecl.Numpy_rules_ufunc._handle_inputs = (
    _Numpy_Rules_ufunc_handle_inputs)


def DictType__init__(self, keyty, valty, initial_value=None):
    from numba.types import DictType, InitialValue, NoneType, Optional, Tuple, TypeRef, unliteral
    assert not isinstance(keyty, TypeRef)
    assert not isinstance(valty, TypeRef)
    keyty = unliteral(keyty)
    valty = unliteral(valty)
    if isinstance(keyty, (Optional, NoneType)):
        lymav__ptxf = 'Dict.key_type cannot be of type {}'
        raise TypingError(lymav__ptxf.format(keyty))
    if isinstance(valty, (Optional, NoneType)):
        lymav__ptxf = 'Dict.value_type cannot be of type {}'
        raise TypingError(lymav__ptxf.format(valty))
    self.key_type = keyty
    self.value_type = valty
    self.keyvalue_type = Tuple([keyty, valty])
    name = '{}[{},{}]<iv={}>'.format(self.__class__.__name__, keyty, valty,
        initial_value)
    super(DictType, self).__init__(name)
    InitialValue.__init__(self, initial_value)


if _check_numba_change:
    lines = inspect.getsource(numba.core.types.containers.DictType.__init__)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '475acd71224bd51526750343246e064ff071320c0d10c17b8b8ac81d5070d094':
        warnings.warn('DictType.__init__ has changed')
numba.core.types.containers.DictType.__init__ = DictType__init__


def _legalize_arg_types(self, args):
    for i, a in enumerate(args, start=1):
        if isinstance(a, types.Dispatcher):
            msg = (
                'Does not support function type inputs into with-context for arg {}'
                )
            raise errors.TypingError(msg.format(i))


if _check_numba_change:
    lines = inspect.getsource(numba.core.dispatcher.ObjModeLiftedWith.
        _legalize_arg_types)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '4793f44ebc7da8843e8f298e08cd8a5428b4b84b89fd9d5c650273fdb8fee5ee':
        warnings.warn('ObjModeLiftedWith._legalize_arg_types has changed')
numba.core.dispatcher.ObjModeLiftedWith._legalize_arg_types = (
    _legalize_arg_types)


def _overload_template_get_impl(self, args, kws):
    pjqur__dmro = self.context, tuple(args), tuple(kws.items())
    try:
        impl, args = self._impl_cache[pjqur__dmro]
        return impl, args
    except KeyError as iezc__rwqn:
        pass
    impl, args = self._build_impl(pjqur__dmro, args, kws)
    return impl, args


if _check_numba_change:
    lines = inspect.getsource(numba.core.typing.templates.
        _OverloadFunctionTemplate._get_impl)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '4e27d07b214ca16d6e8ed88f70d886b6b095e160d8f77f8df369dd4ed2eb3fae':
        warnings.warn(
            'numba.core.typing.templates._OverloadFunctionTemplate._get_impl has changed'
            )
numba.core.typing.templates._OverloadFunctionTemplate._get_impl = (
    _overload_template_get_impl)


def trim_empty_parfor_branches(parfor):
    enzy__igus = False
    blocks = parfor.loop_body.copy()
    for label, block in blocks.items():
        if len(block.body):
            kherg__jtid = block.body[-1]
            if isinstance(kherg__jtid, ir.Branch):
                if len(blocks[kherg__jtid.truebr].body) == 1 and len(blocks
                    [kherg__jtid.falsebr].body) == 1:
                    encly__ppxq = blocks[kherg__jtid.truebr].body[0]
                    pim__geczg = blocks[kherg__jtid.falsebr].body[0]
                    if isinstance(encly__ppxq, ir.Jump) and isinstance(
                        pim__geczg, ir.Jump
                        ) and encly__ppxq.target == pim__geczg.target:
                        parfor.loop_body[label].body[-1] = ir.Jump(encly__ppxq
                            .target, kherg__jtid.loc)
                        enzy__igus = True
                elif len(blocks[kherg__jtid.truebr].body) == 1:
                    encly__ppxq = blocks[kherg__jtid.truebr].body[0]
                    if isinstance(encly__ppxq, ir.Jump
                        ) and encly__ppxq.target == kherg__jtid.falsebr:
                        parfor.loop_body[label].body[-1] = ir.Jump(encly__ppxq
                            .target, kherg__jtid.loc)
                        enzy__igus = True
                elif len(blocks[kherg__jtid.falsebr].body) == 1:
                    pim__geczg = blocks[kherg__jtid.falsebr].body[0]
                    if isinstance(pim__geczg, ir.Jump
                        ) and pim__geczg.target == kherg__jtid.truebr:
                        parfor.loop_body[label].body[-1] = ir.Jump(pim__geczg
                            .target, kherg__jtid.loc)
                        enzy__igus = True
    return enzy__igus


def remove_dead_parfor(parfor, lives, lives_n_aliases, arg_aliases,
    alias_map, func_ir, typemap):
    from numba.core.analysis import compute_cfg_from_blocks, compute_live_map, compute_use_defs
    from numba.core.ir_utils import find_topo_order
    from numba.parfors.parfor import _add_liveness_return_block, _update_parfor_get_setitems, dummy_return_in_loop_body, get_index_var, remove_dead_parfor_recursive, simplify_parfor_body_CFG
    with dummy_return_in_loop_body(parfor.loop_body):
        sles__hmn = find_topo_order(parfor.loop_body)
    dyy__rlq = sles__hmn[0]
    kcrh__zdprc = {}
    _update_parfor_get_setitems(parfor.loop_body[dyy__rlq].body, parfor.
        index_var, alias_map, kcrh__zdprc, lives_n_aliases)
    kmcck__xzl = set(kcrh__zdprc.keys())
    for wnsf__rykcg in sles__hmn:
        if wnsf__rykcg == dyy__rlq:
            continue
        for stmt in parfor.loop_body[wnsf__rykcg].body:
            if (isinstance(stmt, ir.Assign) and isinstance(stmt.value, ir.
                Expr) and stmt.value.op == 'getitem' and stmt.value.index.
                name == parfor.index_var.name):
                continue
            oyxs__nbjf = set(udil__tquzm.name for udil__tquzm in stmt.
                list_vars())
            dvia__cdml = oyxs__nbjf & kmcck__xzl
            for a in dvia__cdml:
                kcrh__zdprc.pop(a, None)
    for wnsf__rykcg in sles__hmn:
        if wnsf__rykcg == dyy__rlq:
            continue
        block = parfor.loop_body[wnsf__rykcg]
        vhw__dodo = kcrh__zdprc.copy()
        _update_parfor_get_setitems(block.body, parfor.index_var, alias_map,
            vhw__dodo, lives_n_aliases)
    blocks = parfor.loop_body.copy()
    wthm__zwm = max(blocks.keys())
    rceo__wimtf, gok__ergo = _add_liveness_return_block(blocks,
        lives_n_aliases, typemap)
    igw__emga = ir.Jump(rceo__wimtf, ir.Loc('parfors_dummy', -1))
    blocks[wthm__zwm].body.append(igw__emga)
    jbs__mqwyq = compute_cfg_from_blocks(blocks)
    wzb__lbtx = compute_use_defs(blocks)
    yhe__nqs = compute_live_map(jbs__mqwyq, blocks, wzb__lbtx.usemap,
        wzb__lbtx.defmap)
    alias_set = set(alias_map.keys())
    for label, block in blocks.items():
        vpvw__ppwm = []
        bevbs__ref = {udil__tquzm.name for udil__tquzm in block.terminator.
            list_vars()}
        for tzj__rlifd, itinr__pmb in jbs__mqwyq.successors(label):
            bevbs__ref |= yhe__nqs[tzj__rlifd]
        for stmt in reversed(block.body):
            vsqs__lznk = bevbs__ref & alias_set
            for udil__tquzm in vsqs__lznk:
                bevbs__ref |= alias_map[udil__tquzm]
            if (isinstance(stmt, (ir.StaticSetItem, ir.SetItem)) and 
                get_index_var(stmt).name == parfor.index_var.name and stmt.
                target.name not in bevbs__ref and stmt.target.name not in
                arg_aliases):
                continue
            elif isinstance(stmt, ir.Assign) and isinstance(stmt.value, ir.Expr
                ) and stmt.value.op == 'call':
                pez__wvvw = guard(find_callname, func_ir, stmt.value)
                if pez__wvvw == ('setna', 'bodo.libs.array_kernels'
                    ) and stmt.value.args[0
                    ].name not in bevbs__ref and stmt.value.args[0
                    ].name not in arg_aliases:
                    continue
            bevbs__ref |= {udil__tquzm.name for udil__tquzm in stmt.list_vars()
                }
            vpvw__ppwm.append(stmt)
        vpvw__ppwm.reverse()
        block.body = vpvw__ppwm
    typemap.pop(gok__ergo.name)
    blocks[wthm__zwm].body.pop()
    enzy__igus = True
    while enzy__igus:
        """
        Process parfor body recursively.
        Note that this is the only place in this function that uses the
        argument lives instead of lives_n_aliases.  The former does not
        include the aliases of live variables but only the live variable
        names themselves.  See a comment in this function for how that
        is used.
        """
        remove_dead_parfor_recursive(parfor, lives, arg_aliases, alias_map,
            func_ir, typemap)
        simplify_parfor_body_CFG(func_ir.blocks)
        enzy__igus = trim_empty_parfor_branches(parfor)
    sifx__vsmw = len(parfor.init_block.body) == 0
    for block in parfor.loop_body.values():
        sifx__vsmw &= len(block.body) == 0
    if sifx__vsmw:
        return None
    return parfor


if _check_numba_change:
    lines = inspect.getsource(numba.parfors.parfor.remove_dead_parfor)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '1c9b008a7ead13e988e1efe67618d8f87f0b9f3d092cc2cd6bfcd806b1fdb859':
        warnings.warn('remove_dead_parfor has changed')
numba.parfors.parfor.remove_dead_parfor = remove_dead_parfor
numba.core.ir_utils.remove_dead_extensions[numba.parfors.parfor.Parfor
    ] = remove_dead_parfor


def simplify_parfor_body_CFG(blocks):
    from numba.core.analysis import compute_cfg_from_blocks
    from numba.parfors.parfor import Parfor
    rebe__jlec = 0
    for block in blocks.values():
        for stmt in block.body:
            if isinstance(stmt, Parfor):
                rebe__jlec += 1
                parfor = stmt
                qjy__bckt = parfor.loop_body[max(parfor.loop_body.keys())]
                scope = qjy__bckt.scope
                loc = ir.Loc('parfors_dummy', -1)
                hyupo__mgzbn = ir.Var(scope, mk_unique_var('$const'), loc)
                qjy__bckt.body.append(ir.Assign(ir.Const(0, loc),
                    hyupo__mgzbn, loc))
                qjy__bckt.body.append(ir.Return(hyupo__mgzbn, loc))
                jbs__mqwyq = compute_cfg_from_blocks(parfor.loop_body)
                for aako__ydo in jbs__mqwyq.dead_nodes():
                    del parfor.loop_body[aako__ydo]
                parfor.loop_body = simplify_CFG(parfor.loop_body)
                qjy__bckt = parfor.loop_body[max(parfor.loop_body.keys())]
                qjy__bckt.body.pop()
                qjy__bckt.body.pop()
                simplify_parfor_body_CFG(parfor.loop_body)
    return rebe__jlec


if _check_numba_change:
    lines = inspect.getsource(numba.parfors.parfor.simplify_parfor_body_CFG)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '437ae96a5e8ec64a2b69a4f23ba8402a1d170262a5400aa0aa7bfe59e03bf726':
        warnings.warn('simplify_parfor_body_CFG has changed')
numba.parfors.parfor.simplify_parfor_body_CFG = simplify_parfor_body_CFG


def simplify_CFG(blocks):
    from numba.core.analysis import compute_cfg_from_blocks
    from numba.core.ir_utils import merge_adjacent_blocks, rename_labels
    jbs__mqwyq = compute_cfg_from_blocks(blocks)

    def find_single_branch(label):
        block = blocks[label]
        return len(block.body) == 1 and isinstance(block.body[0], ir.Branch
            ) and label != jbs__mqwyq.entry_point()
    wwux__dbbp = list(filter(find_single_branch, blocks.keys()))
    hew__iluc = set()
    for label in wwux__dbbp:
        inst = blocks[label].body[0]
        val__boed = jbs__mqwyq.predecessors(label)
        arpo__jekgk = True
        for qvct__ifec, ezip__qsjnd in val__boed:
            block = blocks[qvct__ifec]
            if isinstance(block.body[-1], ir.Jump):
                block.body[-1] = copy.copy(inst)
            else:
                arpo__jekgk = False
        if arpo__jekgk:
            hew__iluc.add(label)
    for label in hew__iluc:
        del blocks[label]
    merge_adjacent_blocks(blocks)
    return rename_labels(blocks)


if _check_numba_change:
    lines = inspect.getsource(numba.core.ir_utils.simplify_CFG)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '0b3f2add05e5691155f08fc5945956d5cca5e068247d52cff8efb161b76388b7':
        warnings.warn('numba.core.ir_utils.simplify_CFG has changed')
numba.core.ir_utils.simplify_CFG = simplify_CFG


def _lifted_compile(self, sig):
    import numba.core.event as ev
    from numba.core import compiler, sigutils
    from numba.core.compiler_lock import global_compiler_lock
    from numba.core.ir_utils import remove_dels
    with ExitStack() as scope:
        cres = None

        def cb_compiler(dur):
            if cres is not None:
                self._callback_add_compiler_timer(dur, cres)

        def cb_llvm(dur):
            if cres is not None:
                self._callback_add_llvm_timer(dur, cres)
        scope.enter_context(ev.install_timer('numba:compiler_lock',
            cb_compiler))
        scope.enter_context(ev.install_timer('numba:llvm_lock', cb_llvm))
        scope.enter_context(global_compiler_lock)
        with self._compiling_counter:
            flags = self.flags
            args, return_type = sigutils.normalize_signature(sig)
            lbn__nnlgn = self.overloads.get(tuple(args))
            if lbn__nnlgn is not None:
                return lbn__nnlgn.entry_point
            self._pre_compile(args, return_type, flags)
            cscs__luvs = self.func_ir
            fcyze__nss = dict(dispatcher=self, args=args, return_type=
                return_type)
            with ev.trigger_event('numba:compile', data=fcyze__nss):
                cres = compiler.compile_ir(typingctx=self.typingctx,
                    targetctx=self.targetctx, func_ir=cscs__luvs, args=args,
                    return_type=return_type, flags=flags, locals=self.
                    locals, lifted=(), lifted_from=self.lifted_from,
                    is_lifted_loop=True)
                if cres.typing_error is not None and not flags.enable_pyobject:
                    raise cres.typing_error
                self.add_overload(cres)
            remove_dels(self.func_ir.blocks)
            return cres.entry_point


if _check_numba_change:
    lines = inspect.getsource(numba.core.dispatcher.LiftedCode.compile)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '1351ebc5d8812dc8da167b30dad30eafb2ca9bf191b49aaed6241c21e03afff1':
        warnings.warn('numba.core.dispatcher.LiftedCode.compile has changed')
numba.core.dispatcher.LiftedCode.compile = _lifted_compile


def compile_ir(typingctx, targetctx, func_ir, args, return_type, flags,
    locals, lifted=(), lifted_from=None, is_lifted_loop=False, library=None,
    pipeline_class=Compiler):
    if is_lifted_loop:
        rax__hmx = copy.deepcopy(flags)
        rax__hmx.no_rewrites = True

        def compile_local(the_ir, the_flags):
            bsm__wmtyq = pipeline_class(typingctx, targetctx, library, args,
                return_type, the_flags, locals)
            return bsm__wmtyq.compile_ir(func_ir=the_ir, lifted=lifted,
                lifted_from=lifted_from)
        vwa__slai = compile_local(func_ir, rax__hmx)
        dyhx__qfmz = None
        if not flags.no_rewrites:
            with warnings.catch_warnings():
                warnings.simplefilter('ignore', errors.NumbaWarning)
                try:
                    dyhx__qfmz = compile_local(func_ir, flags)
                except Exception as iezc__rwqn:
                    pass
        if dyhx__qfmz is not None:
            cres = dyhx__qfmz
        else:
            cres = vwa__slai
        return cres
    else:
        bsm__wmtyq = pipeline_class(typingctx, targetctx, library, args,
            return_type, flags, locals)
        return bsm__wmtyq.compile_ir(func_ir=func_ir, lifted=lifted,
            lifted_from=lifted_from)


if _check_numba_change:
    lines = inspect.getsource(numba.core.compiler.compile_ir)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'c48ce5493f4c43326e8cbdd46f3ea038b2b9045352d9d25894244798388e5e5b':
        warnings.warn('numba.core.compiler.compile_ir has changed')
numba.core.compiler.compile_ir = compile_ir


def make_constant_array(self, builder, typ, ary):
    import math
    from llvmlite import ir as lir
    tajzc__zmske = self.get_data_type(typ.dtype)
    ais__txceo = 10 ** 7
    if self.allow_dynamic_globals and (typ.layout not in 'FC' or ary.nbytes >
        ais__txceo):
        wvezy__bgu = ary.ctypes.data
        eqpo__udm = self.add_dynamic_addr(builder, wvezy__bgu, info=str(
            type(wvezy__bgu)))
        bpniv__yuty = self.add_dynamic_addr(builder, id(ary), info=str(type
            (ary)))
        self.global_arrays.append(ary)
    else:
        stqt__gjehu = ary.flatten(order=typ.layout)
        if isinstance(typ.dtype, (types.NPDatetime, types.NPTimedelta)):
            stqt__gjehu = stqt__gjehu.view('int64')
        val = bytearray(stqt__gjehu.data)
        sla__whi = lir.Constant(lir.ArrayType(lir.IntType(8), len(val)), val)
        eqpo__udm = cgutils.global_constant(builder, '.const.array.data',
            sla__whi)
        eqpo__udm.align = self.get_abi_alignment(tajzc__zmske)
        bpniv__yuty = None
    wkpxf__lxv = self.get_value_type(types.intp)
    isocm__vdfrc = [self.get_constant(types.intp, vyei__rgv) for vyei__rgv in
        ary.shape]
    bizq__ajbp = lir.Constant(lir.ArrayType(wkpxf__lxv, len(isocm__vdfrc)),
        isocm__vdfrc)
    ndkmf__sxh = [self.get_constant(types.intp, vyei__rgv) for vyei__rgv in
        ary.strides]
    qzdm__apnqf = lir.Constant(lir.ArrayType(wkpxf__lxv, len(ndkmf__sxh)),
        ndkmf__sxh)
    tuof__wlw = self.get_constant(types.intp, ary.dtype.itemsize)
    siiys__bhxsk = self.get_constant(types.intp, math.prod(ary.shape))
    return lir.Constant.literal_struct([self.get_constant_null(types.
        MemInfoPointer(typ.dtype)), self.get_constant_null(types.pyobject),
        siiys__bhxsk, tuof__wlw, eqpo__udm.bitcast(self.get_value_type(
        types.CPointer(typ.dtype))), bizq__ajbp, qzdm__apnqf])


if _check_numba_change:
    lines = inspect.getsource(numba.core.base.BaseContext.make_constant_array)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '5721b5360b51f782f79bd794f7bf4d48657911ecdc05c30db22fd55f15dad821':
        warnings.warn(
            'numba.core.base.BaseContext.make_constant_array has changed')
numba.core.base.BaseContext.make_constant_array = make_constant_array


def _define_atomic_inc_dec(module, op, ordering):
    from llvmlite import ir as lir
    from numba.core.runtime.nrtdynmod import _word_type
    amh__tzmb = lir.FunctionType(_word_type, [_word_type.as_pointer()])
    kqazn__arps = lir.Function(module, amh__tzmb, name='nrt_atomic_{0}'.
        format(op))
    [stuv__chc] = kqazn__arps.args
    yuy__jtaw = kqazn__arps.append_basic_block()
    builder = lir.IRBuilder(yuy__jtaw)
    jnf__rxbrq = lir.Constant(_word_type, 1)
    if False:
        uzwe__ycc = builder.atomic_rmw(op, stuv__chc, jnf__rxbrq, ordering=
            ordering)
        res = getattr(builder, op)(uzwe__ycc, jnf__rxbrq)
        builder.ret(res)
    else:
        uzwe__ycc = builder.load(stuv__chc)
        shrk__ztt = getattr(builder, op)(uzwe__ycc, jnf__rxbrq)
        dcl__cmf = builder.icmp_signed('!=', uzwe__ycc, lir.Constant(
            uzwe__ycc.type, -1))
        with cgutils.if_likely(builder, dcl__cmf):
            builder.store(shrk__ztt, stuv__chc)
        builder.ret(shrk__ztt)
    return kqazn__arps


if _check_numba_change:
    lines = inspect.getsource(numba.core.runtime.nrtdynmod.
        _define_atomic_inc_dec)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '9cc02c532b2980b6537b702f5608ea603a1ff93c6d3c785ae2cf48bace273f48':
        warnings.warn(
            'numba.core.runtime.nrtdynmod._define_atomic_inc_dec has changed')
numba.core.runtime.nrtdynmod._define_atomic_inc_dec = _define_atomic_inc_dec


def NativeLowering_run_pass(self, state):
    from llvmlite import binding as llvm
    from numba.core import funcdesc, lowering
    from numba.core.typed_passes import fallback_context
    if state.library is None:
        zgtx__eeq = state.targetctx.codegen()
        state.library = zgtx__eeq.create_library(state.func_id.func_qualname)
        state.library.enable_object_caching()
    library = state.library
    targetctx = state.targetctx
    twji__kntd = state.func_ir
    typemap = state.typemap
    pmhl__fvzr = state.return_type
    calltypes = state.calltypes
    flags = state.flags
    metadata = state.metadata
    xeg__qims = llvm.passmanagers.dump_refprune_stats()
    msg = 'Function %s failed at nopython mode lowering' % (state.func_id.
        func_name,)
    with fallback_context(state, msg):
        fndesc = funcdesc.PythonFunctionDescriptor.from_specialized_function(
            twji__kntd, typemap, pmhl__fvzr, calltypes, mangler=targetctx.
            mangler, inline=flags.forceinline, noalias=flags.noalias,
            abi_tags=[flags.get_mangle_string()])
        targetctx.global_arrays = []
        with targetctx.push_code_library(library):
            lxl__piaw = lowering.Lower(targetctx, library, fndesc,
                twji__kntd, metadata=metadata)
            lxl__piaw.lower()
            if not flags.no_cpython_wrapper:
                lxl__piaw.create_cpython_wrapper(flags.release_gil)
            if not flags.no_cfunc_wrapper:
                for t in state.args:
                    if isinstance(t, (types.Omitted, types.Generator)):
                        break
                else:
                    if isinstance(pmhl__fvzr, (types.Optional, types.Generator)
                        ):
                        pass
                    else:
                        lxl__piaw.create_cfunc_wrapper()
            env = lxl__piaw.env
            teuh__gwmxa = lxl__piaw.call_helper
            del lxl__piaw
        from numba.core.compiler import _LowerResult
        if flags.no_compile:
            state['cr'] = _LowerResult(fndesc, teuh__gwmxa, cfunc=None, env=env
                )
        else:
            zlvq__rvwq = targetctx.get_executable(library, fndesc, env)
            targetctx.insert_user_function(zlvq__rvwq, fndesc, [library])
            state['cr'] = _LowerResult(fndesc, teuh__gwmxa, cfunc=
                zlvq__rvwq, env=env)
        metadata['global_arrs'] = targetctx.global_arrays
        targetctx.global_arrays = []
        bsm__selpa = llvm.passmanagers.dump_refprune_stats()
        metadata['prune_stats'] = bsm__selpa - xeg__qims
        metadata['llvm_pass_timings'] = library.recorded_timings
    return True


if _check_numba_change:
    lines = inspect.getsource(numba.core.typed_passes.NativeLowering.run_pass)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'a777ce6ce1bb2b1cbaa3ac6c2c0e2adab69a9c23888dff5f1cbb67bfb176b5de':
        warnings.warn(
            'numba.core.typed_passes.NativeLowering.run_pass has changed')
numba.core.typed_passes.NativeLowering.run_pass = NativeLowering_run_pass


def _python_list_to_native(typ, obj, c, size, listptr, errorptr):
    from llvmlite import ir as lir
    from numba.core.boxing import _NumbaTypeHelper
    from numba.cpython import listobj

    def check_element_type(nth, itemobj, expected_typobj):
        zgp__gif = nth.typeof(itemobj)
        with c.builder.if_then(cgutils.is_null(c.builder, zgp__gif), likely
            =False):
            c.builder.store(cgutils.true_bit, errorptr)
            ukg__ufpd.do_break()
        bfsm__awn = c.builder.icmp_signed('!=', zgp__gif, expected_typobj)
        if not isinstance(typ.dtype, types.Optional):
            with c.builder.if_then(bfsm__awn, likely=False):
                c.builder.store(cgutils.true_bit, errorptr)
                c.pyapi.err_format('PyExc_TypeError',
                    "can't unbox heterogeneous list: %S != %S",
                    expected_typobj, zgp__gif)
                c.pyapi.decref(zgp__gif)
                ukg__ufpd.do_break()
        c.pyapi.decref(zgp__gif)
    emvv__ays, list = listobj.ListInstance.allocate_ex(c.context, c.builder,
        typ, size)
    with c.builder.if_else(emvv__ays, likely=True) as (tgiq__gpnl, ehjk__dqpx):
        with tgiq__gpnl:
            list.size = size
            gse__qedw = lir.Constant(size.type, 0)
            with c.builder.if_then(c.builder.icmp_signed('>', size,
                gse__qedw), likely=True):
                with _NumbaTypeHelper(c) as nth:
                    expected_typobj = nth.typeof(c.pyapi.list_getitem(obj,
                        gse__qedw))
                    with cgutils.for_range(c.builder, size) as ukg__ufpd:
                        itemobj = c.pyapi.list_getitem(obj, ukg__ufpd.index)
                        check_element_type(nth, itemobj, expected_typobj)
                        mps__vpw = c.unbox(typ.dtype, itemobj)
                        with c.builder.if_then(mps__vpw.is_error, likely=False
                            ):
                            c.builder.store(cgutils.true_bit, errorptr)
                            ukg__ufpd.do_break()
                        list.setitem(ukg__ufpd.index, mps__vpw.value,
                            incref=False)
                    c.pyapi.decref(expected_typobj)
            if typ.reflected:
                list.parent = obj
            with c.builder.if_then(c.builder.not_(c.builder.load(errorptr)),
                likely=False):
                c.pyapi.object_set_private_data(obj, list.meminfo)
            list.set_dirty(False)
            c.builder.store(list.value, listptr)
        with ehjk__dqpx:
            c.builder.store(cgutils.true_bit, errorptr)
    with c.builder.if_then(c.builder.load(errorptr)):
        c.context.nrt.decref(c.builder, typ, list.value)


if _check_numba_change:
    lines = inspect.getsource(numba.core.boxing._python_list_to_native)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'f8e546df8b07adfe74a16b6aafb1d4fddbae7d3516d7944b3247cc7c9b7ea88a':
        warnings.warn('numba.core.boxing._python_list_to_native has changed')
numba.core.boxing._python_list_to_native = _python_list_to_native


def make_string_from_constant(context, builder, typ, literal_string):
    from llvmlite import ir as lir
    from numba.cpython.hashing import _Py_hash_t
    from numba.cpython.unicode import compile_time_get_string_data
    imk__mfauj, rrra__cai, aof__spone, mgq__jndt, vxlbt__njscd = (
        compile_time_get_string_data(literal_string))
    pukq__olxkc = builder.module
    gv = context.insert_const_bytes(pukq__olxkc, imk__mfauj)
    return lir.Constant.literal_struct([gv, context.get_constant(types.intp,
        rrra__cai), context.get_constant(types.int32, aof__spone), context.
        get_constant(types.uint32, mgq__jndt), context.get_constant(
        _Py_hash_t, -1), context.get_constant_null(types.MemInfoPointer(
        types.voidptr)), context.get_constant_null(types.pyobject)])


if _check_numba_change:
    lines = inspect.getsource(numba.cpython.unicode.make_string_from_constant)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '525bd507383e06152763e2f046dae246cd60aba027184f50ef0fc9a80d4cd7fa':
        warnings.warn(
            'numba.cpython.unicode.make_string_from_constant has changed')
numba.cpython.unicode.make_string_from_constant = make_string_from_constant


def parse_shape(shape):
    ppiq__urmz = None
    if isinstance(shape, types.Integer):
        ppiq__urmz = 1
    elif isinstance(shape, (types.Tuple, types.UniTuple)):
        if all(isinstance(vyei__rgv, (types.Integer, types.IntEnumMember)) for
            vyei__rgv in shape):
            ppiq__urmz = len(shape)
    return ppiq__urmz


if _check_numba_change:
    lines = inspect.getsource(numba.core.typing.npydecl.parse_shape)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'e62e3ff09d36df5ac9374055947d6a8be27160ce32960d3ef6cb67f89bd16429':
        warnings.warn('numba.core.typing.npydecl.parse_shape has changed')
numba.core.typing.npydecl.parse_shape = parse_shape


def _get_names(self, obj):
    if isinstance(obj, ir.Var) or isinstance(obj, str):
        name = obj if isinstance(obj, str) else obj.name
        if name not in self.typemap:
            return name,
        typ = self.typemap[name]
        if isinstance(typ, (types.BaseTuple, types.ArrayCompatible)):
            ppiq__urmz = typ.ndim if isinstance(typ, types.ArrayCompatible
                ) else len(typ)
            if ppiq__urmz == 0:
                return name,
            else:
                return tuple('{}#{}'.format(name, i) for i in range(ppiq__urmz)
                    )
        else:
            return name,
    elif isinstance(obj, ir.Const):
        if isinstance(obj.value, tuple):
            return obj.value
        else:
            return obj.value,
    elif isinstance(obj, tuple):

        def get_names(x):
            gfjca__spe = self._get_names(x)
            if len(gfjca__spe) != 0:
                return gfjca__spe[0]
            return gfjca__spe
        return tuple(get_names(x) for x in obj)
    elif isinstance(obj, int):
        return obj,
    return ()


def get_equiv_const(self, obj):
    gfjca__spe = self._get_names(obj)
    if len(gfjca__spe) != 1:
        return None
    return super(numba.parfors.array_analysis.ShapeEquivSet, self
        ).get_equiv_const(gfjca__spe[0])


def get_equiv_set(self, obj):
    gfjca__spe = self._get_names(obj)
    if len(gfjca__spe) != 1:
        return None
    return super(numba.parfors.array_analysis.ShapeEquivSet, self
        ).get_equiv_set(gfjca__spe[0])


if _check_numba_change:
    for name, orig, new, hash in ((
        'numba.parfors.array_analysis.ShapeEquivSet._get_names', numba.
        parfors.array_analysis.ShapeEquivSet._get_names, _get_names,
        '8c9bf136109028d5445fd0a82387b6abeb70c23b20b41e2b50c34ba5359516ee'),
        ('numba.parfors.array_analysis.ShapeEquivSet.get_equiv_const',
        numba.parfors.array_analysis.ShapeEquivSet.get_equiv_const,
        get_equiv_const,
        'bef410ca31a9e29df9ee74a4a27d339cc332564e4a237828b8a4decf625ce44e'),
        ('numba.parfors.array_analysis.ShapeEquivSet.get_equiv_set', numba.
        parfors.array_analysis.ShapeEquivSet.get_equiv_set, get_equiv_set,
        'ec936d340c488461122eb74f28a28b88227cb1f1bca2b9ba3c19258cfe1eb40a')):
        lines = inspect.getsource(orig)
        if hashlib.sha256(lines.encode()).hexdigest() != hash:
            warnings.warn(f'{name} has changed')
numba.parfors.array_analysis.ShapeEquivSet._get_names = _get_names
numba.parfors.array_analysis.ShapeEquivSet.get_equiv_const = get_equiv_const
numba.parfors.array_analysis.ShapeEquivSet.get_equiv_set = get_equiv_set


def raise_on_unsupported_feature(func_ir, typemap):
    import numpy
    xyfk__pwunb = []
    for vdh__rjn in func_ir.arg_names:
        if vdh__rjn in typemap and isinstance(typemap[vdh__rjn], types.
            containers.UniTuple) and typemap[vdh__rjn].count > 1000:
            msg = (
                """Tuple '{}' length must be smaller than 1000.
Large tuples lead to the generation of a prohibitively large LLVM IR which causes excessive memory pressure and large compile times.
As an alternative, the use of a 'list' is recommended in place of a 'tuple' as lists do not suffer from this problem."""
                .format(vdh__rjn))
            raise errors.UnsupportedError(msg, func_ir.loc)
    for qji__zfd in func_ir.blocks.values():
        for stmt in qji__zfd.find_insts(ir.Assign):
            if isinstance(stmt.value, ir.Expr):
                if stmt.value.op == 'make_function':
                    val = stmt.value
                    xdf__mcux = getattr(val, 'code', None)
                    if xdf__mcux is not None:
                        if getattr(val, 'closure', None) is not None:
                            rcag__wvnhf = (
                                '<creating a function from a closure>')
                            idea__ggdyg = ''
                        else:
                            rcag__wvnhf = xdf__mcux.co_name
                            idea__ggdyg = '(%s) ' % rcag__wvnhf
                    else:
                        rcag__wvnhf = '<could not ascertain use case>'
                        idea__ggdyg = ''
                    msg = (
                        'Numba encountered the use of a language feature it does not support in this context: %s (op code: make_function not supported). If the feature is explicitly supported it is likely that the result of the expression %sis being used in an unsupported manner.'
                         % (rcag__wvnhf, idea__ggdyg))
                    raise errors.UnsupportedError(msg, stmt.value.loc)
            if isinstance(stmt.value, (ir.Global, ir.FreeVar)):
                val = stmt.value
                val = getattr(val, 'value', None)
                if val is None:
                    continue
                haq__vrze = False
                if isinstance(val, pytypes.FunctionType):
                    haq__vrze = val in {numba.gdb, numba.gdb_init}
                if not haq__vrze:
                    haq__vrze = getattr(val, '_name', '') == 'gdb_internal'
                if haq__vrze:
                    xyfk__pwunb.append(stmt.loc)
            if isinstance(stmt.value, ir.Expr):
                if stmt.value.op == 'getattr' and stmt.value.attr == 'view':
                    var = stmt.value.value.name
                    if isinstance(typemap[var], types.Array):
                        continue
                    actj__fpf = func_ir.get_definition(var)
                    rpkhd__guox = guard(find_callname, func_ir, actj__fpf)
                    if rpkhd__guox and rpkhd__guox[1] == 'numpy':
                        ty = getattr(numpy, rpkhd__guox[0])
                        if numpy.issubdtype(ty, numpy.integer
                            ) or numpy.issubdtype(ty, numpy.floating):
                            continue
                    xcac__xcz = '' if var.startswith('$') else "'{}' ".format(
                        var)
                    raise TypingError(
                        "'view' can only be called on NumPy dtypes, try wrapping the variable {}with 'np.<dtype>()'"
                        .format(xcac__xcz), loc=stmt.loc)
            if isinstance(stmt.value, ir.Global):
                ty = typemap[stmt.target.name]
                msg = (
                    "The use of a %s type, assigned to variable '%s' in globals, is not supported as globals are considered compile-time constants and there is no known way to compile a %s type as a constant."
                    )
                if isinstance(ty, types.ListType):
                    raise TypingError(msg % (ty, stmt.value.name, ty), loc=
                        stmt.loc)
            if isinstance(stmt.value, ir.Yield) and not func_ir.is_generator:
                msg = 'The use of generator expressions is unsupported.'
                raise errors.UnsupportedError(msg, loc=stmt.loc)
    if len(xyfk__pwunb) > 1:
        msg = """Calling either numba.gdb() or numba.gdb_init() more than once in a function is unsupported (strange things happen!), use numba.gdb_breakpoint() to create additional breakpoints instead.

Relevant documentation is available here:
https://numba.pydata.org/numba-doc/latest/user/troubleshoot.html/troubleshoot.html#using-numba-s-direct-gdb-bindings-in-nopython-mode

Conflicting calls found at:
 %s"""
        udu__mxwdo = '\n'.join([x.strformat() for x in xyfk__pwunb])
        raise errors.UnsupportedError(msg % udu__mxwdo)


if _check_numba_change:
    lines = inspect.getsource(numba.core.ir_utils.raise_on_unsupported_feature)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '237a4fe8395a40899279c718bc3754102cd2577463ef2f48daceea78d79b2d5e':
        warnings.warn(
            'numba.core.ir_utils.raise_on_unsupported_feature has changed')
numba.core.ir_utils.raise_on_unsupported_feature = raise_on_unsupported_feature
numba.core.typed_passes.raise_on_unsupported_feature = (
    raise_on_unsupported_feature)


@typeof_impl.register(dict)
def _typeof_dict(val, c):
    if len(val) == 0:
        raise ValueError('Cannot type empty dict')
    qolux__rpok, udil__tquzm = next(iter(val.items()))
    wwzxt__ggv = typeof_impl(qolux__rpok, c)
    smaqd__nbhc = typeof_impl(udil__tquzm, c)
    if wwzxt__ggv is None or smaqd__nbhc is None:
        raise ValueError(
            f'Cannot type dict element type {type(qolux__rpok)}, {type(udil__tquzm)}'
            )
    return types.DictType(wwzxt__ggv, smaqd__nbhc)


def unbox_dicttype(typ, val, c):
    from llvmlite import ir as lir
    from numba.typed import dictobject
    from numba.typed.typeddict import Dict
    context = c.context
    lpikk__fhb = cgutils.alloca_once_value(c.builder, val)
    vgn__xaky = c.pyapi.object_hasattr_string(val, '_opaque')
    hnij__wetz = c.builder.icmp_unsigned('==', vgn__xaky, lir.Constant(
        vgn__xaky.type, 0))
    wsc__wezg = typ.key_type
    miob__bdt = typ.value_type

    def make_dict():
        return numba.typed.Dict.empty(wsc__wezg, miob__bdt)

    def copy_dict(out_dict, in_dict):
        for qolux__rpok, udil__tquzm in in_dict.items():
            out_dict[qolux__rpok] = udil__tquzm
    with c.builder.if_then(hnij__wetz):
        toyn__lou = c.pyapi.unserialize(c.pyapi.serialize_object(make_dict))
        llylj__hya = c.pyapi.call_function_objargs(toyn__lou, [])
        lbn__xdj = c.pyapi.unserialize(c.pyapi.serialize_object(copy_dict))
        c.pyapi.call_function_objargs(lbn__xdj, [llylj__hya, val])
        c.builder.store(llylj__hya, lpikk__fhb)
    val = c.builder.load(lpikk__fhb)
    uvz__jfy = c.pyapi.unserialize(c.pyapi.serialize_object(Dict))
    eqtvb__ypwv = c.pyapi.object_type(val)
    lxy__ttzux = c.builder.icmp_unsigned('==', eqtvb__ypwv, uvz__jfy)
    with c.builder.if_else(lxy__ttzux) as (tgno__txe, ojxtm__bddnk):
        with tgno__txe:
            xilfl__fkpb = c.pyapi.object_getattr_string(val, '_opaque')
            xtx__erdb = types.MemInfoPointer(types.voidptr)
            mps__vpw = c.unbox(xtx__erdb, xilfl__fkpb)
            mi = mps__vpw.value
            pxxqe__alfly = xtx__erdb, typeof(typ)

            def convert(mi, typ):
                return dictobject._from_meminfo(mi, typ)
            sig = signature(typ, *pxxqe__alfly)
            usfv__vqz = context.get_constant_null(pxxqe__alfly[1])
            args = mi, usfv__vqz
            czi__rjjcr, fncmb__akpc = c.pyapi.call_jit_code(convert, sig, args)
            c.context.nrt.decref(c.builder, typ, fncmb__akpc)
            c.pyapi.decref(xilfl__fkpb)
            yaszy__fjqa = c.builder.basic_block
        with ojxtm__bddnk:
            c.pyapi.err_format('PyExc_TypeError',
                "can't unbox a %S as a %S", eqtvb__ypwv, uvz__jfy)
            wdec__pzlgs = c.builder.basic_block
    jpazu__mfiwc = c.builder.phi(fncmb__akpc.type)
    cvt__cel = c.builder.phi(czi__rjjcr.type)
    jpazu__mfiwc.add_incoming(fncmb__akpc, yaszy__fjqa)
    jpazu__mfiwc.add_incoming(fncmb__akpc.type(None), wdec__pzlgs)
    cvt__cel.add_incoming(czi__rjjcr, yaszy__fjqa)
    cvt__cel.add_incoming(cgutils.true_bit, wdec__pzlgs)
    c.pyapi.decref(uvz__jfy)
    c.pyapi.decref(eqtvb__ypwv)
    with c.builder.if_then(hnij__wetz):
        c.pyapi.decref(val)
    return NativeValue(jpazu__mfiwc, is_error=cvt__cel)


import numba.typed.typeddict
if _check_numba_change:
    lines = inspect.getsource(numba.core.pythonapi._unboxers.functions[
        numba.core.types.DictType])
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '5f6f183b94dc57838538c668a54c2476576c85d8553843f3219f5162c61e7816':
        warnings.warn('unbox_dicttype has changed')
numba.core.pythonapi._unboxers.functions[types.DictType] = unbox_dicttype


def op_DICT_UPDATE_byteflow(self, state, inst):
    value = state.pop()
    index = inst.arg
    target = state.peek(index)
    updatevar = state.make_temp()
    res = state.make_temp()
    state.append(inst, target=target, value=value, updatevar=updatevar, res=res
        )


if _check_numba_change:
    if hasattr(numba.core.byteflow.TraceRunner, 'op_DICT_UPDATE'):
        warnings.warn(
            'numba.core.byteflow.TraceRunner.op_DICT_UPDATE has changed')
numba.core.byteflow.TraceRunner.op_DICT_UPDATE = op_DICT_UPDATE_byteflow


def op_DICT_UPDATE_interpreter(self, inst, target, value, updatevar, res):
    from numba.core import ir
    target = self.get(target)
    value = self.get(value)
    ilojx__gteem = ir.Expr.getattr(target, 'update', loc=self.loc)
    self.store(value=ilojx__gteem, name=updatevar)
    qzm__aor = ir.Expr.call(self.get(updatevar), (value,), (), loc=self.loc)
    self.store(value=qzm__aor, name=res)


if _check_numba_change:
    if hasattr(numba.core.interpreter.Interpreter, 'op_DICT_UPDATE'):
        warnings.warn(
            'numba.core.interpreter.Interpreter.op_DICT_UPDATE has changed')
numba.core.interpreter.Interpreter.op_DICT_UPDATE = op_DICT_UPDATE_interpreter


@numba.extending.overload_method(numba.core.types.DictType, 'update')
def ol_dict_update(d, other):
    if not isinstance(d, numba.core.types.DictType):
        return
    if not isinstance(other, numba.core.types.DictType):
        return

    def impl(d, other):
        for qolux__rpok, udil__tquzm in other.items():
            d[qolux__rpok] = udil__tquzm
    return impl


if _check_numba_change:
    if hasattr(numba.core.interpreter.Interpreter, 'ol_dict_update'):
        warnings.warn('numba.typed.dictobject.ol_dict_update has changed')


def op_CALL_FUNCTION_EX_byteflow(self, state, inst):
    from numba.core.utils import PYVERSION
    if inst.arg & 1 and PYVERSION != (3, 10):
        errmsg = 'CALL_FUNCTION_EX with **kwargs not supported'
        raise errors.UnsupportedError(errmsg)
    if inst.arg & 1:
        varkwarg = state.pop()
    else:
        varkwarg = None
    vararg = state.pop()
    func = state.pop()
    res = state.make_temp()
    state.append(inst, func=func, vararg=vararg, varkwarg=varkwarg, res=res)
    state.push(res)


if _check_numba_change:
    lines = inspect.getsource(numba.core.byteflow.TraceRunner.
        op_CALL_FUNCTION_EX)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '349e7cfd27f5dab80fe15a7728c5f098f3f225ba8512d84331e39d01e863c6d4':
        warnings.warn(
            'numba.core.byteflow.TraceRunner.op_CALL_FUNCTION_EX has changed')
numba.core.byteflow.TraceRunner.op_CALL_FUNCTION_EX = (
    op_CALL_FUNCTION_EX_byteflow)


def op_CALL_FUNCTION_EX_interpreter(self, inst, func, vararg, varkwarg, res):
    func = self.get(func)
    vararg = self.get(vararg)
    if varkwarg is not None:
        varkwarg = self.get(varkwarg)
    idea__ggdyg = ir.Expr.call(func, [], [], loc=self.loc, vararg=vararg,
        varkwarg=varkwarg)
    self.store(idea__ggdyg, res)


if _check_numba_change:
    lines = inspect.getsource(numba.core.interpreter.Interpreter.
        op_CALL_FUNCTION_EX)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '84846e5318ab7ccc8f9abaae6ab9e0ca879362648196f9d4b0ffb91cf2e01f5d':
        warnings.warn(
            'numba.core.interpreter.Interpreter.op_CALL_FUNCTION_EX has changed'
            )
numba.core.interpreter.Interpreter.op_CALL_FUNCTION_EX = (
    op_CALL_FUNCTION_EX_interpreter)


@classmethod
def ir_expr_call(cls, func, args, kws, loc, vararg=None, varkwarg=None,
    target=None):
    assert isinstance(func, ir.Var)
    assert isinstance(loc, ir.Loc)
    op = 'call'
    return cls(op=op, loc=loc, func=func, args=args, kws=kws, vararg=vararg,
        varkwarg=varkwarg, target=target)


if _check_numba_change:
    lines = inspect.getsource(ir.Expr.call)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '665601d0548d4f648d454492e542cb8aa241107a8df6bc68d0eec664c9ada738':
        warnings.warn('ir.Expr.call has changed')
ir.Expr.call = ir_expr_call


@staticmethod
def define_untyped_pipeline(state, name='untyped'):
    from numba.core.compiler_machinery import PassManager
    from numba.core.untyped_passes import DeadBranchPrune, FindLiterallyCalls, FixupArgs, GenericRewrites, InlineClosureLikes, InlineInlinables, IRProcessing, LiteralPropagationSubPipelinePass, LiteralUnroll, MakeFunctionToJitFunction, ReconstructSSA, RewriteSemanticConstants, TranslateByteCode, WithLifting
    from numba.core.utils import PYVERSION
    mrka__bbia = PassManager(name)
    if state.func_ir is None:
        mrka__bbia.add_pass(TranslateByteCode, 'analyzing bytecode')
        if PYVERSION == (3, 10):
            mrka__bbia.add_pass(Bodo310ByteCodePass,
                'Apply Python 3.10 bytecode changes')
        mrka__bbia.add_pass(FixupArgs, 'fix up args')
    mrka__bbia.add_pass(IRProcessing, 'processing IR')
    mrka__bbia.add_pass(WithLifting, 'Handle with contexts')
    mrka__bbia.add_pass(InlineClosureLikes,
        'inline calls to locally defined closures')
    if not state.flags.no_rewrites:
        mrka__bbia.add_pass(RewriteSemanticConstants,
            'rewrite semantic constants')
        mrka__bbia.add_pass(DeadBranchPrune, 'dead branch pruning')
        mrka__bbia.add_pass(GenericRewrites, 'nopython rewrites')
    mrka__bbia.add_pass(MakeFunctionToJitFunction,
        'convert make_function into JIT functions')
    mrka__bbia.add_pass(InlineInlinables, 'inline inlinable functions')
    if not state.flags.no_rewrites:
        mrka__bbia.add_pass(DeadBranchPrune, 'dead branch pruning')
    mrka__bbia.add_pass(FindLiterallyCalls, 'find literally calls')
    mrka__bbia.add_pass(LiteralUnroll, 'handles literal_unroll')
    if state.flags.enable_ssa:
        mrka__bbia.add_pass(ReconstructSSA, 'ssa')
    mrka__bbia.add_pass(LiteralPropagationSubPipelinePass,
        'Literal propagation')
    mrka__bbia.finalize()
    return mrka__bbia


if _check_numba_change:
    lines = inspect.getsource(numba.core.compiler.DefaultPassBuilder.
        define_untyped_pipeline)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'fc5a0665658cc30588a78aca984ac2d323d5d3a45dce538cc62688530c772896':
        warnings.warn(
            'numba.core.compiler.DefaultPassBuilder.define_untyped_pipeline has changed'
            )
numba.core.compiler.DefaultPassBuilder.define_untyped_pipeline = (
    define_untyped_pipeline)


def mul_list_generic(self, args, kws):
    a, nzie__sfne = args
    if isinstance(a, types.List) and isinstance(nzie__sfne, types.Integer):
        return signature(a, a, types.intp)
    elif isinstance(a, types.Integer) and isinstance(nzie__sfne, types.List):
        return signature(nzie__sfne, types.intp, nzie__sfne)


if _check_numba_change:
    lines = inspect.getsource(numba.core.typing.listdecl.MulList.generic)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '95882385a8ffa67aa576e8169b9ee6b3197e0ad3d5def4b47fa65ce8cd0f1575':
        warnings.warn('numba.core.typing.listdecl.MulList.generic has changed')
numba.core.typing.listdecl.MulList.generic = mul_list_generic


@lower_builtin(operator.mul, types.Integer, types.List)
def list_mul(context, builder, sig, args):
    from llvmlite import ir as lir
    from numba.core.imputils import impl_ret_new_ref
    from numba.cpython.listobj import ListInstance
    if isinstance(sig.args[0], types.List):
        ihcc__zxqwv, qqvug__wlt = 0, 1
    else:
        ihcc__zxqwv, qqvug__wlt = 1, 0
    fjyg__ydf = ListInstance(context, builder, sig.args[ihcc__zxqwv], args[
        ihcc__zxqwv])
    jki__wthmu = fjyg__ydf.size
    eab__gsdt = args[qqvug__wlt]
    gse__qedw = lir.Constant(eab__gsdt.type, 0)
    eab__gsdt = builder.select(cgutils.is_neg_int(builder, eab__gsdt),
        gse__qedw, eab__gsdt)
    siiys__bhxsk = builder.mul(eab__gsdt, jki__wthmu)
    esi__mtbj = ListInstance.allocate(context, builder, sig.return_type,
        siiys__bhxsk)
    esi__mtbj.size = siiys__bhxsk
    with cgutils.for_range_slice(builder, gse__qedw, siiys__bhxsk,
        jki__wthmu, inc=True) as (brrl__pgqx, _):
        with cgutils.for_range(builder, jki__wthmu) as ukg__ufpd:
            value = fjyg__ydf.getitem(ukg__ufpd.index)
            esi__mtbj.setitem(builder.add(ukg__ufpd.index, brrl__pgqx),
                value, incref=True)
    return impl_ret_new_ref(context, builder, sig.return_type, esi__mtbj.value)


def unify_pairs(self, first, second):
    from numba.core.typeconv import Conversion
    if first == second:
        return first
    if first is types.undefined:
        return second
    elif second is types.undefined:
        return first
    if first is types.unknown or second is types.unknown:
        return types.unknown
    wtjo__xubi = first.unify(self, second)
    if wtjo__xubi is not None:
        return wtjo__xubi
    wtjo__xubi = second.unify(self, first)
    if wtjo__xubi is not None:
        return wtjo__xubi
    zejt__kuw = self.can_convert(fromty=first, toty=second)
    if zejt__kuw is not None and zejt__kuw <= Conversion.safe:
        return second
    zejt__kuw = self.can_convert(fromty=second, toty=first)
    if zejt__kuw is not None and zejt__kuw <= Conversion.safe:
        return first
    if isinstance(first, types.Literal) or isinstance(second, types.Literal):
        first = types.unliteral(first)
        second = types.unliteral(second)
        return self.unify_pairs(first, second)
    return None


if _check_numba_change:
    lines = inspect.getsource(numba.core.typing.context.BaseContext.unify_pairs
        )
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'f0eaf4cfdf1537691de26efd24d7e320f7c3f10d35e9aefe70cb946b3be0008c':
        warnings.warn(
            'numba.core.typing.context.BaseContext.unify_pairs has changed')
numba.core.typing.context.BaseContext.unify_pairs = unify_pairs


def _native_set_to_python_list(typ, payload, c):
    from llvmlite import ir
    siiys__bhxsk = payload.used
    listobj = c.pyapi.list_new(siiys__bhxsk)
    emvv__ays = cgutils.is_not_null(c.builder, listobj)
    with c.builder.if_then(emvv__ays, likely=True):
        index = cgutils.alloca_once_value(c.builder, ir.Constant(
            siiys__bhxsk.type, 0))
        with payload._iterate() as ukg__ufpd:
            i = c.builder.load(index)
            item = ukg__ufpd.entry.key
            c.context.nrt.incref(c.builder, typ.dtype, item)
            itemobj = c.box(typ.dtype, item)
            c.pyapi.list_setitem(listobj, i, itemobj)
            i = c.builder.add(i, ir.Constant(i.type, 1))
            c.builder.store(i, index)
    return emvv__ays, listobj


def _lookup(self, item, h, for_insert=False):
    from llvmlite import ir
    context = self._context
    builder = self._builder
    suft__iqq = h.type
    ezzz__qbn = self.mask
    dtype = self._ty.dtype
    zkldj__pcuu = context.typing_context
    fnty = zkldj__pcuu.resolve_value_type(operator.eq)
    sig = fnty.get_call_type(zkldj__pcuu, (dtype, dtype), {})
    xmb__bocja = context.get_function(fnty, sig)
    quv__seh = ir.Constant(suft__iqq, 1)
    wau__llutx = ir.Constant(suft__iqq, 5)
    cqqi__hvov = cgutils.alloca_once_value(builder, h)
    index = cgutils.alloca_once_value(builder, builder.and_(h, ezzz__qbn))
    if for_insert:
        kkger__ibuyq = ezzz__qbn.type(-1)
        tlpq__qiwys = cgutils.alloca_once_value(builder, kkger__ibuyq)
    wipik__tzjp = builder.append_basic_block('lookup.body')
    cojab__fyd = builder.append_basic_block('lookup.found')
    nhj__uoi = builder.append_basic_block('lookup.not_found')
    oyni__qftyc = builder.append_basic_block('lookup.end')

    def check_entry(i):
        entry = self.get_entry(i)
        fcltk__xeg = entry.hash
        with builder.if_then(builder.icmp_unsigned('==', h, fcltk__xeg)):
            shwmt__srqyq = xmb__bocja(builder, (item, entry.key))
            with builder.if_then(shwmt__srqyq):
                builder.branch(cojab__fyd)
        with builder.if_then(numba.cpython.setobj.is_hash_empty(context,
            builder, fcltk__xeg)):
            builder.branch(nhj__uoi)
        if for_insert:
            with builder.if_then(numba.cpython.setobj.is_hash_deleted(
                context, builder, fcltk__xeg)):
                oda__txhgl = builder.load(tlpq__qiwys)
                oda__txhgl = builder.select(builder.icmp_unsigned('==',
                    oda__txhgl, kkger__ibuyq), i, oda__txhgl)
                builder.store(oda__txhgl, tlpq__qiwys)
    with cgutils.for_range(builder, ir.Constant(suft__iqq, numba.cpython.
        setobj.LINEAR_PROBES)):
        i = builder.load(index)
        check_entry(i)
        i = builder.add(i, quv__seh)
        i = builder.and_(i, ezzz__qbn)
        builder.store(i, index)
    builder.branch(wipik__tzjp)
    with builder.goto_block(wipik__tzjp):
        i = builder.load(index)
        check_entry(i)
        qvct__ifec = builder.load(cqqi__hvov)
        qvct__ifec = builder.lshr(qvct__ifec, wau__llutx)
        i = builder.add(quv__seh, builder.mul(i, wau__llutx))
        i = builder.and_(ezzz__qbn, builder.add(i, qvct__ifec))
        builder.store(i, index)
        builder.store(qvct__ifec, cqqi__hvov)
        builder.branch(wipik__tzjp)
    with builder.goto_block(nhj__uoi):
        if for_insert:
            i = builder.load(index)
            oda__txhgl = builder.load(tlpq__qiwys)
            i = builder.select(builder.icmp_unsigned('==', oda__txhgl,
                kkger__ibuyq), i, oda__txhgl)
            builder.store(i, index)
        builder.branch(oyni__qftyc)
    with builder.goto_block(cojab__fyd):
        builder.branch(oyni__qftyc)
    builder.position_at_end(oyni__qftyc)
    haq__vrze = builder.phi(ir.IntType(1), 'found')
    haq__vrze.add_incoming(cgutils.true_bit, cojab__fyd)
    haq__vrze.add_incoming(cgutils.false_bit, nhj__uoi)
    return haq__vrze, builder.load(index)


def _add_entry(self, payload, entry, item, h, do_resize=True):
    context = self._context
    builder = self._builder
    tdo__samhm = entry.hash
    entry.hash = h
    context.nrt.incref(builder, self._ty.dtype, item)
    entry.key = item
    molc__ticz = payload.used
    quv__seh = ir.Constant(molc__ticz.type, 1)
    molc__ticz = payload.used = builder.add(molc__ticz, quv__seh)
    with builder.if_then(numba.cpython.setobj.is_hash_empty(context,
        builder, tdo__samhm), likely=True):
        payload.fill = builder.add(payload.fill, quv__seh)
    if do_resize:
        self.upsize(molc__ticz)
    self.set_dirty(True)


def _add_key(self, payload, item, h, do_resize=True):
    from llvmlite import ir
    context = self._context
    builder = self._builder
    haq__vrze, i = payload._lookup(item, h, for_insert=True)
    eveng__ermw = builder.not_(haq__vrze)
    with builder.if_then(eveng__ermw):
        entry = payload.get_entry(i)
        tdo__samhm = entry.hash
        entry.hash = h
        context.nrt.incref(builder, self._ty.dtype, item)
        entry.key = item
        molc__ticz = payload.used
        quv__seh = ir.Constant(molc__ticz.type, 1)
        molc__ticz = payload.used = builder.add(molc__ticz, quv__seh)
        with builder.if_then(numba.cpython.setobj.is_hash_empty(context,
            builder, tdo__samhm), likely=True):
            payload.fill = builder.add(payload.fill, quv__seh)
        if do_resize:
            self.upsize(molc__ticz)
        self.set_dirty(True)


def _remove_entry(self, payload, entry, do_resize=True):
    from llvmlite import ir
    entry.hash = ir.Constant(entry.hash.type, numba.cpython.setobj.DELETED)
    self._context.nrt.decref(self._builder, self._ty.dtype, entry.key)
    molc__ticz = payload.used
    quv__seh = ir.Constant(molc__ticz.type, 1)
    molc__ticz = payload.used = self._builder.sub(molc__ticz, quv__seh)
    if do_resize:
        self.downsize(molc__ticz)
    self.set_dirty(True)


def pop(self):
    context = self._context
    builder = self._builder
    igj__cev = context.get_value_type(self._ty.dtype)
    key = cgutils.alloca_once(builder, igj__cev)
    payload = self.payload
    with payload._next_entry() as entry:
        builder.store(entry.key, key)
        context.nrt.incref(builder, self._ty.dtype, entry.key)
        self._remove_entry(payload, entry)
    return builder.load(key)


def _resize(self, payload, nentries, errmsg):
    context = self._context
    builder = self._builder
    aowe__npctr = payload
    emvv__ays = self._allocate_payload(nentries, realloc=True)
    with builder.if_then(builder.not_(emvv__ays), likely=False):
        context.call_conv.return_user_exc(builder, MemoryError, (errmsg,))
    payload = self.payload
    with aowe__npctr._iterate() as ukg__ufpd:
        entry = ukg__ufpd.entry
        self._add_key(payload, entry.key, entry.hash, do_resize=False)
        context.nrt.decref(builder, self._ty.dtype, entry.key)
    self._free_payload(aowe__npctr.ptr)


def _replace_payload(self, nentries):
    context = self._context
    builder = self._builder
    with self.payload._iterate() as ukg__ufpd:
        entry = ukg__ufpd.entry
        context.nrt.decref(builder, self._ty.dtype, entry.key)
    self._free_payload(self.payload.ptr)
    emvv__ays = self._allocate_payload(nentries, realloc=True)
    with builder.if_then(builder.not_(emvv__ays), likely=False):
        context.call_conv.return_user_exc(builder, MemoryError, (
            'cannot reallocate set',))


def _allocate_payload(self, nentries, realloc=False):
    from llvmlite import ir
    context = self._context
    builder = self._builder
    emvv__ays = cgutils.alloca_once_value(builder, cgutils.true_bit)
    suft__iqq = context.get_value_type(types.intp)
    gse__qedw = ir.Constant(suft__iqq, 0)
    quv__seh = ir.Constant(suft__iqq, 1)
    rvavz__pdixq = context.get_data_type(types.SetPayload(self._ty))
    vsxv__opzwt = context.get_abi_sizeof(rvavz__pdixq)
    exoro__iyz = self._entrysize
    vsxv__opzwt -= exoro__iyz
    gvhw__emtc, lqo__zxtp = cgutils.muladd_with_overflow(builder, nentries,
        ir.Constant(suft__iqq, exoro__iyz), ir.Constant(suft__iqq, vsxv__opzwt)
        )
    with builder.if_then(lqo__zxtp, likely=False):
        builder.store(cgutils.false_bit, emvv__ays)
    with builder.if_then(builder.load(emvv__ays), likely=True):
        if realloc:
            gbkik__jgjde = self._set.meminfo
            stuv__chc = context.nrt.meminfo_varsize_alloc(builder,
                gbkik__jgjde, size=gvhw__emtc)
            mldz__toyvt = cgutils.is_null(builder, stuv__chc)
        else:
            iaaki__dfbhd = _imp_dtor(context, builder.module, self._ty)
            gbkik__jgjde = context.nrt.meminfo_new_varsize_dtor(builder,
                gvhw__emtc, builder.bitcast(iaaki__dfbhd, cgutils.voidptr_t))
            mldz__toyvt = cgutils.is_null(builder, gbkik__jgjde)
        with builder.if_else(mldz__toyvt, likely=False) as (sfmdi__dupam,
            tgiq__gpnl):
            with sfmdi__dupam:
                builder.store(cgutils.false_bit, emvv__ays)
            with tgiq__gpnl:
                if not realloc:
                    self._set.meminfo = gbkik__jgjde
                    self._set.parent = context.get_constant_null(types.pyobject
                        )
                payload = self.payload
                cgutils.memset(builder, payload.ptr, gvhw__emtc, 255)
                payload.used = gse__qedw
                payload.fill = gse__qedw
                payload.finger = gse__qedw
                xtzrb__qfx = builder.sub(nentries, quv__seh)
                payload.mask = xtzrb__qfx
    return builder.load(emvv__ays)


def _copy_payload(self, src_payload):
    from llvmlite import ir
    context = self._context
    builder = self._builder
    emvv__ays = cgutils.alloca_once_value(builder, cgutils.true_bit)
    suft__iqq = context.get_value_type(types.intp)
    gse__qedw = ir.Constant(suft__iqq, 0)
    quv__seh = ir.Constant(suft__iqq, 1)
    rvavz__pdixq = context.get_data_type(types.SetPayload(self._ty))
    vsxv__opzwt = context.get_abi_sizeof(rvavz__pdixq)
    exoro__iyz = self._entrysize
    vsxv__opzwt -= exoro__iyz
    ezzz__qbn = src_payload.mask
    nentries = builder.add(quv__seh, ezzz__qbn)
    gvhw__emtc = builder.add(ir.Constant(suft__iqq, vsxv__opzwt), builder.
        mul(ir.Constant(suft__iqq, exoro__iyz), nentries))
    with builder.if_then(builder.load(emvv__ays), likely=True):
        iaaki__dfbhd = _imp_dtor(context, builder.module, self._ty)
        gbkik__jgjde = context.nrt.meminfo_new_varsize_dtor(builder,
            gvhw__emtc, builder.bitcast(iaaki__dfbhd, cgutils.voidptr_t))
        mldz__toyvt = cgutils.is_null(builder, gbkik__jgjde)
        with builder.if_else(mldz__toyvt, likely=False) as (sfmdi__dupam,
            tgiq__gpnl):
            with sfmdi__dupam:
                builder.store(cgutils.false_bit, emvv__ays)
            with tgiq__gpnl:
                self._set.meminfo = gbkik__jgjde
                payload = self.payload
                payload.used = src_payload.used
                payload.fill = src_payload.fill
                payload.finger = gse__qedw
                payload.mask = ezzz__qbn
                cgutils.raw_memcpy(builder, payload.entries, src_payload.
                    entries, nentries, exoro__iyz)
                with src_payload._iterate() as ukg__ufpd:
                    context.nrt.incref(builder, self._ty.dtype, ukg__ufpd.
                        entry.key)
    return builder.load(emvv__ays)


def _imp_dtor(context, module, set_type):
    from llvmlite import ir
    domay__ccxgx = context.get_value_type(types.voidptr)
    eprt__bilyc = context.get_value_type(types.uintp)
    fnty = ir.FunctionType(ir.VoidType(), [domay__ccxgx, eprt__bilyc,
        domay__ccxgx])
    dzjv__yohb = f'_numba_set_dtor_{set_type}'
    fn = cgutils.get_or_insert_function(module, fnty, name=dzjv__yohb)
    if fn.is_declaration:
        fn.linkage = 'linkonce_odr'
        builder = ir.IRBuilder(fn.append_basic_block())
        dpw__dfoi = builder.bitcast(fn.args[0], cgutils.voidptr_t.as_pointer())
        payload = numba.cpython.setobj._SetPayload(context, builder,
            set_type, dpw__dfoi)
        with payload._iterate() as ukg__ufpd:
            entry = ukg__ufpd.entry
            context.nrt.decref(builder, set_type.dtype, entry.key)
        builder.ret_void()
    return fn


@lower_builtin(set, types.IterableType)
def set_constructor(context, builder, sig, args):
    set_type = sig.return_type
    zrk__blk, = sig.args
    jakc__aocxx, = args
    cher__nszsi = numba.core.imputils.call_len(context, builder, zrk__blk,
        jakc__aocxx)
    inst = numba.cpython.setobj.SetInstance.allocate(context, builder,
        set_type, cher__nszsi)
    with numba.core.imputils.for_iter(context, builder, zrk__blk, jakc__aocxx
        ) as ukg__ufpd:
        inst.add(ukg__ufpd.value)
        context.nrt.decref(builder, set_type.dtype, ukg__ufpd.value)
    return numba.core.imputils.impl_ret_new_ref(context, builder, set_type,
        inst.value)


@lower_builtin('set.update', types.Set, types.IterableType)
def set_update(context, builder, sig, args):
    inst = numba.cpython.setobj.SetInstance(context, builder, sig.args[0],
        args[0])
    zrk__blk = sig.args[1]
    jakc__aocxx = args[1]
    cher__nszsi = numba.core.imputils.call_len(context, builder, zrk__blk,
        jakc__aocxx)
    if cher__nszsi is not None:
        krgdk__zdttm = builder.add(inst.payload.used, cher__nszsi)
        inst.upsize(krgdk__zdttm)
    with numba.core.imputils.for_iter(context, builder, zrk__blk, jakc__aocxx
        ) as ukg__ufpd:
        kjpm__lnwv = context.cast(builder, ukg__ufpd.value, zrk__blk.dtype,
            inst.dtype)
        inst.add(kjpm__lnwv)
        context.nrt.decref(builder, zrk__blk.dtype, ukg__ufpd.value)
    if cher__nszsi is not None:
        inst.downsize(inst.payload.used)
    return context.get_dummy_value()


if _check_numba_change:
    for name, orig, hash in ((
        'numba.core.boxing._native_set_to_python_list', numba.core.boxing.
        _native_set_to_python_list,
        'b47f3d5e582c05d80899ee73e1c009a7e5121e7a660d42cb518bb86933f3c06f'),
        ('numba.cpython.setobj._SetPayload._lookup', numba.cpython.setobj.
        _SetPayload._lookup,
        'c797b5399d7b227fe4eea3a058b3d3103f59345699388afb125ae47124bee395'),
        ('numba.cpython.setobj.SetInstance._add_entry', numba.cpython.
        setobj.SetInstance._add_entry,
        'c5ed28a5fdb453f242e41907cb792b66da2df63282c17abe0b68fc46782a7f94'),
        ('numba.cpython.setobj.SetInstance._add_key', numba.cpython.setobj.
        SetInstance._add_key,
        '324d6172638d02a361cfa0ca7f86e241e5a56a008d4ab581a305f9ae5ea4a75f'),
        ('numba.cpython.setobj.SetInstance._remove_entry', numba.cpython.
        setobj.SetInstance._remove_entry,
        '2c441b00daac61976e673c0e738e8e76982669bd2851951890dd40526fa14da1'),
        ('numba.cpython.setobj.SetInstance.pop', numba.cpython.setobj.
        SetInstance.pop,
        '1a7b7464cbe0577f2a38f3af9acfef6d4d25d049b1e216157275fbadaab41d1b'),
        ('numba.cpython.setobj.SetInstance._resize', numba.cpython.setobj.
        SetInstance._resize,
        '5ca5c2ba4f8c4bf546fde106b9c2656d4b22a16d16e163fb64c5d85ea4d88746'),
        ('numba.cpython.setobj.SetInstance._replace_payload', numba.cpython
        .setobj.SetInstance._replace_payload,
        'ada75a6c85828bff69c8469538c1979801f560a43fb726221a9c21bf208ae78d'),
        ('numba.cpython.setobj.SetInstance._allocate_payload', numba.
        cpython.setobj.SetInstance._allocate_payload,
        '2e80c419df43ebc71075b4f97fc1701c10dbc576aed248845e176b8d5829e61b'),
        ('numba.cpython.setobj.SetInstance._copy_payload', numba.cpython.
        setobj.SetInstance._copy_payload,
        '0885ac36e1eb5a0a0fc4f5d91e54b2102b69e536091fed9f2610a71d225193ec'),
        ('numba.cpython.setobj.set_constructor', numba.cpython.setobj.
        set_constructor,
        '3d521a60c3b8eaf70aa0f7267427475dfddd8f5e5053b5bfe309bb5f1891b0ce'),
        ('numba.cpython.setobj.set_update', numba.cpython.setobj.set_update,
        '965c4f7f7abcea5cbe0491b602e6d4bcb1800fa1ec39b1ffccf07e1bc56051c3')):
        lines = inspect.getsource(orig)
        if hashlib.sha256(lines.encode()).hexdigest() != hash:
            warnings.warn(f'{name} has changed')
        orig = new
numba.core.boxing._native_set_to_python_list = _native_set_to_python_list
numba.cpython.setobj._SetPayload._lookup = _lookup
numba.cpython.setobj.SetInstance._add_entry = _add_entry
numba.cpython.setobj.SetInstance._add_key = _add_key
numba.cpython.setobj.SetInstance._remove_entry = _remove_entry
numba.cpython.setobj.SetInstance.pop = pop
numba.cpython.setobj.SetInstance._resize = _resize
numba.cpython.setobj.SetInstance._replace_payload = _replace_payload
numba.cpython.setobj.SetInstance._allocate_payload = _allocate_payload
numba.cpython.setobj.SetInstance._copy_payload = _copy_payload


def _reduce(self):
    libdata = self.library.serialize_using_object_code()
    typeann = str(self.type_annotation)
    fndesc = self.fndesc
    fndesc.typemap = fndesc.calltypes = None
    referenced_envs = self._find_referenced_environments()
    erls__abnvg = {key: value for key, value in self.metadata.items() if (
        'distributed' in key or 'replicated' in key) and key !=
        'distributed_diagnostics'}
    return (libdata, self.fndesc, self.environment, self.signature, self.
        objectmode, self.lifted, typeann, erls__abnvg, self.reload_init,
        tuple(referenced_envs))


@classmethod
def _rebuild(cls, target_context, libdata, fndesc, env, signature,
    objectmode, lifted, typeann, metadata, reload_init, referenced_envs):
    if reload_init:
        for fn in reload_init:
            fn()
    library = target_context.codegen().unserialize_library(libdata)
    zlvq__rvwq = target_context.get_executable(library, fndesc, env)
    lovxf__xtet = cls(target_context=target_context, typing_context=
        target_context.typing_context, library=library, environment=env,
        entry_point=zlvq__rvwq, fndesc=fndesc, type_annotation=typeann,
        signature=signature, objectmode=objectmode, lifted=lifted,
        typing_error=None, call_helper=None, metadata=metadata, reload_init
        =reload_init, referenced_envs=referenced_envs)
    for env in referenced_envs:
        library.codegen.set_env(env.env_name, env)
    return lovxf__xtet


if _check_numba_change:
    for name, orig, hash in (('numba.core.compiler.CompileResult._reduce',
        numba.core.compiler.CompileResult._reduce,
        '5f86eacfa5202c202b3dc200f1a7a9b6d3f9d1ec16d43a52cb2d580c34fbfa82'),
        ('numba.core.compiler.CompileResult._rebuild', numba.core.compiler.
        CompileResult._rebuild,
        '44fa9dc2255883ab49195d18c3cca8c0ad715d0dd02033bd7e2376152edc4e84')):
        lines = inspect.getsource(orig)
        if hashlib.sha256(lines.encode()).hexdigest() != hash:
            warnings.warn(f'{name} has changed')
        orig = new
numba.core.compiler.CompileResult._reduce = _reduce
numba.core.compiler.CompileResult._rebuild = _rebuild
if _check_numba_change:
    lines = inspect.getsource(numba.core.caching._IPythonCacheLocator.
        get_cache_path)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'eb33b7198697b8ef78edddcf69e58973c44744ff2cb2f54d4015611ad43baed0':
        warnings.warn(
            'numba.core.caching._IPythonCacheLocator.get_cache_path has changed'
            )
if os.environ.get('BODO_PLATFORM_CACHE_LOCATION') is not None:

    def _get_cache_path(self):
        return numba.config.CACHE_DIR
    numba.core.caching._IPythonCacheLocator.get_cache_path = _get_cache_path
if _check_numba_change:
    lines = inspect.getsource(numba.core.types.containers.Bytes)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '977423d833eeb4b8fd0c87f55dce7251c107d8d10793fe5723de6e5452da32e2':
        warnings.warn('numba.core.types.containers.Bytes has changed')
numba.core.types.containers.Bytes.slice_is_copy = True
if _check_numba_change:
    lines = inspect.getsource(numba.core.caching._CacheLocator.
        ensure_cache_path)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '906b6f516f76927dfbe69602c335fa151b9f33d40dfe171a9190c0d11627bc03':
        warnings.warn(
            'numba.core.caching._CacheLocator.ensure_cache_path has changed')
if os.environ.get('BODO_PLATFORM_CACHE_LOCATION') is not None:
    import tempfile

    def _ensure_cache_path(self):
        from mpi4py import MPI
        aee__ztj = MPI.COMM_WORLD
        if aee__ztj.Get_rank() == 0:
            wua__rqgzy = self.get_cache_path()
            os.makedirs(wua__rqgzy, exist_ok=True)
            tempfile.TemporaryFile(dir=wua__rqgzy).close()
    numba.core.caching._CacheLocator.ensure_cache_path = _ensure_cache_path


def _analyze_op_call_builtins_len(self, scope, equiv_set, loc, args, kws):
    from numba.parfors.array_analysis import ArrayAnalysis
    require(len(args) == 1)
    var = args[0]
    typ = self.typemap[var.name]
    require(isinstance(typ, types.ArrayCompatible))
    require(not isinstance(typ, types.Bytes))
    shape = equiv_set._get_shape(var)
    return ArrayAnalysis.AnalyzeResult(shape=shape[0], rhs=shape[0])


if _check_numba_change:
    lines = inspect.getsource(numba.parfors.array_analysis.ArrayAnalysis.
        _analyze_op_call_builtins_len)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '612cbc67e8e462f25f348b2a5dd55595f4201a6af826cffcd38b16cd85fc70f7':
        warnings.warn(
            'numba.parfors.array_analysis.ArrayAnalysis._analyze_op_call_builtins_len has changed'
            )
(numba.parfors.array_analysis.ArrayAnalysis._analyze_op_call_builtins_len
    ) = _analyze_op_call_builtins_len


def generic(self, args, kws):
    assert not kws
    val, = args
    if isinstance(val, (types.Buffer, types.BaseTuple)) and not isinstance(val,
        types.Bytes):
        return signature(types.intp, val)
    elif isinstance(val, types.RangeType):
        return signature(val.dtype, val)


if _check_numba_change:
    lines = inspect.getsource(numba.core.typing.builtins.Len.generic)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '88d54238ebe0896f4s69b7347105a6a68dec443036a61f9e494c1630c62b0fa76':
        warnings.warn('numba.core.typing.builtins.Len.generic has changed')
numba.core.typing.builtins.Len.generic = generic
from numba.cpython import charseq


def _make_constant_bytes(context, builder, nbytes):
    from llvmlite import ir
    bigt__mva = cgutils.create_struct_proxy(charseq.bytes_type)
    isso__vwex = bigt__mva(context, builder)
    if isinstance(nbytes, int):
        nbytes = ir.Constant(isso__vwex.nitems.type, nbytes)
    isso__vwex.meminfo = context.nrt.meminfo_alloc(builder, nbytes)
    isso__vwex.nitems = nbytes
    isso__vwex.itemsize = ir.Constant(isso__vwex.itemsize.type, 1)
    isso__vwex.data = context.nrt.meminfo_data(builder, isso__vwex.meminfo)
    isso__vwex.parent = cgutils.get_null_value(isso__vwex.parent.type)
    isso__vwex.shape = cgutils.pack_array(builder, [isso__vwex.nitems],
        context.get_value_type(types.intp))
    isso__vwex.strides = cgutils.pack_array(builder, [ir.Constant(
        isso__vwex.strides.type.element, 1)], context.get_value_type(types.
        intp))
    return isso__vwex


if _check_numba_change:
    lines = inspect.getsource(charseq._make_constant_bytes)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'b3ed23ad58baff7b935912e3e22f4d8af67423d8fd0e5f1836ba0b3028a6eb18':
        warnings.warn('charseq._make_constant_bytes has changed')
charseq._make_constant_bytes = _make_constant_bytes
