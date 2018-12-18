import socket

def main():
	host = '10.10.9.65'
	port = 5522
	s= socket.socket()
	s.bind((host, port))
	s.listen(1)
	
	c, addr = s.accept()
	print()
	print("Connection established: "+ str(addr))
	print("server started..!!")
	while True:
		print("server started..!!")
		data = c.recv(1024).decode()
		if not data:
			break
		result = str(converter(data))
		c.send(result.encode())
	c.close()
	# 1 Dollar = 67 INR
	# 1 Dollar =0.75 Pounds
	# 1 Dollar = 113.41 Yen

def converter(data):
	lis = []
	lis = data.split(" ")
	value = float(lis[2])
	dest = lis[4]
	if lis[1]== "INR":
		if dest == "INR":
			return value
		if dest == "Dollar":
			return value*(1/67)
		if dest == "Yen":
			return value*(113.41/67)
		if dest == "Pounds":
			return value*(0.75/67)
	if lis[1] == "Dollar":
		if dest == "INR":
			return value*67
		if dest == "Dollar":
			return value
		if dest == "Pounds":
			return value*0.75
		if dest == "Yen":
			return value*113.41
	if lis[1] == "Pounds":
		if dest == "INR":
			return value*(67/0.75)
		if dest == "Dollar":
			return value*(1/0.75)
		if dest == "Pounds":
			return value
		if dest == "Yen":
			return value*(113.41/0.75)
	if lis[1] == "Yen":
		if dest == "INR":
			return value*(67/113.41)
		if dest == "Dollar":
			return value*(1/113.41)
		if dest == "Pounds":
			return value*(0.75/113.41)
		if dest == "Yen":
			return value

if __name__ == '__main__':
	main()
