# Naming - The bubble sort means the largest value gets bubbled to the top of the array

# Pros
# The main advantage of the bubble sort algorithm is its simplicity. It is straightforward to both implement and understand.

# Cons
# bubble sort is that it is slow, with a runtime complexity of O(n2)

import time

# Big O Time complexity - O(N2)
def bubble_sort( arr, n):
    curr_index = 1
    prev_index = 0
    unsorted_length = n

    while curr_index < unsorted_length:
        myarr = arr.copy()
        myarr[prev_index] = "<" + str(myarr[prev_index])
        myarr[curr_index] = str(myarr[curr_index]) + ">"
        print(myarr)

        if arr[prev_index] > arr[curr_index]:
            arr[prev_index], arr[curr_index] = arr[curr_index], arr[prev_index]

        # If the curr_index is one index less to the the length of array, then
        # 1. decrement the n by 1, as last element is sorted
        # 2. Reset the curr_index to 1, and prev_index to 0
        if curr_index + 1 == unsorted_length:
            unsorted_length -= 1
            curr_index = 1
            prev_index = 0
        else:
            #  If the curr_index lesser than length of array, then increment both
            # curr_index and prev_index by one
            curr_index += 1
            prev_index += 1

        # Exit the loop if the last index had moved all the way to the start
        if n-1 == 0:
            break

    return arr


data = [10, 8, 11, 6, 15, 4, 20, 2]
data.sort(reverse=True)
print(data)

print(bubble_sort(data,len(data)))