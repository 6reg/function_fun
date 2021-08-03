"""
convert string of characters to list
create empty list 
for each item in list:
    check if it is a vowel (if item == a e i o u)
    if vowel, add item + b + item to empty list
    else add just item to list
convert list to string
return string

"""

def aba_translate(original):
    translated = []
    for char in original:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            translated.append(char + "b" + char)
        else:
            translated.append(char)
    transl = ''
    return transl.join(translated)


print(aba_translate("Cats and dogs"))
    
