const reverse = () => {
	let revDict = {}
	const myDict = {
		"banana": "yellow",
		"peach": "yellow",
		"apple": "red",
		"strawberry": "red"
	}
	for (const old_key in myDict) {
		let old_value = myDict[old_key]
		if (old_value in revDict) {
			revDict[old_value].push(old_key)
		} else {
			revDict[old_value] = [old_key]
		}

	}
	return console.log(revDict)
}

reverse()
