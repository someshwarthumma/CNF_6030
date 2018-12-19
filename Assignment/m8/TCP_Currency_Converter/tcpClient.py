import socket
def main():
	host = '10.1.132.23'
	port = 5522
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
