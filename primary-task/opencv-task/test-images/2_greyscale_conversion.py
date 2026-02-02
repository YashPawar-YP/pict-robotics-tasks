import cv2

img = cv2.imread("test-images/image.jpg")
if img is None:
    print("Error: Could not read image.")

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("original_image", img)
cv2.waitKey(5000)
cv2.imshow("grayscale_image", grayscale_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

cv2.imwrite("output-images/grayscale_image.jpg", grayscale_img)
print("Grayscale image saved to output-images.")