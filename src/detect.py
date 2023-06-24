from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('../runs/detect/train12/weights/best.pt')
    results = model.predict(source='../data/detect', save_conf=True)
    for result in results:
        print(result)