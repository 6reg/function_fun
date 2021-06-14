const fruitsColors = require('./fruits.json')

console.log(fruitsColors)

const rever = (original) => {
	let reved = {}
	for (fruit in original) {
		let color = original[fruit]
		if (color in reved == false) {
			reved[color] = [fruit]
		} else {
			reved[color].push(fruit)
		}
	}
	return reved
}

console.log(rever(fruitsColors))
