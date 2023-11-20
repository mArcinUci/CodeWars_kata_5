def word_square(letters):
    letter_count = {}
    N = len(letters) ** 0.5
    
    if N != int(N):
        return False
    for i in letters:
        if i not in letter_count:
            letter_count[i] = 1
        else:
            letter_count[i] +=1
    count_of_single_character = sum(1 for value in letter_count.values() if value == 1)
    print(letter_count)
    if count_of_single_character > N:
        return False
    else:
        return True




print(word_square('GHBEAEFGCIIDFHGG'))
#print(word_square('AAAAACEEELLRRRTT'))
#print(word_square('SATORAREPOTENETOPERAROTAS'))
#print(word_square('CARDAREAREARDART'))
#print(word_square('NOTSQUARE'))
#print(word_square('ABCD'))