#!/usr/bin/python
#program to check if a string is palindrom or not

#take input from user
my_string = raw_input("Enter a string: ")
#print my_string

#make it suitable for caseless comparison
my_string = my_string.lower()

#reverse input string
rev_string = reversed(my_string)

#compare string with reverse string
if list(my_string) == list(rev_string):
	print "string %s is a palindrome." % my_string

else:
	print "string %s is not a palindrome." % my_string	
