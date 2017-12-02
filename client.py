from socket import socket, AF_INET, SOCK_STREAM

class Client(object):
	"""docstring for Client"""

	def tourJoueur(self):
		move = int(input("Rentrez le num du move ( entre 0 et 7 exclu)")[0])
		self.plateau.makeMove(move)
		Protocole.sendMove(move)

	def tourEnnemi(self):
		move = Protocole.receiveMove()
		self.plateau.makeMove(move)

	def game(self):
		
		ordre=[]

		if(Protocole.begin() == self.color):
			ordre=[tourJoueur, tourEnnemi]
		else
			ordre=[tourEnnemi, tourJoueur]

		self.plateau.drawBoard()
		while self.plateau.winner():
			board = Plateau.translate(Protocole.receiveBoard())
			if (not self.plateau.verif(board)):
				self.plateau = board
			ordre[0](self)
			self.plateau.drawBoard()
			ordre[1](self)
			self.plateau.drawBoard()
				

	def init(self):
		Protocole.sendVersion()
		login = input("Rentrez votre LOGIN")
		Protocole.sendLogin(login)
		if(Protocole.receiveAnswerLogin()):
			password = input("Rentrez votre password")
			Protocole.sendPassword(password)

		rooms = Protocole.receiveRooms()
		drawRooms()
		room = input("voulez vous créer (c) ou rejoindre (r)")[0]
		if(room == 'c'):
			Protocole.createRoom()
		else(room == 'r'):
			choix = input("rentrez la room sélectionnée")
			Protocole.joinRoom()
			Protocole.receiveAnswerRoom()
		couleurs = ['x', 'o']
		col = int(input("choisissez couleur ( 0 pour 'x' ou 1 pour 'o')")[0])
		self.color = Protocole.initColor(couleurs, couleurs[col])

	def __init__(self, num, width=Plateau.BOARDWIDTH, height=Plateau.BOARDHEIGHT):
		super(Client, self).__init__()
		self.s = socket(AF_INET, SOCK_STREAM)
		self.s.connect(('localhost', 9999))
		self.plateau = Plateau(width, height)
		self.color = ''
		self.init()
		self.game()


if __name__ == '__main__':
	s = socket(AF_INET, SOCK_STREAM)
	s.connect(('localhost', 9999))
	s.send(b'hello world')
	s.recv(1024)