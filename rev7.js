const fruit = {"apple":"red"}

const revFruit = (fruit) => {
	let rev = {}
	for (key in fruit) {
		let fruit_value = fruit[key]
		if (fruit_value in rev == false) {
			rev[fruit_value] = [key]
		} else {
			rev[fruit_value].push(key)
		}
	}
	return rev
}

console.log(revFruit(fruit))
