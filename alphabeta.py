import pdb
import copy

def printb(board):
    for row in range(len(board[0])):
        for col in range(len(board)):
            print(board[row][col],end=' ')
        print()

def potentialsMove(board):
    mouvements = []
    for x in range(len(board)):
        if board[x][0] == "":
            mouvements.append(x)
    return mouvements

def joueurActuel(joueurs):
    mx, joueursPossibles = joueurs
    return joueursPossibles[int(not mx)]

def evaluation(jeu, joueurs):
    mx, joueursPossibles= joueurs
    joueur = joueursPossibles[int(not mx)]
    autreJoueur = joueursPossibles[int(mx)]
    #score = horizontale(board, tuile)
    #score += verticale(board, tuile)
    #score += diagonaleBasse(board, tuile)
    #score += diagonaleHaute(board, tuile)
    score = 0 

    if joueurGagne(jeu, joueur):
        score = 1;
    
    elif joueurGagne(jeu, autreJoueur):
        score = -1;

    return score

def joueurGagne(board, tile):
    BOARDWIDTH = len(board)
    BOARDHEIGHT = len(board[0])
    # check horizontal spaces
    for y in range(BOARDHEIGHT):
        for x in range(BOARDWIDTH - 3):
            if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                return True

    # check vertical spaces
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT - 3):
            if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                return True

    # check / diagonal spaces
    for x in range(BOARDWIDTH - 3):
        for y in range(3, BOARDHEIGHT):
            if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                return True

    # check \ diagonal spaces
    for x in range(BOARDWIDTH - 3):
        for y in range(BOARDHEIGHT - 3):
            if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                return True

    return False

def makeMove(board, player, column):
    BOARDHEIGHT = BOARDHEIGHT = len(board[0])
    for y in range(BOARDHEIGHT-1, -1, -1):
        if board[column][y] == "":
            board[column][y] = player
            return


x=0
# joueur est un booleen ( true c'est le joueur )
def alphabeta(board, alpha, beta, joueurs, prof):
    global x
    x+=1
    mx, joueursPossibles= joueurs
    mouvements = potentialsMove(board)
    if prof == 0 or mouvements == []:
        return (evaluation(board, joueurs), -1)
    val = 0
    if not mx:
        val = 100000
        for succ in mouvements:
            copie = copy.deepcopy(board)
            makeMove(copie, joueurActuel(joueurs), succ)
            val = min(val, alphabeta(copie, alpha, beta, (not mx,joueursPossibles) , prof-1)[0])
            if alpha>=val:
                return (val, succ)
            beta = min(beta, val)
    else:
        val = -100000
        for succ in mouvements:
            copie = copy.deepcopy(board)
            makeMove(copie, joueurActuel(joueurs), succ)
            val = max(val, alphabeta(copie, alpha, beta, (not mx,joueursPossibles), prof-1)[0])
            if val>=beta:
                return (val, succ)
    return (val, -2)


# b = [["","X","O","O"],["","","X","O"],["","","O","X"],["","","",""]]
# b =[["","O","X","X"],["","O","X","O"],["","","O","X"],["","","X","O"],["","","X","O"]]