"""
take in a string
check if each element of string is a vowel
if vowel, add element + letter b plus element to a new result string
match case of input string
return result string
"""
import re # bring in regex module


def get_aba_message(input_msg): # define function with parameter to take in input string
    result = "" # emtpy string to hold result
    for element in input_msg: # loop through each element of input string
        VOWEL = re.search("[aeiouAEIOU]", element) # var to test elements if they are vowels
        if element == VOWEL: # if current element matches any chars in VOWEL search 
            result+= element + "b" + element.lower() # append to result string
        else:
            result+= element
    return result

print(get_aba_message("Cats and dogs"))

            

