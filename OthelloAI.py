import numpy as np 
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
		if (col < size -3):
			if board[row, col+1] == hisC:
				for i in range(col+2, size):
					if board[row,i] == myC:
						return True;
					elif board[row,i] == '-':
						break

		# check to the left
		if (col > 1):
			if (board[row,col-1] == hisC):
				for i in range(col-2, -1, -1):
					if board[row,i] == myC:
						return True;
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
		if (row < size -3):
			if board[row+1, col] == hisC:
				for i in range(row+2, size):
					if board[i,col] == myC:
						return True;
					elif board[i,col] == '-':
						break

		#diagonal ne aka up and right

		counter = 2
		if (row > 1 and col < size - 3):
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
		if (row < size-3 and col > 1):
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
		if (row < size - 3 and col < size - 3):
			if board[row+1, col+1] == hisC:
				for i in range(row+2, size):
					if col+counter < size:
						if board[i, col+counter] == myC:
							return True
						elif board[i, col+counter] == '-':
							break
					counter += 1
		return False
oai = OthelloAI("black")

board = np.matrix([['-', '-', '-', '-', 'w', '-', '-', '-'],
	['w', '-', '-', 'w', '-', '-', '-', '-'],
	['-', '-', 'w', 'w', '-', '-', 'w', 'w'],
	['b', '-', '-', '-', '-', 'w', '-', 'w'],
	['-', '-', '-', '-', 'w', '-', '-', 'w'],
	['-', '-', '-', 'w', '-', '-', '-', 'w'],
	['-', '-', 'w', '-', '-', '-', '-', 'w'],
	['-', 'b', 'w', 'w', '-', '-', '-', '-']])


print oai.check_horizontal(board, 1,7, 'black')