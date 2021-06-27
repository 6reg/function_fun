my_dict = {
        "key1" : 1,
        "key2" : 1,
        "key3" : 2,
        "key4" : 1,
        "key5" : 3
        }


def get_rev(dictionary):
    rev = {}
    for old_key in dictionary:
        old_value = dictionary[old_key]
        if old_value not in rev:
            rev[old_value] = [old_key]
        else:
            rev[old_value].append(old_key)
    return rev

def main():
    rev = get_rev(my_dict)
    print(rev)


main()
