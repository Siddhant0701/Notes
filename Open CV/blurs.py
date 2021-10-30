import cv2

import numpy as np

img = cv2.imread('Photos/scenery.jpg')
cv2.imshow('Landscape', img)


k = 5

## AVERAGE/BOX BLUR -> Average density of the surrounding pixels based on the kernel 
avg = cv2.blur(img,(k,k))
cv2.imshow('Average', avg)

## GAUSSIAN BLUR -> Average weight of surrounding pixels based on kernel (Bell curved average)
gauss = cv2.GaussianBlur(img, (k,k),0)
cv2.imshow('Gauss', gauss)

## MEDIAN BLUR -> Median weight of surrounding pixels based on kernel
median = cv2.medianBlur(img, k)
cv2.imshow('Median', median)
## NOT MEANT FOR BIGGER KERNELS
## LOOKS SMUDGED OUT

## BILATERAL BLUR -> Used to preserve edges
bil = cv2.bilateralFilter(img, k, 2, 50)
cv2.imshow('Bilateral', bil)

cv2.waitKey(0)
