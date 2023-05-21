from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('yolov8n.pt')
    model.train(data='coco128.yaml', epochs=100, imgsz=640, workers=0)