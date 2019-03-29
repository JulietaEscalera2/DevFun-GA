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

    def add_action_listener(self):
        self.central_widget = self.view.centralWidget()
        self.central_widget.get_search_button().clicked.connect(lambda: self.__init_search())
        # self.central.widget.get_save_button().clicked.connect(lambda: self.__init_save())
        # self.central.widget.get_search_button().clicked.connect(lambda: self.__init_clean())
    #     self.central_widget.get_isHidden().checkbox.stateChanged.connect(self.hidden_state)
    #     self.central_widget.get_isReadOnly().checkbox.stateChange.connect(self.readonly_state)

    def __init_search(self):
        __path = self.central_widget.get_path()
        __file_name = self.central_widget.get_file_name()
        __file_extention = self.central_widget.get_file_extention()
        __file_size = self.central_widget.get_file_size()
        __file_date = self.central_widget.get_date_creation()
        __file_hidden = self.central_widget.get_isHidden()
        __file_readOnly = self.central_widget.get_isReadOnly()
        # __file_size_unit = self.central_widget.get_size_combo()
        # __date_with_format = __file_date.strftime('%b%d%Y')


        # create creteria
        object_criteria = ObjectParameters()
        object_criteria.data_to_file(__path, __file_name, __file_extention, __file_date, __file_size, __file_hidden,__file_readOnly)
        resultList = self.model.search_criteria(object_criteria)
        self.fill_table_view(resultList)

    def fill_table_view(self, resultList):
        size = len(resultList)
        self.central_widget.get_table().setRowCount(size)
        col = 0
        for result in resultList:
            row = 0
            for data in result:
                self.central_widget.get_table().setItem(col, row, QTableWidgetItem(str(data)))
                row = row + 1
            col = col + 1

    #
    # def hidden_state(self, statehidden):
    #     if statehidden == Qt.Checked:
    #         self.__file_hidden == True
    #     else:
    #         self.__file_hidden == False
    #
    # def readonly_state(self, statereadonly):
    #     if statereadonly == Qt.Checked:
    #         self.__file_readonly == True
    #     else:
    #         self.__file_readonly == False

    #
    #     # __file_size_unit = self.central_widget.get_size_combo()
    #     # __file_hidden = self.central_widget.get_isHidden()   #.checkbox.stateChanged.connect()
    #     # __file_readonly = self.central_widget.get_isReadOnly()  #.checkbox.stateChange.connect()
    #
    #     #create criteria
    #     object_criteria = ObjectParameters()
    #
    #     object_criteria.data_to_file(__path, __file_name, __file_extention, '',ConvertorSize.get_size_value(__file_size,__file_size_unit), __file_hidden,__file_readonly)
    #






