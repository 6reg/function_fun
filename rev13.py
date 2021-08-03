x = {
	"yellow": "banana",
	"yellow": "peach",
	"green": "banana",
	"orange": "orange",
	"orange": "peach"
}

def rever(x):
	y = {}
	for original_key in x:
		original_value = x[original_key]
		if original_value not in y:
			y[original_value] = [original_key]
		else:
			y[original_value].append(original_key)
	return y

print(rever(x))
