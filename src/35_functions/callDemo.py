from resolver import DNSResolver

d = DNSResolver()

#This will inturn invoke the __call__ method

print d("amazon.com")

print d.get_host_name()
