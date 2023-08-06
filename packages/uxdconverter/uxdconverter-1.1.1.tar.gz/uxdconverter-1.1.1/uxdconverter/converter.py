from uxdconverter.measurement import Measurements, Measurement
from uxdconverter.operation import MultiMerger, MeasurementMerger, MeasurementSubtraction, DataIlluminationCorrection, \
    DataNormalization, QzCalculation, QzCropping, ErrorCalculation


class Converter(object):
    def __init__(self, measurements: Measurements):
        self._backgrounds = measurements.get_background_measurements()
        self._context = measurements.get_context()
        self._measurements = measurements.get_measurements()

        self._multi_merge = MultiMerger(MeasurementMerger())
        self._subtract = MeasurementSubtraction()
        self._illumination = DataIlluminationCorrection()
        self._normalization = DataNormalization()
        self._qz_calc = QzCalculation()
        self._cropping = QzCropping()
        self._error = ErrorCalculation()

    def convert(self) -> Measurement:
        """
        Converts the measurements into a single measurement, by merging, subtracting and correcting the measurements in
        a reasonable manner:
            If there is just one measurement, a correction and normalization is done.
            If there are more than one measurements, the last measurement is considered as background, and the rest are
                normal 'locked coupled' measurements. Hence the 'locked coupled' are merged together, then the background
                is subtracted and after that, the correction and normalization is done.
            At the end, the measurement is converted to q_z values.

        :return Measurement:
        """

        mss = self._measurements
        backgrounds = self._backgrounds
        context = self._context

        # default measurement.
        if len(mss) == 0:
            raise ValueError("Cannot convert if no measurement was given.")

        mss = [self._error.manipulate(ms, context) for ms in mss]

        measurement = self._multi_merge.merge(mss)

        # If we have any background, subtract it from the measurement
        if len(backgrounds) > 0:
            background = self._multi_merge.merge(backgrounds)

            # Do the subtraction: measurement - background
            measurement = self._subtract.subtract(measurement, background)

        if context.knife_edge is False:
            measurement = self._illumination.manipulate(measurement, context)

        measurement = self._error.manipulate(measurement, context)

        if self._context.qz_conversion is True:
            measurement = self._qz_calc.manipulate(measurement, context)

        measurement = self._cropping.manipulate(measurement, context)
        measurement = self._normalization.manipulate(measurement, context)

        return measurement