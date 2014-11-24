#!/usr/bin/python
def rec_fac(x):
	if x == 1:
		return 1
	else:
		return (x * rec_fac(x-1))

num = int(raw_input("Enter a number:"))
if num >= 1:
	print "facorial of",num, "is", rec_fac(num)