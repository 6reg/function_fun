import itertools

def get_combos(lst):
    return list(itertools.combinations(lst,2))
print(get_combos(["a","b","c"]))
