import socket
import random
import threading

def main():
	host = '10.1.132.23'
	port = 5507
	s= socket.socket()
	s.bind((host, port))
	s.listen(1)
	print("server started..!!")
	while True:
		c, addr = s.accept()
		print("Connection established from: "+ str(addr))
		c.send("Welcome to the game 'Guess my number!' \n Guess any number of Your choice To start the game! \n Guess between 1 to 50".encode())
		threading.Thread(target = game, args = (c, addr)).start()
		# game(c, addr)

def game(c, addr):
	connect = True
	num = random.randint(1,51)
	count = 1
	while connect:
		data = c.recv(1024).decode()
		if data == "Quit":
			break
		#Guesser implimentation.
		data = int(data)
		print("client "+str(addr)+" guessed: "+str(data))
		if data == num:
			String = "Bingo!! You Guessed correct number in: "+str(count)+" attempts"
			c.send(String.encode())
			connect = False
		elif data < num and data >= 0:
			c.send("Your Guess is  Less than actual number".encode())
		elif data > num and data <= 100:
			c.send("Your Guess is Greater than actual number".encode())
		else:
			c.send("Enter a valid input: ".encode())
		count += 1
	print("server closed from client: "+str(addr))
	c.close()

	

if __name__ == '__main__':
	main()
