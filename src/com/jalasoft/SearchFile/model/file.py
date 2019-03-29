"""
Search files
This is the Model class.
Author: Teresa Lopez
Last edited: 3/27/2019
"""

import os,time
import win32api, win32con

from datetime import datetime

class File:
    def __init__(self,name,path):
        self.__file_name__ = name
        self.__file_path__ = path

    # this return the size in kb of the file
    def get_size(self):
        return os.path.getsize(os.path.join(self.__file_path__ , self.__file_name__))
    # this return the creation date of the file
    def get_creation_date(self):
        file_time = os.path.getmtime(os.path.join(self.__file_path__ , self.__file_name__))
        d = datetime.utcfromtimestamp(file_time)
        formated_date = d.strftime('%d %b %Y')
        return formated_date
        # return time.ctime(file_time)

    # this return the type of the file
    def get_file_type(self):
        return os.path.splitext(self.__file_name__)[1][1:]

    # this return the nam of the file
    def get_file_name(self):
        return self.__file_name__

    # this return the path of the file
    def get_file_in_path(self):
        return os.path.join(self.__file_path__ , self.__file_name__)

    def is_hidden(self):
        path=os.path.join(self.__file_path__ , self.__file_name__)
        attribute = win32api.GetFileAttributes(path)
        return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
    def is_readOnly(self):
        path=os.path.join(self.__file_path__ , self.__file_name__)
        attribute = win32api.GetFileAttributes(path)
        return attribute & (win32con.FILE_ATTRIBUTE_READONLY | win32con.FILE_ATTRIBUTE_SYSTEM)
