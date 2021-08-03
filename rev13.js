myDict = {
	"green": "banana",
	"yellow": "peach",
	"blue": "blueberry",
	"green": "avocado"
}


const getRev = (obj) => {
	let reved = {};
	for (let old_key in obj) {
		let old_value = obj[old_key];
		if (old_value in reved == false) {
			reved[old_value] = [old_key]
}
		else {
			reved[old_value].push(old_key)
}
}
	return reved
}


console.log(getRev(myDict))
