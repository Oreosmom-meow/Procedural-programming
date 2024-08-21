import random
def roll_dice():
    dice = random.randint(1,6)
    return int(dice)
roll = 0
while roll != 6:
    roll = roll_dice()
    print(roll)


