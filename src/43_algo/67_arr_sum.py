
def find_num1(n, lst):
    sum_val = 0
    found = False
    result = []
    lst = sorted(lst, reverse=True)

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
        return result
    else:
        return []


# a = [12, 11, 10, 5, 6, 3, 2, 1]
a = [3, 4, 6, 1, 2, 9, 7, 5, 8]
# a = [12, 11, 10, 5, 6, 3, 2, 1, 4, 7, 8, 9, 13, 14, 15]

for i in range(1, 50):
    result = find_num1(i, a)
    print("Num:{} Elements:{}".format(i, result))
