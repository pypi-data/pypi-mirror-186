import os

from PyQt5.QtCore import QCoreApplication, QRunnable, QThreadPool
from time import sleep

class Highlighter(QRunnable):
    def __init__(self, ui_element):
        super(Highlighter, self).__init__()
        self.ui = ui_element

    def run(self):
        stylesheet_before = self.ui.styleSheet()
        highlight = "background-color: red;"
        if stylesheet_before == highlight:
            stylesheet_before = ""

        self.ui.setStyleSheet(highlight)
        sleep(0.1)
        self.ui.setStyleSheet(stylesheet_before)
        sleep(0.1)
        self.ui.setStyleSheet(highlight)
        sleep(0.1)
        self.ui.setStyleSheet(stylesheet_before)
        sleep(0.1)
        self.ui.setStyleSheet(highlight)
        sleep(0.5)
        self.ui.setStyleSheet(stylesheet_before)

def hightlight(ui):
    runnable = Highlighter(ui)
    QThreadPool.globalInstance().start(runnable)

def shortify_path(path, length):

    if len(path) <= length:
        return path

    if length <= 0:
        return path[-length + 1:]

    path = os.path.normpath(path)
    file = os.path.split(path)[1]

    if len(file) > length:
        return "..." + file[-length:]

    mod_path = path
    prev_file = file
    while len(file) < length:
        prev_file = file
        mod_path = os.path.dirname(mod_path)
        file = path[+len(mod_path) - len(path):]

    return "..." + prev_file