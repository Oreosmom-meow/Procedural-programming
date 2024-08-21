import random
def roll_dice(number):
    dice = random.randint(1,int(number))
    return int(dice)
max_value = int(input("Enter a number: "))
roll = 0
while roll != max_value:
    roll = roll_dice(max_value)
    print(roll)
