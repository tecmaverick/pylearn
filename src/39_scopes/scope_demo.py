#LEGB Rule
#Local, enlcosing, global, built-in

my_global_var = "this is global"

def outer():
	outer_msg = "outer msg"
	val1 = {"test":"val"}
	def inner():
		#here the variables in the enclosing scope in outer() function
		#is closed over by referencing the vairables referred
		#the enclosed variables can be viewed by printing the references
		#fnref.__closure__
		#to view each closed variable
		#fnref.__closure__[0].cell_contents
		print outer_msg
		print val1
		global my_global_var
		inner_msg = "inner msg"
		my_global_var = "12"
	
	return inner

print ("global: {}".format(globals()))
print ("locals: {}".format(locals()))
print ("calling outer")
inner = outer()

print ("calling inner")
print ("global var before modification:{}".format(my_global_var))
inner()
print ("global var after modification:{}".format(my_global_var))

print ("is outer a closure:{}".format(outer.__closure__))
print ("is inner a closure:{}".format(inner.__closure__))

#Closures allows implementing of features like
#Callback function reference
#Function factories
