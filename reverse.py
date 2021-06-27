original = {
        "Mehran": 51,
        "Gary": 70,
        "Chris": 33,
        "Adele": 33,
        "Lionel": 33,
        "Brahm": 24,
        "Freya": 33
        }

def make_reverse():
    reversed_dict = {}

    for old_key in original:
        old_value = original[old_key]

    # if first time seeing old_value, make new list
        if old_value not in reversed_dict:
            reversed_dict[old_value] = [old_key]
        else: # get list already associated with old_value
              # and add to it
            value_list = reversed_dict[old_value]
            value_list.append(old_key)
            print(reversed_dict)
    return reversed_dict

make_reverse()
