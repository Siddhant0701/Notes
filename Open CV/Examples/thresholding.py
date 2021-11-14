import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Photos/cat.jpg')
cv2.imshow('Cats', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# Simple Thresholding - Basically give a number, any pixel values above become black and rest are white
threshold, thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold Simple', thresh)

# Inverse of Simple. white and black are swapped
threshold, thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Threshold Simple Inverse', thresh)

# Adaptive Thresholding
adaptive_thresh = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV ,3, 5)
cv2.imshow('Adaptive', adaptive_thresh)

cv2.waitKey(0)
