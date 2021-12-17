import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Photos/scenery.jpg')
cv2.imshow('Landscape', img)



##GRAYSCALE
blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grayscale', gray)

circle = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2),50,255,-1)
cv2.imshow('Mask', circle)


masked = cv2.bitwise_and(img,img,mask=circle)
cv2.imshow('Masked', masked)
# gray_hist = cv2.calcHist([gray],[0], circle, [256], [0,256])

# plt.figure()
# plt.title('GrayScale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of Pixels')
# plt.plot(gray_hist)
# plt.xlim(0,256)
# plt.show()


##COLOR

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
colors = ('b','g','r')
for i, col in enumerate(colors):
    hist = cv2.calcHist([img],[i], circle, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim(0,256)
plt.show()
cv2.waitKey(0)
