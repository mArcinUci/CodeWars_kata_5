# https://www.codewars.com/kata/56001790ac99763af400008c

def largest_sum(arr):
    if sum(arr) <= 0 or len(arr) == 0:
        return 0
    
    largest_sum_list = []
    for i in range(len(arr)):
        largest_sum_for_i = []
        new_arr = arr[i:]
        for j in range(len(new_arr)+1):
            new_arr_j = new_arr[i:j]
            print(new_arr_j)
            largest_sum_for_i.append(sum(new_arr_j))

        largest_sum_list.append(max(largest_sum_for_i))


    return max(largest_sum_list)


print(largest_sum([1,2,3,4]))