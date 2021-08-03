my_dict = {
	"name": "greg",
	"eye color": "blue",
	"age": 42,
}


def my_func(name = "default"):
	return "My name is " + name

print(my_func(my_dict["name"]))
print(my_func())
