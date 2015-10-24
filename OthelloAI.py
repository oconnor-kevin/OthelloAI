#!/usr/bin/python

import numpy as np
import json
import sys
import random

## Saving command line arguments
# json_string = json.loads(argv[0])

# mycolor = argv[1]


## Saving command line arguments
json_string = json.loads(sys.argv[2])
mycolor = sys.argv[4]

squ = json_string['squares']


testBoard = np.matrix([['-', '-', '-', '-', 'w', '-', '-', '-'],
                   ['w', '-', '-', 'w', '-', '-', '-', 'b'],
                   ['-', '-', 'w', 'w', '-', '-', 'w', 'w'],
                   ['b', '-', '-', '-', '-', 'w', '-', 'w'],
                   ['-', '-', '-', '-', 'w', '-', '-', 'w'],
                   ['-', '-', '-', 'w', '-', '-', '-', 'w'],
                   ['-', '-', 'w', '-', '-', '-', '-', 'w'],
                   ['-', 'b', 'w', 'w', '-', '-', '-', '-']])


class OthelloAI:
	def __init__(self, color):
		self.color = color

	def check_if_valid(self, board, row, col, myColor):
		size = 8
		myC = 'w'
		hisC = 'b'
		if myColor == 'black':
			myC = 'b'
			hisC = 'w'

		# check to the right
		if (col < size -2):
			if board[row, col+1] == hisC:
				for i in range(col+2, size):
					if board[row,i] == myC:
						return True
					elif board[row,i] == '-':
						break

		# check to the left
		if (col > 1):
			if (board[row,col-1] == hisC):
				for i in range(col-2, -1, -1):
					if board[row,i] == myC:
						return True
					elif board[row,i] == '-':
						break

		# check up
		if (row > 1):
			if board[row-1, col] == hisC:
				for i in range(row-2, -1, -1):
					if board[i, col] == myC:
						return True
					elif board[i, col] == '-':
						break

		#check down
		if (row < size -2):
			if board[row+1, col] == hisC:
				for i in range(row+2, size):
					if board[i,col] == myC:
						return True
					elif board[i,col] == '-':
						break

		#diagonal ne aka up and right

		counter = 2
		if (row > 1 and col < size - 2):
			if board[row-1, col+1] == hisC:
				for i in range(row-2, -1, -1):
					if col+counter < size:
						if board[i, col+counter] == myC:
							return True
						elif board[i, col+counter] == '-':
							break
					counter += 1

		#diagonal nw
		counter = 2
		if (row > 1 and col > 1):
			if board[row-1, col-1] == hisC:
				for i in range(row-2, -1, -1):
					if col-counter >= 0:
						if board[i, col-counter] == myC:
							return True
						elif board[i, col-counter] == '-':
							break
					counter += 1

		#diagonal sw
		counter = 2
		if (row < size-2 and col > 1):
			if board[row+1, col-1] == hisC:
				for i in range(row+2, size):
					if col-counter >= 0:
						if board[i, col-counter] == myC:
							return True
						elif board[i, col-counter] == '-':
							break
					counter += 1

		#diagonal se
		counter = 2
		if (row < size - 2 and col < size - 2):
			if board[row+1, col+1] == hisC:
				for i in range(row+2, size):
					if col+counter < size:
						if board[i, col+counter] == myC:
							return True
						elif board[i, col+counter] == '-':
							break
					counter += 1
		return False

	def get_valid_points(self,board, myColor):
		valid_points = []
		for row in range(8):
			for col in range(8):
				if board[row, col] == '-':
					if self.check_if_valid(board, row, col, myColor):
						valid_points.append((row,col))
		return valid_points

	def get_random_valid(self, board, myColor):
		points = self.get_valid_points(board, myColor) 
		random_int = random.randint(0,len(points)-1)
		point = points[random_int]
		return point[0]*8+point[1]

	def toMatrix(self, json_string):
		stringSquares = json_string['squares']
		return np.matrix([stringSquares[i:i+8] for i in range(0, len(stringSquares), 8)])
	    
	def countPieces(self, board, col):
	    count = 0
	    for i in range(0, 8):
	        for j in range(0,8):
	            if board[i,j] == col:
	            	count+= 1
	    return count


	def flipPieces(self, board, move, myColChar):
	    row = move[0]
	    col = move[1]
	    
	    board[row, col] = myColChar

	    if myColChar == 'b':
	        enemyColChar = 'w'
	    elif myColChar == 'w':
	        enemyColChar = 'b'

	    if row <= 7 and row >= 0 and col <= 7 and col >= 0:

	        #Checking above the move.
	        refRow = row - 1
	        refCol = col
	        willFlip = False

	        while refRow >= 0 and refRow <= 7:
	            if board[refRow, refCol] == enemyColChar:
	                willFlip = True
	                refRow -= 1
	            elif board[refRow, refCol] == myColChar and willFlip:
	                refRow += 1
	                while refRow < row:
	                    board[refRow, refCol] = myColChar
	                    refRow += 1
	                break
	            else:
	                break

	        #Checking below the move.
	        willFlip = False
	        refRow = row+1
	        refCol = col

	        while refRow <= 7 and refRow >= 0:
	            if board[refRow, refCol] == enemyColChar:
	                willFlip = True
	                refRow += 1
	            elif board[refRow, refCol] == myColChar and willFlip:
	                refRow -= 1
	                while refRow > row:
	                    board[refRow, refCol] = myColChar
	                    refRow -= 1
	                break
	            else:
	                break

	        #Checking left of the move.
	        willFlip = False
	        refRow = row
	        refCol = col - 1

	        while refCol >= 0 and refCol <= 7:
	            if board[refRow, refCol] == enemyColChar:
	                willFlip = True
	                refCol -= 1
	            elif board[refRow, refCol] == myColChar and willFlip:
	                refCol += 1
	                while refCol < col:
	                    board[refRow, refCol] = myColChar
	                    refCol += 1
	                break
	            else:
	                break

	        #Checking right of the move.
	        willFlip = False
	        refRow = row
	        refCol = col+1

	        while refCol <= 7 and refCol >= 0:
	            if board[refRow, refCol] == enemyColChar:
	                willFlip = True
	                refCol += 1
	            elif board[refRow, refCol] == myColChar and willFlip:
	                refCol -= 1
	                while refCol > col:
	                    board[refRow, refCol] = myColChar
	                    refCol -= 1
	                break
	            else:
	                break

	        #Checking Nortwest diagonal.
	        willFlip = False
	        refRow = row-1
	        refCol = col-1

	        while refRow >= 0 and refCol >= 0 and refRow <= 7 and refCol <= 7:
	            if board[refRow, refCol] == enemyColChar:
	                willFlip = True
	                refCol -= 1
	                refRow -= 1
	            elif board[refRow, refCol] == myColChar and willFlip:
	                refCol += 1
	                refRow += 1
	                while refCol < col and refRow < row:
	                    board[refRow, refCol] = myColChar
	                    refCol += 1
	                    refRow += 1
	                break
	            else:
	                break

	        #Checking Northeast diagonal.
	        willFlip = False
	        refRow = row-1
	        refCol = col+1

	        while refRow >= 0 and refCol <= 7 and refRow <= 7 and refCol >= 0:
	            if board[refRow, refCol] == enemyColChar:
	                willFlip = True
	                refCol += 1
	                refRow -= 1
	            elif board[refRow, refCol] == myColChar and willFlip:
	                refCol -= 1
	                refRow += 1
	                while refCol > col and refRow < row:
	                    board[refRow, refCol] = myColChar
	                    refCol -= 1
	                    refRow += 1
	                break
	            else:
	                break

	        #Checking Southeast diagonal.
	        willFlip = False
	        refRow = row + 1
	        refCol = col + 1

	        while refRow <= 7 and refCol <= 7 and refRow >= 0 and refCol >= 0:
	            if board[refRow, refCol] == enemyColChar:
	                willFlip = True
	                refCol += 1
	                refRow += 1
	            elif board[refRow, refCol] == myColChar and willFlip:
	                refCol -= 1
	                refRow -= 1
	                while refCol > col and refRow > row:
	                    board[refRow, refCol] = myColChar
	                    refCol -= 1
	                    refRow -= 1
	                break
	            else:
	                break

	        #Checking Southwest diagonal.
	        willFlip = False
	        refRow = row+1
	        refCol = col-1

	        while refRow <= 7 and refCol >= 0 and refRow >= 0 and refCol <= 7:
	            if board[refRow, refCol] == enemyColChar:
	                willFlip = True
	                refCol -= 1
	                refRow += 1
	            elif board[refRow, refCol] == myColChar and willFlip:
	                refCol += 1
	                refRow -= 1
	                while refCol < col and refRow > row:
	                    board[refRow, refCol] = myColChar
	                    refCol += 1
	                    refRow -= 1
	                break
	            else:
	                break

	        return board


if __name__ == '__main__':
	oai = OthelloAI(mycolor)
	move = oai.get_random_valid(oai.toMatrix(json_string), mycolor)
	sys.exit(move)


