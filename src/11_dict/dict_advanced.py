#import pretty print
from pprint import pprint as pp
 
#in dict keys must be unique
countries_captial = {"Australia":"Sydney","India":"Delhi","Pakistan":"Karachi","USA":"Washington"} 
print countries_captial 

#NOTE: 
# - In a dict, the keys must be immutable, like strings numbers and tuples will work however lists are not
# - Value in a dict can be mutable
# - Order of keys in a dict can be of arbitrary order


#converting list to dict
data = [("Alpha","12"),("Beta",11),("Tango",15)]
dict1 = dict(data)
print "Word Converted to dict: {}".format(dict1)

#creating dict from keyword args
data = dict(a="1",b="hi",c="13",d="dog",e=12.23,f=55,g=12.23,h=55.23)
print "dict from keyword args:{}".format(data)

#Copying dict is a shallow copy operation
mydata = {"weightrange":[12,13],"heighrange":[1,2]}
data = mydata.copy()

#add new element to the list, this will alter any references to the elment in the dict which its copied from 
data["weightrange"].append(11)
print "original data:{}".format(mydata) 
print "copied data:{}".format(data)
print "compare both dict 'weightrange' element, whether both points to the same object: {}".format(data["weightrange"] is mydata["weightrange"]) 
print "compare both dict 'weightrange' element, whether both points to the same value: {}".format(data["weightrange"] == mydata["weightrange"]) 

#updating dictionary from other dict
colorcodes = {"house":"red","garden":"green","fence":"black"}
newcolorcodes = {"fence":"white"}
print "OldColorCode:{} \n NewColorCode:{}".format(colorcodes,newcolorcodes)
colorcodes.update(newcolorcodes)
print "updated color codes. NewColorCode:{}".format(newcolorcodes)

#iterating over dict key and value
for color in colorcodes:
	print "Key:{} ==> Value:{}".format(color, colorcodes[color])

#iterating over just the dict value, without causing the values to be copied. But this doesn't provide any way to access keys
for color in colorcodes.values():
	print "Value:{}".format(color)

#iterating over just the dict keys
for key in colorcodes.keys():
	print "key:{}".format(key)

#iterating over just the dict keys and values in tangem
for key,val in colorcodes.items():
	print "key:{} val:{}".format(key,val)


#check key exists in dict
currency = {"USA":"Dollar","Russia":"Ruble","Japan":"Yen"}
print "'Japan' exists in currency dict: {}".format("Japan" in currency)

#pretty print dict
data = dict(a="1",b="hi",c="13",d="dog",e=12.23,f=55,g=12.23,h=55.23)
pp(data)
