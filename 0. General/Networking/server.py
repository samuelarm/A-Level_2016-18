# Server

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

while True:
    print("Server hostname:", host)
    print("Waiting for connection...")
    s.listen(5)

    c, addr = s.accept()
    print("Connection established from", addr)
    c.send("Connection successful!".encode())

    msg = ""
    while msg != "exit":
        msg = c.recv(1024).decode()
        print(msg)
        c.send("Message received".encode())
    c.close()
