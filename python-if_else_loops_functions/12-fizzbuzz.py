#!/usr/bin/python3
def fizzbuzz():
	for i in range(101):
		if i % 5 == 0 and i % 3 == 0:
			print("FizzBuzz", end=" ")
		elif i % 3 == 0:
			print("fizz", end=" ")
		elif i % 5 == 0:
			print("buzz", end=" ")
		else:
			print(i, end=" ")
