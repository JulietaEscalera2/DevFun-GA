from PyQt5.QtWidgets import QMainWindow

class View(QMainWindow):

    def __init__(self):
        super().__init__()


    def initUI(self):
        print("initUI-test")
        self.setWindowTitle('test')
        self.__initComponent()
        self.show()


    def __initComponent(self):
        menuBar = self.menuBar()
        product = menuBar.addMeu('Product')
        insert = self.QMenu('Insert', self)
        product.addMenu(insert)
        self.setCentralWidget(self.__getProductView())

    def __getProductView(self):
        proView = self.ProductView()
        return proView
