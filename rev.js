const original = {
        "Mehran": 51,
        "Gary": 70,
        "Chris": 33,
        "Adele": 33,
        "Lionel": 33,
        "Brahm": 24,
        "Freya": 33
        }


const rev = () => {
	let rev_dict = {}
	for (old_key in original) {
		let old_value = original[old_key];
	}
	if (old_value in rev_dict == false) {
		rev_dict[old_value] = [old_key];
	}
	else {
		let value_list = rev_dict[old_value];
		value_list.push(old_key);
	}
	console.log(rev_dict)
	return rev_dict
}

console.log(rev())

/*
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
*/
