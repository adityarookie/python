import cv2
image = cv2.imread("dog.jpg")

cv2.namedWindow("dog.jpg",cv2.WINDOW_NORMAL)
cv2.resizeWindow("dog.jpg",80 ,80)
cv2.imshow("dog.jpg",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Image Dimension:",image.shape)
