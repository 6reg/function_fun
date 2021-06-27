const fruits = require('./fruits.json');

for (fruit in fruits) {
	let fruitRev = {}
	let old_color = fruits[fruit]
	if (old_color in fruitRev == false) {
		fruitRev[old_color] = [fruit]
	} else {
		fruitRev[old_color].push(fruit)
	}
	console.log(fruitRev)
}
