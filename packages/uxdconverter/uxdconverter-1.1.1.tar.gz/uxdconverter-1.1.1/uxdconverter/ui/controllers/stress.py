import math

from typing import List
from collections import defaultdict

import matplotlib as mpl
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidgetItem, QHeaderView

from uxdconverter.measurement import Measurement, Measurements, MeasurementContext
from uxdconverter.ui.views.stress import StressView

from uxdconverter.plugin.stress.analysis import StressAnalysis
from uxdconverter.operation import MultiMerger, MeasurementMerger, ErrorCalculation

from cycler import cycler
from enum import Enum, auto

class TreeBehavior(Enum):
    # plot only a single measurement
    SINGLE_MEASUREMENT = auto()
    # plot only the merged measurement, merged based on the psi angle
    MERGED_MEASUREMENT = auto()
    # plot all measurements with the same psi angle, but not merged
    MULTIPLE_MEASUREMENT = auto()

class MeasurementTreeData(object):
    def __init__(self):
        self._measurements = []
        self._grouped = defaultdict(list)

    def add_measurements(self, measurements: Measurements):
        for ms in measurements.get_measurements():
            self.add_measurement(ms)

    def add_measurement(self, measurement: Measurement):
        self._measurements.append(measurement)
        self._add_to_group(measurement)

    def _add_to_group(self, measurement: Measurement):
        self._grouped[round(measurement.get_psi(), 3)].append(measurement)

    def get_group(self):
        return list(self._grouped.values())

    def merge(self, ctx: MeasurementContext):
        multi_merge = MultiMerger(MeasurementMerger())
        err = ErrorCalculation()
        self._merged = [err.manipulate(multi_merge.merge(group), ctx) for group in self._grouped.values()]

        for index, psi in enumerate(self._grouped.keys()):
            ms = self._merged[index]
            ms.set_psi(psi)
            ms.set_display_name(f"Merged: $\psi$ = {psi}")

    def get_merged(self):
        return self._merged

class StressAnalysisController(object):
    def __init__(self, view: StressView, app, parent_controller):
        self.view = view
        self.ui = view.ui
        self.app = app
        self._pcontroller = parent_controller
        self._measurements = None
        self._analysis = StressAnalysis(self)
        self.figure = self.view.figure
        self.canvas = self.view.canvas
        self.setup()
        self.sync_measurements()

    def setup(self):
        selection_model = self.ui.measurements.selectionModel()
        selection_model.selectionChanged.connect(self.plot)
        self._pcontroller.filesChanged.connect(self.sync_measurements)

    def sync_measurements(self):
        self._measurements = MeasurementTreeData()
        self._measurements.add_measurements(self._pcontroller._measurement_controller.get_included_measurements())
        self._measurements.merge(self._pcontroller._settings_controller.get_measurement_context())
        self.update_measurement_view()

    def plot(self):
        #data = [random.random() for i in range(10)]
        #import random
        #measurement = random.choice(self._pcontroller._measurement_controller.get_included_measurements().get_measurements()) # type: Measurement

        selection = self.ui.measurements.selectionModel()
        selection.selectedIndexes()

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        ax.set_xlabel(r"$\theta$ [deg]")
        ax.set_ylabel("Intensity [1]")

        color_cycle = mpl.rcParams['axes.prop_cycle']
        merged_color_cycle = cycler(mpl.rcParams['axes.prop_cycle'])
        selected_items = [self.ui.measurements.itemFromIndex(index) for index in selection.selectedRows(0)]

        for item in selected_items:
            # data contains the group_index and measurement_index (if available)
            data = item.data(0, Qt.UserRole)
            # This tells us what the item is representing, ie what type of item is selected
            behavior = TreeBehavior(item.data(1, Qt.UserRole))

            # see https://matplotlib.org/stable/users/dflt_style_changes.html#colors-in-default-property-cycle

            # Note:
            # color_cycle contains the color cycle (obvious) of the default matplotlib color cycle
            # What we want to achieve here:
            # The ''Measurements'' item shows all measurements with the same psi value
            # and all these measurements have a different color based on the color cycle.
            # Now, if we go to the second measurement, we want to have the color match the color of the
            # ``overall'' picture, thus we need to advance the color cycle.
            # This can be done by slicing and concatenating the cycler (there is no simple ``offset'' :/ ):
            # c[i:].concat(c[:i]) is equal to c but moved forward by i steps.
            # This is just a fancy service for the user ...
            # see https://matplotlib.org/cycler/#concatenation

            if behavior == TreeBehavior.SINGLE_MEASUREMENT:
                # plot only a single measurement
                measurements = [self._measurements.get_group()[data[0]][data[1]]]
                color_cycle = color_cycle[data[1]:].concat(color_cycle[:data[1]])
                fmt = '*--'
            elif behavior == TreeBehavior.MERGED_MEASUREMENT:
                # plot only the merged measurement
                measurements = [self._measurements.get_merged()[data[0]]]
                color_cycle = merged_color_cycle
                merged_color_cycle = merged_color_cycle[1:].concat(merged_color_cycle[:1])
                fmt = '*-'
            elif behavior == TreeBehavior.MULTIPLE_MEASUREMENT:
                # plot all measurements with the particular psi angle
                measurements = self._measurements.get_group()[data[0]]
                color_cycle = mpl.rcParams['axes.prop_cycle']
                fmt = '*--'

            # What is zip(..., color_cycle) doing? see https://matplotlib.org/cycler/#examples
            for ms, color in zip(measurements, color_cycle):
                theta, dTheta, Int, dInt = zip(*ms.get_data())
                # **color will yield key=value
                # where key="color" (key of the cycler) and value is the current value of the cycle
                ax.errorbar(theta, Int, xerr=dTheta, yerr=dInt, fmt=fmt, label=ms.get_display_name(), **color)

        ax.legend()

        # refresh canvas
        self.canvas.draw()

    def _add_measurement_to_view(self, group_index, measurements: List[Measurement]):

        if len(measurements) == 0:
            return

        measurement = measurements[0]

        item = QTreeWidgetItem(self.ui.measurements)
        item.setFlags(item.flags() | Qt.ItemIsSelectable)
        item.setText(0, f"ψ = {measurement.get_psi():.2f}")
        item.setText(1, f"sin²(ψ) = {math.sin(math.radians(measurement.get_psi())**2):.3f}")
        item.setData(0, Qt.UserRole, (group_index,))
        item.setData(1, Qt.UserRole, TreeBehavior.MERGED_MEASUREMENT)

        measurement_item = QTreeWidgetItem(item)
        measurement_item.setText(0, "Measurements")
        measurement_item.setData(0, Qt.UserRole, (group_index, ))
        measurement_item.setData(1, Qt.UserRole, TreeBehavior.MULTIPLE_MEASUREMENT)

        for index, measurement in enumerate(measurements):
            measurement_name = QTreeWidgetItem(measurement_item)
            measurement_name.setText(0, f"{measurement.get_display_name()}")
            measurement_name.setData(0, Qt.UserRole, (group_index, index))
            measurement_name.setData(1, Qt.UserRole, TreeBehavior.SINGLE_MEASUREMENT)

    def update_measurement_view(self):
        self.ui.measurements.clear()
        grouped_measurements = self._measurements.get_group()

        for group_index, ms in enumerate(grouped_measurements):
            self._add_measurement_to_view(group_index, ms)

        self.ui.measurements.header().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.ui.measurements.header().setSectionResizeMode(1, QHeaderView.ResizeToContents)