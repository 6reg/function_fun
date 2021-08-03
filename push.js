let arr = ['i', 'hello', 'goodbye']

console.log(arr)

const chicken = () => {
	const animal = 'chicken'
	const add_chicken  = (animal, lst) => {
		lst.push(animal)
		return lst
	}
	return add_chicken(animal, arr)
}

console.log(chicken())
