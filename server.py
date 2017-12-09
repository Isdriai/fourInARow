import socket



if __name__ == '__main__':
	board=b"BOARD:3,X,X,O,O,X,O,X,O,,X,O,"
	l =[b"VERSION:1.0",
			b"UNKNOWN_LOGIN",
			b"CONFIRM_ACCOUNT",
			b"SUCCESS:ACCOUNT_CREATED",
			b"ROOM:1,tata|toto,ON_GOING",
			b"ROOM:2,titi|tutu,NOT_STARTED",
			b"SUCCESS:Rooms sent",
			b"SUCCESS:2", # faut faire join
			b"COLOR:O",
			b"BEGIN:X",
			board]


	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.bind(('', 4444))
	socket.listen(5)




	# c, addresse = socket.accept()
	# c.recv(2048)
	# c.send(b'blabla')