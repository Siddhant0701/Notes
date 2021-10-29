import cv2


def rescale (frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)

    return (cv2.resize(frame,dimensions, interpolation=cv2.INTER_AREA ))


vid = cv2.VideoCapture('Videos/clock.mp4')

while True:
    isTrue, frame = vid.read()

    frame_resize = rescale(frame, 0.5)
    cv2.imshow('Video',frame_resize)
    if (cv2.waitKey(20) & 0xFF==ord('d')):
        break

vid.release()
cv2.destroyAllWindows()
