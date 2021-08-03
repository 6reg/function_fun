def get_zero_sums(lst):
    counter = 0
    for index in range(len(lst)):
        for index1 in range(index+1, len(lst)):
            if lst[index] + lst[index1] == 0: 
                counter += 1
    return counter

print(get_zero_sums([1,-5,-3,5,3,-1]))
