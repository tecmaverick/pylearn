def subArraySum(arr, n, s):
    if len(arr) == 0:
        return [-1]

    if len(arr) != n:
        raise Exception("Invalid length")

    if s < 0:
        raise Exception("Invalid sum")

    if len(arr) == 1 and arr[0] == s:
        return 1, 1
    elif len(arr) == 1 and arr[0] != s:
        return -1

    curr_idx = 0
    start_idx = 0
    sum_val = arr[curr_idx]

    while curr_idx < n:
        if sum_val < s:
            curr_idx += 1
            if curr_idx >= n: break
            sum_val += arr[curr_idx]
        elif sum_val > s:
            sum_val -= arr[start_idx]
            start_idx += 1
        elif sum_val == s:
            if start_idx <= curr_idx:
                return start_idx + 1, curr_idx + 1
            else:
                return [-1]


    return [-1]


# arr = [10, 20, 30, 33, 22, 11, 10001]
# Get start and end index of the sum parameter. Here 5 means, element 2 and 5. Hence the index (1 based) is 2,3
arr = [1, 2, 3, 7, 5]

print(subArraySum(arr, len(arr), 5))
