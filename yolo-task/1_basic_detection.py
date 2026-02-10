from ultralytics import YOLO
import cv2

img = cv2.imread("test-images/img_1.jpg")
if img is None:
    print("Error: Could not read image.")

model = YOLO("yolov8n.pt")

result = model("test-images/img_1.jpg")
result_img = result[0].plot()

cv2.imshow("image", result_img)
cv2.waitKey(5000)

cv2.imwrite("detection-results/basic_image.jpg", img)
print("Detection complete!")
