import json

def rev_the_data():
    with open('./fruits.json') as f:
        original = json.load(f)
 
        reved = {}
        for old_key in original:
            old_val = original[old_key]
            if old_val not in reved:
                reved[old_val] = [old_key]
            else:
                reved[old_val].append(old_key)
    return print(reved)

rev_the_data()
