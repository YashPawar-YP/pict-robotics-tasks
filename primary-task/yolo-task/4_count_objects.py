from ultralytics import YOLO
from collections import Counter
import cv2

img = cv2.imread("test-images/img_3.jpg")
if img is None:
    print("Error: Could not read image.")

model = YOLO("yolov8n.pt")
results = model("test-images/img_3.jpg")

detected_objects = []
for result in results:
    boxes = result.boxes
    for box in boxes:
        class_id = int(box.cls[0])
        class_name = result.names[class_id]
        detected_objects.append(class_name)

object_counts = Counter(detected_objects)


print("-" * 30)
for obj, count in object_counts.items():
    print(f"{obj}: {count}")
print("-" * 30)
print("Object Detection Summary:")
print(f"Total objects detected: {len(detected_objects)}")

cv2.imshow("Image", results[0].plot())
cv2.waitKey(5000)

cv2.imwrite(f"detection-results/counted_objects.jpg", results[0].plot())