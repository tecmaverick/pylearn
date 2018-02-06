"""
Python module for basic arithemtic operations
"""

#Documenting code using docstrings for self documenting methods and classes\modules
#To view the documentation, open python REPL and enter the following
#1.Change to the dir where codedoc.py is located
#2.switch to python prompt
#3.import codedoc
#4.help(codedoc.add_num)
#5.help(codedoc)

def add_num(fno, sno):
	"""
	Add two numbers and return result

	Args:
		fno - Accepts first int number to add
		sno - Accepts second int number to add

	Returns:
		sum of the two ints via two arguments
	"""
	
	return int(fno) + int(sno)



