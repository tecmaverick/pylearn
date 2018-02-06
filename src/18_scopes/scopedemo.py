count_val = 10

def get_count(val):
	count_val =   val
	return count_val

print "Count is {}".format(get_count(1))
print "Count_val {} ".format(count_val)

#Use global keyword to access global variables within function scope
def modify_count(val):
	global count_val
	count_val  =   val

modify_count(1000)
print "Count_val {} ".format(count_val)


