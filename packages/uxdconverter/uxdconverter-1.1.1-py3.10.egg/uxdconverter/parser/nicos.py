from uxdconverter.parser.ndatautils.parser import DataPath, ASCIILoader, InstrumentLoader
from uxdconverter.measurement import Measurements, MeasurementContext, Measurement


class XrayDataPath(DataPath):
    def __init__(self, file):
        self.file = file

    def gen_path(self, fnum):
        return self.file


class NicosParser(object):
    def __init__(self, file_obj, logger):
        self._file = file_obj
        self._logger = logger

    def parse(self) -> Measurements:
        datapath = XrayDataPath(self._file)
        loader = ASCIILoader(datapath, InstrumentLoader())

        loader.read_out_data(0)
        rawdata = loader.datadict['rawdata']
        # d[3] is steptime
        # d[4] is counts
        data = [[d[0], 0.0, d[4], 0.0] for d in rawdata]
        return Measurements([], [Measurement([], data)], [], MeasurementContext())
