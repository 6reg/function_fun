"""
Create empty string to build Aba string
For each element in arg string - 
    check if it is a vowel
    if so, add the element + b + element to Aba string
    else, add element to Aba string
return new Aba string
"""
import re
x = "Cats and Dogs."

def aba_maker(input_string):
    aba_string = ''
    for element in input_string:
        vowels = re.search("[aeiouAEIOU]", element)
        if vowels:
            aba_string+= element + "b" + element
        else:
            aba_string+= element
    return aba_string

print(aba_maker(x))
