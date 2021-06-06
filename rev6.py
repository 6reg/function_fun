my_dict = {
        "greg": "mathias",
        "mike": "malone",
        "jim": "malone",
        "jim": "smith"
        }

def main():
    reverse = make_rev(my_dict)
    print(my_dict)
    print(reverse)

def make_rev(data):
    rev_data = {}
    for old_key in data:
        old_value = data[old_key]
        if old_value not in rev_data:
            rev_data[old_value] = [old_key]
        else:
            rev_data[old_value].append(old_key)
    return rev_data

main()

