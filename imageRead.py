import cv2

image_path = "../assets/yunus.jpg"
image = cv2.imread(image_path)
cv2.imshow("Image Yunus", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
