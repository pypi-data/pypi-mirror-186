# -*- coding: utf-8 -*-
"""@author: Skynet-Devel."""

import os
import sys
import re
from pathlib import Path
import importlib.resources
# from typing import Any, Optional

from gi.repository import GLib
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt, QMetaObject, Slot
from PySide6.QtWidgets import (
    QApplication, QWidget,
    QMainWindow, QMenu,
    QFileDialog, QMessageBox, QLabel,
)

from usb_imager.appinfo import (
    APP_NAME, APP_VERSION, APP_ORGANISATION, APP_ID, APP_TITLE, APP_ABOUT,
)
from usb_imager.device_item import DeviceItem
from usb_imager.modules.udisks2 import UDisks2
from usb_imager.modules.filesize import FileSize
from usb_imager.threads import Signals, WritingThread


STATUSBAR_TIMEOUT = 5000


class Application(QApplication):
    """Application."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setup_application()
        self.mainwindow = MainWindow()
        self.mainwindow.show()

    def setup_application(self) -> None:
        """Application setup."""
        self.setApplicationName(APP_NAME)
        self.setApplicationVersion(APP_VERSION)
        self.setOrganizationName(APP_ORGANISATION)
        self.setOrganizationDomain(APP_ID)

        path = importlib.resources.files('usb_imager.resources')
        icon = QIcon(str(path) + '/' + 'usb-imager.ico')
        self.setWindowIcon(icon)


class MainWindow(QMainWindow):
    """MainWidget."""

    def __init__(self):
        super().__init__()

        self.setup_mainwindow()

        self.signal = Signals()
        self.copythread = None
        # blksize is stored in comboBox_buffers data.

        self.udisks2 = UDisks2()
        self.udisks2.signal_connect_obj_added(self.callback_object_added)
        self.udisks2.signal_connect_obj_removed(self.callback_object_removed)

        self.srcpath = None
        # Target path is stored in comboBox_devices data.

        self.init_target_devices()

    def ui_loader(self, ui_filename: str) -> QWidget:
        """Load user interface from ui-file."""
        loader = QUiLoader()
        path = importlib.resources.files('usb_imager.resources')
        widget = loader.load(path / ui_filename, self)
        if not widget:
            sys.exit(loader.errorString())
        return widget

    def setup_mainwindow(self) -> None:
        """Mainwindow setup."""
        self.setObjectName('MainWindow')
        self.setWindowTitle(APP_TITLE)
        self.setMinimumWidth(475)

        self.add_menubar()
        self.add_statusbar()

        self.ui = self.ui_loader('usb-imager-widget.ui')  # centralwidget
        QMetaObject.connectSlotsByName(self)

    def add_menubar(self) -> None:
        """Add and configure menubar for MainWindow."""
        self.menubar = self.menuBar()  # Create and set menubar
        self.menubar.setObjectName('menubar')
        self.menubar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.menu_info = QMenu(self.tr('Info'), self.menubar)
        self.menu_info.setObjectName('menuInfo')
        self.menubar.addMenu(self.menu_info)

        self.action_about = QAction(self.tr('About'), self)
        self.action_about.setObjectName('actionAbout')
        self.action_about_qt = QAction(self.tr('AboutQt'), self)
        self.action_about_qt.setObjectName('actionAboutQt')

        self.menu_info.addAction(self.action_about)
        self.menu_info.addAction(self.action_about_qt)

    def add_statusbar(self) -> None:
        """Add and configure statusbar for MainWindow."""
        self.statusbar = self.statusBar()  # Create and set statusbar
        self.statusbar.setObjectName('statusbar')

        label = QLabel('v' + APP_VERSION)
        self.statusbar.addPermanentWidget(label)

    def init_target_devices(self) -> None:
        block_device_pathes = self.udisks2.get_object_pathes('block_devices')

        for object_path in block_device_pathes:
            if self.is_usb_key(object_path):
                self.add_device_item(object_path)

        sizes = [512, 1024, 2048, 4096, 8192, 16384, 32768, 1024 ** 2]
        for blksize in sizes:
            filesize = str(FileSize(blksize).convert())
            self.ui.comboBox_buffers.addItem(filesize, blksize)

        pos_last = self.ui.comboBox_buffers.count() - 1
        self.ui.comboBox_buffers.setCurrentIndex(pos_last)

    def callback_object_added(self, sender, dbus_object):
        object_path = dbus_object.get_object_path()

        if self.is_usb_key(object_path):
            device_name = self.add_device_item(object_path)
            if device_name:
                self.statusbar.showMessage(f"USB-Device added:  {device_name}",
                                           STATUSBAR_TIMEOUT)

    def callback_object_removed(self, sender, dbus_object):
        object_path = dbus_object.get_object_path()

        device_name = self.remove_device_item(object_path)
        current_msg = self.statusbar.currentMessage()
        if device_name and not current_msg.startswith("Error"):
            self.statusbar.showMessage(f"USB-Device removed:  {device_name}",
                                       STATUSBAR_TIMEOUT)

    def add_device_item(self, object_path: str) -> str:
        device_name = ""

        device_item = DeviceItem()

        drive_path = \
            self.udisks2.get_property(object_path, 'Block', 'drive')

        # Set device_item attributes
        device_item.object_path = object_path
        device_path = self.udisks2.get_property(object_path, 'Block', 'device')
        device_item.path = Path(device_path)

        interface = self.udisks2.get_interface(drive_path, 'Drive')
        device_item.size, vendor, model = \
            interface.get_properties('size', 'vendor', 'model')

        if vendor:
            device_item.vendor = vendor
        if model:
            device_item.model = model

        # Add device_item to combobox
        size = FileSize(device_item.size).convert(max_decimals=1)
        combobox_text = "{} - {} {} - {}".format(
            device_item.path.name, device_item.vendor, device_item.model, size)
        self.ui.comboBox_devices.addItem(combobox_text, device_item)
        device_name = f"{device_item.vendor} {device_item.model}"

        return device_name

    def remove_device_item(self, object_path: str) -> str:
        device_name = ""

        index_count = self.ui.comboBox_devices.count()
        for index in range(index_count):
            device_item = self.ui.comboBox_devices.itemData(index)
            if not device_item:
                continue
            if object_path == device_item.object_path:
                device_name = f"{device_item.vendor} {device_item.model}"
                self.ui.comboBox_devices.removeItem(index)

        return device_name

    @Slot()
    def on_pushButton_open_clicked(self):
        homedir = Path.home() / 'Downloads'
        filters = ('Image Files (*.iso *.img *.raw *.bin *.dd)',)

        filename = QFileDialog.getOpenFileName(
            parent=self,
            caption="Open Image",
            dir=str(homedir),
            filter=';;'.join(filters)
            )[0]

        if filename:
            filename = Path(filename)
            if filename.match('*.iso') and not self.is_bootable_iso(filename):
                return
            self.srcpath = filename
            self.ui.label_srcpath.setText(self.srcpath.name)

    @Slot()
    def on_pushButton_write_clicked(self) -> None:
        if self.copythread and self.copythread.isRunning():
            return

        device_item = self.ui.comboBox_devices.currentData()

        # IS SOURCE IMAGE AND TARGET DEVICE SELECTED?
        if not self.srcpath:
            message = "Please select an image to use!"
            self.ui.statusbar.showMessage(message, STATUSBAR_TIMEOUT)
            return
        if not device_item:
            message = "Please select a device to use!"
            self.ui.statusbar.showMessage(message, STATUSBAR_TIMEOUT)
            return

        # IS THE TARGET DEVICE TOO SMALL FOR WRITING THE IMAGE?
        srcfile_size = os.path.getsize(self.srcpath)
        if srcfile_size > device_item.size:
            message = \
                "Error:  " \
                "The size of the device is too small to write the image."
            self.statusbar.showMessage(message, STATUSBAR_TIMEOUT)
            return

        # ARE ALL PARTITIONS OF THE TARGET DEVICE UNMOUNTED AND UNLOCKED?
        mounted_filesystem_interfaces = \
            self.udisks2.get_mounted_filesystems(device_item.object_path)

        if mounted_filesystem_interfaces:
            # Security question
            text = \
                "This device is mounted in the filesystem.\n\n" \
                "Would you like to unmount it?"
            result = QMessageBox.warning(self, "Warning", text,
                                         QMessageBox.Yes | QMessageBox.No)
            if result == QMessageBox.No:
                return

            for iface_fs in mounted_filesystem_interfaces:
                # Unmount device
                arg_options = self.udisks2.preset_args['unmount']
                try:
                    iface_fs.call_unmount_sync(arg_options)
                except GLib.Error as error:
                    self.statusbar.showMessage(error.message)
                    return

                self.udisks2.settle()

                # Lock device if unlocked
                object_path = iface_fs.get_object_path()
                unlocked_encrypted = \
                    self.udisks2.get_unlocked_encrypted(object_path)
                if unlocked_encrypted:
                    arg_options = self.udisks2.preset_args['lock']
                    try:
                        unlocked_encrypted.call_lock_sync(arg_options)
                    except GLib.Error as error:
                        self.statusbar.showMessage(error.message)
                        return

                    self.udisks2.settle()

        # SECURITY QUESTION BEFORE WRITING.
        text = \
            "The device will be completely overwritten " \
            "and data on it will be lost.\n\n" \
            "Do you want to continue the process?"

        result = QMessageBox.warning(self, "Warning", text,
                                     QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.No:
            return

        # START WRITING
        blksize = self.ui.comboBox_buffers.currentData()
        self.copythread = WritingThread(self.srcpath, device_item.object_path,
                                        self, blksize)
        self.start_writing()

    @Slot()
    def on_actionAboutQt_triggered(self) -> None:
        QMessageBox.aboutQt(self)

    @Slot()
    def on_actionAbout_triggered(self) -> None:
        QMessageBox.about(self, "About USB-Imager", APP_ABOUT)

    def is_bootable_iso(self, filepath: Path) -> bool:
        is_bootable = False

        try:
            with filepath.open(mode='rb') as file:
                file.seek(510)
                mbr_signature = file.read(2).hex()
        except OSError as error:
            self.statusbar.showMessage(error.args)
        else:
            if mbr_signature == '55aa':
                is_bootable = True
            else:
                message = "Selected ISO file is not bootable!"
                self.statusbar.showMessage(message, STATUSBAR_TIMEOUT)

        return is_bootable

    def is_usb_key(self, object_path: str) -> bool:
        is_usbdev = True

        whole_block_device_pathes = \
            self.udisks2.get_object_pathes_whole_block_device()
        interface = self.udisks2.get_interface(object_path, 'Block')
        if not interface:
            return False

        if object_path not in whole_block_device_pathes:
            is_usbdev = False
        elif re.search(r"[0-9]$", object_path):
            is_usbdev = False
        else:
            drive_path, device_path, size = \
                interface.get_properties('drive', 'device', 'size')

            if not drive_path or drive_path == '/':
                is_usbdev = False
            elif not device_path or device_path == '/':
                is_usbdev = False
            elif not size or size == 0:
                is_usbdev = False
            else:
                interface = self.udisks2.get_interface(drive_path, 'Drive')
                if not interface:
                    return False

                connection_bus, removable = \
                    interface.get_properties('connection-bus', 'removable')

                if removable is False or connection_bus != "usb":
                    is_usbdev = False

        return is_usbdev

    def start_writing(self):
        # SLOTS
        self.copythread.signal.progressbar_value.connect(
            self.ui.progressBar.setValue)
        self.copythread.signal.statusbar_message.connect(
            self.statusbar.showMessage)
        self.ui.pushButton_cancel.clicked.connect(
            self.signal.cancel_thread.emit)
        self.copythread.finished.connect(
            self.finished_writing)

        self.ui.pushButton_open.setEnabled(False)
        self.ui.comboBox_devices.setEnabled(False)
        self.ui.comboBox_buffers.setEnabled(False)
        self.ui.pushButton_write.setEnabled(False)
        self.statusbar.clearMessage()

        self.copythread.start()

    def finished_writing(self):
        self.copythread.wait()
        self.ui.pushButton_open.setEnabled(True)
        self.ui.comboBox_devices.setEnabled(True)
        self.ui.comboBox_buffers.setEnabled(True)
        self.ui.pushButton_write.setEnabled(True)
