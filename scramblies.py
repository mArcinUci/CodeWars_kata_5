# https://www.codewars.com/kata/55c04b4cc56a697bb0000048

def scramble(s1, s2):
    letter_count = {}
    
    for character in s1:
        letter_count[character] = letter_count.get(character, 0) + 1
    
    for char in s2:
        if char not in letter_count or letter_count[char] <= 0:
            return False
        letter_count[char] -= 1

    return True


'''
def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True
'''


'''
def scramble(s1,s2):
    return all( s1.count(x) >= s2.count(x) for x in set(s2))

def scramble(s1, s2):
    return not any(s1.count(char) < s2.count(char) for char in set(s2))

'''