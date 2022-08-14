from threading import Thread
import cv2
import numpy as np


# Webcamera no 0 is used to capture the frames
cap = cv2.VideoCapture(0)


# This drives the program into an infinite loop.
while(1):		
    # Captures the live stream frame-by-frame
    _, frame = cap.read()
    # Converts images from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # what is hsv range for green?
    lower_color = np.array([50,50,50])
    upper_color = np.array([70,255,255])
    
    # what is hsv range for red?
    # lower_color = np.array([0,70,50])
    # upper_color = np.array([8,255,255])

    # what is hsv range for blue?
    # lower_color = np.array([110,50,50])
    # upper_color = np.array([130,255,255])
    
    # what is hsv range for yellow?
    # lower_color = np.array([20,50,50])
    # upper_color = np.array([30,255,255])
    
    # best color for the bulb is green

    print(hsv)
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Draw lines to show the boundaries of leds to be placed ffor each team
    cv2.line(frame, (140, 0), (140, 500), (0, 0, 0), 2)    
    cv2.line(frame, (340, 0), (340, 500), (0, 0, 0), 2)    
    cv2.line(frame, (500, 0), (500, 500), (0, 0, 0), 2)
    cv2.putText(frame, "Team 1", (000, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
    cv2.putText(frame, "Team 2", (140, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
    cv2.putText(frame, "Team 3", (340, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
    cv2.putText(frame, "Team 4", (500, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
    # The bitwise and of the frame and mask is done so
    # that only the blue coloured objects are highlighted
    # and stored in res
    res = cv2.bitwise_and(frame,frame, mask= mask)

    # finds all countous in the mask and checks its coordinates
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            M = cv2.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            # draw the contour and center of the shape on the image
            cv2.drawContours(frame, cnt, -1, (0,255,0), 2)
            cv2.circle(frame,(cx,cy), 7, (255,255,255), -1)
            if (cx < 140):
                print("Right, Team 1")
            elif (cx >= 140 and cx < 340):
                print("Center, Team 2")
            elif (cx >= 340 and cx < 500):
                print("Left, Team 3")
            elif (cx >= 500):
                print("Right, Team 4")

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res) 
                
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()

# release the captured frame
cap.release()
