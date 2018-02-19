#the Iterable objects can be passed to the built-in 
#iter() function to get an iterator
#iterator = iter(iterable)

#Iterator objects can be passed to the built-in 
#next() function to fecth next item
#item = next(iterator)

data = ["white","black","red","green","blue","yellow"]
iterator = iter(data)

for idx  in range(len(data)):
	print next(iterator)

#note: calling next after the last element will raise the StopIteration exception 
#for loop identifies the end of iterable object, when it encounters the StopIteration exception

#Generators in Python provide iterable sequences,
#these seq are lazyily evaluated.
#This allows modelling streams of data with no definite end
#Generators are best suited for stream processing, or for use case like
#1.Just in time compoutation
#2.Infinite sequence
#3.Sensor redaring
#4.Math series
#5.Massive files

#Example
def generator_demo():
	yield 1
	yield 2
	yield 3 
	yield 4 
	yield 5 
	return

itr = generator_demo()
print "Generator demo"
for i in range(3):
	print next(itr)

#Each generator has a different ref, and can be iterated independently
i1 = generator_demo()
i2 = generator_demo()
print "i1:{}  i2:{}".format(i1,i2)
print "i1 is i2:{}".format(i1 is i2)

for i in range(6):
	if i % 2 == 0:
		print "i1: {} ".format(next(i1))
	else:
		print "i2: {}".format(next(i2))


#stateful generators
#can maintain 	state in local variables
#can dbug generator execution
def take_items(iterable,count):
	counter = 0
	for itm in iterable:
		if counter == count:
			return
		
		counter += 1
		yield itm 


data = [1,2,3,4,5,6,7,8,9,10]
print "getting first 5 items"


for i in take_items(data, 5):
	print i


def take_even_items(iterable,count):
	counter = 0
	for itm in iterable:
		if counter == count:
			return
		counter += 1
		
		if itm % 2 != 0 :
			continue

		yield itm 

print "Getting even number via generator function"
for i in take_even_items(data, 5):
	print i


#Generator comprehensions are similar to list coprehensions, except they use 
#parathensis () instead of brackets []
#Syntax:
#(expr(item) for item in iterable)
#Example - here the values aren't generated, isntead only the spec is captured:

x = (x*x for x in range(100))


#Force Evaluation of the generateror using the list constructor
q = list(x)
print "generator comprehension: {} ".format(q)

#re-invoking the generator will return empty list as the values were already returned an
#looped by the previous list function
#NOTE: Generators are single use objects

q = list(x)
print "generator comprehension: {} ".format(q)


#Generate sum of values from 1 to 10 using generators
def triangular_number(val):
	sum = 0
	for i in range(1,val):
		sum +=i
		yield sum
	return

sum = triangular_number(10) 
print next(sum)
print next(sum)
print next(sum)
print list(sum)

