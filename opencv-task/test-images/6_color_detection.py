import cv2
import numpy as np

img = cv2.imread("test-images/image.jpg")
if img is None:
    print("Error: Could not read image.")

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

mask_img = cv2.inRange(hsv_img, lower_blue, upper_blue)
result_img = cv2.bitwise_and(img, img, mask=mask_img)

cv2.imshow("original_image", img)
cv2.waitKey(5000)
cv2.imshow("hsv_img", hsv_img)
cv2.waitKey(5000)
cv2.imshow("masked_image", mask_img)
cv2.waitKey(5000)
cv2.imshow("color_detected_image", result_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

cv2.imwrite("output-images/masked_image.jpg", mask_img)
cv2.imwrite("output-images/masked_result_image.jpg", result_img)
print("Color detection complete. Image saved to output-images.")
