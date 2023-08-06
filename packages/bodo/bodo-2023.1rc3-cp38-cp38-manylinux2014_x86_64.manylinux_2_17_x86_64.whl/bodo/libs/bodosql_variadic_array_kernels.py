"""
Implements array kernels that are specific to BodoSQL which have a variable
number of arguments
"""
from numba.core import types
from numba.extending import overload
import bodo
from bodo.libs.bodosql_array_kernel_utils import *
from bodo.utils.typing import is_str_arr_type, raise_bodo_error


def coalesce(A):
    return


@overload(coalesce)
def overload_coalesce(A):
    if not isinstance(A, (types.Tuple, types.UniTuple)):
        raise_bodo_error('Coalesce argument must be a tuple')
    for lsdut__iqky in range(len(A)):
        if isinstance(A[lsdut__iqky], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.coalesce',
                ['A'], 0, container_arg=lsdut__iqky, container_length=len(A))

    def impl(A):
        return coalesce_util(A)
    return impl


def coalesce_util(A):
    return


@overload(coalesce_util, no_unliteral=True)
def overload_coalesce_util(A):
    if len(A) == 0:
        raise_bodo_error('Cannot coalesce 0 columns')
    peh__eugt = None
    yul__ummj = []
    eqtzh__loxs = False
    for lsdut__iqky in range(len(A)):
        if A[lsdut__iqky] == bodo.none:
            yul__ummj.append(lsdut__iqky)
        elif not bodo.utils.utils.is_array_typ(A[lsdut__iqky]):
            for jtaby__flsv in range(lsdut__iqky + 1, len(A)):
                yul__ummj.append(jtaby__flsv)
                if bodo.utils.utils.is_array_typ(A[jtaby__flsv]):
                    peh__eugt = f'A[{jtaby__flsv}]'
                    eqtzh__loxs = True
            break
        else:
            eqtzh__loxs = True
    kji__rkuau = [f'A{lsdut__iqky}' for lsdut__iqky in range(len(A)) if 
        lsdut__iqky not in yul__ummj]
    vhnq__zkzn = [A[lsdut__iqky] for lsdut__iqky in range(len(A)) if 
        lsdut__iqky not in yul__ummj]
    lxo__bprev = get_common_broadcasted_type(vhnq__zkzn, 'COALESCE')
    pijxe__rmo = eqtzh__loxs and is_str_arr_type(lxo__bprev)
    ieuoi__npi = [False] * (len(A) - len(yul__ummj))
    lhgs__elgx = False
    if pijxe__rmo:
        lhgs__elgx = True
        for jtaby__flsv, jkur__vsfqp in enumerate(vhnq__zkzn):
            lhgs__elgx = lhgs__elgx and (jkur__vsfqp == bodo.string_type or
                jkur__vsfqp == bodo.dict_str_arr_type or isinstance(
                jkur__vsfqp, bodo.SeriesType) and jkur__vsfqp.data == bodo.
                dict_str_arr_type)
    khkam__zmm = ''
    ros__ogi = True
    nalnb__fbwc = False
    jzga__mcskb = 0
    eyp__jjwxj = None
    if lhgs__elgx:
        eyp__jjwxj = 'num_strings = 0\n'
        eyp__jjwxj += 'num_chars = 0\n'
        eyp__jjwxj += 'is_dict_global = True\n'
        for lsdut__iqky in range(len(A)):
            if lsdut__iqky in yul__ummj:
                jzga__mcskb += 1
                continue
            elif vhnq__zkzn[lsdut__iqky - jzga__mcskb] != bodo.string_type:
                eyp__jjwxj += (
                    f'old_indices{lsdut__iqky - jzga__mcskb} = A{lsdut__iqky}._indices\n'
                    )
                eyp__jjwxj += (
                    f'old_data{lsdut__iqky - jzga__mcskb} = A{lsdut__iqky}._data\n'
                    )
                eyp__jjwxj += f"""is_dict_global = is_dict_global and A{lsdut__iqky}._has_global_dictionary
"""
                eyp__jjwxj += (
                    f'index_offset{lsdut__iqky - jzga__mcskb} = num_strings\n')
                eyp__jjwxj += (
                    f'num_strings += len(old_data{lsdut__iqky - jzga__mcskb})\n'
                    )
                eyp__jjwxj += f"""num_chars += bodo.libs.str_arr_ext.num_total_chars(old_data{lsdut__iqky - jzga__mcskb})
"""
            else:
                eyp__jjwxj += f'num_strings += 1\n'
                eyp__jjwxj += f"""num_chars += bodo.libs.str_ext.unicode_to_utf8_len(A{lsdut__iqky})
"""
    jzga__mcskb = 0
    for lsdut__iqky in range(len(A)):
        if lsdut__iqky in yul__ummj:
            jzga__mcskb += 1
            continue
        elif bodo.utils.utils.is_array_typ(A[lsdut__iqky]):
            dbmt__xpjz = 'if' if ros__ogi else 'elif'
            khkam__zmm += (
                f'{dbmt__xpjz} not bodo.libs.array_kernels.isna(A{lsdut__iqky}, i):\n'
                )
            if lhgs__elgx:
                khkam__zmm += f"""   res[i] = old_indices{lsdut__iqky - jzga__mcskb}[i] + index_offset{lsdut__iqky - jzga__mcskb}
"""
            elif pijxe__rmo:
                khkam__zmm += f"""   bodo.libs.str_arr_ext.get_str_arr_item_copy(res, i, A{lsdut__iqky}, i)
"""
            else:
                khkam__zmm += f'   res[i] = arg{lsdut__iqky - jzga__mcskb}\n'
            ros__ogi = False
        else:
            assert not nalnb__fbwc, 'should not encounter more than one scalar due to dead column pruning'
            yma__qytu = ''
            if not ros__ogi:
                khkam__zmm += 'else:\n'
                yma__qytu = '   '
            if lhgs__elgx:
                khkam__zmm += f'{yma__qytu}res[i] = num_strings - 1\n'
            else:
                khkam__zmm += (
                    f'{yma__qytu}res[i] = arg{lsdut__iqky - jzga__mcskb}\n')
            nalnb__fbwc = True
            break
    if not nalnb__fbwc:
        if not ros__ogi:
            khkam__zmm += 'else:\n'
            khkam__zmm += '   bodo.libs.array_kernels.setna(res, i)'
        else:
            khkam__zmm += 'bodo.libs.array_kernels.setna(res, i)'
    bnr__lgwc = None
    if lhgs__elgx:
        jzga__mcskb = 0
        bnr__lgwc = """dict_data = bodo.libs.str_arr_ext.pre_alloc_string_array(num_strings, num_chars)
"""
        bnr__lgwc += 'curr_index = 0\n'
        for lsdut__iqky in range(len(A)):
            if lsdut__iqky in yul__ummj:
                jzga__mcskb += 1
            elif vhnq__zkzn[lsdut__iqky - jzga__mcskb] != bodo.string_type:
                bnr__lgwc += (
                    f'section_len = len(old_data{lsdut__iqky - jzga__mcskb})\n'
                    )
                bnr__lgwc += f'for l in range(section_len):\n'
                bnr__lgwc += f"""    bodo.libs.str_arr_ext.get_str_arr_item_copy(dict_data, curr_index + l, old_data{lsdut__iqky - jzga__mcskb}, l)
"""
                bnr__lgwc += f'curr_index += section_len\n'
            else:
                bnr__lgwc += f'dict_data[curr_index] = A{lsdut__iqky}\n'
                bnr__lgwc += f'curr_index += 1\n'
        bnr__lgwc += """duplicated_res = bodo.libs.dict_arr_ext.init_dict_arr(dict_data, res, is_dict_global, False)
"""
        bnr__lgwc += """res = bodo.libs.array.drop_duplicates_local_dictionary(duplicated_res, False)
"""
    mqx__ixx = 'A'
    jxt__wmfi = {f'A{lsdut__iqky}': f'A[{lsdut__iqky}]' for lsdut__iqky in
        range(len(A)) if lsdut__iqky not in yul__ummj}
    if lhgs__elgx:
        lxo__bprev = bodo.libs.dict_arr_ext.dict_indices_arr_type
    return gen_vectorized(kji__rkuau, vhnq__zkzn, ieuoi__npi, khkam__zmm,
        lxo__bprev, mqx__ixx, jxt__wmfi, peh__eugt, support_dict_encoding=
        False, prefix_code=eyp__jjwxj, suffix_code=bnr__lgwc,
        alloc_array_scalars=not pijxe__rmo)


@numba.generated_jit(nopython=True)
def decode(A):
    if not isinstance(A, (types.Tuple, types.UniTuple)):
        raise_bodo_error('Decode argument must be a tuple')
    for lsdut__iqky in range(len(A)):
        if isinstance(A[lsdut__iqky], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.decode',
                ['A'], 0, container_arg=lsdut__iqky, container_length=len(A))

    def impl(A):
        return decode_util(A)
    return impl


@numba.generated_jit(nopython=True)
def decode_util(A):
    if len(A) < 3:
        raise_bodo_error('Need at least 3 arguments to DECODE')
    kji__rkuau = [f'A{lsdut__iqky}' for lsdut__iqky in range(len(A))]
    vhnq__zkzn = [A[lsdut__iqky] for lsdut__iqky in range(len(A))]
    ieuoi__npi = [False] * len(A)
    khkam__zmm = ''
    for lsdut__iqky in range(1, len(A) - 1, 2):
        dbmt__xpjz = 'if' if len(khkam__zmm) == 0 else 'elif'
        if A[lsdut__iqky + 1] == bodo.none:
            ndi__poprr = '   bodo.libs.array_kernels.setna(res, i)\n'
        elif bodo.utils.utils.is_array_typ(A[lsdut__iqky + 1]):
            ndi__poprr = (
                f'   if bodo.libs.array_kernels.isna({kji__rkuau[lsdut__iqky + 1]}, i):\n'
                )
            ndi__poprr += f'      bodo.libs.array_kernels.setna(res, i)\n'
            ndi__poprr += f'   else:\n'
            ndi__poprr += f'      res[i] = arg{lsdut__iqky + 1}\n'
        else:
            ndi__poprr = f'   res[i] = arg{lsdut__iqky + 1}\n'
        if A[0] == bodo.none and (bodo.utils.utils.is_array_typ(A[
            lsdut__iqky]) or A[lsdut__iqky] == bodo.none):
            if A[lsdut__iqky] == bodo.none:
                khkam__zmm += f'{dbmt__xpjz} True:\n'
                khkam__zmm += ndi__poprr
                break
            else:
                khkam__zmm += f"""{dbmt__xpjz} bodo.libs.array_kernels.isna({kji__rkuau[lsdut__iqky]}, i):
"""
                khkam__zmm += ndi__poprr
        elif A[0] == bodo.none:
            pass
        elif bodo.utils.utils.is_array_typ(A[0]):
            if bodo.utils.utils.is_array_typ(A[lsdut__iqky]):
                khkam__zmm += f"""{dbmt__xpjz} (bodo.libs.array_kernels.isna({kji__rkuau[0]}, i) and bodo.libs.array_kernels.isna({kji__rkuau[lsdut__iqky]}, i)) or (not bodo.libs.array_kernels.isna({kji__rkuau[0]}, i) and not bodo.libs.array_kernels.isna({kji__rkuau[lsdut__iqky]}, i) and arg0 == arg{lsdut__iqky}):
"""
                khkam__zmm += ndi__poprr
            elif A[lsdut__iqky] == bodo.none:
                khkam__zmm += (
                    f'{dbmt__xpjz} bodo.libs.array_kernels.isna({kji__rkuau[0]}, i):\n'
                    )
                khkam__zmm += ndi__poprr
            else:
                khkam__zmm += f"""{dbmt__xpjz} (not bodo.libs.array_kernels.isna({kji__rkuau[0]}, i)) and arg0 == arg{lsdut__iqky}:
"""
                khkam__zmm += ndi__poprr
        elif A[lsdut__iqky] == bodo.none:
            pass
        elif bodo.utils.utils.is_array_typ(A[lsdut__iqky]):
            khkam__zmm += f"""{dbmt__xpjz} (not bodo.libs.array_kernels.isna({kji__rkuau[lsdut__iqky]}, i)) and arg0 == arg{lsdut__iqky}:
"""
            khkam__zmm += ndi__poprr
        else:
            khkam__zmm += f'{dbmt__xpjz} arg0 == arg{lsdut__iqky}:\n'
            khkam__zmm += ndi__poprr
    if len(khkam__zmm) > 0:
        khkam__zmm += 'else:\n'
    if len(A) % 2 == 0 and A[-1] != bodo.none:
        if bodo.utils.utils.is_array_typ(A[-1]):
            khkam__zmm += (
                f'   if bodo.libs.array_kernels.isna({kji__rkuau[-1]}, i):\n')
            khkam__zmm += '      bodo.libs.array_kernels.setna(res, i)\n'
            khkam__zmm += '   else:\n'
        khkam__zmm += f'      res[i] = arg{len(A) - 1}'
    else:
        khkam__zmm += '   bodo.libs.array_kernels.setna(res, i)'
    mqx__ixx = 'A'
    jxt__wmfi = {f'A{lsdut__iqky}': f'A[{lsdut__iqky}]' for lsdut__iqky in
        range(len(A))}
    if len(vhnq__zkzn) % 2 == 0:
        wfzht__rnhfa = [vhnq__zkzn[0]] + vhnq__zkzn[1:-1:2]
        oqi__nrk = vhnq__zkzn[2::2] + [vhnq__zkzn[-1]]
    else:
        wfzht__rnhfa = [vhnq__zkzn[0]] + vhnq__zkzn[1::2]
        oqi__nrk = vhnq__zkzn[2::2]
    sgbn__vjq = get_common_broadcasted_type(wfzht__rnhfa, 'DECODE')
    lxo__bprev = get_common_broadcasted_type(oqi__nrk, 'DECODE')
    if lxo__bprev == bodo.none:
        lxo__bprev = sgbn__vjq
    bslz__umkjw = bodo.utils.utils.is_array_typ(A[0]
        ) and bodo.none not in wfzht__rnhfa and len(vhnq__zkzn) % 2 == 1
    return gen_vectorized(kji__rkuau, vhnq__zkzn, ieuoi__npi, khkam__zmm,
        lxo__bprev, mqx__ixx, jxt__wmfi, support_dict_encoding=bslz__umkjw)


def concat_ws(A, sep):
    return


@overload(concat_ws)
def overload_concat_ws(A, sep):
    if not isinstance(A, (types.Tuple, types.UniTuple)):
        raise_bodo_error('concat_ws argument must be a tuple')
    for lsdut__iqky in range(len(A)):
        if isinstance(A[lsdut__iqky], types.optional):
            return unopt_argument('bodo.libs.bodosql_array_kernels.concat_ws',
                ['A', 'sep'], 0, container_arg=lsdut__iqky,
                container_length=len(A))
    if isinstance(sep, types.optional):
        return unopt_argument('bodo.libs.bodosql_array_kernels.concat_ws',
            ['A', 'sep'], 1)

    def impl(A, sep):
        return concat_ws_util(A, sep)
    return impl


def concat_ws_util(A, sep):
    return


@overload(concat_ws_util, no_unliteral=True)
def overload_concat_ws_util(A, sep):
    if len(A) == 0:
        raise_bodo_error('Cannot concatenate 0 columns')
    kji__rkuau = []
    vhnq__zkzn = []
    for lsdut__iqky, ipj__etq in enumerate(A):
        bkdqf__ngvsn = f'A{lsdut__iqky}'
        verify_string_arg(ipj__etq, 'CONCAT_WS', bkdqf__ngvsn)
        kji__rkuau.append(bkdqf__ngvsn)
        vhnq__zkzn.append(ipj__etq)
    kji__rkuau.append('sep')
    verify_string_arg(sep, 'CONCAT_WS', 'sep')
    vhnq__zkzn.append(sep)
    ieuoi__npi = [True] * len(kji__rkuau)
    lxo__bprev = bodo.string_array_type
    mqx__ixx = 'A, sep'
    jxt__wmfi = {f'A{lsdut__iqky}': f'A[{lsdut__iqky}]' for lsdut__iqky in
        range(len(A))}
    oill__eyiec = ','.join([f'arg{lsdut__iqky}' for lsdut__iqky in range(
        len(A))])
    khkam__zmm = f'  res[i] = arg{len(A)}.join([{oill__eyiec}])\n'
    return gen_vectorized(kji__rkuau, vhnq__zkzn, ieuoi__npi, khkam__zmm,
        lxo__bprev, mqx__ixx, jxt__wmfi)
