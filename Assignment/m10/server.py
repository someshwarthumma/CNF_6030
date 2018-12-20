import socket
from threading import *
import os
import signal
import time
clientDict = {}
s = socket.socket()
def main():
    host = '10.10.9.65'
    port = 1249
    s.bind((host, port))
    s.listen(10)
    print("Server started..! at: "+str(host))
    Thread(target = admin, args = ()).start()
    while True:
        conn, addr = s.accept()
        print("client entering his name at IP: "+str(addr))
        welcomeMsg = "Welcome to the Group Chat! \nPlease enter your name to start the chatting: "
        conn.send(welcomeMsg.encode())
        if conn not in clientDict:
            clientDict[conn] = "user"
            Thread(target = Messenger, args = (conn, "user")).start()
        else:
            conn.send("Oops!!! \n Error Occured, Try after some time".encode())
            clientDict.pop(conn)
    s.close()

def Messenger(conn, UserName):
    UserName = conn.recv(1024).decode()
    clientDict[conn] = UserName
    Broadcast(conn, UserName+" joined the group chat!")
    try:
        while conn in clientDict:
            msg = conn.recv(1024).decode()
            if msg == "QUIT":
                msg = UserName+ " exited the chat !"
                Broadcast(conn, msg)
                conn.send("You successfully exited your chat,Thank you ! ".encode())
                clientDict.pop(conn)
                check()
                return 1
            else:
                msg = UserName + ": " + msg+"  "
                Broadcast(conn,msg)
    except:
        clientDict.pop(conn)
        conn.send("Oops ! Error Occured, please Connect again ! ".encode())

def check():
    if (active_count() == 3):
        Notifier("Waiting to close the group chat, no member online.")
        time.sleep(10)
        if (active_count() == 3):
            os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
def admin():
    while True:
        msg = input("-> ")
        if not msg:
            continue
        if msg == "QUIT":
            Notifier("Server will be shut down in 3 seconds! ")
            time.sleep(3)
            print("server closed")
            os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
            break
        else:
            Notifier(msg)


def Broadcast(conn, msg):
    keys = clientDict.keys()
    print(msg)
    for connection in keys:
        if conn != connection:
            connection.send(msg.encode())


def Notifier(msg):
    msg = "Admin: "+ msg+ " "
    keys = clientDict.keys()
    print(msg)
    for connection in keys:
        connection.send(msg.encode())



if __name__ == '__main__':
    main()