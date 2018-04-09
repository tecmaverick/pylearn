#class as decotrators

class invoke_counter():
	def __init__(self,func):
		self.counter = 0
		self.func = func

	def __call__(self, *args, **kargs):
		self.counter += 1
		return self.func(*args, **kargs)


#this creates a new instance
@invoke_counter
def log_metric(val, metric):
	print("val:{} metric:{}".format(val,metric))

log_metric(152,"pipes")
log_metric(123,"network")
log_metric(234,"pipes")

print "invokes:{} ".format(log_metric.counter)

