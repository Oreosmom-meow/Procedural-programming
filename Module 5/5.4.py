list = []
city = input("Enter a city: ")
list.append(city)
for x in range(4):
    city = input("Enter a city: ")
    list.append(city)
for x in list:
    print(x)