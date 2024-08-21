my_dict = {
    "KATL": "Hartsfield-Jackson Atlanta International Airport",
    "KLAX": "Los Angeles International Airport",
    "KORD": "O'Hare International Airport",
    "KDFW": "Dallas/Fort Worth International Airport",
    "KDEN": "Denver International Airport",
}

def add_entry(var_1, var_2):
    my_dict.update({var_1: var_2})
    return my_dict
def fetch_name(arg):
    result = my_dict[arg]
    return result

ask = input("Do you want to enter a new airport or fetch information or quit (e/f/n): ")
while ask != "n" and ask == "f" or ask == "e":
    if ask == "e":
            code_entry, name_entry = input("Enter the code and name of the airport: ").split()
            add_entry(code_entry, name_entry)
            ask = input("Do you want to enter a new airport or fetch information or quit (e/f/n): ")
    elif ask == "f":
            fetch = input("Enter ICAO code to get airport name: ")
            print(fetch_name(fetch))
            ask = input("Do you want to enter a new airport or fetch information or quit (e/f/n): ")
if ask == "n":
    print("Session ended")
if ask != "e" and ask != "f" and ask != "n":
    print("Invalid input, session end. ")