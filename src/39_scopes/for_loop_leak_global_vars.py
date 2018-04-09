itm = 10
lst = [1,2,3,4,5]

print "value of itm:{}".format(itm)

for itm in lst:
	print itm

#here the var from for loop leaked into global var
print "value of itm:{}".format(itm)

