from .enums import DataNormalizationMethod
import numpy as np


class MeasurementContext(object):
    def __init__(self):
        self.sample_length = 10  # unit: mm
        self.wavelength = 1.5418  # unit: Angstroem
        self.wavelength_error = 1e-4  # unit: Angstroem
        self.theta_error = 0.009585 # unit: deg
        self.xray_width = 0.1  # unit: mm
        self.saturation_threshold = 3.5e5  # unit: None
        self.knife_edge = False  # Whether or not the measurement was carried out with a knife edge.
        self.average_overlapping = False  # If a knife edge was used, no illumination correction is done.
        self.normalization = DataNormalizationMethod.FLANK  # Type of normalization method.
        self.normalization_factor = 1
        self.qz_range = (0, 1)
        self.qz_conversion = True
        self.y_log_scale = True

    def get_wavelength(self):
        return self.wavelength


class Measurement(object):
    def __init__(self, headers, data, is_background=False):
        self._headers = headers
        # data: [theta, dtheta, counts (total; not per second), dcounts]
        self._data = np.array(data)
        self._remove_strange_data_points()
        self._is_background = bool(is_background)
        self._psi = 0
        self.file_name = None
        self.name = ""
        self._pos = {}
        self._ctx = {}

    def set_counting_time(self, time):
        self._time = time

    def get_counting_time(self):
        return self._time

    def is_background(self):
        return self._is_background

    def set_background(self, bkgrd):
        self._is_background = bool(bkgrd)

    def set_headers(self, headers):
        self._headers = headers

    def set_display_name(self, name):
        self.name = name

    def get_display_name(self):
        return self.name

    def _remove_strange_data_points(self):
        """
        Removes "strange" data points, i.e. data points with counts less or equal to zero counts.

        :return:
        """
        if len(self._data ) == 0:
            return

        data = self._data.T

        # Thats the counts.
        ind = data[2] >= 0

        if any(ind) == False:
            raise RuntimeError("Data contains no positive counts?")

        new_data = 4 * [None]

        new_data[0] = data[0][ind]
        new_data[1] = data[1][ind]
        new_data[2] = data[2][ind]
        new_data[3] = data[3][ind]

        self._data = np.array(new_data).T

    def get_data(self):
        return np.copy(self._data)

    def scale_y(self, factor):
        self._data = self._data * np.array([1, 1, factor, factor])

    def get_headers(self):
        return self._headers

    def get_data_region_x(self) -> (float, float):
        """
        Returns the data region for the x-variable (i.e. theta)
        :return: (max, min)
        """
        max = np.amax(self._data, axis=0)[0]
        min = np.amin(self._data, axis=0)[0]

        return max, min

    def set_psi(self, psi):
        self.set_position('psi', psi)

    def get_psi(self) -> float:
        return self.get_position('psi')

    def set_position(self, name, value):
        self._pos[name] = value

    def get_position(self, name) -> float:
        return self._pos.get(name, None)

    def set_context(self, key, value):
        self._ctx[key] = value

    def get_context(self, key, alternative=None):
        return self._ctx.get(key, alternative)

    def as_function(self):
        from skipi.function import Function

        return Function.to_function(2*self._data[:,0], self._data[:,2])

class Measurements(object):
    def __init__(self, header, measurements, backgrounds, measurement_context):
        self._header = header
        self._measurement = measurements
        self._background_measurement = backgrounds
        self._measurement_context = measurement_context
        self.file_name = None

    def get_headers(self):
        return self._header

    def set_context(self, context):
        self._measurement_context = context

    def get_context(self):
        """

        :return MeasurementContext:
        """
        return self._measurement_context

    def get_count_measurements(self):
        return len(self._measurement)

    def get_count_background_measurements(self):
        return len(self._background_measurement)

    def get_measurement(self, index):
        return self._measurement[index]

    def get_measurements(self):
        """

        :return list(Measurement):
        """
        return self._measurement

    def get_background_measurements(self):
        return self._background_measurement

    def get_background_measurement(self, index):
        return self._background_measurement[index]

    def add(self, mss: 'Measurements'):
        self._measurement = self._measurement + mss.get_measurements()
        self._background_measurement = self._background_measurement + mss.get_background_measurements()
