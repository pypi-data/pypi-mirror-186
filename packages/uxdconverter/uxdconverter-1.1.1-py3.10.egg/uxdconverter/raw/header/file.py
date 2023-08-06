from uxdconverter.raw.header.structure import AbstractStructure


class FileHeader(AbstractStructure):

    LENGTH = 712
    VERSION_RAW01 = 1

    UNITS_ANGSTROM = 0
    UNITS_NANOMETER = 1


    def __init__(self, raw_data):
        super(FileHeader, self).__init__(raw_data)
        if not len(raw_data) == self.LENGTH:
            raise RuntimeError("Given input must be exactly 712 bytes long")

    def get_length(self):
        return self.LENGTH

    def can_read(self):
        return self.get_string(0, 8) == 'RAW1.01'

    def get_version(self):
        return self.VERSION_RAW01

    def get_number_of_completed_data_ranges(self):
        return self.get_integer(12)

    def get_date(self):
        return self.get_string(16, 10)

    def get_time(self):
        return self.get_string(26, 10)

    def get_type_anode(self):
        return self.get_string(608, 4)

    def get_units_wavelength(self):
        if self.get_data(656, 4) == b'A\x00\x00\x00':
            return self.UNITS_ANGSTROM
        else:
            return self.UNITS_NANOMETER

    def get_average_wavelength(self):
        return self.get_double(616)

    def get_total_measurement_time(self):
        return self.get_float(664)
