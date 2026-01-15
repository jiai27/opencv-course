import cv2
cam = cv2.VideoCapture(0) # Remove second arg if using webcam
while True:
    ret_val, img = cam.read()
    cv2.imshow('test', img)