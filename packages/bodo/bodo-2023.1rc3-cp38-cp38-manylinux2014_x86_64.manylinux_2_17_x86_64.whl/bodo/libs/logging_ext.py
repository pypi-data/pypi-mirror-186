"""
JIT support for Python's logging module
"""
import logging
import numba
from numba.core import types
from numba.core.imputils import lower_constant
from numba.core.typing.templates import bound_function
from numba.core.typing.templates import AttributeTemplate, infer_getattr, signature
from numba.extending import NativeValue, box, models, overload_attribute, overload_method, register_model, typeof_impl, unbox
from bodo.utils.typing import create_unsupported_overload, gen_objmode_attr_overload


class LoggingLoggerType(types.Type):

    def __init__(self, is_root=False):
        self.is_root = is_root
        super(LoggingLoggerType, self).__init__(name=
            f'LoggingLoggerType(is_root={is_root})')


@typeof_impl.register(logging.RootLogger)
@typeof_impl.register(logging.Logger)
def typeof_logging(val, c):
    if isinstance(val, logging.RootLogger):
        return LoggingLoggerType(is_root=True)
    else:
        return LoggingLoggerType(is_root=False)


register_model(LoggingLoggerType)(models.OpaqueModel)


@box(LoggingLoggerType)
def box_logging_logger(typ, val, c):
    c.pyapi.incref(val)
    return val


@unbox(LoggingLoggerType)
def unbox_logging_logger(typ, obj, c):
    c.pyapi.incref(obj)
    return NativeValue(obj)


@lower_constant(LoggingLoggerType)
def lower_constant_logger(context, builder, ty, pyval):
    bxquy__gjux = context.get_python_api(builder)
    return bxquy__gjux.unserialize(bxquy__gjux.serialize_object(pyval))


gen_objmode_attr_overload(LoggingLoggerType, 'level', None, types.int64)
gen_objmode_attr_overload(LoggingLoggerType, 'name', None, 'unicode_type')
gen_objmode_attr_overload(LoggingLoggerType, 'propagate', None, types.boolean)
gen_objmode_attr_overload(LoggingLoggerType, 'disabled', None, types.boolean)
gen_objmode_attr_overload(LoggingLoggerType, 'parent', None,
    LoggingLoggerType())
gen_objmode_attr_overload(LoggingLoggerType, 'root', None,
    LoggingLoggerType(is_root=True))


@infer_getattr
class LoggingLoggerAttribute(AttributeTemplate):
    key = LoggingLoggerType

    def _resolve_helper(self, logger_typ, args, kws):
        kws = dict(kws)
        skgo__okyc = ', '.join('e{}'.format(soor__dkjk) for soor__dkjk in
            range(len(args)))
        if skgo__okyc:
            skgo__okyc += ', '
        epn__qya = ', '.join("{} = ''".format(zhenm__cbpr) for zhenm__cbpr in
            kws.keys())
        jkwck__gopjn = f'def format_stub(string, {skgo__okyc} {epn__qya}):\n'
        jkwck__gopjn += '    pass\n'
        fqouh__mayh = {}
        exec(jkwck__gopjn, {}, fqouh__mayh)
        ouxo__aig = fqouh__mayh['format_stub']
        irf__ttc = numba.core.utils.pysignature(ouxo__aig)
        inog__uxbz = (logger_typ,) + args + tuple(kws.values())
        return signature(logger_typ, inog__uxbz).replace(pysig=irf__ttc)
    func_names = ('debug', 'warning', 'warn', 'info', 'error', 'exception',
        'critical', 'log', 'setLevel')
    for tiqs__owuo in ('logging.Logger', 'logging.RootLogger'):
        for aodi__miqb in func_names:
            lzxh__cqvu = f'@bound_function("{tiqs__owuo}.{aodi__miqb}")\n'
            lzxh__cqvu += (
                f'def resolve_{aodi__miqb}(self, logger_typ, args, kws):\n')
            lzxh__cqvu += (
                '    return self._resolve_helper(logger_typ, args, kws)')
            exec(lzxh__cqvu)


logging_logger_unsupported_attrs = {'filters', 'handlers', 'manager'}
logging_logger_unsupported_methods = {'addHandler', 'callHandlers', 'fatal',
    'findCaller', 'getChild', 'getEffectiveLevel', 'handle', 'hasHandlers',
    'isEnabledFor', 'makeRecord', 'removeHandler'}


def _install_logging_logger_unsupported_objects():
    for eahz__jjkau in logging_logger_unsupported_attrs:
        domi__lvo = 'logging.Logger.' + eahz__jjkau
        overload_attribute(LoggingLoggerType, eahz__jjkau)(
            create_unsupported_overload(domi__lvo))
    for edkt__ptcia in logging_logger_unsupported_methods:
        domi__lvo = 'logging.Logger.' + edkt__ptcia
        overload_method(LoggingLoggerType, edkt__ptcia)(
            create_unsupported_overload(domi__lvo))


_install_logging_logger_unsupported_objects()
