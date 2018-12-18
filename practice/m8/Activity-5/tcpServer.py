import socket
def main():
	host = '10.10.9.65'
	port = 2000
	s = socket.socket()
	s.bind((host, port))
	s.listen(1)
	print("Server started....!!!!")
	conn, addr = s.accept()
	while True:
		data = conn.recv(1024)
		if not data:
			break
		print("recieved data: "+str(data.decode()))
		data = str(data.decode()).upper()
		print("sending data: "+str(data))
		conn.send(data.encode())
	conn.close()

if __name__ == '__main__':
	main()
