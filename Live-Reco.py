import cv2
cap = cv2.VideoCapture(0)

while True:
    status, photo = cap.read()  # Capture frame-by-frame
    cv2.imshow("video_start", photo)  # Display the resulting frame

    if cv2.waitKey(10) == 13:  # Exit loop if 'Enter' key is pressed
        break
# Release the capture and close any open windows
cap.release()
cv2.destroyAllWindows()


