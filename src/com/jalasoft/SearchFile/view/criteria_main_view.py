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
        self.resize(1500, 1000)
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')
        searchMenu = menuBar.addMenu('Search')
        toolsMenu = menuBar.addMenu('Tools')
        helpMenu = menuBar.addMenu('Help')

        exitButton = QAction(QIcon('./src/com/jalasoft/SearchFile/view/images/file.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        self.setCentralWidget(self.__getSearchView())
        self.__controller.add_action_listener()

    def __getSearchView(self):
        main_view = CriteriaView()
        return main_view
