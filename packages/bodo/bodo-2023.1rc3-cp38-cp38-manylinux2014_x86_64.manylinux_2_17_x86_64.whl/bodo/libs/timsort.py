import numba
import numpy as np
import pandas as pd
from numba.extending import overload
from bodo.utils.utils import alloc_arr_tup
MIN_MERGE = 32


@numba.njit(no_cpython_wrapper=True, cache=True)
def sort(key_arrs, lo, hi, data):
    wdde__isnk = hi - lo
    if wdde__isnk < 2:
        return
    if wdde__isnk < MIN_MERGE:
        pcyph__xfbwc = countRunAndMakeAscending(key_arrs, lo, hi, data)
        binarySort(key_arrs, lo, hi, lo + pcyph__xfbwc, data)
        return
    stackSize, runBase, runLen, tmpLength, tmp, tmp_data, minGallop = (
        init_sort_start(key_arrs, data))
    yina__hxpfz = minRunLength(wdde__isnk)
    while True:
        ljq__ydz = countRunAndMakeAscending(key_arrs, lo, hi, data)
        if ljq__ydz < yina__hxpfz:
            stuyy__xnez = (wdde__isnk if wdde__isnk <= yina__hxpfz else
                yina__hxpfz)
            binarySort(key_arrs, lo, lo + stuyy__xnez, lo + ljq__ydz, data)
            ljq__ydz = stuyy__xnez
        stackSize = pushRun(stackSize, runBase, runLen, lo, ljq__ydz)
        stackSize, tmpLength, tmp, tmp_data, minGallop = mergeCollapse(
            stackSize, runBase, runLen, key_arrs, data, tmpLength, tmp,
            tmp_data, minGallop)
        lo += ljq__ydz
        wdde__isnk -= ljq__ydz
        if wdde__isnk == 0:
            break
    assert lo == hi
    stackSize, tmpLength, tmp, tmp_data, minGallop = mergeForceCollapse(
        stackSize, runBase, runLen, key_arrs, data, tmpLength, tmp,
        tmp_data, minGallop)
    assert stackSize == 1


@numba.njit(no_cpython_wrapper=True, cache=True)
def binarySort(key_arrs, lo, hi, start, data):
    assert lo <= start and start <= hi
    if start == lo:
        start += 1
    while start < hi:
        gaikg__bigy = getitem_arr_tup(key_arrs, start)
        dfg__boy = getitem_arr_tup(data, start)
        cavw__iiga = lo
        exc__ags = start
        assert cavw__iiga <= exc__ags
        while cavw__iiga < exc__ags:
            blbsk__pirh = cavw__iiga + exc__ags >> 1
            if gaikg__bigy < getitem_arr_tup(key_arrs, blbsk__pirh):
                exc__ags = blbsk__pirh
            else:
                cavw__iiga = blbsk__pirh + 1
        assert cavw__iiga == exc__ags
        n = start - cavw__iiga
        copyRange_tup(key_arrs, cavw__iiga, key_arrs, cavw__iiga + 1, n)
        copyRange_tup(data, cavw__iiga, data, cavw__iiga + 1, n)
        setitem_arr_tup(key_arrs, cavw__iiga, gaikg__bigy)
        setitem_arr_tup(data, cavw__iiga, dfg__boy)
        start += 1


@numba.njit(no_cpython_wrapper=True, cache=True)
def countRunAndMakeAscending(key_arrs, lo, hi, data):
    assert lo < hi
    nip__xsfnc = lo + 1
    if nip__xsfnc == hi:
        return 1
    if getitem_arr_tup(key_arrs, nip__xsfnc) < getitem_arr_tup(key_arrs, lo):
        nip__xsfnc += 1
        while nip__xsfnc < hi and getitem_arr_tup(key_arrs, nip__xsfnc
            ) < getitem_arr_tup(key_arrs, nip__xsfnc - 1):
            nip__xsfnc += 1
        reverseRange(key_arrs, lo, nip__xsfnc, data)
    else:
        nip__xsfnc += 1
        while nip__xsfnc < hi and getitem_arr_tup(key_arrs, nip__xsfnc
            ) >= getitem_arr_tup(key_arrs, nip__xsfnc - 1):
            nip__xsfnc += 1
    return nip__xsfnc - lo


@numba.njit(no_cpython_wrapper=True, cache=True)
def reverseRange(key_arrs, lo, hi, data):
    hi -= 1
    while lo < hi:
        swap_arrs(key_arrs, lo, hi)
        swap_arrs(data, lo, hi)
        lo += 1
        hi -= 1


@numba.njit(no_cpython_wrapper=True, cache=True)
def minRunLength(n):
    assert n >= 0
    njqk__hfzi = 0
    while n >= MIN_MERGE:
        njqk__hfzi |= n & 1
        n >>= 1
    return n + njqk__hfzi


MIN_GALLOP = 7
INITIAL_TMP_STORAGE_LENGTH = 256


@numba.njit(no_cpython_wrapper=True, cache=True)
def init_sort_start(key_arrs, data):
    minGallop = MIN_GALLOP
    wokgk__sxp = len(key_arrs[0])
    tmpLength = (wokgk__sxp >> 1 if wokgk__sxp < 2 *
        INITIAL_TMP_STORAGE_LENGTH else INITIAL_TMP_STORAGE_LENGTH)
    tmp = alloc_arr_tup(tmpLength, key_arrs)
    tmp_data = alloc_arr_tup(tmpLength, data)
    stackSize = 0
    abfi__bjqvq = (5 if wokgk__sxp < 120 else 10 if wokgk__sxp < 1542 else 
        19 if wokgk__sxp < 119151 else 40)
    runBase = np.empty(abfi__bjqvq, np.int64)
    runLen = np.empty(abfi__bjqvq, np.int64)
    return stackSize, runBase, runLen, tmpLength, tmp, tmp_data, minGallop


@numba.njit(no_cpython_wrapper=True, cache=True)
def pushRun(stackSize, runBase, runLen, runBase_val, runLen_val):
    runBase[stackSize] = runBase_val
    runLen[stackSize] = runLen_val
    stackSize += 1
    return stackSize


@numba.njit(no_cpython_wrapper=True, cache=True)
def mergeCollapse(stackSize, runBase, runLen, key_arrs, data, tmpLength,
    tmp, tmp_data, minGallop):
    while stackSize > 1:
        n = stackSize - 2
        if n >= 1 and runLen[n - 1] <= runLen[n] + runLen[n + 1
            ] or n >= 2 and runLen[n - 2] <= runLen[n] + runLen[n - 1]:
            if runLen[n - 1] < runLen[n + 1]:
                n -= 1
        elif runLen[n] > runLen[n + 1]:
            break
        stackSize, tmpLength, tmp, tmp_data, minGallop = mergeAt(stackSize,
            runBase, runLen, key_arrs, data, tmpLength, tmp, tmp_data,
            minGallop, n)
    return stackSize, tmpLength, tmp, tmp_data, minGallop


@numba.njit(no_cpython_wrapper=True, cache=True)
def mergeForceCollapse(stackSize, runBase, runLen, key_arrs, data,
    tmpLength, tmp, tmp_data, minGallop):
    while stackSize > 1:
        n = stackSize - 2
        if n > 0 and runLen[n - 1] < runLen[n + 1]:
            n -= 1
        stackSize, tmpLength, tmp, tmp_data, minGallop = mergeAt(stackSize,
            runBase, runLen, key_arrs, data, tmpLength, tmp, tmp_data,
            minGallop, n)
    return stackSize, tmpLength, tmp, tmp_data, minGallop


@numba.njit(no_cpython_wrapper=True, cache=True)
def mergeAt(stackSize, runBase, runLen, key_arrs, data, tmpLength, tmp,
    tmp_data, minGallop, i):
    assert stackSize >= 2
    assert i >= 0
    assert i == stackSize - 2 or i == stackSize - 3
    base1 = runBase[i]
    len1 = runLen[i]
    base2 = runBase[i + 1]
    len2 = runLen[i + 1]
    assert len1 > 0 and len2 > 0
    assert base1 + len1 == base2
    runLen[i] = len1 + len2
    if i == stackSize - 3:
        runBase[i + 1] = runBase[i + 2]
        runLen[i + 1] = runLen[i + 2]
    stackSize -= 1
    ysill__cke = gallopRight(getitem_arr_tup(key_arrs, base2), key_arrs,
        base1, len1, 0)
    assert ysill__cke >= 0
    base1 += ysill__cke
    len1 -= ysill__cke
    if len1 == 0:
        return stackSize, tmpLength, tmp, tmp_data, minGallop
    len2 = gallopLeft(getitem_arr_tup(key_arrs, base1 + len1 - 1), key_arrs,
        base2, len2, len2 - 1)
    assert len2 >= 0
    if len2 == 0:
        return stackSize, tmpLength, tmp, tmp_data, minGallop
    if len1 <= len2:
        tmpLength, tmp, tmp_data = ensureCapacity(tmpLength, tmp, tmp_data,
            key_arrs, data, len1)
        minGallop = mergeLo(key_arrs, data, tmp, tmp_data, minGallop, base1,
            len1, base2, len2)
    else:
        tmpLength, tmp, tmp_data = ensureCapacity(tmpLength, tmp, tmp_data,
            key_arrs, data, len2)
        minGallop = mergeHi(key_arrs, data, tmp, tmp_data, minGallop, base1,
            len1, base2, len2)
    return stackSize, tmpLength, tmp, tmp_data, minGallop


@numba.njit(no_cpython_wrapper=True, cache=True)
def gallopLeft(key, arr, base, _len, hint):
    assert _len > 0 and hint >= 0 and hint < _len
    jij__reeiy = 0
    alt__gjh = 1
    if key > getitem_arr_tup(arr, base + hint):
        iklo__dadv = _len - hint
        while alt__gjh < iklo__dadv and key > getitem_arr_tup(arr, base +
            hint + alt__gjh):
            jij__reeiy = alt__gjh
            alt__gjh = (alt__gjh << 1) + 1
            if alt__gjh <= 0:
                alt__gjh = iklo__dadv
        if alt__gjh > iklo__dadv:
            alt__gjh = iklo__dadv
        jij__reeiy += hint
        alt__gjh += hint
    else:
        iklo__dadv = hint + 1
        while alt__gjh < iklo__dadv and key <= getitem_arr_tup(arr, base +
            hint - alt__gjh):
            jij__reeiy = alt__gjh
            alt__gjh = (alt__gjh << 1) + 1
            if alt__gjh <= 0:
                alt__gjh = iklo__dadv
        if alt__gjh > iklo__dadv:
            alt__gjh = iklo__dadv
        tmp = jij__reeiy
        jij__reeiy = hint - alt__gjh
        alt__gjh = hint - tmp
    assert -1 <= jij__reeiy and jij__reeiy < alt__gjh and alt__gjh <= _len
    jij__reeiy += 1
    while jij__reeiy < alt__gjh:
        xjc__bkx = jij__reeiy + (alt__gjh - jij__reeiy >> 1)
        if key > getitem_arr_tup(arr, base + xjc__bkx):
            jij__reeiy = xjc__bkx + 1
        else:
            alt__gjh = xjc__bkx
    assert jij__reeiy == alt__gjh
    return alt__gjh


@numba.njit(no_cpython_wrapper=True, cache=True)
def gallopRight(key, arr, base, _len, hint):
    assert _len > 0 and hint >= 0 and hint < _len
    alt__gjh = 1
    jij__reeiy = 0
    if key < getitem_arr_tup(arr, base + hint):
        iklo__dadv = hint + 1
        while alt__gjh < iklo__dadv and key < getitem_arr_tup(arr, base +
            hint - alt__gjh):
            jij__reeiy = alt__gjh
            alt__gjh = (alt__gjh << 1) + 1
            if alt__gjh <= 0:
                alt__gjh = iklo__dadv
        if alt__gjh > iklo__dadv:
            alt__gjh = iklo__dadv
        tmp = jij__reeiy
        jij__reeiy = hint - alt__gjh
        alt__gjh = hint - tmp
    else:
        iklo__dadv = _len - hint
        while alt__gjh < iklo__dadv and key >= getitem_arr_tup(arr, base +
            hint + alt__gjh):
            jij__reeiy = alt__gjh
            alt__gjh = (alt__gjh << 1) + 1
            if alt__gjh <= 0:
                alt__gjh = iklo__dadv
        if alt__gjh > iklo__dadv:
            alt__gjh = iklo__dadv
        jij__reeiy += hint
        alt__gjh += hint
    assert -1 <= jij__reeiy and jij__reeiy < alt__gjh and alt__gjh <= _len
    jij__reeiy += 1
    while jij__reeiy < alt__gjh:
        xjc__bkx = jij__reeiy + (alt__gjh - jij__reeiy >> 1)
        if key < getitem_arr_tup(arr, base + xjc__bkx):
            alt__gjh = xjc__bkx
        else:
            jij__reeiy = xjc__bkx + 1
    assert jij__reeiy == alt__gjh
    return alt__gjh


@numba.njit(no_cpython_wrapper=True, cache=True)
def mergeLo(key_arrs, data, tmp, tmp_data, minGallop, base1, len1, base2, len2
    ):
    assert len1 > 0 and len2 > 0 and base1 + len1 == base2
    arr = key_arrs
    arr_data = data
    copyRange_tup(arr, base1, tmp, 0, len1)
    copyRange_tup(arr_data, base1, tmp_data, 0, len1)
    cursor1 = 0
    cursor2 = base2
    dest = base1
    setitem_arr_tup(arr, dest, getitem_arr_tup(arr, cursor2))
    copyElement_tup(arr_data, cursor2, arr_data, dest)
    cursor2 += 1
    dest += 1
    len2 -= 1
    if len2 == 0:
        copyRange_tup(tmp, cursor1, arr, dest, len1)
        copyRange_tup(tmp_data, cursor1, arr_data, dest, len1)
        return minGallop
    if len1 == 1:
        copyRange_tup(arr, cursor2, arr, dest, len2)
        copyRange_tup(arr_data, cursor2, arr_data, dest, len2)
        copyElement_tup(tmp, cursor1, arr, dest + len2)
        copyElement_tup(tmp_data, cursor1, arr_data, dest + len2)
        return minGallop
    len1, len2, cursor1, cursor2, dest, minGallop = mergeLo_inner(key_arrs,
        data, tmp_data, len1, len2, tmp, cursor1, cursor2, dest, minGallop)
    minGallop = 1 if minGallop < 1 else minGallop
    if len1 == 1:
        assert len2 > 0
        copyRange_tup(arr, cursor2, arr, dest, len2)
        copyRange_tup(arr_data, cursor2, arr_data, dest, len2)
        copyElement_tup(tmp, cursor1, arr, dest + len2)
        copyElement_tup(tmp_data, cursor1, arr_data, dest + len2)
    elif len1 == 0:
        raise ValueError('Comparison method violates its general contract!')
    else:
        assert len2 == 0
        assert len1 > 1
        copyRange_tup(tmp, cursor1, arr, dest, len1)
        copyRange_tup(tmp_data, cursor1, arr_data, dest, len1)
    return minGallop


@numba.njit(no_cpython_wrapper=True, cache=True)
def mergeLo_inner(arr, arr_data, tmp_data, len1, len2, tmp, cursor1,
    cursor2, dest, minGallop):
    while True:
        lhc__fmsdd = 0
        tekps__tylms = 0
        while True:
            assert len1 > 1 and len2 > 0
            if getitem_arr_tup(arr, cursor2) < getitem_arr_tup(tmp, cursor1):
                copyElement_tup(arr, cursor2, arr, dest)
                copyElement_tup(arr_data, cursor2, arr_data, dest)
                cursor2 += 1
                dest += 1
                tekps__tylms += 1
                lhc__fmsdd = 0
                len2 -= 1
                if len2 == 0:
                    return len1, len2, cursor1, cursor2, dest, minGallop
            else:
                copyElement_tup(tmp, cursor1, arr, dest)
                copyElement_tup(tmp_data, cursor1, arr_data, dest)
                cursor1 += 1
                dest += 1
                lhc__fmsdd += 1
                tekps__tylms = 0
                len1 -= 1
                if len1 == 1:
                    return len1, len2, cursor1, cursor2, dest, minGallop
            if not lhc__fmsdd | tekps__tylms < minGallop:
                break
        while True:
            assert len1 > 1 and len2 > 0
            lhc__fmsdd = gallopRight(getitem_arr_tup(arr, cursor2), tmp,
                cursor1, len1, 0)
            if lhc__fmsdd != 0:
                copyRange_tup(tmp, cursor1, arr, dest, lhc__fmsdd)
                copyRange_tup(tmp_data, cursor1, arr_data, dest, lhc__fmsdd)
                dest += lhc__fmsdd
                cursor1 += lhc__fmsdd
                len1 -= lhc__fmsdd
                if len1 <= 1:
                    return len1, len2, cursor1, cursor2, dest, minGallop
            copyElement_tup(arr, cursor2, arr, dest)
            copyElement_tup(arr_data, cursor2, arr_data, dest)
            cursor2 += 1
            dest += 1
            len2 -= 1
            if len2 == 0:
                return len1, len2, cursor1, cursor2, dest, minGallop
            tekps__tylms = gallopLeft(getitem_arr_tup(tmp, cursor1), arr,
                cursor2, len2, 0)
            if tekps__tylms != 0:
                copyRange_tup(arr, cursor2, arr, dest, tekps__tylms)
                copyRange_tup(arr_data, cursor2, arr_data, dest, tekps__tylms)
                dest += tekps__tylms
                cursor2 += tekps__tylms
                len2 -= tekps__tylms
                if len2 == 0:
                    return len1, len2, cursor1, cursor2, dest, minGallop
            copyElement_tup(tmp, cursor1, arr, dest)
            copyElement_tup(tmp_data, cursor1, arr_data, dest)
            cursor1 += 1
            dest += 1
            len1 -= 1
            if len1 == 1:
                return len1, len2, cursor1, cursor2, dest, minGallop
            minGallop -= 1
            if not lhc__fmsdd >= MIN_GALLOP | tekps__tylms >= MIN_GALLOP:
                break
        if minGallop < 0:
            minGallop = 0
        minGallop += 2
    return len1, len2, cursor1, cursor2, dest, minGallop


@numba.njit(no_cpython_wrapper=True, cache=True)
def mergeHi(key_arrs, data, tmp, tmp_data, minGallop, base1, len1, base2, len2
    ):
    assert len1 > 0 and len2 > 0 and base1 + len1 == base2
    arr = key_arrs
    arr_data = data
    copyRange_tup(arr, base2, tmp, 0, len2)
    copyRange_tup(arr_data, base2, tmp_data, 0, len2)
    cursor1 = base1 + len1 - 1
    cursor2 = len2 - 1
    dest = base2 + len2 - 1
    copyElement_tup(arr, cursor1, arr, dest)
    copyElement_tup(arr_data, cursor1, arr_data, dest)
    cursor1 -= 1
    dest -= 1
    len1 -= 1
    if len1 == 0:
        copyRange_tup(tmp, 0, arr, dest - (len2 - 1), len2)
        copyRange_tup(tmp_data, 0, arr_data, dest - (len2 - 1), len2)
        return minGallop
    if len2 == 1:
        dest -= len1
        cursor1 -= len1
        copyRange_tup(arr, cursor1 + 1, arr, dest + 1, len1)
        copyRange_tup(arr_data, cursor1 + 1, arr_data, dest + 1, len1)
        copyElement_tup(tmp, cursor2, arr, dest)
        copyElement_tup(tmp_data, cursor2, arr_data, dest)
        return minGallop
    len1, len2, tmp, cursor1, cursor2, dest, minGallop = mergeHi_inner(key_arrs
        , data, tmp_data, base1, len1, len2, tmp, cursor1, cursor2, dest,
        minGallop)
    minGallop = 1 if minGallop < 1 else minGallop
    if len2 == 1:
        assert len1 > 0
        dest -= len1
        cursor1 -= len1
        copyRange_tup(arr, cursor1 + 1, arr, dest + 1, len1)
        copyRange_tup(arr_data, cursor1 + 1, arr_data, dest + 1, len1)
        copyElement_tup(tmp, cursor2, arr, dest)
        copyElement_tup(tmp_data, cursor2, arr_data, dest)
    elif len2 == 0:
        raise ValueError('Comparison method violates its general contract!')
    else:
        assert len1 == 0
        assert len2 > 0
        copyRange_tup(tmp, 0, arr, dest - (len2 - 1), len2)
        copyRange_tup(tmp_data, 0, arr_data, dest - (len2 - 1), len2)
    return minGallop


@numba.njit(no_cpython_wrapper=True, cache=True)
def mergeHi_inner(arr, arr_data, tmp_data, base1, len1, len2, tmp, cursor1,
    cursor2, dest, minGallop):
    while True:
        lhc__fmsdd = 0
        tekps__tylms = 0
        while True:
            assert len1 > 0 and len2 > 1
            if getitem_arr_tup(tmp, cursor2) < getitem_arr_tup(arr, cursor1):
                copyElement_tup(arr, cursor1, arr, dest)
                copyElement_tup(arr_data, cursor1, arr_data, dest)
                cursor1 -= 1
                dest -= 1
                lhc__fmsdd += 1
                tekps__tylms = 0
                len1 -= 1
                if len1 == 0:
                    return len1, len2, tmp, cursor1, cursor2, dest, minGallop
            else:
                copyElement_tup(tmp, cursor2, arr, dest)
                copyElement_tup(tmp_data, cursor2, arr_data, dest)
                cursor2 -= 1
                dest -= 1
                tekps__tylms += 1
                lhc__fmsdd = 0
                len2 -= 1
                if len2 == 1:
                    return len1, len2, tmp, cursor1, cursor2, dest, minGallop
            if not lhc__fmsdd | tekps__tylms < minGallop:
                break
        while True:
            assert len1 > 0 and len2 > 1
            lhc__fmsdd = len1 - gallopRight(getitem_arr_tup(tmp, cursor2),
                arr, base1, len1, len1 - 1)
            if lhc__fmsdd != 0:
                dest -= lhc__fmsdd
                cursor1 -= lhc__fmsdd
                len1 -= lhc__fmsdd
                copyRange_tup(arr, cursor1 + 1, arr, dest + 1, lhc__fmsdd)
                copyRange_tup(arr_data, cursor1 + 1, arr_data, dest + 1,
                    lhc__fmsdd)
                if len1 == 0:
                    return len1, len2, tmp, cursor1, cursor2, dest, minGallop
            copyElement_tup(tmp, cursor2, arr, dest)
            copyElement_tup(tmp_data, cursor2, arr_data, dest)
            cursor2 -= 1
            dest -= 1
            len2 -= 1
            if len2 == 1:
                return len1, len2, tmp, cursor1, cursor2, dest, minGallop
            tekps__tylms = len2 - gallopLeft(getitem_arr_tup(arr, cursor1),
                tmp, 0, len2, len2 - 1)
            if tekps__tylms != 0:
                dest -= tekps__tylms
                cursor2 -= tekps__tylms
                len2 -= tekps__tylms
                copyRange_tup(tmp, cursor2 + 1, arr, dest + 1, tekps__tylms)
                copyRange_tup(tmp_data, cursor2 + 1, arr_data, dest + 1,
                    tekps__tylms)
                if len2 <= 1:
                    return len1, len2, tmp, cursor1, cursor2, dest, minGallop
            copyElement_tup(arr, cursor1, arr, dest)
            copyElement_tup(arr_data, cursor1, arr_data, dest)
            cursor1 -= 1
            dest -= 1
            len1 -= 1
            if len1 == 0:
                return len1, len2, tmp, cursor1, cursor2, dest, minGallop
            minGallop -= 1
            if not lhc__fmsdd >= MIN_GALLOP | tekps__tylms >= MIN_GALLOP:
                break
        if minGallop < 0:
            minGallop = 0
        minGallop += 2
    return len1, len2, tmp, cursor1, cursor2, dest, minGallop


@numba.njit(no_cpython_wrapper=True, cache=True)
def ensureCapacity(tmpLength, tmp, tmp_data, key_arrs, data, minCapacity):
    iyfa__cfgbb = len(key_arrs[0])
    if tmpLength < minCapacity:
        gebkt__brpk = minCapacity
        gebkt__brpk |= gebkt__brpk >> 1
        gebkt__brpk |= gebkt__brpk >> 2
        gebkt__brpk |= gebkt__brpk >> 4
        gebkt__brpk |= gebkt__brpk >> 8
        gebkt__brpk |= gebkt__brpk >> 16
        gebkt__brpk += 1
        if gebkt__brpk < 0:
            gebkt__brpk = minCapacity
        else:
            gebkt__brpk = min(gebkt__brpk, iyfa__cfgbb >> 1)
        tmp = alloc_arr_tup(gebkt__brpk, key_arrs)
        tmp_data = alloc_arr_tup(gebkt__brpk, data)
        tmpLength = gebkt__brpk
    return tmpLength, tmp, tmp_data


def swap_arrs(data, lo, hi):
    for arr in data:
        qcdwh__ukf = arr[lo]
        arr[lo] = arr[hi]
        arr[hi] = qcdwh__ukf


@overload(swap_arrs, no_unliteral=True)
def swap_arrs_overload(arr_tup, lo, hi):
    aylem__whav = arr_tup.count
    qki__qsxj = 'def f(arr_tup, lo, hi):\n'
    for i in range(aylem__whav):
        qki__qsxj += '  tmp_v_{} = arr_tup[{}][lo]\n'.format(i, i)
        qki__qsxj += '  arr_tup[{}][lo] = arr_tup[{}][hi]\n'.format(i, i)
        qki__qsxj += '  arr_tup[{}][hi] = tmp_v_{}\n'.format(i, i)
    qki__qsxj += '  return\n'
    virtg__ztd = {}
    exec(qki__qsxj, {}, virtg__ztd)
    ynkmp__uuvr = virtg__ztd['f']
    return ynkmp__uuvr


@numba.njit(no_cpython_wrapper=True, cache=True)
def copyRange(src_arr, src_pos, dst_arr, dst_pos, n):
    dst_arr[dst_pos:dst_pos + n] = src_arr[src_pos:src_pos + n]


def copyRange_tup(src_arr_tup, src_pos, dst_arr_tup, dst_pos, n):
    for src_arr, dst_arr in zip(src_arr_tup, dst_arr_tup):
        dst_arr[dst_pos:dst_pos + n] = src_arr[src_pos:src_pos + n]


@overload(copyRange_tup, no_unliteral=True)
def copyRange_tup_overload(src_arr_tup, src_pos, dst_arr_tup, dst_pos, n):
    aylem__whav = src_arr_tup.count
    assert aylem__whav == dst_arr_tup.count
    qki__qsxj = 'def f(src_arr_tup, src_pos, dst_arr_tup, dst_pos, n):\n'
    for i in range(aylem__whav):
        qki__qsxj += (
            '  copyRange(src_arr_tup[{}], src_pos, dst_arr_tup[{}], dst_pos, n)\n'
            .format(i, i))
    qki__qsxj += '  return\n'
    virtg__ztd = {}
    exec(qki__qsxj, {'copyRange': copyRange}, virtg__ztd)
    wsb__sbb = virtg__ztd['f']
    return wsb__sbb


@numba.njit(no_cpython_wrapper=True, cache=True)
def copyElement(src_arr, src_pos, dst_arr, dst_pos):
    dst_arr[dst_pos] = src_arr[src_pos]


def copyElement_tup(src_arr_tup, src_pos, dst_arr_tup, dst_pos):
    for src_arr, dst_arr in zip(src_arr_tup, dst_arr_tup):
        dst_arr[dst_pos] = src_arr[src_pos]


@overload(copyElement_tup, no_unliteral=True)
def copyElement_tup_overload(src_arr_tup, src_pos, dst_arr_tup, dst_pos):
    aylem__whav = src_arr_tup.count
    assert aylem__whav == dst_arr_tup.count
    qki__qsxj = 'def f(src_arr_tup, src_pos, dst_arr_tup, dst_pos):\n'
    for i in range(aylem__whav):
        qki__qsxj += (
            '  copyElement(src_arr_tup[{}], src_pos, dst_arr_tup[{}], dst_pos)\n'
            .format(i, i))
    qki__qsxj += '  return\n'
    virtg__ztd = {}
    exec(qki__qsxj, {'copyElement': copyElement}, virtg__ztd)
    wsb__sbb = virtg__ztd['f']
    return wsb__sbb


def getitem_arr_tup(arr_tup, ind):
    jcz__cfun = [arr[ind] for arr in arr_tup]
    return tuple(jcz__cfun)


@overload(getitem_arr_tup, no_unliteral=True)
def getitem_arr_tup_overload(arr_tup, ind):
    aylem__whav = arr_tup.count
    qki__qsxj = 'def f(arr_tup, ind):\n'
    qki__qsxj += '  return ({}{})\n'.format(','.join(['arr_tup[{}][ind]'.
        format(i) for i in range(aylem__whav)]), ',' if aylem__whav == 1 else
        '')
    virtg__ztd = {}
    exec(qki__qsxj, {}, virtg__ztd)
    pbmy__jvxc = virtg__ztd['f']
    return pbmy__jvxc


def setitem_arr_tup(arr_tup, ind, val_tup):
    for arr, kzym__rzway in zip(arr_tup, val_tup):
        arr[ind] = kzym__rzway


@overload(setitem_arr_tup, no_unliteral=True)
def setitem_arr_tup_overload(arr_tup, ind, val_tup):
    aylem__whav = arr_tup.count
    qki__qsxj = 'def f(arr_tup, ind, val_tup):\n'
    for i in range(aylem__whav):
        if isinstance(val_tup, numba.core.types.BaseTuple):
            qki__qsxj += '  arr_tup[{}][ind] = val_tup[{}]\n'.format(i, i)
        else:
            assert arr_tup.count == 1
            qki__qsxj += '  arr_tup[{}][ind] = val_tup\n'.format(i)
    qki__qsxj += '  return\n'
    virtg__ztd = {}
    exec(qki__qsxj, {}, virtg__ztd)
    pbmy__jvxc = virtg__ztd['f']
    return pbmy__jvxc


def test():
    import time
    ojydi__fyt = time.time()
    bns__amobs = np.ones(3)
    data = np.arange(3), np.ones(3)
    sort((bns__amobs,), 0, 3, data)
    print('compile time', time.time() - ojydi__fyt)
    n = 210000
    np.random.seed(2)
    data = np.arange(n), np.random.ranf(n)
    ass__zihd = np.random.ranf(n)
    ysq__pzdk = pd.DataFrame({'A': ass__zihd, 'B': data[0], 'C': data[1]})
    ojydi__fyt = time.time()
    hclks__nqjkk = ysq__pzdk.sort_values('A', inplace=False)
    zrvq__fnele = time.time()
    sort((ass__zihd,), 0, n, data)
    print('Bodo', time.time() - zrvq__fnele, 'Numpy', zrvq__fnele - ojydi__fyt)
    np.testing.assert_almost_equal(data[0], hclks__nqjkk.B.values)
    np.testing.assert_almost_equal(data[1], hclks__nqjkk.C.values)


if __name__ == '__main__':
    test()
