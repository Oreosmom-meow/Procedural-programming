length_str = input("Enter the length of the rectangle: ")
length = float(length_str)
width_str = input("Enter the width of the rectangle: ")
width = float(width_str)
perimeter = length * 2 + width * 2
area = length * width
print("The area of the rectangle is:", str(area))
print("The perimeter of the rectangle is:", str(perimeter))