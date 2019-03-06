from PyQt5.QtWidgets import QMenu, QLabel, QWidget, QFormLayout, QLineEdit


class ProductView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        form = QFormLayout()
        form.addRow(QLabel('name:'), QLineEdit())
        self.setLayout(form)