import itertools

ls = [50, 55, 57, 58, 60]
k = 3
t = 163

def choose_best_sum(t, k, ls):
    if k > len(ls):
        return None
    combinations = list(itertools.combinations(ls, k))
    combinations_sum = [sum(list(x)) for x in combinations]
    if t in combinations_sum:
        return t
    combinations_sum.append(t)
    combinations_sum.sort()
    if combinations_sum.index(t) == 0:
        return None
    answer = combinations_sum[combinations_sum.index(t)-1]
    return answer


print(choose_best_sum(t,k,ls))


'''
import itertools

def choose_best_sum(t, k, ls):
    list = []
    for c in itertools.combinations(ls,k):
        if sum(c) <= t:
            list.append(sum(c))
    return sorted(list)[-1] if len(list) >= 1 else None
'''


'''
from itertools import combinations
choose_best_sum = lambda t, k, ls: list(sorted([sum(i) for i in combinations(ls, k) if t >= sum(i)], reverse=True)+[None])[0]
'''


'''
from itertools import combinations


def choose_best_sum(t: int, k: int, ls: list) -> int:
    return max((sum(comb) for comb in combinations(ls, k) if sum(comb) <= t), default=None)
'''