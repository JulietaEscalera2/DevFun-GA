
from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLabel


class ProductView(QWidget):

    def __int__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        form = QFormLayout()
        form.addRow(QLabel('Name'), QLineEdit())
        self.setLayout(form)
