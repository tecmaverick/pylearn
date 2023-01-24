import math


def binarysearch(arr, n, k):
    if arr is None:
        return

    if len(arr) != n:
        return -1

    n = n - 1

    # Do a bounds value check. This applies only if the array is sorted
    if k > arr[n] or k < arr[0]:
        return -1

    lbound = 0
    ubound = n
    mbound = math.ceil(n / 2)

    # def search(arr, search_val, lbound, ubound, mbound):
    #     # print("Iterate")
    #     if search_val == arr[mbound]:
    #         return mbound
    #
    #     elif search_val < arr[mbound]:
    #         if search_val == arr[lbound]:
    #             return lbound
    #         elif (mbound - lbound) == 1 and (ubound - mbound) == 1:
    #             return -1
    #         else:
    #             new_lbound = lbound
    #             new_ubound = mbound
    #             new_mbound = new_lbound + math.ceil((new_ubound - new_lbound) / 2)
    #             return search(arr, search_val, lbound=new_lbound, ubound=new_ubound, mbound=new_mbound)
    #     elif search_val > arr[mbound]:
    #         if search_val == arr[ubound]:
    #             return ubound
    #         elif (mbound - lbound) == 1 and (ubound - mbound) == 1:
    #             return -1
    #         else:
    #             new_lbound = mbound
    #             new_ubound = ubound
    #             new_mbound = new_lbound + math.ceil((new_ubound - new_lbound) / 2)
    #             return search(arr, search_val, lbound=new_lbound, ubound=new_ubound, mbound=new_mbound)

    # def search(arr, search_val, lbound, ubound):
    #     # print("Iterate")
    #     mbound = lbound + math.ceil((ubound - lbound) / 2)
    #
    #     if search_val == arr[mbound]:
    #         return mbound
    #     # elif (mbound - lbound) <= 1 and (ubound - mbound) <= 1:
    #     #     return -1
    #     elif search_val < arr[mbound]:
    #         return search(arr, search_val, lbound, mbound - 1)
    #     elif search_val > arr[mbound]:
    #         return search(arr, search_val, mbound+1, ubound)
    #
    search_val = k
    counter = 0
    max_val = math.log(n, 2)
    print("max iteration" + str(max_val))
    while counter <= max_val:
        # print("Iterate")
        mbound = lbound + math.ceil((ubound - lbound) / 2)

        if search_val == arr[mbound]:
            return mbound

        elif search_val < arr[mbound]:
            ubound = mbound - 1
        elif search_val > arr[mbound]:
            lbound = mbound + 1

        counter += 1

    return -1


# arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
arr = [10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# arr = [1, 2, 3, 4, 5, 7]
print(binarysearch(arr, len(arr), 20))
