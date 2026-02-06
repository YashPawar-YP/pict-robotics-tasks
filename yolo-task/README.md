YOLO (You Only Look Once) object detection task

1.Overview:-
YOLO (You Only Look Once) is an object detection algorithm that can detect multiple objects with their confidence score in real time. It tells us what objects are present and where they are located. I have used a trained model named "yolov8n" to do image processing, object detection and classification tasks.

2.Setup:- 
pip install ultralytics

3.Detection vs Classification:-
Object detection is the process of identifying, locating, and classifying objects in an image using bounding boxes. Image classification assigns a label to the entire image based on the object that appears with the highest probability.

* Classification:-
Classification answers “What is in this image?”. When the model reads image, it gives that image one label (which has highest probablity), no boxes are drawn, doesn't know where the object is.

* Detection:-
Detection answers “What objects are in this image and where are they?”. It helps to find multiple objects, draw bounding boxes and assigns class and confidence score to each box.

4.Scripts:-

i.Basic Detection (1_basic_detection.py)
- Import YOLO from ultralytics.
- Check if image is readable using OpenCV.
- Loads a trained model "yolov8n" in PyTorch format.
- Model reads the image, processes it and predicts bounding boxes and object class.
- The processed image is displayed.
- The processed image is saved in "detection-results".

ii.Multiple Image Detection (2_multiple_detection.py)
- Import YOLO from ultralytics.
- Check if image is readable using OpenCV.
- Loads a trained model "yolov8n" in PyTorch format.
- Model reads the multiple images, processes it and predicts bounding boxes and object class.
- The processed images are displayed.
- The processed images are saved in "detection-results".

* Use case:-
- Detect people, animals, vehicles.
- Choose target based on class.

iii.Custom Confidence Threshold (3_custom_confidence.py)
- Import YOLO from ultralytics.
- Check if image is readable using OpenCV.
- Loads a trained model "yolov8n" in PyTorch format.
- Model reads the image, processes it and predicts bounding boxes and object class.
- Shows only bounding boxes which have confidence score >= 70 % and hides other.
- The processed image is displayed.
- The processed image is saved in "detection-results".

* Why useful:-
Using custom confidence threshold in YOLO it allows to filter out low probablity predictions to meet the specific needs of particular application. It helps in balancing precision, improving performance in difficult situations, reduces false positives, etc.

iv.Object Counting (4_count_objects.py)
- Import YOLO from ultralytics.
- Check if image is readable using OpenCV.
- Loads a trained model "yolov8n" in PyTorch format.
- Model reads the image, processes it and predicts bounding boxes and object class.
- The detected object classes are stored in a list.
- Import Counter from collections and uses Counter function to count and classify objects and stores it in a dictionary.
- The processed image is displayed.
- The processed image is saved in "detection-results".

* Robotics use:-
Robots need to use object counting to gain quantitative understanding of their environment in real time. It helps robots to manage inventory systems, traffic analysis, autonomouos navigation, etc.

* Why Robots Use YOLO:- 
Robots use YOLO because it offers optimal balance between speed and accuracy in real-time computer vision tasks. Unlike, slow detection methods that require multiple passes over an image, YOLO processes the entire image in a single pass, enabling robots to detect, classify, and track objects instantaneously.
Here are some robotics application of YOLO:
- Autonomous Navigation.
- Drones (Landing pad detection and alignment).

5. Output:-
All detection results are saved in "detection-results" directory.

**Key Learnings:**
    YOLO performs real-time object detection by processing the entire image in a single pass and predicting bounding boxes with confidence scores. Object detection differs from classification by identifying multiple objects and their locations rather than assigning one label to an image. Tuning confidence thresholds and using batch detection helps reduce false positives and handle larger datasets effectively. Because of its speed and reasonable accuracy, YOLO is widely used in robotics applications such as navigation, object counting, and drone vision.