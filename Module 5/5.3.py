number = int(input("Enter a number: "))
if number <= 1:
    print("The number is not prime")
elif number <= 3:
    print("The number is prime")
elif number % 2 == 0 or number % 3 == 0:
    print("The number is not prime")
elif number >= 5:
    for x in range(5, number + 1):
        if number % 2 == 0 and number % 3 == 0 and x != number and x != 1:
            print("The number is not prime")
            break
        else:
            print("The number is prime")
            break

