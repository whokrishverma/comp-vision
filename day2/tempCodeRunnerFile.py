import cv2

from util import get_limits

yellow = [0, 255, 255] #yellow in BGR colorspace

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Mirror the frame horizontally
    mirrored = cv2.flip(frame, 1)

    cv2.imshow("Mirrored Camera", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()