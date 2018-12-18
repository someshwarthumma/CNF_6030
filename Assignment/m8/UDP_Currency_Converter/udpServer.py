import socket

def main():
	host = '10.10.9.65'
	port = 2562
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	print("server started .... !!!!")
	while True:
		data, addr = s.recvfrom(1024)
		print("Connection started from: "+str(addr))
		data = data.decode()
		result = str(converter(str(data))).encode()
		s.sendto(result, addr)
	s.close()

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



