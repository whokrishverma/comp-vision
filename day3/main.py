##STEPS
    #read image
    #detect faces 
    #blur faces
    #save image

#IMAGE

import cv2
import mediapipe as mp

img_path = 'assets/img2.jpg'

img = cv2.imread(img_path)

mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    for dectection in out.detections:
        location_data = detection.location_data
        bbox = location_data