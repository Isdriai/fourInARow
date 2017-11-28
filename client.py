from socket import socket, AF_INET, SOCK_STREAM

if __name__ == '__main__':
	s = socket(AF_INET, SOCK_STREAM)
	s.connect(('localhost', 9999))
	s.send(b'hello world')
	s.recv(1024)