# https://www.codewars.com/kata/51e04f6b544cf3f6550000c1

def beeramid(bonus, price):
    beer_can_count = int(bonus // price)
    how_many_levels = 0
    if beer_can_count == 1:
        return 1
    for i in range(1,beer_can_count):
        if i**2 <= beer_can_count:
            beer_can_count -= i**2
            how_many_levels += 1
        if beer_can_count <= 0:
            break

    return how_many_levels if how_many_levels != 0 else 0
    

print(beeramid(4, 4))  # 1
print(beeramid(21, 1.5)) # 3

'''
def beeramid(bonus, price):
    i = 0
    while bonus > 0:
        i += 1
        bonus -= price * i**2
        if bonus < 0: i -= 1
    return i
'''


'''
def beeramid(bonus, price, level=1):
    return 0 if bonus < price * level**2 else 1 + beeramid(bonus - price * level**2, price, level + 1)
'''


'''
def beeramid(bonus, price):
    num_cans = bonus // price
    level = 0
    while num_cans >= 0:
        level += 1
        num_cans -= level*level
    return max(0, level-1)
'''