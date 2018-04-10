class Trace:
	def __init__(self):
		self.enabled = True

	def __call__(self, f):
		def wrap(*args,**kargs):
			if self.enabled:
				print ("function invoked: {}({},{})".format(f.__name__, args, kargs))
			return f(*args, **kargs)
		return wrap


tracer = Trace()

@tracer
def add(fno, sno):
	return fno + sno

add(1,2)
add(10,12)

tracer.enabled = alse
add(100,200)
