def combinations(lst):
    res = []
    for letter in range(len(lst)):
        for letter1 in range(letter+1,len(lst)):
            combo = [lst[letter],lst[letter1]]
            if combo not in res:
                res.append(combo)
    return res

print(combinations(["a","b","c"]))
print(combinations([0,1,2,3]))
