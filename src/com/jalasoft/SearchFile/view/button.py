from PyQt5.QtWidgets import QPushButton


class SearchButton(QPushButton):

    def __init__(self):
        super().__init__()

    def __init__(self, title):
        super().__init__()
        self.setObjectName("evilButton")
        self.setText(title)


