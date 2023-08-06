from typing import List

from PyQt5.QtWidgets import QTreeWidgetItem, QHeaderView
from PyQt5.QtCore import Qt

from uxdconverter.measurement import Measurements, Measurement
from uxdconverter.ui.util import shortify_path
from uxdconverter.ui.graph import Plotting

from uxdconverter.util import get_logger

class MeasurementTabController(object):
    def __init__(self, ui, app, parent_controller):
        self.ui = ui
        self.app = app
        self._pcontroller = parent_controller
        self.setup()
        self.measurements = None # type: List[Measurements]
        self._plotting = Plotting()
        self.logger = get_logger(__name__)
        self._settings_updated = False

    def setup(self) -> None:
        self._pcontroller.filesChanged.connect(self.update_measurements)
        self.ui.pushButton_plot.clicked.connect(self.plot_selected_measurements)

    def add_measurement(self, measurement: Measurement, id, is_background=False) -> None:
        # context = self.create_context()

        item = QTreeWidgetItem(self.ui.measurements)
        item.setFlags(item.flags() | Qt.ItemIsSelectable | Qt.ItemIsEditable)
        item.setText(0, measurement.get_display_name())
        item.setData(0, Qt.UserRole, id)
        item.setData(1, Qt.UserRole, is_background)
        item.setData(2, Qt.UserRole, measurement.file_name)

        region = QTreeWidgetItem(item)
        data_region = measurement.get_data_region_x()
        region.setText(0, f"Theta [deg]: {data_region[1]} ... {data_region[0]}")
        # region.setText(1, "Qz [Ang]: %s ... %s" % (datapoint_to_qz(data_region[1], context), datapoint_to_qz(data_region[0], context)))
        region.setFlags(region.flags() ^ Qt.ItemIsSelectable)

        if not measurement.get_psi() == 0:
            region.setText(1, f"Psi [deg]: {measurement.get_psi()}")

        include = QTreeWidgetItem(item)
        include.setText(0, "Include")
        include.setText(1, "Background")
        include.setFlags((include.flags() | Qt.ItemIsUserCheckable) ^ Qt.ItemIsSelectable)
        include.setCheckState(0, Qt.Checked)

        if is_background:
            include.setCheckState(1, Qt.Checked)
        else:
            include.setCheckState(1, Qt.Unchecked)

        if measurement.file_name is not None:
            file = QTreeWidgetItem(item)
            file.setText(0, f"File: {shortify_path(measurement.file_name, 30)}")
            file.setFlags(region.flags() ^ Qt.ItemIsSelectable)
            file.setToolTip(0, measurement.file_name)

    def reset(self):
        self._settings_updated = False

    def update_measurements(self) -> None:
        self.measurements = [file.get_measurement() for file in self._pcontroller.get_files()]

        if len(self.measurements) > 0 and self._settings_updated is False:
            self._settings_updated = True
            self._pcontroller._settings_controller.apply_context(self.measurements[0].get_context())

        self.update_measurement_view()

    def update_measurement_view(self) -> None:
        self.ui.measurements.clear()
        for i, measurements in enumerate(self.measurements):
            for j, ms in enumerate(measurements.get_measurements()):
                ms.set_display_name(f"Measurement {i+1}.{j+1}")
                self.add_measurement(ms, (i, j), False)

            for j, ms in enumerate(measurements.get_background_measurements()):
                ms.set_display_name(f"Background {i+1}.{j+1}")
                self.add_measurement(ms, (i, j), True)

            self.ui.measurements.header().setSectionResizeMode(0, QHeaderView.ResizeToContents)
            self.ui.measurements.header().setSectionResizeMode(1, QHeaderView.ResizeToContents)

    def get_measurements(self):
        raise DeprecationWarning("Should not be used anymore")
        return self.measurements

    def get_measurements(self, filter=None) -> Measurements:
        measurements = []
        background = []

        # Find the appropriate measurements and background
        root = self.ui.measurements.invisibleRootItem()

        child_count = root.childCount()
        for i in range(child_count):
            item = root.child(i)

            if filter is not None:
                if not filter(item):
                    continue

            i, j = item.data(0, Qt.UserRole)
            is_background = item.data(1, Qt.UserRole)
            use_as_background = item.child(1).checkState(1) == Qt.Checked

            if is_background:
                ms = self.measurements[i].get_background_measurements()
            else:
                ms = self.measurements[i].get_measurement(j)

            if use_as_background:
                background.append(ms)
            else:
                measurements.append(ms)

        if len(measurements) + len(background) == 0:
            return None

        return Measurements(None, measurements, background, None)

    def get_selected_measurements(self) -> Measurements:
        return self.get_measurements(lambda item: item.isSelected())

    def get_included_measurements(self) -> Measurements:
        return self.get_measurements(lambda item: item.child(1).checkState(0) == Qt.Checked)

    def plot_selected_measurements(self) -> None:
        try:
            mss = self.get_selected_measurements()

            if mss is None:
                return

            ctx = self._pcontroller._settings_controller.get_measurement_context()
            # Set it to false, to display theta values
            ctx.qz_conversion = False

            measurements = mss.get_measurements() + mss.get_background_measurements()
            names = [ms.get_display_name() for ms in measurements]
            self._plotting.plot(measurements, ctx, names, True)

        except Exception as e:
            self.logger.exception(e)
