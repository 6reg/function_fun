"""
Take in string, return sting with rules of Aba game 

import regex (re) module

create empty result string 

loop through input string, if char is vowel, add char + b + char to result
if char is capitalized, change final char to lowercase

return result string
"""

import re

def get_aba(input_string):
    result = ""
    for char in input_string:
        vowels = re.search("[aeiouAEIOU]", char)
        if vowels:
            result+= char + "b" + char.lower()
        else:
            result+= char
    return result

print(get_aba("Everyone can code"))
