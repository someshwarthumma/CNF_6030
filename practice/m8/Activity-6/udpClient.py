import socket

def main():
	host = '10.10.9.65'
	port = 3119
	server = ('10.10.9.65', 3118)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	message = input("enter the input: ")
	while message != 'q':
		s.sendto(message.encode(), server)
		data, addr = s.recvfrom(1024)
		print("recieved from server: "+str(data.decode()))
		message = input("enter again input: ")
	s.close()
if __name__ == '__main__':
	main()