hours = [1,1.15,1.30,1.45,2,2.15,2.30,2.45,3]
temp =  [44,42,41,40,40,43,44,46,48,51,54]

#merges items in both lists into a tuple or transforms the records in the list to fields 
data_points = zip(hours, temp)

for itm in data_points:
	print itm


#the above list merge operation can be passed as an extended list using the * notation
data = [hours, temp]
print "-"*20
for data in zip(*data):
	print data


print "-"*20
data = [hours, temp]
#the above loop can even be shortened to
from pprint import pprint as pp
pp(list(zip(*data)))
