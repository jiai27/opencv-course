import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')      #creates a black image of 500x500 pixels; dtype specifies the data type of the array elements
#cv.imshow('Blank', blank)

#img = cv.imread('Resources/Photos/cat_large.jpg')
#cv.imshow('Cat', img)


#1. Paint the image a certain color
'''
#blank[:] = 0,255,0    #paints the entire image green; format is BGR
#cv.imshow('Green', blank)   #requires "3" channels for color images
blank[200:300, 300:400] = 255,0,0    #paints the entire image blue
#cv.imshow('Blue', blank)
'''

#2. Draw a rectangle - draws a blue rectangle, a filled rectangle and half filled
'''
#parameters: cv.rectangle(image, start_point, end_point, color, thickness)
#cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness=2)   #draws a blue rectangle
#cv.rectangle(blank, (0,0), (250,400), (255,0,0), thickness=cv.FILLED)   #draws a filled blue rectangle ; thickness=-1 also does this
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2 + 100), (255,0,0), thickness=cv.FILLED)   #draws a filled blue rectangle ; thickness=-1 also does this
cv.imshow('Rectangle', blank)
'''

#3. Draw a circle
#parameters: cv.circle(image, center_coordinates, radius, color, thickness)
'''
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=cv.FILLED)   #draws a filled red circle at the center of the image with radius 40
cv.imshow('Circle', blank)
'''

#4. Draw a line
#parameters: cv.line(image, start_point, end_point, color, thickness)
'''
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)   #draws a white line from top-left corner to center
cv.imshow('Line', blank)
'''

#5. Write text
#parameters: cv.putText(image, text, org, font, fontScale, color, thickness, lineType)
cv.putText(blank, 'Hello World!', (225,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)   #writes green text at specified location
cv.imshow('Text', blank)


cv.waitKey(0)