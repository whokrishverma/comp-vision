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

##==============================================================

# import cv2

# from PIL import Image

# from util import get_limits

# # yellow = [0, 255, 255] #yellow in BGR colorspace
# blue = [0, 255, 0]  # Blue in BGR

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     frame = cv2.flip(frame, 1)

#     hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     # lowerLimit, upperLimit = get_limits(color=yellow)
#     lowerLimit, upperLimit = get_limits(color=blue)

#     mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

#     mask_ = Image.fromarray(mask)

#     bbox = mask_.getbbox()

#     if bbox is not None:
#         x1, y1, x2, y2 = bbox
        
#         frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

#     print(bbox)

#     # Mirror the frame horizontally
#     # mirrored = cv2.flip(frame, 1)

#     cv2.imshow("Mirrored Camera", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

##==============================================================
# import cv2

# from util import get_limits

# # Choose the color you want to detect (BGR format)
# color = [0, 0, 255]  # Red

# cap = cv2.VideoCapture(1)

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     # Mirror the frame
#     frame = cv2.flip(frame, 1)

#     # Convert to HSV
#     hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     # Get HSV limits
#     limits = get_limits(color)

#     # Create mask
#     if isinstance(limits[0], tuple):
#         # Red returns two HSV ranges
#         (lower1, upper1), (lower2, upper2) = limits

#         mask1 = cv2.inRange(hsvImage, lower1, upper1)
#         mask2 = cv2.inRange(hsvImage, lower2, upper2)

#         mask = cv2.bitwise_or(mask1, mask2)

#     else:
#         # All other colors return one HSV range
#         lowerLimit, upperLimit = limits
#         mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

#     # Remove small noise
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
#     mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
#     mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

#     # Find contours
#     contours, _ = cv2.findContours(
#         mask,
#         cv2.RETR_EXTERNAL,
#         cv2.CHAIN_APPROX_SIMPLE
#     )

#     # Draw bounding boxes
#     for contour in contours:

#         if cv2.contourArea(contour) < 500:
#             continue

#         x, y, w, h = cv2.boundingRect(contour)

#         cv2.rectangle(
#             frame,
#             (x, y),
#             (x + w, y + h),
#             (0, 255, 0),
#             3
#         )

#     cv2.imshow("Object Detection", frame)

#     # Press 'q' to quit
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows() 


import cv2

from util import get_limits

# ---------------------------------
# SETTINGS
# ---------------------------------

COLOR = "red"      # red, green, blue, yellow, orange,
                     # purple, cyan, white, black

CAMERA = 0

MIN_AREA = 5000

# ---------------------------------

cap = cv2.VideoCapture(CAMERA)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Mirror image
    frame = cv2.flip(frame, 1)

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get HSV limits
    limits = get_limits(COLOR)

    # Red requires two HSV ranges
    if COLOR.lower() == "red":

        lower1, upper1, lower2, upper2 = limits

        mask1 = cv2.inRange(hsv, lower1, upper1)
        mask2 = cv2.inRange(hsv, lower2, upper2)

        mask = cv2.bitwise_or(mask1, mask2)

    else:

        lower, upper = limits

        mask = cv2.inRange(hsv, lower, upper)

    # Remove noise
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (5, 5)
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        kernel
    )

    # Find contours
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:

        area = cv2.contourArea(contour)

        if area < MIN_AREA:
            continue

        x, y, w, h = cv2.boundingRect(contour)

        # Draw rectangle
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Display area
        cv2.putText(
            frame,
            f"Area: {int(area)}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    # Display selected color
    cv2.putText(
        frame,
        f"Color: {COLOR.title()}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.imshow("Mask", mask)
    cv2.imshow("Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()