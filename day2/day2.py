## DETECTING COLOR ##
 

# import cv2

# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()

#     cv2.imshow('frame', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()

# cv2.destroyAllWindows()


import cv2

from PIL import Image

from util import get_limits

# yellow = [0, 255, 255] #yellow in BGR colorspace
blue = [0, 255, 0]  # Blue in BGR

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # lowerLimit, upperLimit = get_limits(color=yellow)
    lowerLimit, upperLimit = get_limits(color=blue)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    print(bbox)

    # Mirror the frame horizontally
    # mirrored = cv2.flip(frame, 1)

    cv2.imshow("Mirrored Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
