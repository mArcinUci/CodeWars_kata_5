# https://www.codewars.com/kata/525caa5c1bf619d28c000335

def is_solved(board):
    count_zeros = 0
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 1:
            return 1
        if board[0][0] == 2:
            return 2
    rotated_matrix = [[board[j][i] for j in range(len(board))] for i in range(len(board[0])-1, -1, -1)]
    if rotated_matrix[0][0] == rotated_matrix[1][1] == rotated_matrix[2][2]:
        if rotated_matrix[0][0] == 1:
            return 1
        if rotated_matrix[0][0] == 2:
            return 2
    for i in range(3):
        ans_1 = [x for x in board[i] if x == 1]
        if len(ans_1) == 3:
            return 1
        ans_2 = [x for x in board[i] if x == 2]
        if len(ans_2) == 3:
            return 2
        ans_3 = [x[i] for x in board if x[i] == 1]
        if len(ans_3) == 3 and sum(ans_3)/sum(list(set(ans_3))) == 3:
            return 1
        ans_4 = [x[i] for x in board if x[i] == 2]
        if len(ans_4) == 3 and sum(ans_4)/sum(list(set(ans_4))) == 3:
            return 2     
    for row in board:
        count_zeros += row.count(0)
    if count_zeros > 0:
        return -1
    else:
        return 0 
       

'''
def isSolved(board):
	for i in range(0,3):
		if board[i][0] == board[i][1] == board[i][2] != 0:
			return board[i][0]
		elif board[0][i] == board[1][i] == board[2][i] != 0:
			return board[0][i]
			
	if board[0][0] == board[1][1] == board[2][2] != 0:
		return board[0][0]
	elif board[0][2] == board[1][1] == board[2][0] != 0:
		return board[0][0]

	elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
		return 0
	else:
		return -1
'''


'''
def isSolved(board):
    for sign in [1, 2]:
        win = [sign] * 3
        if (win in board or
            win in zip(*board[::-1]) or
            win in [[board[x][0], board[1][1], board[2-x][2]] for x in [0, 2]]):
                return sign
    return -1 if 0 in sum(board, []) else 0
'''
