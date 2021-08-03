/* given arr of obj, return full names */

const users = [
	{firstName: "Susan", lastName: "Steward"},
	{firstName: "Daniel", lastName: "Longbottom"},
	{firstName: "Jacob", lastName: "Black"}
];

const makeFullNames = (obj) => obj.map((user) => `${user.firstName} ${user.lastName}`);


console.log(makeFullNames(users));
