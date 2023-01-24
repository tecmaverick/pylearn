def find_num1(n, lst):
    found = False
    result = []
    lst = sorted(lst, reverse=True)

    while len(lst) > 1:
        # reset
        sum_val = 0
        result = []

        for inner in lst:
            result.append(inner)
            sum_val += inner

            if sum_val == n:
                found = True
                break

            elif sum_val > n:
                result.pop()
                sum_val -= inner

        if found:
            break

        lst.pop(0)

    if found:
        return result
    else:
        return []


# a = [12, 11, 10, 5, 6, 3, 2]
a = [ 2, 4, 6, 8, 10]
# a = [12, 11, 10, 5, 6, 3, 2, 1, 4, 7, 8, 9, 13, 14, 15]

# Find the elements in the array which when added up get the X value
for i in range(1, sum(a)):
    result = find_num1(i, a)
    print("Num:{} Elements:{}".format(i, result))
