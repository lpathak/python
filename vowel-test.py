#!/usr/bin/python
vowels = "aeiouAEIOU"

while True:
	v = raw_input("Enter string to check if its  a vowel: ")
	if v in vowels:
		break
	print "This is not a vowel. Please try again"
print "Thank you this is vowel!",v