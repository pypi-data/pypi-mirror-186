import time
import argparse
import torch
import numpy as np
from torchvision import models, transforms
from torch.autograd import Variable
import cv2,yaml,os,mxpi_train
from PIL import Image
from PIL import Image, ImageDraw, ImageFont

def predict(use_cuda,model,image,idx_to_class):
    test_image_tensor = preprocess(image)
    if use_cuda=='cuda':
        test_image_tensor = test_image_tensor.cuda()
    else:
        test_image_tensor = test_image_tensor
    test_image_tensor = Variable(torch.unsqueeze(test_image_tensor, dim=0).float(), requires_grad=False)
    with torch.no_grad():
        model.eval()
        out = model(test_image_tensor)
        ps = torch.exp(out) 
        ps = ps / torch.sum(ps)
        topk, topclass = ps.topk(1, dim=1)
        return(idx_to_class[topclass.cpu().numpy()[0][0]], topk.cpu().numpy()[0][0])


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', type=str, default="cpu", help='device config')
    parser.add_argument('--model', type=str, default="", help='model config')
    parser.add_argument('--yaml', type=str, default="", help='.yaml config')
    opt = parser.parse_args()
    with open(opt.yaml, encoding='utf8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    isgpu='cuda' if torch.cuda.is_available() else 'cpu'
    device = torch.device(isgpu)
    net=torch.load(opt.model).to(device)
    classes=data['DATASET']['CLASSNAME'].split(',')
    preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    print('开始测试模型')
    with torch.no_grad():
        print('---------------------------')
        test=data['DATASET']['CLASS']+'/Train_data/test'
        imgs=os.listdir(test)
        for img in imgs:
            image = cv2.imread(test+'/'+img)
            img_pil=Image.open(test+'/'+img) 
            img_pils = ImageDraw.Draw(img_pil)
            image = image[:, :, [2, 1, 0]]
            permuted = image
            label, score = predict(isgpu,net, image,classes)
            img_pils.rectangle([0,img_pil.height-30,img_pil.width,img_pil.height],'#00AB84',outline='#00AB84')
            img_pils.text(((img_pil.width/2)-len(label)/2*20,img_pil.height-30), text=label+'   %.2f' % score, fill="#fff", font=ImageFont.truetype(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/configs/9121.ttf',20),align='center')
            img_pil.save(os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/ModelNet/result/'+img, quality=95)
            print('Name:'+img+f'(W:%.0f,H:%.0f)'%(img_pil.width,img_pil.height) , ' Label:'+label,'  Score:'+str(score))
        print('---------------------------')
