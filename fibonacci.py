#!/usr/bin/python
n = int(input("Enter positive integer to generate fibonacci: "))
def fib(n): #write fibonacci series upto number n
	"""Print a Fibonacci series up to n."""
	a, b = 0, 1
	while a < n:
		print a,
		a, b = b, a+b
fib(n)