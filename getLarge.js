const apples = [20, 56, 4, 10]

function getLarge(arr) {
	return Math.max.apply(null, arr);
}

console.log(getLarge(apples))
