const fruits = require('./fruits.json')

const rev_fruits = (og) => {
	rev_fruit = {}
	for (let key in og) {
		let ov = og[key]
		if (ov in rev_fruit == false) {
			rev_fruit[ov] = [key]
		} else {
			rev_fruit[ov].push(key)
		}
	}
	return console.log(rev_fruit)
}

rev_fruits(fruits)
