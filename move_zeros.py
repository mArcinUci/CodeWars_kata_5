def move_zeros(num):
    count = 0
    for i in num:
        if i == 0:
            count += 1
    new_num = [x for x in num if x !=0]
    for _ in range(count):
        new_num.append(0)
    return new_num

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))