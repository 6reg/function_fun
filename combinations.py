"""
This method 'combinations' takes in a list of unique elements, and returns 
a 2D list representing all possible combinations of 2 elements of the list.

* write function name with one parameter
* create emtpy lst to hold result
* create for loop with a range size of original list length
* create another loop

original = ["a", "b", "c"]

a[start:stop] items start through stop-1
a[start:] items start through rest of array
a[:stop] items from beginning through stop-1
a[:] copy of whole array
a[-1] last item in array
a[-2:] last two items in array
a[:-2] everything accept last two items 

a[start:end:step] = for(i = start; i < end i += step)

a[index_of_first_character:index_after_last_character]
"""
import itertools 

original = ["a", "b", "c"]
def combos(original):
    return list(itertools.combinations(original,2))
print(combos(original))
