# BigO - algorithm still has an O(n2) runtime complexity on the average case The worst case happens when the supplied
# array is sorted in reverse order. The best case happens when the supplied array is already sorted. Here,
# the inner loop is never executed, resulting in an O(n) runtime complexity

# In practice, insertion sort is considerably more efficient than bubble sort. If you look at the implementation of
# both algorithms, then you can see how insertion sort has to make fewer comparisons to sort the list

# Some Quicksort implementations even use insertion sort internally if the list is small enough to provide a faster
# overall implementation. insertion sort is not practical for large arrays



def insertion_sort(arr, arr_len):
    curr_index = 1

    while curr_index < arr_len:
        curr_val = arr[curr_index]
        prev_index = curr_index - 1

        while prev_index >= 0 and arr[prev_index] > curr_val:
            print(arr)
            arr[prev_index + 1] = arr[prev_index]
            prev_index -= 1


        arr[prev_index + 1] = curr_val
        curr_index += 1
        print(arr)
        print("-" * 10)

    return arr


# data = [10, 8, 11, 6, 15, 4, 20, 2]
data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(data)
print("~" * 10)

print(insertion_sort(data, len(data)))
