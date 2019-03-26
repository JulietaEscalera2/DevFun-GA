import os,time


class File:
    def __init__(self,name,path):
        self.__file_name__ = name
        self.__file_path__ = path

    # this return the size in kb of the file
    def get_size_kb(self):
        return os.path.getsize(os.path.join(self.__file_path__ , self.__file_name__))

    # this return the size in MB of the file
    def get_size_mb(self):
        return os.path.getsize(os.path.join(self.__file_path__ , self.__file_name__))

    # this return the creation date of the file
    def get_creation_date(self):
        file_time = os.path.getmtime(os.path.join(self.__file_path__ , self.__file_name__))
        return time.ctime(file_time)

    # this return the type of the file
    def get_file_type(self):
        return os.path.splitext(self.__file_name__)[1][1:]

    # this return the nam of the file
    def get_file_name(self):
        return self.__file_name__

    # this return the path of the file
    def get_file_in_path(self):
        return os.path.join(self.__file_path__ , self.__file_name__)


