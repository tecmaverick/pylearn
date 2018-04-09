#from mymath import mymath
#from yourmath import yourmath

#Note importing with wildcard will case global vars to be overwritten
#always specify refer by namespace
from mymath import *
from yourmath import * 

print "loaded modules: {}\n".format(globals())

#the max_len global variable is overwritten by the recent import
#which is yourmath which is having a value of 100
print "yourmath.max_len: {}".format(max_len)
print "mymath.max_len: {}".format(max_len)

print mymath.ops1(10)
print yourmath.ops2(10)
