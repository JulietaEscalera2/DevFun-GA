
from PyQt5.QtWidgets import QTableWidgetItem, QCheckBox, QApplication
from PyQt5.QtCore import Qt
from src.com.jalasoft.SearchFile.controller.objectParameters import ObjectParameters
from time import strftime
from src.com.jalasoft.SearchFile.utilities.convertorSize import ConvertorSize


class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.initUI(self)
        self.model.__init__()
        self.criteria = ObjectParameters()

    #function to listen buttons and checkboxes
    def add_action_listener(self):
        self.central_widget = self.view.centralWidget()
        self.central_widget.get_search_button().clicked.connect(lambda: self.__init_search())

    def __init_search(self):
        __path = self.central_widget.get_path()
        __file_name = self.central_widget.get_file_name()
        __file_extention = self.central_widget.get_file_extention()
        __file_size = self.central_widget.get_file_size()
        __file_date = self.central_widget.get_date_creation()
        __file_hidden = self.central_widget.get_isHidden()
        __file_readOnly = self.central_widget.get_isReadOnly()


        #create criteria
        object_criteria = ObjectParameters()
        object_criteria.data_to_file(__path, __file_name, __file_extention, __file_date, __file_size,__file_hidden,__file_readOnly)
        resultList = self.model.search_criteria(object_criteria)
        self.fill_table_view(resultList)

    def fill_table_view(self,resultList):

        size = len(resultList)
        self.central_widget.get_table().setRowCount(size)
        col = 0
        for result in resultList:
            row = 0
            for data in result:
                self.central_widget.get_table().setItem(col, row, QTableWidgetItem(str(data)))
                row = row + 1
            col = col + 1

