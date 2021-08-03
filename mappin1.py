#/* given arr of obj, return full names */
#
#const users = [
#	{firstName: "Susan", lastName: "Steward"},
#	{firstName: "Daniel", lastName: "Longbottom"},
#	{firstName: "Jacob", lastName: "Black"}
#];
#
#const makeFullNames = (obj) => obj.map((user) => `${user.firstName} ${user.lastName}`);
#
#
#console.log(makeFullNames(users));

users = [
	{"first": "Susan", "last": "Steward"},
	{"first": "Daniel", "last": "Longbottom"},
	{"first": "Jacob", "last": "Black"}
]

def get_full_name(obj):
	full_names = []
	for item in obj:
		full_names.append(item["first"] + " " + item["last"])
	return full_names

print(get_full_name(users))
		
		
