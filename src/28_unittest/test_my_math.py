import unittest
import sys
from unittest.mock import patch
import builtins
from io import StringIO

from my_math import MyMath


class Calc(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    # executed before every test
    def setUp(self):
        print("setup phase")
        self.mymath = MyMath()

    # executed after every test
    def tearDown(self):
        print("teardown")

    # ************************************
    # positive\happy path tests BEGIN
    def test_postitive_add(self):
        self.assertEqual(self.mymath.add(100, 100), 200)

    def test_postitive_add_zero(self):
        self.assertEqual(self.mymath.add(0, 0), 0)

    def test_postitive_substract(self):
        self.assertEqual(self.mymath.substract(100, 10), 90)

    def test_postitive_multiply(self):
        self.assertEqual(self.mymath.multiply(10, 10), 100)

    def test_postitive_divide(self):
        self.assertEqual(self.mymath.divide(10, 2), 5)

    def test_simulate_user_input(self):
        with patch('builtins.input', return_value="150 + 120"), patch('sys.stdout', new=StringIO()) as fake_out:
            self.mymath.demo()
            self.assertEqual(fake_out.getvalue().strip(), "result is 270")

    # positive\happy path tests END
    # ************************************

    # ************************************
    # Negative tests BEGIN
    def test_negative_add_none(self):
        with self.assertRaises(TypeError):
            self.mymath.add(None, None)

    def test_negative_add_string_with_int(self):
        with self.assertRaises(TypeError):
            self.mymath.add("abc", 10)

    def test_negative_add_string_with_string(self):
        self.assertEqual(self.mymath.add("abc", "10"), "abc10")

    def test_negative_add_int_overflow(self):
        # sys.maxsize is int64 9223372036854775807
        # Python integer upper bound is limited by the system memory, however float does have a limit
        # When using with libs like numpy, pandas always limit range to int64
        self.assertEqual(self.mymath.add(sys.maxsize, 10), sys.maxsize+10)

    # Negative tests END
    # ************************************


# if __name__ == "__main__":
#     unittest.main()
