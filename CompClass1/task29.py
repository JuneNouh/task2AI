# Task 29
# There is a positive integer number x. Using a for loop check if the number x is a prime number. Prime number has exactly two positive divisors: 1 and x.
# Prime numbers: 3, 5, 7, 11, ...


# number to check
x = int(input("Please enter a number: "))
# Or you can just assign the number to a variable
# x = 29
# declare the help flag
flag = False

# prime numbers are greater than 1
if x > 1:
    # check for factors
    for i in range(2, x):
        if (x % i) == 0:
            # looking for the factor, if tit found set the flag to true
            flag = True
            # break from the loop
            break

# if the flag is true means that it is not a prime number
if flag:
    print(x, "is not a prime number")
else:
    print(x, "is a prime number")
