import cv2

img = cv2.imread('../Photos/tree.jpg')
cv2.imshow('Original', img)

## Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray', gray)

## Blur
blur = cv2.GaussianBlur(img, (7,7) , cv2.BORDER_DEFAULT)
#cv2.imshow('Blur', blur)

## Edge Cascading
canny = cv2.Canny(img, 125, 125)
cv2.imshow('Edge Cascade', canny)

## Dilation
dilate = cv2.dilate(canny, (3,3), iterations = 3)
cv2.imshow('Dilation', dilate)

## Eroding
erode = cv2.erode(dilate, (3,3), iterations = 3)

## Resizing
resized = cv2.resize(img, (500,500), interpolation = cv2.INTER_CUBIC)

## Crop
cropped = img[50:200,150:160]
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)
