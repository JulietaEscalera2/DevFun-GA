import os
from src.com.jalasoft.SearchFile.model.file import File


class Model():

    def __init__(self, objectParameters):
        self.objectParameters = objectParameters
        self.__name_file__ = self.objectParameters['Filename']
        self.__path_file__ = self.objectParameters['Path']
        self.__file_type__ = self.objectParameters['Extension']
        self.__file_size__ = self.objectParameters['Size']
        self.__file_creation_date__ = self.objectParameters['DateCreation']

        result = {'Path': '', 'Filename': '', 'Extension': '', 'DateCreation': '', 'Size': ''}

    def search_criteria(self):
        result = []
        searchParameters = {'Path': 'D:\\', 'Filename': 'vmware', 'Extension': '.log', 'DateCreation': 'Null',
                            'Size': '1059442'}

        for root, dir, files in os.walk(self.__path_file__):

            for file in files:
                file_object = File(file, root)

                if self.__name_file__!= 'Null' and self.__name_file__ not in file.lower():
                    continue

                if self.__file_type__!= 'Null' and not file.endswith(self.__file_type__):
                    continue

                if self.__file_size__!= 'Null' and str(file_object.get_size_kb())!= str(self.__file_size__):
                    continue
                if self.__file_creation_date__!= 'Null' and file_object.get_creation_date()!= self.__file_creation_date__:
                    continue

                result.append([root, file, file_object.get_file_type(), file_object.get_size_kb()])
        return result


    # This will find all matches by file name and path:
    def search_all(self):
        path = self.__path_file__
        name = self.__name_file__
        result = []
        for root, dir, files in os.walk(path):
            for file in files:
                if name in file.lower():
                    file_object = File(file,root)
                    file_size = file_object.get_size_kb()
                    file_time = file_object.get_creation_date()
                    file_type = file_object.get_file_type()
                    result.append([root, file, file_size, file_time,file_type])

        return result

    # Search by file type/ext and path
    def search_by_type(self):
        path = self.__path_file__
        type = self.__file_type__
        result = []

        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(type):
                    file_object = File(file, root)
                    file_size = file_object.get_size_kb()
                    file_time = file_object.get_creation_date()
                    file_type = file_object.get_file_type()
                    result.append([root, file, file_size, file_time, file_type])

        return result

    # Search by file size and path
    def search_by_size(self):
        path = self.__path_file__
        size = self.__file_size__
        result = []
        for root, dirs, files in os.walk(path):
            for file in files:
                file_object = File(file, root)
                if os.stat(file_object.get_file_in_path()).st_size == size:
                    file_size = file_object.get_size_kb()
                    file_time = file_object.get_creation_date()
                    file_type = file_object.get_file_type()
                    result.append([root, file, file_size, file_time, file_type])

        return result



