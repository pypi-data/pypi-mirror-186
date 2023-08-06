import math

from PyQt5.QtWidgets import QTableWidgetItem

from uxdconverter.ui.gui import Ui_UXDConverter
from uxdconverter.transition_energy.database import TransitionDatabase
from uxdconverter.util import get_logger

CONST_H = 6.62607015e-34  # J s
CONST_SPEED_OF_LIGHT = 299792458  # m / s
CONST_HBAR = CONST_H / (2 * math.pi)  # J s
CONST_MASS_NEUTRON = 1.67492749804e-27  # kg
CONST_MASS_PROTON = 1.67262192369e-27  # kg
CONST_MASS_ELECTRON = 9.1093837015e-31  # kg
CONST_ELEMENTARY_CHARGE = 1.602176634e-19  # C
CONST_NUCLEAR_MAGNETON = CONST_ELEMENTARY_CHARGE * CONST_HBAR / 2 / CONST_MASS_PROTON  # J / T
CONST_MU_NEUTRON = -1.91304272 * CONST_NUCLEAR_MAGNETON
CONST_MU_BOHR = CONST_ELEMENTARY_CHARGE * CONST_HBAR / 2 / CONST_MASS_ELECTRON  # J / T

UNIT_meV = 1
UNIT_eV = 2
UNIT_keV = 3
UNIT_MeV = 4
UNIT_MPS = 5
UNIT_J = 6

UNITS_NEUTRON_CONVERSION = [UNIT_eV, UNIT_meV, UNIT_keV, UNIT_MeV, UNIT_MPS, UNIT_J]


class ConversionControllerTab(object):

    def __init__(self, ui: Ui_UXDConverter, app, parent_controller, trans_db: TransitionDatabase):
        self.ui = ui
        self.app = app
        self.logger = get_logger(__name__)
        self._pcontroller = parent_controller
        self._trans_db = trans_db

        self.setup()

    def setup(self):
        self.ui.conversion_to_qz.toggled.connect(self.update_conversion)
        self.ui.conversion_to_theta.toggled.connect(self.update_conversion)

        self.ui.conversion_input_qz.textEdited.connect(self.update_conversion)
        self.ui.conversion_input_theta.textEdited.connect(self.update_conversion)

        self.ui.conversion_input_theta.editingFinished.connect(self.update_radio)
        self.ui.conversion_input_qz.editingFinished.connect(self.update_radio)
        self.ui.conversion_input_theta.selectionChanged.connect(self.update_radio)
        self.ui.conversion_input_qz.selectionChanged.connect(self.update_radio)

        self.ui.pushButton_toSettings.pressed.connect(self.update_wavelength_setting)

        self.ui.conversion_to_theta.setChecked(True)

        self._setup_wavelength()
        self._setup_transition_energies()
        self._setup_wavelength_neutron()

    def _setup_wavelength(self):
        self.ui.conversion_energy.toggled.connect(self.update_wavelength_conversion)
        self.ui.conversion_wavelength.toggled.connect(self.update_wavelength_conversion)
        self.ui.conversion_input_wavelength.textEdited.connect(self.update_wavelength_conversion)
        self.ui.conversion_input_energy.textEdited.connect(self.update_wavelength_conversion)

        self.ui.conversion_input_wavelength.editingFinished.connect(self.update_radio_wavelength)
        self.ui.conversion_input_energy.editingFinished.connect(self.update_radio_wavelength)
        self.ui.conversion_input_wavelength.selectionChanged.connect(self.update_radio_wavelength)
        self.ui.conversion_input_energy.selectionChanged.connect(self.update_radio_wavelength)

        self.ui.conversion_energy.setChecked(True)

    def _setup_wavelength_neutron(self):
        self.ui.conversion_energy_neutron.toggled.connect(self.update_wavelength_neutron_conversion)
        self.ui.conversion_wavelength_neutron.toggled.connect(self.update_wavelength_neutron_conversion)
        self.ui.conversion_input_wavelength_neutron.textEdited.connect(
            self.update_wavelength_neutron_conversion)
        self.ui.conversion_input_energy_neutron.textEdited.connect(self.update_wavelength_neutron_conversion)

        self.ui.conversion_neutron_unit.currentIndexChanged.connect(self.update_wavelength_neutron_conversion)

        self.ui.conversion_input_wavelength_neutron.editingFinished.connect(
            self.update_radio_wavelength_neutron)
        self.ui.conversion_input_energy_neutron.editingFinished.connect(self.update_radio_wavelength_neutron)
        self.ui.conversion_input_wavelength_neutron.selectionChanged.connect(
            self.update_radio_wavelength_neutron)
        self.ui.conversion_input_energy_neutron.selectionChanged.connect(self.update_radio_wavelength_neutron)

        self.ui.conversion_energy_neutron.setChecked(True)

    def _setup_transition_energies(self):
        self.ui.trans_energy_element.textEdited.connect(self.update_transition_table)
        self.ui.trans_energy_transition.textEdited.connect(self.update_transition_table)
        self.ui.trans_energy_table.setColumnWidth(0, 80)
        self.ui.trans_energy_use_selected.clicked.connect(self.select_energy_transition)
        # self.ui.trans_energy_table.horizontalHeader().setSectionResizeMode(2)
        # self.ui.trans_energy_use_experimental.toggled.connect(self.update_transition_table)

    def update_wavelength_setting(self):
        #self.ui.lineEdit_wavelength.setText(self.ui.conversion_input_wavelength.text())
        self._pcontroller._settings_controller.set_wavelength(self.ui.conversion_input_wavelength.text())

    def update_radio(self):
        if self.ui.conversion_input_theta.hasFocus():
            self.ui.conversion_to_qz.setChecked(True)
        elif self.ui.conversion_input_qz.hasFocus():
            self.ui.conversion_to_theta.setChecked(True)

    def update_conversion(self):
        try:
            theta = float(self.ui.conversion_input_theta.text().replace(',', '.'))
            qz = float(self.ui.conversion_input_qz.text().replace(',', '.'))
            ctx = self._pcontroller._settings_controller.get_measurement_context()
            lamb = ctx.wavelength

        except BaseException:
            self.logger.warning("Could get correct input for scattering wavevector conversion")
            theta = 0
            qz = 0
            lamb = 1.54

        try:
            if self.ui.conversion_to_qz.isChecked():
                qz = 4 * math.pi / lamb * math.sin(math.radians(theta))
                self.ui.conversion_input_qz.setText("{:.8f}".format(qz))
            else:
                theta = math.degrees(math.asin(qz * lamb / (4 * math.pi))) % 360.0
                self.ui.conversion_input_theta.setText("{:.8f}".format(theta))

        except BaseException:
            self.logger.warning("Could not calculate the scattering wavevector")

    def update_wavelength_conversion(self):

        try:
            energy = float(self.ui.conversion_input_energy.text().replace(',', '.'))
            wavelength = float(self.ui.conversion_input_wavelength.text().replace(',', '.'))
        except BaseException as e:
            self.logger.warning("Could not get correct input for wavelength conversion")
            energy = 8046
            wavelength = 1.5418

        try:
            if self.ui.conversion_energy.isChecked():
                self.ui.conversion_input_energy.setText("{:.8f}".format(self._to_energy(wavelength)))
            else:
                self.ui.conversion_input_wavelength.setText("{:.8f}".format(self._to_wavelength(energy)))
        except BaseException as e:
            self.logger.warning("Could not calculate the wavelength")

    def _read_neutron_unit(self):
        index = self.ui.conversion_neutron_unit.currentIndex()

        mapping = {
            0: UNIT_meV,
            1: UNIT_eV,
            2: UNIT_keV,
            3: UNIT_MeV,
            4: UNIT_MPS,
            5: UNIT_J
        }

        if index in mapping:
            return mapping[index]

        return UNIT_meV

    def update_wavelength_neutron_conversion(self):
        try:
            energy = float(self.ui.conversion_input_energy_neutron.text().replace(',', '.'))
            wavelength = float(self.ui.conversion_input_wavelength_neutron.text().replace(',', '.'))

            unit = self._read_neutron_unit()

        except BaseException as e:
            self.logger.warning("Could not get correct input for neutron wavelength conversion")
            wavelength = 1
            energy = 1
            unit = UNIT_meV

        try:
            energy = self._unit_prefix(unit, from_energy=energy)
        except BaseException as e:
            self.logger.warning("Undefined unit prefix for neutron wavelength conversion")
            energy = 1e3

        try:
            if self.ui.conversion_energy_neutron.isChecked():
                energy = self._to_neutron_energy(wavelength)
                energy = self._unit_prefix(unit, to_energy=energy)
                self.ui.conversion_input_energy_neutron.setText("{:.5f}".format(energy))
            else:
                self.ui.conversion_input_wavelength_neutron.setText(
                    "{:.5f}".format(self._to_neutron_wavelength(energy)))
        except BaseException as e:
            self.logger.warning("Exception while calculating neutron wavelength")

        e_txt = 'Energy'
        text_mapping = {
            UNIT_meV: (e_txt, 'meV'),
            UNIT_eV: (e_txt, 'eV'),
            UNIT_keV: (e_txt, 'keV'),
            UNIT_MeV: (e_txt, 'MeV'),
            UNIT_MPS: ('Velocity', 'm/s'),
            UNIT_J: (e_txt, 'J')
        }

        energy_txt, unit_txt = text_mapping[unit]
        self.ui.conversion_energy_neutron.setText("{} [{}]".format(energy_txt, unit_txt))

    def update_radio_wavelength_neutron(self):
        if self.ui.conversion_input_energy_neutron.hasFocus():
            self.ui.conversion_wavelength_neutron.setChecked(True)
        elif self.ui.conversion_input_wavelength_neutron.hasFocus():
            self.ui.conversion_energy_neutron.setChecked(True)

    def update_radio_wavelength(self):
        if self.ui.conversion_input_energy.hasFocus():
            self.ui.conversion_wavelength.setChecked(True)
        elif self.ui.conversion_input_wavelength.hasFocus():
            self.ui.conversion_energy.setChecked(True)

    def _to_energy(self, wavelength):
        """
            wavelength is given in angstrom
        :param wavelength:
        :return: energy in eV
        """
        return CONST_H * CONST_SPEED_OF_LIGHT / (wavelength * 1e-10) / CONST_ELEMENTARY_CHARGE

    def _to_wavelength(self, energy):
        """
        energy in eV
        wavelength in Angstrom
        :param energy:
        :return:
        """
        return CONST_H * CONST_SPEED_OF_LIGHT / (energy * CONST_ELEMENTARY_CHARGE) * 1e10

    def _to_neutron_energy(self, wavelength):
        """
        wavelength in AA
        energy in eV
        :param wavelength:
        :return:
        """
        return CONST_H ** 2 / (2 * wavelength ** 2 * 1e-20 * CONST_MASS_NEUTRON) / CONST_ELEMENTARY_CHARGE

    def _to_neutron_wavelength(self, energy):
        """
        energy in eV
        wavelength in AA
        :param energy:
        :return:
        """
        return CONST_H / math.sqrt(2 * energy * CONST_MASS_NEUTRON * CONST_ELEMENTARY_CHARGE) * 1e10

    def _unit_prefix(self, unit, from_energy=None, to_energy=None):
        if not unit in UNITS_NEUTRON_CONVERSION:
            raise RuntimeError("unknown unit")

        if unit == UNIT_MPS:
            if from_energy:
                return 0.5 * CONST_MASS_NEUTRON * from_energy ** 2 / CONST_ELEMENTARY_CHARGE
            if to_energy:
                return math.sqrt(2 * to_energy / CONST_MASS_NEUTRON * CONST_ELEMENTARY_CHARGE)
        # Conversion from eV to ...
        prefix = {
            UNIT_meV: 1e3,
            UNIT_eV: 1e0,
            UNIT_keV: 1e-3,
            UNIT_MeV: 1e-6,
            UNIT_J: CONST_ELEMENTARY_CHARGE
        }

        if from_energy is not None:
            return from_energy / prefix[unit]

        if to_energy is not None:
            return to_energy * prefix[unit]

    def update_transition_table(self):
        element = self.ui.trans_energy_element.text()

        found = self._trans_db.find_all(element)
        if len(found) == 0:
            self.ui.trans_energy_table.setRowCount(0)
            self.ui.trans_energy_table.clearContents()
        elif len(found) == 1:
            self.ui.trans_energy_table.clearContents()
            transitions = self._trans_db.get_all_transitions(found[0],
                                                             filter=self.ui.trans_energy_transition.text())

            self.ui.trans_energy_table.setRowCount(len(transitions))
            for idx, trans in enumerate(transitions):
                e_theory = str(transitions[trans]['theory']) if transitions[trans]['theory'] > 0 else 'NA'
                e_exp = str(transitions[trans]['experimental']) if transitions[trans][
                                                                       'experimental'] > 0 else 'NA'
                self.ui.trans_energy_table.setItem(idx, 0, QTableWidgetItem(found[0]))
                self.ui.trans_energy_table.setItem(idx, 1, QTableWidgetItem(trans))
                self.ui.trans_energy_table.setItem(idx, 2, QTableWidgetItem(e_theory))
                self.ui.trans_energy_table.setItem(idx, 3, QTableWidgetItem(e_exp))

        else:
            self.ui.trans_energy_table.setRowCount(len(found))
            for idx, el in enumerate(found):
                self.ui.trans_energy_table.setItem(idx, 0, QTableWidgetItem(el))
            self.ui.trans_energy_table.rowCount()

    def select_energy_transition(self):
        row = self.ui.trans_energy_table.currentRow()
        column = self.ui.trans_energy_table.currentColumn()

        energy = self.ui.trans_energy_table.item(row, column).text()
        try:
            energy = float(energy)
        except BaseException:
            self.logger.warning("Error while fetching energy from table")
            return

        self.ui.conversion_input_energy.setText(str(energy))
        self.ui.conversion_wavelength.setChecked(True)
        self.update_wavelength_conversion()


def mag_sld_to_mu_bohr(mag_sld):
    # mag_sld is given in 1/AA**2, so convert this to 1/m**2
    mag_sld = mag_sld * 1e20
    B = mag_sld * 2 * math.pi * CONST_HBAR ** 2 / (CONST_MASS_NEUTRON * CONST_MU_NEUTRON)

    return B
    # SLD_m = N * p
    # 2 pi hbar**2/ (m_n µ_n) * SLD_m = B
