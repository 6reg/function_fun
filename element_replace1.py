"""
This program takes in a list and a dictionary. It then returns a new list where
elements of the original list are replaced with their corresponding values in 
the dictionary.

Psuedocode:
    * define function that takes two args, a list and a dictionary
    * create empty list to store result list
    * for each item in the input list, check if it is a key in the input dictionary
        * if so, append the value of the key to the result list
        * else just append list item to result list
    * return result list
"""

def element_replace(lst, dic):
    result = []
    for element in lst:
        if element in dic:
            result.append(dic[element])
        else:
            result.append(element)
    return result

print(element_replace(["dog", "cat", "mouse"], {"dog": "barK","cat": "meow","duck": "quack"}))
