import io
import socket
import struct

# RUN THIS ON THE COMPUTER

server_socket = socket.socket()
server_socket.bind(('10.0.0.60', 8000))
server_socket.listen()

connection = server_socket.accept()[0].makefile('r')
try:
	while True:
		image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
		if not image_len:
			break
		image_stream = io.BytesIO()
		image_stream.write(connection.read(image_len))

		image_stream.seek(0)
		image = Image.open(image_stream)
		print('Image is %dx%d' % image.size)
		image.verify()
		print('Image is verified')
finally:
	connection.close()
	server_socket.close()
