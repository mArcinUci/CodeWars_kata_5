# https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3

def find_uniq(arr):
    new_arr = [''.join(sorted(set(filter(str.isalpha, elem.lower())))) for elem in arr]
    example = new_arr[0] 
    for i in new_arr[1:]:
        if i not in example or len(i) != len(example):
            return arr[new_arr.index(i)]
     
        
  
print(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']))
print(find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]))
print(find_uniq([  'Tom Marvolo Riddle', 'I am Lord Voldemort', 'Harry Potter']))
print(find_uniq([ '    ', '  ', ' ', 'a', ' ', '' ]))
print(find_uniq([ 'foobar', 'barfo', 'fobara', '   ', 'fobra', 'oooofrab' ]))
