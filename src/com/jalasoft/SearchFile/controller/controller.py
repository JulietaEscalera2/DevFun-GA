from src.com.jalasoft.SearchFile.controller.objectParameters import ObjectParameters
#from src.com.jalasoft.SearchFile.model.model import Model
#from src.com.jalasoft.SearchFile.view import productView


class Controller:
    def __init__(self, mainView, model):
        self.mainView = mainView
        self.model = model
        self.mainView.initUI(self)
        self.model.__init__()
        self.searchCriteria()

    def searchCriteria(self):
        criteria = ObjectParameters()
        searchResult = self.model.search_criteria(criteria.data_to_file())
        tableView = self.fillTable(searchResult)
        self.mainView.setTable(tableView)
        return searchResult


    def fillTable(self,resultList):
        table = self.mainView.getTable()
        for result in resultList:
            table.append(result)
        print(table)
        return table



