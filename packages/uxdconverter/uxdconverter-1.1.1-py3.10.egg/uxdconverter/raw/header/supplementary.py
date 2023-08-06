from uxdconverter.raw.header.structure import AbstractStructure

class Supplementaries(object):
    def __init__(self):
        self._suppls = []

    def add_supplementary(self, header: 'SupplementaryHeader'):
        self._suppls.append(header)

    def get_number_of_supplementaries(self):
        return len(self._suppls)

    def get_length(self):
        return sum([suppl.get_length() for suppl in self._suppls])


class SupplementaryHeader(AbstractStructure):

    TYPE_OSCILLATIONS = 100
    TYPE_GONIOMETER = 110
    TYPE_QUANTITIVE_MEASUREMENT = 120
    TYPE_RANGE_COMMENT = 140
    TYPE_REMOVE_DATA = 150
    TYPE_TWO_THETA_OFFSET = 190
    TYPE_AD_PARAMETERS = 200

    def __init__(self, raw_data):

        super(SupplementaryHeader, self).__init__(raw_data)
        self._raw = self._raw[0:self.get_length()]

    def can_read(self):
        return True

    def get_type(self):
        return self.get_integer(0)

    def get_length(self):
        return self.get_integer(4)