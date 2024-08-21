def convert(number):
    liters = int(number) * 3.78541
    return liters
result = 0
gallons = input("Enter a number of the gallons: ")
if int(gallons) < 0:
    print("Session ended.")
else:
    while result >= 0:
        result = float(convert(gallons))
        print(result)
        gallons = input("Enter a number of the gallons: ")
        if int(gallons) < 0:
            print("Session ended.")
            break
        else:
            if result < 0:
                print("Session ended.")
