from PyQt5.QtWidgets import QPushButton

class SearchButton(QPushButton):

    def __init__(self):
        super().__init__()


    def push_button(self,title):
        self.push = QPushButton(title)
        return self.push

