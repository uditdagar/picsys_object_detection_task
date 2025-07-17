import torch
from yolov5 import train, detect

model =torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

result = model('sample.jpg')
result.print()
result.show()