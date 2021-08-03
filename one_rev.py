diet = {
        "breakfast": "eggs",
        "lunch": "eggs",
        "dinner": "pizza"
        }

def spin(stuff):
    spun = {}
    for item in stuff:
        old_value = stuff[item]
        if old_value not in spun:
            spun[old_value] = [item]
        else:
            spun[old_value].append(item)
    return spun
            
print(spin(diet))
