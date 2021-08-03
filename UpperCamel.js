const originalStr = "This_That-TheOther";

const getCameled = (str) => {
	const res = [];
	const getArr = str.split(/[-_]+/);
	if (getArr[0].charAt(0) == /[A-Z]/) {
		res.push(getArr[0].slice(0) + getArr[0].slice(1).toLowerCase())
	} else {
	for (let i = 1; i < getArr.length; i++) {
		res.push(getArr[i].slice(0).toUpperCase() + getArr[i].slice(1).toLowerCase())
	}
}
return res.join("")
}

console.log(getCameled(originalStr))
