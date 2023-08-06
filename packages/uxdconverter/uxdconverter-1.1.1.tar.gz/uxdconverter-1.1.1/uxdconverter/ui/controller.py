import os

from typing import List

from uxdconverter.ui.gui import Ui_UXDConverter
from uxdconverter.ui.graph import Plotting
from uxdconverter.converter import Converter
from uxdconverter.exporter import FileExporter, ParrattExportAlgorithm, ORSOExportAlgorithm
from uxdconverter.measurement import MeasurementContext, Measurements
from uxdconverter.operation import DataNormalization

from PyQt5.QtWidgets import QFileDialog, QTreeWidgetItem, QHeaderView, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal, QObject

from uxdconverter.parser.general import GeneralParser
from uxdconverter.ui.util import shortify_path
from uxdconverter.ui.controllers.settings import SettingsTabController
from uxdconverter.ui.controllers.xrd import XrdControllerTab
from uxdconverter.ui.controllers.conversion import ConversionControllerTab
from uxdconverter.ui.controllers.sld import SldTabController
from uxdconverter.ui.controllers.measurement import MeasurementTabController
from uxdconverter.util import get_logger

from uxdconverter.transition_energy.database import TransitionDatabase

class SignalPropagator(QObject):
    sig = pyqtSignal(list)

class MeasurementFile(object):
    def __init__(self, file, parser):
        self._file = file
        self._parser = parser
        self._measurement = None

    def get_file(self):
        return self._file

    def get_file_shortified(self):
        return shortify_path(self._file, 55)

    def get_measurement(self) -> Measurements:
        if self._measurement is None:
            ms = self._parser.parse(self._file)

            for measurement in ms.get_measurements():
                measurement.file_name = self._file

            self._measurement = ms

        return self._measurement

    def is_same(self, file):
        return file == self._file

    def __eq__(self, other):
        if isinstance(other, MeasurementFile):
            return self._file == other._file
        return False

class Controller(QObject):
    filesChanged = pyqtSignal()

    def __init__(self, ui: Ui_UXDConverter, app):
        super().__init__()
        self.app = app
        self.ui = ui
        self.logger = get_logger(__name__)
        self._parser = GeneralParser(self.logger)
        self._files = [] # type: List[MeasurementFile]


        #self.measurements = None
        self._plotting = Plotting()
        self.setup()

        self._trans_db = TransitionDatabase()

        self._settings_controller = SettingsTabController(ui.settings.ui, app, self)
        self._measurement_controller = MeasurementTabController(self.ui, app, self)
        self._sub_controller = [XrdControllerTab(ui, app, self),
                                ConversionControllerTab(ui, app, self, self._trans_db),
                                SldTabController(ui, app, self._trans_db)]
        self._plugins = {}
        self._views = {}

    def run(self):
        pass

    def setup(self):
        self.ui.pushButton_input.clicked.connect(self.select_file_input)
        self.ui.pushButton_output.clicked.connect(self.select_file_output)
        # self.ui.lineEdit_input.returnPressed.connect(self.read_file)
        self.ui.pushButton_convert.clicked.connect(self.convert)

        # TODO:
        #self.ui.pushbutton_select_graph.clicked.connect(self.plot_with_selection)
        self.ui.pushButton_preview.clicked.connect(self.plot_preview)


        self.ui.pushButton_deletefile.clicked.connect(self.delete_file)
        self.ui.pushButton_addfile.clicked.connect(self.input_file)
        self.ui.pushButton_resetfile.clicked.connect(self.reset)

        self.ui.actionStress.triggered.connect(self.load_stress_plugin)
        self.ui.action_references_LaB6.triggered.connect(lambda: self.load_reference(self.ui.action_references_LaB6))
        self.ui.action_references_Si.triggered.connect(lambda: self.load_reference(self.ui.action_references_Si))

        self.filesChanged.connect(self.update_file_list)

    def load_view(self, view_class):
        view = view_class()

        if view.__class__ in self._views:
            old_view = self._views[view.__class__]
            if not old_view.window.isVisible():
                self._views[view.__class__] = None
            else:
                view = old_view

        self._views[view.__class__] = view
        view.show()
        return view

    def load_stress_plugin(self):
        import traceback
        import sys
        from uxdconverter.plugin.stress.analysis import StressAnalysis, NAME
        try:
            from uxdconverter.ui.views.stress import StressView
            from uxdconverter.ui.controllers.stress import StressAnalysisController

            view = self.load_view(StressView)
            self._plugins[NAME] = StressAnalysisController(view, self.app, self)

            return
            if not (NAME in self._plugins.keys()):
                self._plugins[NAME] = StressAnalysis(self)

            run = self._plugins[NAME]
            run.analyze()
        except Exception as e:
            self.logger.exception(e)
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)
            del exc_info

    def load_reference(self, button):
        from uxdconverter.ui.actions.reference import ReferenceActionController, SampleReference

        reference_name = button.text()

        try:
            reference = SampleReference(reference_name)

            action = ReferenceActionController(self)
            action.set_reference(reference)
            action.run()

        except Exception as e:
            self.logger.exception(e)

    def get_files(self):
        return self._files

    """
    def update_manual_normalization(self, xy_data_point):
        if xy_data_point is None:
            return

        norm = 1 / float(xy_data_point[1])
        self.logger.debug("Normalization factor: {}".format(norm))
        #print("Normalization factor: %s" % str(norm))
        self.ui.lineEdit_normalization_factor.setText(str(norm))
    """

    def check_file(self, file: MeasurementFile):
        try:
            ms = file.get_measurement()

            if ms is not None:
                return ms.get_count_measurements() + ms.get_count_background_measurements()

        except Exception as e:
            self.logger.exception(e)

        return 0

    def reset(self, arbitrary_qt_data=None, message_box=True):
        if message_box is True:
            msg = QMessageBox()
            ret = msg.information(None, "Reset files",
                                  "Are you sure to reset all files?",
                                  buttons=QMessageBox.Ok | QMessageBox.Cancel)
            if ret == QMessageBox.Cancel:
                return

        self._measurement_controller.reset()

        self.ui.lineEdit_input.setText("")
        self.ui.lineEdit_output.setText("")
        self._files = []
        self.filesChanged.emit()

    def delete_file(self):
        root = self.ui.treeWidget_file.invisibleRootItem()
        child_count = root.childCount()
        for i in reversed(range(child_count)):
            item = root.child(i)

            if item.isSelected():
                index = item.data(0, Qt.UserRole)
                del self._files[index]

        if len(self._files) == 0:
            self.ui.lineEdit_output.setText("")

        self.filesChanged.emit()

    def input_file(self):
        self.add_files([self.ui.lineEdit_input.text()])

    def add_files(self, files: List[str]):
        # If a file was added, this is set to true so that
        # the filesChanged signal is emitted only once,
        # and not for every single added file...
        emit_flag = False

        for file in files:
            if file == "":
                continue

            measurement_file = MeasurementFile(file, self._parser)

            # check for duplicate files
            if any([f == measurement_file for f in self._files]):
                msg = QMessageBox()
                ret = msg.information(None, "Input file", f"File {file} is already loaded",
                                          buttons=QMessageBox.Ok)
                continue

            if self.check_file(measurement_file) == 0:
                msg = QMessageBox()
                ret = msg.information(None, "Input file", f"Could not read file {file}",
                                      buttons=QMessageBox.Ok)
                continue

            self._files.append(measurement_file)
            emit_flag = True

        if emit_flag:
            self.filesChanged.emit()

    def update_file_list(self):
        self.ui.treeWidget_file.clear()

        for i, file in enumerate(self._files):
            item = QTreeWidgetItem(self.ui.treeWidget_file)
            item.setFlags(item.flags() | Qt.ItemIsSelectable)
            item.setText(0, f"File {file.get_file_shortified()}")

            fullpath = QTreeWidgetItem(item)
            fullpath.setText(0, f"Path: {file.get_file()}")
            fullpath.setFlags(fullpath.flags() ^ Qt.ItemIsSelectable)

            mscount = QTreeWidgetItem(item)
            mscount.setText(0, f"Measurement count: {self.check_file(file)}")
            mscount.setFlags(mscount.flags() ^ Qt.ItemIsSelectable)
            item.setData(0, Qt.UserRole, i)

    def select_file_input(self):
        files = QFileDialog.getOpenFileNames(filter="UXD/RAW/DAT/XRDML (*.uxd *.raw *.dat *.xrdml);;UXD (*.uxd);;RAW (*.raw);;DAT (*.dat);;XRDML (*.xrdml);;All *.*")[0]

        if len(files) == 0:
            return

        self.ui.lineEdit_input.setText(files[0])
        if self.ui.lineEdit_output.text() == "":
            self.ui.lineEdit_output.setText(files[0].replace('.UXD', '') + ".dat")
            self.ui.lineEdit_output.setText(files[0].replace('.raw', '') + ".dat")
            self.ui.lineEdit_output.setText(files[0].replace('.xrdml', '') + ".dat")

        self.add_files(files)

    def select_file_output(self):
        self.ui.lineEdit_output.setText(QFileDialog.getOpenFileName()[0])

    def convert(self):
        output = self.ui.lineEdit_output.text()
        if output == "":
            msg = QMessageBox()
            msg.warning(None, "No output file", "No output file given")
            return

        output_path = os.path.dirname(os.path.realpath(output))

        try:
            if not os.path.exists(output_path):
                msg = QMessageBox()
                ret = msg.information(None, "Output Directory",
                                      "The directory does not exist. Do you want to create it?",
                                      buttons=QMessageBox.Ok | QMessageBox.Cancel)
                if ret == QMessageBox.Cancel:
                    return

                os.mkdir(output_path)
        except:
            self.logger.warning('Exception while creating path %s', output_path)
            pass

        try:
            measurements = self.setup_measurement()
            ms = Converter(measurements).convert()
        except Exception as e:
            self.logger.exception(e)
            return

        if os.path.exists(output):
            msg = QMessageBox()
            ret = msg.information(None, "Output file", "The output file already exists. Do you want to overwrite it?",
                                  buttons=QMessageBox.Ok | QMessageBox.Cancel)

            if ret == QMessageBox.Cancel:
                return

        export_algo = ORSOExportAlgorithm(ms, measurements.get_context())
        export_algo.set_used_data_files([ms.file_name for ms in measurements.get_measurements()])
        export_algo.set_used_background_files([ms.file_name for ms in measurements.get_background_measurements()])
        #export_algo = ParrattExportAlgorithm(ms, measurements.get_context())
        exporter = FileExporter(output, export_algo)

        exporter.do_export()

        if self.ui.checkBox_view_plot.isChecked():
            self._plotting.plot([ms], measurements.get_context())

    def plot_preview(self):
        try:
            ctx = self._settings_controller.get_measurement_context()
            self._plotting.plot([Converter(self.setup_measurement()).convert()], ctx)
        except Exception as e:
            self.logger.exception(e)

    def setup_measurement(self):
        mss = self._measurement_controller.get_included_measurements()
        mss.set_context(self._settings_controller.get_measurement_context())

        return mss

    def plot_with_selection(self):
        # TODO
        return
        context = self._settings_controller.get_measurement_context()
        context.normalization = 1.0

        if self.measurements is None:
            self.logger.warning("No plotting since no measurements are available")
            return

        self.measurements.set_context(context)
        ms = Converter(self.measurements).convert()
        # ms = convert_measurement(self.measurements)

        signalPropagator = SignalPropagator()
        signalPropagator.sig.connect(self.update_manual_normalization)
        selection = self._plotting.interactive_plot(ms, signalPropagator)

        if selection is None:
            return

        self.ui.lineEdit_normalization_factor.setText(str(1.0 / selection[1]))
