import sys

from src.com.jalasoft.SearchFile.model.model import Model
from src.com.jalasoft.SearchFile.controller.controller import Controller
from PyQt5.QtWidgets import QApplication
from src.com.jalasoft.SearchFile.view.criteria_main_view import MainView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MainView()
    model = Model()
    controller = Controller(view, model)
    sys.exit(app.exec())

