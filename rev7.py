import json

with open("fruits.json") as f:
     fruits = json.load(f)
     fruit = fruits['banana']
     print(fruit)


