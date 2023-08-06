import os,random
from tqdm import tqdm
import shutil
from shutil import copyfile
import traceback

def manage_class_data(train_data):
    iop=[]
    if os.path.exists(train_data+'/Train_data'):
        shutil.rmtree(train_data+'/Train_data')
    classes=os.listdir(train_data)
    for cl in tqdm(classes,desc="校验数据集"):
        ls=get_jpg(train_data+'/'+cl)
        print(cl+'种类具有'+str(len(ls))+'张图像')
        iop.append(cl+'种类具有'+str(len(ls))+'张图像')
        if len(ls)==0:
            return (False,cl+'种类照片为0,请检查!')
    return (True,iop)



def copy_file(train_data):
    try:
        if os.path.exists(train_data+'/Train_data'):
            shutil.rmtree(train_data+'/Train_data')
        classes=os.listdir(train_data)
        os.mkdir(train_data+'/Train_data')
        os.mkdir(train_data+'/Train_data/train')
        os.mkdir(train_data+'/Train_data/val')
        os.mkdir(train_data+'/Train_data/test')
        for i in tqdm(classes,desc="准备训练数据集"):
            os.mkdir(train_data+'/Train_data/train/'+i)
            os.mkdir(train_data+'/Train_data/val/'+i)
            file_list=os.listdir(train_data+'/'+i)
            train_file_list,s=data_split(file_list,ratio=0.8, shuffle=True)
            val_file_list,test_file_list=data_split(s,ratio=0.9, shuffle=True)
            for train_file in train_file_list:
                copyfile(train_data+'/'+i+'/'+train_file,train_data+'/Train_data/train/'+i+'/'+train_file)
            for val_file in val_file_list:
                copyfile(train_data+'/'+i+'/'+val_file,train_data+'/Train_data/val/'+i+'/'+val_file)
            for test_file in test_file_list:
                copyfile(train_data+'/'+i+'/'+test_file,train_data+'/Train_data/test/'+test_file)
        return True
    except Exception as e:
        traceback.print_exc()
        return False


def data_split(full_list, ratio, shuffle=False):
    """
    数据集拆分: 将列表full_list按比例ratio（随机）划分为2个子列表sublist_1与sublist_2
    :param full_list: 数据列表
    :param ratio:     子列表1
    :param shuffle:   子列表2
    :return:
    """
    n_total = len(full_list)
    offset = int(n_total * ratio)
    if n_total == 0 or offset < 1:
        return [], full_list
    if shuffle:
        random.shuffle(full_list)
    sublist_1 = full_list[:offset]
    sublist_2 = full_list[offset:]
    return sublist_1, sublist_2

def get_jpg(path):
    jpg=[]
    path_list=os.listdir(path)
    for filename in path_list:
        if os.path.splitext(filename)[1] == '.jpg':
            jpg.append(filename)
    return jpg

if __name__=='__main__':
    url='refuse_classification'
    if manage_class_data(url):
        if copy_file(url):
            print('数据训练数据准备完成')