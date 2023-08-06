import numpy as np

from uxdconverter.measurement import MeasurementContext, Measurement, Measurements


class SimpleMeasurementsParser(object):
    def __init__(self, file_obj, logger):
        self._file = file_obj
        self._logger = logger

    def parse(self, context=None) -> Measurements:

        # use the default measurement context
        if context is None:
            context = MeasurementContext()

        # we assume that the file structure is readable by numpy.loadtxt
        # and the data format is:
        #
        # 2theta cps
        #
        # where 2theta is the 2 theta angle of incidence
        # and cps (counts per second) is the measured intensity
        data = np.loadtxt(self._file)

        parsed = []

        for key, entry in enumerate(data):
            if len(entry) > 1:
                parsed.append([float(entry[0]) / 2.0, 0.0, float(entry[1]), 0.0])
            else:
                self._logger.error("Could not parse data line '%s'", key)

        parsed = np.array(parsed)

        # we have no headers here...
        measurement = Measurement([], parsed)

        # also, we have no headers here and no background.
        return Measurements([], [measurement], [], context)