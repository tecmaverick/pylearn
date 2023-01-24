def ispalin(S):
    val = S == S[::-1]
    return val


def longestPalin0(S):
    if S is None or len(S) == 1:
        return S

    reverse_counter = -1
    palindrome_list = []

    for counter in range(0, len(S)):
        for end_pos in range(len(S) - 1, counter, -1):
            # if first and last chars match, then take all the chars inbeween and check for palindrome
            till_car_pos = end_pos + 1
            if S[counter] == S[end_pos] and \
                    S[counter:till_car_pos] not in palindrome_list and \
                    ispalin(S[counter:till_car_pos]):
                palindrome_list.append(S[counter:till_car_pos])

    # print(palindrome_list)
    if len(palindrome_list) >= 1:
        palindrome_list.sort(key=lambda x: len(x), reverse=True)
        print(palindrome_list)
        return palindrome_list[0]
    else:
        return [x for x in S][0]


# ****************************************************************************************************

def expand(str, left, right, palindrome_set):
    if str is None:
        return

    while left >= 0 and right < len(str) and str[left] == str[right]:
        palindrome_set.add(str[left:right + 1])
        left -= 1
        right += 1


def longestPalin1(S):
    if S is None:
        return S

    palindrome_set = set()
    for idx in range(len(S)):
        expand(S, idx, idx, palindrome_set)
        expand(S, idx, idx + 1, palindrome_set)

    return sorted(palindrome_set, key=lambda x: len(x), reverse=True)[0]
    # return palindrome_set


# ****************************************************************************************************
def expand(str, left, right):
    if str is None:
        return

    while left >= 0 and right < len(str) and str[left] == str[right]:
        left -= 1
        right += 1
    return str[left:right + 1]


def get_max_str(new_str, max_str, max_str_len):
    if len(new_str) > max_str_len:
        return new_str, len(new_str)
    else:
        return max_str, max_str_len


def longestPalin2(S):
    if S is None:
        return S

    max_str = ""
    max_str_len = 0

    for idx in range(len(S)):
        result = expand(S, idx, idx)
        max_str, max_str_len = get_max_str(result, max_str, max_str_len)

        result = expand(S, idx, idx + 1)
        max_str, max_str_len = get_max_str(result, max_str, max_str_len)

    return max_str
    # return palindrome_set


# ****************************************************************************************************

def get_max_str(new_str, max_str, max_str_len):
    if len(new_str) > max_str_len:
        return new_str, len(new_str)
    else:
        return max_str, max_str_len


# def longestPalin3(S):
#     if len(S) == 1:
#         return S
#     for i in range(len(S), 0, -1):
#         for j in range(len(S) - i + 1):
#             res = S[j:i + j]
#             if res == res[::-1]:
#                 return res

def longestPalin4(S):
    if S is None or len(S) == 1:
        return S

    for r in range(len(S), 0, -1):
        for f in range(len(S) - r + 1):
            res = S[f:r + f]
            print(f"r:{r} f:{f} res:{res}")
            if res == res[::-1]:
                return res


# print(longestPalin1("google"))
# print(longestPalin0("aopobmalayalamgwwwwowwwwayyppooppyyws"))
# print(longestPalin1("aopobmalayalamgwwwwowwwwayyppooppyyws"))
# print(longestPalin("rfkqyuqfjkxy"))
print(longestPalin4("aopobmalayalamgwwwwowwwwayyppooppyyws"))
