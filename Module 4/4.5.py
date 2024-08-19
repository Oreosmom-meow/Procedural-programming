username = input("Enter your username: ")
password = input('Enter your password: ')
attempt = 1
if username == "python" and password == "rule":
    print("Welcome")
while username != "python" or password != "rule":
    if attempt < 5:
        username = input("Enter your username again: ")
        password = input("Enter your password again: ")
    else:
        break
    attempt += 1
print("Access denied")

