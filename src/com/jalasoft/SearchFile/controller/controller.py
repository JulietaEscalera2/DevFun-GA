from PyQt5.QtWidgets import QTableWidgetItem

from src.com.jalasoft.SearchFile import utilities
from src.com.jalasoft.SearchFile.controller.objectParameters import ObjectParameters
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
        # self.central.widget.get_search_button().clicked.connect(lambda: self.__init_save())
        # self.central.widget.get_search_button().clicked.connect(lambda: self.__init_clean())
        # self.central_widget.checkouthidden.stateChanged.connect(self.__init_search())
        # self.central_widget.checkoutreadonly.stateChanged.connect(self.__init_search())


    def __init_search(self):  # buscara los criterios de busqueda de la vista
        __path = self.central_widget.get_path()
        __file_name = self.central_widget.get_file_name()
        __file_extention = self.central_widget.get_file_extention()
        __file_size = self.central_widget.get_file_size()
        __file_size_unit = self.central_widget.get_size_combo()
        __file_size_hidden = self.central_widget.get_isHidden()
        __file_size_ReadOnly = self.central_widget.get_isReadOnly()

        # # verify status of checkboxes  (aca no estoy muy segura de como enviarle al modelo)
        # if self.checkhidden.isChecked() == True :
        #     checkboxHidden = self.model.__file_size_hidden(True)
        #     return __file_size_hidden == True
        # elif self.checkhidden.isChecked() == False:
        #     return __file_size_hidden == False
        # elif self.checkoutread_only.isChecked() == True:
        #     return __file_size_ReadOnly == True
        # elif self.checkoutread_only.isChecked() == False:
        #     return __file_size_ReadOnly == False

        #create criteria
        object_criteria = ObjectParameters()
        object_criteria.data_to_file(__path, __file_name, __file_extention, '', ConvertorSize.get_size_value(__file_size, __file_size_unit), __file_size_hidden, __file_size_ReadOnly)
        resultList = self.model.search_criteria(object_criteria)
        self.fill_table_view(resultList)


    def fill_table_view(self,resultList):
        size = len(resultList)
        self.central_widget.get_table().setRowCount(size)
        col = 0
        for result in resultList:
            row = 0
            for data in result:
                self.central_widget.get_table().setItem(col,row, QTableWidgetItem(str(data)))
                row = row + 1
            col = col + 1




