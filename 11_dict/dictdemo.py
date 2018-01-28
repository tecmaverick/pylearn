#telephone number dictionary
telnums = {"aron":"122-23123-2","ben":"3039-23423-12","sam":"09-342-123123"}

print "Arons Tel #: {}".format(telnums["aron"])

#Update dictionary key
telnums["aron"] = "023-111-13232"

print "Arons New Tel #: {}".format(telnums["aron"])

#Add new entry to dict
telnums["ken"] = "3-23123-34"

print "Kens Tel #: {}".format(telnums["ken"])

print "Elements in telnums dict {}".format(str(telnums))

#iterate thru all elems in dict
for keyVal in telnums:
	print "{} # is: {}".format(keyVal, telnums[keyVal])

