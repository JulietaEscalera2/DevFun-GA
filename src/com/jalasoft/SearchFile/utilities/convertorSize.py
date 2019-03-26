# from src.com.jalasoft.SearchFile.controller.controller import Controller


class ConvertorSize:

    def get_size_value(self, file_size, file_size_unit):
        # parameterSize = Controller()
        # file_size = parameterSize.__init_search(__file_size)
        # file_size_unit  = parameterSize.__init_search(__file_size_unit)
        if file_size_unit == 'Kb':
            return file_size
        if file_size_unit == 'Mb':
            return file_size * 1024
        if file_size_unit == 'Gb':
            return file_size * 1024 * 1024
