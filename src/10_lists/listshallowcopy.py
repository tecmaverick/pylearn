
#copying list demo. Here a and b references the same list.
#any change made to eiter a or b will refect in both varibales
#in python variables are tags atttached to references\ids
a = [1,2,3]
b = a
print "Ref of a:{} and b:{}".format(id(a),id(b))
c = list(a)
print "Ref of c:{} copied using list ctor".format(id(c))

#shallow copy demo
data = [[1,2],{"name":"abraham"},(1,2,3,)]
print "data list: {}".format(data)
newdata = list(data) #copy the list
print "newdat copied list: {}".format(newdata)

#now test for reference quality
print "data is newdata: {}".format(data is newdata)
print "id of both vars are same. data(id:{})  newdata:(id:{})".format(id(data), id(newdata))

#test for value equality
print "data == newdata: {}".format(data == newdata)

#change the contents in 'data' list see if it reflect in copied list 'newdata' list
print "insert new elm value 3 to first elm in the data list"
data[0].append(3)

print "data list: {} \nnewdata:{}".format(data, newdata)
print "data list first elemnt id ==  newdata first elem id: {}".format(id(data[0]) == id(newdata[0]))

