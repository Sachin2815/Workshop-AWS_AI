import cv2  # Import OpenCV library

cap = cv2.VideoCapture(0)  # Access the default webcam

status, photo = cap.read()  # Capture a frame from the webcam

cv2.imshow("myphoto", photo)  # Display the captured image in a window
cv2.imwrite("sachin.png", photo)  # Save the captured image as "sachin.png"
cv2.waitKey(10000)  # Keep the window open for 10 seconds
cv2.destroyAllWindows()  # Close the window

cap.release()  # Release the webcam resource
