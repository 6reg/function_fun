def get_adjacent_sum(original):
    result = []
    for i in range(len(original) - 1):
        result.append(original[i] + original[i+1])
    return result

print(get_adjacent_sum([3,7,2,11]))
