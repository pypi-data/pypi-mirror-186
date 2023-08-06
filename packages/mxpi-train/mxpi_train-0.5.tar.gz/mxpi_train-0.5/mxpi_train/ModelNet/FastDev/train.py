import os,time
import math,mxpi_train
import torch
import argparse
from tqdm import tqdm
from torch import optim
from torchsummary import summary
import onnx
from onnxsim import simplify
from utils.tool import *
from utils.datasets import *
from utils.evaluation import CocoDetectionEvaluator
from torch.utils.tensorboard import SummaryWriter
from module.loss import DetectorLoss
from module.detector import Detector
import subprocess

writer = SummaryWriter(log_dir=os.path.dirname(mxpi_train.__file__).replace('\\','/')+'/logs',flush_secs=1,max_queue=1)
class FastestDet:
    def __init__(self,opt,device):
        # 指定训练配置文件
        assert os.path.exists(opt.yaml), "请指定正确的配置文件路径"
        # 解析yaml配置文件
        self.cfg = LoadYaml(opt.yaml)
        #print(self.cfg)
        # 初始化模型结构
        if opt.weight is not None:
            print("load weight from:%s"%opt.weight)
            self.model = Detector(self.cfg.category_num, True).to(device)
            self.model.load_state_dict(torch.load(opt.weight))
        else:
            self.model = Detector(self.cfg.category_num, False).to(device)

        # # 打印网络各层的张量维度
        summary(self.model, input_size=(3, self.cfg.input_height, self.cfg.input_width))

        #构建优化器
        print("use SGD optimizer")
        self.optimizer = optim.SGD(params=self.model.parameters(),
                                   lr=self.cfg.learn_rate,
                                   momentum=0.949,
                                   weight_decay=0.0005,
                                   )
        # 学习率衰减策略
        self.scheduler = optim.lr_scheduler.MultiStepLR(self.optimizer,
                                                        milestones=self.cfg.milestones,
                                                        gamma=0.1)

        # 定义损失函数
        self.loss_function = DetectorLoss(device)
        
        # 定义验证函数
        self.evaluation = CocoDetectionEvaluator(self.cfg.names, device)

        # 数据集加载
        val_dataset = TensorDataset(self.cfg.val_txt, self.cfg.input_width, self.cfg.input_height, False)
        train_dataset = TensorDataset(self.cfg.train_txt, self.cfg.input_width, self.cfg.input_height, True)

        #验证集
        self.val_dataloader = torch.utils.data.DataLoader(val_dataset,
                                                          batch_size=self.cfg.batch_size,
                                                          shuffle=False,
                                                          collate_fn=collate_fn,
                                                          num_workers=4,
                                                          drop_last=False,
                                                          persistent_workers=True
                                                          )
        # 训练集
        self.train_dataloader = torch.utils.data.DataLoader(train_dataset,
                                                            batch_size=self.cfg.batch_size,
                                                            shuffle=True,
                                                            collate_fn=collate_fn,
                                                            num_workers=4,
                                                            drop_last=True,
                                                            persistent_workers=True
                                                            )

    def train(self,save):
        # 迭代训练
        batch_num = 0
        print('Starting training for %g epochs...' % self.cfg.end_epoch)
        for epoch in range(self.cfg.end_epoch + 1):
            #if epoch==10:
                #res = subprocess.Popen(cmd)
            print('---Epoch:'+str(epoch)+'/'+str(self.cfg.end_epoch))
            self.model.train()
            pbar = tqdm(self.train_dataloader)
            for imgs, targets in pbar:
                # 数据预处理
                imgs = imgs.to(device).float() / 255.0
                targets = targets.to(device)
                # 模型推理
                preds = self.model(imgs)
                # loss计算
                iou, obj, cls, total = self.loss_function(preds, targets)
                # 反向传播求解梯度
                total.backward()
                # 更新模型参数
                self.optimizer.step()
                self.optimizer.zero_grad()

                # 学习率预热
                for g in self.optimizer.param_groups:
                    warmup_num =  5 * len(self.train_dataloader)
                    if batch_num <= warmup_num:
                        scale = math.pow(batch_num/warmup_num, 4)
                        g['lr'] = self.cfg.learn_rate * scale
                    lr = g["lr"]

                # 打印相关训练信息
                info = "Epoch:%d LR:%f IOU:%f Obj:%f Cls:%f Total:%f" % (
                        epoch, lr, iou, obj, cls, total)
                pbar.set_description(info)
                batch_num += 1
            mAP05 = self.evaluation.compute_map(self.val_dataloader, self.model)
            info = "Epoch:%d LR:%f IOU:%f Obj:%f Cls:%f AP:%f Loss:%f" % (
                        epoch, lr, iou, obj, cls, mAP05 ,total)
            writer.add_scalar("Train-AP",mAP05,epoch)
            writer.add_scalar("Train-Loss",total,epoch)
            writer.add_scalar("Train-IOU-Loss",iou,epoch)
            writer.add_scalar("Train-Obj-Loss",obj,epoch)
            writer.add_scalar("Train-Cls-Loss",cls,epoch)
            print(info)

            # 模型验证及保存
            if epoch % 10 == 0 and epoch > 0:
                # 模型评估
                self.model.eval()
                print("computer mAP...")
                mAP05 = self.evaluation.compute_map(self.val_dataloader, self.model)
                torch.save(self.model.state_dict(), save+"/weight_AP05_%f_%d-epoch.pth"%(mAP05, epoch))
                savepth=save+"/weight_AP05_%f_%d-epoch.pth"%(mAP05, epoch)
                save_onnx=save+"/weight_AP05_%f_%d-epoch.onnx"%(mAP05, epoch)
                self.to_onnx(savepth,save_onnx)
            if epoch==self.cfg.end_epoch:
                # 模型评估
                writer.close()
                self.model.eval()
                print("computer mAP...")
                mAP05 = self.evaluation.compute_map(self.val_dataloader, self.model)
                torch.save(self.model.state_dict(), save+"/weight_AP05_%f_%d-epoch.pth"%(mAP05, epoch))
                savepth=save+"/weight_AP05_%f_%d-epoch.pth"%(mAP05, epoch)
                save_onnx=save+"/weight_AP05_%f_%d-epoch.onnx"%(mAP05, epoch)
                self.to_onnx(savepth,save_onnx)
            # 学习率调整
            self.scheduler.step()

    def to_onnx(self,savepth,saveonnx):
        # 模型加载
        print("load weight from:%s"%savepth)
        model = Detector(self.cfg.category_num, True).to(device)
        model.load_state_dict(torch.load(savepth, map_location=device))
        #sets the module in eval node
        model.eval()
        
        # 数据预处理
        img_url=self.cfg.test+'/'+os.listdir(self.cfg.test)[0]
        ori_img = cv2.imread(img_url)
        res_img = cv2.resize(ori_img, (self.cfg.input_width, self.cfg.input_height), interpolation = cv2.INTER_LINEAR) 
        img = res_img.reshape(1, self.cfg.input_height, self.cfg.input_width, 3)
        img = torch.from_numpy(img.transpose(0, 3, 1, 2))
        img = img.to(device).float() / 255.0

        # 导出onnx模型
        torch.onnx.export(model,                     # model being run
                        img,                       # model input (or a tuple for multiple inputs)
                        saveonnx,       # where to save the model (can be a file or file-like object)
                        export_params=True,        # store the trained parameter weights inside the model file
                        opset_version=11,          # the ONNX version to export the model to
                        do_constant_folding=True)  # whether to execute constant folding for optimization
        # onnx-sim
        onnx_model = onnx.load(saveonnx)  # load onnx model
        model_simp, check = simplify(onnx_model)
        assert check, "Simplified ONNX model could not be validated"
        print("onnx sim sucess...")
        onnx.save(model_simp, saveonnx)  
        
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', type=str, default="cpu", help='device config')
    parser.add_argument('--yaml', type=str, default="", help='.yaml config')
    parser.add_argument('--save', type=str, default="", help='.save config')
    parser.add_argument('--weight', type=str, default=None, help='.weight config')
    opt = parser.parse_args()
    isgpu='cuda' if torch.cuda.is_available() else 'cpu'
    print('启用'+isgpu+"训练！")
    device = torch.device(isgpu)
    model = FastestDet(opt,device)
    model.train(opt.save)