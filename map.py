stuff = ["greg", "dill", "roy"]

def get_lengths(names):
	lengths = []
	for name in names:
		lengths.append(len(name))
	return lengths	

print(get_lengths(stuff))
