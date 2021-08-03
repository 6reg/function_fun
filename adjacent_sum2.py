"""
Write a method "adjacent sum" that takes in a list of numbers and returns a new list containing the sums of the adjacent numbers in the original list.

* define method with original list as argument
* create empty result list
* for loop with range of length of original list minus 1
* append to result list current sum of current index and index + 1
* return result list
"""

def adjacent_sum(original_lst):
    result_lst = []
    for num in range(len(original_lst) - 1):
        result_lst.append(original_lst[num] + original_lst[num+1])
    return result_lst

print(adjacent_sum([2,5,1,9,2,4]))
