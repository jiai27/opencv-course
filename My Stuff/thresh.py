import cv2 as cv
import numpy as np

#macos; regular pc move vluigi back to the folder
img = cv.imread('vluigi.png')
cv.imshow('vlaj', img)

#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Simple Thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY) #compares every pixel to 150, if above, it becomes 255, if below, 0
cv.imshow('Simple Thresholding', thresh)
threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV) #compares every pixel to 150, if above, it becomes 255, if below, 0
cv.imshow('Simple Thresholding Inverse', thresh_inv)

#Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       11, 5)
cv.imshow('adaptive thresholding', adaptive_thresh)
'''
src - source image
maxValue - what the upper bound cap is
adaptiveMethod - adaptivethresh (?)
    can be ADAPTIVE_THRESH_MEAN_C - for general average
    can be ADAPTIVE_THRESH_GAUSSIAN_C - for weighted avg
    depends on what you're trying to do
thresholdType - thresh binary (because we want a binary image)
blockSize - defining kernel size (11x11) ; computes a mean over the neighborhood of pixels, then calcuates the "optimal" value
C - integer you're subtracting from the mean

'''

cv.waitKey(0)