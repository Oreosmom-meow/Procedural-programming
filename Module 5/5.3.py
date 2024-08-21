number = int(input("Enter a number: "))
if number <= 1:
    print("The number is not prime")
elif number <= 3:
    print("The number is prime")
elif number >= 4:
    for x in range(4, number + 1):
        if number % x == 0 and x != number and x != 1:
            print("The number is not prime")
        else:
            print("The number is prime")
            break
print(x)
