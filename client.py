from protocole import Protocole

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
        else:
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
           
    def drawRooms(self):
        for room in self.rooms:
            print(room)   

    def __init__(self):
        self.protocole = Protocole()
        tries = 0
        self.protocole.sendVersion()
        #self.protocole.receiveVersion()


        login = input("[?]Enter your login: ")
        self.protocole.sendLogin(login)
        rcv = self.protocole.receive()
        
        if rcv == self.protocole.ASK_PASSWORD:
            while(1):
                if tries == 2:
                  raise Exception("[!]Error three bad login attempts") 
                password = input("[?]Enter your password: ")
                self.protocole.sendPassword(password)
                rcv = self.protocole.receive()
                if rcv == self.protocole.SUCCESS_AUTHENTICATED: # à rajouer
                    break
                else:
                  tries += 1
        
        elif rcv == self.protocole.UNKNOWN_LOGIN:
            password = input("[?]Enter your password: ")
            self.protocole.registerUser(login, password)
            if self.protocole.receive() == self.protocole.CONFIRM_ACCOUNT:
                confirm_password = input("[?]Confirm your password: ")
                self.protocole.confirmUser(login, confirm_password)
                if self.protocole.receive() == self.protocole.ACCOUNT_CREATED:
                    print("[*]Your account has been created")
                else:
                    print(self.protocole.receive())
                    raise Exception("[!]The password didn't match")
            else:
                raise Exception("[!]Server don't ask to confirm credentials")
        else:
            raise Exception("[!]Can't connect to the serveur")
        self.rooms = self.protocole.receiveRooms()
        print("on va draw")
        self.drawRooms()
        room = input("voulez vous créer (c) ou rejoindre (r)\n")[0]
        if(room == 'c'):
            self.protocole.createRoom()
            if self.protocole.receiveAnswerRoom() == -1:
                raise Exception("Le serveur n'a pas reussi a créer une salle")
        elif(room == 'r'):
            choix = input("rentrez la room sélectionnée\n")
            self.protocole.joinRoom(choix)
            if self.protocole.receiveAnswerRoom() == -1:
                raise Exception("Le serveur n'a pas reussi a trouver la salle")
        print("on est rentré")
        col = self.protocole.receiveColor()
        if col == "":
            raise Exception("Le serveur n'a pas envoyé la couleur du joueur")
        self.color = col
        print("wesh")
        beg = self.protocole.receiveBegin()
        if beg == "":
            raise Exception("Le serveur n'a pas envoyé la couleur qui commencait")
        self.begin = beg

if __name__ == '__main__':
    c = Client()
