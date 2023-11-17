def move_zeros(num):
    count = 0
    for i in num:
        if i == 0:
            count += 1
    new_num = [x for x in num if x !=0]
    for _ in range(count):
        new_num.append(0)
    return new_num

# other solutions from CodeWars

'''
def move_zeros(array):
    return [x for x in array if x] + [0]*array.count(0)
'''


'''
def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)
'''


'''
def move_zeros(a):
    a.sort(key=lambda v: v == 0)
    return a
'''