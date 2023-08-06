from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from uxdconverter.ui.widgets.stress import Ui_StressAnalysis


class StressView():
    def __init__(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_StressAnalysis()
        self.ui.setupUi(self.window)
        self.add_canvas()
        self.set_stretch_splitter()

    def add_canvas(self):
        self.canvas_layout = QtWidgets.QVBoxLayout()

        self.canvas_widget = QtWidgets.QWidget()
        self.canvas_widget.setLayout(self.canvas_layout)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.window)
        self.canvas_layout.addWidget(self.canvas)
        self.canvas_layout.addWidget(self.toolbar)
        self.ui.splitter.addWidget(self.canvas_widget)

    def show(self):
        self.window.show()

    def set_stretch_splitter(self):
        # not supported by QtDesigner?
        # So we do it manually
        self.ui.splitter.setStretchFactor(0, 1)
        self.ui.splitter.setStretchFactor(1, 2)

