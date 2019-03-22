from src.com.jalasoft.SearchFile.controller.objectParameters import ObjectParameters
<<<<<<< HEAD
#from src.com.jalasoft.SearchFile.model.model import Model
#from src.com.jalasoft.SearchFile.view import productView

=======
>>>>>>> c4c50b2ff2bd471fcbd0f1404cc34cf3881b9a90

class Controller:
    def __init__(self, mainView, model):
        self.mainView = mainView
        self.model = model
        self.mainView.initUI(self)
        self.model.__init__()
        self.criteria = ObjectParameters()

    # filling object with search criteria
    def fill_criteria_object(self):
        path = self.view.get_path()
        self.criteria['path'] = path
        print(self.criteria)
        return self.criteria

    # Send object criteria to model return dictionary with model search result
    def searchCriteria(self, object_criteria):
        searchResult = self.model.search_criteria(object_criteria)
        tableView = self.fillTable(searchResult)
        self.mainView.setTable(tableView)
        return searchResult


<<<<<<< HEAD
    def fillTable(self,resultList):
        table = self.mainView.getTable()
=======
    def fill_table_view(self,resultList):
        table = self.view.getTable()
>>>>>>> c4c50b2ff2bd471fcbd0f1404cc34cf3881b9a90
        for result in resultList:
            table.append(result)
        print(table)
        return table



