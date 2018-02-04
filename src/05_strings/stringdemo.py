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

#Get substring
print "Substring Demo"
val = "HelloWorld"
val1 = val[2:5] #rturns llo
print val1

#Get first 10 string
val = "my name is abraham"
print "First 0-10  strings '{}' ".format(val[:10])

#Get instance of the text "the" in a string
#Th result returns 5, becuase 'the' in theatre will also be counter
val = "the UK is planning to buy the status of liberty at the cermoney of the queen theatre"
print "instance of 'the' in the sentence: {}".format(val.count("the"))

#Strip spaces from left and right
val = "  The data is containing spaces left and right     "
print "'{}'".format(val)
print "Striping left space: '{}'".format(val.lstrip())
print "Striping right space: '{}'".format(val.rstrip())
print "Striping right and left space: '{}'".format(val.strip())

#Capatilize words
val = "some small words. new stence starts here"
print "Capatilize words in the begining of a string: '{}'".format(val)
print val.capitalize()

#Conver to upper
val = "some lower string"
print "Converting string to upper case: {}".format(val.upper())

#Convert string to upper case
val = "ALL IN UPPER CASE CONVERTED TO LOWER CASE"
print val.upper()

#Convert list to string with space in between
val = ["this", "is", "some", "sample", "text", "which", "will"," be", "joined", "by", "space"]
print " ".join(val)

#Split string to list
val = "this is a sample string"
print "Splitting by space {}".format(val.split())
print "Splitting by 'a' {}".format(val.split("a"))

#find the very first instance of 'the' in the string
val = "welcome, the UK is planning to buy the status of liberty at the cermoney of the queen theatre"
print "Very first instace of 'the' is at index: {}".format(val.find("the"))
print "instace of 'the' after first 10 chars is at index: {}".format(val.find("the",10))


#string replace
val = "welcome, the UK is planning to buy the status of liberty at the cermoney of the queen theatre"
print "replace 'the' with 'a': {}".format(val.replace('the','a'))

#Check for alphabet, number, uppercase, lowercase, space
val = "sometext"
print "Check the string contains only alphabets: {}".format(val.isalpha())

val = "some text" #if the string contains spaces, isalpha() will report false
print "this string contains spaces. Test the string contains only alphabets: {}".format(val.isalpha())

#check value of string is lower
val = "lower"
print "Is value of the string '{}' islower: {}".format(val, val.islower())

#check value of string is upper 
val = "UPPER"
print "Is value of the string '{}' isupper: {}".format(val, val.isupper())

#check value of string is num, doesn't work for float only for int
val = "123.123"
print "Is value of the string '{}' isdigit: {}".format(val, val.isdigit())

#floats can be checked via custom function 
def isfloat(val):
	try:
		float(val)
		return True
	except ValueError:
		return False

val = "123.123"
print "Is value of the string '{}' isfloat: {}".format(val, isfloat(val))

#check value of string is num 
val = "123"
print "Is value of the string '{}' isdigit: {}".format(val, val.isdigit())

#check value of string is space 
val = " "
print "Is value of the string '{}' ispace: {}".format(val, val.isspace())

#Get character value
print "ASCII code for 'A' is: {}".format(ord("A"))

#Get character for ASCII code
print "Get char for ASCI Code 65: {}".format(chr(65))

