"""
This program takes in a string and returns a new string built according to 
the rules of the German children's game "Aba". 
The rules are: 
    if letter is a vowel, replace letter with letter+"b"+letter
    keep case of original string

Psuedocode:
    * import regex module
    * define function name with one argument
    * create empty string to hold result
    * for each character in the argument, 
        create variable that holds regex search for vowels
        check if current char is equal to regex variable
        apply Aba rules and append to result string
    * return result string
"""
import re

def get_aba_translation(original_string):
    result_string = ""
    for char in original_string:
        vowels = re.search("[aeiouAEIOU]", char)
        if vowels:
            result_string += char + "b" + char.lower()
        else:
            result_string += char
    return result_string

print(get_aba_translation("Africa is Africa in German"))

        
