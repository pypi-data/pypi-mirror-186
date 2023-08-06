from numba.core import cgutils, types
from numba.extending import NativeValue, box, make_attribute_wrapper, models, register_model, typeof_impl, unbox


def install_py_obj_class(types_name, module, python_type=None, class_name=
    None, model_name=None):
    class_name = ''.join(map(str.title, types_name.split('_'))
        ) if class_name is None else class_name
    model_name = f'{class_name}Model' if model_name is None else model_name
    htedy__akk = f'class {class_name}(types.Opaque):\n'
    htedy__akk += f'    def __init__(self):\n'
    htedy__akk += f"       types.Opaque.__init__(self, name='{class_name}')\n"
    htedy__akk += f'    def __reduce__(self):\n'
    htedy__akk += (
        f"        return (types.Opaque, ('{class_name}',), self.__dict__)\n")
    bxwv__fttia = {}
    exec(htedy__akk, {'types': types, 'models': models}, bxwv__fttia)
    klwym__wpd = bxwv__fttia[class_name]
    setattr(module, class_name, klwym__wpd)
    class_instance = klwym__wpd()
    setattr(types, types_name, class_instance)
    htedy__akk = f'class {model_name}(models.StructModel):\n'
    htedy__akk += f'    def __init__(self, dmm, fe_type):\n'
    htedy__akk += f'        members = [\n'
    htedy__akk += (
        f"            ('meminfo', types.MemInfoPointer({types_name})),\n")
    htedy__akk += f"            ('pyobj', types.voidptr),\n"
    htedy__akk += f'        ]\n'
    htedy__akk += (
        f'        models.StructModel.__init__(self, dmm, fe_type, members)\n')
    exec(htedy__akk, {'types': types, 'models': models, types_name:
        class_instance}, bxwv__fttia)
    sdim__bldul = bxwv__fttia[model_name]
    setattr(module, model_name, sdim__bldul)
    register_model(klwym__wpd)(sdim__bldul)
    make_attribute_wrapper(klwym__wpd, 'pyobj', '_pyobj')
    if python_type is not None:
        typeof_impl.register(python_type)(lambda val, c: class_instance)
    unbox(klwym__wpd)(unbox_py_obj)
    box(klwym__wpd)(box_py_obj)
    return klwym__wpd


def box_py_obj(typ, val, c):
    etnj__bxoui = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    obj = etnj__bxoui.pyobj
    c.pyapi.incref(obj)
    c.context.nrt.decref(c.builder, typ, val)
    return obj


def unbox_py_obj(typ, obj, c):
    etnj__bxoui = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    etnj__bxoui.meminfo = c.pyapi.nrt_meminfo_new_from_pyobject(c.context.
        get_constant_null(types.voidptr), obj)
    etnj__bxoui.pyobj = obj
    return NativeValue(etnj__bxoui._getvalue())
