import sys
import post
# from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication,QWidget,QDesktopWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout  #水平布局和垂直布局
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QCheckBox 
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QMessageBox


class MainWindow(QWidget):
    def __init__(self,envirs , datebase):
        super().__init__()
        self.setWindowTitle("SQL_EXECUTE")
        self.resize(780,450)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)


        #字体
        font = QFont("宋体")
        font.setPixelSize(20)
        # self.show()

        layout = QHBoxLayout()      #左半部分 水平布局

        layout_left = QHBoxLayout()

        self.textEdit = QTextEdit()
        self.textEdit.setFont(font)
        self.textEdit.setMinimumWidth(350)
        layout_left.addWidget(self.textEdit)
        layout.addLayout(layout_left)



        layout_right = QVBoxLayout()    #右半部分 垂直布局 
        
        #右侧partitinon1  复选框
        self.cb_envir =QComboBox()
        self.cb_envir.addItems(envirs)
        self.cb_envir.setFont(font)
        layout_right.addWidget(self.cb_envir)

        #右侧partitinon2  多选框
        self.layout_db = QVBoxLayout()    #垂直布局 
        self.layout_db.setSpacing(3)
        self.layout_db.setContentsMargins( 10 , 0, 0, 0)

        for db in datebase:
            checkbox = QCheckBox(db.ljust(12, " "))
            # checkbox = QCheckBox(db)

            checkbox.setCheckState(Qt.Checked)
  
            checkbox.setFont(font)

            self.layout_db.addWidget(checkbox)
            # self.layout_db.setAlignment(Qt.AlignCenter)        #居中

        self.layout_db.addStretch()

        #右侧partitinon3  按钮     
        layout_right_button = QHBoxLayout()
        layout_right_button.setContentsMargins(0, 0, 0, 0)
        self.btn_select_all = QPushButton("全选")
        self.btn_select_all.setFont(font)
        self.btn_select_all.clicked.connect(self.ButtonSelect)

        layout_right_button.addWidget(self.btn_select_all)
        btn_stop = QPushButton("执行")
        btn_stop.setFont(font)
        btn_stop.clicked.connect(self.ButtonCommit)
        layout_right_button.addWidget(btn_stop)

        layout_right.addLayout(self.layout_db)
        layout_right.addLayout(layout_right_button)
        layout.addLayout(layout_right)

        self.setLayout(layout)

    #多选按钮
    def ButtonSelect(self):
        if (self.btn_select_all.text() == "全选"):
            for i in range(self.layout_db.count()):
                chBox = self.layout_db.itemAt(i).widget()
                if chBox is not None :
                    chBox.setChecked(True)
            self.btn_select_all.setText( "全不选")
        else:
            for i in range(self.layout_db.count()):
                chBox = self.layout_db.itemAt(i).widget()
                if chBox is not None :
                    chBox.setChecked(False)
            self.btn_select_all.setText( "全选")
        # self.label.setText("selected QCheckBox: " + str(list(checked_list)))  

    #执行按钮
    def ButtonCommit(self):
        checked_list = []
        for i in range(self.layout_db.count()):
            chBox = self.layout_db.itemAt(i).widget()
            if chBox is not None and chBox.isChecked():
                checked_list.append(chBox.text().rstrip() )
        print("selected QCheckBox: " + str(checked_list))
        print("selected QComboBox: " + self.cb_envir.currentText())
        print("Input Text: " + self.textEdit.toPlainText())
        post.commit(self.cb_envir.currentText() , checked_list , self.textEdit.toPlainText() )

    def messageBox(self , msg):
        msg_box = QMessageBox.about(self, "提示", "这是关于软件的说明。。。")
        msg_box.exec_()

def main( envirs , datebase ):
    app = QApplication(sys.argv)
    window = MainWindow(envirs,datebase)
    window.show()
    sys.exit(app.exec_())  

