

from src.com.jalasoft.SearchFile.view.getData import Data

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
        searchParameters['Path'] = get_path_file()
        # searchParameters['Path'] = 'Documents'
        searchParameters['Filename'] = get_file_name()
        searchParameters['Extension'] = get_extension()
        searchParameters['DateCreation'] = get_date_creation()
        searchParameters['Size'] = get_file_size()
        return searchParameters
    # print(parameters)

    # #sintaxis para agregar un valor a un dictionario:   diccionario[clave] = valor
