import cv2
import numpy as np

img = cv2.imread('Photos/dog.jpg')
cv2.imshow('Dog',img)



##Translate
def translate(img,x,y):
    translateMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, translateMat, dimensions)

## x -> Right
## -x -> Left
## y -> Down
## -y -> Up

translated = translate(img, 10,15)
cv2.imshow('Translate',  translated)


##Rotate
def rotate (img, angle, center = None):
    (height,width) = img.shape[:2]

    if center is None:
        center = (width//2, height//2)
    
    matrix = cv2.getRotationMatrix2D(center, angle,1.0)
    dimensions = (width, height)
    return cv2.warpAffine(img, matrix, dimensions)
    
rotated = rotate(img, 60)
cv2.imshow('Rotated', rotated)



##Resize
resized = cv2.resize(img, (img.shape[1]*2,img.shape[0]*2), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized)


##Flip
flipped = cv2.flip(img,0)
cv2.imshow('Flip', flipped)

# 0 -> vertical
# 1 -> horizontal
# -1 -> both


##Crop
cropped = img[20:30, :]
cv2.imshow('Crop', cropped)

cv2.waitKey(0)
