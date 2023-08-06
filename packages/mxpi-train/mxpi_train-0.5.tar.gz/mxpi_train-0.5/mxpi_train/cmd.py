

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QWindow,QCursor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
import win32gui
from mxpi_train.Ui_cmd import Ui_Form
import subprocess
import shlex
from PyQt5.QtCore import QThread , pyqtSignal

class MyThread(QThread):
    s = pyqtSignal(str)
    def __init__(self):
        super(MyThread, self).__init__()
    def run(self):
        self.run_command('ping www.baidu.com')
    def run_command(self,command):
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        while process.poll()==None:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                data=(output.strip()).decode('gbk') 
                print(data)
                self.s.emit(data)
        rc = process.poll()
        return rc


class Window(QWidget,Ui_Form):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self) 
        self._cmdHwnd = -1
        self.embedCmd()
        self.myhwnd = int(self.winId())  # 自己的句柄
        self.setWindowFlag(Qt.FramelessWindowHint)

    def closeEvent(self, event):
        if self._cmdHwnd > -1:
            try:
                win32gui.SetParent(self._cmdHwnd, win32gui.GetDesktopWindow())
            except:
                pass
        super(Window, self).closeEvent(event)

    def embedCmd(self):
        # 嵌入cmd窗口
        self._cmdHwnd = win32gui.FindWindow('ConsoleWindowClass', None)
        print(self._cmdHwnd)
        if self._cmdHwnd > -1:
            self.embedCmdWindow()

    def embedCmdWindow(self):
        window = QWindow.fromWinId(self._cmdHwnd)
        widget = QWidget.createWindowContainer(window)
        self.horizontalLayout.addWidget(widget)
        widget.setMouseTracking(True)
        widget.setFocusPolicy(Qt.StrongFocus)
        widget.setAttribute(Qt.WA_NativeWindow, True)
        widget.setAttribute(Qt.WA_PaintOnScreen, True)
        window.requestActivate()

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
    w = Window()
    w.show()
    sys.exit(app.exec_())
