names = {
	"james": "smith",
	"jim": "smith",
	"jacob": "smith",
	"tom": "allen"
}

def rever(original):
	reverser = {}
	for old_key in original:
		old_value = original[old_key]
		if old_value not in reverser:
			reverser[old_value] = [old_key]		
		else:
			reverser[old_value].append(old_key)
	return reverser

print(rever(names))
