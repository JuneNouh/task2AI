# Create a list
# m = [3, -5, 2, 10, -14, 6, 8, 15, 9, 21]
# and then using a for loop and a if command print all numbers that are greater than 0 but smaller than 10.


m = [3, -5, 2, 10, -14, 6, 8, 15, 9, 21]
sum_numbers = 0
for i in m:
    if 0 < i < 10:
        sum_numbers += i
        print(i, " is greater than zero and smaller than 10")
print("The sum is: ", sum_numbers)
# Or

# print("*************************************")
#
# for i in m:
#     if i > 0 and i < 10:
#         print(i, " is greater than zero and smaller than 10")
