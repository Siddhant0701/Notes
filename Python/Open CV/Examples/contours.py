import cv2

img = cv2.imread('../Photos/monke.jpg')
cv2.imshow('Bird', img)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray', gray)

canny = cv2.Canny(gray, 125,175)
cv2.imshow('Canny', canny)

contours, heirarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

## LIST -> ALL
## TREE -> HEIRARCHIAL
## EXTERNAL -> OUTSIDE

##CHAIN_APPROX_NONE -> ALL
##CHAIN_APPROX_SIMPLE -> ENDPOINTS


## Canny -> Contours
## Threshold -> Contours

## Can count contours using len
## threshold to binarize images
# ret, thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)

cv2.waitKey(0)
