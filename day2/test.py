import cv2

print("OpenCV version:", cv2.__version__)

for i in range(5):
    print(f"\nTrying camera {i}...")

    cap = cv2.VideoCapture(i)

    print("Opened:", cap.isOpened())

    if cap.isOpened():
        ret, frame = cap.read()
        print("Read:", ret)

        if ret:
            print("Frame shape:", frame.shape)
            cv2.imshow(f"Camera {i}", frame)
            cv2.waitKey(2000)
            cv2.destroyAllWindows()

    cap.release()