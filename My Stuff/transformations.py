import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')

#Translation - shifting the image on the x and y axis
def translation(image, x,y): #image, and number of pixels to shift on x and y axis
    '''
    - make a numpy array for the transformation matrix
    - use cv.warpAffine to apply the transformation matrix to the image
    '''    
    transMat = np.float32([[1,0,x],[0,1,y]])  #transformation matrix
    dimensions = (img.shape[1], img.shape[0])  #width, height 
    return cv.warpAffine(image, transMat, dimensions)  #applies the transformation 

    # negative values for x will shift the image to the left
    # negative values for y will shift the image up
    # so positive x shifts right, positive y shifts down

translated_image = translation(img, 100,100) #shift image 100 pixels right and 100 pixels down
#cv.imshow('Translated', translated_image)

#--Rotation--
def rotate(image, angle, rotPoint=None):
    (height, width) = image.shape[:2]

    if rotPoint is None: #assumes we rotate around the center point
        rotPoint = (width//2, height//2)
    
    rotMat = np.float32(cv.getRotationMatrix2D(rotPoint, angle, 1.0)) #1.0 is scale factor (doesn't change size)
    dimensions = (img.shape[1], img.shape[0])  #width, height   
    return cv.warpAffine(image, rotMat, dimensions) #warpAffine applies the rotation matrix to the image


rotated_image = rotate(img, -45)  #rotate 45 degrees clockwise
#cv.imshow('Rotated', rotated_image)

rotatedrotated = rotate(rotated_image, -45)  #rotate another 45 degrees clockwise
#cv.imshow('Rotated Rotated', rotatedrotated)
#note that whatever is rotated originally will be saved as a separate image, therefore rotating WILL CARRY ANY BLACK BORDERS WITH IT


#--Resizing--
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)  #width, height is the destination
cv.imshow('Resized', resize)

#--Flipping--
flip = cv.flip(img, -1)  #0 for vertical flip, 1 for horizontal flip, -1 for both axes
cv.imshow('Flipped', flip)

#--Cropping--
cropped = img[200:400, 300:400]  #y1:y2, x1:x2
cv.imshow('Cropped', cropped)

cv.waitKey(0)