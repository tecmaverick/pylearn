#simple tuple
x = (1,2,3)
print type(x) #prints tuple

#tuples are immutable data strucs. The foll assignment operation will fail
#x[0] = 100

#concat two tuples
y = x + (7,8,9)
print y

#get length of a tuple
print "Length of tupe x: {}".format(len(x))

#tuple can contain multiple data types
hetro_tuple = (1,"alpha",3.14,[1,2,3],True)

#print all items in a tuple
for itm in hetro_tuple:
	print itm

#nested tuple
nested_tuple = ((1,2,3),(4,5,6),(7,8,9))
print nested_tuple[0][1] #prints 2

#single element tuple
single_elm = (12) #NOTE: this will cause python to interpret it as int rather tuple
print type(single_elm)

#creating single elm tuple
single_elm = (12,) #NOTE: the comma at the end of the first element, this will force python to convert it as tuple 
print type(single_elm)

#creating empty tuple
empty_tuple = ()
print "Empty tuple: " + str(type(empty_tuple))


#return multiple results from a function via tuple
def minmax(lst):
	return max(lst),min(lst)

lst = [4,3,77,6,900,432,12,76]
maxval,minval = minmax(lst)
print "In list {} min is {} and max {}".format(lst,minval,maxval)

#tuple unpacking only works with tuples and with other data structs
(a,(b,(c,d))) = (1,(2,(3,4)))
print "tuple unpacking: %s %s %s %s" % (a,b,c,d)


#variable swap
a = "first"
b = "second"
print "a=%s b=%s" % (a,b)
a,b = b,a 
print "after swaping: a=%s b=%s" % (a,b)

#create tuple from existing obects. Eg list to tuple
mytuple = tuple([1,2,3])
print mytuple

#string to tuple
mytuple = tuple("hello")
print mytuple


#searching for elements in tuple
sample_tuple = (23,345,53,23,1,657,989,07,6,)
print "is 6 in sample_tuple {}: {}".format(sample_tuple, 6 in sample_tuple)
print "is 6 not in sample_tuple {}: {}".format(sample_tuple,6 not in sample_tuple)

