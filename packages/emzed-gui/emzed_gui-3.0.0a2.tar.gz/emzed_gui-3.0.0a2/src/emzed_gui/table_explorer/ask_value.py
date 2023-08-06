#!/usr/bin/env python
from emzed import RtType, MzType

from emzed_gui.widgets import (
    AskIntValue,
    AskFloatValue,
    AskRtValue,
    AskMzValue,
    AskStrValue,
    AskBoolValue,
)


def ask_value(col_name, col_type, parent=None):
    dlg_class = {
        float: AskFloatValue,
        int: AskIntValue,
        bool: AskBoolValue,
        str: AskStrValue,
        RtType: AskRtValue,
        MzType: AskMzValue,
    }.get(col_type)

    if dlg_class is None:
        raise RuntimeError(f"type {col_type} not supported")

    dlg = dlg_class(col_name, parent)
    dlg.adjustSize()
    dlg.exec_()

    return dlg.canceled, dlg.value


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    ask_value("this is a very long message", int)

