
from imutils.video import VideoStream
import os
import datetime
import time
from time import sleep, strftime, time
#from datetime import datetime
from scipy.spatial import distance as dist
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import cv2
from PIL import Image
frameSize=(320,240)
FACE_DOWNSAMPLE_RATIO =5
SKIP_FRAMES =25

vs=cv2.VideoCapture('C:/Users/Royale121/Desktop/lane dec/test1.mp4')
frame=0
lst4=[]
i=0
a=0
b=0
c=0
d=0
start = time.time()
while True:
	print("[INFO] starting image...")	
	ret,image=vs.read()
	frame=frame+1
	if(frame>10):
		frame=0
	gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	cv2.imwrite("5.png",gray)
	im = Image.open("5.png")
	pix_val = list(im.getdata())
	print(np.std(np.array(pix_val)))
	if(frame==4):
		a= np.std(np.array(pix_val))
		if(i==0):
			print('vehicle fine')
		else:
			final1=d-a
			if(final1>30):
				print('rollover')
				break
			else:
				print('vehicle fine')
##	if(frame==2):
##		b= np.std(np.array(pix_val))
##		final2=a-b
##		if(final2>20):
##			print('rollover')
##			break
##		else:
##			print('vehicle fine')
##	if(frame==3):
##		c= np.std(np.array(pix_val))
##		final3=b-c
##		if(final3>20):
##			print('rollover')
##			break
##		else:
##			print('vehicle fine')
	if(frame==10):
		d= np.std(np.array(pix_val))
		final4=a-d
		if(final4>20):
			print('rollover')
			break
		else:
			print('vehicle fine')
	i=i=1
end = time.time()
print(end - start)
cv2.destroyAllWindows()
vs.stop()
print(lst)
