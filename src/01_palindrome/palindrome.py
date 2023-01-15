import unittest

# Logic : Get one character from the left, and one from the right.
#          If both char doesn't match, then its not Palindrome
#          If it matches, take the next character from left, and from right
#          continue with match till the middle character of the string

#Reasoning behind this approach:
# Best when strings are large and cannot be accommodated in memory, hence char by char comparison

def is_palindrome(val):
    # Validate if its type string, else cast to string
    if type(val) != str:
        val = str(val)

    # If value is one character or less then no need to do the calc
    if len(val) <= 1:
        return True

    result = ""

    # Need to iterate ONLY half the length
    val_len = int(len(val) / 2)
    char_pos_front = 0
    char_pos_back = -1

    for i in range(val_len):
        print("Iteration: {}".format(i))

        # Get char from the front
        char_from_front = val[char_pos_front]

        # Get char from the end
        char_from_back = char_pos_back
        if char_from_front != char_from_back:
            return False

    return True


class PalindromeTest(unittest.TestCase):
print(is_palindrome(True))
