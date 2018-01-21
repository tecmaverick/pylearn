valInt = 10
#prints int
print type(valInt)

valDecimal = 10.12
#prints float
print type(valDecimal)

valBool = True
#prints bool
print type(valBool)

valNone = None
#print None
print type(valNone)

#Binary vaalue base2
valBinary = 0b10
#print the value in Base10
print int(str(valBinary),10)


#Oct value base8
valOct = 0o10
#print the value in Base10
print int(str(valOct),10)

#Hex value base16
valHex = 0x10
#print the value in Base10
print int(str(valHex),10)


#Covnert string to int
strVal = "123"
print type(int(strVal))

#Convert float to int
print int(3.5)

#Convert 10 to base3
print int("10",3)

#Scientific notation. 3 times 10 to the power of 2 (3*10**2) 
val = 3e2
print val

#Convert int to flot
print float(5)

#convert string to float
print float("23.32")

#Special floating point value nan
print float("nan")

#Special floating point value +infinityn
print float("inf")

#Special floating point value -infinity
print float("-inf")


#convert to bool. Every value other than zero will be parsed to bool
print bool(0) #report false
print bool(0.3) #report true
print bool(1) #report true
print bool(2) #report true
print bool(-1) #report true

#empty list reprots as false
print bool([]) #reports false
print bool([1,2,3]) #reports true

#empty string reports as false
print bool("") #report false
print bool("hello") #reports true

print
