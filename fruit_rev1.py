import json

def rev_maker():

    with open("fruits.json") as f:
        fruits = json.load(f)
        color_lists = {}
        for fruit in fruits:
            color = fruits[fruit]
            if color not in color_lists:
                color_lists[color] = [fruit]
            else:
                color_lists[color].append(fruit)
        return print(color_lists)

rev_maker()
