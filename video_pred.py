from ultralytics import YOLO
model = YOLO("yolov8n-seg.pt")
model.predict(source="cars_road_traffic_driving_lanes_442.mp4",save=False,show=True,conf=0.5)