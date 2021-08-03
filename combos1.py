import itertools

def combos(lst):
    return list(itertools.combinations(lst,2))

print(combos([0,1,2,3]))
