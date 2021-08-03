// split() // map((item, index) => true ? this : that // toUpperCase() // join('')
/* Take string separated with dashes and return string camel-cased 

const dashed = 'dem-tingz-dey-badmind'

const camelizer = (str) => {
	const arr = str.split('-') // ['dem', 'tingz', 'dey', 'badmind']
	.map((item, index) => index == 0 ? item : item[0].toUpperCase() +
	item.slice(1)) 
	.join('');
	return arr
}

console.log(camelizer(dashed))
*/

// split, map(item, index), toUpperCase, slice(), join()

// take string of comma separated vals, create numbered list

const str = "dem,tingz,deh,no,nuh,grimy";

const numLister = (str) => {
	// get arr from str
	const arr = str.split(','); // ['dem', 'tingz',...]
	arr.map((element, index) => index == 0 ? (index + 1) + element : (index + 1) + element[0].toUpperCase() + element.slice(1)).join('');
	return arr
}

console.log(numLister(str))


