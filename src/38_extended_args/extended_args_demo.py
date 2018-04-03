#extended argument syntax
#this allows functions to receive variable number of positional arguments or named arguments
#example for variable positional args, which accepts variable number of argument
print "one","two"

#example of variable keyword args, which accepts variable number of keyword aegs
val = "hello {a}, {b}".format(a="Alpha",b="Good Morning!!!")
print val

#*args returns tuple, and are optional. The *args should precede **kargs. Any args passed after *args must be passed as **kargs
#else it will lead to type error
#**kargs returns dict, and are optional. If present these must be the last parameters, else an InvalidSyntax error will be thrown 

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
def keyword_args(name, *args, **kargs):
	print("name: {}".format(name))
	print("type: {}".format(type(args)))
	print("Args:{}".format(args))
	print("Keyword Args:{}".format(kargs))
	print("keyword args type: {}".format(type(kargs)))

keyword_args(12,fno=1,sno=2,ops="*")
#keyword_args(12,1,2,3,fno=1,sno=2,ops="*")

#iterating *args with iter function
def add_nums(*args):
	print "Adding nums with iter"
	itr = iter(args)
	itm = 0
	
	while True:
		try:
			val = next(itr)
			itm += val 
		except StopIteration:
			break
		else:
			print val

	print "Sum:{}".format(itm)


add_nums(1,2,3)

#Valid calls
#def fn(fno, *args, **kargs)

#invalid calls
#def fn(**kargs, *args)
#def fn(**kargs, fno, sno)
#def fn(fno,sno,**kargs,defaultval)
#def fn(*args, fno, sno, **kargs)

#pass values to args parameter via tuple
data = (1,2,3,4,5)
def nums(fno,sno,*args):
	print fno, sno, args

#tuple unpacking. Here the first 2 params will be mapped to first two args
# and last three will be passed as tuple args 
nums(*data)

#dict unpacking
color1 = dict(red=1,green=2,blue=3,yellow=4,white=5)
color = {"red":"1","green":"2","blue":"3","yellow":"4","white":"5"}
def show_colors(red,green,blue,**kw_args):
	print red,green,blue,kw_args

show_colors(**color)
show_colors(**color1)

