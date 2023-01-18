# MergeSort - applies the divide-and-conquer principle to divide the input array into two lists

# The implementation of the merge sort algorithm needs two different pieces:
#   A function that recursively splits the input in half
#   A function that merges both halves, producing a sorted array

# Pros
# Can be parrallelized
# Scales with increasing array size

# Cons
# the time cost of the recursion allows algorithms such as bubble sort and insertion sort to be faster.
# creates copies of the array when calling itself recursively. This takes up more memory
