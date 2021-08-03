import json

def get_fruits():
    with open("fruits.json") as f:
        fruits = json.load(f)

        fruit = fruits['banana']
        print("Bananas are " + str(fruit))

get_fruits()
