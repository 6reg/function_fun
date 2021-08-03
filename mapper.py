x = ["hello", "goodbye", "see you later"]

def mapper(arr):
    y = []
    for item in arr:
        y.append(index(item))
    return y

print(mapper(x))
