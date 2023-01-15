def reverse_str(str_val):
    result = []
    str_length = len(str_val)
    for i in range(0, str_length):
        result.append(str_val[(str_length-1) - i])

    return ''.join(result)


print(reverse_str("abcd"))