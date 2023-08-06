import os,random
from tqdm import tqdm
import shutil
from shutil import copyfile
import xml.etree.ElementTree as ET
import traceback

def manage_data(img_dirs,xml_dirs):
    img_list=os.listdir(img_dirs)
    xml_list=os.listdir(xml_dirs)
    not_jpg=[]
    for i in tqdm(img_list,desc="校验图片文件"):
        if os.path.isdir(img_dirs+'/'+i):
            not_jpg.append(i)
    if len(not_jpg)>0:
        return (False,'图片文件夹中的: '+str(not_jpg)+'非JPG文件,请检查！')
    no_xml=[]
    for i in tqdm(img_list,desc="校验标签文件"):
        if os.path.exists(xml_dirs+'/'+os.path.splitext(i)[0]+'.xml'):
            pass
        else:
            no_xml.append(i)
    if len(no_xml)>0:
        return (False,'图片: '+str(no_xml)+'的xml文件未找到,请检查！')
    return (True,'数据校验完成!')

def copy_file_txt(img_dirs,xml_dirs,classes):
    try:
        dirs=os.path.abspath(os.path.dirname(img_dirs))
        img_list=os.listdir(img_dirs)
        if os.path.exists(dirs+'/Train_data'):
            shutil.rmtree(dirs+'/Train_data')
        os.mkdir(dirs+'/Train_data')
        os.mkdir(dirs+'/Train_data/train')
        os.mkdir(dirs+'/Train_data/val')
        os.mkdir(dirs+'/Train_data/test')
        train_list,s=data_split(img_list, ratio=0.8, shuffle=True)
        val_list,test_list=data_split(s, ratio=0.9, shuffle=True)
        print("切分数据: "+str({'总量':len(img_list),'训练集':len(train_list),'验证集':len(val_list),'测试集':len(test_list)}))
        f=open(dirs+'/Train_data/train.txt','w')
        for i in tqdm(train_list,desc="准备训练集数据"):
            xml=xml_dirs+'/'+os.path.splitext(i)[0]+'.xml'
            toxml=dirs+'/Train_data/train/'+os.path.splitext(i)[0]+'.txt'
            convert_annotation(xml,toxml,classes)
            copyfile(img_dirs+'/'+i, dirs+'/Train_data/train/'+i)
            f.write(dirs+'/Train_data/train/'+i+'\n')
        f.close()
        f=open(dirs+'/Train_data/val.txt','w')
        for i in tqdm(val_list,desc="准备验证集数据"):
            xml=xml_dirs+'/'+os.path.splitext(i)[0]+'.xml'
            toxml=dirs+'/Train_data/val/'+os.path.splitext(i)[0]+'.txt'
            convert_annotation(xml,toxml,classes)
            copyfile(img_dirs+'/'+i, dirs+'/Train_data/val/'+i)
            f.write(dirs+'/Train_data/val/'+i+'\n')
        f.close()
        f=open(dirs+'/Train_data/test.txt','w')
        for i in tqdm(test_list,desc="准备测试集数据"):
            copyfile(img_dirs+'/'+i, dirs+'/Train_data/test/'+i)
            f.write(dirs+'/Train_data/test/'+i+'\n')
        f.close()
        return (True,dirs+'/Train_data/train.txt',dirs+'/Train_data/val.txt',dirs+'/Train_data/test')
    except Exception as e:
        traceback.print_exc()
        return (False,str(e))
   
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

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def convert_annotation(xml, txt,classes):
    in_file = open(xml,'r',encoding='utf-8')  # 读取xml
    out_file = open(txt, 'w')  # 保存txt
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)  # 获取类别索引
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str('%.6f' % a) for a in bb]) + '\n')

if __name__ == '__main__':
    img_dirs=r'D:/Users/Go/Desktop/FastestDet-main/datase/mk/images'
    xml_dirs='D:/Users/Go/Desktop/FastestDet-main/datase/mk/xml'
    classes=['Un_Masks','Masks']
    s=manage_data(img_dirs,xml_dirs)
    if s[0]:
        copy_file_txt(img_dirs,xml_dirs,classes)