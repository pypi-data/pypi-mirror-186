"""
Analysis and transformation for HDF5 support.
"""
import types as pytypes
import numba
from numba.core import ir, types
from numba.core.ir_utils import compile_to_numba_ir, find_callname, find_const, get_definition, guard, replace_arg_nodes, require
import bodo
import bodo.io
from bodo.utils.transform import get_const_value_inner


class H5_IO:

    def __init__(self, func_ir, _locals, flags, arg_types):
        self.func_ir = func_ir
        self.locals = _locals
        self.flags = flags
        self.arg_types = arg_types

    def handle_possible_h5_read(self, assign, lhs, rhs):
        jbsxe__osa = self._get_h5_type(lhs, rhs)
        if jbsxe__osa is not None:
            mjzhc__vqyb = str(jbsxe__osa.dtype)
            ezfov__vyff = 'def _h5_read_impl(dset, index):\n'
            ezfov__vyff += (
                "  arr = bodo.io.h5_api.h5_read_dummy(dset, {}, '{}', index)\n"
                .format(jbsxe__osa.ndim, mjzhc__vqyb))
            iyan__wwwst = {}
            exec(ezfov__vyff, {}, iyan__wwwst)
            wnoq__wloar = iyan__wwwst['_h5_read_impl']
            pjt__auwq = compile_to_numba_ir(wnoq__wloar, {'bodo': bodo}
                ).blocks.popitem()[1]
            ocovz__ijn = rhs.index if rhs.op == 'getitem' else rhs.index_var
            replace_arg_nodes(pjt__auwq, [rhs.value, ocovz__ijn])
            zhqh__agen = pjt__auwq.body[:-3]
            zhqh__agen[-1].target = assign.target
            return zhqh__agen
        return None

    def _get_h5_type(self, lhs, rhs):
        jbsxe__osa = self._get_h5_type_locals(lhs)
        if jbsxe__osa is not None:
            return jbsxe__osa
        return guard(self._infer_h5_typ, rhs)

    def _infer_h5_typ(self, rhs):
        require(rhs.op in ('getitem', 'static_getitem'))
        ocovz__ijn = rhs.index if rhs.op == 'getitem' else rhs.index_var
        dlw__anzp = guard(find_const, self.func_ir, ocovz__ijn)
        require(not isinstance(dlw__anzp, str))
        val_def = rhs
        obj_name_list = []
        while True:
            val_def = get_definition(self.func_ir, val_def.value)
            require(isinstance(val_def, ir.Expr))
            if val_def.op == 'call':
                return self._get_h5_type_file(val_def, obj_name_list)
            require(val_def.op in ('getitem', 'static_getitem'))
            xduo__vxaz = (val_def.index if val_def.op == 'getitem' else
                val_def.index_var)
            txyzd__klkh = get_const_value_inner(self.func_ir, xduo__vxaz,
                arg_types=self.arg_types)
            obj_name_list.append(txyzd__klkh)

    def _get_h5_type_file(self, val_def, obj_name_list):
        require(len(obj_name_list) > 0)
        require(find_callname(self.func_ir, val_def) == ('File', 'h5py'))
        require(len(val_def.args) > 0)
        nij__ovk = get_const_value_inner(self.func_ir, val_def.args[0],
            arg_types=self.arg_types)
        obj_name_list.reverse()
        import h5py
        nlbz__sctko = h5py.File(nij__ovk, 'r')
        jldd__bcrej = nlbz__sctko
        for txyzd__klkh in obj_name_list:
            jldd__bcrej = jldd__bcrej[txyzd__klkh]
        require(isinstance(jldd__bcrej, h5py.Dataset))
        yxvfh__djj = len(jldd__bcrej.shape)
        mclb__rgvbc = numba.np.numpy_support.from_dtype(jldd__bcrej.dtype)
        nlbz__sctko.close()
        return types.Array(mclb__rgvbc, yxvfh__djj, 'C')

    def _get_h5_type_locals(self, varname):
        ksxq__yvxdd = self.locals.pop(varname, None)
        if ksxq__yvxdd is None and varname is not None:
            ksxq__yvxdd = self.flags.h5_types.get(varname, None)
        return ksxq__yvxdd
