# -*- coding: utf-8 -*-
"""
udisks2.

https://lazka.github.io/pgi-docs/UDisks-2.0/

https://lazka.github.io/pgi-docs/UDisks-2.0/classes/Client.html
-> get_object_manager()

https://lazka.github.io/pgi-docs/Gio-2.0/classes/DBusObjectManager.html
-> get_objects()
-> get_object(object_path)
-> get_object_path()
-> get_interface(object_path, interface_name)

interface-added 	Emitted when interface is added to object.
interface-removed 	Emitted when interface has been removed from object.
object-added        Emitted when object is added to manager.
object-removed      Emitted when object is removed from manager.

https://lazka.github.io/pgi-docs/Gio-2.0/classes/DBusObject.html
-> get_interface(interface_name)
-> get_interfaces()
-> get_object_path()

interface-added 	Emitted when interface is added to object.
interface-removed 	Emitted when interface is removed from object.

https://lazka.github.io/pgi-docs/UDisks-2.0/interfaces.html
"""

import os
import sys
from typing import Union, Any

from .msgbox import MsgBox

import gi
gi.require_version('Gio', '2.0')

try:
    gi.require_version('UDisks', '2.0')
except ValueError:
    message = \
    """
    Missing:
        GObject based library to access udisks2 - introspection data.

    Install:
        'gir1.2-udisks-2.0' for debian based linux.
        'typelib-1_0-UDisks-2_0' for openSUSE linux.
    """
    MsgBox().error(message)
    sys.exit(1)

from gi.repository import Gio, UDisks, GLib


_conv_object_path_types = {
    "drives": "/org/freedesktop/UDisks2/drives/",
    "block_devices": "/org/freedesktop/UDisks2/block_devices/",
    "mdraid": "/org/freedesktop/UDisks2/mdraid/",
    "iscsi/session": "/org/freedesktop/UDisks2/iscsi/session/",
    "jobs": "/org/freedesktop/UDisks2/jobs/",
    }

_conv_interface_names = {
    "Manager": "org.freedesktop.UDisks2.Manager",

    "Drive": "org.freedesktop.UDisks2.Drive",
    "Drive.Ata": "org.freedesktop.UDisks2.Drive.Ata",

    "Block": "org.freedesktop.UDisks2.Block",
    "Partition": "org.freedesktop.UDisks2.Partition",
    "PartitionTable": "org.freedesktop.UDisks2.PartitionTable",
    "Filesystem": "org.freedesktop.UDisks2.Filesystem",
    "Encrypted": "org.freedesktop.UDisks2.Encrypted",
    "Loop": "org.freedesktop.UDisks2.Loop",

    "LogicalVolume": "org.freedesktop.UDisks2.LogicalVolume",
    }


class UDisks2:
    """UDisks2 interface."""

    preset_args = \
        {
            'unmount':
                GLib.Variant('a{sv}', {'force': GLib.Variant('b', False)}),
            'lock':
                GLib.Variant('a{sv}',
                             {'auth.no_user_interaction': GLib.Variant(
                                 'b', True)}),
            'open_device_restore':
                GLib.Variant('a{sv}',
                             {'flags': GLib.Variant(
                                 'i', os.O_EXCL | os.O_CLOEXEC | os.O_SYNC)}),
            'open_for_restore':
                GLib.Variant('a{sv}',
                             {'flags': GLib.Variant(
                                 'i', os.O_WRONLY | os.O_SYNC)}),
            }

    def __init__(self):
        self.__client = None
        self.__object_manager = None
        self.version = None

        self.__init()

    def __init(self):
        self.__client = UDisks.Client.new_sync(None)
        self.__object_manager = self.__client.get_object_manager()
        self.version = self.__get_udisks2_version()

    def __get_udisks2_version(self) -> int:
        version = -1

        manager = self.__client.get_manager()
        if manager:
            string = manager.get_property('version').replace('.', '')
            version = int(string)

        return version

    def settle(self):
        """
        Blocks until all pending D-Bus messages have been delivered.

        Also emits the (rate-limited) UDisks.Client ::changed signal
        if changes are currently pending.

        This is useful in two situations: 1. when using synchronous
        method calls since e.g. D-Bus signals received while waiting
        for the reply are queued up and dispatched after the synchronous
        call ends;

        and when using asynchronous calls where the return value references
        a newly created object (such as the Manager.LoopSetup() method).

        Returns
        -------
        None.

        """
        self.__client.settle()

    def signal_connect_obj_added(self, callback_func: Any) -> int:
        handler_id = \
            self.__object_manager.connect("object-added", callback_func)
        return handler_id

    def signal_connect_obj_removed(self, callback_func: Any) -> int:
        handler_id = \
            self.__object_manager.connect("object-removed", callback_func)
        return handler_id

    def signal_handler_block(self, handler_id) -> None:
        self.__object_manager.handler_block(handler_id)

    def signal_handler_unblock(self, handler_id) -> None:
        self.__object_manager.handler_unblock(handler_id)

    def signal_handler_disconnect(self, handler_id) -> None:
        self.__object_manager.handler_disconnect(handler_id)

    @staticmethod
    def has_udisks2() -> bool:
        return bool(UDisks.Client.new_sync(None))

    def get_block_for_drive(self,
                            object_path_drive: str,
                            get_physical: bool) -> Union[UDisks.Block, None]:
        interface_block = None
        object_drive = self.__object_manager.get_object(object_path_drive)

        interface_name = "org.freedesktop.UDisks2.Drive"
        interface_drive = \
            self.__object_manager.get_interface(object_path_drive,
                                                interface_name)
        if object_drive:
            interface_block = \
                self.__client.get_block_for_drive(interface_drive,
                                                  get_physical)
        return interface_block

    def get_object(self, object_path: str) -> Union[Gio.DBusObject, None]:
        dbus_object = self.__object_manager.get_object(object_path)
        return dbus_object

    def get_objects(self, object_type: str = None) -> list[Gio.DBusObject]:
        objects = []

        objects_all = self.__object_manager.get_objects()

        if object_type:
            if object_type in _conv_object_path_types:
                string = _conv_object_path_types[object_type]
            else:
                valid_pathtypes = tuple(_conv_object_path_types)
                error_message = \
                    f"Valid object_type arguments are {valid_pathtypes}."
                raise ValueError(error_message)
        else:
            string = ""

        for object_ in objects_all:
            object_path = object_.get_object_path()
            if object_path.startswith(string):
                objects.append(object_)

        return objects

    def get_object_pathes(self, object_type: str = None) -> list[str]:
        object_pathes = []

        objects = self.get_objects(object_type)
        if objects:
            object_pathes = sorted([obj.get_object_path()
                                    for obj in objects])
        return object_pathes

    def get_object_pathes_whole_block_device(self):
        object_pathes_whole_disk = []

        object_pathes = self.get_object_pathes("drives")
        for object_path in object_pathes:
            interface = \
                self.get_block_for_drive(object_path, get_physical=True)
            if interface:
                object_pathes_whole_disk.append(interface.get_object_path())
        object_pathes_whole_disk.sort()

        return object_pathes_whole_disk

    def get_interface(self,
                      object_path: str,
                      interface_name: str) -> Union[Gio.DBusInterface, None]:
        """
        Get the interface proxy for interface_name at object_path, if Any.

        Parameters
        ----------
        object_path : str
            Object path to look up.
        interface_name : str
            D-Bus interface name to look up.

        Returns
        -------
        interface : Union[Gio.DBusInterface, None]
            A Gio.DBusInterface instance or None.

        """
        interface_name = self.__validate_interface_name(interface_name)

        interface = \
            self.__object_manager.get_interface(object_path, interface_name)
        return interface

    def get_interface_names(self, object_path: str) -> list:
        interface_names = []

        dbus_object = self.__object_manager.get_object(object_path)
        if dbus_object:
            interfaces = dbus_object.get_interfaces()
            interface_names = [interface.get_interface_name()
                               for interface in interfaces]
        return interface_names

    def get_property(self,
                     object_path: str,
                     interface_name: str,
                     property_name: str) -> Union[Any, None]:

        property_value = None
        interface_name = self.__validate_interface_name(interface_name)

        interface = \
            self.__object_manager.get_interface(object_path, interface_name)
        property_value = interface.get_property(property_name)
        if isinstance(property_value, GLib.Variant):
            property_value = property_value.unpack()

        return property_value

    @staticmethod
    def __validate_interface_name(interface_name: str) -> str:
        if interface_name:
            if interface_name in _conv_interface_names:
                interface_name = _conv_interface_names[interface_name]
            elif interface_name not in _conv_interface_names.values():
                raise ValueError(
                    "Unknown value for argument 'interface_name'.")
        return interface_name

    def get_partition_pathes(self, object_path: str) -> list[str]:
        partition_pathes = []

        interface_ptable = "org.freedesktop.UDisks2.PartitionTable"
        interface_partition = "org.freedesktop.UDisks2.Partition"

        interface = self.__object_manager.get_interface(object_path,
                                                        interface_ptable)
        if interface:
            partition_pathes = interface.get_property("partitions")
        else:
            interface = \
                self.__object_manager.get_interface(object_path,
                                                    interface_partition)
            if interface:
                object_path = interface.get_property("table")
                interface = \
                    self.__object_manager.get_interface(object_path,
                                                        interface_ptable)
                if interface:
                    partition_pathes = interface.get_property("partitions")

        return partition_pathes

    def __get_interface_filesystem(
            self, object_path: str) -> Union[UDisks.Filesystem, None]:
        interface_filesystem = None

        interface_name = "org.freedesktop.UDisks2.Encrypted"
        interface_encrypted = \
            self.__object_manager.get_interface(object_path, interface_name)
        if interface_encrypted:
            cleartext_device = \
                interface_encrypted.get_property('cleartext-device')
            if cleartext_device != '/':
                object_path = cleartext_device

        interface_name = "org.freedesktop.UDisks2.Filesystem"
        interface_filesystem = \
            self.__object_manager.get_interface(object_path, interface_name)

        return interface_filesystem

    def is_mounted(self, object_path: str) -> bool:
        mounted = False

        interface_filesystem = self.__get_interface_filesystem(object_path)
        if interface_filesystem:
            mounted = bool(interface_filesystem.get_property("mount-points"))
        return mounted

    def is_filesystem_mounted(self,
                              interface_filesystem: UDisks.Filesystem) -> bool:
        mounted = False

        if interface_filesystem:
            object_path = interface_filesystem.get_object_path()
            mounted = self.is_mounted(object_path)
        return mounted

    def get_mounted_filesystems(self,
                                object_path: str) -> list[UDisks.Filesystem]:
        mounted_filesystems = []

        partitions = self.get_partition_pathes(object_path)
        if partitions:
            for path in partitions:
                interface_filesystem = self.__get_interface_filesystem(path)
                if interface_filesystem:
                    mounted = \
                        bool(interface_filesystem.get_property("mount-points"))
                    if mounted:
                        mounted_filesystems.append(interface_filesystem)

        return mounted_filesystems

    def __get_interface_encrypted(
            self, object_path: str) -> Union[UDisks.Encrypted, None]:
        interface_encrypted = None

        interface_name = "org.freedesktop.UDisks2.Block"
        interface_block = self.__object_manager.get_interface(object_path,
                                                              interface_name)
        if interface_block:
            crypto_backing_device = \
                interface_block.get_property('crypto_backing_device')
            if crypto_backing_device != '/':
                object_path = crypto_backing_device

        interface_name = "org.freedesktop.UDisks2.Encrypted"
        interface_encrypted = \
            self.__object_manager.get_interface(object_path, interface_name)

        return interface_encrypted

    def is_locked(self, object_path: str) -> bool:
        locked = True

        interface_name = "org.freedesktop.UDisks2.Block"
        interface_block = self.__object_manager.get_interface(object_path,
                                                              interface_name)
        if interface_block:
            cleartext_block = \
                self.__client.get_cleartext_block(interface_block)
            if cleartext_block:
                interface_block = cleartext_block

            crypto_backing_device = \
                interface_block.get_property('crypto_backing_device')
            if crypto_backing_device != '/':
                locked = False

        return locked

    def get_unlocked_encrypted(
            self, object_path: str) -> Union[UDisks.Encrypted, None]:
        unlocked_encrypted = None

        locked = self.is_locked(object_path)
        if not locked:
            unlocked_encrypted = self.__get_interface_encrypted(object_path)

        return unlocked_encrypted
