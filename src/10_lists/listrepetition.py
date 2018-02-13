#repeating a list. Creatign a list with 10 elements with value 0
data = [[1,2]]*10
print data
#modifying first element in data, will cause all 10 elements value to be modified
data[0].append(3)
print data

#init a list with fixed number of elements say 100 elements with value '0'
mylist = [0]*100
print mylist
