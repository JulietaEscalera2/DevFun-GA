import sys

from src.com.jalasoft.SearchFile.view.view import View
from src.com.jalasoft.SearchFile.model.model import Model
from src.com.jalasoft.SearchFile.controller.controller import Controller
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    view = View()
    model = Model()
    controller = Controller(view, model)
    app = QApplication(sys.argv)
    sys.exit(app.exec_())
