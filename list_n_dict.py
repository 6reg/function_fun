my_list = ['a', 'b', 'c']

my_dict = {
        'x' : 'a',
        'y' : 'b',
        'z' : 'c'
        }

print(my_list[1])
print(my_dict['y'])

for i in range(len(my_list)):
    value = my_list[i]
    print(i, value)

for key in my_dict:
    value = my_dict[key]
    print(key, value)
