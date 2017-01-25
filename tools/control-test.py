import RPi.GPIO as GPIO
import picamera
import time

GPIO.setmode(GPIO.BOARD)

#drive
#forward(purple)
GPIO.setup(11, GPIO.OUT)
#backward(black
GPIO.setup(12, GPIO.OUT)
#steering
#left(yellow)
GPIO.setup(15, GPIO.OUT)
#right(green)
GPIO.setup(16, GPIO.OUT)

camera = picamera.PiCamera()
camera.resolution = (640,480)
camera.framerate = 30
camera.vflip = True

time.sleep(2)
#camera.start_recording('drivingvideo.h264', format='h264')
camera.start_preview()
key = ''
forard = False
bakk = False
key = 'n'
direct = ''
side = ''
while key != 'q':
    key = raw_input()
    if key == 'w':
        direct = 'forward'
    if forard:
        GPIO.output([15, 16], GPIO.LOW)
        forard = False
        side = ''
    GPIO.output(12, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)
    forard = True
    bakk = False
    if key == 'a':
        side = 'left'
        GPIO.output(16, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
    if key == 'd':
        side = 'right'
        GPIO.output(15, GPIO.LOW)
        GPIO.output(16, GPIO.HIGH)
    if key == 's':
        direct = 'reverse'
    if bakk:
        GPIO.output([15, 16], GPIO.LOW)
        bakk = False
        side = ''
    GPIO.output(11, GPIO.LOW)                
    GPIO.output(12, GPIO.HIGH)
    bakk = True
    forard = False
    if key == 'f':
        direct = 'full stop'
        side = ''
        GPIO.output([11, 12, 15, 16], GPIO.LOW)
        forard = False
        bakk = False
    camera.annotate_text = direct + ' ' + side
camera.stop_preview()
#camera.wait_recording(3)
#camera.stop_recording()

GPIO.cleanup()
