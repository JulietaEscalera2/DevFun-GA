import os
from src.com.jalasoft.SearchFile.controller.keysparameters import ParametersKeys
from src.com.jalasoft.SearchFile.controller.keysparameters import ObjectParameters

class Validator(ParametersKeys):

    #https://codingornot.com/08-python-validar-entradas-ejemplos
    # https://uniwebsidad.com/libros/python/capitulo-6/metodos-de-validacion
    #https://uniwebsidad.com/libros/python/capitulo-10/modulos-de-sistema
    #lista = ['C:\Users\hp\Documents\python-fundamentals','python-fundamentals',0,0]#path,namefile,extension,tamanofile

    def read_list(list_SearchFile):
        list_model = []
        if os.path.isdir(ObjectParameters.key_path):
            print (ObjectParameters.key_path)
            #return True
        if os.path.isfile(ObjectParameters.key_path):
            return True
        if not os.path.isdir(ObjectParameters.key_path) or os.path.isfile(ObjectParameters.key_path):
            return f'It is not a path'
        if ObjectParameters.key_filename.isalnum():
            return True
        else:
            return False
        if ObjectParameters.key_size.isdigit():
            return True
        if not ObjectParameters.key_size.isdigit():
            return f'Please input only numbers'
        if ObjectParameters.key_datecreation.isalnum():
            return True
        if ObjectParameters.key_extension.os.extsep():
            return True
        if ObjectParameters.key_path == 'NULL':
            ObjectParameters.key_path = "NULL"
            #list_model[0]='NULL'
        if ObjectParameters.key_filename == 'NULL':
            ObjectParameters.key_filename == "NULL"
            #list_model[1] == 'NULL'
        if ObjectParameters.key_extension == 'NULL': list_model[2] == 'NULL'
        if ObjectParameters.key_datecreation == 'NULL': list_model[3] == 'NULL'
        if ObjectParameters.key_size == 'NULL': list_model[4] == 'NULL'
