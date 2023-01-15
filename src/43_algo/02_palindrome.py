import unittest


def is_palindrome_simple(val):
    # Validate if its type String, or Integer
    if type(val) == int or type(val) == str:
        val = str(val)
    else:
        return False

    if len(val) < 1:
        return False

    val_reversed = val[::-1]
    return val_reversed == val


class PalindromeTest(unittest.TestCase):
    def test_negative_invalid_inputs(self):
        self.assertEqual(is_palindrome_simple(None), False, msg="None tested False")
        self.assertEqual(is_palindrome_simple(""), False, msg="Empty string tested False")
        self.assertEqual(is_palindrome_simple(True), False, msg="Boolean tested False")
        self.assertEqual(is_palindrome_simple(1.22), False, msg="Double tested False")
        self.assertEqual(is_palindrome_simple(0x12), False, msg="Hex tested False")
        self.assertEqual(is_palindrome_simple(bin(10)), False, msg="Binary tested False")
        self.assertEqual(is_palindrome_simple(bin(10)), False, msg="Binary tested False")

    def test_negative_valid_input(self):
        self.assertEqual(is_palindrome_simple("Help"), False, msg="Help tested False")
        self.assertEqual(is_palindrome_simple("Help "), False, msg="Help (with space to right) tested False")

    def test_postive_valid_inputs(self):
        self.assertEqual(is_palindrome_simple("A"), True, msg="Single char tested success")
        self.assertEqual(is_palindrome_simple("CIVIC"), True, msg="Multi-char:CIVIC (Odd char count) tested success")
        self.assertEqual(is_palindrome_simple("AATAA"), True, msg="Multi-char:ATTA (Even char count) tested success")
        self.assertEqual(is_palindrome_simple("ßAAß"), True, msg="Multi-char:ßAAß (Unicode) tested success")


unittest.main()
