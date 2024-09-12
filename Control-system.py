import cv2  # Import OpenCV for image capture and manipulation

cap = cv2.VideoCapture(0)  # Access the default webcam (camera index 0)

from cvzone.HandTrackingModule import HandDetector  # Import HandDetector from cvzone library

handDetector = HandDetector()  # Initialize the hand detector

import os  # Import os module to run system commands (e.g., opening apps)
import time  # Import time module for delays

# Infinite loop to continuously capture video and check for hand gestures
while True:
    status, photo = cap.read()  # Capture a frame from the webcam
    findHand = handDetector.findHands(photo, draw=True)  # Detect hands and draw landmarks on the image if found
    
    # If a hand is detected in the frame
    if findHand[0]:
        mylmlist = findHand[0][0]  # Get the landmark list of the detected hand
        myfingerup = handDetector.fingersUp(mylmlist)  # Check which fingers are up (returns a list of 0s and 1s)
    
        # If all five fingers are up
        if myfingerup == [1, 1, 1, 1, 1]:
            print("I'm all okay, 5 fingers up")
            os.system("chrome")  # Open Google Chrome using the system's command
            time.sleep(2)  # Delay for 2 seconds before proceeding
            
        # If only the index and middle fingers are up
        elif myfingerup == [0, 1, 1, 0, 0]:
            print("2 fingers up")
            os.system("notepad")  # Open Notepad using the system's command
            time.sleep(2)  # Delay for 2 seconds before proceeding
            
        # If the gesture does not match predefined patterns
        else:
            print("I don't know this gesture")
    
    # Display the webcam feed with hand landmarks
    cv2.imshow("myphoto", photo)
    # If the "Enter" key is pressed (ASCII code 13), break the loop
    if cv2.waitKey(100) == 13:
        break
        
cv2.destroyAllWindows()  # Close the display window
cap.release()  # Release the webcam resource
