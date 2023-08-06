import os

from uxdconverter.parser.uxd import MeasurementsParser
from uxdconverter.parser.simple import SimpleMeasurementsParser
from uxdconverter.parser.raw import RawMeasurementsParser
from uxdconverter.parser.nicos import NicosParser
from uxdconverter.parser.xrdml import XRDMLParser

from uxdconverter.measurement import Measurements

class GeneralParser(object):
    def __init__(self, logger):
        self._logger = logger

    def parse(self, file) -> Measurements:
        ext = os.path.splitext(file)[1]

        if ext.lower() == '.raw':
            return RawMeasurementsParser(file, self._logger).parse()
        elif ext.lower() == '.uxd':
            return MeasurementsParser(file, self._logger).parse()
        elif ext.lower() == '.dat':
            return NicosParser(file, self._logger).parse()
        elif ext.lower() == '.xrdml':
            return XRDMLParser(file, self._logger).parse()
        else:
            return SimpleMeasurementsParser(file, self._logger).parse()
