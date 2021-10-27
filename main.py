from cvzone.HandTrackingModule import HandDetector
import cv2
import serial
import time

arduino = serial.Serial('COM2', 9600)
time.sleep(2)

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon =0.8, maxHands=1)
while True:
    # Get image frame
    success, img = cap.read()

    # Find hand and its
    hands, image =detector.findHands(img)
    # hands = detector.findHands(img, draw =True)  # without draw
    if hands:
    # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right
        fingers1 = detector.fingersUp(hand1)
        print(f'{fingers1}') 
        if fingers1 == [0,1,0,0,0]:
            arduino.write(b'd')
            print(f'1') 
        if fingers1 == [0,1,1,0,0]:
            print(f'cleaner') 
            arduino.write(b'c')
        if fingers1 == [1,1,1,0,0]:
            print(f'restaurent') 
            arduino.write(b'r')
    cv2.imshow("Image", img)
    cv2.waitKey(1)