# Input: arr = [1,2,3,4,5]
# OUtput: arr = [5,1,2,3,4]

arr = [1,2,3,4,5]
n = len(arr)

# arr.pop() - removes and returns the last element from the array , which is 5

arr.insert(0, arr.pop())