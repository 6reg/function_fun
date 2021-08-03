const isBelow = (currentVal) => currentVal > 0

const arr = [10, 5, 6, 9]

const every = () => console.log(arr.every(isBelow))
	 

console.log(every(arr))
