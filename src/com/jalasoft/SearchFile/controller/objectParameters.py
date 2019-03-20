

from src.com.jalasoft.SearchFile.view.getData import Data
from src.com.jalasoft.SearchFile.view.productView import ProductView
class ObjectParameters:
    def __init__(self):
        pass

    def data_to_file(self, get_path_file, get_file_name, get_extension, get_date_creation, get_file_size):
        searchParameters = {
            'Path':'',
            'Filename':'',
            'Extension':'',
            'DateCreation':'',
            'Size':''
        }
        searchParameters['Path'] = "c:'\'test"
        # searchParameters['Path'] = ProductView.getPath()
        # searchParameters['Filename'] = ProductView.getFileName()
        # searchParameters['Extension'] = ProductView.getExtention()
        # #searchParameters['DateCreation'] = get_date_creation() // comment this lines until view has them
        # #searchParameters['Size'] = get_file_size()
        return searchParameters
    # print(parameters)

    # #sintaxis para agregar un valor a un dictionario:   diccionario[clave] = valor
