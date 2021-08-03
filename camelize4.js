var pumpkin = "this,That , TheOther"

const getCameled = (str) => {
	let arr = str.split(',');
	if (arr[0].charAt(1) == /[A-Z]/) {
		arr[0].slice(1).toLowerCase();
}
	return str
}
console.log(getCameled(pumpkin))
