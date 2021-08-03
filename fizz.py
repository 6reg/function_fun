"""
// // The Problem:
	// Write a program that prints the number from 1 to 20.
	// For multiples of three print "Fizz" instead of the number.
	// For multiples of five print "Buzz" instead of the number.
	// For numbers which area multiples of both three and five print "FizzBuzz".
	// For nums not divisible by 3, 5 or 15, print the number.

// FOR LOOP:
// Set counter to 1
// Break when counter reaches 20
// Increment counter by 1
let str = '';

const getFizzBuzz = (str) => {
for (let i = 1; i<= 20; i++) {
	if (i %  15 === 0) {
		str += `${'FizzBuzz'}${'\n'}`;
	} else if (i % 3 == 0) {
		str += `${'Fizz'}${'\n'}`;
	} else if (i % 5 == 0) {
		str += `${'Buzz'}${i==20?'':'\n'}`;
	} else {
		str += `${i + '\n'}`;	
	}

}

	return str
}
console.log(getFizzBuzz(str))
"""

# FOR loop to 20
# IF i % 15, print FizzBuzz
# IF i % 3, print Fizz
# IF i % 5, print Buzz
# Else print i

def buzzer():
	fizzer  = ''
	for i in range(1,21):
		if i % 15 == 0:
			fizzer += 'FizzBuzz\n'
		elif i % 3 == 0:
			fizzer += 'Fizz\n'
		elif i % 5 == 0:
			fizzer += 'Buzz\n'
		else:
			if i == 20:
				fizzer += str(i)
			else:
				fizzer += str(i) + '\n'
	return fizzer

print(buzzer())
