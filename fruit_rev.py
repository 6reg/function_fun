import json

def fruit_rever():
    with open("fruits.json") as f:
        fruits = json.load(f)

        fruits_rev = {}

        for fruit in fruits:
            old_color = fruits[fruit]
            if old_color not in fruits_rev:
                fruits_rev[old_color] = [fruit]
            else:
                fruits_rev[old_color].append(fruit)
        print(fruits_rev)
        return fruits_rev

fruit_rever()
