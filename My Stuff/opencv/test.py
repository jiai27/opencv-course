'''
import cv2 as cv
import os
print(os.getcwd())

img = cv.imread(os.path.join(os.getcwd(),'Resources','Photos','vluigi.png'))
cv.imshow('vlaj',img)
cv.waitKey(0)
'''

import cv2 as cv

img = cv.imread('vluigi.png')
if img is None:
    print("Failed to load image!")
else:
    cv.imshow('test', img)
    cv.waitKey(0)
