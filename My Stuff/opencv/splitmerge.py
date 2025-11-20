import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/vluigi.png')
#cv.imshow('vlaj',img)

b,g,r = cv.split(img)
#cv.imshow('blue', b)
#cv.imshow('green',g)
#cv.imshow('red',r)

print(img.shape, b.shape, g.shape, r.shape) #img.shape says (336,448,3) -> height, width, color channels

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)


#recreating only in that color value:

#create a blank image
blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue only', blue)
cv.imshow('green only', green)
cv.imshow('red only', red)

cv.waitKey(0)