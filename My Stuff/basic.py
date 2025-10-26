import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')


#1. Converting images to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray) #name, image to pass

#2. Blur - removes noise in an image
park = cv.imread('Resources/Photos/park.jpg')
blur = cv.GaussianBlur(park, (5,5), cv.BORDER_DEFAULT)  #kernel size should be odd numbers
#cv.imshow('Blur', blur)
#the larger the kernel, the more blurred the image will be
super_blur = cv.GaussianBlur(park, (15,15), cv.BORDER_DEFAULT)
#cv.imshow('Blur 15', super_blur)


#3. Edge Cascade - detects edges in an image
vluigi = cv.imread('Resources/Photos/vluigi.png')
canny = cv.Canny(vluigi, 125,175)  #lower and upper threshold values
#cv.imshow('Canny Edges', canny)

#--blur + canny can help reduce the number of edges detected--
blur_canny = cv.Canny(blur, 125,175)
#cv.imshow('Canny Blur', blur_canny)


#4. Dilating the image - increases the thickness of edges
dilated = cv.dilate(canny, (3,3), iterations=1)  #kernel size and number of iterations
#cv.imshow('Dilated', dilated)

#Eroding - opposite of dilating; decreases thickness of edges
eroded = cv.erode(dilated, (3,3), iterations=1)
#cv.imshow('Eroded', eroded)
#essentially "reverses", but some edges may be lost in the process


#5. Resize & Cropping
resized = cv.resize(park, (500,500), interpolation=cv.INTER_AREA)   #width, height; IGNORES ASPECT RATIO
#INTER_AREA - good for shrinking an image
#INTER_LINEAR / INTER_CUBIC - good for zooming in (enlarging past original size)
#cv.imshow('Resized', resized)

#Cropping; since images are just numpy arrays, we can use array slicing
cropped = park[50:200, 200:400]   #y1:y2, x1:x2
cv.imshow('Cropped', cropped)


cv.waitKey(0)