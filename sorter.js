const compare = (a, b) => {
	if (a > b) return 1 // if first val greater than second val
	if (a == b) return 0; // if first val is equal to second val
	if (a < b) return -1; // if first val less than second val
}

let arr = [ 1, 2, 15 ];

console.log(arr.sort())

console.log(arr.sort(compare))
