// function that changges dash-separated words ("this-and-that")
// into camel-cased ("thisAndThat")

// for element in string
// if dash
// delete dash
// capitalize element at index of dash + 1
// return new str

const sample = "this-and-that"

const camelize = (str) => {
	let newStr = [];
	let arrToStr = str.split('-')
	for (let word in str) {
		console.log(word)
		newStr.push(word[0].toUpperCase() + word.substring(1))
	}

	newStr.join()
	return newStr
}

console.log(camelize(sample))

