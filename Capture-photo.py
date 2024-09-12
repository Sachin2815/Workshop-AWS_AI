import cv2
cap = cv2.VideoCapture(0)
status, photo = cap.read()
cv2.imshow("myphoto", photo)
cv2.waitKey(10000) 
cv2.destroyAllWindows()

cap.release()
