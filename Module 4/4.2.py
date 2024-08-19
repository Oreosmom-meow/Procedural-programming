inches = input("Enter inches: ")
centimeter = int(inches) * 2.54
while int(inches) > 0:
    print("Coverted centimeters = " + str(centimeter))
    inches = input("Enter inches: ")
print("Can't convert negative value")