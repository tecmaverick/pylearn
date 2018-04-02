import socket 


class DNSResolver():

	
	#this will make the class a callable instance, by maintaining states between each different call
	#with this the class can be called like this
	#d = DNSResolver()
	#d("amazon.com.au")
	def __call__(self, hostname):
		self._hostname = hostname
		return socket.gethostbyname(hostname)

	def get_host_name(self):
		return self._hostname
