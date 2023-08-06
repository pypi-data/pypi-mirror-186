"""Support for MultiIndex type of Pandas
"""
import operator
import numba
import pandas as pd
from numba.core import cgutils, types
from numba.extending import NativeValue, box, intrinsic, lower_builtin, make_attribute_wrapper, models, overload, register_model, typeof_impl, unbox
from bodo.utils.conversion import ensure_contig_if_np
from bodo.utils.typing import BodoError, check_unsupported_args, dtype_to_array_type, get_val_type_maybe_str_literal, is_overload_none


class MultiIndexType(types.ArrayCompatible):

    def __init__(self, array_types, names_typ=None, name_typ=None):
        names_typ = (types.none,) * len(array_types
            ) if names_typ is None else names_typ
        name_typ = types.none if name_typ is None else name_typ
        self.array_types = array_types
        self.names_typ = names_typ
        self.name_typ = name_typ
        super(MultiIndexType, self).__init__(name=
            'MultiIndexType({}, {}, {})'.format(array_types, names_typ,
            name_typ))
    ndim = 1

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    def copy(self):
        return MultiIndexType(self.array_types, self.names_typ, self.name_typ)

    @property
    def nlevels(self):
        return len(self.array_types)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


@register_model(MultiIndexType)
class MultiIndexModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        fwj__rxz = [('data', types.Tuple(fe_type.array_types)), ('names',
            types.Tuple(fe_type.names_typ)), ('name', fe_type.name_typ)]
        super(MultiIndexModel, self).__init__(dmm, fe_type, fwj__rxz)


make_attribute_wrapper(MultiIndexType, 'data', '_data')
make_attribute_wrapper(MultiIndexType, 'names', '_names')
make_attribute_wrapper(MultiIndexType, 'name', '_name')


@typeof_impl.register(pd.MultiIndex)
def typeof_multi_index(val, c):
    array_types = tuple(numba.typeof(val.levels[wxx__mhyh].values) for
        wxx__mhyh in range(val.nlevels))
    return MultiIndexType(array_types, tuple(get_val_type_maybe_str_literal
        (vfvjl__oljp) for vfvjl__oljp in val.names), numba.typeof(val.name))


@box(MultiIndexType)
def box_multi_index(typ, val, c):
    yciv__aqj = c.context.insert_const_string(c.builder.module, 'pandas')
    fdfcr__qwbdt = c.pyapi.import_module_noblock(yciv__aqj)
    wlft__ayar = c.pyapi.object_getattr_string(fdfcr__qwbdt, 'MultiIndex')
    mnjjr__ola = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    c.context.nrt.incref(c.builder, types.Tuple(typ.array_types),
        mnjjr__ola.data)
    qnzpk__kxdg = c.pyapi.from_native_value(types.Tuple(typ.array_types),
        mnjjr__ola.data, c.env_manager)
    c.context.nrt.incref(c.builder, types.Tuple(typ.names_typ), mnjjr__ola.
        names)
    hzuc__bxu = c.pyapi.from_native_value(types.Tuple(typ.names_typ),
        mnjjr__ola.names, c.env_manager)
    c.context.nrt.incref(c.builder, typ.name_typ, mnjjr__ola.name)
    sowcz__csg = c.pyapi.from_native_value(typ.name_typ, mnjjr__ola.name, c
        .env_manager)
    dowga__neghy = c.pyapi.borrow_none()
    arjku__mjpn = c.pyapi.call_method(wlft__ayar, 'from_arrays', (
        qnzpk__kxdg, dowga__neghy, hzuc__bxu))
    c.pyapi.object_setattr_string(arjku__mjpn, 'name', sowcz__csg)
    c.pyapi.decref(qnzpk__kxdg)
    c.pyapi.decref(hzuc__bxu)
    c.pyapi.decref(sowcz__csg)
    c.pyapi.decref(fdfcr__qwbdt)
    c.pyapi.decref(wlft__ayar)
    c.context.nrt.decref(c.builder, typ, val)
    return arjku__mjpn


@unbox(MultiIndexType)
def unbox_multi_index(typ, val, c):
    krm__icb = []
    fpz__zvdzq = []
    for wxx__mhyh in range(typ.nlevels):
        ftij__xenq = c.pyapi.unserialize(c.pyapi.serialize_object(wxx__mhyh))
        mliaq__oej = c.pyapi.call_method(val, 'get_level_values', (ftij__xenq,)
            )
        umnz__sbscq = c.pyapi.object_getattr_string(mliaq__oej, 'values')
        c.pyapi.decref(mliaq__oej)
        c.pyapi.decref(ftij__xenq)
        dic__jrm = c.pyapi.to_native_value(typ.array_types[wxx__mhyh],
            umnz__sbscq).value
        krm__icb.append(dic__jrm)
        fpz__zvdzq.append(umnz__sbscq)
    if isinstance(types.Tuple(typ.array_types), types.UniTuple):
        data = cgutils.pack_array(c.builder, krm__icb)
    else:
        data = cgutils.pack_struct(c.builder, krm__icb)
    hzuc__bxu = c.pyapi.object_getattr_string(val, 'names')
    cvv__tpq = c.pyapi.unserialize(c.pyapi.serialize_object(tuple))
    heej__ijxy = c.pyapi.call_function_objargs(cvv__tpq, (hzuc__bxu,))
    names = c.pyapi.to_native_value(types.Tuple(typ.names_typ), heej__ijxy
        ).value
    sowcz__csg = c.pyapi.object_getattr_string(val, 'name')
    name = c.pyapi.to_native_value(typ.name_typ, sowcz__csg).value
    mnjjr__ola = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    mnjjr__ola.data = data
    mnjjr__ola.names = names
    mnjjr__ola.name = name
    for umnz__sbscq in fpz__zvdzq:
        c.pyapi.decref(umnz__sbscq)
    c.pyapi.decref(hzuc__bxu)
    c.pyapi.decref(cvv__tpq)
    c.pyapi.decref(heej__ijxy)
    c.pyapi.decref(sowcz__csg)
    return NativeValue(mnjjr__ola._getvalue())


def from_product_error_checking(iterables, sortorder, names):
    uxplj__udc = 'pandas.MultiIndex.from_product'
    ipbeo__rlayx = dict(sortorder=sortorder)
    nuljx__uoavs = dict(sortorder=None)
    check_unsupported_args(uxplj__udc, ipbeo__rlayx, nuljx__uoavs,
        package_name='pandas', module_name='Index')
    if not (is_overload_none(names) or isinstance(names, types.BaseTuple)):
        raise BodoError(f'{uxplj__udc}: names must be None or a tuple.')
    elif not isinstance(iterables, types.BaseTuple):
        raise BodoError(f'{uxplj__udc}: iterables must be a tuple.')
    elif not is_overload_none(names) and len(iterables) != len(names):
        raise BodoError(
            f'{uxplj__udc}: iterables and names must be of the same length.')


def from_product(iterable, sortorder=None, names=None):
    pass


@overload(from_product)
def from_product_overload(iterables, sortorder=None, names=None):
    from_product_error_checking(iterables, sortorder, names)
    array_types = tuple(dtype_to_array_type(iterable.dtype) for iterable in
        iterables)
    if is_overload_none(names):
        names_typ = tuple([types.none] * len(iterables))
    else:
        names_typ = names.types
    opt__dnfu = MultiIndexType(array_types, names_typ)
    ctxp__kgnfp = f'from_product_multiindex{numba.core.ir_utils.next_label()}'
    setattr(types, ctxp__kgnfp, opt__dnfu)
    krwm__twqq = f"""
def impl(iterables, sortorder=None, names=None):
    with numba.objmode(mi='{ctxp__kgnfp}'):
        mi = pd.MultiIndex.from_product(iterables, names=names)
    return mi
"""
    ybzlx__viw = {}
    exec(krwm__twqq, globals(), ybzlx__viw)
    mojxx__crh = ybzlx__viw['impl']
    return mojxx__crh


@intrinsic
def init_multi_index(typingctx, data, names, name=None):
    name = types.none if name is None else name
    names = types.Tuple(names.types)

    def codegen(context, builder, signature, args):
        ezrff__rzhmq, wipb__rhc, apjk__oldzn = args
        hdyf__hpp = cgutils.create_struct_proxy(signature.return_type)(context,
            builder)
        hdyf__hpp.data = ezrff__rzhmq
        hdyf__hpp.names = wipb__rhc
        hdyf__hpp.name = apjk__oldzn
        context.nrt.incref(builder, signature.args[0], ezrff__rzhmq)
        context.nrt.incref(builder, signature.args[1], wipb__rhc)
        context.nrt.incref(builder, signature.args[2], apjk__oldzn)
        return hdyf__hpp._getvalue()
    lpxff__liy = MultiIndexType(data.types, names.types, name)
    return lpxff__liy(data, names, name), codegen


@overload(len, no_unliteral=True)
def overload_len_pd_multiindex(A):
    if isinstance(A, MultiIndexType):
        return lambda A: len(A._data[0])


@overload(operator.getitem, no_unliteral=True)
def overload_multi_index_getitem(I, ind):
    if not isinstance(I, MultiIndexType):
        return
    if not isinstance(ind, types.Integer):
        ewti__hznkp = len(I.array_types)
        krwm__twqq = 'def impl(I, ind):\n'
        krwm__twqq += '  data = I._data\n'
        krwm__twqq += ('  return init_multi_index(({},), I._names, I._name)\n'
            .format(', '.join(
            f'ensure_contig_if_np(data[{wxx__mhyh}][ind])' for wxx__mhyh in
            range(ewti__hznkp))))
        ybzlx__viw = {}
        exec(krwm__twqq, {'init_multi_index': init_multi_index,
            'ensure_contig_if_np': ensure_contig_if_np}, ybzlx__viw)
        mojxx__crh = ybzlx__viw['impl']
        return mojxx__crh


@lower_builtin(operator.is_, MultiIndexType, MultiIndexType)
def multi_index_is(context, builder, sig, args):
    nbng__fofdh, zwesv__sohz = sig.args
    if nbng__fofdh != zwesv__sohz:
        return cgutils.false_bit

    def index_is_impl(a, b):
        return (a._data is b._data and a._names is b._names and a._name is
            b._name)
    return context.compile_internal(builder, index_is_impl, sig, args)
