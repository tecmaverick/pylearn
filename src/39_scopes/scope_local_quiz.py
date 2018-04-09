message="hello"

def test():
	print(message)

#what will this print?
#will print the value in global scope. This is how python will look for the variable
#will look in local scope, doesnt exists. so will look at Global scope, finds it
test()


def test1():
	message = "hi"
	print(message)


#what will this print?
#will print the value in local scope. This is how python will look for the variable
#will look in local scope, and it exists. It doesnt modify the global variable
test1()


def test2():
	message = "test2"
	def test2_1():
		print(message)

	test2_1()

#what will this print?
#will print the value in enclosing scope. This is how python will look for the variable
#will look in local scope, doesnt exist. Will look for in enclosing scope finds it there
test2()


g_counter = 1

def test3():
	g_counter = g_counter + 1
	print "g_counter: {}".format(g_counter)

#what will this print?
#will throw unbound expcetioni, we have to explicitly state python we are to modify the global variable 
#test3()


def test4():
	global g_counter
	g_counter = g_counter + 1
	print "g_counter: {}".format(g_counter)

#what will this print?
#will increment the global var by 1.
#why: will straight away link the reference to global var
test4()	


#demos global,enclosing and local vars
a_var = 'global value'

def outer():
    a_var = 'enclosed value'

    def inner():
        a_var = 'local value'
        print(a_var)

    inner()

outer()


#demo nonlocal keyword
def test5():
	my_local = "this is a local val in test5 function"
	def test5_1():
		print("before nonlocal applied - my_local: {}".format(my_local))
		#NOTE this is only available in Python 3.X and not in Python 2.x
		#nonlocal my_local
		my_local = "modified inside test5_1"
	
	print("after nonlocal applied - my_local: {}".format(my_local))
	
	test5_1()
	
#test5()
