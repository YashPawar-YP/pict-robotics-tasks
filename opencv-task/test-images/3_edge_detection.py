import cv2

img = cv2.imread("test-images/image.jpg")
if img is None:
    print("Error: Could not read image.")

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edge_detected_img = cv2.Canny(grayscale_img, 100, 200)

cv2.imshow("original_image", img)
cv2.waitKey(5000)
cv2.imshow("edge_detected_image", edge_detected_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

cv2.imwrite("output-images/edge_detected_image.jpg", edge_detected_img)
print("Edge detection complete.Image saved to output-images.")