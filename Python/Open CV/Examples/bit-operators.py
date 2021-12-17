import cv2
import numpy as np

blank = np.zeros((400, 400), dtype = "uint8")
cv2.imshow('Blank',blank)

rectangle = cv2.rectangle(blank.copy(),(50,50), (350,350), 255, thickness= -1)
cv2.imshow('Rect', rectangle)

circle = cv2.circle(blank.copy(), (200,200), 175, 255, thickness=-1)
cv2.imshow('Circle', circle)

## AND OPERATOR -> Intersecting regions
and_op = cv2.bitwise_and(circle,rectangle)
cv2.imshow('And', and_op)

## OR OPERATOR -> Combined regions
or_op = cv2.bitwise_or(circle,rectangle)
cv2.imshow('Or', or_op)

## XOR OPERATOR -> Exclusive regions
xor_op = cv2.bitwise_xor(circle,rectangle)
cv2.imshow('Xor', xor_op)

## NOT OPERATOR -> Reversed region
not_op =  cv2.bitwise_not(circle)
cv2.imshow('Not',not_op)

cv2.waitKey(0)
