from uxdconverter.raw.header.range import RangeHeader
from uxdconverter.raw.header.file import FileHeader
from uxdconverter.raw.data import DataSet
from typing import List


class MeasurementRange(object):

    def __init__(self, header: RangeHeader, data: DataSet):
        self._header = header
        self._data = data

    def get_length(self):
        return self._header.get_length() + self._data.get_length()

    def get_header(self):
        return self._header

    def get_data(self):
        return self._data


class Measurements(object):
    def __init__(self, header: FileHeader, measurements: List[MeasurementRange]):
        self._header = header
        self._mss = measurements

    def get_header(self):
        return self._header

    def get_measurements(self) -> List[MeasurementRange]:
        return self._mss


