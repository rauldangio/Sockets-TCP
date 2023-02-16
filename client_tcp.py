import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	sock.connect(("localhost",8083))
	while True:
		msg = input("Digite sua mensage:").encode()
		sock.send(msg)
		print(sock.recv(4096).decode())
	sock.close()
except:
	print("connection doesnt work")
