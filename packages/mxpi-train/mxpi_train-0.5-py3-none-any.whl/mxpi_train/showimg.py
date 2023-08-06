from mxpi_train.ui_showimg import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon,QImage,QPixmap
import sys,cv2

class ShowImgWindow(QWidget,Ui_Form):
    def __init__(self,imgurl,name):
        super(ShowImgWindow, self).__init__()
        self.setupUi(self) 
        self.imgurl=imgurl
        self.name=name
        self.setWindowTitle("图片显示 ："+self.name)
        self.Fun()
    def Fun(self):
        opencv_img = cv2.imread(self.imgurl, 1)
        if opencv_img is None:
            pass
        else:
            self.Image = opencv_img
            self.DispImg()
    def DispImg(self):
        shrink = cv2.cvtColor(self.Image, cv2.COLOR_BGR2RGB)
        self.QtImg = QImage(shrink.data,
                                  shrink.shape[1],
                                  shrink.shape[0],
                                  shrink.shape[1] * 3,
                                  QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(self.QtImg))
        self.label.setScaledContents(True) #图片自适应
        self.label.show()


if __name__=='__main__':
    app = QApplication(sys.argv)
    w = ShowImgWindow()
    w.show()
    sys.exit(app.exec_())