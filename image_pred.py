'''Creating anaconda environment
>>conda create -n yolov8 python=3.9

Activating environment
>>conda activate yolov8

Install ultralytics
>>pip install ultralytics
'''

from ultralytics import YOLO
model = YOLO("yolov8n-seg.pt")
model.predict(source="car.jpg",save=True,conf=0.5)