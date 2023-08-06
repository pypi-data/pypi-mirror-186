"""
Helper functions and classes to simplify Template Generation
for Bodo classes.
"""
import numba
from numba.core.typing.templates import AttributeTemplate


class OverloadedKeyAttributeTemplate(AttributeTemplate):
    _attr_set = None

    def _is_existing_attr(self, attr_name):
        if self._attr_set is None:
            kzbok__dsurg = set()
            tpls__xuwl = list(self.context._get_attribute_templates(self.key))
            silnh__uzrkg = tpls__xuwl.index(self) + 1
            for yqx__xrflk in range(silnh__uzrkg, len(tpls__xuwl)):
                if isinstance(tpls__xuwl[yqx__xrflk], numba.core.typing.
                    templates._OverloadAttributeTemplate):
                    kzbok__dsurg.add(tpls__xuwl[yqx__xrflk]._attr)
            self._attr_set = kzbok__dsurg
        return attr_name in self._attr_set
