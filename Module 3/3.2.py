cabin_class = input("Please enter your class: ")
if cabin_class == "LUX":
    print("Your seat locates in upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("Your seat locates in above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("Your seat locates in windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Your seat locates in windowless cabin below the car deck.")
else:
    print("Invalid cabin class")