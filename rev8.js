colors = {
	blue: "raspberry",
	blue: "blueberry",
	red: "apple",
	red: "strawberry"
}

function colorRev(arr) {
	let reversed = {}
	for (old_key in arr) {
		let old_value = arr[old_key]
		if (old_value in reversed == false) {
			reversed[old_value] = [old_key]
		} else {
			reversed[old_value].push(old_key)
		}
	}
	return reversed
}

console.log(colorRev(colors))
