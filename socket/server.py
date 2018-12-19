#!/usr/bin/env python36

import socket
import threading
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",9999))

s.listen(5)

print("Waiting for connection...")

def tcplink(sock,addr):
	print("Accept new connection from %s:%s..." %addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode("utf-8") == 'exit':
			break
		sock.send(("hello,%s!" %data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print("connection from %s:%s closed" %addr)

while True:
        sock,addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()

