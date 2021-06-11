const fruits = require('./fruits.json');

const color_lists = (arr) => {
	let colors = {}
	for (fruit in arr) {
		let color = arr[fruit]
		if (fruit in colors == false) {
			colors[fruit] = [color]
		} else {
			colors[fruit].push(color)
		}

	}
	return colors
}

console.log(color_lists(fruits))
