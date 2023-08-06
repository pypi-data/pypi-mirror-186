

from __future__ import print_function, division

import torch,mxpi_train
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
from torch.autograd import Variable
import torch.backends.cudnn as cudnn
import numpy as np
import torchvision
from torch.utils.tensorboard import SummaryWriter
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os,yaml
import argparse
from tqdm import tqdm
import copy


######################################################################
# Visualize a few images
# ^^^^^^^^^^^^^^^^^^^^^^
# Let's visualize a few training images so as to understand the data
# augmentations.

def imshow(inp, title=None):
    """Imshow for Tensor."""
    inp = inp.numpy().transpose((1, 2, 0))
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    inp = std * inp + mean
    inp = np.clip(inp, 0, 1)
    plt.imshow(inp)
    if title is not None:
        plt.title(title)
    plt.pause(0.001)  # pause a bit so that plots are updated



def train_model(model,dataloaders,dataset_sizes,criterion, optimizer, scheduler, num_epochs):
    since = time.time()

    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0

    for epoch in range(num_epochs):
        print(f'Epoch {epoch}/{num_epochs - 1} ...')
        # Each epoch has a training and validation phase
        for phase in ['train', 'val']:
            if phase == 'train':
                model.train()  # Set model to training mode
            else:
                model.eval()   # Set model to evaluate mode
            running_loss = 0.0
            running_corrects = 0
            datas=tqdm(dataloaders[phase])
            if phase=='train':
                op='Train'
            else:
                op=' Val '
            
            datas.set_description(f'Epoch {epoch}/{num_epochs - 1} '+f'{op} Loss: ------ Acc: ------')
            # Iterate over data.
            acc=''
            loss=''
            for inputs, labels in datas:
                inputs = Variable(inputs.to(device))
                labels = Variable(labels.to(device))
                # zero the parameter gradients
                optimizer.zero_grad()
                # forward
                # track history if only in train
                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)
                    # backward + optimize only if in training phase
                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                # statistics
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)
                epoch_loss = running_loss / dataset_sizes[phase]
                epoch_acc = running_corrects.double() / dataset_sizes[phase]
                if phase=='train':
                    op='Train'
                else:
                    op=' Val '
                datas.set_description(f'Epoch {epoch}/{num_epochs - 1} '+f'{op} Loss: {epoch_loss:.4f} Acc: {epoch_acc:.4f}')
                acc=f'Acc: {epoch_acc:.4f}'
                loss=f'Loss: {epoch_loss:.4f}'

            print(op,loss,acc)
            if phase == 'train':
                writer.add_scalar("Train-ACC",epoch_acc,epoch)
                writer.add_scalar("Train-Loss",epoch_loss,epoch)
            if phase == 'val':
                writer.add_scalar("Val-ACC",epoch_acc,epoch)
                writer.add_scalar("Val-Loss",epoch_acc,epoch)
            if phase == 'train':
                scheduler.step()
            # deep copy the model
            if phase == 'val' and epoch_acc > best_acc:
                print('Epoch Acc > Best Acc save Best model wts...')
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())
            if phase == 'val':
                print('------------------------------------------')

    time_elapsed = time.time() - since
    print(f'Training complete in {time_elapsed // 60:.0f}m {time_elapsed % 60:.0f}s')
    print(f'Best val Acc: {best_acc:4f}')

    # load best model weights
    model.load_state_dict(best_model_wts)
    return model


def main(device,dev,NUM_CLASSES,data_dir,num_epochs,save_url):
    # Get a batch of training data
    cudnn.benchmark = True
    data_transforms = {
        'train': transforms.Compose([
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
        'val': transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
    }
    image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x),
                                            data_transforms[x])
                    for x in ['train', 'val']}
    dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=4,
                                                shuffle=True, num_workers=4)
                for x in ['train', 'val']}
    dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'val']}
    class_names = image_datasets['train'].classes
    model_ft = models.mobilenet_v2(pretrained=True).to(device)
    model_ft.fc = nn.Linear(model_ft.classifier[1].in_features, NUM_CLASSES)
    model_ft = model_ft.to(device)
    criterion = nn.CrossEntropyLoss()
    # Observe that all parameters are being optimized
    optimizer_ft = optim.SGD(model_ft.parameters(), lr=0.001, momentum=0.9)
    # Decay LR by a factor of 0.1 every 7 epochs
    exp_lr_scheduler = lr_scheduler.StepLR(optimizer_ft, step_size=7, gamma=0.1)

    model_ft = train_model(model_ft,dataloaders,dataset_sizes,criterion, optimizer_ft, exp_lr_scheduler,
                        num_epochs=num_epochs)
    #visualize_model(device,model_ft)
    torch.save(model_ft, save_url)
    writer.close()

    conf_matrix = torch.zeros(NUM_CLASSES, NUM_CLASSES)
    # 使用torch.no_grad()可以显著降低测试用例的GPU占用
    with torch.no_grad():
        for step, (imgs, targets) in enumerate(dataloaders['val']):
            # imgs:     torch.Size([50, 3, 200, 200])   torch.FloatTensor
            # targets:  torch.Size([50, 1]),     torch.LongTensor  多了一维，所以我们要把其去掉
            targets = targets.squeeze()  # [50,1] ----->  [50]
            # 将变量转为gpu
            if dev=="cuda":
                targets = targets.cuda()
                imgs = imgs.cuda()
            # print(step,imgs.shape,imgs.type(),targets.shape,targets.type())
            out = model_ft(imgs)
            #记录混淆矩阵参数
            conf_matrix = confusion_matrix(out, targets, conf_matrix)
    conf_matrix=np.array(conf_matrix.cpu())# 将混淆矩阵从gpu转到cpu再转到np
    corrects=conf_matrix.diagonal(offset=0)#抽取对角线的每种分类的识别正确个数
    per_kinds=conf_matrix.sum(axis=1)#抽取每个分类数据总的测试条数

    print(conf_matrix)
    # 获取每种Emotion的识别准确率
    print("每种种类个数：",per_kinds)
    print("每种种类预测正确的个数：",corrects)
    print("每种种类的识别准确率为：{0}".format([rate*100 for rate in corrects/per_kinds]))

    labels = class_names#每种类别的标签
    # 显示数据
    plt.imshow(conf_matrix, cmap=plt.cm.Blues)

    # 在图中标注数量/概率信息
    thresh = conf_matrix.max() / 2	#数值颜色阈值，如果数值超过这个，就颜色加深。
    for x in range(NUM_CLASSES):
        for y in range(NUM_CLASSES):
            # 注意这里的matrix[y, x]不是matrix[x, y]
            info = int(conf_matrix[y, x])
            plt.text(x, y, info,
                    verticalalignment='center',
                    horizontalalignment='center',
                    color="white" if info > thresh else "black")
                    
    plt.tight_layout()#保证图不重叠
    plt.yticks(range(NUM_CLASSES), labels)
    plt.xticks(range(NUM_CLASSES), labels,rotation=45)#X轴字体倾斜45°
    plt.show()
    plt.close()

def confusion_matrix(preds, labels, conf_matrix):
    preds = torch.argmax(preds, 1)
    for p, t in zip(preds, labels):
        conf_matrix[p, t] += 1
    return conf_matrix

if __name__=='__main__':
    writer = SummaryWriter(log_dir=os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/logs',flush_secs=1,max_queue=1)
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', type=str, default="cpu", help='device config')
    parser.add_argument('--yaml', type=str, default="", help='.yaml config')
    parser.add_argument('--save', type=str, default="", help='.save config')
    opt = parser.parse_args()
    with open(opt.yaml, encoding='utf8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    isgpu='cuda' if torch.cuda.is_available() else 'cpu'
    print('启用'+isgpu+"训练！")
    device = torch.device(isgpu)
    main(device,isgpu,data['MODEL']['CLASSNC'],data['DATASET']['CLASS']+'/Train_data',data['TRAIN']['CLASS_EPOCH'],opt.save)

