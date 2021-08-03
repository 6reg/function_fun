"""
import re module
create emtpy string to hold result
loop through input string
create re var with vowels to test each element
if element matches vowel, add element + b + element to result string
else just add element
return result
print function call to screen
"""

import re

def get_aba(original):
    res = ""
    for i in original:
        vowels = re.search("[aeiouAEIOU]", i)
        if vowels:
            res+= i + "b" + i.lower()
        else:
            res+= i
    return res

print(get_aba("Africa is Africa in German"))
