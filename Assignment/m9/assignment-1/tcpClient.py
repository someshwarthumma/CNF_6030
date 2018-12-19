import socket
def main():
	host = '10.10.9.65'
	port = 5501
	s = socket.socket()
	s.connect((host, port))
	print("Connection established..!!!")
	print(s.recv(1024).decode())
	message = input("enter the text: ")
	try:
		while message != 'q':
			s.send(message.encode())
			message = s.recv(1024)
			print("output : "+message.decode())
			if message.decode() == "Bingo!! You Guessed correct.":
				break
			message = input("Input: ")

		print("Client closed")
		s.close()
	except:
		print("Client closed")
		s.close()

if __name__ == '__main__':
	main()
