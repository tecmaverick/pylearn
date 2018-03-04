#when a module is imported, python searches for modules specified in
#sys.path directory which returns a list of locations

#sys.path when executed from Python REPL, the sys.path returns the first element as empty
#which instructs python to look for modules in present directory
#where as executing from python script, the first element wont be null

#Example:
import sys
print sys.path

#To import a module not contained in sys.path
#you can either add the path the sys.path.append(<path>)

#PYTHONPATH is a env variable which contains the exact set of values in sys.path
#Values in PYTHONPATH is added to sys.path when python us started

#PYTHONPATH follows the same format of your platform
#on windows the paths are separated by semicolons and in linux,mac by colons

#Add new path to PYTHONPATH on linux,mac
#export PYTHONPATH="/usrers/abc/data"
#after which calling python repl and printing out the sys.path will show the 
#directory added to PYTHONPATH env variable

