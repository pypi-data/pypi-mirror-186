
import codecs

from uxdconverter.raw.header.file import FileHeader
from uxdconverter.raw.header.range import RangeHeader
from uxdconverter.raw.header.supplementary import Supplementaries, SupplementaryHeader
from uxdconverter.raw.data import DataSet
from uxdconverter.raw.measurement import MeasurementRange, Measurements


class RawParser(object):
    def __init__(self):
        pass

    def parse_from_file(self, file):
        try:
            f = open(file, 'rb')

            return self.parse(f.read())
        except:
            raise RuntimeError("Could not open file %s" % file)

    def parse(self, byte_stream):
        return self._parse_measurements(byte_stream)

    def _parse_header(self, raw):
        return FileHeader(raw[0:FileHeader.LENGTH])

    def _parse_range(self, raw):
        return RangeHeader(raw[0:RangeHeader.LENGTH])

    def _parse_supplementary_headers(self, raw, range_header: RangeHeader):
        if range_header.has_supplementary_headers() is False:
            return Supplementaries()
        else:
            suppls = Supplementaries()

            raw_data = raw

            while len(raw_data) > 0 and suppls.get_length() < range_header.get_supplementary_header_length():
                suppl = SupplementaryHeader(raw)
                suppls.add_supplementary(suppl)
                raw_data = raw_data[suppl.get_length():]

            return suppls

    def _parse_data(self, raw, range_header: RangeHeader):
        return DataSet(raw[0: range_header.get_data_length() * range_header.get_number_of_data_records()])

    def _parse_measurement(self, raw):

        range = self._parse_range(raw)
        raw = raw[range.get_length():]
        suppls = self._parse_supplementary_headers(raw, range)
        range.set_supplementaries(suppls)
        raw = raw[suppls.get_length():]
        data = self._parse_data(raw, range)

        return MeasurementRange(range, data)

    def _parse_measurements(self, raw):
        file = self._parse_header(raw)
        raw = raw[file.get_length():]
        mss = []

        for i in range(0, file.get_number_of_completed_data_ranges()):
            ms = self._parse_measurement(raw)
            raw = raw[ms.get_length():]
            mss.append(ms)


        return Measurements(file, mss)
