const diet = {
	"breakfast": "eggs",
	"lunch": "eggs",
	"dinner": "bacon"
}


const rev = (foods) => {
	let spun = {};
	for (food in foods) {
		let oldVal = foods[food]
		if (oldVal in spun == false) {
			spun[oldVal] = [food];
		} else {
			spun[oldVal].push(food);
		}
	}
	return spun
	}
console.log(rev(diet))
