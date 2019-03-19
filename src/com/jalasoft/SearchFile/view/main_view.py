from PyQt5.QtWidgets import QMenu, QMainWindow

from src.com.jalasoft.SearchFile.view.productView import ProductView


class View(QMainWindow):

    def __init__(self):
        super().__init__()

    def initUI(self):
    #def initUI(self, controller):
        self.setWindowTitle('Search File')
       # self.__controller = controller
        self.__initComponent()
        self.show()

    def __initComponent(self):
        self.resize(1000, 1500)
        menuBar = self.menuBar()
        product = menuBar.addMenu('Search by criteria')
        insert = QMenu('Insert', self)
        product.addMenu(insert)
        #
        # insertOption = QAction("Insert", self)
        # productMenu.addAction(insertOption)
        # showOption = QAction("Show", self)
        # productMenu.addAction(showOption)
        #
        # insertOption.triggered.connect(lambda: self.loadProductInsertView())
        # showOption.triggered.connect(lambda: self.loadProductShowView())
        #
        self.setCentralWidget(self.__getSearchView())

    def __getSearchView(self):
        main_view = ProductView()
        return main_view

    # def loadProductInsertView(self):
    #     self.setCentralWidget(ProductInsertView())
    #     self.__controller.addActionListener()
    #
    # def loadProductShowView(self):
    #     self.setCentralWidget(ProductShowView())
    #     self.__controller.loadProduct()