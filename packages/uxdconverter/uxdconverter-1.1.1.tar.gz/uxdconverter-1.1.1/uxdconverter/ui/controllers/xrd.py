import os
import re

from CifFile import ReadCif

from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from PyQt5.QtCore import Qt

from uxdconverter.ui.gui import Ui_UXDConverter
from uxdconverter.diffraction.crystal import CubicSpacing, HexagonalSpacing, TriclinicSpacing, \
    TetragonalSpacing, OrthorhombicSpacing, MonoclinicSpacing, RhombohedralSpacing, InterplanarSpacing, \
    BraggCondition, DiffractionContext
from uxdconverter.util import get_logger

class XrdControllerTab(object):
    SYSTEM_CUBIC = 'cubic'
    SYSTEM_HEXAGONAL = 'hexagonal'
    SYSTEM_TETRAGONAL = 'tetragonal'
    SYSTEM_ORTHORHOMBIC = 'orthorhombic'
    SYSTEM_MONOCLINIC = 'monoclinic'
    SYSTEM_TRICLINIC = 'triclinic'
    SYSTEM_RHOMBOHEDRAL = 'rhombohedral'

    COMBOBOX_MAPPING = {
        0: SYSTEM_CUBIC,
        1: SYSTEM_HEXAGONAL,
        2: SYSTEM_RHOMBOHEDRAL,
        3: SYSTEM_TETRAGONAL,
        4: SYSTEM_ORTHORHOMBIC,
        5: SYSTEM_MONOCLINIC,
        6: SYSTEM_TRICLINIC,
    }

    CLASS_MAPPING = {
        SYSTEM_CUBIC: CubicSpacing,
        SYSTEM_HEXAGONAL: HexagonalSpacing,
        SYSTEM_TETRAGONAL: TetragonalSpacing,
        SYSTEM_ORTHORHOMBIC: OrthorhombicSpacing,
        SYSTEM_MONOCLINIC: MonoclinicSpacing,
        SYSTEM_TRICLINIC: TriclinicSpacing,
        SYSTEM_RHOMBOHEDRAL: RhombohedralSpacing,
    }

    def __init__(self, ui: Ui_UXDConverter, app, parent_controller):
        self.ui = ui
        self.app = app
        self._pcontroller = parent_controller
        self.logger = get_logger(__name__)

        self.system = None

        self.default_hkl_list = [(1, 0, 0), (1, 1, 0), (1, 1, 1),
                                 (2, 0, 0), (2, 1, 0), (2, 1, 1),
                                 (2, 2, 0), (2, 2, 1), (2, 2, 2),

                                 (3, 0, 0), (3, 1, 0), (3, 1, 1),
                                 (3, 2, 0), (3, 2, 1), (3, 2, 2),
                                 (3, 3, 0), (3, 3, 1), (3, 3, 2),
                                 (3, 3, 3),

                                 (4, 0, 0), (4, 1, 0), (4, 1, 1),
                                 (4, 2, 0), (4, 2, 1), (4, 2, 2),
                                 (4, 3, 0), (4, 3, 1), (4, 3, 2),
                                 (4, 3, 3), (4, 4, 0), (4, 4, 1),
                                 (4, 4, 2), (4, 4, 3), (4, 4, 4),

                                 (5, 0, 0), (5, 1, 0), (5, 1, 1)]

        self._updating_view = False

        self.setup()
        self.update_view()

    def setup(self):
        self.ui.button_calculate_bragg.clicked.connect(self.calculate_bragg_peak)
        self.ui.cif_browse.clicked.connect(self.select_file_input)
        self.ui.cif_import.clicked.connect(self.import_cif_file)
        self.ui.combobox_crystalfamily.currentIndexChanged.connect(self.update_view)
        self.ui.lattice_a.textEdited.connect(self.calculate_bragg_peak)
        self.ui.lattice_b.textEdited.connect(self.calculate_bragg_peak)
        self.ui.lattice_c.textEdited.connect(self.calculate_bragg_peak)
        self.ui.lattice_alpha.textEdited.connect(self.calculate_bragg_peak)
        self.ui.lattice_beta.textEdited.connect(self.calculate_bragg_peak)
        self.ui.lattice_gamma.textEdited.connect(self.calculate_bragg_peak)
        self.ui.input_bragg_order.textEdited.connect(self.calculate_bragg_peak)


        self.ui.bragg_table.itemChanged.connect(self.table_change)
        self.ui.bragg_table_2.itemChanged.connect(self.table_change)

        # The converter sometimes doesn't set this correctly :/
        # TODO: just a temporary fix
        self.ui.bragg_table.horizontalHeader().setVisible(True)
        self.ui.bragg_table_2.horizontalHeader().setVisible(True)

    def select_file_input(self):
        files = QFileDialog.getOpenFileName(filter="cif (*.cif);; All *.*")[0]

        self.ui.cif_file.setText(files)

    def table_change(self):
        if not self._updating_view:
            self.calculate_bragg_peak()

    def get_parameter_mapping(self):
        return {
            InterplanarSpacing.PARAMETER_A: self.ui.lattice_a,
            InterplanarSpacing.PARAMETER_B: self.ui.lattice_b,
            InterplanarSpacing.PARAMETER_C: self.ui.lattice_c,
            InterplanarSpacing.PARAMETER_ALPHA: self.ui.lattice_alpha,
            InterplanarSpacing.PARAMETER_BETA: self.ui.lattice_beta,
            InterplanarSpacing.PARAMETER_GAMMA: self.ui.lattice_gamma,
        }

    def set_crystal_family(self, crystal_family):
        if not crystal_family in self.COMBOBOX_MAPPING.values():
            raise RuntimeError("Unknown crystal family given")

        crystal_index = None

        for index, crystal_system in self.COMBOBOX_MAPPING.items():
            if crystal_family == crystal_system:
                crystal_index = index

        self.ui.combobox_crystalfamily.setCurrentIndex(crystal_index)

    def update_view(self):
        system = self.ui.combobox_crystalfamily.currentText()

        if system == self.SYSTEM_CUBIC:
            self.system = CubicSpacing()
        elif system == self.SYSTEM_HEXAGONAL:
            self.system = HexagonalSpacing()
        elif system == self.SYSTEM_MONOCLINIC:
            self.system = MonoclinicSpacing()
        elif system == self.SYSTEM_ORTHORHOMBIC:
            self.system = OrthorhombicSpacing()
        elif system == self.SYSTEM_TETRAGONAL:
            self.system = TetragonalSpacing()
        elif system == self.SYSTEM_TRICLINIC:
            self.system = TriclinicSpacing()
        elif system == self.SYSTEM_RHOMBOHEDRAL:
            self.system = RhombohedralSpacing()
        else:
            return

        params = self.system.get_required_parameters()

        parameter_mapping = self.get_parameter_mapping()

        for parameter in parameter_mapping.keys():
            is_read_only = parameter not in params
            parameter_mapping[parameter].setReadOnly(is_read_only)
            parameter_mapping[parameter].setEnabled(not is_read_only)

    def import_cif_file(self):
        file = self.ui.cif_file.text()

        if not os.path.isfile(file):
            return

        try:
            cf = ReadCif(file)

            search_params = {
                '_cell_length_a': InterplanarSpacing.PARAMETER_A,
                '_cell_length_b': InterplanarSpacing.PARAMETER_B,
                '_cell_length_c': InterplanarSpacing.PARAMETER_C,
                '_cell_angle_alpha': InterplanarSpacing.PARAMETER_ALPHA,
                '_cell_angle_beta': InterplanarSpacing.PARAMETER_BETA,
                '_cell_angle_gamma': InterplanarSpacing.PARAMETER_GAMMA,
            }

            ui_mapping = self.get_parameter_mapping()
            import re
            # find the lattice parameters in the cif file
            for key, entry in cf.items():
                for search_key, search_mapping in search_params.items():
                    if entry.has_key(search_key):
                        try:
                            number = float(entry[search_key])
                        except:
                            number = re.findall(r"[-+]?\d*\.\d+|\d+", entry[search_key])
                            if len(number) == 0:
                                continue
                            number = number[0]
                        ui_mapping[search_mapping].setText(str(number))

            self.system.set_parameter(self.get_lattice_parameters())

            system_class = self.system.detect_system()
            # Now set the input text field for the crystal system
            crystal_family = None
            for key, crystal_class in self.CLASS_MAPPING.items():
                if crystal_class == system_class:
                    crystal_family = key

            self.set_crystal_family(crystal_family)

            self.update_view()

        except BaseException as e:
            print(e)

    def get_lattice_parameters(self):
        parameter = self.get_parameter_mapping()

        for key in self.get_parameter_mapping().keys():
            try:
                parameter[key] = float(parameter[key].text().replace(',', '.'))
            except:
                self.logger.warning("Error fetching lattice parameter")
                parameter[key] = 0.0

        return parameter

    def generate_table(self):

        table = [[], [], [], []]
        hkl_list = self._get_hkl_from_ui()

        for col, l in enumerate([1.54059307, 1.54442756, 0.70931724, 0.71360728]):
            diffr_ctx = DiffractionContext()
            diffr_ctx._wavelength = l
            diffr_ctx._bragg_order = int(self.ui.input_bragg_order.text())
            bragg = BraggCondition(diffr_ctx, self.system)
            self.system.set_parameter(self.get_lattice_parameters())

            for row, hkl in enumerate(hkl_list):
                try:
                    theta = round(bragg.get_theta(hkl[0], hkl[1], hkl[2]), 5)
                    ttheta = 2*theta
                    table[col].append((row, f"{ttheta:.3f}"))
                except BaseException as e:
                    table[col].append((row, " - "))


        #for i in range(len(table)):
            #table[i].sort(key=lambda x: x[1])

        for i, hkl in enumerate(hkl_list):
            hkl = hkl_list[table[0][i][0]]
            print(f"|{self._hkl_to_str(hkl)} | {table[0][i][1]} | {table[1][i][1]} | {table[2][i][1]} | {table[3][i][1]}|")


    def calculate_bragg_peak(self):
        try:
            self._updating_view = True
            diffr_ctx = DiffractionContext()
            diffr_ctx._wavelength = self._pcontroller._settings_controller.get_measurement_context().wavelength
            diffr_ctx._bragg_order = int(self.ui.input_bragg_order.text())

            hkl_list = self._get_hkl_from_ui()

            rows = []
            bragg = BraggCondition(diffr_ctx, self.system)
            self.system.set_parameter(self.get_lattice_parameters())

            for row, hkl in enumerate(hkl_list):
                try:
                    theta = round(bragg.get_theta(hkl[0], hkl[1], hkl[2]), 5)
                except BaseException as e:
                    theta = 0

                thetaitem = QTableWidgetItem(str(theta))
                thetaitem.setFlags(thetaitem.flags() ^ Qt.ItemIsEditable)
                tthetaitem = QTableWidgetItem(str(2 * theta))
                tthetaitem.setFlags(tthetaitem.flags() ^ Qt.ItemIsEditable)

                self.ui.bragg_table_2.rowCount()

                rows.append((QTableWidgetItem(self._hkl_to_str(hkl)), thetaitem, tthetaitem))

            def append_to_table(table, rows):
                for row in rows:
                    index = table.rowCount()
                    table.setRowCount(index + 1)
                    table.setItem(index, 0, row[0])
                    table.setItem(index, 1, row[1])
                    table.setItem(index, 2, row[2])

            row1 = rows[:len(rows) // 2]
            row2 = rows[len(rows) // 2:]
            for rows, table in [(row1, self.ui.bragg_table), (row2, self.ui.bragg_table_2)]:
                table.clearContents()
                table.setRowCount(0)
                append_to_table(table, rows)

            #self.generate_table()
        except BaseException as e:
            self.logger.exception(e)
        finally:
            self._updating_view = False

    def _hkl_to_str(self, hkl):
        return str(hkl[0]) + " " + str(hkl[1]) + " " + str(hkl[2])

    def _str_to_hkl(self, string):
        hkls = re.findall(r"(\d{1,})\s*(\d{1,})\s(\d{1,})", string)
        if len(hkls) > 0:
            return tuple(map(int, hkls[0]))
        return (0, 0, 0)

    def _get_hkl_from_ui(self):
        hkl = []
        for table in [self.ui.bragg_table, self.ui.bragg_table_2]:
            for row in range(0, table.rowCount()):
                hkl.append(self._str_to_hkl(table.item(row, 0).text()))

        if len(hkl) == 0:
            return self.default_hkl_list

        # sort now :)
        self.system.set_parameter(self.get_lattice_parameters())
        hkl.sort(key=lambda x: self.system.get_spacing(*x), reverse=True)
        #self.system.get_spacing(h, k, l)

        return hkl
