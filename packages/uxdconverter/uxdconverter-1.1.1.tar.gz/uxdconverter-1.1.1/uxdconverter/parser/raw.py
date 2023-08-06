from uxdconverter.raw.converter import MeasurementsConverter
from uxdconverter.raw.parser import RawParser
from uxdconverter.measurement import Measurements

class RawMeasurementsParser(object):
    def __init__(self, file, logger):
        self._file = file
        self._logger = logger
        self._converter = MeasurementsConverter()

    def parse(self) -> Measurements:
        try:
            f = open(self._file, "rb")
        except:
            raise RuntimeError("Could not open file %s" % self._file)

        return self._converter.convert(RawParser().parse(f.read()))