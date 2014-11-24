#!/usr/bin/python
#Program to find
#sum of all numbers in list

import re
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

num = raw_input("Enter a number: ")

#sum = 0

#for num in numbers:
#	sum = sum+num

#print the sum
#print "The sum of all numbers in list is",sum

for i in numbers:
    if re.match(numbers, num):
 	print "Number found"