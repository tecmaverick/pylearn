from timeit import timeit

#The number parameter specifies the number of times the contents within the 'stmt' argument must be executed
print timeit(setup="from resolver import DNSResolver",stmt="d=DNSResolver();d('amazon.com.au')",number=1)

