# https://www.codewars.com/kata/5511b2f550906349a70004e1



def last_digit(n1, n2):
    if n2 == 0:
        return 1
    else:
       return pow(n1,n2,10)
    

print(last_digit(2,10))
print(last_digit(2 ** 200, 2 ** 300))


'''
def last_digit(n1, n2):
    return (n1 % 10) ** (n2 % 4 + 4 * bool(n2)) % 10
'''


# it seems to be a nice solution
'''
digits = {
    0:[0,0,0,0],   
    1:[1,1,1,1],   
    2:[2,4,8,6],   
    3:[3,9,7,1],   
    4:[4,6,4,6],   
    5:[5,5,5,5],   
    6:[6,6,6,6],   
    7:[7,9,3,1],   
    8:[8,4,2,6], 
    9:[9,1,9,1]
}
def last_digit(n1, n2):
    return digits[n1%10][(n2-1)%4] if n2 else 1
'''


'''
E = [
  [0, 0, 0, 0], [1, 1, 1, 1],
  [6, 2, 4, 8], [1, 3, 9, 7],
  [6, 4, 6, 4], [5, 5, 5, 5],
  [6, 6, 6, 6], [1, 7, 9, 3],
  [6, 8, 4, 2], [1, 9, 1, 9]
]

def last_digit(n1, n2):
    if n2 == 0: return 1
    return E[n1 % 10][n2 % 4]
'''