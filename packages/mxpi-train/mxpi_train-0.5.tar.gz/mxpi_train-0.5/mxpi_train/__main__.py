import sys,os,cv2,traceback,time
import mxpi_train,signal
from PyQt5.QtCore import QThread , pyqtSignal,QSize
from PyQt5.QtGui import QIcon,QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox,QInputDialog,QWidget, QVBoxLayout, QAction,QLineEdit,QFileDialog,QListWidget,QListWidgetItem
from mxpi_train.ui_main import Ui_MainWindow
from mxpi_train.cmd import Window,MyThread
from mxpi_train.msg import MsgWindow
import subprocess
import shlex,traceback
from mxpi_train.showimg import ShowImgWindow
from mxpi_train.ui_about import Ui_Form
import xml.etree.ElementTree as ET
import yaml,torch,time
import mxpi_train.datase as datase
import shutil
import webbrowser
import mxpi_train.classdata as classdata


class AboutWindow(QWidget,Ui_Form):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.setupUi(self) 

#目标识别测试
class TestCmdThread(QThread):
    s = pyqtSignal(str)
    start_test = pyqtSignal(bool)
    def __init__(self,configs,model):
        super(TestCmdThread, self).__init__()
        self.s.emit('开始测试')
        self.configs=configs
        self.model=model
        if os.path.exists(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/ModelNet/result'):
            shutil.rmtree(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/ModelNet/result')
        os.mkdir(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/ModelNet/result')
    def run(self):
        try:
            self.start_test.emit(True)
            cmd='python '+os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/ModelNet/FastDev/test.py --img_path '+self.configs['DATASET']['TEST']+' --yaml '+os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/configs/configs.yaml --onnx '+self.model
            print(cmd)
            cmds=self.run_command(cmd)
            if cmds==0:
                print('测试结束')
                self.s.emit('测试结束')
                self.start_test.emit(False)
        except Exception as e:
            traceback.print_exc()
            self.start_test.emit(False)
            self.s.emit('测试出错,请查看终端信息')

    def kill(self):
        try:
            self.process.kill()
        except:
            pass
        self.start_train.emit(False)

    def run_command(self,command):
        self.process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        while self.process.poll()==None:
            output = self.process.stdout.readline()
            if output == '' and self.process.poll() is not None:
                break
            if output:
                data=str(output,'gbk')
                print(data.replace('\n',''))
                self.s.emit(data.replace('\n',''))
        rc = self.process.poll()
        return rc


#目标识别训练
class RunCmdThread(QThread):
    s = pyqtSignal(str)
    start_train = pyqtSignal(bool)
    def __init__(self,configs):
        super(RunCmdThread, self).__init__()
        self.configs=configs
        self.ok=True
        if os.path.exists(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/logs'):
            shutil.rmtree(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/logs')
    def run(self):
        try:
            self.start_train.emit(True)
            img_dirs=self.configs['DATASET']['IMG']
            xml_dirs=self.configs['DATASET']['XML']
            classes=self.configs['DATASET']['NAMES'].split(',')
            self.s.emit('开始校验数据集')
            print('开始校验数据集')
            msg=datase.manage_data(img_dirs,xml_dirs)
            if msg[0]:
                t=datase.copy_file_txt(img_dirs,xml_dirs,classes)
                if t[0]:
                    now = int(time.time())
                    save_file=os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/Model_file/FastestDet'+str(now)
                    os.mkdir(save_file)
                    self.configs['DATASET']['TRAIN']=t[1]
                    self.configs['DATASET']['VAL']=t[2]
                    self.configs['DATASET']['TEST']=t[3]
                    self.yaml_updata(self.configs)
                    if self.ok:
                        print('开始训练')
                        self.s.emit('开始训练')
                        cmd='python '+os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/ModelNet/FastDev/train.py --device '+self.configs['TRAIN']['DEVICE']+' --yaml '+os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/configs/configs.yaml --save '+save_file
                        print(cmd)
                        cmds=self.run_command(cmd)
                        if cmds==0:
                            print('训练结束')
                            self.s.emit('训练结束')
                            self.start_train.emit(False)
                    else:
                        print('训练终止')
                        self.s.emit('训练终止')
                else:
                    self.s.emit(t[1])
            else:
                self.s.emit(msg[1])
        except Exception as e:
            traceback.print_exc()
            self.start_train.emit(False)
            self.s.emit('训练出错,请查看终端信息')

    def kill(self):
        try:
            self.process.kill()
        except:
            pass
        self.ok=False
        self.start_train.emit(False)

    def run_command(self,command):
        self.process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        while self.process.poll()==None:
            output = self.process.stdout.readline()
            if output == '' and self.process.poll() is not None:
                break
            if output:
                data=str(output,'gbk')
                print(data.replace('\n',''))
                self.s.emit(data.replace('\n',''))
        rc = self.process.poll()
        return rc

    def yaml_updata(self,data):
        f=open(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/configs/configs.yaml','w',encoding='utf-8')
        yaml.dump(data,f)
        f.close()

#图像分类训练
class RunClassCmdThread(QThread):
    s = pyqtSignal(str)
    start_train = pyqtSignal(bool)
    def __init__(self,configs):
        super(RunClassCmdThread, self).__init__()
        self.configs=configs
        self.ok=True
        if os.path.exists(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/logs'):
            shutil.rmtree(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/logs')
    def run(self):
        try:
            self.start_train.emit(True)
            dirs=self.configs['DATASET']['CLASS']
            classes=self.configs['DATASET']['CLASSNAME'].split(',')
            self.s.emit('开始校验数据集')
            print('开始校验数据集')
            msg=classdata.manage_class_data(dirs)
            if msg[0]:
                self.s.emit('数据集校验完成')
                print('数据集校验完成')
                for m in msg[1]:
                    self.s.emit(m)
                self.s.emit('开始准备训练数据集')
                print('开始准备训练数据集')
                t=classdata.copy_file(dirs)
                if t:
                    self.s.emit('训练数据集准备完成')
                    print('训练数据集准备完成')
                    now = int(time.time())
                    save_file=os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/Model_file/Classification'+str(now)
                    os.mkdir(save_file)
                    if self.ok:
                        self.s.emit('开始训练...')
                        print('开始训练...')
                        cmd='python '+os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/ModelNet/Classification/train.py --device '+self.configs['TRAIN']['DEVICE']+' --yaml '+os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/configs/configs.yaml --save '+save_file+'/Classification_Model.pth'
                        print(cmd)
                        cmds=self.run_command(cmd)
                        if cmds==0:
                            print('训练结束')
                            self.s.emit('训练结束')
                            self.start_train.emit(False)
                    else:
                        print('训练终止')
                        self.s.emit('训练终止')
            else:
                self.s.emit(msg[1])
        except Exception as e:
            traceback.print_exc()
            self.start_train.emit(False)
            self.s.emit('训练出错,请查看终端信息')

    def kill(self):
        try:
            self.process.kill()
        except:
            pass
        self.ok=False
        self.start_train.emit(False)

    def run_command(self,command):
        self.process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        while self.process.poll()==None:
            output = self.process.stdout.readline()
            if output == '' and self.process.poll() is not None:
                break
            if output:
                data=str(output,'gbk')
                print(data.replace('\n',''))
                self.s.emit(data.replace('\n',''))
        rc = self.process.poll()
        return rc

    def yaml_updata(self,data):
        f=open(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/configs/configs.yaml','w',encoding='utf-8')
        yaml.dump(data,f)
        f.close()

class TestClassCmdThread(QThread):
    s = pyqtSignal(str)
    start_test = pyqtSignal(bool)
    def __init__(self,configs,model):
        super(TestClassCmdThread, self).__init__()
        self.s.emit('开始测试')
        self.configs=configs
        self.model=model
        if os.path.exists(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/ModelNet/result'):
            shutil.rmtree(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/ModelNet/result')
        os.mkdir(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/ModelNet/result')
    def run(self):
        try:
            self.start_test.emit(True)
            cmd='python '+os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/ModelNet/Classification/test.py --device '+self.configs['TRAIN']['DEVICE']+' --yaml '+os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/configs/configs.yaml --model '+self.model
            print(cmd)
            cmds=self.run_command(cmd)
            if cmds==0:
                print('测试结束')
                self.s.emit('测试结束')
                self.start_test.emit(False)
        except Exception as e:
            traceback.print_exc()
            self.start_test.emit(False)
            self.s.emit('测试出错,请查看终端信息')

    def kill(self):
        try:
            self.process.kill()
        except:
            pass
        self.start_train.emit(False)

    def run_command(self,command):
        self.process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        while self.process.poll()==None:
            output = self.process.stdout.readline()
            if output == '' and self.process.poll() is not None:
                break
            if output:
                data=str(output,'gbk')
                print(data.replace('\n',''))
                self.s.emit(data.replace('\n',''))
        rc = self.process.poll()
        return rc

class CamThread(QThread):
    ok = pyqtSignal(bool)
    err = pyqtSignal(str)
    def __init__(self,id,label):
        super(CamThread, self).__init__()
        self.id=id
        self.label=label
        self.num=1
        self.stop=True
    def run(self):
        self.open_camera(self.id)
    def open_camera(self,id):
        try:
            self.cap = cv2.VideoCapture(id)  # 摄像头
            while self.stop:
                flag, self.image = self.cap.read()  # 从视频流中读取图片
                self.img=self.image.copy()
                width, height = self.image.shape[:2]  # 行:宽，列:高
                self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # opencv读的通道是BGR,要转成RGB
                self.image = cv2.flip(self.image, 1)  # 水平翻转，因为摄像头拍的是镜像的。
                self.showImage = QImage(self.image.data, height, width, QImage.Format_RGB888)
                self.label.setPixmap(QPixmap.fromImage(self.showImage))  # 往显示视频的Label里显示QImage
                self.label.setScaledContents(True) #图片自适应
                self.ok.emit(True)
                time.sleep(0.03)
        except Exception as e:
            self.ok.emit(False)
            self.err.emit('摄像头打开失败！')
            traceback.print_exc()
    def paiz(self,url,name,bar,listw):
        try:
            listw.addItem(name+'_'+str(self.num)+'.jpg')
            bar.showMessage('拍照成功:'+url+'/'+name+'_'+str(self.num)+'.jpg',5000)
            cv2.imwrite(url+'/'+name+'_'+str(self.num)+'.jpg',self.img)
            self.num += 1
        except:
            pass

class Select_name_Thread(QThread):
    s = pyqtSignal(list)
    def __init__(self,xml):
        super(Select_name_Thread, self).__init__()
        self.xml=xml
    def run(self):
        n=self.convert_name(self.xml)
        print(n)
        self.s.emit(n)
    def convert_name(self,xml_url):
        L=[]
        f_name=self.file_name(xml_url)
        for url in f_name:
            tree=ET.parse(url)
            root = tree.getroot()
            for obj in root.iter('object'):
                name=obj.find("name").text
                if name in L:
                    pass
                else:
                    L.append(name)
        return L

    def file_name(self,file_dir):   
        L=[]   
        for root, dirs, files in os.walk(file_dir):  
            for file in files:  
                if os.path.splitext(file)[1] == '.xml':  # 想要保存的文件格式
                    L.append(os.path.join(root, file))  
        return L

class Select_classname_Thread(QThread):
    s = pyqtSignal(list)
    def __init__(self,url):
        super(Select_classname_Thread, self).__init__()
        self.url=url
    def run(self):
        name=[]
        for i in os.listdir(self.url):
            if i !='Train_data':
                name.append(i)
        self.s.emit(name)


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self) 
        self.camo=False
        self.start_t=False
        self.start_tt=False
        self.start_c=False
        self.start_cc=False

        #工具栏
        info = QAction(QIcon(''), '关于', self)
        self.toolBar.addAction(info)
        info.triggered.connect(self.showabout)
        exitAct = QAction(QIcon(''), '模型文件夹', self)
        self.toolBar.addAction(exitAct)
        exitAct1 = QAction(QIcon(''), '信息窗口', self)
        self.toolBar.addAction(exitAct1)
        exitAct2 = QAction(QIcon(''), 'Tensorboard', self)
        self.toolBar.addAction(exitAct2)
        exitAct3 = QAction(QIcon(''), 'LabelImg标注工具', self)
        self.toolBar.addAction(exitAct3)
        exitAct.triggered.connect(self.openmodelFile)
        exitAct1.triggered.connect(self.openmsg)
        exitAct2.triggered.connect(self.openTensorboard)
        exitAct3.triggered.connect(self.openLabelImg)

        #终端窗口
        self.w = Window()
        self.w.show()
        self.w.hide()
        self.w.pushButton.clicked.connect(self.closecmd)
        self.w.pushButton_2.clicked.connect(self.clscmd)

        #信息窗口
        self.msg = MsgWindow()
        self.msg.show()
        self.msg.hide()
        self.msg.pushButton.clicked.connect(self.closemsg)
        self.msg.pushButton_2.clicked.connect(self.clsmsg)

        #初始化
        os.system('cls')
        print('Ready...')

        #读取配置文件
        f=open(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/configs/configs.yaml','r',encoding='utf-8')
        cfg=f.read()
        self.configs=yaml.load(cfg,Loader=yaml.FullLoader)
        f.close()
        self.lineEdit_3.setText(self.configs['DATASET']['IMG'])
        self.lineEdit_4.setText(self.configs['DATASET']['XML'])
        self.lineEdit_5.setText(self.configs['DATASET']['NAMES'])
        self.lineEdit_6.setText(self.configs['DATASET']['CLASS'])
        self.lineEdit_7.setText(self.configs['DATASET']['CLASSNAME'])
        self.spinBox_2.setValue(self.configs['MODEL']['INPUT_WIDTH'])
        self.spinBox_3.setValue(self.configs['MODEL']['INPUT_HEIGHT'])
        self.spinBox_4.setValue(self.configs['TRAIN']['BATCH_SIZE'])
        self.spinBox_5.setValue(self.configs['TRAIN']['END_EPOCH'])
        self.spinBox_6.setValue(self.configs['TRAIN']['CLASS_EPOCH'])
        
        if self.configs['TRAIN']['DEVICE']=='cpu':
            self.radioButton_2.setChecked(True)
            self.radioButton_4.setChecked(True)
        elif self.configs['TRAIN']['DEVICE']=='cuda':
            self.radioButton.setChecked(True)
            self.radioButton_3.setChecked(True)

        act = QAction(self)
        act.setIcon(QIcon(':/ico/image/anniu.png'))
        act.triggered.connect(self.select_img)
        self.lineEdit_3.addAction(act,QLineEdit.TrailingPosition)
        self.lineEdit_3.textChanged.connect(self.x_img) 

        act = QAction(self)
        act.setIcon(QIcon(':/ico/image/anniu.png'))
        act.triggered.connect(self.select_xml)
        self.lineEdit_4.addAction(act,QLineEdit.TrailingPosition)
        self.lineEdit_4.textChanged.connect(self.x_xml) 

        act = QAction(self)
        act.setIcon(QIcon(':/ico/image/anniu.png'))
        act.triggered.connect(self.select_name)
        self.lineEdit_5.addAction(act,QLineEdit.TrailingPosition)
        self.lineEdit_5.textChanged.connect(self.x_name)

        act = QAction(self)
        act.setIcon(QIcon(':/ico/image/anniu.png'))
        act.triggered.connect(self.select_class)
        self.lineEdit_6.addAction(act,QLineEdit.TrailingPosition)
        self.lineEdit_6.textChanged.connect(self.x_class)

        act = QAction(self)
        act.setIcon(QIcon(':/ico/image/anniu.png'))
        act.triggered.connect(self.select_classname)
        self.lineEdit_7.addAction(act,QLineEdit.TrailingPosition)
        self.lineEdit_7.textChanged.connect(self.x_classname)

        self.spinBox_2.valueChanged.connect(self.x_model_width)
        self.spinBox_3.valueChanged.connect(self.x_model_height)
        self.spinBox_4.valueChanged.connect(self.x_train_batch)
        self.spinBox_5.valueChanged.connect(self.x_train_exp)
        self.spinBox_6.valueChanged.connect(self.x_classtrain_exp)
        self.radioButton.clicked.connect(self.x_cuda)
        self.radioButton_2.clicked.connect(self.x_cuda)
        self.radioButton_3.clicked.connect(self.x_cuda)
        self.radioButton_4.clicked.connect(self.x_cuda)

        #拍照
        self.pushButton.clicked.connect(self.opencam)
        self.pushButton_2.clicked.connect(self.campai)
        act = QAction(self)
        act.setIcon(QIcon(':/ico/image/anniu.png'))
        act.triggered.connect(self.select_cam_savefile)
        self.lineEdit.addAction(act,QLineEdit.TrailingPosition)
        self.listWidget.doubleClicked.connect(self.on_double_clicked)
        self.listWidget_2.doubleClicked.connect(self.on_double_clicked_test)
        self.listWidget_3.doubleClicked.connect(self.on_double_clicked_test)

        #开始训练
        self.pushButton_3.clicked.connect(self.start_train_yolo)
        #测试模型
        self.pushButton_5.clicked.connect(self.test_img_bt)

        #开始训练
        self.pushButton_4.clicked.connect(self.start_train_class)
        #测试模型
        self.pushButton_6.clicked.connect(self.test_classimg_bt)

    def openLabelImg(self):
        cmd='labelimg2'
        self.res = subprocess.Popen(cmd)
        
    def showabout(self):
        self.about=AboutWindow()
        self.about.show()

    def start_train_class(self):
        if self.start_c==False:
            self.train_class=RunClassCmdThread(self.configs)
            self.train_class.s.connect(self.add_msg)
            self.train_class.start_train.connect(self.set_trainbuttonclass)
            self.train_class.start()
        else:
            self.train_class.kill()

    def start_train_yolo(self):
        if self.start_t==False:
            self.train_yolo=RunCmdThread(self.configs)
            self.train_yolo.s.connect(self.add_msg)
            self.train_yolo.start_train.connect(self.set_trainbutton)
            self.train_yolo.start()
        else:
            self.train_yolo.kill()
    
    def test_img_bt(self):
        if self.start_tt==False:
            directory,type= QFileDialog.getOpenFileName(self,"选择模型文件",os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/Model_file',"Model Files (*.onnx);;All Files (*)")
            if len(directory)>0:
                self.test_yolo=TestCmdThread(self.configs,directory)
                self.test_yolo.s.connect(self.add_msg)
                self.test_yolo.start_test.connect(self.set_testbutton)
                self.test_yolo.start()
    
    def test_classimg_bt(self):
        if self.start_cc==False:
            directory,type= QFileDialog.getOpenFileName(self,"选择模型文件",os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/Model_file',"Model Files (*.pth);;All Files (*)")
            if len(directory)>0:
                self.test_class=TestClassCmdThread(self.configs,directory)
                self.test_class.s.connect(self.add_msg)
                self.test_class.start_test.connect(self.set_classtestbutton)
                self.test_class.start()

    def openTensorboard(self):
        if os.path.exists(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/logs'):
            try:
                self.res.killpg(self.pid,signal.SIGUSR1)
            except:
                pass
            cmd='cd '+os.path.dirname(mxpi_train.__file__).replace('\\','/')+' & tensorboard --logdir=logs --port=6067'
            print(cmd)
            self.res = subprocess.Popen(cmd,shell = True)
            webbrowser.open("http://localhost:6067/")
        else:
            try:
                self.res.kill()
            except:
                pass
            self.showwarning('没有训练数据可以查看！')
    
    def set_testbutton(self,bo):
        if bo:
            self.pushButton_5.setStyleSheet("QPushButton\n"
            "{\n"
            "    background-color: #fa3a05;\n"
            "    color: #fff;\n"
            "    border-style: solid;\n"
            "    border-width: 1px;\n"
            "    border-radius: 10px;\n"
            "    border-color: #fa3a05;\n"
            "    padding: 2px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::hover\n"
            "{\n"
            "    background-color: #fb6d46;\n"
            "    color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::pressed\n"
            "{\n"
            "    background-color:#fa3a05;\n"
            "    color: #fff;\n"
            "\n"
            "}")
            self.pushButton_5.setText("停止验证")
            self.start_tt=True
        else:
            self.pushButton_5.setStyleSheet("QPushButton\n"
            "{\n"
            "    background-color: #08a15e;\n"
            "    color: #fff;\n"
            "    border-style: solid;\n"
            "    border-width: 1px;\n"
            "    border-radius: 10px;\n"
            "    border-color: #08a15e;\n"
            "    padding: 2px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::hover\n"
            "{\n"
            "    background-color: #09ce78;\n"
            "    color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::pressed\n"
            "{\n"
            "    background-color:#08a15e;\n"
            "    color: #fff;\n"
            "\n"
            "}")
            self.pushButton_5.setText("验证模型")
            self.start_tt=False
            self.add_image_items(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/ModelNet/result')

    def set_classtestbutton(self,bo):
        if bo:
            self.pushButton_6.setStyleSheet("QPushButton\n"
            "{\n"
            "    background-color: #fa3a05;\n"
            "    color: #fff;\n"
            "    border-style: solid;\n"
            "    border-width: 1px;\n"
            "    border-radius: 10px;\n"
            "    border-color: #fa3a05;\n"
            "    padding: 2px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::hover\n"
            "{\n"
            "    background-color: #fb6d46;\n"
            "    color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::pressed\n"
            "{\n"
            "    background-color:#fa3a05;\n"
            "    color: #fff;\n"
            "\n"
            "}")
            self.pushButton_6.setText("停止验证")
            self.start_cc=True
        else:
            self.pushButton_6.setStyleSheet("QPushButton\n"
            "{\n"
            "    background-color: #08a15e;\n"
            "    color: #fff;\n"
            "    border-style: solid;\n"
            "    border-width: 1px;\n"
            "    border-radius: 10px;\n"
            "    border-color: #08a15e;\n"
            "    padding: 2px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::hover\n"
            "{\n"
            "    background-color: #09ce78;\n"
            "    color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::pressed\n"
            "{\n"
            "    background-color:#08a15e;\n"
            "    color: #fff;\n"
            "\n"
            "}")
            self.pushButton_6.setText("验证模型")
            self.start_cc=False
            self.add_image_classitems(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/ModelNet/result')
            

    def add_image_classitems(self,image_path):
        self.listWidget_3.setViewMode(QListWidget.IconMode)
        self.listWidget_3.setWrapping(True)
        self.listWidget_3.setFlow(QListWidget.LeftToRight)
        self.listWidget_3.clear()
        self.image_paths=os.listdir(image_path)
        for img_path in self.image_paths:
            if os.path.isfile(image_path+'/'+img_path):
                item = QListWidgetItem(QIcon(image_path+'/'+img_path),img_path)
                self.listWidget_3.addItem(item)
        self.listWidget_3.setIconSize(QSize(int(self.listWidget_3.width()/6),90))

    def add_image_items(self,image_path):
        self.listWidget_2.setViewMode(QListWidget.IconMode)
        self.listWidget_2.setWrapping(True)
        self.listWidget_2.setFlow(QListWidget.LeftToRight)
        self.listWidget_2.clear()
        self.image_paths=os.listdir(image_path)
        for img_path in self.image_paths:
            if os.path.isfile(image_path+'/'+img_path):
                item = QListWidgetItem(QIcon(image_path+'/'+img_path),img_path)
                self.listWidget_2.addItem(item)
        self.listWidget_2.setIconSize(QSize(int(self.listWidget_2.width()/6),90))

    def set_trainbuttonclass(self,bo):
        if bo:
            self.pushButton_4.setStyleSheet("QPushButton\n"
            "{\n"
            "    background-color: #fa3a05;\n"
            "    color: #fff;\n"
            "    border-style: solid;\n"
            "    border-width: 1px;\n"
            "    border-radius: 10px;\n"
            "    border-color: #fa3a05;\n"
            "    padding: 2px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::hover\n"
            "{\n"
            "    background-color: #fb6d46;\n"
            "    color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::pressed\n"
            "{\n"
            "    background-color:#fa3a05;\n"
            "    color: #fff;\n"
            "\n"
            "}")
            self.pushButton_4.setText("停止训练")
            self.start_c=True
        else:
            self.pushButton_4.setStyleSheet("QPushButton\n"
            "{\n"
            "    background-color: #08a15e;\n"
            "    color: #fff;\n"
            "    border-style: solid;\n"
            "    border-width: 1px;\n"
            "    border-radius: 10px;\n"
            "    border-color: #08a15e;\n"
            "    padding: 2px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::hover\n"
            "{\n"
            "    background-color: #09ce78;\n"
            "    color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::pressed\n"
            "{\n"
            "    background-color:#08a15e;\n"
            "    color: #fff;\n"
            "\n"
            "}")
            self.pushButton_4.setText("开始训练")
            self.start_c=False

    def set_trainbutton(self,bo):
        if bo:
            self.pushButton_3.setStyleSheet("QPushButton\n"
            "{\n"
            "    background-color: #fa3a05;\n"
            "    color: #fff;\n"
            "    border-style: solid;\n"
            "    border-width: 1px;\n"
            "    border-radius: 10px;\n"
            "    border-color: #fa3a05;\n"
            "    padding: 2px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::hover\n"
            "{\n"
            "    background-color: #fb6d46;\n"
            "    color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::pressed\n"
            "{\n"
            "    background-color:#fa3a05;\n"
            "    color: #fff;\n"
            "\n"
            "}")
            self.pushButton_3.setText("停止训练")
            self.start_t=True
        else:
            self.pushButton_3.setStyleSheet("QPushButton\n"
            "{\n"
            "    background-color: #08a15e;\n"
            "    color: #fff;\n"
            "    border-style: solid;\n"
            "    border-width: 1px;\n"
            "    border-radius: 10px;\n"
            "    border-color: #08a15e;\n"
            "    padding: 2px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::hover\n"
            "{\n"
            "    background-color: #09ce78;\n"
            "    color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::pressed\n"
            "{\n"
            "    background-color:#08a15e;\n"
            "    color: #fff;\n"
            "\n"
            "}")
            self.pushButton_3.setText("开始训练")
            self.start_t=False
        
    def x_cuda(self):
        if self.radioButton.isChecked() or self.radioButton_3.isChecked():
            if torch.cuda.is_available():
                self.configs['TRAIN']['DEVICE']='cuda'
                self.yaml_updata(self.configs)
            else:
                self.showwarning('检测到不支持GPU训练环境,请安装Pytorch的GPU版本。')
                self.radioButton_2.setChecked(True)
                self.radioButton_3.setChecked(True)
        if self.radioButton_2.isChecked() or self.radioButton_4.isChecked():
            self.configs['TRAIN']['DEVICE']='cpu'
            self.yaml_updata(self.configs)

    def x_train_batch(self):
        self.configs['TRAIN']['BATCH_SIZE']=self.spinBox_4.value()
        self.yaml_updata(self.configs)

    def x_model_height(self):
        self.configs['MODEL']['INPUT_HEIGHT']=self.spinBox_3.value()
        self.yaml_updata(self.configs)

    def x_model_width(self):
        self.configs['MODEL']['INPUT_WIDTH']=self.spinBox_2.value()
        self.yaml_updata(self.configs)

    def x_train_exp(self):
        self.configs['TRAIN']['END_EPOCH']=self.spinBox_5.value()
        self.yaml_updata(self.configs)

    def x_classtrain_exp(self):
        self.configs['TRAIN']['CLASS_EPOCH']=self.spinBox_6.value()
        self.yaml_updata(self.configs)

    def x_name(self):
        self.configs['DATASET']['NAMES']=self.lineEdit_5.text()
        self.configs['MODEL']['NC']=len(self.lineEdit_5.text().split(','))
        self.yaml_updata(self.configs)
    
    def x_classname(self):
        self.configs['DATASET']['CLASSNAME']=self.lineEdit_7.text()
        self.configs['MODEL']['CLASSNC']=len(self.lineEdit_7.text().split(','))
        self.yaml_updata(self.configs)

    def select_classname(self):
        if os.path.exists(self.lineEdit_6.text()):
            self.select_classname=Select_classname_Thread(self.lineEdit_6.text())
            self.select_classname.s.connect(self.add_classname)
            self.select_classname.start()

    def select_name(self):
        if os.path.exists(self.lineEdit_4.text()):
            self.select_name=Select_name_Thread(self.lineEdit_4.text())
            self.select_name.s.connect(self.add_name)
            self.select_name.start()

    def add_classname(self,name):
        self.lineEdit_7.setText(','.join(name))
        self.statusBar.showMessage('发现种类：'+str(name), 9999)

    def add_name(self,name):
        self.lineEdit_5.setText(','.join(name))
        self.statusBar.showMessage('发现种类：'+str(name), 9999)

    def x_img(self):
        self.configs['DATASET']['IMG']=self.lineEdit_3.text()
        self.yaml_updata(self.configs)

    def x_class(self):
        self.configs['DATASET']['CLASS']=self.lineEdit_6.text()
        self.yaml_updata(self.configs)

    def x_xml(self):
        self.configs['DATASET']['XML']=self.lineEdit_4.text()
        self.yaml_updata(self.configs)

    def select_img(self):
        directory = QFileDialog.getExistingDirectory(self, "选择图片文件夹", "./") 
        if len(directory)>0:
            self.lineEdit_3.setText(directory)
    
    def select_xml(self):
        directory = QFileDialog.getExistingDirectory(self, "选择标签文件夹", "./") 
        if len(directory)>0:
            self.lineEdit_4.setText(directory)

    def select_class(self):
        directory = QFileDialog.getExistingDirectory(self, "选择数据文件夹", "./") 
        if len(directory)>0:
            self.lineEdit_6.setText(directory)

    def select_cam_savefile(self):
        directory = QFileDialog.getExistingDirectory(self, "选择保存文件夹", "./") 
        if len(directory)>0:
            self.lineEdit.setText(directory)
            
    def opencam(self):
        if self.camo==False:
            self.listWidget.clear()
            self.id = QInputDialog(self)
            self.id.setOkButtonText('打开')
            self.id.setCancelButtonText('取消')
            num,ok=self.id.getInt(self, '打开摄像头', '输入摄像头ID')
            if ok and num>=0:
                self.cam=CamThread(num,self.label)
                self.cam.err.connect(self.showerr)
                self.cam.ok.connect(self.camzt)
                self.cam.start()
        else:
            self.camo=False
            self.cam.stop=False
            icon1 = QIcon()
            icon1.addPixmap(QPixmap(":/ico/image/cam.png"), QIcon.Normal, QIcon.Off)
            self.pushButton.setIcon(icon1)
            self.pushButton.setText("打开摄像头")
            self.label.setPixmap(QPixmap(""))

    def is_contains_chinese(self,strs):
        for _char in strs:
            if '\u4e00' <= _char <= '\u9fa5':
                return True
        return False

    def campai(self):
        if self.camo:
            if len(self.lineEdit.text())>0:
                if os.path.exists(self.lineEdit.text()):
                    if len(self.lineEdit_2.text())>0:
                        if self.is_contains_chinese(self.lineEdit.text()):
                            self.showwarning('保存路径不能含有中文。')
                        else:
                            if self.is_contains_chinese(self.lineEdit_2.text()):
                                self.showwarning('名称不能含有中文。')
                            else:
                                self.cam.paiz(self.lineEdit.text(),self.lineEdit_2.text(),self.statusBar,self.listWidget)
                    else:
                        self.showwarning('请输入名称。')
                else:
                    self.showwarning('照片保存路径不存在，请检查。')
            else:
                self.showwarning('请选择照片保存路径。')
        else:
            self.showwarning('请先打开摄像头。')

    def yaml_updata(self,data):
        f=open(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/configs/configs.yaml','w',encoding='utf-8')
        yaml.dump(data,f)
        f.close()

    def camzt(self,b):
        self.camo=b
        if b:
            icon1 = QIcon()
            icon1.addPixmap(QPixmap(":/ico/image/cam-start.png"), QIcon.Normal, QIcon.Off)
            self.pushButton.setIcon(icon1)
            self.pushButton.setText("关闭摄像头")
        else:
            icon1 = QIcon()
            icon1.addPixmap(QPixmap(":/ico/image/cam.png"), QIcon.Normal, QIcon.Off)
            self.pushButton.setIcon(icon1)
            self.pushButton.setText("打开摄像头")

    def runcmd(self):
        self.r=MyThread()
        self.r.s.connect(self.add_msg)
        self.r.start()

    def add_msg(self,txt):
        self.msg.plainTextEdit.appendPlainText(txt)
        self.statusBar.showMessage(txt, 9999)

    def openmsg(self):
        self.msg.show()

    def clscmd(self):
        os.system('cls')
    
    def clsmsg(self):
        self.msg.plainTextEdit.setPlainText('')

    def opencmd(self):
        self.w.show()

    def openmodelFile(self):
        os.startfile(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/Model_file')

    def closecmd(self):
        self.w.hide()

    def closemsg(self):
        self.msg.hide()
    
    def on_double_clicked(self,idx):
        # idx为QModelIndex类型，通过row方法获取数据索引值
        img_url=self.lineEdit.text()+'/'+self.listWidget.item(idx.row()).text()
        name=self.listWidget.item(idx.row()).text()
        self.simg=ShowImgWindow(img_url,name)
        self.simg.show()
    
    def on_double_clicked_test(self,idx):
        # idx为QModelIndex类型，通过row方法获取数据索引值
        name=self.image_paths[idx.row()]
        img_url=os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/ModelNet/result/'+name
        self.simg=ShowImgWindow(img_url,name)
        self.simg.show()

    def showerr(self,txt):
        self.msgbox=QMessageBox()
        self.msgbox.addButton('确定', QMessageBox.YesRole)
        self.msgbox.critical(self, "消息", txt) 

    def showwarning(self,txt):
        self.msgbox=QMessageBox()
        self.msgbox.addButton('确定', QMessageBox.YesRole)
        self.msgbox.warning(self, "消息", txt) 

def main():
    App = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(App.exec_())

main()
