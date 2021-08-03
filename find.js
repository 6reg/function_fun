/*
let result = arr.find(function(item, index, array) {
  // if true is returned, item is returned and iteration is stopped
 // for falsy scenario returns undefined
});
*/

let users = [
	{id: 1, name: "John"},
	{id: 2, name: "Pete"},
	{id: 3, name: "Mary"}
];

let user = users.find(item => item.id == 1); 

console.log(user.name); // John

let otherUser = users.find(item => item.name == "Mary");

console.log(user.id); // 3
