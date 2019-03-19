
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QTableWidgetItem, QHBoxLayout, QGroupBox, QFormLayout, QLabel, \
    QLineEdit, QComboBox, QTableWidget, QVBoxLayout


class ProductView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):


        self.vLayout = QHBoxLayout()
        self.group = QGroupBox()
        self.form = QFormLayout()
        layout = QVBoxLayout()

        self.pathText = QLineEdit()
        self.fileName = QLineEdit()
        self.extText = QLineEdit()

        self.form.addRow(QLabel("Path"), self.pathText)
        self.form.addRow(QLabel("File Name"), self.fileName)
        self.form.addRow(QLabel("Extention"), self.extText)
        #self.form.addChildLayout(layout)

        buttonSearch = QPushButton("Search")
        buttonSearch.setGeometry(10, 70, 70, 25)
        buttonSearch.setStyleSheet("font-size: 12px; color: #3232C0;")
        self.form.addWidget(buttonSearch)

        buttonSave = QPushButton("Save")
        #buttonSave.setGeometry(10, 70, 70, 25)
        buttonSave.setIcon(QIcon(QPixmap("./src/com/jalasoft/SearchFile/view/images/file.png")))
        buttonSave.setStyleSheet("font-size: 12px; color: #3232C0;")
        buttonSave.clicked.connect(lambda:buttonSave.whichbtn(buttonSave, style="font: 20px; color: green;"))
        layout.addWidget(buttonSave)


        self.form.addChildLayout(layout)
        self.form.setVerticalSpacing(20)
        self.group.setLayout(self.form)


        self.table = QTableWidget()
        self.table.size()
        self.table.setStyleSheet("font-size: 12px; color: #3232C0;")
        self.table.setColumnCount(3)
        self.table.setRowCount(1)


        self.table.setHorizontalHeaderLabels(["Path",u"File Name",u"Ext"])
        # self.table.setItem(0,0, QTableWidgetItem("c:'\'test"))
        # self.table.setItem(0,1, QTableWidgetItem("video.mp4"))
        # self.table.setItem(0,2, QTableWidgetItem("mp4"))

        self.vLayout.addWidget(self.group)
        self.vLayout.addWidget(self.table)
        self.setLayout(self.vLayout)

    def getTable(self):
        return self.table

    def getFileName(self):
        return self.fileName.text()

    def getExtention(self):
        return self.extText.text()

    def getPath(self):
        return self.pathText.text()
