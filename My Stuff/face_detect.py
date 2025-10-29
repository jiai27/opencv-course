import cv2 as cv

img = cv.imread("vluigi.png")
cv.imshow('vlaj',img)

#1. convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayvlaj', gray)

#2. Read haar_face.xml
haar_cascade = cv.CascadeClassifier("haar_face.xml")

#3. try to detect the face
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, minNeighbors=3)
'''
src - source image
scaleFactor - ?
minNeighbours - minimum number of rectangles required to recognize it as a face
    takes image, uses vars to detect a face, returns coordinates of the face AS A LIST to faces_rect
'''
print(f'number of faces found: {len(faces_rect)}, coordinates: {faces_rect}')

#4. draw the bounding box
for (x,y,w,h) in faces_rect: 
    #draw a rectangle
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
cv.imshow('detected faces', img)

#note: haar_cascades are very sensitive to noise; so what LOOKS like a face will be considered a face too
#you counter this by modifying scaleFactor & minNeighbors




cv.waitKey(0)