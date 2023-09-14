from ultralytics import YOLO

infer = YOLO("./runs/detect/train2/weights/best.pt")
infer.predict("./f82ec8e3c419a16778da6c7bcc119fc0.jpg",save=True,save_txt=True)