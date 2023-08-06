<div align="center">
<h2>
  Yolor-Pip: Packaged version of the Yolor repository  
</h2>
<h4>
    <img width="800" alt="teaser" src="doc/figure.png">
</h4>
<div>
    <a href="https://pepy.tech/project/yolor"><img src="https://pepy.tech/badge/yolor" alt="downloads"></a>
    <a href="https://badge.fury.io/py/yolor"><img src="https://badge.fury.io/py/yolor.svg" alt="pypi version"></a>
</div>
</div>

## <div align="center">Overview</div>

This repo is a packaged version of the [Yolor](https://github.com/WongKinYiu/yolor) model.
## Benchmark
| Model | Test Size | AP<sup>test</sup> | AP<sub>50</sub><sup>test</sup> | AP<sub>75</sub><sup>test</sup> | batch1 throughput | batch32 inference |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: |
| **YOLOR-CSP** | 640 | **52.8%** | **71.2%** | **57.6%** | 106 *fps* | 3.2 *ms* |
| **YOLOR-CSP-X** | 640 | **54.8%** | **73.1%** | **59.7%** | 87 *fps* | 5.5 *ms* |
| **YOLOR-P6** | 1280 | **55.7%** | **73.3%** | **61.0%** | 76 *fps* | 8.3 *ms* |
| **YOLOR-W6** | 1280 | **56.9%** | **74.4%** | **62.2%** | 66 *fps* | 10.7 *ms* |
| **YOLOR-E6** | 1280 | **57.6%** | **75.2%** | **63.0%** | 45 *fps* | 17.1 *ms* |
| **YOLOR-D6** | 1280 | **58.2%** | **75.8%** | **63.8%** | 34 *fps* | 21.8 *ms* |
|  |  |  |  |  |  |  |
| **YOLOv4-P5** | 896 | **51.8%** | **70.3%** | **56.6%** | 41 *fps* (old) | - |
| **YOLOv4-P6** | 1280 | **54.5%** | **72.6%** | **59.8%** | 30 *fps* (old) | - |
| **YOLOv4-P7** | 1536 | **55.5%** | **73.4%** | **60.8%** | 16 *fps* (old) | - |
|  |  |  |  |  |  |  |
### Installation
```
pip install yolor
```

### Yolov6 Inference
```python
from yolor.helpers import Yolor

model = Yolor(cfg='yolor/cfg/yolor_p6.cfg', weights='yolor/yolor_p6.pt', imgsz=640, device='cuda:0')

model.classes = None
model.conf = 0.25
model.iou_ = 0.45
model.show = False
model.save = True

model.predict('yolor/data/highway.jpg')
```
### Citation
```bibtex
@article{wang2021you,
  title={You Only Learn One Representation: Unified Network for Multiple Tasks},
  author={Wang, Chien-Yao and Yeh, I-Hau and Liao, Hong-Yuan Mark},
  journal={arXiv preprint arXiv:2105.04206},
  year={2021}
}
```
