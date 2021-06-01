arr = ['hello', 'goodbye', 'split', 'concatenate']

print(arr)

def add_chicken(lst, animal):
    lst.append(animal)
    return lst

def reverse(lst):
    rev_lst = lst[::-1]
    return rev_lst

def main():
    chicken = add_chicken(arr, 'chicken')
    print(chicken)
    rev_chick = reverse(chicken)
    print(rev_chick)

main()

