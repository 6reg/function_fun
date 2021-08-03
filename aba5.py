import re

def get_aba(original):
    result = ""
    for i in original:
        vowels = re.search("[aeiouAEIOU]", i)
        if vowels:
            result+= i + "b" + i.lower()
        else:
            result+= i
    return result

print(get_aba("Cats and dogs"))
