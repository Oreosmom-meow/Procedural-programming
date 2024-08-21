import math
def unit_price(diameter, total_price):
    area = math.pi * (diameter / 2) ** 2
    price = total_price * (area / 100000)
    return price
diameter_enter, price_enter = input("Enter the diameter and total price of first pizza: ").split()
price_1 = unit_price(float(diameter_enter), float(price_enter))
diameter_enter, price_enter = input("Enter the diameter and total price of second pizza: ").split()
price_2 = unit_price(float(diameter_enter), float(price_enter))
if price_1 < price_2:
    print("First pizza has lower unit price than second pizza")
else:
    print("Second pizza has lower unit price than first pizza")


