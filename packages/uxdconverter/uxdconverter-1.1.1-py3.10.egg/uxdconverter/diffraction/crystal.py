from math import sqrt, asin, degrees, sin, cos, radians, ceil, pi
import numpy as np

class InterplanarSpacing(object):
    PARAMETER_A = 'a'
    PARAMETER_B = 'b'
    PARAMETER_C = 'c'
    PARAMETER_ALPHA = 'alpha'
    PARAMETER_BETA = 'beta'
    PARAMETER_GAMMA = 'gamma'

    PARAMETERS = [
        PARAMETER_A,
        PARAMETER_B,
        PARAMETER_C,
        PARAMETER_ALPHA,
        PARAMETER_BETA,
        PARAMETER_GAMMA
    ]

    def __init__(self, params={}):
        self._params = params

    def get_spacing(self, h, k, l):
        raise NotImplemented("Should be implemented in child classes")

    def solve_for_miller_indices(self, spacing, **kwargs):
        raise NotImplemented()

    def get_miller_indices(self):
        raise NotImplemented()

    def get_required_parameters(self):
        raise NotImplemented()

    def set_parameter(self, params):
        self._params = params

    def _has_parameter(self, parameter_list=None):
        if parameter_list is None:
            parameter_list = self.get_required_parameters()

        if not isinstance(parameter_list, list):
            parameter_list = [parameter_list]

        for parameter in parameter_list:
            if parameter not in self._params:
                return False

        return True

    def _get_parameter(self, parameter_name):
        if not parameter_name in self._params:
            return 0
        return self._params[parameter_name]

    def detect_system(self):
        a = self._get_parameter(self.PARAMETER_A)
        b = self._get_parameter(self.PARAMETER_B)
        c = self._get_parameter(self.PARAMETER_C)
        alpha = self._get_parameter(self.PARAMETER_ALPHA)
        beta = self._get_parameter(self.PARAMETER_BETA)
        gamma = self._get_parameter(self.PARAMETER_GAMMA)

        if a == b == c and alpha == beta == gamma and gamma == 90.0:
            return CubicSpacing
        elif a == b and alpha == beta == 90 and gamma == 120:
            return HexagonalSpacing
        elif a == b == c and alpha == beta == gamma and not gamma == 90:
            return RhombohedralSpacing
        elif a == b and not b == c and alpha == beta == gamma == 90:
            return TetragonalSpacing
        elif alpha == beta == gamma == 90:
            return OrthorhombicSpacing
        elif alpha == gamma == 90:
            return MonoclinicSpacing
        else:
            return TriclinicSpacing

    def get_all_hkl(self, theta_max, bragg: 'BraggCondition'):
        raise NotImplemented("Should be implemented in child classes")

class CubicSpacing(InterplanarSpacing):
    def get_spacing(self, h, k, l):
        assert self._has_parameter()

        a = self._params[self.PARAMETER_A]

        return a * sqrt(1 / (h ** 2 + k ** 2 + l ** 2))

    def get_required_parameters(self):
        return [self.PARAMETER_A]

    def get_all_hkl(self, theta_max, bragg: 'BraggCondition'):
        min_spacing = bragg.get_lattice_spacing(theta_max)
        sigma = int((self._params[self.PARAMETER_A] / min_spacing)**2)
        # inherent floor to the next integer
        h_max = int(sqrt(sigma))
        k_max = lambda h: int(sqrt(sigma-h**2)) if sigma-h**2 > 0 else 0
        l_max = lambda h, k: int(sqrt(sigma-h**2-k**2)) if sigma - h**2 - k**2 > 0 else 0
        hkl = []
        for h in range(1, h_max + 1):
            for k in range(k_max(h+1)):
                for l in range(l_max(h, k)+1):
                    hkl.append((h, k, l))

        return hkl

class TetragonalSpacing(InterplanarSpacing):
    def get_spacing(self, h, k, l):
        assert self._has_parameter()

        a = self._params[self.PARAMETER_A]
        c = self._params[self.PARAMETER_C]

        dsqr_inv = (h ** 2 + k ** 2) / (a ** 2) + l ** 2 / c ** 2
        return sqrt(1 / dsqr_inv)

    def get_required_parameters(self):
        return [self.PARAMETER_A, self.PARAMETER_C]


class HexagonalSpacing(InterplanarSpacing):
    def get_spacing(self, h, k, l):
        assert self._has_parameter()

        a = self._params[self.PARAMETER_A]
        c = self._params[self.PARAMETER_C]

        dsqr_inv = 4 / 3.0 * (h ** 2 + h * k + k ** 2) / (a ** 2) + l ** 2 / c ** 2
        return sqrt(1 / dsqr_inv)

    def get_required_parameters(self):
        return [self.PARAMETER_A, self.PARAMETER_C]


class RhombohedralSpacing(InterplanarSpacing):
    def get_spacing(self, h, k, l):
        assert self._has_parameter()

        a = self._params[self.PARAMETER_A]
        alpha = self._params[self.PARAMETER_ALPHA]

        dsqr_inv = (h ** 2 + k ** 2 + l ** 2) * sin(alpha) ** 2 + 2 * (h * k + k * l + h * l) * (
                cos(alpha) ** 2 - cos(alpha)) / (a ** 2 * (1 - 3 * cos(alpha) ** 2 + 2 * cos(alpha) ** 3))
        return sqrt(1 / dsqr_inv)

    def get_required_parameters(self):
        return [self.PARAMETER_A, self.PARAMETER_ALPHA]


class OrthorhombicSpacing(InterplanarSpacing):
    def get_spacing(self, h, k, l):
        assert self._has_parameter()
        a = self._params[self.PARAMETER_A]
        b = self._params[self.PARAMETER_B]
        c = self._params[self.PARAMETER_C]

        dsqr_inv = h ** 2 / a ** 2 + k ** 2 / b ** 2 + l ** 2 / c ** 2
        return sqrt(1 / dsqr_inv)

    def get_required_parameters(self):
        return [self.PARAMETER_A, self.PARAMETER_B, self.PARAMETER_C]


class MonoclinicSpacing(InterplanarSpacing):
    def get_spacing(self, h, k, l):
        assert self._has_parameter()
        a = self._params[self.PARAMETER_A]
        b = self._params[self.PARAMETER_B]
        c = self._params[self.PARAMETER_C]
        beta = self._params[self.PARAMETER_BETA]

        dsqr_inv = (h ** 2 / a ** 2 + k ** 2 * sin(beta) ** 2 / b ** 2 + l ** 2 / c ** 2 - 2 * h * l * cos(beta) / (
                a * c)) / sin(beta) ** 2
        return sqrt(1 / dsqr_inv)

    def get_required_parameters(self):
        return [self.PARAMETER_A, self.PARAMETER_B, self.PARAMETER_C, self.PARAMETER_BETA]


class TriclinicSpacing(InterplanarSpacing):
    def get_spacing(self, h, k, l):
        assert self._has_parameter()
        a = self._params[self.PARAMETER_A]
        b = self._params[self.PARAMETER_B]
        c = self._params[self.PARAMETER_C]
        alpha = self._params[self.PARAMETER_ALPHA]
        beta = self._params[self.PARAMETER_BETA]
        gamma = self._params[self.PARAMETER_GAMMA]

        s1 = h ** 2 / a ** 2 * sin(alpha) ** 2 + k ** 2 / b ** 2 * sin(beta) ** 2 + l ** 2 / c ** 2 * sin(gamma) ** 2
        s2 = 2 * k * l / (b * c) * (cos(beta) * cos(gamma) - cos(alpha))
        s3 = 2 * h * l / (a * c) * (cos(gamma) * cos(alpha) - cos(beta))
        s4 = 2 * h * k / (a * b) * (cos(alpha) * cos(beta) - cos(gamma))
        denom = 1 - cos(alpha) ** 2 - cos(beta) ** 2 - cos(gamma) ** 2 + 2 * cos(alpha) * cos(beta) * cos(gamma)

        dsqr_inv = (s1 + s2 + s3 + s4) / denom
        return sqrt(1 / dsqr_inv)

    def get_required_parameters(self):
        return [self.PARAMETER_A, self.PARAMETER_B, self.PARAMETER_C, self.PARAMETER_ALPHA, self.PARAMETER_BETA,
                self.PARAMETER_GAMMA]


class DiffractionContext(object):
    def __init__(self):
        self._wavelength = 1.5418
        self._bragg_order = 1

    def get_wavelength(self):
        return self._wavelength

    def get_bragg_order(self):
        return self._bragg_order


class BraggCondition(object):
    def __init__(self, diffraction_context, interplanar_spacing):
        assert isinstance(diffraction_context, DiffractionContext)
        assert isinstance(interplanar_spacing, InterplanarSpacing)

        self._ctx = diffraction_context
        self._spacing = interplanar_spacing

    def set_spacing(self, spacing):
        assert isinstance(spacing, InterplanarSpacing)

        self._spacing = spacing

    def get_spacing(self):
        return self._spacing

    def get_theta(self, h, k, l):
        lamb = self._ctx.get_wavelength()
        n = self._ctx.get_bragg_order()
        d = self._spacing.get_spacing(h, k, l)
        theta = asin(n * lamb / (2 * d))  # in rad

        return np.rad2deg(theta)

    def get_q(self, h, k, l):
        return 2 * np.pi * self._ctx.get_bragg_order() / self._spacing.get_spacing(h, k, l)

    def get_lattice_spacing(self, theta):
        return self._ctx.get_bragg_order() * self._ctx.get_wavelength() / (2*sin(radians(theta)))

    def get_all_hkl(self, theta_max):
        return self._spacing.get_all_hkl(theta_max, self)