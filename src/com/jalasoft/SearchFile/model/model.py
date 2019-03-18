import sys, os
from src.com.jalasoft.SearchFile.model.file import File


class Model:

    def __init__(self,name_file,path_file, file_type, file_size):
        self.__name_file__ = name_file
        self.__path_file__ = path_file
        self.__file_type__ = file_type
        self.__file_size__ = file_size


    def search_criteria(self):
        path = self.__path_file__
        name = self.__name_file__
        ext = self.__file_type__
        total = 0
        result = []

        for root, dir, files in os.walk(path):
            for file in files:
                file_object = File(file, root)
                if name!= " " and name!= file_object.get_file_name():
                    print(name)
                    print(file_object.get_file_name())
                    continue
                if ext!= " " and ext!= file_object.get_file_type():
                    print(ext)
                    print(file_object.get_file_type())
                    continue
                result.append([root, file, ext])
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

    # This will return the first match found:
    def search(self):
        path = self.__path_file__
        name = self.__name_file__
        total = 0
        result = []

        for root, dir, files in os.walk(path):
            for file in files:
                if name in file.lower():
                    print(os.path.join(root, file))
                    file_object = File(file, root)
                    file_size = file_object.get_size_kb()
                    file_time = file_object.get_creation_date()
                    file_type = file_object.get_file_type()
                    result.append([root, file, file_size, file_time, file_type])
                    break

        print("In total there are", total, " files with", name, "in", path)
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



# main
# model should receive ['File name', 'file path','Ext/type','file creation date', 'File size']
fit= Model('laura', 'D:\\','.avi','6236311')
file_found = fit.search_criteria()
print("************")
print(file_found)
