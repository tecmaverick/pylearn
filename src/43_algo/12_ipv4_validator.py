import re

# def init_validate(num):
#     if num.isnumeric():
#         num_conv = int(num)
#         return (num_conv >= 0 or num_conv <= 255) and num == str(num_conv)
#
#     return False
#
#
# def isValid(s):
#     ip_str_len = len(s)
#     if s is None or \
#             ip_str_len < 7 or \
#             ip_str_len > 15 or \
#             not "." in s or \
#             s.count(".") != 3:
#         return int(False)
#
#     spit_vals = [int(num) for num in s.split(".") if init_validate(num)]
#     if len(spit_vals) != 4: return int(False)
#
#     for idx in range(len(spit_vals)):
#         if spit_vals[idx] < 0 or spit_vals[idx] > 255:
#             return int(False)
#
#     return int(True)


def isValid(s):
    # code here
    # regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    regex = r"\d[0-255]\.\d[0-255]\.\d[0-255]\.\d[0-255]"

    if re.search(regex, s):
        return 1
    else:
        return 0



print(isValid("127.0.0.1"))
