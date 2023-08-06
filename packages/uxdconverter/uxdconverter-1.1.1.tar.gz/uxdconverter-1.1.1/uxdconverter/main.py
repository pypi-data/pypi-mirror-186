import sys
from PyQt5 import QtWidgets
from uxdconverter.ui.gui import Ui_UXDConverter
from uxdconverter.ui.controller import Controller

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    UXDConverter = QtWidgets.QMainWindow()
    ui = Ui_UXDConverter()
    ui.setupUi(UXDConverter)
    UXDConverter.show()

    controller = Controller(ui, app)
    controller.run()
    sys.exit(app.exec_())
