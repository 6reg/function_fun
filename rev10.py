names = {
	"banana" : "yellow",
	"peach" : "yellow",
	"berry" : "blue",
	"lemon" : "yellow"
}


def rever(arr):
	reved = {}
	for key in arr:
		arr[key] = [value]
		if arr[value] not in reved:
			reved[value] = arr[key]
		else:
			reved.append[value]
	return reved

print(rever(names))
