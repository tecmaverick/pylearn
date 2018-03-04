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

#extend list
lista = [1,2,3]
listb = [4,5,6]
listb += lista
print "Contact list with listb += lista: {}".format(listb)

#extend() method can be used on any datatype which supports iteration
listb.extend([90,91,02])
print "Extended list:{} ".format(listb)

#sort list
data = [25,4,71,11,3,8,2,6,99,44,23,54,75,1,48]
print "unsorted list {}".format(data)
data.sort()
print "sorted list {}".format(data)

#reverse sort using sort method
data = [25,4,71,11,3,8,2,6,99,44,23,54,75,1,48]
print "unsorted list {}".format(data)
data.sort(reverse=True)
print "decensing sort:{}".format(data)

#reverse sort
print "unsorted list {}".format(data)
data.reverse()
print "reversed list {}".format(data)

#sort by length
data = ["snozeeeeee","the","I","owner","countries"]
print "list {}".format(data)
data.sort(key=len)
print "sort by word length list {}".format(data)
print "-" * 30

#sort list using the sorted function, works for any type which is iteratable
#The sorted() function doest modify the original obj, instead it returns a new ref
data = [25,4,71,11,3,8,2,6,99,44,23,54,75,1,48]
print "unsorted list {}".format(data)
data1 = sorted(data)
print "sorted list using sorted() function {}".format(data1)
print "-" * 30

#reverse sort using sort method
data = [25,4,71,11,3,8,2,6,99,44,23,54,75,1,48]
print "unsorted list {}".format(data)
data1 = reversed(data)
#note the list() ctor is used to iterate through the result
print "reversed list using reversed function :{}".format(list(data1))
print "-" * 30

#merge unique items from two lists
a = [1,2,3,4,5]
b = [3,4,5,6,7,8,9,10]
c = list(set(a + b)) 
print "merging two lists a = {} b = {} for generating unique items c = {}".format(a,b,c)
print "-" * 30


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

#remove element from list using del 
d = "the quick brown fox jumped over the lazy dag".split(" ")
print d
#remove the element "fox"
del d[d.index("fox")]
print "Removed element 'fox' via del command. result: {}".format(d)

#remove item from list using the remove method
d.remove("the")
print "Removed element 'the' via remove() command. result: {}".format(d)

#insert new element at a specific index
newelm = "tiger"
#insrt after tiger i.e. +1 from the position where 'brown' elm is located
d.insert(d.index("brown")+1,newelm)
print "inserting elm 'tiger' after brown. Result:{}".format(d)


#extend vs append
#extend method adds items to the list
a = [1,2]
b = [3,4]
a.extend(b) 
print(b) #outputs [1,2,3,4]

#append method inserts given object in the append method argument to the end of the list 
a = [1,2]
b = [3,4]
a.append(b) 
print(b) #outputs [1,2,[3,4]]


