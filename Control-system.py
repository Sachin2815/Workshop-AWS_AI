import cv2

cap = cv2.VideoCapture(0)

from cvzone.HandTrackingModule import HandDetector

handDetector = HandDetector()

import os

import time

while True:
    status , photo = cap.read()
    findHand = handDetector.findHands(photo , draw=True)

    if findHand[0]:
        mylmlist = findHand[0][0]
        myfingerup  = handDetector.fingersUp(mylmlist)

        if myfingerup == [ 1,1,1,1,1]:
            print("i m all ok 5 five finger up")
            os.system("chrome")
            time.sleep(2)
        elif myfingerup == [ 0, 1, 1, 0 ,0]:
            print("2 finger up")
            os.system("notepad")
            time.sleep(2)
        else:
            print("idk")


    cv2.imshow("myphoto"  ,  photo)
    if cv2.waitKey(100) == 13:
        break


cv2.destroyAllWindows()

cap.release()