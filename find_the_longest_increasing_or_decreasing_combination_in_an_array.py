# https://www.codewars.com/kata/5715508de1bf8174c1001832

def longest_comb(arr, command):
    answer = []
    if '<' in command:
        pointer = True
    if '>' in command:
        pointer = False
    for i in range(len(arr)-1):
        present_longest_arr = []
        first_element = arr[i]
        present_longest_arr.append(first_element)
        current = i + 1
        while current < len(arr):
            if pointer == True:
                if arr[current] > present_longest_arr[-1]:
                    present_longest_arr.append(arr[current])
                current += 1
            if pointer == False:
                if arr[current] < present_longest_arr[-1]:
                    present_longest_arr.append(arr[current])
                current += 1
        if len(present_longest_arr) > len(answer):
            answer = present_longest_arr
    
    return answer if len(answer)>2 else []

      

    

v = [9,-3,2,3,-2,4,7,8,0]
print(longest_comb(v, '>'))


'''
                    if len(answer) == len(present_longest_arr):
                        answer.append(present_longest_arr)
                    if len(answer) < len(present_longest_arr):
                        answer.append(present_longest_arr)
'''