# A Python iterator object must implement two special methods,
# __iter__() and __next__(), collectively called the iterator protocol
#  On reaching the end, and in subsequent calls, it must raise StopIteration

data = [1, 2, 3]
iterator = iter(data)
print(next(iterator))  # prints 1
print(next(iterator))  # prints 2
print(next(iterator))  # prints 3
# print(next(iterator))  # No data hence exception StopIteration is raised

iterator = iter(data)
for elm in iterator:
    print(elm)
