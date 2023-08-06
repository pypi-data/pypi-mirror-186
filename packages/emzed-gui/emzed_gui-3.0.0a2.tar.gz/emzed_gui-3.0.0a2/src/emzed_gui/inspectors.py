# This file is part of emzed (https://emzed.ethz.ch), a software toolbox for analysing
# LCMS data with Python.
#
# Copyright (C) 2020 ETH Zurich, SIS ID.
#
# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this
# program.  If not, see <http://www.gnu.org/licenses/>.


import os

from emzed import PeakMap, Table

# from ..data_types.col_types import Blob


def has_inspector(clz):
    return clz in (PeakMap, Table)


def try_to_load(path):
    ext = os.path.splitext(path)[1]
    if ext.upper() in (".MZXML", ".MZML", ".MZDATA"):
        import emzed

        return emzed.io.loadPeakMap(path)
    elif ext == ".table":
        import emzed

        return emzed.io.loadTable(path)
    else:
        raise ValueError("I can not handle %s files" % ext)


def inspector(obj, *a, **kw):
    if isinstance(obj, str):
        obj = try_to_load(obj)
    if isinstance(obj, PeakMap):
        from .peakmap_explorer import inspectPeakMap

        return lambda: inspectPeakMap(obj, *a, **kw)
    elif isinstance(obj, (Table)):
        from .table_explorer import inspect

        return lambda: inspect(obj, *a, **kw)
    elif isinstance(obj, (list, tuple)) and all(isinstance(t, Table) for t in obj):
        from .table_explorer import inspect

        return lambda: inspect(obj, *a, **kw)
    elif 0 and isinstance(obj, Blob):
        # TODO:
        from .image_dialog import ImageDialog

        modal = kw.get("modal", True)

        if modal:

            def show():
                dlg = ImageDialog(obj.data)
                dlg.raise_()
                dlg.exec_()

        else:

            def show():
                dlg = ImageDialog(obj.data, parent=kw.get("parent"))
                dlg.show()

        return show

    return None


def inspect(obj, *a, **kw):
    insp = inspector(obj, *a, **kw)
    if insp is not None:
        return insp()
    else:
        raise Exception("no inspector for %r" % obj)
