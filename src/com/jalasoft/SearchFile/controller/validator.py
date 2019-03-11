import os
class Validator:

    def __init__(self, list_SearchFile):  #toodos los parametros deben pasarse al objeto
        self.list_SearchFile = ['C:Users\hp\Documents\python-fundamentals','python-fundamentals',0,0]#path,namefile,extension,tamanofile

    #https://codingornot.com/08-python-validar-entradas-ejemplos
    # https://uniwebsidad.com/libros/python/capitulo-6/metodos-de-validacion
    # cadena = "C:\Python27"
    # print cadena.isalnum()

    #https://uniwebsidad.com/libros/python/capitulo-10/modulos-de-sistema
    #lista = ['C:\Users\hp\Documents\python-fundamentals','python-fundamentals',0,0]#path,namefile,extension,tamanofile

    def read_list(list_SearchFile):
        path = list_SearchFile[0]
        name = list_SearchFile[1]
        extension = list_SearchFile[2]
        size = list_SearchFile[3]
        list_model = []
        if os.path.isdir(path):
            return True
        if os.path.isfile(path):
            return True
        if not os.path.isdir(path) or os.path.isfile(path):
            return f'It is not a path'
        if name.isalnum():
            return True
        else:
            return False
        if size.isdigit():
            return True
        if not size.isdigit():
            return f'Please input only numbers'
        if path == 'NULL': list_model[0]='NULL'
        if name == 'NULL': list_model[1] == 'NULL'
        if extension == 'NULL': list_model[2] == 'NULL'
        if size == 'NULL': list_model[3] == 'NULL'
