arr = [1,2,3,4,5]

def splicer(arr, index, amount):
    new_arr = []
    for item in arr:
        if arr[item] == index:
           new_arr[index] = [item]
           print(new_arr)

print(splicer(arr,0,1))
