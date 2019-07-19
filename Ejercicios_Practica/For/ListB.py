foods = ['hamburger', 'hot-dog', 'salad', 'humus', 'milk', 'peach']
enumerateFoods = enumerate(foods)
print(type(enumerateFoods))
print(list(enumerateFoods))

enumerateFood = enumerate(foods, 2)
print(list(enumerateFoods))

for foodList in foods:
    if foodList == "humus":
        print("You don't need to buy more: ")
    print(foodList)
