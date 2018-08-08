import RPi.GPIO as GPIO
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

def half_time(a):
    while True:
        left()
        time.sleep(a)
        center()
        time.sleep(a)

def left():
    GPIO.output(16, GPIO.LOW)
    GPIO.output(15, GPIO.HIGH)

def center():
    GPIO.output(16, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)

half_time(0.03)

GPIO.cleanup()
