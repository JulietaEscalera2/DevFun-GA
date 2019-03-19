from PyQt5.QtWidgets import QMenu, QMainWindow
from src.com.jalasoft.SearchFile.view.productView import ProductView


class View(QMainWindow):

from src.com.jalasoft.SearchFile.view.productView import ProductView


class View(QMainWindow):

    # def __init__(self):
    #     print('view')
    #
    # def initUI(self):
    #     print("initUI")
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.setWindowTitle('Search File')
        self.__initComponent()
        self.show()

    def __initComponent(self):

        self.resize(1000, 1500)
        menuBar = self.menuBar()
        product = menuBar.addMenu('Search by ...')
        insert = QMenu('Insert', self)
        product.addMenu(insert)
        self.setCentralWidget(self.__getProductView())

    def __getProductView(self):
        proView = ProductView()
        return proView
