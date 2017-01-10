from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
import cv2


camera = PiCamera(resolution = (640,480),framerate = 32)
camera.vflip = True
rawCapture = PiRGBArray(camera, size=(640,480))
time.sleep(0.5)
threshold1 = 20
Max_threshold = 100

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

        image = frame.array    #image is now a nparray
        detected_edges = cv2.blur(image, (3,3))
        detected_edges2 = cv2.Canny(detected_edges, threshold1, threshold1*3, apertureSize=3)

        cv2.imshow("Frame", detected_edges2)


        key = cv2.waitKey(1) & 0xFF
        rawCapture.truncate(0)
        if key == ord('q'):
                break

cv2.destroyWindow("Frame")
