import cv2

img = cv2.imread("test-images/image.jpg")

if img is None:
    print("Error: Could not read image.")
else:
    print(f"Image shape: {img.shape}.")
    cv2.imshow("original_image", img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    
    cv2.imwrite("output-images/original_image.jpg", img)
    print("Image saved to output-images.")