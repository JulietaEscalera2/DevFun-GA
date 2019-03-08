from PyQt5.QtWidgets import QWidget, QPushButton, QTableWidgetItem, QHBoxLayout,QGroupBox, QFormLayout, QLabel,QLineEdit,QComboBox,QTableWidget


class ProductView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        vLayout = QHBoxLayout()
        group = QGroupBox()
        form = QFormLayout()

        form.addRow(QLabel("Path"), QLineEdit())
        form.addRow(QLabel("File Name"), QComboBox())
        form.addRow(QLabel("Ext"), QLineEdit())
        group.setLayout(form)
        buttons = QPushButton("Search")
        table = QTableWidget()
        table.setColumnCount(3)
        table.setRowCount(1)

        table.setHorizontalHeaderLabels(["path","file name","ext"])
        table.setItem(0,0, QTableWidgetItem("c:'\'test"))
        table.setItem(0,1, QTableWidgetItem("video.mp4"))
        table.setItem(0,2, QTableWidgetItem("mp4"))

        vLayout.addWidget(group)
        vLayout.addWidget(buttons)
        vLayout.addWidget(table)
        self.setLayout(vLayout)
