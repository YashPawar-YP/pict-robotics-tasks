from ultralytics import YOLO
import cv2

img = cv2.imread("test-images/img_2.jpg")
if img is None:
    print("Error: Could not read image.")

model = YOLO("yolov8n.pt")
results = model("test-images/img_2.jpg", conf = 0.7)

for result in results:
    boxes = result.boxes
    for box in boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        class_name = result.names[class_id]
        
        print(f"Detected: {class_name} with {confidence: .2%} confidence")

cv2.imwrite("detection-results/confidence_detected_img.jpg", results[0].plot())