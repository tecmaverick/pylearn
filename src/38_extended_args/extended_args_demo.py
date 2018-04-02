#extended argument syntax
#this allows functions to receive variable number of positional arguments or named arguments
#example for variable number of positional args
print "one","two"


#format 
def add_nums(*args):
	print type(args) #returns tuple
	print(args)

	result = 0
	for arg in args:
		result = result + arg

	print result	
	
add_nums(1,2,3,4,5)

#keyword args
def keyword_args(name, **kargs):
	print(kargs)
	print(type(kargs)


keyword_args(12,fno=1,sno=2,ops="*")
