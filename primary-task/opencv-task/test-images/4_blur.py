import cv2

img = cv2.imread("test-images/image.jpg")
blur = cv2.GaussianBlur(img, (15, 15), sigmaX = 0)

cv2.imshow("original_image", img)
cv2.waitKey(5000)
cv2.imshow("blurred_image", blur)
cv2.waitKey(5000)
cv2.destroyAllWindows()

cv2.imwrite("output-images/blur_image.jpg", blur)
print("Blur applied.Image saved to output-images.")