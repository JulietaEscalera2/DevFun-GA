from src.com.jalasoft.SearchFile.controller.objectParameters import ObjectParameters


class ParametersKeys(ObjectParameters):

    def getkeys(self):
        key_path = ObjectParameters.searchParameters['Path']
        key_filename = ObjectParameters.searchParameters['Filename']
        key_extension = ObjectParameters.searchParameters['Extension']
        # key_datecreation = ObjectParameters.searchParameters['DateCreation'] // comment this lines until view has them
        key_size = ObjectParameters.searchParameters['Size']
        print(key_path)
    #print(getkeys)