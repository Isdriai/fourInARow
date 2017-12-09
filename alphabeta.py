def potentialsMove(board):
    mouvements = []
    for x in xrange(board.w):
        if board.board[x][0] == 0:
            mouvements.append(x)
    return mouvements

def evaluation(board):
    

def alphabeta(board, alpha, beta, prof):
    if p == 0:
        evaluation(board)
    else
        meilleur = -float("inf")
        for move in potentialsMove(board):
            copie = board.copy()
            copie.makeMove(move)
            val = -alphabeta(copie, -beta, -alpha)
            if val > meilleur:
                meilleur = val
                if meilleur > alpha:
                    alpha = meilleur
                    if alpha >= beta:
                        return meilleur
