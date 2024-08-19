gender = str(input("Enter your gender (female or male): "))
hemoglobin_value = input("Enter your hemoglobin value (g/l): ")
if gender == "female" and int(hemoglobin_value) < 117:
    print("Your hemoglobin value is too low")
elif gender == "female" and int(hemoglobin_value) > 155:
    print("Your hemoglobin value is too high")
elif gender == "female" and 117 <= int(hemoglobin_value) <= 155:
    print("Your hemoglobin value is normal")
elif gender == "male" and int(hemoglobin_value) < 134:
    print("Your hemoglobin value is too low")
elif gender == "male" and int(hemoglobin_value) > 167:
    print("Your hemoglobin value is too high")
elif gender == "male" and 134 <= int(hemoglobin_value) <= 167:
    print("Your hemoglobin value is normal")
elif gender != "female" and gender != "male":
    print("Invalid input")