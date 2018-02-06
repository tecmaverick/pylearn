#If the file is imported via an import statemtn, the __name__ print the name of the .py filename, however if the same mymodule.py is executed via 'python mymodule.py' them '__main_' will be displayed

def sayhello(name):
	print "Hello %s" % name

def saygoodbye(name):
	print "Goodbye  %s" % name

#print the name of module
print __name__
