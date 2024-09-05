import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")

def nothing(x):
    pass

cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)  # Lower Hue
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)  # Lower Saturation
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)  # Lower Value
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)  # Upper Hue
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)  # Upper Saturation
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)  # Upper Value

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")

    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
