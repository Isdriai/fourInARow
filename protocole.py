from socket import socket, AF_INET, SOCK_STREAM
from time import sleep
import re

class Protocole(object):

    SERVER_IP = "edznux.fr"
    SERVER_SOCKET = 4444
    VERSION = "VERSION"
    NB_VERSION = "1.0"
    LOGIN = "LOGIN"
    UNKNOWN_LOGIN = "UNKNOWN_LOGIN"
    CREATE_ACCOUNT = "CREATE_ACCOUNT"
    CONFIRM_ACCOUNT = "CONFIRM_ACCOUNT"
    PASSWORD = "PASSWORD"
    ASK_PASSWORD = "ASK_PASSWORD"
    WRONG_PASSWORD = "ERROR:WRONG_PASSWORD"
    SUCCESS_AUTHENTICATED = "SUCCESS:AUTHENTICATED"
    ACCOUNT_CREATED = "SUCCESS:ACCOUNT_CREATED"
    SUCCESS_ROOMS = "SUCCESS:Rooms sent"
    EMPTY_ROOMS = "ERROR:no rooms found"
    CREATE_ROOM = "CREATE_ROOM"
    CREATE_ROMM_ERROR = "ERROR:Cannot create room"
    SELECT_ROOM = "SELECT_ROOM"
    SUCCESS_ROOM = "SUCCESS"
    ERROR_ROOM = "ROOM does not exist"
    COLOR = "COLOR"
    PAWN = ['X', 'O', '=']
    ERROR_COLOR = "ERROR:Color not available"
    BEGIN = "BEGIN"
    ERROR_MOVE = "ERROR:Impossible move"
    QUIT_ROOM = "QUIT_ROOM"
    QUIT_ROOM_SUCCESS = "SUCCESS:You left the room"
    QUIT_ROOM_ERROR = "ERROR:Can't left the room"
    GAME_FINISHED = "GAME_FINISHED"
    ASK_LIST = "ASK_LIST"
    LIST = "LIST"
    QUERY_LOGIN = "QUERY_LOGIN"
    LOGIN_INFO = "LOGIN_INFO"
    QUIT_SERVER = "QUIT_SERVER"

    def __init__(self):
        self.sock = socket(AF_INET,  SOCK_STREAM)
        self.sock.connect((self.SERVER_IP, self.SERVER_SOCKET))

    def sendMove(self):
        pass

    def receiveMove(self):
        pass

    def receive(self):
        return self.sock.recv(1024).decode('UTF8')

    def receiveBoard(self):
        pass

    def sendVersion(self):
        ''' send actual version  to the server  and parse  response '''
        self.sock.send("{}:{}".format(self.VERSION, self.NB_VERSION).encode('UTF8'))
        return self.sock.recv(1024).decode('UTF8') == "{}:{}".format(self.VERSION, self.NB_VERSION)

    def receiveVersion(self):
        print("receive version")
        rcv = self.sock.recv(1024).decode('UTF8')
        print("rcv  " + rcv)
        parties = rcv.split(':')
        if self.VERSION == parties[0]:
            return parties[1]
        return ""

    def sendLogin(self, login):
        self.sock.send("{}:{}".format(self.LOGIN, login).encode('UTF8'))

    def sendPassword(self, password):
        self.sock.send("{}:{}".format(self.PASSWORD, password).encode('UTF8'))

    def registerUser(self, login, password):
        self.sock.send("{}:{},{}:{}".format(self.CREATE_ACCOUNT, login, self.PASSWORD, password).encode('UTF8'))

    def confirmUser(self, login, confirm_password):
        self.sock.send("{}:{},{}:{}".format(self.CONFIRM_ACCOUNT, login, self.PASSWORD, confirm_password).encode('UTF8'))

    def receiveRooms(self):
        print("zoeighozugeoz")
        rcv = self.sock.recv(1024).decode('UTF8')
        print("wesh")
        if rcv == self.EMPTY_ROOMS:
            print('[*] No rooms was been found')
        else:
            while not self.SUCCESS_ROOMS in rcv :
                rcv += self.sock.recv(1024).decode('UTF8')
        print(rcv)
        new_rcv=re.sub(self.SUCCESS_ROOMS, "", rcv)
        print("renvoi")

        return re.findall(r"(ROOM:[0-9]*,[0-9a-zA-Z_|]*,[0-9]*.[0-9]*)", new_rcv)

    def createRoom(self):
        self.sock.send("{}".format(self.CREATE_ROOM).encode('UTF8'))

    def joinRoom(self, nb):
        self.sock.send("{}:{}".format(self.SELECT_ROOM, nb).encode('UTF8'))

    def receiveAnswerRoom(self):
        rcv = self.sock.recv(1024).decode('UTF8')
        parties = rcv.split(':')
        if self.SUCCESS_ROOM == parties[0]:
            num = parties[1]
            if num.isdigit():
                return int(num)
        return -1

    def receiveColor(self):
        rcv = self.sock.recv(1024).decode('UTF8')
        parties = rcv.split(':')
        if self.COLOR == parties[0]:
            return parties[1]
        return ""

    def receiveBegin(self):
        rcv = self.sock.recv(1024).decode('UTF8')
        parties = rcv.split(':')
        if self.BEGIN == parties[0]:
            return parties[1]
        return ""