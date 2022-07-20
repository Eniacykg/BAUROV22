#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from pymavlink import mavutil
import datetime                     #!!!!!!!!!!!!!!!!ÇALIŞMASI İÇİN EN SONDAKİ KOMUTU UNCOMMENT EDİN!!!!!!!!!!!!!
from collections import deque
import numpy as np
import cv2
import imutils
import enumm


# bu kodu main koddan threading olarak çağıracağız!!!

def daire_isleme():
	greenLower = (29, 86, 6) # lower
	greenUpper = (64, 255, 255) # upper
	pts = deque(maxlen=64)

	vs = cv2.VideoCapture(0)
	# keep looping
	while True:
		ret, frame = vs.read()
		if frame is None:
			pass
		frame = imutils.resize(frame, width=600)
		blurred = cv2.GaussianBlur(frame, (11, 11), 0)
		hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

		mask = cv2.inRange(hsv, greenLower, greenUpper)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)


		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		center = None
		if len(cnts) > 0:
			c = max(cnts, key=cv2.contourArea)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			if radius > 10:
				enumm.daire_x = x
				enumm.daire_y = y
				
				cv2.circle(frame, (int(x), int(y)), int(radius),
					(0, 255, 255), 2)
				cv2.circle(frame, center, 5, (0, 0, 255), -1)
			print(x, y)
			
			#ykg buradan:
			if(x>0): #for in range(20) yapmak istiyorum nasıl yapabilirim
				enumm.daire_tespit = True
			else:
				enumm.daire_tespit = False
			
			
				
			print(enumm.daire_tespit)
			
			#print(enumm.daire_tespit )

#vs.release()
#cv2.destroyAllWindows()


daire_isleme_thread = threading.Thread(target=daire_isleme_thread, name='HSV Basladi')
#ai_thread.start()

#daire_isleme()