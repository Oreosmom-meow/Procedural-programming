number1_str, number2_str, number3_str = input("Enter three numbers separated by space: ").split()
number1 = float(number1_str)
number2 = float(number2_str)
number3 = float(number3_str)
sum = number1 + number2 + number3
product = number1 * number2 * number3
average = sum / 3
print("The sum of all the numbers is: " + str(sum))
print("The product of all the numbers is: " + str(product))
print("The average of the numbers is: " + str(average))
