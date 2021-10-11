# from cvzone.HandTrackingModule import HandDetector
# import cv2
# from cvzone.FaceDetectionModule import FaceDetector

# cap = cv2.VideoCapture(0)
# detector = HandDetector(detectionCon=0.8, maxHands=2)

# detector1 = FaceDetector()

# while True:
#     # Get image frame
#     success, img = cap.read()
#     # Find the hand and its landmarks
#     hands, img = detector.findHands(img)  # with draw
#     # hands = detector.findHands(img, draw=False)  # without draw

#     if hands:
#         # Hand 1
#         hand1 = hands[0]
#         lmList1 = hand1["lmList"]  # List of 21 Landmark points
#         bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
#         centerPoint1 = hand1['center']  # center of the hand cx,cy
#         handType1 = hand1["type"]  # Handtype Left or Right

#         fingers1 = detector.fingersUp(hand1)

#         if len(hands) == 2:
#             # Hand 2
#             hand2 = hands[1]
#             lmList2 = hand2["lmList"]  # List of 21 Landmark points
#             bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
#             img, bboxs = detector1.findFaces(img)
#             cv2.imshow("Image", img)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#             centerPoint2 = hand2['center']  # center of the hand cx,cy
#             handType2 = hand2["type"]  # Hand Type "Left" or "Right"

#             fingers2 = detector.fingersUp(hand2)

#             # Find Distance between two Landmarks. Could be same hand or different hands
#             length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)  # with draw
#             # length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
#     # Display
#     cv2.imshow("Image", img)
#     cv2.waitKey(1)
#     img, bboxs = detector1.findFaces(img)

#     if bboxs:
#         # bboxInfo - "id","bbox","score","center"
#         center = bboxs[0]["center"]
#         cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

#     cv2.imshow("Image", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()



import cvzone
import cv2
cap = cv2.VideoCapture(1)
while True:
    success, img = cap.read()
    cv2.imshow('Image', img)
    cv2.waitKey(1)