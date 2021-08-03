/*
------------
Method converts dash/underscore delimited words into camel casing.
First word within ouput should be capitalized only if original word
was capped (known as upper camel case / pascal case)
------------
*/

const testStr = "The_STealh_WaRioR"

const toCamelCase = (str) => {
	let arr = str.split(/[_-]+/); // ["The", "STealth", "WaRioR]
	let res = [];
	let caps = /[A-Z]/;

	if (caps.test(arr[0].charAt(0))) {
		res.push(arr[0].charAt(0).toUpperCase() + arr[0].slice(1).toLowerCase());
	} else {
		res.push(arr[0].toLowerCase())
	}
	
	for (let i = 1; i < arr.length; i++) {
		res.push(arr[i].charAt(0).toUpperCase() + arr[i].slice(1).toLowerCase());
	}
	return res.join("")
}


console.log(toCamelCase(testStr))
