colors = {
        "orange": "orange",
        "purple": "plum",
        "orange": "mandarin",
        "purple": "grape"
        }

def main():
    reverse_colors = rev_colors(colors)
    print(reverse_colors)

def rev_colors(data_struct):
    rev_colors = {}
    for og_key in data_struct:
        og_value = data_struct[og_key]
        if og_value not in rev_colors:
            rev_colors[og_value] = [og_key]
        else:
            rev_colors[og_value].append(og_key)
    return rev_colors

main()
