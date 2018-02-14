#format string the very basic one
v = "Hello, {}".format("Abraham")
print v

#format string positional params
v = "Positional params demo: Hello, {0}. Is your full name {0} {1}?".format("Abraham","Joe")
print v

#format string named params
v = "Named params demo: Hello, {fname}. Is your full name {fname} {lname}?".format(fname="Abraham",lname="Joe")
print v

#format string named params with dict
val = {"fname":"Abraham","lname":"Joe"}
v = "Named params demo: Hello, {fname}. Is your full name {fname} {lname}?".format(**val)
print v
v = "Named params demo: Hello, {0[fname]}. Is your full name {0[fname]} {0[lname]}?".format(val)
print v

#format string for objects
class Circle():
	def __init__(self,radius,name):
		self.name = name
		self.radius = radius

cir1 = Circle(3,"Alpha")
v = "Object props demo: The circle radius is: {0.radius} and the name of the circle is: {0.name}".format(cir1)
print v

#Format string from list
listdata = ["Alpha","Beta"]
v = "List first index contains {0[0]}, second index  {0[1]}".format(listdata)
print v

#format nums with zero prefix for upto 4 digits
for i in range(5):
	print "Val {:03}".format(i)

#format decimal places
print "Pi to 2 decimal places {:.2f}".format(3.14159)

#format by comma
print "Pi to 2 decimal places {:,}".format(1000000*29)

#format by comma and decimal places
print "Pi to 2 decimal places {:,.2f}".format(1000000*29)

#inplace formatting, only works with Python 3
#first_name = "John"
#last_name = "Rob"
#print (f"Hello {first_name}, {last_name}")
