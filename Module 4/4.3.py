import random
guess_number = input("Enter a number to start: ")
right_number = random.randint(1,10)
while int(guess_number) != right_number:
    if int(guess_number) < right_number:
        print("Too low")
        guess_number = input("Continue: ")
    elif int(guess_number) > right_number:
        print("Too high")
        guess_number = input("Continue:")
if int(guess_number) == right_number:
    print("Correct!")