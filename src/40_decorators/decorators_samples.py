#{"1":"number","2":"string"}
#this mean the first arg must be number and second arg must be a string

def validate_args(dict_args):
	def validator(f):
		def wrap(*args):
			for dict_arg in dict_args:
				curr_val = args[int(dict_arg)]
				if dict_args[dict_arg] == "number" and type(curr_val).__name__ != "int":
					raise ValueError("invalid data type. Expected Int")
				elif dict_args[dict_arg] == "string" and type(curr_val).__name__ != "str":
					raise ValueError("invalid data type. Expected string")
	 			else:
					pass	
			return f(*args)
		return wrap
	return validator


@validate_args({"0":"number","1":"number"})
def add(fno,sno):
	print fno + sno

@validate_args({"0":"string","1":"string"})
def say_hello(greet_word, person_name):
	print "{} {}".format(greet_word, person_name)

add(1,2)

say_hello("Hello","Pearsow")
