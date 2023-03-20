def parse_list(lst):
    dict = {}
    positive_sign = lambda x: x >= 0
    start_index = 0

    for i in range(1, len(lst)):
        if positive_sign(lst[i - 1]) != positive_sign(lst[i]) or i == len(lst) - 1:
            if i == len(lst) - 1: i+=1
            dict[len(dict)] = lst[start_index:i]
            start_index = i

    return dict

def get_max_sum(hashmap):
    result = {}
    for k,v in hashmap.items():
        result[sum(v)] = v

    return result[max(result.keys())]

# Get the range of contiguous elements whose sum must be the highest
a = [1, 2, -1, 3, 9, 12, -2, -4, -1, 9, 7, 8, 1, 2, 4]
# a = [-1, -2, -1, -3, -9, -12, -2, -4, -1]

b = parse_list(a)
max_sum = get_max_sum(b)
print(max_sum)
# for k, v in b.items():
#     print(k, v)
