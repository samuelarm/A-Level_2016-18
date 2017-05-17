# Client 1

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
#host = input("Enter hostname: ")
#port = int(input("Enter port: "))

s.connect((host, port))
print(s.recv(1024).decode())

msg = ""
while msg != "exit":
    msg = input("> ")
    s.send(msg.encode())
    print(s.recv(1024).decode())
s.close
