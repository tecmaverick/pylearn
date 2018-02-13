#python sets demo
#set is an un-ordered list of unique elments\items which are immutable
#duplicates are discarded
#best used for Algebra set operations like union, differences, intersections
x = {1,2,3,1,10,2,3,4,5,6,7,8,9,10}
print x

#create empty set
#creating set with myset = {} will instantiate a dictionary
myset = set()
print type(myset)

#init a set from list
myset = set([11,23,34,45,234,2,11,324,2,23,34])
print myset

#iterating thru set. Here the output is not ordered as items inserted to the list
for val in myset:
	print val

#Check item exists in set
print "11 exists in myset:{}".format(11 in myset)

#Add single item to set
myset.add(1000)
print "New item in set:{}".format(myset)

#Adding duplicate elments to a set wont throw an error, instead its simply discarded
myset.add(1000)

#adding multiple items to set
myset.update([1001,3002,1234,2342,42,2345])
print myset

#removing element from set
#remove() method only works if the element provided exists, else throws KeyError exception
myset.remove(1001)

#safely removing elements from a set. This method always succeeds 
myset.discard(10101)

#copy sets. Does a shallow copy of the objects
mynewset = myset.copy()

#Algebra operations demo
andrew_visited_places = {"usa","china","uk","india","australia","france","spain","brazil"}
philip_visited_places = {"canada","china","india","australia","greece","spain","brazil","israel"}
john_visited_places = {"mexico","japan","malaysia","india","singapore","srilanka","spain","brazil"}

print "Places visited by John and Andrew:{}".format(john_visited_places.union(andrew_visited_places))
print "Places visited in common by John and Andrew:{}".format(john_visited_places.intersection(andrew_visited_places))
print "Places visited only by John and not by Andrew:{}".format(john_visited_places.difference(andrew_visited_places))
print "Places visited only by John and not by Andrew:{}".format(john_visited_places.difference(andrew_visited_places))
 
