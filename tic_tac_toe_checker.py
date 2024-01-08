# https://www.codewars.com/kata/525caa5c1bf619d28c000335

def is_solved(board):
    for i in range(3):
        if board[0] or board[1] or board[2]:
            pass

board = [[0,1,2],[0,1,1],[2,1,1]]
for i in range(3):
    ans_1 = [x for x in board[i] if x == 1]
    ans_2 = [x for x in board[i] if x == 2]
    if len(ans_1) == 3 or len(ans_2)==3:
        print(True)
    ans_3 = [x[i] for x in board]
    if sum(ans_3)/sum(list(set(ans_3))) == 3:
        print(True)
    
