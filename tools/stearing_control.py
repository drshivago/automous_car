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

def turn_left(a):
        left()
        forward()
        time.sleep(a)
        center()
        time.sleep(0.05)
def turn_right(a):
        right()
        forward()
        time.sleep(a)
        center()
        time.sleep(a)
def go_forth(a):
    forward()
    time.sleep(a)
    stop()
    time.sleep(a/10.0)
    
def right():
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GOIP.HIGH)
def left():
    GPIO.output(16, GPIO.LOW)
    GPIO.output(15, GPIO.HIGH)
def center():
    GPIO.output(16, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
def forward():
    GPIO.output(12, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)
def backward():
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)
def stop():
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)

t_end = time.time() + 1.5

while time.time() < t_end:
    
    turn_left(1)
    #go_forth(0.5)
    

GPIO.cleanup()
