from src.com.jalasoft.SearchFile.controller.objectParameters import ObjectParameters
from src.com.jalasoft.SearchFile.model.model import Model
from src.com.jalasoft.SearchFile.view import productView


class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.initUI()
        self.model.__init__()
        self.searchCriteria()

    def searchCriteria(self):
        criteria = ObjectParameters()
        searchResult = self.model.search_criteria(criteria.data_to_file())
        tableView = self.fillTable(searchResult)
        self.view.setTable(tableView)
        return searchResult


    def fillTable(self,resultList):
        table = self.view.getTable()
        for result in resultList:
            table.append(result)
        print(table)
        return table



