"""
Implements BodoSQL array kernels related to JSON utilities
"""
import numba
from numba.core import types
import bodo
from bodo.libs.bodosql_array_kernel_utils import *


@numba.generated_jit(nopython=True)
def parse_json(arg):
    if isinstance(arg, types.optional):
        return bodo.libs.bodosql_array_kernel_utils.unopt_argument(
            'bodo.libs.bodosql_array_kernels.parse_json', ['arg'], 0)

    def impl(arg):
        return parse_json_util(arg)
    return impl


@numba.generated_jit(nopython=True)
def parse_single_json_map(s):

    def impl(s):
        oqvo__rhe = 1
        waa__ooex = {}
        ewz__vlau = ['{']
        xlq__rvk = ''
        szsj__iohqu = ''
        sdg__haur = False
        for whrt__wia in s:
            if oqvo__rhe == 1:
                if whrt__wia.isspace():
                    continue
                elif whrt__wia == '{':
                    oqvo__rhe = 2
                else:
                    return None
            elif oqvo__rhe == 2:
                if whrt__wia.isspace():
                    continue
                elif whrt__wia == '"':
                    oqvo__rhe = 3
                elif whrt__wia == '}':
                    oqvo__rhe = 9
                else:
                    return None
            elif oqvo__rhe == 3:
                if sdg__haur:
                    xlq__rvk += whrt__wia
                    sdg__haur = False
                elif whrt__wia == '"':
                    oqvo__rhe = 4
                elif whrt__wia == '\\':
                    sdg__haur = True
                else:
                    xlq__rvk += whrt__wia
            elif oqvo__rhe == 4:
                if whrt__wia.isspace():
                    continue
                elif whrt__wia == ':':
                    oqvo__rhe = 5
                else:
                    return None
            elif oqvo__rhe == 5:
                if whrt__wia.isspace():
                    continue
                if whrt__wia in '},]':
                    return None
                else:
                    oqvo__rhe = 7 if whrt__wia == '"' else 6
                    szsj__iohqu += whrt__wia
                    if whrt__wia in '{[':
                        ewz__vlau.append(whrt__wia)
            elif oqvo__rhe == 6:
                if whrt__wia.isspace():
                    continue
                if whrt__wia in '{[':
                    szsj__iohqu += whrt__wia
                    ewz__vlau.append(whrt__wia)
                elif whrt__wia in '}]':
                    tnzz__ykxh = '{' if whrt__wia == '}' else '['
                    if len(ewz__vlau) == 0 or ewz__vlau[-1] != tnzz__ykxh:
                        return None
                    elif len(ewz__vlau) == 1:
                        waa__ooex[xlq__rvk] = szsj__iohqu
                        xlq__rvk = ''
                        szsj__iohqu = ''
                        ewz__vlau.pop()
                        oqvo__rhe = 9
                    elif len(ewz__vlau) == 2:
                        szsj__iohqu += whrt__wia
                        waa__ooex[xlq__rvk] = szsj__iohqu
                        xlq__rvk = ''
                        szsj__iohqu = ''
                        ewz__vlau.pop()
                        oqvo__rhe = 8
                    else:
                        szsj__iohqu += whrt__wia
                        ewz__vlau.pop()
                elif whrt__wia == '"':
                    szsj__iohqu += whrt__wia
                    oqvo__rhe = 7
                elif whrt__wia == ',':
                    if len(ewz__vlau) == 1:
                        waa__ooex[xlq__rvk] = szsj__iohqu
                        xlq__rvk = ''
                        szsj__iohqu = ''
                        oqvo__rhe = 2
                    else:
                        szsj__iohqu += whrt__wia
                else:
                    szsj__iohqu += whrt__wia
            elif oqvo__rhe == 7:
                if sdg__haur:
                    szsj__iohqu += whrt__wia
                    sdg__haur = False
                elif whrt__wia == '\\':
                    sdg__haur = True
                elif whrt__wia == '"':
                    szsj__iohqu += whrt__wia
                    oqvo__rhe = 6
                else:
                    szsj__iohqu += whrt__wia
            elif oqvo__rhe == 8:
                if whrt__wia.isspace():
                    continue
                elif whrt__wia == ',':
                    oqvo__rhe = 2
                elif whrt__wia == '}':
                    oqvo__rhe = 9
                else:
                    return None
            elif oqvo__rhe == 9:
                if not whrt__wia.isspace():
                    return None
        return waa__ooex if oqvo__rhe == 9 else None
    return impl


@numba.generated_jit(nopython=True)
def parse_json_util(arr):
    bodo.libs.bodosql_array_kernels.verify_string_arg(arr, 'PARSE_JSON', 's')
    esxj__cwfe = ['arr']
    rfr__xoea = [arr]
    pjj__brchm = [False]
    kyi__tkldp = """jmap = bodo.libs.bodosql_json_array_kernels.parse_single_json_map(arg0) if arg0 is not None else None
"""
    if bodo.utils.utils.is_array_typ(arr, True):
        lral__edarz = (
            'lengths = bodo.utils.utils.alloc_type(n, bodo.int32, (-1,))\n')
        kyi__tkldp += 'res.append(jmap)\n'
        kyi__tkldp += 'if jmap is None:\n'
        kyi__tkldp += '   lengths[i] = 0\n'
        kyi__tkldp += 'else:\n'
        kyi__tkldp += '   lengths[i] = len(jmap)\n'
    else:
        lral__edarz = None
        kyi__tkldp += 'return jmap'
    qquwr__njo = (
        'res2 = bodo.libs.map_arr_ext.pre_alloc_map_array(n, lengths, out_dtype)\n'
        )
    qquwr__njo += 'numba.parfors.parfor.init_prange()\n'
    qquwr__njo += 'for i in numba.parfors.parfor.internal_prange(n):\n'
    qquwr__njo += '   if res[i] is None:\n'
    qquwr__njo += '     bodo.libs.array_kernels.setna(res2, i)\n'
    qquwr__njo += '   else:\n'
    qquwr__njo += '     res2[i] = res[i]\n'
    qquwr__njo += 'res = res2\n'
    psm__pdkg = bodo.StructArrayType((bodo.string_array_type, bodo.
        string_array_type), ('key', 'value'))
    scne__jzzqw = bodo.utils.typing.to_nullable_type(psm__pdkg)
    return gen_vectorized(esxj__cwfe, rfr__xoea, pjj__brchm, kyi__tkldp,
        scne__jzzqw, prefix_code=lral__edarz, suffix_code=qquwr__njo,
        res_list=True, support_dict_encoding=False)
