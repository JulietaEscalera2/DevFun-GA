from src.com.jalasoft.SearchFile.controller.objectParameters import ObjectParameters


class Controller:
    def __init__(self, view, model):
        view.initUI()

        model.__init__()
        #print(model)


    def searchCriteria(self):
        path = ObjectParameters.key_path()
        filename = ObjectParameters.key_filename()
        extension = ObjectParameters.key_extension()
        '''
        // comment this lines until view has them
        size = ObjectParameters.key_size()
        dateCreation = ObjectParameters.key_datecreation()
        '''


