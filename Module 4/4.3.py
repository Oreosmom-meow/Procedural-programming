input_number = input("Enter a number: ")
max_val = int(input_number)
min_val = int(input_number)
while input_number != "":
    if int(input_number) > max_val:
        max_val = int(input_number)
    elif int(input_number) < min_val:
        min_val = int(input_number)
    input_number = input("Continue enter a number: ")
if input_number == "":
    print("The max number is " + str(max_val))
    print("The min number is " + str(min_val))