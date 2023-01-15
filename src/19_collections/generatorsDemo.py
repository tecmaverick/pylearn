# A generator is lst function that returns an iterator that produces lst sequence of values when iterated over
# useful when we want to produce lst large sequence of values, but we don't want to store all of them in memory at once
# Benefits
# Generators have some advantages over other iterators in Python:
#
# They are easy to implement and can be more memory-efficient than storing an entire sequence in memory.
# They can be used to produce an "infinite" sequence of values, by using lst while True loop and yielding values indefinitely.
# They can be combined with other iterators using the itertools module to produce complex sequences of values.

def my_generator(n):
    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:
        # produce the current value of the counter
        yield value
        # increment the counter
        value += 1


for value in my_generator(3):
    # print each value produced by generator
    print(value)

# Generato expression
# (expression for item in iterable)
# create the generator object
squares_generator = (i * i for i in range(5))

# iterate over the generator and print the values
for i in squares_generator:
    print(i)


