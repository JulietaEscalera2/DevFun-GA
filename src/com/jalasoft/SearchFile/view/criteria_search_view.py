from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QFormLayout, QLabel, \
    QLineEdit,QTableWidget


class CriteriaView(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    '''This method init the main horizontal layout'''

    def init_ui(self):

        self.hLayout = QHBoxLayout()
        self.hLayout.addLayout(self.get_criteria_layout())
        self.hLayout.addLayout(self.get_function_buttons())
        self.hLayout.addWidget(self.get_result_table_search())
        self.setLayout(self.hLayout)

    def get_criteria_layout(self):

        self.form = QFormLayout()
        self.pathText = QLineEdit()
        self.fileName = QLineEdit()
        self.extText = QLineEdit()
        self.form.addRow(QLabel("Path"), self.pathText)
        self.form.addRow(QLabel("File Name"), self.fileName)
        self.form.addRow(QLabel("Extension"), self.extText)
        return self.form

    def get_result_table_search(self):

        self.table = QTableWidget()
        self.table.size()
        self.table.setStyleSheet("font-size: 12px; color: #3232C0;")
        self.table.setColumnCount(3)
        self.table.setRowCount(1)
        self.table.setHorizontalHeaderLabels(["Path",u"File Name",u"Ext"])

        return self.table

    def get_function_buttons(self):

        self.button_layout = QHBoxLayout()
        button_search = QPushButton("Search")
        button_save = QPushButton("Save criteria")
        button_clean = QPushButton("Clean search")
        self.button_layout.addWidget(button_search)
        self.button_layout.addWidget(button_save)
        self.button_layout.addWidget(button_clean)

        return self.button_layout

    def getTable(self):
        return self.table

    def getFileName(self):
        return self.fileName.text()

    def getExtention(self):
        return self.extText.text()

    def getPath(self):
        return self.pathText.text()






