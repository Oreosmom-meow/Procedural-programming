number = input("Enter a number: ")
list = []
while number != "":
    number = input("Enter a number: ")
    list.append(number)
    list.sort(reverse=True)
N = 5
res = list[:N]
print("The biggest five numbers are: " + str(res))