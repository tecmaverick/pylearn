import time

#here the second param is optional and its assigned a default value
def display_banner(message, border="-"):
	border = border * len(message)
	print "{0}\n{1}\n{0}".format(border,message)


#NOTE: The default values are evalueted when the def\function is evaluted and doesnt change
def display_datetime(message, msg_datetime=time.ctime()):
	print "Message printed at {0}\n{1}".format(msg_datetime,message)

display_banner("Hellooo this is my banner text!!!")

#The arguments can be passed in any position if the labels are prefixed
display_banner(border="*",message="some new message!!")

#Here the display_datetime function will show the value same all the time, even if its called after few seconds, minutes. This is because the default argument value got evaluted when the fn 
display_datetime("hellooo!!!")

#BestPractice: Alwsy use immutable types like string or int or None  for optional argument default value, else it can create bugs like the one demoed below
def place(names=[]):
	names.append("myplace")
	return "-".join(names)

print place()
print place()
print place()
#-----------------------------------

def place_fix(names=None):
	if names is None:
		names = []

	names.append("myplace")
	return "-".join(names)
	
print "\nAfter fix:" + "*" * 100
print place_fix()
print place_fix()
print place_fix()

#You can view the name,type, docstring of a module or function via the foll commands in python REPL
#import functiondemo
#print type(functiondemo) #prints module
#print (functiondemo.display_banner.__name__) prints the name of the function
#print (functiondemo.display_banner.__doc__) prints the docstring  of the function

