import sys

def greetme(personname):
	print("Hello {}!!!".format(personname))

your_name = sys.argv[1]
greetme(your_name)
