"""
Class information for DataFrame iterators returned by pd.read_csv. This is used
to handle situations in which pd.read_csv is used to return chunks with separate
read calls instead of just a single read.
"""
import llvmlite.binding as ll
import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from numba.core import cgutils, ir_utils, types
from numba.core.imputils import RefType, impl_ret_borrowed, iternext_impl
from numba.core.typing.templates import signature
from numba.extending import intrinsic, lower_builtin, models, register_model
import bodo
import bodo.ir.connector
import bodo.ir.csv_ext
from bodo import objmode
from bodo.hiframes.pd_dataframe_ext import DataFrameType
from bodo.hiframes.table import Table, TableType
from bodo.io import csv_cpp
from bodo.ir.csv_ext import _gen_read_csv_objmode, astype
from bodo.utils.typing import ColNamesMetaType
from bodo.utils.utils import check_java_installation
from bodo.utils.utils import sanitize_varname
ll.add_symbol('update_csv_reader', csv_cpp.update_csv_reader)
ll.add_symbol('initialize_csv_reader', csv_cpp.initialize_csv_reader)


class CSVIteratorType(types.SimpleIteratorType):

    def __init__(self, df_type, out_colnames, out_types, usecols, sep,
        index_ind, index_arr_typ, index_name, escapechar, storage_options):
        assert isinstance(df_type, DataFrameType
            ), 'CSVIterator must return a DataFrame'
        pkpap__ejz = (
            f'CSVIteratorType({df_type}, {out_colnames}, {out_types}, {usecols}, {sep}, {index_ind}, {index_arr_typ}, {index_name}, {escapechar})'
            )
        super(types.SimpleIteratorType, self).__init__(pkpap__ejz)
        self._yield_type = df_type
        self._out_colnames = out_colnames
        self._out_types = out_types
        self._usecols = usecols
        self._sep = sep
        self._index_ind = index_ind
        self._index_arr_typ = index_arr_typ
        self._index_name = index_name
        self._escapechar = escapechar
        self._storage_options = storage_options

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


@register_model(CSVIteratorType)
class CSVIteratorModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        nns__trg = [('csv_reader', types.stream_reader_type), ('index',
            types.EphemeralPointer(types.uintp))]
        super(CSVIteratorModel, self).__init__(dmm, fe_type, nns__trg)


@lower_builtin('getiter', CSVIteratorType)
def getiter_csv_iterator(context, builder, sig, args):
    wiwp__sqllw = cgutils.create_struct_proxy(sig.args[0])(context, builder,
        value=args[0])
    xjo__xsdx = lir.FunctionType(lir.VoidType(), [lir.IntType(8).as_pointer()])
    xzghe__nwfi = cgutils.get_or_insert_function(builder.module, xjo__xsdx,
        name='initialize_csv_reader')
    ggsu__ixur = cgutils.create_struct_proxy(types.stream_reader_type)(context,
        builder, value=wiwp__sqllw.csv_reader)
    builder.call(xzghe__nwfi, [ggsu__ixur.pyobj])
    builder.store(context.get_constant(types.uint64, 0), wiwp__sqllw.index)
    return impl_ret_borrowed(context, builder, sig.return_type, args[0])


@lower_builtin('iternext', CSVIteratorType)
@iternext_impl(RefType.NEW)
def iternext_csv_iterator(context, builder, sig, args, result):
    [jntj__pgr] = sig.args
    [nup__nad] = args
    wiwp__sqllw = cgutils.create_struct_proxy(jntj__pgr)(context, builder,
        value=nup__nad)
    xjo__xsdx = lir.FunctionType(lir.IntType(1), [lir.IntType(8).as_pointer()])
    xzghe__nwfi = cgutils.get_or_insert_function(builder.module, xjo__xsdx,
        name='update_csv_reader')
    ggsu__ixur = cgutils.create_struct_proxy(types.stream_reader_type)(context,
        builder, value=wiwp__sqllw.csv_reader)
    fmgux__yjd = builder.call(xzghe__nwfi, [ggsu__ixur.pyobj])
    result.set_valid(fmgux__yjd)
    with builder.if_then(fmgux__yjd):
        doho__kknnp = builder.load(wiwp__sqllw.index)
        peo__rye = types.Tuple([sig.return_type.first_type, types.int64])
        atwny__aexd = gen_read_csv_objmode(sig.args[0])
        irr__mvkpi = signature(peo__rye, types.stream_reader_type, types.int64)
        yfjc__lofn = context.compile_internal(builder, atwny__aexd,
            irr__mvkpi, [wiwp__sqllw.csv_reader, doho__kknnp])
        vigqz__ely, tmjo__hev = cgutils.unpack_tuple(builder, yfjc__lofn)
        wjwkj__wnc = builder.add(doho__kknnp, tmjo__hev, flags=['nsw'])
        builder.store(wjwkj__wnc, wiwp__sqllw.index)
        result.yield_(vigqz__ely)


@intrinsic
def init_csv_iterator(typingctx, csv_reader, csv_iterator_typeref):

    def codegen(context, builder, signature, args):
        myf__lsm = cgutils.create_struct_proxy(signature.return_type)(context,
            builder)
        context.nrt.incref(builder, signature.args[0], args[0])
        myf__lsm.csv_reader = args[0]
        jrxwe__dygbx = context.get_constant(types.uintp, 0)
        myf__lsm.index = cgutils.alloca_once_value(builder, jrxwe__dygbx)
        return myf__lsm._getvalue()
    assert isinstance(csv_iterator_typeref, types.TypeRef
        ), 'Initializing a csv iterator requires a typeref'
    inw__pjtgv = csv_iterator_typeref.instance_type
    sig = signature(inw__pjtgv, csv_reader, csv_iterator_typeref)
    return sig, codegen


def gen_read_csv_objmode(csv_iterator_type):
    ukguu__svetl = 'def read_csv_objmode(f_reader):\n'
    yifr__nzgj = [sanitize_varname(gamum__xfztv) for gamum__xfztv in
        csv_iterator_type._out_colnames]
    tszew__hdw = ir_utils.next_label()
    cvz__mwl = globals()
    out_types = csv_iterator_type._out_types
    cvz__mwl[f'table_type_{tszew__hdw}'] = TableType(tuple(out_types))
    cvz__mwl[f'idx_array_typ'] = csv_iterator_type._index_arr_typ
    smakc__fplyr = list(range(len(csv_iterator_type._usecols)))
    ukguu__svetl += _gen_read_csv_objmode(csv_iterator_type._out_colnames,
        yifr__nzgj, out_types, csv_iterator_type._usecols, smakc__fplyr,
        csv_iterator_type._sep, csv_iterator_type._escapechar,
        csv_iterator_type._storage_options, tszew__hdw, cvz__mwl, parallel=
        False, check_parallel_runtime=True, idx_col_index=csv_iterator_type
        ._index_ind, idx_col_typ=csv_iterator_type._index_arr_typ)
    ztf__zxa = bodo.ir.csv_ext._gen_parallel_flag_name(yifr__nzgj)
    ogvh__icsz = ['T'] + (['idx_arr'] if csv_iterator_type._index_ind is not
        None else []) + [ztf__zxa]
    ukguu__svetl += f"  return {', '.join(ogvh__icsz)}"
    cvz__mwl = globals()
    tazc__ctllt = {}
    exec(ukguu__svetl, cvz__mwl, tazc__ctllt)
    cpqz__gho = tazc__ctllt['read_csv_objmode']
    tjj__lro = numba.njit(cpqz__gho)
    bodo.ir.csv_ext.compiled_funcs.append(tjj__lro)
    ikk__yay = 'def read_func(reader, local_start):\n'
    ikk__yay += f"  {', '.join(ogvh__icsz)} = objmode_func(reader)\n"
    index_ind = csv_iterator_type._index_ind
    if index_ind is None:
        ikk__yay += f'  local_len = len(T)\n'
        ikk__yay += '  total_size = local_len\n'
        ikk__yay += f'  if ({ztf__zxa}):\n'
        ikk__yay += """    local_start = local_start + bodo.libs.distributed_api.dist_exscan(local_len, _op)
"""
        ikk__yay += (
            '    total_size = bodo.libs.distributed_api.dist_reduce(local_len, _op)\n'
            )
        vnw__rseco = (
            f'bodo.hiframes.pd_index_ext.init_range_index(local_start, local_start + local_len, 1, None)'
            )
    else:
        ikk__yay += '  total_size = 0\n'
        vnw__rseco = (
            f'bodo.utils.conversion.convert_to_index({ogvh__icsz[1]}, {csv_iterator_type._index_name!r})'
            )
    ikk__yay += f"""  return (bodo.hiframes.pd_dataframe_ext.init_dataframe(({ogvh__icsz[0]},), {vnw__rseco}, __col_name_meta_value_read_csv_objmode), total_size)
"""
    exec(ikk__yay, {'bodo': bodo, 'objmode_func': tjj__lro, '_op': np.int32
        (bodo.libs.distributed_api.Reduce_Type.Sum.value),
        '__col_name_meta_value_read_csv_objmode': ColNamesMetaType(
        csv_iterator_type.yield_type.columns)}, tazc__ctllt)
    return tazc__ctllt['read_func']
