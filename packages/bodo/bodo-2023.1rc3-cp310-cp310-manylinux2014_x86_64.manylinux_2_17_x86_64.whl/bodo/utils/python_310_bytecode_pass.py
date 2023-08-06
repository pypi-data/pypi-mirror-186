"""
transforms the IR to handle bytecode issues in Python 3.10. This
should be removed once https://github.com/numba/numba/pull/7866
is included in Numba 0.56
"""
import operator
import numba
from numba.core import ir
from numba.core.compiler_machinery import FunctionPass, register_pass
from numba.core.errors import UnsupportedError
from numba.core.ir_utils import dprint_func_ir, get_definition, guard


@register_pass(mutates_CFG=False, analysis_only=False)
class Bodo310ByteCodePass(FunctionPass):
    _name = 'bodo_untyped_pass'

    def __init__(self):
        FunctionPass.__init__(self)

    def run_pass(self, state):
        assert state.func_ir
        dprint_func_ir(state.func_ir,
            'starting Bodo 3.10 Bytecode optimizations pass')
        peep_hole_call_function_ex_to_call_function_kw(state.func_ir)
        peep_hole_fuse_dict_add_updates(state.func_ir)
        peep_hole_fuse_tuple_adds(state.func_ir)
        return True


def peep_hole_fuse_tuple_adds(func_ir):
    for npuy__ypo in func_ir.blocks.values():
        new_body = []
        hje__kohj = {}
        for wuvgs__wjwyn, rwr__gklx in enumerate(npuy__ypo.body):
            qixda__dodfc = None
            if isinstance(rwr__gklx, ir.Assign) and isinstance(rwr__gklx.
                value, ir.Expr):
                mdw__cqz = rwr__gklx.target.name
                if rwr__gklx.value.op == 'build_tuple':
                    qixda__dodfc = mdw__cqz
                    hje__kohj[mdw__cqz] = rwr__gklx.value.items
                elif rwr__gklx.value.op == 'binop' and rwr__gklx.value.fn == operator.add and rwr__gklx.value.lhs.name in hje__kohj and rwr__gklx.value.rhs.name in hje__kohj:
                    qixda__dodfc = mdw__cqz
                    new_items = hje__kohj[rwr__gklx.value.lhs.name
                        ] + hje__kohj[rwr__gklx.value.rhs.name]
                    rimw__mty = ir.Expr.build_tuple(new_items, rwr__gklx.
                        value.loc)
                    hje__kohj[mdw__cqz] = new_items
                    del hje__kohj[rwr__gklx.value.lhs.name]
                    del hje__kohj[rwr__gklx.value.rhs.name]
                    if rwr__gklx.value in func_ir._definitions[mdw__cqz]:
                        func_ir._definitions[mdw__cqz].remove(rwr__gklx.value)
                    func_ir._definitions[mdw__cqz].append(rimw__mty)
                    rwr__gklx = ir.Assign(rimw__mty, rwr__gklx.target,
                        rwr__gklx.loc)
            for xtsru__bgtm in rwr__gklx.list_vars():
                if (xtsru__bgtm.name in hje__kohj and xtsru__bgtm.name !=
                    qixda__dodfc):
                    del hje__kohj[xtsru__bgtm.name]
            new_body.append(rwr__gklx)
        npuy__ypo.body = new_body
    return func_ir


def _call_function_ex_replace_kws_small(keyword_expr, new_body, buildmap_idx):
    lwbmy__ppwfo = keyword_expr.items.copy()
    gey__bkb = keyword_expr.value_indexes
    for cnctq__fbtb, vnrt__qfru in gey__bkb.items():
        lwbmy__ppwfo[vnrt__qfru] = cnctq__fbtb, lwbmy__ppwfo[vnrt__qfru][1]
    new_body[buildmap_idx] = None
    return lwbmy__ppwfo


def _call_function_ex_replace_kws_large(body, buildmap_name, buildmap_idx,
    search_end, new_body):
    wegda__wclal = 'CALL_FUNCTION_EX with **kwargs not supported'
    new_body[buildmap_idx] = None
    lwbmy__ppwfo = []
    ozt__bra = buildmap_idx + 1
    while ozt__bra <= search_end:
        ifg__yhc = body[ozt__bra]
        if not (isinstance(ifg__yhc, ir.Assign) and isinstance(ifg__yhc.
            value, ir.Const)):
            raise UnsupportedError(wegda__wclal)
        fed__sdalx = ifg__yhc.target.name
        jum__fyro = ifg__yhc.value.value
        ozt__bra += 1
        kmz__kornc = True
        while ozt__bra <= search_end and kmz__kornc:
            rqq__jxyt = body[ozt__bra]
            if (isinstance(rqq__jxyt, ir.Assign) and isinstance(rqq__jxyt.
                value, ir.Expr) and rqq__jxyt.value.op == 'getattr' and 
                rqq__jxyt.value.value.name == buildmap_name and rqq__jxyt.
                value.attr == '__setitem__'):
                kmz__kornc = False
            else:
                ozt__bra += 1
        if kmz__kornc or ozt__bra == search_end:
            raise UnsupportedError(wegda__wclal)
        zwej__ubnmy = body[ozt__bra + 1]
        if not (isinstance(zwej__ubnmy, ir.Assign) and isinstance(
            zwej__ubnmy.value, ir.Expr) and zwej__ubnmy.value.op == 'call' and
            zwej__ubnmy.value.func.name == rqq__jxyt.target.name and len(
            zwej__ubnmy.value.args) == 2 and zwej__ubnmy.value.args[0].name ==
            fed__sdalx):
            raise UnsupportedError(wegda__wclal)
        lyxsy__lobqt = zwej__ubnmy.value.args[1]
        lwbmy__ppwfo.append((jum__fyro, lyxsy__lobqt))
        new_body[ozt__bra] = None
        new_body[ozt__bra + 1] = None
        ozt__bra += 2
    return lwbmy__ppwfo


def _call_function_ex_replace_args_small(tuple_expr, new_body, buildtuple_idx):
    new_body[buildtuple_idx] = None
    return tuple_expr.items


def _call_function_ex_replace_args_large(vararg_stmt, body, new_body,
    search_end):
    wegda__wclal = 'CALL_FUNCTION_EX with **kwargs not supported'
    ozt__bra = 0
    rybt__fvrqr = []
    if isinstance(vararg_stmt, ir.Assign) and isinstance(vararg_stmt.value,
        ir.Var):
        nbb__cdxa = vararg_stmt.value.name
        new_body[search_end] = None
        search_end -= 1
    else:
        nbb__cdxa = vararg_stmt.target.name
    xtjc__wev = True
    while search_end >= ozt__bra and xtjc__wev:
        tbc__mwb = body[search_end]
        if isinstance(tbc__mwb, ir.Assign
            ) and tbc__mwb.target.name == nbb__cdxa and isinstance(tbc__mwb
            .value, ir.Expr
            ) and tbc__mwb.value.op == 'build_tuple' and not tbc__mwb.value.items:
            xtjc__wev = False
            new_body[search_end] = None
        else:
            if search_end == ozt__bra or not (isinstance(tbc__mwb, ir.
                Assign) and tbc__mwb.target.name == nbb__cdxa and
                isinstance(tbc__mwb.value, ir.Expr) and tbc__mwb.value.op ==
                'binop' and tbc__mwb.value.fn == operator.add):
                raise UnsupportedError(wegda__wclal)
            dzje__jzpy = tbc__mwb.value.lhs.name
            wfcei__hriz = tbc__mwb.value.rhs.name
            tviqb__rlnhl = body[search_end - 1]
            if not (isinstance(tviqb__rlnhl, ir.Assign) and isinstance(
                tviqb__rlnhl.value, ir.Expr) and tviqb__rlnhl.value.op ==
                'build_tuple' and len(tviqb__rlnhl.value.items) == 1):
                raise UnsupportedError(wegda__wclal)
            if tviqb__rlnhl.target.name == dzje__jzpy:
                nbb__cdxa = wfcei__hriz
            elif tviqb__rlnhl.target.name == wfcei__hriz:
                nbb__cdxa = dzje__jzpy
            else:
                raise UnsupportedError(wegda__wclal)
            rybt__fvrqr.append(tviqb__rlnhl.value.items[0])
            new_body[search_end] = None
            new_body[search_end - 1] = None
            search_end -= 2
            nie__qmoa = True
            while search_end >= ozt__bra and nie__qmoa:
                wxet__ivgwk = body[search_end]
                if isinstance(wxet__ivgwk, ir.Assign
                    ) and wxet__ivgwk.target.name == nbb__cdxa:
                    nie__qmoa = False
                else:
                    search_end -= 1
    if xtjc__wev:
        raise UnsupportedError(wegda__wclal)
    return rybt__fvrqr[::-1]


def peep_hole_call_function_ex_to_call_function_kw(func_ir):
    wegda__wclal = 'CALL_FUNCTION_EX with **kwargs not supported'
    for npuy__ypo in func_ir.blocks.values():
        salks__ahg = False
        new_body = []
        for wuvgs__wjwyn, rwr__gklx in enumerate(npuy__ypo.body):
            if (isinstance(rwr__gklx, ir.Assign) and isinstance(rwr__gklx.
                value, ir.Expr) and rwr__gklx.value.op == 'call' and 
                rwr__gklx.value.varkwarg is not None):
                salks__ahg = True
                phl__oee = rwr__gklx.value
                args = phl__oee.args
                lwbmy__ppwfo = phl__oee.kws
                ugjry__rtx = phl__oee.vararg
                zft__mcc = phl__oee.varkwarg
                cdukf__ouk = wuvgs__wjwyn - 1
                fwzq__kiaw = cdukf__ouk
                dszo__xezp = None
                ulkrq__zic = True
                while fwzq__kiaw >= 0 and ulkrq__zic:
                    dszo__xezp = npuy__ypo.body[fwzq__kiaw]
                    if isinstance(dszo__xezp, ir.Assign
                        ) and dszo__xezp.target.name == zft__mcc.name:
                        ulkrq__zic = False
                    else:
                        fwzq__kiaw -= 1
                if lwbmy__ppwfo or ulkrq__zic or not (isinstance(dszo__xezp
                    .value, ir.Expr) and dszo__xezp.value.op == 'build_map'):
                    raise UnsupportedError(wegda__wclal)
                if dszo__xezp.value.items:
                    lwbmy__ppwfo = _call_function_ex_replace_kws_small(
                        dszo__xezp.value, new_body, fwzq__kiaw)
                else:
                    lwbmy__ppwfo = _call_function_ex_replace_kws_large(
                        npuy__ypo.body, zft__mcc.name, fwzq__kiaw, 
                        wuvgs__wjwyn - 1, new_body)
                cdukf__ouk = fwzq__kiaw
                if ugjry__rtx is not None:
                    if args:
                        raise UnsupportedError(wegda__wclal)
                    dwvke__nryv = cdukf__ouk
                    sbmf__yazdd = None
                    ulkrq__zic = True
                    while dwvke__nryv >= 0 and ulkrq__zic:
                        sbmf__yazdd = npuy__ypo.body[dwvke__nryv]
                        if isinstance(sbmf__yazdd, ir.Assign
                            ) and sbmf__yazdd.target.name == ugjry__rtx.name:
                            ulkrq__zic = False
                        else:
                            dwvke__nryv -= 1
                    if ulkrq__zic:
                        raise UnsupportedError(wegda__wclal)
                    if isinstance(sbmf__yazdd.value, ir.Expr
                        ) and sbmf__yazdd.value.op == 'build_tuple':
                        args = _call_function_ex_replace_args_small(sbmf__yazdd
                            .value, new_body, dwvke__nryv)
                    else:
                        args = _call_function_ex_replace_args_large(sbmf__yazdd
                            , npuy__ypo.body, new_body, dwvke__nryv)
                rybmm__aan = ir.Expr.call(phl__oee.func, args, lwbmy__ppwfo,
                    phl__oee.loc, target=phl__oee.target)
                if rwr__gklx.target.name in func_ir._definitions and len(
                    func_ir._definitions[rwr__gklx.target.name]) == 1:
                    func_ir._definitions[rwr__gklx.target.name].clear()
                func_ir._definitions[rwr__gklx.target.name].append(rybmm__aan)
                rwr__gklx = ir.Assign(rybmm__aan, rwr__gklx.target,
                    rwr__gklx.loc)
            new_body.append(rwr__gklx)
        if salks__ahg:
            npuy__ypo.body = [gzr__spm for gzr__spm in new_body if gzr__spm
                 is not None]
    return func_ir


def peep_hole_fuse_dict_add_updates(func_ir):
    for npuy__ypo in func_ir.blocks.values():
        new_body = []
        lit_old_idx = {}
        lit_new_idx = {}
        map_updates = {}
        salks__ahg = False
        for wuvgs__wjwyn, rwr__gklx in enumerate(npuy__ypo.body):
            aud__hvw = True
            zfz__gfokn = None
            if isinstance(rwr__gklx, ir.Assign) and isinstance(rwr__gklx.
                value, ir.Expr):
                if rwr__gklx.value.op == 'build_map':
                    zfz__gfokn = rwr__gklx.target.name
                    lit_old_idx[rwr__gklx.target.name] = wuvgs__wjwyn
                    lit_new_idx[rwr__gklx.target.name] = wuvgs__wjwyn
                    map_updates[rwr__gklx.target.name
                        ] = rwr__gklx.value.items.copy()
                    aud__hvw = False
                elif rwr__gklx.value.op == 'call' and wuvgs__wjwyn > 0:
                    qwgiy__uyp = rwr__gklx.value.func.name
                    rqq__jxyt = npuy__ypo.body[wuvgs__wjwyn - 1]
                    args = rwr__gklx.value.args
                    if (isinstance(rqq__jxyt, ir.Assign) and rqq__jxyt.
                        target.name == qwgiy__uyp and isinstance(rqq__jxyt.
                        value, ir.Expr) and rqq__jxyt.value.op == 'getattr' and
                        rqq__jxyt.value.value.name in lit_old_idx):
                        bch__utuo = rqq__jxyt.value.value.name
                        xwliz__gymrh = rqq__jxyt.value.attr
                        if xwliz__gymrh == '__setitem__':
                            aud__hvw = False
                            map_updates[bch__utuo].append(args)
                            new_body[-1] = None
                        elif xwliz__gymrh == 'update' and args[0
                            ].name in lit_old_idx:
                            aud__hvw = False
                            map_updates[bch__utuo].extend(map_updates[args[
                                0].name])
                            new_body[-1] = None
                        if not aud__hvw:
                            lit_new_idx[bch__utuo] = wuvgs__wjwyn
                            func_ir._definitions[rqq__jxyt.target.name].remove(
                                rqq__jxyt.value)
            if not (isinstance(rwr__gklx, ir.Assign) and isinstance(
                rwr__gklx.value, ir.Expr) and rwr__gklx.value.op ==
                'getattr' and rwr__gklx.value.value.name in lit_old_idx and
                rwr__gklx.value.attr in ('__setitem__', 'update')):
                for xtsru__bgtm in rwr__gklx.list_vars():
                    if (xtsru__bgtm.name in lit_old_idx and xtsru__bgtm.
                        name != zfz__gfokn):
                        _insert_build_map(func_ir, xtsru__bgtm.name,
                            npuy__ypo.body, new_body, lit_old_idx,
                            lit_new_idx, map_updates)
            if aud__hvw:
                new_body.append(rwr__gklx)
            else:
                func_ir._definitions[rwr__gklx.target.name].remove(rwr__gklx
                    .value)
                salks__ahg = True
                new_body.append(None)
        qet__tgni = list(lit_old_idx.keys())
        for ezbw__enprb in qet__tgni:
            _insert_build_map(func_ir, ezbw__enprb, npuy__ypo.body,
                new_body, lit_old_idx, lit_new_idx, map_updates)
        if salks__ahg:
            npuy__ypo.body = [gzr__spm for gzr__spm in new_body if gzr__spm
                 is not None]
    return func_ir


def _insert_build_map(func_ir, name, old_body, new_body, lit_old_idx,
    lit_new_idx, map_updates):
    rybjg__ixhf = lit_old_idx[name]
    leyj__vppc = lit_new_idx[name]
    tlicl__aivw = map_updates[name]
    new_body[leyj__vppc] = _build_new_build_map(func_ir, name, old_body,
        rybjg__ixhf, tlicl__aivw)
    del lit_old_idx[name]
    del lit_new_idx[name]
    del map_updates[name]


def _build_new_build_map(func_ir, name, old_body, old_lineno, new_items):
    rmw__walip = old_body[old_lineno]
    ymk__lhfmv = rmw__walip.target
    uyc__gha = rmw__walip.value
    hyxm__oiksv = []
    jhjg__dfwvq = []
    for cgex__edrj in new_items:
        zcwrg__ftme, cxmgg__urmew = cgex__edrj
        dtfh__hkemo = guard(get_definition, func_ir, zcwrg__ftme)
        if isinstance(dtfh__hkemo, (ir.Const, ir.Global, ir.FreeVar)):
            hyxm__oiksv.append(dtfh__hkemo.value)
        xeh__shlr = guard(get_definition, func_ir, cxmgg__urmew)
        if isinstance(xeh__shlr, (ir.Const, ir.Global, ir.FreeVar)):
            jhjg__dfwvq.append(xeh__shlr.value)
        else:
            jhjg__dfwvq.append(numba.core.interpreter._UNKNOWN_VALUE(
                cxmgg__urmew.name))
    gey__bkb = {}
    if len(hyxm__oiksv) == len(new_items):
        fnb__hrxu = {gzr__spm: zzsvy__tnioa for gzr__spm, zzsvy__tnioa in
            zip(hyxm__oiksv, jhjg__dfwvq)}
        for wuvgs__wjwyn, zcwrg__ftme in enumerate(hyxm__oiksv):
            gey__bkb[zcwrg__ftme] = wuvgs__wjwyn
    else:
        fnb__hrxu = None
    icfmu__neo = ir.Expr.build_map(items=new_items, size=len(new_items),
        literal_value=fnb__hrxu, value_indexes=gey__bkb, loc=uyc__gha.loc)
    func_ir._definitions[name].append(icfmu__neo)
    return ir.Assign(icfmu__neo, ir.Var(ymk__lhfmv.scope, name, ymk__lhfmv.
        loc), icfmu__neo.loc)
