from src.com.jalasoft.SearchFile.controller.objectParameters import ObjectParameters


class ParametersKeys(ObjectParameters):

    def getkeys(self):
        key_path = searchParameters['Path']
        key_filename = searchParameters['Filename']
        key_extension = searchParameters['Extension']
        key_datecreation = searchParameters['DateCreation']
        key_size = searchParameters['Size']