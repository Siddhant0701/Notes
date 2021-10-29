import cv2

# IMAGE

# img = cv2.imread('Photos/dog.jpg')
# cv2.imshow('Cat',img)
# cv2.waitKey(0)


# VIDEO

vid = cv2.VideoCapture('Videos/clock.mp4')

while True:
    isTrue, frame = vid.read()
    cv2.imshow('Video',frame)
    if (cv2.waitKey(20) & 0xFF==ord('d')):
        break

vid.release()
cv2.destroyAllWindows()
