## Take number and create multiplication table to 10 with number

def multi_table(num):
	table = ''
	for i in range(1,11):
		if i == 10:
			table += str(i) + " * " + str(num) + " = " + str((i*num))
		else:
		
			table += str(i) + " * " + str(num) + " = " + str((i*num)) + '\n'
	return table

print(multi_table(3))

