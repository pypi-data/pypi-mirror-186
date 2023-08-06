import math
import numpy as np
import periodictable.constants

from periodictable.xsf import xray_sld, xray_wavelength
from periodictable.nsf import neutron_sld, neutron_scattering
from periodictable.formulas import formula

from uxdconverter.units.si import SI
from uxdconverter.units.wavelength import Wavelength

from uxdconverter.transition_energy.database import TransitionDatabase
from uxdconverter.ui.gui import Ui_UXDConverter

from uxdconverter.ui.util import hightlight

SI_PREFIX = {
    'M': 1e6,
    'k': 1e3,
    'd': 1e-1,
    'c': 1e-2,
    'm': 1e-3,
    'µ': 1e-6,
    'n': 1e-9,
    'p': 1e-12,
    'f': 1e-15,
}

EMISSON_LINES = {
    'Ka1': 'KL3',
    'Ka2': 'KL2',
    'Kb': 'KM3',
    # Ka has to be the last element, as we iterate through it and it conflicts with Ka1
    'Ka': 'KL3',
}


class SldTabController(object):
    def __init__(self, ui: Ui_UXDConverter, app, trans_db: TransitionDatabase):
        self.ui = ui
        self._app = app
        self._trans_db = trans_db

        self.setup()

    @staticmethod
    def _r(f):
        r = lambda x: round(x, 6)
        if isinstance(f, list) or isinstance(f, tuple) or isinstance(f, np.ndarray):
            return [r(fs) for fs in f]

        return r(f)

    def setup(self):
        self.ui.btn_SLD_calculate.clicked.connect(self.calculate)
        self.ui.lE_SLD_sample_material.returnPressed.connect(self.calculate)
        self.ui.lE_SLD_sample_density.returnPressed.connect(self.calculate)
        self.ui.lE_SLD_sample_thickness.returnPressed.connect(self.calculate)

    def _log_ex(self, exception):
        print(exception)

    def calculate(self):
        compound = self.get_compound()
        wavelength_n = self.get_neutron_wavelength()
        wavelength_x = self.get_xray_wavelength()
        thickness = self.get_thickness()

        if compound is None or compound.density is None or wavelength_x is None or wavelength_n is None or thickness is None:
            return

        res = neutron_scattering(compound, density=compound.density, wavelength=wavelength_n)

        if res == (None, None, None):
            hightlight(self.ui.lE_SLD_sample_material)
            self._log_ex("missing neutron cross sections")
            return

        try:
            self.calculate_penetration_depth(compound, wavelength_n, wavelength_x, thickness)
            self.calculate_sld(compound, wavelength_n, wavelength_x)
            self.calculate_cross_sections(compound, wavelength_n, wavelength_x)
            self.calculate_critical_reflection(wavelength_n, wavelength_x)
        except Exception as e:
            self._log_ex(e)

    def calculate_cross_sections(self, compound, wavelength_n, wavelength_x):
        #_, xs, _ = neutron_scattering(compound, density=compound.density, wavelength=wavelength_n)

        num_atoms = 0
        xs_coh, xs_incoh, xs_abs = 0, 0, 0
        for element, quantity in compound.atoms.items():
            if not element.neutron.has_sld():
                return

            xs_coh += quantity * element.neutron.coherent
            xs_incoh += quantity * element.neutron.incoherent
            xs_abs += quantity * element.neutron.absorption

            num_atoms += quantity

        xs_abs /= periodictable.nsf.ABSORPTION_WAVELENGTH * wavelength_n

        xs = np.array([xs_coh, xs_abs, xs_incoh])

        #xs_coh, xs_abs, xs_incoh = xs
        xs_coh, xs_abs, xs_incoh = self._r(xs / num_atoms)
        xs_scatt = self._r(xs_coh + xs_incoh)
        xs_total = self._r(xs_scatt + xs_abs)

        self.ui.lE_xs_neutron_coh.setText(f"{xs_coh}")
        self.ui.lE_xs_neutron_abs.setText(f"{xs_abs}")
        self.ui.lE_xs_neutron_incoh.setText(f"{xs_incoh}")
        self.ui.lE_xs_neutron_scatt.setText(f"{xs_scatt}")
        self.ui.lE_xs_neutron_total.setText(f"{xs_total}")

    def calculate_penetration_depth(self, compound, wavelength_n, wavelength_x, thickness):
        _, xs, _ = neutron_scattering(compound, density=compound.density, wavelength=wavelength_n)
        sld_x_real, sld_x_imag = xray_sld(compound, density=compound.density, wavelength=wavelength_x)

        xs_coh, xs_abs, xs_incoh = xs
        p_abs, p_abs_incoh, p_abs_incoh_coh = [1 / xs_abs, 1/(xs_abs+xs_incoh), 1 / (xs_abs+xs_coh+xs_incoh)]
        p_abs_r, p_abs_incoh_r, p_abs_incoh_coh_r = self._r([p_abs, p_abs_incoh, p_abs_incoh_coh])

        # not 100% sure about the 1/2...
        p_abs_xray = 1 / (2 * wavelength_x * sld_x_imag * 1e-6) * 1e-4

        tr_att = lambda d, pen: (np.exp(-d / pen) * 100, np.exp(d / pen))
        # thickness is in [m], p_abs_incoh in [cm], thus 1e-2
        tr_n, att_n = tr_att(thickness, p_abs_incoh * 1e-2)
        # p_abs_xray in [µm], thus 1e-6
        tr_x, att_x = tr_att(thickness, p_abs_xray * 1e-6)

        self.ui.lE_SLD_pendepth_neutron_abs.setText(f"{p_abs_r}")
        self.ui.lE_SLD_pendepth_neutron_abs_incoh.setText(f"{p_abs_incoh_r}")
        self.ui.lE_SLD_pendepth_neutron_abs_incoh_coh.setText(f"{p_abs_incoh_coh_r}")
        self.ui.lE_SLD_pendepth_neutron_transmission.setText(f"{tr_n} %")
        self.ui.lE_SLD_pendepth_neutron_attenuation.setText(f"{att_n}")

        self.ui.lE_SLD_pendepth_xray_abs.setText(f"{self._r(p_abs_xray)}")
        self.ui.lE_SLD_pendepth_xray_transmission.setText(f"{tr_x} %")
        self.ui.lE_SLD_pendepth_xray_attenuation.setText(f"{att_x}")

    def calculate_sld(self, compound, neutron_wavelength, xray_wavelength):
        wavelength_n = neutron_wavelength
        wavelength_x = xray_wavelength
        density = compound.density

        n_real, n_imag, n_incoh = self._r(neutron_sld(compound, density=density, wavelength=wavelength_n))
        x_real, x_imag = self._r(xray_sld(compound, density=density, wavelength=wavelength_x))

        self.ui.lE_SLD_neutron_real.setText(f"{n_real}")
        self.ui.lE_SLD_neutron_imag.setText(f"{n_imag}")
        self.ui.lE_SLD_neutron_incoh.setText(f"{n_incoh}")

        self.ui.lE_SLD_xray_real.setText(f"{x_real}")
        self.ui.lE_SLD_xray_imag.setText(f"{x_imag}")

    def calculate_critical_reflection(self, neutron_wavelength, xray_wavelength):
        qc = lambda wavelength, sld: self._r(math.sqrt(16*math.pi*sld))
        thetac = lambda wavelength, sld: self._r(math.degrees(math.asin(math.sqrt(sld/math.pi) * wavelength)))

        try:
            # Units are 10^-6 [AA^-2]
            sld_xray = float(self.ui.lE_SLD_xray_real.text()) * 1e-6
            sld_neutron = float(self.ui.lE_SLD_neutron_real.text()) * 1e-6
        except:
            return

        self.ui.lE_critical_angle_xray.setText(f"{thetac(xray_wavelength, sld_xray)}")
        self.ui.lE_critical_wavevector_xray.setText(f"{qc(xray_wavelength, sld_xray)}")
        self.ui.lE_critical_angle_neutron.setText(f"{thetac(neutron_wavelength, sld_neutron)}")
        self.ui.lE_critical_wavevector_neutron.setText(f"{qc(neutron_wavelength, sld_neutron)}")

    def get_neutron_wavelength(self):
        """
        Returns the neutron wavelength in [AA]
        :return:
        """
        wavelength_str = self.ui.lE_source_neutron.text()
        try:
            wavelength = float(wavelength_str.replace('AA', '').replace('Ang', ''))
            if wavelength > 0:
                return wavelength
        except BaseException as e:
            hightlight(self.ui.lE_source_neutron)
            self._log_ex(e)

        return None

    def get_xray_wavelength(self):
        """
        Returns the xray wavelength in [AA]
        :return:
        """
        wavelength_str = self.ui.lE_source_xray.text()
        try:
            return Wavelength.from_string(wavelength_str, self._trans_db)
        except Exception as e:
            self._log_ex(e)
            hightlight(self.ui.lE_source_xray)
            return None

    def get_compound(self):
        compound_str = self.ui.lE_SLD_sample_material.text()
        density = self.get_density()

        if compound_str == "":
            hightlight(self.ui.lE_SLD_sample_material)
            return None

        return formula(compound_str, density=density)

    def get_density(self):
        density_str = self.ui.lE_SLD_sample_density.text()

        if density_str == '':
            return None

        try:
            return float(density_str)
        except BaseException as e:
            hightlight(self.ui.lE_SLD_sample_density)
            self._log_ex(e)
            return None

    def get_thickness(self):
        """
        Returns the thickness in [m]
        :return:
        """
        thickness_str = self.ui.lE_SLD_sample_thickness.text()
        if thickness_str == '':
            return 1e-2  # 1 cm is default

        try:
            return SI.extract_number(thickness_str, 'm')
        except Exception as e:
            self._log_ex(e)
            hightlight(self.ui.lE_SLD_sample_thickness)
            return None
