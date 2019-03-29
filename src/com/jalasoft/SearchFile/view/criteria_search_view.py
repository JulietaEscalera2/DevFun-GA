from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QFormLayout, QLabel, \
    QLineEdit, QTableWidget, QVBoxLayout, QCheckBox, QSpacerItem, QSizePolicy, QDateEdit, QComboBox, QGroupBox
from src.com.jalasoft.SearchFile.view.table_tamplate import TableTemplate



class CriteriaView(QWidget):

    def __init__(self):
        super().__init__()
        with open("./styles/styles.css") as f:
            self.setStyleSheet(f.read())
        self.init_ui()

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
        self.size_line = QLineEdit()
        self.createDate = QDateEdit()
        self.createDate.setCalendarPopup(True)
        self.hidden = QCheckBox()
        self.read_only = QCheckBox()

        self.pathText.setStyleSheet("QLineEdit { background-color: white }")
        self.fileName.setStyleSheet("QLineEdit { background-color: white }")
        self.extText.setStyleSheet("QLineEdit { background-color: white }")
        self.size_line.setStyleSheet("QLineEdit { background-color: white }")
        self.createDate.setStyleSheet("QLineEdit { background-color: white }")

        self.form.addRow(QLabel("Path"), self.pathText)
        self.form.addRow(QLabel("File Name"), self.fileName)
        self.form.addRow(QLabel("Extension"), self.extText)
        self.form.addRow(QLabel("Size"), self.size_line)
        self.form.addRow(QLabel("         "), self.combo_size())
        self.form.addRow(QLabel("Create Date"), self.createDate)

        return self.form

    def check_box(self):
        self.check_group = QHBoxLayout()
        self.hidden = QCheckBox()
        self.read_only = QCheckBox()
        self.hidden = QCheckBox("Is Hidden")
        self.read_only = QCheckBox("Is Read Only")
        self.check_group.addWidget(self.hidden)
        self.check_group.addWidget(self.read_only)
        return self.check_group


    def get_result_table_search(self):

        self.table = TableTemplate(["Path",u"File Name",u"Ext",u"Size","Create Date"],"LightBlue")
        self.table.size()
        self.table.setColumnCount(5)
        return self.table

    def get_left_criteria_layout(self):
        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(self.get_criteria_layout())
        self.v_layout.addLayout(self.check_box())
        self.v_layout.addLayout(self.get_function_buttons())

        self.v_layout.addItem(self.get_vertical_spacer())

        return self.v_layout

    def get_vertical_spacer(self):
        vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        return vertical_spacer

    def get_function_buttons(self):

        self.button_layout = QHBoxLayout()
        self.button_search = QPushButton("Search")
        self.button_search.setObjectName("SearchButton")
        self.button_save = QPushButton("Save criteria")
        self.button_save.setObjectName("SearchButton")
        self.button_clean = QPushButton("Clean search")
        self.button_clean.setObjectName("SearchButton")
        self.button_layout.addWidget(self.button_search)
        self.button_layout.addWidget(self.button_save)
        self.button_layout.addWidget(self.button_clean)

        return self.button_layout

    def combo_size(self):
        self.size = QComboBox()
        self.size.setStyleSheet("QComboBox { background-color: LightBlue }; border-width: 2px")
        self.size.addItem("Bytes")
        self.size.addItem("Kb")
        self.size.addItem("Mb")
        self.size.addItem("Gb")

        return self.size


    def get_table(self):
        return self.table

    def get_file_name(self):
        return self.fileName.text()

    def get_file_extention(self):
        return self.extText.text()

    def get_path(self):
        return self.size_line.text()

    def get_search_button(self):
        return self.button_search

    def get_size_combo(self):
        return self.size.text()

    def get_file_size(self):
        return self.size_line.text()

    def get_isHidden(self):
        if self.hidden.isChecked() == True:
            return True
        else:
            return False

    def get_isReadOnly(self):
        if self.read_only.isChecked() == True:
            return True
        else:
            return False

