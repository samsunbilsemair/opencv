import cv2

image_path = "../assets/yunus.jpg"
image = cv2.imread(image_path)

new_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY IMAGE", new_image)

cv2.imwrite("../assets/grayYunus.jpg", new_image)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()


