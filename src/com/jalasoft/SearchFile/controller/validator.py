import os
from src.com.jalasoft.SearchFile.controller.keysparameters import ParametersKeys
from src.com.jalasoft.SearchFile.controller.keysparameters import ObjectParameters

class Validator(ParametersKeys):

    #def __init__(self, list_SearchFile):  #toodos los parametros deben pasarse al objeto
        #self.list_SearchFile = ['C:Users\hp\Documents\python-fundamentals','python-fundamentals',0,0]#path,namefile,extension,tamanofile

    #https://codingornot.com/08-python-validar-entradas-ejemplos
    # https://uniwebsidad.com/libros/python/capitulo-6/metodos-de-validacion
    # cadena = "C:\Python27"
    # print cadena.isalnum()

    #https://uniwebsidad.com/libros/python/capitulo-10/modulos-de-sistema
    #lista = ['C:\Users\hp\Documents\python-fundamentals','python-fundamentals',0,0]#path,namefile,extension,tamanofile

    def read_list(list_SearchFile):
        #path = list_SearchFile[0]
        #name = list_SearchFile[1]
        #extension = list_SearchFile[2]
        #size = list_SearchFile[3]
        list_model = []
        if os.path.isdir(self.key_path):
            print (self.key_path)
            #return True
        if os.path.isfile(self.key_path):
            return True
        if not os.path.isdir(path) or os.path.isfile(self.key_path):
            return f'It is not a path'
        if self.key_filename.isalnum():
            return True
        else:
            return False
        if self.key_size.isdigit():
            return True
        if not size.isdigit():
            return f'Please input only numbers'
        if self.key_datecreation.isalnum():
            return True
        if self.key_extension.os.extsep():
            return True
        if self.key_path == 'NULL': list_model[0]='NULL'
        if self.key_filename == 'NULL': list_model[1] == 'NULL'
        if self.key_extension == 'NULL': list_model[2] == 'NULL'
        if self.key_datecreation == 'NULL': list_model[3] == 'NULL'
        if self.key_size == 'NULL': list_model[4] == 'NULL'
