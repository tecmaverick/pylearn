#An object can be validated whether its callable or NOT by passing it to 'callable' function
def is_even(num):
	return x % 2

print("is_even callable: {}".format(callable(is_even)))


is_odd = lambda x: x % 1
print("is_odd callable: {}".format(callable(is_odd)))

#constructor is called
print("list callable: {}".format(callable(list)))

#constructor method
print("list.append callable: {}".format(callable(list.append)))


class call_me:
	def __call__(self):
		return test()

	def test():
		print "test"


print("class call_me callable: {}".format(callable(call_me)))


#strings aren't callable
print("Strings callable: {}".format(callable("this is a test")))
