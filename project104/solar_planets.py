import cv2
import numpy

img=cv2.imread("solar-system.jpg")

cv2.putText(img,"sun",(20,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,"mercury",(110,240),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,"venus",(200,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,"earth",(290,240),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,"mars",(380,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,"jupiter",(530,250),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,"saturn",(750,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,"uranus",(970,250),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,"neptune",(1110,190),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255))
cv2.imwrite("Solar_systemwithname.jpg",img)
            
cv2.imshow("output",img)

cv2.waitKey(0)

