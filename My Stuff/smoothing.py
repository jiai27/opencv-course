import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/vluigi.png')
cv.imshow('vlaj', img)

#averaging - middle of the kernel is the average of surrounding
average = cv.blur(img, (10,10))
cv.imshow('average blur', average)

#gaussian blur - each surrounding has a weight, so you take the weighted average
gauss = cv.GaussianBlur(img, (7,7), 0)  
'''
src - source image
krs - kernel size - must be odd number
sigmaX = standard deviation in the x direction 
'''
cv.imshow('gauss',gauss)

#median blur - finds median of surrounding pixels (more effective in reducing noise)
median = cv.medianBlur(img, 3)
'''
doesn't require kernel size; it assumes its 3x3 based on the one integer
not effective in large kernel sizes (>5)
'''
cv.imshow('median', median)

#bilateral blurring - most effective in reducing noises; retains most edges
bilateral = cv.bilateralFilter(img, 5, 15, 15)
'''
sigmaColor - value indicates the number of colors in the neighbourhood that will be considered
sigmaSpace - value influences the distance of influencing pixels
'''
cv.imshow('bilateral', bilateral)


cv.waitKey(0)
