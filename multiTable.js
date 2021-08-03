/** This function takes in a number and prints out a multiplication table
of the number up to 10 */

const printTable = (num) => {
	let table = "";
	for (let i = 1; i < 11; i++) {
		table +=
		`${i} * ${num} = ${i * num}${i==10?'':'\n'}`
	}
	return table
}

console.log(printTable(3))

	
