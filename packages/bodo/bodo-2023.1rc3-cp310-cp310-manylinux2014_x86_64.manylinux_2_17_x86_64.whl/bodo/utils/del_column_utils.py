"""Helper information to keep table column deletion
pass organized. This contains information about all
table operations for optimizations.
"""
from typing import Dict, Tuple
from numba.core import ir, types
from bodo.hiframes.table import TableType
table_usecol_funcs = {('get_table_data', 'bodo.hiframes.table'), (
    'table_filter', 'bodo.hiframes.table'), ('table_subset',
    'bodo.hiframes.table'), ('set_table_data', 'bodo.hiframes.table'), (
    'set_table_data_null', 'bodo.hiframes.table'), (
    'generate_mappable_table_func', 'bodo.utils.table_utils'), (
    'table_astype', 'bodo.utils.table_utils'), ('generate_table_nbytes',
    'bodo.utils.table_utils'), ('table_concat', 'bodo.utils.table_utils'),
    ('py_data_to_cpp_table', 'bodo.libs.array'), ('logical_table_to_table',
    'bodo.hiframes.table')}


def is_table_use_column_ops(fdef: Tuple[str, str], args, typemap):
    return fdef in table_usecol_funcs and len(args) > 0 and isinstance(typemap
        [args[0].name], TableType)


def get_table_used_columns(fdef: Tuple[str, str], call_expr: ir.Expr,
    typemap: Dict[str, types.Type]):
    if fdef == ('get_table_data', 'bodo.hiframes.table'):
        lel__afrn = typemap[call_expr.args[1].name].literal_value
        return {lel__afrn}
    elif fdef in {('table_filter', 'bodo.hiframes.table'), ('table_astype',
        'bodo.utils.table_utils'), ('generate_mappable_table_func',
        'bodo.utils.table_utils'), ('set_table_data', 'bodo.hiframes.table'
        ), ('set_table_data_null', 'bodo.hiframes.table')}:
        ifd__ljbp = dict(call_expr.kws)
        if 'used_cols' in ifd__ljbp:
            rjjv__ngcn = ifd__ljbp['used_cols']
            gvr__gzulx = typemap[rjjv__ngcn.name]
            gvr__gzulx = gvr__gzulx.instance_type
            return set(gvr__gzulx.meta)
    elif fdef == ('table_concat', 'bodo.utils.table_utils'):
        rjjv__ngcn = call_expr.args[1]
        gvr__gzulx = typemap[rjjv__ngcn.name]
        gvr__gzulx = gvr__gzulx.instance_type
        return set(gvr__gzulx.meta)
    elif fdef == ('table_subset', 'bodo.hiframes.table'):
        ptl__cjbm = call_expr.args[1]
        nkf__qgh = typemap[ptl__cjbm.name]
        nkf__qgh = nkf__qgh.instance_type
        smbnk__slc = nkf__qgh.meta
        ifd__ljbp = dict(call_expr.kws)
        if 'used_cols' in ifd__ljbp:
            rjjv__ngcn = ifd__ljbp['used_cols']
            gvr__gzulx = typemap[rjjv__ngcn.name]
            gvr__gzulx = gvr__gzulx.instance_type
            qbee__bjq = set(gvr__gzulx.meta)
            dtj__aea = set()
            for saa__rmox, ebayc__plegu in enumerate(smbnk__slc):
                if saa__rmox in qbee__bjq:
                    dtj__aea.add(ebayc__plegu)
            return dtj__aea
        else:
            return set(smbnk__slc)
    elif fdef == ('py_data_to_cpp_table', 'bodo.libs.array'):
        djbn__ajtr = typemap[call_expr.args[2].name].instance_type.meta
        elg__obad = len(typemap[call_expr.args[0].name].arr_types)
        return set(saa__rmox for saa__rmox in djbn__ajtr if saa__rmox <
            elg__obad)
    elif fdef == ('logical_table_to_table', 'bodo.hiframes.table'):
        apn__ypvn = typemap[call_expr.args[2].name].instance_type.meta
        fbbf__ocmbb = len(typemap[call_expr.args[0].name].arr_types)
        ifd__ljbp = dict(call_expr.kws)
        if 'used_cols' in ifd__ljbp:
            qbee__bjq = set(typemap[ifd__ljbp['used_cols'].name].
                instance_type.meta)
            qpof__kug = set()
            for exo__zzz, llvl__lgw in enumerate(apn__ypvn):
                if exo__zzz in qbee__bjq and llvl__lgw < fbbf__ocmbb:
                    qpof__kug.add(llvl__lgw)
            return qpof__kug
        else:
            return set(saa__rmox for saa__rmox in apn__ypvn if saa__rmox <
                fbbf__ocmbb)
    return None
