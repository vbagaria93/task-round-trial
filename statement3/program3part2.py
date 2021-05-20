from PIL import Image
from cv2 import cv2
import sounddevice as sd
img=cv2.imread("maze_lv3.png")
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#img=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
lower=(230,0,0)
upper=(230,255,255)
mask=cv2.inRange(img,lower,upper)
o=cv2.bitwise_and(img,img,mask=mask)

b,g,r=cv2.split(img)
cv2.imshow('b',mask)
cv2.imwrite('MAZE_D.png',mask)
#canny=cv2.dilate(b,(1,1),iterations=5)
#b=cv2.resize(b,(1500,300),interpolation=cv2.INTER_CUBIC)
#cv2.imshow('canny',canny)
#cv2.imshow('b',b)
cv2.waitKey(0)