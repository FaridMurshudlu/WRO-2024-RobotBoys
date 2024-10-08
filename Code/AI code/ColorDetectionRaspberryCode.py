import cv2
import numpy as np
import serial
import time
import RPi.GPIO as GPIO

arduino = serial.Serial('/dev/ttyACM0', 9600)

# Initialize the camera
cap = cv2.VideoCapture(0)

GPIO.setmode(GPIO.BOARD)
GREEN_PIN = 11
RED_PIN = 12
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(RED_PIN, GPIO.OUT)

def getRedColor(frame: np.ndarray) -> np.ndarray:
    into_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    L1_limit = np.array([0, 100, 100])
    U1_limit = np.array([20, 255, 255])
    L2_limit = np.array([160, 100, 100])
    U2_limit = np.array([180, 255, 255])

    red_mask1 = cv2.inRange(into_hsv, L1_limit, U1_limit)
    red_mask2 = cv2.inRange(into_hsv, L2_limit, U2_limit)
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)

    return cv2.bitwise_and(frame, frame, mask=red_mask)

def getGreenColor(frame: np.ndarray) -> np.ndarray:
    into_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    L_limit = np.array([40, 100, 100])  
    U_limit = np.array([75, 255, 255]) 

    green_mask = cv2.inRange(into_hsv, L_limit, U_limit)
    
    return cv2.bitwise_and(frame, frame, mask=green_mask)

def defineSize(img: np.ndarray, px_size=150) -> bool:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        return False

    largest_contour_area = max([cv2.contourArea(cnt) for cnt in contours])

    if largest_contour_area > px_size:
        return True
    return False

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    green = getGreenColor(frame)
    red = getRedColor(frame)

    green_detected = defineSize(green, 300)
    red_detected = defineSize(red, 50)

    GPIO.output(GREEN_PIN, green_detected)
    GPIO.output(RED_PIN, red_detected)

    print(f"Green detected: {green_detected}, Red detected: {red_detected}")

    cv2.imshow("Green Detection", green)
    cv2.imshow("Red Detection", red)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
