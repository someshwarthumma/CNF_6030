import socket
from threading import *


def main():
	host = '10.1.132.23'
	port = 6010
	s = socket.socket()
	s.connect((host, port))
	welcomeMsg = s.recv(1024).decode()
	print(welcomeMsg)
	# Thread(target = sender, args = ())
	msg = input("RollNum: ")
	msg = "MARK-ATTENDANCE "+msg
	# print(msg)
	s.send(msg.encode())
	while True:
		message = s.recv(1024).decode()
		
		if message.split("-")[0] == "SECRETQUESTION":
			dat = message.split("-")[1]
			print("Secret Quention: "+dat)
			inp = input()
			inp = "SECRETANSWER "+inp
			# print(inp)
			s.send(inp.encode())
		elif message.split("-")[0] == "ATTENDANCE SUCCESS":
			print("ATTENDANCE SUCCESS")
			break;
		elif message.split("-")[0] == "ATTENDANCE FAILUE":
			print("ATTENDANCE FAILUE")
		else:
			print(message)

		


if __name__ == '__main__':
	main()