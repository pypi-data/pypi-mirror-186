"""
Array of intervals corresponding to IntervalArray of Pandas.
Used for IntervalIndex, which is necessary for Series.value_counts() with 'bins'
argument.
"""
import numba
import pandas as pd
from numba.core import cgutils, types
from numba.extending import NativeValue, box, intrinsic, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_model, typeof_impl, unbox
from numba.parfors.array_analysis import ArrayAnalysis
import bodo


class IntervalType(types.Type):

    def __init__(self):
        super(IntervalType, self).__init__('IntervalType()')


class IntervalArrayType(types.ArrayCompatible):

    def __init__(self, arr_type):
        self.arr_type = arr_type
        self.dtype = IntervalType()
        super(IntervalArrayType, self).__init__(name=
            f'IntervalArrayType({arr_type})')

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    def copy(self):
        return IntervalArrayType(self.arr_type)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


@register_model(IntervalArrayType)
class IntervalArrayModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        cdtvj__eyvot = [('left', fe_type.arr_type), ('right', fe_type.arr_type)
            ]
        models.StructModel.__init__(self, dmm, fe_type, cdtvj__eyvot)


make_attribute_wrapper(IntervalArrayType, 'left', '_left')
make_attribute_wrapper(IntervalArrayType, 'right', '_right')


@typeof_impl.register(pd.arrays.IntervalArray)
def typeof_interval_array(val, c):
    arr_type = bodo.typeof(val._left)
    return IntervalArrayType(arr_type)


@intrinsic
def init_interval_array(typingctx, left, right=None):
    assert left == right, 'Interval left/right array types should be the same'

    def codegen(context, builder, signature, args):
        omocj__uyhkk, qzgjo__bkz = args
        suop__kuv = cgutils.create_struct_proxy(signature.return_type)(context,
            builder)
        suop__kuv.left = omocj__uyhkk
        suop__kuv.right = qzgjo__bkz
        context.nrt.incref(builder, signature.args[0], omocj__uyhkk)
        context.nrt.incref(builder, signature.args[1], qzgjo__bkz)
        return suop__kuv._getvalue()
    ggn__ydo = IntervalArrayType(left)
    qtrqw__jow = ggn__ydo(left, right)
    return qtrqw__jow, codegen


def init_interval_array_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 2 and not kws
    olnc__qpxc = []
    for mpl__mazs in args:
        liar__mdbox = equiv_set.get_shape(mpl__mazs)
        if liar__mdbox is not None:
            olnc__qpxc.append(liar__mdbox[0])
    if len(olnc__qpxc) > 1:
        equiv_set.insert_equiv(*olnc__qpxc)
    left = args[0]
    if equiv_set.has_shape(left):
        return ArrayAnalysis.AnalyzeResult(shape=left, pre=[])
    return None


(ArrayAnalysis._analyze_op_call_bodo_libs_interval_arr_ext_init_interval_array
    ) = init_interval_array_equiv


def alias_ext_init_interval_array(lhs_name, args, alias_map, arg_aliases):
    assert len(args) == 2
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)
    numba.core.ir_utils._add_alias(lhs_name, args[1].name, alias_map,
        arg_aliases)


numba.core.ir_utils.alias_func_extensions['init_interval_array',
    'bodo.libs.int_arr_ext'] = alias_ext_init_interval_array


@box(IntervalArrayType)
def box_interval_arr(typ, val, c):
    suop__kuv = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    c.context.nrt.incref(c.builder, typ.arr_type, suop__kuv.left)
    zepf__zih = c.pyapi.from_native_value(typ.arr_type, suop__kuv.left, c.
        env_manager)
    c.context.nrt.incref(c.builder, typ.arr_type, suop__kuv.right)
    uexh__dlu = c.pyapi.from_native_value(typ.arr_type, suop__kuv.right, c.
        env_manager)
    ofiu__zvmps = c.context.insert_const_string(c.builder.module, 'pandas')
    zcbyy__njta = c.pyapi.import_module_noblock(ofiu__zvmps)
    dyjp__zss = c.pyapi.object_getattr_string(zcbyy__njta, 'arrays')
    upws__vmj = c.pyapi.object_getattr_string(dyjp__zss, 'IntervalArray')
    efyxr__fnb = c.pyapi.call_method(upws__vmj, 'from_arrays', (zepf__zih,
        uexh__dlu))
    c.pyapi.decref(zepf__zih)
    c.pyapi.decref(uexh__dlu)
    c.pyapi.decref(zcbyy__njta)
    c.pyapi.decref(dyjp__zss)
    c.pyapi.decref(upws__vmj)
    c.context.nrt.decref(c.builder, typ, val)
    return efyxr__fnb


@unbox(IntervalArrayType)
def unbox_interval_arr(typ, val, c):
    zepf__zih = c.pyapi.object_getattr_string(val, '_left')
    left = c.pyapi.to_native_value(typ.arr_type, zepf__zih).value
    c.pyapi.decref(zepf__zih)
    uexh__dlu = c.pyapi.object_getattr_string(val, '_right')
    right = c.pyapi.to_native_value(typ.arr_type, uexh__dlu).value
    c.pyapi.decref(uexh__dlu)
    suop__kuv = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    suop__kuv.left = left
    suop__kuv.right = right
    qhv__wyhn = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(suop__kuv._getvalue(), is_error=qhv__wyhn)


@overload(len, no_unliteral=True)
def overload_interval_arr_len(A):
    if isinstance(A, IntervalArrayType):
        return lambda A: len(A._left)


@overload_attribute(IntervalArrayType, 'shape')
def overload_interval_arr_shape(A):
    return lambda A: (len(A._left),)


@overload_attribute(IntervalArrayType, 'ndim')
def overload_interval_arr_ndim(A):
    return lambda A: 1


@overload_attribute(IntervalArrayType, 'nbytes')
def overload_interval_arr_nbytes(A):
    return lambda A: A._left.nbytes + A._right.nbytes


@overload_method(IntervalArrayType, 'copy', no_unliteral=True)
def overload_interval_arr_copy(A):
    return lambda A: bodo.libs.interval_arr_ext.init_interval_array(A._left
        .copy(), A._right.copy())
