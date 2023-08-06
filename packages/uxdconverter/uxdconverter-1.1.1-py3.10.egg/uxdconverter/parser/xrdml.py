import numpy as np
from enum import Enum

from lxml import etree

from uxdconverter.enums import DataNormalizationMethod
from uxdconverter.measurement import MeasurementContext, Measurements, Measurement

AXIS_2THETA = '2Theta'
AXIS_OMEGA = 'Omega'
AXIS_PHI = 'Phi'
AXIS_CHI = 'Chi'
AXIS_Z = 'Z'
AXIS_X = 'X'
AXIS_Y = 'Y'

class DetectorMode(Enum):
    UNKNOWN = 'unknown'
    STATIC = 'static'
    CONTINUOUS = 'scanning'

class GeneralXRDMLParser(object):
    def __init__(self, file, tree=None):
        self._file = file
        self._tree = tree
        self._root = None
        self._ns = None

    def _parse_root(self):
        if self._tree is None:
            self._tree = etree.parse(self._file)

        self._root = self._tree.getroot()
        self._ns = self._root.nsmap

    def get_measurement_element(self):
        self._parse_root()

        try:
            measurement = self._root.findall("xrdMeasurement", self._ns)
        except Exception as e:
            self._logger.exception(e)
            raise RuntimeError(f"xrdMeasurement entry not found in file {self._file}")

        if len(measurement) > 1:
            raise RuntimeError("More than one xrdMeasurement entry?")

        return measurement[0]

class XRDMLContextParser(GeneralXRDMLParser):
    def parse(self):
        xrd_entry = self.get_measurement_element()
        wavelength = self._get_wavelength(xrd_entry)

        ctx = MeasurementContext()
        ctx.wavelength = wavelength
        ctx.normalization = DataNormalizationMethod.FACTOR
        ctx.normalization_factor = 1
        ctx.qz_conversion = False
        ctx.qz_range = (0, 180)
        ctx.knife_edge = False

        return ctx

    def _get_wavelength(self, xrd_entry):
        wavelength = xrd_entry.find("usedWavelength", self._ns)
        if wavelength is None:
            return 0.0

        kAlpha1 = wavelength.find("kAlpha1", self._ns)

        if kAlpha1 is None:
            return 0.0

        return float(kAlpha1.text)

class XRDMLParser(GeneralXRDMLParser):
    def __init__(self, file, logger):
        super(XRDMLParser, self).__init__(file)
        self._logger = logger

    def parse(self, context=None) -> Measurements:
        xrd_entry = self.get_measurement_element()

        # use the default measurement context
        ctxParser = XRDMLContextParser(self._file, self._tree)
        context = ctxParser.parse()

        """
        try:
            tree = etree.parse(self._file)
            root = tree.getroot()
            mss = root.findall("xrdMeasurement", root.nsmap)
        except Exception as e:
            self._logger.exception(e)
            raise RuntimeError("Could not read file %s" % self._file)

        self._ns = root.nsmap

        if len(mss) > 1:
            raise RuntimeError("More than one xrdMeasurement entry?")

        xrd_entry = mss[0]
        """

        detector_mode = self._get_detector_mode(xrd_entry)
        measurements = [self._get_measurement(scan) for scan in xrd_entry.findall("scan", self._ns)]

        for ms in measurements:
            ms.set_context('DetectorMode', detector_mode)

        return Measurements([], measurements, [], context)

    def _get_detector_mode(self, xrd_entry):
        diffractedBeamPath = xrd_entry.find("diffractedBeamPath", self._ns)

        if diffractedBeamPath is None:
            return DetectorMode.UNKNOWN

        detector = diffractedBeamPath.find("detector", self._ns)

        if detector is None:
            return DetectorMode.UNKNOWN

        mode = detector.find("mode", self._ns)

        if mode is None:
            return DetectorMode.UNKNOWN

        if mode.text == "Static":
            return DetectorMode.STATIC
        elif mode.text == "Scanning":
            return DetectorMode.CONTINUOUS
        else:
            return DetectorMode.UNKNOWN

    def _construct_measurement(self, theta, counts):
        dtheta = len(theta) * [0.0]
        dcounts = len(counts) * [0.0]
        data = np.array(list(zip(theta, dtheta, counts, dcounts)))

        return Measurement([], data)

    def _get_measurement(self, scan):
        datapoints = scan.find("dataPoints", self._ns)

        counts = self._get_counts(datapoints)
        len_counts = len(counts)
        theta = self._get_axis(AXIS_2THETA, datapoints, len_counts) / 2.0
        omega = self._get_axis(AXIS_OMEGA, datapoints, len_counts)
        z = self._get_axis(AXIS_Z, datapoints, len_counts)
        phi = self._get_axis(AXIS_PHI, datapoints, len_counts)
        chi = self._get_axis(AXIS_CHI, datapoints, len_counts)

        measurement = self._construct_measurement(theta, counts)

        if self._is_single_value(omega):
            measurement.set_position('omega', omega)
        if self._is_single_value(z):
            measurement.set_position('z', z)
        if self._is_single_value(phi):
            measurement.set_position('phi', phi)
        if self._is_single_value(chi):
            measurement.set_position('chi', chi)

        measurement.set_counting_time(self._get_time(datapoints))

        if omega is not None:
            # psi or omega_offset
            psi = - (theta - omega)
            measurement.set_psi(psi[0])

        return measurement

    def _get_time(self, datapoints):
        entries = datapoints.findall("commonCountingTime", self._ns)
        if entries is None or len(entries) < 1:
            raise RuntimeException("Could not find counting time")
        if len(entries) == 1:
            return float(entries[0].text)
        raise RuntimeException("Found multiple counting times")

    def _find_axis(self, axis_name, datapoints):
        for position in datapoints.findall("positions", self._ns):
            if position.get("axis") == axis_name:
                return position

        return None

    def _is_single_value(self, obj):
        if obj is None:
            return False

        if isinstance(obj, float):
            return True

        return False

    def _get_axis(self, axis_name, datapoints, number_of_steps, type=float):
        axis = self._find_axis(axis_name, datapoints)

        if axis is None:
            return None

        common_position = axis.find("commonPosition", self._ns)
        if common_position is not None:
            return type(common_position.text)

        list_position = axis.find("listPositions", self._ns)
        if list_position is not None:
            return np.array(list(map(type, list_position.text.split(" "))))

        start_position = axis.find("startPosition", self._ns)
        end_position = axis.find("endPosition", self._ns)

        if start_position is not None and end_position is not None:
            start = type(start_position.text)
            end = type(end_position.text)
            return np.linspace(start, end, number_of_steps)
        if start_position is not None or end_position is not None:
            raise RuntimeError("Only found startPosition or endPosition, but not both")

        return None

    def _get_counts(self, datapoints):
        element = datapoints.find("counts", self._ns)

        if element is None:
            raise RuntimeError("datapoint entry did not contain counts")

        counts = np.array(list(map(int, element.text.split(" "))))

        return counts