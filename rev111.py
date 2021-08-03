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


scores = {
        'mike': 30,
        'tom': 30,
        'phil': 33,
        'ed': 33
        }

def rev():
    # create empty dict 
    rev_scores = {}

    # loop through scores and assign old_value to value on each iteration
    for old_key in scores:
        old_value = scores[old_key]

    # check if it's been created yet, if not create and add to new dict
        if old_value not in rev_scores:
            rev_scores[old_value] = [old_key]
        else: # get list from dict already associated with old_value and add 
            # to it
             value_list = rev_scores[old_value]
             value_list.append(old_key)
             print(rev_scores)
    return rev_scores

rev()

def get_rev(names):
	ages = {}
	for old_key in names:
		old_value = names[old_key]
	if old_value not in ages:
		ages[old_value] = [old_key]
	else:
		val_list = age[old_val]
		val_list.append(old_key)
	return val_list

print(get_rev(original))


