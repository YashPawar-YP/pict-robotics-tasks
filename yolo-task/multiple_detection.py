from ultralytics import YOLO
import os
import cv2

for i in range(3):
    img = cv2.imread(f"test-images/img_{i + 1}.jpg")
    if img is None:
        print(f"Error: Could not read {i + 1} image.")

model = YOLO("yolov8n.pt")

image_folder = "test-images"
images = [os.path.join(image_folder, file) for file in os.listdir(image_folder) 
          if file.lower().endswith((".jpg", ".png", ".jpeg"))]
print(f"Processing {len(images)} images...")

for img_path in images:
    results = model(img_path)
    img_name = os.path.basename(img_path)
    
    cv2.imwrite(f"detection-results/{img_name}.jpg", img)
    print(f"Processed: {img_name}")

print("All images processed!")