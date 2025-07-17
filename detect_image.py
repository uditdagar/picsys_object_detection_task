from ultralytics import YOLO

model = YOLO('yolov5n.pt')

results= model('image.jpg')
results[0].show()