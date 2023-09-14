from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
model.train(data="coonfig.yaml", epochs=3)  # train the model

#terminal yolo detect train data=coonfig.yaml model="yolov8n.yaml" epochs=3 yazmak da aynı işlemi gerçekleştirir