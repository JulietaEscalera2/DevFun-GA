from src.com.jalasoft.SearchFile.controller.objectParameters import ObjectParameters


class ParametersKeys(ObjectParameters):

    def getkeys(self):
        key_path = ObjectParameters.searchParameters['Path']
        key_filename = ObjectParameters.searchParameters['Filename']
        key_extension = ObjectParameters.searchParameters['Extension']
        key_datecreation = ObjectParameters.searchParameters['DateCreation']
        key_size = ObjectParameters.searchParameters['Size']