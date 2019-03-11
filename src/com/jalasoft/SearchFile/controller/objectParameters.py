

from src.com.jalasoft.SearchFile.view.getData import Data

class ObjectParameters:
    def __init__(self):
        pass
    def data_to_file(self, get_path_file, get_file_name, get_extension, get_date_creation, get_file_size):

        parameters = {'Path':'', 'Filename':'', 'Extension':'', 'DateCreation':'', 'Size':''}
        parameters['Path'] = get_path_file()
        parameters['File Name'] = get_file_name()
        parameters['Extension'] = get_extension()
        parameters['DateCreation'] = get_date_creation()
        parameters['Size'] = get_file_size()
        return parameters
    # print(parameters)

    # #sintaxis para agregar un valor a un dictionario:   diccionario[clave] = valor
    gazpacho = {}

    gazpacho['Aceite'] = '300 ml'
    gazpacho['Vinagre'] = '100 ml'
    gazpacho['Pepino'] = 1
    gazpacho['Pimiento'] = 1

    print(gazpacho)
