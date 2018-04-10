import functools

def test_decor(f):
	def internal(*args, **kargs):
		return_val = f(*args, **kargs)
		return return_val

	return internal


@test_decor
def hello(name):
	"Prints hello"
	print "Hello {}".format(name)

h = hello
h("Andrew")

#This prints outs the decorator name "internal" rather the function name "hello"
print h.__name__

#doesnt print the DocString in hello function
print help(h)

#-------------------------------------------------------------------------------
#to fix the overwritten metadata, you can explicitly assing these props manually
def test_decor1(f):
	def internal(*args, **kargs):
		return_val = f(*args, **kargs)
		return return_val

	internal.__name__ = f.__name__
	internal.__doc__ = f.__doc__
	return internal

@test_decor1
def greet(person):
	"Greets person"
	print "Greetings {}".format(person)

g = greet

#prints the name of the function greet instead of internal
print g.__name__

#prints the DocString associated with the function
print g.__doc__
#----------------------------------------------------------------------------------

#inbult functions in python to copy all the meta data for wrapper functions

def test_decor2(f):
	@functools.wraps(f)
	def internal(*args, **kargs):
		return_val = f(*args, **kargs)
		return return_val

	return internal

@test_decor2
def bye(person):
	"bye person"
	print "Greetings {}".format(person)

b = bye

#prints the function name instead of wrapper name
print b.__name__
@prints the docstring of the function
print b.__doc__
#----------------------------------------------------------------------------------


