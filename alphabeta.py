def potentialsMove(plateau):
    mouvements = []
    for x in xrange(plateau.w):
        if plateau.board[x][0] == 0:
            mouvements.append(x)
    return mouvements

def evaluation(board, joueur):
    _, tuile = joueur
    
    score = horizontale(board, tuile)
    score += verticale(board, tuile)
    score += diagonaleBasse(board, tuile)
    score += diagonaleHaute(board, tuile)

    return score


def horizontale(board, tuile):
    tot = 0
    for row in range(len(board[0])):
        for col in range(len(board)-3):
            if board[col][row] == tuile:
                if board[col+1][row] == tuile:
                    if board[col+2][row] == tuile:
                        if board[col+3][row] == tuile:
                            tot += 10000
                        else:
                            tot += 1000
                    else:
                        tot += 50
                else:
                    tot += 5
    return tot

def verticale(board, tuile):
    tot = 0
    for col in range(len(board)):
        for row in range(len(col)-3):
            if board[col][row] == tuile:
                if board[col][row+1] == tuile:
                    if board[col][row+2] == tuile:
                        if board[col][row+3] == tuile:
                            tot += 10000
                        else:
                            tot += 1000
                    else:
                        tot += 50
                else:
                    tot += 5
    return tot

# diagonale basse = \
def diagonaleBasse(board, tuile):
    tot = 0
    for col in range(len(board)-3):
        for row in range(len(col)-3):
            if board[col][row] == tuile:
                if board[col+1][row+1] == tuile:
                    if board[col+2][row+2] == tuile:
                        if board[col+3][row+3] == tuile:
                            tot += 10000
                        else:
                            tot += 1000
                    else:
                        tot += 50
                else:
                    tot += 5
    return tot


# diagonale haute = /
def diagonaleHaute(board, tuile):
    tot =0 
    for col in range(len(board)-3):
        for row in range(3,len(col)):
            if board[col][row] == tuile:
                if board[col+1][row-1] == tuile:
                    if board[col+2][row-2] == tuile:
                        if board[col+3][row-3] == tuile:
                            tot += 10000
                        else:
                            tot += 1000
                    else:
                        tot += 50
                else:
                    tot += 5
    return tot

# joueur = (Boolean, tuile)
# le boolean dit si c'est un etage ou c'est le joueur qui joue
# la tuile c'est pr la fonction
# d'evaluation repéré les coups sur le plateau
def alphabeta(plateau, alpha, beta, prof, joueur):
    tourMax, tuile = joueur
    if prof == 0:
        evaluation(plateau.board, joueur)
    else
        for move in potentialsMove(plateau):
            copie = plateau.copy()
            copie.makeMove(move)
            val = -alphabeta(copie, -beta, -alpha, prof-1, (not tourMax,tuile))
            if val > meilleur:
                meilleur = val
                if meilleur > alpha:
                    alpha = meilleur
                    if alpha >= beta:
                        return meilleur
