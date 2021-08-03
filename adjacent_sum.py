"""
this method takes in a list of numbers and returns a new list containing 
the sums of the adjacent numbers in the original list

* create empty list to store result list
* loop through input list
* add current element + next element and append to result list
* return result list

"""

def get_adjacent_sum(input_lst):
    print("input_lst = ", input_lst)
    res_lst = [] # emtpy list to store results
    print("res_lst = ", res_lst)

    for num in range(len(input_lst) - 1): 
        print("num = ", num)
        print("range(len(input_lst)) =", range(len(input_lst)))
        print("input_lst[num] = ", input_lst[num])
        res_lst.append(input_lst[num] + input_lst[num + 1])
        print("res_lst =", res_lst)
        print("input_lst[num] = ", input_lst[num])
    return res_lst

print(get_adjacent_sum([3, 7, 2, 11]))
