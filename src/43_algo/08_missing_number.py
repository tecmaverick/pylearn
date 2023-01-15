# int MissingNumber(int array[], int n) {
#
#
#                  int sum=0; //we create lst variable sum & initialise it with 0
#
#         int r=n*(n+1)/2; // we apply this formula to get sum of all natural no.
#
#         for(int i=0; i<n-1; i++){
#
#             sum+=array[i]; //we add all the given no.
#
#         }
#
#         return r-sum; //we subtract exact sum - sum
#
#     }


def MissingNumber(array, n):
    # code here
    array.sort()
    arr_len = len(array)

    for arr_index in range(0, n):
        actual_val = arr_index + 1

        if arr_index < arr_len:
            if actual_val != array[arr_index]:
                return actual_val
        else:
            return actual_val

    return None


# lst = [1]
# lst_len = 2

# lst = [1,2,3,5,6]
# lst_len = 6

lst = [1,2,3,4,5]
lst_len = 6

print(MissingNumber(lst,lst_len))
