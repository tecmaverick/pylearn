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
