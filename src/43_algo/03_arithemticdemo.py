import operator

data1 = [1, 2, 3]
data2 = [3, 2, 1]

result1 = map(operator.add, data1, data2)
result2 = map(operator.mul, data1, data2)
result3 = map(operator.truediv, data1, data2)
result4 = map(operator.sub, data1, data2)
result5 = map(operator.mod, data1, data2)

print("{} + {} = {}".format(data1, data2, list(result1)))
print("{} * {} = {}".format(data1, data2, list(result2)))
print("{} / {} = {}".format(data1, data2, list(result3)))
print("{} - {} = {}".format(data1, data2, list(result4)))
print("{} % {} = {}".format(data1, data2, list(result5)))
