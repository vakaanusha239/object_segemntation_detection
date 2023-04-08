# object_segmentation_detection
It is a project to detect and segment objects in images &amp; videos

Object classification:
Classification is a machine learning task for determining which objects are in an image or video. It refers to training machine learning models with the intent of finding out which classes (objects) are present. Classification is useful at the yes-no level of deciding whether an image contains an object/anomaly or not.Classification refers to a type of labeling where an image/video is assigned certain concepts, with the goal of answering the question, “What is in this image/video?”
![image](https://user-images.githubusercontent.com/105503752/230726314-b74c9255-0b94-44bb-8a9d-c9077059312c.png)
Input image
![image](https://user-images.githubusercontent.com/105503752/230726328-a1b7a588-29e3-4528-9d67-7c31df539c64.png)
Output image

Image Segmentatiion:
Any image consists of both useful and useless information, depending on the user’s interest. Image segmentation separates an image into regions, each with its particular shape and border, delineating potentially meaningful areas for further processing, like classification and object detection. The regions may not take up the entire image, but the goal of image segmentation is to highlight foreground elements and make it easier to evaluate them. Image segmentation provides pixel-by-pixel details of an object, making it different from classification and object detection.

Below, the image on the left illustrates object detection, highlighting only the location of the objects. The image on the right illustrates image segmentation, showing pixel-by-pixel outlines of the objects.
![image](https://user-images.githubusercontent.com/105503752/230726277-80e6dd4a-6938-454f-9b46-563d7d093a6d.png)
Input image
![image](https://user-images.githubusercontent.com/105503752/230726287-818cd770-5878-486f-bd99-b781ee71d881.png)
Output image

To do such operations in an image or video I used a pre- trained model named as YOLOV8 (You Only Look Once)

YOLOV8:
Ultralytics YOLOv8, the latest version of the acclaimed real-time object detection and image segmentation model. YOLOv8 is built on cutting-edge advancements in deep learning and computer vision, offering unparalleled performance in terms of speed and accuracy. Its streamlined design makes it suitable for various applications and easily adaptable to different hardware platforms, from edge devices to cloud APIs.

 In this repository the file named image_pred.py consists the code for segmenting the images, video_pred.py consists the code for segementing the objects in a video.
