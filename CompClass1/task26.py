# Write a program that will print a sum of the odd numbers smaller than 20,
# i.e.: 1, 3, ..., 17, 19.

sum_number = 0
for i in range(20):
    if i % 2 != 0:
        sum_number += i
        print(i, " is an odd number")
print("The sum of the odd number is: ", sum_number)
