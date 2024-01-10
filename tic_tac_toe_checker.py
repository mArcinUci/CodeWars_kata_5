# https://www.codewars.com/kata/525caa5c1bf619d28c000335

def is_solved(board):
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
        ans_2 = [x for x in board[i] if x == 2]
        if len(ans_1) == 3:
             return 1
        if len(ans_2) == 3:
             return 2
        ans_3 = [x[i] for x in board]
        if ans_3[0] == 1 and sum(ans_3)/sum(list(set(ans_3))) == 3:
            return 1
        if ans_3[0] == 2 and sum(ans_3)/sum(list(set(ans_3))) == 3:
            return 2     
       


board = [[0,0,2],[0,2,0],[2,0,0]]
print(is_solved(board))

