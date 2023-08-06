"""
Common IR extension functions for connectors such as CSV, Parquet and JSON readers.
"""
import sys
from collections import defaultdict
from typing import Literal, Set, Tuple
import numba
from numba.core import ir, types
from numba.core.ir_utils import replace_vars_inner, visit_vars_inner
from bodo.hiframes.table import TableType
from bodo.transforms.distributed_analysis import Distribution
from bodo.transforms.table_column_del_pass import get_live_column_nums_block
from bodo.utils.py_objs import install_py_obj_class
from bodo.utils.typing import BodoError
from bodo.utils.utils import debug_prints, is_array_typ


def connector_array_analysis(node, equiv_set, typemap, array_analysis):
    sdn__ipcts = []
    assert len(node.out_vars) > 0, 'empty {} in array analysis'.format(node
        .connector_typ)
    if node.connector_typ == 'csv' and node.chunksize is not None:
        return [], []
    dorop__jpi = []
    for msci__brl, mmma__wmcsm in enumerate(node.out_vars):
        lbbe__enpl = typemap[mmma__wmcsm.name]
        if lbbe__enpl == types.none:
            continue
        yjzug__jvocv = msci__brl == 0 and node.connector_typ in ('parquet',
            'sql') and not node.is_live_table
        vzo__qobl = node.connector_typ == 'sql' and msci__brl > 1
        if not (yjzug__jvocv or vzo__qobl):
            qus__zqka = array_analysis._gen_shape_call(equiv_set,
                mmma__wmcsm, lbbe__enpl.ndim, None, sdn__ipcts)
            equiv_set.insert_equiv(mmma__wmcsm, qus__zqka)
            dorop__jpi.append(qus__zqka[0])
            equiv_set.define(mmma__wmcsm, set())
    if len(dorop__jpi) > 1:
        equiv_set.insert_equiv(*dorop__jpi)
    return [], sdn__ipcts


def connector_distributed_analysis(node, array_dists):
    from bodo.ir.sql_ext import SqlReader
    if isinstance(node, SqlReader) and not node.is_select_query:
        ufj__fsjn = Distribution.REP
    elif isinstance(node, SqlReader) and node.limit is not None:
        ufj__fsjn = Distribution.OneD_Var
    else:
        ufj__fsjn = Distribution.OneD
    for imph__vgdrk in node.out_vars:
        if imph__vgdrk.name in array_dists:
            ufj__fsjn = Distribution(min(ufj__fsjn.value, array_dists[
                imph__vgdrk.name].value))
    for imph__vgdrk in node.out_vars:
        array_dists[imph__vgdrk.name] = ufj__fsjn


def connector_typeinfer(node, typeinferer):
    if node.connector_typ == 'csv':
        if node.chunksize is not None:
            typeinferer.lock_type(node.out_vars[0].name, node.out_types[0],
                loc=node.loc)
        else:
            typeinferer.lock_type(node.out_vars[0].name, TableType(tuple(
                node.out_types)), loc=node.loc)
            typeinferer.lock_type(node.out_vars[1].name, node.
                index_column_typ, loc=node.loc)
        return
    if node.connector_typ in ('parquet', 'sql'):
        typeinferer.lock_type(node.out_vars[0].name, TableType(tuple(node.
            out_types)), loc=node.loc)
        typeinferer.lock_type(node.out_vars[1].name, node.index_column_type,
            loc=node.loc)
        if node.connector_typ == 'sql':
            if len(node.out_vars) > 2:
                typeinferer.lock_type(node.out_vars[2].name, node.
                    file_list_type, loc=node.loc)
            if len(node.out_vars) > 3:
                typeinferer.lock_type(node.out_vars[3].name, node.
                    snapshot_id_type, loc=node.loc)
        return
    for mmma__wmcsm, lbbe__enpl in zip(node.out_vars, node.out_types):
        typeinferer.lock_type(mmma__wmcsm.name, lbbe__enpl, loc=node.loc)


def visit_vars_connector(node, callback, cbdata):
    if debug_prints():
        print('visiting {} vars for:'.format(node.connector_typ), node)
        print('cbdata: ', sorted(cbdata.items()))
    tjh__efi = []
    for mmma__wmcsm in node.out_vars:
        gjps__eulf = visit_vars_inner(mmma__wmcsm, callback, cbdata)
        tjh__efi.append(gjps__eulf)
    node.out_vars = tjh__efi
    if node.connector_typ in ('csv', 'parquet', 'json'):
        node.file_name = visit_vars_inner(node.file_name, callback, cbdata)
    if node.connector_typ == 'csv':
        node.nrows = visit_vars_inner(node.nrows, callback, cbdata)
        node.skiprows = visit_vars_inner(node.skiprows, callback, cbdata)
    if node.connector_typ in ('parquet', 'sql') and node.filters:
        for rru__hznn in node.filters:
            for msci__brl in range(len(rru__hznn)):
                tzr__crw = rru__hznn[msci__brl]
                rru__hznn[msci__brl] = tzr__crw[0], tzr__crw[1
                    ], visit_vars_inner(tzr__crw[2], callback, cbdata)


def connector_usedefs(node, use_set=None, def_set=None):
    if use_set is None:
        use_set = set()
    if def_set is None:
        def_set = set()
    def_set.update({imph__vgdrk.name for imph__vgdrk in node.out_vars})
    if node.connector_typ in ('csv', 'parquet', 'json'):
        use_set.add(node.file_name.name)
    if node.connector_typ == 'csv':
        if isinstance(node.nrows, numba.core.ir.Var):
            use_set.add(node.nrows.name)
        if isinstance(node.skiprows, numba.core.ir.Var):
            use_set.add(node.skiprows.name)
    if node.connector_typ in ('parquet', 'sql') and node.filters:
        for mfnyr__orpy in node.filters:
            for imph__vgdrk in mfnyr__orpy:
                if isinstance(imph__vgdrk[2], ir.Var):
                    use_set.add(imph__vgdrk[2].name)
    return numba.core.analysis._use_defs_result(usemap=use_set, defmap=def_set)


def get_copies_connector(node, typemap):
    nhas__ujatg = set(imph__vgdrk.name for imph__vgdrk in node.out_vars)
    return set(), nhas__ujatg


def apply_copies_connector(node, var_dict, name_var_table, typemap,
    calltypes, save_copies):
    tjh__efi = []
    for mmma__wmcsm in node.out_vars:
        gjps__eulf = replace_vars_inner(mmma__wmcsm, var_dict)
        tjh__efi.append(gjps__eulf)
    node.out_vars = tjh__efi
    if node.connector_typ in ('csv', 'parquet', 'json'):
        node.file_name = replace_vars_inner(node.file_name, var_dict)
    if node.connector_typ in ('parquet', 'sql') and node.filters:
        for rru__hznn in node.filters:
            for msci__brl in range(len(rru__hznn)):
                tzr__crw = rru__hznn[msci__brl]
                rru__hznn[msci__brl] = tzr__crw[0], tzr__crw[1
                    ], replace_vars_inner(tzr__crw[2], var_dict)
    if node.connector_typ == 'csv':
        node.nrows = replace_vars_inner(node.nrows, var_dict)
        node.skiprows = replace_vars_inner(node.skiprows, var_dict)


def build_connector_definitions(node, definitions=None):
    if definitions is None:
        definitions = defaultdict(list)
    for mmma__wmcsm in node.out_vars:
        sag__vuhjk = definitions[mmma__wmcsm.name]
        if node not in sag__vuhjk:
            sag__vuhjk.append(node)
    return definitions


def generate_filter_map(filters):
    if filters:
        filter_vars = []
        xzepw__uhsv = [imph__vgdrk[2] for mfnyr__orpy in filters for
            imph__vgdrk in mfnyr__orpy]
        yhhcl__ulpbz = set()
        for oht__zgf in xzepw__uhsv:
            if isinstance(oht__zgf, ir.Var):
                if oht__zgf.name not in yhhcl__ulpbz:
                    filter_vars.append(oht__zgf)
                yhhcl__ulpbz.add(oht__zgf.name)
        return {imph__vgdrk.name: f'f{msci__brl}' for msci__brl,
            imph__vgdrk in enumerate(filter_vars)}, filter_vars
    else:
        return {}, []


this_module = sys.modules[__name__]
StreamReaderType = install_py_obj_class(types_name='stream_reader_type',
    module=this_module, class_name='StreamReaderType', model_name=
    'StreamReaderModel')


def trim_extra_used_columns(used_columns: Set, num_columns: int):
    return {msci__brl for msci__brl in used_columns if msci__brl < num_columns}


def cast_float_to_nullable(df, df_type):
    import bodo
    qmif__dmr = {}
    for msci__brl, sfou__xvv in enumerate(df_type.data):
        if isinstance(sfou__xvv, bodo.IntegerArrayType):
            xsdg__hdyoh = sfou__xvv.get_pandas_scalar_type_instance
            if xsdg__hdyoh not in qmif__dmr:
                qmif__dmr[xsdg__hdyoh] = []
            qmif__dmr[xsdg__hdyoh].append(df.columns[msci__brl])
    for lbbe__enpl, gnaat__vyp in qmif__dmr.items():
        df[gnaat__vyp] = df[gnaat__vyp].astype(lbbe__enpl)


def connector_table_column_use(node, block_use_map, equiv_vars, typemap,
    table_col_use_map):
    return


def base_connector_remove_dead_columns(node, column_live_map, equiv_vars,
    typemap, nodename, possible_cols, require_one_column=True):
    khb__dzrgi = node.out_vars[0].name
    assert isinstance(typemap[khb__dzrgi], TableType
        ), f'{nodename} Node Table must be a TableType'
    if possible_cols:
        used_columns, ediu__qlde, pyl__rki = get_live_column_nums_block(
            column_live_map, equiv_vars, khb__dzrgi)
        if not (ediu__qlde or pyl__rki):
            used_columns = trim_extra_used_columns(used_columns, len(
                possible_cols))
            if not used_columns and require_one_column:
                used_columns = {0}
            if len(used_columns) != len(node.out_used_cols):
                node.out_used_cols = list(sorted(used_columns))
    """We return flase in all cases, as no changes performed in the file will allow for dead code elimination to do work."""
    return False


def is_connector_table_parallel(node, array_dists, typemap, node_name):
    kjl__dcwvi = False
    if array_dists is not None:
        ume__jhe = node.out_vars[0].name
        kjl__dcwvi = array_dists[ume__jhe] in (Distribution.OneD,
            Distribution.OneD_Var)
        orig__ree = node.out_vars[1].name
        assert typemap[orig__ree
            ] == types.none or not kjl__dcwvi or array_dists[orig__ree] in (
            Distribution.OneD, Distribution.OneD_Var
            ), f'{node_name} data/index parallelization does not match'
    return kjl__dcwvi


def generate_arrow_filters(filters, filter_map, filter_vars, col_names,
    partition_names, original_out_types, typemap, source: Literal['parquet',
    'iceberg'], output_dnf=True) ->Tuple[str, str]:
    jeg__pzznr = 'None'
    dmri__xrt = 'None'
    if filters:
        oan__ympn = []
        bsuhm__hgjy = []
        yxlxs__qrs = False
        orig_colname_map = {vyqe__vnbr: msci__brl for msci__brl, vyqe__vnbr in
            enumerate(col_names)}
        for rru__hznn in filters:
            liehu__pbgja = []
            gpb__qfb = []
            for imph__vgdrk in rru__hznn:
                if isinstance(imph__vgdrk[2], ir.Var):
                    qiakh__qbn, yoeyz__isf = determine_filter_cast(
                        original_out_types, typemap, imph__vgdrk,
                        orig_colname_map, partition_names, source)
                    if imph__vgdrk[1] == 'in':
                        dtisf__ofour = (
                            f"(ds.field('{imph__vgdrk[0]}').isin({filter_map[imph__vgdrk[2].name]}))"
                            )
                    else:
                        dtisf__ofour = (
                            f"(ds.field('{imph__vgdrk[0]}'){qiakh__qbn} {imph__vgdrk[1]} ds.scalar({filter_map[imph__vgdrk[2].name]}){yoeyz__isf})"
                            )
                else:
                    assert imph__vgdrk[2
                        ] == 'NULL', 'unsupport constant used in filter pushdown'
                    if imph__vgdrk[1] == 'is not':
                        jbe__njpro = '~'
                    else:
                        jbe__njpro = ''
                    dtisf__ofour = (
                        f"({jbe__njpro}ds.field('{imph__vgdrk[0]}').is_null())"
                        )
                gpb__qfb.append(dtisf__ofour)
                if not yxlxs__qrs:
                    if imph__vgdrk[0] in partition_names and isinstance(
                        imph__vgdrk[2], ir.Var):
                        if output_dnf:
                            bznq__crn = (
                                f"('{imph__vgdrk[0]}', '{imph__vgdrk[1]}', {filter_map[imph__vgdrk[2].name]})"
                                )
                        else:
                            bznq__crn = dtisf__ofour
                        liehu__pbgja.append(bznq__crn)
                    elif imph__vgdrk[0] in partition_names and not isinstance(
                        imph__vgdrk[2], ir.Var) and source == 'iceberg':
                        if output_dnf:
                            bznq__crn = (
                                f"('{imph__vgdrk[0]}', '{imph__vgdrk[1]}', '{imph__vgdrk[2]}')"
                                )
                        else:
                            bznq__crn = dtisf__ofour
                        liehu__pbgja.append(bznq__crn)
            ldpl__ciym = ''
            if liehu__pbgja:
                if output_dnf:
                    ldpl__ciym = ', '.join(liehu__pbgja)
                else:
                    ldpl__ciym = ' & '.join(liehu__pbgja)
            else:
                yxlxs__qrs = True
            unzr__dsv = ' & '.join(gpb__qfb)
            if ldpl__ciym:
                if output_dnf:
                    oan__ympn.append(f'[{ldpl__ciym}]')
                else:
                    oan__ympn.append(f'({ldpl__ciym})')
            bsuhm__hgjy.append(f'({unzr__dsv})')
        if output_dnf:
            fpt__ncn = ', '.join(oan__ympn)
        else:
            fpt__ncn = ' | '.join(oan__ympn)
        jvlbc__qlhx = ' | '.join(bsuhm__hgjy)
        if fpt__ncn and not yxlxs__qrs:
            if output_dnf:
                jeg__pzznr = f'[{fpt__ncn}]'
            else:
                jeg__pzznr = f'({fpt__ncn})'
        dmri__xrt = f'({jvlbc__qlhx})'
    return jeg__pzznr, dmri__xrt


def determine_filter_cast(col_types, typemap, filter_val, orig_colname_map,
    partition_names, source):
    import bodo
    msj__xqf = filter_val[0]
    itw__dksvo = col_types[orig_colname_map[msj__xqf]]
    cbsyg__tdeov = bodo.utils.typing.element_type(itw__dksvo)
    if source == 'parquet' and msj__xqf in partition_names:
        if cbsyg__tdeov == types.unicode_type:
            ntg__tug = '.cast(pyarrow.string(), safe=False)'
        elif isinstance(cbsyg__tdeov, types.Integer):
            ntg__tug = f'.cast(pyarrow.{cbsyg__tdeov.name}(), safe=False)'
        else:
            ntg__tug = ''
    else:
        ntg__tug = ''
    oocxl__chrw = typemap[filter_val[2].name]
    if isinstance(oocxl__chrw, (types.List, types.Set)):
        mqsie__ybu = oocxl__chrw.dtype
    elif is_array_typ(oocxl__chrw):
        mqsie__ybu = oocxl__chrw.dtype
    else:
        mqsie__ybu = oocxl__chrw
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(cbsyg__tdeov,
        'Filter pushdown')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(mqsie__ybu,
        'Filter pushdown')
    if not bodo.utils.typing.is_common_scalar_dtype([cbsyg__tdeov, mqsie__ybu]
        ):
        if not bodo.utils.typing.is_safe_arrow_cast(cbsyg__tdeov, mqsie__ybu):
            raise BodoError(
                f'Unsupported Arrow cast from {cbsyg__tdeov} to {mqsie__ybu} in filter pushdown. Please try a comparison that avoids casting the column.'
                )
        if cbsyg__tdeov == types.unicode_type and mqsie__ybu in (bodo.
            datetime64ns, bodo.pd_timestamp_tz_naive_type):
            return ".cast(pyarrow.timestamp('ns'), safe=False)", ''
        elif mqsie__ybu == types.unicode_type and cbsyg__tdeov in (bodo.
            datetime64ns, bodo.pd_timestamp_tz_naive_type):
            if isinstance(oocxl__chrw, (types.List, types.Set)):
                awm__bcym = 'list' if isinstance(oocxl__chrw, types.List
                    ) else 'tuple'
                raise BodoError(
                    f'Cannot cast {awm__bcym} values with isin filter pushdown.'
                    )
            return ntg__tug, ".cast(pyarrow.timestamp('ns'), safe=False)"
        elif cbsyg__tdeov == bodo.datetime_date_type and mqsie__ybu in (bodo
            .datetime64ns, bodo.pd_timestamp_tz_naive_type):
            return ".cast(pyarrow.timestamp('ns'), safe=False)", ''
        elif mqsie__ybu == bodo.datetime_date_type and cbsyg__tdeov in (bodo
            .datetime64ns, bodo.pd_timestamp_tz_naive_type):
            return ntg__tug, ".cast(pyarrow.timestamp('ns'), safe=False)"
    return ntg__tug, ''
