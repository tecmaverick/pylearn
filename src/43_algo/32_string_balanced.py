def ispar(x):
    if x is None:
        return

    open_char = {"[": "]", "{": "}", "(": ")"}
    close_char = {"]": "[", "}": "{", ")": "("}
    chars_list = []

    for char in x:
        if char in open_char:
            chars_list.append(char)

        elif char in close_char:
            if len(chars_list) < 1:
                return False

            if close_char[char] != chars_list.pop():
                return False
        else:
            return False

    return len(chars_list) == 0


data = [None, "", "[", "]", ")(", "][", "}{", "{([)}", "{([])}"]
for itm in data:
    # itm = "]"
    print("{} - {}".format(itm, ispar(itm)))
