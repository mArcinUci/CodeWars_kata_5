# Kata proper description:   https://www.codewars.com/kata/5863f1c8b359c4dd4e000001/python


food = { 
  "chicken": [20, 5, 10], 
  "eggs": [10, 5, 15], 
  "salmon": [27, 0, 10], 
  "beans": [8, 25, 0], 
  "bananas": [1, 23, 0],
}
# protein and carbohydrate has 4 calories, while 1 gram of fat provides 9 calories.
# Round your results to 2 decimal places and return a string in the form "Total proteins: n grams, Total calories: n".
# Delete all trailing zeros on every float and remove trailing point if the result is an integer. Note: No invalid input testing.

b = ["110g salmon, 30g eggs", "250g bananas, 106g chicken, 30g beans, 45g salmon"]
def bulk(arr):
    proteins = 0
    calories = 0
    calories_per_gram = [4,4,9]
    ingredients_and_weight = {}

    for item in arr:
        pairs = item.split(', ')
        for pair in pairs:
            parts = pair.split()
            weight = int(parts[0][:-1])
            ingredient = ' '.join(parts[1:])
            if ingredient in ingredients_and_weight:
                ingredients_and_weight[ingredient] += weight
            else:
                ingredients_and_weight[ingredient] = weight
    
    for ingredient in ingredients_and_weight:
        key_value = ingredients_and_weight[ingredient]
        if ingredient in food:
            food_value = food[ingredient]
            multiplier = key_value/100 
            food_value_scaled = [x * multiplier for x in food_value]
            calories_here = sum(x * y for x, y in zip(food_value_scaled, calories_per_gram))
            calories += calories_here
            proteins += food_value_scaled[0]
    if proteins == int(proteins):
        proteins = int(proteins)
    else:
        proteins = round(proteins,2)

    if calories == int(calories):
        calories = int(calories)
    else:
        calories = round(calories,2) 

    return (f'Total proteins: {proteins} grams, Total calories: {calories}')


print(bulk(b)) # Total proteins: 70.95 grams, Total calories: 846.4



'''
import re

PATTERN = re.compile(r'(\d+)g (\w+)')
CALORIES_PER_100g = { typ: sum( m*cal for m,cal in zip(masses, [4, 4, 9])) for typ,masses in food.items() }

formatAns = lambda n: str(round(n, 2)) if n%1 else str(int(n))

def bulk(arr):
    prots, cals = 0, 0
    for plate in arr:
        for mass,typ in PATTERN.findall(plate):
            prots += int(mass) * food[typ][0] / 100
            cals  += int(mass) * CALORIES_PER_100g[typ] / 100
    return 'Total proteins: {} grams, Total calories: {}'.format(formatAns(prots), formatAns(cals))
'''


'''
def bulk(arr):
    protein = calories = 0
    for meal in arr:
        for item in meal.split(', '):
            weight, foodtype = item.split('g ')
            weight = int(weight)
            p, c, f = food[foodtype]
            protein += p / 100 * weight
            calories += (p + c) / 100 * weight * 4 + f / 100 * weight * 9
    fmt = lambda f: ('%.2f'%f).rstrip('0').rstrip('.')
    return 'Total proteins: %s grams, Total calories: %s' % (fmt(protein), fmt(calories))
'''

'''
def bulk(arr):
    protein, calory = 0, 0
    for a in arr:
        for b in a.split(','):
            g, f = b.strip().split(' ')
            m = int(g[:-1])
            prot, carb, fat = food[f]
            protein += m * prot
            calory += m * (4 * (prot + carb) + 9 * fat)
    formatNum = lambda x: x / 100 if x % 100 else x // 100
    return f"Total proteins: {formatNum(protein)} grams, Total calories: {formatNum(calory)}"
'''