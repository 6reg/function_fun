"""
inputs: sentence string
outputs: translated string

vars: new list of words

apply split method to input string and save it to new var
Check 
"""

def aba_translate(string):
    new_str = ''
    for element in string:
        if element == "a" or element == "e" or element == "i" or element == "o" or element == "u":
            new_str += element + "b" + element
        else:
            new_str += element
    return new_str

print(aba_translate("Cats and Dogs"))
