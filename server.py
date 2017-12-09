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
			board,
			b"MOVE"]


	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.bind(('', 4444))
	socket.listen(5)




	# c, addresse = socket.accept()
	# c.recv(2048)

	'''

	svetlana@svetlana-X550CC:~/Documents/fourInARow$ python3 -i server.py 
c, addresse = socket.accept()
c.recv(2048)
b'VERSION:1.0'
c.send(l[0])
11
c.recv(2048)
b'LOGIN:coucou'
c.send(l[1])
13
c.recv(2048)
b'CREATE_ACCOUNT:coucou,PASSWORD:coucou'
c.send(l[2])
15
c.recv(2048)
b'CONFIRM_ACCOUNT:coucou,PASSWORD:coucou'
c.send(l[3])
23
c.send(l[4])
25
c.send(l[5])
28
c.send(l[6])
18



c.initRoom(2)


c.recv(2048)
b'ASK_ROOMSSELECT_ROOM:2'
c.send(l[7])
9


c.initColor()



c.send(l[8])
7
c.send(l[9])
7


board = c.getBoard()


c.send(l[10])
29

'''