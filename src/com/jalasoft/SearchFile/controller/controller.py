from src.com.jalasoft.SearchFile.controller.objectParameters import ObjectParameters

class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.initUI()
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
        self.view.setTable(tableView)
        return searchResult


    def fill_table_view(self,resultList):
        table = self.view.getTable()
        for result in resultList:
            table.append(result)
        print(table)
        return table



