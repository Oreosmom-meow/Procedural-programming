number = int(input("Enter a number: "))
check_prime = 0
if number <= 1:
    print("The number is not prime")
elif number <= 3:
    print("The number is prime")
elif number >= 4:
    for x in range(4, number - 1):
        if number % x == 0:
            print("The number is not prime")
            check_prime = 1
            break
    if check_prime == 0:
        print("The number is prime")

