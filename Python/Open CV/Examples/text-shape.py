import cv2 as cv

img = cv.imread('../Photos/dog.jpg')
cv.rectangle(img, (100,0),(200,100), (0,255,0), thickness= 1)
cv.putText(img, 'Dog', (150,120) ,cv.FONT_HERSHEY_TRIPLEX, 0.75, (0,255,0), thickness=1)
cv.imshow('shape',img)

cv.waitKey(0)
