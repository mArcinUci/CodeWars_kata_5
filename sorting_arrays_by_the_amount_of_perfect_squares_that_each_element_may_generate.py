# https://www.codewars.com/kata/582fdcc039f654905400001e

from itertools import permutations 
import math

    
def is_perfect_square(number):
    square_root = math.isqrt(number)
    return square_root**2 == number

def sort_by_perfsq(arr):
    count_perfect_square = []
    for i in arr:
        str_i = str(i)
        all_permutations = permutations(str_i)
        permutations_as_int = {int(''.join(permutation)) for permutation in all_permutations}
        perfect_square_permutations = [x for x in permutations_as_int if is_perfect_square(x)]
        count_perfect_square.append(len(perfect_square_permutations))
    print(count_perfect_square)


sort_by_perfsq([715, 112, 136, 169, 144])