/*
arr.map
let result = arr.map(function(item, index, array) {
// returns new val instead of item
})
*/

let size = ["greg", "mike", "bill"].map(item => item.length, -1)
console.log(size)
