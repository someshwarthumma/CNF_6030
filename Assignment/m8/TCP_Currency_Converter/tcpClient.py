import socket
def main():
	host = '10.10.9.6'
	port = 1234
	s = socket.socket()
	s.connect((host, port))
	print("Connection established..!!!")
	message = input("enter the text: ")
	while message != 'q':
		s.send(message.encode())
		message = s.recv(1024)
		print("output : "+message.decode())
		message = input("enter the text again: ")
	s.close()

if __name__ == '__main__':
	main()
