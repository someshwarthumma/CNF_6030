import socket
import threading
clientDict = {}
s = socket.socket()
Flag = True
def main():
	host = '10.10.9.65'
	port = 1236
	s.bind((host, port))
	s.listen(20)
	print("Server started..! at: "+str(host))
	threading.Thread(target = admin, args = ()).start()
	while Flag:
		try:
			conn, addr = s.accept()
			print("client at entering his name at IP: "+str(addr))
			welcomeMsg = "Welcome to the Group Chat! \nPlease enter your name to start the chatting: "
			conn.send(welcomeMsg.encode())
			UserName = conn.recv(1024).decode()
			print(UserName+" joined the group chat!")
			if conn not in clientDict:
				clientDict[conn] = UserName
				threading.Thread(target = Messenger, args = (conn, UserName)).start()
			else:
				conn.send("Oops!!! \n Error Occured, Try after some time".encode())
				clientDict.pop(conn)
		except:
			print("server closed")
			break
	s.close()

def Messenger(conn, UserName):
	
	try:
		while conn in clientDict:
			msg = conn.recv(1024).decode()
			if msg == "QUIT":
				clientDict.pop(conn)
				conn.send("You successfully exited your chat,Thank you ! ".encode())
			else:
				msg = UserName + ": " + msg
				Broadcast(conn,msg)
	except:
		clientDict.pop(conn)
		conn.send("Oops ! Error Occured, please Connect again ! ".encode())
	s.close()


def admin():
	print("A1")
	# print("PT 1")
	while True:
		msg = input("-> ")
		if not msg:
			continue
		if msg == "QUIT":
			Notifier("Group chat closed by admin")
			Flag = False
			s.close()
			break
		else:
			if not msg:
				continue
			else:
				Notifier(msg)


def Broadcast(conn, msg):
	keys = clientDict.keys()
	print(msg)
	for connection in keys:
		if conn != connection:
			connection.send(msg.encode())
def Notifier(msg):
	keys = clientDict.keys()
	print(msg)
	for connection in keys:
		connection.send(msg.encode())



if __name__ == '__main__':
	main()