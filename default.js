const myObj = {
	name: "greg",
	age: 41,
	eye_color: "blue"
}

const myFunc = (name = "bill") => `my name is ${name}`

console.log(myFunc(), myFunc(myObj.name))
