# for line in open("data.csv"):
# 	print(line.split(",")[0])

import socket
from threading import *
import os

studentDict = {}
clientLis = []
def main():
	host = '10.10.9.65'
	port = 6009
	s = socket.socket()
	s.bind((host, port))
	s.listen(1)
	print("server started..!")
	for line in open("data.csv"):
		dat = line.split(",")
		lis = []
		msg = dat[1] +" ** "+ dat[2]
		studentDict[dat[0]] = msg
	while True:
		conn, addr = s.accept()
		print("Client connected with IP: "+str(addr))
		Thread(target = Attendance, args = (conn, studentDict)).start()


	# print(studentDict)
def Attendance(conn, studentDict):
	welMsg = "Welcome!! \nPlease provide your rollnumber"
	conn.send(welMsg.encode())
	# print("11")
	count = 10
	while True and count!= 0:
		msg = conn.recv(1024).decode()
		# print(msg)
		data = msg.split(" ")
		# print("data: "+str(data))
		rollnum = 0
		secret = ""
		ans = ""
		# print(data[0])
		if data[0] == "MARK-ATTENDANCE":
			if check(int(data[1])):
				rollnum = int(data[1])
				detail = studentDict.get(str(rollnum))
				details = detail.split(" ** ")
				print(details)
				secret = details[0]
				ans = details[1]
				# ans = Substr(ans, 0, len(ans)-1)
				ans.replace("\n", "")
				reMsg = "SECRETQUESTION-"+secret
				conn.send(reMsg.encode())
			else:
				conn.send("ROLLNUMBER-NOTFOUND".encode())
				print("rollnum not found: "+str(rollnum))
		elif data[0] == "SECRETANSWER":
			print(data[1] +" == "+ans)
			if str(data[1]) == str(ans):
				conn.send("ATTENDANCE SUCCESS".encode())
				print("success for rollnum: "+str(rollnum))
			else:
				print("failure for rollnum: "+str(rollnum))
				conn.send("ATTENDANCE FAILUE".encode())
				




def check(roll):
	for line in open("data.csv"):
		if int(line.split(",")[0]) == roll:
			return True
	return False


if __name__ == '__main__':
	main()
