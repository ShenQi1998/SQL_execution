import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication

def msg(msg):
    app = QApplication(sys.argv)
    msgWindow(msg)

class msgWindow(QWidget):

    def __init__(self , msg):
        super().__init__()
        msg_box = QMessageBox(QMessageBox.about(self, "提示", msg) )
        # msg_box.buttonClicked.connect(self.close)
        self.close