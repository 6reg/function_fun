my_dict = {
        "apple": "red",
        "banana": "yellow",
        "strawberry": "red",
        "mango": "yellow"
        }

def rev(data_struc):
    reversal = {}
    for old_key in data_struc:
        old_value = data_struc[old_key]
        if old_value not in reversal:
            reversal[old_value] = [old_key]
        else: 
            reversal[old_value].append(old_key)
    return reversal

def main():
    reversal = rev(my_dict)
    print(my_dict)
    print(reversal)

main()
