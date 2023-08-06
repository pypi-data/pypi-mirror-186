from uxdconverter.raw.header.structure import AbstractStructure
from uxdconverter.raw.header.supplementary import Supplementaries

class RangeHeader(AbstractStructure):

    LENGTH = 304

    SCAN_MODE_CONTINOUS = 1
    SCAN_MODE_STEP = 0

    MEASUREMENT_LOCKED_COUPLED = 0
    MEASUREMENT_UNLOCKED_COUPLED = 1
    MEASUREMENT_DETECTOR_SCAN = 2
    MEASUREMENT_ROCKING_CURVE = 3
    MEASUREMENT_CHI_SCAN = 4
    MEASUREMENT_PHI_SCAN = 5
    MEASUREMENT_X_SCAN = 6
    MEASUREMENT_Y_SCAN = 7
    MEASUREMENT_Z_SCAN = 8
    MEASUREMENT_AUX1_SCAN = 9
    MEASUREMENT_AUX2_SCAN = 10
    MEASUREMENT_AUX3_SCAN = 11
    MEASUREMENT_PSI_SCAN = 12
    MEASUREMENT_HKL_SCAN = 13
    MEASUREMENT_PSD_FIXED_SCAN = 129
    MEASUREMENT_PSD_FAST_SCAN = 130

    def __init__(self, raw_data):

        super(RangeHeader, self).__init__(raw_data)

        if not len(raw_data) == self.LENGTH:
            raise RuntimeError("Given input must be exactly 304 bytes long")

        self._supplementaries = None

    def can_read(self):
        return self.get_integer(0) == self.LENGTH

    def get_number_of_data_records(self):
        return self.get_integer(4)

    def get_start_theta(self):
        return self.get_double(8)

    def get_start_two_theta(self):
        return self.get_double(16)

    def get_start_chi(self):
        return self.get_double(24)

    def get_start_phi(self):
        return self.get_double(32)

    def get_start_x(self):
        return self.get_double(40)

    def get_start_y(self):
        return self.get_double(48)

    def get_start_z(self):
        return self.get_double(56)

    def get_scan_mode(self):
        return self.get_integer(168)

    def get_step_size(self):
        return self.get_double(176)

    def get_step_time(self):
        return self.get_float(192)

    def get_measurement_mode(self):
        return self.get_integer(196)

    def get_generator_kilovoltage(self):
        return self.get_integer(224)

    def get_generator_milliamps(self):
        return self.get_integer(228)

    def get_wavelength(self):
        return self.get_double(240)

    def get_data_length(self):
        return self.get_integer(252)

    def has_supplementary_headers(self):
        return self.get_supplementary_header_length() > 0

    def get_supplementary_header_length(self):
        return self.get_integer(256)

    def get_supplementaries(self):
        return self._supplementaries

    def set_supplementaries(self, suppls: Supplementaries):
        self._supplementaries = suppls

    def get_length(self):
        return self.LENGTH + self.get_supplementary_header_length()