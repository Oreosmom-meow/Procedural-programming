season = ("spring", "summer", "fall", "winter")
month = input("Enter a month in number format: ")
if 1 <= int(month) <= 3:
    print(season[0])
elif 4 <= int(month) <= 6:
    print(season[1])
elif 7 <= int(month) <= 9:
    print(season[2])
elif 10 <= int(month) <= 12:
    print(season[3])
else:
    print("Invalid input")
