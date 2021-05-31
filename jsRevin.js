const vehicles = {
	car: "blue",
	bike: "red",
	plane: 'red',
	boat: "green",
	truck: "green"
}

const rever = (obj) => {
	const rev_dict = {}
	const keys = Object.keys(obj)
	keys.forEach((old_key, index) => {
		let old_value = obj[old_key]
		if (old_value in rev_dict == false) {
			rev_dict[old_value] = [old_key];
		} else {
			let value_list = rev_dict[old_value];
			value_list.push(old_key);
		}
	})
	return rev_dict
}

console.log(rever(vehicles))
