import io
import socket
import struct
import time
import picamera

rez = (640,480)

client_socket = socket.socket()	#create a new socket
client_socket.connect(('192.168.2.21', 8000))	#whatever tank ip is

connection = client_socket.makefile('w')
try:
        with picamera.PiCamera() as camera:
                camera.resolution = rez
                camera.framerate = 30

	
                camera.start_recording(connection, format= h264)

finally:
	camera.stop_recording()
	connection.close()
	client_socket.close()
