name = input("Enter your name: ")
set_name = set()
while name != "":
    set_name.add(name)
    name = input("Enter your name: ")
    if name in set_name:
        print("Existing name")
    elif name == "":
        break
    else:
        print("New name")
print("Session ended")

