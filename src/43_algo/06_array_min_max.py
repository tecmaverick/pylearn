def getMinMax(a, n):
    min_val = None
    max_val = None

    for i in range(n):
        if min_val is None or max_val is None:
            min_val = a[i]
            max_val = a[i]

        if a[i] > max_val:
            max_val = a[i]

        if a[i] < min_val:
            min_val = a[i]

    return min_val, max_val


lst = [1,2,3,4,5]
print(getMinMax(lst, len(lst)))