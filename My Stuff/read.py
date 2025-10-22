#jiai27 - notes according to OpenCV course video

import cv2 as cv


#reading images
'''
#display image of a cat (640x427)
img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)       #keyboard binding function; waits for specified milliseconds for any keyboard event

#display image of the cat but bigger (1280x854)
img_bigger = cv.imread('Resources/Photos/cat_large.jpg')
cv.imshow('Cat Bigger', img_bigger)
cv.waitKey(0)      
'''

#reading videos
'''
capture = cv.VideoCapture('Resources/Videos/dog.mp4') #can take integer arguments; 0 for default camera, 1 for external camera, etc.

while True:
    isTrue, frame = capture.read()   #reads video frame by frame; isTrue is boolean value to check if frame is read correctly
    cv.imshow('Video', frame)

    #a way to stop the video
    if cv.waitKey(20) & 0xFF==ord('d'):   #waits for 20 milliseconds for keyboard event; if 'd' is pressed, breaks loop
        break

capture.release()   #releases the video capture object
cv.destroyAllWindows()  #closes all OpenCV windows

# should return a -215 error if the video runs out of frames to read
'''
