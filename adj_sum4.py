"""
This program "get_adjacent_sum" takes in a list of numbers
and returns a new list containing the sums of adjacent
numbers in the original list.

Psuedocode:
    * define function with list as parameter
    * create emtpy list to store result
    * for i in range length of list - 1 (stop at second to last index) -
        add lst[i] + lst[i+1] and append result to result list
    * return result list
"""

def get_adjacent_sum(lst):
    result = []
    for i in range(len(lst) - 1):
        result.append(lst[i] + lst[i+1])
    return result

print(get_adjacent_sum([2,5,1,9,2,4]))

