#Python uses open() method to open a file. Arguments
#file: path to file (required)
#mode: read\write\append, binary/text
#encoding: text encoding like utf-8, utf-16 ( this param only supported on Python3+)
#			default encoding of a system can be viewed using the following command
import sys
print "default ecoding: {}".format(sys.getdefaultencoding())

#writing to a file in text mode
#wt = write text
f = open("data.txt",mode="wt")
f.write("Hello world 0 \n")
f.write("Hello world 1 \n")
f.write("Hello world 2 \n")
f.close()


#reading file
#rt = read text
f = open("data.txt",mode="rt")
print f.read(5) #read 3 chars (not bytes) from the file
f.close()

#reading file line by line for loop demo
f = open("data.txt",mode="rt")
for line in f.readlines():
	print line
f.close()

#reading file line by line while loop demo
f = open("data.txt",mode="rt")
while True:
	line = f.readline()
	print "-"*10
	if not line: break
	print line
f.close()

#Seek demo
