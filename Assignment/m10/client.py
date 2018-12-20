import socket
import threading
s = socket.socket()
def main():
	host = '10.10.9.65'
	port = 1236
	
	s.connect((host, port))
	welcomeMsg = s.recv(1024).decode()
	print(welcomeMsg)
	s.send(input().encode())
	threading.Thread(target = sender, args = ()).start()
	while True:
		try:
			msg = s.recv(1024).decode()
			if not msg:
				continue
			print(msg)
		except:
			break
	s.close()
def sender():
	while True:
		msg = input("->")
		if not msg:
			continue
		s.send(msg.encode())
		if msg == "QUIT":
			break
	s.close()

if __name__ == '__main__':
	main()