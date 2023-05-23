from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('../runs/detect/train10/weights/best.pt')
    results = model('../data/detect/2.jpg')
    for result in results:
        print(result)