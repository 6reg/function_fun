my_data = {
        "this":"that",
        "that":"this"
        }
print(my_data)
def do_sumn(stuff):
    stuff["the other"] = "he"
    return stuff

print(do_sumn(my_data))
