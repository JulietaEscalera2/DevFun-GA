import os
from src.com.jalasoft.SearchFile.model.file import File


class Model():

    def __init__(self, objectParameters):
        self.objectParameters = objectParameters
        print(objectParameters['Filename'])
        self.__name_file__ = self.objectParameters['Filename']
        self.__path_file__ = self.objectParameters['Path']
        self.__file_type__ = self.objectParameters['Extension']
        self.__file_size__ = self.objectParameters['Size']
        self.__file_creation_date__ = self.objectParameters['DateCreation']

    def search_criteria(self):
        result = []

        for root, dir, files in os.walk(self.__path_file__):
            for file in files:
                if self.__name_file__!= " " and self.__name_file__ not in file.lower():
                    continue
                if self.__file_type__!= " " and not file.endswith(self.__file_type__):
                    continue
                print("add to list")
                print(self.__file_type__)
                print(file)
                result.append([root, file, self.__file_type__, self.__file_size__])
        return result


    # This will find all matches by file name and path:
    def search_all(self):
        path = self.__path_file__
        name = self.__name_file__
        total = 0
        result = []
        for root, dir, files in os.walk(path):
            for file in files:
                if name in file.lower():
                    print(os.path.join(root, file))
                    total += 1
                    file_object = File(file,root)
                    file_size = file_object.get_size_kb()
                    file_time = file_object.get_creation_date()
                    file_type = file_object.get_file_type()
                    result.append([root, file, file_size, file_time,file_type])

        print("In total there are", total, " files with filename:", name, ",in the path:", path)
        return result

    # Search by file type/ext and path
    def search_by_type(self):
        path = self.__path_file__
        type = self.__file_type__
        total = 0
        result = []

        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(type):
                    print(os.path.join(root, file))
                    total += 1
                    file_object = File(file, root)
                    file_size = file_object.get_size_kb()
                    file_time = file_object.get_creation_date()
                    file_type = file_object.get_file_type()
                    result.append([root, file, file_size, file_time, file_type])

        print("In total there are", total, " files with", type, "in", path)
        return result

    # Search by file size and path
    def search_by_size(self):
        path = self.__path_file__
        size = self.__file_size__
        total = 0
        result = []
        for root, dirs, files in os.walk(path):
            for file in files:
                file_object = File(file, root)
                if os.stat(file_object.get_file_in_path()).st_size == size:
                    print(os.path.join(root, file))
                    total += 1

                    file_size = file_object.get_size_kb()
                    file_time = file_object.get_creation_date()
                    file_type = file_object.get_file_type()
                    result.append([root, file, file_size, file_time, file_type])

        print("In total there are", total, " files with", size, "in", path)
        return result



