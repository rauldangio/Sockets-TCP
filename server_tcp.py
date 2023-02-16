import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('0.0.0.0', 8083))
server.listen(5)

socket_client, client = server.accept()
while True:
	data = client[0] + ": " + socket_client.recv(1024).decode()
	if data == "mensagem secreta\n":
		socket_client.send("mensagem ultra rara".encode())
	print(data + "\n")
socket_client.close()
