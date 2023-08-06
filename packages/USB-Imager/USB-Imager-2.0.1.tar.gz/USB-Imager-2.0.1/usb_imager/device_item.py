# -*- coding: utf-8 -*-
"""@author: skynet-devel."""

from pathlib import Path


class DeviceItem:
    """DeviceItem."""

    def __init__(self):
        self.__object_path = ""
        self.__path = None
        self.__vendor = "[No Vendor]"
        self.__model = "[No Model]"
        self.__size = 0

    @property
    def object_path(self) -> str:
        """Getter."""
        return self.__object_path

    @object_path.setter
    def object_path(self, value: str) -> None:
        """Setter."""
        self.__object_path = value

    @property
    def path(self) -> Path:
        """Getter."""
        return self.__path

    @path.setter
    def path(self, value: str) -> Path:
        """Setter."""
        self.__path = value

    @property
    def vendor(self) -> str:
        """Getter."""
        return self.__vendor

    @vendor.setter
    def vendor(self, value: str) -> None:
        """Setter."""
        self.__vendor = value

    @property
    def model(self) -> str:
        """Getter."""
        return self.__model

    @model.setter
    def model(self, value: str) -> None:
        """Setter."""
        self.__model = value

    @property
    def size(self) -> int:
        """Getter."""
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        """Setter."""
        self.__size = value
