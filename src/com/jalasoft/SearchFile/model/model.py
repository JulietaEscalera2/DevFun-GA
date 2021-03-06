"""
Search files

This is the Model class.

Author: Teresa Lopez
Last edited: 3/27/2019
"""
import os
from datetime import datetime

from src.com.jalasoft.SearchFile.model.file import File

import os


from src.com.jalasoft.SearchFile.model.file import File

class Model:

    def __init__(self):
        print("Model class")

    def search_criteria(self, objectParameters):
        self.objectParameters= objectParameters
        result = []
        for root, dirs, files in os.walk(self.objectParameters.searchParameters['Path']):

            for file in files:
                file_object = File(file, root)
                if self.objectParameters.searchParameters['Hidden'] and int(file_object.is_hidden())!=2:
                    continue
                if self.objectParameters.searchParameters['ReadOnly'] and int(file_object.is_readOnly())!=1:
                    continue
                if self.objectParameters.searchParameters['Filename']!= '' and self.objectParameters.searchParameters['Filename'] not in file.lower():
                    continue
                if self.objectParameters.searchParameters['Extension']!= '' and not file.endswith(self.objectParameters.searchParameters['Extension']):
                    continue
                if self.objectParameters.searchParameters['Size']!= '' and not int(file_object.get_size())<= int(self.objectParameters.searchParameters['Size']):
                    continue

                # d = datetime.utcfromtimestamp(self.objectParameters.searchParameters['DateCreation'])
                # formated_date = d.strftime('%d %b %Y')
                #  print(formated_date)
                # print("after")
                # print(file_object.get_creation_date())
                # if self.objectParameters.searchParameters['DateCreation']!= '' and file_object.get_creation_date()!= self.objectParameters.searchParameters['DateCreation']:
                #     continue
                result.append([root, file, file_object.get_file_type(), file_object.get_size()])
        print(result)
        return result


    # This will find all matches by file name and path:
    def search_all(self,objectParameters):
        result = []
        for root, dir, files in os.walk(self.objectParameters.searchParameters['Path']):
            for file in files:
                if self.objectParameters.searchParameters['Filename'] in file.lower():
                    file_object = File(file,root)
                    file_size = file_object.get_size_kb()
                    #file_time = file_object.get_creation_date()
                    file_type = file_object.get_file_type()
                    result.append([root, file, file_size,file_type])

        return result

    # Search by file type/ext and path
    def search_by_type(self,objectParameters):
        result = []

        for root, dirs, files in os.walk(self.objectParameters.searchParameters['Path']):
            for file in files:
                if file.endswith(self.objectParameters.searchParameters['Extension']):
                    file_object = File(file, root)
                    file_size = file_object.get_size()
                    #file_time = file_object.get_creation_date()
                    file_type = file_object.get_file_type()
                    result.append([root, file, file_size, file_type])

        return result

    # Search by file size and path
    def search_by_size(self,objectParameters):
        result = []
        for root, dirs, files in os.walk(self.objectParameters.searchParameters['Path']):
            for file in files:
                file_object = File(file, root)
                if os.stat(file_object.get_file_in_path()).st_size == self.objectParameters.searchParameters['Size']:
                    file_size = file_object.get_size_kb()
                    #file_time = file_object.get_creation_date()
                    file_type = file_object.get_file_type()
                    result.append([root, file, file_size, file_type])

        return result

