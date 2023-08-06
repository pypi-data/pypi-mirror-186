#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""__main__."""

import sys
from PySide6.QtCore import QCoreApplication, Qt

from usb_imager.gui_qt import Application
from usb_imager.modules.udisks2 import UDisks2
from usb_imager.modules.msgbox import MsgBox


def check_deps() -> None:
    """Check system dependencies."""
    # Check for platform 'linux'
    if not sys.platform.startswith('linux'):
        MsgBox().error("Programm only supports Unix!")
        sys.exit(1)

    # Check for installed UDisks2/D-Bus
    if not UDisks2.has_udisks2():
        MsgBox().error("UDisks2 was not found!")
        sys.exit(1)


def main() -> int:
    """Start application."""
    check_deps()

    # Application settings (suppress some warnings)
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = Application(sys.argv)
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
