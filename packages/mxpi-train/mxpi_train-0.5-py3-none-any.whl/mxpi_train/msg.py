import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QWidget
from mxpi_train.ui_msg import Ui_Form

class MsgWindow(QWidget,Ui_Form):
    def __init__(self):
        super(MsgWindow, self).__init__()
        self.setupUi(self) 
        self.setWindowFlag(Qt.FramelessWindowHint)

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MsgWindow()
    w.show()
    sys.exit(app.exec_())