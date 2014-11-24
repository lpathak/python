#!/usr/bin/python
#list of integers
digits = [1,2,3,5,0,7,8,9,11,14,15]
number = raw_input("Enter some number: ")

for i in digits:
	if number == i:
		print "Digit is in the list"
		break
else:
	print "Digit is not in the list"