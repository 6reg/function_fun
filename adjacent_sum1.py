def get_adj_sum(lst):
    res_lst = []
    for num in range(len(lst) - 1):
        res_lst.append(lst[num] + lst[num + 1])
    return res_lst

print(get_adj_sum([3, 7, 2, 11]))
