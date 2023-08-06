import numpy as np
from typing import List
from uxdconverter.measurement import Measurement, MeasurementContext
from uxdconverter.compare import Comparator
from uxdconverter.enums import DataNormalizationMethod

from math import log

class AbstractMeasurementMerger(object):
    def merge(self, measurement_1: Measurement, measurement_2: Measurement) -> Measurement:
        raise NotImplementedError()


class MeasurementMerger(AbstractMeasurementMerger):
    def __init__(self, scaling_factor=None, averaging=False, comparator: Comparator = None):
        self._scaling = scaling_factor
        self._averaging = averaging

        if comparator is None:
            comparator = Comparator()

        self._compare = comparator

    def merge(self, measurement_1: Measurement, measurement_2: Measurement) -> Measurement:
        """
            This function merges two measurements. The merging is done in such a way,
            that at the overlap of the two measurements a scaling factor is computed.
            Then, we assume that at the overlap region, the measurements are identical (after a scaling)
            and thus we just take one of the measurements in the overlap region.
            At the other two regions, we just take one of the measurements (after a re-scaling).

            A user-defined scaling_factor can be passed by the argument.
            An averaging function at the overlap region can be performed by the averaging=True parameter.

            Note:
                The scaling factor is calculated to be bigger than 1 and is chosen to minimize the following problem:

                min_{alpha > 0} || f - \alpha g ||^2 = min_{\alpha > 0} \sum_{i=1}^{n} | f(x_i) - \alpha g(x_i) | ^2

                The solution to this problem is \alpha = (\sum f(x_i)) / (\sum g(x_i)) if f >= g.
                    Otherwise switch f with g.

            :param Measurement measurement_1: First measurement
            :param Measurement measurement_2: Second measurement
            :return Measurement:
        """

        # first sort them, such that measurement_1 contains the data for the 'left' region
        # and measurement_2 contains the data for the 'right' region.
        measurement_1, measurement_2 = self._compare.sort(measurement_1, measurement_2)

        # find out the region where they overlap
        overlap_region = self._compare.overlap_limits(measurement_1, measurement_2)
        # and get the data in the overlapping region
        overlap_data_1, overlap_data_2 = self._compare.overlapping_data(measurement_1, measurement_2, overlap_region)

        # We now assume that the x-values are correctly ordered,
        # i.e. the x-values are decreasing.

        # Next we want to compare at the same x-values. For that we just check for the
        # same amount of elements in the list. This should be enough.
        if not len(overlap_data_1) == len(overlap_data_2):
            raise ValueError("Cannot merge data sets, if the overlapping region has not the same data elements.")

        scaling_factor = self._scaling

        # Compute the scaling factor if the user did not specify it.
        if scaling_factor is None:
            scaling_factors = [overlap_data_1[i][2] / overlap_data_2[i][2] for i in range(len(overlap_data_1))]
            scaling_factor = np.average(scaling_factors)
            scaling_factor_std = np.std(scaling_factors)

            scaling_factor = sum([overlap_data_1[i][2]*overlap_data_2[i][2] for i in range(len(overlap_data_1))]) / sum([overlap_data_2[i][2]**2 for i in range(len(overlap_data_1))])

            #scaling_factor = sum([x[2] for x in overlap_data_1]) / sum([x[2] for x in overlap_data_2])
            if scaling_factor < 1:
                scaling_factor = 1.0 / scaling_factor

        # figure out, which measurement has bigger values in the overlapping region
        # then we scale the other measurement.
        diff = sum([overlap_data_1[i][2] - overlap_data_2[i][2] for i in range(len(overlap_data_1))])
        print(f"Scaling factor std {scaling_factor_std}")
        if diff >= 0:
            print(f"Scaling measurement 2 with {scaling_factor:.3f}, diff={diff}")
            # measurement 1 is bigger, hence scale measurement 2
            measurement_2.scale_y(scaling_factor)
        else:
            print(f"Scaling measurement 1 with {scaling_factor:.4f}, diff={-diff}")
            measurement_1.scale_y(scaling_factor)

        data_left = []
        data_right = []
        # Already calculate the left and right data regions. They need to be scaled in the next step.
        # Choose the regions, such that we keep most of the data...
        if measurement_1.get_data_region_x()[1] <= measurement_2.get_data_region_x()[1]:
            data_left = np.array([x for x in measurement_1.get_data() if x[0] < overlap_region[1]])
        else:
            data_left = np.array([x for x in measurement_2.get_data() if x[0] < overlap_region[1]])

        if measurement_1.get_data_region_x()[0] >= measurement_2.get_data_region_x()[0]:
            data_right = np.array([x for x in measurement_1.get_data() if x[0] > overlap_region[0]])
        else:
            data_right = np.array([x for x in measurement_2.get_data() if x[0] > overlap_region[0]])

        """
        if diff >= 0:
            # measurement_1 is bigger, hence scale measurement 2
            if len(data_right) > 0:
                data_right = data_right * scaling_array
            overlap_data_2 = overlap_data_2 * scaling_array
        else:
            if len(data_left) > 0:
                data_left = data_left * scaling_array
            overlap_data_1 = overlap_data_1 * scaling_array
        """

        # Now we can perform the merging :)
        # The left region comes from measurement_1
        # The right region from measurement_2 (scaled)
        # The overlapping region either from measurement_1 or from the average of both
        if self._averaging is True:
            # now average over the two data sets
            data_middle = np.array(0.5 * (overlap_data_2 + overlap_data_1))
        else:
            # as the middle part, take the measurements which were not scaled.
            if diff >= 0:
                data_middle = overlap_data_1
            else:
                data_middle = overlap_data_2

        # Now ,just use the data where there is actually any data
        data = [data_left, data_middle, data_right]
        if len(data_left) == 0:
            data = data[1:]
        if len(data_right) == 0:
            data = data[:-1]
        data = np.concatenate(tuple(data))

        return Measurement(measurement_1.get_headers(), data)


class MultiMerger(object):
    def __init__(self, merger_class: AbstractMeasurementMerger):
        self._merger = merger_class

    def sort(self, measurements: List[Measurement]) -> List[Measurement]:
        """
        Sort a list of measurements in such a way, that one can make the most efficient and best
        merging of them.
        What we mean by 'efficient' and 'best' merging:
            The first measurement should be the measurement with the most statistics, i.e. most of the counts. So this
            will probably be the measurement with the lowest theta angle.
            Then order in such a way, that every measurement overlaps with the previous measurement.

        So, what we do: Sort the measurements by the angles in an ascending order.
        :param measurement:
        :return:
        """
        mss = [(ms.get_data_region_x()[1], ms) for ms in measurements]
        mss.sort(key=lambda x: x[0])
        return [ms[1] for ms in mss]

    def merge(self, measurements: List[Measurement]) -> Measurement:

        measurements = self.sort(measurements)

        measurement = measurements[0]

        if len(measurements) > 1:
            # merge all measurements together
            merged = measurement
            for i in range(len(measurements) - 1):
                merged = self._merger.merge(merged, measurements[i + 1])

            measurement = merged

        return measurement


class MeasurementSubtraction(object):
    def __init__(self, comparator: Comparator = None):
        if comparator is None:
            comparator = Comparator()

        self._comp = comparator

    def subtract(self, measurement_1: Measurement, measurement_2: Measurement) -> Measurement:
        """
             Calculates measurement_1 - measurement_2.
             This can only carried out in the overlapping region. Since, this is only used for subtracting the
             background from the measurement, the overlapping region is the whole data region. Nevertheless, we check
             that and print an error if this is not the case.
             The returned Measurement will only contain the overlapping region, the rest is thrown away.

            :param Measurement measurement_1:
            :param Measurement measurement_2:
            :return: A new measurement which is the difference of measurement_1 with measurement_2
            """

        overlap_data_1, overlap_data_2 = self._comp.overlapping_data(measurement_1, measurement_2)

        if not len(overlap_data_1) == len(measurement_1.get_data()):
            print("Subtracting measurements: The overlapping region is smaller than before. Ignoring entries...")

        if not len(overlap_data_1) == len(overlap_data_2):
            raise ValueError(
                "Cannot subtract measurements, if the overlapping region does not contains the same amount of elements")

        # little trick, the minuend is just [0, 0, -cps, 0] ;)
        data = overlap_data_1 - (overlap_data_2 * [0, 0, 1, 0])
        return Measurement(measurement_1.get_headers(), data)


class AbstractDataManipulation(object):
    def manipulate(self, measurement: Measurement, context: MeasurementContext) -> Measurement:
        raise NotImplementedError()

class DataNormalization(AbstractDataManipulation):

    def manipulate(self, measurement: Measurement, context: MeasurementContext) -> Measurement:
        """
            Normalizes the measurement to one.

            Available methods:
                'max': Normalizes the maximum count to 1.
                'flank': Find the first flank of the reflectivity curve, and then normalizes the point with the lowest
                            absolute slope to 1.

            Normalizing is applied to the whole data set and done by scaling the y values and errors (i.e. counts).
        """

        method = context.normalization

        if method == DataNormalizationMethod.MAX:
            """
             Just find the point with the most counts per second, and normalize this point to 1. The scaling factor is 
             applied to every point.
            """
            data = measurement.get_data()
            max = np.amax([x[2] for x in data])
            norm = 1.0 / max
            return Measurement(measurement.get_headers(), data * np.array([1, 1, norm, norm]))

        if method == DataNormalizationMethod.FLANK:
            """
             First find the first flank (i.e. the point with the smallest derivative (the point where the graph's gradient 
             has the greatest descending. Then look for the points left to it (this should then be the region of total
             reflection) and find there the point with the slope nearest to zero, i.e. with the smallest absolute gradient.
            """

            data = measurement.get_data()
            # Find the first flank via the gradient.
            deriv = np.gradient([x[2] for x in data], [x[0] for x in data])
            first_flank = np.argmin(deriv)

            if first_flank == 0:
                idx = 0
            else:
                # Now look at the points left to the first flank, and find the smallest absolute slope.
                vf = np.vectorize(abs)
                left_deriv = vf(deriv[0:first_flank])
                idx = np.argmin(left_deriv)

            # The scaling factor is then 1 / y_c, where y_c is the point with the lowest absolute slope
            norm = 1.0 / data[idx][2]
            return Measurement(measurement.get_headers(), data * np.array([1, 1, norm, norm]))

        if method == DataNormalizationMethod.FACTOR:
            factor = context.normalization_factor
            data = measurement.get_data()
            return Measurement(measurement.get_headers(), data * np.array([1, 1, factor, factor]))


class DataIlluminationCorrection(AbstractDataManipulation):
    def manipulate(self, measurement: Measurement, context: MeasurementContext) -> Measurement:
        """
            This method takes the measurement data and applies a illumination correction.

            When measuring samples without a knife edge, it happens that for small angles, the footprint of the
            x-ray beam is bigger than the sample itself. Hence, we scale the reflected x-rays with the proportion of the
            footprint and the sample size.

            The footprint of the x-ray beam can be calculated as :
                w / \sin(\theta)
            with w being the x-ray beam width, \theta the angle between the incidence beam and the sample plane.

            Hence the scaling factor is w/(l * \sin(\theta) )
            with l being the sample size.

            Note that the scaling factor is only applied if the x-ray footprint is larger than the sample size, i.e.
                w / \sin(\theta) > l  <=> \theta <= \arcsin( w / l ) =: \theta_c

        :param Measurement measurement: the measurement to correct
        :param MeasurementContext context: the context of the measurement (needed for e.g. xray width and sample length)
        :return: Performs a new measurement with illumination correction applied
        """

        w = context.xray_width
        l = context.sample_length

        # in the docstring, \theta_c denoted, in degree
        critical_angle = np.arcsin(w / l) * 180 / np.pi
        # make a copy of the data, so we do not modify the data from the measurement (i.e. measurement is immutable)
        data = measurement.get_data()

        pre_scaling = float(w) / l

        # Correct the data
        for i in range(len(data)):
            # Correct only if the footprint is larger than the sample
            # So, scale the cps and the relative error
            if data[i][0] <= critical_angle:
                correction = pre_scaling / np.sin(data[i][0] * np.pi / 180)
                # do nothing with the q-error
                #data[i][1] = data[i][1]
                data[i][2] = data[i][2] * correction
                data[i][3] = data[i][3] * correction

        return Measurement(measurement.get_headers(), data)


class ErrorCalculation(AbstractDataManipulation):
    def manipulate(self, measurement: Measurement, context: MeasurementContext) -> Measurement:
        """
         Simply calculate the relative error. For poisson distributed data,
         the absolute error is \sqrt(y) where y is the measurement counts.
         The relative error is hence 1/\sqrt(y).

        :param Measurement measurement:
        :param MeasurementContext context
        :return:
        """
        dT = context.theta_error
        data = [[x[0], dT, x[2], np.sqrt(x[2])] for x in measurement.get_data()]
        #data = [[x[0], dT, x[2], 1/np.sqrt(x[2])] for x in measurement.get_data()]
        return Measurement(measurement.get_headers(), data)


class QzCalculation(AbstractDataManipulation):
    def manipulate(self, measurement: Measurement, context: MeasurementContext) -> Measurement:
        """
            Converts the x-data of measurement into qz data by the formula
                q_z = 4 * pi / \lambda * \sin(\theta)
            where \lambda is the wavelength to the x-ray beam and \theta is the reflectance angle.

            :param Measurement measurement:
            :param MeasurementContext context:
            :return Measurement:
                """

        # this is the constant pre-factor for the conversion
        # 4 * pi / \lambda
        pre_factor = 4 * np.pi / context.wavelength

        # make a copy
        data = measurement.get_data()

        # delta Lambda / Lambda squared
        dLoLsq = (context.wavelength_error / context.wavelength)**2
        #dTsq = dT ** 2

        for i in range(len(data)):
            t_rad = np.deg2rad(data[i][0])
            dTsq = np.deg2rad(data[i][1])**2

            data[i][0] = pre_factor * np.sin(t_rad)
            data[i][1] = pre_factor * np.sqrt(np.sin(t_rad)**2 * dLoLsq + np.cos(t_rad)**2 * dTsq)

        return Measurement(measurement.get_headers(), data)


class QzCropping(AbstractDataManipulation):
    def manipulate(self, measurement: Measurement, context: MeasurementContext) -> Measurement:
        """
            Crops the qz data, i.e. removes data which does not lie in the interval
                [qz_min, qz_max], where qz_min, qz_max are defined from context.qz_range

        :param Measurement measurement:
        :param MeasurementContext context:
        :return:
        """

        qz_min = context.qz_range[0]
        qz_max = context.qz_range[1]

        new_data = np.array([d for d in measurement.get_data() if qz_min <= d[0] <= qz_max])

        if len(new_data) == 0:
            raise RuntimeWarning("No data point in selected range. Check settings")

        return Measurement(measurement.get_headers(), np.array(new_data))
