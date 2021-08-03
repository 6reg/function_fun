def get_combos(lst):
    res = []
    for i in range(len(lst)):
        for y in range(i+1, len(lst)):
            checker = [lst[i], lst[y]]
            if checker not in res:
                res.append(checker)
    return res

print(get_combos([0,1,2,3]))
