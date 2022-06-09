from colorsys import hsv_to_rgb
import cv2 
import numpy as np

cap = cv2.VideoCapture(2)



while True:

    _, frame = cap.read(0)  


    #cropu1 = frame[:520,0:650]      # Top left part of the photo
    
    #cropd1 = frame[240:,0:650]      # Bottom left part of the photo
    

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #for red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low_red, high_red)
    
    #for blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])#168de iyi çalışıyor
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask = blue_mask)
    cropu_blue = blue[:520, 0:650]


    #for green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask = green_mask)


    cv2.imshow("frame" , frame)
    #cv2.imshow("Red mask" , mask) (for redmask)
    cv2.imshow("Blue", cropu_blue	)  #for blue
    #cv2.imshow("green", green) 
    #cv2.imshow("cropu1",cropu1)     # It will show cropu1 part in a window     
    #cv2.imshow("cropd1",cropd1)     # It will show cropd1 part in a window    

    key = cv2.waitKey(1)
    if key == 27:
        break



