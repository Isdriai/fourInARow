import random
import copy
import sys

class Plateau(object):
	"""docstring for Plateau"""

	BOARDWIDTH = 7
	BOARDHEIGHT = 6

	def drawBoard(self):
	    print()
	    print(' ', end='')
	    for x in range(1, BOARDWIDTH + 1):
	        print(' %s  ' % x, end='')
	    print()

	    print('+---+' + ('---+' * (BOARDWIDTH - 1)))

	    for y in range(BOARDHEIGHT):
	        print('|   |' + ('   |' * (BOARDWIDTH - 1)))

	        print('|', end='')
	        for x in range(BOARDWIDTH):
	            print(' %s |' % self.plateau[x][y], end='')
	        print()

	        print('|   |' + ('   |' * (BOARDWIDTH - 1)))

	        print('+---+' + ('---+' * (BOARDWIDTH - 1)))
	        

	def makeMove(self, player, column):
	    for y in range(BOARDHEIGHT-1, -1, -1):
	        if self.plateau[column][y] == 0:
	            self.plateau[column][y] = player
	            return

	def possiblesMove(self):
		possible = []
		for move in range(BOARDWIDTH):
			if self.plateau[move][0] == 0:
				possible.append(move)
		return possible

	def addPlayer(self, nplayer):
		for mark in self.player:
			if(mark == nplayer):
				''' Si l'entier représentant le joueur est 
				deja utilisé, on ne le rajoute pas '''
				return
		self.player.append(nplayer)

	def __init__(self, width=BOARDWIDTH, height=BOARDHEIGHT):
		self.plateau = [[0] * width ] * height
		self.player=[]