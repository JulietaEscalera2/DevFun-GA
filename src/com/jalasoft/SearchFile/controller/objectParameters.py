class ObjectParameters:
    def __init__(self):
        self.searchParameters = {}

    def data_to_file(self, get_path_file, get_file_name, get_extension, get_date_creation, get_file_size, isHidden,isReadOnly):
        self.searchParameters['Path'] = get_path_file
        self.searchParameters['Filename'] = get_file_name
        self.searchParameters['Extension'] = get_extension
        self.searchParameters['DateCreation'] = get_date_creation
        self.searchParameters['Size'] = get_file_size
        self.searchParameters['Hidden'] = isHidden
        self.searchParameters['ReadOnly'] = isReadOnly