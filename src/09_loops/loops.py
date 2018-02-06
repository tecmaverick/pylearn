#for loop
for i in range(10):
	print("Itm: {}".format(i))


#Loop until the expression is true
counter = 10
while counter != 0:
	print "Counter: " + str(counter)
	counter = counter - 1


#Break out from loop
for k in range(10):
	if k == 3:
		print "exiting loop"
		break;

	print "inside loop " + str(k)


val = 17
while True:
	#If value is perfectly divisble by 9 exit the loop
	if val % 9 == 0:
		print "Val: {} divisble by 9".format(val)
		break

	val = val - 1
