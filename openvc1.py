import cv2

import random

sizes = [(80,80),(160,160),(320,320)]
pick = random.choice(sizes)

image = cv2.imread("dog.jpg")

resize = cv2.resize(image,pick)
cv2.namedWindow("dog.jpg",cv2.WINDOW_NORMAL)
cv2.resizeWindow("dog.jpg",80 ,80)
cv2.imshow("dog.jpg",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Original Dimensions:",image.shape)
print("New dimensions:",resize.shape)