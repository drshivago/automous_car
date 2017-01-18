from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
import cv2


camera = PiCamera(resolution = (640,480),framerate = 32)
camera.vflip = True
rawCapture = PiRGBArray(camera, size=(640,480))
time.sleep(0.5)
thresholdlow = 20
thresholdhigh = 70

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

        image = frame.array    #image is now a nparray
        detected_edges = cv2.Canny(image, thresholdlow, thresholdhigh, apertureSize=3)

        cv2.imshow("Frame", detected_edges)


        key = cv2.waitKey(1) & 0xFF
        rawCapture.truncate(0)
        if key == ord('q'):
                break

cv2.destroyWindow("Frame")
