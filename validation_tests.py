from OthelloAI import OthelloAI
import numpy as np



def sw_checks(board):
	oai = OthelloAI("black")
	assert oai.check_if_valid(board, 1,7, 'black') == True
	board[5,3] = '-'
	assert oai.check_if_valid(board, 1,7, 'black') == False
	board[5,3] = 'w'
	board[4,4] = 'b'
	assert oai.check_if_valid(board, 1,7, 'black') == True
	board[3,1] = 'b'
	assert oai.check_if_valid(board, 0,4, 'black') == True
	board[6,1] = 'w'
	board[5,2] = 'b'
	assert oai.check_if_valid(board, 7,0, 'black') == True
	board[5,2] = 'w'
	board[4,3] = 'b'
	assert oai.check_if_valid(board, 7,0, 'black') == True
	board[5,2] = '-'
	assert oai.check_if_valid(board, 7,0, 'black') == False
	board[6,6] = 'w'
	board[5,5] = 'w'
	assert oai.check_if_valid(board, 7,7, 'black') == True
	board[4,4] = 'w'
	board[3,3] = 'w'
	board[2,2] = 'w'
	board[1,1] = 'w'
	board[0,0] = 'b'
	assert oai.check_if_valid(board, 7,7, 'black') == True
	board[2,2] = '-'
	assert oai.check_if_valid(board, 7,7, 'black') == False
	board[3,3] = '-'
	assert oai.check_if_valid(board, 7,7, 'black') == False
	board[7,0] = 'b'
	assert oai.check_if_valid(board, 5,2, 'black') == True

def nw_checks(board):
	oai = OthelloAI("black")
	assert oai.check_if_valid(board, 7,7,'black') == True
	board[2,2] = 'b'
	assert oai.check_if_valid(board, 7,7,'black') == True
	board[3,3] = '-'
	assert oai.check_if_valid(board, 7,7,'black') == False
	board[5,1] = 'w'
	board[4,0] = 'b'
	assert oai.check_if_valid(board, 7,3,'black') == True
	assert oai.check_if_valid(board, 4,4,'black') == True

def up_checks(board):
	oai = OthelloAI("black")
	assert oai.check_if_valid(board, 3, 0, 'black') == True
	assert oai.check_if_valid(board, 7, 0, 'black') == False
	assert oai.check_if_valid(board, 7, 7, 'black') == False
	board[0,7] = 'b'
	board[1,7] = 'w'
	assert oai.check_if_valid(board, 5, 7, 'black') == True
	board[0,3] = 'b'
	assert oai.check_if_valid(board, 3, 3, 'black') == True
	assert oai.check_if_valid(board, 7, 7, 'black') == True

def down_checks(board):
	oai = OthelloAI("black")
	assert oai.check_if_valid(board, 0, 0, 'black') == True
	board[3,0] ='w'
	assert oai.check_if_valid(board, 0, 0, 'black') == True
	assert oai.check_if_valid(board, 1, 7, 'black') == False
	board[7, 7] = 'b'
	assert oai.check_if_valid(board, 1, 7, 'black') == True
	board[4, 7] = '-'
	assert oai.check_if_valid(board, 1, 7, 'black') == False
	assert oai.check_if_valid(board, 5, 7, 'black') == True

def left_check(board):
	oai = OthelloAI("black")
	assert oai.check_if_valid(board, 2, 7, 'black') == True
	assert oai.check_if_valid(board, 3, 3, 'black') == False
	assert oai.check_if_valid(board, 3, 2, 'black') == True
def right_check(board):
	oai = OthelloAI("black")
	assert oai.check_if_valid(board, 2, 1, 'black') == True
	assert oai.check_if_valid(board, 7, 2, 'black') == True
	assert oai.check_if_valid(board, 5, 5, 'black') == True
	assert oai.check_if_valid(board, 5, 0, 'black') == True
	board[5,3] = '-'
	assert oai.check_if_valid(board, 5, 0, 'black') == True

def ne_check(board):
	oai = OthelloAI("black")
	assert oai.check_if_valid(board, 7, 0, 'black') == True
	assert oai.check_if_valid(board, 5, 3, 'black') == True
	assert oai.check_if_valid(board, 7, 5, 'black') == True
	board[5,2] ='-'
	assert oai.check_if_valid(board, 7, 0, 'black') == False
	assert oai.check_if_valid(board, 6, 6, 'black') == False
def se_checks(board):
	oai = OthelloAI("black")
	assert oai.check_if_valid(board, 0, 0, 'black') == True
	assert oai.check_if_valid(board, 4, 4, 'black') == True
	assert oai.check_if_valid(board, 6, 6, 'black') == False
	board[4,4] = '-'
	assert oai.check_if_valid(board, 5, 5, 'black') == True

def white_checks(board):
	assert oai.check_if_valid(board, 2, 1, 'white') == True
	assert oai.check_if_valid(board, 1,7, 'white') == True
	assert oai.check_if_valid(board, 2,5 , 'white') == True
	assert oai.check_if_valid(board, 3,3 , 'white') == True
	assert oai.check_if_valid(board, 1,5 , 'white') == True
	assert oai.check_if_valid(board, 6,1 , 'white') == False

if __name__ == '__main__':
	board = np.matrix(
		[['-', '-', '-', '-', 'w', '-', '-', '-'],
		['w', '-', '-', 'w', '-', '-', '-', '-'],
		['-', '-', 'w', 'w', '-', '-', 'w', 'w'],
		['b', '-', '-', '-', '-', 'w', '-', 'w'],
		['-', '-', '-', '-', 'w', '-', '-', 'w'],
		['-', '-', '-', 'w', '-', '-', '-', 'w'],
		['-', '-', 'w', '-', '-', '-', '-', 'w'],
		['-', 'b', 'w', 'w', '-', '-', '-', '-']])
	sw_checks(board)
	nw_board = np.matrix(
		[['b', '-', '-', '-', 'w', '-', '-', '-'],
		['w', 'w', '-', 'w', '-', '-', '-', '-'],
		['-', '-', 'w', 'w', '-', '-', 'w', 'w'],
		['b', '-', '-', 'w', '-', 'w', '-', 'w'],
		['-', '-', '-', '-', 'w', '-', 'w', 'w'],
		['-', '-', '-', 'w', '-', 'w', '-', '-'],
		['b', '-', 'w', '-', '-', '-', 'w', 'w'],
		['w', 'b', 'w', 'w', '-', '-', '-', '-']])
	up_board = np.matrix(
		[['b', '-', '-', '-', 'w', '-', '-', '-'],
		['w', '-', '-', 'w', '-', '-', '-', '-'],
		['w', '-', 'w', 'w', '-', '-', 'w', 'w'],
		['b', '-', '-', '-', '-', 'w', '-', 'w'],
		['-', '-', '-', '-', 'w', '-', '-', 'w'],
		['-', '-', '-', 'w', '-', '-', '-', 'w'],
		['-', '-', 'w', '-', '-', '-', '-', 'w'],
		['-', 'b', 'w', 'w', '-', '-', '-', '-']])
	nw_checks(nw_board)
	up_checks(up_board)
	down_board = np.matrix(
		[['-', '-', '-', '-', 'w', '-', '-', '-'],
		['w', '-', '-', 'w', '-', '-', '-', '-'],
		['w', '-', 'w', 'w', '-', '-', 'w', 'w'],
		['b', '-', '-', '-', '-', 'w', '-', 'w'],
		['w', '-', '-', '-', 'w', '-', '-', 'w'],
		['w', '-', '-', 'w', '-', '-', '-', 'w'],
		['w', '-', 'w', '-', '-', '-', '-', 'w'],
		['b', '-', 'w', 'w', '-', '-', '-', '-']])
	down_checks(down_board)
	left_board = np.matrix(
		[['-', '-', '-', '-', 'w', '-', '-', '-'],
		['w', '-', '-', 'w', '-', '-', '-', '-'],
		['w', '-', 'w', 'w', 'b', 'w', 'w', '-'],
		['b', 'w', '-', '-', '-', 'w', '-', 'w'],
		['w', '-', '-', '-', 'w', '-', '-', 'w'],
		['w', 'w', 'w', 'w', 'w', 'w', 'w', 'b'],
		['w', '-', 'w', '-', '-', '-', '-', 'w'],
		['b', '-', 'w', 'w', 'b', '-', '-', '-']])
	left_check(left_board)
	right_check(left_board)
	ne_board = np.matrix(
		[['-', '-', '-', '-', 'b', '-', '-', 'b'],
		['w', '-', '-', 'w', '-', '-', 'w', '-'],
		['w', '-', 'w', 'w', 'b', 'w', 'w', '-'],
		['b', 'w', '-', '-', 'w', 'w', '-', 'w'],
		['-', '-', '-', 'w', 'w', '-', '-', 'w'],
		['w', 'w', 'w', 'w', 'w', 'w', 'w', 'b'],
		['w', 'w', 'w', '-', '-', '-', 'w', 'w'],
		['-', '-', 'w', 'w', 'b', '-', '-', '-']])
	ne_check(ne_board)
	se_board = np.matrix(
		[['-', '-', '-', '-', 'b', '-', '-', 'b'],
		['w', 'w', '-', 'w', '-', '-', 'w', '-'],
		['w', '-', 'w', 'w', 'b', 'w', 'w', '-'],
		['b', 'w', '-', 'w', '-', '-', '-', 'w'],
		['-', 'w', '-', '-', 'w', '-', '-', 'w'],
		['w', 'w', 'w', '-', '-', 'w', '-', 'b'],
		['w', 'w', 'w', 'w', '-', '-', 'w', 'w'],
		['-', '-', 'b', 'w', 'b', '-', '-', 'b']])
	se_checks(se_board)

	white_board = np.matrix(
		[['-', '-', '-', '-', 'b', 'w', '-', 'w'],
		['w', 'w', '-', 'w', 'b', '-', 'w', '-'],
		['w', '-', 'w', 'b', 'b', 'w', 'w', 'w'],
		['b', 'b', '-', 'w', '-', '-', '-', 'b'],
		['-', 'b', '-', '-', 'w', '-', '-', 'b'],
		['w', 'b', 'w', '-', '-', 'w', '-', 'b'],
		['w', 'w', 'w', 'w', '-', '-', 'w', 'b'],
		['-', '-', 'b', 'w', 'b', '-', '-', 'w']])

