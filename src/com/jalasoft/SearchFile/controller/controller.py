from src.com.jalasoft.SearchFile.controller.objectParameters import ObjectParameters

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

    def __init_search(self):
        __path = self.central_widget.get_path()
        __file_name = self.central_widget.get_file_name()
        __file_extention = self.central_widget.get_file_extention()
        __file_size = self.central_widget.get_file_size()
        print(__path)
        print(__file_name)
        print(__file_extention)
        print(__file_size)

    # filling object with search criteria
    def fill_criteria_object(self):
        path = self.view.get_path()


    # Send object criteria to model return dictionary with model search result
    def searchCriteria(self, object_criteria):
        searchResult = self.model.search_criteria(object_criteria)
        tableView = self.fillTable(searchResult)
        self.view.setTable(tableView)
        return searchResult


    def fill_table_view(self,resultList):
        table = self.view.getTable()
        for result in resultList:
            table.append(result)
        print(table)
        return table



