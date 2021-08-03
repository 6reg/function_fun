"""
Given a list of elements, return every possible 2D combination of the elements

* import itertools
* define function with original list as argument
* list(itertools.combinations(arg, 2))
* return it

"""
import itertools

original_list = ["a", "b", "c"]

def get_combos(lst):
    return list(itertools.combinations(lst, 2))

print(get_combos(original_list))
