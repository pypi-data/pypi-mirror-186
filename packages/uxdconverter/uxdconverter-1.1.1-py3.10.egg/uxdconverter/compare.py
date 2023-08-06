from uxdconverter.measurement import Measurement
import numpy as np


class Comparator(object):
    def __init__(self):
        pass

    def overlap_limits(self, measurement_1: Measurement, measurement_2: Measurement) -> (float, float):
        """
        This method finds the x-value overlap of two measurements.
        This should be a symmetric function, i.e. overlap_limits(x, y) = overlap_limits(y, x)
        If one interprets the measurements as sets, then this method finds the intersection of them.

        :param Measurement measurement_1:
        :param Measurement measurement_2:
        :return: Tuple of x-values. (x_max, x_min) with x_max > x_min
        """

        data_region_1 = measurement_1.get_data_region_x()
        data_region_2 = measurement_2.get_data_region_x()

        # Compute the max's and min's for the x- values
        maxs = [data_region_1[0], data_region_2[0]]
        mins = [data_region_1[1], data_region_2[1]]

        overlap_max = min(maxs)
        overlap_min = max(mins)

        if overlap_max < overlap_min:
            raise ValueError("No overlap of the measurements found")

        return overlap_max, overlap_min

    def merge_region(self, measurement_1: Measurement, measurement_2: Measurement) -> (float, float):
        """
        This methods finds the 'merging region', i.e. the region where we have data points
        either from measurement_1, or from measurement_2.
        If one interprets the measurements as sets, then this corresponds to the union of them.

        :param Measurement measurement_1:
        :param Measurement measurement_2:
        :return:
        """

        data_region_1 = measurement_1.get_data_region_x()
        data_region_2 = measurement_2.get_data_region_x()

        # Compute the max's and min's for the x- values
        maxs = [data_region_1[0], data_region_2[0]]
        mins = [data_region_1[1], data_region_2[1]]

        return max(maxs), min(mins)

    def sort(self, measurement_1: Measurement, measurement_2: Measurement) -> (Measurement, Measurement):
        """
        Sorts the measurements according to their x-value regions.
        Returns two measurements (ms_1, ms_2) such that the x-values of ms_1 <= ms_2

        :param Measurement measurement_1:
        :param Measurement measurement_2:
        :return:
        """

        data_region_1 = measurement_1.get_data_region_x()
        data_region_2 = measurement_2.get_data_region_x()

        if data_region_1[1] <= data_region_2[1]:
            return measurement_1, measurement_2
        else:
            return measurement_2, measurement_1

    def overlapping_data(self, measurement_1: Measurement, measurement_2: Measurement, overlapping_region=None) -> (
    list, list):
        """
        Returns the overlapping data from the two measurements.
        It computes the overlapping region, see overlap_limits and extracts the data which lies in this region

        A custom region can be passed via the overlapping_region parameter.

        :param Measurement measurement_1:
        :param Measurement measurement_2:
        :param tuple overlapping_region: First entry contains max limit, second one the min limit
        :return:
        """
        if overlapping_region is None:
            overlapping_region = self.overlap_limits(measurement_1, measurement_2)

        overlap_data = []

        for ms in [measurement_1, measurement_2]:
            data = [x for x in ms.get_data() if (overlapping_region[0] >= x[0] >= overlapping_region[1])]
            overlap_data.append(np.array(data))

        return overlap_data[0], overlap_data[1]
