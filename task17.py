# Write a program that test if the number stored in variable a is an even number or an odd number. The program will write the info about the parity of the number.
a = int(input("Enter a number: "))
if a % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
    