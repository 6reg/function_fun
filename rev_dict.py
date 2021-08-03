x = {
        "car" : "green",
        "truck": "blue",
        "suv": "red",
        "car": "yellow",
        "car": "orange"
        }

def dict_rev(original):
    reved = {}
    for original_key in original:
        original_value = original[original_key]
        if original_value not in reved:
            reved[original_value] = [original_key]
        else:
            reved[original_value].append(ariginal_key)
    return reved

print(dict_rev(x))

