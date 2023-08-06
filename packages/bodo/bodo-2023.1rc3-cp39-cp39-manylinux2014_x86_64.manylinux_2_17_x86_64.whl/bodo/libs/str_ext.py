import operator
import re
import llvmlite.binding as ll
import numba
import numpy as np
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.typing.templates import AbstractTemplate, AttributeTemplate, bound_function, infer_getattr, infer_global, signature
from numba.extending import intrinsic, lower_cast, make_attribute_wrapper, models, overload, overload_attribute, register_jitable, register_model
from numba.parfors.array_analysis import ArrayAnalysis
import bodo
from bodo.libs import hstr_ext
from bodo.utils.typing import BodoError, get_overload_const_int, get_overload_const_str, is_overload_constant_int, is_overload_constant_str


def unliteral_all(args):
    return tuple(types.unliteral(a) for a in args)


ll.add_symbol('del_str', hstr_ext.del_str)
ll.add_symbol('unicode_to_utf8', hstr_ext.unicode_to_utf8)
ll.add_symbol('memcmp', hstr_ext.memcmp)
ll.add_symbol('int_to_hex', hstr_ext.int_to_hex)
string_type = types.unicode_type


@numba.njit
def contains_regex(e, in_str):
    with numba.objmode(res='bool_'):
        res = bool(e.search(in_str))
    return res


@numba.generated_jit
def str_findall_count(regex, in_str):

    def _str_findall_count_impl(regex, in_str):
        with numba.objmode(res='int64'):
            res = len(regex.findall(in_str))
        return res
    return _str_findall_count_impl


utf8_str_type = types.ArrayCTypes(types.Array(types.uint8, 1, 'C'))


@intrinsic
def unicode_to_utf8_and_len(typingctx, str_typ):
    assert str_typ in (string_type, types.Optional(string_type)) or isinstance(
        str_typ, types.StringLiteral)
    eufue__yxc = types.Tuple([utf8_str_type, types.int64])

    def codegen(context, builder, sig, args):
        ortvy__dyy, = args
        ake__dfnk = cgutils.create_struct_proxy(string_type)(context,
            builder, value=ortvy__dyy)
        ocyhx__aqpt = cgutils.create_struct_proxy(utf8_str_type)(context,
            builder)
        gbvnj__raw = cgutils.create_struct_proxy(eufue__yxc)(context, builder)
        is_ascii = builder.icmp_unsigned('==', ake__dfnk.is_ascii, lir.
            Constant(ake__dfnk.is_ascii.type, 1))
        with builder.if_else(is_ascii) as (xxlt__mhcls, ycd__xqfpi):
            with xxlt__mhcls:
                context.nrt.incref(builder, string_type, ortvy__dyy)
                ocyhx__aqpt.data = ake__dfnk.data
                ocyhx__aqpt.meminfo = ake__dfnk.meminfo
                gbvnj__raw.f1 = ake__dfnk.length
            with ycd__xqfpi:
                nlf__gyh = lir.FunctionType(lir.IntType(64), [lir.IntType(8
                    ).as_pointer(), lir.IntType(8).as_pointer(), lir.
                    IntType(64), lir.IntType(32)])
                axpjj__mmbpl = cgutils.get_or_insert_function(builder.
                    module, nlf__gyh, name='unicode_to_utf8')
                xpmms__bsii = context.get_constant_null(types.voidptr)
                amus__ubi = builder.call(axpjj__mmbpl, [xpmms__bsii,
                    ake__dfnk.data, ake__dfnk.length, ake__dfnk.kind])
                gbvnj__raw.f1 = amus__ubi
                oewa__eadso = builder.add(amus__ubi, lir.Constant(lir.
                    IntType(64), 1))
                ocyhx__aqpt.meminfo = context.nrt.meminfo_alloc_aligned(builder
                    , size=oewa__eadso, align=32)
                ocyhx__aqpt.data = context.nrt.meminfo_data(builder,
                    ocyhx__aqpt.meminfo)
                builder.call(axpjj__mmbpl, [ocyhx__aqpt.data, ake__dfnk.
                    data, ake__dfnk.length, ake__dfnk.kind])
                builder.store(lir.Constant(lir.IntType(8), 0), builder.gep(
                    ocyhx__aqpt.data, [amus__ubi]))
        gbvnj__raw.f0 = ocyhx__aqpt._getvalue()
        return gbvnj__raw._getvalue()
    return eufue__yxc(string_type), codegen


def unicode_to_utf8(s):
    return s


@overload(unicode_to_utf8)
def overload_unicode_to_utf8(s):
    return lambda s: unicode_to_utf8_and_len(s)[0]


def unicode_to_utf8_len(s):
    return s


@overload(unicode_to_utf8_len)
def overload_unicode_to_utf8_len(s):
    return lambda s: unicode_to_utf8_and_len(s)[1]


@overload(max)
def overload_builtin_max(lhs, rhs):
    if lhs == types.unicode_type and rhs == types.unicode_type:

        def impl(lhs, rhs):
            return lhs if lhs > rhs else rhs
        return impl


@overload(min)
def overload_builtin_min(lhs, rhs):
    if lhs == types.unicode_type and rhs == types.unicode_type:

        def impl(lhs, rhs):
            return lhs if lhs < rhs else rhs
        return impl


@intrinsic
def memcmp(typingctx, dest_t, src_t, count_t=None):

    def codegen(context, builder, sig, args):
        nlf__gyh = lir.FunctionType(lir.IntType(32), [lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(64)])
        zzr__ilufl = cgutils.get_or_insert_function(builder.module,
            nlf__gyh, name='memcmp')
        return builder.call(zzr__ilufl, args)
    return types.int32(types.voidptr, types.voidptr, types.intp), codegen


def int_to_str_len(n):
    return len(str(n))


@overload(int_to_str_len)
def overload_int_to_str_len(n):
    dyood__zjnnq = n(10)

    def impl(n):
        if n == 0:
            return 1
        znhwt__yvwog = 0
        if n < 0:
            n = -n
            znhwt__yvwog += 1
        while n > 0:
            n = n // dyood__zjnnq
            znhwt__yvwog += 1
        return znhwt__yvwog
    return impl


class StdStringType(types.Opaque):

    def __init__(self):
        super(StdStringType, self).__init__(name='StdStringType')


std_str_type = StdStringType()
register_model(StdStringType)(models.OpaqueModel)
del_str = types.ExternalFunction('del_str', types.void(std_str_type))
get_c_str = types.ExternalFunction('get_c_str', types.voidptr(std_str_type))
dummy_use = numba.njit(lambda a: None)


@overload(int)
def int_str_overload(in_str, base=10):
    if in_str == string_type:
        if is_overload_constant_int(base) and get_overload_const_int(base
            ) == 10:

            def _str_to_int_impl(in_str, base=10):
                val = _str_to_int64(in_str._data, in_str._length)
                dummy_use(in_str)
                return val
            return _str_to_int_impl

        def _str_to_int_base_impl(in_str, base=10):
            val = _str_to_int64_base(in_str._data, in_str._length, base)
            dummy_use(in_str)
            return val
        return _str_to_int_base_impl


@infer_global(float)
class StrToFloat(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        [mbrm__fwqa] = args
        if isinstance(mbrm__fwqa, StdStringType):
            return signature(types.float64, mbrm__fwqa)
        if mbrm__fwqa == string_type:
            return signature(types.float64, mbrm__fwqa)


ll.add_symbol('init_string_const', hstr_ext.init_string_const)
ll.add_symbol('get_c_str', hstr_ext.get_c_str)
ll.add_symbol('str_to_int64', hstr_ext.str_to_int64)
ll.add_symbol('str_to_uint64', hstr_ext.str_to_uint64)
ll.add_symbol('str_to_int64_base', hstr_ext.str_to_int64_base)
ll.add_symbol('str_to_float64', hstr_ext.str_to_float64)
ll.add_symbol('str_to_float32', hstr_ext.str_to_float32)
ll.add_symbol('get_str_len', hstr_ext.get_str_len)
ll.add_symbol('str_from_float32', hstr_ext.str_from_float32)
ll.add_symbol('str_from_float64', hstr_ext.str_from_float64)
get_std_str_len = types.ExternalFunction('get_str_len', signature(types.
    intp, std_str_type))
init_string_from_chars = types.ExternalFunction('init_string_const',
    std_str_type(types.voidptr, types.intp))
_str_to_int64 = types.ExternalFunction('str_to_int64', signature(types.
    int64, types.voidptr, types.int64))
_str_to_uint64 = types.ExternalFunction('str_to_uint64', signature(types.
    uint64, types.voidptr, types.int64))
_str_to_int64_base = types.ExternalFunction('str_to_int64_base', signature(
    types.int64, types.voidptr, types.int64, types.int64))


def gen_unicode_to_std_str(context, builder, unicode_val):
    ake__dfnk = cgutils.create_struct_proxy(string_type)(context, builder,
        value=unicode_val)
    nlf__gyh = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.IntType(8
        ).as_pointer(), lir.IntType(64)])
    rbu__xrrhw = cgutils.get_or_insert_function(builder.module, nlf__gyh,
        name='init_string_const')
    return builder.call(rbu__xrrhw, [ake__dfnk.data, ake__dfnk.length])


def gen_std_str_to_unicode(context, builder, std_str_val, del_str=False):
    kind = numba.cpython.unicode.PY_UNICODE_1BYTE_KIND

    def _std_str_to_unicode(std_str):
        length = bodo.libs.str_ext.get_std_str_len(std_str)
        ajlh__fioj = numba.cpython.unicode._empty_string(kind, length, 1)
        bodo.libs.str_arr_ext._memcpy(ajlh__fioj._data, bodo.libs.str_ext.
            get_c_str(std_str), length, 1)
        if del_str:
            bodo.libs.str_ext.del_str(std_str)
        return ajlh__fioj
    val = context.compile_internal(builder, _std_str_to_unicode,
        string_type(bodo.libs.str_ext.std_str_type), [std_str_val])
    return val


def gen_get_unicode_chars(context, builder, unicode_val):
    ake__dfnk = cgutils.create_struct_proxy(string_type)(context, builder,
        value=unicode_val)
    return ake__dfnk.data


@intrinsic
def unicode_to_std_str(typingctx, unicode_t=None):

    def codegen(context, builder, sig, args):
        return gen_unicode_to_std_str(context, builder, args[0])
    return std_str_type(string_type), codegen


@intrinsic
def std_str_to_unicode(typingctx, unicode_t=None):

    def codegen(context, builder, sig, args):
        return gen_std_str_to_unicode(context, builder, args[0], True)
    return string_type(std_str_type), codegen


class RandomAccessStringArrayType(types.ArrayCompatible):

    def __init__(self):
        super(RandomAccessStringArrayType, self).__init__(name=
            'RandomAccessStringArrayType()')

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    @property
    def dtype(self):
        return string_type

    def copy(self):
        RandomAccessStringArrayType()


random_access_string_array = RandomAccessStringArrayType()


@register_model(RandomAccessStringArrayType)
class RandomAccessStringArrayModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        muyc__ucwlq = [('data', types.List(string_type))]
        models.StructModel.__init__(self, dmm, fe_type, muyc__ucwlq)


make_attribute_wrapper(RandomAccessStringArrayType, 'data', '_data')


@intrinsic
def alloc_random_access_string_array(typingctx, n_t=None):

    def codegen(context, builder, sig, args):
        pybc__psk, = args
        ovl__nteif = types.List(string_type)
        musv__gbizv = numba.cpython.listobj.ListInstance.allocate(context,
            builder, ovl__nteif, pybc__psk)
        musv__gbizv.size = pybc__psk
        qnpy__tvd = cgutils.create_struct_proxy(sig.return_type)(context,
            builder)
        qnpy__tvd.data = musv__gbizv.value
        return qnpy__tvd._getvalue()
    return random_access_string_array(types.intp), codegen


@overload(operator.getitem, no_unliteral=True)
def random_access_str_arr_getitem(A, ind):
    if A != random_access_string_array:
        return
    if isinstance(ind, types.Integer):
        return lambda A, ind: A._data[ind]


@overload(operator.setitem)
def random_access_str_arr_setitem(A, idx, val):
    if A != random_access_string_array:
        return
    if isinstance(idx, types.Integer):
        assert val == string_type

        def impl_scalar(A, idx, val):
            A._data[idx] = val
        return impl_scalar


@overload(len, no_unliteral=True)
def overload_str_arr_len(A):
    if A == random_access_string_array:
        return lambda A: len(A._data)


@overload_attribute(RandomAccessStringArrayType, 'shape')
def overload_str_arr_shape(A):
    return lambda A: (len(A._data),)


def alloc_random_access_str_arr_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 1 and not kws
    return ArrayAnalysis.AnalyzeResult(shape=args[0], pre=[])


(ArrayAnalysis.
    _analyze_op_call_bodo_libs_str_ext_alloc_random_access_string_array
    ) = alloc_random_access_str_arr_equiv
str_from_float32 = types.ExternalFunction('str_from_float32', types.void(
    types.voidptr, types.float32))
str_from_float64 = types.ExternalFunction('str_from_float64', types.void(
    types.voidptr, types.float64))


def float_to_str(s, v):
    pass


@overload(float_to_str)
def float_to_str_overload(s, v):
    assert isinstance(v, types.Float)
    if v == types.float32:
        return lambda s, v: str_from_float32(s._data, v)
    return lambda s, v: str_from_float64(s._data, v)


@overload(str)
def float_str_overload(v):
    if isinstance(v, types.Float):
        kind = numba.cpython.unicode.PY_UNICODE_1BYTE_KIND

        def impl(v):
            if v == 0:
                return '0.0'
            rga__mvg = 0
            jwj__evc = v
            if jwj__evc < 0:
                rga__mvg = 1
                jwj__evc = -jwj__evc
            if jwj__evc < 1:
                lvacr__hufm = 1
            else:
                lvacr__hufm = 1 + int(np.floor(np.log10(jwj__evc)))
            length = rga__mvg + lvacr__hufm + 1 + 6
            s = numba.cpython.unicode._malloc_string(kind, 1, length, True)
            float_to_str(s, v)
            return s
        return impl


@overload(format, no_unliteral=True)
def overload_format(value, format_spec=''):
    if is_overload_constant_str(format_spec) and get_overload_const_str(
        format_spec) == '':

        def impl_fast(value, format_spec=''):
            return str(value)
        return impl_fast

    def impl(value, format_spec=''):
        with numba.objmode(res='string'):
            res = format(value, format_spec)
        return res
    return impl


@lower_cast(StdStringType, types.float64)
def cast_str_to_float64(context, builder, fromty, toty, val):
    nlf__gyh = lir.FunctionType(lir.DoubleType(), [lir.IntType(8).as_pointer()]
        )
    rbu__xrrhw = cgutils.get_or_insert_function(builder.module, nlf__gyh,
        name='str_to_float64')
    res = builder.call(rbu__xrrhw, (val,))
    bodo.utils.utils.inlined_check_and_propagate_cpp_exception(context, builder
        )
    return res


@lower_cast(StdStringType, types.float32)
def cast_str_to_float32(context, builder, fromty, toty, val):
    nlf__gyh = lir.FunctionType(lir.FloatType(), [lir.IntType(8).as_pointer()])
    rbu__xrrhw = cgutils.get_or_insert_function(builder.module, nlf__gyh,
        name='str_to_float32')
    res = builder.call(rbu__xrrhw, (val,))
    bodo.utils.utils.inlined_check_and_propagate_cpp_exception(context, builder
        )
    return res


@lower_cast(string_type, types.float64)
def cast_unicode_str_to_float64(context, builder, fromty, toty, val):
    std_str = gen_unicode_to_std_str(context, builder, val)
    return cast_str_to_float64(context, builder, std_str_type, toty, std_str)


@lower_cast(string_type, types.float32)
def cast_unicode_str_to_float32(context, builder, fromty, toty, val):
    std_str = gen_unicode_to_std_str(context, builder, val)
    return cast_str_to_float32(context, builder, std_str_type, toty, std_str)


@lower_cast(string_type, types.int64)
@lower_cast(string_type, types.int32)
@lower_cast(string_type, types.int16)
@lower_cast(string_type, types.int8)
def cast_unicode_str_to_int64(context, builder, fromty, toty, val):
    ake__dfnk = cgutils.create_struct_proxy(string_type)(context, builder,
        value=val)
    nlf__gyh = lir.FunctionType(lir.IntType(toty.bitwidth), [lir.IntType(8)
        .as_pointer(), lir.IntType(64)])
    rbu__xrrhw = cgutils.get_or_insert_function(builder.module, nlf__gyh,
        name='str_to_int64')
    res = builder.call(rbu__xrrhw, (ake__dfnk.data, ake__dfnk.length))
    bodo.utils.utils.inlined_check_and_propagate_cpp_exception(context, builder
        )
    return res


@lower_cast(string_type, types.uint64)
@lower_cast(string_type, types.uint32)
@lower_cast(string_type, types.uint16)
@lower_cast(string_type, types.uint8)
def cast_unicode_str_to_uint64(context, builder, fromty, toty, val):
    ake__dfnk = cgutils.create_struct_proxy(string_type)(context, builder,
        value=val)
    nlf__gyh = lir.FunctionType(lir.IntType(toty.bitwidth), [lir.IntType(8)
        .as_pointer(), lir.IntType(64)])
    rbu__xrrhw = cgutils.get_or_insert_function(builder.module, nlf__gyh,
        name='str_to_uint64')
    res = builder.call(rbu__xrrhw, (ake__dfnk.data, ake__dfnk.length))
    bodo.utils.utils.inlined_check_and_propagate_cpp_exception(context, builder
        )
    return res


@infer_getattr
class StringAttribute(AttributeTemplate):
    key = types.UnicodeType

    @bound_function('str.format', no_unliteral=True)
    def resolve_format(self, string_typ, args, kws):
        kws = dict(kws)
        xee__qlywv = ', '.join('e{}'.format(nej__qtb) for nej__qtb in range
            (len(args)))
        if xee__qlywv:
            xee__qlywv += ', '
        bcjpv__prkdm = ', '.join("{} = ''".format(a) for a in kws.keys())
        vjpnq__ofi = f'def format_stub(string, {xee__qlywv} {bcjpv__prkdm}):\n'
        vjpnq__ofi += '    pass\n'
        nejq__tbuw = {}
        exec(vjpnq__ofi, {}, nejq__tbuw)
        kwhb__dyfpa = nejq__tbuw['format_stub']
        yqot__xcljd = numba.core.utils.pysignature(kwhb__dyfpa)
        ozm__xsas = (string_typ,) + args + tuple(kws.values())
        return signature(string_typ, ozm__xsas).replace(pysig=yqot__xcljd)


@numba.njit(cache=True)
def str_split(arr, pat, n):
    lxej__dpq = pat is not None and len(pat) > 1
    if lxej__dpq:
        agzh__tmj = re.compile(pat)
        if n == -1:
            n = 0
    elif n == 0:
        n = -1
    musv__gbizv = len(arr)
    zxc__wzqt = 0
    rzdl__pnef = 0
    for nej__qtb in numba.parfors.parfor.internal_prange(musv__gbizv):
        if bodo.libs.array_kernels.isna(arr, nej__qtb):
            continue
        if lxej__dpq:
            eqsg__bbrmo = agzh__tmj.split(arr[nej__qtb], maxsplit=n)
        elif pat == '':
            eqsg__bbrmo = [''] + list(arr[nej__qtb]) + ['']
        else:
            eqsg__bbrmo = arr[nej__qtb].split(pat, n)
        zxc__wzqt += len(eqsg__bbrmo)
        for s in eqsg__bbrmo:
            rzdl__pnef += bodo.libs.str_arr_ext.get_utf8_size(s)
    dtoif__uufqn = bodo.libs.array_item_arr_ext.pre_alloc_array_item_array(
        musv__gbizv, (zxc__wzqt, rzdl__pnef), bodo.libs.str_arr_ext.
        string_array_type)
    nwk__brwg = bodo.libs.array_item_arr_ext.get_offsets(dtoif__uufqn)
    oixq__tcpvj = bodo.libs.array_item_arr_ext.get_null_bitmap(dtoif__uufqn)
    fueyh__dhg = bodo.libs.array_item_arr_ext.get_data(dtoif__uufqn)
    vxu__anwvm = 0
    for vinjc__tqbho in numba.parfors.parfor.internal_prange(musv__gbizv):
        nwk__brwg[vinjc__tqbho] = vxu__anwvm
        if bodo.libs.array_kernels.isna(arr, vinjc__tqbho):
            bodo.libs.int_arr_ext.set_bit_to_arr(oixq__tcpvj, vinjc__tqbho, 0)
            continue
        bodo.libs.int_arr_ext.set_bit_to_arr(oixq__tcpvj, vinjc__tqbho, 1)
        if lxej__dpq:
            eqsg__bbrmo = agzh__tmj.split(arr[vinjc__tqbho], maxsplit=n)
        elif pat == '':
            eqsg__bbrmo = [''] + list(arr[vinjc__tqbho]) + ['']
        else:
            eqsg__bbrmo = arr[vinjc__tqbho].split(pat, n)
        ulki__isp = len(eqsg__bbrmo)
        for famn__rsuiu in range(ulki__isp):
            s = eqsg__bbrmo[famn__rsuiu]
            fueyh__dhg[vxu__anwvm] = s
            vxu__anwvm += 1
    nwk__brwg[musv__gbizv] = vxu__anwvm
    return dtoif__uufqn


@overload(hex)
def overload_hex(x):
    if isinstance(x, types.Integer):
        kind = numba.cpython.unicode.PY_UNICODE_1BYTE_KIND

        def impl(x):
            x = np.int64(x)
            if x < 0:
                wybix__tff = '-0x'
                x = x * -1
            else:
                wybix__tff = '0x'
            x = np.uint64(x)
            if x == 0:
                wmoud__pjvzi = 1
            else:
                wmoud__pjvzi = fast_ceil_log2(x + 1)
                wmoud__pjvzi = (wmoud__pjvzi + 3) // 4
            length = len(wybix__tff) + wmoud__pjvzi
            output = numba.cpython.unicode._empty_string(kind, length, 1)
            bodo.libs.str_arr_ext._memcpy(output._data, wybix__tff._data,
                len(wybix__tff), 1)
            int_to_hex(output, wmoud__pjvzi, len(wybix__tff), x)
            return output
        return impl


@register_jitable
def fast_ceil_log2(x):
    qhkcy__aucx = 0 if x & x - 1 == 0 else 1
    jknx__vvu = [np.uint64(18446744069414584320), np.uint64(4294901760), np
        .uint64(65280), np.uint64(240), np.uint64(12), np.uint64(2)]
    nvj__uxzl = 32
    for nej__qtb in range(len(jknx__vvu)):
        rgjpm__ofy = 0 if x & jknx__vvu[nej__qtb] == 0 else nvj__uxzl
        qhkcy__aucx = qhkcy__aucx + rgjpm__ofy
        x = x >> rgjpm__ofy
        nvj__uxzl = nvj__uxzl >> 1
    return qhkcy__aucx


@intrinsic
def int_to_hex(typingctx, output, out_len, header_len, int_val):

    def codegen(context, builder, sig, args):
        output, out_len, header_len, int_val = args
        vbmxw__ykbte = cgutils.create_struct_proxy(sig.args[0])(context,
            builder, value=output)
        nlf__gyh = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(64), lir.IntType(64)])
        urj__awpsz = cgutils.get_or_insert_function(builder.module,
            nlf__gyh, name='int_to_hex')
        ifeo__ngc = builder.inttoptr(builder.add(builder.ptrtoint(
            vbmxw__ykbte.data, lir.IntType(64)), header_len), lir.IntType(8
            ).as_pointer())
        builder.call(urj__awpsz, (ifeo__ngc, out_len, int_val))
    return types.void(output, out_len, header_len, int_val), codegen


def alloc_empty_bytes_or_string_data(typ, kind, length, is_ascii=0):
    pass


@overload(alloc_empty_bytes_or_string_data)
def overload_alloc_empty_bytes_or_string_data(typ, kind, length, is_ascii=0):
    typ = typ.instance_type if isinstance(typ, types.TypeRef) else typ
    if typ == bodo.bytes_type:
        return lambda typ, kind, length, is_ascii=0: np.empty(length, np.uint8)
    if typ == string_type:
        return (lambda typ, kind, length, is_ascii=0: numba.cpython.unicode
            ._empty_string(kind, length, is_ascii))
    raise BodoError(
        f'Internal Error: Expected Bytes or String type, found {typ}')


def get_unicode_or_numpy_data(val):
    pass


@overload(get_unicode_or_numpy_data)
def overload_get_unicode_or_numpy_data(val):
    if val == string_type:
        return lambda val: val._data
    if isinstance(val, types.Array):
        return lambda val: val.ctypes
    raise BodoError(
        f'Internal Error: Expected String or Numpy Array, found {val}')
