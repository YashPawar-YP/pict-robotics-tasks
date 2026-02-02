import cv2

img = cv2.imread("test-images/image.jpg")
if img is None:
    print("Error: Could not read image.")

height, width = img.shape[:2]

cv2.rectangle(img, (50, 50), (200, 150), (0, 255, 0), 3)

center = (width//2, height//2)
cv2.circle(img, center, 50, (255, 0, 0), -1)

cv2.line(img, (0, 0), (width, height), (0, 0, 255), 2)

cv2.putText(img, "OpenCV Test", (50, height-50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imshow("shapes_image", img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

cv2.imwrite("output-images/shapes_drawn_image.jpg", img)
print("Shapes drawn. Image saved to output-images.")