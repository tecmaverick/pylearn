#decorators are functions which accepts a function and returns a function
#these allows to modify or enchance functions without changing their definition


def zero_index(f):
	def internal(*args, **kargs):
		return_val = f(*args, **kargs)
		if return_val > 0:
			return  return_val -1 
		else:
			return return_val

	return internal

a = [1,2,3,4,5]

#return value by zero index
@zero_index
def list_len(list_ref):
	return len(list_ref)

print list_len(a)
print list_len([])

