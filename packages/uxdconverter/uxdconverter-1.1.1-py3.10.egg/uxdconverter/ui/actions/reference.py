import matplotlib.pyplot as plt
from uxdconverter.ui.controller import Controller
from uxdconverter.diffraction.crystal import DiffractionContext, BraggCondition, CubicSpacing, \
    InterplanarSpacing
from uxdconverter.converter import Converter

from enum import Enum

class PseudoStructureFactor(object):
    @staticmethod
    def is_mixed_parity(h, k, l):
        return not PseudoStructureFactor.is_same_parity(h, k, l)

    @staticmethod
    def is_same_parity(h, k, l):
        return all([h % 2 == 0, k % 2 == 0, l % 2 == 0]) or all([h % 2 == 1, k % 2 == 1, l % 2 == 1])

    @staticmethod
    def structure_factor_diamond_crystal(h, k, l):
        if PseudoStructureFactor.is_mixed_parity(h, k, l):
            return 0

        if (h + k + l - 2) % 4 == 0:
            return 0

        return 1


class SampleReference(Enum):
    NIST_LaB6 = 'LaB6 (660c)'
    NIST_Si = 'Si (640f)'

    CRYSTAL_STRUCTURE = {
        NIST_LaB6: CubicSpacing({InterplanarSpacing.PARAMETER_A: 4.156826}),
        NIST_Si: CubicSpacing({InterplanarSpacing.PARAMETER_A: 5.431144}),
    }

    PSEUDOSTRUCTURE_FACTOR = {
        NIST_Si: lambda h, k, l: PseudoStructureFactor.structure_factor_diamond_crystal(h, k, l),
        NIST_LaB6: lambda h, k, l: 1,
    }



class ReferenceActionController(object):
    def __init__(self, controller: Controller):
        self.controller = controller
        self._int_spacing = None
        self._pstructure_factor = None

    def set_reference(self, reference: SampleReference):
        self._ref = reference
        self._int_spacing = SampleReference.CRYSTAL_STRUCTURE.value[reference.value]
        self._pstructure_factor = SampleReference.PSEUDOSTRUCTURE_FACTOR.value[reference.value]

    def run(self):
        ctx = self.controller._settings_controller.get_measurement_context()
        ctx.qz_conversion = False
        theta_min, theta_max = ctx.qz_range

        diff_ctx = DiffractionContext()
        diff_ctx._wavelength = ctx.get_wavelength()

        if self._int_spacing is None or self._pstructure_factor is None:
            return

        bragg = BraggCondition(diff_ctx, self._int_spacing)
        hkl = bragg.get_all_hkl(theta_max)
        hkl = self.filter_hkl(hkl, self._pstructure_factor)

        try:

            measurements = self.controller.setup_measurement()
            measurements.set_context(ctx)
            ms = Converter(measurements).convert()
        except BaseException as e:
            self.controller.logger.exception(e)
            return

        self._plot_peaks(bragg, hkl)
        self.controller._plotting.plot([ms], ctx)

    def filter_hkl(self, hkls, filter_fctn):
        return [hkl for hkl in hkls if not filter_fctn(*hkl) == 0]

    def _plot_peaks(self, bragg, hkls):
        thetas = []
        for hkl in hkls:
            h, k, l = hkl
            theta = bragg.get_theta(*hkl)
            if theta in thetas:
                continue
            plt.axvline(theta)
            plt.text(theta, 0, f"[{h} {k} {l}]", horizontalalignment='left')
            thetas.append(theta)
