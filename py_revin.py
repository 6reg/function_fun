
foods = {
        "banana" : "sweet",
        "strawberry": "sweet",
        "kiwi": "sweet",
        "french fry": "salty",
        "hamburger": "salty"
        }

re_food = {}
for food in foods:
    
    old_value = foods[food]

    if old_value not in re_food:

        re_food[old_value] = [food]

    else:

        re_food[old_value].append(food)

print(re_food)
