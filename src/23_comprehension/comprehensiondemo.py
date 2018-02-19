import os
import glob
from pprint import pprint
from math import factorial

#Comprehensions in python are concise syntax for describing list,set, dict 
#in a delcarative or functional style

#Syntax of list comprehensions
#[expr(item) for item in iterable [optional filtering clause]]
#Example
sentence = "how are you Py developers?"
words = sentence.split()

#prints out length of each word
#this is an example of list comprehension, where the outcome is a list
x = [len(word) for word in words]
print "result: {}  type:{}".format(x,type(x))

#list comprehnesion print length of factorial 
#this prints out duplicates, which is acceptable with lists
print [len(str(factorial(num))) for num in range(10)]

#Set comprehension eliminates duplicates
print "Comprehension with sets"
print {len(str(factorial(num))) for num in range(10)}

#Dictionary comprehension
data = {"universe":"galaxies","solarsystem":"planets","continents":"counties","states":"counties"}
pprint (data)
print "-" * 30
data = {val:ky for ky,val in data.items()}
pprint (data)

#Read file sizes and print to console, via dict comprehensions
file_sizes = {os.path.realpath(p):os.stat(p).st_size 
				for p in glob.glob("*.py")}

pprint(file_sizes)


#List comprehensions with filtering predicates 
#return only values >2
x= [x+1 for x in range(10) if x>2] 
print x


#List comprehension with function are predicates
def is_even(x):
	return x % 2 == 0 

x= [x for x in range(10) if is_even(x)] 
print x
