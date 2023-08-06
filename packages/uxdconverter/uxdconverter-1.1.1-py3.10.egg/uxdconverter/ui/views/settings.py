from PyQt5.QtWidgets import QWidget
from uxdconverter.ui.widgets.settings import Ui_Settings

class SettingsWidget(QWidget):
    def __init__(self, ui_tab):
        super().__init__()

        settings = Ui_Settings()
        settings.setupUi(ui_tab)
        self.ui = settings
