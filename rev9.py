import json

def rev():
    with open("fruits.json") as f:
        fruits = json.load(f)
        rev_fruits = {}
        for o_key in fruits:
            o_val = fruits[o_key]
            if o_val not in rev_fruits:
                rev_fruits[o_val] = [o_key]
            else:
                rev_fruits[o_val].append(o_key)
    return rev_fruits

print(rev())
