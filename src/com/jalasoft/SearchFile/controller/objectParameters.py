

#from src.com.jalasoft.SearchFile.view.getData import Data
from src.com.jalasoft.SearchFile.view.criteria_search_view import CriteriaView
class ObjectParameters:
    def __init__(self):
        pass

    def data_to_file(self,criteriaDic):
        criteriaDic = {'Path': '','Filename': '','Extension': '','DateCreation': '','Size': ''}
        #criteria['Path'] = CriteriaView.getPath()
        criteriaDic['Path'] = ["c:test"]
        #criteriaDic['Filename'] = CriteriaView.getFileName()
        #criteriaDic['Extension'] = CriteriaView.getExtention()
        return criteriaDic
        print(criteria['Path'])

#print (data_to_file)
#ObjectParameters.data_to_file(criteria)

#criteria = {'Path': '','Filename': '','Extension': '','DateCreation': '','Size': ''}
#criteria['Path'] = ["c:test"]
#print (criteria['Path'])

    # #sintaxis para agregar un valor a un dictionario:   diccionario[clave] = valor



materias = {"lunes":''}
materias["lunes"] = [6103, 7540]
materias["martes"] = [6201]
materias["miércoles"] = [6103, 7540]
materias["jueves"] = []
materias["viernes"] = [6201]

print (materias["lunes"])