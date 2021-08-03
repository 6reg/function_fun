let arr = ["this", "that", "the other"]

const forEacher = (arr) => {
	arr.forEach((item, index, array) => console.log(`${item} is at ${index}
	in ${array}`))
}

forEacher(arr)
