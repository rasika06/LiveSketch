
import cv2
import numpy as np
import matplotlib.pyplot as plt
def sketch(image):
    #conver to gray scale
    image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #Clean up image using guassian blur
    image_gray_blur=cv2.GaussianBlur(image_gray,(5,5),0)
    #extracting edges
    edges=cv2.Canny(image_gray_blur,10,70)
    #Invert binarize the image
    ret,mask=cv2.threshold(edges,70,255,cv2.THRESH_BINARY_INV)
    return mask

##Video Capture from camera. 
##To capture video from a file, just type in the name of the file. eg(cap=cv2.VideoCapture('filename.avi'))
capture_video=cv2.VideoCapture(0) # 0-->Default camera

while True:
    ret,frame=capture_video.read()
    cv2.imshow('Live Sketcher', sketch(frame))
    if cv2.waitKey(1)==13: #13 is enter key
        break
    
capture_video.release()
cv2.destroyAllWindows()




