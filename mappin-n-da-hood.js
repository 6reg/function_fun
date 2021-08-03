const yObj = {
  fname: "greg",
  lname: "mathias",
  age: 42,
  height: 6.3
}

const myArr = [yObj, 1, 3]

const mapper = (arr) => arr.map((item) => item + arr.indexOf()) 

console.log(mapper(myArr))

