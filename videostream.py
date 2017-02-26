import io
import socket
import struct
import time
import picamera

framesize = (640,480)
client_socket = socket.socket()
client_socket.connect(('192.168.2.7', 8000))

connection = client_socket.makefile('wb')
try:
        with picamera.PiCamera() as camera:
                camera.resolution = framesize
                camera.start_preview()
                time.sleep(2)

                start = time.time()
                stream = io.BytesIO()
                for foo in camera.capture_continuous(stream, 'jpeg'):

                        connection.write(struct.pack('<L', stream.tell()))
                        connection.flush()

                        stream.seek(0)
                        connection.write(stream.read())

                        if time.time() - start < 30:
                                break
                        stream.seek(0)
                        stream.trunkate()

                connection.write(struct.pack('<L', 0))
finally:
        connection.close()
        client_socket.close()
