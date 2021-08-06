def get_nested(lst):
    result = []
    for i in range(len(lst)):
        for y in range(i+1, len(lst)):
            new_lst = [lst[i], lst[y]]
            if new_lst not in result:
                result.append(new_lst)
    return result

print(get_nested(["a","b","c","d"]))
