from yolor.models.models import Darknet
import torch
from yolor.utils.datasets import LoadStreams, LoadImages
from yolor.utils.general import non_max_suppression, scale_coords
from yolor.utils.plots import plot_one_box
import torch.backends.cudnn as cudnn
import random
from yolor.detect import load_classes
import cv2


class Yolor:
    def __init__(
        self, 
        cfg: str = 'yolor/cfg/yolor_p6.cfg',
        weights: str = 'yolor/yolor_p6.pt',
        imgsz: int = 640,
        half : bool = False,
        device: str = 'cuda:0'
    ):
        self.cfg = cfg
        self.weights = weights
        self.imgsz = imgsz
        self.half = half
        self.webcam = False
        self.conf = 0.25
        self.iou = 0.45
        self.classes = None
        self.class_name = 'yolor/data/coco.names'
        self.save = True
        self.show = False
        self.save_path = 'yolor/data/output.jpg'
        
        self.device = torch.device(device)
        self.model = self.load_model()
        
        
    def load_model(self):
        model = Darknet(self.cfg, self.imgsz).cuda()
        model.load_state_dict(torch.load(self.weights, map_location=self.device)['model'])
        model.to(self.device).eval()
        if self.half:
            model.half()  # to FP16
            
        return model
    
    
    def predict(self, source):
        if self.webcam:
            cudnn.benchmark = True  # set True to speed up constant image size inference
            dataset = LoadStreams(source, img_size=self.imgsz)
        else:
            save_img = True
            dataset = LoadImages(source, img_size=self.imgsz, auto_size=64)

        # Get names and colors
        names = load_classes(self.class_name)
        colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(names))]

        # Run inference
        img = torch.zeros((1, 3, self.imgsz, self.imgsz), device=self.device)  # init img
        for path, img, im0s, vid_cap in dataset:
            img = torch.from_numpy(img).to(self.device)
            img = img.half() if self.half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)

            # Inference
            pred = self.model(img, augment=False)[0]

            # Apply NMS
            pred = non_max_suppression(pred, self.conf, self.iou, classes=self.classes, agnostic=False)
            for i, det in enumerate(pred):  # detections per image
                if self.webcam:  # batch_size >= 1
                    p, s, im0 = path[i], '%g: ' % i, im0s[i].copy()
                else:
                    p, s, im0 = path, '', im0s

                s += '%gx%g ' % img.shape[2:]  # print string
                gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
                if det is not None and len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                    # Print results
                    for c in det[:, -1].unique():
                        n = (det[:, -1] == c).sum()  # detections per class
                        s += '%g %ss, ' % (n, names[int(c)])  # add to string

                    # Write results
                    for *xyxy, conf, cls in det:
                        if self.save or self.show:  # Add bbox to image
                            label = '%s %.2f' % (names[int(cls)], conf)
                            plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=3)
                            

                # Stream results
                if self.show:
                    cv2.imshow(p, im0)
                    if cv2.waitKey(1) == ord('q'):  # q to quit
                        raise StopIteration

                # Save results (image with detections)
                if save_img:
                    if dataset.mode == 'images':  
                        cv2.imwrite(self.save_path, im0)       
        
        return self.save_path

if __name__ == '__main__':
    yolor = Yolor(cfg='yolor/cfg/yolor_p6.cfg', weights='yolor/yolor_p6.pt', imgsz=640, device='cuda:0')
    yolor.predict('yolor/data/highway.jpg')
