#jiai27 - notes according to OpenCV course video
#topic: rescaling images and videos

#motivation: sometimes images or videos are too large to fit on the screen, so we need to rescale them

import cv2 as cv

#img = cv.imread('Resources/Photos/cat_large.jpg')
#cv.imshow('Cat', img)

def rescaleFrame(frame, scale = 0.75):
    print(frame.shape)   #prints original dimensions
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale) 
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA) #resizes the frame to "dimensions"; does the heavy liftin


#pasted from read.py
capture = cv.VideoCapture('Resources/Videos/dog.mp4') #can take integer arguments; 0 for default camera, 1 for external camera, etc.
while True:
    isTrue, frame = capture.read()   #reads video frame by frame; isTrue is boolean value to check if frame is read correctly
    frame_resizes = rescaleFrame(frame, scale=0.75)

    #WILL PLAY TWO WINDOWS: ORIGINAL AND RESCALED
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resizes)

    #a way to stop the video
    if cv.waitKey(20) & 0xFF==ord('d'):   #waits for 20 milliseconds for keyboard event; if 'd' is pressed, breaks loop
        break

capture.release()   #releases the video capture object
cv.destroyAllWindows()  #closes all OpenCV windows

def changeRes(width, height): #ideal width and height
    capture.set(3, width)   #3 is the property of the class for width
    capture.set(4, height)  #4 is the property of the class for height

    