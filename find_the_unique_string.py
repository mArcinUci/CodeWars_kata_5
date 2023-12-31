# https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3

def find_uniq(arr):
    new_arr = [''.join(sorted(set(filter(str.isalpha, elem.lower())))) for elem in arr]
    for i in range(1,len(new_arr)-1):
        if new_arr[i-1] != new_arr[i] and new_arr[i] != new_arr[i+1] or len(new_arr[i-1]) != len(new_arr[i]) and len(new_arr[i]) != len(new_arr[i+1]):
            return arr[i]
        elif new_arr[0] != new_arr[1] and new_arr[0] != new_arr[-1]:
            return arr[0]
        elif new_arr[-1] != new_arr[1] and new_arr[-1] != new_arr[0]:
            return arr[-1]


'''

def find_uniq(arr):
    arr.sort(key=lambda x: x.lower())
    arr1 = [set(i.lower()) for i in arr]
    return arr[0] if arr1.count(arr1[0]) == 1 and str(arr1[0]) != 'set()' else arr[-1]
'''

   
'''
def find_uniq(arr):
    for word in set(arr):
        for letter in set(word):
            if sum([1 if letter in w else 0 for w in arr]) == 1:
                return word
            else: continue
'''    
    
    
'''
def find_uniq(arr):
    if set(arr[0].lower()) == set(arr[1].lower()):
        majority_set = set(arr[0].lower())
    elif set(arr[0].lower()) == set(arr[2].lower()):
        majority_set = set(arr[0].lower())
    else:
        majority_set = set(arr[1].lower())
    
    for string in arr:
        if set(string.lower()) != majority_set:
            return string
'''


'''
def find_uniq(arr):
    r = [''.join((''.join(sorted(list(set(x.lower()))))).split()) for x in arr]
    a, b = tuple(set(r))
    if r.count(a) == 1:
        return arr[r.index(a)]
    else:
        return arr[r.index(b)]
'''
  
  
print(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']))
print(find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]))
print(find_uniq([  'Tom Marvolo Riddle', 'I am Lord Voldemort', 'Harry Potter']))
print(find_uniq([ '    ', '  ', ' ', 'a', ' ', '' ]))
print(find_uniq([ 'foobar', 'barfo', 'fobara', '   ', 'fobra', 'oooofrab' ]))
