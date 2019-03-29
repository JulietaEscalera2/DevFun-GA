import os
# from src.com.jalasoft.SearchFile.utilities.keysparameters import ObjectParameters

class Validator():
    # path = 'C:\\Users'
    # saludo = 'hola'
    # if os.path.isdir(path):
    #     print(path)
    # if not os.path.isdir(saludo):
    #     print('it is not a path')

    def read_criteria(self):
        # file_path = ObjectParameters.searchParameters['path']
        if os.path.isdir(self.ObjectParameters.searchParameters['path']):
            print(self.ObjectParameters.searchParameters['path'])
            return self.ObjectParameters.searchParameters['path']

        if os.path.isfile(self.ObjectParameters.searchParameters['path']):
            return self.ObjectParameters.searchParameters['path']

        if not os.path.isdir(self.ObjectParameters.searchParameters['path']) or os.path.isfile(self.ObjectParameters.searchParameters['path']):
            return f'It is not a path'

        if self.ObjectParameters.searchParameters['Filename'].isalnum():
            return self.ObjectParameters.searchParameters['Filename']
        else:
            return f'filename doesnot accept special characters'

# num = "exe"
# if num.os.extsep():
#     print (num)
# else:
#     print('it is not alphanumeric')

