from PyQt5.QtWidgets import QMenu, QLabel, QWidget, QFormLayout, QLineEdit, QVBoxLayout, QGroupBox, QPushButton, \
    QTableWidget, QTableWidgetItem, QComboBox, QHBoxLayout


class ProductView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # form = QFormLayout()
        # form.addRow(QLabel('name:'), QLineEdit())
        # self.setLayout(form)
        vLayout = QHBoxLayout() # si quiero que sea vertical usar QVBoxLayout()
        group = QGroupBox()
        form = QFormLayout()
        form.addRow(QLabel("Path"),QLineEdit())
        form.addRow(QLabel("FileName"),QComboBox())
        form.addRow(QLabel("Ext"),QLineEdit())
        group.setLayout(form)


        buttons = QPushButton("Search")
        table = QTableWidget()
        table.setColumnCount(3)
        table.setRowCount(1)
        table.setHorizontalHeaderLabels(["Path", "FN", "Ext"])
        table.setItem(0,0,QTableWidgetItem("C:\ttest"))
        table.setItem(0,1,QTableWidgetItem("Video.mp4"))
        table.setItem(0,2,QTableWidgetItem("mp4"))

        vLayout.addWidget(group)
        vLayout.addWidget(buttons)
        vLayout.addWidget(table)
        self.setLayout(vLayout)

