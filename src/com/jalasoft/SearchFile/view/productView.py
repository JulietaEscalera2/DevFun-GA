from PyQt5.QtWidgets import QWidget, QPushButton, QTableWidgetItem, QHBoxLayout,QGroupBox, QFormLayout, QLabel,QLineEdit,QComboBox,QTableWidget


class ProductView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        vLayout = QHBoxLayout()
        group = QGroupBox()
        form = QFormLayout()
        self.pathText = QLineEdit()

        form.addRow(QLabel("Path"), self.pathText)
        form.addRow(QLabel("File Name"), QComboBox())
        form.addRow(QLabel("Ext"), QLineEdit())
        group.setLayout(form)
        buttons = QPushButton("Search")
        self.table = QTableWidget()
        #self.table.setStyle("background-color: red")
        self.table.setColumnCount(3)
        self.table.setRowCount(1)

        self.table.setHorizontalHeaderLabels(["path","file name","ext"])
        # self.table.setItem(0,0, QTableWidgetItem("c:'\'test"))
        # self.table.setItem(0,1, QTableWidgetItem("video.mp4"))
        # self.table.setItem(0,2, QTableWidgetItem("mp4"))

        vLayout.addWidget(group)
        vLayout.addWidget(buttons)
        vLayout.addWidget(self.table)
        self.setLayout(vLayout)

    def getTable(self):
        return self.table

    def getPath(self):
        return self.pathText.text()
