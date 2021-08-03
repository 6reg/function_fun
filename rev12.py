names = {
	"Mehran": 33,
	"James": 24,
	"Mike": 33,
	"Tim": 33,
}


def get_rev(names):
	ages = {}
	for old_key in names:
		old_value = names[old_key]
		if old_value not in ages:
			ages[old_value] = [old_key]
		else:
			ages[old_value].append(old_key)
	return ages


print(get_rev(names))
