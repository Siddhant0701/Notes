import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Photos/monke.jpg')
cv2.imshow('Monke',img)

plt.imshow(img) ## MAKES RGB

## BGR TO RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)

## BGR to GRAY
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

## BGR TO HSV (Hue Saturation Level)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

## BGR TO LAB 
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB', lab)


## USE BGR AS INTERMEDIATE FOR ALL SWITCHES

plt.show()
cv2.waitKey(0)
