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
            print(arr[current])
            current += 1
        

      

    

v = [9,2,3,4,7,8,0]
print(longest_comb(v, '<<'))