from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction

from src.com.jalasoft.SearchFile.view.criteria_search_view import CriteriaView

class MainView(QMainWindow):

    def __init__(self):
        super().__init__()

    def initUI(self, controller):
        self.__controller = controller
        self.setWindowTitle('Search File DevFun-GA')
        self.__initComponent()
        self.show()

    def __initComponent(self):
        self.resize(1500, 500)
        self.setStyleSheet("background-color: LightGray;")
        self.setWindowIcon(QIcon("./images/search-icon-png-30.png"))
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')
        aboutMenu = menuBar.addMenu('About Us...')

        exitButton = QAction(QIcon('./images/back.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        aboutButton = QAction(QIcon("./images/search-icon-png-30.png"),"Members",self)
        aboutButton.triggered.connect(self.close)
        aboutMenu.addAction(aboutButton)

        self.setCentralWidget(self.__getSearchView())
        self.__controller.add_action_listener()

    def __getSearchView(self):
        main_view = CriteriaView()
        return main_view
