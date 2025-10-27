import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
#cv.imshow('Original', img)

#--Contours: boundaries of objects in an image--

#grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)


#blur
#blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
#cv.imshow('Blurred', gray)

#then apply canny edge detector
canny = cv.Canny(gray, 125,175)  #lower and upper threshold values
#cv.imshow('Canny Edges', gray)


#ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) #apply binary thresholding to get a binary image
#cv.imshow('Thresholded', thresh)

#find contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
'''
parameters:
- input image (should be a binary image) - so should be cannied
- contour retrieval mode:
    - cv.RETR_LIST: retrieves all contours without establishing any hierarchical relationships
    - cv.RETR_EXTERNAL: retrieves only the extreme outer contours
    - cv.RETR_CCOMP: retrieves all contours and organizes them into a two-level hierarchy
    - cv.RETR_TREE: retrieves all contours and reconstructs a full hierarchy of nested contours
- contour approximation method:
    - cv.CHAIN_APPROX_NONE: stores all the contour points, resulting in a complete representation of the contour
    - cv.CHAIN_APPROX_SIMPLE: compresses horizontal, vertical, and diagonal segments and leaves only their end points
'''
print(f'{len(contours)} contours found!')

#draw contours

#start with a blank canvas
blank = 255 * np.ones(img.shape, dtype='uint8')  #white blank
cv.drawContours(blank,contours, -1, (0,0,0), 1)  #-1 means draw all contours, color black, thickness 1
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)