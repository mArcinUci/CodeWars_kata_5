# https://www.codewars.com/kata/582fdcc039f654905400001e

from itertools import permutations 
import math

    
def is_perfect_square(number):
    square_root = math.isqrt(number)
    return square_root**2 == number

def sort_by_perfsq(arr):
    count_perfect_square = []
    answer = []
    for i in arr:
        str_i = str(i)
        all_permutations = permutations(str_i)
        permutations_as_int = {int(''.join(permutation)) for permutation in all_permutations}
        perfect_square_permutations = [x for x in permutations_as_int if is_perfect_square(x)]
        count_perfect_square.append(len(perfect_square_permutations))

    sorted_pairs = sorted(zip(arr, count_perfect_square), key=lambda pair: (pair[1], -pair[0]), reverse=True)
    answer = [pair[0] for pair in sorted_pairs]
    return answer


'''
from itertools import permutations

def sort_by_perfsq(arr):
    return sorted(arr, key = lambda x: [-sum(int("".join(y)) ** 0.5 % 1 == 0 for y in set(permutations(str(x)))), x])
'''


'''
from itertools import permutations
from math import isqrt

def perfect_square_perms(n: int) -> int:
    return sum(isqrt(i) ** 2 == i for i in map(int, map(''.join, set(permutations(str(n))))))

def sort_by_perfsq(arr: list[int]) -> list[int]:
    return sorted(arr, key=lambda n: (-perfect_square_perms(n), n))
'''