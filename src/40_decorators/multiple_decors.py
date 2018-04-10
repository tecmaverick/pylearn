#multiple decorators can be applied to a function
#they are evaluated in the order from bottom to top


def decorator_3(f):
	def internal(*args, **kargs):
		return_val = f(*args, **kargs)
		print "dec3:{}".format(return_val)
		return  return_val -3

	return internal


def decorator_2(f):
	def internal(*args, **kargs):
		return_val = f(*args, **kargs)
		print "dec2:{}".format(return_val)
		return  return_val -3

	return internal

def decorator_1(f):
	def internal(*args, **kargs):
		return_val = f(*args, **kargs)
		print "dec1:{}".format(return_val)
		return  return_val -1

	return internal


@decorator_3
@decorator_2
@decorator_1
def change_sign(val):
	return val * -1


change_sign(10)

