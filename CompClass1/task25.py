# Write a program that will print squares of the twenty first natural numbers
# (0, 1, 4, 9, 16, etc.)
import math

for i in range(21):
    square = int(math.pow(i, 2))
    print("The square of the natural number is: ", square)

# or
print("************************************************")
for i in range(21):
    square = i * i
    print("The square of the natural number is: ", square)
