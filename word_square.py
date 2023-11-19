def word_square(letters):
    N = len(letters) ** 0.5
    N = int(N)
    matrix = [letters[i:i+N] for i in range(0,len(letters), N)]
    flipped_characters = [''.join(row[::-1]) for row in matrix]
    rotated_matrix = flipped_characters[::-1]
    print(matrix)
    print(rotated_matrix)
    if matrix == rotated_matrix:
        return True
    else:
        return False




print(word_square('123456789'))
print(word_square('AAAAACEEELLRRRTT'))
#print(word_square('SATORAREPOTENETOPERAROTAS'))
#print(word_square('CARDAREAREARDART'))
#print(word_square('NOTSQUARE'))
#print(word_square('ABCD'))