from socket import socket, AF_INET, SOCK_STREAM

class Client(object):
	"""docstring for Client"""

	def game(self):
		while self.plateau.winner() == -1:
			while True :
				rec = s.recv(1024)
				if(rec == Protocole.RUN):
					break;
				self.plateau

	def init():
		while True:
			rec = s.recv(1024)
			if(Protocole.receiveEndInit(rec)):
				return
			

	def __init__(self, num, width=Plateau.BOARDWIDTH, height=Plateau.BOARDHEIGHT):
		super(Client, self).__init__()
		self.plateau = Plateau(width, height)
		self.num = num


if __name__ == '__main__':
	s = socket(AF_INET, SOCK_STREAM)
	s.connect(('localhost', 9999))
	s.send(b'hello world')
	s.recv(1024)