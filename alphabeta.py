fonction ALPHABETA(P, A, B) /* A < B */
   si P est une feuille alors
       retourner la valeur de P
   sinon
       Meilleur = –INFINI
       pour tout enfant Pi de P faire
           Val = -ALPHABETA(Pi,-B,-A)
           si Val > Meilleur alors
               Meilleur = Val
               si Meilleur > A alors
                   A = Meilleur
                   si A ≥ B alors
                       retourner Meilleur
                   finsi
               finsi
           finsi 
       finpour 
       retourner Meilleur
   finsi
fin

def potentialsMove(board):
  mouvements = []
  for x in xrange(board.w):
    if board.board[x][0] == 0:
      mouvements.append(x)
  return mouvements


def alphabeta(board, alpha, beta, prof):
  if p == 0:
    evaluation(board)
  else
    meilleur = -float("inf")
    for  in board.:
      pass