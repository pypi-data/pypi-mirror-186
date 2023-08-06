""" Implementation of binary operators for the different types.
    Currently implemented operators:
        arith: add, sub, mul, truediv, floordiv, mod, pow
        cmp: lt, le, eq, ne, ge, gt
"""
import operator
import numba
from numba.core import types
from numba.core.imputils import lower_builtin
from numba.core.typing.builtins import machine_ints
from numba.core.typing.templates import AbstractTemplate, infer_global
from numba.extending import overload
import bodo
from bodo.hiframes.datetime_date_ext import datetime_date_array_type, datetime_date_type, datetime_timedelta_type
from bodo.hiframes.datetime_timedelta_ext import datetime_datetime_type, datetime_timedelta_array_type, pd_timedelta_type
from bodo.hiframes.pd_dataframe_ext import DataFrameType
from bodo.hiframes.pd_index_ext import DatetimeIndexType, HeterogeneousIndexType, is_index_type
from bodo.hiframes.pd_offsets_ext import date_offset_type, month_begin_type, month_end_type, week_type
from bodo.hiframes.pd_timestamp_ext import pd_timestamp_tz_naive_type
from bodo.hiframes.series_impl import SeriesType
from bodo.hiframes.time_ext import TimeType
from bodo.libs.binary_arr_ext import binary_array_type, bytes_type
from bodo.libs.bool_arr_ext import boolean_array
from bodo.libs.decimal_arr_ext import Decimal128Type
from bodo.libs.float_arr_ext import FloatingArrayType
from bodo.libs.int_arr_ext import IntegerArrayType
from bodo.libs.str_ext import string_type
from bodo.utils.typing import BodoError, is_overload_bool, is_str_arr_type, is_timedelta_type


class SeriesCmpOpTemplate(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        assert len(args) == 2
        lhs, rhs = args
        if cmp_timeseries(lhs, rhs) or (isinstance(lhs, DataFrameType) or
            isinstance(rhs, DataFrameType)) or not (isinstance(lhs,
            SeriesType) or isinstance(rhs, SeriesType)):
            return
        if is_cmp_tz_mismatch(lhs, rhs):
            wfps__bpbc, klocc__edmmf = get_series_tz(lhs)
            zuphu__rpztk, klocc__edmmf = get_series_tz(rhs)
            raise BodoError(
                f'{numba.core.utils.OPERATORS_TO_BUILTINS[self.key]} with two Timestamps requires both Timestamps share the same timezone. '
                 +
                f'Argument 0 has timezone {wfps__bpbc} and argument 1 has timezone {zuphu__rpztk}. '
                 +
                'To compare these values please convert to timezone naive with ts.tz_convert(None).'
                )
        bjbwh__lrk = lhs.data if isinstance(lhs, SeriesType) else lhs
        opuh__tvrsw = rhs.data if isinstance(rhs, SeriesType) else rhs
        if bjbwh__lrk in (bodo.pd_timestamp_tz_naive_type, bodo.
            pd_timedelta_type) and opuh__tvrsw.dtype in (bodo.datetime64ns,
            bodo.timedelta64ns):
            bjbwh__lrk = opuh__tvrsw.dtype
        elif opuh__tvrsw in (bodo.pd_timestamp_tz_naive_type, bodo.
            pd_timedelta_type) and bjbwh__lrk.dtype in (bodo.datetime64ns,
            bodo.timedelta64ns):
            opuh__tvrsw = bjbwh__lrk.dtype
        kdgug__biqje = bjbwh__lrk, opuh__tvrsw
        wewo__fuuk = (
            f'{lhs} {numba.core.utils.OPERATORS_TO_BUILTINS[self.key]} {rhs} not supported'
            )
        try:
            nqvnz__qalg = self.context.resolve_function_type(self.key,
                kdgug__biqje, {}).return_type
        except Exception as bfjgn__iuqw:
            raise BodoError(wewo__fuuk)
        if is_overload_bool(nqvnz__qalg):
            raise BodoError(wewo__fuuk)
        ilw__mnl = lhs.index if isinstance(lhs, SeriesType) else rhs.index
        jfgis__euqk = lhs.name_typ if isinstance(lhs, SeriesType
            ) else rhs.name_typ
        wfyki__ovlxs = types.bool_
        yvj__rnh = SeriesType(wfyki__ovlxs, nqvnz__qalg, ilw__mnl, jfgis__euqk)
        return yvj__rnh(*args)


def series_cmp_op_lower(op):

    def lower_impl(context, builder, sig, args):
        qasq__xfu = bodo.hiframes.series_impl.create_binary_op_overload(op)(*
            sig.args)
        if qasq__xfu is None:
            qasq__xfu = create_overload_cmp_operator(op)(*sig.args)
        return context.compile_internal(builder, qasq__xfu, sig, args)
    return lower_impl


class SeriesAndOrTyper(AbstractTemplate):

    def generic(self, args, kws):
        assert len(args) == 2
        assert not kws
        lhs, rhs = args
        if not (isinstance(lhs, SeriesType) or isinstance(rhs, SeriesType)):
            return
        bjbwh__lrk = lhs.data if isinstance(lhs, SeriesType) else lhs
        opuh__tvrsw = rhs.data if isinstance(rhs, SeriesType) else rhs
        kdgug__biqje = bjbwh__lrk, opuh__tvrsw
        wewo__fuuk = (
            f'{lhs} {numba.core.utils.OPERATORS_TO_BUILTINS[self.key]} {rhs} not supported'
            )
        try:
            nqvnz__qalg = self.context.resolve_function_type(self.key,
                kdgug__biqje, {}).return_type
        except Exception as dmy__eqvbp:
            raise BodoError(wewo__fuuk)
        ilw__mnl = lhs.index if isinstance(lhs, SeriesType) else rhs.index
        jfgis__euqk = lhs.name_typ if isinstance(lhs, SeriesType
            ) else rhs.name_typ
        wfyki__ovlxs = nqvnz__qalg.dtype
        yvj__rnh = SeriesType(wfyki__ovlxs, nqvnz__qalg, ilw__mnl, jfgis__euqk)
        return yvj__rnh(*args)


def lower_series_and_or(op):

    def lower_and_or_impl(context, builder, sig, args):
        qasq__xfu = bodo.hiframes.series_impl.create_binary_op_overload(op)(*
            sig.args)
        if qasq__xfu is None:
            lhs, rhs = sig.args
            if isinstance(lhs, DataFrameType) or isinstance(rhs, DataFrameType
                ):
                qasq__xfu = (bodo.hiframes.dataframe_impl.
                    create_binary_op_overload(op)(*sig.args))
        return context.compile_internal(builder, qasq__xfu, sig, args)
    return lower_and_or_impl


def overload_add_operator_scalars(lhs, rhs):
    if lhs == week_type or rhs == week_type:
        return (bodo.hiframes.pd_offsets_ext.
            overload_add_operator_week_offset_type(lhs, rhs))
    if lhs == month_begin_type or rhs == month_begin_type:
        return (bodo.hiframes.pd_offsets_ext.
            overload_add_operator_month_begin_offset_type(lhs, rhs))
    if lhs == month_end_type or rhs == month_end_type:
        return (bodo.hiframes.pd_offsets_ext.
            overload_add_operator_month_end_offset_type(lhs, rhs))
    if lhs == date_offset_type or rhs == date_offset_type:
        return (bodo.hiframes.pd_offsets_ext.
            overload_add_operator_date_offset_type(lhs, rhs))
    if add_timestamp(lhs, rhs):
        return bodo.hiframes.pd_timestamp_ext.overload_add_operator_timestamp(
            lhs, rhs)
    if add_dt_td_and_dt_date(lhs, rhs):
        return (bodo.hiframes.datetime_date_ext.
            overload_add_operator_datetime_date(lhs, rhs))
    if add_datetime_and_timedeltas(lhs, rhs):
        return (bodo.hiframes.datetime_timedelta_ext.
            overload_add_operator_datetime_timedelta(lhs, rhs))
    raise_error_if_not_numba_supported(operator.add, lhs, rhs)


def overload_sub_operator_scalars(lhs, rhs):
    if sub_offset_to_datetime_or_timestamp(lhs, rhs):
        return bodo.hiframes.pd_offsets_ext.overload_sub_operator_offsets(lhs,
            rhs)
    if (isinstance(lhs, bodo.PandasTimestampType) and rhs in (
        datetime_timedelta_type, pd_timedelta_type) or lhs ==
        pd_timestamp_tz_naive_type and rhs == pd_timestamp_tz_naive_type):
        return bodo.hiframes.pd_timestamp_ext.overload_sub_operator_timestamp(
            lhs, rhs)
    if sub_dt_or_td(lhs, rhs):
        return (bodo.hiframes.datetime_date_ext.
            overload_sub_operator_datetime_date(lhs, rhs))
    if sub_datetime_and_timedeltas(lhs, rhs):
        return (bodo.hiframes.datetime_timedelta_ext.
            overload_sub_operator_datetime_timedelta(lhs, rhs))
    if lhs == datetime_datetime_type and rhs == datetime_datetime_type:
        return (bodo.hiframes.datetime_datetime_ext.
            overload_sub_operator_datetime_datetime(lhs, rhs))
    raise_error_if_not_numba_supported(operator.sub, lhs, rhs)


def create_overload_arith_op(op):

    def overload_arith_operator(lhs, rhs):
        if op not in [operator.add, operator.sub]:
            bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(lhs,
                f'{op} operator')
            bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(rhs,
                f'{op} operator')
        if isinstance(lhs, DataFrameType) or isinstance(rhs, DataFrameType):
            return bodo.hiframes.dataframe_impl.create_binary_op_overload(op)(
                lhs, rhs)
        if time_series_operation(lhs, rhs) and op in [operator.add,
            operator.sub]:
            return bodo.hiframes.series_dt_impl.create_bin_op_overload(op)(lhs,
                rhs)
        if isinstance(lhs, SeriesType) or isinstance(rhs, SeriesType):
            return bodo.hiframes.series_impl.create_binary_op_overload(op)(lhs,
                rhs)
        if sub_dt_index_and_timestamp(lhs, rhs) and op == operator.sub:
            return (bodo.hiframes.pd_index_ext.
                overload_sub_operator_datetime_index(lhs, rhs))
        if operand_is_index(lhs) or operand_is_index(rhs):
            return bodo.hiframes.pd_index_ext.create_binary_op_overload(op)(lhs
                , rhs)
        if args_td_and_int_array(lhs, rhs):
            return bodo.libs.int_arr_ext.get_int_array_op_pd_td(op)(lhs, rhs)
        if isinstance(lhs, IntegerArrayType) or isinstance(rhs,
            IntegerArrayType):
            return bodo.libs.int_arr_ext.create_op_overload(op, 2)(lhs, rhs)
        if isinstance(lhs, FloatingArrayType) or isinstance(rhs,
            FloatingArrayType):
            return bodo.libs.float_arr_ext.create_op_overload(op, 2)(lhs, rhs)
        if lhs == boolean_array or rhs == boolean_array:
            return bodo.libs.bool_arr_ext.create_op_overload(op, 2)(lhs, rhs)
        if op == operator.add and (is_str_arr_type(lhs) or types.unliteral(
            lhs) == string_type):
            return bodo.libs.str_arr_ext.overload_add_operator_string_array(lhs
                , rhs)
        if op == operator.add and (isinstance(lhs, bodo.DatetimeArrayType) or
            isinstance(rhs, bodo.DatetimeArrayType)):
            return (bodo.libs.pd_datetime_arr_ext.
                overload_add_operator_datetime_arr(lhs, rhs))
        if op == operator.add:
            return overload_add_operator_scalars(lhs, rhs)
        if op == operator.sub:
            return overload_sub_operator_scalars(lhs, rhs)
        if op == operator.mul:
            if mul_timedelta_and_int(lhs, rhs):
                return (bodo.hiframes.datetime_timedelta_ext.
                    overload_mul_operator_timedelta(lhs, rhs))
            if mul_string_arr_and_int(lhs, rhs):
                return bodo.libs.str_arr_ext.overload_mul_operator_str_arr(lhs,
                    rhs)
            if mul_date_offset_and_int(lhs, rhs):
                return (bodo.hiframes.pd_offsets_ext.
                    overload_mul_date_offset_types(lhs, rhs))
            raise_error_if_not_numba_supported(op, lhs, rhs)
        if op in [operator.truediv, operator.floordiv]:
            if div_timedelta_and_int(lhs, rhs):
                if op == operator.truediv:
                    return (bodo.hiframes.datetime_timedelta_ext.
                        overload_truediv_operator_pd_timedelta(lhs, rhs))
                else:
                    return (bodo.hiframes.datetime_timedelta_ext.
                        overload_floordiv_operator_pd_timedelta(lhs, rhs))
            if div_datetime_timedelta(lhs, rhs):
                if op == operator.truediv:
                    return (bodo.hiframes.datetime_timedelta_ext.
                        overload_truediv_operator_dt_timedelta(lhs, rhs))
                else:
                    return (bodo.hiframes.datetime_timedelta_ext.
                        overload_floordiv_operator_dt_timedelta(lhs, rhs))
            raise_error_if_not_numba_supported(op, lhs, rhs)
        if op == operator.mod:
            if mod_timedeltas(lhs, rhs):
                return (bodo.hiframes.datetime_timedelta_ext.
                    overload_mod_operator_timedeltas(lhs, rhs))
            raise_error_if_not_numba_supported(op, lhs, rhs)
        if op == operator.pow:
            raise_error_if_not_numba_supported(op, lhs, rhs)
        raise BodoError(
            f'{op} operator not supported for data types {lhs} and {rhs}.')
    return overload_arith_operator


def create_overload_cmp_operator(op):

    def overload_cmp_operator(lhs, rhs):
        if isinstance(lhs, DataFrameType) or isinstance(rhs, DataFrameType):
            bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(lhs,
                f'{op} operator')
            bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(rhs,
                f'{op} operator')
            return bodo.hiframes.dataframe_impl.create_binary_op_overload(op)(
                lhs, rhs)
        if cmp_timeseries(lhs, rhs):
            return bodo.hiframes.series_dt_impl.create_cmp_op_overload(op)(lhs,
                rhs)
        if isinstance(lhs, SeriesType) or isinstance(rhs, SeriesType):
            return
        if isinstance(lhs, bodo.libs.pd_datetime_arr_ext.DatetimeArrayType
            ) or isinstance(rhs, bodo.libs.pd_datetime_arr_ext.
            DatetimeArrayType):
            return bodo.libs.pd_datetime_arr_ext.create_cmp_op_overload_arr(op
                )(lhs, rhs)
        if isinstance(lhs, types.Array
            ) and lhs.dtype == bodo.datetime64ns and rhs in (
            datetime_date_array_type, datetime_date_type) or lhs in (
            datetime_date_array_type, datetime_date_type) and isinstance(rhs,
            types.Array) and rhs.dtype == bodo.datetime64ns:
            return (bodo.hiframes.datetime_date_ext.
                create_datetime_array_date_cmp_op_overload(op)(lhs, rhs))
        if lhs == datetime_date_array_type or rhs == datetime_date_array_type:
            return bodo.hiframes.datetime_date_ext.create_cmp_op_overload_arr(
                op)(lhs, rhs)
        if (lhs == datetime_timedelta_array_type or rhs ==
            datetime_timedelta_array_type):
            qasq__xfu = (bodo.hiframes.datetime_timedelta_ext.
                create_cmp_op_overload(op))
            return qasq__xfu(lhs, rhs)
        if is_str_arr_type(lhs) or is_str_arr_type(rhs):
            return bodo.libs.str_arr_ext.create_binary_op_overload(op)(lhs, rhs
                )
        if isinstance(lhs, Decimal128Type) and isinstance(rhs, Decimal128Type):
            return bodo.libs.decimal_arr_ext.decimal_create_cmp_op_overload(op
                )(lhs, rhs)
        if lhs == boolean_array or rhs == boolean_array:
            return bodo.libs.bool_arr_ext.create_op_overload(op, 2)(lhs, rhs)
        if isinstance(lhs, IntegerArrayType) or isinstance(rhs,
            IntegerArrayType):
            return bodo.libs.int_arr_ext.create_op_overload(op, 2)(lhs, rhs)
        if isinstance(lhs, FloatingArrayType) or isinstance(rhs,
            FloatingArrayType):
            return bodo.libs.float_arr_ext.create_op_overload(op, 2)(lhs, rhs)
        if binary_array_cmp(lhs, rhs):
            return bodo.libs.binary_arr_ext.create_binary_cmp_op_overload(op)(
                lhs, rhs)
        if cmp_dt_index_to_string(lhs, rhs):
            return bodo.hiframes.pd_index_ext.overload_binop_dti_str(op)(lhs,
                rhs)
        if operand_is_index(lhs) or operand_is_index(rhs):
            return bodo.hiframes.pd_index_ext.create_binary_op_overload(op)(lhs
                , rhs)
        if lhs == datetime_date_type and rhs == datetime_date_type:
            return bodo.hiframes.datetime_date_ext.create_cmp_op_overload(op)(
                lhs, rhs)
        if isinstance(lhs, TimeType) and isinstance(rhs, TimeType):
            return bodo.hiframes.time_ext.create_cmp_op_overload(op)(lhs, rhs)
        if can_cmp_date_datetime(lhs, rhs, op):
            return (bodo.hiframes.datetime_date_ext.
                create_datetime_date_cmp_op_overload(op)(lhs, rhs))
        if lhs == datetime_datetime_type and rhs == datetime_datetime_type:
            return bodo.hiframes.datetime_datetime_ext.create_cmp_op_overload(
                op)(lhs, rhs)
        if lhs == datetime_timedelta_type and rhs == datetime_timedelta_type:
            return bodo.hiframes.datetime_timedelta_ext.create_cmp_op_overload(
                op)(lhs, rhs)
        if cmp_timedeltas(lhs, rhs):
            qasq__xfu = (bodo.hiframes.datetime_timedelta_ext.
                pd_create_cmp_op_overload(op))
            return qasq__xfu(lhs, rhs)
        if cmp_timestamp_or_date(lhs, rhs):
            return (bodo.hiframes.pd_timestamp_ext.
                create_timestamp_cmp_op_overload(op)(lhs, rhs))
        if cmp_op_supported_by_numba(lhs, rhs):
            return
        raise BodoError(
            f'{op} operator not supported for data types {lhs} and {rhs}.')
    return overload_cmp_operator


def add_dt_td_and_dt_date(lhs, rhs):
    vjz__pctu = lhs == datetime_timedelta_type and rhs == datetime_date_type
    nie__xaaq = rhs == datetime_timedelta_type and lhs == datetime_date_type
    return vjz__pctu or nie__xaaq


def add_timestamp(lhs, rhs):
    iec__vklzm = isinstance(lhs, bodo.PandasTimestampType
        ) and is_timedelta_type(rhs)
    owl__lww = is_timedelta_type(lhs) and isinstance(rhs, bodo.
        PandasTimestampType)
    return iec__vklzm or owl__lww


def add_datetime_and_timedeltas(lhs, rhs):
    oxn__nuiy = [datetime_timedelta_type, pd_timedelta_type]
    iue__shln = [datetime_timedelta_type, pd_timedelta_type,
        datetime_datetime_type]
    yfr__wgrc = lhs in oxn__nuiy and rhs in oxn__nuiy
    btjy__mjgws = (lhs == datetime_datetime_type and rhs in oxn__nuiy or 
        rhs == datetime_datetime_type and lhs in oxn__nuiy)
    return yfr__wgrc or btjy__mjgws


def mul_string_arr_and_int(lhs, rhs):
    opuh__tvrsw = isinstance(lhs, types.Integer) and is_str_arr_type(rhs)
    bjbwh__lrk = is_str_arr_type(lhs) and isinstance(rhs, types.Integer)
    return opuh__tvrsw or bjbwh__lrk


def mul_timedelta_and_int(lhs, rhs):
    vjz__pctu = lhs in [pd_timedelta_type, datetime_timedelta_type
        ] and isinstance(rhs, types.Integer)
    nie__xaaq = rhs in [pd_timedelta_type, datetime_timedelta_type
        ] and isinstance(lhs, types.Integer)
    return vjz__pctu or nie__xaaq


def mul_date_offset_and_int(lhs, rhs):
    lxbam__fifis = lhs in [week_type, month_end_type, month_begin_type,
        date_offset_type] and isinstance(rhs, types.Integer)
    gbu__dagu = rhs in [week_type, month_end_type, month_begin_type,
        date_offset_type] and isinstance(lhs, types.Integer)
    return lxbam__fifis or gbu__dagu


def sub_offset_to_datetime_or_timestamp(lhs, rhs):
    ajaq__ehkmx = [datetime_datetime_type, datetime_date_type,
        pd_timestamp_tz_naive_type]
    tz_aware_classes = bodo.PandasTimestampType,
    mjhi__oaoj = week_type, month_begin_type, month_end_type
    ddqqd__pqweq = date_offset_type,
    return rhs in mjhi__oaoj and isinstance(lhs, tz_aware_classes) or (rhs in
        ddqqd__pqweq or rhs in mjhi__oaoj) and lhs in ajaq__ehkmx


def sub_dt_index_and_timestamp(lhs, rhs):
    ufyl__rfsc = isinstance(lhs, DatetimeIndexType
        ) and rhs == pd_timestamp_tz_naive_type
    vqvw__yfcnu = isinstance(rhs, DatetimeIndexType
        ) and lhs == pd_timestamp_tz_naive_type
    return ufyl__rfsc or vqvw__yfcnu


def sub_dt_or_td(lhs, rhs):
    ogjc__phyds = lhs == datetime_date_type and rhs == datetime_timedelta_type
    qxfas__vmc = lhs == datetime_date_type and rhs == datetime_date_type
    uyf__xae = (lhs == datetime_date_array_type and rhs ==
        datetime_timedelta_type)
    return ogjc__phyds or qxfas__vmc or uyf__xae


def sub_datetime_and_timedeltas(lhs, rhs):
    pwupq__jyxkj = (is_timedelta_type(lhs) or lhs == datetime_datetime_type
        ) and is_timedelta_type(rhs)
    mji__gqmjf = (lhs == datetime_timedelta_array_type and rhs ==
        datetime_timedelta_type)
    return pwupq__jyxkj or mji__gqmjf


def div_timedelta_and_int(lhs, rhs):
    yfr__wgrc = lhs == pd_timedelta_type and rhs == pd_timedelta_type
    ovc__qgva = lhs == pd_timedelta_type and isinstance(rhs, types.Integer)
    return yfr__wgrc or ovc__qgva


def div_datetime_timedelta(lhs, rhs):
    yfr__wgrc = (lhs == datetime_timedelta_type and rhs ==
        datetime_timedelta_type)
    ovc__qgva = lhs == datetime_timedelta_type and rhs == types.int64
    return yfr__wgrc or ovc__qgva


def mod_timedeltas(lhs, rhs):
    ovq__imisi = lhs == pd_timedelta_type and rhs == pd_timedelta_type
    zfa__oegke = (lhs == datetime_timedelta_type and rhs ==
        datetime_timedelta_type)
    return ovq__imisi or zfa__oegke


def cmp_dt_index_to_string(lhs, rhs):
    ufyl__rfsc = isinstance(lhs, DatetimeIndexType) and types.unliteral(rhs
        ) == string_type
    vqvw__yfcnu = isinstance(rhs, DatetimeIndexType) and types.unliteral(lhs
        ) == string_type
    return ufyl__rfsc or vqvw__yfcnu


def cmp_timestamp_or_date(lhs, rhs):
    rgbkt__unl = isinstance(lhs, bodo.hiframes.pd_timestamp_ext.
        PandasTimestampType
        ) and rhs == bodo.hiframes.datetime_date_ext.datetime_date_type
    xnwmz__cmon = (lhs == bodo.hiframes.datetime_date_ext.
        datetime_date_type and isinstance(rhs, bodo.hiframes.
        pd_timestamp_ext.PandasTimestampType))
    lrmth__gxudh = isinstance(lhs, bodo.hiframes.pd_timestamp_ext.
        PandasTimestampType) and isinstance(rhs, bodo.hiframes.
        pd_timestamp_ext.PandasTimestampType)
    frsib__mopu = (lhs == pd_timestamp_tz_naive_type and rhs == bodo.
        datetime64ns)
    aptl__ugbpt = (rhs == pd_timestamp_tz_naive_type and lhs == bodo.
        datetime64ns)
    return (rgbkt__unl or xnwmz__cmon or lrmth__gxudh or frsib__mopu or
        aptl__ugbpt)


def get_series_tz(val):
    if bodo.hiframes.pd_series_ext.is_dt64_series_typ(val):
        if isinstance(val.data, bodo.libs.pd_datetime_arr_ext.DatetimeArrayType
            ):
            nnb__piwhm = val.data.tz
        else:
            nnb__piwhm = None
    elif isinstance(val, bodo.libs.pd_datetime_arr_ext.DatetimeArrayType):
        nnb__piwhm = val.tz
    elif isinstance(val, types.Array) and val.dtype == bodo.datetime64ns:
        nnb__piwhm = None
    elif isinstance(val, bodo.PandasTimestampType):
        nnb__piwhm = val.tz
    elif val == bodo.datetime64ns:
        nnb__piwhm = None
    else:
        return None, False
    return nnb__piwhm, True


def is_cmp_tz_mismatch(lhs, rhs):
    wfps__bpbc, srp__dkdl = get_series_tz(lhs)
    zuphu__rpztk, byz__gltc = get_series_tz(rhs)
    return srp__dkdl and byz__gltc and wfps__bpbc != zuphu__rpztk


def cmp_timeseries(lhs, rhs):
    euxqn__wphi = bodo.hiframes.pd_series_ext.is_dt64_series_typ(rhs) and (bodo
        .utils.typing.is_overload_constant_str(lhs) or lhs == bodo.libs.
        str_ext.string_type)
    ydjq__qtv = bodo.hiframes.pd_series_ext.is_dt64_series_typ(lhs) and (bodo
        .utils.typing.is_overload_constant_str(rhs) or rhs == bodo.libs.
        str_ext.string_type)
    felk__nzo = (bodo.hiframes.pd_series_ext.is_dt64_series_typ(rhs) and 
        rhs.dtype == bodo.datetime64ns and lhs == bodo.hiframes.
        pd_timestamp_ext.pd_timestamp_tz_naive_type or bodo.hiframes.
        pd_series_ext.is_dt64_series_typ(lhs) and lhs.dtype == bodo.
        datetime64ns and rhs == bodo.hiframes.pd_timestamp_ext.
        pd_timestamp_tz_naive_type)
    ruaop__jiifh = euxqn__wphi or ydjq__qtv or felk__nzo
    lwgxs__mgg = bodo.hiframes.pd_series_ext.is_timedelta64_series_typ(rhs
        ) and lhs == bodo.hiframes.datetime_timedelta_ext.datetime_timedelta_type
    kyr__tmur = bodo.hiframes.pd_series_ext.is_timedelta64_series_typ(lhs
        ) and rhs == bodo.hiframes.datetime_timedelta_ext.datetime_timedelta_type
    yjyrr__duioz = lwgxs__mgg or kyr__tmur
    return ruaop__jiifh or yjyrr__duioz


def cmp_timedeltas(lhs, rhs):
    yfr__wgrc = [pd_timedelta_type, bodo.timedelta64ns]
    return lhs in yfr__wgrc and rhs in yfr__wgrc


def operand_is_index(operand):
    return is_index_type(operand) or isinstance(operand, HeterogeneousIndexType
        )


def helper_time_series_checks(operand):
    ahmx__fqhq = bodo.hiframes.pd_series_ext.is_dt64_series_typ(operand
        ) or bodo.hiframes.pd_series_ext.is_timedelta64_series_typ(operand
        ) or operand in [datetime_timedelta_type, datetime_datetime_type,
        pd_timestamp_tz_naive_type]
    return ahmx__fqhq


def binary_array_cmp(lhs, rhs):
    return lhs == binary_array_type and rhs in [bytes_type, binary_array_type
        ] or lhs in [bytes_type, binary_array_type
        ] and rhs == binary_array_type


def can_cmp_date_datetime(lhs, rhs, op):
    return op in (operator.eq, operator.ne) and (lhs == datetime_date_type and
        rhs == datetime_datetime_type or lhs == datetime_datetime_type and 
        rhs == datetime_date_type)


def time_series_operation(lhs, rhs):
    qgxoi__xlmcs = bodo.hiframes.pd_series_ext.is_timedelta64_series_typ(lhs
        ) and rhs == datetime_timedelta_type
    xtanv__jbtwv = bodo.hiframes.pd_series_ext.is_timedelta64_series_typ(rhs
        ) and lhs == datetime_timedelta_type
    pvl__gynh = bodo.hiframes.pd_series_ext.is_dt64_series_typ(lhs
        ) and helper_time_series_checks(rhs)
    syk__jdcyn = bodo.hiframes.pd_series_ext.is_dt64_series_typ(rhs
        ) and helper_time_series_checks(lhs)
    return qgxoi__xlmcs or xtanv__jbtwv or pvl__gynh or syk__jdcyn


def args_td_and_int_array(lhs, rhs):
    ppjjf__hhzgh = (isinstance(lhs, IntegerArrayType) or isinstance(lhs,
        types.Array) and isinstance(lhs.dtype, types.Integer)) or (isinstance
        (rhs, IntegerArrayType) or isinstance(rhs, types.Array) and
        isinstance(rhs.dtype, types.Integer))
    nbq__pkusj = lhs in [pd_timedelta_type] or rhs in [pd_timedelta_type]
    return ppjjf__hhzgh and nbq__pkusj


def arith_op_supported_by_numba(op, lhs, rhs):
    if op == operator.mul:
        nie__xaaq = isinstance(lhs, (types.Integer, types.Float)
            ) and isinstance(rhs, types.NPTimedelta)
        vjz__pctu = isinstance(rhs, (types.Integer, types.Float)
            ) and isinstance(lhs, types.NPTimedelta)
        zlyx__jgkln = nie__xaaq or vjz__pctu
        bhpur__mym = isinstance(rhs, types.UnicodeType) and isinstance(lhs,
            types.Integer)
        ikr__uepe = isinstance(lhs, types.UnicodeType) and isinstance(rhs,
            types.Integer)
        bxyd__vmo = bhpur__mym or ikr__uepe
        nlfee__fvymz = isinstance(lhs, types.Integer) and isinstance(rhs,
            types.Integer)
        azalm__ckuc = isinstance(lhs, types.Float) and isinstance(rhs,
            types.Float)
        wdqtp__ouzq = isinstance(lhs, types.Complex) and isinstance(rhs,
            types.Complex)
        itihq__lkhy = nlfee__fvymz or azalm__ckuc or wdqtp__ouzq
        ubt__ruf = isinstance(lhs, types.List) and isinstance(rhs, types.
            Integer) or isinstance(lhs, types.Integer) and isinstance(rhs,
            types.List)
        tys = types.UnicodeCharSeq, types.CharSeq, types.Bytes
        inicq__whe = isinstance(lhs, tys) or isinstance(rhs, tys)
        gqufl__vcnwu = isinstance(lhs, types.Array) or isinstance(rhs,
            types.Array)
        return (zlyx__jgkln or bxyd__vmo or itihq__lkhy or ubt__ruf or
            inicq__whe or gqufl__vcnwu)
    if op == operator.pow:
        ihl__gahz = isinstance(lhs, types.Integer) and isinstance(rhs, (
            types.IntegerLiteral, types.Integer))
        rnml__jzl = isinstance(lhs, types.Float) and isinstance(rhs, (types
            .IntegerLiteral, types.Float, types.Integer) or rhs in types.
            unsigned_domain or rhs in types.signed_domain)
        wdqtp__ouzq = isinstance(lhs, types.Complex) and isinstance(rhs,
            types.Complex)
        gqufl__vcnwu = isinstance(lhs, types.Array) or isinstance(rhs,
            types.Array)
        return ihl__gahz or rnml__jzl or wdqtp__ouzq or gqufl__vcnwu
    if op == operator.floordiv:
        azalm__ckuc = lhs in types.real_domain and rhs in types.real_domain
        nlfee__fvymz = isinstance(lhs, types.Integer) and isinstance(rhs,
            types.Integer)
        osjxx__atigj = isinstance(lhs, types.Float) and isinstance(rhs,
            types.Float)
        yfr__wgrc = isinstance(lhs, types.NPTimedelta) and isinstance(rhs,
            (types.Integer, types.Float, types.NPTimedelta))
        gqufl__vcnwu = isinstance(lhs, types.Array) or isinstance(rhs,
            types.Array)
        return (azalm__ckuc or nlfee__fvymz or osjxx__atigj or yfr__wgrc or
            gqufl__vcnwu)
    if op == operator.truediv:
        scs__thu = lhs in machine_ints and rhs in machine_ints
        azalm__ckuc = lhs in types.real_domain and rhs in types.real_domain
        wdqtp__ouzq = (lhs in types.complex_domain and rhs in types.
            complex_domain)
        nlfee__fvymz = isinstance(lhs, types.Integer) and isinstance(rhs,
            types.Integer)
        osjxx__atigj = isinstance(lhs, types.Float) and isinstance(rhs,
            types.Float)
        nak__unhwu = isinstance(lhs, types.Complex) and isinstance(rhs,
            types.Complex)
        yfr__wgrc = isinstance(lhs, types.NPTimedelta) and isinstance(rhs,
            (types.Integer, types.Float, types.NPTimedelta))
        gqufl__vcnwu = isinstance(lhs, types.Array) or isinstance(rhs,
            types.Array)
        return (scs__thu or azalm__ckuc or wdqtp__ouzq or nlfee__fvymz or
            osjxx__atigj or nak__unhwu or yfr__wgrc or gqufl__vcnwu)
    if op == operator.mod:
        scs__thu = lhs in machine_ints and rhs in machine_ints
        azalm__ckuc = lhs in types.real_domain and rhs in types.real_domain
        nlfee__fvymz = isinstance(lhs, types.Integer) and isinstance(rhs,
            types.Integer)
        osjxx__atigj = isinstance(lhs, types.Float) and isinstance(rhs,
            types.Float)
        gqufl__vcnwu = isinstance(lhs, types.Array) or isinstance(rhs,
            types.Array)
        return (scs__thu or azalm__ckuc or nlfee__fvymz or osjxx__atigj or
            gqufl__vcnwu)
    if op == operator.add or op == operator.sub:
        zlyx__jgkln = isinstance(lhs, types.NPTimedelta) and isinstance(rhs,
            types.NPTimedelta)
        qekof__ikn = isinstance(lhs, types.NPDatetime) and isinstance(rhs,
            types.NPDatetime)
        esx__ywet = isinstance(lhs, types.NPDatetime) and isinstance(rhs,
            types.NPTimedelta)
        xyh__lun = isinstance(lhs, types.Set) and isinstance(rhs, types.Set)
        nlfee__fvymz = isinstance(lhs, types.Integer) and isinstance(rhs,
            types.Integer)
        azalm__ckuc = isinstance(lhs, types.Float) and isinstance(rhs,
            types.Float)
        wdqtp__ouzq = isinstance(lhs, types.Complex) and isinstance(rhs,
            types.Complex)
        itihq__lkhy = nlfee__fvymz or azalm__ckuc or wdqtp__ouzq
        gqufl__vcnwu = isinstance(lhs, types.Array) or isinstance(rhs,
            types.Array)
        phnt__uuy = isinstance(lhs, types.BaseTuple) and isinstance(rhs,
            types.BaseTuple)
        ubt__ruf = isinstance(lhs, types.List) and isinstance(rhs, types.List)
        trzey__qlp = isinstance(lhs, types.UnicodeCharSeq) and isinstance(rhs,
            types.UnicodeType)
        dioy__gohgk = isinstance(rhs, types.UnicodeCharSeq) and isinstance(lhs,
            types.UnicodeType)
        muoa__vpzww = isinstance(lhs, types.UnicodeCharSeq) and isinstance(rhs,
            types.UnicodeCharSeq)
        beitt__ict = isinstance(lhs, (types.CharSeq, types.Bytes)
            ) and isinstance(rhs, (types.CharSeq, types.Bytes))
        qzom__yoggk = trzey__qlp or dioy__gohgk or muoa__vpzww or beitt__ict
        bxyd__vmo = isinstance(lhs, types.UnicodeType) and isinstance(rhs,
            types.UnicodeType)
        lgt__uni = isinstance(lhs, types.UnicodeType) and isinstance(rhs,
            types.UnicodeCharSeq)
        aqzu__pdtps = bxyd__vmo or lgt__uni
        chn__beky = lhs == types.NPTimedelta and rhs == types.NPDatetime
        nwkg__yaipk = (phnt__uuy or ubt__ruf or qzom__yoggk or aqzu__pdtps or
            chn__beky)
        losk__yca = op == operator.add and nwkg__yaipk
        return (zlyx__jgkln or qekof__ikn or esx__ywet or xyh__lun or
            itihq__lkhy or gqufl__vcnwu or losk__yca)


def cmp_op_supported_by_numba(lhs, rhs):
    gqufl__vcnwu = isinstance(lhs, types.Array) or isinstance(rhs, types.Array)
    ubt__ruf = isinstance(lhs, types.ListType) and isinstance(rhs, types.
        ListType)
    zlyx__jgkln = isinstance(lhs, types.NPTimedelta) and isinstance(rhs,
        types.NPTimedelta)
    wdqs__srha = isinstance(lhs, types.NPDatetime) and isinstance(rhs,
        types.NPDatetime)
    unicode_types = (types.UnicodeType, types.StringLiteral, types.CharSeq,
        types.Bytes, types.UnicodeCharSeq)
    bxyd__vmo = isinstance(lhs, unicode_types) and isinstance(rhs,
        unicode_types)
    phnt__uuy = isinstance(lhs, types.BaseTuple) and isinstance(rhs, types.
        BaseTuple)
    xyh__lun = isinstance(lhs, types.Set) and isinstance(rhs, types.Set)
    itihq__lkhy = isinstance(lhs, types.Number) and isinstance(rhs, types.
        Number)
    ypty__vofs = isinstance(lhs, types.Boolean) and isinstance(rhs, types.
        Boolean)
    xkv__oyod = isinstance(lhs, types.NoneType) or isinstance(rhs, types.
        NoneType)
    yvksq__myr = isinstance(lhs, types.DictType) and isinstance(rhs, types.
        DictType)
    qwhf__swebn = isinstance(lhs, types.EnumMember) and isinstance(rhs,
        types.EnumMember)
    advf__htar = isinstance(lhs, types.Literal) and isinstance(rhs, types.
        Literal)
    return (ubt__ruf or zlyx__jgkln or wdqs__srha or bxyd__vmo or phnt__uuy or
        xyh__lun or itihq__lkhy or ypty__vofs or xkv__oyod or yvksq__myr or
        gqufl__vcnwu or qwhf__swebn or advf__htar)


def raise_error_if_not_numba_supported(op, lhs, rhs):
    if arith_op_supported_by_numba(op, lhs, rhs):
        return
    raise BodoError(
        f'{op} operator not supported for data types {lhs} and {rhs}.')


def _install_series_and_or():
    for op in (operator.or_, operator.and_):
        infer_global(op)(SeriesAndOrTyper)
        lower_impl = lower_series_and_or(op)
        lower_builtin(op, SeriesType, SeriesType)(lower_impl)
        lower_builtin(op, SeriesType, types.Any)(lower_impl)
        lower_builtin(op, types.Any, SeriesType)(lower_impl)


_install_series_and_or()


def _install_cmp_ops():
    for op in (operator.lt, operator.eq, operator.ne, operator.ge, operator
        .gt, operator.le):
        infer_global(op)(SeriesCmpOpTemplate)
        lower_impl = series_cmp_op_lower(op)
        lower_builtin(op, SeriesType, SeriesType)(lower_impl)
        lower_builtin(op, SeriesType, types.Any)(lower_impl)
        lower_builtin(op, types.Any, SeriesType)(lower_impl)
        tnjz__kdjc = create_overload_cmp_operator(op)
        overload(op, no_unliteral=True)(tnjz__kdjc)


_install_cmp_ops()


def install_arith_ops():
    for op in (operator.add, operator.sub, operator.mul, operator.truediv,
        operator.floordiv, operator.mod, operator.pow):
        tnjz__kdjc = create_overload_arith_op(op)
        overload(op, no_unliteral=True)(tnjz__kdjc)


install_arith_ops()
