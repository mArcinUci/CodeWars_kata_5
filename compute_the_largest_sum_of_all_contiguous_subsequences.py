# https://www.codewars.com/kata/56001790ac99763af400008c

def largest_sum(arr):
    if len(arr) == 0:
        return 0
    
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum if max_sum > 0 else 0 


print(largest_sum([1,2,3,4]))