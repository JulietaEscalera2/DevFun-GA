
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QFormLayout, QLabel, \
    QLineEdit, QTableWidget, QVBoxLayout, QCheckBox, QSpacerItem, QSizePolicy


class CriteriaView(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    '''This method init the main horizontal layout'''

    def init_ui(self):

        self.hLayout = QHBoxLayout()
        self.hLayout.addLayout(self.get_left_criteria_layout())
        self.hLayout.addWidget(self.get_result_table_search())
        self.setLayout(self.hLayout)

    def get_criteria_layout(self):

        self.form = QFormLayout()
        self.pathText = QLineEdit()
        self.fileName = QLineEdit()
        self.extText = QLineEdit()
        self.size = QLineEdit()
        self.createDate = QLineEdit()
        self.hidden = QCheckBox()

        self.form.addRow(QLabel("Path"), self.pathText)
        self.form.addRow(QLabel("File Name"), self.fileName)
        self.form.addRow(QLabel("Extension"), self.extText)
        self.form.addRow(QLabel("Size"), self.size)
        self.form.addRow(QLabel("Create Date"), self.createDate)
        self.form.addWidget( self.hidden)

        return self.form

    def get_result_table_search(self):

        self.table = QTableWidget()
        self.table.size()
        self.table.setStyleSheet("font-size: 12px; color: #3232C0;")
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Path",u"File Name",u"Ext",u"Size"])

        return self.table

    def get_left_criteria_layout(self):
        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(self.get_criteria_layout())
        self.v_layout.addLayout(self.get_function_buttons())
        self.v_layout.addItem(self.get_vertical_spacer())

        return self.v_layout

    def get_vertical_spacer(self):
        vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        return vertical_spacer

    def get_function_buttons(self):

        self.button_layout = QHBoxLayout()
        self.button_search = QPushButton("Search")
        button_save = QPushButton("Save criteria")
        button_clean = QPushButton("Clean search")

        # vertical_spacer = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        # self.button_layout.addItem(vertical_spacer)

        self.button_layout.addWidget(self.button_search)
        self.button_layout.addWidget(button_save)
        self.button_layout.addWidget(button_clean)

        return self.button_layout

    def get_table(self):
        return self.table

    def get_file_name(self):
        return self.fileName.text()

    def get_file_extention(self):
        return self.extText.text()

    def get_path(self):
        return self.pathText.text()

    #def get_date_creation(self):
    #    return self.extText.text()

    def get_file_size(self):
        return self.size.text()

    def get_search_button(self):
        return self.button_search




