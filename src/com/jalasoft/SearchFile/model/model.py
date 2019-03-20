import os
from src.com.jalasoft.SearchFile.model.file import File


class Model:

    def __init__(self):
        pass

        # self.objectParameters = objectParameters
        # self.__name_file__ = self.objectParameters['Filename']
        # self.__path_file__ = self.objectParameters['Path']
        # self.__file_type__ = self.objectParameters['Extension']
        # self.__file_size__ = self.objectParameters['Size']
        # self.__file_creation_date__ = self.objectParameters['DateCreation']


    def search_criteria(self,objectParameters):
        result = []
        for root, dir, files in os.walk(self.objectParameters['Path']):

            for file in files:
                file_object = File(file, root)

                if self.objectParameters['Filename']!= 'Null' and self.objectParameters['Filename'] not in file.lower():
                    continue

                if self.objectParameters['Extension']!= 'Null' and not file.endswith(self.objectParameters['Extension']):
                    continue

                if self.objectParameters['Size']!= 'Null' and str(file_object.get_size_kb())!= str(self.objectParameters['Size']):
                    continue
                if self.objectParameters['DateCreation']!= 'Null' and file_object.get_creation_date()!= self.objectParameters['DateCreation']:
                    continue

                result.append([root, file, file_object.get_file_type(), file_object.get_size_kb()])
        return result


    # This will find all matches by file name and path:
    def search_all(self,objectParameters):

        result = []
        for root, dir, files in os.walk(self.objectParameters['Path']):
            for file in files:
                if self.objectParameters['Filename'] in file.lower():
                    file_object = File(file,root)
                    file_size = file_object.get_size_kb()
                    file_time = file_object.get_creation_date()
                    file_type = file_object.get_file_type()
                    result.append([root, file, file_size, file_time,file_type])

        return result

    # Search by file type/ext and path
    def search_by_type(self,objectParameters):
        result = []

        for root, dirs, files in os.walk(self.objectParameters['Path']):
            for file in files:
                if file.endswith(self.objectParameters['Extension']):
                    file_object = File(file, root)
                    file_size = file_object.get_size_kb()
                    file_time = file_object.get_creation_date()
                    file_type = file_object.get_file_type()
                    result.append([root, file, file_size, file_time, file_type])

        return result

    # Search by file size and path
    def search_by_size(self,objectParameters):
        result = []
        for root, dirs, files in os.walk(self.objectParameters['Path']):
            for file in files:
                file_object = File(file, root)
                if os.stat(file_object.get_file_in_path()).st_size == self.objectParameters['Size']:
                    file_size = file_object.get_size_kb()
                    file_time = file_object.get_creation_date()
                    file_type = file_object.get_file_type()
                    result.append([root, file, file_size, file_time, file_type])

        return result



