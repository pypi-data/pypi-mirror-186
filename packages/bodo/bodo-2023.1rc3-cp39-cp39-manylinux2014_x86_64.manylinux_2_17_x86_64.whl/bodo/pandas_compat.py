import hashlib
import inspect
import warnings
import numpy as np
import pandas as pd
from pandas._libs import lib
pandas_version = tuple(map(int, pd.__version__.split('.')[:2]))
_check_pandas_change = False
if pandas_version < (1, 4):

    def _set_noconvert_columns(self):
        assert self.orig_names is not None
        xizat__fqvy = {cdojt__mkpt: xgpfk__ddpx for xgpfk__ddpx,
            cdojt__mkpt in enumerate(self.orig_names)}
        aijjn__qbx = [xizat__fqvy[cdojt__mkpt] for cdojt__mkpt in self.names]
        lrjyd__hdbt = self._set_noconvert_dtype_columns(aijjn__qbx, self.names)
        for bzei__yxx in lrjyd__hdbt:
            self._reader.set_noconvert(bzei__yxx)
    if _check_pandas_change:
        lines = inspect.getsource(pd.io.parsers.c_parser_wrapper.
            CParserWrapper._set_noconvert_columns)
        if (hashlib.sha256(lines.encode()).hexdigest() !=
            'afc2d738f194e3976cf05d61cb16dc4224b0139451f08a1cf49c578af6f975d3'
            ):
            warnings.warn(
                'pd.io.parsers.c_parser_wrapper.CParserWrapper._set_noconvert_columns has changed'
                )
    (pd.io.parsers.c_parser_wrapper.CParserWrapper._set_noconvert_columns
        ) = _set_noconvert_columns


def ArrowStringArray__init__(self, values):
    import pyarrow as pa
    from pandas.core.arrays.string_ import StringDtype
    self._dtype = StringDtype(storage='pyarrow')
    if isinstance(values, pa.Array):
        self._data = pa.chunked_array([values])
    elif isinstance(values, pa.ChunkedArray):
        self._data = values
    else:
        raise ValueError(
            f"Unsupported type '{type(values)}' for ArrowStringArray")
    if not (pa.types.is_string(self._data.type) or pa.types.is_large_string
        (self._data.type) or pa.types.is_dictionary(self._data.type) and (
        pa.types.is_string(self._data.type.value_type) or pa.types.
        is_large_string(self._data.type.value_type)) and pa.types.is_int32(
        self._data.type.index_type)):
        raise ValueError(
            'ArrowStringArray requires a PyArrow (chunked) array of string type'
            )


if _check_pandas_change:
    lines = inspect.getsource(pd.core.arrays.string_arrow.ArrowStringArray.
        __init__)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'cbb9683b2e91867ef12470d4fda28ca6243fbb7b4f78ac2472fca805607c0942':
        warnings.warn(
            'pd.core.arrays.string_arrow.ArrowStringArray.__init__ has changed'
            )
pd.core.arrays.string_arrow.ArrowStringArray.__init__ = (
    ArrowStringArray__init__)


def factorize(self, na_sentinel: int=-1):
    import numpy as np
    import pyarrow as pa
    jauzx__pnxaq = self._data if pa.types.is_dictionary(self._data.type
        ) else self._data.dictionary_encode()
    jqo__xqw = pa.chunked_array([hiii__wibv.indices for hiii__wibv in
        jauzx__pnxaq.chunks], type=jauzx__pnxaq.type.index_type).to_pandas()
    if jqo__xqw.dtype.kind == 'f':
        jqo__xqw[np.isnan(jqo__xqw)] = na_sentinel
    jqo__xqw = jqo__xqw.astype(np.int64, copy=False)
    if jauzx__pnxaq.num_chunks:
        ovsi__mjmhj = type(self)(jauzx__pnxaq.chunk(0).dictionary)
    else:
        ovsi__mjmhj = type(self)(pa.array([], type=jauzx__pnxaq.type.
            value_type))
    return jqo__xqw.values, ovsi__mjmhj


if _check_pandas_change:
    lines = inspect.getsource(pd.core.arrays.string_arrow.ArrowStringArray.
        factorize)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '80669a609cfe11b362dacec6bba8e5bf41418b35d0d8b58246a548858320efd9':
        warnings.warn(
            'pd.core.arrays.string_arrow.ArrowStringArray.factorize has changed'
            )
pd.core.arrays.string_arrow.ArrowStringArray.factorize = factorize


def to_numpy(self, dtype=None, copy: bool=False, na_value=lib.no_default
    ) ->np.ndarray:
    wany__dplxy = self._data.combine_chunks() if len(self) != 0 else self._data
    svqft__kvpk = np.array(wany__dplxy, dtype=dtype)
    if self._data.null_count > 0:
        if na_value is lib.no_default:
            if dtype and np.issubdtype(dtype, np.floating):
                return svqft__kvpk
            na_value = self._dtype.na_value
        xfwe__euz = self.isna()
        svqft__kvpk[xfwe__euz] = na_value
    return svqft__kvpk


if _check_pandas_change:
    lines = inspect.getsource(pd.core.arrays.string_arrow.ArrowStringArray.
        to_numpy)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != '2f49768c0cb51d06eb41882aaf214938f268497fffa07bf81964a5056d572ea3':
        warnings.warn(
            'pd.core.arrays.string_arrow.ArrowStringArray.to_numpy has changed'
            )
pd.core.arrays.string_arrow.ArrowStringArray.to_numpy = to_numpy
