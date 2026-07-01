#OPEN CV

# import cv2

# image = cv2.imread("assets/image1.jpg")
# print(image.shape)
# print(type(image))


# ==============================================================================

import os
import cv2

image_path = os.path.join('.', 'assets', "image1.jpg")
img = cv2.imread(image_path)

cv2.imwrite(os.path.join('.', 'assets', 'image4_out.jpg'), img)
cv2.imshow('img', img)
cv2.waitKey(5000)          # Wait for 5 seconds
cv2.destroyWindow('img')
