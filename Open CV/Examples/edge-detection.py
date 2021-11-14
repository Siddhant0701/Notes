import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Photos/cat.jpg')
cv2.imshow('cats', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# Laplacian
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('Lap', lap)

# Sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F,1,0)
sobely = cv2.Sobel(gray, cv2.CV_64F,0,1)
combined = cv2.bitwise_or(sobelx, sobely)

cv2.imshow('Sobelx', sobelx)
cv2.imshow('Sobely', sobely)
cv2.imshow('Combined', combined)


# Canny
canny = cv2.Canny(gray, 150,175)
cv2.imshow('Canny', canny)

# Canny is multi step process, uses sobel as one of the steps

cv2.waitKey(0)
