import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/vluigi.png')      #openCV displays images in BGR format by default




#plt.imshow(img)     #matplotlib assumes images are in RGB format
#plt.show()


#Color Spaces:
#BGR to Grayscale conversion
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)      #gray color code
#cv.imshow('Gray', gray)

#BGR to HSV conversion (hue, saturation, value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)        #hsv color code
#cv.imshow('HSV', hsv)

#BGR to LAB conversion (lightness, a, b)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)        #lab color code
#cv.imshow('LAB', lab)


#BGR to RGB conversion
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)        #rgb color code
cv.imshow('RGB', rgb)
plt.imshow(rgb)     #now matplotlib will display the colors correctly
plt.show()

#note: cannot convert grayscale to other color spaces; must start with a 3-channel image

#hsv to BGR conversion
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)

cv.waitKey(0)