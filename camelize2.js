// split() 
// map((item, index) => true ? this : that
// toUpperCase()
// join('')
/* Take string separated with dashes and return string camel-cased */

const dashed = 'dem-tingz-dey-badmind'

const camelizer = (str) => {
	const arr = str.split('-') // ['dem', 'tingz', 'dey', 'badmind']
	.map((item, index) => index == 0 ? item : item[0].toUpperCase() +
	item.slice(1)) 
	.join('');
	return arr
}

console.log(camelizer(dashed))
