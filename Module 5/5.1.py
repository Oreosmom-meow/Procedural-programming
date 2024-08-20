import random
total = 0
number = input("Enter a number for the dice to roll: ")
for x in range(int(number)):
    dice = random.randint(1, 6)
    total += dice
print(total)