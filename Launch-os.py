import cv2
cap = cv2.VideoCapture(0)

from cvzone.HandTrackingModule import HandDetector
handDetector = HandDetector()

import boto3

myec2client = boto3.client(
                    "ec2", 
                    aws_access_key_id="AKIAUW5PJDEB2MITC3C",
                    aws_secret_access_key="VTNISAZu1xsK0KSYEtoxJvtW8mjQ9RMONmM6v1S",
                    region_name="ap-south-1"
            )

def lwOSrun():
    myosrun = myec2client.run_instances(
        InstanceType="t2.micro",
        ImageId="ami-02a2af70a66af6dfb", 
        MaxCount=1,
        MinCount=1,
    )
    return myosrun

def lwOSterminate(myosrun):
    myosterminate = myec2client.terminate_instances(
        InstanceIds=[ myosrun['Instances'][0]['InstanceId'] ]
    )

import time


while True:
    status, myphoto = cap.read()
    handPhotoDraw = handDetector.findHands(myphoto, draw=True)
    
    if handPhotoDraw[0]:
        photoDraw = handPhotoDraw[1]
        handLmList = handPhotoDraw[0][0]
        handFingerUp = handDetector.fingersUp(handLmList)

        if handFingerUp == [0, 1, 0, 0, 0]:
            myos = lwOSrun()
            print("os launching ..")
            time.sleep(2)
        elif handFingerUp == [0, 1, 1, 0, 0]:
            lwOSterminate(myos)
            print("os terminating ..")
            time.sleep(2)
        else:
            pass
    
    cv2.imshow("My photo" , myphoto)
    if cv2.waitKey(100) == 13:
        break
        
cv2.destroyAllWindows()


cap.release()
