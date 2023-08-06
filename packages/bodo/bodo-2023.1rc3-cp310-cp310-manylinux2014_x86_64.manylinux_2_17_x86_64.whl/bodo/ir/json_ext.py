import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from numba.core import cgutils, ir, ir_utils, typeinfer, types
from numba.core.ir_utils import compile_to_numba_ir, replace_arg_nodes
from numba.extending import intrinsic
import bodo
import bodo.ir.connector
from bodo import objmode
from bodo.io.fs_io import get_storage_options_pyobject, storage_options_dict_type
from bodo.libs.str_ext import string_type
from bodo.transforms import distributed_analysis, distributed_pass
from bodo.utils.utils import check_and_propagate_cpp_exception, check_java_installation, sanitize_varname


class JsonReader(ir.Stmt):

    def __init__(self, df_out, loc, out_vars, out_types, file_name,
        df_colnames, orient, convert_dates, precise_float, lines,
        compression, storage_options):
        self.connector_typ = 'json'
        self.df_out = df_out
        self.loc = loc
        self.out_vars = out_vars
        self.out_types = out_types
        self.file_name = file_name
        self.df_colnames = df_colnames
        self.orient = orient
        self.convert_dates = convert_dates
        self.precise_float = precise_float
        self.lines = lines
        self.compression = compression
        self.storage_options = storage_options

    def __repr__(self):
        return ('{} = ReadJson(file={}, col_names={}, types={}, vars={})'.
            format(self.df_out, self.file_name, self.df_colnames, self.
            out_types, self.out_vars))


import llvmlite.binding as ll
from bodo.io import json_cpp
ll.add_symbol('json_file_chunk_reader', json_cpp.json_file_chunk_reader)


@intrinsic
def json_file_chunk_reader(typingctx, fname_t, lines_t, is_parallel_t,
    nrows_t, compression_t, bucket_region_t, storage_options_t):
    assert storage_options_t == storage_options_dict_type, "Storage options don't match expected type"

    def codegen(context, builder, sig, args):
        ljdzv__gaaw = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(1), lir.IntType(1), lir.
            IntType(64), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer()])
        ksk__rxtpv = cgutils.get_or_insert_function(builder.module,
            ljdzv__gaaw, name='json_file_chunk_reader')
        pwfb__jmo = builder.call(ksk__rxtpv, args)
        context.compile_internal(builder, lambda :
            check_and_propagate_cpp_exception(), types.none(), [])
        bev__nnseg = cgutils.create_struct_proxy(types.stream_reader_type)(
            context, builder)
        fufx__inemf = context.get_python_api(builder)
        bev__nnseg.meminfo = fufx__inemf.nrt_meminfo_new_from_pyobject(context
            .get_constant_null(types.voidptr), pwfb__jmo)
        bev__nnseg.pyobj = pwfb__jmo
        fufx__inemf.decref(pwfb__jmo)
        return bev__nnseg._getvalue()
    return types.stream_reader_type(types.voidptr, types.bool_, types.bool_,
        types.int64, types.voidptr, types.voidptr, storage_options_dict_type
        ), codegen


def remove_dead_json(json_node, lives_no_aliases, lives, arg_aliases,
    alias_map, func_ir, typemap):
    wmyky__pcqd = []
    rxg__wlk = []
    gclf__wjalc = []
    for qoqa__ccwb, megfc__lao in enumerate(json_node.out_vars):
        if megfc__lao.name in lives:
            wmyky__pcqd.append(json_node.df_colnames[qoqa__ccwb])
            rxg__wlk.append(json_node.out_vars[qoqa__ccwb])
            gclf__wjalc.append(json_node.out_types[qoqa__ccwb])
    json_node.df_colnames = wmyky__pcqd
    json_node.out_vars = rxg__wlk
    json_node.out_types = gclf__wjalc
    if len(json_node.out_vars) == 0:
        return None
    return json_node


def json_distributed_run(json_node, array_dists, typemap, calltypes,
    typingctx, targetctx):
    if bodo.user_logging.get_verbose_level() >= 1:
        dkyvd__rcv = (
            'Finish column pruning on read_json node:\n%s\nColumns loaded %s\n'
            )
        kqlk__rhu = json_node.loc.strformat()
        jrs__plt = json_node.df_colnames
        bodo.user_logging.log_message('Column Pruning', dkyvd__rcv,
            kqlk__rhu, jrs__plt)
        eil__xalt = [onjg__rndn for qoqa__ccwb, onjg__rndn in enumerate(
            json_node.df_colnames) if isinstance(json_node.out_types[
            qoqa__ccwb], bodo.libs.dict_arr_ext.DictionaryArrayType)]
        if eil__xalt:
            bdys__whih = """Finished optimized encoding on read_json node:
%s
Columns %s using dictionary encoding to reduce memory usage.
"""
            bodo.user_logging.log_message('Dictionary Encoding', bdys__whih,
                kqlk__rhu, eil__xalt)
    parallel = False
    if array_dists is not None:
        parallel = True
        for oypbz__kwj in json_node.out_vars:
            if array_dists[oypbz__kwj.name
                ] != distributed_pass.Distribution.OneD and array_dists[
                oypbz__kwj.name] != distributed_pass.Distribution.OneD_Var:
                parallel = False
    emgme__rkrx = len(json_node.out_vars)
    laiir__mczx = ', '.join('arr' + str(qoqa__ccwb) for qoqa__ccwb in range
        (emgme__rkrx))
    xng__gyv = 'def json_impl(fname):\n'
    xng__gyv += '    ({},) = _json_reader_py(fname)\n'.format(laiir__mczx)
    ydvz__mtcw = {}
    exec(xng__gyv, {}, ydvz__mtcw)
    qtoz__yvhb = ydvz__mtcw['json_impl']
    svtfz__jms = _gen_json_reader_py(json_node.df_colnames, json_node.
        out_types, typingctx, targetctx, parallel, json_node.orient,
        json_node.convert_dates, json_node.precise_float, json_node.lines,
        json_node.compression, json_node.storage_options)
    kwcm__srubu = compile_to_numba_ir(qtoz__yvhb, {'_json_reader_py':
        svtfz__jms}, typingctx=typingctx, targetctx=targetctx, arg_typs=(
        string_type,), typemap=typemap, calltypes=calltypes).blocks.popitem()[1
        ]
    replace_arg_nodes(kwcm__srubu, [json_node.file_name])
    qfzq__pit = kwcm__srubu.body[:-3]
    for qoqa__ccwb in range(len(json_node.out_vars)):
        qfzq__pit[-len(json_node.out_vars) + qoqa__ccwb
            ].target = json_node.out_vars[qoqa__ccwb]
    return qfzq__pit


numba.parfors.array_analysis.array_analysis_extensions[JsonReader
    ] = bodo.ir.connector.connector_array_analysis
distributed_analysis.distributed_analysis_extensions[JsonReader
    ] = bodo.ir.connector.connector_distributed_analysis
typeinfer.typeinfer_extensions[JsonReader
    ] = bodo.ir.connector.connector_typeinfer
ir_utils.visit_vars_extensions[JsonReader
    ] = bodo.ir.connector.visit_vars_connector
ir_utils.remove_dead_extensions[JsonReader] = remove_dead_json
numba.core.analysis.ir_extension_usedefs[JsonReader
    ] = bodo.ir.connector.connector_usedefs
ir_utils.copy_propagate_extensions[JsonReader
    ] = bodo.ir.connector.get_copies_connector
ir_utils.apply_copy_propagate_extensions[JsonReader
    ] = bodo.ir.connector.apply_copies_connector
ir_utils.build_defs_extensions[JsonReader
    ] = bodo.ir.connector.build_connector_definitions
distributed_pass.distributed_run_extensions[JsonReader] = json_distributed_run
compiled_funcs = []


def _gen_json_reader_py(col_names, col_typs, typingctx, targetctx, parallel,
    orient, convert_dates, precise_float, lines, compression, storage_options):
    upu__rzvc = [sanitize_varname(onjg__rndn) for onjg__rndn in col_names]
    svl__mbgy = ', '.join(str(qoqa__ccwb) for qoqa__ccwb, gtrc__mmd in
        enumerate(col_typs) if gtrc__mmd.dtype == types.NPDatetime('ns'))
    mbk__qaqe = ', '.join(["{}='{}'".format(pqtx__xdbg, bodo.ir.csv_ext.
        _get_dtype_str(gtrc__mmd)) for pqtx__xdbg, gtrc__mmd in zip(
        upu__rzvc, col_typs)])
    flvav__bqbhc = ', '.join(["'{}':{}".format(sln__somyz, bodo.ir.csv_ext.
        _get_pd_dtype_str(gtrc__mmd)) for sln__somyz, gtrc__mmd in zip(
        col_names, col_typs)])
    if compression is None:
        compression = 'uncompressed'
    xng__gyv = 'def json_reader_py(fname):\n'
    xng__gyv += '  df_typeref_2 = df_typeref\n'
    xng__gyv += '  check_java_installation(fname)\n'
    xng__gyv += f"""  bucket_region = bodo.io.fs_io.get_s3_bucket_region_njit(fname, parallel={parallel})
"""
    if storage_options is None:
        storage_options = {}
    storage_options['bodo_dummy'] = 'dummy'
    xng__gyv += (
        f'  storage_options_py = get_storage_options_pyobject({str(storage_options)})\n'
        )
    xng__gyv += (
        '  f_reader = bodo.ir.json_ext.json_file_chunk_reader(bodo.libs.str_ext.unicode_to_utf8(fname), '
        )
    xng__gyv += (
        """    {}, {}, -1, bodo.libs.str_ext.unicode_to_utf8('{}'), bodo.libs.str_ext.unicode_to_utf8(bucket_region), storage_options_py )
"""
        .format(lines, parallel, compression))
    xng__gyv += '  if bodo.utils.utils.is_null_pointer(f_reader._pyobj):\n'
    xng__gyv += "      raise FileNotFoundError('File does not exist')\n"
    xng__gyv += f'  with objmode({mbk__qaqe}):\n'
    xng__gyv += f"    df = pd.read_json(f_reader, orient='{orient}',\n"
    xng__gyv += f'       convert_dates = {convert_dates}, \n'
    xng__gyv += f'       precise_float={precise_float}, \n'
    xng__gyv += f'       lines={lines}, \n'
    xng__gyv += '       dtype={{{}}},\n'.format(flvav__bqbhc)
    xng__gyv += '       )\n'
    xng__gyv += (
        '    bodo.ir.connector.cast_float_to_nullable(df, df_typeref_2)\n')
    for pqtx__xdbg, sln__somyz in zip(upu__rzvc, col_names):
        xng__gyv += '    if len(df) > 0:\n'
        xng__gyv += "        {} = df['{}'].values\n".format(pqtx__xdbg,
            sln__somyz)
        xng__gyv += '    else:\n'
        xng__gyv += '        {} = np.array([])\n'.format(pqtx__xdbg)
    xng__gyv += '  return ({},)\n'.format(', '.join(zre__aacr for zre__aacr in
        upu__rzvc))
    ulp__auhkp = globals()
    ulp__auhkp.update({'bodo': bodo, 'pd': pd, 'np': np, 'objmode': objmode,
        'check_java_installation': check_java_installation, 'df_typeref':
        bodo.DataFrameType(tuple(col_typs), bodo.RangeIndexType(None),
        tuple(col_names)), 'get_storage_options_pyobject':
        get_storage_options_pyobject})
    ydvz__mtcw = {}
    exec(xng__gyv, ulp__auhkp, ydvz__mtcw)
    svtfz__jms = ydvz__mtcw['json_reader_py']
    hhsc__cytb = numba.njit(svtfz__jms)
    compiled_funcs.append(hhsc__cytb)
    return hhsc__cytb
