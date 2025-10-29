import cv2 as cv
import numpy as np

img = cv.imread('vluigi.png')
cv.imshow('vlaj', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Laplacian - shows laplacian edges (?)
'''
computes grayscale -> requires plenty of calculations
since pixel values can't be negative, we compute them to absolute values, then convert them to uint8
'''
lap = cv.Laplacian(gray, cv.CV_64F)    #what is this doing?
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#Sobbel (sobbel filter?)
'''
computes gradients in 2 directions: x and y
'''
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) #xdir=1, ydir=0
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)

combined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow('combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)


cv.waitKey(0)