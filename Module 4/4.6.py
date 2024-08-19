import random
N = input("Enter a number for random points: ")
repeat = 0
n = 0
while repeat < int(N):
    x = random.uniform (-1, 1)
    y = random.uniform (-1, 1)
    if x * x + y * y < 1:
        n += 1
    repeat += 1
pi = 4 * int(n) / int(N)
print("The approximation of pi = " + str(pi))
