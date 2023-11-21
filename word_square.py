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
    #print(N)
    #print(len(letter_count))
    #print(letter_count)
    if count_of_single_character > N or len(letter_count) > 3*N:
        return False
    else:
        return True




#print(word_square('LNGZRDVIPUFYXKOZOXZXQVBQFFVRDJYUSJYDOIUFXPUFJKFYI'))
#print(word_square('LEQUEYIZLCZZSUUYOUCRTSKCMBRBWKAYSGHWWQYJSFEIFPZJRINGASJLJPYJIYXB'))
#print(word_square('VCJZZDXQJAHRUBNKVJPCKQYWSXYQCIPTXFVDMCFPURGYNHBKWHAQYUFXMAOSKBCX'))
#print(word_square('AENESOTDUAVWANOMODYAWBRWCMQJZXZEKJPNSEMAYHUBSFUNBAZFVBBWARFAUEDQ'))
#print(word_square('ADWZNSESDYWFFXFCORDUZDEJUYXDRDNROWTJBUOAIHKVXCXYSEORAESRIUSMEOAQ'))
#print(word_square('XXXJXXJERXXXJGXS'))
#print(word_square('IIXKOZTKRKRXILTOSXUSRTFIZ'))