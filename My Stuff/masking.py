import cv2 as cv
import numpy as np

#img = cv.imread('Resources/Photos/vlaj.png')
#macos change:
img = cv.imread('vluigi.png')
cv.imshow('vlaj',img)

blank = np.zeros(img.shape[:2], dtype='uint8')
#cv.imshow('blank',blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2+45, img.shape[0]//2), 100, 255, -1)
#cv.imshow('mask', mask)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circle,rectangle) #mask needs to be same size as image
cv.imshow('weird shape', weird_shape)

#mask intersection
masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('weird shaped masked image', masked)


cv.waitKey(0)