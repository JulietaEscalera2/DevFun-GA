import sys

from src.com.jalasoft.SearchFile.view.main_view import View
from src.com.jalasoft.SearchFile.model.model import Model
from src.com.jalasoft.SearchFile.controller.controller import Controller
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    model = Model()
    controller = Controller(view, model)
    sys.exit(app.exec())

