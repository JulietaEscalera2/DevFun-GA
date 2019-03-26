import os

# from src.com.jalasoft.SearchFile.controller.controller import Controller


class ObjectParameters:
    def __init__(self):
        self.searchParameters = {}

    def data_to_file(self, get_path_file, get_file_name, get_extension, get_date_creation, get_file_size,get_isHidden, get_isReadOnly):
        self.searchParameters['Path'] = get_path_file
        self.searchParameters['Filename'] = get_file_name
        self.searchParameters['Extension'] = get_extension
        #self.searchParameters['DateCreation'] = get_date_creation() // comment this lines until view has them
        self.searchParameters['Size'] = get_file_size
        self.searchParameters['Hidden'] = get_isHidden
        self.searchParameters['ReadOnly'] = get_isReadOnly

        # #to empty data
        # if self.searchParameters['Path'] == '':
        #     self.searchParameters['Path'] = ''
        # if self.searchParameters['Filename'] == '':
        #     self.searchParameters['Filename'] = ''
        # if self.searchParameters['Extension'] == '':
        #     self.searchParameters['Extension'] = ''
        # if self.searchParameters['Size'] == '':
        #     self.searchParameters['Size'] = ''

