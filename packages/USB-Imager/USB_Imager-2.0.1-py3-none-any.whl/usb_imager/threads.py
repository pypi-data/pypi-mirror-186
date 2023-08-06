# -*- coding: utf-8 -*-
"""Threading."""

import os
from pathlib import Path
from typing import Union

from gi.repository import GLib, Gio
from PySide6 import QtCore
from PySide6.QtCore import QObject, QThread, Slot


MIB = 1024 * 1024


class Signals(QObject):
    """QtCore.Signal."""

    # Application
    cancel_thread = QtCore.Signal()

    # WritingThread
    progressbar_value = QtCore.Signal(int)
    statusbar_message = QtCore.Signal(str)
    result = QtCore.Signal(object)


class WritingThread(QThread):
    """Writing class."""

    def __init__(self,
                 in_file: Path,
                 out_object_path: str,
                 application,
                 blksize: int = MIB):
        super().__init__()

        self.__in_file = in_file
        self.__object_path = out_object_path
        self.__blksize = blksize
        self.__application = application
        self.__udisks2 = application.udisks2

        self.signal = Signals()

        self.__cancel_thread = False

        # SLOTS
        self.__application.signal.cancel_thread.connect(self.cancel)

    @Slot()
    def cancel(self):
        """Cancel thread."""
        self.__cancel_thread = True

    def run(self):
        """Run thread."""
        file_decriptors = self.__get_file_descriptors()
        if not file_decriptors:
            return
        in_fd, out_fd = file_decriptors

        filesize = os.path.getsize(self.__in_file)
        written = 0
        progress_value = 0

        try:
            self.signal.statusbar_message.emit("Writing ...")
            while written < filesize:
                if self.__cancel_thread is True:
                    break

                written += os.sendfile(out_fd, in_fd,
                                       offset=None, count=self.__blksize)
                written_percent = int(written * 100 / filesize)
                if written_percent != progress_value:
                    progress_value = written_percent
                    if progress_value > 99:
                        break
                    self.signal.progressbar_value.emit(progress_value)
        except OSError:
            # Here is not always thrown an exception.
            # (e.g. when removing a USB stick while writing).
            self.__close_all_fd(file_decriptors)
            message = "Error while writing ... Writing canceled."
            self.signal.statusbar_message.emit(message)
        else:
            self.__close_all_fd(file_decriptors)
            if self.__cancel_thread is True:
                self.signal.statusbar_message.emit("Writing canceled.")
            else:
                self.signal.progressbar_value.emit(100)
                self.signal.statusbar_message.emit("Writing finished.")

    def __get_file_descriptors(self) -> tuple:
        file_decriptors = ()

        in_fd = self.__get_fd_image(self.__in_file)
        if in_fd != -1:
            out_fd = self.__get_fd_device(self.__object_path)
            if not out_fd:
                self.__close_all_fd((in_fd,))

        file_decriptors = (in_fd, out_fd)

        return file_decriptors

    def __get_fd_image(self, file: Path) -> int:
        file_fd = -1

        try:
            file_fd = os.open(file, os.O_RDONLY)
        except OSError as error:
            self.signal.statusbar_message.emit(error.args)

        return file_fd

    def __get_fd_device(self, object_path: str) -> Union[int, None]:
        file_fd = None

        interface_block = \
            self.__udisks2.get_interface(object_path, 'Block')

        if not interface_block:
            return None

        try:
            if self.__is_valid_version(min_version=273):
                arg_options = self.__udisks2.preset_args['open_device_restore']
                result = \
                    interface_block.call_open_device_sync('w',
                                                          arg_options,
                                                          Gio.UnixFDList(),
                                                          None)
            else:
                # Deprecated
                arg_options = self.__udisks2.preset_args['open_for_restore']
                result = \
                    interface_block.call_open_for_restore_sync(
                        arg_options,
                        Gio.UnixFDList(),
                        None)
        except GLib.Error as error:
            self.signal.statusbar_message.emit(error.message)
            return file_fd
        else:
            if result:
                out_fd, out_fd_list = result
                file_fd = out_fd_list.get(out_fd.unpack())
            self.__udisks2.settle()

        return file_fd

    def __close_all_fd(self, file_decriptors: tuple) -> bool:
        all_fd_closed = False

        try:
            for file_fd in file_decriptors:
                os.close(file_fd)
        except OSError as error:
            self.signal.statusbar_message.emit(error.args)
        else:
            all_fd_closed = True

        return all_fd_closed

    def __is_valid_version(self, min_version: int) -> bool:
        valid_version = False

        udisks2_version = self.__udisks2.version
        if min_version <= udisks2_version:
            valid_version = True

        return valid_version
