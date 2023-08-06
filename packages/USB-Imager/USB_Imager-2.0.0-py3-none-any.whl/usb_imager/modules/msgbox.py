# -*- coding: utf-8 -*-
"""MessageBox wrapper."""

import os
import sys


DETECTED_GTK = []


# GTK
try:
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk
    DETECTED_GTK.append('gi')
except ImportError:
    pass

# QT -> PyQt
try:
    from PyQt6.QtWidgets import QApplication, QMessageBox
    DETECTED_GTK.append('pyqt')
except ImportError:
    try:
        from PyQt6.QtWidgets import QApplication, QMessageBox
        DETECTED_GTK.append('pyqt')
    except ImportError:
        pass

# QT -> PySide
try:
    from PySide6.QtWidgets import QApplication, QMessageBox
    DETECTED_GTK.append('pyside')
except ImportError:
    try:
        from PySide6.QtWidgets import QApplication, QMessageBox
        DETECTED_GTK.append('pyside')
    except ImportError:
        pass

# TkInter
try:
    from tkinter import Tk, messagebox
    DETECTED_GTK.append('tkinter')
except ImportError:
    pass

# wxPython
try:
    import wx
    DETECTED_GTK.append('wxpython')
except ImportError:
    pass


class MsgBox:
    """
    Print GUI-Messages before an application is started.

    MessageBox wrapper supports:

        GTK >= 3
        PyQt >=6
        PySide >= 6
        TkInter
        wxPython

    """

    Supported_gtk = ['gi', 'pyqt', 'pyside', 'tkinter', 'wxpython']

    def __init__(self, gtk_name: str = None):

        if gtk_name:
            if gtk_name in self.Supported_gtk:
                self.__gtk_type = gtk_name
            else:
                raise ValueError(
                    f"Valid values are {self.Supported_gtk}.")
        else:
            if DETECTED_GTK:
                self.__gtk_type = DETECTED_GTK[0]

    def information(self, message: str) -> None:
        """Information message."""
        self.__caller("Information", message)

    def warning(self, message: str) -> None:
        """Warning message."""
        self.__caller("Warning", message)

    def error(self, message: str) -> None:
        """Error message."""
        self.__caller("Error", message)

    def __caller(self, title: str, message: str) -> None:

        desktop = bool(os.getenv('DESKTOP_SESSION'))

        if desktop:
            if self.__gtk_type == 'gi':
                self.__gi(title, message)
            elif self.__gtk_type == 'pyqt' or self.__gtk_type == 'pyside':
                self.__qt(title, message)
            elif self.__gtk_type == 'tkinter':
                self.__tk(title, message)
            elif self.__gtk_type == 'wxpython':
                self.__wx(title, message)
            else:
                self.__cli(title, message)

    @staticmethod
    def __gi(title: str, message: str) -> None:

        # BUG -> No icons are displayed in the dialog box.

        if title == "Warning":
            msg_type = Gtk.MessageType.WARNING
        elif title == "Error":
            msg_type = Gtk.MessageType.ERROR
        else:
            msg_type = Gtk.MessageType.INFO

        dialog = Gtk.MessageDialog(
            title=title,
            message_type=msg_type,
            buttons=Gtk.ButtonsType.OK,
            text=message
            )

        dialog.run()
        dialog.destroy()

        # This is necessary to remove the dialog from the screen
        # after destroying it. (Standalone messagebox)
        while Gtk.events_pending():
            Gtk.main_iteration()

    @staticmethod
    def __qt(title: str, message: str) -> None:

        if QApplication.instance() is None:
            app = QApplication(sys.argv)

        if title == "Warning":
            QMessageBox.warning(None, title, message)
        elif title == "Error":
            QMessageBox.critical(None, title, message)
        else:
            QMessageBox.information(None, title, message)

    @staticmethod
    def __tk(title: str, message: str) -> None:

        root = Tk()
        root.withdraw()

        if title == "Warning":
            messagebox.showwarning(title, message)
        elif title == "Error":
            messagebox.showerror(title, message)
        else:
            messagebox.showinfo(title, message)

        root.destroy()

    @staticmethod
    def __wx(title: str, message: str) -> None:

        # BUG -> No icons are displayed in the dialog box.

        if title == "Warning":
            icon = wx.ICON_WARNING
        elif title == "Error":
            icon = wx.ICON_ERROR
        else:
            icon = wx.ICON_INFORMATION

        if wx.App.Get() is None:
            app = wx.App()

        wx.MessageBox(message, caption=title, style=icon | wx.CENTRE | wx.OK)

        # This is necessary to remove the dialog from the screen
        # after destroying it. (Standalone messagebox)
        frame = wx.Frame(None)
        frame.Destroy()

    @staticmethod
    def __cli(title: str, message: str) -> None:

        if title == "Error":
            print(f"{title}: {message}", file=sys.stderr)
        else:
            print(f"{title}: {message}")


# Testing
if __name__ == "__main__":
    msgbox = MsgBox('tkinter')
    msgbox.error(message="Programm only supports Unix!")
