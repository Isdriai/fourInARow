import random
import copy
import sys

class Plateau(object):
	"""docstring for Plateau"""

	BOARDWIDTH = 7
	BOARDHEIGHT = 6

	COLORS = ['x', 'o']

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

	def winner(self):
	for tile in COLORS:
	    # check horizontal spaces
	    for y in range(BOARDHEIGHT):
	        for x in range(BOARDWIDTH - 3):
	            if self.plateau[x][y] == tile and self.plateau[x+1][y] == tile and self.plateau[x+2][y] == tile and self.plateau[x+3][y] == tile:
	                return tile

	    # check vertical spaces
	    for x in range(BOARDWIDTH):
	        for y in range(BOARDHEIGHT - 3):
	            if self.plateau[x][y] == tile and self.plateau[x][y+1] == tile and self.plateau[x][y+2] == tile and self.plateau[x][y+3] == tile:
	                return tile

	    # check / diagonal spaces
	    for x in range(BOARDWIDTH - 3):
	        for y in range(3, BOARDHEIGHT):
	            if self.plateau[x][y] == tile and self.plateau[x+1][y-1] == tile and self.plateau[x+2][y-2] == tile and self.plateau[x+3][y-3] == tile:
	                return tile

	    # check \ diagonal spaces
	    for x in range(BOARDWIDTH - 3):
	        for y in range(BOARDHEIGHT - 3):
	            if self.plateau[x][y] == tile and self.plateau[x+1][y+1] == tile and self.plateau[x+2][y+2] == tile and self.plateau[x+3][y+3] == tile:
	                return tile

    return -1

	def __init__(self, width=BOARDWIDTH, height=BOARDHEIGHT):
		self.plateau = [[0] * width ] * height
