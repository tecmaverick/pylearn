import unittest


# Logic : Get one character from the left, and one from the right.
#          If both char doesn't match, then its not Palindrome
#          If it matches, take the next character from left, and from right
#          continue with match till the middle character of the string

# Reasoning behind this approach:
# Best when strings are large and cannot be accommodated in memory, hence char by char comparison

def is_palindrome_complex(val):
    # Validate if its type String, or Integer
    if type(val) == int or type(val) == str:
        val = str(val)
    else:
        return False

    if len(val) < 1:
        return False

    # Need to iterate ONLY half the length
    val_len = int(len(val) / 2)
    char_pos_front = 0
    char_pos_back = -1

    for i in range(val_len):
        # print("Iteration: {}".format(i))

        # Get char from the front
        char_from_front = val[char_pos_front]

        # Get char from the end
        char_from_back = val[char_pos_back]

        # If the chars doesn't match then no need to proceed, and return False
        if char_from_front != char_from_back:
            return False
        else:
            char_pos_front += 1
            char_pos_back -= 1

    return True


class PalindromeTest(unittest.TestCase):
    def test_negative_invalid_inputs(self):
        self.assertEqual(is_palindrome_complex(None), False, msg="None tested False")
        self.assertEqual(is_palindrome_complex(""), False, msg="Empty string tested False")
        self.assertEqual(is_palindrome_complex(True), False, msg="Boolean tested False")
        self.assertEqual(is_palindrome_complex(1.22), False, msg="Double tested False")
        self.assertEqual(is_palindrome_complex(0x12), False, msg="Hex tested False")
        self.assertEqual(is_palindrome_complex(bin(10)), False, msg="Binary tested False")


    def test_negative_valid_input(self):
        self.assertEqual(is_palindrome_complex("Help"), False, msg="Help tested False")
        self.assertEqual(is_palindrome_complex("Help "), False, msg="Help (with space to right) tested False")


    def test_postive_valid_inputs(self):
        self.assertEqual(is_palindrome_complex("A"), True, msg="Single char tested success")
        self.assertEqual(is_palindrome_complex("CIVIC"), True, msg="Multi-char:CIVIC (Odd char count) tested success")
        self.assertEqual(is_palindrome_complex("AATAA"), True, msg="Multi-char:ATTA (Even char count) tested success")
        self.assertEqual(is_palindrome_complex("ßAAß"), True, msg="Multi-char:ßAAß (Unicode) tested success")


unittest.main()
