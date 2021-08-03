const nums = [5,8,9,1]

const filtRange = (arr,a,b) => {
	// keep elements greater than a and less than b
	const res = arr.filter(item => item > a || item < b)
	return res
}

console.log(filtRange(nums,7,0))
