#!/usr/bin/python
# Program to show
# the control flow
# when using else block
# in a for loop

# a list of digit
digits = [0,1,2,3,4,5,6,7,8,9]

# take input from user
input_digit = int(input("Enter a digit: "))

# search the input digit in our list
for i in digits:
    if input_digit == i:
        print("Digit is in the list")
        break
else:
    print("Digit not found in list")
