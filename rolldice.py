#!/usr/bin/python
import random

while True:
	raw_input("Press enter to roll dice")
	num = random.randint(1,6)
	print "You got number",num
	option = raw_input("Roll dice again(y/n)")

	if option == 'n':
		break