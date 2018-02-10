numbers = [1,2,3,4]
names = ["alhpa","beta","gamma"]

print "Element 1 in names is {}".format(names[1])

#updating list element with new value
names[1] = "Zeta"
print "Updated element 1 in names to {}".format(names[1])


#A list can contain hetrogenous data types includng str, int, float, bool, nested lists etc
misc = [1,"two",3.3,4e2, True,["A","B"]]

print "elements in hetrogenous list"
for elm in misc:
	print str(elm) + " " + str(type(elm))
	#print elm + " " + str(type(elm))


#Appending items to empty list
emptylist = []
emptylist.append(1)
emptylist.append("One")
emptylist.append(1.222)
emptylist.append(True)
emptylist.append([0,9])

print emptylist


#Init list with string
username = list("abraham")
print "Username list val: " + str(username)
print "# elements in list username is:{}".format(len(username))

for chr in username:
	print chr

#Delete entry from list
print "deleting first element '0' from data"
data = [1,2,3,4,5]
del data[0]
print (data)

#delete items from a list by element value rather by index
data = ["one","two","three","four","four","five"]
print "deleting element with the value 'two' and 'four' from list {}".format(data)
data.remove("two")
data.remove("four")
print "after deleting item value two from list {}".format(data)



data = [1,2,3,4,5]

#join list
lista = [1,2,3]
listb = [4,5,6]
listc = lista + listb
print "joining two lists lista {} and listb {} = listc {}".format(lista, listb,listc)

#sort list
data = [25,4,71,11,3,8,2,6,99,44,23,54,75,1,48]
print "unsorted list {}".format(data)
data.sort()
print "sorted list {}".format(data)

#merge unique items from two lists
a = [1,2,3,4,5]
b = [3,4,5,6,7,8,9,10]
c = list(set(a + b)) 
print "merging two lists a = {} b = {} for generating unique items c = {}".format(a,b,c)

#add two lists
a = ["alpha","beta"]
b = ["alpha","gamma","tango"]
c = a + b 
print "list  a + list b = {}".format(c)

#get item from list by index
a = ["one","two","three"]
print "Accessing seond eleent in a list  by index: a[1] = {}".format(a[1])

#Search items in list
some_data = [1,"help",34,"name",90,"val"]
print "is 90 in some_data {}: {}".format(some_data,90 in some_data)

#Get element from the last
k = [0,1,2,3,4,5,6,7,8,9,10]
print "list k: {}".format(k)
print "Last item in the list is k[-1] :{}".format(k[-1])
print "Fifth element from the last k[-5] :{}".format(k[-5])
print "Get items from second element to fifth element k[2:5] :{}".format(k[2:5])
print "Get items from second element to fifth element from last  k[2:-5] :{}".format(k[2:-5])
print "Get items from second element to last k[2:] :{}".format(k[2:])
print "Get items from very first element to third k[:3] :{}".format(k[:3])
print "Get all items from list k[:] :{}".format(k[:])

#Copy lists, when a list is copied it does a shallow copy, which means the objects within both the list 
#refernce the same variables
dictData = {"name":"abraham"}
listdata = [1,2,3]
list1 = ["Alpha",dictData, listdata]
# this is the widely used method by py devs for copying list. This however doesn't work with generators
list2 = list1[:]
print "list1 is list2 {}".format(list1 is list2) #false because both ids are different
print "list1 == list2 {}".format(list1 == list2) #true because both lists refer to the same values

print "modifying list2 1st element from 'abraham' to 'beta'"
list2[1]["name"] = "beta"

print "here the change is reflected in both lists"
print "list1 values:{} \nlist2 values:{}".format(list1, list2)

print "different ways to copy lists. Note all these does a shallow copy"
#newlist = list1.copy()
newlist = list1[:]

#this is the preferred method, as the ctor allows accpeting any datastruct capable over iterable series of source and not just lists.
#and it works with generators
newlist = list(list1)

