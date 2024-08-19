input_year = int(input("Enter a year: "))
if input_year % 4 == 0 and input_year % 100 != 0 or input_year % 400 == 0:
    print("The year is a leap year")
elif input_year % 100 == 0 and input_year % 400 == 0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")