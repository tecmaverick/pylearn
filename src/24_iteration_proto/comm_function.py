#tuple unpacking does a join between two lists
ids = [1,2,3,4,5,6,7,8,9,10]
amt = [122,244,367,432,5867,635,7345]

for a in zip(ids,amt):
	print a
 
poll = [True, False, True, True, False]

#if any of the element is true, built-in function 'any' will ouput True, else False
print any(poll)

#sum built-in function to print sum of all values in the list
nums = [1,2,3,4,5]
print sum(nums)


#list comprehension
for i in [x*x for x in range(10)]:
	print i


