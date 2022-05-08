# Task 27
# In the for loop you can nest an if statement and vice vers:
# in the if statement you can nest a for loop.
# Just remember that each of the commands needs an additional 4- space indentation.
# Write this program and check how it works:

list = [3, 12, 7, 18, 21, 5, 14, 7, 8]

for i in list:
    print(i)
    if i % 2 == 0:
        print("Even")
    else:
        print("Odd")

# iterate through a list and prints the number, if a number is even print out Even, else it will print out Odd
