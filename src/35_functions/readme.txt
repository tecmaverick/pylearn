functional args comes in two flavour positional and keywords

positional args demo
#--------------------------
def sum(fno,sno):
	return fno + sno

#here the 12 is passed as positional arg and 10 is passed as keyword arg
sum(12, sno= 10)


default arguments
def say_hello(name, greeting="Hello"):
	print greeting + " " + hello

say_hello("Abe") #prints Hello Abe
say_hello("Abe","Good morning") #prints Good morning Abe

#---------------------------

In python function are first class, i.e. they can be passed around like any other object

example:

def hello_world():
	print "Hello World"

#this shows the id\address of the object.
hello_world #prints <function resolve at 0x10ffa1410>
id(hello_world) #prints out the hexadecimal number of the memory address


#-----------------------------


