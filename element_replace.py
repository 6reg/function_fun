"""
This program takes in a list and a dictionary. It then returns a new
list where elements of original list are replaced with their corresponding values in 
the dictionary

* define function with name and parameters for list and dictionary
create new list to hold result
for item in list, 
    check for it's value in dictionary and append it to new list
    else just append list item to new list
return new list
"""
lst1 = ["Lebron James", "Lionel Messi", "Serena Williams"]
dict1 = {"Serena Williams": "tennis", "Lebron James": "basketball"}

def element_replace(lst, dct):
    res_lst = []
    for item in lst:
        if item in dct:
            res_lst.append(dct[item])
        else:
            res_lst.append(item)

    return res_lst

print(element_replace(lst1, dict1))
