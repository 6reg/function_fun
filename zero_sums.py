def get_zero_sums(arr):
    counter = 0
    for i in range(0, len(arr)):
        for x in range(i+1, len(arr)):
            if arr[i] + arr[x] == 0:
                counter += 1
    return counter

print(get_zero_sums([-2, 2, 0, 5, -5]))
