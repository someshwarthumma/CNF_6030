import socket
import random
import threading

def main():
	host = '10.10.9.65'
	port = 5501
	s= socket.socket()
	s.bind((host, port))
	s.listen(1)
	print("server started..!!")
	while True:
		c, addr = s.accept()
		print("Connection established from: "+ str(addr))
		c.send("Welcome to the Game! Guess any number of Your choice To start the game! ".encode())
		threading.Thread(target = game, args = (c, addr)).start()
		# game(c, addr)

def game(c, addr):
	connect = True
	num = random.randint(1,101)
	while connect:
		data = c.recv(1024).decode()
		if data == "Quit":
			break
		#Guesser implimentation.
		data = int(data)
		if data == num:
			c.send("Bingo!! You Guessed correct.".encode())
			connect = False
		elif data < num and data >= 0:
			c.send("Your Guess is  Less than actual number".encode())
		elif data > num and data <= 100:
			c.send("Your Guess is Greater than actual number".encode())
		else:
			c.send("Enter a valid input: ".encode())
	print("server closed from client: "+str(addr))
	c.close()

	

if __name__ == '__main__':
	main()
