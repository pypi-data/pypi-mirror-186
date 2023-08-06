from uxdconverter.raw.header.structure import AbstractStructure


class DataSet(AbstractStructure):
    def __init__(self, raw_data):
        super(DataSet, self).__init__(raw_data)

    def get_length(self):
        return len(self._raw)

    def get_number_of_data_points(self):
        return int(self.get_length() / self.LENGTH_FLOAT)

    def get_data_points(self):
        return [self.get_float(self.LENGTH_FLOAT * addr) for addr in range(0, self.get_number_of_data_points())]
