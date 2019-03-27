import os

from src.com.jalasoft.SearchFile.controller import objectParameters
# from src.com.jalasoft.SearchFile.utilities.keysparameters import ParametersKeys
# from src.com.jalasoft.SearchFile.utilities.keysparameters import ObjectParameters

class Validator():
    path = 'C:\\Users'
    saludo = 'hola'
    if os.path.isdir(path):
        print(path)
    if not os.path.isdir(saludo):
        print('it is not a path')

    # def read_criteria(self):
    #     file_path = ObjectParameters.searchParameters['path']
    #
    #     if os.path.isdir(file_path):
    #         print(file_path)
    #     if not os.path.isdir(file_path):
    #         print('That it is not a path')

    objectParameters = objectParameters
    file_path = objectParameters.searchParameters['path']
    print(file_path)

    # print(readCriteria())
        # if os.path.isdir(ParametersKeys.key_path):
        #     # print (ObjectParameters.key_path)
        #     return ParametersKeys.key_path
        # if os.path.isfile(ParametersKeys.key_path):
        #     return ParametersKeys.key_path
        # if not os.path.isdir(ParametersKeys.key_path) or os.path.isfile(ParametersKeys.key_path):
        #     return f'It is not a path'
        # if ParametersKeys.key_path == '':
        #     return ParametersKeys.key_path.ObjectParameters == "NULL"
        #     #list_model[0]='NULL'

        # if ParametersKeys.key_filename.isalnum():
        #     return ParametersKeys.key_filename
        # else:
        #     return f'filename doesnot accept special characters'
        #
        # if ParametersKeys.key_extension.os.extsep():
        #     return ObjectParameters.key_extension
        #
        # if ParametersKeys.key_filename == 'NULL':
        #     return ParametersKeys.key_filename == "NULL"
        #     #list_model[1] == 'NULL'
        # if ParametersKeys.key_extension == 'NULL':
        #     return ParametersKeys.key_extension == "NULL"
        #     #list_model[2] == 'NULL'
