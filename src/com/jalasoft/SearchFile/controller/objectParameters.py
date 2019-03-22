
class ObjectParameters:
    def __init__(self):
        pass

<<<<<<< HEAD
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
=======
    def data_to_file(self, get_path_file, get_file_name, get_extension, get_date_creation, get_file_size):
        searchParameters = {
            'Path':'',
            'Filename':'',
            'Extension':'',
            'DateCreation':'',
            'Size':''
        }

        searchParameters['Path'] = "c://"
        # searchParameters['Path'] = ProductView.getPath()
        # searchParameters['Filename'] = ProductView.getFileName()
        # searchParameters['Extension'] = ProductView.getExtention()
        # #searchParameters['DateCreation'] = get_date_creation() // comment this lines until view has them
        # #searchParameters['Size'] = get_file_size()

        return searchParameters
    # print(parameters)
>>>>>>> c4c50b2ff2bd471fcbd0f1404cc34cf3881b9a90

    # #sintaxis para agregar un valor a un dictionario:   diccionario[clave] = valor



materias = {"lunes":''}
materias["lunes"] = [6103, 7540]
materias["martes"] = [6201]
materias["miércoles"] = [6103, 7540]
materias["jueves"] = []
materias["viernes"] = [6201]

print (materias["lunes"])