from uxdconverter.measurement import Measurement, Measurements as UXDMeasurements, MeasurementContext
from uxdconverter.raw.measurement import MeasurementRange, Measurements
from uxdconverter.raw.parser import RawParser
from uxdconverter.raw.header.range import RangeHeader

import numpy as np

class MeasurementConverter(object):
    def __init__(self):
        pass

    def convert(self, measurement: MeasurementRange):
        stepsize = measurement.get_header().get_step_size()
        steptime = measurement.get_header().get_step_time()

        is_background = False
        theta_data = (np.array(range(0, measurement.get_header().get_number_of_data_records())) * stepsize) / 2.0

        psi = 0

        # convert to theta, currently it is 2 theta
        # 2Theta = 2 * Theta
        if measurement.get_header().get_measurement_mode() == RangeHeader.MEASUREMENT_LOCKED_COUPLED:
            offset = measurement.get_header().get_start_theta()
        # 2Theta != 2 * Theta, i.e. usually used for a background scan and Theta has an offset (typ. 0.15deg)
        # or for stress measurements using larger offsets
        elif measurement.get_header().get_measurement_mode() == RangeHeader.MEASUREMENT_UNLOCKED_COUPLED:
            is_background = True
            psi = measurement.get_header().get_start_theta() - measurement.get_header().get_start_two_theta() / 2.0
            if abs(psi) > 0.5:
                is_background = False
            offset = measurement.get_header().get_start_two_theta() / 2
        elif measurement.get_header().get_measurement_mode() == RangeHeader.MEASUREMENT_DETECTOR_SCAN:
            offset = measurement.get_header().get_start_two_theta() / 2
        elif measurement.get_header().get_measurement_mode() == RangeHeader.MEASUREMENT_ROCKING_CURVE:
            offset = measurement.get_header().get_start_theta()
        elif measurement.get_header().get_measurement_mode() == RangeHeader.MEASUREMENT_PHI_SCAN:
            offset = measurement.get_header().get_start_phi()
        else:
            raise RuntimeError("Unknown measurement mode")

        #print(measurement.get_header().get_start_chi())

        if measurement.get_header().get_measurement_mode() == RangeHeader.MEASUREMENT_ROCKING_CURVE:
            data_x = 2 * theta_data + offset # we multiply by two since the division at the start was already wrong...
        elif measurement.get_header().get_measurement_mode() == RangeHeader.MEASUREMENT_PHI_SCAN:
            data_x = 2*theta_data + offset
        else:
            data_x = theta_data + offset

        # Convert to counts per second
        # Naaaah, do not convert to counts per second
        data_y = np.array(measurement.get_data().get_data_points())# / steptime

        # do not calculate errors here, we're calculating them later on...
        error_y = np.array(len(data_x) * [0])

        error_x = np.array(len(data_x) * [0])

        # we do not care about headers at this point
        ms = Measurement([], [list(a) for a in zip(data_x, error_x, data_y, error_y)], is_background=is_background)
        ms.set_psi(psi)
        ms.set_counting_time(steptime)
        return ms


class MeasurementsConverter(object):
    def __init__(self):
        self.converter = MeasurementConverter()

    def convert_from_file(self, file):
        return self.convert(RawParser().parse_from_file(file))

    def convert(self, measurements: Measurements):
        converted = []

        for ms in measurements.get_measurements():
            converted.append(self.converter.convert(ms))

        meas = [ms for ms in converted if not ms.is_background()]
        back = [ms for ms in converted if ms.is_background()]

        return UXDMeasurements([], meas, back, MeasurementContext())



