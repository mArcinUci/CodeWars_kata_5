# https://www.codewars.com/kata/5536a85b6ed4ee5a78000035


import math

def tour(friends, friend_towns, home_to_town_distances):
    total_distance = 0
    friends_and_distance = [[friend, int(home_to_town_distances[town])] for friend, town in friend_towns if friend in friends and town in home_to_town_distances]
    first_value = friends_and_distance[0][1]
    last_value = friends_and_distance[-1][1]

    for i in range(len(friends_and_distance) - 1):
        value1 = friends_and_distance[i][1]
        value2 = friends_and_distance[i+1][1]
        total_distance += math.sqrt(abs(value2**2 - value1**2))
    total_distance = total_distance + first_value + last_value
    return int(total_distance)


'''
def tour(friends, friend_towns, home_to_town_distances):
    res=0
    s=0
    for i in friend_towns:
        if i[0] in friends:
            res=res+(home_to_town_distances[i[1]]**2-s**2)**(0.5)
            s=home_to_town_distances[i[1]]
    res=res+s
    return int(res)
'''


'''
def tour(friends, friend_towns, home_to_town_distances):
    ft = dict(friend_towns)
    d = [home_to_town_distances[ft[f]] for f in friends if f in ft] + [0]
    return int(sum((abs(d[i]**2 - d[i-1]**2))**0.5 for i in range(0, len(d))))
'''


'''
def tour(friends, towns, distances):
    visits = [distances[i[1]] for i in towns if i[0] in friends]
    
    return int(visits[0] + sum((b ** 2 - a ** 2) ** .5 for a, b in zip(visits[:-1], visits[1:])) + visits[-1])
'''