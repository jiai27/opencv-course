import cv2 as cv
import numpy as np

#correlates to AND, OR, NOT etc in regular logic courses
#operates in a binary matter: 0 = OFF, 1 = ON

#initialization: makes two images: one with a circle and one with a rectangle
blank = np.zeros((400,400), dtype='uint8') #makes a blank 400x400 numpy array (image)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)


#bitwise AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise AND', bitwise_and)

#bitwise OR --> intersecting + non-intersecting regions
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise OR', bitwise_or)

#bitwise XOR - good for returning NON intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwise XOR', bitwise_xor)

#bitwise NOT
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('bitwise NOT', bitwise_not)


cv.waitKey(0)