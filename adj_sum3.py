def get_adjacent_sum(lst):
    result = []
    for i in range(len(lst) - 1):
        result.append(lst[i] + lst[i+1])
    return result

print(get_adjacent_sum([3,7,2,11]))
