from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QGroupBox, QFormLayout, QLabel, \
    QLineEdit, QComboBox, QTableWidget, QVBoxLayout, QCheckBox


class ProductView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.hLayout = QHBoxLayout()
        self.group = QGroupBox()
        self.form = QFormLayout()
        layout = QFormLayout()
        layout_button = QHBoxLayout()

        self.pathText = QLineEdit()
        self.fileName = QLineEdit()
        self.extText = QLineEdit()
        self.size = QLineEdit()
        self.create_date = QLineEdit()
        self.hidden = QCheckBox()

        self.form.addRow(QLabel("Path"), self.pathText)
        self.form.addRow(QLabel("File Name"), self.fileName)
        self.form.addRow(QLabel("Extention"), self.extText)
        self.form.addRow(QLabel("Size"), self.size)
        self.form.addRow(QLabel("Create Date"), self.create_date)
        self.form.addRow(QLabel("Is hidden?"),self.hidden)


        self.buttonSearch = QPushButton("Search")
        self.buttonSave = QPushButton("Save")
        self.buttonClean = QPushButton("Clean")
        self.buttonSearch.setStyleSheet("font-size: 12px; color: #3232C0;")
        self.buttonSave.setStyleSheet("font-size: 12px; color: #3232C0;")
        self.buttonSave.setIcon(QIcon(QPixmap("./images/file.png")))
        self.buttonSave.setStyleSheet("font-size: 12px; color: #3232C0;")


        # self.form.addWidget(self.buttonSearch)
        # self.form.addWidget(self.buttonSave)
        # self.form.addWidget(self.buttonClean)

        layout.addWidget(self.buttonSearch)
        layout.addWidget(self.buttonSave)
        layout.addWidget(self.buttonClean)
        layout_button.addLayout(layout)

        self.form.setVerticalSpacing(10)
        self.form.addItem(layout)
        self.form.addItem(layout_button)

        self.group.setLayout(self.form)
        self.group.setLayout(layout_button)



        def loadProductInsertView(self):
            print("estoy aqui")

        self.buttonSave.clicked.connect(lambda: loadProductInsertView(self.buttonSave))

        self.table = QTableWidget()
        self.table.size()
        self.table.setStyleSheet("font-size: 12px; color: #3232C0;")
        self.table.setColumnCount(5)
        self.table.setRowCount(1)


        self.table.setHorizontalHeaderLabels(["Path",u"File Name",u"Ext","size", "Create Date"])
        self.hLayout.addWidget(self.group)
        self.hLayout.addLayout(self.form)
        self.hLayout.addWidget(self.table)

        self.setLayout(self.hLayout)

    def getTable(self):
        return self.table

    def getFileName(self):
        return self.fileName.text()

    def getExtention(self):
        return self.extText.text()

    def getPath(self):
        return self.pathText.text()
