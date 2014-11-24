#!/usr/bin/python
age = int(input('How old are you? \n'))

if age <= 2:
	print "Free entry \n"
elif 2 < age < 13:
	print "child fare \n"
else:
	print "adult fare \n"