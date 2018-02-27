#!/usr/bin/python3

#Packages in python are way to organize modules in Python
#Packages are directories where as modules are files
#package has __path__ property to view the location 
#module has __file__ property to view the location of the file

#Example

#PackageA
#--> ModuleA 
#--> PackageB
#-----> Module1 (nested in PackageB)

#Demo
#in Python REPL enter

import urllib
import urllib.request

print (type(urllib))
print (type(urllib.request))

#Prints out the directory where the package is located
print (urllib.__path__)

#As request is a module, which physically is a file
#hence trying to print the __path__ will fail
#instead modules has __file__ property which 
#print out the module file location

try:
	print ("urllib.request path:{}".format(urllib.request.__path__))
except Exception as  e:
	print("Err while fetching __path__" + str(e))



print ("urllib.request path:{}".format(urllib.request.__file__))
