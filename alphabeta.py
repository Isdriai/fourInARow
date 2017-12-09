def potentialsMove(board):
    mouvements = []
    for x in xrange(board.w):
        if board[x][0] == 0:
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

# joueur est un booleen ( true c'est le joueur )
def alphabeta(board, a, b, joueur, prof):
    if prof == 0:
        return evaluation(board, joueur)
    alpha = a 
    beta = b 
    if joueur:
        for succ in potentialsMove(board):
            copie = board.copy(0)
            copie.makeMove(succ)
            beta = min(beta, alphabeta(copie, alpha, beta, not joueur, prof-1))
            if alpha>=beta:
                return alpha
        return beta
    else:
        for succ in potentialsMove(board):
            copie = board.copy(0)
            copie.makeMove(succ)
            alpha = max(alpha, alphabeta(copie, alpha, beta, not joueur, prof-1))
            if alpha>=beta:
                return beta
        return alpha