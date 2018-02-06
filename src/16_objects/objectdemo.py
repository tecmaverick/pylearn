#Py passes varaible ref. Demo
x = 100
y = x #Now both x and y points to same ref.
print "id(x) == id(y) {}".format( id(x) == id(y)) #test to check equality of identity. returns True as both vars point to same ref
print "'x is y': {}".format(x is y)  # tests quality of identity
print "x is None {}".format( x is None) # returns false

#if the value is changed, like the one below for 't', which seems like mutating, in reality it doesn't. The ids are different 
t = 10
print "t id {}:".format(id(t))
t += 1
print "t+=1 id: {}".format(id(t))

#lists are mutable objects
a = [1,2,3]
b = a # now both vars refer to the same list
print "List a == b :{}".format(a==b)
print "List a is  b :{}".format(a is b)

#here the both vars a and b point to the same list despite the value in the list changed. Whereas the 't' int assignment operation changed the ref (id) as it immutable


#demo on how  functions accepts args by ref and not by value for objects
a = [1,2,3,4,5]

def modify_int(intVal):
	intVal = 10

def modify_list(lst):
	lst.append(10)

def modify_list_ret(lst):
	lst.append(12)
	return lst

print "list a before modifying {}".format(a)
modify_list(a) 
print "list a after modifying {}".format(a)

#This demonstrates both fuction arg and return statement operates on ref rather by value
print "list a before modifying {}".format(a)
val = modify_list_ret(a)
print "list a after modifying ret {}".format(val)
print "a is val: {}".format(a is val)

#demo how functions args are pased by value for primitive datatypes like int, float, bool
b = 1
print "int b  before modifying {}".format(b)
modify_int(b) 
print "int b after modifying {}".format(b)

