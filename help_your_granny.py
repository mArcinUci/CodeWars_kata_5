# https://www.codewars.com/kata/5536a85b6ed4ee5a78000035

def tour(friends, friend_towns, home_to_town_distances):
    return 0

# [ ["X1", 100.0], ["X2", 200.0], ["X3", 250.0], ["X4", 300.0] ]
import math

a = 100
b = 200
c = 250
d = 300



f1 = math.sqrt(b**2 - a**2)
f2 = math.sqrt(c**2 - b**2)
f3 = math.sqrt(d**2 - c**2)

f = a + f1 + f2 + f3 + d
print(f)