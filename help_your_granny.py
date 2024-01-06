# https://www.codewars.com/kata/5536a85b6ed4ee5a78000035


import math

def tour(friends, friend_towns, home_to_town_distances):
    how_many_friends = len(friends)
    total_distance = 0
    keys = list(home_to_town_distances.keys())

    for i in range(len(keys) - 1):
        value0 = home_to_town_distances[keys[0]]
        key1 = keys[i]
        key2 = keys[i + 1]
        value1 = home_to_town_distances[key1]
        value2 = home_to_town_distances[key2]
        total_distance += math.sqrt(value2**2 - value1**2)
    total_distance = int(total_distance) + value0 + value2
    return int(total_distance)
    

friends1 = ["A1", "A2", "A3", "A4", "A5"]
fTowns1 = [["A1", "X1"], ["A2", "X2"], ["A3", "X3"], ["A4", "X4"]]
distTable1 = {"X1": 100.0, "X2": 200.0, "X3": 250.0, "X4": 300.0}

print(tour(friends1, fTowns1, distTable1))