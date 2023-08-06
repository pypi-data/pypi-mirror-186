from uxdconverter.measurement import MeasurementContext
from uxdconverter.ui.widgets.settings import Ui_Settings
from uxdconverter.enums import DataNormalizationMethod
from uxdconverter.units.wavelength import Wavelength
from uxdconverter.util import get_logger


class SettingsModel():
    def __init__(self, ui: Ui_Settings, xray_database):
        self.ui = ui
        self._db = xray_database

    def read_float(self, line_edit):
        return float(line_edit.text().replace(',', '.'))

    def read_checkbox(self, checkbox):
        return bool(checkbox.isChecked())

    def read_radio(self, radio):
        return bool(radio.isChecked())

    def read_wavelength(self):
        return Wavelength.from_string(self.ui.wavelength.text(), self._db)

    def set_wavelength(self, wavelength):
        self.ui.wavelength.setText(f"{wavelength}")

    def read_beam_width(self):
        return self.read_float(self.ui.beam_width)

    def read_sample_length(self):
        return self.read_float(self.ui.sample_length)

    def read_data_range(self):
        return self.read_float(self.ui.data_range_min), self.read_float(self.ui.data_range_max)

    def set_data_range(self, data_range):
        self.ui.data_range_min.setText(f"{data_range[0]}")
        self.ui.data_range_max.setText(f"{data_range[1]}")

    def read_wavelength_error(self):
        return self.read_float(self.ui.wavelength_error)

    def read_theta_error(self):
        return self.read_float(self.ui.theta_error)

    def read_normalization_factor(self):
        return self.read_float(self.ui.normalization_factor)

    def set_normalization_factor(self, factor):
        self.ui.normalization_factor.setText(f"{factor}")

    def read_knife_edge(self):
        return self.read_checkbox(self.ui.knige_edge)

    def set_knife_edge(self, state):
        self.ui.knige_edge.setChecked(state)


    def read_average_data(self):
        return self.read_checkbox(self.ui.average_data)

    def read_convert_qz(self):
        return self.read_checkbox(self.ui.convert_qz)

    def set_convert_qz(self, state):
        self.ui.convert_qz.setChecked(state)

    def read_plot_log_scale(self):
        return self.read_checkbox(self.ui.plot_log_scale)

    def read_normalization_max(self):
        return self.read_radio(self.ui.normalization_max)

    def read_normalization_flank(self):
        return self.read_radio(self.ui.normalization_flank)

    def read_normalization_manual(self):
        return self.read_radio(self.ui.normalization_manual)

    def read_normalization_method(self):
        if self.read_normalization_max():
            return DataNormalizationMethod.MAX
        if self.read_normalization_flank():
            return DataNormalizationMethod.FLANK
        if self.read_normalization_factor():
            return DataNormalizationMethod.FACTOR

        raise RuntimeError("Unimplemented normalization method?")

    def set_normalization_method(self, method):
        if method == DataNormalizationMethod.MAX:
            self.ui.normalization_max.setChecked(True)
        if method == DataNormalizationMethod.FLANK:
            self.ui.normalization_flank.setChecked(True)
        if method == DataNormalizationMethod.FACTOR:
            self.ui.normalization_manual.setChecked(True)


class SettingsTabController(object):
    def __init__(self, ui: Ui_Settings, app, parent_controller):
        self.ui = ui
        self.app = app
        self._logger = get_logger(__name__)

        self.model = SettingsModel(self.ui, parent_controller._trans_db)
        self.setup()

    def setup(self):
        self.ui.convert_qz.clicked.connect(self.update_label_data)

    def update_label_data(self):
        if self.model.read_convert_qz():
            self.ui.label_cropping.setText("Qz range [A^-1]")
        else:
            self.ui.label_cropping.setText("Theta range [deg]")

    def get_measurement_context(self) -> MeasurementContext:
        ctx = MeasurementContext()

        ctx.wavelength = self.model.read_wavelength()
        ctx.wavelength_error = self.model.read_wavelength_error()

        ctx.average_overlapping = self.model.read_average_data()
        ctx.knife_edge = self.model.read_knife_edge()
        ctx.sample_length = self.model.read_sample_length()
        ctx.xray_width = self.model.read_beam_width()
        ctx.qz_conversion = self.model.read_convert_qz()
        ctx.y_log_scale = self.model.read_plot_log_scale()

        ctx.theta_error = self.model.read_theta_error()

        range_1, range_2 = self.model.read_data_range()
        ctx.qz_range = (min(range_1, range_2), max(range_1, range_2))

        ctx.normalization = self.model.read_normalization_method()
        ctx.normalization_factor = self.model.read_normalization_factor()

        return ctx

    def apply_context(self, context: MeasurementContext):
        self.model.set_wavelength(context.wavelength)
        self.model.set_convert_qz(context.qz_conversion)
        self.model.set_data_range(context.qz_range)
        self.model.set_normalization_factor(context.normalization_factor)
        self.model.set_normalization_method(context.normalization)
        self.model.set_knife_edge(context.knife_edge)

    def set_wavelength(self, wavelength):
        self.model.set_wavelength(wavelength)
