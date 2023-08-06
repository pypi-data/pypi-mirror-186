# -*- coding: utf-8 -*-
"""FileSize class."""

from typing import Union, NamedTuple


class FileSize:
    """Data type for file sizes with value and unit."""

    __slots__ = ('_value', '_unit')

    Multiples = {
        'Byt': 1,
        'KiB': 1024,
        'MiB': 1024 ** 2,
        'GiB': 1024 ** 3,
        'TiB': 1024 ** 4,
        'PiB': 1024 ** 5,
        'EiB': 1024 ** 6,
        'ZiB': 1024 ** 7,
        'YiB': 1024 ** 8,
        }

    def __init__(self,
                 size: Union[int, float],
                 unit: str = 'Byt'):

        if not FileSize.Multiples.get(unit):
            raise ValueError(f"Unknown value '{unit}' for parameter 'unit'")

        if unit == 'Byt':
            if size % 1:
                raise ValueError(
                    "Parameter 'size' must be a multiple of 1 Byte")

        if not size % 1:
            size = int(size)

        self._value = size
        self._unit = unit

        # Parameter 'size' must not be less than 1 byte
        if size * FileSize.Multiples.get(unit) < 1:
            print("Parameter 'size' must not be less than 1 byte.")
            self._value = None

    @property
    def value(self) -> Union[int, float]:
        """Get filesize value."""
        return self._value

    @property
    def unit(self) -> str:
        """Get filesize unit."""
        return self._unit

    @property
    def namedtuple(self) -> NamedTuple:
        """Get filesize as named tuple."""
        nt = NamedTuple('filesize', [('size', Union[int, float]),
                                     ('unit', str)])
        return nt(self._value, self._unit)

    def __str__(self):
        if self._value is None:
            return ""

        return f"{self._value} {self._unit}"

    def __iter__(self):
        for item in (self._value, self._unit):
            yield item

    # Arithmetic operators
    def __add__(self, other):
        if isinstance(other, FileSize):
            result = self._value * FileSize.Multiples.get(self._unit)
            result += other._value * FileSize.Multiples.get(other._unit)
            return FileSize(size=result, unit='Byt')
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, FileSize):
            result = self._value * FileSize.Multiples.get(self._unit)
            result -= other._value * FileSize.Multiples.get(other._unit)
            return FileSize(size=result, unit='Byt')
        return NotImplemented

    def __mul__(self, other: Union[int, float]):
        if isinstance(other, (int, float)):
            result = self._value * other
            return FileSize(size=result, unit=self._unit)
        return NotImplemented

    def __rmul__(self, other: Union[int, float]):
        if isinstance(other, (int, float)):
            result = self._value * other
            return FileSize(size=result, unit=self._unit)
        return NotImplemented

    def __truediv__(self, other: Union[int, float]):
        if isinstance(other, (int, float)):
            result = self._value / other
            return FileSize(size=result, unit=self._unit)
        return NotImplemented

    def __pow__(self, other: Union[int, float]):
        if isinstance(other, (int, float)):
            result = self._value ** other
            return FileSize(size=result, unit=self._unit)
        return NotImplemented

    # Comparison operators
    def __eq__(self, other):
        if isinstance(other, FileSize):
            return self._value == other._value
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, FileSize):
            return self._value != other._value
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, FileSize):
            return self._value < other._value
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, FileSize):
            return self._value <= other._value
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, FileSize):
            return self._value > other._value
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, FileSize):
            return self._value >= other._value
        return NotImplemented

    # Custom methods
    def convert(self, unit: str = 'auto', max_decimals: int = -1):
        r"""
        Convert FileSize unit to another FileSize unit.

        Parameters
        ----------
        unit : str, optional
            New unit to convert to. Valid parameters are: \n
            ['auto', 'Byt', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'] \n
            The default is 'auto'.
        max_decimals : int, optional
            max_decimals == -1; No changes of result\n
            max_decimals == 0; No decimals in result\n
            max_decimals > 0; Rounded result to given maximum decimals\n
            The default is -1.

        Raises
        ------
        ValueError
            Invalid value for parameter 'unit'.

        Returns
        -------
        FileSize
            A new instance of FileSize.

        """
        value = self._value * FileSize.Multiples.get(self._unit)

        if unit == 'auto':
            if value < FileSize.Multiples.get('KiB'):
                size = value
                unit = 'Byt'
            elif value < FileSize.Multiples.get('MiB'):
                size = value / FileSize.Multiples.get('KiB')
                unit = 'KiB'
            elif value < FileSize.Multiples.get('GiB'):
                size = value / FileSize.Multiples.get('MiB')
                unit = 'MiB'
            elif value < FileSize.Multiples.get('TiB'):
                size = value / FileSize.Multiples.get('GiB')
                unit = 'GiB'
            elif value < FileSize.Multiples.get('PiB'):
                size = value / FileSize.Multiples.get('TiB')
                unit = 'TiB'
            elif value < FileSize.Multiples.get('EiB'):
                size = value / FileSize.Multiples.get('PiB')
                unit = 'PiB'
            elif value < FileSize.Multiples.get('ZiB'):
                size = value / FileSize.Multiples.get('EiB')
                unit = 'EiB'
            elif value < FileSize.Multiples.get('YiB'):
                size = value / FileSize.Multiples.get('ZiB')
                unit = 'ZiB'
            else:
                size = value / FileSize.Multiples.get('YiB')
                unit = 'YiB'
        elif FileSize.Multiples.get(unit):
            size = value / FileSize.Multiples.get(unit)
        else:
            raise ValueError("Invalid value for parameter 'unit'")

        if max_decimals == 0:
            # No decimals
            size = round(size)
        if max_decimals > 0:
            size = round(size, max_decimals)

        return FileSize(size, unit)
