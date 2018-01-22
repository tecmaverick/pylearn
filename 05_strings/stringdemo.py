import math

val = math.factorial(5)

#Convert to string using str() and get the length of the string using len() function
print "String length of factorial {} is {}".format(5,len(str(val)))


someval = "AlphaBeta"
print ("String length of val {} is {}".format(someval,len(someval)))

#multiline strings double quotes
val = """ Hello
world.
This is in a new lin...
"""

print "Multi-line demo" + val



#multiline strings single quotes
val = '''
Single quote 
multi line string
'''
print val


#escape sequence
val = "This string contains spl chars \t tab, doublequotes \" backslash \\ "
print val

#backticks are depricated in python. While the followin line will throw an error hence commenting out
#val = `some text`
#print val

#Raw string, allows to author strings without escaping spl. characters. Best suited while creating reg expressions
val = r"C:\data\source.txt"
print "Raw  string demo: " + val

#Creating string via str() function
val = str(123)
print str(type(val)) + " " + val

#Get length of a string
val = "hello world"
print "length of \"{}\" is {}".format(val,len(val))
print "2 char in string \"{}\" is {}".format(val,val[1])
